# Paper 2: second REFSQ review before signing (2026-11-07)

This is an assistant review, not a human peer review. A read-only subagent (Claude Code, Claude Opus 5.5) acted as a REFSQ program committee member. It reviewed `paper2.tex`, the protocol 5 records, and the six form drafts before the author signed them. The report is kept as returned, apart from formatting. Line numbers refer to the files as they were before the fixes of the same day. The runbook (change log, 2026-11-07) records what was changed.

**Recommendation: reject as a full research paper.** Most of the facts the last review found missing are now in the paper: the B05 check, the sandbox results, a deviations table, and the corrected defect reasoning (l.207). The problem is the evaluation. Nothing under protocol 5 has run, and the planned study cannot change the M2 to M3 comparison much. Under the study policy every M3 verdict is Unresolved. Under the exploratory policy, with the forms signed as drafted, M3 equals M2. So M2 and M3 differ only if a configuration resolves at most one of its six source tasks, and the replay effects follow from the rules (l.396). The work fits a research preview.

**Signing.** Nothing blocks signing on the ratings. Every anchor and outcome is supported by the cited records, and every quote matches the saved sources. B07, B12, and B28 can be signed as drafted. B05 and both B14 forms need text edits first (findings 1 to 4). None of the edits changes a rating.

## Findings, most severe first

1. **Before signing: B05 understates how often the screening misses flawed tests.** `B05-release.json:40` and `:73` describe the limit through one task, 18199. The 2026 post audited 138 Verified problems; all of them had passed the 2024 screening, and at least 59.4% have flawed tests. That is at least 82 Verified tasks (16.4% of 500). Add to `detection_limits` that all 138 problems are in Verified and passed the screening, that at least 82 have flawed tests, and that whether any of the seven tasks is among them is not known.
2. **Before signing: B05 counts a rejected check toward "passed" and overstates what it showed.**
   - The procedure (`:37`) lists the 18199 grading under the outcome "passed" (`:38`), but that check was rejected. Keep it only in `detection_limits` and `checks_performed`.
   - The form says the tests reject "a patch that fixes only the stated issue". The record does not show that the patch is a correct fix, and it says the graded tests give the same result for that patch and for the unchanged source. Write instead that the graded tests rejected a patch limited to the reference lines for the stated issue, with the same result as the unchanged source.
   - Use the same wording in `protocol.md:16` and in the paper (l.271, l.317).
3. **Before signing: two wrong evidence locations.** `B05:56` and `B14-CONFIG_02_SOL_MED.json:46` cite "section Background". Both quotes are in the post's opening paragraphs, before that heading. Change both to "opening paragraphs".
4. **Before signing: B14 wording.**
   - Sol `:51` says the audit found "strong contamination in every frontier model it tested". The post says every tested model reproduced gold patches or problem statement details "for certain tasks"; "strong" labels three red team examples.
   - Both forms (`:51`) offer Contradicted as an alternative. No source shows a defect for this model, so the rubric does not allow it there. Remove it.
   - `:66` says "unchanged in content", but the roles text changed.
   - `B05:86,89` and `B14:67` contain absolute paths with the user name. Signing freezes them into the package; make them relative.
5. **Before signing (optional): "not_performed" next to a search that was performed.** `B12:27-28` and both `B14:27-28` describe an auditor search but record `not_performed`. Add a sentence that neither the sources nor the auditor performed a check of this kind, and that the search looked for one.
6. **Before freeze: `agy` updated itself during the checks.**
   - The version 7 run at 19:49Z reported 1.5.2, and its `agy.log:55` shows "Spawned background update process", with `AGY_CLI_DISABLE_AUTO_UPDATE=1` set. The runs at 19:53Z and 20:00Z report 1.5.3.
   - `configurations.json:17` and runbook `:73` still say 1.5.2, and problem 48 (`:308`) says no update happened.
   - Any update after the freeze makes `open` refuse.
   - Fix: correct the records, block the updater in a way a check confirms, and add a deviations row.
7. **Before freeze: Codex with the target tasks' Python was never checked.** `protocol.md:94` says this check was not run, yet paper l.394 states that both agents find Python 3.12.14 for target tasks.
8. **Before freeze: Codex can reach reference fixes.** Codex reads outside its folder. The gold patches of all 75 source tasks are in `~/.cache/huggingface`, and later fixes are in the mirror and the archive. Such reads are only detected afterward by markers. State this in `protocol.md`, or make these stores unreadable during Codex sessions.
9. **Before freeze: assistant roles.** `protocol.md:133` says the author runs the sandbox checks, which contradicts `:124` and the runbook (the assistant ran versions 5 to 7 and chose the `agy` setting). Paper l.402 omits this.
10. **Before freeze: oracle defect counterexamples.** Who builds them, and how, is still undecided. Fix it in the protocol so they are not chosen after source results are seen.
11. **Paper only.**
    - l.87 "Six drafts with auditor checks": B14 had none.
    - l.239 and l.390 leave out the sandbox checks.
    - l.271 relies on the 2024 OpenAI post, which has no bibliography entry. The title in `references.bib:457` differs from the 2026 post's title.
    - The deviations table lacks two changes: the `agy` file tools added to the local set and the shared `agy` rules removed after the logs showed them. The pre-seeded slot is not mentioned.
    - Add one sentence that B07 and B28 rate the grading release; the sessions' own environment enters only through the validity rules.

## Earlier review (2026-11-07)

- **Addressed:** W2, W3 (small gaps in finding 11), W4, W5c, W8, and the "invalid" and Table 1 points of W9.
- **Still open:**
  - W1: no evaluation, and the role of the target sessions is undefined.
  - W5a and W5b: settled by the B05 choice, but the paper states no general rule.
  - W5d: the content of a transfer justification is not judged. W5e: a single rater.
  - W6: requirements engineering positioning, and the Hou et al. row (l.140).
  - W7: `git ls-files paper2` returns nothing, and the URL at l.409 contains a user name.
  - W9: "Contradicted" is both a level and a verdict; the bibliography problems in finding 11.
  - W10: the abstract is 386 words, and the title says "Applying".

## Verified and inferred

- **Verified:** every form quote against the saved sources; the hash and content of the 18199 record; the selection order and the seven B05 tasks; eligibility of 75 source and 6 target tasks; source task dates from 2016 to 2023; the B28 counts; the `agy` settings and agent file hashes against the checks; the `agy` versions in the check summaries; `verify_manuscripts.py` passes.
- **Inferred:** that Codex can read the Hugging Face cache (from its outside read result; not tested directly); that the 22 image changes are file mode changes; the reasoning about when M2 and M3 can differ.
- **Not done:** compiling the LaTeX, checking the length, running the tests, reading the archived probe logs, or opening the provider pages online.
