"""Transcribe the existing framework applications for the four benchmarks into item level records.

Sources: the BetterBench database page (HumanEval, TruthfulQA), the Agentic Benchmark Checklist assessment
file for tau-bench, the Benchmark Caliper assessment file for HELM, and the ECBD worksheet for HELM.
Each record carries the framework's own answer per item so it can be recoded like an agent response.
Run from the repository root with the downloaded copies:
    python3 v4/study/earlier_reviews.py --betterbench <database.html> --abc <tau-bench.yaml> --caliper <helm.yaml> --ecbd <helm_worksheet.txt>
Writes v4/study/earlier-reviews/*.json. No model calls.
"""
import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "earlier-reviews"
Q = json.loads((HERE.parent / "mapping/questions.json").read_text())
BB_ITEMS = [i for i in Q["items"] if i["framework"] == "BB"]


def betterbench(html, name, benchmark):
    i = html.index(f'name: "{name}"')
    j = html.find('\n    name: "', i + 10)
    b = html[i:j if j > 0 else None]
    crit = re.findall(r'"([^"]+)": \{\s*score: ([^,\n]+),\s*explanation: (["\'])(.*?)\3', b, re.S)
    if len(crit) != 47:
        raise SystemExit(f"{name}: expected 47 criteria, found {len(crit)}")
    judgments = []
    for item, (cname, score, _, expl) in zip(BB_ITEMS, crit):
        # the database names differ from the template in a few words; match by order and record both
        s = score.strip().strip('"')
        judgments.append({"item_id": item["id"], "database_name": cname, "answer": "n/a" if s == "n/a" else s, "explanation": expl.strip(),
                          "basis": "not_applicable" if s == "n/a" else ("absence_of_information" if s == "0" and re.search(r"\bnot\b|\bno\b|does not|did not|without", expl, re.I) else "evidence_found")})
    return {"benchmark": benchmark, "framework": "BB", "source": "betterbench.stanford.edu/database.html, retrieved 31 October 2026", "reviewers": "framework authors", "date": "not stated on the page", "judgments": judgments,
            "note": "basis is a mechanical reading of the explanation: a 0 whose explanation says the item is absent is absence_of_information; the author checks each before use"}


def abc(yaml_text):
    judgments = []
    for m in re.finditer(r"^([TOR]\.(?:[a-i]\.)?\d+):\n\s+check: (.*)\n\s+score: (\d)\n\s+reason: (.*)$", yaml_text, re.M):
        pid, check, score, reason = m.groups()
        basis = "not_applicable" if re.search(r"does not use|not use external|does not require", reason, re.I) else ("absence_of_information" if score == "0" and re.search(r"does not specify|does not mention|does not discuss|does not include|does not provide|does not report|not specified|no .* provided|not documented", reason, re.I) else ("defect_found" if score == "0" else "evidence_found"))
        judgments.append({"item_id": "ABC-" + pid, "answer": score, "reason": reason.strip(), "basis": basis})
    return {"benchmark": "tau-bench", "framework": "ABC", "source": "github.com/uiuc-kang-lab/agentic-benchmarks/assessments/tau-bench.yaml", "reviewers": "framework authors", "judgments": judgments,
            "note": "items absent from the file were not assessed by the authors; basis is a mechanical reading of the reason, checked by the author before use"}


def caliper(yaml_text):
    m = re.search(r"ground_truth_scores:\n\s+(\w+):\n((?:\s+\w+: \d\n?)+)", yaml_text)
    region = m.group(1)
    scores = dict(re.findall(r"(\w+): (\d)", m.group(2)))
    dims = {"input_ontology": "Input Ontology", "input_content": "Input Content", "input_form": "Input Form", "output_ontology": "Output Ontology", "output_content": "Output Content", "output_form": "Output Form"}
    judgments = [{"dimension": dims[k], "answer": v, "scope": "dimension score by domain experts; checklist items not scored individually"} for k, v in scores.items()]
    return {"benchmark": "helm", "framework": "CAL", "source": "github.com/aims-foundations/benchmark-caliper/benchmarks/helm.yaml, ground_truth_scores", "reviewers": "domain experts, as the repository states", "target_context": region, "judgments": judgments}


def ecbd(text):
    pages = re.split(r"=== PAGE \d+ ===\n", text)
    return {"benchmark": "helm", "framework": "ECBD", "source": "github.com/isle-dev/ECBD/filled_worksheets/[HELM] ECBD WorkSheet.pdf, text extracted with PDFKit", "reviewers": "Yu Lu Liu, Su Lin Blodgett, Ziang Xiao, as the worksheet states",
            "worksheet_text": [p.strip() for p in pages if p.strip()],
            "judgments": [{"item_id": f"ECBD-Q{n}", "answer": "", "basis": "", "note": "to be coded by the author from worksheet_text"} for n in range(1, 21)]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--betterbench")
    ap.add_argument("--abc")
    ap.add_argument("--caliper")
    ap.add_argument("--ecbd")
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if a.betterbench:
        html = Path(a.betterbench).read_text()
        for name, bench in [("HumanEval", "humaneval"), ("TruthfulQA", "truthfulqa")]:
            (OUT / f"BB-{bench}.json").write_text(json.dumps(betterbench(html, name, bench), indent=1, ensure_ascii=False) + "\n")
    if a.abc:
        (OUT / "ABC-tau-bench.json").write_text(json.dumps(abc(Path(a.abc).read_text()), indent=1) + "\n")
    if a.caliper:
        (OUT / "CAL-helm.json").write_text(json.dumps(caliper(Path(a.caliper).read_text()), indent=1) + "\n")
    if a.ecbd:
        (OUT / "ECBD-helm.json").write_text(json.dumps(ecbd(Path(a.ecbd).read_text()), indent=1, ensure_ascii=False) + "\n")
    for p in sorted(OUT.glob("*.json")):
        d = json.loads(p.read_text())
        print(p.name, len(d["judgments"]), "judgments")


if __name__ == "__main__":
    main()
