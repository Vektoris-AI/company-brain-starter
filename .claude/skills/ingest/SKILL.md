---
name: ingest
description: Add a new source to the company brain (ingest loop). Use when a file, transcript, meeting notes, email, URL or proposal should become lasting company knowledge, e.g. "add this to the brain", "ingest this transcript", "file these call notes". Runs source → _raw/ → atomic pages → links and contradictions → ingest log → lint. Never commits.
---

# Ingest: a source becomes linked knowledge

The schema contract in `CLAUDE.md` (vault root) is binding. If this skill and
the contract disagree, the contract wins.

## Steps (always in this order)

1. **Preserve the source in `_raw/`.**
   - Save the original unchanged as `_raw/<YYYY-MM-DD>-<slug>.<ext>` (date of
     the source, not of today). Transcripts and exports as `.md` or `.txt`,
     PDFs as PDF.
   - `_raw/` is immutable: never edit or overwrite. If the name exists, add
     `-2`. If a byte-identical file already exists (compare SHA-256), reference
     it instead of adding a copy.
   - Strip secrets (passwords, keys, access links) before saving. They never
     go into the vault.

2. **Find what already exists.** Before writing anything, search for pages on
   the same topics and entities: `python3 tools/search.py "<topic>"` if the
   index exists, plus grep for names and exact terms. Update existing pages
   instead of creating duplicates.

3. **Extract knowledge into pages.**
   - `30_knowledge/`: one idea per page. Condense; never paste whole sections
     of the source. Three small linked pages beat one dump.
   - `50_people/`: new companies and people (one file each).
   - `10_projects/` or `20_areas/`: only status changes that belong there.
   - Every new page gets the full required frontmatter. `sources:` links the
     `_raw/` file. Set `confidence` honestly (one source = usually `low` or
     `medium`).
   - Updated pages: bump `updated:`, add the new source to `sources:`.
   - Link generously with `[[page-name]]`, in both directions: the new page
     links to related pages, and the most related existing pages get a link back.

4. **Flag contradictions, don't resolve them.** If the source conflicts with
   an existing page, keep both statements, add `contradicts: ["[[...]]"]` and
   the tag `needs-review` to the newer page, and mention it in your summary.

5. **Log it.** Append one row to `_meta/ingest-log.md`: date · source link ·
   pages created (+) and updated (~). Bump the log's `updated:`.

6. **Check.** Run `python3 tools/lint.py --files <every page you touched>` and
   fix what it reports. Then `python3 tools/lint.py` for orphans you created.

7. **Hand over for review.** Do not commit (unless the autonomy level for
   ingest was raised in an ADR). Show `git status --short` and a summary:
   source, pages created/updated, contradictions flagged, open questions.

## Done when
- The source is in `_raw/`, unchanged.
- Every new fact lives on exactly one page and is linked from at least one other.
- Lint reports no errors for the touched pages.
- The ingest log has the new row.
