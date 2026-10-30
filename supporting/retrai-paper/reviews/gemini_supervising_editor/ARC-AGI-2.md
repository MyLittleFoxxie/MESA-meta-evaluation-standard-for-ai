# Editor's Prefatory Notes

> **Version note:** Reviewed against an earlier version of the MESA template (89 items), 2025-2026. Section numbers cite v1; see `feedback/95-mesa-core-plan.md` Part 3 for the v1→v2 mapping.

## Editor Reconciliation Note

As the MESA Supervising Editor Agent, I have reconciled two independently generated draft MESA reviews for the ARC-AGI-2 benchmark into a single, authoritative, source-grounded evaluation. Both reviewers operated from the same source packet and produced high-quality, comprehensive drafts. Reviewer 1 (R1) meticulously documented the official documentation's textual inconsistencies (e.g., a conflict between 2-trial and 3-trial rules) and detailed the exact-match scoring mechanisms. Reviewer 2 (R2) provided a rigorous statistical critique, emphasizing the fragility of leaderboard rankings on 120-task splits without confidence intervals, and astutely separated the "Kaggle cohort" (offline, compute-bounded) from the "API-hosted cohort" (cost-bounded). This final evaluation synthesizes R1's procedural attention to detail with R2's rigorous psychometric and statistical limits, applying the _BetterBench_, _Measuring what Matters_, and _A Definition of AGI_ literature to discipline the benchmark's broad claims.

## Discrepancy Summary

The following major discrepancies between the drafts were resolved based on source-grounded editorial judgment:

1. **Overall Reliability and Precision (Section 9):** R1 rated overall reliability a `2` based on the deterministic exact-match scoring and pass@2 structure. R2 rated it a `1`, arguing that on a 120-item split, a 1 percentage point difference equals a single task, rendering small leaderboard differences indistinguishable from noise without reported confidence intervals. _Resolution:_ Adjusted to `1`. Following _BetterBench_ and _Measuring what Matters_, the absence of uncertainty reporting on a competitive leaderboard fundamentally undermines the reliability of inter-model comparisons.
2. **Quality of Reports and Leaderboards (Section 12):** R1 rated reporting a `3` due to the accessibility of the leaderboard and cost-efficiency framing. R2 rated it a `2` because the public leaderboard mixes Kaggle (offline, hardware-bounded) and API-hosted (cost-bounded) cohorts without formal separation or uncertainty bands. _Resolution:_ Adjusted to `2`. The mixing of distinct evaluation conditions without condition-matched labels or error bars creates a high risk of unfair or misleading cross-system comparison.
3. **Gameability (Item 10.5.2):** R1 rated gameability controls a `2`, noting that test-time training (TTT) and benchmark-specific solver engineering can heavily tune results. R2 rated it a `3` due to the Kaggle offline sandbox and fully hidden private set. _Resolution:_ Adjusted to `3`. While TTT is prevalent, the offline constraints and strict private holdout represent strong structural controls relative to typical LLM benchmarks.

## Unresolved Evidence Gaps

1. **Statistical Uncertainty:** No published confidence intervals, standard errors, or repeat-run variance metrics are available for the headline leaderboard scores.
2. **Procedural Inconsistency:** The public repository README contains a documented inconsistency, describing two trials in the task success criterion but later referencing "3 trials" in the task file format section.
3. **Subgroup/Category Performance:** Although tasks are built around four conceptual "challenge types," per-item category labels and corresponding subscores are not publicly provided, preventing internal-structure validity analyses.

## Interpretation Cautions

1. **Construct Breadth vs. AGI Claims:** ARC-AGI-2 is a rigorous test of a narrow construct: compositional grid-puzzle generalization. It maps to only three of the ten CHC cognitive domains (On-the-Spot Reasoning, Visual Processing, Working Memory). It does not test long-term memory, general knowledge, language, or auditory processing, and therefore cannot be used as standalone evidence for AGI or general intelligence.
2. **Cohort Mixing:** Do not directly compare Kaggle competition scores (12-hour wall-clock, 4x L4 GPUs, offline) with public API-hosted leaderboard scores (cost-bounded, online, potentially different scaffolding) without explicit caveats.
3. **Margin of Error:** Because the public and semi-private evaluation splits contain only 120 tasks each, score differences of less than 2-3 percentage points should be treated as statistically insignificant noise unless proven otherwise.

---

# MESA Review: ARC-AGI-2

## Short Stand-Alone Non-Evaluative Benchmark Description

ARC-AGI-2 is a public grid-transformation benchmark maintained by the ARC Prize Foundation. Each task presents a small number of demonstration input-output grid pairs and asks the evaluated system to infer the underlying rule and produce exact output grids for unseen test inputs. The release contains 1,000 training tasks and a 120-task calibrated public evaluation set under Apache-2.0, with 120-task semi-private and private evaluation sets withheld for the Kaggle leaderboard and the ARC Prize contest. Task difficulty was calibrated through a human-testing campaign of 407 participants across 515 sessions, and every retained task was solved by at least two independent testers within two attempts. Scoring is exact-cell match under a pass@2 rule, and the headline metric is unweighted accuracy across a split, reported alongside cost-per-task. Evaluation runs in two regimes: an offline Kaggle sandbox bounded by hardware and a 12-hour budget, and an API-hosted public leaderboard bounded by cost. The benchmark is publicly framed around progress toward general intelligence, with the maintainers' stated caveat that solving it is necessary but not sufficient for AGI.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt                  | Description                                           |
| :---------------------- | :---------------------------------------------------- |
| Reviewer Name           | MESA Supervising Editor Agent (Reconciled Evaluation) |
| Date of Current Review  | 2026-05-18                                            |
| Date of Previous Review | n/a                                                   |

### 1.2 Benchmark Identity & Provenance

| Prompt                                 | Description                                                                                                                                                           |
| :------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reviewed Entity Name                   | Abstraction and Reasoning Corpus for Artificial General Intelligence, version 2 (ARC-AGI-2)                                                                           |
| Short Name / Acronym                   | ARC-AGI-2                                                                                                                                                             |
| Entity Type                            | Original benchmark version in the ARC-AGI family; includes public dataset release plus controlled semi-private/private evaluation splits and an official leaderboard. |
| Parent / Source Benchmark              | ARC-AGI-1 (Chollet, 2019). ARC-AGI-2 preserves the grid input-output format while expanding and recalibrating the task set.                                           |
| Exact Version / Release Split          | ARC-AGI-2 public release: 1,000 public training tasks and 120 public evaluation tasks. Semi-private (120 tasks) and private (120 tasks) sets are held out.            |
| Implementation / Scorer Version        | Exact cell-by-cell matching of integer grids. Public ARC-AGI-2 repository and `arc-agi-benchmarking` repository as accessed on 2026-05-18.                            |
| Creators & Current Maintainers         | François Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard. Maintained by the ARC Prize Foundation / `arcprize`.                                 |
| Host Organization / Repository Owner   | ARC Prize Foundation (`arcprize` GitHub organization, `arcprize.org`).                                                                                                |
| Release Dates                          | Initial release 2025-03-24; arXiv v1 2025-05-17; arXiv v2 revised 2026-01-15.                                                                                         |
| License & Access Terms                 | Public repository materials are under Apache License 2.0. Semi-private and private evaluation sets are controlled-access and not included in the public repo.         |
| Persistent Identifier / DOI / Citation | arXiv:2505.11831, DOI 10.48550/arXiv.2505.11831.                                                                                                                      |

### 1.3 Materials, Sources, & Access Tracking

| Material / Source Type       | URL, Location, or Identifier                                                                | Access Date |
| :--------------------------- | :------------------------------------------------------------------------------------------ | :---------- |
| Paper / Technical Report     | https://arxiv.org/abs/2505.11831                                                            | 2026-05-18  |
| Website / Documentation Hub  | https://arcprize.org/arc-agi/2                                                              | 2026-05-18  |
| Code Repository              | https://github.com/arcprize/ARC-AGI-2                                                       | 2026-05-18  |
| Dataset / Task / Prompt Set  | `data/training/` and `data/evaluation/` in the ARC-AGI-2 repository.                        | 2026-05-18  |
| Evaluation Harness / Runner  | https://github.com/arcprize/arc-agi-benchmarking                                            | 2026-05-18  |
| Leaderboard / Results Portal | https://arcprize.org/leaderboard; Kaggle competition leaderboard.                           | 2026-05-18  |
| Guides (User/Scoring/Rubric) | https://arcprize.org/guide/1 and https://arcprize.org/policy                                | 2026-05-18  |
| Changelog / Release Logs     | ARC-AGI-2 repository `changelog.md`                                                         | 2026-05-18  |
| Official Announcements       | https://arcprize.org/blog/arc-agi-2-technical-report                                        | 2026-05-18  |
| Contextual Literature        | `literature/betterbench.md`, `Measuring_what_Matters.md`, `A_Definition_of_AGI.md` | 2026-05-18  |
| Feedback / Contact Channels  | GitHub repository issues and ARC Prize contact/policy routes.                               | 2026-05-18  |

## Section 2. Classification

### 2.1 Claimed Capability Domains

- [x] On-the-Spot Reasoning (R)
- [x] Working Memory (WM)
- [x] Visual Processing (V)
- [ ] General Knowledge (K)
- [ ] Long-Term Memory Storage (MS)
- [ ] Long-Term Memory Retrieval (MR)
- [ ] Reading and Writing Ability (RW)
- [ ] Mathematical Ability (M)
- [ ] Auditory Processing (A)
- [ ] Speed (S)

_Reviewer comments:_ The primary claim is "fluid intelligence" and "abstract reasoning" on novel tasks, mapping directly to On-the-Spot Reasoning. Visual Processing is secondary (symbolic grids), and Working Memory is utilized for multi-step reasoning. Speed is tracked contextually (cost/efficiency) but not as a core CHC cognitive speed dimension.

### 2.2 Area of Use

- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [x] Public communication or marketing

### 2.3 Intended AI Systems

- [x] Frontier general-purpose language models
- [x] Multimodal models
- [x] Chat or instruction-following models
- [x] Base language models
- [x] Agentic systems
- [x] Open-weight local models
- [x] API-hosted models

### 2.4 Intended Users of Benchmark Outputs

- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [x] Product teams
- [x] Safety evaluators
- [x] Policy or governance actors
- [x] Public leaderboard users

### 2.5 Task Families, Subdomains, and Scores

| Component                                                          | Description                                                                                                                                                                  |
| :----------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capability, phenomenon, or quality the benchmark claims to measure | Abstract reasoning, problem solving, fluid intelligence, and progress toward AGI.                                                                                            |
| Definition of the capability or quality being measured             | The ability to infer a transformation rule from a few demonstration input/output grid pairs and apply it exactly to held-out test inputs, utilizing minimal prior knowledge. |
| Subcomponents of the claimed capability                            | Four challenge types: multi-rule reasoning, multi-step reasoning, contextual rule application, and in-context symbol definition.                                             |
| Excluded scope or non-target abilities                             | World knowledge, language comprehension, tool use, long-horizon planning, and real-world embodiment are excluded.                                                            |
| Benchmark item families or subdomains                              | JSON-encoded grid puzzles (1x1 to 30x30 matrices of integers 0-9).                                                                                                           |
| Sources for benchmark items                                        | Newly authored ARC Prize Foundation tasks and previously unused reserves.                                                                                                    |
| Sampling method                                                    | Curated authoring with human-difficulty calibration (solvable by ≥2 independent human testers).                                                                              |
| Splits or partitions                                               | 1,000 public training; 120 public evaluation; 120 semi-private evaluation (leaderboard); 120 private evaluation (contest).                                                   |
| Primary score                                                      | Aggregate exact-match task accuracy (pass@2 logic).                                                                                                                          |
| Subscores                                                          | Split-specific scores. No official task-family subscores are published.                                                                                                      |
| Derived scores                                                     | Cost-per-task (USD) / efficiency reporting.                                                                                                                                  |
| Qualitative score ranges                                           | 85% hidden private evaluation accuracy triggers the Grand Prize. Below 5% is deemed low signal.                                                                              |
| Boundaries or caveats                                              | Authors state ARC is a necessary but not sufficient condition for AGI, and log-linear scaling alone is insufficient.                                                         |

### 2.6 Model Response Mode

- [x] Structured output, such as JSON or XML

### 2.7 Prerequisites for Evaluated Systems

| Requirement                                   | Irrelevant or not necessary | Necessary information given | Information missing |
| :-------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: |
| Context length                                |             [ ]             |             [x]             |         [ ]         |
| Structured output support                     |             [ ]             |             [x]             |         [ ]         |
| Exact format, schema, or parser compatibility |             [ ]             |             [x]             |         [ ]         |
| Retry, repair, or correction-loop support     |             [ ]             |             [x]             |         [ ]         |
| Code execution                                |             [ ]             |             [x]             |         [ ]         |
| API compatibility                             |             [ ]             |             [x]             |         [ ]         |
| Latency or time budget                        |             [ ]             |             [x]             |         [ ]         |
| Cost or compute budget                        |             [ ]             |             [x]             |         [ ]         |

### 2.8 Evaluation Conditions

| Condition                               | Description                                                                                      |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Prompting protocol                      | Not centrally fixed; repository provides raw JSON. Kaggle environment uses standardized runners. |
| Few-shot examples                       | 2-5 demonstration grid pairs provided intrinsically within each task JSON.                       |
| Sampling settings                       | Not universally specified; left to evaluator discretion / harness defaults.                      |
| Tool permissions                        | Kaggle: No internet access. API leaderboard: Unrestricted.                                       |
| Time limits                             | Kaggle: 12 hours for 240 tasks. API Leaderboard: Latency/cost reported.                          |
| Official rerun, retry, or repair policy | Evaluated on a pass@2 basis (two attempts per test input).                                       |
| Hardware or hosted service              | Kaggle uses 4x NVIDIA L4 GPUs.                                                                   |

### 2.9 Task Interaction and Observable Evidence Types

- [x] Structured data
- [x] Response latency
- [x] Cost
- [x] Token usage (reported by some)
- [x] Leaderboard submission metadata
- [x] Raw output or audit trace under controlled access

### 2.10 Input Stimulus Type

- [x] Tables or structured data (integer grids)
- [x] Images (can be rendered visually)

### 2.11 Number of Items or Measurement Points

| Prompt                        | Response                                                         |
| :---------------------------- | :--------------------------------------------------------------- |
| Total public items or tasks   | 1,000 training tasks; 120 public evaluation tasks.               |
| Total private or hidden items | 120 semi-private evaluation tasks; 120 private evaluation tasks. |
| Score aggregation unit        | Unweighted average exact-match accuracy across tasks in a split. |

### 2.12 Mode of Evaluation

- [x] Local batch evaluation
- [x] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [x] Competition or challenge submission
- Identity/condition controls: [x] Some control over submitted systems; [x] Controlled evaluation center or private harness (Kaggle).

### 2.13 Technological Arrangements

| Technology                             |  A  |  R  |
| :------------------------------------- | :-: | :-: |
| API access                             |  x  |     |
| Local inference                        |  x  |  x  |
| GPU                                    |  x  |  x  |
| CPU-only execution                     |  x  |     |
| Python package or CLI                  |  x  |     |
| Proprietary platform                   |  x  |  x  |
| Hosted scoring service                 |  x  |  x  |
| Filesystem, terminal, or sandbox state |  x  |     |

### 2.14 Time and Resource Requirements

The Kaggle competition regime imposes a hard budget of 12 hours of wall-clock compute on 4x NVIDIA L4 GPUs for 240 tasks, with no internet access. The API-hosted public leaderboard regime imposes no wall-clock limit but is bounded by a per-task cost cap, and cost-per-task is reported alongside accuracy as an explicit efficiency axis. Human calibration sessions ran 90 minutes, with a median of 2.2 minutes per solved task. No official estimate of total evaluation cost for the API cohort is published.

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant         | Purpose                 | Stated score-comparability interpretation            | Status           |
| :---------------------- | :---------------------- | :--------------------------------------------------- | :--------------- |
| Public Training (1,000) | Development/prototyping | Uncalibrated; not comparable                         | Active           |
| Public Eval (120)       | Local public evaluation | Calibrated (IDD to private sets)                     | Active           |
| Semi-Private Eval (120) | Kaggle leaderboard      | IDD to public eval                                   | Active, withheld |
| Private Eval (120)      | Final prize scoring     | IDD to other eval sets                               | Active, withheld |
| ARC-AGI-1               | Parent benchmark        | Non-interchangeable; used to show v2 difficulty jump | Prior version    |

### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [x] Hidden test set selected by maintainers
- [x] Versioned dataset slice

### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [x] Reference answer
- [x] External verifier (Kaggle sandbox/harness)
- [x] Leaderboard submission metadata

### 2.18 Broad-Claim Flags for Later Evaluation

| Prompt                                                     | Response                                                                                        |
| :--------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| Term used for broad interpretation from benchmark scores   | "AGI", "general fluid intelligence", "human-like AI capabilities".                              |
| Breadth implied by the score interpretation across domains | High breadth implied by naming/marketing, despite narrow single-domain task structure.          |
| Capability domains explicitly excluded or not tested       | Language, world knowledge, social reasoning, long-term memory, tool use, auditory processing.   |
| Stated AGI, autonomy, or agency caveats                    | Policy states ARC is "necessary but not sufficient" for AGI, not a complete litmus test.        |
| Documented caveats to carry forward into Part B            | Gap between AGI marketing language and task breadth; missing statistical uncertainty intervals. |

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

Scoring is fully automated, rule-based, and deterministic: a submitted output grid is compared cell-by-cell against the reference grid, and a task counts as solved only if every test input for that task is reproduced exactly. Two attempts per test input are permitted by design (pass@2). Semi-private and private scoring is executed by a leaderboard service rather than by the evaluator, through the Kaggle sandbox for competition entries. No model-as-judge, human rater, or partial-credit mechanism is involved.

### 3.2 Scores and Metrics

- **Primary score:** fraction of tasks fully solved within two attempts, as an unweighted average across the tasks in an evaluation split.
- **Subscores:** per-split accuracy for Public Eval, Semi-Private Eval, and Private Eval, reported separately rather than aggregated.
- **Derived score:** cost-per-task in USD, submitter-reported and presented alongside accuracy on the public leaderboard as an efficiency axis.
- **Threshold:** 85% on Private Eval triggers the ARC Prize Grand Prize. This is a competition trigger, not a calibrated capability band.

Malformed outputs fail the corresponding test input. Explicit error handling, retry, and parser-fallback policy is delegated to the evaluator or to the Kaggle harness rather than being specified in the public repository, and no adjudication route exists beyond the two permitted attempts. The Kaggle regime enforces a 12-hour wall-clock budget, after which a submission fails.

### 3.3 Scale or Metric Types

All scores are accuracy or pass-rate quantities bounded in [0,1], with pass@2 fixed by construction. A cost-adjusted axis (cost-per-task) accompanies accuracy, and a single decision threshold (85%) is defined for the prize. Scoring is binary at the task level; no partial credit is available.

### 3.4 Score Transformation

No transformation, standardization, equating, or norming is applied. The published formula for combining results is an unweighted average across tasks within a split.

### 3.5 Documented Reference Groups, Baselines, and Comparators

- **Chance floor:** effectively 0% given the open-ended grid output space.
- **Human reference:** a controlled human-testing campaign of 407 unique participants across 515 sessions and 13,405 attempts, conducted November 2024 to May 2025, with 90-minute sessions and per-task incentives. Reported outcomes include 75% per-attempt success and 62% session-level success, with a median of 2.2 minutes per solved task. Every retained ARC-AGI-2 task was solved by at least two independent testers within two attempts.
- **Model cohort:** frontier reasoning models (including o3 medium/high and o3-mini high) reported in the technical report, with a broader cohort on the public leaderboard.
- **Historical comparator:** per-model ARC-AGI-1 versus ARC-AGI-2 scores, used to establish the difficulty jump. The authors treat v1 and v2 scores as non-interchangeable.
- **Split comparator:** Public, Semi-Private, and Private Eval, claimed to be independent and identically distributed by the calibration procedure.
- **Expert baseline:** no separately reported qualified domain-expert cohort.

### 3.6 Score Uncertainty and Stability

Headline scores are reported as point estimates. No confidence intervals, standard errors, bootstrap intervals, per-split intervals, repeat-run variance, or prompt-sensitivity analysis was located for the reported accuracies. The only reported consistency statistic concerns human raters: task retention required at least two independent human solves. The splits are documented as calibrated to within roughly 1% of equivalent human difficulty. With 120 tasks per split, a 1 percentage point difference corresponds to approximately one task, so the absence of uncertainty quantification is an evidence gap rather than a refuted claim.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

Exact-match accuracy was chosen as a deterministic, language-free, knowledge-light scoring rule that minimizes scorer ambiguity for grid outputs, and its range is documented as [0,1] with 100% saturating a split. The authors identify brute-force program search as the principal non-target behavior and report active suppression of it during curation. Because the canonical scorer is an exact integer-matrix comparison, no separate parser-validation report is provided. Response-format burden is only partially separated from the target capability: the two-attempt allowance permits recovery from minor formatting mistakes, but no study quantifies how often format errors are recorded as reasoning failures. Sensitivity to small item or prompt changes is not formally reported, score differences are not interpreted statistically, and score interpretation is linked only qualitatively to fluid intelligence and compositional reasoning. Aggregate reporting is a single accuracy number; the maintainers' caveat that solving ARC-AGI-2 is necessary but not sufficient for AGI lives in the paper and policy pages rather than on the leaderboard, and no enumerated non-use list was located.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

Public aggregate scores, submission metadata, evaluation-cohort labels, public/private split scores, and a leaderboard snapshot are available through `arcprize.org/leaderboard` and the Kaggle competition leaderboard. Per-item scores, model responses, traces, capability-domain profiles, and confidence intervals are not published. Kaggle solutions remain with submitters absent prize-related disclosure.

### 4.2 Output Name or Description

| Output | Description | Public/private | Maintainer / host |
| :--- | :--- | :--- | :--- |
| ARC Prize public leaderboard | Accuracy and cost-per-task by model, with cohort labels | Public | ARC Prize Foundation |
| Kaggle competition leaderboard | Semi-private set accuracy during the competition | Public | Kaggle / ARC Prize Foundation |
| Technical report tables (arXiv:2505.11831v2) | Per-model accuracy, human baseline, design analysis | Public | Authors |
| ARC Prize blog posts | Narrative analysis, winners, prize awards, methods notes | Public | ARC Prize Foundation |

### 4.3 Output Design or Presentation

Outputs appear as a static technical report with tables, a cost-versus-accuracy scatter visualization on the website, and a public leaderboard supporting basic filtering. There is no results API and no per-item export.

### 4.4 Output Structure

Reporting is aggregate-score based, rank based, cost or efficiency adjusted, split or cohort based, and version-window based by ARC Prize cycle. No capability-domain profile, difficulty band, or per-item structure is published, and per-task labels for the four core challenge types are not released.

### 4.5 Sensitivity to Context

A single primary leaderboard format serves all contexts. No context-dependent reporting variant is defined, and the Kaggle and API-hosted cohorts are presented on the same surface without prominent runtime-environment labelling.

### 4.6 Development of Outputs

Outputs derive from the benchmark authors' design, from human annotation for the human-baseline data, and from automatic generation by the Kaggle platform for competition standings.

### 4.7 Modifiability

Outputs are not modifiable by end users. Evaluators may run public tasks locally with their own harness, but the official leaderboard record is maintainer-controlled.

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

Linkage between tasks, the exact-match score, and the reported interpretation is clear, but the labels involved are coarse: one capability framing and one accuracy number. The absence of per-task challenge-type labels prevents any finer linkage between sub-categories and reported scores.

### 4.9 Output Content

Outputs include aggregate rankings, cost/latency and efficiency data, worked success and failure examples in the paper figures, and caveats that are prominent in the paper but less visible on the leaderboard. No confidence intervals, coverage map, or excluded-domain caveat panel accompanies the headline numbers.

### 4.10 Intended Recipients

Named recipients are AI researchers, model developers, benchmark maintainers, competition entrants, and a general public audience reached through the leaderboard and blog.

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

Documentation forms present are the arXiv technical report, the repository README, an informal README-level dataset description, Kaggle competition submission instructions, scoring documentation in the repository and paper, and a partial changelog through arXiv revision history and ARC Prize blog posts.

### 5.2 Distribution and Access Model

Access is public for training and public evaluation materials but with restricted answer keys and hidden tests beyond them. The semi-private set is reachable only through a controlled-access Kaggle route, the private set is a held-out evaluation service retained by the maintainers, and both are leaderboard-only submission routes operating under competition distribution rules.

### 5.3 Methods of Publication

Publication routes are the academic paper (arXiv:2505.11831v2), the benchmark website `arcprize.org`, the Git repository `arcprize/ARC-AGI-2` under Apache-2.0, the Kaggle leaderboard platform, and contest-organizer channels including the ARC Prize blog.

### 5.4 User Requirements or Qualifications

Users need comfort with JSON task files, model APIs or local inference, and Python tooling; for the competition route they must be able to package an offline Kaggle submission. Dataset access is public for training and public evaluation, Kaggle-mediated for semi-private, and closed for private. Compute requirements are 4x L4 GPUs within a 12-hour budget for Kaggle, or pay-as-you-go inference for the API cohort. A Kaggle account, ARC Prize registration, and acceptance of the competition agreement are required for contest entry. No human expertise is needed at scoring time, and the public materials carry an Apache-2.0 licence. Competitors are bound by standard Kaggle terms and must not use the private set.

### 5.5 Dataset and Item Access

Training items (1,000) and public evaluation items (120) are fully public with answer keys. The semi-private set (120) is restricted and hidden, accessible only through Kaggle scoring; the private set (120) is hidden and functions as the controlled reserve. Retired or archived evaluation items are not available, and raw model outputs, traces, and submitted solutions are not published.

### 5.6 Provenance and Contamination Documentation

Data origin and task creation, the rationale for the public-versus-hidden split, the private-set owner, and a persistent benchmark identifier are documented. Source-material timing, contributor qualifications, deduplication and overlap checks, prior-exposure screening, searchability checks, post-release contamination risk, training-use prohibition, and item-rotation rules are only partially documented. Canary strings, prior-exposure diagnostics, leak-response policy, rerun or replacement triggers, hash commitments or tamper-evident logs, and reporting of unintended disclosures are absent. The tiered public/semi-private/private split design is itself the principal contamination control, and the private set functions as the encrypted or controlled-release reserve.

### 5.7 Reproducibility Materials

Complete public task data, an administering platform (the Kaggle sandbox plus community reference implementations), and scoring code are available, the last being near-trivial given exact matching. Absent are a canonical prompt template (prompting is evaluator-defined), an environment file or dependency list, a container image, judge or simulator versioning, random seeds or deterministic settings, a reproduction script for published results, fixtures, and CI. Independent replication of a published leaderboard figure is therefore not push-button.

### 5.8 Maintenance and Versioning

The ARC Prize Foundation (Chollet, Knoop, Kamradt, Landers, and Pinkard) maintains the benchmark, owns the private set, and operates the public leaderboard, with Kaggle operating the competition leaderboard. Kaggle competition rules govern contest eligibility and permit multiple submissions per cycle, while public leaderboard reporting policy is described only informally. Cohort labels exist by ARC Prize cycle, and public and private scores are reported separately with no formal aggregation. The scoring rule is invariant, but harness versions are not exposed externally. Stale-score policy, model-version update policy, item-correction process, deprecated-item handling, hidden-item rotation rules, harness health checks, build or CI status, retired-item audit policy, and cross-cohort comparison policy are all undocumented. The arXiv revision history and blog serve as a partial changelog. The 85% Grand Prize threshold acts as the de facto saturation target, and the announced ARC-AGI-3 implies continued parallel operation rather than deprecation. The authors explicitly treat v1 and v2 scores as non-interchangeable. Long-term archival rests on the repository and arXiv; no dataset DOI was located.

---

## Appendix A. General Description of the Benchmark

ARC-AGI-2 is the second-generation public benchmark in the Abstraction and Reasoning Corpus family, created by François Chollet and colleagues at the ARC Prize Foundation. It preserves the original ARC format, in which each item is a grid puzzle built from a small number of demonstration input/output integer-grid pairs plus one or two held-out test inputs, while being newly curated to target compositional patterns the authors group into four challenge types: multi-rule reasoning, multi-step reasoning, contextual rule application, and in-context symbol definition. The release comprises a 1,000-task uncalibrated training set and a 120-task calibrated public evaluation set under Apache-2.0, with two further 120-task sets (semi-private and private) withheld for the Kaggle leaderboard and the ARC Prize contest respectively. All three evaluation sets are described as statistically similar and were calibrated through a controlled human-testing campaign involving 407 participants across 515 sessions, with every retained task solved by at least two independent testers within two attempts. Scoring is exact-match: a task counts as solved when all of its test outputs are reproduced correctly within two attempts, and the headline metric is unweighted accuracy across a split, reported alongside cost-per-task. The benchmark is administered in two materially different regimes, an offline Kaggle sandbox bounded by hardware and a 12-hour budget, and an API-hosted public leaderboard bounded by cost. It is publicly framed as a stress test of fluid intelligence and as progress toward AGI, with the explicit maintainer caveat that solving it is necessary but not sufficient for AGI.

---

# Part B. Evaluation of the Benchmark

## Information Sources

Information sources that might inform Part B include:

- Official benchmark papers, technical reports, model cards, dataset cards, websites, documentation hubs, repositories, leaderboards, scorecards, dashboards, and changelogs supplied or maintained by benchmark creators.
- Public benchmark materials such as task files, prompts, rubrics, reference answers, scorer code, harness code, examples, raw outputs, submission rules, issue trackers, release notes, and archived versions.
- Open information in academic literature, benchmark-quality literature, audit reports, replication studies, analyses of prior model exposure to benchmark items or answers, validation studies, and independent technical commentary. Use these sources to contextualize or challenge score interpretations, not to replace official facts.
- Maintainer-provided or access-controlled information that is not normally supplied to users. If such material affects a rating, state clearly in the Reviewer notes that the rating depends on non-public material inspected by the reviewer.
- Confidential or restricted technical information, such as hidden test splits, item provenance, audits for prior exposure to benchmark items or answers, scorer validation reports, calibration data for scoring by another model, or security details. If reviewed under access restrictions, describe only the rating implication and the access status, without disclosing restricted content.

## Explanation of Ratings

All rating items use the EFPA-style scale below unless a section states otherwise. Detailed "Excellent" anchors identify what a rating of `4` would require for that item. Lower ratings should be assigned by reviewer judgment, considering the benchmark's intended use, scope of score interpretation, decision stakes, technical complexity, evidence quality, and consequences of misinterpretation.

Where a `0` or `1` rating is assigned to an attribute that is critical for the benchmark's stated purpose, the review should caution that the benchmark is suitable only for limited exploratory, research, or expert-qualified use unless stronger evidence is supplied. Critical attributes will vary by benchmark: for example, controls for prior model exposure to benchmark items or answers may be critical for public knowledge benchmarks, scorer consistency may be critical for open-ended generation benchmarks, and reference points used to interpret scores may be critical for leaderboards used in procurement or policy.

Overall ratings must be based on reviewer judgment rather than mechanical averaging. A single severe gap may dominate the overall rating when it undermines the intended score meaning; conversely, a narrow gap may be less consequential when the benchmark's score interpretation is modest and clearly bounded.

### Rating Scale

| Rating | Meaning                                                                                |
| :----: | :------------------------------------------------------------------------------------- |
|  n/a   | This attribute is not applicable to this benchmark or its stated use.                  |
|   0    | Not possible to rate because no, or insufficient, information is provided.             |
|   1    | Inadequate for the benchmark's stated purpose or intended interpretation.              |
|   2    | Adequate: sufficient for cautious use, with limitations that should be stated.         |
|   3    | Good: clear, relevant, and mostly complete support, with no major interpretive threat. |
|   4    | Excellent: comprehensive, well-documented, and strongly aligned with the item anchor.  |

## General Guidance on Assigning Ratings

It is difficult to set universal thresholds for benchmark quality. The adequacy of evidence depends on what capability or quality the benchmark claims to measure, how scores are used, whether comparisons are high stakes, whether tasks are public or hidden, whether scoring is deterministic or judgment-based, and whether the benchmark is stable or regularly refreshed. Ratings should therefore be anchored in the intended score meaning, not in a generic expectation that every benchmark must supply every possible form of evidence.

For descriptive gaps, first ask what evidence would be needed to support the benchmark's actual score interpretation. A missing human reference point, for example, may be serious for a benchmark claiming expert-level performance but less central for a narrow regression test. A missing audit for prior model exposure may be serious for public web-derived knowledge tasks but less central for a private live-environment evaluation with documented release controls.

For broad interpretations made from benchmark scores about intelligence, AGI, reasoning, agency, autonomy, or cross-domain competence, require stronger breadth and validity evidence than for narrow capability interpretations.

Ratings should be based on the information available, with comments explaining consequential evidence, limitations, and rating rationale where needed.

## Section 6. Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition

- **Rating:** 3
- **Evidence:** The benchmark gives a clear, theoretically grounded definition of fluid intelligence via compositional generalization on novel grid tasks, explicitly excluding general world knowledge.
- **Missing evidence:** The mapping between the narrow grid-task construct and the broad "AGI" claim used in marketing is not formally theoretically bridged.
- **Reviewer/editor rationale:** The rationale for the narrow operationalization is excellent and clear. The broader AGI framing exceeds what the construct definition supports.
- **Interpretation caution:** Interpret scores as "compositional grid-puzzle generalization", not as proof of domain-general AGI.

#### 6.1.2 Summary of prior research and benchmark context

- **Rating:** 3
- **Evidence:** The technical report situates ARC-AGI-2 in the lineage of ARC-AGI-1, names the documented limitations of v1 (brute-force susceptibility, low ceiling on hard items, calibration drift), and explains how v2 responds to each.
- **Missing evidence:** External comparison to reasoning benchmarks outside the ARC family is light, and no engagement with psychometric or measurement-quality literature is present.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Within-family contextualization is strong; cross-family contextualization is thin but does not undermine the section.

#### 6.1.3 Phenomenon-task-metric-claim chain

- **Rating:** 2
- **Evidence:** The chain from fluid reasoning to held-out grid tests and exact-match pass@2 scoring is logical and explicit in the technical report.
- **Missing evidence:** The chain from exact-match metrics to broad "progress toward AGI" claims remains contested. Additionally, formatting/serialization burdens for LLMs are not cleanly separated from reasoning failures.
- **Reviewer/editor rationale:** The inner chain (task to metric) is strong. The outer chain (metric to AGI claim) is weak. Adequate for cautious use.
- **Interpretation caution:** Claims must be phrased around ARC-style abstraction, not generalized intelligence.

#### 6.1.4 Task or item design

- **Rating:** 3
- **Evidence:** Grid format, colour set, demonstration count, and the two-attempt policy are documented and justified as continuous with ARC-AGI-1. The four challenge categories (multi-rule reasoning, multi-step reasoning, contextual rule application, in-context symbol definition) give an explicit design rationale for new items.
- **Missing evidence:** Per-task category labels are not shipped with the data, so per-category analysis cannot be independently reproduced.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The design is well-motivated and deliberately continuous with the prior version; the auditability gap on category labels is real but bounded.
- **Interpretation caution:** Claims about which challenge type a system struggles with cannot be verified from the public release.

#### 6.1.5 Procedures for developing task or item content

- **Rating:** 3
- **Evidence:** Tasks were authored by foundation experts, subjected to redundancy detection, and calibrated through a massive 407-participant human testing campaign (requiring ≥2 human solves per task).
- **Missing evidence:** Full task-authoring rubrics and detailed item-level provenance logs are not fully public.
- **Reviewer/editor rationale:** The empirical human-solvability gating is unusually rigorous for AI benchmarks, warranting a Good rating.
- **Interpretation caution:** Hidden-set item quality remains trust-mediated as it cannot be independently audited.

#### 6.1.6 Thoroughness of the final task or item selection process

- **Rating:** 3
- **Evidence:** Selection is anchored by an empirical human-solvability gate, and the three evaluation sets are claimed to be independent and identically distributed, calibrated to within roughly 1% of equivalent human difficulty.
- **Missing evidence:** The IDD claim is not accompanied by a published statistical test or distributional analysis.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The selection principle is strong and empirically grounded; public validation of the equivalence claim is partial.
- **Interpretation caution:** Cross-split comparisons rest on an asserted rather than demonstrated equivalence.

#### 6.1.7 Quantitative evidence of task or item quality

- **Rating:** 2
- **Evidence:** Human attempt-level success (~75%), session-level success (~62%), median solve time (2.2 minutes), and reported non-correlation with participant demographics establish aggregate task tractability.
- **Missing evidence:** No per-item difficulty parameters, discrimination indices, ceiling or floor analysis, or IRT-style item statistics are published.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. The aggregate human evidence is genuinely strong, but MESA distinguishes aggregate tractability evidence from item-level quality statistics, and the latter is absent. This is consistent with the strict stance taken at 6.2.4.
- **Interpretation caution:** Item-level quality is established collectively, not individually; a low score cannot be attributed to specific item defects.

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice

- **Rating:** n/a
- **Evidence:** ARC-AGI-2 is a newly curated successor benchmark rather than an adaptation, translation, or slice of ARC-AGI-1, and the authors explicitly describe v1 and v2 scores as non-interchangeable.
- **Reviewer/editor rationale:** Reviewer 1 assigned 3 and Reviewer 2 assigned n/a. Resolved to n/a. Assigning a substantive rating to a criterion that does not apply to the reviewed entity is a category error; the successor relationship is already evaluated under 6.1.2 and 8.1.4.

#### 6.1.9 Overall Rationale, development, and task or item quality

- **Rating:** 3
- **Evidence:** Strong official rationale, exceptional human calibration, curated task selection, and public documentation of goals.
- **Missing evidence:** Full broad-claim formalization and complete hidden-set auditability.
- **Reviewer/editor rationale:** A well-motivated construct with a documented calibration procedure. Good for a narrow ARC-style reasoning benchmark.
- **Interpretation caution:** Use as a specific capability signal within a broader portfolio.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- **Rating:** 3
- **Evidence:** The technical report and website state the benchmark's purpose, its intended audience of frontier-reasoning researchers, and its relation to ARC-AGI-1. The policy page carries the necessary-but-not-sufficient AGI caveat.
- **Missing evidence:** No formal out-of-scope use list, and no procurement or policy non-use guidance.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Purpose and audience are clearly stated; the absence of an enumerated non-use list is carried into Section 10.6 and 11.5 rather than penalised twice here.

#### 6.2.2 Documentation of development process

- **Rating:** 3
- **Evidence:** The paper documents the human-testing campaign, the calibration procedure, the removal of brute-forceable tasks, and the overall design philosophy.
- **Missing evidence:** Per-task provenance, individual author credits, and selection logs are not externally visible.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The process documentation is above the norm for AI benchmarks, with residual gaps confined to item-level attribution.

#### 6.2.3 Documentation of scoring and metrics

- **Rating:** 2
- **Evidence:** Guide and benchmarking repo document exact scoring (pass@2).
- **Missing evidence:** There is a noted discrepancy in the repository README mentioning "3 trials" while official rules state 2 trials. Complete malformed-output fallback policies are not fully centralized.
- **Reviewer/editor rationale:** Scoring is understandable and objective, but procedural edge cases (like trial limits and JSON parsing errors) require a tighter, consolidated rulebook.
- **Interpretation caution:** Trial count implementations must be verified before making direct inter-system comparisons.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- **Rating:** 1
- **Evidence:** The benchmark reports that the three evaluation splits were calibrated to equivalent human difficulty (within 1%).
- **Missing evidence:** No model-side confidence intervals, standard errors, run-to-run variance, or prompt sensitivity analyses are published for headline scores.
- **Reviewer/editor rationale:** On a 120-task split, 1 percentage point equals approximately 1 task. The lack of confidence intervals makes small leaderboard differences mathematically uninterpretable.
- **Interpretation caution:** Close leaderboard ranks should be treated as ties unless statistical significance is independently calculated.

#### 6.2.5 Documentation of validity evidence

- **Rating:** 2
- **Evidence:** The paper argues content validity through curation against brute-force tactics and through empirical human solvability, and reports the ARC-AGI-1 to ARC-AGI-2 difficulty jump per model.
- **Missing evidence:** No external convergent or discriminant evidence, no cross-benchmark correlation, and no predictive-relevance study.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Content validity is documented; relations to other variables are not.

#### 6.2.6 Documentation of fair use and comparability

- **Rating:** 2
- **Evidence:** The distinction between the Kaggle sandbox cohort and the API-hosted cohort is described informally on the site, and cost-per-task is reported as an efficiency axis.
- **Missing evidence:** No formal cohort-comparability guidance, no rules stating when cross-cohort comparison is valid, and no accessibility discussion.
- **Reviewer/editor rationale:** Both reviewers rated this 2. The cohorts are named but not governed, which is the root of the Section 11.3 comparability finding.
- **Interpretation caution:** Do not compare a Kaggle-sandbox score against an API-hosted score without verifying the runtime conditions.

#### 6.2.7 Documentation of maintenance and versioning

- **Rating:** 2
- **Evidence:** arXiv revision history and ARC Prize blog posts provide an informal changelog, and ARC Prize cycle labels give coarse evaluation-window identification.
- **Missing evidence:** No formal benchmark-data changelog, deprecation policy, or item-correction process.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Maintenance is evidently active but informally recorded, leaving score provenance under-specified over time.

#### 6.2.8 Adequacy of documentation available to users

- **Rating:** 2
- **Evidence:** Multiple sources cover purpose, tasks, scoring, and basic access policies.
- **Missing evidence:** Information is distributed across blogs, GitHub, and websites. Uncertainty reporting and detailed edge-case scoring rules are missing.
- **Reviewer/editor rationale:** Documentation is sufficient for basic research use but lacks the statistical and procedural rigor required for high-stakes interpretations.
- **Interpretation caution:** Users must actively document their specific run conditions (e.g., cohort, prompt, verifier) as the docs do not enforce a single standard.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- **Rating:** 2
- **Evidence:** The public repository is trivially usable for local runs on the public split, and the Kaggle competition supplies a fully enforced runtime with fixed hardware and time budget.
- **Missing evidence:** No canonical prompt template and no reference harness for the API-hosted cohort, so different evaluators can produce materially non-identical conditions.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. The Kaggle route is well specified, but the leaderboard mixes it with an unspecified API route, and the weaker of the two governs auditability. This is consistent with the existing 6.3.7 rating.
- **Interpretation caution:** Independently run scores need not match official leaderboard conditions.

#### 6.3.2 Scoring procedure and error handling

- **Rating:** 2
- **Evidence:** Exact-match scoring leaves little ambiguity once outputs are parsed, and the pass@2 rule is stated in both the paper and the repository.
- **Missing evidence:** Documented behaviour for malformed JSON, partial grids, and dimension mismatches outside the Kaggle harness. Reviewer 2 additionally rated the Kaggle path higher than the open-use path.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 gave a split 3/2 by route. Resolved to 2 on the open-use path, matching the existing 6.2.3 finding that malformed-output policy is not centralised.

#### 6.3.3 Interpretation and reporting guidance

- **Rating:** 2
- **Evidence:** The paper carries strong interpretive caveats, including the explicit necessary-but-not-sufficient framing for AGI.
- **Missing evidence:** The leaderboard surface does not foreground these caveats for lay readers, and no statistical guidance defines a meaningful score difference.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Guidance exists where researchers read it and is absent where the public reads it.

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- **Rating:** 2
- **Evidence:** Kaggle competition rules state hardware, offline, and time constraints, and the Apache-2.0 licence governs the public materials.
- **Missing evidence:** Public-leaderboard rules for fair cross-system comparison, including permitted run counts and how cost is computed, are not centrally codified.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. Contest restrictions are well documented, but the public leaderboard, which is the surface most widely cited, is the one lacking codified rules.

#### 6.3.5 Technical support and implementation guidance

- **Rating:** 2
- **Evidence:** GitHub issues and the Kaggle discussion forum are active community channels, and the ARC Prize blog provides methods notes.
- **Missing evidence:** No documented troubleshooting page, no smoke-test fixtures, and no stated support expectations.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. Community channels exist, but MESA treats maintained fixtures and troubleshooting material as the evidence that support is reproducible rather than ad hoc.

#### 6.3.6 References and supporting materials

- **Rating:** 3
- **Evidence:** The paper, blog, policy pages, and repository cross-reference each other, and the ARC-AGI-1 lineage is thoroughly cited.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Referencing is complete and navigable.

#### 6.3.7 Quality of procedural instructions

- **Rating:** 2
- **Evidence:** Usable instructions exist for the Kaggle sandbox and open benchmarking CLI.
- **Missing evidence:** No single canonical prompt template or frozen evaluation package is mandated for the API-hosted leaderboard cohort.
- **Reviewer/editor rationale:** Adequate for cautious technical use, but the lack of a universal reference harness for API models permits evaluation variance.
- **Interpretation caution:** Do not assume independently run public scores perfectly match official leaderboard setups.

### 6.4 Overall Adequacy of Rationale and Documentation

- **Rating:** 3
- **Reviewer/editor rationale:** The benchmark provides a strong, source-grounded rationale, defensible human-calibrated development, and usable instructions. The rating is withheld from a 4 primarily due to missing statistical uncertainty documentation and fragmented scoring edge-case rules.

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability

- **Rating:** 3
- **Evidence:** Public tasks are fully available via GitHub under Apache 2.0. Hidden sets are controlled through Kaggle/ARC Prize infrastructure.
- **Missing evidence:** Semi-private/private sets cannot be independently inspected.
- **Reviewer/editor rationale:** The public/private split design is well-executed and justified to prevent data contamination.
- **Interpretation caution:** Hidden-set validity relies entirely on the maintainer's claim that sets are Independent and Identically Distributed (IID).

#### 7.1.2 Prompts, instructions, and input materials

- **Rating:** 2
- **Evidence:** Task JSON is self-describing, and the grid format requires no natural-language instruction to interpret.
- **Missing evidence:** No canonical prompt template is published. Community implementations vary in how grids are textually encoded, and that encoding choice can materially affect scores.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. Self-describing data is not the same as a specified input condition; because the leaderboard compares systems whose serialization differs, the absence of a canonical prompt is a comparability defect rather than a convenience gap.
- **Interpretation caution:** Score differences may partly reflect grid-serialization choices rather than reasoning ability.

#### 7.1.3 Rubrics, reference answers, and response format requirements

- **Rating:** 3
- **Evidence:** Reference outputs are exact grids and the comparison rule is unambiguous, which removes the rubric ambiguity that affects free-text benchmarks.
- **Missing evidence:** No documented admissible-variant policy for whitespace, trailing rows, or dimension mismatch outside the Kaggle harness.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The reference-answer design is a genuine strength of the exact-match format; the residual edge-case gap is recorded at 6.3.2 rather than penalised again here.

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- **Rating:** 2
- **Evidence:** Open benchmarking repository exists with adapters; Kaggle provides an official, controlled scoring runtime.
- **Missing evidence:** No official, version-pinned, canonical open-source harness is enforced for the API-hosted leaderboard results.
- **Reviewer/editor rationale:** Implementation infrastructure exists, but variance in community harnesses can affect serialization and parsing, altering scores.
- **Interpretation caution:** Ensure harness versions and JSON parsing scripts are identical when comparing local or API-based model runs.

#### 7.1.5 Interface and workflow usability

- **Rating:** 3
- **Evidence:** The testing interface at `arcprize.org/play` provides a polished web UI for human testing and exploration, and the repository follows a conventional, navigable structure.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Workflow usability is a clear strength for both human testers and evaluators working on the public split.

#### 7.1.6 Accessibility across modalities, languages, and system types

- **Rating:** 2
- **Evidence:** The design is language-free and runs on any system able to read JSON. Colours are encoded as discrete integer indices, so systems consuming raw integers are unaffected by colour perception.
- **Missing evidence:** The human-testing UI's accessibility for visually impaired testers is not documented, and the calibration campaign was sighted-only. Grid tasks presented visually versus as token sequences impose materially different burdens across system types.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 3. Resolved to 2. The language-free design genuinely aids cross-linguistic accessibility, but the modality asymmetry between the human UI and model serialization is a documented accessibility limit, and Reviewer 1's stricter reading is better supported.
- **Interpretation caution:** The human reference and the model condition are not modality-matched.

#### 7.1.7 Licensing, use requirements, and risk warnings

- **Rating:** 3
- **Evidence:** Public materials carry an explicit Apache-2.0 licence, competition rules cover prize eligibility and permitted use, and grid puzzles present no sensitive-content risk.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Licensing is explicit and unambiguous, which contrasts sharply with benchmarks that ship no licence at all.

#### 7.1.8 Overall quality of benchmark materials

- **Rating:** 3
- **Reviewer/editor rationale:** Materials are clean, licensed, and highly usable. The exact-match integer grid format is highly accessible to multimodal and text-only models alike.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- **Rating:** 2
- **Evidence:** The effective chance floor is approximately 0% given the open-ended grid output space, and the ceiling is 100% within a split. A sample random baseline is present in the open benchmarking repository.
- **Missing evidence:** No empirical trivial-strategy baseline is reported, such as copy-input, identity transformation, or majority-pixel fill.
- **Reviewer/editor rationale:** Both reviewers rated this 2. The analytic floor is obvious, but obviousness is not measurement: without trivial-strategy baselines, the benchmark cannot demonstrate that low scores reflect failed reasoning rather than failed output formatting.

#### 8.1.2 Human or expert baselines

- **Rating:** 3
- **Evidence:** An extensive campaign (407 participants, 515 sessions, 13,405 attempts) with documented compensation and solvability gating.
- **Missing evidence:** Full demographic distributions, geographic coverage, and condition-matching (humans use a visual UI; models use JSON) are not fully detailed.
- **Reviewer/editor rationale:** This is one of the most rigorous human calibration campaigns in current AI benchmarks. It establishes clear human feasibility.
- **Interpretation caution:** Human UI interaction differs fundamentally from LLM token serialization; the "human baseline" is a reference, not an exact equivalent process.

#### 8.1.3 Model comparator cohort

- **Rating:** 3
- **Evidence:** Technical reports and leaderboards track major frontier models (o3, Claude 3.5, Gemini, etc.).
- **Missing evidence:** Cohort conditions (prompts, exact scaffolding, budget) for the API-hosted models are not systematically tracked or standardized on the leaderboard.
- **Reviewer/editor rationale:** Good general context, but cohort hygiene is mixed.
- **Interpretation caution:** API-hosted model scores utilizing custom scaffolding should not be directly compared to offline, compute-bounded Kaggle submissions.

#### 8.1.4 Historical, version, or benchmark-family comparators

- **Rating:** 3
- **Evidence:** Per-model ARC-AGI-1 versus ARC-AGI-2 deltas are reported and are large enough to be interpretable without uncertainty intervals (for example o3 medium falling from roughly 53% to 3%).
- **Missing evidence:** No formal equating or normalization between v1 and v2 is provided, though the authors explicitly caveat non-interchangeability.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The version comparison is well-documented and the non-interchangeability caveat is stated rather than implied.

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- **Rating:** 2
- **Evidence:** The 85% Private Eval Grand Prize threshold is operationally defined and unambiguous.
- **Missing evidence:** The threshold is a competition decision rather than an empirically justified proficiency band, and the paper does not tie it to a specific capability claim. No intermediate score bands are defined.
- **Reviewer/editor rationale:** Both reviewers rated this 2. A number that triggers a prize is not a criterion-referenced standard.
- **Interpretation caution:** Do not read the 85% threshold as a validated marker of human-level or AGI-level competence.

#### 8.1.6 Representativeness of reference groups

- **Rating:** 2
- **Evidence:** The human cohort is large (407 participants, 515 sessions), demographically heterogeneous, time-bounded to November 2024 through May 2025, and reported as non-correlated with participant demographics.
- **Missing evidence:** Geographic and linguistic coverage of the participant pool is not fully described, and no qualified domain-expert subgroup is separately reported. The model cohort is not systematically sampled.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 3. Resolved to 2. The cohort size is impressive, but representativeness is a claim about composition rather than size, and the composition is only partially documented.

#### 8.1.7 Currency and maintenance of baseline evidence

- **Rating:** 3
- **Evidence:** The human baseline is current to within roughly twelve months of the v2 release, and the leaderboard is updated as new models appear.
- **Missing evidence:** No documented plan to refresh the human baseline if task semantics or the participant pool shift, and no schedule for re-running earlier model entries.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Baseline evidence is current; its maintenance is undocumented but not yet stale.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- **Rating:** 3
- **Reviewer/editor rationale:** The human baseline is exceptionally strong. Reference interpretation is only limited by the lack of statistical uncertainty margins for the model comparator cohorts.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- **Rating:** 1
- **Evidence:** Deterministic exact scoring is used.
- **Missing evidence:** No full reliability study across prompts, reruns, seeds, model settings, or confidence intervals for the 120-task splits.
- **Reviewer/editor rationale:** The lack of variance reporting is a critical flaw for a benchmark utilized to make fine-grained leaderboard distinctions.
- **Interpretation caution:** A single-run score on 120 tasks provides a fragile point estimate of a model's true capability.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- **Rating:** 1
- **Evidence:** The pass@2 protocol captures one limited dimension of stochasticity by allowing a second attempt per test input.
- **Missing evidence:** No multi-seed, multi-run, or temperature-sensitivity report was located, and sampling settings are evaluator-defined rather than specified by the benchmark.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 1. Adjusted to 1. Pass@2 is an attempt-allowance rule, not a stability measurement; treating it as stability evidence would overstate what the protocol demonstrates. This is consistent with the existing 9.1.1 rating.
- **Interpretation caution:** A single reported score carries unquantified decoding variance.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- **Rating:** 1
- **Evidence:** No intervals reported.
- **Missing evidence:** Confidence intervals for headline scores.
- **Reviewer/editor rationale:** Without standard errors, leaderboard ranks are statistically uninterpretable.
- **Interpretation caution:** Treat models within a few percentage points of each other as tied.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- **Rating:** 3
- **Evidence:** Scoring is an exact integer-grid comparison. The scorer is mathematically trivial and effectively perfect within its own scope, which removes the scorer-validity risk that dominates free-text and model-judged benchmarks.
- **Missing evidence:** The reliability of _parsing_ raw model output into a grid depends on the evaluator's harness, which is not standardized outside Kaggle. No parser error rate is published.
- **Reviewer/editor rationale:** Both reviewers rated this 3. The scorer proper is a genuine strength; the unmeasured risk sits in the parsing layer ahead of it, which is recorded at 7.1.2 and 6.3.2.
- **Interpretation caution:** A score of zero on a task does not distinguish a reasoning failure from a serialization failure.

#### 9.3.2 Human rater or expert scorer agreement

- **Rating:** n/a
- **Evidence:** Final scoring is fully automated and involves no human rating. Human participation is confined to the calibration campaign, whose redundancy gate is evaluated at 6.1.5 and 8.1.2.
- **Reviewer/editor rationale:** Reviewer 1 assigned 2 and Reviewer 2 assigned n/a. Resolved to n/a, since the criterion concerns human raters in the scoring loop and there are none.

#### 9.3.3 Model-as-judge reliability and validity checks

- **Rating:** n/a
- **Evidence:** No LLM judge participates in scoring; correctness is determined by deterministic grid comparison.
- **Reviewer/editor rationale:** Both reviewers assigned n/a.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- **Rating:** 1
- **Evidence:** No prompt-sensitivity analyses are published.
- **Missing evidence:** Given that models interpret serialized JSON grids, formatting choices heavily influence LLMs.
- **Reviewer/editor rationale:** Insufficient evidence to claim score stability across different prompt strategies.
- **Interpretation caution:** High performance may reflect optimized JSON prompting rather than fundamentally superior fluid intelligence.

#### 9.4.2 Form, split, version, or refresh equivalence

- **Rating:** 2
- **Evidence:** The maintainers claim the Public, Semi-Private, and Private evaluation sets are independent and identically distributed, and report calibration to within roughly 1% of equivalent human difficulty.
- **Missing evidence:** No formal distributional or score-based equivalence analysis supports the IDD claim, and no alternate-form reliability statistic is published.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. Cross-split comparison is the mechanism by which hidden-set scores acquire meaning, so an asserted rather than demonstrated equivalence is a material gap rather than a documentation nicety.
- **Interpretation caution:** Public-split and hidden-split scores are treated as comparable on the maintainers' assurance alone.

#### 9.4.3 Execution environment and dependency stability

- **Rating:** 2
- **Evidence:** The Kaggle regime pins hardware (4x NVIDIA L4), runtime, and offline status, giving that cohort strong environmental stability.
- **Missing evidence:** No dependency manifest, lockfile, or container image exists for the API-hosted leaderboard cohort, whose hosted model versions drift silently over time.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 gave a split 3/2 by route. Resolved to 2, governed by the weaker open-use path that the public leaderboard actually reports.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- **Rating:** 1
- **Evidence:** Report cautions that scores below 5% are low signal.
- **Missing evidence:** No statistical significance tests for leaderboard deltas.
- **Reviewer/editor rationale:** Meaningful score differences cannot be established without interval reporting.
- **Interpretation caution:** Rank ordering should not imply meaningful capability differences without independent statistical testing.

### 9.6 Overall Reliability, Precision, and Score Stability

- **Rating:** 1
- **Reviewer/editor rationale:** While the exact-match scorer itself is perfectly reliable, the _evidence base_ for interpreting stochastic LLM score differences on a small split is entirely absent.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- **Rating:** 2
- **Evidence:** The four challenge types (multi-rule reasoning, multi-step reasoning, contextual rule application, in-context symbol definition) operationalize the target construct explicitly, and tasks are both curated against brute-force solutions and human-calibrated.
- **Missing evidence:** No published coverage analysis showing the relative frequency of each challenge type or its distribution across difficulty bands, and per-task category labels are not shipped.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. Content is plausibly representative within the grid-puzzle universe, but representativeness is a claim about coverage, and without per-category distribution data the claim cannot be checked.
- **Interpretation caution:** Read scores as performance on the sampled grid-task mix, not on requirements-general abstraction.

#### 10.1.2 Construct breadth and capability-domain coverage

- **Rating:** 1
- **Evidence:** The benchmark explicitly measures fluid intelligence via a narrow visual-symbolic grid format.
- **Missing evidence:** The broad "AGI" claims invoked by the benchmark's name and marketing are not supported by evidence across other necessary CHC domains (e.g., Reading/Writing, General Knowledge, Auditory Processing, Long-Term Memory).
- **Reviewer/editor rationale:** The task surface is fundamentally narrow. It cannot independently support broad cognitive versatility claims.
- **Interpretation caution:** ARC-AGI-2 is a single-domain signal. Do not treat it as a proxy for comprehensive general intelligence.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- **Rating:** 1
- **Evidence:** The paper describes four challenge types qualitatively.
- **Missing evidence:** No quantitative subscores, factor analyses, or per-task category labels are published.
- **Reviewer/editor rationale:** Without data on sub-dimensions, the internal structure remains unvalidated.
- **Interpretation caution:** Aggregate accuracy may mask severe deficits in specific types of reasoning (e.g., multi-step vs. in-context symbol definition).

#### 10.2.2 Item or task behavior across the score scale

- **Rating:** 1
- **Evidence:** Aggregate human-success statistics establish that tasks sit in a tractable difficulty range for people.
- **Missing evidence:** No published item-level discrimination, difficulty distribution, or per-item human-versus-model contrast.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 1. Adjusted to 1. Aggregate human tractability says nothing about how individual items behave across the score scale, which is what this criterion asks; the evidence base for it is absent rather than thin. This is consistent with the existing 10.2.1 rating.

#### 10.2.3 Failure modes and error analysis

- **Rating:** 2
- **Evidence:** The technical report discusses qualitative model-failure patterns, including the brute-force shortcuts that the v2 design suppresses and the compositional-generalization gaps that remain.
- **Missing evidence:** No systematic quantitative error taxonomy with category-level model performance, which the absent per-task challenge-type labels would be required to produce.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Adjusted to 2. The qualitative analysis is genuine but cannot be extended or verified by third parties without category labels.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- **Rating:** 3
- **Evidence:** Exact match aligns naturally with grid-puzzle correctness, leaving no scorer-construct gap of the kind that affects free-text grading, and pass@2 mitigates trivial format-recovery effects.
- **Missing evidence:** No formal study of how often an incorrect output reflects a formatting error rather than a reasoning error, and the unweighted task average conceals per-category structure.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Metric-construct alignment is one of the benchmark's strongest validity properties.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- **Rating:** 2
- **Evidence:** The authors explicitly removed brute-force-amenable tasks during curation and designed v2 specifically to suppress program-search shortcuts that succeeded on v1.
- **Missing evidence:** The mitigation cannot be independently verified, and no red-team study against prompt-engineering shortcuts or grid-representation tricks is published. Serialization choice remains an uncontrolled source of construct-irrelevant variance.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Deliberate shortcut suppression is documented but unaudited.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- **Rating:** 2
- **Evidence:** Per-model ARC-AGI-1 versus ARC-AGI-2 comparisons are reported, and the human calibration campaign supplies a documented human reference point.
- **Missing evidence:** No correlation with other reasoning benchmarks such as HLE, GPQA, or FrontierMath, and no relation to downstream task performance.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Within-family and human relations are documented; external relations are not.

#### 10.4.2 Convergent and discriminant evidence

- **Rating:** 1
- **Evidence:** Comparisons are drawn to ARC-AGI-1.
- **Missing evidence:** No systematic correlation studies against other reasoning benchmarks (e.g., Mensa, GPQA) or knowledge-heavy benchmarks to prove discriminant validity.
- **Reviewer/editor rationale:** Formal convergent/discriminant validity evidence is currently missing.
- **Interpretation caution:** It is unknown how ARC-AGI-2 performance correlates with real-world logical or mathematical reasoning tasks.

#### 10.4.3 Ecological or predictive relevance

- **Rating:** 1
- **Evidence:** The authors do not claim ecological or deployment relevance and explicitly position ARC-AGI-2 as an abstract diagnostic rather than a task-transfer predictor.
- **Missing evidence:** No evidence that ARC-AGI-2 performance predicts success on any real-world task.
- **Reviewer/editor rationale:** Both reviewers rated this 1. The rating records the state of the evidence, not a criticism of the design: the maintainers' own framing is that ecological relevance is out of scope.
- **Interpretation caution:** Do not use ARC-AGI-2 scores to forecast deployed system performance.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- **Rating:** 3
- **Evidence:** A strict public/semi-private/private split is maintained. The Kaggle contest utilizes an offline sandbox.
- **Missing evidence:** No canary strings or public leak-response protocols are documented.
- **Reviewer/editor rationale:** The structural controls (offline sandbox and fully hidden private sets) are robust and effectively mitigate passive data contamination.
- **Interpretation caution:** Semi-private sets used for live leaderboards may still suffer from adaptive overfitting via repeated submissions.

#### 10.5.2 Gameability and benchmark-specific tuning controls

- **Rating:** 3
- **Evidence:** The Kaggle offline sandbox and the maintainer-held private set materially constrain leaderboard gaming, and the 85% Grand Prize threshold remained unmet as of the 2025 cycle, with the top private-eval submission near 24%.
- **Missing evidence:** No formal policy governs test-time training, which is widely used by competitive submitters, so the boundary between legitimate adaptation and benchmark-specific overfitting is left implicit. No rule restricts tuning on the fully public training and evaluation splits.
- **Reviewer/editor rationale:** Reviewer 1 rated 2, citing test-time training and benchmark-specific solver engineering; Reviewer 2 rated 3, citing the offline sandbox and hidden private set. Resolved to `3` as recorded in the Discrepancy Summary: although test-time training is prevalent, the offline compute constraints and the strict private holdout are strong structural controls relative to typical LLM benchmarks.
- **Interpretation caution:** Public-split scores are more vulnerable to tuning effects than semi-private or private scores.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- **Rating:** 2
- **Evidence:** The authors include the explicit caveat that ARC-AGI is a "necessary but not sufficient" condition for AGI.
- **Missing evidence:** The benchmark _name_ ("AGI") and associated prize marketing frequently drive public discourse that exceeds the formal caveats.
- **Reviewer/editor rationale:** The technical authors are cautious, but the public branding is disproportionately broad.
- **Interpretation caution:** Reviewers and journalists must actively rein in "AGI" headlines when reporting ARC scores.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- **Rating:** 1
- **Evidence:** The benchmark name, the prize framing, and the surrounding public communication invoke AGI, psychometric intelligence, and general fluid intelligence, while the task surface is a single modality within a single domain.
- **Missing evidence:** No multi-domain validity argument links ARC-AGI-2 performance to broader cognitive abilities. Under the CHC-grounded breadth framework MESA adopts, the benchmark exercises only the three domains recorded at 2.1 (On-the-Spot Reasoning, Working Memory, Visual Processing) and omits language, general knowledge, long-term memory, planning, social cognition, embodiment, tool use, long-horizon agency, auditory processing, and real-world transfer.
- **Reviewer/editor rationale:** Both reviewers rated this 1. The rating reflects the state of the evidence base rather than the maintainers' conduct: their necessary-but-not-sufficient caveat is explicit and in good faith, but a caveat is not a validity argument.
- **Interpretation caution:** ARC-AGI-2 scores must not be treated as proxies for general intelligence or AGI proximity. They are evidence about novel compositional grid-puzzle reasoning and nothing wider.

### 10.7 Overall Validity Support

- **Rating:** 2
- **Reviewer/editor rationale:** Content validity is solid for the narrow operationalization of grid-based fluid reasoning. Contamination controls are strong. However, internal structure, convergent/discriminant validity, and construct breadth are severely lacking, limiting the validity of broad interpretations.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- **Rating:** 2
- **Evidence:** The construct is plausibly relevant to any system able to ingest grid representations, and the language-free format avoids the linguistic bias that affects text benchmarks.
- **Missing evidence:** No formal discussion of how the construct generalizes across system classes, such as program-synthesis systems versus language models versus hybrid scaffolds.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Relevance is broad in principle but undocumented in practice.

#### 11.1.2 Documentation of fair-use considerations

- **Rating:** 1
- **Evidence:** Very little. The public materials contain no dedicated fair-use, accessibility, or bias-consideration section.
- **Missing evidence:** Any structured treatment of fairness across system classes, access tiers, or participant groups.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 1. Adjusted to 1. The absence is near-total rather than partial, and MESA reserves 2 for documentation that exists but has important gaps.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- **Rating:** 2
- **Evidence:** The language-free design is intrinsically inclusive across linguistic groups, and integer-encoded grids are consumable by text-only and multimodal systems alike.
- **Missing evidence:** Accessibility of the play interface for visually impaired human testers is not documented, and the calibration campaign was sighted-only.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Resolved to 2, consistent with the 7.1.6 resolution: linguistic inclusivity is real, but human-side accessibility is undocumented.

#### 11.2.2 Domain, language, modality, and subgroup coverage

- **Rating:** 1
- **Evidence:** One task surface, one modality (visual grids encoded as integers), and no linguistic or cultural variation.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 1. Adjusted to 1. The rating records the breadth gap, not a design failure: the benchmark is deliberately narrow, and MESA's convention is that the rating describes evidence coverage while the rationale carries the intent.
- **Interpretation caution:** Narrowness here is intentional; do not read the low rating as a construction defect.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- **Rating:** 2
- **Evidence:** The Kaggle sandbox enforces strict compute and access controls (4x L4 GPUs, offline) ensuring high comparability for contest participants.
- **Missing evidence:** The public leaderboard mixes API-hosted models utilizing massive compute/scaffolding budgets with varied prompt structures.
- **Reviewer/editor rationale:** Comparability is excellent within the Kaggle cohort but poor across the broader public leaderboard due to mixed evaluation conditions.
- **Interpretation caution:** Never compare a raw API-hosted model score directly to a Kaggle-submitted model score without adjusting for compute, scaffolding, and retry budgets.

#### 11.3.2 Access, compute, tooling, and API or local comparability

- **Rating:** 2
- **Evidence:** Cost-per-task is reported alongside accuracy, which partially addresses compute comparability and discourages pure accuracy-at-any-price reporting.
- **Missing evidence:** No standardized definition of cost across submitters, leaving model cost, end-to-end pipeline cost, and amortized inference cost conflated on one axis.
- **Reviewer/editor rationale:** Both reviewers rated this 2. The efficiency axis is a genuine advance over accuracy-only leaderboards, but an undefined unit limits its comparability value.

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- **Rating:** 2
- **Evidence:** ARC Prize cycle labels (2025, 2026) provide a cohort axis, and the public evaluation set is static.
- **Missing evidence:** No policy stating whether scores from successive cycles are directly comparable, given that the task set is fixed while reference cohorts, scaffolds, and hosted model versions evolve.
- **Reviewer/editor rationale:** Both reviewers rated this 2. A static item set stabilizes one side of the comparison while the system side drifts unrecorded.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- **Rating:** 2
- **Evidence:** Demographic non-correlation among human testers is reported from the calibration campaign, and the language-free design removes linguistic and cultural bias by construction.
- **Missing evidence:** No analysis of model-class differential performance, such as whether particular scaffolds advantage certain model families.
- **Reviewer/editor rationale:** Reviewer 1 rated 1 and Reviewer 2 rated 2. Resolved to 2. Human-side bias analysis is genuinely present and reported, which distinguishes this from the near-total absence that a 1 denotes; the model-side gap is recorded at 11.4.2.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- **Rating:** 1
- **Evidence:** None located.
- **Missing evidence:** Any subgroup analysis across model families, scaffolds, cost tiers, or runtime regimes.
- **Reviewer/editor rationale:** Both reviewers rated this 1.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- **Rating:** 2
- **Evidence:** The necessary-but-not-sufficient AGI caveat appears in the paper and policy pages, and the authors state that scaling alone will not solve v2.
- **Missing evidence:** No formal enumeration of non-use cases such as procurement, deployment gating, safety certification, or broad-capability claims.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Guidance exists as narrative caveat rather than as an actionable restriction list.

#### 11.5.2 Release rules and sensitive-content handling

- **Rating:** 3
- **Evidence:** Apache-2.0 licensing on public materials, explicit Kaggle competition terms governing contest submissions, and no sensitive-content risk inherent to grid puzzles.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Release rules are explicit and the content domain is benign.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- **Rating:** 2
- **Reviewer/editor rationale:** The benchmark design (language-free grids) promotes inherent accessibility and cross-modal fairness. However, uneven compute budgets and cohort mixing on reporting surfaces degrade cross-system comparability.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope

- **Rating:** 3
- **Evidence:** The public leaderboard surfaces accuracy and cost-per-task with cohort labels, and the technical report and blog posts supply narrative analysis, human-baseline context, and version comparisons.
- **Missing evidence:** No per-task or per-category breakdowns are reported.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Reporting scope is appropriate to the single-construct design.

#### 12.1.2 Score granularity and level of detail

- **Rating:** 2
- **Evidence:** The leaderboard effectively maps accuracy against a cost-per-task efficiency axis.
- **Missing evidence:** The implied precision of the single aggregate score (reported to decimal percentages) over-represents the actual statistical power of a 120-item split.
- **Reviewer/editor rationale:** The cost/efficiency framing is an excellent innovation. However, the lack of subscores and uncertainty margins reduces the report's utility.
- **Interpretation caution:** Ignore decimal-level distinctions in leaderboard rankings.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- **Rating:** 2
- **Evidence:** Model versions and evaluation cohorts are generally noted.
- **Missing evidence:** Error bars/confidence intervals are entirely absent. Precise scaffolding/prompt conditions for API entries are not standardized.
- **Reviewer/editor rationale:** Basic traceability exists, but statistical uncertainty is omitted from the public dashboard.
- **Interpretation caution:** High-stakes rank claims derived from the leaderboard are statistically unsound without supplementary variance testing.

#### 12.2.2 Reproducibility and traceability of reported scores

- **Rating:** 2
- **Evidence:** Kaggle submissions are nominally reproducible inside the sandbox, which pins hardware and runtime, and the public task data is openly available.
- **Missing evidence:** Published frontier-model scores are not accompanied by runnable scripts, and no standardized reproduction recipe exists for the public leaderboard.
- **Reviewer/editor rationale:** Both reviewers rated this 2. Traceability holds inside the competition route and lapses on the route most widely cited.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- **Rating:** 2
- **Evidence:** The technical report articulates careful interpretive language, and the blog posts are generally more conservative than the benchmark's name implies.
- **Missing evidence:** The leaderboard surface and the benchmark name together can drive public interpretations that exceed the construct evidence, and the caveats are not carried onto the reporting surface itself.
- **Reviewer/editor rationale:** Both reviewers rated this 2. The gap is between where the caveats live and where the numbers are read.

#### 12.3.2 Raw outputs, per-item data, or trace availability

- **Rating:** 1
- **Evidence:** Per-item outputs are not generally published, and submitted solutions remain with entrants absent prize-related disclosure.
- **Missing evidence:** Any audit access to model traces or per-item results for the leaderboard cohort.
- **Reviewer/editor rationale:** Reviewer 1 rated 2 and Reviewer 2 rated 1. Adjusted to 1. Third-party audit of a reported score is not possible at any level of granularity below the headline number, which is the condition a 1 describes.
- **Interpretation caution:** Reported scores cannot be independently verified from published artefacts.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- **Rating:** 2
- **Evidence:** Reporting is neutral across model providers, and the cost axis counteracts a pure-accuracy bias toward expensive systems.
- **Missing evidence:** No explicit statement of coverage bias, such as which systems are and are not run by the maintainers versus self-reported.
- **Reviewer/editor rationale:** Both reviewers rated this 2.

#### 12.4.2 Acceptability and usability for intended audiences

- **Rating:** 3
- **Evidence:** The paper and leaderboard are well presented for a research audience, the cost-accuracy visualization is legible, and blog posts are accessible to lay readers.
- **Reviewer/editor rationale:** Both reviewers rated this 3. Presentation quality is a strength.

#### 12.4.3 Public communication and leaderboard governance

- **Rating:** 2
- **Evidence:** ARC Prize governance is centralized, named, and transparent at the cycle level, with published competition rules and a verified-testing policy.
- **Missing evidence:** Formal eligibility rules, audit routes, and update-cadence policies are not all centrally codified outside the Kaggle competition page, and the public leaderboard mixes runtime regimes without prominent labels.
- **Reviewer/editor rationale:** Reviewer 1 rated 3 and Reviewer 2 rated 2. Resolved to 2. Governance is materially stronger than a typical manually curated leaderboard, but the codification gap that drives the 11.3.1 comparability finding also constrains this rating.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- **Rating:** 2
- **Reviewer/editor rationale:** The reporting infrastructure is polished, visually accessible, and cleverly integrates cost data. The rating is limited to a 2 due to the omission of statistical uncertainty and the risk of public overinterpretation driven by the "AGI" branding.

---

## Final Evaluation

### Evaluative Report of the Benchmark

ARC-AGI-2 is a rigorously constructed, highly curated measurement instrument for assessing fluid intelligence via compositional generalization on novel grid tasks. Its primary strengths lie in its exceptional human-calibration campaign, its objective exact-match scoring, and a robust public/semi-private/private split architecture that successfully mitigates passive data contamination—a rarity in contemporary AI evaluation. The introduction of cost-per-task efficiency tracking on the leaderboard is a progressive feature that discourages brute-force search optimization.

However, its utility as an authoritative measurement tool is constrained by critical statistical and psychometric gaps. The benchmark provides no confidence intervals or run-to-run variance data, meaning the headline scores generated from small (120-task) evaluation splits are statistically fragile. Furthermore, while the technical report carefully caveats that solving ARC-AGI-2 is a "necessary but not sufficient" condition for AGI, the benchmark's branding implies a breadth of cognitive versatility that a single-modality, single-domain test cannot validate. There is currently no convergent or discriminant validity evidence connecting ARC-AGI-2 performance to real-world reasoning, language comprehension, or long-term memory.

The benchmark is highly adequate for tracking frontier model progress on abstract, localized reasoning puzzles under controlled environments (like the Kaggle sandbox). It is inadequate as a standalone metric for determining general intelligence or making high-stakes, cross-system comparisons on the public leaderboard where compute budgets and scaffolding conditions are mixed.

### Conclusions

ARC-AGI-2 is an excellent, contamination-resistant benchmark for tracking advancements in narrow, grid-based fluid reasoning, supported by an outstanding human baseline. However, its lack of published statistical uncertainty and narrow construct breadth mean it should not be used as standalone evidence for Artificial General Intelligence (AGI) or broad cognitive capabilities; responsible interpretation requires deep technical familiarity with its split design and the statistical limits of small-sample testing.

### Recommendations

1. **Benchmark Maintainers:** Publish binomial confidence intervals or standard errors for all leaderboard scores immediately.
2. **Benchmark Maintainers:** Separate the public leaderboard into explicit cohorts (e.g., "Offline Compute-Bounded" vs. "API Cost-Bounded") to prevent misleading cross-system comparisons.
3. **Benchmark Maintainers:** Release per-item category labels (for the four challenge types) in the public evaluation set to enable researchers to conduct internal-structure validity analyses.
4. **Benchmark Users:** Report ARC-AGI-2 results alongside explicit confidence intervals, and clearly state the scaffolding, prompt structure, and compute budget utilized.
5. **Policy Makers & Public:** Do not equate high scores on ARC-AGI-2 with the attainment of AGI, autonomy, or real-world problem-solving readiness.

### Summary of Ratings

| Section                                                      | Overall Rating (`n/a`, `0`-`4`) |
| :----------------------------------------------------------- | :-----------------------------: |
| Section 6. Rationale, documentation, and task/item quality   |                3                |
| Section 7. Benchmark materials and usability                 |                3                |
| Section 8. Reference points and documented comparison groups |                3                |
| Section 9. Reliability and precision                         |                1                |
| Section 10. Validity support                                 |                2                |
| Section 11. Fair use and comparability                       |                2                |
| Section 12. Reports, leaderboards, and public score claims   |                2                |

_Reviewer comments:_ The structural design, data curation, and baseline human testing are of high quality (`3`). The lower ratings (`1` and `2`) are concentrated entirely in the absence of statistical uncertainty reporting, cohort mixing on leaderboards, and the gap between the narrow construct and the broad AGI claims.

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected entity or reporting surface | Affected capability domain or score interpretation | Affected rating(s)          | Why it matters                                                                                                                        | Needed for a higher rating                                              |
| :------------------------------------------------------------ | :----------------------------------- | :------------------------------------------------- | :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------- |
| Confidence intervals / standard errors                        | Public Leaderboard, Technical Report | Meaningfulness of score differences, rank ordering | 6.2.4, 9.2.2, 9.5.1, 12.2.1 | On a 120-task split, 1% = 1 task. Small leaderboard differences are statistically indistinguishable from noise.                       | Publish binomial CIs or bootstrap standard errors alongside all scores. |
| Trial-count inconsistency                                     | README vs. Scoring Guide             | Exact task success                                 | 6.2.3                       | Attempt rules affect score comparability; the repository mentions 3 trials while the rules specify pass@2.                            | A consolidated, corrected scoring specification.                        |
| Cohort condition mapping                                      | Public Leaderboard                   | Cross-system comparability                         | 11.3.1, 12.2.1              | Comparing an offline, 12h-bounded Kaggle model to an unrestricted API model using custom scaffolding is misleading.                   | Clear visual separation of evaluation cohorts on the leaderboard.       |
| Convergent / discriminant validity data                       | Technical Report, Public Claims      | Construct validity, AGI claims                     | 10.4.1, 10.4.2              | Content validity alone cannot prove that the benchmark measures general fluid reasoning as opposed to ARC-specific puzzle adaptation. | Correlation studies against other established reasoning benchmarks.     |
| Per-task category labels                                      | Public Evaluation Set                | Internal structure validity                        | 10.2.1, 10.2.2, 10.2.3      | Without labels for the four "challenge types," users cannot audit whether models succeed evenly or fail specific reasoning patterns.  | Add category metadata to the public JSON files.                         |
| Canonical prompt template / grid serialization                | Public leaderboard, evaluator harnesses | Comparability of reported scores                | 7.1.2, 9.4.1, 10.3.2        | Grid encoding is evaluator-defined, so score differences can reflect serialization choices rather than reasoning ability.             | A published reference prompt and encoding specification.                |
| Run-to-run variance and seed reporting                        | Public leaderboard, Technical Report | Score stability                                    | 9.2.1, 9.4.3                | Single-run point estimates carry unquantified decoding variance, and hosted API model versions drift unrecorded.                      | Published multi-run distributions and pinned environment metadata.      |
| Test-time-training policy                                     | Competition rules, leaderboard       | Gameability and benchmark-specific tuning          | 10.5.2                      | Test-time training is widely used but ungoverned, leaving the line between legitimate adaptation and overfitting implicit.            | An explicit policy defining permitted test-time adaptation.             |
| Per-item outputs and audit traces                             | Public leaderboard                   | Independent verification of reported scores        | 12.2.2, 12.3.2              | No published artefact lets a third party verify a leaderboard score below the headline number.                                       | An audit route or archived per-item results for reported entries.       |
| Trivial-strategy baselines                                    | Technical Report                     | Floor interpretation                               | 8.1.1                       | Without copy-input or identity baselines, a low score cannot be shown to reflect failed reasoning rather than failed formatting.      | Published trivial-strategy baseline results per split.                  |

## Bibliography

1. F. Chollet, M. Knoop, G. Kamradt, B. Landers, and H. Pinkard, "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems," arXiv:2505.11831v2, 2025. <https://arxiv.org/abs/2505.11831>.
2. ARC Prize, ARC-AGI-2 official benchmark page. <https://arcprize.org/arc-agi/2>. Accessed 2026-05-18.
3. ARC Prize, ARC-AGI-2 repository (public task data, Apache-2.0, README and changelog). <https://github.com/arcprize/ARC-AGI-2>. Accessed 2026-05-18.
4. ARC Prize, ARC-AGI-1 and ARC-AGI-2 Guide. <https://arcprize.org/guide/1>. Accessed 2026-05-18.
5. ARC Prize, Verified Testing Policy. <https://arcprize.org/policy>. Accessed 2026-05-18.
6. ARC Prize, public leaderboard. <https://arcprize.org/leaderboard>. Accessed 2026-05-18.
7. ARC Prize, arc-agi-benchmarking harness repository. <https://github.com/arcprize/arc-agi-benchmarking>. Accessed 2026-05-18.
8. F. Chollet, "On the Measure of Intelligence," arXiv:1911.01547, 2019.
9. D. Hendrycks et al., "A Definition of AGI," arXiv:2510.18212, 2025. Local transcript: `literature/A_Definition_of_AGI.md`.
10. A. M. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," arXiv:2511.04703, 2025. Local transcript: `literature/Measuring_what_Matters.md`.
11. A. Reuel et al., "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices," arXiv:2411.12990, 2024. Local transcript: `literature/betterbench.md`.
12. EFPA. "EFPA Test Review Model - Version 2025." Local transcription used through `literature/EFPA_Test_Review_Model_2025_Markdown.md`.
