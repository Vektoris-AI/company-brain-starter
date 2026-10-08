---
title: "ADR-005: AI agents draft; humans send"
type: adr
status: active
created: 2026-03-18
updated: 2026-08-12
tags: [decision, strategy, tech, example]
sources: []
confidence: high
---

# ADR-005: AI agents draft; humans send

## Context
We started using AI writing tools for follow-ups and posts. A wrong message to a client costs more
than the minutes saved.

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Agents draft, a named human sends | Safe, keeps tone personal | Human stays a bottleneck |
| B: Agents send low-risk messages | Faster | Who decides what is low-risk? |
| C: No AI drafting | Simple | Wastes time |

## Decision
A for all external communication. Decided by [[Dana-Kettlewell]] on 2026-03-18.

## Consequences
Every agent writes drafts to `00_inbox/` or as email drafts. Owners from [[pipeline]].
Basis for [[agents-draft-humans-decide]] and [[follow-up-rules]].

## Revisit when
Six months of drafts with fewer than 5% needing edits for one message type.
