# Context and continuation plan for version three

Updated 30 October 2026, after the Claude batch. This document replaces the earlier handoff, which listed the Claude batch as pending. Read it before continuing in a new chat. It is a handoff, not authorization to launch more experiments.

## Start here

The repository is `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. The current branch is `codex/mesa-v3`. Both experiment batches are complete and the manuscript reports both. Do not rerun Codex or Claude, modify the existing survey, or compile LaTeX as a default continuation action.

The next work is review of the manuscript and analysis using saved records, and any packaging or publication the user requests. There are no unstarted jobs in either batch. Any later experiment requires its own protocol version and the user's instruction to run it.

Read in this order:

1. The repository's `AGENTS.md`, `README.md` and `CHASE-study.md` for the parent project and preservation rules.
2. This handoff for the user's decisions that apply specifically to v3.
3. [Paper plan](README.md) and [experiment design](experiments.md).
4. [Codex protocol](study/protocol.md), [Claude protocol](study/claude/protocol.md), [analysis plan](study/analysis-plan.md), [study guide](study/README.md), [Codex results](study/analysis/summary.json) and [Claude results](study/claude/analysis/summary.json).
5. [Manuscript](../paper_mesa_v3.tex), [rubric](study/materials/rubric.md), [Codex selected audit](study/analysis/selected-reviews.md) and [Claude selected audit](study/claude/analysis/selected-reviews.md).

The repository guide describes the earlier questionnaire as the current instrument. The user selected a ten criterion design for this branch. That decision applies to v3, not to the preserved CHASE, REFSQ, RETRAI or older manuscripts. Do not rewrite the rest of the project to make it appear that it always used ten criteria.

## What the project is

MESA studies how to review artificial intelligence benchmarks rather than how to answer their test problems. Its earlier instrument is a questionnaire with 25 questions, six domains and five choices. It draws on the European Federation of Psychologists' Associations Test Review Model, with benchmark and measurement literature. Those categorical answers are not numerical quality ratings.

The earlier CHASE paper reports adaptation and model experiments. The REFSQ paper is intended to extend that work with human evaluation. Earlier study outputs and the existing participant survey are separate research records. They are not inputs to the v3 experiment and do not validate the v3 rubric.

The user supplied `/Users/mylittlefoxxie/Downloads/paper_plan_auditing_ai_benchmarks_with_cli_agents.md` and asked for a new paper version and experiments on a separate branch. The attachment proposed ten audit criteria, five benchmarks and comparisons between coding agents. It also contained supposed findings before any corresponding experiment existed. Those passages were treated as a proposal, not evidence, and none of its invented results appear in the paper.

## Decisions made so far

1. The user chose **Option B**: v3 uses the **MESA benchmark audit rubric**, with ten criteria and provenance identifier `mesa-audit-10-v3`.
2. MESA remains the instrument name in the body. The user prohibits acronyms in titles. The manuscript title is **Auditing Artificial Intelligence Benchmarks with Coding Agents**. Do not restore MESA, AI or CLI to that title.
3. The design is **12 main sessions per batch**: three benchmarks × two access conditions × two repetitions.
4. Codex batch: `gpt-6-luna`, medium reasoning effort, through Codex. Do not revert to low effort or replace it with a more costly model.
5. Claude batch: the user instructed, on 30 October 2026, to run the pending Claude part with **Claude Fable 5.1 (`claude-fable-5-1`) at medium effort** through Claude Code, and to finalize the paper.
6. No study imposed per session token, output, tool call or time ceilings. Each batch has a cap of **16 physical attempts**. Codex used 14; Claude used 15.
7. The existing survey is ignored for v3. Leave its files and records untouched.
8. CHASE cannot contain human survey results. Any later human evaluation belongs only in a REFSQ extension and is deferred.
9. Prompts, materials, sources and analyst references are byte identical across batches. The Claude batch is a later, sequential batch. It is not jointly randomized with Codex, and no difference may be attributed to the command line tool alone.

## What v3 contains

The rubric has five software and documentation criteria (A1 evaluation scripts, A2 scoring implementation, A3 dataset documentation, A4 permissions and dependencies, A5 reproduction instructions) and five measurement criteria (B1 construct definition, B2 answer checking, B3 score reliability, B4 human comparisons, B5 training exposure). Each criterion has its own 0, 5, 10 and 15 anchors. Insufficient evidence and not applicable have null ratings. Do not average or add ratings into an overall benchmark quality score. Earlier questionnaire results cannot be converted to these ratings.

The ten criteria omit or compress concerns from the questionnaire, in particular aggregation, shortcuts, submission rules, fairness, release changes and public claims. The manuscript retains this limitation. Do not describe the rubric as a complete measure of construct validity.

## What ran

Both batches: HumanEval, TruthfulQA and DesignQA; a documents condition with the extracted paper text and top level README and no source tools; a repository condition adding a confined file listing and text reading server over the frozen repository. The agent could not execute code, write files, browse or read analyst records. Sessions started in empty temporary directories.

Codex batch: 12 main sessions, 120 judgments, two pilots, 14 attempts, no retries. All main sessions completed and every repository session used the tools. The repository pilot's file call failed because approval was required; it is retained. The freeze covers 619 file hashes.

Claude batch: 12 main sessions, 120 judgments, three pilot attempts, 15 attempts. The first documents pilot failed before any model request because Claude Code rejected the `$schema` key of the frozen response schema; the runner now omits only that key from the command line argument, and the frozen file is unchanged. The repository pilot read files under the Claude Code tool names despite the Codex style names in the prompt, so prompts stayed identical. Claude Code made an auxiliary call to a smaller model in every session; its inputs are not exposed. The Claude freeze covers 616 file hashes. Structured output arrives through a `StructuredOutput` tool call that the analysis excludes from tool boundary checks by name.

## Observed results and their meaning

Codex ([summary.json](study/analysis/summary.json)): 46 of 60 repeat pairs and 42 of 60 access pairs matched; 295 citations, all to allowed sources; 122 exact quote matches, 189 after whitespace normalization; 205 resolvable locators.

Claude ([summary.json](study/claude/analysis/summary.json)): 55 of 60 repeat pairs and 45 of 60 access pairs matched; 460 citations, 459 to allowed sources (one cites the file listing itself); 299 exact quote matches, 356 after normalization; 315 resolvable locators. Every access change concerned an A criterion. Reported input tokens about 2.5 million and output tokens about 111 thousand, summing uncached, cache creation and cache read input.

Cross batch ([cross-batch.json](study/claude/analysis/cross-batch.json)): 92 of 120 paired judgments matched in status and rating, 115 in status. These are descriptive counts, not provider rankings or accuracy. Agreement does not make a judgment correct.

The semantic audits cover the repetition one responses of each batch, six responses and sixty judgments each. The Codex audit was written by the Codex assistant; the Claude audit by Claude Fable 5.1, the same model as the Claude reviewer. No independent human analysis is claimed. Repository responses in the Claude batch recorded code and documentation discrepancies (an active execution line described as commented out, a commented out metric that appears in a results table, an undocumented reference answer injection, a fixed divisor). The preparing assistant confirmed the cited lines offline; this does not make the ratings correct.

## Artifact map

| Location | Role |
| --- | --- |
| `paper_mesa_v3.tex` | Manuscript in IEEE format reporting both batches; earlier manuscripts are preserved |
| `v3/README.md`, `v3/experiments.md` | Paper decisions and design history |
| `v3/study/README.md` | Study entry point and reproduction instructions |
| `v3/study/protocol.md`, `v3/study/claude/protocol.md` | Frozen executed protocols |
| `v3/study/analysis-plan.md` | Frozen analysis decisions, shared by both batches |
| `v3/study/materials/`, `prompts/`, `sources/`, `analyst/` | Shared frozen inputs |
| `v3/study/jobs.json`, `v3/study/claude/jobs.json` | Execution schedules; the Codex file's `claude` field is the historical pending note |
| `v3/study/freeze-manifest.json`, `v3/study/claude/freeze-manifest.json` | Input fingerprints; do not rewrite |
| `v3/study/run.py`, `v3/study/claude/run.py` | Runners; do not invoke for the completed batches |
| `v3/study/outputs/`, `v3/study/claude/outputs/` | Raw responses, events, errors and attempt metadata |
| `v3/study/analyze.py`, `v3/study/claude/analyze.py` | Shared analysis with per tool event parsers; Claude script also writes the cross batch comparison |
| `v3/study/analysis/`, `v3/study/claude/analysis/` | Generated counts, `results.tex`, authored `interpretation.tex`, `review_selected.py` and rendered audits |
| `v3/study/verify.py`, `v3/study/claude/verify.py` | Offline verifiers; the Codex one also checks the manuscript |
| `v3/study/claude-pending.md` | Historical name; now records the completed Claude batch |

`study/instrument-map.md` is a frozen copy of the paper plan at freeze time, not a maintained index.

## Remaining steps

1. **Review the manuscript and analyses using saved records.** Execution and structural checks are complete. The manuscript has been read end to end once by the preparing assistant after the second batch, but not by a human author. Check whether each interpretation follows from the cited source and the exact response. Do not calculate a semantic error rate unless a defined review procedure supports it. Quote mismatches have not been inspected exhaustively for either batch.
2. **Verify after any edits** with the commands below. Keep generated counts and authored interpretation separate. A freeze mismatch is a preservation issue, not something to fix by replacing the saved hash. Do not compile LaTeX unless the user changes that instruction.
3. **Human work and publication remain deferred.** If a REFSQ extension is requested, plan human evaluation of the ten criterion rubric as its own study. If the user asks for a commit, inspect Git status first: `v3/`, `paper_mesa_v3.tex` and `literature/README.md` are untracked and many unrelated edits and deletions from earlier work remain in the checkout. Stage only the intended files. Local source archives and binary datasets are not automatically available to repository readers. No publishing action is authorized by this handoff.

## Offline commands

Run from the repository root; none makes a model call:

```sh
python3 v3/study/test_harness.py
python3 v3/study/claude/test_harness.py
python3 v3/study/validate.py
python3 v3/study/analyze.py
python3 v3/study/claude/analyze.py
python3 v3/study/analysis/review_selected.py
python3 v3/study/claude/analysis/review_selected.py
python3 v3/study/verify.py
python3 v3/study/claude/verify.py
```

`analyze.py` scripts rewrite generated files; the Claude script also rewrites the Codex analysis deterministically. `review_selected.py` scripts rewrite the rendered audits from authored notes. The verifiers rerun analysis to check determinism and write verification and output manifests. Do not hand edit generated counts or rendered audits. Do not run `build_materials.py`, `prepare_references.py` or either `freeze.py`. Do not delete failure logs or repair raw responses.

## Writing rules

Write with simple terms, direct sentences and no marketing language. Keep unknown information separate from negative evidence, checking from its outcome, agreement from correctness and model behavior from human behavior. Preserve the distinction between a complete experiment and a validated instrument, and between agreement across batches and a model comparison.
