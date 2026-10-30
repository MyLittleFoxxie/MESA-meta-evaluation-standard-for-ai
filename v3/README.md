# Paper and experiment plan for version three

Status: both batches completed on 30 October 2026. Branch: `codex/mesa-v3`. The user selected the MESA rubric with ten criteria and authorized the Codex experiment, then later the Claude batch with Claude Fable 5.1 at medium effort. The Codex batch completed twelve main sessions with two retained pilots and no retries. The Claude batch completed twelve main sessions with three pilot attempts, one of which failed before any model request and is retained. See the [study records](study/README.md), [Codex results](study/analysis/summary.md), [Claude results](study/claude/analysis/summary.md), [manuscript](../paper_mesa_v3.tex) and [continuation plan](CONTINUE.md). Each batch's frozen protocol governs its interpretation; this document records the broader design.

This plan responds to `paper_plan_auditing_ai_benchmarks_with_cli_agents.md` supplied from Downloads. That document is a proposal, not evidence of completed experiments. Its results, human ratings, agreement statistics and examples of agent failures cannot be reported as observations.

The branch was created from `claude/sonnet-5-5-study` while the checkout contained edits, deletions and additions. Those changes remain in the checkout; creating a branch does not commit or isolate them. This work adds `v3/` files and `paper_mesa_v3.tex`. Preserve the existing manuscripts, v2 plan, survey and study records.

## Purpose and name

Study how agents use papers and repository files to review AI benchmarks, and where the available evidence leaves questions unresolved. Do not assume in advance that agents succeed on software checks and fail on validity judgments.

Proposed title: **Auditing Artificial Intelligence Benchmarks with Coding Agents**.

Do not use acronyms in manuscript titles or section titles. Introduce MESA as the instrument name in the abstract and body.

MESA can name this revision because it continues the project's purpose of reviewing benchmarks, but it is a new instrument design. In v3, call it the MESA benchmark audit rubric, with ten criteria. Use `mesa-audit-10-v3` as its provenance identifier. Distinguish it explicitly from the earlier MESA questionnaire with 25 questions. Evidence about that questionnaire does not validate the rubric, and its answers must not be converted into rubric ratings.

The user selected Option B after considering both options. Option A is not an experimental condition. Preserve all earlier manuscripts and survey materials under their existing identities; this decision applies to v3 only.

## Selected design: a rubric with ten criteria

Develop the attachment's A1–A5 and B1–B5 as the MESA benchmark audit rubric. These criteria still need definitions and anchors; selection does not establish validation. Preserve the earlier questionnaire under its existing identity.

Advantages: an explicit focus on repository checks and selected measurement concerns; fewer judgments to record; direct links from some checks to scripts, data and documentation. Fewer criteria do not establish less human effort or easier use.

Limits: the proposed rubric changes both coverage and response meanings. Its 0, 5, 10 and 15 ratings cannot be compared directly with MESA answers. Missing information must not share a rating with a demonstrated defect. A human baseline is relevant only to claims that require it, and no audit can establish that an answer key is free of every error. Repository inspection cannot prove that scripts work or that instructions reproduce results.

Before using numerical ratings, define anchors for each criterion, keep “insufficient evidence” and “not applicable” outside the scale, and state whether a rating concerns documentation, checking or outcomes. The attachment's scale descriptions differ from those in the repository's BetterBench transcription; verify the original source before claiming adoption. Do not average the ten criteria into an overall score.

The following correspondences are proposals, not historical derivations or equivalent coverage:

| Candidate criterion | Related MESA questions | Difference to resolve |
| --- | --- | --- |
| A1 Evaluation scripts | Q22 | Presence does not establish execution or availability of all materials |
| A2 Scoring implementation | Q5, Q10, Q12 | Matching a formula, implementing it correctly and supporting an interpretation differ |
| A3 Dataset documentation | Q1, Q3, Q7 | Description does not justify task selection |
| A4 License and dependencies | Q4, Q22, Q23 | Split evidence about software requirements, permissions and protections |
| A5 Reproduction instructions | Q4, Q22 | Reading instructions does not demonstrate reproduction |
| B1 Construct definition | Q2, Q6, Q9 | Defining an ability does not demonstrate task coverage |
| B2 Answer checking | Q8, Q12 | Record checking and its findings separately; remove the demand for proof of no errors |
| B3 Reliability | Q14, Q15, Q16 | Repeated runs, changed conditions and uncertainty require separate evidence |
| B4 Human comparisons | Q13, Q20, Q21 | Other comparison points can be relevant; applicability depends on the claim |
| B5 Contamination | Q18, Q19 | Safeguards, prior exposure and submission rules are not interchangeable |

The ten criteria do not explicitly retain all of Q11 (score aggregation), Q17 (shortcuts), Q20 (claims beyond tested tasks), Q21 (fair comparisons), Q24 (release changes) and Q25 (limits of published claims). Some have partial overlap above. A rubric presented as a general benchmark audit must explain these omissions. It cannot claim complete construct validity coverage from B1–B5.

## Study scope

Test only the rubric with ten criteria. Use one model, three benchmarks, two access conditions and two repetitions: 12 main sessions, plus two pilot sessions outside the study set. Cap all attempts, including infrastructure retries, at 16. Do not automatically expand to another model, instrument or benchmark. See [experiments.md](experiments.md) for the design and cost controls.

Use `gpt-6-luna` at medium reasoning effort for study generation. It is available in this session and has the lowest published credit rates among the exposed models, checked on 30 October 2026 against [OpenAI pricing](https://learn.chatgpt.com/docs/pricing). Verify access in the intended runner before execution. Keep the model fixed after freezing; do not substitute a more costly model when a limit or failure occurs.

## Changes needed in the supplied paper plan

| Proposal | Treatment in v3 |
| --- | --- |
| Predicted agreement, bias, error reductions and example outputs | Remove from the abstract and results; record questions to test |
| 45 runs with one text baseline and two agents | Use one model with matched access conditions; 12 main sessions |
| Human expert baseline assembled from publications | Build traceable reference records; name actual reviewers and retain disagreements |
| Every answer key must be free of errors | Examine the scope of checks and evidence of defects |
| File exists, therefore its citation is accurate | Check existence, location, quoted content and support for the claim separately |
| Agents should automatically decide software quality | Consider delegation only after inspecting observed failures and limits |
| All construct validity belongs to human reviewers | Treat as a possible implication, not a finding established before testing |
| Weighted kappa, MAE, ICC and signed bias for all outputs | Define measures from the rubric's anchors; numerical labels alone do not establish equal distances |
| Legal compliance and standards claims | Omit unless needed and verified against sources; benchmarks alone do not establish compliance |
| Fifteen pages in LNCS for both venues | Preserve IEEE for a CHASE manuscript; verify REFSQ requirements separately |

## Manuscript scope

CHASE reports the instrument design and model experiments, without human survey methods or results. Human evaluation appears only as future work and is not required to complete the CHASE paper. This boundary applies to the selected rubric.

Human evaluation for a possible REFSQ extension is deferred. The current v3 scope is the ten criterion rubric, manuscript and model experiments. Ignore the existing survey for this work: do not use its materials, responses or analysis plan as v3 inputs or dependencies, and do not redesign it. Leave its files untouched. Define any future human evaluation separately when requested; it is not required to complete v3 for CHASE.

Create `paper_mesa_v3.tex` beside the existing manuscripts. For CHASE, reuse the IEEE structure without changing the preserved manuscripts. Do not choose a REFSQ format or overwrite its planned human extension. Confirm venue before setting a page budget.

1. Introduction: why benchmark review needs both source inspection and interpretation; research questions without predicted answers.
2. Basis: EFPA adaptation, measurement arguments and BetterBench; explain how this differs from grading individual model answers.
3. Review procedure: rubric definitions, evidence fields, coverage, omissions and source access.
4. Method: source snapshots, reference preparation, agent configurations, conditions, execution and analysis.
5. Results: placeholders until data exist; completion, evidence support, judgments, changes with access and repetition.
6. Discussion: what the observed results support about using agents, unresolved judgments and scope of human checking.
7. Limits and conclusion: source selection, training exposure, configuration differences, reference preparation, repeated outputs and three benchmark cases.

Do not pool v3 with CHASE or v2 results. Disclose assistant involvement in preparing materials, executing checks and interpreting responses. Do not call assistant analysis independent human validation. No human survey findings belong in CHASE. Any future human extension requires its own method and records; it is outside the current v3 work.

## Work sequence and completion checks

1. Define and check the selected ten criteria and their rating anchors. Record the differences from the earlier questionnaire before freezing.
2. Verify source claims and bibliography records. In particular, verify the scope and edition of HLE criticism, the BetterBench anchors, and claims about each benchmark's missing analyses. A claim in the attachment is not a verified finding.
3. Prepare source snapshots, intended uses and reference judgments. Complete the checks in the experiment plan.
4. Write the manuscript method and results placeholders; implement the runner, validators and analysis without making model calls.
5. Run harness checks using fixtures, then a declared development pilot on material excluded from the study. Freeze the main protocol only after any pilot changes.
6. Execute the frozen study with model identifiers, runner settings and observed usage recorded. Retain every attempt and failure.
7. Analyze saved outputs, check claims against records, and fill the manuscript results.
8. Check citation keys, LaTeX structure, asset paths, links and study counts. Do not compile LaTeX or open a PDF preview. Layout and page length remain unchecked.

The deliverables now include the manuscript, rubric, execution software for both command line tools, frozen materials, saved Codex and Claude outputs, offline analysis for each batch and a descriptive comparison between them. Reference judgments are assistant proposals, not human ground truth. The two batches ran sequentially and are not a jointly randomized model comparison. No files have been committed, pushed or published.
