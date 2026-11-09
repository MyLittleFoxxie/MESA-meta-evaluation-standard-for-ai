# MESA as a standard for comparing benchmark reviews

Current manuscript: [mesa_paper.tex](../mesa_paper.tex), intended for REFSQ in Springer LNCS format. It uses the mapping and the Study 1 records here; its rubric study (Study 2 in the paper) is `../v5/study/`, and it adds a requirements traceability proposal. The mapping has 30 comparison concerns; the derived rubric has eight description fields and 29 evaluation questions. Neither is the earlier 25 question questionnaire.

Study status recorded on 31 October 2026: all ten checks done, inputs frozen, seven pilots, 26 main sessions and two amendment sessions (`study/addition.md`) run and analysed. The RQ4 source check and RQ2 disagreement causes were coded by the preparing assistant; the recorded author review status is pending. Study paths, version identifiers, and frozen records are unchanged. Earlier manuscripts are indexed in the [consolidation record](../provenance/manuscript-consolidation-2026-11-03.md).

## The idea

Seven frameworks for reviewing an artificial intelligence benchmark already exist: BetterBench, the ECBD worksheet, the Scorecard of AI Benchmark Quality, How2Bench, the Agentic Benchmark Checklist, Benchmark Caliper and the OECD facets. They ask overlapping questions in different words, on different scales, and treat information a benchmark does not report differently. Nobody has applied two of them to the same benchmarks. Medicine compares its appraisal tools on the same studies as a matter of routine; benchmark review cannot, because it has no common vocabulary.

MESA, the Meta-Evaluation Standard for AI, is that vocabulary: a list of shared concerns that every framework's questions map onto; three outcomes, favorable, unfavorable and unresolved, into which any answer is recoded; an evidence record per judgment; and a description of the benchmark, with the OECD facets, that says which concerns apply. Two studies use it.

Study 1 compares the seven frameworks. Coding agents apply each framework to four benchmarks, three of which the framework authors reviewed earlier, and the mapping lets the outcomes be compared per concern, with the earlier reviews as reference points.

Study 2 applies a derived rubric specified from the mapping and the frameworks' item specifications before any session: a description part from the OECD facets, then one evidence question per shared concern. Agents apply it twice to the same four benchmarks, and every rating is checked against the cited sources.

## Research questions

1. Which concerns do existing benchmark review frameworks cover?
2. Do the frameworks agree when applied to the same benchmark?
3. How does each framework treat information that a benchmark does not report?
4. When a rubric is derived from the existing frameworks, do its ratings hold up when the cited sources are checked?

## Benchmarks and frozen snapshots

Four benchmarks plus one fictional pilot fixture (`AddTwo`), frozen under `study/sources/` (metadata in `study/sources.json` and `study/sizes.csv`):

| Benchmark | Commit (prefix) | Retrieved (UTC) | Earlier reviews | Paper pages | Paper chars | Repo files | Repo text bytes | Prompt size across sessions (chars / est. tokens) |
|---|---|---|---|---:|---:|---:|---:|---|
| HumanEval | `b9453e8f18` | 2026-10-30 | BetterBench (`BB-humaneval.json`, 47 items), How2Bench (aggregate) | 35 | 154,877 | 12 | 19,482 | 165,396–176,659 chars (41,349–44,164 tokens) |
| TruthfulQA | `d71c110897` | 2026-10-30 | BetterBench (`BB-truthfulqa.json`, 47 items) | 39 | 131,273 | 25 | 19,056,953 | 148,706–159,969 chars (37,176–39,992 tokens) |
| Humanity's Last Exam (HLE) | `22ed3074b1` | 2026-10-31 | None | 29 | 107,586 | 16 | 66,510 | 115,700–126,963 chars (28,925–31,740 tokens) |
| τ-bench | `59a200c6d5` | 2026-10-31 | Agentic Benchmark Checklist (`ABC-tau-bench.json`, 31 of 44 items) | 50 | 130,308 | 113 | 61,747,798 | 144,226–155,489 chars (36,056–38,872 tokens) |
| Pilot fixture (`AddTwo`) | Local fixture | 2026-10-31 | None (pilots only) | 1 | 357 | 2 | 357 | 6,088–17,351 chars (1,522–4,337 tokens) |

### Code-level and packaging specifics documented in the repository

- **HumanEval (`b9453e8f18`):** Repository snapshot includes `human_eval/execution.py`, where candidate code executes via `exec(check_program, exec_globals)` inside a reliability guard while `README.md` states execution is commented out. Six of seven HumanEval sessions called `read_file` on `human_eval/execution.py`; rubric repetition 2 recorded the contradiction on `B28`.
- **TruthfulQA (`d71c110897`):** Repository snapshot includes evaluation datasets, legacy `v0`/`v1` files, `evaluate.py`, and `truthfulqa/metrics.py` (where the BLEU/ROUGE scoring function appends the best reference answer to the list of additional correct references if absent). Only the BetterBench session read a repository file (`evaluate.py`); no session opened `truthfulqa/metrics.py`.
- **Humanity's Last Exam (`22ed3074b1`):** Code repository (`github.com/centerforaisafety/hle`, 16 files including `hle_eval/run_judge_results.py`, `hle-rolling-changes.txt`, `docs/evaluation-with-tools.md`, `LICENSE`, `citation.txt`) is distributed separately from the gated Hugging Face dataset (`cais/hle`, revision `5a81a4c727`). The author obtained `data/test-00000-of-00001.parquet` (2,500 rows) under its access terms and ran `study/export_hle_text.py` to generate a local text export (`repository/data/hle-test.jsonl`, 2,500 rows with image bytes and author names omitted) alongside `dataset-card.md`. Both the parquet file and `hle-test.jsonl` are excluded via `.gitignore`, with SHA256 digests recorded in `study/sources.json`. Inspection of all six HLE session event logs (`study/outputs/hle-*/attempt-1/events.jsonl`) verified that **none of the six HLE sessions called `read_file` on `data/hle-test.jsonl`** (they only called `list_files` and read `hle_eval/run_judge_results.py`, `LICENSE`, `citation.txt`, `docs/evaluation-with-tools.md`, and `hle-rolling-changes.txt`), so `events.jsonl` and `response.txt` contain no gated question text and remain safe for the public replication package.
- **τ-bench (`59a200c6d5`):** Repository snapshot includes 113 files (environment, tool and task definitions, `setup.py`, and historical trajectory logs). Only the Checklist session read repository files (`setup.py`).
- **HELM:** Fetched and removed on 31 October 2026 before freeze because its 162-page paper produced ~167,000-token prompts and its earlier reviews were paper-only.

## Frameworks and where each applies

| Framework | Applied to |
|---|---|
| BetterBench, ECBD, Scorecard, OECD facets | all four |
| How2Bench | HumanEval |
| Agentic Benchmark Checklist | τ-bench |
| Benchmark Caliper | none; mapped for coverage only |

Sessions: 18 framework and benchmark pairs plus the derived rubric twice on four benchmarks (26 main sessions), plus 7 pilots on the fictional `AddTwo` fixture, plus 2 post-hoc amendment sessions (`study/addition.md`: a second repetition of BetterBench and the Scorecard on HumanEval). One configuration: Claude Sonnet 5.5 (`claude-sonnet-5-5`) through Claude Code (`claude -p`) at `medium` effort, validated via `--json-schema`, with only two read-only MCP tools exposed (`list_files` and `read_file` served by `study/file_server.py`). Paper text is extracted with `PDFKit` (`study/pdftext.swift`).

## Terms used in the v4 records and earlier manuscripts

| Paper term | Record name |
|---|---|
| criterion (C01 to C30) | concern in `mapping/concerns.md`, `mapping.csv` and `analysis/*.csv` |
| evidence: documented, undocumented, contradicted, not applicable | `basis`: `evidence_found`, `absence_of_information`, `defect_found`, `not_applicable` |
| verdict: met, not met, open | `outcome`: `favorable`, `unfavorable`, `unresolved` |
| qualifier: in part, undocumented, not applicable, descriptive | `marker`: `partial`, `unresolved_by_rule`, `not_applicable`, `description` |
| rubric levels: claimed, documented, verified, contradicted, undocumented, not applicable | `stated`, `shown`, `checked`, `contradicted`, `insufficient_evidence`, `not_applicable` in `materials/rubric.json` and the responses |
| source check findings: confirmed, overstated, not confirmed, absence plausible, absence contradicted | `verdict` in `analysis/source-check.csv`: `supported`, `weaker`, `not_supported`, `absence_plausible`, `absence_contradicted` |
| disagreement causes: item granularity, rule for undocumented items, reading of the criterion, threshold, sources read | `cause` in `analysis/disagreement-log.csv`: `granularity`, `missing_rule`, `reading`, `threshold`, `sources` |

## Files

| File | Content |
|---|---|
| `mapping/build_questions.py`, `mapping/questions.json` | every item of the seven frameworks, 280 in all, with answer scale, source location, reuse terms and `answerable_from_inputs` (`yes`: 238, context-dependent Caliper items: 25, `partly`: 11 [`BB-24`, `BB-30`, `SC-50`, `H2B-41`, `H2B-42`, `ABC-T.10`, and 5 OECD judgment facets], `no`: 6 [`BB-45`, `BB-46`, `H2B-45`, `CAL-IC-4`, `CAL-OO-4`, `CAL-OC-4`]) |
| `mapping/concerns.md` | the shared concern list, 30 rows, reviewed and finalized by the author |
| `mapping/build_mapping.py`, `mapping/mapping.csv` | item to concern mapping; carries `assistant_draft`, `author` and `final` columns with reconciliation notes on all 100 differences |
| `mapping/recoding-rules.md` | the three outcomes per answer scale, with `partial` and `unresolved_by_rule` markers |
| `mapping/check.py`, `mapping/coverage.md`, `mapping/coverage.tex` | checks and the coverage table (RQ1) |
| `rubric/rubric-draft.md`, `study/materials/rubric.json` | the derived rubric, specified from the final mapping and item specifications, with lineage |
| `study/` | the agent study: snapshots (`sources/`), materials (`materials/`), prompts (`prompts/`), schemas, `jobs.json`, `earlier-reviews/`, `run.py`, `run_addition.py`, `validate.py`, `analyze.py`, `disagreements.py`, `test_harness.py`, `freeze.py`, `freeze-manifest.json`, `protocol.md`, `addition.md`, `outputs/` and `analysis/` (`paper-grid-*.tex`, `pairwise.tex`, `disagreement-log.csv`, `rq3-conflicts.csv`, `source-check.csv`, `addition-repeat.json`); see `study/README.md` |
| [mesa_paper.tex](../mesa_paper.tex) | Current MESA manuscript for REFSQ |
| `../figures/v4_study1_diagram.*`, `../figures/v4_study2_diagram.*` | the two study figures |
| `../figures/v4_chase_design.*` | the CHASE study design figure, coloured by role (render steps in the SVG comment) |

Run `python3 v4/mapping/build_questions.py`, `python3 v4/mapping/build_mapping.py` and `python3 v4/mapping/check.py` from the repository root. None makes a model call.

## Public package and licensing notes

The author is the only person on the project. The mapping is the author's, checked against the assistant draft. Verbatim framework items are used in prompts and kept in these files. The public package carries verbatim text where a license allows it (BetterBench assessments from `betterbench.stanford.edu/database.html`, the 2022 OECD workshop paper) and where the framework authors gave the author permission to use their repository files (ECBD template, the checklist's `ABC.md`, Caliper's framework and prompt files; permission given 31 October 2026). How2Bench items and the OECD chapter text appear as paraphrases with source locations.
