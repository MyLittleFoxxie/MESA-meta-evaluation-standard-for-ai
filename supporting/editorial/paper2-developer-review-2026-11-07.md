# Paper 2 protocol 5: developer review before the freeze (assistant review, 2026-11-07)

Written by an assistant subagent (Claude Code, Claude Opus 5.5) acting as a senior developer, at the author's request, before the protocol 5 freeze. It ran only read-only commands and the test suite. The text below is its report with repository paths made relative.

---

**Protocol 5 pre-freeze review: not ready to freeze.** The freeze step currently refuses, as designed: the `agy` `permission_flag` is `null` and none of the six forms is signed. Past that, three problems sit in files that become frozen and would make pilot results unreliable, and several more would make a session fail or be recorded wrongly.

Paths are relative to `/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai`. Short names: `S` = `paper2/preparation/sessions.py`, `SC` = `paper2/preparation/study_controls.py`, `TS` = `paper2/tests/test_sessions.py`, `AC` = `paper2/preparation/protocol-5/audit_checks`.

Besides the three allowed commands, I ran read-only checks: Python one-offs that only print, `git ls-tree`/`git grep` on the mirror, listings of `~/.gemini`, `/tmp` and the archive, and one `bash` test using only `sleep` to check process groups. `v4/mapping/check.py` rewrote `v4/mapping/coverage.md` and `coverage.tex`; git shows no content change.

## Blockers (fix before the freeze, because the fix touches frozen files or the pilot's validity)

**B1. The `agy` sandbox isolates nothing, and the rules don't treat that as invalid.**
- **What the check shows:** the `--dangerously-skip-permissions` check already exists (`AC/sandbox-check-agy-20261107T000829Z`). With `--sandbox` on, `curl https://example.com` returned the page, `ls ~` worked, the outside marker was read, and the inside write worked. The log says "enabling terminal sandbox" and `permission_mode: always-proceed`.
- **What the code does:**
  - Shell network commands only add text to the evidence (`S:82-83`, `S:465`). They never make a session invalid.
  - `agy` network is recorded as `not_observable` (`S:485-489`), although the check shows it open.
  - Outside tools are a deny-list (`S:54-56`). It misses `schedule`, `run_workflow`, `manage_inbox`, `manage_task`, `list_plugin_accounts` and `notebook_execution`, all auto-approved.
- **Failure:** `gh` is signed in and is even in the shared allow rules. An agent can run `gh pr diff 13798 -R sympy/sympy`, or `curl` a file from `raw.githubusercontent.com`, or run `pip install -U sympy`. It gets the fix and the session is recorded as valid.
- **Smallest fix:**
  - Set `permission_flag` to `--dangerously-skip-permissions` (`configurations.json:21`); `--mode accept-edits` was shown unusable.
  - Make network-marker hits invalidating, and add `gh `, `pip3 `, `python -m pip`, `uv `, `npm `, `api.github.com`, `githubusercontent`.
  - Record `agy` network as `violated`, citing the sandbox check.
  - Change `AGY_OUTSIDE_TOOLS` to an allow-list of local tools: `run_command`, `command_status`, `send_command_input`, `view_file`, `list_dir`, `find_by_name`, `grep_search`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `sed_file`, `wait*`, `finish`.

**B2. The leak rule matches only literal strings in tool-call inputs, and copies of the pilot fix are readable.**
- **Demonstrated:** I ran protocol 4 slot 01's transcript through `ORACLE_MARKERS`. The exact command that printed the reference patch, `grep -rn "mul_symbol" paper2/ literature/`, matches nothing.
- **Other bypasses:**
  - Wildcards and folder hops, for example `cd ~/paper2-ar*/pro*4/slot-01; git diff`.
  - `find ~ ... -exec grep`.
  - `~/.cache/huggingface/datasets/SWE-bench___swe-bench_verified`.
  - `~/.claude/projects/...` transcripts.
  - **`OLDPWD`:** `run.sh` is started from the repo root, so after `cd "$WS"` (`S:309`) the agent inherits `OLDPWD=<repo>`. I confirmed this. `cd -` then reaches the repo.
- **Unrecorded copy in `/tmp`:** `/tmp/paper2-slot01-backup/` (created 17:08 local, the moment of the deletion) holds `patch.diff`, the copied reference fix for `sympy__sympy-13798`, which is the protocol 5 pilot task again. No marker matches that path. `/tmp` is a writable root for Codex.
  - The same folder holds trial 1's `session.json` (`208bb176…`, `closed_at` 20:55Z). `history/index.json` lists that record as deleted and not recovered. `/tmp` is purged by macOS.
- **Smallest fix:**
  - Move `/tmp/paper2-slot01-backup` into `protocol-4/history/` with hashes in the index (author's call).
  - Add `unset OLDPWD` after `S:309`.
  - Scan tool outputs as well as inputs for content markers (`FAIL_TO_PASS`, `PASS_TO_PASS`, `test_patch`, `instance_id`), and add one broad `paper2` path marker (the workspace path is already replaced first).

**B3. Codex steps are undercounted.**
- `codex_log` counts one `custom_tool_call` as one step (`S:398-401`). Codex 0.166 runs commands inside one JavaScript `exec` call. In the sandbox check it ran all 4 commands in one call: Codex `steps = 1`, `agy` `steps = 4` for the same work.
- **Failure:** the 30-step limit is not enforced for Codex, and step counts can't be compared between the two configurations.
- **Fix:** count `command_execution` items in `codex-events.jsonl`, or count `tools.\w+(` calls in the `exec` input.

## High

**H1. An interrupted `run.sh` can't be closed, and `agy` can be launched twice.**
- **Cause:** the Claude Code Bash tool stops foreground commands after at most 600 s, and sessions run up to 900 or 930 s. With `set -m`, the agent and the watchdog survive in their own process groups, but `run.sh` dies.
- **Result:** no `run.json` is written, the Codex sign-in is not copied back, the run home is not archived, and the rollout log is not moved, so `close` refuses. Re-running gives exit 94 for Codex. For `agy`, the only guard is `run.json` (`S:310`), so a second launch starts and overwrites the logs (`>`).
- **Fix:** the runbook (step 15.2) must say the assistant uses `run_in_background`, and change `mkdir -p "$FOLDER/logs"` (`S:313`) to `mkdir "$FOLDER/logs" || exit 93`.

**H2. The reservation check can refuse an honest session.**
- `STARTED` is whole seconds (`S:314`); `reserved_at` has microseconds (`SC:43-44`). If `run.sh` starts within the same second as the reservation (e.g. `open && bash run.sh` chained), `S:532-534` raises.
- The fix would then change `sessions.py`, which counts as drift after the freeze.
- **Fix:** allow 1 s tolerance. The test misses this because it writes microsecond times (`TS:220-227`).

**H3. False "operator intervention" on target tasks.**
- `S:394-397` counts every user message that doesn't start with `<environment_context>` or `<user_instructions>`.
- The base commits of targets 30779, 30600 and 30575 contain `AGENTS.md`, which I checked in the mirror. If Codex adds it as a user message (format `# AGENTS.md instructions…`), 3 of 6 Codex target sessions become invalid. Unverified for 0.166; the sandbox folder had no `AGENTS.md`.
- **Fix:** count only user messages after the prompt, which is the rule as worded. Same for `agy` `user_input` steps.

**H4. `agy` keeps state across sessions.**
- It uses the shared `~/.gemini/antigravity-cli` folder: conversations, a summary store ("synced 2 records" at startup) and `implicit/*.pb`. Codex gets a fresh home each session.
- `protocol.md:113` says carried knowledge "found in a log is reported", but no code does that.
- **Fix:** before each `agy` session, move that state into the archive (not delete), or give `agy` a fresh home if it supports one. Either needs a check run. Otherwise drop the claim and list it as a threat.

**H5. Codex sub-agents are not detected.**
- `spawn_agent`, `send_message` and `followup_task` are offered (developer message in the rollout) and are not counted as outside tools.
- A sub-agent writes a second rollout file, so `close` refuses (`S:523-526`). The same happens if long sessions split the history into several files (`history_mode: paginated`).
- **Fix:** flag collaboration tools as outside tools, and parse all rollout files.

**H6. The two configurations are not compared on equal terms.** Codex has network blocked, writes limited to the workspace and temporary folders, and no web tools. `agy` has network open, every tool auto-approved, unknown write limits, shared state, different step counting, and a timer that starts after about 3 s of startup. Write this into `protocol.md` and the paper before the freeze, and make the invalidation rules the same for both (B1).

## Medium

**M1. Freeze and drift gaps.**
- Form hashes are written to the manifest but never re-checked in `frozen_drift` (`S:185-208`).
- Tool versions are not frozen, and `agy` has an auto-updater (`~/.gemini/antigravity-cli/updater`).
- `decision_engine.py` (Wilson interval and decision) and `replay.py` are not in `CODE_FILES` (`S:57-58`).
- `agy`'s own `settings.json`, `mcp_config.json` and `plugins/` are not hashed.
- `run.sh` and `prompt.md` are not hashed at `open`.
- `close` takes `config_id`, `task_id` and `workspace` from the editable `record.json` (`S:511-540`) instead of from the ledger.
- The harness virtual environment version is not re-checked at `close`.

**M2. With B05 `Contradicted`, two replay conditions can't change the evidence status.**
- Provenance removed and oracle defect leave the status at inadmissible, because a defect takes precedence. I confirmed this in an in-memory case.
- `paper2.tex:300` says a condition that doesn't change "the level and reason it targets" counts against the method; `protocol.md:53` says only "reason". The table at `paper2.tex:286` and `:288` promises level changes that can't happen.
- **Fix:** state this as a known outcome and align the wording before the freeze.

**M3. Exit code 3 is assumed to mean the `agy` timeout** (`S:470-471`, runbook line 188). No log shows it. **Fix:** also require elapsed time ≥ 900 s or the finish reason.

**M4. No cleanup after the tool exits.** Processes left in the tool's group keep running, and there is no SIGKILL fallback (`S:317-320`). **Fix:** add `kill -TERM -- -$PID 2>/dev/null` after the `wait`.

**M5. The `*.log` rule (`.gitignore:59`) ignores `agy.log`** for sessions and sandbox checks, although `session.json` hashes it, and it is the only `agy` log with timestamps.

**M6. Personal data in logs headed for a public repository.**
- `agy.log` contains the author's email.
- Codex rollouts contain account IDs.
- The tool streams contain the home-folder listing.

**M7. `paper2/` is untracked in git.** Three code files changed since the protocol 4 freeze, and their frozen versions can't be recovered. Committing before the protocol 5 freeze is the author's call.

**M8. Stale or inconsistent documents.**
- Runbook line 105 says 126 tests; there are 128.
- Runbook line 107 says the skip-permissions check is next, but it exists.
- Runbook line 238 says to re-check the `agy` parser; it now parses the 4-step stream correctly.
- `protocol.md:90` and `configurations.json:25` leave out the network result.
- `paper2.tex:365` says outside reads "are detected", which overstates the check.
- `paper2.tex:367` ties "never Contradicted" to defects that only inflate scores. B05's own defect lowers scores.

**M9. Starting `run.sh` from the assistant's shell is untested.** The agent would inherit `CLAUDE_CODE_*` variables and possibly a sandbox. Codex's own sandbox may not start inside another sandbox. A clean environment (`env -i` with `HOME`, `PATH`, `CODEX_HOME`) would also fix `OLDPWD`.

## Low

- `freeze` regenerates `readiness.md` without the test results (`S:152` → `SC:566`).
- Marker false positives:
  - `github.com/sympy/sympy/pull` appears in SymPy comments (10 at the pilot base, 28 at `b386392`) and lands in edit context lines.
  - `superseded` appears once.
  - Codex reading its own skills under `.paper2-codex-runs` matches `paper2-codex`.
- An `agy` session that ends naturally between 900 and about 903 s of wall time is recorded as `violated`.
- B05 draft: the evidence "quote" for the 18199 record is a paraphrase. The 18199 record labels the image HEAD `8414459` as "base commit"; the row's base commit is `ba80d1e4`.
- The B14 drafts' assistant role says "ran the listed auditor checks", but no check was run for B14.
- `history/index.json:271` calls the slot 01 transcript a copy. It is a 102,640-byte prefix of the 103,976-byte original.
- `sandbox_check.sh` doesn't test writing outside the folder.
- The policy IDs are still `P4`.

## Tests

128 pass, and `verify_manuscripts.py` and `check.py` pass. Some pass for the wrong reason:
- **Codex fixture:** one command per call (`TS:27-43`), unlike real Codex.
- **Reservation test:** uses microsecond times, so it misses H2.
- **Run script tests:** check only text and `bash -n` (`TS:325-354`). The watchdog, `run.json`, the Codex home restore and the exit codes are never executed. Fake `codex`/`agy` scripts on `PATH` with a short time limit would cover them.
- **`agy` network test:** `TS:159` locks in `not_observable`.
- **Drift test:** leaves out the configuration and `agy` keys, and the forms aren't tested.
- **Missing tests:** none cover `AGENTS.md` messages, wildcard bypasses, or the real `agy` stream with 4 steps.

## Checked and sound

- **Watchdog:** the process-group kill works without a terminal under both bash 5.3 and 3.2 (exit 143).
- **Script:** `run.sh` quoting and the `run.json` block are valid; the Codex sign-in is removed before the home is archived.
- **Workspace:** it has no later history; the test covers this.
- **Codex log:** shows workspace-write with network off, `gpt-6.1-sol`, medium effort.
- **`agy` parser on the real stream:** 4 steps, 1 user message, correct tokens.
- **Drafts:**
  - All six validate once signed and match the blank forms and their protocol 4 sources.
  - B05 cites the 18199 record with the correct hash `07ae13d5…`.
  - An in-memory case reproduces the stated known outcomes: inadmissible under both policies, and 6/6 gives [0.610, 1.0].
- **Protocol 4 history:** 42 of 42 files match the index; both external transcripts match; the protocol 4 manifest `b6bbe05a…` matches its authorization.
- **Prompt and selection:**
  - The prompt is byte-identical to protocol 4's.
  - The selection matches the runbook.
  - No issue text contains a marker.
- **Settings and folders:**
  - The `agy` runs did not change `config.json`.
  - Codex `config.toml` equals the fixed configuration.
  - The workspace and Codex run folders are empty.

## Could not check

Without running the tools I could not confirm:
- what `agy` does at its print timeout, and whether Codex injects `AGENTS.md` as a user message;
- whether long Codex sessions write several rollout files, and whether `agy` reuses stored summaries in new conversations;
- whether `agy` blocks writes outside the folder or honors deny rules under skip-permissions;
- grading in Docker, the quotes against `~/paper2-sources`, and the LaTeX layout.

### Critical Files for Implementation
- paper2/preparation/sessions.py
- paper2/preparation/protocol-5/configurations.json
- paper2/preparation/protocol-5/protocol.md
- paper2/tests/test_sessions.py
- paper2_runbook.md

Not reviewed: `targets.py`, `repository_runner.py`, and the B07/B12/B28 source quotes. The most urgent risk is outside the code: `/tmp/paper2-slot01-backup` holds the pilot task's fix and the only surviving trial 1 session record, and macOS may purge `/tmp`.
