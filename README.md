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

## How a MESA Review Works
A MESA review has two phases, adapted from the EFPA Test Review Model. The **descriptive phase** records what the benchmark is and how it operates — a standardized "spec sheet" that makes benchmark claims transparent and comparable, without judging them. The **evaluative phase** then judges how good the benchmark is as a measurement instrument, using EFPA-style `n/a` and `0`-`4` ratings to assess whether the available evidence supports the benchmark's stated interpretation. (In the template itself, these two phases are labeled Part A and Part B.)

### What the descriptive phase covers:
1.  **Factual Description:** Provenance, authors, versioning, and code/data repositories.
2.  **Classification:** Intended systems (e.g., Frontier LLMs), response modes (e.g., multiple choice, code generation), and cognitive demands.
3.  **Measurement & Scoring:** The logic of how outputs become scores (e.g., exact match vs. Model-as-Judge).
4.  **Benchmark Outputs:** The structure of reports, leaderboards, and process data (like token usage).
5.  **Supply & Materials:** Technical documentation, changelogs, and usage requirements.

### What the evaluative phase covers:
Rationale and documentation quality, materials and usability, baselines and reference interpretation, reliability, validity, fair use and comparability, and report/leaderboard quality — each rolling up into evidence-grounded ratings.

## The Description / Evaluation Boundary
> [!IMPORTANT]
> The descriptive phase should not contain ratings. The evaluative phase should not contain unsupported claims.
>
> The descriptive phase asks *"What is this benchmark?"* The evaluative phase asks *"How good is this benchmark as a measurement instrument for its stated purpose?"* Every evaluative rating must cite evidence, missing evidence, reviewer rationale, and interpretation caution.

## Repository Contents
* `MESA EFPA template official.md` — the active unified Part A + Part B review template.
* `literature/` — markdown corpus of 13 transcribed sources, including the EFPA Test Review Model, BetterBench, Measuring what Matters, A Definition of AGI, and benchmark-critique literature.
* `reviews/` — pilot benchmark reviews for Humanity's Last Exam, ARC-AGI-2, and DesignQA, produced by two independent reviewer models and reconciled by a supervising editor, organized under `chatgpt_reviewer1/`, `claude_reviewer2/`, and `gemini_supervising_editor/`.
* `Papers/` — original PDF source library.
* `dist/hf_mesa_dataset/` — Hugging Face-style dataset export of the reviews (generated artifact, not source of truth).

## Case Studies
The paper applies MESA to three benchmarks: Humanity's Last Exam (HLE), ARC-AGI-2, and DesignQA. The reconciled reviews and the underlying reviewer drafts are available in `reviews/` — and browsable interactively, alongside a fillable copy of the review template itself, on the project site — and illustrate how MESA separates supported narrow interpretations (e.g., a difficult academic question-answering benchmark; an exact-grid abstraction benchmark under specified conditions; a multimodal engineering-requirements benchmark) from broader claims about general intelligence or agency that are not supported by the benchmark evidence alone.
