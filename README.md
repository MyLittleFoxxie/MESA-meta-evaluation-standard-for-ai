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

A review opens with a **General Description** (a short stand-alone, non-evaluative summary) and a **Source Inventory** recording every source consulted with its access date.

### What the descriptive phase covers:
1.  **Factual Description:** Provenance, authors, versioning, and code/data repositories.
2.  **Classification:** Intended systems (e.g., Frontier LLMs), task interaction and response types (e.g., multiple choice, code generation), and evaluation conditions.
3.  **Measurement and Scoring:** The logic of how outputs become scores (e.g., exact match vs. model-as-judge).
4.  **Benchmark Outputs and Reports:** The structure of reports, leaderboards, and process data (like token usage).
5.  **Benchmark Access, Materials, and Lifecycle:** Access routes, contamination documentation, reproducibility materials, licensing, maintenance, and versioning.

### What the evaluative phase covers:
Seven rated sections: Rationale, Development, Documentation, and Task/Item Quality (6) · Quality and Usability of Benchmark Materials (7) · Baselines, Comparators, and Reference Interpretation (8) · Reliability, Precision, and Score Stability (9) · Validity Evidence (10) · Fair Use, Comparability, and Appropriate Use (11) · Quality of Reports, Leaderboards, Dashboards, and Public Claims (12) — each rolling up into evidence-grounded ratings, closing with a Final Evaluation, Summary of Ratings, and Gap Register.

## Not Every Question Applies to Every Benchmark
Following EFPA, a review completes every section that applies and marks the rest `n/a`. There is no separate short form: a benchmark with no leaderboard, no model-based scorer, and a single static form simply marks those items `n/a`, and the review records why.

The distinction that matters is `n/a` versus `0`. Mark an item `n/a` when the attribute does not exist for the benchmark — there is no judge to validate, no subscores whose structure could be examined. Mark it `0` when the attribute exists but the documentation says nothing usable about it. `n/a` records that the question does not arise; `0` records that it arises and is unanswered.

## The Scorecard — a short form for routine use
A full MESA review carries 87 rated items and is built for certification-grade work. For routine decisions — comparing candidate benchmarks, or checking whether a published score can carry the claim attached to it — the repository also ships **`MESA scorecard.md`**, a short form with **40 rated questions**, the Part A descriptive fields those questions depend on, and the complete Final Evaluation including the Gap Register.

The 40 questions were not chosen by intuition. They were fixed by a coverage check against the three pilot reviews: every item that produced a deficiency rating in a reconciled case study had to be in the set, and the items that escaped were added.

Item numbers in the scorecard are the full template's own numbers, so a scorecard review can be extended into a full review at any time by answering the items it omits — nothing is renumbered, and the interactive form stores an answer under the same key in either view. Use the full template rather than the scorecard when the review supports a procurement decision, a policy position, or a safety case.

The scorecard is generated, not hand-maintained: `tools/build-scorecard.py` produces it from the full template using the list in `tools/scorecard-manifest.md`, so the two cannot drift apart. Edit the template or the manifest and re-run the generator; never edit `MESA scorecard.md` directly.

## The Description / Evaluation Boundary
> [!IMPORTANT]
> The descriptive phase should not contain ratings. The evaluative phase should not contain unsupported claims.
>
> The descriptive phase asks *"What is this benchmark?"* The evaluative phase asks *"How good is this benchmark as a measurement instrument for its stated purpose?"* Every evaluative rating must cite evidence, missing evidence, reviewer rationale, and interpretation caution.

## Repository Contents
* `MESA EFPA template official.md` — the active unified Part A + Part B review template.
* `MESA scorecard.md` — the 40-question short form, generated from the template by `tools/build-scorecard.py`.
* `literature/` — markdown corpus of 13 transcribed sources, including the EFPA Test Review Model, BetterBench, Measuring what Matters, A Definition of AGI, and benchmark-critique literature.
* `reviews/` — pilot benchmark reviews for Humanity's Last Exam, ARC-AGI-2, and DesignQA, produced by two independent reviewer models and reconciled by a supervising editor, organized under `chatgpt_reviewer1/`, `claude_reviewer2/`, and `gemini_supervising_editor/`. These were completed against an earlier version of the template (89 items) and are frozen as dated evidence with a version stamp; `feedback/95-mesa-core-plan.md` Part 3 carries the item mapping.
* `Papers/` — original PDF source library.
* `dist/hf_mesa_dataset/` — Hugging Face-style dataset export of the reviews (generated artifact, not source of truth).

## Case Studies
The paper applies MESA to three benchmarks: Humanity's Last Exam (HLE), ARC-AGI-2, and DesignQA. The reconciled reviews and the underlying reviewer drafts are available in `reviews/` — and browsable interactively, alongside a fillable copy of the review template itself, on the project site — and illustrate how MESA separates supported narrow interpretations (e.g., a difficult academic question-answering benchmark; an exact-grid abstraction benchmark under specified conditions; a multimodal engineering-requirements benchmark) from broader claims about general intelligence or agency that are not supported by the benchmark evidence alone.
