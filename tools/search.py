#!/usr/bin/env python3
"""search.py: semantic search over the company brain (cosine scan of the page index).

Usage:
    .venv/bin/python tools/search.py "why do onboarding projects stall?"
    .venv/bin/python tools/search.py -k 10 --json "pricing decision"

Prints the top-k most similar pages with score and a snippet. Meant as the
retrieval step of the query loop: the agent then reads the full pages and
their links, not just the snippets. Combine with grep for exact terms.

Refuses to search a stale index (a page changed, was added or removed since
the last build) unless --allow-stale is given, so answers are not silently
based on outdated pages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import embed  # noqa: E402
from lint import ROOT  # noqa: E402


def load_index(root: Path):
    data = np.load(embed.index_path(root), allow_pickle=False)
    return {key: data[key] for key in data.files}


def stale_pages(root: Path, index) -> list[str]:
    """Pages whose content differs from the index, plus pages added or removed."""
    indexed = {str(p): str(h) for p, h in zip(index["paths"], index["hashes"])}
    current = {rel: hashlib.sha256(content).hexdigest() for rel, content in embed.indexed_notes(root)}
    return sorted(p for p in indexed.keys() | current.keys() if indexed.get(p) != current.get(p))


def rank(index, query_vector, k: int = 5):
    q = np.asarray(query_vector, dtype=np.float32)
    q = q / (np.linalg.norm(q) + 1e-12)
    scores = index["vectors"] @ q  # rows are normalized, so this is cosine similarity
    order = np.argsort(-scores)[:k]
    return [(float(scores[i]), str(index["paths"][i])) for i in order]


def snippet(root: Path, rel: str, n: int = 180) -> str:
    try:
        text = (Path(root) / rel).read_text(encoding="utf-8")
    except OSError:
        return ""
    if text.startswith("---"):
        text = text.split("---", 2)[-1]
    return " ".join(text.split())[:n]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Semantic search over the company brain.")
    parser.add_argument("query", nargs="+")
    parser.add_argument("-k", type=int, default=5, help="number of results (default 5)")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--allow-stale", action="store_true", help="search even if the index is outdated")
    args = parser.parse_args(argv)
    if args.k < 1:
        parser.error("-k must be at least 1")
    if not embed.index_path(args.root).exists():
        print("No index yet. Run: .venv/bin/python tools/embed.py", file=sys.stderr)
        return 1
    index = load_index(args.root)
    if str(index["model"]) != embed.MODEL:
        print(f"Index was built with {index['model']}, search uses {embed.MODEL}. Rebuild the index.",
              file=sys.stderr)
        return 1
    stale = stale_pages(args.root, index)
    if stale and not args.allow_stale:
        print(f"Index is outdated ({len(stale)} pages changed). Run tools/embed.py "
              "or pass --allow-stale.", file=sys.stderr)
        return 1
    results = rank(index, embed.ollama_embed(" ".join(args.query)), args.k)
    if args.json:
        print(json.dumps([{"score": round(s, 4), "path": p, "snippet": snippet(args.root, p)}
                          for s, p in results], indent=2))
    else:
        for i, (score, path) in enumerate(results, 1):
            print(f"{i:>2}. {score:.3f}  {path}\n      {snippet(args.root, path)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
