# Paper 2 handoff (2026-11-09, end of session)

This is for the next AI working on Paper 2 (`paper2.tex`, "Applying MESA Benchmark Reviews to Requirement Decisions"). The repository is `MESA-meta-evaluation-standard-for-ai`, on branch `refsq-v1`.

The target is REFSQ 2027:
- papers due **12 November 2026**;
- Springer LNCS, 15 pages including references;
- double-blind review;
- a four-paragraph structured abstract and a data availability statement are required.

## Read first

1. `CLAUDE.md`: the repository rules and writing style.
2. `paper2_runbook.md`, sections 1, 5, 7, and 10 (terms, current state, procedure, change log). Update it in the same change whenever anything changes.
3. `paper2/preparation/protocol-5/protocol.md`: the design, rules, and amendment history.
4. `supporting/editorial/paper2-mesa-refsq-review-2026-11-09.md`: the reviews, the reference sweep, the mapping of audit categories to MESA, and the ABA overlap.
5. `mesa_paper_feedback_from_paper_2.md`: feedback to the MESA paper (items 1 to 17).

## Where things stand

**Ready to sign. Nothing is signed or frozen.** All changes up to this file were committed and pushed on `refsq-v1` on 2026-11-09 at the author's request (the commit that adds this file).

The next step belongs to the author. They review `paper2/preparation/protocol-5/audit_checks/signing-changes.json`, then sign:

```bash
for f in B05-release B07-release B12-release B14a-release B28a-release B28b-release B14b-CONFIG_01_GEMINI_FLASH_MED B14b-CONFIG_02_SOL_MED ABC-release; do python3 -m paper2.preparation.sessions sign-form "$f" --author "Name"; done
python3 -m paper2.preparation.sessions sign-requirement --author "Name"
```

Only when the author asks:
1. rerun `signing_changes()`;
2. commit the signed records on `refsq-v1`;
3. freeze (`python3 -m paper2.preparation.sessions freeze`);
4. commit again.

The pilot, source, and target sessions each start only after the author's own authorization (runbook steps 14 to 17).

## The study (final design; the paper describes only this)

**The requirement** (illustrative, written for the study): "Working alone on a bug report from the SymPy repository, the coding agent changes the code so that the tests the maintainers later wrote for that bug pass, for at least 70% of bug reports, within 15 minutes each." It uses 95% Wilson bounds, and `n_min` = 9.

**Research questions.** They name no repository, dates, or models.
- **RQ1:** How does reviewing a benchmark with MESA or ABC, beyond an automated audit, change the decision on whether a coding agent meets a requirement?
- **RQ2:** Does a decision from a reviewed benchmark agree with a direct test of the same requirement?

**Gaps:**
- Automated audits (BenchGuard, ABA, BenchJack) already find benchmark flaws, and UTBoost and SWE-bench+ show that resolve rates move when flawed tasks are removed.
- ABC has no rule to accept or reject a result.
- MESA's own studies rated benchmarks from files only.
- SWE-bench Live, SWE-rebench, and the SWE-Bench Illusion compare whole benchmarks.
- None turns a review into a decision on a stated requirement, or checks such a decision against a direct test.

**Setup:**
- **Coding agents:** Gemini 3.8 Flash Medium in `agy` 1.5.3, and GPT-6.1 Sol medium in Codex 0.167.0. Both tools are locked against updates.
- **Source tasks:** 20 SWE-bench Verified SymPy tasks.
- **Direct test:** 20 target tasks, SymPy fixes merged from 2026-06-13 to 2026-11-05, after both stated cutoffs (Gemini: March 2026; Sol: 30 April 2026). Five target issues were opened before the cutoffs (targets 29939, 30591, 29815, 30959, 30872); the direct test is also reported without them.
- **Budget:** at most 90 sessions, with a 15-minute limit each.

**Methods per agent (RQ1):**
- M2: the resolve rate alone.
- **Audit only:** the tasks the executed checks flag are left out, with no criteria gate. This equals MESA's decision before the evidence status.
- **ABA:** its published findings flag `13031` and `18199`, giving 18 tasks.
- **M3 (MESA):** strict and lenient policies, the evidence status, and what each blocking criterion is missing.
- **ABC as its paper describes it:** item scores per part, the decision on all 20 tasks, and unmet or unknown items as caveats. ABC never withholds a decision.

**RQ2:** each decision is set against the direct test's decision. "Agree" means the same decision. The source minus target difference is reported with a Newcombe 95% interval.

**Control, not a question:** invalid sessions by kind, and the resolve rate by test result alone.

**Outcomes known in advance** (drafts as the author will sign them):
- Strict MESA is Inadmissible (B14a and B28a failed), with inquiry on B12 and B14b.
- Lenient MESA is Inadmissible (B28a).
- So MESA withholds the decision under both policies.
- Audit only and MESA's decision before the status use 14 tasks: Accept at 14 of 14, Reject at 6 or fewer.
- ABA uses 18 tasks: Accept at 17 or more, Reject at 8 or fewer.
- ABC decides on 20 tasks (Accept at 19 or more, Reject at 9 or fewer), with 15 caveats.
- **Tasks left out:** 13878, 15809, 18199, 21847, 22914, 23824.

## What this session did

**1. Judgment calls settled** against MESA rubric v5.1. The edits are in `audit_forms/drafts/`. Run A's originals are unchanged in `rating-run-v5-A/` and `abc-run/`.
- B05 outcome changed to passed (rubric lines 76, 140, 187).
- B05's reason on 18199 rewritten: it is listed under both B05 and B07 as two different defects.
- B07 set-asides unchanged.
- B14a failed unchanged.
- B14b task creation dates added (2017-01-25 to 2023-01-17).
- ABC T.5 changed to unknown, and the quotes for T.4, O.e.1, O.e.2, O.f.1, O.f.2, and O.i.1 replaced.
- B28a set from the new check: Verified, failed.

`study_controls.signing_changes()` lists all 34 changed fields.

**2. The B28a grading check (executed).**
- Prompt: `b28a-check-prompt.md`; tool: `counterexamples.scoring_check` / `scoring-check TASK`.
- Records: `audit_checks/b28a-scoring-check/*/check.json`; run record: `b28a-check-run-2026-11-09.json`.
- Nine patches that change only `bin/test` or `runtests.py`, on tasks 13031, 20590, and 24539, were all graded resolved by the SWE-bench harness.
- New session rule: a patch that changes a test-running file makes the session invalid. The files are `bin/test`, `runtests.py`, `conftest.py`, `pytest.ini`, `setup.cfg`, `tox.ini`, and SymPy's `pytest.py`. The rule is in `study_controls.scoring_files` and `sessions.close_session`.

**3. ABA overlap.**
- `paper2/preparation/aba.py` writes `audit_checks/aba-overlap.json` from `https://data.autobenchaudit.com/benchmarks/swe_bench_verified/benchmark.json`. Its sha256 is recorded; the raw file was not kept.
- A task counts as flagged when ABA reports at least one major finding.
- ABA flags 13031 and 18199 among the source tasks, plus the pilot task 13798. Only 18199 is also a defect in our forms.

**4. Analysis code** (`cases.py`):
- `abc_decision` follows ABC's paper.
- New: `audit_only`, the ABA row, `to_reach_decision`, `would_be`/`M3_withheld`, `rate_difference` (Newcombe), and `target_without_early`.
- `INVALID_KINDS` gains "grading files changed".
- The result templates are updated.

**5. Freeze inputs:** `FROZEN_RECORDS` adds `b28a-check-prompt.md` and `audit_checks/aba-overlap.json`; `CODE_FILES` adds `aba.py`.

**6. Requirement draft:**
- the text names the SymPy repository;
- the transfer justifications state the cutoffs as the providers' claims;
- `target_issues_before_cutoff` is added;
- no "team" wording remains.

**7. Literature and references.**
- The ABC paper is saved: `literature/pdfs/Establishing_Best_Practices_Rigorous_Agentic_Benchmarks.pdf` (arXiv v5), with a transcription and index lines.
- Six entries added to `references.bib`: `yu_utboost_2025`, `aleithan_swebench_plus_2024`, `liang_swebench_illusion_2025`, `wang_benchjack_2026`, `jain_cursor_reward_hacking_2026`, `stein_debugml_cheating_2026`. BenchGuard (`tu_benchguard_2026`) and ABA (`wang_auto_benchmark_audit_2026`) already existed.
- Notes for each are in `literature/notes/paper2-sources.md`.

**8. The paper (`paper2.tex`)** was rewritten to the two research questions:
- gap paragraphs with the audit literature;
- the term "direct test";
- an audit paragraph and a mapping table (`tab:audit_map`);
- the methods (audit only, ABA, ABC as its paper describes it);
- the B28a check, the ABA overlap, B05 passed, and the ABC counts (8 met, 9 not met, 10 not applicable, 6 unknown; part scores T 5/8, O 2/11, R 1/4);
- session validity as a control;
- the outcomes known in advance;
- every "team", "our repository", and "Paper 2" removed;
- the GitHub link replaced by `% TODO(author): add the anonymized link`.

**9. MESA feedback:**
- **Item 16:** unlocated defect rates, and grading defects in the outcome field.
- **Item 17:** Study 1's framework scope (18 sessions), anonymity (`mesa_paper.tex:383`), "an assistant", the 210 against 13 contrast, the ambiguous "created after the cutoff", and the overlap with Paper 2.

MESA's use of ABC was checked and is correct: ABC was applied only to τ-bench.

**10. Protocol and runbook:**
- the questions and gaps;
- the ABC rule;
- the audit and ABA paragraph;
- the B28a paragraph and session rule;
- the outcomes;
- amendment rows (protocol); state rows, step 10d, and a change log entry (runbook).

## Checks (all pass)

```bash
python3 -m unittest discover -s paper2/tests -p 'test_*.py'   # 181 tests
python3 verify_manuscripts.py
python3 v4/mapping/check.py && python3 v4/study/test_harness.py && python3 v5/study/test_harness.py
python3 -m paper2.preparation.study_controls prepare --run-tests
```

The freeze dry run in a scratch folder succeeded with 9 forms, 5 frozen records, and 10 code files. It wrote nothing in the repository.

## Open items

- **The author:**
  - review `signing-changes.json`, then sign;
  - add the anonymized replication link in both papers;
  - decide where the traceability equations live, MESA or Paper 2, since they appear in both (feedback item 17);
  - confirm whether the abstract was registered by 5 November.
- **Unchecked:**
  - LaTeX layout and the 15-page limit (no compilation is allowed);
  - the audit category names in `tab:audit_map`, which come from page summaries and need checking against the PDFs;
  - the new references, checked only on their abstract or blog pages.
- **MESA's answers to items 16 and 17:** pending; they do not block signing.

## Rules the author set (keep them)

**Process:**
- Do not compile LaTeX or open a PDF preview. Never handle credentials, and never read `~/.codex/auth.json`. Raw session and rehearsal logs stay out of git.
- Signing, freezing, committing, pushing, and authorizing a phase are the author's acts: do them only when asked.
- Use Claude Sonnet 5.5 (`model: "sonnet"`) for subagents, with separate scratch folders when they run in parallel.
- Keep `paper2_runbook.md` current in every change.

**The paper:**
- Describe only the final design: no earlier protocols, pilots, drafts, rubric versions, or deviations. The protocol, runbook, and provenance files keep the history.
- Never mention subscriptions, quotas, or cost.
- Write simple academic prose. Avoid hyphenated terms and adjectives unless necessary, and avoid marketing words.

**Terms in the paper:**
- Name models, never "the assistant".
- Say "resolve rate" (not "pass rate") and "decision" (not "verdict").
- Use the levels Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable; and "rating form", "coding agent", "direct test".
- Never "team" or "our repository".
- Research questions must be simple, generic, tied to a cited gap, and about requirement decisions, not about comparing models or sessions. The author's review and signing are a validation step, not a research question.
