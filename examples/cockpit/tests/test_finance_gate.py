"""Tests for hooks/finance-gate.py.

Run with either:
    python3 -m unittest discover -s tests -v
    python3 -m pytest tests          (if pytest is installed)

Most tests run the hook the way Claude Code does: as a subprocess with the tool
call as JSON on stdin, checking the exit code (0 = allowed, 2 = blocked).
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE = ROOT / "hooks" / "finance-gate.py"
SETTINGS = ROOT / ".claude" / "settings.example.json"
PREFIX = "mcp__yourbank__"


def load_gate():
    spec = importlib.util.spec_from_file_location("finance_gate", GATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_gate(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(GATE)],
        input=stdin,
        capture_output=True,
        text=True,
        timeout=10,
    )


def call(tool_name: str) -> str:
    return json.dumps({"tool_name": tool_name, "tool_input": {}})


class ReadToolsAllowed(unittest.TestCase):
    def test_read_tool_is_allowed(self):
        result = run_gate(call(PREFIX + "list_transactions"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")

    def test_every_allowlisted_tool_is_allowed(self):
        gate = load_gate()
        for tool in sorted(gate.READ_ONLY_TOOLS):
            with self.subTest(tool=tool):
                self.assertTrue(gate.decide(PREFIX + tool))


class WriteAndUnknownToolsBlocked(unittest.TestCase):
    def test_write_tool_is_blocked(self):
        result = run_gate(call(PREFIX + "create_transfer"))
        self.assertEqual(result.returncode, 2)
        self.assertIn("create_transfer", result.stderr)
        self.assertIn("blocked", result.stderr)

    def test_approval_is_blocked(self):
        self.assertEqual(run_gate(call(PREFIX + "approve_request")).returncode, 2)

    def test_unknown_tool_is_blocked(self):
        # A tool the bank adds later is blocked until someone reviews it.
        self.assertEqual(run_gate(call(PREFIX + "brand_new_tool_from_next_release")).returncode, 2)

    def test_read_tool_name_on_other_server_is_blocked(self):
        self.assertEqual(run_gate(call("mcp__otherserver__list_transactions")).returncode, 2)

    def test_nested_name_trick_is_blocked(self):
        self.assertEqual(run_gate(call(PREFIX + "create_transfer__list_transactions")).returncode, 2)

    def test_bare_prefix_is_blocked(self):
        self.assertEqual(run_gate(call(PREFIX)).returncode, 2)

    def test_case_variant_is_blocked(self):
        self.assertEqual(run_gate(call(PREFIX + "List_Transactions")).returncode, 2)


class BrokenInputBlocked(unittest.TestCase):
    def test_invalid_json_is_blocked(self):
        self.assertEqual(run_gate("{not json").returncode, 2)

    def test_empty_input_is_blocked(self):
        self.assertEqual(run_gate("").returncode, 2)

    def test_missing_tool_name_is_blocked(self):
        self.assertEqual(run_gate(json.dumps({"tool_input": {}})).returncode, 2)

    def test_non_string_tool_name_is_blocked(self):
        self.assertEqual(run_gate(json.dumps({"tool_name": ["list_transactions"]})).returncode, 2)

    def test_json_that_is_not_an_object_is_blocked(self):
        self.assertEqual(run_gate(json.dumps([PREFIX + "list_transactions"])).returncode, 2)


class HookWiring(unittest.TestCase):
    def test_interpreter_failure_still_blocks(self):
        # Why the hook command ends in "|| exit 2": if Python is missing or
        # crashes with another exit code, the tool call is still blocked.
        result = subprocess.run(
            ["sh", "-c", "definitely-not-an-interpreter hooks/finance-gate.py 2>/dev/null || exit 2"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 2)

    def test_settings_example_matches_gate_prefix(self):
        settings = json.loads(SETTINGS.read_text())
        entries = settings["hooks"]["PreToolUse"]
        self.assertEqual(len(entries), 1)
        matcher = entries[0]["matcher"]
        command = entries[0]["hooks"][0]["command"]
        self.assertTrue(command.rstrip().endswith("|| exit 2"))
        self.assertIn("finance-gate.py", command)
        gate = load_gate()
        for prefix in gate.SERVER_PREFIXES:
            self.assertTrue(re.fullmatch(matcher, prefix + "list_transactions"))

    def test_denied_tools_are_not_allowlisted(self):
        settings = json.loads(SETTINGS.read_text())
        gate = load_gate()
        for rule in settings["permissions"]["deny"]:
            with self.subTest(rule=rule):
                self.assertFalse(gate.decide(rule))


if __name__ == "__main__":
    unittest.main()
