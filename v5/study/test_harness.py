"""Fixture tests for the Study 3 harness. No model calls. Run from the repository root after build_materials.py:
    python3 v5/study/test_harness.py
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from build_materials import rubric_a, rubric_b, LEVELS  # noqa: E402
from validate import validate, rule_findings  # noqa: E402
from reliability import kalpha, summarize  # noqa: E402
import analyze  # noqa: E402

RUBRIC = json.loads((HERE / "materials/rubric.json").read_text())


def judgment(i, level="documented"):
    return {"item_id": i, "level": level, "basis": "evidence_found", "reason": "r", "missing": "", "checks": "read README",
            "evidence": [{"source": "paper.txt", "locator": "p. 1", "quote": "q"}], "outcome": "not_performed", "check_kind": "none",
            "scope": {"level": "release", "ids": []}, "detection_limits": "", "task_defects": [], "applicability_reason": ""}


def response(benchmark="humaneval"):
    return {"benchmark": benchmark, "framework": "RUBRIC", "limits": "",
            "description": [{"facet": f["facet"], "value": f["values"][0], "reason": "r", "evidence": []} for f in RUBRIC["part_a"]],
            "judgments": [judgment(q["id"]) for q in RUBRIC["part_b"]]}


class Tests(unittest.TestCase):
    def test_rubric_parse(self):
        ids = [r["id"] for r in rubric_b()]
        self.assertEqual(len(ids), 31)
        self.assertTrue({"B14a", "B14b", "B28a", "B28b"} <= set(ids))
        self.assertFalse({"B14", "B28"} & set(ids))
        self.assertEqual([r["facet"] for r in rubric_a()], ["Purpose", "Judgeability", "Reference", "Containedness", "Objectivity", "Autonomy", "Progression", "Variation"])

    def test_jobs_prompts_schema(self):
        cfg = json.loads((HERE / "jobs.json").read_text())
        self.assertEqual((cfg["model"], cfg["effort"]), ("claude-sonnet-5-5", "medium"))
        self.assertEqual(sum(j["phase"] == "main" for j in cfg["jobs"]), 8)
        self.assertEqual(sum(j["phase"] == "pilot" for j in cfg["jobs"]), 1)
        for j in cfg["jobs"]:
            self.assertTrue((HERE / "prompts" / f"{j['id']}.txt").exists(), j["id"])
        schema = json.loads((HERE / "materials/schema-RUBRIC.json").read_text())
        item = schema["properties"]["judgments"]["items"]
        self.assertEqual(item["properties"]["level"]["enum"], LEVELS)
        for field in ("outcome", "check_kind", "scope", "detection_limits", "task_defects", "applicability_reason"):
            self.assertIn(field, item["required"])

    def test_validate(self):
        self.assertEqual(validate(response()), [])
        bad = response()
        bad["judgments"][0]["level"] = "shown"  # a v4 name is not a v5 level
        self.assertTrue(validate(bad))
        bad = response()
        del bad["judgments"][0]["outcome"]
        self.assertTrue(validate(bad))
        bad = response()
        bad["judgments"].pop()
        self.assertTrue(validate(bad))

    def test_rule_findings(self):
        r = response()
        self.assertEqual(rule_findings(r), [])
        j = {x["item_id"]: x for x in r["judgments"]}
        j["B01"].update(level="contradicted", evidence=[])
        j["B02"].update(level="not_applicable", applicability_reason="")
        j["B05"]["task_defects"] = [{"task_id": "t1", "direction": "accepts_wrong", "source": "s", "locator": "l1", "quote": "q"}]
        j["B06"]["outcome"] = "passed"
        found = set(rule_findings(r))
        self.assertEqual(found, {("B01", "contradicted_without_location"), ("B02", "not_applicable_without_reason"), ("B02", "not_applicable_on_always"),
                                 ("B05", "task_defect_wrong_question_or_direction"), ("B06", "check_without_detection_limits")})

    def test_kalpha(self):
        self.assertEqual(kalpha([("a", "a"), ("b", "b")]), 1.0)
        order = ["x", "y", "z"]
        self.assertLess(kalpha([("x", "z"), ("z", "x"), ("y", "y")], order), 0)

    def test_v4_figures_reproduce(self):
        s = summarize(ROOT / "v4/study/outputs", "v4")
        self.assertEqual((s["part_a_same_category"], s["part_a_pairs"], s["part_a_same_text"]), (29, 32, 23))
        self.assertEqual((s["part_b_same_level"], s["part_b_pairs"], s["part_b_applicable_pairs"]), (93, 116, 107))
        self.assertEqual(s["part_b_alpha_ordinal"], 0.779)
        self.assertEqual(s["part_a_alpha_nominal"], 0.899)

    def test_analysis_dry_run(self):
        jobs = [j for j in json.loads((HERE / "jobs.json").read_text())["jobs"] if j["phase"] == "main"]
        with tempfile.TemporaryDirectory() as tmp:
            outputs, out = Path(tmp) / "outputs", Path(tmp) / "analysis"
            for job in jobs:
                att = outputs / job["id"] / "attempt-1"
                att.mkdir(parents=True)
                (att / "metadata.json").write_text(json.dumps({"status": "completed"}))
                (att / "response.txt").write_text(json.dumps(response(job["benchmark"])))
                (att / "events.jsonl").write_text("")
            s = analyze.main(outputs, out)
            self.assertEqual(s["valid"], 8)
            self.assertEqual(s["reliability"]["part_b_pairs"], 124)
            self.assertEqual(s["field_agreement"]["same_outcome"], 124)
            self.assertEqual(sum(s["v4_to_v5"]["split"][k]["pairs"] for k in s["v4_to_v5"]["split"]), 32)
            self.assertTrue((out / "source-check-blank.csv").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
