# Example: an ops cockpit on top of the brain

Optional. Once the brain holds something true, you can put agents to work on
it. This folder is the cockpit we run next to our own brain, with our data
removed:

| File | What it is |
|---|---|
| `CLAUDE.md` | Kernel: routes requests to agents and commands, lists data sources, sets operating rules |
| Agents and commands | Not here any more: the eight-role AI leadership team lives in the brain itself (`.claude/agents/`, `.claude/commands/` at the vault root). Symlink them into the cockpit |
| `hooks/finance-gate.py` + `.claude/settings.example.json` | A PreToolUse hook that keeps the cfo read-only on a bank MCP server (allowlist, fail-closed) |
| `tests/test_finance_gate.py` | Tests for the hook: `python3 -m unittest discover -s tests` |

Use it by copying this folder somewhere outside the vault (for example
`~/ops`), replacing the `<placeholders>`, and starting Claude Code there. The
agents read and write the brain through the paths you set in `CLAUDE.md`, and
they follow the brain's schema contract when they write.

The finance gate is a small example of the general idea: rules that must never
break belong in code that runs before the tool call, not in a prompt. If your
bank connector can simply be set to read-only, do that first; the hook is a
second layer for setups where it can't.
