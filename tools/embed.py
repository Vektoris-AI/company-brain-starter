#!/usr/bin/env python3
"""embed.py: build a page-level semantic index of the company brain.

One embedding per PAGE (not per chunk), computed locally with Ollama, saved to
_index/embeddings.npz. A linear cosine scan (search.py) is fast enough for a
few thousand pages, so there is no vector database to run.

What gets indexed: notes in the vault folders (see lint.NOTE_DIRS), except
90_archive/, templates and _raw/. Raw sources are reached through the pages
that cite them.

Setup:
    ollama pull bge-m3                   # multilingual embedding model
    python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
Run:
    .venv/bin/python tools/embed.py
Config (environment): OLLAMA_HOST (default http://localhost:11434),
EMBED_MODEL (default bge-m3).

Nothing leaves your machine: the only network call goes to OLLAMA_HOST.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint import NOTE_DIRS, ROOT, iter_notes  # noqa: E402

INDEX_DIRS = tuple(d for d in NOTE_DIRS if d != "90_archive")
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
MODEL = os.environ.get("EMBED_MODEL", "bge-m3")
MAX_CHARS = 6000  # bge-m3 handles about 8k tokens; Ollama truncates the rest


def index_path(root: Path) -> Path:
    return Path(root) / "_index" / "embeddings.npz"


def indexed_notes(root: Path):
    """(relative path, bytes) for every non-empty page that belongs in the index."""
    root = Path(root)
    for path in iter_notes(root, INDEX_DIRS):
        content = path.read_bytes()
        if content.strip():
            yield path.relative_to(root).as_posix(), content


def ollama_embed(text: str) -> list[float]:
    """Embed one page with the local Ollama server."""
    body = json.dumps({"model": MODEL, "input": text[:MAX_CHARS], "truncate": True}).encode()
    request = urllib.request.Request(f"{OLLAMA}/api/embed", data=body,
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.load(response)["embeddings"][0]


def build_index(root: Path = ROOT, out: Path | None = None, embed_fn=None, quiet=False) -> Path:
    """Write a complete, consistent index or nothing.

    The old index stays in place if anything fails, and the run is rejected if
    a page changed while it was being embedded.
    """
    root = Path(root)
    out = Path(out) if out else index_path(root)
    embed_fn = embed_fn or ollama_embed
    snapshot = list(indexed_notes(root))
    if not snapshot:
        raise ValueError("no pages found; the existing index is left unchanged")
    paths, vectors, hashes = [], [], []
    for i, (rel, content) in enumerate(snapshot, 1):
        vector = np.asarray(embed_fn(content.decode("utf-8", errors="replace")), dtype=np.float32)
        if vector.ndim != 1 or not vector.size or not np.isfinite(vector).all() or not np.linalg.norm(vector) > 0:
            raise ValueError(f"invalid embedding for {rel}")
        paths.append(rel)
        vectors.append(vector)
        hashes.append(hashlib.sha256(content).hexdigest())
        if not quiet:
            print(f"  [{i}/{len(snapshot)}] {rel}", flush=True)
    if list(indexed_notes(root)) != snapshot:
        raise RuntimeError("pages changed while indexing; run again")
    matrix = np.stack(vectors)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".embeddings-", suffix=".npz", dir=out.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            np.savez(handle, paths=np.array(paths), vectors=matrix,
                     hashes=np.array(hashes), model=np.array(MODEL))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, out)  # atomic: readers see the old or the new index, never half
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    if not quiet:
        print(f"Index written: {out.relative_to(root) if out.is_relative_to(root) else out} "
              f"({len(paths)} pages, dim={matrix.shape[1]})")
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the semantic index of the company brain.")
    parser.add_argument("--root", type=Path, default=ROOT, help="vault root (default: parent of tools/)")
    args = parser.parse_args(argv)
    out = index_path(args.root)
    out.parent.mkdir(parents=True, exist_ok=True)
    with (out.parent / "embed.lock").open("a") as lock:
        try:  # serialize runs queued by the post-commit hook (Unix only)
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_EX)
        except ImportError:
            pass
        try:
            build_index(args.root, out)
            return 0
        except Exception as error:  # noqa: BLE001
            print(f"Index build failed, previous index kept: {error}", file=sys.stderr)
            return 1


if __name__ == "__main__":
    sys.exit(main())
