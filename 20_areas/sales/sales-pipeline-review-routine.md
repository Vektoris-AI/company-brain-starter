---
title: "Routine: sales pipeline review"
type: area
status: active
created: 2026-08-03
updated: 2026-10-06
tags: [sales, routine, example]
sources: []
confidence: high
---

# Routine: sales pipeline review

**Agent:** Head of Sales · **Command:** `/sales-pipeline-review` · **When:** Mondays 9 am · **Human:** [[Jordan-Pike]]

## Reads
[[pipeline]], client pages in `50_people/`, [[follow-up-rules]], [[service-catalog]], [[capacity-board]].

## Does
- Lists deals with a next step due or overdue, grouped by owner.
- Flags deals without contact in 7+ days ([[follow-up-within-48-hours]]).
- Drafts follow-up emails (never sends), in [[brand-voice]].
- Checks every quoted price and term against [[service-catalog]] and the ADRs; flags
  conflicts (currently the Cobaltline term vs. [[ADR-004-six-month-minimum-for-retainers]]).

## Writes
`00_inbox/<date>-sales-pipeline-review.md` with a proposed diff for [[pipeline]].

## Never
Sends, changes a price, or promises a start date.
