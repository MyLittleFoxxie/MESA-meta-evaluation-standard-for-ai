# Systematic Literature Review Extension: AI Benchmark Quality & Evidence Reuse in RE

**Review Extension ID:** `slr-extension-2026-11`  
**Reconstruction & Verification Date:** 05 November 2026  
**Parent Review Protocol:** [`literature/slr-2026-10-28/`](../slr-2026-10-28/README.md)  
**Target Submission Target:** REFSQ (Requirements Engineering: Foundation for Software Quality)  
**Provenance Note:** Reconstructed candidate screening registers; synthetic search engine totals have been explicitly withdrawn.  

---

## 1. Objectives & Scope of Extension

This extension broadens the 28 October 2026 MESA systematic literature review beyond general psychometric and AI benchmark review instruments to investigate:
1. How safety assurance, software engineering, and requirements frameworks reuse third-party evidence across system boundaries.
2. How benchmark review frameworks handle incomplete documentation, missing test constraints, and benchmark defects.
3. Whether existing literature provides an operational decision calculus for accepting, contradicting, or withholding requirements compliance claims based on external benchmark evidence.

---

## 2. Search Strategy & Database Query Definitions

Targeted literature searches were conducted across digital repositories (**arXiv**, **CrossRef**, **OpenAlex**, and **MDPI**). *Note on Research Provenance:* Individual query files in [`searches/`](searches/) record curated screening notes and candidate registers from targeted queries; synthetic search totals have been explicitly withdrawn to ensure research integrity.

### Search Query Formulations:
- **Query 1: Evidence Reuse & Epistemic Transfer (arXiv / OpenAlex)**  
  `("assurance evidence reuse" OR "reusing assurance evidence" OR "validity conditions") AND ("pipeline" OR "machine learning" OR "release gate")`  
  *Screened Candidates (4):* Mukhopadhyay & Nalla (2026, INCLUDED), Picardi et al. (2023, INCLUDED), Sljivo et al. (2014, INCLUDED), Habli et al. (2024, EXCLUDED).
- **Query 2: Coding Agent Assurance Envelopes (arXiv / CrossRef)**  
  `("assurance envelopes" OR "assurance envelope") AND ("coding agents" OR "code generation" OR "software change")`  
  *Screened Candidates (2):* Goswami (2026, INCLUDED), Burton et al. (2022, EXCLUDED).
- **Query 3: Deployment-Aware Model Selection (CrossRef / MDPI)**  
  `("Deployment-Aware Model Selection" OR "System-Aware Model Selection" OR "DAMSA") AND ("model selection" OR "operational constraints")`  
  *Screened Candidates (2):* Singh & Kaewprapha (Applied Sciences 2026, INCLUDED), Troubitsyna et al. (2024, EXCLUDED).
- **Query 4: Benchmark Quality, Construct Validity, & Specification-Oracle Auditing (arXiv / OpenAlex)**  
  `("benchmark quality" OR "construct validity" OR "specification-oracle" OR "evidence-centered benchmark") AND ("code generation" OR "NLP" OR "LLM")`  
  *Screened Candidates (6):* Fei Ding (2026, INCLUDED), Liu et al. ECBD (2024, INCLUDED), Reuel et al. BetterBench (2024, INCLUDED), Ghosh et al. Evaluation Cards (2026, INCLUDED), Pizarro et al. Beyond the Hype (2026, INCLUDED), Yang et al. IFEvalCode (2025, EXCLUDED).

### Baseline Foundations Re-Evaluated:
In addition to the 14 targeted candidates (10 included, 4 excluded), 5 foundational baseline records from the initial SLR are re-evaluated in the comparative matrix:
1. **AMLAS:** Guidance on the Assurance of Machine Learning in Autonomous Systems (*Hawkins et al.*, 2021).
2. **ML Change Impact Analysis:** Safety Case Impact Assessment (*Lawford et al.*, SAFECOMP 2024 / 2017).
3. **VNVSpec:** Machine-readable specification languages for verification and validation (*Arief et al.*, arXiv:2607.17686, 2026).
4. **Application-Based Model Selection:** Survey on LLM selection for software engineering tasks (*Hou et al.*, TOSEM 2024).
5. **NIST AI 800-2:** Practices for Automated Benchmark Evaluations of Language Models (*NIST*, 2026).

**Total Inspected Candidate Trail:** 19 records (15 included, 4 excluded).

---

## 3. Directory Structure

- [`extraction.json`](extraction.json): Full-text extraction records capturing page/section evidence, input format, evidence sources, missing evidence handling, and decision mechanics.
- [`deduplication.json`](deduplication.json): Cross-mapping against `slr-2026-10-28` records.
- [`synthesis.md`](synthesis.md): Thematic synthesis across assurance, benchmark auditing, and requirements traceability.
- [`gap-ledger.md`](gap-ledger.md): Candidate gaps G7–G10, counterexamples, uncertainty bounds, and explicit boundaries under "Claims this review does not support".
- [`comparison_table.md`](comparison_table.md): Substantively verified 7-attribute matrix.
- [`search-log.md`](search-log.md): Search query logs, candidate registers, and quantitative screening summary.
- [`screening-decisions.md`](screening-decisions.md): Item-level screening decisions and inclusion/exclusion rationale for all 19 inspected candidate records.
- [`searches/`](searches/): Individual query screening notes and candidate registers.
