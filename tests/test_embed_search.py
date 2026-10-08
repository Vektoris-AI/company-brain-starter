"""Tests for tools/embed.py and tools/search.py with a fake embedding function.

No Ollama needed. Skipped automatically when numpy is not installed
(use the .venv from the README: .venv/bin/python -m unittest discover -s tests).
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import unittest

from helpers import TempVault, frontmatter

HAS_NUMPY = importlib.util.find_spec("numpy") is not None
if HAS_NUMPY:
    import numpy as np

    import embed
    import search


def fake_embed(text: str, dims: int = 64):
    """Deterministic bag-of-words vector: pages sharing words end up close."""
    vector = [0.0] * dims
    for word in re.findall(r"[a-z]{3,}", text.lower()):
        vector[int(hashlib.md5(word.encode()).hexdigest(), 16) % dims] += 1.0
    vector[0] += 0.01  # never all zeros
    return vector


@unittest.skipUnless(HAS_NUMPY, "numpy not installed")
class EmbedAndSearch(unittest.TestCase):
    def setUp(self):
        self.vault = TempVault()
        self.root = self.vault.root
        self.vault.write("30_knowledge/onboarding.md", frontmatter() + "customer onboarding checklist stalls handover")
        self.vault.write("30_knowledge/pricing.md", frontmatter() + "pricing tiers annual discount invoice")
        self.vault.write("50_people/Acme.md", frontmatter("person") + "acme corp operations contact")
        # Never indexed:
        self.vault.write("_raw/2026-01-10-call.md", "onboarding onboarding onboarding raw source")
        self.vault.write("90_archive/old.md", frontmatter(status="archived") + "onboarding archived")
        self.vault.write("40_resources/templates/note.md", "onboarding template")
        self.vault.write("30_knowledge/.hidden/secret.md", "onboarding secret")

    def tearDown(self):
        self.vault.cleanup()

    def build(self, fn=fake_embed):
        return embed.build_index(self.root, embed_fn=fn, quiet=True)

    def test_index_contains_only_wiki_pages(self):
        self.build()
        index = search.load_index(self.root)
        self.assertEqual(sorted(map(str, index["paths"])),
                         ["30_knowledge/onboarding.md", "30_knowledge/pricing.md", "50_people/Acme.md"])
        norms = np.linalg.norm(index["vectors"], axis=1)
        self.assertTrue(np.allclose(norms, 1.0, atol=1e-5))

    def test_search_ranks_the_matching_page_first(self):
        self.build()
        index = search.load_index(self.root)
        results = search.rank(index, fake_embed("why does customer onboarding stall"), k=2)
        self.assertEqual(results[0][1], "30_knowledge/onboarding.md")
        self.assertEqual(len(results), 2)
        self.assertGreater(results[0][0], results[1][0])

    def test_failed_build_keeps_the_previous_index(self):
        out = self.build()
        before = out.read_bytes()
        self.vault.write("30_knowledge/new.md", frontmatter() + "new page")

        def broken(_text):
            raise ConnectionError("ollama not running")

        with self.assertRaises(ConnectionError):
            self.build(broken)
        self.assertEqual(out.read_bytes(), before)
        with self.assertRaises(ValueError):
            self.build(lambda _t: [0.0, 0.0])  # zero vector is rejected
        self.assertEqual(out.read_bytes(), before)

    def test_stale_index_is_detected(self):
        self.build()
        self.assertEqual(search.stale_pages(self.root, search.load_index(self.root)), [])
        self.vault.write("30_knowledge/pricing.md", frontmatter() + "pricing changed")
        self.vault.write("30_knowledge/added.md", frontmatter() + "brand new")
        (self.root / "50_people/Acme.md").unlink()
        self.assertEqual(search.stale_pages(self.root, search.load_index(self.root)),
                         ["30_knowledge/added.md", "30_knowledge/pricing.md", "50_people/Acme.md"])

    def test_empty_vault_is_rejected(self):
        empty = TempVault()
        try:
            with self.assertRaises(ValueError):
                embed.build_index(empty.root, embed_fn=fake_embed, quiet=True)
        finally:
            empty.cleanup()


if __name__ == "__main__":
    unittest.main()
