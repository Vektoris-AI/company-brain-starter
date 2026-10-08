---
name: lint
description: Health check of the company brain (lint loop). Use for "check the brain", "lint the vault", "clean up the knowledge base", before a review, or after a large ingest. Runs the structural check, then reviews content for stale, unsourced, duplicate and contradictory pages, and proposes fixes as a diff.
---

# Lint: keep the brain trustworthy

## 1. Structure (scripted)

Run `python3 tools/lint.py`. It reports:

| Severity | Kind | Typical fix |
|---|---|---|
| error | `frontmatter` | Add the missing fields or correct the values |
| error | `wikilink`, `markdown_link` | Fix the target name, or create the missing page if it should exist |
| error | `raw_modified` | Restore the `_raw/` file (`git restore`); put the new content in a new source |
| warning | `orphan` | Link the page from its most related pages, or archive it |
| warning | `contradiction` | Add the `needs-review` tag so a human sees it |

Fix structural issues directly in the files (they are mechanical), except:
never edit `_raw/` content, never delete pages, never merge entities on your own.

## 2. Content (judgment)

Then review and list, without changing content on your own:

- **Stale:** `status: active` pages whose `updated:` is older than 90 days
  and that describe something that changes (prices, status, plans).
- **Unsourced:** `confidence: high` with empty `sources:`.
- **Duplicates:** two pages about the same idea or entity (search for
  similar titles). Propose a merge; a human decides.
- **Open contradictions:** every page tagged `needs-review`, with the two
  conflicting statements side by side.
- **Not atomic:** pages in `30_knowledge/` that clearly contain several ideas.
  Propose a split.

## 3. Report

Write the report to `00_inbox/<YYYY-MM-DD>-lint-report.md` (type `inbox`,
status `draft`): numbers per category, then the items, each with a proposed
action. Do not commit. Re-run `python3 tools/lint.py` at the end and include
the final line of its output.
