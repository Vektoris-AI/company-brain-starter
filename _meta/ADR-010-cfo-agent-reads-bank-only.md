---
title: "ADR-010: The CFO agent reads bank data and never moves money"
type: adr
status: active
created: 2026-06-03
updated: 2026-08-05
tags: [decision, finance, tech, example]
sources: ["[[2026-08-05-ai-leadership-pilot-notes]]"]
confidence: high
---

# ADR-010: The CFO agent reads bank data and never moves money

## Context
We wanted the CFO agent to answer cash questions from live bank data. The bank connector also
exposes write actions.

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Read-only tools + a pre-tool hook that blocks writes | Enforced in code, testable | Some setup |
| B: Prompt rule only | Easy | One bad instruction away from a transfer |
| C: No bank access | Safest | Agent can't answer cash questions |

## Decision
A. Only [[Priya-Raman]] (backup: [[Dana-Kettlewell]]) approves payments. Decided on 2026-06-03.

## Consequences
The finance gate (in `examples/cockpit/hooks/`) blocks every write call. In the pilot it blocked
an attempt to mark an invoice paid ([[2026-08-05-ai-leadership-pilot-notes]]).

## Revisit when
Never for money movement. Revisit the tooling if the bank offers a true read-only token.
