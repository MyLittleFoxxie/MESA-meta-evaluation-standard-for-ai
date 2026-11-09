"""Offline analysis of Study 3 (rubric v5). No model calls. Writes v5/study/analysis/.

Outputs: summary.json (counts below), judgments.csv, citations.csv, runs.csv, rule-findings.csv, v4-v5.csv, and
source-check-blank.csv, the list the source checker fills in as source-check.csv. Reuses the frozen v4 citation check
and event parser. Run from the repository root: python3 v5/study/analyze.py
"""
import collections
import csv
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from validate import validate, rule_findings  # noqa: E402
from reliability import summarize, load, BENCHMARKS  # noqa: E402

_spec = importlib.util.spec_from_file_location("v4_analyze", ROOT / "v4/study/analyze.py")
_v4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v4)
V4_TO_V5 = {"stated": "claimed", "shown": "documented", "checked": "verified", "contradicted": "contradicted", "insufficient_evidence": "undocumented", "not_applicable": "not_applicable"}
SPLITS = {"B14a": "B14", "B14b": "B14", "B28a": "B28", "B28b": "B28"}


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        if not rows:
            return
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def latest(folder):
    attempts = sorted(folder.glob("attempt-*"), key=lambda p: int(p.name.split("-")[1]))
    return attempts[-1] if attempts else None


def cost(events):
    return sum(e.get("total_cost_usd", 0) or 0 for e in events if e.get("type") == "result")


def main(outputs=HERE / "outputs", out=HERE / "analysis"):
    jobs = [j for j in json.loads((HERE / "jobs.json").read_text())["jobs"] if j["phase"] == "main"]
    runs, rows, cites, findings, check_rows, responses = [], [], [], [], [], {}
    for job in jobs:
        att = latest(Path(outputs) / job["id"])
        if att is None:
            runs.append({"job": job["id"], "status": "not run"})
            continue
        meta = json.loads((att / "metadata.json").read_text())
        events = _v4.read_events(att / "events.jsonl") if (att / "events.jsonl").exists() else []
        calls, other, usage, model = _v4.parse_claude_events(events)
        try:
            resp = json.loads((att / "response.txt").read_text())
            errors = validate(resp)
        except Exception as e:  # a malformed response is a result, not something to repair
            resp, errors = None, [str(e)]
        runs.append({"job": job["id"], "attempt": att.name, "status": meta.get("status"), "valid": not errors, "returned_model": model, "file_server_calls": len(calls),
                     "failed_calls": sum(not c["ok"] for c in calls), "other_tools": len(other), "input_tokens": (usage or {}).get("input"),
                     "output_tokens": (usage or {}).get("output"), "cost_usd": round(cost(events), 4), "rated_by": meta.get("rated_by"), "signed_by": meta.get("signed_by")})
        if errors:
            continue
        b, rep = job["benchmark"], job["repeat"]
        responses[(b, rep)] = resp
        for d in resp["description"]:
            check_rows.append({"benchmark": b, "repeat": rep, "part": "A", "item_id": d["facet"], "level_or_value": d["value"],
                               "evidence": " | ".join(f"{e['source']} {e['locator']}: {e['quote']}" for e in d["evidence"]), "verdict": "", "note": ""})
        for j in resp["judgments"]:
            rows.append({"benchmark": b, "repeat": rep, "item_id": j["item_id"], "level": j["level"], "basis": j["basis"], "outcome": j["outcome"], "check_kind": j["check_kind"],
                         "scope": j["scope"]["level"], "scope_ids": len(j["scope"]["ids"]), "evidence": len(j["evidence"]), "task_defects": len(j["task_defects"]),
                         "detection_limits": bool(j["detection_limits"].strip())})
            check_rows.append({"benchmark": b, "repeat": rep, "part": "B", "item_id": j["item_id"], "level_or_value": j["level"],
                               "evidence": " | ".join(f"{e['source']} {e['locator']}: {e['quote']}" for e in j["evidence"]), "verdict": "", "note": ""})
        cites += [{"benchmark": b, "repeat": rep, **c} for c in _v4.check_citations(resp, b)]
        findings += [{"benchmark": b, "repeat": rep, "item_id": i, "rule": r} for i, r in rule_findings(resp)]

    summary = {"sessions": len(jobs), "valid": len(responses), "cost_usd": round(sum(r.get("cost_usd", 0) or 0 for r in runs), 2),
               "returned_models": sorted({r.get("returned_model") for r in runs if r.get("returned_model")}),
               "other_tools_used": sum(r.get("other_tools", 0) or 0 for r in runs)}
    if len(responses) == len(jobs):
        summary["reliability"] = summarize(outputs, "v5")
        fields = collections.Counter()
        for b in BENCHMARKS:
            j1 = {j["item_id"]: j for j in responses[(b, 1)]["judgments"]}
            for j in responses[(b, 2)]["judgments"]:
                k = j1[j["item_id"]]
                fields["pairs"] += 1
                fields["same_outcome"] += j["outcome"] == k["outcome"]
                fields["same_check_kind"] += j["check_kind"] == k["check_kind"]
                fields["same_scope"] += j["scope"]["level"] == k["scope"]["level"]
                fields["same_level_and_outcome"] += (j["level"], j["outcome"]) == (k["level"], k["outcome"])
        summary["field_agreement"] = dict(fields)
    summary["levels"] = dict(collections.Counter(r["level"] for r in rows))
    summary["outcomes"] = dict(collections.Counter(r["outcome"] for r in rows))
    summary["check_kinds"] = dict(collections.Counter(r["check_kind"] for r in rows))
    summary["scopes"] = dict(collections.Counter(r["scope"] for r in rows))
    summary["absence"] = dict(collections.Counter(r["level"] for r in rows if r["basis"] == "absence_of_information"))
    summary["contradicted"] = {"ratings": sum(r["level"] == "contradicted" for r in rows), "with_location": sum(r["level"] == "contradicted" and r["evidence"] > 0 for r in rows)}
    summary["not_applicable"] = sum(r["level"] == "not_applicable" for r in rows)
    summary["task_defects"] = sum(r["task_defects"] for r in rows)
    summary["rule_findings"] = dict(collections.Counter(f["rule"] for f in findings))
    summary["citations"] = {"evidence": len(cites), "source_exists": sum(c["exists"] for c in cites), "quote_found": sum(c["whitespace_quote"] for c in cites)}

    # v4 to v5, same benchmark and repeat number; the pairing by repeat number is arbitrary
    compare = []
    for (b, rep), resp in sorted(responses.items()):
        v4 = {j["item_id"]: V4_TO_V5[j["answer"]] for j in load(ROOT / "v4/study/outputs", b, rep)["judgments"]}
        for j in resp["judgments"]:
            old = SPLITS.get(j["item_id"], j["item_id"])
            compare.append({"benchmark": b, "repeat": rep, "v4_item": old, "v5_item": j["item_id"], "v4_level": v4[old], "v5_level": j["level"], "same": v4[old] == j["level"]})
    unsplit = [c for c in compare if c["v5_item"] not in SPLITS]
    summary["v4_to_v5"] = {"unsplit_pairs": len(unsplit), "unsplit_same": sum(c["same"] for c in unsplit),
                           "split": {k: {"pairs": sum(c["v5_item"] == k for c in compare), "same_as_v4": sum(c["v5_item"] == k and c["same"] for c in compare)} for k in SPLITS}}

    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    write_csv(out / "runs.csv", runs)
    write_csv(out / "judgments.csv", rows)
    write_csv(out / "citations.csv", cites)
    write_csv(out / "rule-findings.csv", findings)
    write_csv(out / "v4-v5.csv", compare)
    write_csv(out / "source-check-blank.csv", check_rows)
    print(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    main()
