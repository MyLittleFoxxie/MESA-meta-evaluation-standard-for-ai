# Study Cycle 2 Protocol (MESA Rubric v5)

## Purpose

Study Cycle 2 extends Study 2 of the MESA paper in a separate directory (`v5/study-cycle2/`) while preserving `v4/` and `v5/study/` byte for byte:

1. **Second model family (`C2-1`):** Run the 8 main rubric sessions (4 benchmarks: `humaneval`, `truthfulqa`, `hle`, `tau-bench`, 2 repeats each) with `gemini-3.8-flash-medium` through `agy` at `medium` effort, using the same read-only MCP file server (`file_server.py`), system prompt (`materials/system.txt`), teaching example (`materials/example.txt`), and JSON schema (`materials/schema-RUBRIC.json`) as the Claude Sonnet 5.5 (`claude-sonnet-5-5`, `medium` effort) sessions in `v5/study/`.
2. **Reference standard by construction (`C2-2`):** Build 6 copies of the fictional `AddTwo` fixture (`sources/addtwo-*`):
   - `addtwo-b28a`: test runner executes model submission in the shared grading namespace (`B28a` `contradicted` / `failed`),
   - `addtwo-b07`: scorer accepts a wrong answer within $\pm 1$ (`B07` `contradicted` / `failed`, `accepts_wrong`),
   - `addtwo-b05`: manual answer key records `2+2 = 5`, rejecting the correct answer `4` (`B05` `contradicted` / `failed`, `rejects_correct`),
   - `addtwo-license`: `repository/LICENSE` is a proprietary all-rights-reserved license contradicting the `CC0 1.0` claim in `paper.txt` and `README.md` (`B19` `contradicted` / `failed`),
   - `addtwo-missing-count`: task count and task list omitted from `paper.txt`, `README.md`, and `score.py` (`B04` `undocumented` / `absence_of_information`),
   - `addtwo-clean`: clean control copy with no planted defect and documented task count (`n = 2`).
   Run the rubric on each copy twice with both `claude-sonnet-5-5` (`medium`) and `gemini-3.8-flash-medium` (`medium`) ($6 \times 2 \times 2 = 24$ seeded sessions). Report detection rate (sensitivity) and false-alarm rate per criterion and pooled across criteria.
3. **Known defects from the literature (`C2-3`):** Pre-register 7 published, located defects of the four benchmarks in `known_defects.json` before the sessions and report how many each model family found.
4. **Executed confirmation of located defects (`C2-4`):** For every rating with level `contradicted` or outcome `failed` in Cycle 1 and Cycle 2, run an isolated script (`confirm_defects.py`) without network access that demonstrates the defect or verifies the contradiction against the frozen snapshot, and record the result in `analysis/executed-confirmations.json`.
5. **Blind author rating (`C2-5`):** Draw a deterministic sample (seed `20261111`: 72 of 143 Study 1 disagreements, 62 of 248 Part B ratings stratified by benchmark and level, and all 64 Part A classifications) into a blind rating checklist (`blind_author_sheet.json`) that hides the model's labels until the author completes the ratings, then compute raw agreement and Cohen's $\kappa$ with 10,000-resample bootstrap 95% confidence intervals.
6. **Pre-frozen statistical analysis (`C2-6`):**
   - 10,000-resample bootstrap 95% intervals (seed `20261111`) for every Krippendorff's $\alpha$ and Cohen's $\kappa$.
   - Part A agreement reported per field (`Purpose`, `Judgeability`, `Reference`, `Containedness`, `Objectivity`, `Autonomy`, `Progression`, `Variation`) as well as pooled.
   - Chance-corrected agreement (Krippendorff's $\alpha$ and pairwise Cohen's $\kappa$) for the 302 Study 1 framework pairs with a cluster bootstrap over `(benchmark, concern)` cells.
   - Same-measure Tier 2 comparison (`favorable`, `unfavorable`, `unresolved`) on HumanEval only, concern by concern, against the Study 1 repeats of BetterBench (21 concerns) and Safety-Critical Benchmark Scorecard (22 concerns), alongside the 4-benchmark figures. Disclose that this recoded comparison was designed after the Claude Cycle 1 results were known (post-hoc for Claude, prospective for Gemini).

## Session Isolation and Handling Rules

- Every session runs in an empty temporary directory with no project history, expected answers, or other reviewer outputs.
- Only `list_files` and `read_file` on the `benchmark` MCP server (plus `finish` / `StructuredOutput`) are permitted; a `PreToolUse` hook (`guard.py`) blocks all other tools in `agy`, and `--tools ""` / `--allowedTools` blocks all other tools in Claude Code.
- Every attempt is saved untouched under `outputs/<job-id>/attempt-<n>/`. Invalid JSON or schema errors allow at most one retry per job within the phase attempt cap (`12` for the 8 main sessions, `30` for the 24 seeded sessions).


## Gated HLE dataset files

Two gated Humanity's Last Exam dataset files recorded in `v4/study/freeze-manifest.json` and `v5/study/freeze-manifest.json` (`sources/hle/data/test-00000-of-00001.parquet` and `sources/hle/repository/data/hle-test.jsonl`) are gitignored and absent in this working tree. Cycle 1 logs (`v5/study/outputs/hle-RUBRIC-1` and `hle-RUBRIC-2`) show neither session read those files. `freeze.py` allows those two keys to be absent locally while checking SHA-256 hashes for all committed files and for those files whenever present.

## Amendment 1 (Claude CLI --json-schema flag fix before Claude seeded runs)

Before running the seeded Claude sessions (after the Gemini pilot and all 8 Gemini main sessions had already completed under original `freeze-manifest.json` SHA-256 `a20fbb8415ef794eb07c8c11688dcb034ba7d583165882a1df3bcbd97fcc1d55`), `--phase seeded` halted after `claude.exe` rejected the draft 2020-12 `"$schema"` metadata key in `--json-schema` before invoking any model (`nonzero_exit_1`, ~2-4s, 0 events). `run_claude_attempt` in `run.py` was updated to strip `"$schema"` in memory when constructing the CLI argument (matching `v5/study/run.py`), while leaving `materials/schema-RUBRIC.json` and all completed Gemini records unchanged. The 8 pre-model failure/interrupted directories (`addtwo-b28a-RUBRIC-claude-1/attempt-{1,2}`, `addtwo-b05-RUBRIC-claude-1/attempt-{1,2}`, `addtwo-clean-RUBRIC-claude-1/attempt-{1,2}`, `addtwo-license-RUBRIC-claude-1/attempt-{1,2}`) are retained intact, `run_one` excludes pre-model CLI-flag aborts from the per-job 2-attempt cap, `attempt_cap_seeded` in `jobs.json` was raised from `30` to `38` (+8 slots), and `freeze-manifest.json` was regenerated.

## Amendment 2 (Claude Pro 5-hour rate-limit 429 exclusion before final 3 seeded runs)

During seeded execution under Amendment 1 (`freeze-manifest.json` SHA-256 `a74a6174903e7b628d6b8ee2c2ab584f13c7d065a0d6cac6df1076889533231a`), 21 of 24 seeded sessions (9 Claude + all 12 Gemini) completed valid on first model call, while the remaining 3 Claude repeat-2 jobs (`addtwo-license-RUBRIC-claude-2`, `addtwo-missing-count-RUBRIC-claude-2`, `addtwo-b07-RUBRIC-claude-2`) hit Claude Pro's 5-hour session rate limit (`api_error_status: 429`, resetting 6:30 PM America/Toronto) on `attempt-1` and `attempt-2` with zero input/output tokens. Those 6 rate-limited attempt directories are retained untouched, `run_one` in `run.py` excludes `429` session-limit aborts from the per-job 2-model-attempt cap, `attempt_cap_seeded` in `jobs.json` was raised from `38` to `44` (+6 slots), and `freeze-manifest.json` was regenerated prior to completing those 3 jobs after the limit reset.
