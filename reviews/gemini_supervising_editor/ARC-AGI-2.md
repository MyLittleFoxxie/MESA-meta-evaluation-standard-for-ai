# Editor's Prefatory Notes

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

# Final Reconciled MESA Evaluation: ARC-AGI-2

## Part A. Description of the Benchmark

### Section 1. Factual Description

#### 1.1 Review Administration

| Prompt                  | Description                                           |
| :---------------------- | :---------------------------------------------------- |
| Reviewer Name           | MESA Supervising Editor Agent (Reconciled Evaluation) |
| Date of Current Review  | 2026-05-18                                            |
| Date of Previous Review | n/a                                                   |

#### 1.2 Benchmark Identity & Provenance

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

#### 1.3 Materials, Sources, & Access Tracking

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

### Section 2. Classification

#### 2.1 Claimed Capability Domains

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

#### 2.2 Area of Use

- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [x] Public communication or marketing

#### 2.3 Intended AI Systems

- [x] Frontier general-purpose language models
- [x] Multimodal models
- [x] Chat or instruction-following models
- [x] Base language models
- [x] Agentic systems
- [x] Open-weight local models
- [x] API-hosted models

#### 2.4 Intended Users of Benchmark Outputs

- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [x] Product teams
- [x] Safety evaluators
- [x] Policy or governance actors
- [x] Public leaderboard users

#### 2.5 Task Families, Subdomains, and Scores

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

#### 2.6 Model Response Mode

- [x] Structured output, such as JSON or XML

#### 2.7 Prerequisites for Evaluated Systems

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

#### 2.8 Evaluation Conditions

| Condition                               | Description                                                                                      |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Prompting protocol                      | Not centrally fixed; repository provides raw JSON. Kaggle environment uses standardized runners. |
| Few-shot examples                       | 2-5 demonstration grid pairs provided intrinsically within each task JSON.                       |
| Sampling settings                       | Not universally specified; left to evaluator discretion / harness defaults.                      |
| Tool permissions                        | Kaggle: No internet access. API leaderboard: Unrestricted.                                       |
| Time limits                             | Kaggle: 12 hours for 240 tasks. API Leaderboard: Latency/cost reported.                          |
| Official rerun, retry, or repair policy | Evaluated on a pass@2 basis (two attempts per test input).                                       |
| Hardware or hosted service              | Kaggle uses 4x NVIDIA L4 GPUs.                                                                   |

#### 2.9 Task Interaction and Observable Evidence Types

- [x] Structured data
- [x] Response latency
- [x] Cost
- [x] Token usage (reported by some)
- [x] Leaderboard submission metadata
- [x] Raw output or audit trace under controlled access

#### 2.10 Input Stimulus Type

- [x] Tables or structured data (integer grids)
- [x] Images (can be rendered visually)

#### 2.11 Number of Items or Measurement Points

| Prompt                        | Response                                                         |
| :---------------------------- | :--------------------------------------------------------------- |
| Total public items or tasks   | 1,000 training tasks; 120 public evaluation tasks.               |
| Total private or hidden items | 120 semi-private evaluation tasks; 120 private evaluation tasks. |
| Score aggregation unit        | Unweighted average exact-match accuracy across tasks in a split. |

#### 2.12 Mode of Evaluation

- [x] Local batch evaluation
- [x] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [x] Competition or challenge submission
- Identity/condition controls: [x] Some control over submitted systems; [x] Controlled evaluation center or private harness (Kaggle).

#### 2.13 Technological Arrangements

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

#### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant         | Purpose                 | Stated score-comparability interpretation            | Status           |
| :---------------------- | :---------------------- | :--------------------------------------------------- | :--------------- |
| Public Training (1,000) | Development/prototyping | Uncalibrated; not comparable                         | Active           |
| Public Eval (120)       | Local public evaluation | Calibrated (IDD to private sets)                     | Active           |
| Semi-Private Eval (120) | Kaggle leaderboard      | IDD to public eval                                   | Active, withheld |
| Private Eval (120)      | Final prize scoring     | IDD to other eval sets                               | Active, withheld |
| ARC-AGI-1               | Parent benchmark        | Non-interchangeable; used to show v2 difficulty jump | Prior version    |

#### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [x] Hidden test set selected by maintainers
- [x] Versioned dataset slice

#### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [x] Reference answer
- [x] External verifier (Kaggle sandbox/harness)
- [x] Leaderboard submission metadata

#### 2.18 Broad-Claim Flags for Later Evaluation

| Prompt                                                     | Response                                                                                        |
| :--------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| Term used for broad interpretation from benchmark scores   | "AGI", "general fluid intelligence", "human-like AI capabilities".                              |
| Breadth implied by the score interpretation across domains | High breadth implied by naming/marketing, despite narrow single-domain task structure.          |
| Capability domains explicitly excluded or not tested       | Language, world knowledge, social reasoning, long-term memory, tool use, auditory processing.   |
| Stated AGI, autonomy, or agency caveats                    | Policy states ARC is "necessary but not sufficient" for AGI, not a complete litmus test.        |
| Documented caveats to carry forward into Part B            | Gap between AGI marketing language and task breadth; missing statistical uncertainty intervals. |

---

## Part B. Evaluation of the Benchmark

### Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

#### 6.1.1 Rationale and construct definition

- **Rating:** 3
- **Evidence:** The benchmark gives a clear, theoretically grounded definition of fluid intelligence via compositional generalization on novel grid tasks, explicitly excluding general world knowledge.
- **Missing evidence:** The mapping between the narrow grid-task construct and the broad "AGI" claim used in marketing is not formally theoretically bridged.
- **Editor rationale:** The rationale for the narrow operationalization is excellent and clear. The broader AGI framing exceeds what the construct definition supports.
- **Interpretation caution:** Interpret scores as "compositional grid-puzzle generalization", not as proof of domain-general AGI.

#### 6.1.3 Phenomenon-task-metric-claim chain

- **Rating:** 2
- **Evidence:** The chain from fluid reasoning to held-out grid tests and exact-match pass@2 scoring is logical and explicit in the technical report.
- **Missing evidence:** The chain from exact-match metrics to broad "progress toward AGI" claims remains contested. Additionally, formatting/serialization burdens for LLMs are not cleanly separated from reasoning failures.
- **Editor rationale:** The inner chain (task to metric) is strong. The outer chain (metric to AGI claim) is weak. Adequate for cautious use.
- **Interpretation caution:** Claims must be phrased around ARC-style abstraction, not generalized intelligence.

#### 6.1.5 Procedures for developing task or item content

- **Rating:** 3
- **Evidence:** Tasks were authored by foundation experts, subjected to redundancy detection, and calibrated through a massive 407-participant human testing campaign (requiring ≥2 human solves per task).
- **Missing evidence:** Full task-authoring rubrics and detailed item-level provenance logs are not fully public.
- **Editor rationale:** The empirical human-solvability gating is unusually rigorous for AI benchmarks, warranting a Good rating.
- **Interpretation caution:** Hidden-set item quality remains trust-mediated as it cannot be independently audited.

#### 6.1.9 Overall quality of rationale, development, and task or item quality

- **Rating:** 3
- **Evidence:** Strong official rationale, exceptional human calibration, curated task selection, and public documentation of goals.
- **Missing evidence:** Full broad-claim formalization and complete hidden-set auditability.
- **Editor rationale:** A well-motivated construct with a documented calibration procedure. Good for a narrow ARC-style reasoning benchmark.
- **Interpretation caution:** Use as a specific capability signal within a broader portfolio.

#### 6.2.3 Documentation of scoring and metrics

- **Rating:** 2
- **Evidence:** Guide and benchmarking repo document exact scoring (pass@2).
- **Missing evidence:** There is a noted discrepancy in the repository README mentioning "3 trials" while official rules state 2 trials. Complete malformed-output fallback policies are not fully centralized.
- **Editor rationale:** Scoring is understandable and objective, but procedural edge cases (like trial limits and JSON parsing errors) require a tighter, consolidated rulebook.
- **Interpretation caution:** Trial count implementations must be verified before making direct inter-system comparisons.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- **Rating:** 1
- **Evidence:** The benchmark reports that the three evaluation splits were calibrated to equivalent human difficulty (within 1%).
- **Missing evidence:** No model-side confidence intervals, standard errors, run-to-run variance, or prompt sensitivity analyses are published for headline scores.
- **Editor rationale:** On a 120-task split, 1 percentage point equals approximately 1 task. The lack of confidence intervals makes small leaderboard differences mathematically uninterpretable.
- **Interpretation caution:** Close leaderboard ranks should be treated as ties unless statistical significance is independently calculated.

#### 6.2.8 Adequacy of documentation available to users

- **Rating:** 2
- **Evidence:** Multiple sources cover purpose, tasks, scoring, and basic access policies.
- **Missing evidence:** Information is distributed across blogs, GitHub, and websites. Uncertainty reporting and detailed edge-case scoring rules are missing.
- **Editor rationale:** Documentation is sufficient for basic research use but lacks the statistical and procedural rigor required for high-stakes interpretations.
- **Interpretation caution:** Users must actively document their specific run conditions (e.g., cohort, prompt, verifier) as the docs do not enforce a single standard.

#### 6.3.7 Quality of procedural instructions

- **Rating:** 2
- **Evidence:** Usable instructions exist for the Kaggle sandbox and open benchmarking CLI.
- **Missing evidence:** No single canonical prompt template or frozen evaluation package is mandated for the API-hosted leaderboard cohort.
- **Editor rationale:** Adequate for cautious technical use, but the lack of a universal reference harness for API models permits evaluation variance.
- **Interpretation caution:** Do not assume independently run public scores perfectly match official leaderboard setups.

#### 6.4 Overall Adequacy of Rationale and Documentation

- **Rating:** 3
- **Editor rationale:** The benchmark provides a strong, source-grounded rationale, defensible human-calibrated development, and usable instructions. The rating is withheld from a 4 primarily due to missing statistical uncertainty documentation and fragmented scoring edge-case rules.

---

### Section 7. Quality and Usability of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability

- **Rating:** 3
- **Evidence:** Public tasks are fully available via GitHub under Apache 2.0. Hidden sets are controlled through Kaggle/ARC Prize infrastructure.
- **Missing evidence:** Semi-private/private sets cannot be independently inspected.
- **Editor rationale:** The public/private split design is well-executed and justified to prevent data contamination.
- **Interpretation caution:** Hidden-set validity relies entirely on the maintainer's claim that sets are Independent and Identically Distributed (IID).

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- **Rating:** 2
- **Evidence:** Open benchmarking repository exists with adapters; Kaggle provides an official, controlled scoring runtime.
- **Missing evidence:** No official, version-pinned, canonical open-source harness is enforced for the API-hosted leaderboard results.
- **Editor rationale:** Implementation infrastructure exists, but variance in community harnesses can affect serialization and parsing, altering scores.
- **Interpretation caution:** Ensure harness versions and JSON parsing scripts are identical when comparing local or API-based model runs.

#### 7.1.8 Overall quality of benchmark materials

- **Rating:** 3
- **Editor rationale:** Materials are clean, licensed, and highly usable. The exact-match integer grid format is highly accessible to multimodal and text-only models alike.

---

### Section 8. Baselines, Comparators, and Reference Interpretation

#### 8.1.2 Human or expert baselines

- **Rating:** 3
- **Evidence:** An extensive campaign (407 participants, 515 sessions, 13,405 attempts) with documented compensation and solvability gating.
- **Missing evidence:** Full demographic distributions, geographic coverage, and condition-matching (humans use a visual UI; models use JSON) are not fully detailed.
- **Editor rationale:** This is one of the most rigorous human calibration campaigns in current AI benchmarks. It establishes clear human feasibility.
- **Interpretation caution:** Human UI interaction differs fundamentally from LLM token serialization; the "human baseline" is a reference, not an exact equivalent process.

#### 8.1.3 Model comparator cohort

- **Rating:** 3
- **Evidence:** Technical reports and leaderboards track major frontier models (o3, Claude 3.5, Gemini, etc.).
- **Missing evidence:** Cohort conditions (prompts, exact scaffolding, budget) for the API-hosted models are not systematically tracked or standardized on the leaderboard.
- **Editor rationale:** Good general context, but cohort hygiene is mixed.
- **Interpretation caution:** API-hosted model scores utilizing custom scaffolding should not be directly compared to offline, compute-bounded Kaggle submissions.

#### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- **Rating:** 3
- **Editor rationale:** The human baseline is exceptionally strong. Reference interpretation is only limited by the lack of statistical uncertainty margins for the model comparator cohorts.

---

### Section 9. Reliability, Precision, and Score Stability

#### 9.1.1 Coverage of reliability and stability evidence

- **Rating:** 1
- **Evidence:** Deterministic exact scoring is used.
- **Missing evidence:** No full reliability study across prompts, reruns, seeds, model settings, or confidence intervals for the 120-task splits.
- **Editor rationale:** The lack of variance reporting is a critical flaw for a benchmark utilized to make fine-grained leaderboard distinctions.
- **Interpretation caution:** A single-run score on 120 tasks provides a fragile point estimate of a model's true capability.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- **Rating:** 1
- **Evidence:** No intervals reported.
- **Missing evidence:** Confidence intervals for headline scores.
- **Editor rationale:** Without standard errors, leaderboard ranks are statistically uninterpretable.
- **Interpretation caution:** Treat models within a few percentage points of each other as tied.

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- **Rating:** 1
- **Evidence:** No prompt-sensitivity analyses are published.
- **Missing evidence:** Given that models interpret serialized JSON grids, formatting choices heavily influence LLMs.
- **Editor rationale:** Insufficient evidence to claim score stability across different prompt strategies.
- **Interpretation caution:** High performance may reflect optimized JSON prompting rather than fundamentally superior fluid intelligence.

#### 9.5.1 Meaningfulness of score differences

- **Rating:** 1
- **Evidence:** Report cautions that scores below 5% are low signal.
- **Missing evidence:** No statistical significance tests for leaderboard deltas.
- **Editor rationale:** Meaningful score differences cannot be established without interval reporting.
- **Interpretation caution:** Rank ordering should not imply meaningful capability differences without independent statistical testing.

#### 9.6 Overall Reliability, Precision, and Score Stability

- **Rating:** 1
- **Editor rationale:** While the exact-match scorer itself is perfectly reliable, the _evidence base_ for interpreting stochastic LLM score differences on a small split is entirely absent.

---

### Section 10. Validity Evidence

#### 10.1.2 Construct breadth and capability-domain coverage

- **Rating:** 1
- **Evidence:** The benchmark explicitly measures fluid intelligence via a narrow visual-symbolic grid format.
- **Missing evidence:** The broad "AGI" claims invoked by the benchmark's name and marketing are not supported by evidence across other necessary CHC domains (e.g., Reading/Writing, General Knowledge, Auditory Processing, Long-Term Memory).
- **Editor rationale:** The task surface is fundamentally narrow. It cannot independently support broad cognitive versatility claims.
- **Interpretation caution:** ARC-AGI-2 is a single-domain signal. Do not treat it as a proxy for comprehensive general intelligence.

#### 10.2.1 Internal structure, subscores, or dimensionality

- **Rating:** 1
- **Evidence:** The paper describes four challenge types qualitatively.
- **Missing evidence:** No quantitative subscores, factor analyses, or per-task category labels are published.
- **Editor rationale:** Without data on sub-dimensions, the internal structure remains unvalidated.
- **Interpretation caution:** Aggregate accuracy may mask severe deficits in specific types of reasoning (e.g., multi-step vs. in-context symbol definition).

#### 10.4.2 Convergent and discriminant evidence

- **Rating:** 1
- **Evidence:** Comparisons are drawn to ARC-AGI-1.
- **Missing evidence:** No systematic correlation studies against other reasoning benchmarks (e.g., Mensa, GPQA) or knowledge-heavy benchmarks to prove discriminant validity.
- **Editor rationale:** Formal convergent/discriminant validity evidence is currently missing.
- **Interpretation caution:** It is unknown how ARC-AGI-2 performance correlates with real-world logical or mathematical reasoning tasks.

#### 10.5.1 Contamination and leakage controls

- **Rating:** 3
- **Evidence:** A strict public/semi-private/private split is maintained. The Kaggle contest utilizes an offline sandbox.
- **Missing evidence:** No canary strings or public leak-response protocols are documented.
- **Editor rationale:** The structural controls (offline sandbox and fully hidden private sets) are robust and effectively mitigate passive data contamination.
- **Interpretation caution:** Semi-private sets used for live leaderboards may still suffer from adaptive overfitting via repeated submissions.

#### 10.6.1 Proportionality of stated benchmark claims

- **Rating:** 2
- **Evidence:** The authors include the explicit caveat that ARC-AGI is a "necessary but not sufficient" condition for AGI.
- **Missing evidence:** The benchmark _name_ ("AGI") and associated prize marketing frequently drive public discourse that exceeds the formal caveats.
- **Editor rationale:** The technical authors are cautious, but the public branding is disproportionately broad.
- **Interpretation caution:** Reviewers and journalists must actively rein in "AGI" headlines when reporting ARC scores.

#### 10.7 Overall Validity Support

- **Rating:** 2
- **Editor rationale:** Content validity is solid for the narrow operationalization of grid-based fluid reasoning. Contamination controls are strong. However, internal structure, convergent/discriminant validity, and construct breadth are severely lacking, limiting the validity of broad interpretations.

---

### Section 11. Fair Use, Comparability, and Appropriate Use

#### 11.3.1 Cross-system comparability

- **Rating:** 2
- **Evidence:** The Kaggle sandbox enforces strict compute and access controls (4x L4 GPUs, offline) ensuring high comparability for contest participants.
- **Missing evidence:** The public leaderboard mixes API-hosted models utilizing massive compute/scaffolding budgets with varied prompt structures.
- **Editor rationale:** Comparability is excellent within the Kaggle cohort but poor across the broader public leaderboard due to mixed evaluation conditions.
- **Interpretation caution:** Never compare a raw API-hosted model score directly to a Kaggle-submitted model score without adjusting for compute, scaffolding, and retry budgets.

#### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- **Rating:** 2
- **Editor rationale:** The benchmark design (language-free grids) promotes inherent accessibility and cross-modal fairness. However, uneven compute budgets and cohort mixing on reporting surfaces degrade cross-system comparability.

---

### Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

#### 12.1.2 Score granularity and level of detail

- **Rating:** 2
- **Evidence:** The leaderboard effectively maps accuracy against a cost-per-task efficiency axis.
- **Missing evidence:** The implied precision of the single aggregate score (reported to decimal percentages) over-represents the actual statistical power of a 120-item split.
- **Editor rationale:** The cost/efficiency framing is an excellent innovation. However, the lack of subscores and uncertainty margins reduces the report's utility.
- **Interpretation caution:** Ignore decimal-level distinctions in leaderboard rankings.

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- **Rating:** 2
- **Evidence:** Model versions and evaluation cohorts are generally noted.
- **Missing evidence:** Error bars/confidence intervals are entirely absent. Precise scaffolding/prompt conditions for API entries are not standardized.
- **Editor rationale:** Basic traceability exists, but statistical uncertainty is omitted from the public dashboard.
- **Interpretation caution:** High-stakes rank claims derived from the leaderboard are statistically unsound without supplementary variance testing.

#### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- **Rating:** 2
- **Editor rationale:** The reporting infrastructure is polished, visually accessible, and cleverly integrates cost data. The rating is limited to a 2 due to the omission of statistical uncertainty and the risk of public overinterpretation driven by the "AGI" branding.

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
| Per-task category labels                                      | Public Evaluation Set                | Internal structure validity                        | 10.2.1                      | Without labels for the four "challenge types," users cannot audit whether models succeed evenly or fail specific reasoning patterns.  | Add category metadata to the public JSON files.                         |
