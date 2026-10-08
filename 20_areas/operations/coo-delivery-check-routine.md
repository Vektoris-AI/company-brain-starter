---
title: "Routine: COO delivery check"
type: area
status: active
created: 2026-08-03
updated: 2026-10-02
tags: [ops, routine, example]
sources: []
confidence: high
---

# Routine: COO delivery check

**Agent:** COO · **Command:** `/coo-delivery-check` · **When:** Mondays and Thursdays · **Human:** [[Marcus-Finch]]

## Reads
All active pages in `10_projects/`, [[capacity-board]], [[client-health-scorecard]], the last
weekly status notes ([[weekly-status-report-sop]]).

## Checks
- Project page older than 7 days without an update.
- Next step without an owner or a date.
- Sprint past its planned week ([[pipeline-sprint-six-week-scope]]).
- More than three sprints in parallel ([[ADR-008-cap-concurrent-sprints-at-three]]).
- Small extra asks in client notes ([[scope-creep-arrives-as-small-asks]]).

## Writes
`00_inbox/<date>-coo-delivery-check.md`: red/amber/green per project with the reason, and a
proposed update for [[client-health-scorecard]]. Marcus edits and merges.

## Never
Reassigns people, tells clients anything, or changes deadlines.
