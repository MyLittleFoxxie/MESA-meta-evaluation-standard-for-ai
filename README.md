# MESA-meta-evaluation-standard-for-ai

## Overview
MESA is a structured review framework designed to audit AI benchmarks as measurement instruments. Instead of treating benchmark scores as unquestioned proof of capability, MESA provides a methodology to review the benchmarks themselves—evaluating what they claim to measure, how they operate, and whether their engineering infrastructure is trustworthy.

## Theoretical Foundations
MESA is built on three pillars:
* **Psychometric Discipline (EFPA):** Adapts the structured instrument-description logic used in human psychological testing.
* **Cognitive Mapping (CHC):** Grounded in the Cattell-Horn-Carroll (CHC) theory to define specific capability domains (Reasoning, Knowledge, Multimodality, etc.).
* **Engineering Quality (BetterBench):** Treats benchmarks as lifecycle software artifacts, emphasizing reproducibility and maintenance.

## Current Scope: Unified Part A + Part B Review
The framework now implements a unified EFPA-inspired template. **Part A** is the descriptive scaffold: it serves as a standardized "spec sheet" to make benchmark claims transparent and comparable. **Part B** is the evaluative scaffold: it uses EFPA-style `n/a` and `0`-`4` ratings to judge whether the benchmark supports its stated interpretation.

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

## Case Study: Humanity's Last Exam (HLE)
The repository includes a sample review of the HLE benchmark, demonstrating how MESA surfaces the distinction between "high academic performance" and "general autonomous agency."
