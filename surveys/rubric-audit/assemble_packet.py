#!/usr/bin/env python3
"""Assemble the HumanEval MESA rubric audit packet from v4 study materials and outputs."""
import csv
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
V4_STUDY = ROOT / "v4" / "study"
AUDIT_DIR = Path(__file__).resolve().parent

def load_json(p):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    rubric = load_json(V4_STUDY / "materials" / "rubric.json")
    resp = load_json(V4_STUDY / "outputs" / "humaneval-RUBRIC-1" / "attempt-1" / "response.txt")
    
    # Copy paper.pdf to audit directory if present
    pdf_source = V4_STUDY / "sources" / "humaneval" / "paper.pdf"
    if pdf_source.exists():
        shutil.copy(pdf_source, AUDIT_DIR / "paper.pdf")
        print(f"Copied {pdf_source} to {AUDIT_DIR / 'paper.pdf'}")

    # Load definitions from colleague-review packet
    colleague_packet = load_json(ROOT / "surveys" / "colleague-review" / "packet.json")
    definitions = list(colleague_packet.get("definitions", []))

    # Add code-benchmark & HumanEval specific terms
    code_terms = [
        {
            "term": "pass@k",
            "aliases": ["pass@k", "pass@1", "pass@10", "pass@100"],
            "label": "pass@k",
            "definition": "An unbiased evaluation metric estimating the probability that at least one of k generated code samples per problem passes all functional unit tests."
        },
        {
            "term": "Sandboxing",
            "aliases": ["sandbox", "sandboxed", "sandboxing", "container isolation"],
            "label": "Sandboxing",
            "definition": "Executing untrusted AI-generated code in a restricted, isolated virtual environment to prevent filesystem, process, or network access to the host machine."
        },
        {
            "term": "gVisor",
            "aliases": ["gvisor", "gvisor container", "container runtime"],
            "label": "gVisor",
            "definition": "An open-source application kernel and secure container runtime developed by Google that isolates untrusted code execution from the host kernel."
        },
        {
            "term": "Reliability Guard",
            "aliases": ["reliability guard", "reliability_guard", "safety guard"],
            "label": "Reliability Guard",
            "definition": "A lightweight Python context manager in HumanEval that sets resource limits (CPU time, memory) and blocks dangerous OS calls, but is explicitly NOT a security sandbox."
        },
        {
            "term": "Estimator Variance",
            "aliases": ["variance", "estimator variance", "sampling variance"],
            "label": "Estimator Variance",
            "definition": "The statistical variation in benchmark pass rates resulting from finite sample sizes or temperature sampling rather than true underlying model capability."
        },
        {
            "term": "Unbiased Estimator",
            "aliases": ["unbiased estimator", "unbiased"],
            "label": "Unbiased Estimator",
            "definition": "A mathematical formula whose expected value equals the true capability parameter without systematically over- or under-estimating performance."
        }
    ]
    for ct in code_terms:
        if not any(d.get("label") == ct["label"] or d.get("term") == ct["term"] for d in definitions):
            definitions.append(ct)

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

    # Part A plain-language metadata
    part_a_meta = {
        "Purpose": {
            "title": "Benchmark Purpose",
            "plain_question": "What is the primary purpose of HumanEval (research, conformity, or other)?",
            "hint": "Identifies whether the benchmark is intended for research exploration or strict production compliance."
        },
        "Judgeability": {
            "title": "Scoring Mode (Test Oracle)",
            "plain_question": "How are generated code solutions marked (automated execution, human grading, or mixed)?",
            "hint": "HumanEval executes Python programs automatically. Because scoring is automated, Question B07 will ask you to audit the execution harness for safety and anti-gaming protection."
        },
        "Reference": {
            "title": "Reference Norm (Score Comparison)",
            "plain_question": "Are scores evaluated against absolute pass/fail standards or relative model rankings?",
            "hint": "HumanEval computes absolute pass@k correctness scores. Question B09 will check whether baseline model comparisons are justified."
        },
        "Containedness": {
            "title": "Environment Isolation (Sandboxing)",
            "plain_question": "Is candidate code executed inside a secure, hermetic sandbox or directly on the host machine?",
            "hint": "Checks whether running candidate AI-generated code could harm the host system or access network resources."
        },
        "Objectivity": {
            "title": "Test Objectivity & Prompt Independence",
            "plain_question": "Are test problems fixed and standardized across all models, or customized per prompt?",
            "hint": "Checks whether all evaluated models receive the exact same prompts and docstrings without prompt engineering bias."
        },
        "Autonomy": {
            "title": "Interaction Paradigm",
            "plain_question": "Does the benchmark evaluate stateless single-turn code generation or multi-turn agentic loops?",
            "hint": "HumanEval measures single-turn docstring-to-code completion where the model produces the function body in one shot."
        },
        "Progression": {
            "title": "Fixture Adaptivity",
            "plain_question": "Are test fixtures static for all models or do problem difficulties adapt dynamically?",
            "hint": "Checks whether problem difficulty is static or if the test suite adapts based on previous model answers."
        },
        "Variation": {
            "title": "Test Stability & Release Versioning",
            "plain_question": "Are benchmark problems fixed across releases or procedurally generated / refreshed?",
            "hint": "HumanEval problems are fixed in the repository. Question B20 will examine versioning and release maintenance."
        }
    }

    # Assemble Part A
    part_a = []
    agent_desc = {d["facet"]: d for d in resp["description"]}
    for f in rubric["part_a"]:
        facet_name = f["facet"]
        a_data = agent_desc.get(facet_name, {})
        meta = part_a_meta.get(facet_name, {
            "title": facet_name,
            "plain_question": f"What is the {facet_name} profile of HumanEval?",
            "hint": ""
        })
        part_a.append({
            "facet": facet_name,
            "title": meta["title"],
            "plain_question": meta["plain_question"],
            "hint": meta["hint"],
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

    # Standardized 4 Opening Familiarity items
    familiarity = [
        {
            "id": "ai",
            "question": "How familiar are you with artificial intelligence (AI)?",
            "help": "Think about your experience using or learning about AI tools and models. This is your own background description, not a test.",
            "labels": [
                "1 — Not familiar: Little or no experience with AI tools.",
                "2 — Slightly familiar: Have heard about or tried basic AI tools.",
                "3 — Moderately familiar: Use AI occasionally; understand basic purpose.",
                "4 — Familiar: Use AI regularly; understand common capabilities and limits.",
                "5 — Very familiar: Work with AI regularly; understand inner workings and failure modes."
            ]
        },
        {
            "id": "benchmarks",
            "question": "How familiar are you with AI benchmarks?",
            "help": "An AI benchmark is a standardized test suite used to evaluate and compare AI models.",
            "labels": [
                "1 — Not familiar: Had not heard of AI benchmarks before.",
                "2 — Slightly familiar: Have heard the term but could not explain how benchmarks work.",
                "3 — Moderately familiar: Know benchmarks test models on problem sets and give scores.",
                "4 — Familiar: Understand how benchmark tasks and metrics (e.g. pass@1) are used.",
                "5 — Very familiar: Regularly use or design benchmarks; know what scores can and cannot prove."
            ]
        },
        {
            "id": "python",
            "question": "How familiar are you with reading Python code?",
            "help": "HumanEval evaluates models by executing Python code with unit tests. Rate your comfort reading Python scripts.",
            "labels": [
                "1 — Not familiar: Little or no experience reading Python code.",
                "2 — Slightly familiar: Can recognize basic syntax but need help reading scripts.",
                "3 — Moderately familiar: Can read Python functions, loops, and basic scripts.",
                "4 — Familiar: Regularly read/write Python; understand unit tests and imports.",
                "5 — Very familiar: Fluent in Python; comfortable auditing test harnesses and execution calls."
            ]
        },
        {
            "id": "scores",
            "question": "How familiar are you with interpreting AI benchmark scores?",
            "help": "Interpreting benchmark scores means deciding what a score proves and whether two models can be compared fairly.",
            "labels": [
                "1 — Not familiar: Little experience interpreting scores; would need guidance.",
                "2 — Slightly familiar: Understand basic accuracy scores but need help comparing models.",
                "3 — Moderately familiar: Can explain basic scores and recognize common limitations.",
                "4 — Familiar: Can compare model results, check sample sizes, and spot important caveats.",
                "5 — Very familiar: Can evaluate whether a model comparison is fair, robust, and statistically sound."
            ]
        }
    ]

    packet = {
        "audit_id": "mesa-v4-humaneval-audit-v1",
        "title": "MESA Benchmark Review Audit & Verification Platform",
        "subtitle": "Human Software Engineering Audit of Claude Sonnet 5.5's Review of HumanEval",
        "version": "1.1",
        "benchmark": {
            "id": "humaneval",
            "name": "HumanEval",
            "commit": "b9453e8f18",
            "paper_title": "Evaluating Large Language Models Trained on Code (Chen et al., 2021)",
            "paper_pdf": "paper.pdf",
            "overview": "OpenAI's benchmark of 164 hand-crafted Python programming problems with docstrings and unit tests, created to measure the functional correctness of code generation models using pass@k.",
            "what_is_a_benchmark": "An AI benchmark is a standardized test suite used by researchers and software engineering teams to evaluate how well an AI model performs specific tasks (such as writing software, answering questions, or reasoning). Benchmark scores are widely cited on leaderboards to compare models.",
            "humaneval_primer": "HumanEval is an influential code-generation benchmark released by OpenAI in 2021 for the Codex model (the foundation of GitHub Copilot). It contains 164 original Python coding problems. Each problem provides a function signature with a docstring prompt and hidden unit test assertions. Candidate models generate Python code to complete the function body. HumanEval then executes the completed program locally and checks whether all unit tests pass (pass@1).",
            "sample_problem": {
                "prompt": "def has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.9], 0.3)\n    False\n    >>> has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8)\n    True\n    \"\"\"",
                "test": "check(has_close_elements)  # asserts whether all test cases pass",
                "execution": "exec(check_program, exec_globals)  # in human_eval/execution.py"
            },
            "scope": "Python docstring-to-function code synthesis, language comprehension, reasoning, algorithms, and simple mathematics.",
            "intended_use": "Evaluating functional correctness of code generation models using pass@k (unbiased estimator).",
            "paper_text": paper_text,
            "repo_files": repo_files
        },
        "familiarity": familiarity,
        "definitions": definitions,
        "part_a": part_a,
        "part_b": part_b,
        "verdict_options": [
            {
                "value": "supported",
                "label": "Confirmed / Supported",
                "desc": "The cited quote is accurate and fully supports the assigned evidence level."
            },
            {
                "value": "weaker",
                "label": "Overstated / Weaker",
                "desc": "The evidence supports only a lower level (e.g. Stated instead of Shown, or Shown instead of Checked)."
            },
            {
                "value": "absence_plausible",
                "label": "Absence Plausible",
                "desc": "The benchmark documentation genuinely lacks this information as claimed."
            },
            {
                "value": "contradicted",
                "label": "Contradicted / Defect Found",
                "desc": "The sources contradict the rating or reveal an active flaw/vulnerability."
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
                "question": "How clear were the review questions and evidence level distinctions?",
                "labels": ["1 Very unclear", "2 Mostly unclear", "3 Moderately clear", "4 Mostly clear", "5 Very clear", "Cannot judge"]
            },
            {
                "id": "audit_ease",
                "question": "How easy was it to evaluate the agent's cited quotes against the benchmark sources?",
                "labels": ["1 Very difficult", "2 Difficult", "3 Moderate", "4 Easy", "5 Very easy", "Cannot judge"]
            },
            {
                "id": "workload",
                "question": "How manageable was the audit workload and review speed?",
                "labels": ["1 Very unmanageable", "2 Unmanageable", "3 Moderate", "4 Manageable", "5 Very manageable", "Cannot judge"]
            },
            {
                "id": "audit_confidence",
                "question": "How confident do you feel in the accuracy of your final verified review of this benchmark?",
                "labels": ["1 Not confident", "2 Slightly confident", "3 Moderately confident", "4 Confident", "5 Very confident", "Cannot judge"]
            },
            {
                "id": "pairing_utility",
                "question": "How would you rate the experience of auditing pre-extracted agent evidence cards versus reading the paper and code from scratch?",
                "labels": ["Substantially slower / worse", "Slightly worse", "About the same", "Noticeably faster / better", "Substantially better", "Cannot judge"]
            }
        ]
    }

    out_p = AUDIT_DIR / "packet.json"
    out_p.write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(part_a)} Part A items, {len(part_b)} Part B items, {len(definitions)} definitions, and {len(repo_files)} repo files to {out_p} ({out_p.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
