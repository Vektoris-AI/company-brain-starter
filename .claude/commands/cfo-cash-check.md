---
description: CFO cash check: balance, runway in weeks, receivables, two scenarios (bank read-only)
---

# /cfo-cash-check

Run as agent `cfo`. Routine page: `20_areas/finance/cfo-cash-check-routine.md`.

1. Read-only bank tools: current balance and the last 8 weeks of transactions. If the connector is
   not available, say "not checked" and use the last report with its date.
2. In a script (never in your head): average weekly outflow, runway in weeks without new inflows.
3. Receivables from `20_areas/finance/receivables.md` and invoices: total, share older than 30 days.
4. Two scenarios from `forecast-model.md`: conservative (signed work only) and trend (weighted
   pipeline from `20_areas/sales/pipeline.md`).
5. Draft reminders for invoices past 7 or 21 days, addressed to the finance owner. Do not send.
6. Write `00_inbox/<YYYY-MM-DD>-cfo-cash-check.md` (figure · value · source · as of).

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
