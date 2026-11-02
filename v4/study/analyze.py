"""Analyze saved responses only. Never calls a model or repairs output.

Steps: validate each response; check citations against the snapshot; parse tool use from the event log;
recode every judgment into an outcome; aggregate outcomes per concern with the final mapping; compute the
RQ2 grids and agreement counts, the RQ3 missing information counts, and the RQ4 rubric measures; recode the
existing framework applications the same way; write CSV, JSON and LaTeX tables to analysis/.
Run from the repository root: python3 v4/study/analyze.py [--outputs DIR] [--analysis DIR]
"""
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from validate import validate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
Q = json.loads((ROOT / "v4/mapping/questions.json").read_text())
JOBS = json.loads((HERE / "jobs.json").read_text())["jobs"]
BENCHMARKS = ["humaneval", "truthfulqa", "hle", "tau-bench"]
FRAMEWORKS = ["BB", "ECBD", "SC", "H2B", "ABC", "CAL", "OECD"]
NAMES = {**{k: Q["frameworks"][k]["name"] for k in FRAMEWORKS}, "RUBRIC": "New rubric"}
OECD_PREFERRED = {i["id"]: i["preferred_value"] for i in Q["items"] if i["framework"] == "OECD" and i.get("enters_agreement")}
UNANSWERABLE = {i["id"] for i in Q["items"] if str(i.get("answerable_from_inputs", "")).startswith("no")}  # recorded but kept out of concern outcomes
RUBRIC = json.loads((HERE / "materials/rubric.json").read_text())


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def write_csv(folder, name, rows, fields=None):
    with (folder / name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields or list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def mapping():
    out = defaultdict(list)
    for r in csv.DictReader((ROOT / "v4/mapping/mapping.csv").open()):
        cell = r["final"].strip() or r["assistant_draft"].strip()
        out[r["item_id"]] = [c.strip() for c in cell.split(";") if c.strip()]
    rubric_map = {}
    for b in RUBRIC["part_b"]:
        rubric_map[b["id"]] = ["C" + b["id"][1:]]  # B01 maps to C01 and so on
    out.update(rubric_map)
    return out


def concerns():
    out = {}
    for line in (ROOT / "v4/mapping/concerns.md").read_text().splitlines():
        m = re.match(r"\| (C\d\d) \| ([^|]+) \|", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


# ---------- recoding ----------

def recode(framework, item_id, answer, basis):
    """Return (outcome, marker). outcome in favorable, unfavorable, unresolved, not_recoded; marker partial, unresolved_by_rule, not_applicable, description or empty."""
    a = (answer or "").strip()
    by_rule = basis == "absence_of_information"
    if basis == "not_applicable":
        return "unresolved", "not_applicable"
    if framework == "BB":
        if a == "15":
            return "favorable", ""
        if a == "10":
            return "favorable", "partial"
        if a == "5":
            return "unfavorable", "unresolved_by_rule"
        if a == "0":
            return "unfavorable", "unresolved_by_rule" if by_rule else ""
        return "unresolved", "not_applicable"
    if framework == "ECBD":
        if basis == "defect_found":
            return "unfavorable", ""
        return ("favorable", "") if basis == "evidence_found" else ("unresolved", "")
    if framework == "SC":
        if a == "satisfied":
            return "favorable", ""
        if a == "unsatisfied":
            return "unfavorable", "unresolved_by_rule" if by_rule else ""
        return "unresolved", "not_applicable"
    if framework == "H2B":
        if a == "present":
            return "favorable", ""
        if a == "not_mentioned":
            return "unfavorable", "unresolved_by_rule"
        return "unfavorable", ""
    if framework == "ABC":
        if a == "1":
            return "favorable", ""
        return "unfavorable", "unresolved_by_rule" if by_rule else ""
    if framework == "CAL":
        if a in ("4", "5"):
            return "favorable", ""
        if a == "3":
            return "favorable", "partial"
        if a in ("1", "2"):
            return "unfavorable", "unresolved_by_rule" if by_rule else ""
        return "unresolved", ""
    if framework == "OECD":
        pref = OECD_PREFERRED.get(item_id)
        if pref is None:
            return "not_recoded", "description"
        if a.upper().startswith("N/A"):
            return "unresolved", ""
        return ("favorable", "") if a.split(" (")[0].upper() == pref.upper() else ("unfavorable", "")
    if framework == "RUBRIC":
        if a == "checked":
            return "favorable", ""
        if a in ("shown", "stated"):
            return "favorable", "partial"
        if a == "contradicted":
            return "unfavorable", ""
        if a == "not_applicable":
            return "unresolved", "not_applicable"
        return "unresolved", ""
    return "not_recoded", ""


def concern_outcome(items):
    """Aggregate item outcomes for one framework on one benchmark and concern."""
    outs = [o for o, _ in items if o != "not_recoded"]
    if not outs:
        return "not_recoded", ""
    if "unfavorable" in outs:
        marked = all(m == "unresolved_by_rule" for o, m in items if o == "unfavorable")
        return "unfavorable", "unresolved_by_rule" if marked else ""
    if all(o == "favorable" for o in outs) and not any(m == "partial" for o, m in items):
        return "favorable", ""
    if any(o == "favorable" for o in outs):
        return "favorable", "partial"
    return "unresolved", ""


# ---------- citations and events ----------

def check_citations(response, benchmark):
    src = HERE / "sources" / benchmark
    paper = (src / "paper.txt").read_text()
    paper_n = norm(paper)
    rows = []
    for j in response["judgments"]:
        for e in j.get("evidence", []):
            source = e.get("source", "")
            exists = False
            text = None
            if source in ("paper.txt", "paper"):
                exists, text = True, paper
            elif source == "dataset-card.md" and (src / "dataset-card.md").exists():
                exists, text = True, (src / "dataset-card.md").read_text()
            elif source.startswith("repository/"):
                p = (src / source)
                exists = p.is_file()
                if exists:
                    data = p.read_bytes()
                    text = None if b"\0" in data else data.decode("utf-8", errors="replace")
            quote = e.get("quote", "")
            exact = bool(text) and quote in text if quote else False
            ws = bool(text) and norm(quote) in norm(text) if quote else False
            locator = e.get("locator", "")
            resolves = bool(re.search(r"\d", locator)) if locator else False
            rows.append({"item_id": j["item_id"], "source": source, "exists": exists, "exact_quote": exact, "whitespace_quote": ws or exact, "locator_resolves": resolves, "quote_chars": len(quote)})
    return rows


def parse_claude_events(events):
    results = {}
    for e in events:
        if e.get("type") == "user":
            for c in e.get("message", {}).get("content", []) or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    results[c.get("tool_use_id")] = c
    calls, other = [], []
    for e in events:
        if e.get("type") != "assistant":
            continue
        for c in e.get("message", {}).get("content", []) or []:
            if not isinstance(c, dict) or c.get("type") != "tool_use":
                continue
            name = c.get("name", "")
            if name == "StructuredOutput":
                continue
            r = results.get(c.get("id"))
            if name.startswith("mcp__"):
                parts = name.split("__", 2)
                calls.append({"server": parts[1] if len(parts) > 2 else None, "tool": parts[2] if len(parts) > 2 else name, "ok": r is not None and not r.get("is_error")})
            else:
                other.append({"tool": name})
    usage, model = None, None
    for e in events:
        if e.get("type") == "result" and isinstance(e.get("usage"), dict):
            u = e["usage"]
            usage = {"input": u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0), "output": u.get("output_tokens", 0)}
        if e.get("type") == "assistant" and e.get("message", {}).get("model"):
            model = e["message"]["model"]
    return calls, other, usage, model


def read_events(path):
    out = []
    for line in path.read_text().splitlines():
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


# ---------- main analysis ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs", default=str(HERE / "outputs"))
    ap.add_argument("--analysis", default=str(HERE / "analysis"))
    a = ap.parse_args()
    OUT, A = Path(a.outputs), Path(a.analysis)
    A.mkdir(exist_ok=True)
    M, C = mapping(), concerns()
    jobs = {j["id"]: j for j in JOBS}
    runs, judgments, citations = [], [], []
    responses = {}
    for job_dir in sorted(OUT.glob("*")):
        job = jobs.get(job_dir.name)
        if not job:
            continue
        attempts = sorted(job_dir.glob("attempt-*"))
        for att in attempts:
            meta = json.loads((att / "metadata.json").read_text()) if (att / "metadata.json").exists() else {}
            rp = att / "response.txt"
            row = {"job": job["id"], "benchmark": job["benchmark"], "framework": job["framework"], "repeat": job["repeat"], "phase": job["phase"], "attempt": att.name,
                   "status": meta.get("status"), "valid": False, "errors": "", "tool_calls": 0, "tool_calls_ok": 0, "foreign_tools": 0, "input_tokens": None, "output_tokens": None, "returned_model": None, "elapsed_seconds": meta.get("elapsed_seconds")}
            if (att / "events.jsonl").exists():
                calls, other, usage, model = parse_claude_events(read_events(att / "events.jsonl"))
                row.update(tool_calls=len(calls), tool_calls_ok=sum(c["ok"] for c in calls), foreign_tools=len(other), returned_model=model)
                if usage:
                    row.update(input_tokens=usage["input"], output_tokens=usage["output"])
            if rp.exists():
                try:
                    data = json.loads(rp.read_text())
                    errors = validate(data, job["framework"])
                except Exception as e:
                    data, errors = None, [str(e)]
                row["valid"] = not errors
                row["errors"] = "; ".join(errors)
                if data and not errors and job["phase"] == "main":
                    responses[(job["benchmark"], job["framework"], job["repeat"])] = data
                    for j in data["judgments"]:
                        o, m = recode(job["framework"], j["item_id"], j["answer"], j.get("basis", ""))
                        judgments.append({"benchmark": job["benchmark"], "framework": job["framework"], "repeat": job["repeat"], "item_id": j["item_id"], "answer": j["answer"], "basis": j.get("basis", ""), "outcome": o, "marker": m, "concerns": ";".join(M.get(j["item_id"], [])), "answerable": j["item_id"] not in UNANSWERABLE})
                    for c in check_citations(data, job["benchmark"]):
                        citations.append({"benchmark": job["benchmark"], "framework": job["framework"], "repeat": job["repeat"], **c})
            runs.append(row)
    write_csv(A, "runs.csv", runs, ["job", "benchmark", "framework", "repeat", "phase", "attempt", "status", "valid", "errors", "tool_calls", "tool_calls_ok", "foreign_tools", "input_tokens", "output_tokens", "returned_model", "elapsed_seconds"])
    if judgments:
        write_csv(A, "judgments.csv", judgments)
    if citations:
        write_csv(A, "citations.csv", citations)

    # concern outcomes per benchmark and framework (Study 1, repeat 1) and rubric (both repeats)
    grid = defaultdict(lambda: defaultdict(list))  # (benchmark, framework, repeat) -> concern -> [(outcome, marker)]
    for j in judgments:
        if not j["answerable"]:
            continue
        for c in j["concerns"].split(";"):
            if c:
                grid[(j["benchmark"], j["framework"], j["repeat"])][c].append((j["outcome"], j["marker"]))
    outcomes = []
    for (b, f, r), cs in grid.items():
        for c, items in cs.items():
            o, m = concern_outcome(items)
            outcomes.append({"benchmark": b, "framework": f, "repeat": r, "concern": c, "outcome": o, "marker": m, "items": len(items)})
    if outcomes:
        write_csv(A, "concern-outcomes.csv", outcomes)

    # earlier reviews recoded the same way
    earlier = []
    for p in sorted((HERE / "earlier-reviews").glob("*.json")) if (HERE / "earlier-reviews").exists() else []:
        d = json.loads(p.read_text())
        for j in d["judgments"]:
            if "item_id" not in j or not j.get("answer"):
                continue
            o, m = recode(d["framework"], j["item_id"], j["answer"], j.get("basis", ""))
            earlier.append({"benchmark": d["benchmark"], "framework": d["framework"], "item_id": j["item_id"], "answer": j["answer"], "basis": j.get("basis", ""), "outcome": o, "marker": m, "concerns": ";".join(M.get(j["item_id"], [])), "answerable": j["item_id"] not in UNANSWERABLE})
    if earlier:
        write_csv(A, "earlier-judgments.csv", earlier)
    egrid = defaultdict(lambda: defaultdict(list))
    for j in earlier:
        if not j["answerable"]:
            continue
        for c in j["concerns"].split(";"):
            if c:
                egrid[(j["benchmark"], j["framework"])][c].append((j["outcome"], j["marker"]))
    earlier_outcomes = {k: {c: concern_outcome(v) for c, v in cs.items()} for k, cs in egrid.items()}

    # RQ2: pairwise agreement per benchmark among frameworks, repeat 1, on concerns both have an outcome for
    pairs = []
    summary_agreement = {}
    for b in BENCHMARKS:
        fw_out = {f: {o["concern"]: o["outcome"] for o in outcomes if o["benchmark"] == b and o["framework"] == f and o["repeat"] == 1 and o["outcome"] != "not_recoded"} for f in FRAMEWORKS}
        fw_mark = {f: {o["concern"]: (o["outcome"], o["marker"] == "partial") for o in outcomes if o["benchmark"] == b and o["framework"] == f and o["repeat"] == 1 and o["outcome"] != "not_recoded"} for f in FRAMEWORKS}
        fw_out = {f: v for f, v in fw_out.items() if v}
        for f1, f2 in combinations(sorted(fw_out), 2):
            shared = sorted(set(fw_out[f1]) & set(fw_out[f2]))
            same = sum(fw_out[f1][c] == fw_out[f2][c] for c in shared)
            strict = sum(fw_mark[f1][c] == fw_mark[f2][c] for c in shared)
            pairs.append({"benchmark": b, "framework_1": f1, "framework_2": f2, "shared_concerns": len(shared), "same_outcome": same, "same_outcome_and_partial_marker": strict})
        # agreement with the earlier review of the same framework
        for (eb, ef), eo in earlier_outcomes.items():
            if eb != b or ef not in fw_out or ef != "BB":  # the earlier review comparison is a proof of concept on BetterBench only
                continue
            shared = sorted(set(fw_out[ef]) & set(eo))
            summary_agreement[f"{b}:{ef}:agent_vs_earlier"] = {
                "shared_concerns": len(shared),
                "same_outcome": sum(fw_out[ef][c] == eo[c][0] for c in shared),
                "same_outcome_and_partial_marker": sum(fw_mark[ef][c] == (eo[c][0], eo[c][1] == "partial") for c in shared),
            }
    if pairs:
        write_csv(A, "pairwise-agreement.csv", pairs)

    # RQ3: per benchmark, concerns where one framework is unfavorable by rule and another unresolved
    rq3 = []
    for b in BENCHMARKS:
        per_c = defaultdict(dict)
        for o in outcomes:
            if o["benchmark"] == b and o["repeat"] == 1 and o["framework"] != "RUBRIC":
                per_c[o["concern"]][o["framework"]] = (o["outcome"], o["marker"])
        n = 0
        for c, fws in per_c.items():
            by_rule = [f for f, (o, m) in fws.items() if o == "unfavorable" and m == "unresolved_by_rule"]
            unresolved = [f for f, (o, m) in fws.items() if o == "unresolved"]
            if by_rule and unresolved:
                n += 1
                rq3.append({"benchmark": b, "concern": c, "unfavorable_by_rule": ";".join(by_rule), "unresolved": ";".join(unresolved)})
        summary_agreement[f"{b}:rq3_conflicts"] = n
    if rq3:
        write_csv(A, "rq3-conflicts.csv", rq3)

    # RQ4: rubric repeat agreement and missing items; a checklist for the human source check
    rq4 = {"repeat_pairs": 0, "repeat_same": 0, "absence_as_insufficient": 0, "absence_as_contradicted": 0, "absence_other": 0}
    check_rows = []
    for b in BENCHMARKS:
        r1, r2 = responses.get((b, "RUBRIC", 1)), responses.get((b, "RUBRIC", 2))
        for rep, resp in ((1, r1), (2, r2)):
            if not resp:
                continue
            for j in resp["judgments"]:
                check_rows.append({"benchmark": b, "repeat": rep, "item_id": j["item_id"], "answer": j["answer"], "cited": " | ".join(f"{e.get('source')}:{e.get('locator')}" for e in j.get("evidence", [])), "reason": j.get("reason", "")[:300], "human_verdict": "", "human_note": ""})
        if r1 and r2:
            a1 = {j["item_id"]: j["answer"] for j in r1["judgments"]}
            a2 = {j["item_id"]: j["answer"] for j in r2["judgments"]}
            for k in a1:
                if k in a2:
                    rq4["repeat_pairs"] += 1
                    rq4["repeat_same"] += a1[k] == a2[k]
        for resp in (r1, r2):
            if not resp:
                continue
            for j in resp["judgments"]:
                if j.get("basis") == "absence_of_information":  # the agent says the answer rests on an absence
                    if j["answer"] == "insufficient_evidence":
                        rq4["absence_as_insufficient"] += 1
                    elif j["answer"] == "contradicted":
                        rq4["absence_as_contradicted"] += 1
                    else:
                        rq4["absence_other"] += 1
    if check_rows:
        write_csv(A, "rq4-source-check.csv", check_rows)

    # summary
    main_runs = [r for r in runs if r["phase"] == "main"]
    summary = {
        "attempts": len(runs), "main_attempts": len(main_runs), "main_valid": sum(r["valid"] for r in main_runs),
        "main_sessions_expected": sum(1 for j in JOBS if j["phase"] == "main"),
        "judgments": len(judgments), "citations": len(citations),
        "citations_source_exists": sum(c["exists"] for c in citations), "exact_quotes": sum(c["exact_quote"] for c in citations), "whitespace_quotes": sum(c["whitespace_quote"] for c in citations), "locators_resolve": sum(c["locator_resolves"] for c in citations),
        "outcomes": dict(Counter(o["outcome"] for o in outcomes)), "unresolved_by_rule_items": sum(j["marker"] == "unresolved_by_rule" for j in judgments),
        "agreement": summary_agreement, "rq4": rq4, "earlier_judgments": len(earlier),
        "note": "Descriptive counts over nested judgments. Agreement does not establish correctness. Recoding follows v4/mapping/recoding-rules.md; outcomes marked unresolved_by_rule are unfavorable under the framework's own rule and would be unresolved under a rule that keeps missing information apart.",
    }
    (A / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")

    # tables
    tex = []
    tex.append("\\begin{table}[t]\n\\caption{Execution accounting.}\n\\label{tab:execution}\n\\centering\\begin{tabular}{lr}\\toprule\nMeasure & Count \\\\\n\\midrule\n")
    for label, key in [("Planned main sessions", "main_sessions_expected"), ("Main attempts", "main_attempts"), ("Structurally valid main responses", "main_valid"), ("Judgments", "judgments"), ("Evidence citations", "citations"), ("Citations whose source exists", "citations_source_exists"), ("Exact quote matches", "exact_quotes"), ("Whitespace normalized quote matches", "whitespace_quotes"), ("Locators that resolve", "locators_resolve")]:
        tex.append(f"{label} & {summary[key]} \\\\\n")
    tex.append("\\bottomrule\\end{tabular}\n\\end{table}\n")
    (A / "execution.tex").write_text("".join(tex))
    for b in BENCHMARKS:
        fws = [f for f in FRAMEWORKS + ["RUBRIC"] if any(o["benchmark"] == b and o["framework"] == f for o in outcomes)]
        if not fws:
            continue
        sym = {"favorable": "+", "unfavorable": "-", "unresolved": "?", "not_recoded": "d"}
        t = ["\\begin{table}[t]\n", f"\\caption{{Outcomes per concern for {b}: + favorable, (+) favorable in part, - unfavorable, ? unresolved, d description only; r marks an unfavorable outcome that follows from the framework's rule for missing information. Repeat 1.}}\n", f"\\label{{tab:grid-{b}}}\n\\small\\centering\\begin{{tabular}}{{l{'c' * len(fws)}}}\\toprule\nConcern & " + " & ".join(NAMES[f].split()[0] for f in fws) + " \\\\\n\\midrule\n"]
        for c in C:
            cells = []
            for f in fws:
                o = next((x for x in outcomes if x["benchmark"] == b and x["framework"] == f and x["repeat"] == 1 and x["concern"] == c), None)
                cells.append("" if not o else ("(+)" if o["outcome"] == "favorable" and o["marker"] == "partial" else sym[o["outcome"]]) + ("r" if o["marker"] == "unresolved_by_rule" else ""))
            if any(cells):
                t.append(f"{c} & " + " & ".join(cells) + " \\\\\n")
        t.append("\\bottomrule\\end{tabular}\n\\end{table}\n")
        (A / f"grid-{b}.tex").write_text("".join(t))
    print(json.dumps({k: v for k, v in summary.items() if k not in ("note",)}, indent=1))


if __name__ == "__main__":
    main()
