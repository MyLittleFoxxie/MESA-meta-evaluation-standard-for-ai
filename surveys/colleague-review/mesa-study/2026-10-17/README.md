# Archived, stopped design

The user selected a smaller 30-conversation design after this execution began. This series stopped scheduling and let active runs finish: 44 completed conversations through 45 physical attempts, including one retained service-failure retry. All records remain preserved. They are not pooled with the [final study](../main/README.md).

# MESA model study

This study uses MESA as one fixed 25-question questionnaire with its explanations, five answer choices, optional comments and no total quality score. The comparison methods are the original EFPA Test Review Model (EFPA-TRM) and general benchmark-review instructions. All use GPT-6.1 Sol, medium reasoning effort. Human ease of use and decision benefits are not measured.

## Materials and protocol

- [Questionnaire reading document](questionnaire.html): explanations are visible beside the questions; no expandable help, response fields, scripts, saving, tracking or submission.
- [Exact MESA text supplied to the model](materials/mesa.txt).
- [Protocol](protocol.md), [input freeze](freeze-manifest.json) and [source provenance](source-provenance.json).
- [180 planned conversations](jobs.json) and [exact prompts](inputs/).
- [Benchmark passages](materials/real-passages.txt), [eight-case set](materials/cases-eight.json), and [sixteen-case set](materials/cases-sixteen.json).
- [Expected answers](analyst/expected.json), never provided to reviewer conversations.
- [Fixed comparison checklist](analyst/real-comparison-checklist.json), used to examine the six neutral-first benchmark reviews.

Three methods × four reviewer instructions × five repetitions × three batches give 180 conversations. The batches review ARC-AGI-2 then DesignQA, classify 17 claims in eight cases, or classify 32 claims in sixteen cases. This gives 120 planned benchmark reviews and 2,940 repeated claim answers. Repeated answers are dependent outputs of one model, not independent people or cases. Both case sets have been used before; they are not new held-out evidence. The same assistant designed the cases, expected answers and analysis.

Each conversation starts without previous review history. Available settings disable project documents, memories, external search, shell access and multi-agent features. Platform instructions and pretrained knowledge remain possible influences. Backend model revision, temperature and generation seed are unavailable. Every original attempt, failure and permitted retry is retained. A completed invalid response is neither repaired nor replaced. The live survey and earlier studies remain unchanged.

## Results and records

- [Results summary](analysis/summary.md) and [machine-readable summary](analysis/summary.json).
- [All runs](analysis/runs.csv), [physical attempts](analysis/attempts.csv), [raw outputs](outputs/) and [launch settings](launches/).
- [Claim answers](analysis/claims.csv), [counts per conversation](analysis/case-runs.csv), [counts per case](analysis/case-families.csv), and [related-case comparisons](analysis/paired-cases.csv).
- [MESA choices](analysis/mesa-answers.csv), [choice distributions](analysis/mesa-distributions.csv), and [repeated-choice matches](analysis/mesa-agreement.csv).
- [Complete usable benchmark reviews](analysis/reviews.csv) and [closing notes](analysis/closing-notes.csv).
- [Input, preservation and accounting checks](analysis/verification.json).

While execution is in progress, derived summaries are partial. They must not be read as final study findings. The runner records missing and incomplete conversations explicitly.

## Reproduce offline calculations

From this directory:

```sh
python3 test_analysis.py
python3 analyze.py
python3 verify.py
```

These commands do not launch experiments. To continue an interrupted execution, `run_series.py --root <this-directory> --resume` schedules only jobs without an existing output directory. One retained retry is permitted only after an execution failure without any completed response or turn. See the protocol before using `retry_failed_once.py`.

Earlier studies remain archived in `simulation-study/` and `accessibility-study/v1/` beside this study's parent directory. Their observations are not pooled with this series. The archived names describe the experiments as they were run, not multiple current MESA instruments.

No LaTeX compilation or PDF preview is part of this study. Manuscript layout and page length remain unchecked.
