# MESA-meta-evaluation-standard-for-ai

This repository is the replication package for the paper **MESA: Requirements-Oriented Review of AI Benchmarks as Measurement Instruments**, by Vitor Raposo (Faculty of Engineering, Ontario Tech University), manuscript in preparation, 2026.

The paper argues that AI benchmark scores are routinely used to justify capability, safety, and procurement claims, yet the benchmarks themselves are rarely audited as measurement instruments. MESA adapts the psychometric EFPA Test Review Model into a requirements-oriented framework for reviewing AI benchmarks before their scores are trusted to back such claims.

## Overview
MESA is a structured review framework designed to audit AI benchmarks as measurement instruments. Instead of treating benchmark scores as unquestioned proof of capability, MESA provides a methodology to review the benchmarks themselves—evaluating what they claim to measure, how they operate, and whether their engineering infrastructure is trustworthy.

## Theoretical Foundations
MESA is built on three pillars:
* **Psychometric Discipline (EFPA):** Adapts the structured instrument-description logic used in human psychological testing.
* **Cognitive Mapping (CHC):** Grounded in the Cattell-Horn-Carroll (CHC) theory to define specific capability domains (Reasoning, Knowledge, Multimodality, etc.).
* **Engineering Quality (BetterBench):** Treats benchmarks as lifecycle software artifacts, emphasizing reproducibility and maintenance.

## Unified Part A + Part B Review
The framework implements a unified EFPA-inspired template. **Part A** is the descriptive scaffold: it serves as a standardized "spec sheet" to make benchmark claims transparent and comparable. **Part B** is the evaluative scaffold: it uses EFPA-style `n/a` and `0`-`4` ratings to judge whether the benchmark supports its stated interpretation.

### Key Sections:
1.  **Factual Description:** Provenance, authors, versioning, and code/data repositories.
2.  **Classification:** Intended systems (e.g., Frontier LLMs), response modes (e.g., multiple choice, code generation), and cognitive demands.
3.  **Measurement & Scoring:** The logic of how outputs become scores (e.g., exact match vs. Model-as-Judge).
4.  **Benchmark Outputs:** The structure of reports, leaderboards, and process data (like token usage).
5.  **Supply & Materials:** Technical documentation, changelogs, and usage requirements.
6.  **Part B Evaluation:** Rationale, materials, baselines, reliability, validity, fair use, reports, and overall evidence-grounded ratings.

## Part A / Part B Boundary
> [!IMPORTANT]
> Part A is descriptive and should not contain ratings. Part B is evaluative and should not contain unsupported claims.
>
> Part A asks *"What is this benchmark?"* Part B asks *"How good is this benchmark as a measurement instrument for its stated purpose?"* Part B ratings must cite evidence, missing evidence, reviewer rationale, and interpretation caution.

## Repository Contents
* `MESA EFPA template official.md` — the active unified Part A + Part B review template.
* `literature/` — markdown literature corpus (EFPA Test Review Model, BetterBench, Measuring what Matters, A Definition of AGI, the HLE source paper).
* `reviews/` — pilot benchmark reviews for Humanity's Last Exam and ARC-AGI-2, produced by two independent reviewer models and reconciled by a supervising editor, organized under `chatgpt_reviewer1/`, `claude_reviewer2/`, and `gemini_supervising_editor/`.
* `Papers/` — original PDF source library.
* `dist/hf_mesa_dataset/` — Hugging Face-style dataset export of the reviews (generated artifact, not source of truth).
* `tools/` — validation and utility scripts.
* `reports/` — generated validation and inventory reports.

## Case Studies
The paper applies MESA to two high-visibility benchmarks: Humanity's Last Exam (HLE) and ARC-AGI-2. The reconciled reviews and the underlying reviewer drafts are available in `reviews/`, and illustrate how MESA separates supported narrow interpretations (e.g., a difficult academic question-answering benchmark; an exact-grid abstraction benchmark under specified conditions) from broader claims about general intelligence or agency that are not supported by the benchmark evidence alone.
