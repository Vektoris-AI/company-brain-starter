---
description: Verified metrics on demand (sales, usage, payments, traffic, pipeline)
argument-hint: "[sales|usage|payments|traffic|pipeline, empty = all]"
---

# /numbers

Ask the `analyst` agent for a fresh pull of verified metrics.
Scope: `$ARGUMENTS` (empty = all sources).

Requirements for the answer:
- Table: metric · value · delta vs. baseline · source · timestamp
- Unreachable sources are listed as "not verifiable". Never estimate.
- 1 to 3 sentences of context. No unrequested recommendations.
