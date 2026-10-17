# Manuscript results and source records

Finalized 15 October 2026. This record links the observed claims in `paper_chase.tex` to retained data. Paths below are relative to `simulation-study/`. Machine counts and assistant interpretations have different evidential status. Neither is independent human validation.

| Manuscript claim | Record and calculation |
| --- | --- |
| 120 planned and completed Sol jobs; 125 physical attempts; five infrastructure failures and five retained retries | `series/gpt-6.1-sol/analysis/summary.json`, `runs.csv`, `physical_attempts.csv`; all 120 selected statuses are process_completed, while physical statuses are 120 completed + five failed |
| 118 eligible: 58 real sessions and 60 controlled sessions | Same summary/groups and `runs.csv`; 20 MESA + 18 EFPA + 20 ordinary real sessions; all 20 sessions per controlled condition |
| Two excluded completed responses | `outputs/real-efpa-research_assistant-{2,4}/response.txt` within the Sol series; exact field errors in `analysis/runs.csv`. Raw objects retained; no repair or replacement |
| 124 distinct threads and no observed tools | Sol `analysis/verification.json`; thread IDs in each attempt's metadata and independent event-log check. One interrupted launch has no recorded thread ID |
| 1,020/1,020 expected controlled labels, 340 per condition; each of 60 sessions matches 17/17 | Sol `analysis/controlled_probes.csv`, `controlled_summary.csv`, `controlled_run_scores.csv`; expected key frozen in `analyst/expected.json` within the series |
| 420/420 paired contrasts and 1,020/1,020 quote substrings | Sol `analysis/controlled_contrasts.csv` (`both_match_key`) and `controlled_probes.csv` (`quote_substring`). These are label/substring checks, not judgments of all prose |
| 1,000 MESA selections; 12 variable question–benchmark combinations and 34 variable role–question–benchmark combinations | Sol `analysis/mesa_answers.csv`, `mesa_distributions.csv`, `writing-facts.json`; each 20-run pool has 25 questions × two benchmarks; four roles × 50 combinations |
| ARC Q8: 12 Yes/eight Partly; DesignQA Q12: nine Yes/eleven Partly; ARC Q11: 17 Partly/three Not sure | Sum role rows for each item in Sol `analysis/mesa_distributions.csv`; all other choices zero for these examples |
| Pair agreement 462, 464, 448, 458 out of 500 by neutral, newcomer, research assistant, benchmark reviewer | Sol `analysis/mesa_agreement.csv`, within_role rows. Sum matching pairs over 50 question–benchmark combinations; five repetitions give ten dependent pairs per combination |
| Forty closing notes, five questioning experimental phrase | `analysis/closing-notes-audit.md`, verbatim notes with run, benchmark and chosen attempt. Experimental wording is absent from canonical questionnaire |
| Fixed six-review substantive examples, EFPA transformations and classifications needing qualification | `analysis/qualitative-comparison.md`, with exact quotations and IDs; selected Sol neutral repetition 1 in all three conditions. Twelve passage concerns fixed in `analyst/real-comparison-guide.md`; full outputs inspected. Coverage of every original EFPA requirement is not certified |
| Incomplete Astra series: 14 complete, 106 failed, no pooled confirmation | Root `analysis/summary.json` and root `outputs/`; distinct from Sol subdirectory |
| Conceptual correspondence and omissions | `analyst/adaptation-map.md`; proposed mapping to original EFPA, not an observed historical derivation |

The input freeze precedes runs in each series. All original prompts and expected labels remain unchanged. The manuscript preserves a pending anonymized artifact location. No human study, independently checked answer key, complete second-model confirmation, layout check, or page-length measurement is claimed.
