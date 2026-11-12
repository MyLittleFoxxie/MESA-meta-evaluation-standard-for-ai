"""Read-only supplemental audit script for Paper 1 (outside the frozen set).

Never writes to or alters any frozen file under v4/, v5/study/, or v5/study-cycle2/.
Recomputes exact derived aggregates from frozen mappings and analysis CSV/JSON records
to trace every manuscript number to a deterministic file on disk:
  1. v4/mapping/mapping.csv compound and Caliper secondary-link counts.
  2. v4/study/analysis/judgments.csv Study 1 majority-rule sensitivity,
     unreported-mark (-r) denominators, and defect_found splits.
  3. Per-study mechanical file-existence and literal quote matches
     (v4/study, v5/study, and v5/study-cycle2 kept distinct).
  4. Blind author checklist empty-label verification.

Run from repository root:
    python3 v5/study-cycle2/supplemental_paper_audit.py
"""
import collections
import csv
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]
FRAMEWORKS = ["BB", "ECBD", "SC", "H2B", "ABC", "CAL", "OECD"]


def norm(s: str) -> str:
    return " ".join(s.split())


def mapping_audit():
    rows = list(csv.DictReader((ROOT / "v4/mapping/mapping.csv").open(encoding="utf-8")))
    links = 0
    per_item_counts = collections.Counter()
    cal_dist = collections.Counter()
    cal_sec_concerns = collections.Counter()
    cal_with_sec = 0
    for r in rows:
        cell = r["final"].strip() or r["assistant_draft"].strip()
        cs = [c.strip() for c in cell.split(";") if c.strip()]
        links += len(cs)
        per_item_counts[len(cs)] += 1
        if r["framework"] == "CAL":
            cal_dist[",".join(sorted(cs))] += 1
            if len(cs) > 1:
                cal_with_sec += 1
                for c in cs:
                    if c != "C23":
                        cal_sec_concerns[c] += 1
    return {
        "items": len(rows),
        "total_links": links,
        "items_with_more_than_one_concern": sum(v for k, v in per_item_counts.items() if k > 1),
        "concerns_per_item_distribution": dict(sorted(per_item_counts.items())),
        "caliper_total_items": sum(1 for r in rows if r["framework"] == "CAL"),
        "caliper_items_with_secondary_links": cal_with_sec,
        "caliper_secondary_concern_counts": dict(sorted(cal_sec_concerns.items())),
    }


def study1_sensitivity_and_counts():
    jrows = list(csv.DictReader((ROOT / "v4/study/analysis/judgments.csv").open(encoding="utf-8")))
    s1_all = [r for r in jrows if r["repeat"] == "1" and r["framework"] in FRAMEWORKS]
    s1_ans = [r for r in s1_all if r["answerable"] == "True"]

    grid = collections.defaultdict(list)
    for r in s1_ans:
        for c in r["concerns"].split(";"):
            if c:
                grid[(r["benchmark"], r["framework"], c)].append(r["outcome"])

    def eval_rule(rule_fn):
        agree = total = 0
        for b in BENCHMARKS:
            fw_out = {}
            for f in FRAMEWORKS:
                d = {}
                for (bb, ff, c), outs in grid.items():
                    if bb == b and ff == f:
                        val = rule_fn([o for o in outs if o != "not_recoded"])
                        if val is not None:
                            d[c] = val
                if d:
                    fw_out[f] = d
            for f1, f2 in itertools.combinations(sorted(fw_out), 2):
                shared = sorted(set(fw_out[f1]) & set(fw_out[f2]))
                total += len(shared)
                agree += sum(fw_out[f1][c] == fw_out[f2][c] for c in shared)
        return {"agree": agree, "pairs": total, "pct": round(agree / total * 100, 1)}

    def rule_strict_conj(xs):
        if not xs:
            return None
        if "unfavorable" in xs:
            return "unfavorable"
        if any(x == "favorable" for x in xs):
            return "favorable"
        return "unresolved"

    def rule_strict_majority(xs):
        if not xs:
            return None
        cnt = collections.Counter(xs)
        n = len(xs)
        for k, v in cnt.items():
            if v * 2 > n:
                return k
        return "unfavorable"

    def rule_plurality_ties_unfav(xs):
        if not xs:
            return None
        cnt = collections.Counter(xs)
        mx = max(cnt.values())
        top = [k for k, v in cnt.items() if v == mx]
        return top[0] if len(top) == 1 else "unfavorable"

    diff_cells = []
    for key in sorted(grid):
        xs = [o for o in grid[key] if o != "not_recoded"]
        if not xs:
            continue
        sm = rule_strict_majority(xs)
        pl = rule_plurality_ties_unfav(xs)
        if sm != pl:
            diff_cells.append(
                {
                    "cell": list(key),
                    "counts": dict(collections.Counter(xs)),
                    "strict_majority": sm,
                    "plurality": pl,
                }
            )

    abs_unfav_by_fw = collections.Counter(
        r["framework"]
        for r in s1_all
        if r["basis"] == "absence_of_information" and r["outcome"] == "unfavorable"
    )
    unreported_mark_by_fw = collections.Counter(
        r["framework"] for r in s1_all if r["marker"] == "unresolved_by_rule"
    )
    defect_rows = [r for r in s1_all if r["basis"] == "defect_found"]
    defect_by_fw = collections.Counter(r["framework"] for r in defect_rows)
    expanded_defect_cells = {
        (r["benchmark"], c)
        for r in defect_rows
        for c in r["concerns"].split(";")
        if c
    }

    return {
        "study1_total_answers": len(s1_all),
        "study1_answerable_answers": len(s1_ans),
        "strict_conjunction": eval_rule(rule_strict_conj),
        "strict_majority_gt_half_ties_unsatisfied": eval_rule(rule_strict_majority),
        "plurality_unique_mode_ties_unsatisfied": eval_rule(rule_plurality_ties_unfav),
        "strict_majority_vs_plurality_differing_cells": diff_cells,
        "absence_of_information_unfavorable_total": sum(abs_unfav_by_fw.values()),
        "absence_of_information_unfavorable_by_framework": dict(abs_unfav_by_fw),
        "unreported_mark_total": sum(unreported_mark_by_fw.values()),
        "unreported_mark_by_framework": dict(unreported_mark_by_fw),
        "bb_score5_evidence_found_count": sum(
            1
            for r in s1_all
            if r["framework"] == "BB" and r["answer"] == "5" and r["basis"] == "evidence_found"
        ),
        "four_penalizing_frameworks_total_answers": sum(
            1 for r in s1_all if r["framework"] in ("BB", "SC", "H2B", "ABC")
        ),
        "defect_found_answers_total": len(defect_rows),
        "defect_found_by_framework": dict(defect_by_fw),
        "defect_found_expanded_benchmark_concern_cells": len(expanded_defect_cells),
        "defect_found_items": [
            {
                "benchmark": r["benchmark"],
                "framework": r["framework"],
                "item_id": r["item_id"],
                "concerns": r["concerns"],
                "answerable": r["answerable"] == "True",
            }
            for r in defect_rows
        ],
    }


def citation_audit():
    c4 = list(csv.DictReader((ROOT / "v4/study/analysis/citations.csv").open(encoding="utf-8")))
    s1_c4 = [r for r in c4 if r["repeat"] == "1" and r["framework"] in FRAMEWORKS]

    c5 = list(csv.DictReader((ROOT / "v5/study/analysis/citations.csv").open(encoding="utf-8")))

    c2_jobs = [
        j
        for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))["jobs"]
        if j["phase"] == "main"
    ]
    c1_jobs = [
        j
        for j in json.loads((ROOT / "v5/study/jobs.json").read_text(encoding="utf-8"))["jobs"]
        if j["phase"] == "main"
    ]

    def inspect_raw_evidence(jobs, out_root, src_fn):
        total = exists = exact = ws = partb = pb_ex = pb_exact = pb_ws = 0
        for j in jobs:
            atts = sorted((out_root / j["id"]).glob("attempt-*"))
            data = json.loads((atts[-1] / "response.txt").read_text(encoding="utf-8"))
            sdir = src_fn(j)
            for part, arr in (("A", data["description"]), ("B", data["judgments"])):
                for item in arr:
                    for e in item["evidence"]:
                        total += 1
                        src = e["source"].replace("\\", "/")
                        p = (
                            sdir / "paper.txt"
                            if src in ("paper.txt", "paper")
                            else (
                                sdir / src
                                if src == "dataset-card.md" or src.startswith("repository/")
                                else None
                            )
                        )
                        ok = bool(p and p.is_file() and p.resolve().is_relative_to(sdir.resolve()))
                        if ok:
                            exists += 1
                        txt = (
                            p.read_text(encoding="utf-8", errors="replace")
                            if ok and b"\0" not in p.read_bytes()
                            else ""
                        )
                        q = e["quote"]
                        ex_q = bool(q.strip()) and q in txt
                        ws_q = bool(q.strip()) and (ex_q or norm(q) in norm(txt))
                        if ex_q:
                            exact += 1
                        if ws_q:
                            ws += 1
                        if part == "B":
                            partb += 1
                            if ok:
                                pb_ex += 1
                            if ex_q:
                                pb_exact += 1
                            if ws_q:
                                pb_ws += 1
        return {
            "total": total,
            "source_exists": exists,
            "exact_quote": exact,
            "whitespace_normalized_quote": ws,
            "part_b_only": {
                "total": partb,
                "source_exists": pb_ex,
                "exact_quote": pb_exact,
                "whitespace_normalized_quote": pb_ws,
            },
        }

    return {
        "study1_v4_18_sessions": {
            "total": len(s1_c4),
            "source_exists": sum(r["exists"] == "True" for r in s1_c4),
            "exact_quote": sum(r["exact_quote"] == "True" for r in s1_c4),
            "whitespace_normalized_quote": sum(r["whitespace_quote"] == "True" for r in s1_c4),
        },
        "study1_v4_all_26_main_sessions": {
            "total": len(c4),
            "source_exists": sum(r["exists"] == "True" for r in c4),
            "exact_quote": sum(r["exact_quote"] == "True" for r in c4),
            "whitespace_normalized_quote": sum(r["whitespace_quote"] == "True" for r in c4),
        },
        "cycle1_v5_study_part_b": {
            "total": len(c5),
            "source_exists": sum(r["exists"] == "True" for r in c5),
            "exact_quote": sum(r["exact_quote"] == "True" for r in c5),
            "whitespace_normalized_quote": sum(r["whitespace_quote"] == "True" for r in c5),
        },
        "cycle2_claude_part_a_and_b": inspect_raw_evidence(
            c1_jobs, ROOT / "v5/study/outputs", lambda j: ROOT / "v4/study/sources" / j["benchmark"]
        ),
        "cycle2_gemini_part_a_and_b": inspect_raw_evidence(
            [j for j in c2_jobs if j["family"] == "gemini"],
            HERE / "outputs",
            lambda j: ROOT / j["source_root"],
        ),
    }


def blind_sheet_check():
    sheet = json.loads((HERE / "blind_author_sheet.json").read_text(encoding="utf-8"))
    key = json.loads((HERE / "blind_author_key.json").read_text(encoding="utf-8"))
    filled = {
        sec: sum(1 for row in sheet[sec] if row.get("author_label", "").strip())
        for sec in ("disagreements_72", "part_b_62", "part_a_64")
    }
    key_causes = collections.Counter(row["model_cause"] for row in key["disagreements_72"])
    return {
        "filled_counts": filled,
        "disagreements_options_count": len(sheet["disagreements_72"][0]["options"]),
        "disagreements_key_causes": dict(key_causes),
        "part_a_rows": len(sheet["part_a_64"]),
        "part_a_unique_benchmark_facet_pairs": len(
            {(r["benchmark"], r["facet"]) for r in sheet["part_a_64"]}
        ),
    }


def main():
    out = {
        "note": "Read-only supplemental audit outside frozen manifest (Path B).",
        "mapping": mapping_audit(),
        "study1": study1_sensitivity_and_counts(),
        "citations": citation_audit(),
        "blind_sheet_status": blind_sheet_check(),
    }
    out_path = HERE / "analysis/supplemental-paper-checks.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
