# Screening Decisions: SLR Extension 2026-11

**Document ID:** `slr-extension-screening-2026-11`  
**Date:** November 2026 (Reconstructed & Verified 05 November 2026)  
**Status:** Reconstructed Candidate Screening Register (16 Confirmed Publications: 15 Included, 1 Excluded; plus 3 Disambiguation Notes)  

---

## 1. Screening Criteria

### Core Inclusion Criteria (Targeted SLR Extension):
- **Inclusion Criterion 1 (Methodological Relevance):** Proposes a formal, algorithmic, or structural method for evaluating, reusing, or bounding AI evidence, safety cases, or benchmark evaluations.
- **Inclusion Criterion 2 (Requirements or Benchmark Focus):** Connects evidence directly to system requirements, operational domain specifications, software change obligations, or benchmark construct validity.

### Exclusion Criteria:
- **Exclusion Criterion 1 (Internal-Only Static Verification):** Static code analysis or internal unit test generation without AI component evaluation or evidence reuse.
- **Exclusion Criterion 2 (Domain Misalignment):** Focuses on runtime cyber-physical dynamic monitors (e.g., autonomous vehicle perception), rather than evidence qualification for coding agents or software change obligations.
- **Exclusion Criterion 3 (Lack of Operational Calculus / Task Benchmark Only):** Evaluates benchmark task suites or reporting layers lacking an operational decision calculus, statistical confidence bounds, or executable release gates.

### Baseline Foundation Inclusion Rule:
Five foundational baseline records from the parent SLR (`slr-2026-10-28`) are retained in the comparative matrix to anchor foundational paradigms in ML safety (AMLAS), modular contracts (Sljivo), change impact (Lawford), institutional guidelines (NIST), and empirical SE LLM adoption context (Hou et al. survey).

---

## 2. Confirmed Inspected Publications (16 Records)

| Candidate Record | Target Domain | Screening Verdict | Primary Reason & Evidence Location |
|---|---|---|---|
| **Mukhopadhyay & Nalla** (arXiv:2610.27672, 2026) | Reusing Assurance Evidence in AI Pipelines | **INCLUDED** (EXT-06) | Implements fail-closed release gate with Ed25519 signatures and evaluates on 714 DVC pipelines (§3–5). |
| **Goswami** (arXiv:2609.16302, 2026) | Assurance Envelopes for Coding Agents | **INCLUDED** (EXT-07) | Formulates minimum-cost evidence selection over typed inference graphs with CP-SAT solver (§3–4). |
| **Singh & Kaewprapha** (Applied Sciences 16(21):10447, 2026) | DAMSA / System-Aware Model Selection (SMS) | **INCLUDED** (EXT-11) | Three-layer post-training model selection architecture with DAMSA Pareto screening for operational deployment (DOI: 10.3390/app162110447, §3–4). |
| **Fei Ding** (arXiv:2610.30635, 2026) | What the Specification Did Not Say: Specification-Oracle Gaps | **INCLUDED** (EXT-09) | Identifies over-constrained hidden testcases causing false failures on HumanEval/SWE-bench (§3, §5). |
| **Liu et al.** (ACL 2024) | ECBD: Evidence-Centered Benchmark Design | **INCLUDED** (EXT-12) | 20-question construct validity design worksheet for NLP benchmarks (DOI: 10.18653/v1/2024.acl-long.872, Appendix A). |
| **Reuel et al.** (NeurIPS 2024 / arXiv:2411.12990) | BetterBench: Assessing AI Benchmarks | **INCLUDED** (EXT-13) | Multi-attribute quality scoring across 15 benchmark dimensions (§3–5). |
| **Ghosh et al.** (arXiv:2606.09809v2, 2026) | Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting | **INCLUDED** (EXT-14) | Standardized reporting schemas isolating documentation gaps for stakeholders (48 co-authors, §2–3). |
| **Pizarro et al.** (Science of Computer Programming 254:103530, 2026) | Beyond the Hype: Enabling Informed LLM Adoption in Industry | **INCLUDED** (EXT-15) | Epistemological and systematic evaluation of benchmark limits for industry adoption (DOI: 10.1016/j.scico.2026.103530, §3–4). |
| **Sljivo et al.** (SAFECOMP 2014) | Assurance Contracts for Component Systems | **INCLUDED** (EXT-02) | Modular safety case composition via assumption-guarantee contracts (DOI: 10.1007/978-3-319-10506-2_12, §4). |
| **Picardi et al.** (SafeAI 2023) | Transfer Assurance | **INCLUDED** (EXT-04) | Statistical divergence bounds for transferring safety cases across perceptual domains (CEUR 3381, §2). |
| **Hawkins et al.** (2021) | AMLAS | **INCLUDED** (EXT-01; Baseline Foundation) | Foundational safety assurance process for ML components in autonomous systems (§3.2). |
| **Lawford et al.** (SAFECOMP 2024 / 2017) | Safety Case Impact Assessment | **INCLUDED** (EXT-03; Baseline Foundation) | Foundational traceability graph traversal identifying safety arguments invalidated by code changes (DOI: 10.1007/978-3-031-70068-2_5, §3). |
| **Arief et al.** (arXiv:2607.17686, 2026) | VNVSpec | **INCLUDED** (EXT-05; Baseline Foundation) | Foundational machine-readable DSL compiling specifications into executable test harnesses (§3). |
| **NIST AI 800-2** (NIST 2026) | Automated Benchmark Evaluations of LLMs | **INCLUDED** (EXT-08; Baseline Foundation) | Foundational institutional guidance on benchmark quality, contamination, and reporting (§4). |
| **Hou et al.** (TOSEM 2024) | Large Language Models for Software Engineering | **INCLUDED** (EXT-10; Baseline Foundation) | Foundational survey scoping LLM capabilities and empirical benchmarks in software engineering (DOI: 10.1145/3643777, §5). |
| *Jian Yang et al.* (arXiv:2507.22462, 2025) | IFEvalCode: Controlled Code Generation | **EXCLUDED** from comparative matrix | Excluded under Criterion 3: evaluates instruction-following benchmark artifact; lacks a requirements engineering evidence qualification calculus. |

---

## 3. Historical Attribution Disambiguation Records (Unverified Candidate Notes)

These three entries represent historical disambiguation notes generated during earlier review iterations to clarify author attribution errors. They are preserved for provenance transparency but are excluded from confirmed screened publications:
1. *Habli et al. (2024)*: Concept note on epistemic ML justification, disambiguated from the empirical pipeline implementation of Mukhopadhyay & Nalla (2026).
2. *Burton et al. (2022)*: Concept note on runtime vehicle safety monitors, disambiguated from the coding agent software change envelopes of Goswami (2026).
3. *Troubitsyna et al. (2024)*: Concept note on dynamic assurance mapping, disambiguated from the deployment-aware model selection architecture of Singh & Kaewprapha (2026).
