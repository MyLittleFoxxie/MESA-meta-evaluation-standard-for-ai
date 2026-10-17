# Recorded simulation results

Attempted 120 / 120 planned runs; 14 eligible for quantitative analysis.

| Batch | Condition | Role | Eligible/planned | Controlled matches/valid probes |
|---|---|---|---:|---:|
| controlled | efpa | benchmark_reviewer | 1/5 | 17/17 |
| controlled | efpa | neutral | 0/5 | 0/0 |
| controlled | efpa | newcomer | 0/5 | 0/0 |
| controlled | efpa | research_assistant | 0/5 | 0/0 |
| controlled | mesa | benchmark_reviewer | 2/5 | 34/34 |
| controlled | mesa | neutral | 2/5 | 34/34 |
| controlled | mesa | newcomer | 0/5 | 0/0 |
| controlled | mesa | research_assistant | 0/5 | 0/0 |
| controlled | ordinary | benchmark_reviewer | 0/5 | 0/0 |
| controlled | ordinary | neutral | 0/5 | 0/0 |
| controlled | ordinary | newcomer | 0/5 | 0/0 |
| controlled | ordinary | research_assistant | 0/5 | 0/0 |
| real | efpa | benchmark_reviewer | 2/5 | 0/0 |
| real | efpa | neutral | 0/5 | 0/0 |
| real | efpa | newcomer | 1/5 | 0/0 |
| real | efpa | research_assistant | 1/5 | 0/0 |
| real | mesa | benchmark_reviewer | 0/5 | 0/0 |
| real | mesa | neutral | 1/5 | 0/0 |
| real | mesa | newcomer | 0/5 | 0/0 |
| real | mesa | research_assistant | 1/5 | 0/0 |
| real | ordinary | benchmark_reviewer | 2/5 | 0/0 |
| real | ordinary | neutral | 0/5 | 0/0 |
| real | ordinary | newcomer | 1/5 | 0/0 |
| real | ordinary | research_assistant | 0/5 | 0/0 |

MESA choices are categories, not quality scores. Controlled matches refer only to the frozen fictional-case key. Missing and invalid runs are excluded and reported separately, not silently marked correct or incorrect.

## Limits

- Execution is incomplete: failed, running, or unattempted jobs limit model confirmation and condition comparisons.
- Only process-completed, turn-completed, wholly schema-valid responses without observed tool use enter quantitative tables. All excluded and unattempted runs remain in runs.csv.
- No independence assumed across items, pairs, or repeated runs. No inferential significance tests.
- Exact quotes are whitespace-normalized substring checks, not semantic support judgments.
- Numbered EFPA item mentions are lexical observations, not evidence of a complete EFPA review. Summaries or headings alone do not establish full application.
- Real-case conclusions have no correctness key and require qualitative examination.
- Same assistant designed and analyzed this study; no independent human validation.

## Files

`runs.csv` contains every planned run and validation errors. `controlled_probes.csv` contains each eligible probe and its quote check. `controlled_run_scores.csv` preserves the session as the analysis unit. `controlled_contrasts.csv` compares labels within eligible sessions against the frozen paired-case design without judging prose. `mesa_distributions.csv` includes all five categories, including zero counts. `mesa_agreement.csv` reports within-role and matched-repeat cross-role pairs; pairs are dependent. `conclusions.csv` and `instrument_reviews.csv` retain prose for qualitative inspection.
