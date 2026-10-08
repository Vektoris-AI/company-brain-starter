---
title: "ADR-001: The company brain is our single source of truth"
type: adr
status: active
created: 2026-01-08
updated: 2026-08-12
tags: [decision, strategy, meta, example]
sources: ["[[2026-01-07-founders-offsite-notes]]"]
confidence: high
---

# ADR-001: The company brain is our single source of truth

## Context
Client knowledge lived in chat threads and in two people's heads; two account handovers went
badly in Q4 2025 ([[2026-01-07-founders-offsite-notes]]). We wanted AI help, but an assistant on top
of scattered documents answers confidently and wrong ([[single-source-of-truth-before-ai]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Plain Markdown brain in git, Obsidian for humans | Diffs, no lock-in, agents can read it | Needs discipline to keep current |
| B: A wiki tool | Familiar | Hard for agents to write to safely; no review step |
| C: Keep chat + shared drive | No effort | The problem stays |

## Decision
A. Everything that matters (clients, decisions, offers, processes) lives in the brain; chat is for
talking. Decided by [[Dana-Kettlewell]] and [[Marcus-Finch]] on 2026-01-08.

## Consequences
Marcus reviews brain diffs. "If it's not in the brain, it didn't happen" ([[2026-03-26-all-hands-notes-q1]]).
Enables the [[ai-leadership-team]] later.

## Revisit when
The May or November survey shows "I can find information without asking" below 50%
([[people-kpis]]).
