# MESA Repository Context

This repository contains MESA, the Meta-Evaluation Standard for AI Benchmarks. MESA adapts the EFPA Test Review Model 2025 from human psychometrics into an AI benchmark auditing framework.

## Project Purpose

Treat AI benchmarks as formal measurement instruments. The goal is not simply to rank models, but to review whether benchmark claims, construction, scoring, documentation, maintenance, and interpretation are transparent and scientifically defensible.

## Research Foundations

- EFPA Test Review Model 2025: primary structural source for the review architecture.
- CHC theory: capability-domain grounding for benchmark classification.
- BetterBench and related benchmark-quality literature: benchmark lifecycle quality, reproducibility, contamination controls, usability, implementation, documentation, and maintenance.
- Benchmark critique literature: use to challenge overclaims, leaderboard interpretation, validity gaps, and claims about general intelligence or agency. Transcriptions now available in `literature/` include The Leaderboard Illusion, Line Goes Up?, Evaluating the Evaluations, What Does Your Benchmark Really Measure?, PeerBench, Prioritization First, and the AI Cognitive Examination survey.
- Measuring what Matters: use for construct validity, especially the relationship between the claimed phenomenon, task design, scoring metric, and resulting claims.
- AGI/CHC literature: use when benchmarks make broad cognitive, AGI, general intelligence, or cross-domain capability claims.

## Repository Layout

- `README.md`: high-level project description and roadmap.
- `paper.tex` / `references.bib`: the MESA paper (IEEEtran conference format, "MESA: Requirements-Oriented Review of AI Benchmarks as Measurement Instruments") and its bibliography.
- `MESA EFPA template official.md`: active unified MESA Part A + Part B adaptation template for AI benchmarks.
- `benchmark_official_documentation_inventory.md`: inventory mapping candidate benchmarks to their official or primary documentation (Part A evidence sourcing).
- `Papers/`: original PDF source library.
- `literature/`: markdown corpus of verbatim transcriptions of the PDF sources plus the EFPA model (currently 13 documents). `EFPA_Test_Review_Model_2025_Markdown.md` is the review-architecture source. The corpus also includes the benchmark-quality and critique transcriptions `betterbench.md`, `Measuring_what_Matters.md`, `Evaluating_the_Evaluations.md`, `The_Leaderboard_Illusion.md`, `lineUP.md` (Line Goes Up?), `What_Does_Your_Benchmark_Really_Measure.md`, `PRIORITIZATION_FIRST.md`, `PeerBench_PROPOSAL_PAPER.md`, and `AI_Cognitive_Examination.md`, plus `A_Definition_of_AGI.md` and `Humanitys_Last_Exam.md`, and the benchmark transcription `DesignQA.md` (a multimodal engineering-requirements benchmark, used as an RE-native benchmark example).
- `reviews/`: pilot benchmark reviews produced by the multi-LLM review pipeline. Two independent reviewer drafts (`chatgpt_reviewer1/`, `claude_reviewer2/`) are reconciled by `gemini_supervising_editor/` into the final source-grounded review. Each reviewer covers Humanity's Last Exam and ARC-AGI-2.
- `dist/hf_mesa_dataset/`: generated Hugging Face-style dataset export (data, schema, reviews, README); use it as derived output, not the source of truth.
- `AGENTS.md`, `GEMINI.md`: agent operating instructions. `AGENTS.md` is the default repository guide; `GEMINI.md` defines the supervising-editor reconciliation role.
- `.codex/agents/`: agent profiles, including `research-assistant.md` and `benchmark-reviewer.md`.
- `.codex/memory/`: durable project memory for agents (`project.md`, `research-method.md`, `workflow.md`).

## Working Principles

- Preserve the distinction between factual description and evaluative judgment.
- Prefer cautious language when benchmark documentation is incomplete.
- Attribute claims to benchmark creators, maintainers, or source papers where possible.
- Flag uncertainty explicitly instead of filling gaps with confident speculation.
- Keep MESA terminology consistent: benchmark, AI system, evaluator, scoring, capability domain, reference interpretation, repository transparency, versioning.
- Avoid treating leaderboard performance as direct evidence of broad intelligence without measurement-validity support.
- Do not attempt to complie latex code.

## Style

- Use concise academic prose.
- Make assumptions explicit.
- Keep tables and templates easy to scan.
- Use markdown headings, short paragraphs, and checklists where they improve review usability.
- Preserve citation placeholders or notes if full citation management is not yet configured.
