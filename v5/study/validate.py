"""Validate Study 3 responses against the v5 schema and list rule findings. Never repairs output.

Schema errors make a response invalid. Rule findings (a Contradicted level without evidence, Not applicable without
a reason or on a question that applies always, a task defect under the wrong question or direction, missing detection
limits) are results of the study, counted by analyze.py, not reasons to discard a response.
Run from the repository root: python3 v5/study/validate.py [outputs-dir]
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
_spec = importlib.util.spec_from_file_location("v4_validate", ROOT / "v4/study/validate.py")
_v4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v4)
check = _v4.check  # the frozen v4 checker for the JSON Schema subset the schemas use
DEFECT_DIRECTION = {"B05": "rejects_correct", "B07": "accepts_wrong"}


def rubric():
    return json.loads((HERE / "materials/rubric.json").read_text())


def validate(data):
    errors = check(data, json.loads((HERE / "materials/schema-RUBRIC.json").read_text()))
    if errors:
        return errors
    r = rubric()
    ids = [j["item_id"] for j in data["judgments"]]
    if len(set(ids)) != len(ids):
        errors.append("duplicate item ids")
    if sorted(ids) != sorted(q["id"] for q in r["part_b"]):
        errors.append("part B ids do not match the rubric")
    if sorted(d["facet"] for d in data["description"]) != sorted(f["facet"] for f in r["part_a"]):
        errors.append("part A facets do not match the rubric")
    return errors


def rule_findings(data):
    """Return (item_id, rule) pairs for judgments that break a v5 rule."""
    always = {q["id"] for q in rubric()["part_b"] if q["applies_when"].startswith("always")}
    out = []
    for j in data["judgments"]:
        i, level = j["item_id"], j["level"]
        if level == "contradicted" and not j["evidence"]:
            out.append((i, "contradicted_without_location"))
        if level == "not_applicable" and not j["applicability_reason"].strip():
            out.append((i, "not_applicable_without_reason"))
        if level == "not_applicable" and i in always:
            out.append((i, "not_applicable_on_always"))
        if j["outcome"] != "not_performed" and not j["detection_limits"].strip():
            out.append((i, "check_without_detection_limits"))
        for d in j["task_defects"]:
            if DEFECT_DIRECTION.get(i) != d["direction"]:
                out.append((i, "task_defect_wrong_question_or_direction"))
            if not d["locator"].strip():
                out.append((i, "task_defect_without_location"))
    return out


def main():
    outputs = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "outputs"
    for p in sorted(outputs.glob("*/attempt-*/response.txt")):
        try:
            data = json.loads(p.read_text())
            errors = validate(data)
            findings = [] if errors else rule_findings(data)
        except Exception as e:  # malformed JSON is a result, not something to repair
            errors, findings = [str(e)], []
        print(p.relative_to(outputs), errors or "valid", findings or "")


if __name__ == "__main__":
    main()
