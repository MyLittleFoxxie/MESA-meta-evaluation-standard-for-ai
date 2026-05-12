# Project Memory

## MESA

MESA stands for Meta-Evaluation Standard for AI Benchmarks. It is a research-driven framework for reviewing AI benchmarks as measurement instruments.

## Core Thesis

AI benchmarks should be audited with the same discipline used for formal human assessment instruments. Benchmark scores are not self-interpreting; they depend on claims, construction, scoring, reliability, validity, documentation, and maintenance practices.

## Current Implementation

The repository implements a unified EFPA-inspired review model. Part A is descriptive. It captures benchmark identity, provenance, classification, intended systems, capability domains, response/scoring modes, outputs, repositories, datasets, reports, documentation, and the phenomenon-task-metric-claim chain.

Part B is evaluative. It supports formal review judgments for reliability, validity, fairness, reproducibility, interpretation quality, baselines/comparators, reports, contamination controls, maintenance, and overall benchmark quality using EFPA-style `n/a` and `0`-`4` ratings.

## Important Distinction

Part A answers: What is this benchmark?

Part B answers: How good is this benchmark as a measurement instrument for its stated purpose?
