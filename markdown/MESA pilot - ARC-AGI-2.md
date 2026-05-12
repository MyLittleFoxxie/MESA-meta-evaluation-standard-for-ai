# MESA Pilot Review: ARC-AGI-2 v2

This v2 pilot now applies the targeted `markdown/MESA EFPA template v6.md` modifications to the prior ARC-AGI-2 v1/v5 migration. It uses the same official ARC materials available on 2026-05-09 and does not perform a new online source refresh. Part A describes what the official materials state, including unresolved inconsistencies. Part B assigns ratings using Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

Before completing the review, inspect the most authoritative available materials. Prefer official benchmark papers, websites, repositories, data hosts, leaderboards, harnesses, changelogs, and maintainer statements. Independent commentary should be used only for context, external critique, or disputed claims, and should not replace official benchmark facts.

Documentation status summary for Part A:

- [x] Documented: benchmark name, official page, technical report, arXiv record, public task repository, public training and public evaluation task counts, semi-private/private split counts, exact-grid task format, human solvability criterion, controlled human testing, cost/efficiency emphasis, public leaderboard page, public changelog, official benchmarking repository, and exact-grid scoring path.
- [x] Partially documented: current leaderboard values in text-accessible form, Kaggle competition rules from the page as rendered in this environment, exact current private-set governance, cost-estimation methods for all systems, raw model outputs, split-equivalence statistics beyond official summary claims, malformed-output handling, response-format sensitivity, private-set temporal comparability, and retirement readiness.
- [x] Not documented: formal broad-AGI non-use rules, public hash/signature audit logs for hidden sets, complete official raw traces, current private-set governance details, and complete retirement or archival criteria.
- [x] Unclear from available materials: whether the user-facing attempt rule should be read as exactly two trials/pass@2 everywhere or three trials in the repository task-interface wording. This review treats that as an official-material inconsistency and a gap to resolve, not as a settled fact.

Part B rating scale used here:

| Rating | Meaning                                                                                |
| :----- | :------------------------------------------------------------------------------------- |
| `n/a`  | This attribute is not applicable to this benchmark or its stated use.                  |
| `0`    | Not possible to rate because no, or insufficient, information is provided.             |
| `1`    | Inadequate for the benchmark's stated purpose or intended interpretation.              |
| `2`    | Adequate: sufficient for cautious use, with limitations that should be stated.         |
| `3`    | Good: clear, relevant, and mostly complete support, with no major interpretive threat. |
| `4`    | Excellent: comprehensive, well-documented, and strongly aligned with the item anchor.  |

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

Section 1 identifies the review event, benchmark identity, and official materials inspected.

### 1.1 Review Information

| Prompt                                 | Response                                                                                                                                 |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Reviewer                               | MESA pilot reviewer                                                                                                                      |
| Date of current review                 | 2026-05-09                                                                                                                               |
| Date of previous review, if applicable | 2026-05-09 for the original ARC-AGI-2 pilot source review.                                                                               |
| Review scope                           | Targeted v6 update of the ARC-AGI-2 v2 pilot, preserving the 2026-05-09 source base and adding the new v6 fields and equivalent answers. |
| Review boundary                        | Official ARC materials first; local MESA literature used only for Part B rating criteria and AGI/CHC caution.                            |

Review notes: This v2 pilot preserves the original source review and treats official-source inconsistencies as gaps. It does not resolve them by inference.

### 1.2 Information Sources Reviewed

| Material type                                 | Artifact reviewed                                                                                                                                                                  | Access date | Role in review                                                                                                                                         |
| :-------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Benchmark website or documentation hub        | [ARC-AGI-2 official page](https://arcprize.org/arc-agi/2)                                                                                                                          | 2026-05-09  | Primary public description of goals, dataset structure, calibration, efficiency measurement, and changelog summary.                                    |
| Official paper or technical report            | [ARC-AGI-2 technical report page](https://arcprize.org/blog/arc-agi-2-technical-report)                                                                                            | 2026-05-09  | Official launch/technical-report page with design goals, human testing, model-score context, and competition links.                                    |
| Official paper or technical report            | [arXiv:2505.11831](https://arxiv.org/abs/2505.11831)                                                                                                                               | 2026-05-09  | Versioned technical report record; v2 last revised 2026-01-15.                                                                                         |
| Repository                                    | [arcprize/ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2)                                                                                                                        | 2026-05-09  | Public task data repository, README, license, file format, task success criterion, and public changelog.                                               |
| Repository                                    | [arcprize/arc-agi-benchmarking](https://github.com/arcprize/arc-agi-benchmarking)                                                                                                  | 2026-05-09  | Official benchmarking harness linked from official materials; supports model adapters, scoring, sample tasks, random baseline, and cost configuration. |
| Leaderboard, dashboard, or results page       | [ARC Prize leaderboard](https://arcprize.org/leaderboard)                                                                                                                          | 2026-05-09  | Public leaderboard page with ARC-AGI-2 tab, cost/performance framing, and verification caveats.                                                        |
| Release log, changelog, or maintenance record | [ARC-AGI-2 changelog](https://github.com/arcprize/ARC-AGI-2/blob/main/changelog.md)                                                                                                | 2026-05-09  | Public task release and public-evaluation update record.                                                                                               |
| Leaderboard, dashboard, or results page       | [ARC Prize 2025 Kaggle competition](https://www.kaggle.com/competitions/arc-prize-2025)                                                                                            | 2026-05-09  | Official competition page linked from ARC Prize; content did not render text in this environment, so details remain a gap here.                        |
| Contextual literature                         | `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`; `markdown/Papers/betterbench.md`; `markdown/Papers/Measuring_what_Matters.md`; `markdown/Papers/A_Definition_of_AGI.md` | 2026-05-09  | Used only for MESA Part B rating criteria and broad-claim caution.                                                                                     |

Other materials/comments: Official ARC pages link the ARC Prize testing policy and competition infrastructure; this pilot records them as official artifacts but does not rely on inaccessible page details.

### 1.3 Benchmark Information

| Prompt                                                             | Response                                                                                                                                                            |
| :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Benchmark name                                                     | Abstraction and Reasoning Corpus for Artificial General Intelligence v2                                                                                             |
| Short name or acronym                                              | ARC-AGI-2                                                                                                                                                           |
| Benchmark version, edition, or release                             | ARC-AGI-2 public release; changelog records a 2025-03-24 release of 1,360 tasks and public-evaluation updates on 2025-04-14 and 2025-04-17.                         |
| Original benchmark name, if this is an adaptation                  | Successor to ARC-AGI-1 / original ARC.                                                                                                                              |
| Benchmark creators or authors                                      | Francois Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard are listed on arXiv. ARC Prize, Inc. hosts the official materials.                  |
| Current maintainers                                                | ARC Prize / `arcprize` GitHub organization.                                                                                                                         |
| Host organization, platform host, repository owner, or distributor | ARC Prize, Inc.; GitHub task repository; Kaggle competition infrastructure; arXiv technical report.                                                                 |
| Date of original release                                           | Official changelog records ARC-AGI-2 release on 2025-03-24.                                                                                                         |
| Date of current release or revision                                | Public task changelog updates are dated 2025-04-14 and 2025-04-17; arXiv v2 is dated 2026-01-15.                                                                    |
| License or access terms                                            | ARC-AGI-2 task repository lists Apache-2.0 license. Official benchmarking repository lists MIT license. Kaggle and ARC Prize testing terms require separate review. |
| Persistent identifier, citation, or DOI                            | arXiv identifier `2505.11831` and DOI `10.48550/arXiv.2505.11831`.                                                                                                  |

Review notes: The benchmark is explicitly positioned as AGI-relevant and as a general-fluid-intelligence measure. This creates a high validity burden in Part B.

### 1.4 Public Artifacts

| Artifact                                  | URL or location                                                                                                                     | Access status                         | Review detail                                                                                                                  |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| Paper or technical report                 | [arXiv:2505.11831](https://arxiv.org/abs/2505.11831); [technical report page](https://arcprize.org/blog/arc-agi-2-technical-report) | Public                                | Technical report and official summary are available.                                                                           |
| Benchmark website                         | [ARC-AGI-2 official page](https://arcprize.org/arc-agi/2)                                                                           | Public                                | Documents goals, task structure, calibration, efficiency, and links.                                                           |
| Code repository                           | [arcprize/ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2)                                                                         | Public                                | Contains public training/evaluation JSON tasks, README, license, and changelog.                                                |
| Evaluation harness                        | [arcprize/arc-agi-benchmarking](https://github.com/arcprize/arc-agi-benchmarking)                                                   | Public                                | Provides CLI, provider adapters, random baseline, scoring, sample tasks, and config path.                                      |
| Dataset or task set                       | `data/training` and `data/evaluation` in the public GitHub repository                                                               | Public plus hidden/private components | Public repository contains 1,000 training tasks and 120 public evaluation tasks; semi-private and private sets are not public. |
| Prompt set                                | Benchmarking repository and technical report context                                                                                | Partially public                      | ARC itself is grid input/output; model prompting details depend on harness/model adapter.                                      |
| Rubric or scoring guide                   | README task-success criterion and benchmarking scoring code                                                                         | Public, with inconsistency            | Exact-grid success is clear, but official materials conflict between two-trial and three-trial wording.                        |
| Leaderboard or result display             | [ARC Prize leaderboard](https://arcprize.org/leaderboard); Kaggle competition link                                                  | Public/hosted                         | Public page has ARC-AGI-2 tab and cost/performance framing; current ARC-AGI-2 entries were not text-extracted here.            |
| Release log or changelog                  | [changelog.md](https://github.com/arcprize/ARC-AGI-2/blob/main/changelog.md)                                                        | Public                                | Records release and public-evaluation task fixes.                                                                              |
| Contact, issue channel, or feedback route | GitHub issues; ARC Prize website/community links                                                                                    | Public                                | Repository issue channel and ARC Prize community links exist.                                                                  |

Other artifacts/comments: The private and semi-private sets are intentionally hidden to reduce leakage and competition gaming, which supports integrity while limiting independent inspection.

---

## Section 2. Classification

Section 2 classifies the benchmark's intended measurement domain, target systems, users, task structure, and administration conditions.

### 2.1 Claimed Capability Domains

- [ ] Not explicitly stated
- [x] General capability or intelligence
- [x] Reasoning
- [ ] Knowledge
- [ ] Language understanding
- [ ] Writing or generation quality
- [ ] Mathematics
- [ ] Coding or software engineering
- [ ] Scientific or technical expertise
- [ ] Domain-specific professional expertise
- [x] Multimodal perception
- [ ] Audio or speech
- [ ] Video understanding
- [ ] Tool use
- [x] Planning or agency
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [ ] Calibration or uncertainty

Other domains/comments: Official materials emphasize abstract reasoning, problem solving, general fluid intelligence, human-like generalization, symbolic interpretation, compositional reasoning, contextual rule application, and efficiency/cost.

Review notes: Multimodal perception here means visual grid perception, not broad image understanding. Planning/agency is marked only because solvers may need search or iterative construction, not because ARC-AGI-2 is an agentic environment.

### 2.2 Area of Use

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

Other areas/comments: Official materials position ARC-AGI-2 as a signal on AGI progress and as a competition benchmark.

Review notes: Deployment gating and procurement uses are not documented and would require separate validation.

### 2.3 Intended AI Systems

- [ ] Not explicitly stated
- [x] Frontier general-purpose language models
- [x] Chat or instruction-following models
- [ ] Base language models
- [ ] Code models
- [x] Multimodal models
- [ ] Audio or speech models
- [x] Agentic systems
- [x] Tool-using systems
- [ ] Retrieval-augmented systems
- [ ] Domain-specialized models
- [x] Open-weight local models
- [x] API-hosted models

Other systems/comments: The official benchmarking harness supports several API providers and custom adapters. Kaggle competition systems may be self-contained under competition constraints.

Free text description: ARC-AGI-2 targets humans and artificial systems that aim to emulate human-like general fluid intelligence, including LLM-based reasoning systems, program-synthesis systems, search systems, and competition-grade solvers.

### 2.4 Intended Users of Benchmark Outputs

- [ ] Not explicitly stated
- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [ ] Product teams
- [x] Safety evaluators
- [x] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [ ] Educators or academic reviewers
- [x] Public leaderboard users

Other users/comments: Competition participants, ARC Prize organizers, and the broader AI-progress audience are intended recipients.

Review notes: The benchmark has public communication power because the name invokes AGI; this increases the need for careful interpretation.

### 2.5 Task Families, Subdomains, and Scores

| Component                                                                                    | Description                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claimed construct or phenomenon                                                              | Abstract reasoning and problem solving at higher levels of fluid intelligence, with AGI-progress relevance.                                                                                                                               |
| Claimed capability definition                                                                | Ability to infer a hidden transformation from few demonstration input/output grids and construct exact output grids for novel test inputs under specified attempt and cost conditions.                                                    |
| Construct subcomponents                                                                      | Few-shot grid transformation induction, symbolic interpretation, compositional reasoning, contextual rule application, efficient search/generalization, and output-grid construction.                                                     |
| Excluded scope or non-target abilities                                                       | Broad language, semantic world knowledge, long-term memory, social cognition, embodied interaction, autonomous tool use, open-ended planning, and real-world transfer are outside the direct task family.                                 |
| Task families or subdomains                                                                  | ARC-style colored-grid tasks with demonstration input/output pairs and hidden test input grids. Official examples highlight symbolic interpretation, compositional reasoning, and contextual rule application.                            |
| Task sources, including reused datasets or adapted benchmarks                                | Hand-designed ARC-AGI-2 tasks distributed through the official repository and hidden competition splits; ARC-AGI-2 is a successor to ARC-AGI-1, not a reused broad cognitive battery.                                                     |
| Task sampling method, such as random, stratified, criterion, targeted, convenience, or mixed | Criterion/targeted task design: tasks are selected for human solvability, low prior-knowledge burden, resistance to brute force, and difficulty for current AI rather than as a random sample of all reasoning tasks.                     |
| Task selection or filtering logic                                                            | Tasks are designed to require minimal prior knowledge/Core Knowledge priors, be feasible for humans, resist brute-force search, and challenge current AI systems.                                                                         |
| Splits or partitions                                                                         | 1,000 public training tasks, 120 public evaluation tasks, 120 semi-private evaluation tasks, and 120 private evaluation tasks.                                                                                                            |
| Primary score                                                                                | Task success / accuracy under an exact-grid criterion, with pass@2 wording in official page and two-trial wording in README.                                                                                                              |
| Subscores                                                                                    | Public, semi-private, private, leaderboard/competition scores, and cost/performance views.                                                                                                                                                |
| Derived or aggregate scores                                                                  | Efficiency/cost metrics are part of official reporting; leaderboard filters and cost-per-task framing are used.                                                                                                                           |
| Qualitative labels or bands                                                                  | The official page asks whether a system can reach 85% accuracy; this is a challenge/competition target rather than a validated psychometric band.                                                                                         |
| Claim boundaries or caveats                                                                  | ARC-AGI-2 is a grid-abstraction benchmark. It is AGI-relevant by author framing, but it does not measure full AGI breadth such as language, memory, embodiment, social cognition, tool autonomy, broad knowledge, or real-world planning. |

Review notes: Part B should evaluate two interpretations separately: narrow ARC grid reasoning and broad AGI/general-fluid-intelligence inference.

### 2.6 Model Response Mode

- [ ] Not explicitly stated
- [ ] Multiple choice
- [ ] Short text
- [ ] Long-form text
- [x] Structured output, such as JSON or XML
- [x] Code
- [x] Mathematical expression
- [x] Tool call
- [ ] Browser or web action
- [ ] File, document, or artifact generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [x] Interaction in a simulated environment
- [ ] Interaction in a real or external environment

Other response modes/comments: Core task response is an output grid: a rectangular matrix of integers 0-9. Solvers may produce grids through an interface, code, program search, model output, or harness adapter.

Required output format, if any: Exact output grid dimensions and cell values for each test input.

### 2.7 Prerequisites for Evaluated Systems

| Requirement                                                     | Irrelevant or not necessary | Necessary information given | Information missing | Evidence / notes                                                                                                              |
| :-------------------------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: | :---------------------------------------------------------------------------------------------------------------------------- |
| Language support                                                |            - [x]            |            - [ ]            |        - [ ]        | Tasks are primarily visual/grid based; language may be used by LLM prompts but is not the target task content.                |
| Context length                                                  |            - [ ]            |            - [x]            |        - [ ]        | Tasks are small JSON grids; no long-context requirement is central.                                                           |
| Multimodal input support                                        |            - [ ]            |            - [x]            |        - [ ]        | Systems must perceive or parse grid patterns.                                                                                 |
| Structured output support                                       |            - [ ]            |            - [x]            |        - [ ]        | Output grids must be exact.                                                                                                   |
| Exact format, schema, or parser compatibility                   |            - [ ]            |            - [x]            |        - [ ]        | Output grids have exact dimensions and integer cell values; benchmark code can validate exact outputs.                        |
| Retry, repair, or correction-loop support for malformed outputs |            - [ ]            |            - [ ]            |        - [x]        | Official materials do not fully specify a malformed-output retry or repair policy, and attempt-count wording is inconsistent. |
| Tool access                                                     |            - [ ]            |            - [x]            |        - [ ]        | Solver architecture may use search/code/tools; competition contexts may constrain this.                                       |
| Browser or internet access                                      |            - [x]            |            - [ ]            |        - [ ]        | Not required for task solving; browser only supports human interface and hosted pages.                                        |
| Code execution                                                  |            - [ ]            |            - [x]            |        - [ ]        | Programmatic solvers and benchmarking harnesses require code execution.                                                       |
| Memory or persistent state                                      |            - [ ]            |            - [ ]            |        - [x]        | Training/adaptation assumptions vary; persistent state policy is not fully specified in all contexts.                         |
| API compatibility                                               |            - [ ]            |            - [x]            |        - [ ]        | Benchmarking harness supports multiple provider APIs and custom adapters.                                                     |
| Latency or time budget                                          |            - [ ]            |            - [ ]            |        - [x]        | Time/cost constraints vary by leaderboard and competition context.                                                            |
| Cost or compute budget                                          |            - [ ]            |            - [x]            |        - [ ]        | Official reporting emphasizes cost; leaderboard notes cost-related display constraints.                                       |

Other requirements/comments: Systems need reliable grid parsing, grid generation, and exact-output submission. Human interface use is not the same as model-harness evaluation.

Review notes: Efficiency is part of the ARC-AGI-2 concept, so compute and cost are measurement-relevant rather than incidental.

### 2.8 Evaluation Conditions

| Condition                         | Description                                                                                                                                       |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| Prompting protocol                | Depends on solver/harness adapter. Official benchmarking repository documents model configs and provider adapters.                                |
| System prompt                     | Not a core ARC task concept; may vary by LLM harness.                                                                                             |
| Few-shot examples                 | Each task includes demonstration input/output pairs, typically three train pairs.                                                                 |
| Sampling settings                 | Model-specific in the benchmarking harness; not uniform across all solvers.                                                                       |
| Tool permissions                  | Competition and benchmark contexts may allow algorithmic search or code; exact constraints vary by platform and require separate review.          |
| Time limits                       | Not fully specified in public task repository; competition constraints require Kaggle/testing-policy review.                                      |
| Human intervention rules          | Human testing was controlled for task calibration; model submissions should not leak evaluation-set information into development.                 |
| Hardware or hosted service        | Public task repository supports local use; benchmarking harness supports API providers; Kaggle competition uses hosted submission infrastructure. |
| Network requirements              | Required for API-based benchmarking and hosted leaderboard/competition use, not for local task files.                                             |
| Sandbox or security constraints   | Kaggle and competition contexts likely impose constraints; details were not text-accessible here.                                                 |
| Special administration conditions | Public, semi-private, and private evaluation sets are calibrated and used for different leakage/competition purposes.                             |

Other conditions/comments: Official materials conflict on attempts: pass@2/two trials in the official page and README criterion, but three trials in README task-interface wording.

Review notes: Attempt-rule inconsistency is consequential because it affects task success, human comparability, and leaderboard interpretation.

### 2.9 Task and Response Types

Selection-based responses:

- [ ] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [ ] Ranking
- [ ] Classification
- [ ] Pairwise preference

Production-based responses:

- [ ] Open-ended text
- [x] Code generation
- [x] Proof, derivation, or explanation
- [x] Structured data
- [ ] Generated media
- [x] Artifact production

Interaction-based responses:

- [x] Tool use
- [ ] Browser or web navigation
- [x] API interaction
- [ ] Computer-use interaction
- [x] Simulated environment task
- [ ] Real or external environment task

Process data:

- [ ] Response latency
- [ ] Token usage
- [x] Cost
- [ ] Tool traces
- [ ] Intermediate reasoning traces
- [x] Execution logs

Other task/response types: The final judged artifact is an output grid, regardless of whether the solver used code, natural language, search, or direct grid construction.

Review notes: Explanations are not required for scoring; exact grid output is what matters.

### 2.10 Input Stimulus Type

- [ ] Not explicitly stated
- [ ] Text
- [x] Code
- [x] Tables or structured data
- [x] Images
- [ ] Audio
- [ ] Video
- [ ] Documents
- [ ] Web pages
- [ ] APIs or tools
- [x] Dynamic environment

Other stimulus types/comments: The canonical stimulus is a structured colored grid represented as JSON and/or visualized in an interface. "Dynamic environment" applies only to interactive solving interfaces and iterative attempts, not to changing task worlds.

### 2.11 Number of Items or Measurement Points

| Prompt                                  | Response                                                                                                                                                               |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total public items or tasks             | 1,120 public tasks in the repository: 1,000 training and 120 public evaluation.                                                                                        |
| Total private or hidden items           | 240 non-public evaluation tasks: 120 semi-private and 120 private, according to official page/changelog.                                                               |
| Development or example items            | Training set contains 1,000 public tasks used to demonstrate format and Core Knowledge priors.                                                                         |
| Test items                              | Public evaluation set has 120 tasks; semi-private and private sets each have 120 tasks.                                                                                |
| Dynamic or generated tasks              | Tasks are static JSON files; leaderboard/competition evaluation may be dynamic in submission timing, not item generation.                                              |
| Episodes, trials, or measurement points | Each task includes 1-2 test pairs typically; task success requires all test outputs correct. Attempt count is inconsistently stated as two/pass@2 versus three trials. |
| Item count uncertainty                  | Counts are clear across official page and changelog; attempt rule is unclear.                                                                                          |

Review notes: The count structure is strong; the attempt-count ambiguity should be fixed by maintainers.

### 2.12 Mode of Evaluation

- [ ] Not indicated
- [x] Local batch evaluation
- [x] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [ ] Interactive agent evaluation
- [x] Human-in-the-loop evaluation
- [ ] Continuous or rolling evaluation

Other modes/comments: Human-in-the-loop applies to controlled human testing for calibration and the human task interface, not to model scoring.

Identity and condition controls:

- [ ] No control over submitted systems
- [x] Some control over submitted systems
- [x] Controlled model access or audit
- [x] Controlled evaluation center or private harness
- [ ] Not documented

Review notes: The public/semi-private/private structure is a major integrity mechanism.

### 2.13 Technological Arrangements

| Technology            |   A   |   R   | Evidence / notes                                                                |
| :-------------------- | :---: | :---: | :------------------------------------------------------------------------------ |
| API access            | - [x] | - [ ] | Benchmarking repo supports API providers; not required for all solvers.         |
| Local inference       | - [x] | - [ ] | Public task data and custom solvers can run locally.                            |
| GPU                   | - [ ] | - [ ] | Depends on solver; not inherent to the benchmark.                               |
| CPU-only execution    | - [x] | - [ ] | Simple solvers and scoring can run CPU-side.                                    |
| Docker or container   | - [ ] | - [ ] | Not documented as a primary path in reviewed materials.                         |
| Python package or CLI | - [x] | - [ ] | Official benchmarking repository provides CLI and Python package configuration. |
| Browser               | - [x] | - [ ] | Human play/testing interface uses browser.                                      |
| External tools        | - [x] | - [ ] | Solvers may use program search/code; constraints vary.                          |
| Internet access       | - [x] | - [ ] | Needed for hosted/API and leaderboard use.                                      |
| Proprietary platform  | - [x] | - [ ] | Kaggle and API model providers may be used.                                     |

Other technologies/comments: Benchmarking repository has model adapters, provider config, pricing fields, sample tasks, random baseline, and scoring scripts.

### 2.14 Time and Resource Requirements

| Activity                           | Time, compute, or cost estimate                                                                                                              |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Setup                              | Official benchmarking repository provides quickstart but not a universal setup-time estimate.                                                |
| Model inference or task completion | Human testing average reported around 2.3 minutes per task on candidate tasks in the technical-report page.                                  |
| Scoring                            | Exact-grid scoring is scriptable; no full scoring-time estimate is stated.                                                                   |
| Human adjudication                 | Controlled human testing involved 400+ participants and 1,417 unique tasks according to official technical-report page.                      |
| Analysis or reporting              | Not specified as a time budget.                                                                                                              |
| Full benchmark run                 | Depends on solver and split; not specified universally.                                                                                      |
| API or compute cost                | Official reporting emphasizes cost/performance; leaderboard shows cost-related constraints, but complete cost rules require separate review. |

Other requirements/comments: Cost is not just operational overhead; it is part of ARC-AGI-2's intended efficiency interpretation.

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant             | Purpose                                                                                                    | Equivalence claim                                                | Status               |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :------------------- |
| Public training set         | Demonstrate task format and Core Knowledge priors; can be used for training/prototyping.                   | Not intended as final evaluation.                                | Public, 1,000 tasks. |
| Public evaluation set       | Public testing for systems not developed against those tasks.                                              | Official page says calibrated with semi-private/private sets.    | Public, 120 tasks.   |
| Semi-private evaluation set | Live contest and ARC Prize leaderboard for remotely hosted commercial models with low leakage probability. | Official page says calibrated to public/private difficulty.      | Hidden, 120 tasks.   |
| Private evaluation set      | Final Kaggle contest leaderboard for self-contained models with near-zero leakage probability.             | Official page says calibrated to public/semi-private difficulty. | Hidden, 120 tasks.   |
| ARC-AGI-1 predecessor       | Earlier benchmark and continuity reference.                                                                | Not equivalent; ARC-AGI-2 is harder and redesigned.              | Public predecessor.  |

Other forms/comments: Official page claims comparable scores across eval sets within less than 1 percentage point expected assuming no overfitting; this is a strong but summary-level claim.

### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [ ] Random sample from fixed pool
- [x] Hidden test set selected by maintainers
- [ ] Procedurally generated tasks
- [ ] Adaptive routing based on performance
- [ ] Dynamic environment generation
- [ ] Rolling or periodically refreshed task set
- [ ] Not explicitly stated

Other task selection/comments: Public changelog records corrections to public evaluation tasks after release.

Describe task selection method: Candidate tasks are designed around ARC principles, filtered for human solvability and resistance to brute-force search, and calibrated across public/semi-private/private splits through controlled human testing and AI testing.

### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [ ] Model intermediate trace
- [ ] Tool-use trace
- [x] Code execution result
- [ ] Environment state
- [x] Reference answer
- [ ] Unit test
- [ ] Human judge
- [ ] Model judge
- [ ] Ensemble or panel adjudication
- [ ] External verifier

Other scoring inputs/comments: Cost metrics may use token/pricing/runtime configuration from the benchmarking harness and leaderboard policy.

Review notes: Core correctness scoring is exact and reference-based; no model-as-judge is required.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

- [ ] Not explicitly stated
- [x] Automated exact-match scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] Unit-test or execution-based scoring
- [x] Rule-based scoring
- [ ] Human rating
- [ ] Model-as-judge scoring
- [x] Output parser or extractor
- [x] Fuzzy, schema-aware, or admissible-variant parsing
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [x] Leaderboard service scoring
- [ ] Manual adjudication

Other scoring methods/comments: Human testing is used to calibrate tasks and baselines, not to score AI submissions.

Review notes: The scoring method is exact-grid comparison. Attempt-count wording is inconsistent across official materials.

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or metric  | Definition                                                                            | Aggregation                                                                          | Interpretation stated by authors                                              |
| :--------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Primary score    | Task success / accuracy under exact grid matching.                                    | A task is solved when all test output grids are correct within the allowed attempts. | Measures ARC-style abstract reasoning and problem solving.                    |
| Subscore         | Public, semi-private, private, leaderboard, competition, and model/system categories. | Split or leaderboard grouping.                                                       | Supports public research, live leaderboard, and final competition evaluation. |
| Derived score    | Cost/efficiency, including cost-per-task framing.                                     | Depends on benchmark/leaderboard configuration and model pricing/runtime.            | Efficiency is treated as central to intelligence measurement.                 |
| Qualitative band | 85% challenge target appears on official page.                                        | Not a validated psychometric band.                                                   | Competition/AGI-progress target, not standalone proof of AGI.                 |

Treatment of invalid, missing, malformed, or refused responses: Benchmarking repository scoring expects submission directories with output grids. Leaderboard page says remaining tasks are marked incorrect when models cannot produce full test outputs.

Response-format retry, repair, parser fallback, or manual adjudication policy: Partially documented. Exact-grid outputs are expected and incomplete outputs may be counted incorrect, but the reviewed official materials do not fully reconcile pass@2/two-trial wording with three-trial interface wording or specify a general malformed-output repair path.

Review notes: The exact-grid metric is clear. Broad interpretation depends on whether the ARC task format adequately represents the claimed construct.

### 3.3 Scale or Metric Types

- [ ] Raw score
- [x] Accuracy
- [x] Success rate
- [x] Pass rate or pass@k
- [ ] Unit-test pass rate
- [ ] Win rate
- [ ] Elo or ranking score
- [ ] Pairwise preference score
- [ ] Reward or return
- [x] Cost-adjusted score
- [ ] Calibration or uncertainty score
- [ ] Percentile or normalized score
- [x] Threshold or decision index

Other metric types/comments: Pass@2 is used in official page language, but README also contains three-trial wording.

### 3.4 Score Transformation

- [ ] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against baseline
- [ ] Weighting across subdomains
- [x] Aggregation formula documented
- [ ] Aggregation formula partially documented
- [ ] Aggregation formula not documented
- [ ] Not applicable

Formula or transformation comments: Correct tasks are aggregated as accuracy/success rate. Cost metrics require additional pricing/runtime inputs.

### 3.5 Reference Groups, Baselines, and Comparators

- [ ] No baseline or comparator documented
- [x] Random or chance baseline
- [x] Human baseline
- [ ] Expert human baseline
- [x] Model baseline
- [x] Previous model cohort
- [x] Commercial system comparator
- [x] Open-weight model comparator
- [ ] Domain-specific reference group

Other comparators/comments: Official human testing is central. Random baseline support exists in the benchmarking repository sample, but not as a full interpretive baseline across all public results.

| Comparator or baseline               | Construction method                                                                                                                                  | Intended interpretation                                                    |
| :----------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| Random or chance baseline            | Benchmarking repo includes random baseline sample; exact random success is near-zero for grid tasks.                                                 | Demonstrates a trivial floor.                                              |
| Human baseline                       | Official materials report 400+ participants, 1,417 unique tasks, minimum two-human solvability, and average public-eval human performance in README. | Anchors "easy for humans, hard for AI" and split calibration.              |
| Expert baseline                      | Not the main comparator; general public human testing is emphasized.                                                                                 | Not used as expert norming.                                                |
| Model cohort                         | Technical-report page and leaderboard report current AI system performance, with top systems below 5% at report publication.                         | Demonstrates challenge difficulty for contemporary AI.                     |
| Prior benchmark or version           | ARC-AGI-1 is predecessor and comparison point; official materials state ARC-AGI-2 is designed to address saturation/progress.                        | Places ARC-AGI-2 as harder, more fine-grained successor.                   |
| Criterion threshold or floor/ceiling | 85% challenge target, pass@2 task solvability, cost constraints, and expected split comparability.                                                   | Supports competition framing, not validated broad-AGI threshold by itself. |

Review notes: Baseline structure is unusually strong for AI benchmarks, but attempt-rule ambiguity and broad-claim scope limit interpretation.

### 3.6 Score Uncertainty and Stability

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Hierarchical, clustered, or item-level bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [x] Sensitivity analyses
- [ ] Prompt, input-perturbation, or response-format sensitivity metrics
- [ ] IRT, adaptive testing, or item-parameter precision estimates
- [ ] Not reported

Other uncertainty/stability comments: Official page states eval sets are calibrated and scores are expected to be comparable across sets within less than 1 percentage point assuming no overfitting. Full statistical details are in/behind the technical report rather than fully captured on the page.

Review notes: Split-equivalence support is useful. AI run-to-run variance remains underdocumented.

### 3.7 Metric-to-Claim Linkage

| Prompt                                                                   | Response                                                                                                                                                                                          |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Why the primary metric was chosen                                        | Exact grid matching fits ARC's task definition: infer transformation and construct correct output grid.                                                                                           |
| Whether metric floors or ceilings are documented                         | Random floor is practically near-zero; human and AI performance contrasts are documented; leaderboard cost filters are documented.                                                                |
| Whether the metric may reward non-target behavior named by the benchmark | Official materials explicitly seek to reduce brute-force search and emphasize efficiency to avoid rewarding exhaustive compute.                                                                   |
| Whether parsing, judge, or scorer validation is documented               | Exact scorer and CLI are public; parser/harness behavior is documented in code but not fully reviewed here.                                                                                       |
| Whether response-format burden is separated from the target capability   | Partially. Exact grid construction is part of the task, but serialization/interface burden, malformed-output handling, and attempt-rule ambiguity are not fully separated from reasoning ability. |
| Whether perturbation or prompt-sensitivity evidence affects the claim    | Not directly documented. Split calibration and human testing are reported, but systematic prompt, interface, response-format, or input-perturbation sensitivity evidence is limited.              |
| Whether score uncertainty affects claim interpretation                   | Yes. Split calibration helps, but AI run variance and current leaderboard uncertainty require caution.                                                                                            |
| Whether score differences are interpreted statistically                  | Official page states expected split comparability; broader statistical comparison methods are not fully public in reviewed page text.                                                             |
| Whether benchmark reports state what users should not infer              | Official materials emphasize AGI relevance but do not provide a complete non-use statement for broad AGI interpretation.                                                                          |

Review notes: The metric-to-task link is strong. The metric-to-AGI link is much weaker.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [x] Public leaderboard available
- [x] Public aggregate scores available
- [ ] Public per-domain scores available
- [x] Public per-item scores available
- [ ] Public raw model outputs available
- [ ] Public traces or logs available
- [ ] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

Other output availability/comments: Public per-item task files are available; public per-item model outcomes are not documented as available.

### 4.2 Output Name or Description

| Output                         | Description                                                                             | Public/private                                          |
| :----------------------------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| ARC Prize leaderboard          | Public cost/performance leaderboard with ARC-AGI version tabs and verification caveats. | Public web output.                                      |
| Technical report results       | Human testing and AI performance context.                                               | Public paper/report output.                             |
| Kaggle competition leaderboard | ARC Prize 2025 competition page linked from official materials.                         | Hosted; not text-accessible in this review environment. |
| Benchmarking repo results      | Local outputs from official harness, including sample random baseline.                  | User-generated public-tool output.                      |

Review notes: Current leaderboard data should be date-stamped and inspected interactively for any future score-specific claims.

### 4.3 Output Design or Presentation

- [x] Static text report
- [x] Tables
- [x] Graphs or visualizations
- [x] Leaderboard
- [x] Interactive dashboard
- [ ] Downloadable CSV or JSON
- [ ] API output
- [ ] Paper-only results

Other presentation/comments: Leaderboard page includes cost/performance scatterplot framing, but not all values are text-extracted here.

### 4.4 Output Structure

- [x] Aggregate-score based
- [x] Capability-domain based
- [ ] Task-family based
- [x] Criterion-threshold based
- [ ] Pairwise-comparison based
- [x] Rank based
- [x] Cost or efficiency adjusted
- [ ] Error-analysis based
- [ ] Trace or process based

Other output structure/comments: Capability-domain structure is narrow: ARC-style passive fluid reasoning, not broad subdomains.

### 4.5 Sensitivity to Context

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [x] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts: ARC-AGI-1, ARC-AGI-2, ARC-AGI-3 tabs; public/semi-private/private splits; Kaggle competition; verified/community leaderboard contexts.

Review notes: Context labels are helpful, but current leaderboard extraction and policy details need date-stamped inspection.

### 4.6 Development of Outputs

- [x] Based on benchmark authors' design
- [x] Based on empirical or actuarial relationships
- [x] Based on expert judgment
- [x] Based on human annotation
- [ ] Based on model-as-judge outputs
- [x] Automatically generated by benchmark platform

Other development basis/comments: Human-testing calibration and exact scoring underpin outputs; no model judge is required.

Describe origin of report content: Official ARC Prize pages, arXiv technical report, leaderboard infrastructure, Kaggle competition infrastructure, and official benchmarking code.

### 4.7 Modifiability

- [ ] Not modifiable
- [x] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

Review notes: Users can run local harness outputs; official leaderboard outputs are controlled by ARC Prize/Kaggle procedures.

### 4.8 Transparency

- [ ] Clear linkage between tasks, scores, and reported claims
- [x] Partial linkage between tasks, scores, and reported claims
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Review notes: Linkage is clear for exact-grid task success, but only partial for broad AGI/fluid-intelligence claims and current leaderboard governance.

### 4.9 Output Content

- [x] Capability descriptions
- [x] Aggregate rankings
- [ ] Subdomain comparisons
- [x] Error categories
- [ ] Examples of successes or failures
- [x] Cost, latency, or efficiency data
- [ ] Process traces
- [ ] Recommendations or interpretation notes
- [x] Warnings or caveats

Other output content/comments: Official page identifies symbolic interpretation, compositional reasoning, and contextual rule application as challenge types, but not as validated score subscores.

### 4.10 Intended Recipients

- [x] Benchmark maintainers
- [x] Model developers
- [x] AI researchers
- [x] Safety evaluators
- [x] Policy or governance actors
- [ ] Product or deployment teams
- [ ] Procurement teams
- [x] Public audience

Other recipients/comments: Competition participants and leaderboard readers are central recipients.

---

## Section 5. Benchmark Access, Artifacts, and Lifecycle

### 5.1 Supporting Information Provided

- [x] Technical report
- [ ] User guide
- [x] Repository README
- [ ] API documentation
- [ ] Dataset card
- [x] Model submission instructions
- [x] Scoring documentation
- [ ] Rubric or annotation guide
- [x] Evaluation examples
- [ ] FAQ or discussion forum
- [x] Changelog or release notes

Other supporting materials/comments: The official benchmarking repository functions as a user guide for model evaluation, even if it is not labeled that way.

### 5.2 Methods of Publication

- [x] Academic paper
- [x] Benchmark website
- [x] Git repository
- [ ] Package registry
- [ ] Dataset hosting platform
- [x] Leaderboard platform
- [x] Downloadable documents
- [x] Private distribution

Other publication methods/comments: Private distribution applies to semi-private/private evaluation sets and competition infrastructure.

### 5.3 User Requirements or Qualifications

| Requirement type                             | Requirement                                                                                                                          |
| :------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Technical skill                              | Ability to parse ARC JSON tasks, build output grids, run Python CLI/scoring, and manage solver submissions.                          |
| Model access                                 | Either local solver access or API access through supported/custom harness adapters.                                                  |
| Dataset access                               | Public GitHub access for training/evaluation; controlled access for semi-private/private sets.                                       |
| Compute or budget                            | Cost matters for official interpretation; leaderboard notes cost display limits and competition constraints require separate review. |
| Human expertise                              | Interpretation requires understanding ARC task format, exact-grid scoring, search/program-synthesis confounds, and AGI claim limits. |
| Account, license, or competition eligibility | GitHub public access for tasks; Kaggle/ARC Prize accounts and terms for competition/leaderboard submission.                          |
| Ethical, safety, or data-use obligations     | Avoid leaking public evaluation tasks into model development; respect private-set and competition rules.                             |

Other requirements/comments: The public evaluation set should not become an iterative training feedback loop, per README warning.

### 5.4 Dataset and Item Access

| Component                                      | Public | Restricted | Hidden | Not available | Evidence / notes                                                                                                                                    |
| :--------------------------------------------- | :----: | :--------: | :----: | :-----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| Training or development items                  | - [x]  |   - [ ]    | - [ ]  |     - [ ]     | 1,000 public training tasks.                                                                                                                        |
| Public evaluation items                        | - [x]  |   - [ ]    | - [ ]  |     - [ ]     | 120 public evaluation tasks.                                                                                                                        |
| Private or held-out evaluation items           | - [ ]  |   - [x]    | - [x]  |     - [ ]     | 120 semi-private and 120 private tasks are not in the repository.                                                                                   |
| Secret, encrypted, or reserve evaluation items | - [ ]  |   - [x]    | - [x]  |     - [ ]     | Semi-private/private reserves are hidden for leaderboard and competition integrity; encryption or cryptographic handling details were not reviewed. |
| Retired or archived evaluation items           | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | Changelog records corrections, but a systematic retired-task archive was not documented.                                                            |
| Answer keys or reference solutions             | - [x]  |   - [x]    | - [x]  |     - [ ]     | Public answers exist in JSON for public tasks; hidden answers exist for competition splits.                                                         |
| Metadata or annotations                        | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | Full task metadata and human-testing annotations are not public in reviewed materials.                                                              |
| Raw model outputs or logs                      | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | Public raw outputs/traces for official model runs are not documented.                                                                               |

Other access/comments: The public repository is strong for task access; hidden splits are necessary for integrity but limit independent inspection.

### 5.5 Provenance and Contamination Documentation

| Topic                                                      | Documented | Partially documented | Not documented | Evidence / notes                                                                                                                                       |
| :--------------------------------------------------------- | :--------: | :------------------: | :------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data origin or task creation                               |   - [x]    |        - [ ]         |     - [ ]      | ARC principles and ARC-AGI-2 design goals are described.                                                                                               |
| Persistent dataset or artifact identifier                  |   - [ ]    |        - [x]         |     - [ ]      | arXiv DOI and official repositories provide stable anchors; no separate dataset DOI or release tag was reviewed.                                       |
| Author or contributor qualifications                       |   - [x]    |        - [ ]         |     - [ ]      | Technical report authors and ARC Prize organization are identified.                                                                                    |
| Deduplication or overlap checks                            |   - [ ]    |        - [x]         |     - [ ]      | Brute-force susceptible tasks and prior contest-solved tasks were removed, but full overlap metrics are limited.                                       |
| Public/private split rationale                             |   - [x]    |        - [ ]         |     - [ ]      | Semi-private/private split functions are clearly described.                                                                                            |
| Contamination screening                                    |   - [x]    |        - [ ]         |     - [ ]      | Leakage probabilities, private sets, public-eval warning, and competition split are documented.                                                        |
| Canary strings or training-data warnings                   |   - [ ]    |        - [x]         |     - [ ]      | README warns not to leak evaluation tasks into algorithms; no canary string identified.                                                                |
| Memorization or `training_on_test_set` diagnostic task     |   - [ ]    |        - [ ]         |     - [x]      | Leakage warnings and hidden splits exist, but no dedicated memorization diagnostic task was documented.                                                |
| Pre-exposure or source-material searchability checks       |   - [ ]    |        - [x]         |     - [ ]      | Prior contest-solved and brute-force-susceptible tasks were reportedly removed, but full searchability evidence was not public in this review.         |
| Hash commitments, signatures, or tamper-evident audit logs |   - [ ]    |        - [ ]         |     - [x]      | No public hash commitment, signature, or tamper-evident audit-log mechanism was documented.                                                            |
| Encrypted, secret, or controlled-release item reserve      |   - [ ]    |        - [x]         |     - [ ]      | Semi-private/private reserves and competition infrastructure are documented, but detailed access-control or encryption mechanics are not fully public. |
| Refresh or rotation policy                                 |   - [ ]    |        - [x]         |     - [ ]      | Public changelog exists; longer-term refresh policy is not fully documented.                                                                           |
| Reporting of known leaks or retired items                  |   - [ ]    |        - [x]         |     - [ ]      | Changelog records task corrections; leak reporting policy is not comprehensive.                                                                        |

Other provenance/contamination comments: Official materials are unusually direct about leakage probability and split purpose, but public eval exposure remains a known risk.

### 5.6 Reproducibility Materials

- [x] Complete task data
- [ ] Complete prompt templates
- [x] Evaluation harness
- [x] Scoring code
- [x] Environment file or dependency list
- [ ] Container or reproducible environment
- [x] Version pinning
- [ ] Random seeds or deterministic settings
- [x] Raw outputs
- [ ] Reproduction script for published results
- [x] Push-button replication script or single documented command
- [x] Expected-output fixtures or smoke-test example
- [x] Continuous integration or test suite
- [ ] Public build status or equivalent passing-test signal

Other reproducibility comments: Raw outputs are available for user-generated harness runs, not necessarily for official leaderboard systems. CI/test suite is inferred from the benchmarking repository's test configuration and contribution guidance; exact CI status was not fully reviewed.

### 5.7 Maintenance and Versioning

| Topic                                                    | Response                                                                                                                                                                      |
| :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maintainer identity                                      | ARC Prize / `arcprize` GitHub organization.                                                                                                                                   |
| Version naming or release tags                           | ARC-AGI-2 main release; no repository release tag reviewed.                                                                                                                   |
| Changelog or update record                               | Public changelog records release and public-evaluation corrections.                                                                                                           |
| Issue or feedback process                                | GitHub issues and pull requests are public.                                                                                                                                   |
| Item correction process                                  | Public changelog records minor corrections to public evaluation tasks.                                                                                                        |
| Deprecated item handling                                 | Brute-force susceptible and prior-solved tasks were removed before release; public post-release corrections documented.                                                       |
| Private-set refresh policy                               | Not fully documented.                                                                                                                                                         |
| Last code-usability or harness health check              | Public repository and quickstart exist, but the last independent health check was not fully reviewed.                                                                         |
| Build, CI, or smoke-test status                          | Tests and sample tasks are present; public build status was not fully reviewed.                                                                                               |
| Saturation threshold or retirement criteria              | ARC-AGI-2 responds to ARC-AGI-1 saturation and includes an 85% challenge target, but formal retirement criteria are not fully documented.                                     |
| Retirement, deprecation, or archival policy              | Not fully documented beyond changelog and predecessor context.                                                                                                                |
| Retired-item publication or audit policy                 | Public corrections are documented; a full retired-task audit policy was not reviewed.                                                                                         |
| Score comparability across versions                      | Official page claims public/semi-private/private eval sets are calibrated and comparable within less than 1 percentage point expected, assuming no overfitting.               |
| Cohort, rolling-window, or temporal comparability policy | Partially documented through split calibration and changelog; leaderboard cohort labels, stale-score handling, and post-correction comparability need stronger public detail. |
| Long-term archival plan                                  | Not documented.                                                                                                                                                               |

Review notes: Changelog discipline is a strength. Versioned score comparability still requires careful handling because public evaluation tasks changed after release.

---

## Appendix A. General Description of the Benchmark

ARC-AGI-2 is the second Abstraction and Reasoning Corpus for Artificial General Intelligence benchmark. It consists of colored-grid transformation tasks in which a solver infers a rule from demonstration input/output pairs and produces output grids for test inputs. The public repository contains 1,000 training tasks and 120 public evaluation tasks; official materials also describe 120 semi-private and 120 private evaluation tasks. ARC-AGI-2 is designed to be easy for humans but difficult for current AI systems, resistant to brute-force search, calibrated across public/private splits, and reported with cost/efficiency metrics. Its narrowest defensible interpretation is performance on ARC-style abstract grid reasoning tasks under exact-grid scoring and specified attempt/cost conditions. Its broad AGI/general-fluid-intelligence interpretation requires substantial caution because the task family is narrow relative to full cognitive breadth.

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether ARC-AGI-2 is adequate as a measurement instrument for its intended use. This version applies the targeted `markdown/MESA EFPA template v6.md` modifications to the existing pilot evidence. It does not perform a new online source refresh; the evidence base remains the 2026-05-09 source inventory recorded in Part A.

## Information Sources

Use the materials inventoried in Part A Section 1.2 as the source base for these ratings. Official benchmark papers, websites, repositories, datasets, leaderboards, harnesses, changelogs, and maintainer statements remain the factual base. Local MESA literature and EFPA/BetterBench/Measuring what Matters/AGI-CHC sources are used only to structure evaluation criteria and broad-claim cautions.

No additional benchmark facts, leaderboard positions, release changes, or external commentary are introduced in this migrated version.

## Explanation of Ratings

All rating items use the EFPA-style scale below unless a section states otherwise. Lower ratings are assigned by reviewer judgment, considering the benchmark's intended use, claim scope, decision stakes, technical complexity, evidence quality, and consequences of misinterpretation.

Overall ratings are based on reviewer judgment rather than mechanical averaging. A single severe gap may dominate an overall rating when it undermines the intended interpretation; conversely, a narrow gap may be less consequential when the benchmark's claim is modest and clearly bounded.

### Rating Scale

| Rating  | Meaning                                                                                |
| :-----: | :------------------------------------------------------------------------------------- |
| **n/a** | This attribute is not applicable to this benchmark or its stated use.                  |
|  **0**  | Not possible to rate because no, or insufficient, information is provided.             |
|  **1**  | Inadequate for the benchmark's stated purpose or intended interpretation.              |
|  **2**  | Adequate: sufficient for cautious use, with limitations that should be stated.         |
|  **3**  | Good: clear, relevant, and mostly complete support, with no major interpretive threat. |
|  **4**  | Excellent: comprehensive, well-documented, and strongly aligned with the item anchor.  |

## General Guidance on Assigning Ratings

Ratings are anchored in the benchmark's intended interpretation, not in a generic expectation that every benchmark must supply every possible form of evidence. For descriptive gaps, the reviewer first asks what evidence would be needed to support the benchmark's actual claim.

For broad claims about intelligence, AGI, reasoning, agency, autonomy, or cross-domain competence, stronger breadth and validity evidence is required than for narrow capability claims. Isolated high performance on one task family should be treated as evidence about that task family unless the benchmark supplies a validity argument for broader interpretation.

For every rating, this migrated pilot records the evidence basis, missing evidence, rationale for the score, and cautions for interpretation. Missing documentation is treated as an evidence gap, not automatic proof of poor benchmark quality.

---

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

EFPA Section 6 asks whether the test explains its rationale, development, documentation, and item quality. MESA asks whether the benchmark defines the target phenomenon, explains why its tasks and metrics operationalize that phenomenon, documents task development, supports item quality, and gives users enough procedural information for cautious qualified use.

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition

- Rating: `3`
- Review note: Basis: ARC-AGI-2 has a clear rationale rooted in ARC-style abstract reasoning, Core Knowledge priors, and human-easy/AI-hard task design. Gap: the AGI and general-fluid-intelligence construct is not decomposed into a broad cognitive model. Rationale: good for ARC-style grid reasoning. Caution: a strong ARC rationale is not a complete AGI measurement theory.

#### 6.1.2 Summary of prior research and benchmark context

- Rating: `3`
- Review note: Basis: Official materials situate ARC-AGI-2 as a successor to ARC-AGI-1 and explain the benchmark gap around abstraction and brute-force resistance. Gap: the research context is not a full psychometric review of intelligence measurement. Rationale: prior context is good for intended technical users. Caution: AGI framing still needs separate validity support.

#### 6.1.3 Phenomenon-task-metric-claim chain

- Rating: `2`
- Review note: Basis: The narrow task-to-metric chain is explicit: infer grid transformation, produce exact grid, score success and cost. Gap: the metric-to-AGI claim chain is underdeveloped. Rationale: adequate overall because narrow support is strong and broad support is limited. Caution: exact-grid success is not a standalone general-intelligence claim.

#### 6.1.4 Task or item design

- Rating: `3`
- Review note: Basis: Grid demonstrations, test grids, exact outputs, pass criteria, and cost framing are documented. Gap: some user-facing attempt-rule wording conflicts across official materials. Rationale: task design is good for narrow abstraction measurement. Caution: attempt count must be standardized for comparison.

#### 6.1.5 Procedures for developing task or item content

- Rating: `3`
- Review note: Basis: Official materials describe new task design, removal of brute-force-susceptible tasks, controlled human testing, split calibration, and public corrections. Gap: full item-development metadata are not all public. Rationale: task-development procedure is good. Caution: hidden details limit independent audit.

#### 6.1.6 Thoroughness of the final task or item selection process

- Rating: `3`
- Review note: Basis: Public, semi-private, and private splits are described, and included tasks were human-solvable under documented criteria. Gap: full final selection records and tradeoff analyses are summarized rather than fully inspectable. Rationale: final selection appears thorough. Caution: public task corrections require version awareness.

#### 6.1.7 Quantitative evidence of task or item quality

- Rating: `2`
- Review note: Basis: Human testing, split calibration, and model difficulty evidence are summarized. Gap: detailed item-level diagnostics, full human data, uncertainty, and discrimination statistics are not fully public. Rationale: quantitative evidence is adequate but incomplete. Caution: item-level claims need stronger data.

#### 6.1.8 Adaptation, translation, or benchmark version derivation

- Rating: `2`
- Review note: Basis: ARC-AGI-2 is documented as a successor to ARC-AGI-1 with public release and changelog. Gap: equivalence with ARC-AGI-1 and implications of public task fixes are not fully resolved. Rationale: version derivation is adequate. Caution: compare ARC versions with explicit caveats.

#### 6.1.9 Overall quality of rationale, development, and task or item quality

- Rating: `2`
- Review note: Basis: Rationale and development are strong for ARC-style grid reasoning. Gap: broad AGI construct mapping and public quantitative detail are incomplete. Rationale: overall support is adequate because claim scope is ambitious. Caution: narrow task quality should not be promoted to broad AGI validity.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- Rating: `2`
- Review note: Basis: Official materials explain ARC-AGI-2's purpose, competition use, and general-fluid-intelligence framing. Gap: explicit non-use guidance for broad AGI interpretation is incomplete. Rationale: purpose documentation is adequate. Caution: public AGI language raises the burden of interpretation.

#### 6.2.2 Documentation of development process

- Rating: `3`
- Review note: Basis: Development goals, task redesign, human testing, split structure, and changelog are described. Gap: complete task-authoring and human-study records are not public. Rationale: development documentation is good for technical users. Caution: hidden details still affect auditability.

#### 6.2.3 Documentation of scoring and metrics

- Rating: `2`
- Review note: Basis: Exact-grid scoring, task format, success criteria, and harness scoring are documented. Gap: attempt-rule inconsistency and malformed-output handling need resolution. Rationale: scoring documentation is adequate but not clean. Caution: official comparisons need one authoritative scoring rule.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- Rating: `2`
- Review note: Basis: Split calibration and deterministic exact scoring support stability claims. Gap: stochastic model repeat runs, seeds, and uncertainty intervals are not comprehensively public. Rationale: reliability documentation is adequate. Caution: LLM solver results may vary.

#### 6.2.5 Documentation of validity evidence

- Rating: `2`
- Review note: Basis: Official materials present human feasibility, difficulty, brute-force resistance, and split calibration. Gap: broad validity evidence across non-ARC cognitive domains is missing. Rationale: validity documentation is adequate for narrow tasks. Caution: AGI claims need broader evidence.

#### 6.2.6 Documentation of fair use and comparability

- Rating: `2`
- Review note: Basis: Low language dependence, split design, exact scoring, and cost framing are documented. Gap: visual accessibility, human sample representativeness, and cross-system fairness are incomplete. Rationale: fair-use documentation is adequate. Caution: grid tasks are not universally accessible or broadly representative.

#### 6.2.7 Documentation of maintenance and versioning

- Rating: `3`
- Review note: Basis: Public changelog, task repository, technical report, and benchmarking repository document release and maintenance. Gap: private-set governance and competition-rule details require separate platform review. Rationale: maintenance documentation is good. Caution: public task fixes require version labels.

#### 6.2.8 Adequacy of documentation available to users

- Rating: `3`
- Review note: Basis: Official page, report, arXiv record, repositories, changelog, leaderboard, and harness give strong documentation. Gap: Kaggle text, current leaderboard details, and hidden split governance were not fully accessible in the prior review. Rationale: documentation is good for technical users. Caution: competition claims need platform-specific review.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- Rating: `2`
- Review note: Basis: Task format, repository layout, harness CLI, and split structure are documented. Gap: private platform constraints and attempt-rule wording are not fully harmonized. Rationale: setup support is adequate. Caution: official comparison requires matching split and attempt conditions.

#### 6.3.2 Scoring procedure and error handling

- Rating: `2`
- Review note: Basis: Exact scoring and harness behavior are public. Gap: malformed outputs, adapter parsing, and trial-count conflicts need clearer handling. Rationale: scoring procedure is adequate. Caution: parser and attempt differences can change scores.

#### 6.3.3 Interpretation and reporting guidance

- Rating: `2`
- Review note: Basis: Official reports explain human/model contrast, cost framing, and challenge target. Gap: broad AGI non-use guidance and uncertainty interpretation are incomplete. Rationale: interpretation support is adequate. Caution: leaderboard movement should not be equated with general intelligence.

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- Rating: `2`
- Review note: Basis: Public/private splits, competition context, cost framing, and leakage warnings are documented. Gap: exact platform terms and unsupported use cases were not fully accessible. Rationale: restrictions are adequate. Caution: competition and public-eval use need current rules.

#### 6.3.5 Technical support and implementation guidance

- Rating: `3`
- Review note: Basis: The official benchmarking repository includes quickstart, adapters, random baseline, pricing config, tests, and sample tasks. Gap: no fully reviewed release/CI status in the prior review. Rationale: technical support is good. Caution: leaderboard replication still requires matching platform conditions.

#### 6.3.6 References and supporting materials

- Rating: `3`
- Review note: Basis: Official page, technical report, arXiv record, public task repository, benchmark harness, leaderboard, Kaggle link, and changelog are linked. Gap: some platform details were not text-accessible. Rationale: supporting materials are good. Caution: cite leaderboard snapshots with date and source.

#### 6.3.7 Quality of procedural instructions

- Rating: `2`
- Review note: Basis: Procedures are adequate for skilled users and solvers. Gap: attempt-rule conflict, cost details, and hidden-platform constraints remain. Rationale: procedural quality is adequate. Caution: resolve scoring-rule ambiguity before formal comparison.

### 6.4 Overall Adequacy of Rationale and Documentation

#### 6.4 Overall adequacy of rationale and documentation

- Rating: `2`
- Review note: Basis: ARC-AGI-2 has strong rationale, materials, and development documentation for narrow grid reasoning. Gap: broad AGI framing, attempt inconsistency, and incomplete public validation details constrain interpretation. Rationale: overall Section 6 support is adequate. Caution: this rating reflects the broader stated claim scope.

Review notes:

Section 6 ratings are pulled downward by broad-claim scope and official wording inconsistency, not by lack of task artifacts.

---

## Section 7. Quality and Usability of Benchmark Artifacts

MESA evaluates benchmark artifacts: datasets, task files, prompts, rubrics, scoring code, harnesses, interfaces, access routes, setup instructions, accessibility, and usability. Artifact quality includes both what is available and whether intended users can run or inspect it without hidden procedural knowledge.

### 7.1 Quality of Benchmark Artifacts

#### 7.1.1 Dataset, task set, or evaluation environment availability

- Rating: `3`
- Review note: Basis: Public training/evaluation tasks, hidden split descriptions, and task changelog are available. Gap: semi-private/private tasks and full human-testing data are not public. Rationale: task-set availability is good for open research. Caution: public evaluation exposure can invite overfitting.

#### 7.1.2 Prompts, instructions, and input artifacts

- Rating: `2`
- Review note: Basis: JSON grid task format and model-adapter context are public. Gap: LLM prompt conventions and adapter choices vary by harness and system. Rationale: input artifacts are adequate. Caution: prompt and serialization choices can affect performance.

#### 7.1.3 Rubrics, reference answers, and response format requirements

- Rating: `2`
- Review note: Basis: Exact grid output and reference matching are clear. Gap: attempt-rule wording and malformed-output handling vary by context. Rationale: response requirements are adequate but need cleanup. Caution: official comparisons require standardized attempts and parsers.

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- Rating: `3`
- Review note: Basis: Official benchmarking repository provides CLI, adapters, scoring, sample tasks, random baseline, pricing config, and tests. Gap: no published releases and no fully reviewed CI status in the prior review. Rationale: harness quality is strong compared with many benchmarks. Caution: private leaderboard replication still depends on platform conditions.

#### 7.1.5 Interface and workflow usability

- Rating: `3`
- Review note: Basis: Public files, harness, examples, and leaderboard workflow support technical use. Gap: competition-specific workflow details were not fully text-accessible. Rationale: workflow usability is good for intended technical users. Caution: competition submissions need current platform rules.

#### 7.1.6 Accessibility across modalities, languages, and system types

- Rating: `2`
- Review note: Basis: Tasks use low language load and simple colored grids. Gap: visual-grid accessibility, exact-output serialization, and human sample representativeness are limited. Rationale: accessibility is adequate for technical users and many systems. Caution: grid-specific interface skills can affect scores.

#### 7.1.7 Licensing, use requirements, and risk warnings

- Rating: `2`
- Review note: Basis: Public task repository lists Apache-2.0 and harness repository lists MIT. Gap: Kaggle rules, ARC Prize testing policy details, and sensitive-content warnings were not fully reviewed. Rationale: licensing support is adequate for repository use. Caution: competition use requires platform terms.

#### 7.1.8 Overall quality of benchmark artifacts

- Rating: `3`
- Review note: Basis: Public data, hidden split design, harness, changelog, and leaderboard ecosystem are usable and traceable. Gap: hidden split governance and some platform details are incomplete. Rationale: overall artifact quality is good. Caution: hidden artifacts support integrity while limiting independent inspection.

Review notes:

Section 7 is strong because artifacts and harness are public and usable. Hidden split opacity is expected but should be clearly governed.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

EFPA Section 8 evaluates norms. MESA translates this into baselines, comparator cohorts, reference groups, score bands, floors and ceilings, and guidance about what score comparisons mean.

#### Figure 2: Structure of Section 8 on Baselines, Comparators, and Reference Interpretation

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- Rating: `3`
- Review note: Basis: Random baseline tooling exists, exact-grid random success is extremely low, and official materials discuss brute-force resistance. Gap: full random/search baselines by task and compute budget are not all public. Rationale: chance and floor support is good. Caution: brute-force resistance should be periodically retested.

#### 8.1.2 Human or expert baselines

- Rating: `3`
- Review note: Basis: Official human testing involved 400+ people and 1,417 tasks, with each included task solved by at least two humans under pass@2 criteria. Gap: full human data, sampling details, and uncertainty are not all public. Rationale: human baseline support is good. Caution: the sample is not a universal human norm.

#### 8.1.3 Model comparator cohort

- Rating: `2`
- Review note: Basis: Official pages report leading model performance and a public leaderboard exists. Gap: current leaderboard entries and exact model conditions were not text-extracted in the prior review. Rationale: model comparator support is adequate and date-sensitive. Caution: do not cite rankings without a fresh snapshot.

#### 8.1.4 Historical, version, or benchmark-family comparators

- Rating: `2`
- Review note: Basis: ARC-AGI-2 is positioned relative to ARC-AGI-1 and prior AI performance. Gap: cross-version comparability and historical linking are not fully validated. Rationale: benchmark-family comparator support is adequate. Caution: ARC-AGI-1 and ARC-AGI-2 scores should not be treated as interchangeable.

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- Rating: `2`
- Review note: Basis: 85% challenge target, cost constraints, pass@2 solvability, and split calibration are documented. Gap: 85% is not validated as a psychometric AGI threshold and attempt wording conflicts. Rationale: threshold support is adequate for competition use. Caution: reaching a challenge target would not alone establish AGI.

#### 8.1.6 Representativeness of reference groups

- Rating: `2`
- Review note: Basis: Human testing and model cohorts provide useful references. Gap: human sample demographics, task sampling representativeness, and model cohort coverage are incomplete. Rationale: reference groups are adequate but not norm-like. Caution: avoid treating them as population norms.

#### 8.1.7 Currency and maintenance of baseline evidence

- Rating: `2`
- Review note: Basis: Public leaderboard and changelog support maintenance. Gap: current model-comparator currency, hidden split governance, and baseline refresh procedures are only partly public. Rationale: baseline currency is adequate. Caution: leaderboard and cost comparisons need date labels.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

#### 8.2 Overall adequacy of baselines and reference interpretation

- Rating: `3`
- Review note: Basis: Random baseline, human testing, split calibration, cost framing, and model difficulty evidence are meaningful. Gap: current leaderboard details and broad AGI threshold validity are incomplete. Rationale: baseline support is good for narrow ARC-style interpretation. Caution: broad intelligence interpretation remains limited.

Review notes:

Baseline design is one of ARC-AGI-2's strengths.

---

## Section 9. Reliability, Precision, and Score Stability

EFPA Section 9 evaluates reliability and precision. MESA applies this to run-to-run stability, prompt and environment sensitivity, scorer or judge reliability, parser behavior, uncertainty reporting, and whether reported differences are meaningful.

#### Figure 3: Structure of Section 9 on Reliability, Precision, and Score Stability

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- Rating: `2`
- Review note: Basis: Exact scoring, split calibration, and benchmark harness provide some reliability evidence. Gap: stochastic model variance, seed policies, and full uncertainty detail are incomplete. Rationale: reliability coverage is adequate. Caution: coverage differs between deterministic solvers and LLM systems.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- Rating: `2`
- Review note: Basis: Exact-grid scoring is deterministic once submissions exist, and benchmarking configs can specify model settings. Gap: repeat-run evidence for stochastic systems is not comprehensive. Rationale: run-stability support is adequate. Caution: LLM solver runs may vary.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- Rating: `2`
- Review note: Basis: Official materials state split calibration and expected comparability within less than 1 percentage point under assumptions. Gap: detailed intervals and model-comparison uncertainty are not fully public. Rationale: uncertainty support is adequate. Caution: leaderboard differences should be interpreted with uncertainty.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- Rating: `3`
- Review note: Basis: Exact reference matching reduces scorer ambiguity and the harness implements scoring. Gap: malformed-output parser reliability and adapter edge cases need more documentation. Rationale: automated scoring reliability is good for valid submissions. Caution: parser failures can still create avoidable errors.

#### 9.3.2 Human rater or expert scorer agreement

- Rating: `2`
- Review note: Basis: Human testing supports solvability and calibration. Gap: detailed human agreement, sampling, and calibration statistics are incomplete. Rationale: human-rater evidence is adequate. Caution: human feasibility is not the same as detailed rater reliability.

#### 9.3.3 Model-as-judge reliability and validity checks

- Rating: `n/a`
- Review note: Basis: ARC-AGI-2 uses exact-grid reference matching rather than model-as-judge scoring. Gap: not applicable to the benchmark's scoring method. Rationale: model-as-judge reliability should not be rated here. Caution: parser and exact-scorer reliability remain relevant under 9.3.1.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- Rating: `2`
- Review note: Basis: Task format is stable and prompts are adapter-dependent rather than inherent to the benchmark. Gap: prompt/serialization sensitivity for LLM adapters is not comprehensively tested. Rationale: prompt stability is adequate but system-dependent. Caution: report adapter and prompt details.

#### 9.4.2 Form, split, version, or refresh equivalence

- Rating: `2`
- Review note: Basis: Public/semi-private/private split calibration and changelog support form/version control. Gap: public task corrections and attempt-rule inconsistency complicate comparability. Rationale: version stability is adequate. Caution: scores before and after fixes may not be fully comparable.

#### 9.4.3 Execution environment and dependency stability

- Rating: `2`
- Review note: Basis: Public harness and configuration files support execution consistency. Gap: provider endpoints, costs, dependencies, and private platform conditions may drift. Rationale: environment stability support is adequate. Caution: report runtime, dependency, and pricing assumptions.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- Rating: `2`
- Review note: Basis: Split calibration, cost framing, and exact scoring support meaningful comparison. Gap: uncertainty intervals and significance tests for current model differences are incomplete. Rationale: statistical comparison quality is adequate. Caution: small leaderboard differences need caution.

### 9.6 Overall Reliability, Precision, and Score Stability

#### 9.6 Overall reliability, precision, and score stability

- Rating: `2`
- Review note: Basis: Deterministic scoring and split calibration are strengths. Gap: stochastic repeat runs, version corrections, parser handling, and uncertainty reporting remain incomplete. Rationale: overall reliability and precision are adequate. Caution: broad comparisons need matched attempts, split, and cost conditions.

Review notes:

Reliability is stronger than HLE on scorer determinism but still limited for stochastic models and broad leaderboard comparisons.

---

## Section 10. Validity Evidence

EFPA Section 10 evaluates validity. MESA focuses on the phenomenon-task-metric-claim chain: whether the benchmark content, internal structure, scoring, relations with other evidence, contamination controls, and public claims support the intended interpretation.

#### Figure 4: Structure of Section 10 on Validity Evidence

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- Rating: `2`
- Review note: Basis: ARC tasks are carefully designed around abstract grid reasoning, symbolic interpretation, composition, and contextual rules. Gap: representativeness for broad fluid intelligence or AGI is not established. Rationale: content support is adequate overall because the task family is narrow relative to claims. Caution: grid abstraction is a narrow cognitive slice.

#### 10.1.2 Construct breadth and sub-ability coverage

- Rating: `1`
- Review note: Basis: Official materials discuss abstraction, symbolic interpretation, compositional reasoning, and contextual rule application. Gap: no broad cognitive battery or CHC-style coverage across language, memory, knowledge, agency, social cognition, or embodiment. Rationale: construct breadth support is inadequate for broad AGI interpretation. Caution: ARC can be AGI-relevant without being a full AGI test.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- Rating: `1`
- Review note: Basis: Official materials identify challenge types and split structure. Gap: no validated dimensionality, subscales, or latent structure. Rationale: internal-structure evidence is weak. Caution: example categories should not be treated as validated dimensions.

#### 10.2.2 Item or task behavior across the score scale

- Rating: `1`
- Review note: Basis: Human solvability and model difficulty are summarized. Gap: item behavior across the score scale, difficulty bands, and discrimination are not fully public. Rationale: item-behavior evidence is limited. Caution: score-scale interpretation remains coarse.

#### 10.2.3 Failure modes and error analysis

- Rating: `1`
- Review note: Basis: Official materials describe challenge types, human/AI contrast, and some task filtering. Gap: no systematic error analysis separates intended abstraction difficulty from interface, search, attempt-count, exact-format, or solver-architecture artifacts. Rationale: failure-mode evidence is weak. Caution: ARC failures should not automatically be read as broad cognitive failures.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- Rating: `3`
- Review note: Basis: Exact-grid scoring directly matches task success, and cost/efficiency addresses brute-force confounding. Gap: attempt-rule inconsistency and malformed-output handling remain. Rationale: metric validity is good for narrow task success. Caution: attempts and cost estimates must be standardized.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- Rating: `2`
- Review note: Basis: Brute-force-resistant task design, hidden splits, and cost framing target shortcut risks. Gap: full search baselines, solver-specific tuning risks, and public-eval overuse are not fully controlled. Rationale: shortcut sensitivity is adequately addressed. Caution: public evaluation should not become iterative development feedback.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- Rating: `2`
- Review note: Basis: Human baseline, ARC-AGI-1 comparison, model cohort difficulty, and leaderboard provide relational support. Gap: relations to non-ARC cognitive tasks and real-world adaptive behavior are limited. Rationale: relational evidence is adequate for challenge difficulty. Caution: hard-for-AI and easy-for-humans is not enough to establish AGI.

#### 10.4.2 Convergent and discriminant evidence

- Rating: `1`
- Review note: Basis: Some relation to ARC-AGI-1 and current models is documented. Gap: convergent and discriminant validation across independent constructs is sparse. Rationale: convergent/discriminant evidence is weak. Caution: ARC-specific performance may not generalize.

#### 10.4.3 Ecological or predictive relevance

- Rating: `1`
- Review note: Basis: ARC-AGI-2 is framed as AGI-relevant. Gap: ecological or predictive links to broad adaptive behavior, agency, or real-world performance are not established. Rationale: ecological support is weak. Caution: do not infer broad real-world intelligence from ARC score alone.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- Rating: `3`
- Review note: Basis: Semi-private/private splits, leakage rationale, competition structure, public-eval warning, and brute-force-resistant task design are strong controls. Gap: full private governance and ongoing leak metrics are not public. Rationale: contamination control is good. Caution: public evaluation tasks should not be overused.

#### 10.5.2 Gameability and benchmark-specific tuning controls

- Rating: `3`
- Review note: Basis: Hidden splits, cost constraints, brute-force resistance, and testing-policy links address gameability. Gap: detailed private-set enforcement and ongoing leak monitoring are incomplete. Rationale: gameability controls are good. Caution: competition incentives require continuous governance.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- Rating: `1`
- Review note: Basis: Official materials use AGI, general artificial intelligence, psychometric intelligence test, and general-fluid-intelligence language. Gap: the task family does not support that breadth by itself. Rationale: stated broad claims exceed the available validity evidence. Caution: narrow ARC success should not be converted into broad cognitive conclusions.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- Rating: `1`
- Review note: Basis: ARC-AGI-2 is explicitly AGI-framed. Gap: no evidence across language, knowledge, memory, planning, agency, embodiment, social cognition, or real-world transfer. Rationale: broad AGI support is inadequate as standalone evidence. Caution: use it only as one narrow component in a broader portfolio.

### 10.7 Overall Validity Support

#### 10.7 Overall validity support

- Rating: `2`
- Review note: Basis: ARC-AGI-2 is strong for exact-grid abstraction and contamination-resistant competition use. Gap: internal structure, failure-mode analysis, broad construct breadth, ecological relevance, and claim proportionality are weak. Rationale: overall validity is adequate only under a bounded interpretation. Caution: broad AGI framing should be softened or separately validated.

Review notes:

ARC-AGI-2 is strong as an ARC-style abstract reasoning benchmark and weak as standalone broad-intelligence measurement.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

EFPA Section 11 evaluates fairness and acceptability. MESA applies this to cross-system comparability, access conditions, language, domain and modality coverage, evaluation-condition fairness, and guidance about appropriate use and non-use.

#### Figure 5: Relevant Ratings for Fair Use, Comparability, and Appropriate Use from Other Sections

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- Rating: `2`
- Review note: Basis: The construct is relevant for systems that can solve visual grid transformation tasks. Gap: relevance across broader system classes, human groups, languages, and cognitive contexts is limited. Rationale: construct relevance is adequate for ARC-style benchmarking. Caution: broader fairness claims need separate evidence.

#### 11.1.2 Documentation of fair-use considerations

- Rating: `2`
- Review note: Basis: Leakage warnings, split design, cost framing, and public materials support fair-use documentation. Gap: accessibility, AGI non-use, and competition-rule details are incomplete. Rationale: fair-use documentation is adequate. Caution: public AGI framing may invite overinterpretation.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- Rating: `2`
- Review note: Basis: Low language dependence and public JSON tasks make the benchmark broadly technical-user accessible. Gap: visual-grid accessibility and exact-output serialization can disadvantage some systems and users. Rationale: inclusive design is adequate. Caution: accessibility is not fully analyzed.

#### 11.2.2 Domain, language, modality, and subgroup coverage

- Rating: `2`
- Review note: Basis: The task family minimizes language but focuses on visual grids. Gap: domain, modality, subgroup, and non-grid cognitive coverage are limited. Rationale: coverage is adequate for ARC tasks, not broad cognition. Caution: fairness across abilities or modalities should not be assumed.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- Rating: `2`
- Review note: Basis: Exact scoring, calibrated splits, and benchmarking configs support comparison. Gap: attempt-rule inconsistency, cost-estimation variation, and hidden-platform constraints remain. Rationale: cross-system comparability is adequate. Caution: compare systems only under matched attempts, cost, and split conditions.

#### 11.3.2 Access, compute, tooling, and API or local comparability

- Rating: `2`
- Review note: Basis: Public data and harness support local/API evaluation; cost framing improves transparency. Gap: private competition infrastructure, API pricing changes, and compute budgets require current review. Rationale: access comparability is adequate. Caution: cost-aware scores are fair only when pricing and runtime are standardized.

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- Rating: `2`
- Review note: Basis: Public changelog, public/semi-private/private split calibration, and leaderboard infrastructure support some temporal interpretation. Gap: post-correction comparability, stale-score handling, leaderboard cohort labels, and archival rules are not fully documented in the reviewed materials. Rationale: temporal comparability is adequate for cautious date-stamped use. Caution: cite benchmark version, split, leaderboard date, and attempt rule with every score.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- Rating: `1`
- Review note: Basis: Human testing and low language dependence offer partial context. Gap: differential performance or bias analysis across groups, interfaces, modalities, or solver types is limited. Rationale: bias evidence is weak. Caution: fairness claims should be modest.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- Rating: `1`
- Review note: Basis: Split calibration and exact scoring are documented. Gap: reliability and validity across human subgroups, system classes, and contexts are not established. Rationale: subgroup/context evidence is weak. Caution: performance differences may reflect interface or solver constraints.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- Rating: `2`
- Review note: Basis: Public-eval leakage warnings, private splits, testing policy links, and leaderboard caveats exist. Gap: broad AGI non-use guidance is incomplete. Rationale: appropriate-use guidance is adequate. Caution: use as narrow AGI-relevant evidence, not standalone AGI proof.

#### 11.5.2 Release rules and sensitive-content handling

- Rating: `2`
- Review note: Basis: Hidden splits, public changelog, testing links, and repository licenses exist. Gap: competition rules, sensitive-content handling, and private-set governance were not fully reviewed. Rationale: release and restriction support is adequate. Caution: competition claims require platform terms.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

#### 11.6 Overall fair use, comparability, and appropriate use

- Rating: `2`
- Review note: Basis: ARC-AGI-2 is usable for technical competition and research comparisons. Gap: accessibility, subgroup fairness, broad-claim use, attempt consistency, and platform constraints remain. Rationale: fair use and comparability are adequate. Caution: public AGI interpretation needs stronger safeguards.

Review notes:

Fair use is good for technical competition/research contexts and weaker for public AGI interpretation.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

EFPA Section 12 evaluates digitally generated reports. MESA applies that logic to AI benchmark outputs: paper tables, scorecards, leaderboards, dashboards, downloadable result files, raw traces, public claims, and score interpretations.

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or result artifact scope

- Rating: `3`
- Review note: Basis: Official page, technical report, arXiv, public leaderboard, Kaggle link, repository, and harness outputs provide broad reporting coverage. Gap: current leaderboard values and competition details were not fully text-accessible in the prior review. Rationale: report scope is good. Caution: score-specific claims need a current snapshot.

#### 12.1.2 Score granularity and level of detail

- Rating: `2`
- Review note: Basis: Split counts, human/AI contrast, cost framing, and leaderboard categories are documented. Gap: uncertainty intervals, raw score distributions, and detailed version labels are incomplete. Rationale: score granularity is adequate. Caution: public task corrections and hidden splits require version discipline.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- Rating: `2`
- Review note: Basis: Reports include split, cost, and model-performance context. Gap: uncertainty, exact conditions, current leaderboard metadata, and version labels are incomplete. Rationale: reporting trace labels are adequate. Caution: date and configuration should accompany any score citation.

#### 12.2.2 Reproducibility and traceability of reported scores

- Rating: `2`
- Review note: Basis: Public tasks, harness, and scoring code support partial traceability. Gap: official raw submissions, traces, and per-item model outcomes are not documented as public. Rationale: reproducibility and traceability are adequate but incomplete. Caution: independent error analysis of leaderboard systems is constrained.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- Rating: `2`
- Review note: Basis: Reports link scores to ARC-style reasoning and AGI progress. Gap: broad AGI claim limits are not sufficiently explicit. Rationale: linkage is adequate for narrow task claims and weak for broad public claims. Caution: leaderboard movement should not be equated with general intelligence.

#### 12.3.2 Raw outputs, per-item data, or trace availability

- Rating: `1`
- Review note: Basis: Public task files and local user-generated outputs are available. Gap: official raw model outputs, submissions, traces, and per-item outcomes are not documented. Rationale: trace availability is limited. Caution: independent analysis of system errors is constrained.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- Rating: `2`
- Review note: Basis: Reports include some caveats about leakage, cost, and splits. Gap: fairness, accessibility, and coverage limits are not fully foregrounded. Rationale: report fairness is adequate. Caution: public AGI language can be misleading without limitations.

#### 12.4.2 Acceptability and usability for intended audiences

- Rating: `2`
- Review note: Basis: Official reports, pages, and repositories are accessible to technical audiences and partially to public audiences. Gap: competition details and uncertainty may be difficult to inspect. Rationale: usability is adequate. Caution: non-expert readers need stronger interpretive guardrails.

#### 12.4.3 Public communication and leaderboard governance

- Rating: `2`
- Review note: Basis: Leaderboard, competition links, changelog, and testing policy references provide governance signals. Gap: current leaderboard exports, version discipline, eligibility, and broad-claim governance are incomplete. Rationale: public communication governance is adequate but not comprehensive. Caution: cite leaderboard date and rules.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

#### 12.5 Overall quality of reports, leaderboards, dashboards, and public claims

- Rating: `2`
- Review note: Basis: ARC-AGI-2 has a mature reporting ecosystem with official pages, technical report, repositories, and leaderboard. Gap: uncertainty, raw traces, current platform details, and AGI claim limits are incomplete. Rationale: overall reporting quality is adequate. Caution: distinguish ARC task success from broad AGI.

Review notes:

The reporting ecosystem is mature but public communication should more sharply distinguish ARC task success from broad AGI.

---

## Final Evaluation

### Evaluative Report of the Benchmark

ARC-AGI-2 is a strong benchmark for ARC-style abstract grid reasoning. It has a clear task format, public data, hidden competition splits, controlled human testing, explicit attention to efficiency, an official benchmarking harness, a public changelog, and a leaderboard ecosystem. Its strongest measurement qualities are task clarity, exact scoring, human feasibility testing, split calibration, contamination controls, and public reproducibility materials.

Its main weakness is claim proportionality. Official materials repeatedly use AGI, general artificial intelligence, psychometric intelligence test, and general fluid intelligence language. ARC-AGI-2 provides meaningful evidence about a narrow family of visual/structured abstraction tasks, but it does not cover the breadth of abilities normally needed for broad AGI or CHC-style cognitive interpretation: language, knowledge, memory, planning, agency, social cognition, embodiment, and real-world transfer are mostly outside scope. The two-versus-three-trial inconsistency also needs correction because it affects success criteria and human/model comparability.

Known ongoing development is represented by the ARC Prize leaderboard and competition ecosystem, public repositories, and changelog activity. These support maintenance and continued use, but future review should verify private-set governance, leaderboard exportability, score uncertainty, post-correction comparability, and retirement or archival policy.

### Conclusions

ARC-AGI-2 can support cautious claims about performance on exact-grid abstraction tasks designed to be easy for humans and difficult for current AI systems. It can also be an AGI-relevant research signal if interpreted as one narrow component of a broader evaluation portfolio. It should not be used alone as proof of AGI, general fluid intelligence, human-like cognition, or broad cognitive versatility. Responsible use requires technical benchmark literacy, understanding of exact-grid scoring and solver constraints, and enough measurement-validity expertise to separate narrow ARC task success from broad cognitive or AGI claims.

### Recommendations

Use ARC-AGI-2 for abstract reasoning research, competition benchmarking, and cost-aware solver comparison under matched evaluation conditions. Report split, attempt count, cost assumptions, model configuration, solver type, data version, and leaderboard date. Maintainers should resolve the attempt-rule inconsistency, publish clearer non-use guidance for AGI claims, provide more transparent current leaderboard exports, and document private-set governance and score uncertainty.

### Summary of Ratings

| Section or area                                            | Rating (`n/a`, `0`-`4`) |
| :--------------------------------------------------------- | :---------------------: |
| Section 6. Rationale, documentation, and task/item quality |           `2`           |
| Section 7. Benchmark artifacts and usability               |           `3`           |
| Section 8. Baselines and comparators                       |           `3`           |
| Section 9. Reliability and precision                       |           `2`           |
| Section 10. Validity support                               |           `2`           |
| Section 11. Fair use and comparability                     |           `2`           |
| Section 12. Reports, leaderboards, and public claims       |           `2`           |
| Construct definition and claim scope                       |           `2`           |
| Scoring validity                                           |           `3`           |
| Reproducibility and implementation transparency            |           `3`           |
| Contamination and gameability controls                     |           `3`           |
| Maintenance, versioning, and retirement readiness          |           `2`           |
| Temporal comparability, if relevant                        |           `2`           |
| Overall claim-bounded measurement quality                  |           `2`           |

Review notes: Overall quality would be `3` for narrow ARC-style grid reasoning alone. It is `2` for the benchmark's broader AGI/general-fluid-intelligence framing because the construct scope exceeds the task family.

### Gap Register

| Gap                                                                        | Affected rating(s)        | Why it matters                                                                                        | Needed for a higher rating                                                                             |
| :------------------------------------------------------------------------- | :------------------------ | :---------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| Official attempt rule conflicts between pass@2/two trials and three trials | 3, 6, 8, 9, 10, 11, final | Changes task success and comparability between humans and AI systems.                                 | Single authoritative attempt rule across official page, README, harness, Kaggle, and leaderboard.      |
| Broad AGI/general-fluid-intelligence construct is not fully mapped         | 2.18, 10, 12, final       | Prevents standalone broad-intelligence interpretation.                                                | Explicit construct map, non-use guidance, and validation across broader ability domains.               |
| Current ARC-AGI-2 leaderboard values were not text-accessible here         | 8, 12                     | Limits date-specific model comparison.                                                                | Downloadable or text-accessible leaderboard snapshot with model/config/cost metadata.                  |
| Temporal comparability and retirement policy are incomplete                | 5, 11, 12, maintenance    | Public corrections, hidden cohorts, and leaderboard updates can affect score comparability over time. | Clear cohort labels, stale-score rules, archival policy, retired-task policy, and retirement criteria. |
| Kaggle competition page did not render reviewable text in this environment | 1.2, 5, 11, 12            | Competition rules can affect valid interpretation.                                                    | Reviewable copy of rules, compute limits, submissions, scoring, and split use.                         |
| Raw official model outputs and traces are not public                       | 9, 10, 12                 | Limits error analysis and scorer/harness validation.                                                  | Public or controlled audit access to outputs, submissions, logs, and per-task outcomes.                |
| Human-testing details are summarized rather than fully inspectable         | 8, 9, 10, 11              | Human baseline strength depends on sampling and procedures.                                           | Full human-study methods, demographics, attempt logs, uncertainty, and item-level solve data.          |

Other gaps/comments: These gaps do not erase ARC-AGI-2's value as an abstract-reasoning benchmark. They limit the broader AGI interpretation.

### Reviewer Caution Statement

The narrowest defensible interpretation is: ARC-AGI-2 measures system performance on exact-grid abstraction tasks requiring few-shot transformation induction under specified split, attempt, and cost conditions. It is useful AGI-relevant evidence only as one narrow reasoning component inside a broader evaluation portfolio. It is not, by itself, a validated measure of AGI, general fluid intelligence, human-like cognition, or broad cross-domain cognitive ability.
