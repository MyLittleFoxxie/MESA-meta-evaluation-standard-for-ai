"""Offline tests for the Study Cycle 2 harness, seeded fixtures, reliability, and analysis. No model calls.

Run from the repository root: python v5/study-cycle2/test_harness.py
"""
import copy
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
import analyze
import freeze
from reliability import ORDER_V5, alpha_with_ci, cohen_kappa_with_ci, nominal_distance, part_b_ordinal_distance
from validate import rubric, rule_findings, validate


def sample_response():
    r = rubric()
    return {
        "benchmark": "pilot",
        "framework": "RUBRIC",
        "limits": "Static inspection only.",
        "description": [
            {
                "facet": f["facet"],
                "value": f["values"][0] + " (stated)",
                "reason": "Stated in paper.",
                "evidence": [{"source": "paper.txt", "locator": "line 1", "quote": "Fictional pilot benchmark"}],
            }
            for f in r["part_a"]
        ],
        "judgments": [
            {
                "item_id": q["id"],
                "level": "documented",
                "basis": "evidence_found",
                "reason": "Stated in paper.",
                "evidence": [{"source": "paper.txt", "locator": "line 1", "quote": "Fictional pilot benchmark"}],
                "missing": "None.",
                "checks": "Read paper.txt.",
                "outcome": "not_performed",
                "check_kind": "none",
                "scope": {"level": "release", "ids": []},
                "detection_limits": "",
                "task_defects": [],
                "applicability_reason": "",
            }
            for q in r["part_b"]
        ],
    }


def main():
    r = rubric()
    assert len(r["part_a"]) == 8 and len(r["part_b"]) == 31
    ids = [q["id"] for q in r["part_b"]]
    for expected in ("B14a", "B14b", "B28a", "B28b"):
        assert expected in ids
    assert "B14" not in ids and "B28" not in ids

    good = sample_response()
    assert validate(good) == []
    assert rule_findings(good) == []

    bad = copy.deepcopy(good)
    bad["judgments"][0]["level"] = "verified_by_check"
    assert validate(bad)

    rules = copy.deepcopy(good)
    rules["judgments"][0].update(level="contradicted", evidence=[])
    rules["judgments"][1].update(level="not_applicable", applicability_reason="")
    rules["judgments"][2].update(outcome="passed", detection_limits="")
    rules["judgments"][4]["task_defects"] = [
        {"task_id": "t1", "direction": "accepts_wrong", "source": "paper.txt", "locator": "", "quote": "x"}
    ]
    found = set(rule_findings(rules))
    assert ("B01", "contradicted_without_location") in found
    assert ("B02", "not_applicable_without_reason") in found
    assert ("B02", "not_applicable_on_always") in found
    assert ("B03", "check_without_detection_limits") in found
    assert ("B05", "task_defect_wrong_question_or_direction") in found
    assert ("B05", "task_defect_without_location") in found

    # Check seeded fixtures and file_server
    seeded = json.loads((HERE / "seeded_truth.json").read_text(encoding="utf-8"))
    assert len(seeded["fixtures"]) == 6
    assert len(seeded["criteria_evaluated"]) == 5
    for fname in seeded["fixtures"]:
        fdir = HERE / "sources" / fname
        assert (fdir / "paper.txt").is_file()
        assert (fdir / "repository/README.md").is_file()
        assert (fdir / "repository/LICENSE").is_file()
        assert (fdir / "repository/score.py").is_file()

    # Check file_server output uses forward slashes
    proc = subprocess.run(
        [sys.executable, str(HERE / "file_server.py"), str(HERE / "sources/addtwo-clean")],
        input='{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_files","arguments":{}}}\n',
        text=True,
        capture_output=True,
        check=True,
    )
    res_text = json.loads(proc.stdout.strip())["result"]["content"][0]["text"]
    assert "repository/README.md" in res_text and "\\" not in res_text

    # Check Cycle 1 reliability reproduction and bootstrap intervals
    c1_resp, _, _, _ = analyze.load_claude_cycle1()
    rel = analyze.summarize_reliability(c1_resp, analyze.BENCHMARKS, n_boot=500)
    assert rel["part_a_alpha_nominal"] == 0.797, rel
    assert rel["part_b_alpha_ordinal"] == 0.702, rel
    assert rel["part_b_alpha_nominal"] == 0.680, rel
    assert rel["part_b_alpha_ordinal_ci95"][0] <= 0.702 <= rel["part_b_alpha_ordinal_ci95"][1]
    assert len(rel["part_a_per_facet"]) == 8

    # Check known defects registry
    known = json.loads((HERE / "known_defects.json").read_text(encoding="utf-8"))
    assert len(known["defects"]) == 7

    if (HERE / "freeze-manifest.json").exists():
        assert freeze.check(), "Cycle 2 freeze check failed"

    print("v5 Study Cycle 2 harness tests passed")


if __name__ == "__main__":
    main()
