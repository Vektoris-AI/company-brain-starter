---
title: "Routine: CFO cash check"
type: area
status: active
created: 2026-08-03
updated: 2026-10-06
tags: [finance, routine, example]
sources: []
confidence: high
---

# Routine: CFO cash check

**Agent:** CFO · **Command:** `/cfo-cash-check` · **When:** Mondays 8 am · **Human:** [[Priya-Raman]]

## Reads
Bank balance and last 14 days of transactions (read-only connector, blocked from writing by the
finance gate, [[ADR-010-cfo-agent-reads-bank-only]]), [[receivables]], [[pipeline]] (expected
income), [[forecast-model]].

## Calculates (in a script, never in its head)
Balance with as-of date; average weekly outflow (8 weeks); runway in weeks without new inflows
([[cash-runway-in-weeks]]); receivables older than 30 days; conservative and trend scenario
([[forecasts-show-two-scenarios]]).

## Writes
`00_inbox/<date>-cfo-cash-check.md` (latest: [[2026-10-06-cfo-cash-check]]). Payment reminders
as drafts for Priya; questions for [[Ashgrove-CPA-Group]] as a list.

## Never
Pays, approves, categorizes, uploads, cancels, or sends a reminder.
