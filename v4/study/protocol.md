# Study protocol, version 1 draft

Prepared 31 October 2026. Frozen on 31 October 2026 after the pilots. This protocol governs the agent sessions of Study 1 (seven existing frameworks) and Study 2 (the new rubric). It is frozen by `freeze.py` after the checks before the sessions pass and before the first main session; pilots on the fictional fixture may run before the freeze.

## Scope

Four benchmarks: HumanEval, TruthfulQA, Humanity's Last Exam and τ-bench, each with a fixed repository snapshot and extracted paper text (`sources.json`). Humanity's Last Exam was added on the author's decision of 31 October 2026; no framework author has reviewed it, so it has no earlier review, and its dataset is gated on Hugging Face and not in the code repository; the author obtained the dataset file under its access terms and `export_hle_text.py` wrote a text export of the question file into the snapshot's repository tree (`repository/data/hle-test.jsonl`, 2,500 rows, images dropped, author names omitted) so the file server can serve it; the parquet file and the export are gitignored and excluded from the public package; the public dataset card text is supplied as a third source, `dataset-card.md`. HELM was fetched and then removed on 31 October 2026: its 162 page paper made every prompt about 167 thousand tokens, and both of its earlier reviews were made from the paper alone. Six frameworks are applied: BetterBench, the ECBD worksheet, the Scorecard of AI Benchmark Quality and the OECD facets on all four; How2Bench on HumanEval; the Agentic Benchmark Checklist on τ-bench. Benchmark Caliper stays in the mapping and the coverage table but has no benchmark in the study, because its only earlier review in the set was HELM. The new rubric runs on all four benchmarks, twice. Eighteen framework sessions and eight rubric sessions make 26 main sessions, run once each in the order of `jobs.json` (randomized within blocks with the recorded seed). Seven pilots, one per prompt, on the fictional AddTwo fixture. Attempt cap 36, counting pilots and retained failures.

## Instrument and inputs

Each session receives: the study system instruction; one framework packet with the framework's own items verbatim and a short guidance paragraph; the teaching example; the paper text and the top level README; and a confined file server over the repository snapshot with two tools, list files and read file. It cannot execute code, browse, write files or read anything outside the snapshot. The response is structured output against the framework's schema: one record per item with the framework's own answer, the basis of the answer (evidence found, absence of information, defect found, not applicable), a reason, source locations with short quotes, what was missing and the checks performed. The rubric response adds eight description facets before the judgments.

Input sizes were measured (`sizes.csv`): the largest prompt is about 44 thousand tokens by a four characters per token estimate. The runner sets the auto compaction window to its maximum so that supplied text is not summarized away. No per session token, output, tool call or time ceilings are set.

## Model and isolation

Requested model `claude-sonnet-5-5` at medium effort through Claude Code. The returned model identifier in the event log is recorded per attempt; the requested identifier does not prove the serving snapshot. Each session runs `claude -p` in an empty temporary directory with the prompt on standard input, the default system prompt replaced, no user or project settings, no skills, no built in tools, only the study file server, permission prompts denied. The existing local Claude Code login is used; no API key passes into the session.

## Checks before the sessions

Ten checks in order, each with a pass condition; main sessions do not start until all pass. Status at the time of writing:

| Check | Status |
|---|---|
| 1 Materials and reuse terms | done; see `v4/mapping/questions.json` |
| 2 Answerability of every item | done; column in `questions.json`, reviewed and finalized by the author on 31 October 2026 |
| 3 Mapping and recoding finished; earlier reviews recoded | mapping final; recoding rules written; earlier reviews transcribed for BetterBench on HumanEval and TruthfulQA and for the checklist on τ-bench; only the BetterBench pair is compared with the agent's application, as a proof of concept that the prompting and the framework packet work; the checklist file is kept as reference data |
| 4 Snapshots fetched and frozen | done; `sources.json` |
| 5 Input sizes measured | done; `sizes.csv` |
| 6 Response schemas validated | done; `validate.py` accepts correct samples and rejects malformed ones (`test_harness.py`) |
| 7 Offline dry run | done; `synth.py` then `analyze.py --outputs dry-run` produced every table; the synthetic folders were deleted afterwards; repeated after HELM was removed |
| 8 Harness tests | done; nine tests pass |
| 9 Pilots on the fixture | done on 31 October 2026; seven pilots, seven attempts, all completed and structurally valid, every file server call succeeded, no other tool used, returned model `claude-sonnet-5-5` in every event log; no harness change |
| 10 Freeze and register | done on 31 October 2026 by `freeze.py`, after the pilots and before the first main session |

## Rubric derivation and outcomes

The new rubric was specified from the final question mapping and the frameworks' item specifications before any session and is frozen together with the Study 1 materials; Study 1 results do not shape it. Outcomes are three: favorable, unfavorable, unresolved. Partial is a marker on favorable; unresolved by rule and not applicable are markers too. Agreement is counted on the three outcomes with a stricter count beside it that also requires the partial marker to match. Three items among the applied frameworks that cannot be answered from the inputs (`BB-45`, `BB-46`, and `H2B-45`, plus three porting action items in unapplied Benchmark Caliper, `CAL-IC-4`, `CAL-OO-4`, and `CAL-OC-4`) are recorded but kept out of concern outcomes.

## Pilots and harness changes

A pilot is a full session on a fictional benchmark, the two task AddTwo fixture from the earlier study. Its prompt carries the complete framework packet, the same system instruction, the same schema and the same file server as a main session; only the benchmark is fictional and tiny. Pilots exist to catch harness, schema and tool failures before a real benchmark is spent on them, and their judgments are never analysed. Pilots are recorded under `outputs/pilot-*`. Any harness change made after the pilots is listed here before the freeze. Harness changes after the pilots: one. The first freeze manifest, written at 18:17 UTC on 31 October 2026, listed the mapping and rubric files by their path from the repository root, while `run.py` resolved every listed path from the study folder, so the first main session attempt stopped in the freeze check before any model call and before any output folder was created. `run.py` now resolves a listed path from the study folder and otherwise from the repository root; the first manifest was discarded and the freeze was run again. No prompt, material, source, schema or analysis file changed. The seven pilots ran on 31 October 2026 in 21 to 45 seconds each, each making two or three file server calls, and all seven responses passed `validate.py`. Framework packets, prompts and sources are never changed in response to pilot judgments.

## Hypotheses registered before the sessions

1. Frameworks agree on documentation presence and licensing and diverge on validity concerns.
2. Much of the disagreement on validity concerns comes from how each framework treats information the benchmark does not report, not from reading the benchmark differently.
3. Several concerns appear in only one framework (from the coverage table: maintenance in BetterBench, result presentation in How2Bench, the descriptive facets in the OECD framework).
4. Under the new rubric, items a benchmark does not report are recorded as insufficient evidence where BetterBench and How2Bench record a low score or a failure.
5. The rubric questions matching the OECD facets with low rater agreement (capability, coverage, specificity) are the ones whose ratings a person can least often confirm from the cited sources.

## Analysis

`analyze.py` only. Validation, citation checks (source exists, exact and whitespace normalized quote, locator resolves), tool use from the event log, recoding into outcomes with the markers, aggregation per concern with the final mapping, pairwise agreement per benchmark, agreement of the BetterBench agent application with the BetterBench authors' review on HumanEval and TruthfulQA, the missing information conflict count, rubric repeat agreement and the human source check list (`rq4-source-check.csv`, filled by the author after the sessions). No significance tests. No overall score.
