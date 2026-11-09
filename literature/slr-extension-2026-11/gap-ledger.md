# Candidate Gap Ledger: SLR Extension 2026-11

Assistant synthesis; author review pending. "Observed problem" refers to evidence in particular sources. "Candidate gap" is an inference requiring further investigation. No claim below establishes that a solution is absent from the field.

| ID | Problem and Status | Supporting Evidence | Existing Responses & Counterexamples | Limits and Uncertainty | Candidate MESA / Paper 2 Implication |
|---|---|---|---|---|---|
| **G7** | Reusing public benchmark leaderboards as requirements acceptance evidence induces decision errors. Observed in empirical audits and statistical models. | Ding et al. (2026) specification-oracle gaps; OpenAI SWE-bench audit (2026); BetterBench (Reuel et al., 2024); Beyond the Hype (Pizarro et al., 2026). | Task matching filters (e.g., subsetting by language or repo); commercial procurement scorecards. | Task matching filters syntax and category, but does not verify whether benchmark test oracles faithfully enforce requirements or whether test environments match target deployment. | Formalize Method 3: apply Kane scoring inference checks (MESA criteria C07, C28, C14, C12) to gate evidence admissibility before accepting benchmark pass rates. |
| **G8** | Quality frameworks assess benchmarks in the abstract, lacking integration into Requirements Traceability Matrices (RTMs). Conceptual and empirical gap. | ECBD (Liu et al., 2024) focuses on benchmark authoring; BetterBench (Reuel et al., 2024) outputs general quality scores; Evaluation Cards (Ghosh et al., 2026) provides human-facing reporting layers. | NIST AI 800-2 recommends benchmark reporting; AMLAS provides general ML verification assurance; Singh & Kaewprapha (2026) DAMSA/SMS deployment selection for predictive ML. | General quality scores (e.g. 80/100) do not indicate whether a specific software requirement (e.g., $\theta \ge 0.70$ on networking bugfixes) is satisfied. | Connect benchmark evidence directly to target system requirements within an RTM, recording assumptions and missing evidence explicitly. |
| **G9** | Assurance evidence reuse in pipelines addresses internal change re-execution, lacking a calculus for external third-party benchmarks. Methodological gap. | Mukhopadhyay & Nalla (2026) implement release gates for internal DVC pipelines; Goswami (2026) optimizes prior evidence subsets for code changes; Sljivo et al. (2014) formalize deterministic assurance contracts. | VNVSpec (Arief et al., 2026) provides machine-readable DSL for internal tests; Picardi et al. (2023) use statistical distance metrics for perceptual robotics. | Internal pipeline and change-maintenance frameworks do not evaluate external third-party benchmark construct validity or finite binomial sampling uncertainty for COTS foundation model selection. | Pair 95% Wilson score confidence bounds with MESA admissibility gates to establish an executable decision engine for benchmark evidence reuse. |
| **G10** | Missing benchmark documentation is often conflated with model failure, or conversely, treated as an automatic pass. Documented variation in answer rules. | BetterBench penalizes missing documentation with zero scores; traditional leaderboards ignore missing contamination checks entirely. | EFPA section 6.4 separates missing information from negative results; MESA scorecard non-fulfillment rules. | Conflating unstated benchmark documentation with model incompetence distorts procurement decisions; ignoring gaps invites catastrophic failure. | Enforce Missing Evidence Neutrality: missing benchmark evidence renders the requirement decision *Unresolved* (mandating local testing), rather than *Contradicted*. |

---

## Claims This Review Extension Does Not Support

1. No prior work has ever evaluated benchmark quality or test oracles (refuted by BetterBench, Ding et al., and EvalPlus).
2. Existing frameworks never consider validity or evidence models (refuted by ECBD and Mukhopadhyay & Nalla).
3. Benchmark scores can never be reused under any circumstances (evidence can be reused when admissibility gates are satisfied).
4. Review-based abstention (Method 3) is automatically superior simply because it makes fewer false acceptances (abstention trades off against decision coverage; must be benchmarked against uncertainty-matched baselines).
5. The retrieved literature proves that MESA is the only possible evidence qualification framework.

---

## Author Review Record

All G7–G10: **pending**. Record reviewer, date, decision, reasons, and any modified supporting sources before adopting a gap as a manuscript conclusion.
