---
title: "AI leadership team: roster and rules"
type: area
status: active
created: 2026-08-03
updated: 2026-10-01
tags: [strategy, tech, example]
sources: ["[[2026-08-05-ai-leadership-pilot-notes]]"]
confidence: high
---

# AI leadership team: roster and rules

Eight agents in `.claude/agents/`, one per leadership role. Each has a human owner who
decides. Rollout: [[ai-leadership-team-rollout]].

| Role | Human owner | Area | Routine |
|---|---|---|---|
| CEO | [[Dana-Kettlewell]] | [[strategy-overview]] | [[ceo-weekly-review-routine]] |
| COO | [[Marcus-Finch]] | [[operations-overview]] | [[coo-delivery-check-routine]] |
| CFO | [[Priya-Raman]] | [[finance-overview]] | [[cfo-cash-check-routine]] |
| CMO | [[Lena-Vasquez]] | [[marketing-overview]] | [[cmo-content-plan-routine]] |
| Head of Sales | [[Jordan-Pike]] | [[sales-overview]] | [[sales-pipeline-review-routine]] |
| CTO | [[Sam-Whitaker]] | [[technology-overview]] | [[cto-automation-review-routine]] |
| Head of People | [[Hannah-Brooks]] | [[people-overview]] | [[people-onboarding-routine]] |
| Legal & Compliance | [[Dana-Kettlewell]] with [[Pembury-Lane-Legal]] | [[legal-overview]] | [[legal-contract-check-routine]] |

## Rules for all eight
1. Propose, never decide: [[agents-draft-humans-decide]], [[ADR-005-agents-draft-humans-send]].
2. No sending, no money movement, no signatures ([[ADR-010-cfo-agent-reads-bank-only]]).
3. Write to `00_inbox/`, never commit ([[ADR-014-ai-leadership-team-at-autonomy-level-1]]).
4. Only as good as the pages they read ([[single-source-of-truth-before-ai]]).

The daily brief combines several roles: [[ADR-016-daily-brief-before-standup]].
