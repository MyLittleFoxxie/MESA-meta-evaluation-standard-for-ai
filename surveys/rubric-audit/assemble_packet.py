#!/usr/bin/env python3
"""Assemble the HumanEval MESA rubric audit packet from v4 study materials and outputs."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
V4_STUDY = ROOT / "v4" / "study"
AUDIT_DIR = Path(__file__).resolve().parent

def load_json(p):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    rubric = load_json(V4_STUDY / "materials" / "rubric.json")
    resp = load_json(V4_STUDY / "outputs" / "humaneval-RUBRIC-1" / "attempt-1" / "response.txt")
    
    # Load reference source-check notes
    ref_checks = {}
    with open(V4_STUDY / "analysis" / "source-check.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["benchmark"] == "humaneval" and r["repeat"] == "1":
                ref_checks[(r["part"], r["item_id"])] = {
                    "verdict": r["verdict"],
                    "note": r["note"]
                }

    # Load HumanEval sources
    source_dir = V4_STUDY / "sources" / "humaneval"
    paper_text = (source_dir / "paper.txt").read_text(encoding="utf-8")
    repo_dir = source_dir / "repository"
    
    repo_files = {}
    for p in sorted(repo_dir.rglob("*")):
        if p.is_file() and not p.name.endswith(".gz") and not p.name.endswith(".pyc"):
            rel_path = str(p.relative_to(repo_dir))
            try:
                repo_files[rel_path] = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                pass

    # Assemble Part A
    part_a = []
    agent_desc = {d["facet"]: d for d in resp["description"]}
    for f in rubric["part_a"]:
        facet_name = f["facet"]
        a_data = agent_desc.get(facet_name, {})
        part_a.append({
            "facet": facet_name,
            "values": f["values"],
            "decides": f["decides"],
            "agent": {
                "value": a_data.get("value"),
                "reason": a_data.get("reason"),
                "evidence": a_data.get("evidence", [])
            },
            "reference": ref_checks.get(("A", facet_name), {})
        })

    # Assemble Part B
    part_b = []
    agent_judg = {j["item_id"]: j for j in resp["judgments"]}
    for q in rubric["part_b"]:
        qid = q["id"]
        j_data = agent_judg.get(qid, {})
        part_b.append({
            "id": qid,
            "question": q["question"],
            "shown": q["shown"],
            "checked": q["checked"],
            "applies_when": q["applies_when"],
            "source_items": q["source_items"],
            "agent": {
                "answer": j_data.get("answer"),
                "basis": j_data.get("basis"),
                "reason": j_data.get("reason"),
                "missing": j_data.get("missing", ""),
                "checks": j_data.get("checks", ""),
                "evidence": j_data.get("evidence", [])
            },
            "reference": ref_checks.get(("B", qid), {})
        })

    packet = {
        "audit_id": "mesa-v4-humaneval-audit-v1",
        "title": "MESA Benchmark Review Audit & Verification Platform",
        "subtitle": "Human Software Engineering Audit of Claude Sonnet 5.5's Review of HumanEval",
        "version": "1.0",
        "benchmark": {
            "id": "humaneval",
            "name": "HumanEval",
            "commit": "b9453e8f18",
            "overview": "Evaluation set of 164 original programming problems with docstrings and unit tests released by OpenAI to measure the functional correctness of Python code synthesis from docstrings.",
            "scope": "Python docstring-to-function code synthesis, language comprehension, reasoning, algorithms, and simple mathematics.",
            "intended_use": "Evaluating functional correctness of code generation models using pass@k (unbiased estimator).",
            "paper_text": paper_text,
            "repo_files": repo_files
        },
        "part_a": part_a,
        "part_b": part_b,
        "verdict_options": [
            {
                "value": "supported",
                "label": "Confirmed / Supported",
                "desc": "The cited quote is accurate and fully supports the assigned anchor."
            },
            {
                "value": "weaker",
                "label": "Overstated / Weaker",
                "desc": "The evidence supports only a lower anchor (e.g. Stated instead of Shown, or Shown instead of Checked)."
            },
            {
                "value": "absence_plausible",
                "label": "Absence Plausible",
                "desc": "The benchmark documentation lacks this information as claimed."
            },
            {
                "value": "contradicted",
                "label": "Contradicted / Defect Found",
                "desc": "The sources contradict the rating or demonstrate a flaw/defect."
            },
            {
                "value": "cannot_judge",
                "label": "Cannot Judge",
                "desc": "The provided excerpt is insufficient to determine the verdict."
            }
        ],
        "feedback": [
            {
                "id": "clarity",
                "question": "How clear were the rubric questions and anchor distinctions?",
                "labels": ["1 Very unclear", "2 Mostly unclear", "3 Moderately clear", "4 Mostly clear", "5 Very clear", "Cannot judge"]
            },
            {
                "id": "audit_ease",
                "question": "How easy was it to evaluate the agent's cited quotes against the benchmark sources?",
                "labels": ["1 Very difficult", "2 Difficult", "3 Moderate", "4 Easy", "5 Very easy", "Cannot judge"]
            },
            {
                "id": "workload",
                "question": "How manageable was the reading and verification workload?",
                "labels": ["1 Unmanageable", "2 Heavy", "3 Manageable", "4 Low effort", "5 Minimal effort", "Cannot judge"]
            },
            {
                "id": "confidence",
                "question": "How confident do you feel in this final verified benchmark review?",
                "labels": ["1 Not at all confident", "2 Slightly confident", "3 Moderately confident", "4 Confident", "5 Highly confident", "Cannot judge"]
            },
            {
                "id": "pairing_value",
                "question": "How useful was starting from the agent's extracted evidence compared to auditing from scratch?",
                "labels": ["1 Much worse than scratch", "2 Slightly worse", "3 About the same", "4 Noticeably faster/better", "5 Substantially better", "Cannot judge"]
            }
        ],
        "definitions": [
            {
                "term": "pass@k",
                "definition": "An unbiased metric for functional correctness: generating n samples per problem and estimating the probability that at least one of k generated samples passes all unit tests."
            },
            {
                "term": "Functional Correctness",
                "definition": "Evaluating code synthesis by whether generated code successfully passes test cases, rather than comparing surface tokens via BLEU or match metrics."
            },
            {
                "term": "Reliability Guard",
                "definition": "A Python context manager in human_eval/execution.py that limits execution time and memory and disables dangerous system calls, but is explicitly NOT a secure sandbox."
            },
            {
                "term": "Unbiased Estimator",
                "definition": "A statistical estimator whose expected value equals the true parameter; Codex uses an unbiased estimator to compute pass@k from n samples without evaluating all combinations."
            },
            {
                "term": "Contamination",
                "definition": "The inclusion of benchmark test problems and test cases in the training data of evaluated models, leading to memorized solutions rather than genuine synthesis."
            },
            {
                "term": "Gating Facet",
                "definition": "A descriptive design attribute from Part A (e.g. Judgeability, Variation) that formally determines whether a specific Part B evaluation question is applicable."
            }
        ]
    }

    out_file = AUDIT_DIR / "packet.json"
    out_file.write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Successfully assembled {out_file} ({out_file.stat().st_size:,} bytes)")
    print(f"Part A facets: {len(part_a)}, Part B questions: {len(part_b)}")
    print(f"Repo files embedded: {list(repo_files.keys())}")

if __name__ == "__main__":
    main()
