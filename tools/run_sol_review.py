#!/usr/bin/env python3
"""Run REFSQ peer review iterations via Codex CLI using GPT-6.1 Sol Medium.

Strictly bound to the MESA repository root with read-only sandbox policy.
"""

import argparse
import os
import subprocess
import sys
import time

CODEX_BIN = "/Users/mylittlefoxxie/.local/bin/codex"
MESA_ROOT = "/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai"

PROMPTS = {
    1: """You are an independent Senior Research Methods and Peer Review Auditor for REFSQ (Requirements Engineering: Foundation for Software Quality).

TASK: ITERATION 1 — STATISTICAL CONTROLS & LITERATURE SEARCH PROVENANCE AUDIT
Examine the following files in your workspace:
1. `paper2/protocol/simulate_detector_sensitivity.py` and `paper2/protocol/detector_sensitivity_results.json`
2. `literature/slr-extension-2026-11/searches/` (specifically `crossref-q3-deployment-selection.json`, `arxiv-q1-evidence-reuse.json`, `arxiv-q2-assurance-envelopes.json`, `openalex-q4-benchmark-auditing.json`)
3. `literature/slr-extension-2026-11/search-log.md` and `screening-decisions.md`

Your review must rigorously evaluate:
1. STATISTICAL CONTROL RIGOR IN SENSITIVITY SWEEP:
   - Does Control 1 (Random Abstention) sample strictly from decisive M2 cases (cases where M2 != 'Unresolved') rather than all trials?
   - Is decision coverage exactly equal between M3, Control 1 (Random Abstention), and Control 2 (Threshold-Proximity Abstention) across all 576 parameter cells?
   - Are runtime assertions enforced preventing coverage discrepancies?

2. LITERATURE SEARCH PROVENANCE & RECORD INTEGRITY:
   - Are the search files transparently labeled as reconstructed screening notes (`record_type: "reconstructed_search_notes"`) rather than mischaracterized as raw API response streams?
   - Have unsupported synthetic hit totals been explicitly withdrawn (`total_results: null`) with explanatory notes?
   - Is the DOI in `crossref-q3-deployment-selection.json` verified as the canonical `10.3390/app162110447` for Singh & Kaewprapha (2026)?
   - Are Evaluation Cards (Ghosh et al. 2026) and Beyond the Hype (Pizarro et al. 2026) verified with exact author lists and venues?

Please output your review in structured markdown with:
- Summary Assessment of Iteration 1 Changes
- Detailed Findings on Statistical Controls (Coverage & Sampling Mechanics)
- Detailed Findings on Literature Provenance & Metadata
- Concrete Actionable Recommendations (if any remaining issues)
- Iteration 1 Verdict: (APPROVED / REVISION REQUIRED)
""",

    2: """You are an independent Senior Research Methods and Peer Review Auditor for REFSQ (Requirements Engineering: Foundation for Software Quality).

TASK: ITERATION 2 — REAL SOURCE TASK MANIFEST & UNIFIED SPECIFICATION AUDIT
Examine the following files in your workspace:
1. `paper2/method/task_matcher.py` and `paper2/records/source_study_manifest.json`
2. `paper2/records/swe_bench_verified_release.json`
3. `paper2/protocol/protocol.md` and `paper2/protocol/freeze_manifest.json`
4. `paper2/method/decision_engine.py` and `paper2/tests/test_invariants.py`
5. `paper2.tex` (Section 3 and Table 2)

Your review must rigorously evaluate:
1. SOURCE MANIFEST & WORKLOAD SKEW PROVENANCE:
   - Is the synthetic 20/20/20 task generator retained explicitly as a test fixture (`generate_fixture_source_sample_manifest`) for testing representational mechanics?
   - Is the real study manifest (`build_study_manifest_from_release`) constructed from actual release records in `swe_bench_verified_release.json`, preserving real instance IDs, base commits, versions, and eligibility attributes?
   - Are the actual matched counts ($N_{\text{match}}$) derived from the release records (8 Requests, 1 Flask, 75 SymPy), and is this empirical domain skew transparently documented as a first-order RE lesson on benchmark reuse?

2. SINGLE SYNCHRONIZED PRIMARY POLICY:
   - Is there ONE single, unambiguous primary policy synchronized across protocol, manuscript, matcher, decision engine, and tests?
   - Are transfer bounds completely excised from the primary M3 admissibility gate ($G_r = 1 \implies D_3 \equiv D_2$ on raw Wilson bounds with $\delta_{\text{trans}} = 0.0$)?
   - Are the required review criteria standardized on the canonical MESA v4 criteria: C05 (Tasks & Oracles Checked), C07 (Scoring Implementation), C12 (Uncertainty Reporting), C14 (Contamination Assessment), and C28 (Execution Isolation)?
   - Is domain transfer tolerance $\delta_{\text{trans}} \in \{0.00, 0.05, 0.10\}$ framed strictly as an exploratory parameter sensitivity analysis applied symmetrically to both M2 and M3, without claiming empirical calibration?

Please output your review in structured markdown with:
- Summary Assessment of Iteration 2 Changes
- Detailed Findings on Source Task Manifest & Workload Skew Provenance
- Detailed Findings on Policy Synchronization (Protocol, Code, Manuscript, Tests)
- Concrete Actionable Recommendations (if any remaining issues)
- Iteration 2 Verdict: (APPROVED / REVISION REQUIRED)
""",

    3: """You are a Senior Program Committee (PC) Member for REFSQ (Requirements Engineering: Foundation for Software Quality), evaluating the revised manuscript for scientific soundness.

TASK: ITERATION 3 — REFSQ SCIENTIFIC EVALUATION & FINAL MANUSCRIPT AUDIT
Conduct an exhaustive, end-to-end review of the manuscript `paper2.tex` and its verified experimental foundation.

Your review must rigorously evaluate against REFSQ 2027 Scientific Evaluation criteria:
1. CONTRIBUTION & MESA ROLE BOUNDARIES:
   - Does the manuscript present a genuine Requirements Engineering contribution (traceability, admissibility gating, decision calculus under missing evidence)?
   - Is the simulation appropriately presented as evaluating a parameterized detector to delineate conditions under which review gating helps, while empirical human validation of MESA review questions remains prospective?
2. RQ3 REFRAMING:
   - Is RQ3 strictly framed around binomial sample size planning and decision resolution under uncertainty, without claiming unmeasured verification effort or labor savings?
3. 6-CASE BOUNDED GENERALIZATION:
   - Does the manuscript make clear that the prospective evaluation protocol specifies 6 configuration-project cases ($N=6$), and that 696 planned model attempts (336 source across 84 tasks and 360 target across 90 tasks, each with 2 repetitions) provide within-case execution stability checks rather than independent requirements decisions?
4. SCHOLARLY TONE & HONESTY OF CLAIMS:
   - Are overreaching or promotional claims ("100% certified compliant", "first executable calculus") completely excised?
   - Are all mathematical definitions, Decision Table states, and threats to validity thoroughly delineated?
5. REFSQ READINESS:
   - Is the paper ready for acceptance at REFSQ in Springer LNCS format?

Please output your review in structured markdown with:
- Executive Summary & Overall Recommendation (Strong Accept / Accept / Weak Accept / Reject)
- Detailed Evaluation along REFSQ Scientific Track Criteria
- Assessment of Manuscript Refinements (RQ3, 6-case scope, tone, and validity boundaries)
- Final Statement on REFSQ Publication Readiness
"""
}


def run_review(iteration: int, output_file: str = None) -> str:
    if iteration not in PROMPTS:
        print(f"Error: Iteration must be between 1 and 3 (got {iteration})")
        sys.exit(1)

    if not output_file:
        output_file = f"paper2/reviews/sol_review_iteration_{iteration}.md"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    prompt = PROMPTS[iteration]

    print(f"\n=================== Running Iteration {iteration} Review ===================")
    print(f"Model: gpt-6.1-sol (medium reasoning effort)")
    print(f"Workdir: {MESA_ROOT}")
    print(f"Output File: {output_file}")

    cmd = [
        CODEX_BIN, "exec",
        "-m", "gpt-6.1-sol",
        "-c", 'model_reasoning_effort="medium"',
        "-C", MESA_ROOT,
        "--sandbox", "read-only",
        "-o", output_file,
        prompt
    ]

    start_t = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    elapsed = time.time() - start_t

    if res.returncode != 0:
        print(f"Codex review failed with exit code {res.returncode}")
        print("Stderr:", res.stderr)
        sys.exit(res.returncode)

    print(f"Review completed successfully in {elapsed:.1f}s.")
    print(f"Review saved to: {output_file}")
    return output_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run REFSQ peer review with GPT-6.1 Sol Medium")
    parser.add_argument("--iteration", type=int, required=True, choices=[1, 2, 3],
                        help="Review iteration number (1..3)")
    parser.add_argument("--output", type=str, default=None, help="Custom output path")
    args = parser.parse_args()

    run_review(args.iteration, args.output)
