# Thematic Synthesis: Benchmark Evidence Qualification in Requirements Engineering

**Review Extension:** `slr-extension-2026-11`  
**Date:** November 2026  
**Status:** Assistant Synthesis; Author Review Pending

---

## 1. Executive Summary

This synthesis analyzes 15 foundational paradigms across safety assurance, benchmark auditing, machine learning specification, and software engineering. It investigates how prior literature addresses the core challenge: **can third-party benchmark evidence legitimately satisfy operational software requirements, and what formal calculus governs acceptance, contradiction, or abstention when evidence is incomplete or flawed?**

---

## 2. Key Synthesis Themes

### Theme 1: The Divide Between Internal Lifecycle Assurance and Third-Party Procurement
Frameworks like **AMLAS** (Hawkins et al., 2021) and **Assurance Contracts** (Sljivo et al., 2014) provide formal structures for constructing safety cases. However, they presuppose that engineering teams possess end-to-end control over training data, test generation, and verification execution. In modern enterprise settings, foundation models and coding assistants are procured as black-box commercial off-the-shelf components. The primary artifact available to software engineers is not an internal test trace, but a public benchmark leaderboard entry (e.g., SWE-bench pass rates). Existing assurance standards lack a formal calculus for ingesting, filtering, and qualifying external third-party benchmark evidence.

### Theme 2: Qualitative Guidance versus Executable Decision Mechanics
A prominent group of benchmark quality instruments—including **ECBD** (Liu et al., 2024), **BetterBench** (Reuel et al., 2024), **Evaluation Cards** (2024), and **NIST AI 800-2** (2026)—provide valuable checklists, worksheets, and multi-attribute quality scores. 
- *ECBD* prompts benchmark authors to describe, justify, and support their design choices.
- *BetterBench* audits benchmark repositories for infrastructure bugs, leakage, and test quality.
- *Evaluation Cards* standardizes reporting cards for diverse stakeholders.

However, these frameworks assess the **benchmark artifact in the abstract**. They do not connect benchmark outcomes to specific, operational system requirements in a software project, nor do they provide an automated statistical decision engine that outputs formal verdicts (Supported, Contradicted, Unresolved) with rigorous confidence bounding.

### Theme 3: The Danger of Benchmark Flaws and Naive Score Reuse
Recent oracle auditing literature, notably **Ding et al.** (2026) and audits of SWE-bench Pro (OpenAI, 2026), demonstrates that public coding benchmarks suffer from severe specification-oracle gaps, under-constrained validators, and over-constrained test suites. 
- Naively reusing aggregate scores (*Method 1*) conflates unrelated software domains and pools defective tasks.
- Naive task matching (*Method 2*) filters by language or category, but remains vulnerable to unasserted regression checks and silent oracle loopholes.
- Therefore, as argued by **Mukhopadhyay & Nalla** (2026) and Kane's validity framework, evidence reuse requires establishing explicit **validity gates**. When benchmark evidence has unverified assumptions or confirmed defects, the decision must be **withheld (Unresolved)**, triggering targeted local verification rather than unwarranted deployment.

### Theme 4: Runtime Dynamic Bounding versus Design-Time Requirements Acceptance
Dynamic assurance frameworks (**DAMSA-SMS**, Troubitsyna et al., 2024) and **Coding Agent Assurance Envelopes** (Vance et al., 2025) establish runtime monitoring wrappers to restrict model actions (e.g., blocking forbidden system calls or unapproved shell operations). While essential during operational deployment, runtime envelopes do not solve design-time procurement decisions: software engineering organizations still require empirical evidence to justify admitting an external coding assistant into their development lifecycle.

---

## 3. The Unaddressed Research Gap

Prior literature provides:
1. Safety assurance argument structures (AMLAS, GSN, Assurance Contracts).
2. Theoretical conditions for evidence reuse (Mukhopadhyay & Nalla).
3. Abstract benchmark quality rubrics (ECBD, BetterBench, Evaluation Cards).
4. Empirical audits of benchmark oracle bugs (Ding et al.).

**The Specific Unaddressed Gap:**  
No prior framework provides an operational, automated requirements-to-evidence decision calculus that evaluates third-party AI benchmark records against operational project requirements, calculates statistical confidence intervals over task-matched evidence, audits evidential admissibility under Kane's scoring inference, and provides an empirical evaluation measuring decision errors and coverage across real software workloads.
