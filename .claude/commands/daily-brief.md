---
description: Morning brief before standup: decisions needed, delivery, pipeline, cash (orchestrates COO, Head of Sales and CFO)
---

# /daily-brief

One page that everyone reads before standup. Run steps 1 to 3 in parallel as subagents, then merge.

1. **Delivery** (agent `coo`): active projects with health, anything due in the next 48 hours,
   red clients from `20_areas/operations/client-health-scorecard.md`.
2. **Pipeline** (agent `head-of-sales`): deals in `20_areas/sales/pipeline.md` with a next step due
   today or overdue, grouped by owner; new leads in `50_people/` or `00_inbox/` since yesterday.
3. **Cash** (agent `cfo`): three lines from the latest `00_inbox/*-cfo-cash-check.md`; if older
   than 7 days, a fresh read-only check.
4. **Decisions needed:** collect every "decision needed" from steps 1 to 3 plus pages tagged
   `needs-review`. Max five, each with owner and due date.
5. **Write** `00_inbox/<YYYY-MM-DD>-daily-brief.md` with the sections `## Decisions needed`,
   `## Delivery`, `## Pipeline`, `## Cash`, `## Not checked`.
   Example: `00_inbox/2026-10-07-daily-brief.md`.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
