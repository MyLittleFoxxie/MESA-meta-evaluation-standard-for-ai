# Paper 2: readiness and soundness review before signing (2026-11-07, third)

This is an assistant review, not a human peer review. A read-only subagent (Claude Code, Claude Opus 5.5) answered two questions the author asked after the rehearsal: whether only the experiment's results are left, and whether the paper and its contribution are sound. The findings are summarized below; the assistant checked H1, H2, H4, H5, M1, and M2 against the files before recording them. The runbook (section 9 and the change log, 2026-11-07) records what follows from them.

**Verdicts.**
- **A.** Not only the results are left. Besides the six signatures, four gaps remain, and they need changes to files the freeze hashes. A change to any of these files after the freeze makes every `open` refuse, so they belong before the freeze. The planned commit before the freeze would also have committed the rehearsal raw logs.
- **B.** The paper is honest about what has been done. But the planned evaluation cannot answer RQ2 as posed: under the draft forms, every M3 verdict and every requirement verdict is fixed before any session, and the target sessions feed no research question.

## Findings, most severe first

- **H1. A reserve slot cannot be opened.** `open` accepts only pilot, source, and target (`sessions.py` `main`), and `open_session` never passes `replaces` to `ledger.reserve`. `agent_python` would give a reserve slot replacing a target task the source Python. The protocol and the paper promise a replacement after an infrastructure failure.
- **H2. The oracle defect replay counts a non-demonstrated counterexample against the method.**
  - What happens: when no defect is demonstrated, `replay.make_variant` sets the B07 check to `pending`, and `targeted_change` then returns False, because it accepts only "inadmissible". The protocol says such a result counts against the method, though the method behaved as specified.
  - A second problem: with no candidate patch at all, `make_variant` raises an error.
- **H3. Case assembly and its rules are missing.** Still undecided:
  - the requirement record;
  - who writes the transfer justification, and when (without one, every requirement verdict is Unresolved);
  - how failed or interrupted sessions enter a case (a declared task without an observation rejects the whole case);
  - which policy the replay uses;
  - the definitions of `target_verdict` and `relation`, which the templates use but only a protocol 3 file defines.

  The templates also lack exploratory policy and `targeted_change` columns.
- **H4. Counterexample timing and B07.** The protocol builds the counterexamples before any source session, but its step list has no step for building them. It also does not say whether a defect demonstrated on a selected task changes the B07 form, which is drafted as passed with no exploit test.
- **H5. The rehearsal raw logs were not git-ignored.** They hold the author's email and account identifiers. Fixed on 2026-11-07 (`.gitignore`).
- **M1. The replication package cannot reproduce verdicts.** Observation provenance points to the raw log, which is git-ignored, and `check_integrity` hashes it, so a copy of the repository rejects every case.
- **M2. The stated cause of abstention is incomplete.** B07 is drafted at Documented, which the study policy also rejects. The protocol, the paper, the runbook, and the template note name only B12 and B14.
- **M3. Stale documents:**
  - `paper2/README.md` and `paper2/preparation/README.md` (protocol 4 called active);
  - runbook lines (the date, "If B05 is Contradicted", the step limit called undecided);
  - `readiness.md` (counterexamples "none defined");
  - `configurations.json`'s definition of resolved, which lacks the network and tool conditions;
  - CLAUDE.md and AGENTS.md ("protocol 4 evaluation").
- **B1. Research questions against the evaluation.**
  - With the drafts: the study policy gives inquiry required and Unresolved for any count of successes. Under the exploratory policy M3 equals M2. The requirement verdict is always Unresolved, because there is no transfer justification.
  - The 12 target sessions feed no research question.
  - Suggested: reframe RQ2 around what sessions can show, justify or drop the target phase, or present the work as a research preview.
- **B2. Reasoning and terms:**
  - the "therefore" that assigns B05 Checked (the rubric's definition is the reason);
  - "auditor" means the assistant;
  - tests that accept incomplete patches belong under B07, those that reject correct fixes under B05;
  - "Checked" and "Verified" alternate.
- **B3. Threats not covered:**
  - one rater, with forms drafted by the assistant;
  - the same assistant builds the counterexamples that test its engine;
  - the simulation for RQ3 uses only the Wilson function, not the engine;
  - B14's held-out target window;
  - "may lead to uniform abstention" is already certain.
- **Deferred points.**
  - Research preview format: still stands, and B1 strengthens it.
  - Requirements engineering positioning, and length, title, and abstract: still stand.
  - Replication package: still stands, and is now a technical gap (M1).
  - `POLICY-P4-*` IDs: still stand, with a deadline; they must be renamed before the freeze, since `evidence.py` is hashed.
  - Anonymity: the paper claims double-blind review but links the named repository.

**Verified by the reviewer:**
- 152 tests and `verify_manuscripts.py` pass;
- in-memory engine and replay runs on the drafts under both policies;
- the git ignore status of the rehearsal logs;
- no reserve path exists in `sessions.py`;
- the `agy` settings digest, and both tools locked;
- the table figures.

**Not checked by the reviewer:** run-time behavior, page length, the sensitivity figures, and the source quotes.
