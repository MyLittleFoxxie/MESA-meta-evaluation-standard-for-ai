# MESA model-review study

MESA is the 25-question questionnaire. The study compares its application with the original EFPA Test Review Model 2025 and competent ordinary review instructions.

## Records and model series

- `freeze-manifest.json`, `jobs.json`, `inputs/`, `materials/`, and `analyst/expected.json`: original frozen inputs and expected fictional labels.
- `outputs/` and `analysis/`: interrupted Astra series. All 120 jobs were attempted; 14 processes completed and 106 failed. Infrastructure failures are not wrong review judgments.
- `series/gpt-6.1-sol/`: separate, user-requested Sol series. Its manifest records identical source inputs and expectations. All 120 jobs completed on 15 October 2026 after five retained infrastructure retries (125 physical attempts). Two completed EFPA outputs failed the required structure, leaving 118 eligible sessions. See that series' `analysis/summary.md` for results and exclusions.
- `analyst/sol-series-amendment.md`: explanation of the model change and bounded scheduler.
- `analyst/standards-assessment.md`: ACM SIGSOFT method requirements, implementation, and unresolved limits.
- `analyst/adaptation-map.md`: proposed correspondence for all 25 questionnaire items.
- `analyst/real-comparison-guide.md`: fixed small sample and passage-based criteria for qualitative examination.

The intended complete series has 60 real-passage sessions and 60 separate fictional-case sessions (3 conditions × 4 instruction groups × 5 repeats in each batch). Each real session reviews ARC-AGI-2 then DesignQA. Each fictional session has 8 cases and 17 statement classifications. MESA's real subset has 1,000 planned categorical selections. These are model outputs, not participants.

## Reproduce offline analysis

From the repository root:

```sh
python3 surveys/colleague-review/simulation-study/test_analysis.py
python3 surveys/colleague-review/simulation-study/analyze.py
python3 surveys/colleague-review/simulation-study/verify_study.py
python3 surveys/colleague-review/simulation-study/analyze.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol
python3 surveys/colleague-review/simulation-study/verify_study.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol
```

`summary.json` reports planned, attempted, eligible, and failed counts. `runs.csv` lists every planned session. Controlled counts refer to the frozen researcher-defined key, not a validated benchmark quality scale. Native text and common conclusions are preserved for examination; exact lexical item mentions or quote matches are not semantic correctness checks.

## Execution commands (completed series)

The Sol series is complete. The resume command below now schedules zero jobs. Use it only for an interrupted series when no other runner is using that series:

```sh
python3 surveys/colleague-review/simulation-study/run_series.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol --workers 3 --resume
```

The command uses the requested `gpt-6.1-sol` model and existing Codex authentication, creates fresh sessions, and saves raw records. It skips any previously attempted job and does not overwrite responses. It stops scheduling if a process fails; active jobs finish. It does not silently retry a failed or malformed response. Any permitted retry requires a separately retained attempt and documented handling.

A retry eligible under the protocol is executed separately, for example:

```sh
python3 surveys/colleague-review/simulation-study/retry_failed_once.py --root surveys/colleague-review/simulation-study/series/gpt-6.1-sol --job real-mesa-research_assistant-3
```

This command refuses an existing second attempt or a completed original response. Do not rerun it after the attempt has been recorded. `analysis/physical_attempts.csv` accounts for every execution; `analysis/runs.csv` accounts for planned jobs and identifies the selected attempt. Neither table treats an infrastructure failure as an incorrect judgment.

Do not rebuild frozen inputs after execution. A changed study needs its own version and manifest. The original raw records are immutable research data; derived analysis can be regenerated. No command sends a participant survey submission.

## Sources and limitations

The original 90-page EFPA source is attributed in `materials/efpa-original.txt` and is licensed CC BY-SA 4.0. The source PDF is authoritative; text extraction loses visual layout. MESA and real passages derive from the identified survey packet, whose canonical files remain unchanged. Reading content is text-only, including textual diagram descriptions.

The assistant helped prepare materials, conduct sessions, analyze outputs, and draft the manuscript. Model roles are instructions, not verified human perspectives. The cases and expected labels lack independent validation; no human comprehension, usefulness, review duration, or decision improvement was measured. An incomplete additional model series is not complete second-model confirmation.

The repository-level [CHASE study guide](../../../CHASE-study.md) links the materials, results, and calculations cited by the paper. No LaTeX compilation or automatic PDF preview is part of these checks.
