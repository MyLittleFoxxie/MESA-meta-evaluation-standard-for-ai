"""Fixture tests for the study harness. No model calls. Run from the repository root: python3 v4/study/test_harness.py"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from validate import validate  # noqa: E402
from analyze import recode, concern_outcome, parse_claude_events, UNANSWERABLE  # noqa: E402


class Tests(unittest.TestCase):
    def test_unanswerable_items_excluded(self):
        self.assertEqual(UNANSWERABLE, {"BB-45", "BB-46", "H2B-45", "CAL-IC-4", "CAL-OO-4", "CAL-OC-4"})
        for b in ("humaneval", "truthfulqa"):
            d = json.loads((HERE / f"earlier-reviews/BB-{b}.json").read_text())
            maint_items = [recode("BB", j["item_id"], j["answer"], j["basis"]) for j in d["judgments"] if j["item_id"] in ("BB-45", "BB-46", "BB-47") and j["item_id"] not in UNANSWERABLE]
            self.assertEqual(len(maint_items), 1)
            self.assertEqual(concern_outcome(maint_items), ("favorable", ""))
            c22_all = [recode("BB", j["item_id"], j["answer"], j["basis"]) for j in d["judgments"] if j["item_id"] in ("BB-24", "BB-45", "BB-46", "BB-47") and j["item_id"] not in UNANSWERABLE]
            self.assertEqual(len(c22_all), 2)
            self.assertEqual(concern_outcome(c22_all), ("unfavorable", "unresolved_by_rule"))

    def test_jobs(self):
        cfg = json.loads((HERE / "jobs.json").read_text())
        self.assertEqual(cfg["model"], "claude-sonnet-5-5")
        self.assertEqual(cfg["effort"], "medium")
        self.assertEqual(sum(j["phase"] == "main" for j in cfg["jobs"]), 26)
        self.assertEqual(sum(j["phase"] == "pilot" for j in cfg["jobs"]), 7)
        self.assertEqual(sum(j["framework"] == "RUBRIC" and j["phase"] == "main" for j in cfg["jobs"]), 8)
        for j in cfg["jobs"]:
            self.assertTrue((HERE / "prompts" / f"{j['id']}.txt").exists(), j["id"])
            self.assertTrue((HERE / "materials" / f"schema-{j['framework']}.json").exists(), j["framework"])

    def test_schemas_have_no_unknown_item_ids(self):
        q = json.loads((HERE.parent / "mapping/questions.json").read_text())
        ids = {i["id"] for i in q["items"]}
        for p in HERE.glob("materials/schema-*.json"):
            if p.stem.endswith("RUBRIC"):
                continue
            s = json.loads(p.read_text())
            enum = s["properties"]["judgments"]["items"]["properties"]["item_id"]["enum"]
            self.assertTrue(set(enum) <= ids, p.name)
            self.assertEqual(s["properties"]["judgments"]["minItems"], len(enum))

    def test_validate_accepts_sample_and_rejects_malformed(self):
        packet = json.loads((HERE / "materials/framework-ABC.json").read_text())
        good = {"benchmark": "x", "framework": "ABC", "limits": "", "judgments": [{"item_id": i["id"], "answer": "1", "basis": "evidence_found", "reason": "r", "missing": "", "checks": "", "evidence": []} for i in packet["items"]]}
        self.assertEqual(validate(good, "ABC"), [])
        bad = json.loads(json.dumps(good))
        bad["judgments"][0]["answer"] = "yes"
        self.assertTrue(validate(bad, "ABC"))
        bad2 = json.loads(json.dumps(good))
        bad2["judgments"].pop()
        self.assertTrue(validate(bad2, "ABC"))
        bad3 = json.loads(json.dumps(good))
        bad3["judgments"][0]["extra"] = 1
        self.assertTrue(validate(bad3, "ABC"))

    def test_oecd_values_checked(self):
        packet = json.loads((HERE / "materials/framework-OECD.json").read_text())
        resp = {"benchmark": "x", "framework": "OECD", "limits": "", "judgments": [{"item_id": i["id"], "answer": i["values"][0].split(" (")[0], "basis": "evidence_found", "reason": "", "missing": "", "checks": "", "evidence": []} for i in packet["items"]]}
        self.assertEqual(validate(resp, "OECD"), [])
        resp["judgments"][0]["answer"] = "SOMETHING ELSE"
        self.assertTrue(validate(resp, "OECD"))

    def test_recoding_rules(self):
        self.assertEqual(recode("BB", "BB-01", "15", "evidence_found"), ("favorable", ""))
        self.assertEqual(recode("BB", "BB-01", "0", "absence_of_information"), ("unfavorable", "unresolved_by_rule"))
        self.assertEqual(recode("BB", "BB-01", "0", "defect_found"), ("unfavorable", ""))
        self.assertEqual(recode("BB", "BB-01", "n/a", "not_applicable"), ("unresolved", "not_applicable"))
        self.assertEqual(recode("H2B", "H2B-01", "not_mentioned", "absence_of_information"), ("unfavorable", "unresolved_by_rule"))
        self.assertEqual(recode("SC", "SC-01", "unsatisfied", "defect_found"), ("unfavorable", ""))
        self.assertEqual(recode("OECD", "OECD-Reliability", "RELIABLE", "evidence_found"), ("favorable", ""))
        self.assertEqual(recode("OECD", "OECD-Purpose", "RESEARCH", "evidence_found"), ("not_recoded", "description"))
        self.assertEqual(recode("RUBRIC", "B01", "insufficient_evidence", "absence_of_information"), ("unresolved", ""))
        self.assertEqual(concern_outcome([("favorable", ""), ("unfavorable", "unresolved_by_rule")]), ("unfavorable", "unresolved_by_rule"))
        self.assertEqual(concern_outcome([("favorable", ""), ("unresolved", "")]), ("favorable", "partial"))
        self.assertEqual(recode("BB", "BB-01", "10", "evidence_found"), ("favorable", "partial"))
        self.assertEqual(recode("RUBRIC", "B01", "shown", "evidence_found"), ("favorable", "partial"))

    def test_event_parser(self):
        events = [{"type": "assistant", "message": {"model": "m", "content": [{"type": "tool_use", "id": "a", "name": "Bash", "input": {}}, {"type": "tool_use", "id": "c", "name": "mcp__benchmark__read_file", "input": {}}, {"type": "tool_use", "id": "s", "name": "StructuredOutput", "input": {}}]}},
                  {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "c", "is_error": True, "content": "binary"}]}},
                  {"type": "result", "usage": {"input_tokens": 1, "cache_creation_input_tokens": 2, "cache_read_input_tokens": 3, "output_tokens": 4}}]
        calls, other, usage, model = parse_claude_events(events)
        self.assertEqual([o["tool"] for o in other], ["Bash"])
        self.assertEqual(len(calls), 1)
        self.assertFalse(calls[0]["ok"])
        self.assertEqual(usage, {"input": 6, "output": 4})
        self.assertEqual(model, "m")

    def test_file_server_confinement(self):
        root = HERE / "sources/pilot/repository"
        proc = subprocess.Popen([sys.executable, str(HERE / "file_server.py"), str(root)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        reqs = [{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "README.md"}}},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "../paper.txt"}}},
                {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_files", "arguments": {}}}]
        out, _ = proc.communicate("\n".join(json.dumps(r) for r in reqs) + "\n", timeout=30)
        lines = [json.loads(l) for l in out.splitlines()]
        self.assertFalse(lines[0]["result"].get("isError"))
        self.assertTrue(lines[1]["result"].get("isError"))
        self.assertIn("README.md", lines[2]["result"]["content"][0]["text"])

    def test_runner_command_shape(self):
        import run
        job = {"id": "pilot-BB", "benchmark": "pilot", "framework": "BB", "repeat": 1, "phase": "pilot"}
        if run.BIN:
            cmd = run.command(job)
            self.assertIn("claude-sonnet-5-5", cmd)
            self.assertIn("--json-schema", cmd)
            self.assertNotIn("$schema", cmd[cmd.index("--json-schema") + 1])
            self.assertIn("--allowedTools", cmd)


if __name__ == "__main__":
    unittest.main()
