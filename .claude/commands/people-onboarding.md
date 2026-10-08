---
description: Head of People onboarding pack for a new hire: 30-60-90 plan, reading list, buddy, account checklist
argument-hint: "<name>"
---

# /people-onboarding

Run as agent `head-of-people` for `$ARGUMENTS`. Routine page:
`20_areas/people/people-onboarding-routine.md`.

1. Read the person's page in `50_people/` and their role in `role-scorecards.md`.
2. Draft a 30-60-90 plan from the scorecard outcomes.
3. Reading list: ten brain pages for week 1 (company profile, service catalog, the projects they
   join, the relevant SOPs).
4. Propose a buddy (someone on the same client) and a "who to ask about what" list from the org chart.
5. Account checklist per `40_resources/sops/access-request-sop.md`: accounts only, no passwords.
6. Write `00_inbox/<YYYY-MM-DD>-onboarding-<name>.md`. No salary, no personal data.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
