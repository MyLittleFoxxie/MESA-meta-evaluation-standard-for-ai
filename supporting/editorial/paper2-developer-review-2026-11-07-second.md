# Paper 2: second developer review before signing (2026-11-07)

This is an assistant review. A read-only subagent (Claude Code, Claude Opus 5.5) acted as a senior developer and reviewed the protocol 5 code and records before the author signed the six forms. The report is kept as returned, apart from formatting. Line numbers refer to the files as they were before the fixes of the same day. The runbook (problems 57 to 60 and the change log, 2026-11-07) records what was changed.

**Verdict: ready to sign, with fixes needed before the freeze.** Signing and the freeze would both succeed. But the freeze would lock in an `agy` that updates itself and is at a version the documents do not record, plus three validity rules that make honest sessions invalid.

## What the reviewer ran or verified

- **Checks:** 145 tests pass; `verify_manuscripts.py` passes; `check.py` reports no errors.
- **Forms:** all six drafts pass `validate_form` in memory after the changes `sign_form` makes. None is signed, and no form mentions a tool version.
- **Freeze, dry run in memory with all writes patched out:** it succeeds, and the drift list is empty afterward. The selection is not blocked; the B05 task scope equals the pilot plus source tasks; all 13 images are present; the `agy` shared settings digest (`745e4415`), agent file, and session settings hashes match the version 7 summaries.
- **Codex base home:** holds only `auth.json` and `config.toml` (existence checked; `auth.json` not read). `config.toml` equals `CODEX_CONFIG`.
- **Tool versions:** `codex-cli 0.166.0`, but `agy` 1.5.3, not 1.5.2.
- **Agent Pythons:** `python_description` gives 3.9.20 and 3.12.14, each with 9 packages; the folder is read only.

## Findings

**High 1: `agy` updated itself during the checks; the update switch does not work. Fix before the freeze.**
- `~/.local/bin/agy` was modified at 14:49 on Nov 7, and the 1.5.2 program was kept as `agy.1794080977606729000.old`. `updater/update_status.json` says "Update successful". The log of `sandbox-check-agy-20261107T194936Z` shows 1.5.2 and "Spawned background update process" although `AGY_CLI_DISABLE_AUTO_UPDATE=1` was set; the two later version 7 runs report 1.5.3.
- Documents still say 1.5.2: `configurations.json:17` and the runbook (`:73`, `:308`).
- Every `agy` session starts the updater. If a newer version appears, `open` refuses every later `agy` session; if it lands between `open` and `run.sh`, the script exits 96 after the slot is reserved and started. Either case needs a new protocol version.
- Fix: stop updates in a way a check confirms (for example `chflags uchg ~/.local/bin/agy`), confirm with one `agy` run whose log shows no update, and correct the documents.

**High 2: three rules mark honest commands invalid. Fix before the freeze.**
- `grep -n "1 / 2" sympy/concrete/products.py` counts as study material: the bare `/` root matches " / " inside the pattern. Source task 13551 is about `n + 1 / 2**k`.
- `ls -R /opt/homebrew/var/agent-python/...` or `ls -R /tmp/x` counts as study material: the `ls` pattern lacks the end of path check.
- `python3 -m pip list` or `python3 -m pip show` counts as a network command; the protocol 4 Codex trial ran `python -m pip cache list`.
- Fix: the end of path check for `ls`; accept a bare `/` root only as the last argument; `-m\s+pip\s+(install|download)`; tests.

**Medium 3: the protocol and the code disagree on a denied `agy` file access.** The protocol says it counts as not resolved; `close` ignores `denied_actions`. A run that a denial ends exits 0 with status SUCCESS. Either reword the protocol or change the code.

**Medium 4: an untested `agy` path that real sessions will likely hit (inferred).** `agy` shortens long outputs and points to `brain/<id>/.system_generated/steps/N/output.txt`. Reading that file, or a traceback path under the agent Python, with `read_file` is outside the workspace and may end the session. Add sandbox check steps for both.

**Medium 5: `AGENTS.md` in three target workspaces (30779, 30600, 30575).** If a tool puts repository instructions after the prompt, the session is invalid. Put an `AGENTS.md` in the next check's scratch folder, and run Codex with the target Python too.

**Low**
- An `agy` run cut off with an exit code other than 3 that reports at most 900 s counts as within the limits; use `seconds < TIME_LIMIT`.
- The `agy` network observation keeps stale evidence text.
- Runbook step 15.2 omits exit codes 97 and 98 and gives no rule for `close` against `fail` after an `agy` error step or a Codex API error.
- Still open from the earlier review: `freeze` rewrites `readiness.md` without test results; the policy IDs are still `POLICY-P4-*`.
- `ps` output shows repository paths and makes a session invalid; accept or document.
- The `agy` settings hash does not cover `~/.gemini/config/agents`, `skills`, or `rules`.

## Checked and sound

`.agents/` is kept out of the patch; the agent Python path matches no marker except through `ls -R`; `*.pyc`, `.hypothesis/`, and `.pytest_cache/` do not reach the patch at any base commit; no case clashing file names or study markers at the base commits; the `agy` stream has one `user_input`, logs only `Path` for file tools, and its tool names are in the local set; the version 7 Codex log shows the right model, effort, and sandbox with no outside tools; `run.sh` renders correctly for both configurations.

**Inferred, not observed:** what `agy` does at its 900 s limit, where it stores shortened outputs, how both tools handle `AGENTS.md`, and whether `agy --version` alone starts the updater. The reviewer ran no tool or model and did not review the paper or `targets.py`.
