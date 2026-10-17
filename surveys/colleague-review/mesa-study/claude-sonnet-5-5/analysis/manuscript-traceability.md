# Manuscript traceability: paper_chase.tex → Claude Sonnet 5.5 records

Each number reported in `paper_chase.tex` and where it comes from. Paths are relative to this series folder. Interpretations are by the assistant conducting the study (Claude Code with Claude Opus 5.5).

| Paper statement | Value | Source |
| --- | --- | --- |
| Planned, attempted, completed conversations; physical attempts | 30, 30, 30; 30 | `analysis/summary.json` (`planned`, `attempted`, `completed`, `attempts`) |
| Responses meeting the format | 28 | `analysis/summary.json` `eligible`; `analysis/runs.csv` |
| Exclusions and reasons | `real-efpa-neutral-4` (invalid control character), `cases-ordinary-neutral-2` (case IDs; extra `R8`) | `analysis/runs.csv` `errors`; raw `outputs/*/response.txt` |
| Usable conversations per method and batch (Table `tab:usable`) | MESA 5/5, 5/5; EFPA-TRM 4/5, 5/5; general 5/5, 4/5 | `analysis/summary.md`, `analysis/runs.csv` |
| Expected claim answers matched | MESA 243/245, EFPA-TRM 237/245, general 191/196 | `analysis/summary.json` `cases.cases.*.matches/answers`; `analysis/claims.csv` |
| Conversations matching all 49 claims | MESA 3/5, EFPA-TRM 1/5, general 1/4 | `analysis/case-runs.csv` |
| 686 answers; 686 quotations found | 686; 686 | sum of `answers` and `quotes_found` in `analysis/summary.json` |
| 15 mismatches, all Contradicted for Not established | P6B 7 (MESA 1, EFPA-TRM 4, general 2); P5A 5 (MESA 1, EFPA-TRM 1, general 3); C6, C7, C8 in `cases-efpa-neutral-2` | `analysis/claims.csv` rows with `match` False |
| Quoted MESA reason "reads as not tested (strictly, not reported)" | — | `analysis/claims.csv`, `cases-mesa-neutral-1`, P5A claim1 |
| Related-claim comparisons | 322 total; 322 change/stability as expected; both labels expected MESA 113/115, EFPA-TRM 109/115, general 87/92 | `analysis/paired-cases.csv`; `analysis/summary.json` `paired_matches` |
| Unjustified negative claims supported | 0 of 84 (30 + 30 + 24) | `analysis/summary.json` `negative_opportunities`, `unjustified_negative_support` |
| MESA choices | 250; Yes 59, Partly 141, No 35, Not sure 15, Not applicable 0 | `analysis/mesa-distributions.csv` (role `all`) |
| Varying question–benchmark pairs (Table `tab:variation`) | 9 of 50; four between No and Not sure | `analysis/mesa-distributions.csv` |
| Repeated-choice matches | 456/500 (91.2%) | `analysis/mesa-agreement.csv`; `analysis/summary.json` `mesa.all` |
| DesignQA Q8 and Q12 choices and comments | Partly, Partly; comments quoted exactly | `outputs/real-mesa-neutral-1/response.txt`; `analysis/paper-observations.json` (checked by `verify_manuscript.py`) |
| All five MESA conversations chose Partly for DesignQA Q8 and Q12 | 5/5, 5/5 | `analysis/mesa-distributions.csv` |
| MESA closing notes: 5 of 10 name Q8 or Q12; overlaps 5/10 and 17/18; 3 DesignQA notes on Not sure | — | `analysis/closing-notes.csv` (`real-mesa-*`) |
| EFPA-TRM notes on 0 versus not applicable | 7 of 8 | `analysis/closing-notes.csv` (`real-efpa-*`; `real-efpa-neutral-5` DesignQA does not raise it) |
| General-instruction notes on the missing "completed review" and "assigned method" | 2 and 1 | `analysis/closing-notes.csv` (`real-ordinary-3`/`-4` DesignQA; `real-ordinary-5`) |
| Six selected reviews: checklist status | EFPA-TRM 12/12, general 12/12, MESA 10 addressed + 2 partly (points 3 and 11) | `analysis/selected-review-observations.json`, `analysis/selected-reviews.md` |
| Table `tab:review-tradeoffs` and RQ3 qualifications | quotations and EFPA-TRM item mappings | `outputs/real-{mesa,efpa}-neutral-1/response.txt`; `analysis/selected-review-observations.json` `qualifications` |
| ARC Q14: four No, one Not sure | — | `analysis/mesa-distributions.csv` |
| Model reported by every session | `claude-sonnet-5-5` | `outputs/*/metadata.json` `reported_model`; checked by `verify.py` |
| No tools offered or used | `init_tools` = [], `tool_items` = [] | `outputs/*/metadata.json`; checked by `verify.py` |
| Run date | 17 October 2026 (05:33–05:45 UTC) | `launches/*.json`, `outputs/*/metadata.json` |
