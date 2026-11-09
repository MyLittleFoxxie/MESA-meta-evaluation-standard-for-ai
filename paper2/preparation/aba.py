"""ABA overlap record for protocol 5 of Paper 2 (an external automated audit, used as a comparison only).

ABA (Wang et al. 2026, arXiv 2605.26079) publishes per-task audit findings for SWE-bench Verified. A task counts as
flagged when ABA reports at least one major finding in either audit mode (static or trajectory), ABA's own headline
measure. The record lists, for the pilot and source tasks, ABA's findings beside the task defects of the rating
forms and the B07 attempts set aside. It is never an input to the rating forms.

    python3 -m paper2.preparation.aba PATH_TO_benchmark.json
"""
import hashlib
import json
import sys
from pathlib import Path

from paper2.preparation import study_controls as s

URL = "https://data.autobenchaudit.com/benchmarks/swe_bench_verified/benchmark.json"
OUT = s.PROTOCOL / "audit_checks" / "aba-overlap.json"
FIELDS = ("static_findings_major", "static_findings_minor", "static_findings_by_category", "static_summary",
          "trajectory_findings_major", "trajectory_findings_minor", "trajectory_findings_by_category",
          "trajectory_summary")


def flagged(task):
    return bool(task.get("static_findings_major") or task.get("trajectory_findings_major"))


def overlap(benchmark_json, forms_dir=None, out=OUT):
    raw = Path(benchmark_json).read_bytes()
    tasks = {t["task_id"]: t for t in json.loads(raw)["tasks"]}
    requirement = json.loads((s.PROTOCOL / "requirement-draft.json").read_text())
    pilot = ["sympy__sympy-13798"]
    source = requirement["task_set"]["source"]
    forms_dir = Path(forms_dir or s.PROTOCOL / "audit_forms" / "drafts")
    defects = {}
    for name in ("B05-release", "B07-release"):
        for d in json.loads((forms_dir / f"{name}.json").read_text()).get("task_defects") or []:
            defects.setdefault(d["task_id"], []).append(name.split("-")[0])
    attempts = s.PROTOCOL / "audit_checks" / "b07-counterexamples"
    shown = {p.parent.name for p in attempts.glob("*/attempt.json")
             if json.loads(p.read_text())["outcome"] == "defect demonstrated"}
    rows = []
    for t in pilot + source:
        a = tasks.get(t)
        rows.append(dict(task_id=t, role="pilot" if t in pilot else "source", in_aba=a is not None,
                         aba_flagged=flagged(a) if a else None, **({k: a.get(k) for k in FIELDS} if a else {}),
                         form_task_defects=defects.get(t, []),
                         b07_set_aside=t in shown and "B07" not in defects.get(t, [])))
    src = [r for r in rows if r["role"] == "source"]
    record = dict(record="paper2-aba-overlap/1", source=URL, sha256=hashlib.sha256(raw).hexdigest(),
                  fetched_at="2026-11-09", rule="flagged: at least one major finding, static or trajectory",
                  compared_with=str(forms_dir.relative_to(s.ROOT)), tasks=rows,
                  flagged_source_tasks=[r["task_id"] for r in src if r["aba_flagged"]],
                  summary=dict(source_tasks=len(src), aba_flagged=sum(bool(r["aba_flagged"]) for r in src),
                               form_defects=sum(bool(r["form_task_defects"]) for r in src),
                               both=sum(bool(r["aba_flagged"]) and bool(r["form_task_defects"]) for r in src)))
    s.save_new(out, record)
    return record


if __name__ == "__main__":
    print(json.dumps(overlap(sys.argv[1])["summary"]))
