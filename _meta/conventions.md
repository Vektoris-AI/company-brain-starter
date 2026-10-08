---
title: Naming and tag conventions
type: sop
status: active
created: 2026-01-05
updated: 2026-01-05
tags: [meta, conventions]
sources: []
confidence: high
---

# Naming and tag conventions

- File names: lowercase kebab-case, ASCII only (`pricing-model-2026.md`).
  Exception: people and companies in `50_people/` use `Company-Name.md` or
  `First-Last.md`.
- Sources in `_raw/`: `<YYYY-MM-DD>-<slug>.<ext>`, date = when the source was
  created, not when it was ingested.
- Decisions: `_meta/ADR-<NNN>-<slug>.md`, numbered without gaps.
- Agent reports and drafts: `00_inbox/<YYYY-MM-DD>-<kind>.md`.
- Tags: lowercase, singular, from this short list. Add new ones here first.
  `sales`, `strategy`, `brand`, `finance`, `ops`, `product`, `customer`,
  `decision`, `meta`, `needs-review`, `example`.
