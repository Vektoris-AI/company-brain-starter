---
title: "AI leadership team rollout"
type: project
status: active
created: 2026-07-20
updated: 2026-10-01
tags: [strategy, tech, project, example]
sources: ["[[2026-08-05-ai-leadership-pilot-notes]]", "[[2026-10-01-q3-all-hands-notes]]"]
confidence: high
---

# AI leadership team rollout

| | |
|---|---|
| Owner | [[Sam-Whitaker]] (setup), [[Dana-Kettlewell]] (sponsor) |
| Started | 2026-08-03 |
| Status | In daily use, autonomy level 1 |

## What it is
Eight agents, one per leadership role, working on top of this brain. The roster and
what each one may and may not do: [[ai-leadership-team]].

## Rules
- Agents draft, humans send and decide ([[ADR-005-agents-draft-humans-send]],
  [[agents-draft-humans-decide]]).
- Level 1 for all agents: write files, never commit ([[ADR-014-ai-leadership-team-at-autonomy-level-1]]).
- The CFO agent reads bank data only ([[ADR-010-cfo-agent-reads-bank-only]]).
- The daily brief runs before standup ([[ADR-016-daily-brief-before-standup]]).

## What we saw
- Week 1: useful, but stale pages produced confident nonsense
  ([[2026-08-05-ai-leadership-pilot-notes]], [[single-source-of-truth-before-ai]]).
- Q3 all-hands: 15 of 23 use the daily brief ([[2026-10-01-q3-all-hands-notes]]).

## Next step
Review in December whether any loop can move to level 2 (see [[decisions-need-revisit-triggers]]).
