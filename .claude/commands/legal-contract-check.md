---
description: Legal & Compliance contract check against the playbook: deviations, fallbacks, questions for counsel
argument-hint: "<file or page>"
---

# /legal-contract-check

Run as agent `legal-compliance` for `$ARGUMENTS`. Routine page:
`20_areas/legal/legal-contract-check-routine.md`.

1. Make sure the document is saved unchanged in `_raw/` (via `/ingest` if it is new).
2. Go clause by clause against `20_areas/legal/contract-playbook.md`: payment, liability, IP,
   approvals, data, AI use, subprocessors, termination, insurance.
3. Mark each: standard / deviates / missing. Give the playbook fallback for each deviation.
4. Check data and AI clauses against `internal-privacy-policy.md`, `ai-use-policy.md` and
   `data-access-policy.md`.
5. List precise questions for counsel.
6. Write `00_inbox/<YYYY-MM-DD>-legal-contract-check.md` with a recommendation: sign as is /
   negotiate / escalate. You never sign or accept anything.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
