# MESA model study: Claude Sonnet 5.5

This study uses one fixed MESA questionnaire: 25 questions, six domains, five choices, explanations beside each question, optional comments and no total quality score. Claude Sonnet 5.5 (`claude-sonnet-5-5`), medium effort, reviews with no assigned identity. The comparison methods are the original EFPA Test Review Model (EFPA-TRM) and general benchmark-review instructions.

The study has **30 planned conversations**: five benchmark-review conversations and five separate test-case conversations for each method. Each benchmark conversation reviews ARC-AGI-2 then DesignQA. Each test-case conversation assesses all 24 constructed descriptions and their 49 claims. Planned totals are 30 benchmark reviews, ten MESA questionnaires, 250 MESA answer choices and 735 repeated claim answers. These are dependent outputs of one model, not independent participants or distinct test cases.

This series repeats the design of [`../main/`](../main/README.md), which ran with GPT-6.1 Sol and stopped at a Codex usage limit. Inputs, materials, expected answers and the comparison checklist are byte-identical copies; nothing from `main/` is reused or pooled. See the [protocol](protocol.md) amendment.

## Results

All 30 conversations completed on 17 October 2026 through 30 physical attempts; 28 met the format. See the [summary](analysis/summary.md), [structured summary](analysis/summary.json), [six selected reviews](analysis/selected-reviews.md) and the [CHASE study guide](../../../../CHASE-study.md#observed-results).

## Materials and records

- [Questionnaire reading document](questionnaire.html): visible explanations beside the 25 questions, without response fields, scripts, saving, tracking or submission.
- [Exact MESA instrument](materials/mesa.txt), [benchmark passages](materials/real-passages.txt), and [constructed cases](materials/test-cases.json).
- [Protocol](protocol.md), [input freeze](freeze-manifest.json), [all jobs](jobs.json), and [exact inputs](inputs/).
- [Expected answers](analyst/expected.json) and the [12-point comparison checklist](analyst/real-comparison-checklist.json), fixed before execution and withheld from reviewers.
- [All runs](analysis/runs.csv), [physical attempts](analysis/attempts.csv), [raw outputs](outputs/), and [launch settings](launches/). `launches/smoke-1-auth-failed/` and `launches/smoke-2/` are isolation checks before the freeze, not study conversations.
- [Claim answers](analysis/claims.csv), [per-conversation counts](analysis/case-runs.csv), [per-case counts](analysis/case-families.csv), and [related-claim comparisons](analysis/paired-cases.csv).
- [MESA choices](analysis/mesa-answers.csv), [distributions](analysis/mesa-distributions.csv), and [repeated-choice matches](analysis/mesa-agreement.csv).
- [Usable benchmark reviews](analysis/reviews.csv), [closing notes](analysis/closing-notes.csv), [selected-review observations](analysis/selected-review-observations.json) and the [DesignQA example](analysis/paper-observations.json).
- [Preservation and accounting checks](analysis/verification.json), [manuscript checks](analysis/manuscript-verification.json) and [traceability](analysis/manuscript-traceability.md).
- `analyst/before-*`: copies of `paper_chase.tex`, `README.md` and `CHASE-study.md` taken before this series updated them.

Completed invalid responses are retained without repair or replacement. A single separately retained retry is permitted only for an execution failure without a completed response or turn; none was needed.

## Reproduce offline calculations

```sh
python3 test_analysis.py
python3 analyze.py
python3 render_audit.py
python3 verify.py
python3 verify_manuscript.py
```

These commands do not launch model reviews or submit survey answers. `run_series.py --root <this-directory> --resume` schedules only unattempted jobs; it needs a signed-in `claude` CLI.

Human interpretation, effort, perceived ease and decision benefits remain future research for CHASE and planned evaluation for REFSQ. No LaTeX compilation or PDF preview is performed; manuscript layout and page length remain unchecked.
