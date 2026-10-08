---
title: "ADR-001: Pitch a documented onboarding checklist before any AI assistant"
type: adr
status: draft
created: 2026-01-13
updated: 2026-01-13
tags: [decision, sales, example]
sources: ["[[2026-01-12-example-discovery-call]]"]
confidence: medium
---

# ADR-001: Pitch a documented onboarding checklist before any AI assistant

> Fictional example decision record. Copy `40_resources/templates/adr.md` for
> real ones.

## Context
[[Example-Customer-Inc]] asked for "a chatbot that knows our processes". Their
last chatbot failed because it read outdated documents. See
[[example-onboarding-is-the-real-bottleneck]].

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Build the assistant right away | What the customer asked for | Repeats the failure: it reads unreviewed documents |
| B: First write the onboarding process as reviewed pages, then add the assistant | The assistant reads one true version | Slower first visible result |
| C: Do nothing | No effort | Lost deal |

## Decision
B. The pilot starts with the documented process; the assistant is phase two.
Decided by the founder on 2026-01-13.

## Consequences
The proposal leads with the documentation work. We need a short template for
process pages in `40_resources/`.

## Revisit when
Two pilots in a row show that customers will not pay for the documentation
phase on its own.
