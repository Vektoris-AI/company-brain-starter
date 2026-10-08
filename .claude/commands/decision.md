---
description: Record a decision as an ADR in _meta/ (draft, no commit)
argument-hint: "<decision topic>"
---

# /decision

Record the decision on `$ARGUMENTS` as a decision record in `_meta/`.

1. **Clarify the context.** If the conversation doesn't make it clear, ask: what is the problem,
   which options were on the table, what was decided, by whom, and why?
2. **Number it.** Next free number after the existing `_meta/ADR-*.md`. File:
   `ADR-<NNN>-<kebab-slug>.md`.
3. **Write it** from `40_resources/templates/adr.md`: Context, Options (pros and cons), Decision
   (who, when), Consequences, **Revisit when** (a number, a date or an event). `status: draft`
   until a human merges it.
4. **Link it** to the affected pages, and add a link back from the most related ones. If it
   contradicts an existing page, set `contradicts:` and the tag `needs-review` there.

**Always:** frontmatter per `CLAUDE.md` (`type: adr`, `status: draft`). Never commit; the diff stays for human review.
