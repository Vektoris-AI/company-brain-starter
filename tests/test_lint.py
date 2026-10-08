"""Tests for tools/lint.py. Run: python3 -m unittest discover -s tests -v"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import unittest

from helpers import ROOT, TempVault, frontmatter

import lint


def kinds(result, severity=None):
    return sorted(i["kind"] for i in result["issues"] if severity in (None, i["severity"]))


class LintTestCase(unittest.TestCase):
    def setUp(self):
        self.vault = TempVault()
        self.root = self.vault.root
        # A small, healthy vault: a person and a knowledge page that link to
        # each other, both citing a raw source.
        self.vault.write("_raw/2026-01-10-call.md", "raw notes, no frontmatter needed")
        self.vault.write("50_people/Acme-Corp.md",
                         frontmatter("person") + "See [[idea-one]] and [[2026-01-10-call]].\n")
        self.vault.write("30_knowledge/idea-one.md",
                         frontmatter("knowledge") + "From [[Acme-Corp]].\n")

    def tearDown(self):
        self.vault.cleanup()

    def audit(self, **kw):
        kw.setdefault("use_git", False)
        return lint.audit(self.root, **kw)


class HealthyVault(LintTestCase):
    def test_clean_vault_has_no_issues(self):
        result = self.audit()
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["checked_notes"], 2)

    def test_raw_and_templates_are_not_checked_for_frontmatter(self):
        self.vault.write("40_resources/templates/note.md", "---\ntitle: <t>\ncreated: {{date}}\n---\n")
        self.assertEqual(self.audit()["issues"], [])

    def test_alias_heading_and_path_links_resolve(self):
        self.vault.write("20_areas/sales/overview.md", frontmatter("area") +
                         "[[idea-one|the idea]] [[idea-one#Evidence]] [[30_knowledge/idea-one]] "
                         "[[sales/overview]] [[acme-corp]] [link](../../30_knowledge/idea-one.md)\n")
        self.assertEqual(self.audit()["issues"], [])

    def test_links_inside_code_are_ignored(self):
        self.vault.write("40_resources/howto.md", frontmatter("sop") +
                         "Write links like `[[page-name]]`.\n\n```\n[[also-not-a-link]]\n```\n")
        self.assertEqual(self.audit()["issues"], [])

    def test_external_links_are_ignored(self):
        self.vault.write("40_resources/links.md", frontmatter("sop") +
                         "[site](https://example.com) [top](#heading) [mail](mailto:someone)\n")
        self.assertEqual(self.audit()["issues"], [])


class FrontmatterErrors(LintTestCase):
    def test_missing_frontmatter(self):
        self.vault.write("00_inbox/loose.md", "just text")
        self.assertEqual(kinds(self.audit(), "error"), ["frontmatter"])

    def test_missing_required_field(self):
        self.vault.write("00_inbox/x.md", frontmatter("inbox", drop=("sources", "confidence")))
        detail = self.audit()["issues"][0]["detail"]
        self.assertIn("sources", detail)
        self.assertIn("confidence", detail)

    def test_invalid_enum_values(self):
        self.vault.write("00_inbox/x.md", frontmatter("memo", status="done"))
        details = " ".join(i["detail"] for i in self.audit()["issues"])
        self.assertIn("invalid type", details)
        self.assertIn("invalid status", details)

    def test_invalid_date_and_reversed_dates(self):
        self.vault.write("00_inbox/a.md", frontmatter("inbox", created="2026-13-01"))
        self.vault.write("00_inbox/b.md", frontmatter("inbox", created="2026-02-01", updated="2026-01-01"))
        details = " ".join(i["detail"] for i in self.audit()["issues"])
        self.assertIn("invalid date in created", details)
        self.assertIn("updated is earlier than created", details)

    def test_duplicate_field(self):
        self.vault.write("00_inbox/x.md", frontmatter("inbox", extra="status: draft"))
        self.assertIn("duplicate field: status", self.audit()["issues"][0]["detail"])


class LinkErrors(LintTestCase):
    def test_dead_wikilink(self):
        self.vault.write("30_knowledge/idea-two.md",
                         frontmatter() + "Links [[Acme-Corp]] and [[does-not-exist]].\n")
        issues = [i for i in self.audit()["issues"] if i["severity"] == "error"]
        self.assertEqual([(i["kind"], i["detail"]) for i in issues], [("wikilink", "does-not-exist")])

    def test_dead_link_in_frontmatter_sources(self):
        self.vault.write("30_knowledge/idea-two.md",
                         frontmatter(extra='').replace('sources: []', 'sources: ["[[2099-missing-source]]"]')
                         + "[[Acme-Corp]]\n")
        self.assertIn("wikilink", kinds(self.audit(), "error"))

    def test_dead_markdown_link(self):
        self.vault.write("40_resources/x.md", frontmatter("sop") + "[guide](./missing.md)\n")
        self.assertEqual(kinds(self.audit(), "error"), ["markdown_link"])


class Warnings(LintTestCase):
    def test_orphan_knowledge_page_is_a_warning_not_an_error(self):
        self.vault.write("30_knowledge/lonely.md", frontmatter() + "Links out to [[Acme-Corp]].\n")
        result = self.audit()
        self.assertEqual(kinds(result), ["orphan"])
        self.assertEqual(result["errors"], 0)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(lint.main(["--root", str(self.root), "--no-git"]), 0)
            self.assertEqual(lint.main(["--root", str(self.root), "--no-git", "--strict"]), 1)

    def test_self_link_does_not_count_as_inbound(self):
        self.vault.write("30_knowledge/lonely.md", frontmatter() + "See [[lonely]].\n")
        self.assertEqual(kinds(self.audit()), ["orphan"])

    def test_archived_and_non_wiki_pages_are_not_orphans(self):
        self.vault.write("90_archive/old.md", frontmatter(status="archived"))
        self.vault.write("00_inbox/note.md", frontmatter("inbox"))
        self.assertEqual(self.audit()["issues"], [])

    def test_contradiction_without_needs_review_tag(self):
        self.vault.write("30_knowledge/idea-two.md",
                         frontmatter(extra='contradicts: ["[[idea-one]]"]') + "[[Acme-Corp]]\n")
        self.vault.write("50_people/Acme-Corp.md",
                         frontmatter("person") + "[[idea-one]] [[idea-two]] [[2026-01-10-call]]\n")
        self.assertEqual(kinds(self.audit()), ["contradiction"])

    def test_contradiction_with_needs_review_tag_is_fine(self):
        fm = frontmatter(extra='contradicts: ["[[idea-one]]"]').replace("tags: [test]", "tags: [test, needs-review]")
        self.vault.write("30_knowledge/idea-two.md", fm + "[[Acme-Corp]]\n")
        self.vault.write("50_people/Acme-Corp.md",
                         frontmatter("person") + "[[idea-one]] [[idea-two]] [[2026-01-10-call]]\n")
        self.assertEqual(self.audit()["issues"], [])


class SelectedFiles(LintTestCase):
    def test_files_option_limits_the_report(self):
        self.vault.write("00_inbox/broken.md", "no frontmatter")
        result = self.audit(selected=["30_knowledge/idea-one.md"])
        self.assertEqual(result["checked_notes"], 1)
        self.assertEqual(result["issues"], [])


@unittest.skipUnless(shutil.which("git"), "git not installed")
class RawImmutability(LintTestCase):
    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=Test",
                        "-c", "user.email=test@example.invalid", "-c", "commit.gpgsign=false", *args],
                       check=True, capture_output=True)

    def test_editing_a_committed_raw_file_is_an_error(self):
        self.git("init", "-q")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "init")
        self.vault.write("_raw/2026-01-11-new.md", "a new source is fine")
        self.assertEqual(lint.audit(self.root)["issues"], [])
        self.vault.write("_raw/2026-01-10-call.md", "edited!")
        result = lint.audit(self.root)
        self.assertEqual(kinds(result, "error"), ["raw_modified"])
        self.assertEqual(lint.audit(self.root, use_git=False)["issues"], [])


class ShippedVault(unittest.TestCase):
    def test_example_vault_is_clean(self):
        result = lint.audit(ROOT, use_git=False)
        self.assertEqual(result["issues"], [], json.dumps(result["issues"], indent=2))
        self.assertGreaterEqual(result["checked_notes"], 4)

    def test_cli_json_output(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = lint.main(["--json", "--no-git"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out.getvalue())["errors"], 0)


if __name__ == "__main__":
    unittest.main()
