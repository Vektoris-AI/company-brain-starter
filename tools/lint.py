#!/usr/bin/env python3
"""lint.py: structural health check for the company brain. Standard library only.

Checks every note in the vault folders (not _raw/, not templates):

  errors    frontmatter missing or not closed
            required field missing, duplicated, or with an invalid value
            invalid date, or `updated` earlier than `created`
            dead [[wikilink]] or dead relative [markdown](link)
            uncommitted edits to existing files in _raw/ (needs git)
  warnings  orphan: a knowledge or person page that nothing links to
            `contradicts:` set but the page is not tagged needs-review

Usage:
    python3 tools/lint.py                          # whole vault
    python3 tools/lint.py --files 30_knowledge/x.md 50_people/Y.md
    python3 tools/lint.py --json                   # machine-readable
    python3 tools/lint.py --strict                 # warnings fail too

Exit code: 0 = no errors, 1 = errors (or any issue with --strict).
"""
from __future__ import annotations

import argparse
import collections
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent

NOTE_DIRS = ("00_inbox", "10_projects", "20_areas", "30_knowledge",
             "40_resources", "50_people", "90_archive", "_meta")
RAW_DIR = "_raw"
SKIP_DIRS = {"templates", "_index", "_workspace", "_local", "node_modules", "__pycache__"}
SKIP_FILES = {"CLAUDE.md", "AGENTS.md", "SKILL.md", "README.md"}

REQUIRED = ("title", "type", "status", "created", "updated", "tags", "sources", "confidence")
ALLOWED = {
    "type": {"inbox", "project", "area", "knowledge", "person", "sop", "template", "adr", "log"},
    "status": {"active", "draft", "archived"},
    "confidence": {"high", "medium", "low"},
}
ORPHAN_TYPES = {"knowledge", "person"}
NOTE_EXTENSIONS = (".md",)
LINK_EXTENSIONS = (".md", ".pdf", ".png", ".jpg", ".jpeg", ".txt", ".csv", ".json", ".html")

FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
FIELD = re.compile(r"^([A-Za-z_][\w-]*):[ \t]*(.*?)[ \t]*$", re.M)
FENCED = re.compile(r"^(```|~~~)[^\n]*\n.*?^\1[^\n]*$", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
WIKILINK = re.compile(r"!?\[\[([^\]\n]+)\]\]")
MDLINK = re.compile(r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")


# ---------------------------------------------------------------- file walking

def iter_files(root: Path, tops, skip_dirs=SKIP_DIRS):
    """All regular files under the given top-level folders.

    Hidden folders, skip_dirs and symlinks are never followed, so a linked code
    checkout or a secrets folder cannot leak into the check or the index.
    """
    for top in tops:
        base = root / top
        if not base.is_dir():
            continue
        for directory, dirs, names in os.walk(base, followlinks=False):
            here = Path(directory)
            dirs[:] = sorted(d for d in dirs
                             if not d.startswith(".") and d not in skip_dirs
                             and not (here / d).is_symlink())
            for name in sorted(names):
                path = here / name
                if not name.startswith(".") and not path.is_symlink():
                    yield path


def iter_notes(root: Path, tops=NOTE_DIRS):
    for path in iter_files(root, tops):
        if path.suffix in NOTE_EXTENSIONS and path.name not in SKIP_FILES:
            yield path


# --------------------------------------------------------------------- parsing

def parse_frontmatter(text: str):
    """(fields, entries) or (None, []) if there is no frontmatter block."""
    match = FRONTMATTER.match(text)
    if not match:
        return None, []
    entries = FIELD.findall(match.group(1))
    return dict(entries), entries


def scalar(value: str) -> str:
    return value.strip().strip("\"'")


def visible_text(text: str) -> str:
    """Text without code blocks and inline code: [[examples]] there are not links."""
    return INLINE_CODE.sub("", FENCED.sub("", text))


def wikilink_target(raw: str) -> str:
    target = raw.split("|", 1)[0]
    target = target.split("#", 1)[0].split("^", 1)[0]
    return unquote(target).strip()


# ------------------------------------------------------------------ link index

class LinkIndex:
    """Resolves links the way Obsidian does: by path, or by unique file name."""

    def __init__(self, root: Path):
        self.root = root
        self.by_path = {}
        self.by_name = collections.defaultdict(list)
        for path in iter_files(root, NOTE_DIRS + (RAW_DIR,), skip_dirs=SKIP_DIRS - {"templates"}):
            rel = path.relative_to(root).as_posix().lower()
            self.by_path[rel] = path
            self.by_name[path.name.lower()].append(path)
            self.by_name[path.stem.lower()].append(path)

    def resolve_wikilink(self, target: str, origin: Path):
        if not target:
            return origin  # [[#heading]] points at the page itself
        key = target.lower().lstrip("/")
        for candidate in (key, key + ".md"):
            if candidate in self.by_path:
                return self.by_path[candidate]
        if "/" not in key:
            hits = self.by_name.get(key)
            return hits[0] if hits else None
        for rel, path in self.by_path.items():  # partial path, e.g. [[sales/pipeline]]
            if rel.endswith("/" + key) or rel.endswith("/" + key + ".md"):
                return path
        return None

    def resolve_mdlink(self, target: str, origin: Path):
        target = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
        if not target:
            return origin
        path = (origin.parent / target).resolve()
        return path if path.exists() else None


# ----------------------------------------------------------------------- audit

def git_raw_changes(root: Path):
    """Existing _raw/ files with uncommitted edits, deletions or renames."""
    try:
        inside = subprocess.run(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
                                capture_output=True, text=True, timeout=10)
        if inside.returncode != 0 or inside.stdout.strip() != "true":
            return []
        status = subprocess.run(["git", "-C", str(root), "status", "--porcelain=v1", "-z",
                                 "--untracked-files=no", "--", RAW_DIR],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return []
    changed = []
    records = status.stdout.split("\0")
    i = 0
    while i < len(records):
        record = records[i]
        i += 1
        if len(record) < 4:
            continue
        code, path = record[:2], record[3:]
        if "R" in code or "C" in code:
            i += 1  # the next record is the original path
        if code.strip() and code.strip() != "A":
            changed.append((code.strip(), path))
    return changed


def audit(root: Path = ROOT, selected=None, use_git: bool = True) -> dict:
    root = Path(root).resolve()
    links = LinkIndex(root)
    all_notes = list(iter_notes(root))
    notes = [(root / s).resolve() for s in selected] if selected else all_notes
    issues = []

    def issue(path, severity, kind, detail):
        try:
            rel = path.relative_to(root).as_posix()
        except ValueError:
            rel = str(path)
        issues.append({"file": rel, "severity": severity, "kind": kind, "detail": detail})

    inbound = collections.defaultdict(set)
    meta = {}
    for path in all_notes:
        text = path.read_text(encoding="utf-8", errors="replace")
        body = visible_text(text)
        targets = []
        for raw in WIKILINK.findall(body):
            targets.append(("wikilink", raw, links.resolve_wikilink(wikilink_target(raw), path)))
        for raw in MDLINK.findall(body):
            raw = raw.strip("<>")
            if urlsplit(raw).scheme or raw.startswith("#") or raw.startswith("mailto:"):
                continue
            targets.append(("markdown_link", raw, links.resolve_mdlink(raw, path)))
        for _, _, resolved in targets:
            if resolved is not None and resolved.resolve() != path.resolve():
                inbound[resolved.resolve()].add(path)
        meta[path.resolve()] = (text, targets)

    for path in notes:
        if not path.is_file():
            issue(path, "error", "missing_file", "file does not exist")
            continue
        text, targets = meta.get(path.resolve()) or (path.read_text(encoding="utf-8"), [])
        fields, entries = parse_frontmatter(text)
        if fields is None:
            issue(path, "error", "frontmatter", "frontmatter missing")
        else:
            missing = [k for k in REQUIRED if k not in fields]
            if missing:
                issue(path, "error", "frontmatter", "missing fields: " + ", ".join(missing))
            for key, count in collections.Counter(k for k, _ in entries).items():
                if count > 1:
                    issue(path, "error", "frontmatter", "duplicate field: " + key)
            for key, allowed in ALLOWED.items():
                if key in fields and scalar(fields[key]) not in allowed:
                    issue(path, "error", "frontmatter",
                          f"invalid {key}: '{scalar(fields[key])}' (allowed: {', '.join(sorted(allowed))})")
            dates = {}
            for key in ("created", "updated"):
                if key in fields:
                    try:
                        dates[key] = datetime.date.fromisoformat(scalar(fields[key]))
                    except ValueError:
                        issue(path, "error", "frontmatter", f"invalid date in {key}: '{scalar(fields[key])}'")
            if len(dates) == 2 and dates["updated"] < dates["created"]:
                issue(path, "error", "frontmatter", "updated is earlier than created")
            if "contradicts" in fields and "needs-review" not in text:
                issue(path, "warning", "contradiction", "contradicts: is set but the page is not tagged needs-review")
            note_type = scalar(fields.get("type", ""))
            status = scalar(fields.get("status", ""))
            if note_type in ORPHAN_TYPES and status != "archived" and not inbound.get(path.resolve()):
                issue(path, "warning", "orphan", "no other page links here")
        for kind, raw, resolved in targets:
            if resolved is None:
                issue(path, "error", kind, raw)

    if use_git:
        for code, rel in git_raw_changes(root):
            issues.append({"file": rel, "severity": "error", "kind": "raw_modified",
                           "detail": f"_raw/ is immutable, but this file has uncommitted changes ({code})"})

    counts = collections.Counter(i["severity"] for i in issues)
    return {"checked_notes": len(notes), "errors": counts.get("error", 0),
            "warnings": counts.get("warning", 0), "issues": issues}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Structural health check for the company brain.")
    parser.add_argument("--root", type=Path, default=ROOT, help="vault root (default: parent of tools/)")
    parser.add_argument("--files", nargs="+", help="check only these vault-relative notes")
    parser.add_argument("--json", action="store_true", help="print JSON")
    parser.add_argument("--strict", action="store_true", help="fail on warnings too")
    parser.add_argument("--no-git", action="store_true", help="skip the _raw/ immutability check")
    args = parser.parse_args(argv)
    result = audit(args.root, selected=args.files, use_git=not args.no_git)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for item in result["issues"]:
            print(f"{item['severity']:<7} {item['kind']:<14} {item['file']}: {item['detail']}")
        print(f"{result['checked_notes']} notes checked: "
              f"{result['errors']} errors, {result['warnings']} warnings")
    failed = result["errors"] or (args.strict and result["warnings"])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
