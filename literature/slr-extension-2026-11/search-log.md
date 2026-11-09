# Search Log: SLR Extension 2026-11

**Protocol ID:** `slr-extension-protocol-2026-11`  
**Retrieval Dates:** 03–04 November 2026  
**Target Discipline:** Requirements Engineering, Safety Assurance, and AI Benchmark Quality  

---

## 1. Search Strategy & Database Query Definitions

To extend the initial literature review beyond general benchmark review instruments to specific paradigms in safety cases, evidence reuse, machine-readable specifications, and deployment model selection, four targeted literature searches and screening registers were conducted. *Note on Research Provenance:* Individual query files in `searches/` record curated screening notes and candidate registers from targeted queries; synthetic search totals have been explicitly withdrawn to ensure research integrity.

### Query 1: Evidence Reuse & Epistemic Transfer (arXiv / OpenAlex)
- **Search String:** `("assurance evidence reuse" OR "reusing assurance evidence" OR "validity conditions") AND ("pipeline" OR "machine learning" OR "release gate")`
- **Databases:** arXiv CS.SE / CS.AI, OpenAlex
- **Screened Candidates:** 4 candidate records (Mukhopadhyay & Nalla 2026, Habli et al. 2024, Sljivo et al. 2014, Picardi et al. 2023)
- **Primary Extraction:** Mukhopadhyay & Nalla (arXiv:2610.27672)

### Query 2: Coding Agent Assurance Envelopes (arXiv / CrossRef)
- **Search String:** `("assurance envelopes" OR "assurance envelope") AND ("coding agents" OR "code generation" OR "software change")`
- **Databases:** arXiv CS.SE, CrossRef
- **Screened Candidates:** 2 candidate records (Goswami 2026, Burton et al. 2022)
- **Primary Extraction:** Anjan Goswami (arXiv:2609.16302)

### Query 3: Deployment-Aware Model Selection (CrossRef / Applied Sciences)
- **Search String:** `("Deployment-Aware Model Selection" OR "System-Aware Model Selection" OR "DAMSA") AND ("model selection" OR "operational constraints")`
- **Databases:** CrossRef, Google Scholar / MDPI
- **Screened Candidates:** 2 candidate records (Singh & Kaewprapha 2026, Troubitsyna et al. 2024)
- **Primary Extraction:** Singh & Kaewprapha (Applied Sciences 16(21):10447, 2026)

### Query 4: Benchmark Quality, Construct Validity, & Specification-Oracle Auditing (arXiv / OpenAlex)
- **Search String:** `("benchmark quality" OR "construct validity" OR "specification-oracle" OR "evidence-centered benchmark") AND ("code generation" OR "NLP" OR "LLM")`
- **Databases:** arXiv, OpenAlex
- **Screened Candidates:** 6 candidate records (Fei Ding 2026, Liu et al. ECBD 2024, Reuel et al. BetterBench 2024, Ghosh et al. Evaluation Cards 2026, Pizarro et al. Beyond the Hype 2026, Yang et al. IFEvalCode 2025)
- **Primary Extractions:** Ding (EXT-09), Liu et al. (EXT-12), Reuel et al. (EXT-13), Ghosh et al. (EXT-14), Pizarro et al. (EXT-15)

---

## 2. Quantitative Screening Summary

| Paradigm / Query Group | Database Sources | Confirmed Candidates Screened | Retained for Comparative Matrix | Excluded from Matrix |
|---|---|---|---|---|
| Q1: Evidence Reuse & Epistemic Transfer | arXiv / OpenAlex | 3 (Mukhopadhyay & Nalla, Picardi, Sljivo) | 3 | 0 |
| Q2: Coding Agent Assurance Envelopes | arXiv / CrossRef | 1 (Goswami 2026) | 1 | 0 |
| Q3: Deployment-Aware Model Selection | CrossRef / MDPI | 1 (Singh & Kaewprapha 2026) | 1 | 0 |
| Q4: Benchmark Auditing & Construct Validity | arXiv / OpenAlex | 6 (Ding, Liu et al., Reuel et al., Ghosh et al., Pizarro et al., Yang et al.) | 5 | 1 (Yang et al. 2025) |
| Baseline Foundations (Re-Evaluated) | Primary Sources | 5 (Hawkins et al., Lawford et al., Arief et al., Hou et al., NIST) | 5 | 0 |
| **Total Confirmed Publications** | --- | **16 records** | **15 included** | **1 excluded** |
| Historical Disambiguation Notes | Project Records | 3 (Habli, Burton, Troubitsyna) | 0 | 3 (Preserved for provenance; unverified) |

Detailed inclusion and exclusion decisions are preserved in `screening-decisions.md`. Reconstructed screening notes are preserved in `searches/`.
