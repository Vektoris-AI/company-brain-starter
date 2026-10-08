---
description: Morning brief with today's plan, pipeline, verified numbers, cash, calendar, inbox triage
---

# /daily-brief

Run the morning brief. Steps 1 to 6 are independent; run them in parallel
where possible. A source that is not reachable in this session goes into the
brief as **"not checked"**. Never drop it silently.

1. **Today's plan:** read `<path-to-brain>/20_areas/ops/tasks.json` and list
   the 3 to 5 most important tasks for today (due today or overdue first,
   then by priority).
2. **Pipeline:** read `<path-to-brain>/20_areas/sales/pipeline.json`. List
   deals whose next action is due today or earlier: deal, owner, next action.
   Group by owner. Report data errors; do not fix them.
3. **Numbers:** ask the `analyst` for yesterday's numbers. Highlight only
   deviations from the baseline.
4. **Cash:** ask the `cfo` for balance (with as-of date), runway, and new
   incoming payments. Three lines. Read-only.
5. **Calendar:** list **all** calendars first, then today's and tomorrow's
   events for each, with the calendar name. Flag customer meetings that appear
   in the pipeline but in no calendar.
6. **Inbox:** search unread threads from the last 48 hours. Triage only: name
   the 3 to 5 most important threads (sender, subject, suggested reaction).
   Do not reply, do not label, do not archive.
7. **Write the brief** to `<path-to-brain>/00_inbox/<YYYY-MM-DD>-daily-brief.md`
   with the frontmatter from the brain's schema contract (`type: inbox`,
   `status: draft`, `confidence`, `sources`). Use the sections `## Plan`, `## Pipeline`, `## Numbers`,
   `## Cash`, `## Calendar`, `## Inbox`, `## Not checked`. **Do not commit.**

Reply in chat with a summary that fits on one screen.
