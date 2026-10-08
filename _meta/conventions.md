---
title: "Naming and tag conventions"
type: sop
status: active
created: 2026-01-05
updated: 2026-10-07
tags: [meta, example]
sources: []
confidence: medium
---

# Naming and tag conventions

- File names: lowercase kebab-case, ASCII only (`pricing-model-2026.md`).
  Exception: people and companies in `50_people/` use `Company-Name.md` or `First-Last.md`.
- File names are unique across the vault (Obsidian links by name). Project pages carry the
  client prefix: `alderbrook-pipeline-sprint.md`, not `pipeline-sprint.md`.
- Sources in `_raw/`: `<YYYY-MM-DD>-<slug>.<ext>`, date = when the source was created, not when it
  was ingested.
- Decisions: `_meta/ADR-<NNN>-<slug>.md`, numbered without gaps.
- Agent reports and drafts: `00_inbox/<YYYY-MM-DD>-<kind>.md`.
- Routines (what an agent does on a schedule) live in the area they belong to:
  `20_areas/<area>/<role>-<routine>-routine.md`, and the matching command in `.claude/commands/`.
- Tags: lowercase, singular, from this short list. Add new ones here first.
  `strategy`, `ops`, `finance`, `marketing`, `brand`, `sales`, `tech`, `people`, `legal`,
  `customer`, `partner`, `team`, `project`, `routine`, `kpi`, `decision`, `meta`, `needs-review`,
  `example`.
- `example` marks content of the fictional example company ([[about-this-example]]). Delete
  everything tagged `example` when you start your own brain.

Words we use with a fixed meaning: [[glossary]].
