#!/usr/bin/env python3
"""finance-gate: a PreToolUse hook that keeps AI agents read-only on your bank.

Your bank's MCP server usually runs with an owner login. That means the agent
could, in principle, do anything the bank's web app can do: create transfers,
approve requests, issue cards, edit invoices. A sentence in a prompt ("never
move money") is a request. This hook is a wall.

How it works
------------
Claude Code runs this script before every tool call whose name matches the
hook's matcher (see .claude/settings.example.json). The script reads the tool
call as JSON on stdin and:

  * exits 0  -> the tool runs (only for tools on READ_ONLY_TOOLS)
  * exits 2  -> the tool is blocked, and stderr is shown to the agent

It is an ALLOWLIST and it FAILS CLOSED:

  * a tool your bank adds next month is blocked until you review and add it
  * unreadable or empty input is blocked
  * any unexpected exception is blocked
  * if Python cannot start at all, the "|| exit 2" in the hook command blocks

Configure
---------
1. Set SERVER_PREFIXES to the tool-name prefix of your bank's MCP server.
   Local servers look like "mcp__<server-name>__". Connectors added through a
   web account often look like "mcp__<connector-id>__". Run /mcp in Claude
   Code to see the exact names.
2. Trim READ_ONLY_TOOLS to the read tools your server actually exposes. Only
   add a tool after reading its documentation. "get_" or "list_" in the name
   is not proof that a tool is harmless (some list tools return card details
   or personal data of team members).
3. Use the same prefix in the hook "matcher" in .claude/settings.json.

Test
----
    echo '{"tool_name":"mcp__yourbank__list_transactions"}' | python3 hooks/finance-gate.py; echo $?   # 0
    echo '{"tool_name":"mcp__yourbank__create_transfer"}'   | python3 hooks/finance-gate.py; echo $?   # 2
    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import json
import sys

# Tool-name prefixes of your bank's MCP server(s). Placeholder: replace it.
SERVER_PREFIXES: tuple[str, ...] = (
    "mcp__yourbank__",
)

# Read-only tools the agent may call. Example names, typical for a business
# bank API. Keep only what your server exposes and what you have reviewed.
READ_ONLY_TOOLS: frozenset[str] = frozenset({
    # Accounts and organization (balances)
    "get_organization",
    "list_bank_accounts",
    "get_bank_account",
    # Transactions and statements
    "list_transactions",
    "get_transaction",
    "list_statements",
    "get_statement",
    # Receipts (read only: no upload, no delete)
    "list_transaction_attachments",
    "get_attachment",
    # Categories (read the catalog, do not re-tag)
    "list_labels",
    "list_cash_flow_categories",
    # Receivables and payables
    "list_client_invoices",
    "get_client_invoice",
    "list_supplier_invoices",
    "get_supplier_invoice",
    # Pending requests (e.g. transfers waiting for approval): view only
    "list_requests",
})

MAX_NAME_IN_MESSAGE = 120


def short_name(tool_name: str) -> str:
    """Tool name without the server prefix, or "" if no prefix matches."""
    for prefix in SERVER_PREFIXES:
        if tool_name.startswith(prefix):
            return tool_name[len(prefix):]
    return ""


def decide(tool_name: str) -> bool:
    """True only if the tool belongs to a configured server AND is allowlisted.

    The prefix is stripped exactly (not split on the last "__"), so a name like
    "mcp__yourbank__x__list_transactions" does not sneak through.
    """
    return short_name(tool_name) in READ_ONLY_TOOLS


def read_tool_name(raw: str) -> str:
    data = json.loads(raw)
    if not isinstance(data, dict):
        return ""
    name = data.get("tool_name")
    return name if isinstance(name, str) else ""


def main() -> int:
    try:
        tool_name = read_tool_name(sys.stdin.read())
    except Exception:  # unreadable input: block
        tool_name = ""
    if tool_name and decide(tool_name):
        return 0
    shown = (short_name(tool_name) or tool_name or "unknown tool")[:MAX_NAME_IN_MESSAGE]
    print(
        f"finance-gate: '{shown}' is not on the read-only allowlist and was blocked. "
        "Agents may read bank data but never move money, approve, pay, cancel, "
        "or change anything at the bank. A human does that in the bank's own app. "
        "Allowlist: hooks/finance-gate.py",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException:  # any unexpected error blocks
        sys.exit(2)
