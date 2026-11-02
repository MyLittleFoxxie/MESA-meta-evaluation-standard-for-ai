"""Build the disagreement log context for Study 1 after the sessions. No model calls.

For every benchmark, every pair of applied frameworks (repeat 1) and every shared concern where the recoded
concern outcomes differ, write one row with both frameworks' item level judgments (answer, basis, reason,
cited sources) so that the cause can be coded by hand with the five protocol categories. Also lists the
citations whose source string did not match a snapshot path as written. Run from the repository root:
    python3 v4/study/disagreements.py
Writes analysis/disagreement-context.json and analysis/disagreement-log.csv (cause and note blank), the
pairwise agreement table analysis/pairwise.tex, and the source check summary analysis/source-check.tex once
the coded files under analysis/coding/ exist.
"""
import csv
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE / "analysis"
J = list(csv.DictReader((A / "judgments.csv").open()))
O = list(csv.DictReader((A / "concern-outcomes.csv").open()))
JOBS = {j["id"]: j for j in json.loads((HERE / "jobs.json").read_text())["jobs"]}
responses = {}
for job in JOBS.values():
    if job["phase"] == "main" and job["repeat"] == 1:
        p = HERE / "outputs" / job["id"] / "attempt-1" / "response.txt"
        if p.exists():
            responses[(job["benchmark"], job["framework"])] = {x["item_id"]: x for x in json.loads(p.read_text())["judgments"]}

rows, context = [], []
for b in ["humaneval", "truthfulqa", "hle", "tau-bench"]:
    out = defaultdict(dict)
    for o in O:
        if o["benchmark"] == b and o["repeat"] == "1" and o["framework"] != "RUBRIC" and o["outcome"] != "not_recoded":
            out[o["framework"]][o["concern"]] = (o["outcome"], o["marker"])
    items = defaultdict(lambda: defaultdict(list))
    for j in J:
        if j["benchmark"] == b and j["repeat"] == "1" and j["answerable"] == "True":
            for c in j["concerns"].split(";"):
                if c:
                    items[j["framework"]][c].append(j["item_id"])
    for f1, f2 in combinations(sorted(out), 2):
        for c in sorted(set(out[f1]) & set(out[f2])):
            if out[f1][c][0] == out[f2][c][0]:
                continue
            def side(f):
                return [{"item_id": i, "answer": responses[(b, f)][i]["answer"], "basis": responses[(b, f)][i].get("basis"), "reason": responses[(b, f)][i].get("reason"), "missing": responses[(b, f)][i].get("missing"), "sources": [f"{e.get('source')}:{e.get('locator')}" for e in responses[(b, f)][i].get("evidence", [])]} for i in items[f][c]]
            key = f"{b}|{c}|{f1}|{f2}"
            context.append({"key": key, "benchmark": b, "concern": c, "framework_1": f1, "outcome_1": out[f1][c], "framework_2": f2, "outcome_2": out[f2][c], "items_1": side(f1), "items_2": side(f2)})
            rows.append({"key": key, "benchmark": b, "concern": c, "framework_1": f1, "outcome_1": out[f1][c][0] + ("/" + out[f1][c][1] if out[f1][c][1] else ""), "framework_2": f2, "outcome_2": out[f2][c][0] + ("/" + out[f2][c][1] if out[f2][c][1] else ""), "cause": "", "note": ""})
(A / "disagreement-context.json").write_text(json.dumps(context, indent=1) + "\n")
coded = {}
for p_ in sorted((A / "coding").glob("*-disagreements.csv")) if (A / "coding").exists() else []:
    for r in csv.DictReader(p_.open()):
        coded[r["key"]] = r
for r in rows:  # keep the causes coded under analysis/coding/ instead of blanking them on every run
    if r["key"] in coded:
        r["cause"], r["note"] = coded[r["key"]]["cause"], coded[r["key"]]["note"]
with (A / "disagreement-log.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print("disagreements", len(rows), "coded", sum(1 for r in rows if r["cause"]))

# citations whose source string did not match a path as written
C = list(csv.DictReader((A / "citations.csv").open()))
bad = [c for c in C if c["exists"] != "True"]
resolved = 0
for c in bad:
    src = HERE / "sources" / c["benchmark"]
    s = c["source"]
    if (src / "repository" / s).is_file() or (s == "README.md" and (src / "repository/README.md").is_file()):
        resolved += 1
print("unmatched source strings", len(bad), "of which name a real repository file without the repository/ prefix", resolved)

# pairwise agreement table for the manuscript
P = list(csv.DictReader((A / "pairwise-agreement.csv").open()))
NAMES = {"BB": "BetterBench", "ECBD": "ECBD", "SC": "Scorecard", "H2B": "How2Bench", "ABC": "Checklist", "OECD": "OECD facets"}
BENCH = ["humaneval", "truthfulqa", "hle", "tau-bench"]
LAB = {"humaneval": "HumanEval", "truthfulqa": "TruthfulQA", "hle": "HLE", "tau-bench": "$\\tau$-bench"}
pairs = []
for p in P:
    k = (p["framework_1"], p["framework_2"])
    if k not in pairs:
        pairs.append(k)
order = ["BB", "ECBD", "SC", "OECD", "H2B", "ABC"]
pairs.sort(key=lambda k: (order.index(k[0]), order.index(k[1])))
t = ["\\begin{table}[t]\n\\caption{Pairwise agreement across frameworks per benchmark, repeat 1: concerns with the same outcome over concerns both frameworks cover, with the stricter count that also requires the partial marker to match in parentheses. Empty cells are pairs not applied to that benchmark.}\n\\label{tab:pairwise}\n\\small\\centering\\begin{tabular}{l" + "r" * len(BENCH) + "}\\toprule\nPair & " + " & ".join(LAB[b] for b in BENCH) + " \\\\\n\\midrule\n"]
for f1, f2 in pairs:
    cells = []
    for b in BENCH:
        r = next((p for p in P if p["benchmark"] == b and (p["framework_1"], p["framework_2"]) == (f1, f2)), None)
        cells.append("" if not r else f"{r['same_outcome']}/{r['shared_concerns']} ({r['same_outcome_and_partial_marker']})")
    t.append(f"{NAMES[f1]} and {NAMES[f2]} & " + " & ".join(cells) + " \\\\\n")
tot = []
for b in BENCH:
    ps = [p for p in P if p["benchmark"] == b]
    tot.append(f"{sum(int(p['same_outcome']) for p in ps)}/{sum(int(p['shared_concerns']) for p in ps)} ({sum(int(p['same_outcome_and_partial_marker']) for p in ps)})")
t.append("\\midrule\nAll pairs & " + " & ".join(tot) + " \\\\\n\\bottomrule\\end{tabular}\n\\end{table}\n")
(A / "pairwise.tex").write_text("".join(t))
print("wrote pairwise.tex")

# manuscript copies of the grids with full names (analyze.py is frozen, so its captions are not edited)
FULL = {"humaneval": "HumanEval", "truthfulqa": "TruthfulQA", "hle": "Humanity's Last Exam", "tau-bench": "$\\tau$-bench"}
for b, name in FULL.items():
    g = (A / f"grid-{b}.tex").read_text()
    g = g.replace(f"Outcomes per concern for {b}:", f"Outcomes per concern for {name}:").replace("Repeat 1.}", "Repetition 1; the last column is the derived rubric, repetition 1, for reference only.}")
    g = g.replace("& Agentic ", "& Checklist ").replace("& New \\\\", "& Rubric \\\\").replace("& OECD ", "& OECD facets ")
    (A / f"paper-grid-{b}.tex").write_text(g)
print("wrote paper grids")

# amendment 1: same framework repeat agreement on HumanEval (see addition.md)
import sys
sys.path.insert(0, str(HERE))
from validate import validate  # noqa: E402
from analyze import recode, concern_outcome, UNANSWERABLE, parse_claude_events, read_events  # noqa: E402
M = defaultdict(list)
for r in csv.DictReader((ROOT / "v4/mapping/mapping.csv").open()) if (ROOT := HERE.parent.parent) else []:
    cell = r["final"].strip() or r["assistant_draft"].strip()
    M[r["item_id"]] = [c.strip() for c in cell.split(";") if c.strip()]
addition = {}
for fw in ("BB", "SC"):
    r1 = HERE / "outputs" / f"humaneval-{fw}" / "attempt-1" / "response.txt"
    r2s = sorted((HERE / "outputs" / f"humaneval-{fw}-2").glob("attempt-*/response.txt")) if (HERE / "outputs" / f"humaneval-{fw}-2").exists() else []
    if not r2s:
        continue
    d1, d2 = json.loads(r1.read_text()), json.loads(r2s[-1].read_text())
    errors = validate(d2, fw)
    a1 = {j["item_id"]: j for j in d1["judgments"]}
    a2 = {j["item_id"]: j for j in d2["judgments"]}
    items = sorted(set(a1) & set(a2))
    same_answer = sum(a1[i]["answer"] == a2[i]["answer"] for i in items)
    same_basis = sum(a1[i].get("basis") == a2[i].get("basis") for i in items)
    o1 = {i: recode(fw, i, a1[i]["answer"], a1[i].get("basis", "")) for i in items}
    o2 = {i: recode(fw, i, a2[i]["answer"], a2[i].get("basis", "")) for i in items}
    same_outcome = sum(o1[i][0] == o2[i][0] for i in items)
    g1, g2 = defaultdict(list), defaultdict(list)
    for i in items:
        if i in UNANSWERABLE:
            continue
        for c in M.get(i, []):
            g1[c].append(o1[i]); g2[c].append(o2[i])
    c1 = {c: concern_outcome(v) for c, v in g1.items()}
    c2 = {c: concern_outcome(v) for c, v in g2.items()}
    shared = sorted(set(c1) & set(c2))
    calls, other, usage, model = parse_claude_events(read_events(r2s[-1].parent / "events.jsonl"))
    meta = json.loads((r2s[-1].parent / "metadata.json").read_text())
    addition[fw] = {"attempt": r2s[-1].parent.name, "valid": not errors, "errors": errors, "items": len(items), "same_answer": same_answer, "same_basis": same_basis, "same_item_outcome": same_outcome,
                    "concerns": len(shared), "same_concern_outcome": sum(c1[c][0] == c2[c][0] for c in shared), "same_concern_outcome_and_partial": sum((c1[c][0], c1[c][1] == "partial") == (c2[c][0], c2[c][1] == "partial") for c in shared),
                    "differing_concerns": {c: [c1[c], c2[c]] for c in shared if c1[c][0] != c2[c][0]},
                    "differing_items": {i: [a1[i]["answer"], a2[i]["answer"]] for i in items if a1[i]["answer"] != a2[i]["answer"]},
                    "tool_calls": len(calls), "foreign_tools": len(other), "usage": usage, "returned_model": model, "elapsed_seconds": meta.get("elapsed_seconds"), "status": meta.get("status"), "prompt_sha256": meta.get("prompt_sha256")}
if addition:
    (A / "addition-repeat.json").write_text(json.dumps(addition, indent=1) + "\n")
    print("addition", json.dumps({k: {x: v[x] for x in ("items", "same_answer", "same_item_outcome", "concerns", "same_concern_outcome", "same_concern_outcome_and_partial")} for k, v in addition.items()}))
