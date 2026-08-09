# MESA Review: ARC-AGI-2

Reviewer: Claude (Opus 4.7), as MESA benchmark reviewer agent
Date of review: 2026-05-18
Template: `MESA EFPA template official.md` (MESA EFPA Template v2)

---

## Short Stand-Alone Non-Evaluative Benchmark Description

ARC-AGI-2 is the second-generation public benchmark in the Abstraction and Reasoning Corpus family, created by François Chollet and colleagues at the ARC Prize Foundation. Each item is a grid puzzle composed of 2-5 demonstration input/output integer-grid pairs and 1-2 held-out test inputs, newly curated to target four compositional "challenge types": multi-rule reasoning, multi-step reasoning, contextual rule application, and in-context symbol definition. The benchmark releases a 1,000-task uncalibrated training set and a 120-task calibrated public evaluation set under Apache-2.0, with two further 120-task evaluation sets (semi-private and private) withheld by the maintainers for the Kaggle leaderboard and the ARC Prize contest. All three evaluation sets are described as statistically similar and were calibrated through a human-testing campaign with 407 participants across 515 sessions. Scoring is exact-match: a task counts as solved if all test outputs are reproduced correctly within two attempts, and the headline metric is unweighted accuracy across an evaluation split, reported alongside a cost-per-task axis. The benchmark is administered in two materially different regimes: an offline Kaggle sandbox (no internet, four NVIDIA L4 GPUs, 12-hour budget for 240 tasks) and an API-hosted public leaderboard used for frontier-model reporting.

---

## Source Inventory

| Material / Source Type         | URL, Location, or Identifier                                                                                                       | Access Date |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| Paper / Technical Report       | Chollet et al., "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems," arXiv:2505.11831v2 (PRIMARY)                       | 2026-05-18  |
| Website / Documentation Hub    | `https://arcprize.org/arc-agi/2`                                                                                                   | 2026-05-18  |
| Code Repository                | `https://github.com/arcprize/ARC-AGI-2` (Apache-2.0)                                                                               | 2026-05-18  |
| Dataset / Task / Prompt Set    | `data/training/` (1,000 tasks), `data/evaluation/` (120 public eval tasks); semi-private and private sets not in repository        | 2026-05-18  |
| Evaluation Harness / Runner    | Public repository contains task data; Kaggle competition provides the official scoring runtime (Kaggle sandbox, NVIDIA L4 GPUs)    | 2026-05-18  |
| Leaderboard / Results Portal   | `https://arcprize.org/leaderboard`; Kaggle competition leaderboard `kaggle.com/competitions/arc-prize-2026-arc-agi-2/leaderboard`  | 2026-05-18  |
| License                        | Apache-2.0 on `arcprize/ARC-AGI-2`                                                                                                 | 2026-05-18  |
| Changelog / Release Logs       | arXiv revision history (v1 2025-05; v2 2026-01); ARC Prize blog posts. No formal benchmark-data changelog inspected                | 2026-05-18  |
| Contextual Literature          | Chollet, "On the Measure of Intelligence" (2019); Hendrycks et al., "A Definition of AGI" (2025); BetterBench (Reuel et al., 2024) | 2026-05-18  |
| Feedback / Contact Channels    | GitHub issues on `arcprize/ARC-AGI-2`; Kaggle discussion forum                                                                     | 2026-05-18  |

Reviewer comments: Part A facts trace to the arXiv technical report, the official ARC Prize pages, and the public repository. Independent third-party leaderboard aggregators report ARC-AGI-2 scores for many models, but those values are not part of the official benchmark report and are used here only as contextual signals. The semi-private set is accessible only via Kaggle submission and the private set is not externally accessible; contamination and scoring judgments should be read with that access constraint in mind.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt                                    | Description                                     |
| :---------------------------------------- | :---------------------------------------------- |
| Reviewer Name                             | Claude (Opus 4.7), MESA benchmark-reviewer role |
| Date of Current Review                    | 2026-05-18                                      |
| Date of Previous Review _(if applicable)_ | n/a                                             |

### 1.2 Benchmark Identity & Provenance

| Prompt                                 | Description                                                                                                                                                                                                                                                                                                              |
| :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reviewed Entity Name                   | Abstraction and Reasoning Corpus for Artificial General Intelligence, version 2                                                                                                                                                                                                                                          |
| Short Name / Acronym                   | ARC-AGI-2                                                                                                                                                                                                                                                                                                                |
| Entity Type                            | Original benchmark with a maintained public repository, multi-tier public/semi-private/private evaluation splits, a hosted public leaderboard at `arcprize.org/leaderboard`, and an annual Kaggle competition surface (ARC Prize 2025 / ARC Prize 2026 - ARC-AGI-2)                                                       |
| Parent / Source Benchmark              | ARC-AGI-1 (Chollet, 2019, "On the Measure of Intelligence"); ARC-AGI-2 preserves the input-output grid-pair task format of its predecessor                                                                                                                                                                                |
| Exact Version / Release Split          | ARC-AGI-2 repository at `github.com/arcprize/ARC-AGI-2` (Apache-2.0); paper arXiv:2505.11831 v2 (revised 2026-01-15)                                                                                                                                                                                                     |
| Implementation / Scorer Version        | Exact cell-by-cell matching of integer grids; up to 2 attempts per test input; success requires correct outputs on all test inputs; for Kaggle the official scoring runs in a Kaggle secure sandbox on four NVIDIA L4 GPUs with no internet access and a 12-hour wall clock budget. Independent harness version unstated |
| Creators & Current Maintainers         | François Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, Henry Pinkard. Maintained by the ARC Prize Foundation                                                                                                                                                                                                      |
| Host Organization / Repository Owner   | ARC Prize Foundation (`arcprize` GitHub organization, `arcprize.org`)                                                                                                                                                                                                                                                    |
| Release Dates                          | Initial paper submission 2025-05-17; revision v2 2026-01-15; ARC Prize 2025 cycle ran on ARC-AGI-2; ARC Prize 2026 announced as continuation                                                                                                                                                                              |
| License & Access Terms                 | Public training set and public evaluation set released under Apache-2.0 in the GitHub repository; semi-private evaluation set used for Kaggle leaderboard (not public); private evaluation set held by maintainers for the final contest leaderboard                                                                      |
| Persistent Identifier / DOI / Citation | arXiv:2505.11831 (doi: 10.48550/arXiv.2505.11831); canonical site `arcprize.org/arc-agi/2`                                                                                                                                                                                                                               |

### 1.3 Materials, Sources, & Access Tracking

| Material / Source Type         | URL, Location, or Identifier                                                                                                       | Access Date |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| Paper / Technical Report       | Chollet et al., "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems," arXiv:2505.11831v2                                 | 2026-05-18  |
| Website / Documentation Hub    | `https://arcprize.org/arc-agi/2`                                                                                                   | 2026-05-18  |
| Code Repository                | `https://github.com/arcprize/ARC-AGI-2` (Apache-2.0)                                                                               | 2026-05-18  |
| Dataset / Task / Prompt Set    | `data/training/` (1,000 tasks), `data/evaluation/` (120 public eval tasks); semi-private and private sets not in repository        | 2026-05-18  |
| Evaluation Harness / Runner    | Public repository contains task data; Kaggle competition provides the official scoring runtime (Kaggle sandbox, NVIDIA L4 GPUs)    | 2026-05-18  |
| Leaderboard / Results Portal   | `https://arcprize.org/leaderboard`; Kaggle competition leaderboard `kaggle.com/competitions/arc-prize-2026-arc-agi-2/leaderboard`  | 2026-05-18  |
| Guides _(User/Scoring/Rubric)_ | Repository README; testing UI at `arcprize.org/play`                                                                               | 2026-05-18  |
| Changelog / Release Logs       | arXiv revision history (v1 2025-05; v2 2026-01); ARC Prize blog posts. No formal benchmark-data changelog inspected                | 2026-05-18  |
| Official Announcements         | ARC Prize blog, "ARC Prize 2025 Results and Analysis"                                                                              | 2026-05-18  |
| Contextual Literature          | Chollet, "On the Measure of Intelligence" (2019); Hendrycks et al., "A Definition of AGI" (2025); BetterBench (Reuel et al., 2024) | 2026-05-18  |
| Feedback / Contact Channels    | GitHub issues on `arcprize/ARC-AGI-2`; Kaggle discussion forum                                                                     | 2026-05-18  |

Reviewer comments: Independent third-party leaderboard aggregators (e.g., `llm-stats.com`, `benchlm.ai`, `agentmarketcap.ai`) report ARC-AGI-2 scores for many models, but those values are not part of the official benchmark report and are used here only as contextual signals. The official semi-private set is accessible only via Kaggle submission, and the private set is not externally accessible; ratings about contamination and scoring behavior should be interpreted with that access constraint in mind.

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

- [x] On-the-Spot Reasoning (R)
- [x] Visual Processing (V)
- [x] Working Memory (WM)
- [ ] General Knowledge (K) — explicitly minimized by design ("core knowledge priors only")
- [ ] Long-Term Memory Storage (MS)
- [ ] Long-Term Memory Retrieval (MR)
- [ ] Reading and Writing Ability (RW)
- [ ] Mathematical Ability (M) — adjacent but not the stated target
- [ ] Auditory Processing (A)
- [ ] Speed (S) — efficiency/cost is measured but framed as a secondary axis

Reviewer comments: The authors frame the target as "fluid intelligence" and "abstract reasoning" on novel tasks requiring "minimal prior knowledge," operationalized as compositional generalization over grid transformations. In CHC terms this maps most directly to On-the-Spot Reasoning (Gf), with Visual Processing acting as a stimulus channel rather than a deeply tested ability. The authors' broader interpretation invokes "progress toward AGI," which Part B treats as a claim warranting scrutiny.

### 2.2 Area of Use

- [x] Model comparison
- [x] Leaderboard ranking
- [x] Research diagnostics
- [x] Public communication or marketing (ARC Prize headline metric)
- [x] Capability profiling (in relation to ARC-AGI-1 and human baselines)
- [ ] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison (not stated as an intended use)
- [ ] Internal regression testing
- [ ] Policy or governance analysis

Reviewer comments: The benchmark is positioned as a frontier research stress-test and as the headline metric of the ARC Prize competition. The maintainers do not pitch it as a procurement, deployment, or safety instrument.

### 2.3 Intended AI Systems

- [x] Frontier general-purpose language models
- [x] Multimodal models (grids are presented as visual stimuli to humans; models typically receive textual JSON encodings)
- [x] Agentic systems and program-search systems (the prize competition is open to any architecture meeting the sandbox constraints)
- [x] Open-weight local models (Kaggle sandbox requires self-contained execution)
- [x] API-hosted models (used by the public leaderboard cohort, with cost reported)
- [ ] Audio or speech models
- [ ] Retrieval-augmented systems (Kaggle environment has no internet)

Reviewer comments: The Kaggle competition format effectively requires offline, self-contained systems; the `arcprize.org` public leaderboard additionally reports API-hosted frontier-model results in a different evaluation cohort.

### 2.4 Intended Users of Benchmark Outputs

- [x] AI researchers
- [x] Model developers
- [x] Benchmark creators or maintainers
- [x] Public leaderboard users
- [ ] Procurement or enterprise decision-makers (not the stated target)
- [ ] Policy or governance actors

Reviewer comments: Communication is aimed primarily at the research community and ARC Prize participants, with secondary public-facing communication.

### 2.5 Task Families, Subdomains, and Scores

| Component                                                                                          | Description                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capability, phenomenon, or quality the benchmark claims to measure                                 | Abstract reasoning / fluid intelligence on novel grid-transformation tasks                                                                                                                                                                                                                            |
| Definition of the capability or quality being measured                                             | Operationalized as the ability to infer transformation rules from 2-5 demonstration input/output grid pairs and apply them to held-out test inputs, with minimal reliance on memorized world knowledge; framed in the paper as "deeper levels of compositional generalization"                          |
| Subcomponents of the claimed capability, phenomenon, or quality                                    | Four challenge types named by the authors: (1) multi-rule reasoning; (2) multi-step reasoning; (3) contextual rule application; (4) in-context symbol definition                                                                                                                                       |
| Excluded scope or non-target abilities                                                             | World knowledge, language understanding, factual recall, multimodal real-world perception, long-horizon planning over external environments, tool use                                                                                                                                                  |
| Benchmark item, prompt, episode, environment, or interaction families or subdomains                | Grid puzzles, each item with 2-5 train pairs and 1-2 test pairs; grids are rectangular 1×1 to 30×30 with values in {0..9}                                                                                                                                                                              |
| Sources for benchmark items, prompts, episodes, environments, or interactions                      | Newly curated and designed by ARC Prize Foundation contributors; difficulty-calibrated using a human-testing program                                                                                                                                                                                   |
| Sampling method for benchmark items, prompts, episodes, environments, or interactions              | Curated authoring with human-difficulty calibration; final inclusion requires the task to be solved by at least two independent human testers within 2 attempts                                                                                                                                        |
| Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions | Removal of tasks susceptible to brute-force program search; calibration via the human-testing campaign; statistical similarity (IDD) across eval sets enforced                                                                                                                                          |
| Splits or partitions                                                                               | Training (1,000 public, uncalibrated), Public Eval (120, calibrated, human-verified), Semi-Private Eval (120, withheld, used for Kaggle leaderboard), Private Eval (120, fully held by maintainers, used for the contest)                                                                                |
| Primary score                                                                                      | Accuracy: fraction of tasks for which the model produces correct outputs for all test inputs within 2 attempts (pass@2)                                                                                                                                                                                 |
| Subscores                                                                                          | Per-split scores (Public Eval, Semi-Private Eval, Private Eval). The repository describes a "partial correctness" variant in the human-testing context (at least one test pair solved). Task-category breakdowns (multi-rule, multi-step, etc.) are described qualitatively but not as official subscores |
| Derived scores or scores combined from item, task-family, or subscore results                      | Cost-per-task is reported alongside accuracy on the public leaderboard as an efficiency axis                                                                                                                                                                                                            |
| Qualitative score ranges such as low/medium/high or novice/expert                                  | Implicit: 85% on the Private Eval set is the Grand Prize threshold; otherwise no formal band scheme                                                                                                                                                                                                     |
| Boundaries or caveats for interpretations made from benchmark scores                               | Authors caution that scaling alone is insufficient and that low scores indicate gaps in compositional generalization. No formal non-use statement was located                                                                                                                                            |

Reviewer comments: The "four challenge types" function as a design taxonomy, not as audit-grade subscores; the repository does not appear to ship category labels per task.

### 2.6 Model Response Mode

- [x] Structured output, such as JSON or XML (grids as integer matrices)
- [ ] Multiple choice / short text / long-form text / code / mathematical expression / tool call / browser action / image, audio, video output / environment interaction

Reviewer comments: Required output is a 2D integer grid, typically returned as JSON in the Kaggle competition.

### 2.7 Prerequisites for Evaluated Systems

| Requirement                                                     | Irrelevant or not necessary | Necessary information given | Information missing |
| :-------------------------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: |
| Language support                                                |              -              |              -              |          x          |
| Context length                                                  |              -              |              x              |          -          |
| Multimodal input support                                        |              x              |              -              |          -          |
| Structured output support                                       |              -              |              x              |          -          |
| Exact format, schema, or parser compatibility                   |              -              |              x              |          -          |
| Retry, repair, or correction-loop support for malformed outputs |              -              |              x              |          -          |
| Tool access                                                     |              x              |              -              |          -          |
| Browser or internet access                                      |              x              |              -              |          -          |
| Code execution                                                  |              -              |              x              |          -          |
| External API or tool credentials                                |              x              |              -              |          -          |
| Memory or persistent state                                      |              x              |              -              |          -          |
| Environment, simulator, or task-registry compatibility          |              -              |              x              |          -          |
| API compatibility                                               |              -              |              x              |          -          |
| Latency or time budget                                          |              -              |              x              |          -          |
| Cost or compute budget                                          |              -              |              x              |          -          |

Reviewer comments: For the Kaggle competition cohort, the 12-hour budget across 240 tasks on four NVIDIA L4 GPUs is binding. For the API-hosted leaderboard cohort, cost-per-task is reported but explicit per-task budgets vary by submission.

### 2.8 Evaluation Conditions

| Condition                                     | Description                                                                                                                                                              |
| :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompting protocol                            | Not centrally fixed by the maintainers; the repository ships raw JSON task data and leaves prompt construction to the evaluator. The Kaggle environment fixes the runner |
| System prompt                                 | Not specified by the benchmark                                                                                                                                            |
| Few-shot examples                             | Each task supplies 2-5 demonstration input/output pairs; additional cross-task few-shotting is at the evaluator's discretion                                              |
| Sampling settings                             | Not specified; up to 2 attempts per test input are scored                                                                                                                 |
| Tool permissions                              | No internet on Kaggle; otherwise unrestricted for the public API leaderboard cohort                                                                                       |
| Tool/API credential policy                    | Not applicable in the Kaggle sandbox; outside Kaggle, evaluators arrange their own access                                                                                 |
| Time limits                                   | 12 hours across 240 tasks on Kaggle (effectively ~3 minutes/task wall-clock budget on the supplied hardware)                                                              |
| Human intervention rules                      | None during scored evaluation                                                                                                                                             |
| Official rerun, retry, or repair policy       | Two attempts per test input within a single submission; resubmissions to the Kaggle leaderboard are allowed within competition limits                                     |
| Hardware or hosted service                    | Kaggle sandbox with 4× NVIDIA L4 GPUs                                                                                                                                     |
| Network requirements                          | No internet during scoring                                                                                                                                                |
| Sandbox or security constraints               | Kaggle's standard secure sandbox                                                                                                                                          |
| Model identity and version-label requirements | Leaderboard entries list model name and version where applicable                                                                                                          |
| Special administration conditions             | None additional located                                                                                                                                                   |

Reviewer comments: The benchmark has two materially different evaluation regimes (Kaggle compute-bounded sandbox vs. API-hosted cost-bounded leaderboard); the documentation surfaces both but does not formally separate them as distinct comparators.

### 2.9 Task Interaction and Observable Evidence Types

Production: [x] Structured data (grid output)
Observable evidence: [x] Cost (on the public leaderboard) [x] Token usage (reported by some leaderboard entries) [x] Submission metadata (Kaggle)

### 2.10 Input Stimulus Type

- [x] Tables or structured data (integer grids)
- [ ] Text / code / images (grids are typically encoded textually rather than rendered as images for models)

### 2.11 Number of Items or Measurement Points

| Prompt                                                         | Response                                                                                                                                  |
| :------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Total public items or tasks                                    | 1,000 (training) + 120 (public eval) = 1,120                                                                                              |
| Total private or hidden items                                  | 120 (semi-private) + 120 (private) = 240                                                                                                  |
| Development or example items                                   | The 1,000-task training set is uncalibrated and spans easy-to-very-hard                                                                   |
| Test items                                                     | 120 per evaluation split; Kaggle scoring uses 240 unseen tasks (semi-private + private, per the paper)                                    |
| Dynamic or generated tasks                                     | None; static curated set                                                                                                                  |
| Episodes, trials, or measurement points                        | 2 attempts per test input; 1-2 test inputs per task                                                                                       |
| Counts by split, form, or variant                              | See above                                                                                                                                  |
| Counts by language, culture, or locale                         | n/a (language-free)                                                                                                                       |
| Counts by claimed capability domain                            | Not published per-task                                                                                                                     |
| Counts by context-length bin                                   | Not published; grids range 1×1 to 30×30                                                                                                   |
| Counts by difficulty band                                      | Authors report difficulty calibration via human testing but do not publish a per-task difficulty band in the repository                   |
| Counts by public, private, hidden, or controlled-access status | 1,000 public training, 120 public eval, 120 semi-private (Kaggle), 120 private (held by maintainers)                                      |
| Item count uncertainty                                         | Stable as of the v2 paper and current repository state                                                                                    |

### 2.12 Mode of Evaluation

- [x] Local batch evaluation (public training/eval)
- [x] Hosted benchmark platform (Kaggle)
- [x] Leaderboard submission
- [x] Private controlled evaluation (private eval)
- [x] Competition or challenge submission (ARC Prize)
- [ ] Interactive agent / human-in-the-loop / continuous-rolling / registry / third-party-evaluator implementation

Identity and condition controls: [x] Controlled evaluation center or private harness (Kaggle sandbox); [x] Some control over submitted systems (Kaggle rules)

### 2.13 Technological Arrangements

| Technology                             |  A  |  R  |
| :------------------------------------- | :-: | :-: |
| API access                             |  x  |  -  |
| Local inference                        |  x  |  x  |
| GPU                                    |  x  |  x  |
| CPU-only execution                     |  x  |  -  |
| Docker or container                    |  x  |  -  |
| Python package or CLI                  |  x  |  -  |
| Browser                                |  -  |  -  |
| External tools                         |  -  |  -  |
| Internet access                        |  -  |  -  |
| Proprietary platform                   |  x  |  x  |
| Hosted scoring service                 |  x  |  x  |
| Benchmark registry or task environment |  -  |  -  |
| Simulator or user simulator            |  -  |  -  |
| Filesystem, terminal, or sandbox state |  x  |  -  |

Reviewer comments: For the official Kaggle pathway, GPU, local inference, and the Kaggle sandbox are required and internet is prohibited.

### 2.14 Time and Resource Requirements

| Activity                               | Time, compute, or cost estimate                                                                                                                |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Setup                                  | Cloning the repository and parsing JSON tasks is trivial; Kaggle account and competition acceptance required for the contest pathway          |
| Model inference or task completion     | Wall-clock not formally specified per task; Kaggle budget of 12 hours across 240 tasks                                                          |
| Token or context-window use            | Highly evaluator-dependent; typical text encodings of grids fit in a few thousand tokens                                                       |
| Scoring                                | Exact-match grid comparison; effectively instantaneous                                                                                          |
| Human adjudication                     | n/a                                                                                                                                            |
| Analysis or reporting                  | Not specified                                                                                                                                  |
| Full benchmark run                     | Kaggle: 12 hours / 240 tasks                                                                                                                   |
| API or compute cost                    | Reported per-submission on the public leaderboard, e.g., (third-party reports) Claude Opus 4.5 ~$2.20/task at ~37.6%; Gemini 3 Pro orchestrations ~$30/task at 54% |
| External tool, service, or search cost | n/a                                                                                                                                            |

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant   | Purpose                                          | Stated score-comparability interpretation                                                       | Status                                     |
| :---------------- | :----------------------------------------------- | :---------------------------------------------------------------------------------------------- | :----------------------------------------- |
| Training (1,000)  | Algorithm development and program-induction prototyping; uncalibrated difficulty | Not used for headline scoring; not comparable to evaluation scores                              | Active                                     |
| Public Eval (120) | Calibrated public evaluation, also surfaces in the API-hosted leaderboard cohort | Comparable across submitters on the same set; calibrated against semi-private and private sets  | Active                                     |
| Semi-Private (120) | Kaggle leaderboard during competition           | Statistically similar (IDD) to public eval per the authors; used for live leaderboard standings | Active, withheld                           |
| Private (120)     | Final ARC Prize contest scoring                   | Statistically similar (IDD) to other eval sets; not externally accessible                       | Active, held by maintainers                |
| ARC-AGI-1         | Parent benchmark                                 | Authors explicitly contrast ARC-AGI-2 scores with ARC-AGI-1 scores (e.g., o3 medium 53% on v1 vs ~3% on v2); not interchangeable | Retained as prior version                  |

### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [x] Hidden test set selected by maintainers

### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [x] Reference answer
- [x] Leaderboard submission metadata

### 2.18 Broad-Claim Flags for Later Evaluation

| Prompt                                                         | Response                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Term used for broad interpretation from benchmark scores       | "AGI" (in the benchmark name), "fluid intelligence," "abstract reasoning," "progress toward artificial general intelligence"                                                                                                                                                       |
| Breadth implied by the score interpretation across domains     | Wide: the prize framing presents ARC-AGI-2 as a stress-test for AGI-relevant reasoning, although the task surface is narrow (grid puzzles)                                                                                                                                         |
| Depth or proficiency level implied by the score interpretation | Implied human-level: 85% on Private Eval is the Grand Prize threshold; the human-testing campaign reports majority human solvability                                                                                                                                                |
| Capability domains from 2.1 explicitly covered                 | On-the-Spot Reasoning (R), with Visual Processing (V) and Working Memory (WM) as stimulus/processing channels                                                                                                                                                                       |
| Capability domains from 2.1 explicitly excluded or not tested  | General Knowledge, Reading/Writing, Mathematical Ability, Long-Term Memory Storage/Retrieval, Auditory Processing, agency, tool use, multilingual, safety, robustness, calibration                                                                                                  |
| Coverage across modalities, tools, memory, planning, or speed  | Single modality (symbolic grid), no tools, short-horizon reasoning, no persistent memory; cost/efficiency is reported as a secondary axis but not as a CHC speed measure                                                                                                            |
| Whether aggregate scores preserve capability-domain caveats    | Headline score is a single accuracy number; capability-domain framing lives in the paper and prize materials rather than in score reports                                                                                                                                            |
| Stated AGI, autonomy, or agency caveats                        | The authors explicitly state that ARC-AGI-2 is a *necessary but not sufficient* condition for AGI and that solving it does not imply AGI; they also state that "log-linear scaling is insufficient" to beat it                                                                       |
| Documented broad-claim limits or non-use statements            | The maintainers' position that scoring well does not equal AGI is stated in paper text and blog posts; no formal "non-use" list was located                                                                                                                                          |
| Documented caveats to carry forward into Part B                | (a) Breadth gap between the AGI framing and the single-modality grid-puzzle task surface; (b) the Kaggle vs API-hosted cohort distinction; (c) cost-per-task as an interpretation axis that is reported but not formally normalized                                                  |

Reviewer comments: ARC-AGI-2's name and prize framing invoke AGI, which mandates the broad-claim review path in Part B Section 10.6.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

- [x] Automated exact-match scoring
- [x] Rule-based scoring
- [x] Leaderboard service scoring
- [x] Multi-run or pass@k sampling policy (pass@2 by design)

### 3.2 Scores and Metrics

| Score or scoring rule/quantity | Definition                                                                                                | How item, task-family, or subscore results are combined                  | Capability-domain linkage stated by authors                  | Interpretation stated by authors                                                                |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- | :----------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| Primary score                  | Fraction of tasks fully solved within 2 attempts (all test inputs of a task must be exactly matched)      | Unweighted average across tasks in the evaluation split                  | Abstract reasoning / fluid intelligence on novel grid tasks  | Higher = stronger compositional generalization on novel tasks; 85% on Private Eval triggers the Grand Prize |
| Subscore                       | Per-split accuracy (Public Eval / Semi-Private Eval / Private Eval)                                       | Same as primary score within the respective split                        | Same as primary score                                        | Comparability across splits is supported by the authors' IDD-calibration claim                  |
| Derived score                  | Cost-per-task (USD) reported alongside accuracy on the public leaderboard                                 | Submitter-reported; combined visually with accuracy on the leaderboard   | Framed as an efficiency axis ("intelligence is efficient")   | Authors prefer Pareto-frontier interpretation: accuracy at a given cost                          |
| Qualitative band               | Grand Prize threshold: 85% on Private Eval                                                                | Tier reached if score crosses threshold                                  | Same as primary                                              | Threshold is a competition trigger, not a calibrated capability band                              |

Treatment of responses that fail format, schema, refusal, completion, or parsing requirements: malformed outputs fail the corresponding test input; explicit error-handling policy is delegated to evaluators or to the Kaggle harness, not specified in the public repository.

Treatment of eligibility failures, API/tool blocks, timeouts, tool-call failures, environment crashes, malformed final states, duplicate submissions, and other run failures: not separately defined for the public release; the Kaggle competition enforces a 12-hour wall-clock budget, after which submissions fail.

Retry, repair, parser fallback, platform rerun, or manual adjudication policy for response-format or run-completion problems: two attempts per test input are permitted by design; no documented adjudication beyond that.

### 3.3 Scale or Metric Types

- [x] Accuracy
- [x] Pass rate or pass@k (pass@2 by construction)
- [x] Cost-adjusted score (cost-per-task reported alongside accuracy)
- [x] Threshold or decision index (85% Grand Prize trigger)

### 3.4 Score Transformation

- [x] No transformation (raw accuracy)
- [x] Formula for combining item, task-family, or subscore results documented (unweighted average across tasks)

### 3.5 Documented Reference Groups, Baselines, and Comparators

- [x] Performance from human participants under documented conditions
- [x] Contest human population under source-instrument conditions (the 407-participant human-testing campaign)
- [x] Performance from a reference model used to interpret scores (frontier reasoning models, e.g., o3 variants reported alongside)
- [x] Previous model cohort (results reported against multiple frontier models)
- [x] Prior benchmark or version (ARC-AGI-1 comparisons reported per model)
- [x] Score boundary or lower/upper reference point (85% Grand Prize threshold)

| Reference point or documented comparison group                    | Construction method                                                                                                                                                                                                                                                                              | Intended score interpretation                                                                                            |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| Random guessing or trivial-selection reference point              | Implicit ~0% given the open-ended grid output space                                                                                                                                                                                                                                              | Floor = essentially zero                                                                                                 |
| Human-participant performance under documented conditions         | 407 unique participants across 515 sessions; 90-minute sessions; $115-150 base + $5 per correct task; conducted Nov 2024 - May 2025; 75% per-attempt success, 62% over-all session success; median 2.2 minutes per solved task; all final ARC-AGI-2 tasks solved by ≥2 testers within 2 attempts | Establishes that tasks are tractable for non-expert humans, supporting the "easy for humans, hard for AI" framing        |
| Qualified domain-expert performance                               | Not separately reported as a distinct "expert" cohort                                                                                                                                                                                                                                            | n/a                                                                                                                      |
| Contest human population or source-instrument reference           | Same human-testing campaign as above                                                                                                                                                                                                                                                              | Calibration cohort for difficulty                                                                                        |
| Documented group of models used for comparison                    | Frontier reasoning models (e.g., o3 medium/high, o3-mini high) reported in the paper; broader cohort on the public leaderboard                                                                                                                                                                   | Establishes the v1-to-v2 difficulty jump and the current frontier ceiling                                                |
| Public/private split, suite-component, or tool/no-tool comparator | Public Eval vs Semi-Private vs Private (claimed IDD); Kaggle (no-internet, hardware-bound) vs API-hosted (cost-bound) cohorts                                                                                                                                                                    | Comparability within a cohort; cross-cohort comparisons require caution                                                  |
| Prior benchmark or version                                        | Per-model ARC-AGI-1 vs ARC-AGI-2 scores reported in the paper                                                                                                                                                                                                                                    | Frames v2 as substantially harder for current models                                                                     |
| Score boundary or lower/upper reference point                     | 85% on Private Eval = Grand Prize threshold                                                                                                                                                                                                                                                      | Operational competition trigger; not a psychometrically calibrated proficiency band                                       |

### 3.6 Score Uncertainty and Stability

- [x] Multiple runs or seeds (the pass@2 design admits two attempts but a formal multi-seed analysis is not in the v2 paper's main text as inspected)
- [ ] Reported ranges expressing uncertainty around a score or comparison
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Per-split or per-subscore confidence intervals
- [ ] Public/private split intervals
- [ ] Sensitivity analyses or prompt-sensitivity reporting
- [ ] IRT, adaptive testing, or item-parameter precision estimates
- [x] Statistics on consistency across human raters (human-testing campaign reports redundancy: ≥2 testers must solve each retained task)

Reviewer comments: I did not locate official confidence intervals or repeat-run variance reporting on the headline accuracy numbers. With 120 tasks per split, a single 1% leaderboard delta corresponds to a single task; uncertainty quantification is therefore an evidence gap rather than a refuted claim.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

| Prompt                                                                                  | Response                                                                                                                                                          |
| :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why the primary rule or quantity used to convert model behavior into a score was chosen | Exact-match accuracy is a deterministic, language-free, knowledge-light scorer that minimizes scorer ambiguity for grid outputs                                   |
| Whether lower or upper limits of the score rule are documented                          | Range [0,1]; 100% saturates the split                                                                                                                              |
| Whether documentation identifies possible non-target rewarded behavior                  | Authors call out brute-force program search as the non-target tactic to suppress (and report active removal during curation)                                       |
| Whether parser, judge, or scorer validation is documented                               | Scorer is exact integer-matrix comparison; no separate parser-validation report needed for the canonical scorer                                                    |
| Whether response-format burden is separated from the target capability                  | Partially: 2 attempts/test input allow recovery from minor format mistakes; no formal study of how often format errors masquerade as reasoning failures            |
| Whether score changes from small item or prompt changes affect the score interpretation | Not formally reported in the v2 paper as inspected                                                                                                                  |
| Whether score uncertainty affects interpretation                                        | Not formally reported                                                                                                                                              |
| Whether score differences are interpreted statistically                                 | Authors highlight large differences (e.g., v1 vs v2) but do not provide statistical-significance tests for small leaderboard deltas                                  |
| Whether score or subscore interpretations are linked to capability domains from 2.1     | Linked qualitatively to "fluid intelligence / compositional reasoning"                                                                                              |
| Whether aggregate score interpretations preserve capability-domain caveats              | The aggregate is a single accuracy number; caveats live in the paper and blog rather than on the leaderboard                                                        |
| Whether benchmark reports state what users should not infer                             | Maintainers state that solving ARC-AGI-2 is necessary-but-not-sufficient for AGI; no enumerated non-use list found                                                  |

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [x] Public leaderboard available (`arcprize.org/leaderboard`; Kaggle leaderboard)
- [x] Public aggregate scores available
- [x] Submission metadata available
- [x] Evaluation date or cohort labels available (semi-private vs private, ARC Prize cycle)
- [x] Public/private split scores available
- [x] Leaderboard snapshot or export available (visible on website)
- [ ] Public capability-domain scores or profiles available
- [ ] Public per-item scores available
- [ ] Public model responses, traces, logs, judge rationales, or per-item data available
- [ ] Confidence intervals or error bars available
- [ ] Raw submissions available under controlled access (Kaggle solutions remain with submitters absent prize-related disclosure)

### 4.2 Output Name or Description

| Output                                                | Description                                              | Public/private | Maintainer / host                  |
| :---------------------------------------------------- | :------------------------------------------------------- | :------------- | :--------------------------------- |
| ARC Prize public leaderboard                          | Accuracy and cost-per-task by model, with cohort labels  | Public         | ARC Prize Foundation               |
| Kaggle ARC Prize competition leaderboard              | Semi-private set accuracy during the competition         | Public         | Kaggle / ARC Prize Foundation      |
| ARC-AGI-2 paper (Tables in arXiv:2505.11831v2)        | Per-model accuracy, human baseline, design analysis      | Public         | Authors                            |
| ARC Prize blog posts (e.g., 2025 results analysis)    | Narrative analysis, winners, prize awards, methods notes | Public         | ARC Prize Foundation               |

### 4.3 Output Design or Presentation

- [x] Static text report (paper)
- [x] Tables
- [x] Graphs or visualizations (cost-accuracy scatter on the website)
- [x] Leaderboard
- [x] Interactive dashboard (the public leaderboard supports basic filtering)

### 4.4 Output Structure

- [x] Aggregate-score based
- [x] Cost or efficiency adjusted
- [x] Rank based
- [x] Split or cohort based
- [x] Version-window based (per ARC Prize cycle)

### 4.5 Sensitivity to Context

- [x] One output format for all contexts (single primary leaderboard format)

### 4.6 Development of Outputs

- [x] Based on benchmark authors' design
- [x] Based on human annotation (for human-baseline data)
- [x] Automatically generated by benchmark platform (Kaggle leaderboard for the competition)

### 4.7 Modifiability

- [x] Not modifiable for end users

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

- [x] Clear linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels (the labels involved are coarse: one capability framing, one accuracy score)

### 4.9 Output Content

- [x] Aggregate rankings
- [x] Cost, latency, or efficiency data
- [x] Examples of successes or failures (in paper figures)
- [x] Warnings or caveats (in paper; less visible on leaderboard)

### 4.10 Intended Recipients

- [x] AI researchers, model developers, benchmark maintainers, public audience

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

- [x] Technical report (arXiv paper)
- [x] Repository README
- [x] Dataset card (informal; README-level description)
- [x] Model submission instructions (Kaggle competition rules)
- [x] Scoring documentation (in repository / paper)
- [x] Changelog or release notes (arXiv revision history; ARC Prize blog)

### 5.2 Distribution and Access Model

- [x] Public materials with restricted answer keys or hidden tests
- [x] Controlled-access dataset or task host (semi-private set via Kaggle)
- [x] Private or held-out evaluation service (private set)
- [x] Leaderboard-only submission route (semi-private and private sets)
- [x] Competition or challenge distribution (Kaggle)

### 5.3 Methods of Publication

- [x] Academic paper, benchmark website, Git repository, leaderboard platform, contest organizer source

### 5.4 User Requirements or Qualifications

| Requirement type                             | Requirement                                                                                                                                       |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| Technical skill                              | Comfort with JSON, model APIs or local inference, Python tooling; for Kaggle, ability to package an offline submission                            |
| Model access                                 | Any system that can run within the Kaggle sandbox (offline) or be queried via the evaluator's own infrastructure for the API-hosted cohort       |
| Dataset access                               | Training and public eval: public. Semi-private: via Kaggle. Private: held by maintainers                                                          |
| Compute or budget                            | Kaggle: 4× L4 GPUs / 12h. API cohort: pay-as-you-go                                                                                              |
| Tool/API credentials                         | n/a for Kaggle                                                                                                                                    |
| Hosted submission or leaderboard account     | Kaggle account, ARC Prize registration, competition agreement                                                                                    |
| Human expertise                              | Not required (no human-in-the-loop scoring)                                                                                                       |
| Account, license, or competition eligibility | Apache-2.0 license on the public materials; competition rules apply to ARC Prize submissions                                                     |
| Ethical, safety, or data-use obligations     | Standard Kaggle terms; competitors must not use the private set                                                                                  |

### 5.5 Dataset and Item Access

| Component                                      | Public | Restricted | Hidden | Not available |
| :--------------------------------------------- | :----: | :--------: | :----: | :-----------: |
| Training or development items                  |   x    |     -      |   -    |       -       |
| Public evaluation items                        |   x    |     -      |   -    |       -       |
| Private or held-out evaluation items           |   -    |     x      |   x    |       -       |
| Secret, encrypted, or reserve evaluation items |   -    |     -      |   x    |       -       |
| Private leaderboard set                        |   -    |     x      |   x    |       -       |
| Retired or archived evaluation items           |   -    |     -      |   -    |       x       |
| Answer keys or reference solutions             |   x (public eval)   |     x (Kaggle scoring)     |   x (private) |   -   |
| Metadata or annotations                        |   -    |     -      |   -    |       x       |
| Human annotations or verification labels       |   -    |     -      |   -    |       x       |
| Raw model outputs or logs                      |   -    |     -      |   -    |       x       |
| Model submissions and traces                   |   -    |     x (Kaggle internal)     |   -    |       -       |
| Hosted scoring service                         |   x (Kaggle) |  -  |   -    |       -       |
| Simulator or environment state                 |   -    |     -      |   -    |     n/a       |
| Task registry entry                            |   -    |     -      |   -    |     n/a       |
| Tool/API credentials or configuration          |   -    |     -      |   -    |     n/a       |

### 5.6 Provenance and Contamination Documentation

| Topic                                                                        | Documented | Partially documented | Not documented |
| :--------------------------------------------------------------------------- | :--------: | :------------------: | :------------: |
| Data origin or task creation                                                 |     x      |          -           |       -        |
| Source-material release date                                                 |     -      |          x           |       -        |
| Contest or problem-source timing                                             |     -      |          x           |       -        |
| Persistent dataset or benchmark-material identifier                          |     x      |          -           |       -        |
| Author or contributor qualifications                                         |     -      |          x           |       -        |
| Deduplication or overlap checks                                              |     -      |          x           |       -        |
| Rationale for public items and hidden or restricted evaluation items         |     x      |          -           |       -        |
| Screening for prior model exposure to benchmark items, answers, or sources   |     -      |          x           |       -        |
| Canary strings or training-data warnings                                     |     -      |          -           |       x        |
| Diagnostic task for performance driven by prior exposure to items or answers |     -      |          -           |       x        |
| Pre-exposure or source-material searchability checks                         |     -      |          x           |       -        |
| Public-source searchability                                                  |     -      |          x           |       -        |
| Post-release contamination risk                                              |     -      |          x           |       -        |
| Training-use prohibition                                                     |     -      |          x (Kaggle rules and license context) |       -        |
| Private-set owner                                                            |     x      |          -           |       -        |
| Leak response policy                                                         |     -      |          -           |       x        |
| Rerun or replacement trigger                                                 |     -      |          -           |       x        |
| Hash commitments, signatures, or tamper-evident audit logs                   |     -      |          -           |       x        |
| Encrypted, secret, or controlled-release item reserve                        |     x (private set acts as a reserve) |          -           |       -        |
| Rules for updating, rotating, replacing, or adding benchmark items over time |     -      |          x           |       -        |
| Reporting of known unintended disclosures or deprecated/archived items       |     -      |          -           |       x        |

Reviewer comments: The public/semi-private/private split design is itself the principal contamination control. I did not locate canaries, hash commitments, or a formal leak-response policy.

### 5.7 Reproducibility Materials

- [x] Complete task data (public splits)
- [x] Code or platform that administers tasks and scoring (Kaggle sandbox; community reference implementations)
- [x] Scoring code (exact-match is trivial; some scripts in repository)
- [ ] Complete prompt templates (no canonical prompt; evaluator-defined)
- [ ] Environment file or dependency list, container image, simulator version, judge model and prompt version, random seeds or deterministic settings
- [ ] Reproduction script for published results / push-button replication / fixtures / CI

### 5.8 Maintenance and Versioning

| Topic                                                                                | Response                                                                                                                                                            |
| :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Maintainer identity                                                                  | ARC Prize Foundation (Chollet, Knoop, Kamradt, Landers, Pinkard)                                                                                                    |
| Private or held-out set owner                                                        | ARC Prize Foundation                                                                                                                                                |
| Leaderboard operator                                                                 | ARC Prize Foundation (public leaderboard); Kaggle (competition leaderboard)                                                                                         |
| Submission eligibility rules                                                         | Kaggle competition rules apply for the contest; public leaderboard reporting policies are described informally                                                      |
| Rerun policy                                                                         | Kaggle allows multiple submissions per cycle within competition rules                                                                                                |
| Stale-score policy                                                                   | Not formally documented                                                                                                                                              |
| Model-version update policy                                                          | Not formally documented; leaderboard entries list model labels                                                                                                       |
| Scorer, judge, parser, or harness versioning                                         | Scoring rule is invariant; harness versions not exposed externally                                                                                                   |
| Cohort or evaluation-window labels                                                   | ARC Prize cycle labels (2025, 2026)                                                                                                                                  |
| Public/private score aggregation policy                                              | Reported separately; no formal aggregation                                                                                                                          |
| Retirement and archival policy                                                       | Public eval items are not expected to be retired; private set is retained                                                                                            |
| Documented release names, tags, changes, and score-comparability implications        | arXiv revision history serves as a partial changelog                                                                                                                |
| Changelog or update record                                                           | Partial (arXiv + blog)                                                                                                                                              |
| Issue or feedback process                                                            | GitHub issues; Kaggle discussion                                                                                                                                    |
| Item correction process                                                              | Not formally documented                                                                                                                                              |
| Deprecated item handling                                                             | Not documented                                                                                                                                                       |
| Rules for updating, rotating, replacing, or adding hidden evaluation items over time | Not documented externally                                                                                                                                            |
| Last code-usability or harness health check                                          | Not externally signposted                                                                                                                                            |
| Build, CI, or smoke-test status                                                      | Not externally visible                                                                                                                                              |
| Score-ceiling threshold or criteria for deprecating, archiving, or ending use        | 85% Grand Prize threshold is the de facto saturation target; the maintainers have signaled that ARC-AGI-3 (interactive) is in preparation                          |
| Policy for deprecating, archiving, or ending use                                     | Not formally codified; the ARC-AGI-3 announcement implies continued operation of ARC-AGI-2 alongside the new benchmark                                              |
| Retired-item publication or audit policy                                             | Not documented                                                                                                                                                       |
| Score comparability across versions                                                  | Authors explicitly treat v1 and v2 scores as non-interchangeable                                                                                                    |
| Policy for comparing scores across dates, cohorts, refreshes, or rolling windows     | Not formally codified for ARC-AGI-2                                                                                                                                  |
| Long-term archival plan                                                              | Repository + arXiv provide reasonable archival; no DOI for the dataset itself was located                                                                            |

---

## Appendix A. General Description of the Benchmark

ARC-AGI-2 is the second-generation public benchmark in the Abstraction and Reasoning Corpus family, created by François Chollet and colleagues at the ARC Prize Foundation. It preserves the original ARC task format—each item is a grid puzzle composed of 2-5 demonstration input/output integer-grid pairs and 1-2 held-out test inputs—while being newly curated to target compositional reasoning patterns that the authors group into four "challenge types": multi-rule reasoning, multi-step reasoning, contextual rule application, and in-context symbol definition. The benchmark releases a 1,000-task uncalibrated training set and a 120-task calibrated public evaluation set under Apache-2.0; two additional 120-task evaluation sets (semi-private and private) are withheld by the maintainers for the Kaggle leaderboard and the ARC Prize contest, respectively. All three evaluation sets are described as statistically similar (independent and identically distributed) to each other and were calibrated via a controlled human-testing campaign with 407 participants across 515 sessions. Scoring is exact-match: a model "solves" a task if all of its test outputs are correctly reproduced within two attempts, and the headline metric is the unweighted accuracy across an evaluation split. A cost-per-task axis accompanies accuracy on the public leaderboard. The benchmark is administered in two materially different regimes: an offline Kaggle sandbox (no internet, four NVIDIA L4 GPUs, 12-hour budget for 240 tasks) used for the prize competition, and an API-hosted public leaderboard used for frontier-model reporting. The benchmark is framed as a stress-test of "fluid intelligence" and as progress-toward-AGI, with the explicit caveat that solving it is necessary but not sufficient for AGI.

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
- Rating: 3
- Evidence: The paper and prize site articulate a clear construct (compositional generalization on novel grid tasks operationalizing fluid intelligence) and define what the benchmark deliberately excludes (world knowledge). The four "challenge types" make the design intent concrete.
- Missing evidence: The construct is invoked under the broad label "AGI" but mapped to a single narrow task surface; no formal mapping of the construct to a multi-domain CHC-style framework appears in the official materials.
- Reviewer rationale: Good clarity for the narrow operationalization; the broader AGI framing exceeds what the construct definition itself supports, which prevents a 4.
- Interpretation caution: Treat "fluid intelligence" here as "compositional grid-puzzle generalization," not as a domain-general construct.

#### 6.1.2 Summary of prior research and benchmark context
- Rating: 3
- Evidence: The paper situates ARC-AGI-2 in the lineage of ARC-AGI-1, names the documented limitations of v1 (brute-force susceptibility, low ceiling on hard items, calibration drift), and explains how v2 responds.
- Missing evidence: Limited external comparison to other reasoning benchmarks beyond ARC-AGI-1.
- Reviewer rationale: Within-family contextualization is strong; cross-family contextualization is light.

#### 6.1.3 Phenomenon-task-metric-claim chain
- Rating: 3
- Evidence: The chain from "fluid reasoning on novel tasks" → grid puzzles with held-out tests → exact-match pass@2 → claim that models that score well have stronger novel-task reasoning is coherent and explicit.
- Missing evidence: The link from the metric to the broader "progress toward AGI" claim is not fully argued; the authors' own necessary-but-not-sufficient caveat acknowledges this.
- Reviewer rationale: Strong inner chain; weaker outer interpretive chain.

#### 6.1.4 Task or item design
- Rating: 3
- Evidence: Grid format, color set, demonstration count, and 2-attempt policy are documented and justified as continuous with ARC-AGI-1; the four challenge categories give a design rationale for new items.
- Missing evidence: Per-task category labels are not shipped, making per-category analysis hard to reproduce.
- Reviewer rationale: Design is well-motivated; some auditability gaps.

#### 6.1.5 Procedures for developing task or item content
- Rating: 3
- Evidence: The paper describes curation by the foundation, removal of brute-forceable tasks, and a 407-participant human calibration campaign with specific compensation, session length, and inclusion rules (≥2 humans solving within 2 attempts).
- Missing evidence: Author/contributor identities for individual tasks, full inclusion/exclusion criteria for the calibration round, and inter-author redundancy checks are not externally visible.
- Reviewer rationale: A documented, non-trivial development process.

#### 6.1.6 Thoroughness of the final task or item selection process
- Rating: 3
- Evidence: Selection is anchored by the human-solvability gate; statistical similarity (IDD) across the three eval sets is claimed.
- Missing evidence: The IDD claim is not accompanied by a statistical test or distributional analysis I could locate.
- Reviewer rationale: Strong principle, partial public validation.

#### 6.1.7 Quantitative evidence of task or item quality
- Rating: 2
- Evidence: Human attempt-level success rate (~75%) and session-level success rate (~62%), median solve time (2.2 minutes), and demographic non-correlation are reported.
- Missing evidence: Per-item difficulty parameters, discrimination indices, ceiling/floor analysis, or IRT-style item statistics are not published.
- Reviewer rationale: Aggregate quality evidence is adequate; per-item quantitative quality is thin.

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice
- Rating: n/a
- Evidence: ARC-AGI-2 is a successor rather than a derived slice; the relationship to ARC-AGI-1 is explicitly described as non-interchangeable.

#### 6.1.9 Overall Rationale, development, and task or item quality
- Rating: 3
- Reviewer rationale: A well-motivated construct, a documented calibration procedure, and a multi-tier split design support qualified use; the principal residual gaps are per-item quantitative evidence and external (cross-benchmark) construct anchoring.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use — Rating: 3
- Evidence: Paper and website state purpose, intended audience (frontier-reasoning research), and the relation to ARC-AGI-1.
- Missing evidence: A formal "out-of-scope uses" list and procurement/policy non-use guidance.

#### 6.2.2 Documentation of development process — Rating: 3
- Evidence: Paper covers human-testing campaign, calibration, and design philosophy.
- Missing evidence: Per-task provenance, author credits, and selection logs.

#### 6.2.3 Documentation of scoring and metrics — Rating: 3
- Evidence: Pass@2 exact-match rule is clear in both paper and repository.
- Missing evidence: Formal treatment of malformed outputs, format-recovery policies, and Kaggle harness internals.

#### 6.2.4 Documentation of reliability, stability, and uncertainty — Rating: 1
- Evidence: Human-testing redundancy (≥2 solvers per task) is reported.
- Missing evidence: No model-side run-to-run variance, prompt sensitivity analysis, confidence intervals, or alternate-form equivalence statistics located.
- Reviewer rationale: For a leaderboard where 1 percentage point = 1 task, the absence of uncertainty reporting is consequential.

#### 6.2.5 Documentation of validity evidence — Rating: 2
- Evidence: Paper argues content validity through curation against brute-force tactics and human solvability.
- Missing evidence: External convergent/discriminant evidence, cross-benchmark correlation, predictive-relevance studies.

#### 6.2.6 Documentation of fair use and comparability — Rating: 2
- Evidence: The Kaggle vs API-hosted cohort distinction is described informally on the site.
- Missing evidence: Formal cohort-comparability guidance, multilingual coverage discussion (n/a in practice but not stated), accessibility considerations.

#### 6.2.7 Documentation of maintenance and versioning — Rating: 2
- Evidence: arXiv revision history and ARC Prize blog provide an informal changelog.
- Missing evidence: Formal benchmark-data changelog, deprecation policy, item-correction process.

#### 6.2.8 Adequacy of documentation available to users — Rating: 2
- Reviewer rationale: Documentation is sufficient for the research-research use loop but thin on uncertainty, validity, and maintenance specifics that an auditor would want.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration — Rating: 2
- Evidence: Public repository is trivially usable; Kaggle competition supplies an enforced runtime.
- Missing evidence: No canonical prompt template or reference harness for the API-hosted cohort, which means different evaluators may produce non-identical conditions.

#### 6.3.2 Scoring procedure and error handling — Rating: 3 (Kaggle) / 2 (open use)
- Evidence: Exact-match scoring leaves little ambiguity once outputs are parsed.
- Missing evidence: Documented behavior for malformed JSON, partial grids, dimension mismatches outside Kaggle.

#### 6.3.3 Interpretation and reporting guidance — Rating: 2
- Evidence: Paper carries strong interpretive caveats (necessary-but-not-sufficient AGI).
- Missing evidence: The leaderboard surface does not foreground these caveats to lay readers.

#### 6.3.4 Restrictions, prerequisites, and appropriate use — Rating: 2
- Evidence: Kaggle competition rules state hardware and offline constraints.
- Missing evidence: Public-leaderboard rules for fair cross-system comparison (e.g., how many runs, how cost is computed) are not centrally codified.

#### 6.3.5 Technical support and implementation guidance — Rating: 2
- Evidence: GitHub issues and Kaggle discussion are active community channels.
- Missing evidence: No formal SLAs, no documented troubleshooting page, no smoke-test fixtures.

#### 6.3.6 References and supporting materials — Rating: 3
- Evidence: Paper, blog, and repo cross-reference each other; ARC-AGI-1 lineage is well-cited.

#### 6.3.7 Quality of procedural instructions — Rating: 2
- Reviewer rationale: Adequate for research use, weaker for auditable cross-evaluator reproducibility.

### 6.4 Overall Adequacy of Rationale and Documentation
- Rating: 3
- Reviewer comments: ARC-AGI-2's design rationale and core documentation are strong by current AI-benchmark standards; the principal gaps are uncertainty reporting, formalized procedural reproducibility outside Kaggle, and formal cross-cohort comparability guidance.

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability — Rating: 3
- Evidence: 1,000 training + 120 public eval tasks are available as plain JSON in a versioned Apache-2.0 repository; semi-private set is delivered through Kaggle; private set is held by maintainers.
- Missing evidence: No formal dataset DOI located.

#### 7.1.2 Prompts, instructions, and input materials — Rating: 2
- Evidence: Task JSON is self-describing.
- Missing evidence: No canonical prompt template; community implementations vary in textual encoding, which can affect scores.

#### 7.1.3 Rubrics, reference answers, and response format requirements — Rating: 3
- Evidence: Reference outputs are grids; exact-match comparison is unambiguous.
- Missing evidence: No documented admissible-variant policy for whitespace, trailing rows, dimension-mismatch handling outside Kaggle.

#### 7.1.4 Evaluation harness, scorer, and implementation quality — Rating: 2
- Evidence: Kaggle hosts the official scorer for the competition; the public repository contains the canonical data.
- Missing evidence: No official open-source harness for the public-leaderboard regime; no CI badges or smoke-test fixtures externally visible on the v2 repo at review time.

#### 7.1.5 Interface and workflow usability — Rating: 3
- Evidence: `arcprize.org/play` provides a polished web UI for human testing and exploration; repository structure is conventional.

#### 7.1.6 Accessibility across modalities, languages, and system types — Rating: 3
- Evidence: Language-free design; runs on any system that can read JSON. Color encoding is also discrete integer indices, which is robust to colorblind concerns when models consume the raw integers.
- Missing evidence: For visually impaired *human* testers the website UI's accessibility is not formally documented (the human-testing campaign was sighted-only).

#### 7.1.7 Licensing, use requirements, and risk warnings — Rating: 3
- Evidence: Apache-2.0 on public materials; competition rules cover prize eligibility; no sensitive-content risk in grid puzzles.

#### 7.1.8 Overall quality of benchmark materials — Rating: 3
- Reviewer rationale: Materials are clean, licensed, and usable; the principal weaknesses are the absence of a canonical open-source harness and prompt template.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines — Rating: 2
- Evidence: Effective chance floor is ~0% given the open output space; ceiling is 100% on a split.
- Missing evidence: No empirical trivial-strategy baseline reported (e.g., copy-input, identity, majority-pixel).

#### 8.1.2 Human or expert baselines — Rating: 4
- Evidence: 407 participants, 515 sessions, 1,848 test pairs, 13,405 attempts, controlled compensation, defined session length, ≥2-solver inclusion gate. Per-attempt success ~75%, per-session ~62%, median solve time 2.2 minutes, demographic non-correlation.
- Missing evidence: No expert subgroup analysis; no condition-matching to AI evaluation (humans see a UI, models receive a JSON encoding), but this is documented and intrinsic to the task design.
- Reviewer rationale: This is among the most carefully constructed human baselines in the current AI-benchmark literature.

#### 8.1.3 Model comparator cohort — Rating: 3
- Evidence: Paper and leaderboard report a frontier-model cohort with consistent split (Semi-Private) for the prize and the public leaderboard.
- Missing evidence: Conditions across leaderboard entries (prompt templates, attempts policy, scaffolding) are not centrally documented per entry; the API-hosted cohort and the Kaggle cohort are mixed in some public discussions.

#### 8.1.4 Historical, version, or benchmark-family comparators — Rating: 3
- Evidence: Per-model ARC-AGI-1 vs ARC-AGI-2 deltas are reported (e.g., o3 medium 53% → 3%).
- Missing evidence: Authors do not provide a formal equating or normalization between v1 and v2, but explicitly caveat non-interchangeability.

#### 8.1.5 Criterion thresholds, score bands, or performance categories — Rating: 2
- Evidence: 85% Grand Prize threshold is operationally defined.
- Missing evidence: The 85% threshold is a competition decision, not an empirically justified proficiency band; the paper does not tie it to a specific capability claim.

#### 8.1.6 Representativeness of reference groups — Rating: 3
- Evidence: Human cohort is large, demographically heterogeneous, and time-bounded (Nov 2024 - May 2025).
- Missing evidence: Geographic and linguistic coverage of the participant pool not fully described.

#### 8.1.7 Currency and maintenance of baseline evidence — Rating: 3
- Evidence: Human baseline is current to within ~12 months of the v2 release; the leaderboard is updated for new models.
- Missing evidence: No documented plan to refresh the human baseline if task semantics shift.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation
- Rating: 3
- Reviewer comments: The human baseline is a major strength; the chance/trivial baseline and cross-cohort comparator hygiene are weaker.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence — Rating: 1
- Evidence: Pass@2 is built into the protocol; human-side redundancy gates task inclusion.
- Missing evidence: No published model-side run-to-run variance, no prompt-sensitivity study, no per-split confidence intervals on the headline accuracy, no formal alternate-form equivalence test for Public/Semi-Private/Private (only the IDD claim).
- Reviewer rationale: For a leaderboard where small percentage-point deltas drive ranking, the absence of published uncertainty estimates is consequential.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings — Rating: 1
- Evidence: Pass@2 captures one limited dimension of stochasticity.
- Missing evidence: No multi-seed, multi-run, or temperature-sensitivity report located.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors — Rating: 1
- Evidence: None located on the headline scores.
- Missing evidence: Binomial confidence intervals on a 120-task split would be straightforward to add; their absence is an evidence gap.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability — Rating: 3
- Evidence: Scoring is exact integer-grid match; the scorer is mathematically trivial and effectively perfect within its scope.
- Missing evidence: Reliability of *parsing* model outputs into grids depends on the evaluator's harness, which is not standardized.

#### 9.3.2 Human rater or expert scorer agreement — Rating: n/a
- Reviewer rationale: Final scoring does not involve human rating.

#### 9.3.3 Model-as-judge reliability and validity checks — Rating: n/a
- Reviewer rationale: No LLM judge in the scoring loop.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity — Rating: 1
- Evidence: None located.
- Missing evidence: Given that grid encoding is evaluator-defined, prompt-sensitivity could materially shift scores; no study published.

#### 9.4.2 Form, split, version, or refresh equivalence — Rating: 2
- Evidence: IDD claim across Public/Semi-Private/Private; empirical confirmation is implicit.
- Missing evidence: A formal distributional or score-based equivalence analysis.

#### 9.4.3 Execution environment and dependency stability — Rating: 3 (Kaggle) / 2 (open use)
- Evidence: Kaggle pins the hardware and runtime.
- Missing evidence: No dependency manifest or container image for the public-leaderboard cohort.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences — Rating: 1
- Evidence: None located.
- Missing evidence: No statistical guidance on when leaderboard deltas are meaningful; a 1-point difference equals 1 task in a 120-task split.

### 9.6 Overall Reliability, Precision, and Score Stability
- Rating: 1
- Reviewer comments: The exact-match scorer is reliable; what is not reliable is the published *evidence base* for interpreting score differences. This is the benchmark's largest evidence gap for leaderboard use.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness — Rating: 2
- Evidence: The four challenge types (multi-rule, multi-step, contextual rules, in-context symbol definition) operationalize the target construct; tasks are curated and human-calibrated.
- Missing evidence: No published coverage analysis showing the relative frequency of each challenge type or distribution across difficulty bands.
- Reviewer rationale: Content is plausibly representative *within* the grid-puzzle universe but the universe itself is narrow relative to the AGI framing.

#### 10.1.2 Construct breadth and capability-domain coverage — Rating: 1
- Evidence: The benchmark deliberately focuses on Gf-like reasoning under minimal-knowledge conditions.
- Missing evidence: No coverage across modalities, planning horizons, tool use, memory, language, or expertise.
- Reviewer rationale: The "AGI" framing implies breadth that the task surface does not deliver; under Hendrycks et al.'s ten-domain framework, ARC-AGI-2 exercises essentially one domain.
- Interpretation caution: ARC-AGI-2 should not be read as a broad capability profile.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality — Rating: 1
- Evidence: A single aggregate accuracy is reported; the four challenge types are not exposed as per-task labels.
- Missing evidence: No factor or cluster analysis; no per-category subscore breakdowns shipped.

#### 10.2.2 Item or task behavior across the score scale — Rating: 1
- Evidence: Aggregate human-success statistics exist.
- Missing evidence: No published item-level discrimination, difficulty distribution analysis, or per-item human-vs-model contrast.

#### 10.2.3 Failure modes and error analysis — Rating: 2
- Evidence: The paper discusses qualitative model-failure patterns (brute-force shortcuts that v2 design suppresses; compositional-generalization gaps).
- Missing evidence: No systematic quantitative error taxonomy with category-level model performance.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity — Rating: 3
- Evidence: Exact match aligns naturally with grid-puzzle correctness; pass@2 mitigates trivial format-recovery effects.
- Missing evidence: No formal study of how often "wrong" outputs reflect format errors vs reasoning errors.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance — Rating: 2
- Evidence: Authors explicitly removed brute-force-amenable tasks during curation.
- Missing evidence: Cannot independently verify mitigation; no published red-team study against prompt-engineering shortcuts or representation tricks.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings — Rating: 2
- Evidence: Per-model ARC-AGI-1 vs ARC-AGI-2 comparison is reported; human baseline is documented.
- Missing evidence: Correlations with other reasoning benchmarks (HLE, GPQA, FrontierMath, etc.) or with downstream task performance.

#### 10.4.2 Convergent and discriminant evidence — Rating: 1
- Evidence: None located formally.
- Missing evidence: No correlation analysis with similar reasoning benchmarks (convergent) or with knowledge-heavy benchmarks (discriminant).

#### 10.4.3 Ecological or predictive relevance — Rating: 1
- Evidence: Authors do not claim ecological/deployment relevance; they explicitly position ARC-AGI-2 as an abstract diagnostic.
- Reviewer rationale: 1 reflects "limited support for ecological use," which matches the authors' own framing. Not a defect per se, but interpretation should respect this.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls — Rating: 3
- Evidence: The public/semi-private/private split is the principal control; private set is held by maintainers; Kaggle runs offline; ARC Prize blog acknowledges that "ARC data is well represented" in frontier-model training corpora and uses the held-out splits as the mitigation.
- Missing evidence: No canary strings; no formal pre-exposure searchability audit; no public leak-response protocol.
- Reviewer rationale: Structural controls are strong for a public/private split design; missing evidence prevents a 4.

#### 10.5.2 Gameability and benchmark-specific tuning controls — Rating: 3
- Evidence: Kaggle's offline sandbox and the private set materially constrain leaderboard gaming; the 85% Grand Prize threshold has not been met as of the 2025 cycle (top private-eval submission ~24%).
- Missing evidence: No formal policy on permissible test-time-training (TTT), which is widely used by competitive submitters; the boundary between legitimate adaptation and benchmark-specific overfitting is implicit.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims — Rating: 2
- Evidence: Authors include the necessary-but-not-sufficient AGI caveat and stress that scaling alone will not solve v2.
- Missing evidence: The benchmark *name* and prize framing carry an implicit broad claim that the caveats only partially defuse; secondary commentary (blog, public communications) sometimes leans more strongly on the AGI framing than the construct evidence supports.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims — Rating: 1
- Evidence: The single-modality, single-domain task surface does not provide cross-domain breadth required to support broad intelligence claims under the CHC framework adopted in MESA.
- Missing evidence: No multi-domain validity argument linking ARC-AGI-2 performance to broader cognitive abilities.
- Reviewer rationale: The authors' own caveats partly address this, but the rating reflects the evidence base, not the maintainers' good-faith caution.
- Interpretation caution: ARC-AGI-2 scores should not be interpreted as proxies for general intelligence or AGI proximity; treat them as evidence about novel compositional grid-puzzle reasoning.

### 10.7 Overall Validity Support
- Rating: 2
- Reviewer comments: ARC-AGI-2 provides solid content validity within its narrow operationalization and strong contamination controls via its split design. It does not yet provide the convergent/discriminant evidence, internal-structure analysis, or breadth coverage that would be needed to license broader interpretations. Within the intended frontier-research-diagnostic use, the rating is "cautious" rather than "inadequate."

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts — Rating: 2
- Evidence: The construct is plausibly relevant across any system that can ingest grid representations.
- Missing evidence: No formal discussion of how the construct generalizes across system classes (e.g., program-synthesis systems vs LLMs vs hybrid scaffolds).

#### 11.1.2 Documentation of fair-use considerations — Rating: 1
- Evidence: Little.
- Missing evidence: No formal fair-use, accessibility, or bias-consideration section in the public materials I inspected.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design — Rating: 2
- Evidence: Language-free design is intrinsically inclusive; integer-encoded grids work for any modality.
- Missing evidence: Accessibility consideration for visually impaired *humans* using the play interface not externally documented.

#### 11.2.2 Domain, language, modality, and subgroup coverage — Rating: 1
- Evidence: Single modality (visual grids encoded as integers), one task surface.
- Reviewer rationale: A 1 here reflects the breadth gap, not a design failure: the benchmark is designed to be narrow.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability — Rating: 2
- Evidence: Kaggle sandbox enforces a controlled comparator for the prize cohort.
- Missing evidence: The public-leaderboard cohort mixes API-hosted models with different scaffolds, prompt encodings, attempt-budget interpretations, and cost models; comparability hygiene varies.

#### 11.3.2 Access, compute, tooling, and API or local comparability — Rating: 2
- Evidence: Cost-per-task is reported alongside accuracy, which partially addresses compute comparability.
- Missing evidence: No standardized definition of "cost" across submitters (model cost vs end-to-end pipeline cost vs amortized inference).

#### 11.3.3 Temporal comparability for rolling or live benchmarks — Rating: 2
- Evidence: ARC Prize cycle labels (2025, 2026) provide a cohort axis.
- Missing evidence: No formal policy on whether year-N and year-N+1 scores are directly comparable, given that the public eval set is static but reference cohorts and scaffolds evolve.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis — Rating: 2
- Evidence: Demographic non-correlation among *human* testers is reported.
- Missing evidence: No analysis of model-class differential performance (e.g., whether scaffolds advantage certain model families); no language/cultural bias since the benchmark is language-free.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts — Rating: 1
- Evidence: None located.
- Missing evidence: Subgroup analysis across model families, scaffolds, cost tiers.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases — Rating: 2
- Evidence: Necessary-but-not-sufficient AGI caveat in paper.
- Missing evidence: A formal enumeration of non-use cases (e.g., procurement, deployment gating, safety certification, broad-capability claims).

#### 11.5.2 Release rules and sensitive-content handling — Rating: 3
- Evidence: Apache-2.0 license, Kaggle competition terms, no sensitive content risk for grid puzzles.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use
- Rating: 2
- Reviewer comments: Comparability is structurally good within the Kaggle cohort and weaker across the public-leaderboard cohort; appropriate-use guidance leans on author caveats rather than formal non-use statements.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope — Rating: 3
- Evidence: Public leaderboard surfaces accuracy and cost-per-task; paper and blog provide narrative analysis.
- Missing evidence: Per-task or per-category breakdowns not reported.

#### 12.1.2 Score granularity and level of detail — Rating: 2
- Evidence: Single accuracy number per split is appropriately coarse for a single-construct benchmark.
- Missing evidence: With 120-task splits, the implied precision (two-decimal percentages) outruns what binomial uncertainty supports without intervals.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling — Rating: 2
- Evidence: Model and cohort labels are present.
- Missing evidence: No confidence intervals; no formal evaluation-condition labels (prompt, attempt policy, scaffold) per leaderboard entry; cohort-mixing risk between Kaggle and API-hosted entries.

#### 12.2.2 Reproducibility and traceability of reported scores — Rating: 2
- Evidence: Kaggle submissions are at least nominally reproducible inside the sandbox; published frontier-model scores are not always accompanied by a runnable script.
- Missing evidence: No standardized reproduction recipe for the public leaderboard.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims — Rating: 2
- Evidence: Paper articulates careful interpretive language; blog posts are more conservative than the benchmark name suggests.
- Missing evidence: The leaderboard surface and the benchmark *name* together can drive public interpretations that exceed the construct evidence.

#### 12.3.2 Raw outputs, per-item data, or trace availability — Rating: 1
- Evidence: Per-item outputs not generally published.
- Missing evidence: Audit access to model traces for the leaderboard cohort.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports — Rating: 2
- Evidence: Reporting is neutral across model providers; cost axis prevents pure-accuracy bias toward expensive systems.
- Missing evidence: Explicit bias-of-coverage statements.

#### 12.4.2 Acceptability and usability for intended audiences — Rating: 3
- Evidence: Paper and leaderboard are well-presented for the research audience; blog posts are accessible to lay readers.

#### 12.4.3 Public communication and leaderboard governance — Rating: 2
- Evidence: ARC Prize governance is centralized and transparent at the cycle level.
- Missing evidence: Formal eligibility rules, audit routes, and update-cadence policies are not all centrally codified outside the Kaggle competition page.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims
- Rating: 2
- Reviewer comments: Reporting is clear and competently designed; what holds the rating back is the absence of uncertainty/condition labels and the gap between the benchmark's framing ("AGI") and the granularity of evidence presented.

---

## Final Evaluation

### Evaluative Report of the Benchmark

ARC-AGI-2 is, as a measurement instrument for novel-task compositional generalization under minimal-knowledge conditions, one of the more carefully constructed AI benchmarks currently in active use. Its strengths are: (i) a defensible construct that is operationalized via a tightly curated grid-puzzle format inherited from a well-studied predecessor; (ii) a substantial first-party human-calibration program (407 participants, controlled compensation, structured sessions, redundancy gating) that gives the benchmark an unusually credible human baseline; (iii) a multi-tier public/semi-private/private split design backed by an offline Kaggle sandbox, which together provide strong structural protections against item-level leakage and brute-force gaming; (iv) explicit author caveats about claim proportionality, including a clear necessary-but-not-sufficient framing for AGI interpretations; and (v) a permissive Apache-2.0 license with active public materials and an active maintainer-led prize ecosystem.

Its principal limitations as an evaluation instrument are concentrated in three areas. First, reliability and precision reporting is thin: there are no published confidence intervals, no run-to-run variance studies, no prompt-sensitivity analyses, and no formal alternate-form equivalence tests for the three eval splits beyond the IDD claim. For a leaderboard whose splits are 120 tasks each, a one-percentage-point delta equals one task, so the absence of uncertainty quantification matters for ranking interpretation. Second, validity evidence beyond content validity is limited: there is no published convergent/discriminant analysis against other reasoning benchmarks, no internal-structure analysis of the four challenge types, and no ecological/predictive-relevance argument (and the authors do not claim one). Third, the benchmark's framing as an "AGI" diagnostic exceeds what the single-modality, single-domain task surface can support under the CHC-style breadth criterion used in MESA; this is partly defused by the authors' own caveats but is not eliminated, especially in public communication.

The reviewed entity (ARC-AGI-2 in its current v2 release, with the maintained public/semi-private/private split, the ARC Prize Kaggle cohort, and the public-leaderboard cohort) is well-suited to research-diagnostic and competition use, and is appropriate as evidence about novel compositional reasoning on abstract grid tasks. It is not suitable on current evidence as a procurement, deployment-gating, safety, or general-capability instrument, and scores should not be read as proxies for general intelligence. Ongoing work signaled by the maintainers includes an ARC-AGI-3 (interactive) successor in preparation and continued ARC Prize cycles on v2 through 2026.

### Conclusions

ARC-AGI-2 is a well-designed narrow-construct benchmark with one of the strongest human baselines and contamination-control regimes in current AI evaluation, and is appropriate for cautious research diagnostic and prize-competition use; it is *not* on current evidence appropriate for broad intelligence claims, procurement, or deployment decisions. Responsibly using ARC-AGI-2 requires familiarity with its split design, the difference between the Kaggle and API-hosted cohorts, and the absence of published uncertainty estimates; this matches the maintainers' own positioning of the benchmark as a frontier-research stress-test rather than as a capability certification.

### Recommendations

1. **Maintainers (original benchmark and leaderboard):** publish binomial confidence intervals on per-split accuracy and a minimal multi-seed/prompt-sensitivity study, even if conducted on the public eval set only; codify leaderboard eligibility rules, prompt-encoding conventions, and cost-accounting definitions in a single public document; ship per-task challenge-type labels to enable third-party subscore analysis.
2. **Maintainers (public claims):** add a brief "what scores do and do not support" panel to the leaderboard page, mirroring the paper's necessary-but-not-sufficient caveat; clearly separate Kaggle-cohort from API-hosted-cohort entries on the leaderboard surface.
3. **Maintainers (reproducibility):** release a canonical open-source evaluation harness (prompt template, parser, scoring script) for the public eval set so that independent reports are comparable.
4. **Benchmark users:** report ARC-AGI-2 results with cohort labels, prompt encoding, attempts policy, and at minimum a binomial confidence interval; avoid headline framings that equate ARC-AGI-2 performance with progress toward AGI.
5. **Future reviewers:** revisit Section 9 once the maintainers publish uncertainty evidence, and Section 10.4 once external convergent/discriminant data accumulate; track whether ARC-AGI-3 absorbs the AGI framing in a way that lets v2 be positioned more narrowly.

### Summary of Ratings

| Section                                                      | Overall Rating (`n/a`, `0`-`4`) |
| :----------------------------------------------------------- | :-----------------------------: |
| Section 6. Rationale, documentation, and task/item quality   |               3                 |
| Section 7. Benchmark materials and usability                 |               3                 |
| Section 8. Reference points and documented comparison groups |               3                 |
| Section 9. Reliability and precision                         |               1                 |
| Section 10. Validity support                                 |               2                 |
| Section 11. Fair use and comparability                       |               2                 |
| Section 12. Reports, leaderboards, and public score claims   |               2                 |

Reviewer comments: The overall picture is "structurally strong, evidentially incomplete." Section 9 is the single rating most likely to change with modest additional maintainer effort.

### Gap Register

| Missing or inaccessible information needed for interpretation                                              | Affected entity or reporting surface                              | Affected capability domain or score interpretation                                           | Affected rating(s)              | Why it matters                                                                                                          | Needed for a higher rating                                                            |
| :--------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| Confidence intervals / standard errors on per-split accuracy                                               | Public leaderboard, paper tables                                  | All score interpretations                                                                    | 6.2.4, 9.1.1, 9.2.2, 12.2.1     | 120-task splits make 1pp ≈ 1 task; rankings can flip within noise                                                       | Binomial intervals or bootstrap CIs reported alongside every score                    |
| Multi-seed / multi-run variance reports for stochastic systems                                             | Paper, leaderboard                                                | Score stability                                                                              | 9.2.1                           | Frontier reasoning models are stochastic; pass@2 captures only one dimension                                            | Published k-run variance for at least the public eval cohort                          |
| Prompt-sensitivity / grid-encoding sensitivity study                                                       | API-hosted cohort                                                 | Cross-system comparability                                                                   | 6.2.4, 9.4.1, 11.3.1            | Different evaluators encode grids differently; scores can shift materially                                              | A canonical prompt or a sensitivity table across reasonable encodings                 |
| Per-task category labels for the four challenge types                                                      | Repository                                                        | Internal-structure validity                                                                  | 10.2.1, 6.1.4                   | Without labels, the design taxonomy is not auditable                                                                    | Ship category labels in the public eval set JSON                                      |
| Convergent/discriminant correlation studies with other reasoning and knowledge benchmarks                   | Paper, future analyses                                            | Construct validity                                                                           | 10.4.1, 10.4.2                  | Without these, the construct rests on content-validity arguments alone                                                  | Published correlations across a representative model cohort                            |
| Formal equivalence analysis of Public/Semi-Private/Private splits beyond the IDD claim                      | Paper                                                             | Cross-split comparability                                                                    | 9.4.2, 10.2.1                   | The headline interpretation depends on splits being interchangeable                                                     | Distributional and score-based equivalence tests                                       |
| Trivial-strategy baselines (copy-input, majority-pixel, identity)                                          | Paper, leaderboard                                                | Chance/floor interpretation                                                                  | 8.1.1                           | Empirical floors strengthen the meaning of low-but-nonzero model scores                                                 | Reported empirical floor scores                                                       |
| Canonical open-source evaluation harness for the public eval set                                           | Repository                                                        | Reproducibility, cross-evaluator comparability                                                | 7.1.4, 9.4.3, 12.2.2            | Independent reports are not directly comparable without a shared harness                                                | Released harness + smoke-test fixtures + CI signal                                    |
| Formal cohort separation on the public leaderboard (Kaggle vs API-hosted)                                  | Public leaderboard                                                | Comparability                                                                                | 11.3.1, 12.2.1                  | Cross-cohort comparisons are not condition-matched                                                                      | Cohort-labeled views and explicit cross-cohort warning                                |
| Formal non-use and appropriate-use statements                                                              | Website, leaderboard                                              | Claim proportionality                                                                        | 11.5.1, 12.3.1, 10.6.1, 10.6.2 | Without explicit non-use guidance, the AGI framing risks misinterpretation                                              | Published "supported uses / unsupported uses" panel                                   |
| Per-item or trace-level audit access                                                                       | Leaderboard cohort                                                | Validity, reproducibility                                                                    | 12.3.2                          | Independent scrutiny of frontier-model behavior is currently limited                                                    | Controlled-access trace release for selected submissions                              |
| Formal benchmark-data changelog and deprecation/refresh policy                                              | Repository                                                        | Lifecycle interpretation                                                                     | 5.8, 6.2.7                      | Users cannot tell what is stable vs evolving                                                                            | A versioned CHANGELOG.md and a deprecation policy                                     |

---

## Bibliography

[1] D. Hendrycks et al., "A Definition of AGI," arXiv:2510.18212, 2025.

[2] A. M. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," arXiv:2511.04703, 2025.

[3] A. Reuel et al., "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices," arXiv:2411.12990, 2024.

[4] F. Chollet, M. Knoop, G. Kamradt, B. Landers, H. Pinkard, "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems," arXiv:2505.11831v2, 2026.

[5] ARC Prize Foundation, "ARC-AGI-2" benchmark page, `https://arcprize.org/arc-agi/2`, accessed 2026-05-18.

[6] ARC Prize Foundation, ARC-AGI-2 public repository, `https://github.com/arcprize/ARC-AGI-2`, accessed 2026-05-18.

[7] ARC Prize Foundation, ARC Prize public leaderboard, `https://arcprize.org/leaderboard`, accessed 2026-05-18.

[8] ARC Prize Foundation, "ARC Prize 2025 Results and Analysis," blog post, accessed 2026-05-18.

[9] F. Chollet, "On the Measure of Intelligence," arXiv:1911.01547, 2019 (parent ARC-AGI-1 reference).
