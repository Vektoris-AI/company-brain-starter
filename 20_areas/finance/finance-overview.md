---
title: "Finance (CFO area)"
type: area
status: active
created: 2026-01-12
updated: 2026-09-17
tags: [finance, example]
sources: []
confidence: high
---

# Finance (CFO area)

**Human owner:** [[Priya-Raman]] · **AI role:** CFO agent (bank read-only) · **Routine:** [[cfo-cash-check-routine]]

## What lives here
- Cash and runway rules: [[cash-runway-in-weeks]], [[forecasts-show-two-scenarios]].
- Who owes us: [[receivables]]. Where we are heading: [[forecast-model]].
- Month-end: [[month-end-close-routine]], [[invoice-run-sop]]. KPIs: [[finance-kpis]].
- Outside accountant: [[Ashgrove-CPA-Group]].

## Hard rules
- Only Priya (and Dana as backup) approves payments. Agents never move money
  ([[ADR-010-cfo-agent-reads-bank-only]]).
- Sprints 50% upfront ([[ADR-006-fifty-percent-upfront-for-sprints]]); new clients net-15
  ([[ADR-017-net-15-payment-terms]]).
- Individual salaries never appear in the brain; payroll only as a total.
