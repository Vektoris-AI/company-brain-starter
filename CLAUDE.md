# CLAUDE.md: Company Brain schema contract

This folder is the company's long-term memory: plain Markdown in git, opened
as an Obsidian vault by humans and read and maintained by agents. This file is
the contract every agent follows when it reads or writes here. If a skill or
another instruction conflicts with this file, this file wins.

Inspiration: Andrej Karpathy's "LLM wiki" idea
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Raw
material gets "compiled" into a linked wiki that compounds, and the schema
file (this one) tells the agent how. Here it is applied to a whole company
instead of one research topic.

Keep the vault private. A company brain ends up holding customer names,
contact data and contracts.

## Two views on the same files

| View | Folders | Purpose |
|---|---|---|
| **Humans** (PARA) | `00_inbox` `10_projects` `20_areas` `40_resources` `90_archive` | Fast navigation by what you are working on |
| **Agents** (LLM wiki) | `30_knowledge` (wiki) · `50_people` (entities) · `_raw` (immutable sources) · `_meta` (schema, decisions, log) · `_index` (search index) | Retrieval, linking, upkeep |

Same files, two entry points. Nothing is duplicated between the views.

## Where things go

| Content | Folder | `type` |
|---|---|---|
| Unsorted: notes, drafts, agent reports waiting for review | `00_inbox/` | `inbox` |
| Project with a goal and an end date | `10_projects/<client-or-product>/` | `project` |
| Ongoing responsibility (sales, strategy, brand, finance, ops) | `20_areas/<area>/` | `area` |
| One idea per page | `30_knowledge/` | `knowledge` |
| SOP, runbook, template | `40_resources/` (templates in `40_resources/templates/`) | `sop` / `template` |
| Customer, partner, team member | `50_people/<Company-or-Name>.md` | `person` |
| Finished or inactive | `90_archive/` | keep the type, set `status: archived` |
| Immutable source (transcript, PDF, export, email) | `_raw/<YYYY-MM-DD>-<slug>.<ext>` | none, never edited |
| Decision record | `_meta/ADR-<NNN>-<slug>.md` | `adr` |
| Ingest log, conventions | `_meta/` | `log` / `sop` |
| Generated search index | `_index/` | none, built by `tools/embed.py` |

## Required frontmatter (every note outside `_raw/` starts with it)

```yaml
---
title: Clear title
type: inbox | project | area | knowledge | person | sop | template | adr | log
status: active | draft | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [topic, area]
sources: []          # [[_raw/...]] links or external URLs this page is based on
confidence: high | medium | low
---
```

Optional: `contradicts: ["[[other-page]]"]`, `aliases: [...]`.

## Principles

1. **Link, don't copy.** Reference other pages as `[[page-name]]`. Never
   duplicate content. The links are the structure.
2. **`_raw/` is immutable.** Sources are added, read and cited, never edited
   or overwritten. Insights go into new or updated pages in `30_knowledge/`.
3. **Atomic and dense.** One knowledge page = one idea. Several small, linked
   pages beat one long dump. Knowledge quality is the bottleneck, not volume.
4. **Flag contradictions, don't resolve them silently.** When new information
   conflicts with a page, keep both, add `contradicts: ["[[...]]"]` to the
   frontmatter and the tag `needs-review`. A human decides.
5. **Every change is a git diff.** Agents write files; a human reviews the
   diff and commits. Risky operations (deleting pages, merging entities,
   renaming people) always need a human.
6. **Autonomy slider.** Turn agent autonomy up only where the checks are
   stably green (see below).

## Agent loops

| Loop | Skill | What it does |
|---|---|---|
| **Ingest** | `/ingest` | Source → `_raw/` → atomic pages → links and contradictions → line in `_meta/ingest-log.md` |
| **Query** | `/query` | Answer a question from the pages, with `[[citations]]`. Good answers become new pages |
| **Lint** | `/lint` | Health check: `python3 tools/lint.py`, then content review (stale, unsourced, contradictions) |

Retrieval: `python3 tools/search.py "<question>"` (semantic, needs the local
index) combined with grep for exact terms. Structure check:
`python3 tools/lint.py` (or `--files <paths>` for just the pages you touched).

## Autonomy slider

| Level | Agent may | Use when |
|---|---|---|
| 0 | Propose changes in chat only | New vault, new agent, sensitive area |
| 1 | Write files, human reviews the diff and commits | **Default** |
| 2 | Commit on its own branch, human merges | Lint has been green for weeks for this loop |
| 3 | Commit directly | Narrow, mechanical tasks only (e.g. fixing a renamed link) |

Raise the level per loop, not globally, and write the decision down as an ADR.

## Off limits

- Editing, renaming or deleting anything in `_raw/`.
- Secrets, passwords, tokens or API keys anywhere in the vault.
- Deleting from `90_archive/`. It only grows.
- Committing on behalf of a human at level 0 or 1.
