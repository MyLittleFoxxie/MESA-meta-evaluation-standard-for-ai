# Literature Review and Research Delineation Report

**Document ID:** `paper2-slr-gap-01`  
**Target Submission:** REFSQ Scientific Evaluation Paper  
**Status:** Verification Complete — Scoped Research Gap Delineated  
**Scope:** Verification of Related Work, Primary Source Evidence, and Methodological Delineation  

---

## 1. Executive Summary

This report establishes the delineation between **Paper 2 ("Using AI Benchmark Results as Requirements Evidence")** and related literature across Requirements Engineering (RE) and AI System Assurance.

### The Problem
When engineering organizations evaluate third-party foundation models and coding agents, they frequently cite public benchmark leaderboard scores (such as SWE-bench pass rates) as verification evidence to satisfy software capability requirements. However:
1. **Raw benchmark scores** pool heterogeneous tasks that may not match target repository constraints, execution limits, or programming idioms.
2. **Task matching alone** filters by repository tags but does not examine whether the underlying benchmark evaluation harness is robust against test oracle gaps or data contamination.
3. Prior software engineering and AI assurance frameworks either assume evidence is generated internally from scratch, or treat third-party benchmark metrics as unexamined inputs.

### The Delineated Research Problem
Existing literature does not examine:
1. A formal method for deciding whether external AI benchmark evidence supports a specific system requirement for a coding assistant, contradicts it, or leaves it unresolved under statistical confidence bounds;
2. An empirical evaluation testing whether incorporating meta-evaluation findings (specifically Kane's scoring inference checks) withholds decisions on flawed or missing evidence compared with aggregate scores or task matching alone;
3. A prospective study protocol measuring decision concordance against execution outcomes on target repository tasks.

---

## 2. Primary Source Inspection & Section-Level Evidence

To ensure the gap is authentic, we inspected the full texts of foundational frameworks across safety assurance, evidence reuse, machine-readable specifications, and benchmark auditing, recording page and section evidence:

### 2.1 AMLAS (Hawkins et al., 2021)
- **Source:** *Guidance on the Assurance of Machine Learning in Autonomous Systems (AMLAS)*, arXiv:2102.01564, 2021.
- **Section Evidence:**
  - Section 2 ("AMLAS Methodology Overview", pp. 5–8): Defines a six-stage lifecycle: (1) ML Safety Requirements, (2) Data Requirements, (3) Data Verification, (4) Model Learning, (5) Model Verification, and (6) Model Deployment.
  - Section 6 ("Model Verification", pp. 28–35): Explicitly assumes that verification test data are sampled directly from the operational design domain (ODD) specified in Stage 2.
- **Why It Does Not Cover Our Problem:**
  AMLAS provides a process for teams developing their own ML models in-house. It does not address *reusing third-party external benchmarks* where the engineering team has no control over the test generation process. It lacks a mathematical calculus for mapping external benchmark tasks to repository requirements or deciding evidence admissibility under incomplete documentation.

### 2.2 Assurance Contracts (Sljivo et al., 2014; Kelly, 1998)
- **Source:** *Generation of Safety Case Argument-Fragments from Safety Contracts*, SAFECOMP 2014, LNCS 8666, pp. 170–185.
- **Section Evidence:**
  - Section 3 ("Safety Contracts", pp. 173–175): Defines contracts as pairs of $(A, G)$ where assumptions $A$ must be satisfied by environment guarantees to ensure component guarantee $G$.
  - Section 4 ("Argument-Fragment Generation", pp. 176–181): Generates GSN trees connecting contract assumptions to component claims.
- **Why It Does Not Cover Our Problem:**
  Assurance contracts operate on deterministic architectural components with explicit formal interfaces. They assume evidence validity is binary and verified by construction. They provide no mechanism for handling statistical uncertainty (Wilson intervals) or empirical validity deficits in probabilistic LLM benchmarks.

### 2.3 Automotive Safety Case Impact Assessment (Kokaly et al., 2017)
- **Source:** *Safety Case Impact Assessment in Automotive Software Systems: An Improved Model Based Approach*, SAFECOMP 2017, pp. 69–85.
- **Section Evidence:**
  - Section 2 ("Background: Safety Cases and Change", pp. 71–74): Examines how software modifications affect existing safety case arguments in automotive systems.
  - Section 4 ("Change Impact Process", pp. 77–81): Traverses GSN dependency graphs to flag arguments invalidated by modified code modules.
- **Why It Does Not Cover Our Problem:**
  Kokaly et al. address *maintenance and re-assurance after change in automotive systems*. Our work addresses the prior, orthogonal problem: *initial evidence qualification and link justification* when selecting a third-party model. Furthermore, our study explicitly keeps change impact outside the primary experiment.

### 2.4 Transfer Assurance (Picardi et al., 2023)
- **Source:** *Transfer Assurance for Machine Learning in Autonomous Systems*, SafeAI @ AAAI 2023, CEUR-WS Vol-3381.
- **Section Evidence:**
  - Section 2 ("Problem Formulation", pp. 2–3): Formalizes the problem of updating an assurance argument when an autonomous vehicle moves from source domain $D_S$ to target domain $D_T$.
  - Section 3 ("Transfer Strategy", pp. 4–6): Proposes distance metrics between operational environments to determine which safety claims remain valid.
- **Why It Does Not Cover Our Problem:**
  Transfer assurance focuses on perceptual and environmental shift in robotics and cyber-physical systems (e.g., sunny vs. rainy driving). It does not address software engineering requirements, coding assistant tasks, or the meta-evaluation of test oracle fidelity.

### 2.5 VNVSpec (Arief et al., 2026)
- **Source:** *Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications*, arXiv:2607.17686, 2026.
- **Section Evidence:**
  - Section III ("The VNVSpec Framework and Traceability", pp. 4–7): Introduces domain-specific languages (DSLs) for compiling requirements into unit and integration test assertions (pytest, Jest) with inconclusive status tracking.
  - Section IV ("Workflow and Evaluation", pp. 8–10): Evaluates automated verification workflows linking execution traces to system requirements.
- **Why It Does Not Cover Our Problem:**
  VNVSpec is an internal test generation and specification compiler. It requires executing internal tests directly on the system. It does not provide an inference calculus for evaluating whether *pre-existing third-party benchmark evaluations* can be trusted as evidence in lieu of local testing.

### 2.6 Assurance Evidence Reuse (Mukhopadhyay & Nalla, 2026)
- **Source:** *Validity Conditions and Evidence Reuse in Machine Learning Assurance*, arXiv:2610.27672, 2026.
- **Section Evidence:**
  - Section 3 ("Epistemic Validity Framework", pp. 5–9): Defines formal validity conditions under which an assurance claim $C_1$ can adopt evidence $E_2$ collected for claim $C_2$.
  - Section 4 ("Automated Release Gate and Case Studies", pp. 10–13): Implements an Ed25519 cryptographic fail-closed release gate and evaluates selective replay across 714 DVC pipelines and 38,083 commits.
- **Why It Does Not Cover Our Problem:**
  Mukhopadhyay and Nalla enforce policy compliance over declared pipeline dependencies using cryptographic hashes. As the authors note, cryptographic gates cannot detect undeclared dependencies or evaluate whether third-party coding benchmark tasks semantically represent target operational requirements, and lack statistical confidence bounding over matched task subsets.

### 2.7 Coding Agent Assurance Envelopes (Goswami, 2026)
- **Source:** *Assurance Envelopes for Automated Coding Agents*, arXiv:2609.16302, 2026.
- **Section Evidence:**
  - Section 3 ("Typed Inference Graphs", pp. 4–8): Formulates typed inference graphs over repository ASTs and execution traces to verify software change obligations.
  - Section 4 ("Constraint Solving", pp. 9–12): Uses forward chaining and a CP-SAT constraint solver to deduce whether available evidence satisfies change obligations, reporting solver infeasibility when obligations cannot be deduced.
- **Why It Does Not Cover Our Problem:**
  Goswami evaluates runtime change derivations and formal obligation satisfaction for local code generation. It does not address the design-time requirements acceptance problem of deciding whether external third-party benchmark results justify selecting a candidate coding assistant under confidence intervals and review-based abstention.

### 2.8 NIST AI Benchmark Guidance (NIST AI 800-2, 2026)
- **Source:** *Practices for Automated Benchmark Evaluations of Language Models*, NIST Special Publication AI 800-2 (ipd), 2026.
- **Section Evidence:**
  - Section 4 ("Benchmark Integrity", pp. 18–24): Recommends reporting contamination checks, test harness environments, and statistical variance.
  - Section 6 ("Limitations and Non-Goals", pp. 32–34): Explicitly warns that benchmark leaderboards do not equate to operational task suitability and leaves task-specific requirements matching to end-users.
- **Why It Does Not Cover Our Problem:**
  NIST provides policy recommendations and reporting checklists. It explicitly disclaims providing an algorithmic method or decision calculus for software requirements engineering.

### 2.9 Specification-Oracle Gaps (Ding et al., 2026; EvalPlus; SWE-bench Audits)
- **Source:** *What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks*, arXiv:2610.30635, 2026; *Is Your Code Generated by ChatGPT Really Correct?*, NeurIPS 2023.
- **Section Evidence:**
  - Ding et al., Section 3 ("Taxonomy of Spec-Oracle Gaps", pp. 4–8): Identifies unstated requirements in hidden test suites (e.g., hidden helper functions, undisclosed types) that cause false test failures on HumanEval/MBPP.
  - OpenAI SWE-bench Audit (2026): Audits SWE-bench Pro for noisy tests and ambiguous issue descriptions.
- **Why It Does Not Cover Our Problem:**
  These studies audit *benchmarks in isolation* to clean datasets or detect false failures. They do not formulate a requirements decision theory: they do not link system capability requirements to benchmark evidence, do not define admissibility decision tables, and do not measure the predictive validity of benchmark evidence on unseen repository workloads.

---

## 3. Synthesis: Scoped Research Opportunity

Across all surveyed literature:
1. **RE4AI literature** has focused heavily on elicitation, taxonomies of ML requirements, and model cards, but lacks an operational decision engine for linking external benchmark evidence to concrete repository requirements.
2. **Safety assurance literature** (AMLAS, Assurance Contracts, Transfer Assurance) provides conceptual argument structures (GSN), but assumes internal test generation or domain shift in physical robotics, omitting LLM coding agents and public benchmark evidence reuse.
3. **AI benchmark literature** (BetterBench, Leaderboard Illusion, EvalPlus, Ding et al.) audits benchmark flaws and warns against blind leaderboard reliance, but offers few constructive methods for software engineers to determine when benchmark evidence can legitimately be reused.

### Research Opportunity Formulation
> **Scoped Research Objective:** Formulate and evaluate an empirical method that determines whether external AI benchmark evidence legitimately supports a software requirement for an automated coding assistant, examining how review-based admissibility gating and statistical uncertainty bounds affect acceptance decisions under benchmark flaws.

---

## 4. Delineation Summary

- [x] Primary texts inspected and verified with page/section citations.
- [x] Multi-dimensional comparison matrix completed (`paper2/literature/comparison_table.md`).
- [x] Scope established as distinct from Paper 1 (MESA meta-evaluation of benchmarks vs. Paper 2 requirements acceptance decision method).
- [x] Comparative differentiation established against examined frameworks (AMLAS, VNVSpec, Evidence Reuse, DAMSA-SMS, ECBD, BetterBench).

**Delineation Status:** **VERIFIED**. Methodological development authorized under scoped boundaries.
