# Reviews of Paper 2 and the MESA paper before signing (2026-11-09)

Three read-only Claude Sonnet 5.5 subagents worked at the author's request:
1. a review of both manuscripts in the role of a REFSQ 2027 program committee member;
2. a sweep of the references for each research question;
3. a mapping of automated audit categories onto MESA's criteria.

Claude Opus 5.5 checked their main claims against the files and web pages, and recorded below what was done with each point. The texts are summaries, not transcripts.

## 1. REFSQ-style review

**REFSQ 2027 call** (EasyChair, read 2026-11-09):
- technical design papers have 15 pages including references and need "a preliminary validation of the artifacts";
- papers are due 12 November 2026;
- review is double-blind;
- a structured four-paragraph abstract and a data availability statement are required.

**Scores:** MESA paper weak accept; Paper 2 weak reject, because it had no observations yet.

### Paper 2: points and what was done

| Point | Action |
|---|---|
| The GitHub URL with the author's handle (line 414) breaks double-blind review | Taken: replaced by an anonymized copy of the replication package; the author adds the link |
| "Paper 2" in the abstract; "for the MESA authors" (line 61) | Taken |
| M3 uses a narrower profile than MESA's mandatory one (B01 to B04, B16, B23 left out) | Taken: the paper says Admissible here covers only the seven selected criteria. Line 119 already listed the left-out criteria |
| RQ3 cannot separate ABC from the resolve rate alone; two agents give two cases | Taken: the research questions were rewritten (two questions); ABC's decision is stated to equal the resolve rate alone, apart from its caveats; "agree" is fixed in advance; the difference in resolve rates is reported with its interval |
| The transfer justification overstated exposure ("cannot have seen") | Taken: stated cutoffs as the providers' claims; five target issues opened before the cutoffs named; the direct test is also reported without them |
| The decided edits (B05 passed, executed B28a check, invalid-session rule) must reach the text | Taken |
| "No session has been run" while an earlier pilot exists in the records | Not taken: the author's rule is that the paper describes the final design only; the status sentences say "no study session", which is exact; the records keep the pilot |
| Recut as an 8-page research preview | Not taken: the author will run the sessions |
| Cut the restatement of MESA's rules to save pages | Deferred: page length is unchecked; an editorial choice after the sessions |
| Terms differ between papers (session, configuration, decision, level) | Partly taken: a session is defined as one coding agent run on one task |

### MESA paper: points sent to MESA as feedback item 17

The following were verified against `mesa_paper.tex`:
- Study 1's framework scope (ABC only on τ-bench, How2Bench only on HumanEval, so 18 sessions; the reviewer misread six times four);
- the GitHub URL, branch, and "Identity Notice" (line 383);
- "an assistant" (lines 30, 268);
- the 210 against 13 contrast given sessions that could not run code;
- the ambiguity of "created after the cutoff";
- the overlap of the traceability rules with Paper 2.

**Not sent:** the reviewer's claim that "81%" conflicts with "26 of 32", which is wrong (26 of 32 is 81%).

## 2. Reference sweep: what earlier work already answers

- **Weak tests in SWE-bench:** UTBoost (`yu_utboost_2025`), SWE-bench+ (`aleithan_swebench_plus_2024`), and Wang, Pradel, and Liu (arXiv 2503.15223, not added) show that weak tests inflate resolve rates and change rankings.
- **Agents retrieving fixes:** the Cursor post (`jain_cursor_reward_hacking_2026`) and DebugML (`stein_debugml_cheating_2026`) show agents retrieving fixes from git history or the web, and a stricter harness lowering scores. Mohl et al. (`mohl_transcript_flaws_2026`) detect reading of reference fixes and git history on SWE-Bench-Verified, but not changes to test or grading files.
- **Automated audits:** BenchGuard (`tu_benchguard_2026`), ABA (`wang_auto_benchmark_audit_2026`), and BenchJack (`wang_benchjack_2026`) have agents audit real benchmarks and find confirmed flaws.
- **Newer tasks:** SWE-bench Live, SWE-rebench, and the SWE-Bench Illusion (`liang_swebench_illusion_2025`) show score gaps or memorization on newer tasks, for whole benchmarks.

**Consequence for Paper 2.** "What do agents find when they review a benchmark" and "how often do coding agents cheat" are no longer open questions. The two remaining research questions concern decisions on a stated requirement:
- **RQ1:** how a review with MESA or ABC, beyond an automated audit, changes the decision on whether a coding agent meets a requirement.
- **RQ2:** whether a decision from a reviewed benchmark agrees with a direct test of the same requirement.

Session validity is kept as a control.

## 3. Automated audit categories mapped onto MESA's criteria

The categories come from each paper (read through summaries of the arXiv HTML; check the names against the PDFs before printing). The mapping is one model's judgment.

| Audit category | MESA criteria | Fit |
|---|---|---|
| BenchGuard GT (wrong logic, data handling, output format) | B05 (B06, B27 in part) | full to partial |
| BenchGuard EVAL (judge bias, spec–eval mismatch, coverage, tolerance, non-determinism) | B05, B06, B07 (B10 in part) | full to partial |
| BenchGuard INST (underspecified, contradictory, infeasible task) | B05 (B06 in part) | partial |
| BenchGuard ENV (dependencies, paths, resources) | B18, B28b | partial |
| ABA Instruction | B05 | partial |
| ABA Environment | B18, B28b | partial |
| ABA Evaluation | B05, B07 | full |
| BenchJack V1 isolation failure, V2 answers shipped with the test, V3 code execution in the evaluator, V7 trusting untrusted output | B28a, B28b, B07 | full |
| BenchJack V4 judge prompt injection, V5 weak string matching, V6 evaluation logic gaps | B07 | full |
| BenchJack V8 excessive permissions | B28b | partial |

**No audit category covers:**
- B01 to B04 (construct and task selection);
- B08, B09, B11;
- B12 (the benchmark's own uncertainty reporting);
- B13;
- B14a and B14b (training exposure);
- B15 to B17;
- B19 to B27 (except B27 at the edge);
- B29.

**Summary for the paper.** Automated audits supply evidence mainly for tests and reference answers (B05), scoring that accepts wrong solutions (B07), and isolation (B28a, B28b). The review also covers the construct, uncertainty reporting, training exposure, and documentation, and turns the evidence into a decision on a requirement. MESA covers every shared concern by construction, so the mapping shows what audits leave out, not that MESA works.

## 4. ABA on this study's tasks (`paper2/preparation/protocol-5/audit_checks/aba-overlap.json`)

ABA flags a task when it reports at least one major finding in either of its modes, static or trajectory; this is ABA's own headline measure. Against this study's checks:
- **Flagged by ABA:** 2 of the 20 source tasks, `13031` and `18199`, plus the pilot task `13798`.
- **Listed as task defects in the rating forms:** 6 tasks (B05 and B07).
- **Both:** only `18199`. ABA's finding there is the same one B05 records: the hidden tests require composite-modulus support that the issue does not ask for.
- **Forms only:** the other five form defects come from executed B07 exploits that ABA's audit did not find.
- **ABA only:** ABA's `13031` finding is not in the forms.

So on these tasks, the audit and the review's checks mostly find different defects.
