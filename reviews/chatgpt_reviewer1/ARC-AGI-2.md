# MESA Review: ARC-AGI-2

Review status: full Part A + Part B MESA review  
Reviewed entity: ARC-AGI-2 official benchmark, public data, semi-private/private evaluation structure, official ARC Prize leaderboard surfaces, and official benchmarking materials  
Reviewer profile: `.codex/agents/benchmark-reviewer.md`  
Date of current review: 2026-05-17

## Short Stand-Alone Non-Evaluative Benchmark Description

ARC-AGI-2 is a public grid-transformation benchmark in the ARC-AGI family. Each task presents a small number of demonstration input-output grids and asks the evaluated system to infer the underlying rule and produce exact output grid(s) for unseen test input(s). The public release contains 1,000 training tasks and 120 public evaluation tasks, with additional 120-task semi-private and private evaluation sets used for controlled leaderboard and competition purposes. ARC Prize positions the benchmark as a harder successor to ARC-AGI-1, designed to challenge current reasoning systems, reduce brute-force susceptibility, improve human calibration, and report both performance and efficiency. The strongest descriptive classification is performance on ARC-style exact-grid abstraction tasks under specified access, attempt, and compute conditions.

## Source Inventory

| ID  | Source                                                                                                                                                              | Access date | Use in this review                                                                                                                  |
| :-- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| S01 | ARC Prize, [ARC-AGI-2 official benchmark page](https://arcprize.org/arc-agi/2)                                                                                      | 2026-05-17  | Benchmark identity, claims, dataset structure, calibration, changelog summary, efficiency framing.                                  |
| S02 | ARC Prize, [ARC-AGI-2 GitHub repository](https://github.com/arcprize/ARC-AGI-2), including README, license, public data, and changelog                              | 2026-05-17  | Public task data, public split counts, file format, task success criterion, release/changelog, license.                             |
| S03 | ARC Prize, [ARC-AGI-2 technical report blog page](https://arcprize.org/blog/arc-agi-2-technical-report)                                                             | 2026-05-17  | Report landing page, publication date, benchmark goals, human testing summary, state-of-the-art framing.                            |
| S04 | Chollet, Knoop, Kamradt, Landers, and Pinkard, [ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems](https://arxiv.org/abs/2505.11831), arXiv:2505.11831v2 | 2026-05-17  | Technical report details, task design, human calibration protocol, split calibration, baseline model results, competition protocol. |
| S05 | ARC Prize, [ARC-AGI-1 & ARC-AGI-2 Guide](https://arcprize.org/guide/1)                                                                                              | 2026-05-17  | Task format, public/semi-private/private data descriptions, scoring methods, development guidance.                                  |
| S06 | ARC Prize, [Verified Testing Policy](https://arcprize.org/policy)                                                                                                   | 2026-05-17  | Verification policy, valid submission types, hidden-set rationale, cost caps, submission rules, reporting governance.               |
| S07 | ARC Prize, [ARC-AGI leaderboard](https://arcprize.org/leaderboard)                                                                                                  | 2026-05-17  | Public reporting surface, cost/performance framing, preview and incomplete-testing caveats.                                         |
| S08 | ARC Prize, [arc-agi-benchmarking repository](https://github.com/arcprize/arc-agi-benchmarking)                                                                      | 2026-05-17  | Open benchmarking harness, adapters, scoring script, sample random baseline, model configuration and cost fields.                   |
| S09 | Repository report, `reports/benchmark_official_documentation_inventory.md`                                                                                          | 2026-05-17  | Local source inventory starting point.                                                                                              |
| S10 | MESA template, `MESA EFPA template official.md`                                                                                                                     | 2026-05-17  | Review structure, field guidance, rating scale, ARC-AGI-2 examples.                                                                 |
| S11 | BetterBench, `literature/betterbench.md`                                                                                                                            | 2026-05-17  | Documentation, implementation, reproducibility, and maintenance criteria.                                                           |
| S12 | Measuring what Matters, `literature/Measuring_what_Matters.md`                                                                                                      | 2026-05-17  | Construct-validity chain: phenomenon, task, metric, claim.                                                                          |
| S13 | A Definition of AGI, `literature/A_Definition_of_AGI.md`                                                                                                            | 2026-05-17  | Broad AGI/CHC-style capability breadth cautions.                                                                                    |

# Part A. Description of the Benchmark

Part A is descriptive. It records what the available sources state or make inspectable. Evaluative judgments are reserved for Part B.

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt                                    | Description                                                 |
| :---------------------------------------- | :---------------------------------------------------------- |
| Reviewer Name                             | MESA review generated under the benchmark-reviewer profile. |
| Date of Current Review                    | 2026-05-17                                                  |
| Date of Previous Review _(if applicable)_ | n/a                                                         |

Reviewer comments: Full MESA Part A + Part B review of ARC-AGI-2 public benchmark materials, semi-private/private evaluation structure where documented, official leaderboard surfaces, and official benchmarking materials. Official ARC Prize materials and the arXiv technical report are primary. Local MESA literature is used for evaluative criteria. ARC-AGI-1, ARC-AGI-3, Kaggle variants, and third-party systems are contextual only unless cited by ARC Prize materials.

### 1.2 Benchmark Identity & Provenance

| Prompt                                 | Description                                                                                                                                                                                             |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reviewed Entity Name                   | ARC-AGI-2                                                                                                                                                                                               |
| Short Name / Acronym                   | ARC-AGI-2                                                                                                                                                                                               |
| Entity Type                            | Original benchmark version in the ARC-AGI benchmark family; includes public dataset release plus controlled semi-private/private evaluation forms.                                                      |
| Parent / Source Benchmark              | ARC-AGI-1 / Abstraction and Reasoning Corpus for Artificial General Intelligence. ARC-AGI-2 preserves the grid input-output format while expanding and recalibrating the task set [S01, S04, S05].      |
| Exact Version / Release Split          | ARC-AGI-2 public release: 1,000 public training tasks and 120 public evaluation tasks in the repository; 120 semi-private and 120 private evaluation tasks are not public [S01, S02, S05].              |
| Implementation / Scorer Version        | Public ARC-AGI-2 repository and `arc-agi-benchmarking` repository as accessed on 2026-05-17. No pinned commit or release tag was selected for this review [S02, S08].                                   |
| Creators & Current Maintainers         | Francois Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard are listed as technical report authors; ARC Prize / `arcprize` maintains the official site and repositories [S02, S04]. |
| Host Organization / Repository Owner   | ARC Prize / `arcprize` GitHub organization [S02, S08].                                                                                                                                                  |
| Release Dates                          | Repository changelog states ARC-AGI-2 was released on 2025-03-24; technical report blog page was published 2025-05-20; arXiv v1 was submitted 2025-05-17 and v2 was revised 2026-01-15 [S02, S03, S04]. |
| License & Access Terms                 | Public repository materials are under Apache License 2.0 [S02]. Semi-private and private evaluation sets are controlled-access and not included in the public repository [S01, S05, S06].               |
| Persistent Identifier / DOI / Citation | arXiv:2505.11831, DOI 10.48550/arXiv.2505.11831 [S04].                                                                                                                                                  |

### 1.3 Materials, Sources, & Access Tracking

| Material / Artifact Type       | URL, Location, or Identifier                                                                                                        | Access Date |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| Paper / Technical Report       | https://arxiv.org/abs/2505.11831                                                                                                    | 2026-05-17  |
| Website / Documentation Hub    | https://arcprize.org/arc-agi/2                                                                                                      | 2026-05-17  |
| Code Repository                | https://github.com/arcprize/ARC-AGI-2                                                                                               | 2026-05-17  |
| Dataset / Task / Prompt Set    | `data/training` and `data/evaluation` in the ARC-AGI-2 repository; semi-private/private task sets are controlled [S02, S05].        | 2026-05-17  |
| Evaluation Harness / Runner    | https://github.com/arcprize/arc-agi-benchmarking                                                                                    | 2026-05-17  |
| Leaderboard / Results Portal   | https://arcprize.org/leaderboard                                                                                                    | 2026-05-17  |
| Guides _(User/Scoring/Rubric)_ | https://arcprize.org/guide/1 and https://arcprize.org/policy                                                                        | 2026-05-17  |
| Changelog / Release Logs       | ARC-AGI-2 repository `changelog.md`                                                                                                 | 2026-05-17  |
| Official Announcements         | https://arcprize.org/blog/arc-agi-2-technical-report                                                                                | 2026-05-17  |
| Contextual Literature          | `literature/betterbench.md`; `literature/Measuring_what_Matters.md`; `literature/A_Definition_of_AGI.md`                            | 2026-05-17  |
| Feedback / Contact Channels    | GitHub repository issues and ARC Prize contact/policy routes where available [S02, S06, S08].                                       | 2026-05-17  |

Reviewer comments: ARC-AGI-2 is an upgraded ARC-AGI benchmark version for evaluating abstract reasoning and problem-solving on novel grid-transformation tasks. Tasks present demonstration input-output grid pairs and require the test-taker to infer an unstated transformation rule and construct output grid(s) for held-out input grid(s). ARC Prize frames ARC-AGI-2 as a challenge for frontier reasoning systems and as an AGI-progress signal, while the task evidence itself is limited to the ARC grid-transformation domain [S01, S03, S04, S05].

---

## Section 2. Classification

### 2.1 Claimed Capability Domains

Specify the capabilities, phenomena, or qualities the benchmark claims to measure, using the CHC-inspired domains above where applicable.

- [ ] Not explicitly stated
- [ ] General Knowledge (K)
- [ ] Reading and Writing Ability (RW)
- [ ] Mathematical Ability (M)
- [x] On-the-Spot Reasoning (R)
- [x] Working Memory (WM)
- [ ] Long-Term Memory Storage (MS)
- [ ] Long-Term Memory Retrieval (MR)
- [x] Visual Processing (V)
- [ ] Auditory Processing (A)
- [x] Speed (S)
- [ ] Coding or software engineering
- [ ] Specialized scientific or technical expertise
- [ ] Domain-specific professional expertise
- [ ] Tool use
- [ ] Agency or autonomy
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [ ] Factuality or grounding
- [ ] Multilingual or cross-cultural capability
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [ ] Calibration or uncertainty

Reviewer comments: The primary claim is on-the-spot abstract reasoning over novel grid transformations. Visual processing is secondary because inputs and outputs are colored symbolic grids; working memory is relevant for multi-rule and multi-step tasks. Speed is included as a reporting/efficiency dimension rather than task content because ARC Prize reports cost and efficiency alongside score [S01, S04, S07]. Broad AGI/general intelligence language appears in official framing but is evaluated as a broad-claim issue in Part B [S02, S04, S06].

### 2.2 Area of Use

Select all documented use contexts.

- [ ] Not explicitly stated
- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [ ] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison
- [ ] Internal regression testing
- [x] Public communication or marketing
- [x] Policy or governance analysis

Reviewer comments: ARC-AGI-2 is used for AI benchmark research, ARC Prize competitions, public leaderboard comparison, frontier model evaluation, solver development, and public communication about progress on ARC-style abstract reasoning [S01, S04, S06, S07].

### 2.3 Intended AI Systems

Only record systems stated or clearly implied by benchmark documentation.

- [ ] Not explicitly stated
- [x] Frontier general-purpose language models
- [x] Chat or instruction-following models
- [x] Base language models
- [ ] Code models
- [x] Multimodal models
- [ ] Audio or speech models
- [ ] Agentic systems
- [ ] Tool-using systems
- [ ] Retrieval-augmented systems
- [x] Domain-specialized models
- [x] Open-weight local models
- [x] API-hosted models

Reviewer comments: Official materials report selected closed-source frontier model performance, support local/open-source solvers through competition and harness routes, and state that the leaderboard is open to all model types and does not require multimodal models [S04, S06, S08].

### 2.4 Intended Users of Benchmark Outputs

Select all that apply.

- [ ] Not explicitly stated
- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [x] Product teams
- [x] Safety evaluators
- [x] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [ ] Educators or academic reviewers
- [x] Public leaderboard users

Reviewer comments: Intended users include ARC Prize maintainers, benchmark researchers, AI developers, competition participants, model providers, leaderboard users, public observers of AI progress, and policy/safety audiences interested in frontier capability measurement [S01, S03, S06, S07].

### 2.5 Task Families, Subdomains, and Scores

Describe the number and meaning of task families, subdomains, splits, score families, aggregate scoring rules, subscores, or derived outputs. This section is descriptive; do not judge representativeness here.

| Component                                                                                          | Description                                                                                                                                                                                                                                    |
| :------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capability, phenomenon, or quality the benchmark claims to measure                                 | Abstract reasoning, problem solving, general fluid intelligence, and progress toward AGI-relevant reasoning as framed by ARC Prize materials [S01, S03, S04].                                                                                  |
| Definition of the capability or quality being measured                                             | The available documentation operationalizes the construct through novel grid-transformation tasks requiring inference from demonstrations and exact output-grid construction [S02, S04, S05].                                                  |
| Subcomponents of the claimed capability, phenomenon, or quality                                    | Symbolic interpretation, compositional reasoning, contextual rule application, multi-step compositional reasoning, and in-context symbol definition [S01, S04].                                                                                |
| Excluded scope or non-target abilities                                                             | Language, long-horizon agency, broad world knowledge, social reasoning, auditory processing, many memory forms, tool use, embodied interaction, and real-world task performance are not directly sampled by the reviewed ARC-AGI-2 grid tasks. |
| Benchmark item, prompt, episode, environment, or interaction families or subdomains                | Structured JSON grid tasks with training examples and test input(s); no official subscore by task family was identified in public reporting [S02, S05].                                                                                        |
| Sources for benchmark items, prompts, episodes, environments, or interactions                      | Newly authored ARC Prize Foundation/staff/partner tasks and previously unused reserves, excluding ARC-AGI-1 public training tasks from human testing [S04].                                                                                    |
| Sampling method for benchmark items, prompts, episodes, environments, or interactions              | Curated and filtered task pool rather than random sampling from a fully specified universe [S04].                                                                                                                                              |
| Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions | Human solvability filtering, redundancy detection, final validation, and split calibration [S04].                                                                                                                                              |
| Splits or partitions                                                                               | 1,000 public training tasks; 120 public evaluation tasks; 120 semi-private evaluation tasks; 120 private evaluation tasks [S01, S02, S05].                                                                                                     |
| Primary score                                                                                      | Aggregate exact-match task accuracy / success rate [S04, S05, S07].                                                                                                                                                                            |
| Subscores                                                                                          | No official task-family subscores identified; split-specific scores or task-level results may be reported in controlled contexts [S06, S07].                                                                                                   |
| Derived scores or scores combined from item, task-family, or subscore results                      | Cost / efficiency reporting is used alongside score; pixel correctness is described as an auxiliary diagnostic rather than primary success [S05, S06, S07].                                                                                    |
| Qualitative score ranges such as low/medium/high or novice/expert                                  | Grand Prize threshold is 85% hidden private evaluation accuracy; report also states ARC-AGI-2 accuracies below 5% are generally not treated as meaningful signal [S04].                                                                        |
| Boundaries or caveats for interpretations made from benchmark scores                               | ARC Prize policy states that ARC Prize benchmarks are designed to measure AI progress and are not a litmus test for AGI [S06].                                                                                                                 |

Reviewer comments: The primary public score is aggregate task accuracy, often reported with cost/efficiency information. Task-family labels are descriptive rather than official subscore dimensions [S01, S04, S07].

### 2.6 Model Response Mode

Select all that apply.

- [ ] Not explicitly stated
- [ ] Multiple choice
- [ ] Short text
- [ ] Long-form text
- [x] Structured output, such as JSON or XML
- [ ] Code
- [ ] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or other output generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment

Reviewer comments: The expected response is a structured output grid for each test input. Native task files are JSON dictionaries with `train` and `test` fields containing input/output grid pairs. A grid is a rectangular matrix of integers from 0 to 9, with size from 1x1 to 30x30 [S02, S05]. Natural language explanation is not part of the score.

### 2.7 Prerequisites for Evaluated Systems

EFPA asks about demands placed on the person being assessed. MESA translates this into prerequisites placed on the evaluated AI system. Record what capabilities, interfaces, resources, or access conditions a system must have to participate as intended. Distinguish a true requirement from a convenience or from information that is simply missing.

| Requirement                                                     | Irrelevant or not necessary | Necessary information given | Information missing |
| :-------------------------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: |
| Language support                                                |             [x]             |             [ ]             |         [ ]         |
| Context length                                                  |             [ ]             |             [ ]             |         [x]         |
| Multimodal input support                                        |             [x]             |             [ ]             |         [ ]         |
| Structured output support                                       |             [ ]             |             [x]             |         [ ]         |
| Exact format, schema, or parser compatibility                   |             [ ]             |             [x]             |         [ ]         |
| Retry, repair, or correction-loop support for malformed outputs |             [ ]             |             [ ]             |         [x]         |
| Tool access                                                     |             [x]             |             [ ]             |         [ ]         |
| Browser or internet access                                      |             [x]             |             [ ]             |         [ ]         |
| Code execution                                                  |             [ ]             |             [x]             |         [ ]         |
| External API or tool credentials                                |             [ ]             |             [x]             |         [ ]         |
| Memory or persistent state                                      |             [x]             |             [ ]             |         [ ]         |
| Environment, simulator, or task-registry compatibility          |             [x]             |             [ ]             |         [ ]         |
| API compatibility                                               |             [ ]             |             [x]             |         [ ]         |
| Latency or time budget                                          |             [ ]             |             [x]             |         [ ]         |
| Cost or compute budget                                          |             [ ]             |             [x]             |         [ ]         |

Reviewer comments: Evaluated systems must read or receive grid tasks, infer a transformation rule from demonstration pairs, generate output grid dimensions and cell values, and format outputs so that a scorer can compare them exactly against reference outputs [S02, S05, S08]. Systems using the official verification path must satisfy submission and runtime rules, including open-source requirements for some submissions, Kaggle notebook execution, and cost caps where applicable [S06].

### 2.8 Evaluation Conditions

EFPA records special testing conditions because scores can change when administration changes. MESA records the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules under which AI systems are evaluated. These conditions are part of the benchmark definition, not implementation trivia.

| Condition                                     | Description                                                                                                                                                                       |
| :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompting protocol                            | Public tasks are administered as grid examples and test input(s); the verified testing policy states a preference for minimal generic LLM prompts where relevant [S02, S05, S06]. |
| System prompt                                 | No single public system prompt is specified for all evaluations; harness/provider prompts may vary [S06, S08].                                                                    |
| Few-shot examples                             | Each task includes demonstration input-output grid pairs in the task file [S02, S05].                                                                                             |
| Sampling settings                             | Harness exposes configurable model parameters; official universal settings are not fully centralized [S08].                                                                       |
| Tool permissions                              | 2025 competition protocol described no internet access; public leaderboard testing may use different routes [S04, S06].                                                           |
| Tool/API credential policy                    | Verification policy covers provider keys and cost caps for selected evaluations [S06].                                                                                            |
| Time limits                                   | Human calibration used 90-minute sessions; 2025 Kaggle competition used a 12-hour wall-clock window for 240 hidden tasks [S04].                                                   |
| Human intervention rules                      | Official competition/verification constrains submission form and run route; manual task solving by humans is used as calibration, not AI scoring [S04, S06].                      |
| Official rerun, retry, or repair policy       | Public sources do not provide a complete centralized malformed-output retry/repair rule; policy gives selected verification routes [S06].                                         |
| Hardware or hosted service                    | 2025 competition protocol described four NVIDIA L4 GPUs; verification and API testing may vary by route [S04, S06].                                                               |
| Network requirements                          | Competition described no internet; public local runs and API runs can require local files or provider access depending on route [S04, S06, S08].                                  |
| Sandbox or security constraints               | Kaggle competition route uses offline notebook substitution; public harness runs depend on user environment [S04, S08].                                                           |
| Model identity and version-label requirements | Policy and leaderboard report model/system identity where verified or listed [S06, S07].                                                                                          |

Reviewer comments: ARC-AGI-2 supports local public evaluation, hosted/controlled verification, and competition submission. Scores can depend on model configuration, reasoning level, prompt, number of attempts, API pricing, compute budget, public versus hidden split, and whether a result is verified or self-reported [S06, S07, S08].

### 2.9 Task Interaction and Observable Evidence Types

- [ ] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [x] Ranking
- [ ] Classification
- [ ] Pairwise preference
- [ ] Open-ended text
- [ ] Code generation
- [ ] Proof, derivation, or explanation
- [x] Structured data
- [ ] Generated media
- [ ] Artifact production
- [ ] Patch or repository modification
- [ ] Coordinate, bounding target, or GUI-grounding target
- [ ] Document parsing, layout reconstruction, or OCR-style extraction
- [ ] Tool use
- [ ] Browser or web navigation
- [ ] API interaction
- [ ] Computer-use interaction
- [ ] Simulated environment task
- [ ] Real or external environment task
- [ ] Terminal, shell, or filesystem task
- [ ] User-simulator interaction
- [ ] Long-horizon episode or stateful task
- [x] Response latency
- [ ] Token usage
- [x] Cost
- [ ] Tool traces
- [ ] Search or retrieval transcript
- [ ] User-simulator actions
- [ ] Intermediate reasoning traces
- [ ] Execution logs
- [ ] Unit-test, patch, or verifier result
- [ ] Environment or simulator state
- [x] Leaderboard submission metadata
- [x] Raw output or audit trace under controlled access

Reviewer comments: Observable evidence includes final output grids, exact task correctness, optional pixel correctness, submission metadata, cost estimates, evaluation duration, model configuration, and individual task scores where ARC Prize publishes verified outputs or task-level results [S05, S06, S07, S08].

### 2.10 Input Stimulus Type

Select all that apply.

- [ ] Not explicitly stated
- [ ] Text
- [ ] Code
- [x] Tables or structured data
- [ ] Charts or figures
- [x] Images
- [ ] GUI screenshots
- [ ] Audio
- [ ] Video
- [ ] Documents
- [ ] PDF or document pages
- [ ] Web pages
- [ ] Terminal or filesystem state
- [ ] Long-context transcript or retrieved corpus
- [ ] APIs or tools
- [ ] Dynamic environment
- [ ] Simulation state
- [ ] External search results

Reviewer comments: Inputs are structured grid arrays. They can be rendered visually as colored-cell grids, but the underlying data are integer matrices [S02, S05].

### 2.11 Number of Items or Measurement Points

| Prompt                                                               | Response                                                                                                                                                                |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total number of scored items, tasks, episodes, or test cases         | 120 public evaluation tasks, 120 semi-private evaluation tasks, and 120 private evaluation tasks; public repository also includes 1,000 training tasks [S01, S02, S05]. |
| Total number of unscored examples, demonstrations, or training items | 1,000 public training tasks; each task includes demonstration input-output pairs [S02, S05].                                                                            |
| Total private or hidden items                                        | 120 semi-private and 120 private evaluation tasks are documented as non-public controlled sets [S01, S05, S06].                                                         |
| Development or example items                                         | Public training tasks are intended for training/prototyping and demonstrating the format, not as the primary evaluation set [S02, S05].                                 |
| Counts by task family, subdomain, language, modality, or difficulty  | No official public count by task family was identified; public, semi-private, and private evaluation splits are described as human-calibrated [S01, S04, S05].          |
| Counts by public, private, hidden, or controlled-access status       | 1,120 public tasks in GitHub; 240 controlled semi-private/private evaluation tasks; 1,360 total tasks described by changelog [S01, S02, S05].                           |
| Score aggregation unit                                               | Aggregate exact-match task success rate, often paired with cost/efficiency reporting [S04, S05, S07].                                                                   |

Reviewer comments: Public evaluation, semi-private, and private evaluation tasks were filtered so at least two humans solved each task within two attempts according to official materials [S01, S04, S05].

### 2.12 Mode of Evaluation

- [ ] Not indicated
- [x] Local batch evaluation
- [x] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [ ] Interactive agent evaluation
- [ ] Human-in-the-loop evaluation
- [ ] Continuous or rolling evaluation
- [ ] Benchmark suite or sub-leaderboard
- [x] Competition or challenge submission
- [ ] Third-party evaluator implementation
- [ ] Registry-hosted task pack

Degree of control over evaluated systems:

- [ ] No control over submitted systems
- [x] Some control over submitted systems
- [x] Controlled model access or audit
- [x] Controlled evaluation center or private harness
- [ ] Not documented

Reviewer comments: ARC-AGI-2 supports local public evaluation, hosted/controlled verification, and competition submission. The primary mode is automated exact scoring of structured grid outputs, with human baselines used for calibration and interpretation [S04, S05, S06, S08].

### 2.13 Technological Arrangements

| Requirement                            | Required | Optional |
| :------------------------------------- | :------: | :------: |
| API access                             |   [ ]    |   [x]    |
| Local inference                        |   [ ]    |   [x]    |
| GPU                                    |   [ ]    |   [x]    |
| CPU-only execution                     |   [x]    |   [ ]    |
| Docker or container                    |   [ ]    |   [x]    |
| Python package or CLI                  |   [x]    |   [ ]    |
| Browser                                |   [ ]    |   [x]    |
| External tools                         |   [ ]    |   [x]    |
| Internet access                        |   [ ]    |   [x]    |
| Proprietary platform                   |   [ ]    |   [x]    |
| Hosted scoring service                 |   [ ]    |   [x]    |
| Benchmark registry or task environment |   [ ]    |   [ ]    |
| Simulator or user simulator            |   [ ]    |   [ ]    |
| Filesystem, terminal, or sandbox state |   [ ]    |   [x]    |

Reviewer comments: Public use requires task JSON files and a way to generate and score output grids. ARC Prize provides an open benchmarking repository with multiple provider adapters, rate limiting, retries, configuration files, sample tasks, a random-baseline dry run, and a scoring script [S08]. Official competition/verification may use Kaggle notebooks and ARC Prize-controlled dataset substitution [S04, S06].

### 2.14 Time and Resource Requirements

| Requirement            | Response                                                                                                                                                   |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Per-item time limit    | No universal per-item AI time limit was identified in public materials.                                                                                    |
| Per-run time limit     | 2025 competition protocol described a 12-hour Kaggle wall-clock window for 240 hidden tasks [S04].                                                         |
| Human calibration time | Human calibration sessions were 90 minutes, with task attempts and times recorded [S04].                                                                   |
| Hardware               | 2025 competition protocol described four NVIDIA L4 GPUs for Kaggle execution [S04].                                                                        |
| Cost or compute budget | ARC Prize verification policy caps selected model evaluations at USD 10,000 per run and may report retail-cost estimates per test-pair attempt [S06, S07]. |
| Latency reporting      | Leaderboard/reporting surfaces include cost/efficiency framing; full latency reporting is not always public [S07].                                         |

Reviewer comments: Time and resource requirements vary by public local run, official verification, and competition route.

### 2.15 Benchmark Forms, Versions, and Variants

| Form, version, or variant | Purpose or use                                                                               | Reviewer comments                     |
| :------------------------ | :------------------------------------------------------------------------------------------- | :------------------------------------ |
| Public training           | Practice, development, and format demonstration                                              | 1,000 public tasks [S02, S05].        |
| Public evaluation         | Public testing and audit                                                                     | 120 public tasks [S01, S02, S05].     |
| Semi-private evaluation   | Live leaderboard and selected closed-source model testing as described by official materials | 120 controlled tasks [S01, S05, S06]. |
| Private evaluation        | Final competition standings as described by official materials                               | 120 controlled tasks [S01, S04, S05]. |
| ARC-AGI-1                 | Parent/source benchmark family context                                                       | Not the reviewed entity.              |
| ARC-AGI-3                 | Later benchmark family context                                                               | Not the reviewed entity.              |

Reviewer comments: The repository changelog documents public evaluation task corrections in April 2025 [S02].

### 2.16 Static or Dynamic Task Determination

Select all that apply.

- [x] Static fixed task set
- [ ] Random sample from fixed pool
- [x] Hidden test set selected by maintainers
- [ ] Procedurally generated tasks
- [ ] Adaptive routing based on performance
- [ ] Dynamic environment generation
- [ ] Rolling or periodically refreshed task set
- [ ] Contest-stream or recent-source capture
- [x] Versioned dataset slice
- [ ] Translated or localized form
- [ ] Stateful environment instance
- [ ] Not explicitly stated

Reviewer comments: ARC-AGI-2 is a static task set within each split as released. Public tasks are inspectable. Semi-private and private forms are controlled by ARC Prize / competition infrastructure and are not independently inspectable by ordinary users [S01, S02, S05, S06].

### 2.17 Evidence Sources Used in Scoring

Select all that apply.

- [x] Model final answer
- [ ] Model intermediate trace
- [ ] Tool-use trace
- [ ] Search, retrieval, or browser transcript
- [ ] Code execution result
- [ ] Environment state
- [ ] Simulator state or user-simulator actions
- [x] Reference answer
- [ ] Unit test
- [ ] Patch, verifier, or final-state check
- [ ] Coordinate, bounding target, or GUI target
- [ ] Document layout or structured extraction target
- [ ] Human judge
- [ ] Model judge
- [ ] Ensemble or panel adjudication
- [x] External verifier
- [x] Leaderboard submission metadata

Reviewer comments: Scoring uses reference output grids. Correct/incorrect scoring requires exact match in shape, colors/integers, and positions. Pixel correctness is described as an auxiliary indicator used by some teams, not the primary success rule [S02, S05, S08].

### 2.18 Broad-Claim Flags for Later Evaluation

| Prompt                                                        | Response                                                                                                                                                                                                                             |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Term used for broad interpretation from benchmark scores      | "Artificial General Intelligence," "general fluid intelligence," "human-like AI capabilities," "AGI progress," and "reasoning systems" appear in official materials [S01, S02, S03, S04].                                            |
| Score or output attached to the broad interpretation          | Aggregate exact-match ARC-AGI-2 task success, often paired with cost/efficiency reporting [S04, S07].                                                                                                                                |
| Capability domains from 2.1 explicitly invoked or implied     | On-the-spot reasoning, visual processing, working memory, and efficiency/speed; broader AGI language is also present [S01, S04].                                                                                                     |
| Capability domains from 2.1 explicitly excluded or not tested | Language, long-horizon agency, broad world knowledge, social reasoning, auditory processing, many memory forms, tool use, embodied interaction, and real-world task performance are not directly sampled by the reviewed grid tasks. |
| Stated AGI, autonomy, or agency caveats                       | ARC Prize policy states that ARC Prize benchmarks are designed to measure AI progress and are not a litmus test for AGI [S06].                                                                                                       |
| Documented broad-claim limits or non-use statements           | Partly documented in policy; not consistently foregrounded across all public reporting surfaces [S06, S07].                                                                                                                          |

Reviewer comments: Part B distinguishes score validity for ARC-style grid abstraction from standalone AGI or broad cognitive versatility claims [S12, S13].

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

Select scoring methods only. Do not describe the scoring pipeline in this subsection.

- [ ] Not explicitly stated
- [x] Automated exact-match scoring
- [ ] LLM equality-checker scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] String-similarity or edit-distance scoring
- [ ] Unit-test or execution-based scoring
- [ ] Patch, verifier, or final-state scoring
- [x] Rule-based scoring
- [ ] Coordinate or bounding-target scoring
- [ ] Document structure, layout, or OCR scoring
- [ ] State-based environment reward
- [ ] Simulator-verified task success
- [ ] Human rating
- [ ] Scoring by another model that evaluates outputs
- [x] Output parser or extractor that turns model responses into scoreable values
- [ ] Fuzzy, schema-aware, or admissible-variant parsing
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [x] Leaderboard service scoring
- [x] Multi-run or pass@k sampling policy
- [ ] Manual adjudication

Reviewer comments: The primary scoring procedure is exact-match task success. ARC Prize materials repeatedly use pass@2 language for human calibration and task inclusion [S01, S04, S05]. The public repository README contains a noted inconsistency: it describes two trials in the task success criterion and later says "3 trials" in the task file format section [S02]. This review treats pass@2 as the authoritative documented calibration and comparison rule because it is repeated across the official page, guide, and technical report.

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or scoring rule/quantity | Definition                                                                                                                                                                            | How item, task-family, or subscore results are combined                                                   | Capability-domain linkage stated by authors                                                                      | Interpretation stated by authors                                                                               |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| Primary score                  | Exact-match task accuracy / success rate. A task is solved when the test-taker produces the correct output grid for all test inputs, including dimensions and cell values [S02, S05]. | Solved tasks divided by evaluated tasks; aggregate score reported as percentage accuracy [S04, S05, S07]. | Abstract reasoning, problem solving, general fluid intelligence, and AGI-relevant reasoning language [S01, S04]. | Higher score indicates more ARC-AGI-2 grid tasks solved under the stated access/attempt/evaluation conditions. |
| Subscore                       | Public, semi-private, private, or task-level results where reported; no official task-family subscore found.                                                                          | Split-specific or task-level records where official reporting provides them [S06, S07].                   | Split comparison and leakage/comparability context.                                                              | Helps distinguish public, hidden, verified, or competition settings.                                           |
| Derived score                  | Cost / efficiency reporting, including cost per task or score/cost presentation where available [S01, S06, S07].                                                                      | Reported alongside score rather than as a single universal transformed score.                             | Efficiency/speed as reporting dimension.                                                                         | Designed to discourage brute-force or uneconomical search-style interpretations [S01, S07].                    |
| Qualitative band               | 85% hidden private evaluation threshold for Grand Prize; below 5% generally not treated as meaningful signal in the technical report [S04].                                           | Threshold applied to hidden private evaluation for competition context.                                   | Competition achievement / low-signal boundary.                                                                   | Operational competition threshold, not a formal AGI threshold.                                                 |

Treatment of responses that fail format, schema, refusal, completion, or parsing requirements, or are missing or refused: Exact output-grid matching requires scoreable grid outputs. Public sources do not provide a complete centralized malformed-output policy [S02, S05, S08].

Treatment of eligibility failures, API or tool blocks, timeouts, tool-call failures, environment crashes, malformed final states, duplicate submissions, and other run failures: Verification policy and competition rules cover selected routes; complete general failure handling is not centralized [S04, S06, S08].

Retry, repair, parser fallback, platform rerun, or manual adjudication policy for response-format or run-completion problems: Not fully documented in one public rulebook; this is carried into Part B as an evidence gap.

Reviewer comments: Pixel correctness is described as an auxiliary diagnostic measure, not the primary correctness criterion [S05].

### 3.3 Scale or Metric Types

Select all that apply.

- [ ] Raw score
- [x] Accuracy
- [x] Success rate
- [x] Pass rate or pass@k
- [ ] Unit-test pass rate
- [ ] Edit distance
- [ ] BLEU, METEOR, or text-similarity metric
- [ ] TEDS or structural similarity
- [ ] Sequence-matcher ratio
- [ ] Coordinate accuracy
- [ ] Win rate
- [ ] Elo or ranking score
- [ ] Pairwise preference score
- [ ] Reward or return
- [ ] Task-completion reward
- [ ] Final balance or accumulated return
- [ ] Delta or gain score
- [ ] Aggregated suite score
- [x] Cost-adjusted score
- [ ] Calibration or uncertainty score
- [ ] Percentile or normalized score
- [x] Threshold or decision index

Reviewer comments: Task accuracy is a proportion/percentage bounded by 0% and 100%. Cost is a ratio-style operational metric denominated in USD or cost per attempt/task when pricing information is available. Leaderboard placement is ordinal, but the core benchmark score is accuracy rather than Elo [S05, S06, S07].

### 3.4 Score Transformation

Select all that apply.

- [x] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against a reference point used to interpret scores
- [ ] Weighting across subdomains
- [ ] Weighting across capability domains
- [x] Formula for combining item, task-family, or subscore results documented
- [ ] Formula for combining item, task-family, or subscore results partially documented
- [ ] Formula for combining item, task-family, or subscore results not documented
- [x] Domain aggregation caveats documented
- [ ] Not applicable

Reviewer comments: The reviewed public materials describe aggregate accuracy as solved tasks divided by evaluated tasks. No psychometric scale transformation, normed score, item-response model, or confidence interval transformation was identified in public documentation [S04, S07].

### 3.5 Documented Reference Groups, Baselines, and Comparators

Select all that apply.

- [ ] No reference point or documented comparison group used to interpret scores
- [x] Expected performance from random guessing or trivial selection
- [x] Performance from human participants under documented conditions
- [ ] Performance from qualified domain experts
- [ ] Contest human population under source-instrument conditions
- [x] Professional annotator or expert validator
- [x] Performance from a reference model used to interpret scores
- [x] Previous model cohort
- [x] Commercial system used as a documented comparison point
- [x] Open-weight model used as a documented comparison point
- [ ] Domain-specific reference group
- [x] Public/private split comparator
- [ ] Suite component comparator
- [ ] Tool-enabled versus no-tool comparator

Reviewer comments: Human calibration, model baselines, public/private split context, and random-baseline sample support reference interpretation [S04, S08].

| Reference point or documented comparison group                    | Construction method                                                                                                                                                                                              | Intended score interpretation                                            |
| :---------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| Random guessing or trivial-selection reference point              | Benchmarking repository includes a random-baseline sample and scoring instructions [S08].                                                                                                                        | Floor/smoke-test context rather than meaningful chance model.            |
| Human-participant performance under documented conditions         | Technical report records 407 unique participants, 515 sessions, 1,848 unique task test pairs attempted, 13,405 total test-pair attempts, 8,277 solved test-pair attempts, and calibration/selection rules [S04]. | Human solvability and difficulty calibration.                            |
| Qualified domain-expert performance                               | No separate expert benchmark group identified.                                                                                                                                                                   | n/a                                                                      |
| Contest human population or source-instrument reference           | ARC Prize human testing; not a source contest human population.                                                                                                                                                  | Supports task inclusion and split calibration, not population norms.     |
| Documented group of models used for comparison                    | Technical report table lists selected model/system scores on ARC-AGI-1 and ARC-AGI-2 semi-private evaluation as of 2025-05-14 [S04].                                                                             | Relative model comparison under documented conditions.                   |
| Public/private split, suite-component, or tool/no-tool comparator | Public, semi-private, and private forms; split terminology varies across official sources [S01, S05, S06].                                                                                                       | Leakage/comparability context.                                           |
| Prior benchmark or version                                        | ARC-AGI-1 is used as historical context for saturation, brute-force susceptibility, leakage risk, and score comparison [S04].                                                                                    | Benchmark-family progress context.                                       |
| Score boundary or lower/upper reference point                     | 85% hidden private evaluation Grand Prize threshold; below 5% generally not treated as meaningful signal [S04].                                                                                                  | Operational threshold and low-score caution, not a formal AGI threshold. |

Reviewer comments: Public, semi-private, and private evaluation tasks were filtered so at least two humans solved each task within two attempts according to official materials [S01, S04, S05].

### 3.6 Score Uncertainty and Stability

This remains descriptive in Part A. Record whether uncertainty or similar scores across repeated evaluations under documented conditions are reported.

- [ ] Reported ranges expressing uncertainty around a score or comparison
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Hierarchical, clustered, or item-level bootstrap intervals
- [ ] Per-split or per-subscore confidence intervals
- [ ] Public/private split intervals
- [ ] Small-sample sensitivity
- [ ] Multiple runs or seeds
- [ ] Statistics on consistency across judges
- [ ] Evidence that human or expert scorers apply rubrics consistently
- [ ] Sensitivity analyses
- [ ] Score changes caused by prompt wording, small input changes, ordering, phrasing, format, or response schema
- [ ] IRT, adaptive testing, or item-parameter precision estimates
- [x] Not reported

Reviewer comments: Official materials state that public, semi-private, and private evaluation splits were calibrated to similar human-facing difficulty, with less than 1 percentage point difference expected or targeted across calibrated sets [S01, S04, S05]. The reviewed public sources do not provide full confidence intervals for model scores, split-equivalence uncertainty, prompt sensitivity studies, repeated-run variance, or standardized statistical tests for leaderboard rank differences.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

This remains descriptive in Part A. Record the documented link between scoring-rule behavior and interpretations made from benchmark scores.

| Prompt                                                                                  | Response                                                                                                                                                                   |
| :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why the primary rule or quantity used to convert model behavior into a score was chosen | Exact-match scoring follows directly from the task definition: the target behavior is to construct the correct grid [S02, S05].                                            |
| Whether lower or upper limits of the score rule are documented                          | Accuracy is bounded 0%-100%; 85% is the hidden private evaluation Grand Prize threshold; below 5% is generally treated as low signal by the report [S04].                  |
| Whether documentation identifies possible non-target rewarded behavior                  | ARC Prize argues that efficiency matters because brute-force search could solve tasks given enough resources and would not represent the intended intelligence [S01, S07]. |
| Whether parser, judge, or scorer validation is documented                               | Public scoring code and exact reference outputs are available for public tasks; formal parser validation for malformed outputs is not centralized [S02, S08].              |
| Whether response-format burden is separated from the target capability                  | Not fully separated. Exact grid serialization is part of scoreability and can affect LLM results.                                                                          |
| Whether score changes from small item or prompt changes affect the score interpretation | No systematic public prompt/item sensitivity study identified.                                                                                                             |
| Whether score uncertainty affects interpretation                                        | Split calibration is reported; score intervals and model-run uncertainty are not reported [S04].                                                                           |
| Whether score differences are interpreted statistically                                 | No confidence intervals or statistical comparison guidance identified in public leaderboard materials [S07].                                                               |
| Whether score or subscore interpretations are linked to capability domains from 2.1     | Official materials link scores to abstract reasoning and general-fluid-intelligence framing [S01, S04].                                                                    |
| Whether aggregate score interpretations preserve capability-domain caveats              | Policy states ARC Prize benchmarks are not a litmus test for AGI, but caveats are not equally prominent across all public surfaces [S06, S07].                             |
| Whether benchmark reports state what users should not infer                             | Policy says ARC Prize benchmarks are not a litmus test for AGI [S06].                                                                                                      |

Reviewer comments: The strongest documented score interpretation is performance on ARC-style exact-grid abstraction tasks under specified access, attempt, and compute conditions.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [x] Public leaderboard available
- [x] Public aggregate scores available
- [ ] Public capability-domain scores or profiles available
- [x] Public per-item scores available
- [x] Public model responses, traces, logs, judge rationales, or per-item data available
- [ ] Public traces or logs available
- [ ] Leaderboard snapshot or export available
- [x] Submission metadata available
- [x] Evaluation date or cohort labels available
- [x] Public/private split scores available
- [ ] Confidence intervals or error bars available
- [x] Raw submissions available under controlled access
- [ ] Retired-item or post-evaluation releases available
- [x] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

Reviewer comments: Public outputs include the official leaderboard, technical report, repository, guide, changelog, and benchmarking repository. Verified results may include outputs, evaluation durations, costs, and individual task scores when ARC Prize publishes them alongside verified model results [S06, S07, S08].

### 4.2 Output Name or Description

| Output                         | Description                                                                                                            | Public/private                                        | Maintainer, platform host, third-party evaluator, or leaderboard operator |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------ |
| ARC Prize leaderboard          | Aggregate ARC-AGI score, cost/efficiency framing, rank/positioning, and caveats for preview or incomplete tests [S07]. | Public surface; underlying hidden tasks controlled.   | ARC Prize                                                                 |
| Technical report tables        | Human calibration and selected model/system results [S04].                                                             | Public paper/report.                                  | ARC Prize / report authors                                                |
| Public local evaluation output | Scores generated by user-run scorer/harness on public tasks [S08].                                                     | User-generated public or private, depending on user.  | User / ARC Prize tooling                                                  |
| Verified output artifacts      | Verified outputs, durations, costs, and individual task scores where ARC Prize publishes them [S06].                   | Public or controlled depending on verification route. | ARC Prize                                                                 |

Reviewer comments: Primary output is ARC-AGI-2 accuracy / success rate. Supplementary outputs include cost/efficiency, rank, individual task scores where published, and optional pixel correctness diagnostics [S05, S06, S07, S08].

### 4.3 Output Design or Presentation

Select all that apply.

- [x] Static text report
- [x] Tables
- [x] Graphs or visualizations
- [x] Leaderboard
- [x] Interactive dashboard
- [ ] Downloadable CSV or JSON
- [ ] API output
- [x] Paper-only results

Reviewer comments: The official leaderboard presents systems in a cost/performance relationship, with notes about reasoning-system trend lines, base LLMs, Kaggle systems, preview results, incomplete testing, and cost caps [S07].

### 4.4 Output Structure

Select all that apply.

- [x] Aggregate-score based
- [ ] Capability-domain based
- [ ] Capability-domain profile based
- [ ] Task-family based
- [x] Criterion-threshold based
- [ ] Pairwise-comparison based
- [x] Rank based
- [x] Cost or efficiency adjusted
- [ ] Error-analysis based
- [x] Trace or process based
- [ ] Suite-aggregate based
- [x] Split or cohort based
- [x] Version-window based
- [ ] Environment-episode based
- [ ] Difficulty-band based

Reviewer comments: Outputs are structured as aggregate score, cost information, rank/positioning, and sometimes per-task details or raw outputs for verified results [S06, S07]. Public repository outputs for user-run evaluations are generated by the benchmarking/scoring scripts [S08].

### 4.5 Sensitivity to Context

Select one.

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [x] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts: public local evaluation, official verification, competition evaluation, public leaderboard display, technical report tables.

Reviewer comments: Scores can depend on model configuration, reasoning level, prompt, number of attempts, API pricing, compute budget, public versus hidden split, and whether a result is verified or self-reported [S06, S07, S08].

### 4.6 Development of Outputs

Select all that apply.

- [x] Based on benchmark authors' design
- [x] Based on empirical or actuarial relationships
- [x] Based on expert judgment
- [x] Based on human annotation
- [ ] Based on outputs scored by another model
- [x] Automatically generated by benchmark platform

Reviewer comments: Output design is tied to ARC Prize's stated objective of measuring both capability and efficiency. The reviewed sources document score/cost reporting, but do not provide a full formal reporting specification for every leaderboard field [S01, S06, S07].

Describe origin of report content: Report content derives from exact task scoring, human calibration, official verification/competition results, selected model evaluations, and ARC Prize leaderboard design [S04, S06, S07].

### 4.7 Modifiability

Select one.

- [ ] Not modifiable
- [x] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

Reviewer comments: Public users can run local evaluations and create their own reports using the public data and benchmarking repository. Official leaderboard and verification outputs are controlled by ARC Prize policies [S02, S06, S08].

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

Select one.

- [ ] Clear linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels
- [x] Partial linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Reviewer comments: The linkage from task to exact-match score is clear. The linkage from score to "abstract reasoning" is plausible and documented through task design and human calibration. The linkage from score to broad AGI or general intelligence is intentionally more limited and requires caution [S04, S06, S12, S13].

### 4.9 Output Content

Select all that apply.

- [x] Capability-domain descriptions or profiles
- [x] Aggregate rankings
- [ ] Subdomain comparisons
- [ ] Capability-domain coverage map
- [x] Excluded-domain caveats
- [x] Aggregate-score warnings
- [ ] Error categories
- [x] Examples of successes or failures
- [x] Cost, latency, or efficiency data
- [x] Process traces
- [x] Recommendations or interpretation notes
- [x] Warnings or caveats

Reviewer comments: Official reports include aggregate scores, model/system identifiers, cost and efficiency framing, human calibration results, selected model comparisons, and caveats for preview or incomplete testing [S04, S06, S07].

### 4.10 Intended Recipients

Select all that apply.

- [x] Benchmark maintainers
- [x] Model developers
- [x] AI researchers
- [x] Safety evaluators
- [x] Policy or governance actors
- [x] Product or deployment teams
- [ ] Procurement teams
- [x] Public audience

Reviewer comments: Recipients include AI researchers, ARC Prize participants, model providers, benchmark users, public leaderboard audiences, and stakeholders using AI benchmark results for capability tracking [S01, S03, S06, S07].

---

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

Select all that apply.

- [x] Technical report
- [x] User guide
- [x] Repository README
- [ ] API documentation
- [ ] Dataset card
- [x] Model submission instructions
- [x] Scoring documentation
- [ ] Rubric or annotation guide
- [x] Evaluation examples
- [ ] FAQ or discussion forum
- [x] Changelog or release notes

Reviewer comments: Available materials include the official benchmark page, technical report, guide, public repository, changelog, testing policy, leaderboard, and benchmarking repository [S01-S08]. Public documentation is substantial but distributed across several sources.

### 5.2 Distribution and Access Model

Select all that apply.

- [x] Fully public materials
- [x] Public materials with restricted answer keys or hidden tests
- [x] Controlled-access dataset or task host
- [x] Private or held-out evaluation service
- [ ] Hosted scoring service
- [x] Leaderboard-only submission route
- [ ] Benchmark registry or task-pack distribution
- [x] Competition or challenge distribution
- [x] Private maintainer-mediated distribution
- [ ] Retired or archived materials available
- [ ] Access model not documented

Reviewer comments: Public training and public evaluation tasks are fully public in GitHub. Semi-private and private sets are controlled and used for leaderboard/competition purposes. The public policy states that hidden sets are important for authoritative measurement without overfitting to known tasks [S01, S05, S06].

### 5.3 Methods of Publication

Select all that apply.

- [x] Academic paper
- [x] Benchmark website
- [x] Git repository
- [ ] Package registry
- [ ] Dataset hosting platform
- [x] Leaderboard platform
- [x] Hosted evaluation service
- [ ] Benchmark registry
- [x] Contest organizer source
- [x] Controlled-access data host
- [x] Downloadable documents
- [x] Private distribution

Reviewer comments: ARC-AGI-2 is published through the ARC Prize website, GitHub, arXiv, Kaggle competition infrastructure, and ARC Prize leaderboard surfaces [S01-S08].

### 5.4 User Requirements or Qualifications

Describe any requirements specified for running, submitting to, interpreting, or maintaining the benchmark.

| Requirement type                             | Requirement                                                                                                                                                                         |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Technical skill                              | Ability to manipulate JSON grid tasks, run scripts or use a harness, and interpret exact-match scores [S02, S05, S08].                                                              |
| Model access                                 | Public local solvers, API-hosted models, or selected verified models depending on route [S06, S08].                                                                                 |
| Dataset access                               | Public GitHub download for public tasks; controlled access for semi-private/private sets [S01, S02, S05, S06].                                                                      |
| Compute or budget                            | Public runs depend on solver; competition route described four NVIDIA L4 GPUs and 12-hour wall-clock; verification policy caps selected model evaluations at USD 10,000 [S04, S06]. |
| Tool/API credentials                         | Provider credentials may be needed for API-based harness runs or ARC Prize verification [S06, S08].                                                                                 |
| Hosted submission or leaderboard account     | ARC Prize/Kaggle routes and verification selection rules apply for official hidden-set evaluation [S04, S06].                                                                       |
| Human expertise                              | Benchmark users need technical and measurement literacy to avoid overinterpreting broad AGI claims. Human calibration used paid participants [S04].                                 |
| Account, license, or competition eligibility | Public repository uses Apache 2.0; official competition/verification requires compliance with ARC Prize/Kaggle policy [S02, S04, S06].                                              |
| Ethical, safety, or data-use obligations     | Public docs warn not to leak public evaluation tasks into algorithms; controlled hidden sets use data-retention and release restrictions [S02, S05, S06].                           |

Reviewer comments: Public users need technical ability to manipulate JSON grid tasks or use the task viewer/harness. Official verification requires satisfying ARC Prize selection criteria, submission rules, and possibly open-source requirements, Kaggle notebook execution, API key provision, and cost/runtime constraints [S05, S06, S08].

### 5.5 Dataset and Item Access

| Component                                      | Public | Restricted | Hidden | Not available |
| :--------------------------------------------- | :----: | :--------: | :----: | :-----------: |
| Training or development items                  |  [x]   |    [ ]     |  [ ]   |      [ ]      |
| Public evaluation items                        |  [x]   |    [ ]     |  [ ]   |      [ ]      |
| Private or held-out evaluation items           |  [ ]   |    [x]     |  [x]   |      [ ]      |
| Secret, encrypted, or reserve evaluation items |  [ ]   |    [x]     |  [x]   |      [ ]      |
| Private leaderboard set                        |  [ ]   |    [x]     |  [x]   |      [ ]      |
| Retired or archived evaluation items           |  [ ]   |    [ ]     |  [ ]   |      [x]      |
| Answer keys or reference solutions             |  [x]   |    [x]     |  [x]   |      [ ]      |
| Metadata or annotations                        |  [x]   |    [ ]     |  [ ]   |      [ ]      |
| Human annotations or verification labels       |  [ ]   |    [ ]     |  [ ]   |      [x]      |
| Raw model outputs or logs                      |  [x]   |    [x]     |  [ ]   |      [ ]      |
| Model submissions and traces                   |  [x]   |    [x]     |  [ ]   |      [ ]      |
| Hosted scoring service                         |  [ ]   |    [x]     |  [ ]   |      [ ]      |
| Simulator or environment state                 |  [ ]   |    [ ]     |  [ ]   |      [x]      |
| Task registry entry                            |  [ ]   |    [ ]     |  [ ]   |      [x]      |
| Tool/API credentials or configuration          |  [ ]   |    [x]     |  [ ]   |      [ ]      |

Reviewer comments: Public items and answers are inspectable for the public splits. Semi-private and private task items/answers are not inspectable by ordinary users. This supports benchmark integrity but limits independent auditability of hidden forms [S01, S02, S05, S06]. The reviewed official sources are not perfectly uniform in split terminology for leaderboard use: the ARC-AGI-2 page and policy describe semi-private leaderboard/model testing, while the guide also uses private-set wording for the leaderboard [S01, S05, S06].

### 5.6 Provenance and Contamination Documentation

| Topic                                                                        | Documented | Partially documented | Not documented |
| :--------------------------------------------------------------------------- | :--------: | :------------------: | :------------: |
| Data origin or task creation                                                 |    [x]     |         [ ]          |      [ ]       |
| Source-material release date                                                 |    [x]     |         [ ]          |      [ ]       |
| Contest or problem-source timing                                             |    [x]     |         [ ]          |      [ ]       |
| Persistent dataset or benchmark-material identifier                          |    [x]     |         [ ]          |      [ ]       |
| Author or contributor qualifications                                         |    [ ]     |         [x]          |      [ ]       |
| Deduplication or overlap checks                                              |    [x]     |         [ ]          |      [ ]       |
| Rationale for public items and hidden or restricted evaluation items         |    [x]     |         [ ]          |      [ ]       |
| Screening for prior model exposure to benchmark items, answers, or sources   |    [ ]     |         [x]          |      [ ]       |
| Canary strings or training-data warnings                                     |    [ ]     |         [ ]          |      [x]       |
| Diagnostic task for performance driven by prior exposure to items or answers |    [ ]     |         [ ]          |      [x]       |
| Pre-exposure or source-material searchability checks                         |    [ ]     |         [x]          |      [ ]       |
| Public-source searchability                                                  |    [ ]     |         [x]          |      [ ]       |
| Post-release contamination risk                                              |    [ ]     |         [x]          |      [ ]       |
| Training-use prohibition                                                     |    [x]     |         [ ]          |      [ ]       |
| Private-set owner                                                            |    [x]     |         [ ]          |      [ ]       |
| Leak response policy                                                         |    [ ]     |         [x]          |      [ ]       |
| Rerun or replacement trigger                                                 |    [ ]     |         [x]          |      [ ]       |
| Hash commitments, signatures, or tamper-evident audit logs                   |    [ ]     |         [ ]          |      [x]       |
| Encrypted, secret, or controlled-release item reserve                        |    [ ]     |         [x]          |      [ ]       |
| Rules for updating, rotating, replacing, or adding benchmark items over time |    [ ]     |         [x]          |      [ ]       |
| Reporting of known unintended disclosures or deprecated/archived items       |    [x]     |         [ ]          |      [ ]       |

Reviewer comments: Official materials state that candidate tasks came from newly authored ARC Prize Foundation/staff/partner tasks and previously unused reserves, excluding ARC-AGI-1 public training tasks from human testing [S04]. The technical report describes redundancy detection and preference for newly authored tasks in private sets [S04]. Public materials also warn users not to leak public evaluation tasks into algorithms during development [S02, S05]. The full provenance of every private/semi-private task and detailed contamination audits are not publicly inspectable.

### 5.7 Reproducibility Materials

Select all that apply.

- [x] Complete task data
- [ ] Complete prompt templates
- [x] Code or platform that administers tasks, collects outputs, and often runs scoring
- [x] Scoring code
- [x] Environment file or dependency list
- [ ] Container or reproducible environment
- [ ] Container image
- [ ] Task environment registry
- [ ] Simulator or user simulator version
- [x] Evaluation adapter
- [ ] Judge model and prompt version
- [ ] Version pinning
- [ ] Random seeds or deterministic settings
- [x] Model responses, traces, logs, judge rationales, or per-item data
- [ ] Reproduction script for published results
- [x] Push-button replication script or single documented command
- [x] Expected-output fixtures or smoke-test example
- [x] Scorer fixtures
- [x] Known-good baseline run
- [x] Task-level expected outputs
- [ ] Continuous integration or test suite
- [ ] Public build status or equivalent passing-test signal

Reviewer comments: Public reproduction is supported by public task data, file-format documentation, open benchmarking code, scorer scripts, sample tasks, provider adapters, and configuration files [S02, S05, S08]. Reproduction of semi-private/private official scores depends on ARC Prize-controlled data and verification policy [S06].

### 5.8 Maintenance and Versioning

| Topic                                                                                               | Response                                                                                                                              |
| :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Maintainer identity                                                                                 | ARC Prize / `arcprize` GitHub organization [S02, S08].                                                                                |
| Private or held-out set owner                                                                       | ARC Prize / competition infrastructure, based on policy and guide [S05, S06].                                                         |
| Leaderboard operator                                                                                | ARC Prize [S07].                                                                                                                      |
| Submission eligibility rules                                                                        | Verification policy states valid submission types, selection rules, public model testing, community submissions, and cost caps [S06]. |
| Rerun policy                                                                                        | Partly documented in verification policy; no complete general rerun policy identified [S06].                                          |
| Stale-score policy                                                                                  | Not fully documented; leaderboard caveats distinguish preview and incomplete testing [S07].                                           |
| Model-version update policy                                                                         | Model identity and version labels appear in leaderboard/policy contexts, but full update policy is not centralized [S06, S07].        |
| Scorer, judge, parser, or harness versioning                                                        | Public repositories available; no pinned scorer/harness release selected in this review [S02, S08].                                   |
| Cohort or evaluation-window labels                                                                  | Technical report gives 2025-05-14 model score context; leaderboard is live/current [S04, S07].                                        |
| Public/private score aggregation policy                                                             | Split use is documented but terminology is not fully harmonized across official sources [S01, S05, S06].                              |
| Retirement and archival policy                                                                      | No comprehensive retirement policy identified.                                                                                        |
| Documented release names, tags, changes, and score-comparability implications                       | Repository changelog records initial release and public evaluation corrections [S02].                                                 |
| Changelog or update record                                                                          | ARC-AGI-2 repository `changelog.md` [S02].                                                                                            |
| Issue or feedback process                                                                           | GitHub issue channels and ARC Prize contact/policy routes where available [S02, S06, S08].                                            |
| Item correction process                                                                             | Public evaluation corrections are documented in changelog; full process not centralized [S02].                                        |
| Deprecated item handling                                                                            | Not fully documented.                                                                                                                 |
| Rules for updating, rotating, replacing, or adding hidden evaluation items over time                | Not fully documented.                                                                                                                 |
| Last code-usability or harness health check                                                         | This review inspected public docs and harness availability on 2026-05-17; no automated health check was run.                          |
| Build, CI, or smoke-test status                                                                     | Public smoke-test/sample baseline materials exist; no CI status was used in this review [S08].                                        |
| Score-ceiling threshold or criteria for deprecating, archiving, or ending use                       | Grand Prize threshold documented; no full benchmark retirement/saturation policy found [S04].                                         |
| Policy for deprecating, archiving, or ending use of items, versions, leaderboards, or the benchmark | Not fully documented.                                                                                                                 |
| Retired-item publication or audit policy                                                            | Not identified.                                                                                                                       |
| Score comparability across versions                                                                 | ARC-AGI-1 and ARC-AGI-2 comparison is documented qualitatively, but formal cross-version equating is limited [S04].                   |
| Policy for comparing scores across dates, cohorts, refreshes, or rolling windows                    | Not fully documented.                                                                                                                 |
| Long-term archival plan                                                                             | GitHub and arXiv provide public access; no additional preservation plan identified [S02, S04].                                        |

Reviewer comments: Repository changelog records initial release on 2025-03-24 and public evaluation corrections on 2025-04-14 and 2025-04-17 [S02]. Public docs indicate continued leaderboard/testing policy maintenance in 2026 [S06, S07].

---

## Appendix A. General Description of the Benchmark

Write a concise descriptive summary of the benchmark for readers who have not inspected the materials. Keep this descriptive and defer evaluation to Part B.

Free Text:

ARC-AGI-2 is a structured grid-transformation benchmark in the ARC-AGI family. Each task gives a small number of demonstration input-output grids and asks the evaluated system to infer the underlying rule and produce exact output grid(s) for unseen test input(s). The public ARC-AGI-2 release contains 1,000 training tasks and 120 public evaluation tasks, with additional 120-task semi-private and private evaluation sets used for controlled leaderboard and competition purposes. ARC Prize positions the benchmark as a harder successor to ARC-AGI-1, designed to challenge current reasoning systems, reduce brute-force susceptibility, improve human calibration, and report both performance and efficiency. The strongest descriptive score interpretation is performance on ARC-style exact-grid abstraction tasks under specified access, attempt, and compute conditions.

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether the benchmark is adequate as a measurement instrument for its intended use.

## Information Sources

Information sources used for Part B are listed in the Source Registry. Official ARC Prize materials [S01-S08] provide the benchmark facts. Local MESA criteria, BetterBench, Measuring what Matters, and AGI/CHC literature [S10-S13] provide evaluative framing. Missing documentation is treated as missing evidence, not proof of poor benchmark quality.

## Explanation of Ratings

Ratings use the MESA/EFPA-style scale: `n/a`, `0`, `1`, `2`, `3`, `4`, where `2` means adequate for cautious use, `3` means good support with limited gaps, and `4` means comprehensive support.

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

Ratings below are based on intended score meaning, not mechanical averaging. For ARC-AGI-2, the narrow interpretation is ARC-style exact-grid abstraction under specified conditions; broad AGI/general-intelligence interpretation requires stronger evidence across broader capability domains [S12, S13].

## Section 6. Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition

- Excellent: The benchmark gives a clear, theoretically grounded account of the real capability, behavior, or quality of interest, explains why the benchmark was constructed, defines boundaries and exclusions for what is being measured, identifies whether the phenomenon is contested or composite, maps broad claims to relevant capability domains where applicable, and distinguishes the target capability from adjacent or broader score interpretations.
- Rating: 3
- Evidence: Official materials define ARC-AGI-2 around abstract reasoning, problem solving, fluid intelligence, minimal prior knowledge, and grid-rule generalization [S01, S03, S04].
- Missing evidence: The boundary between ARC-style abstraction and broad AGI/general intelligence is not fully formalized.
- Reviewer rationale: Strong for a targeted ARC-style reasoning construct; weaker for broad intelligence claims.
- Interpretation caution: Do not treat ARC-AGI-2 score alone as evidence of overall AGI.

---

#### 6.1.2 Summary of prior research and benchmark context

- Excellent: The benchmark documentation situates the benchmark in relevant research and prior evaluations, explains what gap it addresses, and identifies how prior findings, benchmark failures, or measurement limitations informed the design.
- Rating: 3
- Evidence: Technical report situates ARC-AGI-2 against ARC-AGI-1, prior competitions, brute-force susceptibility, human-baseline limitations, and leakage risk [S04].
- Missing evidence: Broader psychometric and external validation literature is not deeply integrated into the official argument.
- Reviewer rationale: Clear benchmark-family rationale and update motivation.
- Interpretation caution: Historical ARC-AGI context is not a substitute for external validity evidence.

---

#### 6.1.3 Phenomenon-task-metric-claim chain

- Excellent: The documentation explicitly links the real capability or behavior being measured to task design, response requirements, the rule or quantity used to convert behavior into a score, any claimed capability-domain mapping, the method for combining scores, and the intended score meaning, with plausible confounds, non-target tactics, formatting effects, parser effects, prior exposure to items or answers, sensitivity to small item changes, and benchmark-specific tuning considered.
- Rating: 2
- Evidence: Task format and exact scoring are clearly linked to grid-rule inference [S02, S04, S05].
- Missing evidence: Confounds such as serialization burden, prompt sensitivity, model-specific tool use, and broad score interpretation are not fully resolved.
- Reviewer rationale: Adequate for cautious use; chain is strongest from task to exact score, weaker from score to broad capability.
- Interpretation caution: Claims should be phrased as ARC-style abstraction performance, not general intelligence.

---

#### 6.1.4 Task or item design

- Excellent: Task formats, item types, forms of model output, difficulty range, scoring protocols, time or tool constraints, and score-combination choices are clearly justified as appropriate for the stated measurement aims and intended AI systems.
- Rating: 3
- Evidence: Technical report describes design goals: same ARC format, less brute-forcible tasks, first-party human testing, wider signal bandwidth, calibrated difficulty [S04].
- Missing evidence: Full task-authoring rubrics and complete item-level design logs are not public.
- Reviewer rationale: Design account is clear and relevant to the intended benchmark family.
- Interpretation caution: Hidden-set item quality cannot be independently inspected by ordinary users.

---

#### 6.1.5 Procedures for developing task or item content

- Excellent: Content development used relevant domain expertise, benchmark design expertise, qualitative review, clear inclusion and exclusion criteria, documented sampling or sourcing procedures, and task-quality checks to ensure task content represents the intended capability space.
- Rating: 3
- Evidence: Candidate task sources, human testing, redundancy detection, final validation, and internal/external review are documented [S04].
- Missing evidence: Detailed provenance per task and complete reviewer records are not public.
- Reviewer rationale: Good task-development documentation relative to many AI benchmarks.
- Interpretation caution: Private task provenance remains trust-mediated.

---

#### 6.1.6 Thoroughness of the final task or item selection process

- Excellent: The final task or item pool is justified through documented selection decisions, a defensible sampling strategy such as random, stratified, criterion, targeted, or well-justified mixed sampling, review evidence, pilot results where available, coverage analysis, removal of unsuitable items, and explanation of tradeoffs between breadth, depth, difficulty, and feasibility. Convenience sampling is not automatically disqualifying when its limits are explicit and score interpretations are narrow.
- Rating: 3
- Evidence: Inclusion required human solvability, split calibration, redundancy review, and final validation [S04].
- Missing evidence: Exact sampling frame and all rejected-task statistics are not fully available.
- Reviewer rationale: Selection process is traceable and defensible for ARC-style tasks.
- Interpretation caution: Calibration evidence should not be generalized beyond the selected task family.

---

#### 6.1.7 Quantitative evidence of task or item quality

- Excellent: Quantitative item or task evidence is reported where appropriate, such as difficulty, discrimination, ceiling and floor effects, domain coverage, inter-item redundancy, scorer behavior, model cohort performance, human or expert performance, or other benchmark-relevant indicators.
- Rating: 3
- Evidence: Human testing reports participants, sessions, attempts, solve rates, median times, split calibration, and model baseline scores [S04].
- Missing evidence: Public item-level psychometric tables, confidence intervals, and discrimination indices are not supplied in full.
- Reviewer rationale: Good first-party quantitative evidence for difficulty and solvability.
- Interpretation caution: Public aggregate statistics do not fully expose hidden-set item behavior.

---

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice

- Excellent: Any adaptation, translation, source-instrument reuse, domain transfer, dataset reuse, synthetic data generation, benchmark refresh, derived entity, hosted implementation, or benchmark slice follows a documented process with expert review, source-limit analysis, equivalence checks, cultural or domain considerations where relevant, and clear limits on comparability with parent benchmarks or prior versions.
- Rating: 3
- Evidence: ARC-AGI-2 explicitly updates ARC-AGI-1 while preserving format and addressing stated limitations [S04, S05].
- Missing evidence: Formal equivalence testing against ARC-AGI-1 is limited; some public training content combines ARC-AGI-1 and new tasks [S02].
- Reviewer rationale: Version relationship is documented and purposeful.
- Interpretation caution: Direct ARC-AGI-1 versus ARC-AGI-2 score comparison needs caveats.

---

#### 6.1.9 Overall Rationale, development, and task or item quality

- Excellent: Reviewer judgment, based on items 6.1.1-6.1.8, supports the conclusion that the benchmark rationale, definition of what is being measured, development process, and task or item quality are comprehensive and fit for the intended score meaning. Do not mechanically average ratings.
- Rating: 3
- Evidence: Strong official rationale, documented human calibration, task selection, and public release [S01-S05].
- Missing evidence: Broad-claim formalization and hidden-set auditability are incomplete.
- Reviewer rationale: Good for a narrow ARC-style reasoning benchmark; not comprehensive for AGI.
- Interpretation caution: Use as one capability signal in a broader portfolio.

---

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- Excellent: Documentation clearly explains what capability or quality the reviewed entity is designed to measure, what it is not designed to measure, any capability-domain coverage or exclusions when broad claims are made, its relationship to any parent or source benchmark, intended users, intended AI systems, suitable use cases, and explicit uses that should not be supported.
- Rating: 3
- Evidence: Official pages and report state goals and intended use for AI reasoning progress and competition [S01, S03, S04].
- Missing evidence: Non-use cases are present mainly in policy language, not consolidated in the benchmark page.
- Reviewer rationale: Purpose is clear for benchmark users.
- Interpretation caution: Public marketing language may still invite overbroad readings.

---

#### 6.2.2 Documentation of development process

- Excellent: Documentation gives full details of data or item sources, sampling method, task construction, filtering, review, piloting, scoring design, reused-dataset limitations, changes during development, and reasons for major design decisions.
- Rating: 3
- Evidence: Technical report explains human testing, task inclusion, calibration, redundancy detection, and validation [S04].
- Missing evidence: Full item-level records are not public.
- Reviewer rationale: Development process is unusually well documented.
- Interpretation caution: Hidden forms require trust in maintainers.

---

#### 6.2.3 Documentation of scoring and metrics

- Excellent: Documentation clearly explains output parsing, scoring rules, definitions of the quantities used to convert behavior into scores, how item or subscore results are combined, treatment of outputs that fail format, schema, refusal, completion, or parsing requirements, tie handling, uncertainty reporting, and how scores should be interpreted.
- Rating: 2
- Evidence: Guide, README, and harness document exact scoring and pixel correctness [S02, S05, S08].
- Missing evidence: README contains a trial-count inconsistency; complete malformed-output policy is not centralized.
- Reviewer rationale: Scoring is understandable, but procedural edge cases need tightening.
- Interpretation caution: Trial count and output-format errors should be standardized before high-stakes comparison.

---

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- Excellent: Documentation clearly explains how score stability, run variance, scorer or judge agreement, parser handling of valid and malformed responses, sensitivity to prompt wording or small item changes, form or version equivalence, and statistical uncertainty were assessed and how these affect interpretation.
- Rating: 1
- Evidence: Split calibration and human testing are described [S01, S04].
- Missing evidence: Model-score confidence intervals, rerun variance, prompt sensitivity, and uncertainty for rank differences are not public.
- Reviewer rationale: Reliability evidence is limited beyond deterministic scoring and calibration.
- Interpretation caution: Close leaderboard differences should not be overinterpreted.

---

#### 6.2.5 Documentation of validity evidence

- Excellent: Documentation presents a clear validity argument for the intended score meanings, including content support, task representativeness, evidence that scoring rewards the target capability, support for any claimed capability-domain interpretations, relations with other evidence, controls for prior model exposure to benchmark items or answers, and limits of inference.
- Rating: 2
- Evidence: Official report gives a design argument and human/model contrast [S04].
- Missing evidence: External convergent/discriminant validation and broad AGI validation are limited.
- Reviewer rationale: Adequate for cautious ARC-task validity, not for broad AGI validity.
- Interpretation caution: Strong model performance would need broader evidence to support broad cognitive claims.

---

#### 6.2.6 Documentation of fair use and comparability

- Excellent: Documentation describes fairness, accessibility, language or domain coverage, cross-system comparability, evaluation-condition comparability, and any restrictions needed to interpret results responsibly.
- Rating: 2
- Evidence: Policy documents verification types, hidden-set rationale, cost caps, and submission rules [S06].
- Missing evidence: Comparability across API/local models, reasoning settings, and compute environments remains partly policy-mediated.
- Reviewer rationale: Adequate but not complete.
- Interpretation caution: Verified, community, and self-reported scores should not be mixed without labels.

---

#### 6.2.7 Documentation of maintenance and versioning

- Excellent: Documentation provides version history, changelog, release rules, refresh policy, deprecation or retirement policy, saturation or archival criteria where relevant, data or task updates, leaderboard operator identity, private split ownership, scorer or judge changes, stale-score policy, leaderboard update practices, and clear guidance on comparability across versions or temporal cohorts.
- Rating: 2
- Evidence: Changelog documents release and public evaluation corrections [S02].
- Missing evidence: No comprehensive long-term replacement/deprecation policy found.
- Reviewer rationale: Basic maintenance is visible.
- Interpretation caution: Historical scores may be affected by public task corrections.

---

#### 6.2.8 Adequacy of documentation available to users

- Excellent: Reviewer judgment, based on items 6.2.1-6.2.7, supports the conclusion that documentation is comprehensive, current, traceable, and sufficient for qualified users to run, inspect, score, and interpret the benchmark responsibly. Do not mechanically average ratings.
- Rating: 3
- Evidence: Multiple official sources cover purpose, tasks, scoring, access, policy, and harness [S01-S08].
- Missing evidence: Information is distributed and some policies are incomplete or inconsistent.
- Reviewer rationale: Good documentation overall, with important gaps for high-stakes or broad interpretation.
- Interpretation caution: Users should cite exact source, split, date, and verification status.

---

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- Excellent: Step-by-step setup and administration instructions are complete, reproducible, and include required environment, dependencies, credentials, compute assumptions, seeds, sampling settings, tool permissions, hosted submission procedures, controlled private evaluation routes, registry task execution, environment setup, smoke-test or replication commands where relevant, and handling of expected failures.
- Rating: 3
- Evidence: Guide and benchmarking README provide download, data, CLI, adapter, and scoring instructions [S05, S08].
- Missing evidence: No single frozen evaluation package is specified for all official scores.
- Reviewer rationale: Clear enough for qualified public users.
- Interpretation caution: Reproduction should pin repository commits and config versions.

---

#### 6.3.2 Scoring procedure and error handling

- Excellent: Scoring instructions are clear and include checks for parser failures, malformed outputs, format retries or repairs, judge failures, missing responses, duplicate submissions, manual overrides, and audit trails for any corrections.
- Rating: 2
- Evidence: Exact matching and remaining-task incorrect policy are documented [S05, S07, S08].
- Missing evidence: Malformed outputs, retries, parser failures, and trial-count discrepancy need a consolidated rulebook.
- Reviewer rationale: Adequate but edge cases matter.
- Interpretation caution: Parser or formatting burden can affect score.

---

#### 6.3.3 Interpretation and reporting guidance

- Excellent: Users receive detailed guidance on interpreting aggregate scores, subscores, uncertainty, comparisons against reference points, version differences, upper or lower reference-point effects, and common risks of interpreting beyond what evidence supports.
- Rating: 2
- Evidence: Leaderboard notes and policy include preview, incomplete-output, cost, and verification caveats [S06, S07].
- Missing evidence: The official benchmark page does not fully consolidate score-interpretation limits.
- Reviewer rationale: Some guidance is present but fragmented.
- Interpretation caution: Public users may miss caveats unless they read policy and leaderboard notes.

---

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- Excellent: The benchmark clearly states system prerequisites, access requirements, tool-use assumptions, modality requirements, unsupported system classes, prohibited uses, and the consequences of violating prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules.
- Rating: 3
- Evidence: Policy states valid submission types, open-source conditions, Kaggle run requirements, cost caps, and verification discretion [S06].
- Missing evidence: Criteria are partly discretionary and subject to change.
- Reviewer rationale: Good operational guidance for official verification.
- Interpretation caution: Discretionary verification limits general comparability.

---

#### 6.3.5 Technical support and implementation guidance

- Excellent: Technical instructions cover software and hardware requirements, known failure modes, troubleshooting, test runs, expected outputs, dependency versions, issue-reporting channels, and support for reproducibility.
- Rating: 3
- Evidence: Public harness, issues, examples, sample runs, and provider adapters are available [S02, S08].
- Missing evidence: Support commitments and release cadence are not formalized.
- Reviewer rationale: Good practical implementation support.
- Interpretation caution: Community results may diverge from official settings.

---

#### 6.3.6 References and supporting materials

- Excellent: Documentation provides source-linked references to benchmark papers, datasets, task sources, code repositories, validation materials, related benchmarks, and supporting literature needed for informed review.
- Rating: 3
- Evidence: Report, guide, code, policy, and leaderboard are cross-linked [S01-S08].
- Missing evidence: Bibliographic and procedural details are not always centralized.
- Reviewer rationale: Strong source ecosystem.
- Interpretation caution: Reviewers should check multiple sources.

---

#### 6.3.7 Quality of procedural instructions

- Excellent: Reviewer judgment, based on items 6.3.1-6.3.6, supports the conclusion that procedural instructions are complete, reproducible, and sufficient for qualified users to run and interpret the benchmark without hidden procedural knowledge. Do not mechanically average ratings.
- Rating: 2
- Evidence: Usable instructions exist across guide, repo, harness, and policy [S02, S05, S06, S08].
- Missing evidence: Scoring edge cases, trial count, and hidden-set procedures remain partly fragmented.
- Reviewer rationale: Adequate for cautious qualified use.
- Interpretation caution: Do not assume independently run public scores are official leaderboard equivalents.

---

### 6.4 Overall Adequacy of Rationale and Documentation

- This overall rating is based on reviewer judgment across sub-sections 6.1, 6.2, and 6.3. Do not mechanically average ratings.
- Excellent: The benchmark provides a comprehensive, source-grounded rationale, a defensible development account, strong task or item quality evidence, complete documentation, and procedural instructions sufficient for responsible qualified use.
- Rating: 3

Reviewer comments: ARC-AGI-2 has clear official rationale, unusually detailed human calibration, public data, visible scoring logic, and a maintained policy ecosystem. The rating is not higher because broad intelligence interpretation, trial-count consistency, hidden-set auditability, uncertainty reporting, and long-term versioning/deprecation policy remain incomplete.

---

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability

- Excellent: The dataset, task set, environment, registry entry, hosted evaluation service, private evaluation route, or controlled audit route is complete, versioned, licensed where applicable, clearly linked, and available in a form that supports independent inspection or justified controlled access.
- Rating: 3
- Evidence: Public training and evaluation tasks are available in GitHub under Apache 2.0; hidden sets are documented but controlled [S02, S05].
- Missing evidence: Semi-private/private tasks cannot be independently inspected.
- Reviewer rationale: Strong public availability with justified controlled forms.
- Interpretation caution: Hidden-set quality is not fully auditable.

---

#### 7.1.2 Prompts, instructions, and input materials

- Excellent: Prompts, task instructions, examples, system messages, input files, context windows, multimodal assets, GUI screenshot assets, video assets, document images or PDFs, layout annotations, filesystem or simulator state, and any hidden or private instructions are documented or controlled in a way that supports reproducible evaluation and fair interpretation.
- Rating: 3
- Evidence: Task JSON schema and viewer guidance are documented [S02, S05].
- Missing evidence: Official prompt templates for all leaderboard model evaluations are not fully centralized.
- Reviewer rationale: Core input artifacts are clear.
- Interpretation caution: LLM prompt choices can affect scores.

---

#### 7.1.3 Rubrics, reference answers, and response format requirements

- Excellent: Rubrics, answer keys, reference outputs, response schemas, parsing rules, admissible variants, retry or repair rules, and invalid-response handling are clear, versioned, tested where relevant, and appropriate for the capability or quality being measured.
- Rating: 3
- Evidence: Reference answers exist for public tasks; exact grid correctness is documented [S02, S05].
- Missing evidence: Hidden reference answers are not public; README trial inconsistency remains.
- Reviewer rationale: Primary rubric is objective and inspectable for public tasks.
- Interpretation caution: Exact-match objective scoring still requires parser and format discipline.

---

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- Excellent: The harness, hosted scorer, task environment, simulator or user simulator, and scoring tools are runnable or auditable through a documented route, tested, robust to common errors and malformed outputs, version-pinned where needed, covered by smoke tests or CI/build status where relevant, and include a replication script or examples that reproduce expected outputs.
- Rating: 3
- Evidence: Open benchmarking repo provides adapters, CLI, scoring, sample tasks, config, and random baseline [S08].
- Missing evidence: No pinned official release was used in this review; all leaderboard settings may not be reproducible from public defaults.
- Reviewer rationale: Good implementation infrastructure.
- Interpretation caution: Pin versions before comparing scores.

---

#### 7.1.5 Interface and workflow usability

- Excellent: The benchmark workflow is easy for intended users to understand and operate, with clear command paths, expected inputs and outputs, progress or failure signals, and no hidden procedural steps.
- Rating: 3
- Evidence: Task viewer, repository, and benchmark harness support public use [S05, S08].
- Missing evidence: Usability for nontechnical users depends on separate viewers and docs.
- Reviewer rationale: Usable for technical benchmark users.
- Interpretation caution: Manual task viewing can contaminate public evaluation development.

---

#### 7.1.6 Accessibility across modalities, languages, and system types

- Excellent: Benchmark materials and workflows are usable by design for relevant modalities, languages, deployment modes, API or local systems, and assistive or alternate interaction needs, with justified adaptations when usability is limited.
- Rating: 2
- Evidence: JSON grids make the task accessible to text/structured-data and visual-grid systems [S02, S05].
- Missing evidence: Accessibility for systems with different I/O constraints, non-grid-native agents, and API format limits is not fully analyzed.
- Reviewer rationale: Adequate but domain-specific.
- Interpretation caution: Performance may reflect grid serialization and interface adaptation, not only reasoning.

---

#### 7.1.7 Licensing, use requirements, and risk warnings

- Excellent: Licenses, terms of use, redistribution limits, privacy constraints, sensitive-content warnings, safety restrictions, and required user qualifications are explicit and compatible with the benchmark's intended use.
- Rating: 3
- Evidence: Public data license is Apache 2.0; policy and guide warn about leakage and verification requirements [S02, S05, S06].
- Missing evidence: Hidden-set terms and competition-specific restrictions are spread across policy/competition infrastructure.
- Reviewer rationale: Good public terms and warnings.
- Interpretation caution: Always distinguish public, semi-private, private, verified, and competition results.

---

#### 7.1.8 Overall quality of benchmark materials

- Excellent: Reviewer judgment, based on items 7.1.1-7.1.7, supports the conclusion that benchmark materials are complete, usable, accessible, reproducible, and appropriate for the intended evaluation. Do not mechanically average ratings.
- Rating: 3
- Evidence: Public data, guide, scorer, harness, policy, and leaderboard are available [S01-S08].
- Missing evidence: Hidden-set access and full official-run reproducibility are limited.
- Reviewer rationale: Good artifact package for public research and controlled challenge use.
- Interpretation caution: Official hidden results remain trust-mediated.

Reviewer comments: Benchmark artifacts are usable and traceable for public ARC-style research, but hidden-set access and official-run reproducibility remain controlled.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- Excellent: Random, chance, lower reference point, upper reference point, score-ceiling, and trivial-strategy reference points are reported where relevant, empirically checked when possible, and integrated into score interpretation.
- Rating: 2
- Evidence: Harness includes random-baseline sample; exact-match task success has a natural 0-100% scale [S08].
- Missing evidence: Analytic chance levels are not meaningful/easy for arbitrary grids and are not fully developed.
- Reviewer rationale: Adequate floor support, limited chance interpretation.
- Interpretation caution: Scores near zero may still reflect incidental fits, as technical report cautions [S04].

---

#### 8.1.2 Human or expert baselines

- Excellent: Human, contest-population, professional annotator, or expert performance is collected or reported with clear sampling, qualification, task exposure, instructions, timing, tools, uncertainty, coverage of relevant capability domains when broad human-level claims are made, and limits on comparability to AI systems.
- Rating: 3
- Evidence: Human calibration includes 407 participants, 515 sessions, 13,405 test-pair attempts, compensation, timing, attempts, and solvability filters [S04].
- Missing evidence: Human sample representativeness and full item-level data are not public.
- Reviewer rationale: Strong human baseline for feasibility and difficulty.
- Interpretation caution: Human baseline should not be generalized to all populations without caution.

---

#### 8.1.3 Model comparator cohort

- Excellent: Documented model comparison groups are selected and documented to support the intended score meaning, including model identity, version, date, public/private split or suite component, access mode, prompting, sampling settings, tool-enabled or no-tool condition, compute conditions, and uncertainty.
- Rating: 3
- Evidence: Technical report and leaderboard report frontier models/systems and selected scores [S04, S07].
- Missing evidence: Current leaderboard entries can change; some results are preview or partial [S07].
- Reviewer rationale: Useful model context.
- Interpretation caution: Always cite date, model version, and verified status.

---

#### 8.1.4 Historical, version, or benchmark-family comparators

- Excellent: Comparisons to previous benchmark versions, related benchmarks, earlier model generations, or reference suites are clearly documented, justified, and caveated for differences in task content, scoring, risk of unintended disclosure, and prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules.
- Rating: 3
- Evidence: ARC-AGI-1 history and limitations motivate ARC-AGI-2; table compares selected systems across ARC-AGI-1 and ARC-AGI-2 [S04].
- Missing evidence: Formal cross-version equating is limited.
- Reviewer rationale: Good qualitative historical context.
- Interpretation caution: ARC-AGI-1 and ARC-AGI-2 are not interchangeable forms.

---

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- Excellent: Any score boundaries, qualitative bands, pass/fail points, capability labels, score-ceiling interpretations, or tier labels are empirically justified, uncertainty-aware, and tied to intended use rather than arbitrary leaderboard convenience.
- Rating: 2
- Evidence: 85% hidden-set accuracy is competition Grand Prize threshold; report says below 5% is generally not treated as meaningful signal [S04].
- Missing evidence: Thresholds are not psychometrically validated score bands.
- Reviewer rationale: Adequate operational thresholds.
- Interpretation caution: Do not treat 85% as formal AGI threshold without broader validation.

---

#### 8.1.6 Representativeness of reference groups

- Excellent: Reference points and documented comparison groups are representative of the intended score interpretation, with documented inclusion criteria, known gaps, subgroup or capability-domain coverage where relevant, condition-matching evidence, small-sample cautions where relevant, and implications for interpreting benchmark results.
- Rating: 2
- Evidence: Human participants had varied self-reported backgrounds and no clear demographic-performance relationships in measured factors [S04].
- Missing evidence: Full demographic distribution, subgroup reliability, and external human samples are limited.
- Reviewer rationale: Adequate for calibration, partial for broad inference.
- Interpretation caution: Human comparison is a benchmark reference, not a universal population norm.

---

#### 8.1.7 Currency and maintenance of baseline evidence

- Excellent: Evidence from reference points and documented comparison groups is current for the benchmark's intended use, with clear update practices, dates, model-version tracking, and guidance on when outdated comparisons should no longer be used.
- Rating: 3
- Evidence: Leaderboard is maintained and policy describes publication timing [S06, S07].
- Missing evidence: Historical snapshots and retest cadence are not fully formalized.
- Reviewer rationale: Good current reporting infrastructure.
- Interpretation caution: Scores can become stale as model versions/pricing change.

---

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- This overall rating is based on reviewer judgment across 8.1. Do not mechanically average ratings.
- Excellent: Reference points and documented comparison groups are current, representative, condition-matched, uncertainty-aware, and clearly linked to intended score interpretation.
- Rating: 3

Reviewer comments: ARC-AGI-2 has strong human calibration and meaningful model comparators for ARC-style tasks. Reference interpretation is weaker for formal score bands, broad AGI claims, and statistical comparison of close leaderboard results.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- Excellent: The benchmark reports reliability, precision, or stability evidence across the major sources of score variation relevant to the benchmark, including repeated runs, prompt wording, small item changes, claimed capability domains or capability-domain profiles where applicable, scorers, judges, parsers, scorer or judge versions, external APIs and services, search indexes, tools, simulators, user models, tokenizers, context bins, versions, forms, public/private splits, temporal cohorts, environments, leaderboard reruns, and model settings.
- Rating: 2
- Evidence: Deterministic exact scoring, split calibration, and human testing are documented [S04, S05].
- Missing evidence: No full reliability study across prompts, reruns, seeds, model settings, or hidden forms.
- Reviewer rationale: Adequate starting evidence, not comprehensive.
- Interpretation caution: Stability should be checked for each model/system.

---

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- Excellent: Repeat-run studies or equivalent analyses quantify whether repeated evaluations under documented conditions produce similar scores across relevant seeds, sampling settings, temperatures, tool-use conditions, and execution environments, with settings fully documented.
- Rating: 2
- Evidence: Harness exposes configuration, temperature, max tokens, retry attempts, and model/provider settings [S08].
- Missing evidence: Official repeated-run variance for leaderboard scores is not public.
- Reviewer rationale: Configuration support exists; empirical stability evidence is limited.
- Interpretation caution: Single-run leaderboard results may not capture stochastic systems.

---

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- Excellent: Scores and score differences are accompanied by appropriate uncertainty estimates, reported ranges expressing uncertainty around scores or comparisons, standard errors, bootstrap intervals, clustered or hierarchical bootstrap intervals where the design requires them, or other justified precision estimates suitable for the benchmark design.
- Rating: 1
- Evidence: Split calibration target is described [S01, S04, S05].
- Missing evidence: Confidence intervals and standard errors for model scores/ranks are not reported.
- Reviewer rationale: Insufficient for precise comparison.
- Interpretation caution: Small score differences should be treated cautiously.

---

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- Excellent: Automated scoring and parsing are validated against representative outputs, edge cases, responses that fail format or schema requirements, admissible variants, and failure modes, with documented error rates, regression tests, and procedures for resolving ambiguous cases.
- Rating: 3
- Evidence: Exact matching and public scoring code make scorer behavior inspectable for public tasks [S05, S08].
- Missing evidence: Edge-case parser/malformed-output rules are not fully centralized.
- Reviewer rationale: Objective scoring supports scorer reliability.
- Interpretation caution: Structured-output parsing can still introduce implementation variance.

---

#### 9.3.2 Human rater or expert scorer agreement

- Excellent: Human or expert scoring uses clear rubrics, training, representative response samples, adequate numbers of raters, evidence that raters apply rubrics consistently, adjudication procedures, and reporting of residual disagreement.
- Rating: 2
- Evidence: Human task solving and external/internal validation are described [S04].
- Missing evidence: Inter-rater agreement for qualitative task review/redundancy decisions is not quantified.
- Reviewer rationale: Adequate for solvability, partial for item-review reliability.
- Interpretation caution: Task-selection judgments remain partly qualitative.

---

#### 9.3.3 Model-as-judge reliability and validity checks

- Excellent: Scoring by another model is validated against human or expert judgments, tested for bias and score changes caused by prompt wording or format, checked across domains and response styles, and monitored for drift when judge models change.
- Rating: n/a
- Evidence: ARC-AGI-2 uses exact reference-output scoring, not model-as-judge scoring [S05, S08].
- Missing evidence: n/a
- Reviewer rationale: Not applicable.
- Interpretation caution: n/a

---

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- Excellent: The benchmark assesses whether plausible prompt wording, instructions, examples, item phrasing, answer order, formatting, or response-schema variations materially affect scores, reports sensitivity evidence where relevant, and documents which variants are official or comparable.
- Rating: 1
- Evidence: Policy states generic/minimal LLM prompts as a philosophy [S06].
- Missing evidence: No public systematic prompt-sensitivity study.
- Reviewer rationale: Evidence is insufficient for strong stability claims.
- Interpretation caution: Prompting can be a major source of variance for LLMs.

---

#### 9.4.2 Form, split, version, or refresh equivalence

- Excellent: Alternate forms, public and hidden splits, benchmark item updates, capability-domain slices or profiles, translated versions, rolling cohorts, and version updates have documented equivalence evidence, score normalization or equating where needed, or clear warnings about non-comparability.
- Rating: 3
- Evidence: Splits were calibrated to similar human-facing difficulty and mean human accuracy within about 1 percentage point across partitions [S01, S04, S05].
- Missing evidence: Detailed uncertainty around equivalence is not public.
- Reviewer rationale: Good split-equivalence evidence.
- Interpretation caution: Calibration does not remove overfitting risk on public splits.

---

#### 9.4.3 Execution environment and dependency stability

- Excellent: Environment, dependency, API, hardware, external-tool, search-index, simulator, user-model, tokenizer, context-window, and data-access variation is controlled or tested, with guidance on how such variation affects reproducibility and score interpretation.
- Rating: 2
- Evidence: Harness and Kaggle/verification policies document execution routes [S04, S06, S08].
- Missing evidence: Environment versions and provider/API drift may affect results.
- Reviewer rationale: Adequate but needs pinning.
- Interpretation caution: Provider changes can affect reproducibility.

---

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- Excellent: The benchmark provides statistically justified guidance for interpreting model differences, including uncertainty, multiple comparisons where relevant, practical significance, limits on comparing scores across dates or cohorts, and cases where rank differences should not be treated as meaningful.
- Rating: 1
- Evidence: Technical report gives a 5% low-score signal caution [S04].
- Missing evidence: No confidence intervals, significance tests, or minimum-difference guidance for leaderboard comparisons.
- Reviewer rationale: Limited statistical comparison support.
- Interpretation caution: Rank ordering should not imply meaningful differences without uncertainty.

---

### 9.6 Overall Reliability, Precision, and Score Stability

- This overall rating is based on reviewer judgment across sub-sections 9.1-9.5. Do not mechanically average ratings.
- Excellent: Reliability, precision, and score stability evidence is comprehensive across relevant runs, prompts, forms, scorers, parsers, environments, versions, and comparison contexts.
- Rating: 2

Reviewer comments: Deterministic exact scoring and documented split calibration support cautious use. Reliability evidence is incomplete for stochastic model runs, prompt sensitivity, environment drift, confidence intervals, and statistical comparison of leaderboard differences.

---

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- Excellent: The task sample comprehensively represents the intended capability domain or use context, with explicit coverage analysis across relevant language families, scripts, cultures, modalities, application domains, environment states, context-length bins, difficulty bands, task horizons, expert review where relevant, documented exclusions, and clear limits on generalization.
- Rating: 3
- Evidence: ARC-AGI-2 tasks are designed around novel grid-rule inference, compositional generalization, symbolic interpretation, and contextual rule application [S01, S04].
- Missing evidence: The full universe of abstract reasoning tasks is broader than ARC grids.
- Reviewer rationale: Strong for ARC-style abstraction.
- Interpretation caution: Do not generalize to all reasoning domains.

---

#### 10.1.2 Construct breadth and capability-domain coverage

- Excellent: The benchmark identifies relevant capability domains, modalities, difficulty levels, and contexts, and shows that the score meaning is supported across that breadth rather than by isolated task performance.
- Rating: 1
- Evidence: Official broad framing invokes AGI and fluid intelligence [S02, S04].
- Missing evidence: Tasks do not cover the breadth of cognitive domains described in AGI/CHC-style literature [S13].
- Reviewer rationale: Narrow task family cannot support broad cognitive versatility alone.
- Interpretation caution: Use ARC-AGI-2 as one subdomain signal.

---

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- Excellent: Subscores, capability-domain profiles, clusters, task families, suite components, aggregate suite scores, or dimensional interpretations are empirically and conceptually supported, with evidence that score combination does not hide incompatible capabilities or misleadingly combine unrelated abilities.
- Rating: 2
- Evidence: Task families are qualitatively described [S01, S04].
- Missing evidence: No official dimensionality analysis or subscore model was identified.
- Reviewer rationale: Adequate qualitative taxonomy, limited quantitative structure.
- Interpretation caution: Aggregate score may hide different reasoning profiles.

---

#### 10.2.2 Item or task behavior across the score scale

- Excellent: Task behavior supports the intended measurement structure, including appropriate difficulty spread, discriminative value, absence of severe redundancy, and lack of dominant non-target effects such as formatting tactics, score changes caused by prompt wording, parser effects, or performance driven by prior exposure to items.
- Rating: 2
- Evidence: Human solve rates and model score table provide some item/task behavior context [S04].
- Missing evidence: Full item-level difficulty/discrimination tables are not public.
- Reviewer rationale: Partial support.
- Interpretation caution: Model performance at low scores may be noisy.

---

#### 10.2.3 Failure modes and error analysis

- Excellent: Qualitative and quantitative error analysis shows that common failure modes plausibly reflect the capability or quality being measured rather than non-target confounders such as format compliance, parser behavior, memorized source material, instruction complexity, rater or judge bias, or non-target tactics that earn points.
- Rating: 3
- Evidence: Technical report discusses brute-force susceptibility, symbolic interpretation, compositional reasoning, contextual rules, and current AI failure patterns [S04].
- Missing evidence: Full model output error taxonomy is not public for all systems.
- Reviewer rationale: Good qualitative failure-mode evidence.
- Interpretation caution: Failure examples may not exhaust all shortcut strategies.

---

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- Excellent: Scoring rules, scorers, rubrics, parsers, equality-checker LLMs, models used as judges, hash-prefix or strict output rules, coordinate formats, bank-balance or accumulated-return rewards, simulator-based rewards, and score-combination rules are justified and validated as measuring the intended capability rather than irrelevant behavior, output format compliance, parser strictness, verbosity, prior exposure to items or answers, or benchmark-specific tactics; strict formats are tested, relaxed, retried, or justified when they are not part of the target capability.
- Rating: 3
- Evidence: Exact-match success is aligned with task objective; cost adds efficiency context [S01, S05, S07].
- Missing evidence: Partial-credit validity and full cost comparability are not fully formalized.
- Reviewer rationale: Strong primary metric for exact-grid tasks.
- Interpretation caution: Pixel correctness should not be treated as equivalent to task success.

---

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- Excellent: The benchmark tests or convincingly mitigates non-target tactics, superficial cues, score effects caused by response-format compliance, judge preferences, unintended disclosure through prompts, score changes caused by small item changes, prior exposure to items or answers, tool-specific advantages, and other score variation caused by factors outside the target capability.
- Rating: 2
- Evidence: ARC-AGI-2 was designed to reduce brute-force vulnerability and hidden sets protect against exposure [S04, S06].
- Missing evidence: Prompt/format burden, public-eval overfitting, and solver-specific search effects remain possible.
- Reviewer rationale: Adequate controls but not complete.
- Interpretation caution: High performance could reflect efficient ARC-specific engineering rather than broad intelligence.

---

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- Excellent: Relationships with relevant benchmarks, human or expert performance, real-world tasks, external criteria, or expected model differences are hypothesized, justified, empirically examined, and interpreted with appropriate caution.
- Rating: 2
- Evidence: Technical report compares humans, ARC-AGI-1, and selected AI systems [S04].
- Missing evidence: External criterion studies and independent replications for ARC-AGI-2 are limited.
- Reviewer rationale: Adequate initial relational evidence.
- Interpretation caution: Human-AI contrast does not establish broad construct validity.

---

#### 10.4.2 Convergent and discriminant evidence

- Excellent: The benchmark shows expected relationships with measures of similar capabilities and appropriate separation from measures of different capabilities, with explanations for unexpected convergence or divergence.
- Rating: 1
- Evidence: ARC-AGI-1 history and model comparisons provide context [S04].
- Missing evidence: No systematic convergent/discriminant validation against other reasoning benchmarks was identified.
- Reviewer rationale: Weak formal evidence.
- Interpretation caution: Similar or divergent model rankings across benchmarks remain an open question.

---

#### 10.4.3 Ecological or predictive relevance

- Excellent: Evidence supports the relevance of benchmark performance to intended real-world, deployment, scientific, or policy interpretations, with limits clearly stated when the benchmark is abstract, synthetic, or narrow.
- Rating: 1
- Evidence: ARC Prize argues the tasks provide signal toward AI progress [S01, S04, S06].
- Missing evidence: No evidence that ARC-AGI-2 predicts real-world reasoning, agency, safety, or deployment performance.
- Reviewer rationale: Limited evidence.
- Interpretation caution: Scores should not be used as direct real-world readiness indicators.

---

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- Excellent: The benchmark documents data provenance, source-release timing, contest-source leakage controls, public/hidden splits, release rules, canaries or audits where appropriate, searchability risks, training-data exposure risks, diagnostics for prior exposure to benchmark items or answers, and procedures for responding to suspected prior exposure. For benchmarks with high risk of unintended disclosure, live benchmarks, or certification-style benchmarks, stronger evidence may include secret or encrypted reserves, hash commitments, signed logs, synchronized evaluation, post-retirement release, or tasks that test whether performance is driven by prior exposure to items or answers.
- Rating: 3
- Evidence: Hidden sets, no-internet competition protocol, data retention agreements, and public warnings are documented [S02, S04, S05, S06].
- Missing evidence: Full contamination audits and hidden-set provenance are not public.
- Reviewer rationale: Good controls relative to public benchmarks.
- Interpretation caution: Semi-private exposure and public leaderboard feedback remain residual risks.

---

#### 10.5.2 Gameability and benchmark-specific tuning controls

- Excellent: The benchmark identifies and mitigates risks from training, prompting, or optimization targeted narrowly at the benchmark, tuning prompts or systems to exploit known benchmark quirks, leaderboard gaming, reverse engineering, repeated submissions, and optimization against known scorer, rubric, parser, judge, or score-combination effects.
- Rating: 2
- Evidence: ARC-AGI-2 removes brute-force-susceptible tasks and uses hidden sets [S01, S04].
- Missing evidence: Repeated public-eval tuning and ARC-specific solver engineering can still shape results.
- Reviewer rationale: Adequate but not exhaustive.
- Interpretation caution: Solving ARC-AGI-2 may measure ARC-specific adaptation.

---

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- Excellent: Score interpretations are explicitly bounded to what the reviewed entity, task sample, scoring rule, validation evidence, and uncertainty support, and public language avoids unsupported extrapolation from scores to broad capability, expert-level competence, long-horizon agency, real-world readiness, AGI, autonomy, or general intelligence.
- Rating: 2
- Evidence: Policy states ARC benchmarks measure AI progress and are not a litmus test for AGI [S06].
- Missing evidence: Official name and public framing still use AGI/general-fluid-intelligence language [S02, S04].
- Reviewer rationale: Claims are partly bounded but still broad.
- Interpretation caution: Reviewer should phrase conclusions narrowly.

---

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- Excellent: If broad score interpretations are made, the benchmark provides evidence across relevant capability domains, modalities, planning horizons, memory demands, tool-use conditions, and transfer contexts; otherwise it explicitly rejects or limits such interpretations.
- Rating: 1
- Evidence: ARC-AGI-2 samples a narrow visual-symbolic grid task family [S02, S05].
- Missing evidence: Broad cognitive coverage across CHC/AGI domains is absent [S13].
- Reviewer rationale: Insufficient as standalone evidence of AGI or broad cognitive versatility.
- Interpretation caution: ARC-AGI-2 can inform, but cannot settle, AGI claims.

---

### 10.7 Overall Validity Support

- This overall rating is based on reviewer judgment across sub-sections 10.1-10.6. Do not mechanically average ratings.
- Excellent: Validity evidence supports the intended score interpretation through content, structure, scoring, external relations, contamination controls, and proportional public claims.
- Rating: 2

Reviewer comments: Validity support is good for the narrow interpretation "exact-grid abstraction under ARC-AGI-2 conditions." It is limited for broad claims about AGI, general intelligence, real-world reasoning, or cognitive versatility. The phenomenon-task-metric-claim chain should be explicitly bounded in all uses [S12, S13].

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- Excellent: The benchmark explains whether the capability or quality it claims to measure is relevant across intended AI system classes, capability domains, languages, modalities, deployment contexts, and user groups, with limits and exclusions clearly justified.
- Rating: 2
- Evidence: Policy says the leaderboard is open to all model types and public data are usable by local solvers [S05, S06].
- Missing evidence: No full analysis of which system architectures are advantaged or disadvantaged by grid serialization and exact output.
- Reviewer rationale: Broadly usable but task-specific.
- Interpretation caution: Comparability depends on matching I/O, attempts, compute, and verification status.

---

#### 11.1.2 Documentation of fair-use considerations

- Excellent: Documentation gives clear details of fairness, accessibility, bias, language, domain, modality, sensitive-content, and comparability issues considered during benchmark design, evaluation, and interpretation.
- Rating: 2
- Evidence: Policy, guide, and leaderboard notes discuss verification, leakage, preview results, costs, and incomplete tests [S05, S06, S07].
- Missing evidence: Appropriate-use guidance is distributed and not fully formalized as a user-facing warning section.
- Reviewer rationale: Adequate but fragmented.
- Interpretation caution: Users may overread headline scores.

---

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- Excellent: Tasks, prompts, interfaces, rubrics, and evaluation materials are designed to avoid unnecessary exclusion of relevant systems or users, with adaptations and their consequences for score interpretation documented.
- Rating: 3
- Evidence: Tasks require minimal specialized world knowledge and can be represented as JSON or colored grids [S02, S05].
- Missing evidence: Accessibility for assistive technologies or nonvisual human users is not documented.
- Reviewer rationale: Good AI-system accessibility, limited human accessibility documentation.
- Interpretation caution: Human calibration may depend on visual interface.

---

#### 11.2.2 Domain, language, modality, and subgroup coverage

- Excellent: Coverage across relevant capability domains, languages, language families, scripts, modalities, cultures, local cultural authorship, translation or adaptation methods, community participation where relevant, and subgroups is analyzed and linked to the interpretation of scores, with coverage gaps explicitly stated.
- Rating: 2
- Evidence: ARC tasks avoid language and specialized knowledge [S02, S04].
- Missing evidence: Human subgroup analyses are limited; AI system subgroup equivalents are not defined.
- Reviewer rationale: Useful cross-language independence, but narrow domain.
- Interpretation caution: Lack of language does not mean universal fairness.

---

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- Excellent: Prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules support fair comparison across intended AI systems, including model versions, API or local access modes, tool availability, context limits, compute budget, multimodal inputs, safety or refusal policies, latency constraints, and system-specific affordances.
- Rating: 2
- Evidence: Exact scoring and hidden sets support comparison [S05, S06].
- Missing evidence: Prompting, reasoning level, model access, API/local execution, and compute differ across systems [S06, S08].
- Reviewer rationale: Adequate for controlled settings, partial for mixed leaderboard contexts.
- Interpretation caution: Compare only similarly evaluated systems.

---

#### 11.3.2 Access, compute, tooling, and API or local comparability

- Excellent: Access routes, compute requirements, hardware assumptions, API limitations, local execution constraints, tool-use differences, context windows, external service access, and hosted/private evaluation routes are documented and managed so that score comparisons are not distorted without warning.
- Rating: 2
- Evidence: Policy documents cost caps, API rules, Kaggle execution, and no-internet competition protocol [S04, S06].
- Missing evidence: Public leaderboard permits no compute/internet limit for some tests, while competitions impose constraints [S04, S06].
- Reviewer rationale: Conditions are documented but heterogeneous.
- Interpretation caution: Verified leaderboard and competition scores answer different questions.

---

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- Excellent: Rolling, refreshed, or live benchmarks document evaluation dates, cohort identifiers, item-retirement rules, score normalization or equating methods where used, stale-score handling, and direct-comparison limits between models evaluated on different item sets or time windows.
- Rating: 2
- Evidence: Changelog and leaderboard exist [S02, S07].
- Missing evidence: Retest, retirement, and hidden-set refresh policies are not fully specified.
- Reviewer rationale: Basic temporal traceability.
- Interpretation caution: Scores across dates need source and version labels.

---

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- Excellent: The benchmark investigates performance differences, scorer bias, model-judge bias, language or domain bias, accessibility effects, and other differential impacts relevant to the intended use, with implications clearly explained.
- Rating: 1
- Evidence: Technical report says measured demographics did not show clear significant relationships with human performance [S03, S04].
- Missing evidence: Detailed subgroup statistics and AI-system differential analyses are not public.
- Reviewer rationale: Limited evidence.
- Interpretation caution: Absence of detected demographic effects is not a comprehensive fairness study.

---

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- Excellent: Reliability, score stability, and validity evidence are examined across relevant subgroups, capability domains, languages, modalities, or system classes, and any differences are tied to interpretation limits.
- Rating: 1
- Evidence: Human calibration sample was diverse in self-reported background [S04].
- Missing evidence: Subgroup reliability/validity and cross-context evidence are not reported.
- Reviewer rationale: Insufficient for broad subgroup claims.
- Interpretation caution: Treat subgroup fairness as unresolved.

---

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- Excellent: The benchmark provides clear guidance about supported uses, prohibited or unsupported uses, interpretation limits, broad-score-interpretation cautions, source-contest reuse cautions where relevant, and conditions under which comparison or deployment decisions would be inappropriate.
- Rating: 2
- Evidence: Policy says ARC Prize benchmarks are not a litmus test for AGI and warns about verification limits [S06].
- Missing evidence: Non-use cases are not prominently integrated across all public benchmark surfaces.
- Reviewer rationale: Adequate but needs clearer public-facing consolidation.
- Interpretation caution: Do not use score as sole procurement, safety, or AGI-readiness evidence.

---

#### 11.5.2 Release rules and sensitive-content handling

- Excellent: Release rules, data access restrictions, sensitive-content warnings, privacy considerations, safety constraints, and benchmark refresh practices support fair and responsible use.
- Rating: 3
- Evidence: Hidden-set protection, data retention agreements, no-internet competition rules, and badge rules are documented [S04, S06].
- Missing evidence: Detailed incident response and leak-response triggers are limited.
- Reviewer rationale: Good release and integrity controls.
- Interpretation caution: Semi-private exposure remains a known residual risk.

---

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- This overall rating is based on reviewer judgment across sub-sections 11.1-11.5. Do not mechanically average ratings.
- Excellent: The benchmark actively supports fair, accessible, comparable, and appropriately bounded use across its intended systems, users, contexts, domains, languages, and modalities.
- Rating: 2

Reviewer comments: ARC-AGI-2 has clear integrity-oriented policies and strong public/private separation, but fair comparison depends heavily on execution conditions, compute, API access, verification status, and cost reporting. Appropriate-use caveats should be more prominent whenever scores are communicated publicly.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope

- Excellent: Reports, leaderboards, dashboards, tables, scorecards, downloadable files, or papers cover the scores, subscores, and capability-domain profiles relevant to the benchmark's intended use without omitting essential context or implying unsupported granularity.
- Rating: 3
- Evidence: Technical report, official page, policy, and leaderboard define the reporting ecosystem [S01, S03, S04, S06, S07].
- Missing evidence: Public pages do not always make split and verification differences immediately visible.
- Reviewer rationale: Good scope documentation overall.
- Interpretation caution: Users should distinguish official, verified, community, preview, and competition results.

---

#### 12.1.2 Score granularity and level of detail

- Excellent: The level of detail in reported scores, subscores, capability-domain profiles, item-level outputs, rankings, and qualitative labels is justified by the measurement precision, task coverage, and intended interpretation.
- Rating: 3
- Evidence: Leaderboard includes score/cost framing; policy says verified results may include outputs, durations, costs, and individual task scores [S06, S07].
- Missing evidence: Not every result has full raw outputs or per-item traces in the same place.
- Reviewer rationale: Good for official verified reporting, partial for all results.
- Interpretation caution: Aggregate rank can hide task-level patterns.

---

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- Excellent: Reports identify benchmark version, model version, evaluation date, cohort or rolling-window label where relevant, prompts, settings, tools, time limits, access rules, hardware, human-intervention rules, uncertainty, confidence or variability information, and whether differences are meaningful or comparable across dates or cohorts.
- Rating: 2
- Evidence: Leaderboard notes preview, incomplete testing, cost caps, and estimates [S07].
- Missing evidence: Confidence intervals and complete configuration labels are not always shown.
- Reviewer rationale: Adequate labels but incomplete statistical traceability.
- Interpretation caution: Treat close ranks and estimates cautiously.

---

#### 12.2.2 Reproducibility and traceability of reported scores

- Excellent: Reported scores can be traced to documented runs, configurations, raw outputs or sufficient summaries, scoring code, scorer versions, build or replication status where relevant, and data or task versions needed to reproduce or audit the result.
- Rating: 2
- Evidence: Public harness and policy support reproduction of selected results; verified outputs may be shared [S06, S08].
- Missing evidence: Hidden tasks and some official run conditions are not independently reproducible.
- Reviewer rationale: Partial traceability.
- Interpretation caution: Public reproduction cannot fully validate hidden-set scores.

---

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- Excellent: Reports clearly explain what each score supports, what it does not support, how scores relate to score interpretations, where capability-domain coverage does or does not support broad claims, and where uncertainty, validity limits, prior-exposure risk, limits on comparing scores across time, stale scores, or score ceilings affect interpretation.
- Rating: 2
- Evidence: Official reports connect score to ARC-style reasoning and cost efficiency [S01, S04, S07].
- Missing evidence: Broad AGI interpretation limits are not consistently foregrounded.
- Reviewer rationale: Adequate for narrow interpretation.
- Interpretation caution: Avoid headline "AGI" conclusions from score alone.

Reviewer comments: The linkage is strongest for exact-grid abstraction and weaker for broad AGI/general-intelligence interpretation.

---

#### 12.3.2 Raw outputs, per-item data, or trace availability

- Excellent: Raw outputs, per-item results, traces, judge rationales, error categories, retired-item materials, signed logs, or sufficiently detailed audit materials are available or access-controlled in a way that supports independent scrutiny while respecting privacy and release limits.
- Rating: 2
- Evidence: Policy says verified outputs, durations, costs, and task scores are shared on Hugging Face for selected models [S06].
- Missing evidence: Complete trace availability for all leaderboard entries is not public.
- Reviewer rationale: Some trace support exists.
- Interpretation caution: Unverified and preview results have lower auditability.

Reviewer comments: Trace availability depends on result type and verification route.

---

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- Excellent: Reports and public materials use inclusive, non-misleading language; identify potential bias, capability-domain coverage gaps, or other coverage limits; and avoid interpretations that would be unfair across relevant systems, domains, languages, or user groups.
- Rating: 2
- Evidence: Policy distinguishes verified, community, and selected model testing; leaderboard notes incomplete/preview conditions [S06, S07].
- Missing evidence: Subgroup fairness and detailed condition-equivalence reporting are limited.
- Reviewer rationale: Adequate reporting caveats.
- Interpretation caution: Report consumers may miss methodological heterogeneity.

Reviewer comments: Fairness and comparability caveats are present but distributed across multiple surfaces.

---

#### 12.4.2 Acceptability and usability for intended audiences

- Excellent: Reports are understandable, appropriately detailed, accessible, and suited to intended audiences, including technical reviewers, benchmark users, model developers, decision-makers, or the public as applicable.
- Rating: 3
- Evidence: Leaderboard and official pages are public and readable; guide and repo support technical users [S01, S05, S07, S08].
- Missing evidence: Technical caveats are spread across pages.
- Reviewer rationale: Good usability.
- Interpretation caution: Public-facing simplicity can obscure measurement limits.

Reviewer comments: Public users need to inspect policy and guide materials to understand score conditions.

---

#### 12.4.3 Public communication and leaderboard governance

- Excellent: Public score interpretations, rankings, badges, headlines, and rules for leaderboard submissions, eligibility, updates, versions, ranking, audits, and public score claims are transparent, cautious, versioned, resistant to overinterpretation, and clear about update rules, eligibility, cohort or refresh labels, deprecation or archival rules, ranking uncertainty, raw output or trace audit route, private-set governance, public claim rules, capability-domain claim limits where applicable, and known limitations.
- Rating: 3
- Evidence: Verification policy has badges, independent academic panel, funding independence statements, model selection criteria, publication timing, and contact route [S06].
- Missing evidence: ARC Prize retains discretion and may change criteria; governance details for every decision are not fully public.
- Reviewer rationale: Strong governance relative to typical benchmark leaderboards.
- Interpretation caution: Discretionary verification can affect perceived neutrality and coverage.

Reviewer comments: Public governance is comparatively strong, but uncertainty and broad-claim caveats need more prominence.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- This overall rating is based on reviewer judgment across sub-sections 12.1-12.4. Do not mechanically average ratings.
- Excellent: Reporting materials make the benchmark's scores, conditions, uncertainty, validity limits, capability-domain coverage where applicable, supported interpretations, unsupported uses, and public score claims clear enough for responsible use by intended audiences.
- Rating: 3

Reviewer comments: ARC-AGI-2 reporting is relatively strong: official leaderboard, policy, technical report, score/cost framing, and verification governance are available. Remaining weaknesses concern uncertainty, hidden-run traceability, distributed caveats, and public overinterpretation of AGI-framed language.

---

## Final Evaluation

### Evaluative Report of the Benchmark

ARC-AGI-2 is a well-documented and practically useful benchmark for ARC-style exact-grid abstraction. Its strongest measurement features are public task availability, objective exact-match scoring, first-party human calibration, calibrated public/semi-private/private split design, visible changelog, and an open benchmarking harness. Compared with many AI benchmarks, the official materials provide a strong task-development rationale and unusually concrete human solvability evidence.

The main interpretive limitation is construct breadth. ARC-AGI-2 can support cautious claims about performance on novel visual-symbolic grid transformation tasks under specified conditions. It does not, by itself, support broad conclusions about AGI, general cognitive versatility, autonomy, agency, real-world reasoning, or deployment readiness. Its official policy partly acknowledges this by stating that ARC Prize benchmarks are not a litmus test for AGI [S06].

### Conclusions

ARC-AGI-2 is strongest as a benchmark for measuring and comparing ARC-style exact-grid abstraction performance under documented public, semi-private, private, competition, or verification conditions. It can support cautious tracking of frontier model progress on a narrow but demanding abstract-reasoning task family, especially when cost and verification status are included, but it should not be used as standalone proof of AGI, broad general intelligence, real-world reasoning, autonomy, or complete human-like cognitive capability. Responsible administration and interpretation require technical benchmark expertise plus measurement-validity caution.

### Recommendations

1. Publish a consolidated scoring specification for ARC-AGI-2 that resolves the documented two-trial versus three-trial inconsistency and defines malformed-output, retry, parser, and remaining-task policies.
2. Add confidence intervals, repeated-run variance, and minimum meaningful difference guidance to leaderboard reports.
3. Publish more item-level and split-level calibration evidence, including uncertainty for the claimed public/semi-private/private equivalence.
4. Make broad non-use guidance prominent on the benchmark page and leaderboard: ARC-AGI-2 is not standalone AGI evidence.
5. Provide a clearer long-term lifecycle policy for hidden-set refresh, leak response, score archival, and version comparability.
6. Standardize reporting labels for split, model version, prompt/configuration, attempt count, compute budget, cost basis, verification status, and partial/preview status.
7. Expand validation against external reasoning benchmarks and broader cognitive-domain portfolios if ARC-AGI-2 scores are used in general-intelligence narratives.

### Summary of Ratings

| Section                                                      | Overall Rating (`n/a`, `0`-`4`) |
| :----------------------------------------------------------- | :-----------------------------: |
| Section 6. Rationale, documentation, and task/item quality   |                3                |
| Section 7. Benchmark materials and usability                 |                3                |
| Section 8. Reference points and documented comparison groups |                3                |
| Section 9. Reliability and precision                         |                2                |
| Section 10. Validity support                                 |                2                |
| Section 11. Fair use and comparability                       |                2                |
| Section 12. Reports, leaderboards, and public score claims   |                3                |

Reviewer comments: Ratings support cautious use for ARC-style exact-grid abstraction. The broadest public interpretations are limited by construct breadth, uncertainty reporting, hidden-set auditability, and cross-system comparability gaps.

### Gap Register

| Missing or inaccessible information needed for interpretation        | Affected entity or reporting surface                                                | Affected capability domain or score interpretation          | Affected rating(s)               | Why it matters                                                                     | Needed for a higher rating                                                                                         |
| :------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :---------------------------------------------------------- | :------------------------------- | :--------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| Broad AGI language exceeds direct task coverage                      | Official name, report, benchmark page, and leaderboard framing [S01, S02, S04, S07] | Broad AGI/general intelligence interpretation               | 10.1.2, 10.6.1, 10.6.2, 12.3.1   | Users may infer broad cognitive capability from a narrow grid benchmark.           | Prominent non-use guidance and validation portfolio across broader cognitive domains [S13].                        |
| Trial-count inconsistency                                            | README and scoring/guide materials [S01, S02, S04, S05]                             | Exact task success and pass@k comparison                    | 3.1, 3.2, 6.2.3, 6.3.2, 7.1.3    | Attempt rules affect score comparability and human/model equivalence.              | Consolidated scoring spec and corrected docs.                                                                      |
| Limited statistical uncertainty                                      | Leaderboard and technical report [S01, S04, S07]                                    | Score differences, rank differences, split comparison       | 3.6, 8.1.5, 9.2.2, 9.5.1, 12.2.1 | Close leaderboard differences may be overinterpreted.                              | Confidence intervals, repeated runs, and minimum meaningful-difference guidance.                                   |
| Hidden-set auditability limits                                       | Semi-private/private evaluation forms [S01, S05, S06]                               | Hidden-set validity, contamination control, reproducibility | 5.5, 7.1.1, 10.5.1, 12.2.2       | Integrity improves, but independent review of hidden forms is limited.             | Third-party audit summaries, item-level metadata, and post-retirement publication policy.                          |
| Semi-private/private leaderboard terminology is not fully harmonized | ARC-AGI-2 page, guide, policy, and leaderboard [S01, S05, S06, S07]                 | Split labels, leakage interpretation, score comparability   | 5.5, 8.1.4, 11.3.3, 12.1.1       | Split labels affect contamination, auditability, and comparability interpretation. | Consolidated split-use table for public, semi-private, private, competition, verification, and leaderboard routes. |
| Prompt/config sensitivity not systematically reported                | Harness, policy, and leaderboard settings [S06, S08]                                | LLM score stability and cross-system comparability          | 9.2.1, 9.4.1, 11.3.1             | LLM scores may vary by prompt, reasoning level, and parser design.                 | Prompt sensitivity experiments and standardized prompt/config publication.                                         |
| Long-term lifecycle policy incomplete                                | Changelog, hidden-set governance, leaderboard policy [S02, S06, S07]                | Temporal comparability and maintenance                      | 5.8, 6.2.7, 8.1.7, 11.3.3        | Temporal comparability and benchmark integrity require governance.                 | Versioning, retirement, leak response, and archive policy.                                                         |
| External validity evidence limited                                   | Technical report and public claims [S01, S04]                                       | Real-world reasoning and broad intelligence claims          | 10.4.1, 10.4.2, 10.4.3           | Real-world reasoning and broad intelligence claims need external evidence.         | Convergent/discriminant studies and predictive/ecological validation [S12].                                        |

## Bibliography

1. ARC Prize. "ARC-AGI-2." https://arcprize.org/arc-agi/2. Accessed 2026-05-17.
2. ARC Prize. "ARC-AGI-2 GitHub repository." https://github.com/arcprize/ARC-AGI-2. Accessed 2026-05-17.
3. Greg Kamradt. "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems." ARC Prize blog, 2025-05-20. https://arcprize.org/blog/arc-agi-2-technical-report. Accessed 2026-05-17.
4. Francois Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard. "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems." arXiv:2505.11831v2, 2026. https://arxiv.org/abs/2505.11831.
5. ARC Prize. "ARC-AGI-1 & ARC-AGI-2 Guide." https://arcprize.org/guide/1. Accessed 2026-05-17.
6. ARC Prize. "ARC Prize Verified Testing Policy." https://arcprize.org/policy. Accessed 2026-05-17.
7. ARC Prize. "ARC Prize Leaderboard." https://arcprize.org/leaderboard. Accessed 2026-05-17.
8. ARC Prize. "arc-agi-benchmarking." https://github.com/arcprize/arc-agi-benchmarking. Accessed 2026-05-17.
9. MESA repository. `MESA EFPA template official.md`. Accessed 2026-05-17.
10. MESA repository literature corpus. `literature/betterbench.md`, `literature/Measuring_what_Matters.md`, and `literature/A_Definition_of_AGI.md`. Accessed 2026-05-17.
