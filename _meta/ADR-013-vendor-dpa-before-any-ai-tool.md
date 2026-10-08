---
title: "ADR-013: No AI tool sees client data without a signed DPA"
type: adr
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [decision, legal, tech, example]
sources: ["[[2026-07-15-pembury-legal-memo-ai-vendors]]", "[[2026-07-02-tool-audit-export]]"]
confidence: high
---

# ADR-013: No AI tool sees client data without a signed DPA

## Context
Three AI writing tools were bought on personal cards without data terms
([[2026-07-02-tool-audit-export]]); counsel explained the risk
([[2026-07-15-pembury-legal-memo-ai-vendors]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: DPA + approved list per data class | Defensible, answerable in questionnaires | Fewer tools |
| B: Ban AI tools | Simple | Loses the benefit |
| C: Trust each person | Fast | Unknown exposure |

## Decision
A, criteria in [[vendor-dpa-checklist]]. Decided by [[Dana-Kettlewell]] on 2026-07-22.

## Consequences
[[ai-use-policy]]; two of three tools dropped, one approved after signing.

## Revisit when
A client MSA requires stricter terms, or counsel updates the guidance.
