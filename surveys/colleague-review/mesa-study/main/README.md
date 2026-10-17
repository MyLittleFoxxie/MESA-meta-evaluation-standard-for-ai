# Archived, stopped series

This GPT-6.1 Sol series stopped on 17 October 2026 when the Codex account reached its usage limit: 20 of 30 conversations completed, `real-ordinary-neutral-1` failed without a response (usage-limit error, kept unchanged) and nine jobs were never attempted. The `analysis/` files are partial snapshots taken during execution. All records remain preserved. The user then asked for the whole design to be run again with Claude Sonnet 5.5; that complete series is in [`../claude-sonnet-5-5/`](../claude-sonnet-5-5/README.md). Nothing here is pooled with it.

# MESA model study

This study uses one fixed MESA questionnaire: 25 questions, six domains, five choices, explanations, optional comments and no total quality score. GPT-6.1 Sol, medium reasoning effort, reviews without an assigned identity. The comparison methods are the original EFPA Test Review Model (EFPA-TRM) and general benchmark-review instructions.

The study has **30 planned conversations**: five benchmark-review conversations and five separate test-case conversations for each method. Each benchmark conversation reviews ARC-AGI-2 then DesignQA. Each test-case conversation assesses all 24 constructed descriptions and their 49 claims. Planned totals are 30 benchmark reviews, ten MESA questionnaires, 250 MESA answer choices and 735 repeated claim answers. These are dependent outputs of one model, not independent participants or 735 distinct test cases.

## Materials

- [Questionnaire reading document](questionnaire.html): visible explanations beside the 25 questions, without expandable help, response fields, scripts, saving, tracking or submission.
- [Exact MESA instrument](materials/mesa.txt), [benchmark passages](materials/real-passages.txt), and [constructed cases](materials/test-cases.json).
- [Protocol](protocol.md), [input freeze](freeze-manifest.json), [all jobs](jobs.json), and [exact inputs](inputs/).
- [Expected answers](analyst/expected.json): labels and reasons withheld from reviewer conversations.
- [Six-review comparison checklist](analyst/real-comparison-checklist.json), fixed before execution.

Every method receives the same benchmark descriptions, intended uses, cases and common output requirements. MESA alone receives its explanations and HLE example; EFPA-TRM receives its complete 90-page source text. The complete supplied materials are compared, not questionnaire wording in isolation. The cases and expectations have already been used and were prepared by the same assistant; they are not new independent tests.

Each conversation starts without previous review history. Available settings disable project documents, memories, external search, shell and multi-agent features. Expected answers, organizer notes and previous responses are not supplied to reviewers. Platform instructions and pretrained knowledge remain possible influences. Backend revision, temperature and generation seed are unavailable.

## Results and records

- [Summary](analysis/summary.md) and [structured summary](analysis/summary.json).
- [All runs](analysis/runs.csv), [physical attempts](analysis/attempts.csv), [raw outputs](outputs/), and [launch settings](launches/).
- [Claim answers](analysis/claims.csv), [per-conversation counts](analysis/case-runs.csv), [per-case counts](analysis/case-families.csv), and [related-claim comparisons](analysis/paired-cases.csv).
- [MESA choices](analysis/mesa-answers.csv), [distributions](analysis/mesa-distributions.csv), and [repeated-choice matches](analysis/mesa-agreement.csv).
- [Complete usable benchmark reviews](analysis/reviews.csv), [closing notes](analysis/closing-notes.csv), and [six selected reviews](analysis/selected-reviews.md).
- [Preservation and accounting checks](analysis/verification.json).

During execution, derived summaries are partial and must not be read as final findings. Completed invalid responses are retained without repair or replacement. A single separately retained retry is permitted only for an execution failure without a completed response or turn.

## Reproduce offline calculations

```sh
python3 test_analysis.py
python3 analyze.py
python3 render_audit.py
python3 verify.py
```

These commands do not launch model reviews or submit survey answers. The execution runner schedules unattempted jobs using `run_series.py --root <this-directory> --resume`. Follow the protocol before using `retry_failed_once.py` for the one permitted infrastructure retry.

## Archived studies

The [stopped larger design](../2026-10-17/README.md) completed 44 conversations before the user selected this smaller design. All its outputs remain preserved. None is reused or pooled here: all 30 conversations in this study are fresh. Earlier records in `simulation-study/` and `accessibility-study/v1/` are also preserved separately. Historical record names do not define multiple current MESA instruments.

Human interpretation, effort, perceived ease and decision benefits remain future research for CHASE and planned evaluation for REFSQ. No LaTeX compilation or PDF preview is performed; manuscript layout and page length remain unchecked.
