"""After the sessions: merge the per benchmark source check files into analysis/source-check.csv and count verdicts.

Written after the freeze, like v4/study/disagreements.py; analyze.py is frozen and unchanged. The coding files
are written by the source checker (a Claude Fable 5.1 subagent per benchmark) from analysis/source-check-blank.csv.
Run from the repository root: python3 v5/study/merge_source_check.py
"""
import collections
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE / "analysis"
CHECKER = "source checker (Claude Fable 5.1 subagent)"
VERDICTS = {"supported", "weaker", "not_supported", "absence_plausible", "absence_contradicted"}


def main():
    blank = list(csv.DictReader((A / "source-check-blank.csv").open()))
    coded = {}
    for p in sorted((A / "coding").glob("*-source-check.csv")):
        for r in csv.DictReader(p.open()):
            coded[(r["benchmark"], str(r["repeat"]), r["item_id"])] = r
    rows, missing = [], []
    for b in blank:
        c = coded.get((b["benchmark"], str(b["repeat"]), b["item_id"]))
        if c is None or c["verdict"] not in VERDICTS:
            missing.append((b["benchmark"], b["repeat"], b["item_id"]))
            continue
        rows.append({"benchmark": b["benchmark"], "repeat": b["repeat"], "part": b["part"], "item_id": b["item_id"], "level_or_value": b["level_or_value"],
                     "verdict": c["verdict"], "note": c["note"], "checker": CHECKER})
    assert not missing, f"{len(missing)} rows without a valid verdict, e.g. {missing[:3]}"
    assert len(rows) == len(blank) == len(coded), (len(rows), len(blank), len(coded))
    with (A / "source-check.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    counts = {part: dict(collections.Counter(r["verdict"] for r in rows if r["part"] == part)) for part in ("A", "B")}
    counts["B_by_level"] = {lvl: dict(collections.Counter(r["verdict"] for r in rows if r["part"] == "B" and r["level_or_value"] == lvl))
                            for lvl in sorted({r["level_or_value"] for r in rows if r["part"] == "B"})}
    (A / "source-check-summary.json").write_text(json.dumps(counts, indent=1) + "\n")
    print(json.dumps(counts, indent=1))


if __name__ == "__main__":
    main()
