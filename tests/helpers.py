"""Shared helpers: build throwaway vaults in a temp folder."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))


def frontmatter(type_="knowledge", status="active", created="2026-01-10", updated="2026-01-10",
                extra="", drop=()):
    fields = {
        "title": "Test page", "type": type_, "status": status, "created": created,
        "updated": updated, "tags": "[test]", "sources": "[]", "confidence": "medium",
    }
    lines = [f"{k}: {v}" for k, v in fields.items() if k not in drop]
    return "---\n" + "\n".join(lines) + ("\n" + extra if extra else "") + "\n---\n"


class TempVault:
    def __init__(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name).resolve()

    def write(self, rel: str, text: str) -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def cleanup(self):
        self._tmp.cleanup()
