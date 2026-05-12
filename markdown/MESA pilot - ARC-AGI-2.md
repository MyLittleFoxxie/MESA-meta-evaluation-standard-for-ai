# MESA Pilot Review: ARC-AGI-2

This pilot applies `markdown/MESA EFPA template v5.md` to ARC-AGI-2. It uses current official ARC materials available on 2026-05-09 and keeps the Part A / Part B boundary explicit. Part A describes what the official materials state, including unresolved inconsistencies. Part B assigns ratings using Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

Before completing the review, inspect the most authoritative available materials. Prefer official benchmark papers, websites, repositories, data hosts, leaderboards, harnesses, changelogs, and maintainer statements. Independent commentary should be used only for context, external critique, or disputed claims, and should not replace official benchmark facts.

Documentation status summary for Part A:

- [x] Documented: benchmark name, official page, technical report, arXiv record, public task repository, public training and public evaluation task counts, semi-private/private split counts, exact-grid task format, human solvability criterion, controlled human testing, cost/efficiency emphasis, public leaderboard page, public changelog, and official benchmarking repository.
- [x] Partially documented: current leaderboard values in text-accessible form, Kaggle competition rules from the page as rendered in this environment, exact current private-set governance, cost-estimation methods for all systems, raw model outputs, and split-equivalence statistics beyond official summary claims.
- [x] Unclear from available materials: whether the user-facing attempt rule should be read as exactly two trials/pass@2 everywhere or three trials in the repository task-interface wording. This review treats that as an official-material inconsistency and a gap to resolve, not as a settled fact.

Part B rating scale used here:

| Rating | Meaning |
| :--- | :--- |
| `n/a` | Criterion is not applicable to this benchmark or intended use. |
| `0` | Cannot rate because the available basis is insufficient. |
| `1` | Inadequate support or practice for the intended interpretation. |
| `2` | Adequate for cautious use within a clearly bounded interpretation. |
| `3` | Good support or practice, with meaningful but non-fatal gaps. |
| `4` | Excellent support or practice, comprehensive and well matched to the intended use. |

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

Section 1 identifies the review event, benchmark identity, and official materials inspected.

### 1.1 Review Information

| Prompt | Response |
| :--- | :--- |
| Reviewer | MESA pilot reviewer |
| Date of current review | 2026-05-09 |
| Date of previous review, if applicable | Not applicable. |
| Review scope | Full Part A/B pilot for ARC-AGI-2 using current official online ARC Prize and GitHub materials. |
| Review boundary | Official ARC materials first; local MESA literature used only for Part B rating criteria and AGI/CHC caution. |

Review notes: This pilot treats official-source inconsistencies as gaps. It does not resolve them by inference.

### 1.2 Information Sources Reviewed

| Material type | Artifact reviewed | Access date | Role in review |
| :--- | :--- | :--- | :--- |
| Benchmark website or documentation hub | [ARC-AGI-2 official page](https://arcprize.org/arc-agi/2) | 2026-05-09 | Primary public description of goals, dataset structure, calibration, efficiency measurement, and changelog summary. |
| Official paper or technical report | [ARC-AGI-2 technical report page](https://arcprize.org/blog/arc-agi-2-technical-report) | 2026-05-09 | Official launch/technical-report page with design goals, human testing, model-score context, and competition links. |
| Official paper or technical report | [arXiv:2505.11831](https://arxiv.org/abs/2505.11831) | 2026-05-09 | Versioned technical report record; v2 last revised 2026-01-15. |
| Repository | [arcprize/ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) | 2026-05-09 | Public task data repository, README, license, file format, task success criterion, and public changelog. |
| Repository | [arcprize/arc-agi-benchmarking](https://github.com/arcprize/arc-agi-benchmarking) | 2026-05-09 | Official benchmarking harness linked from official materials; supports model adapters, scoring, sample tasks, random baseline, and cost configuration. |
| Leaderboard, dashboard, or results page | [ARC Prize leaderboard](https://arcprize.org/leaderboard) | 2026-05-09 | Public leaderboard page with ARC-AGI-2 tab, cost/performance framing, and verification caveats. |
| Release log, changelog, or maintenance record | [ARC-AGI-2 changelog](https://github.com/arcprize/ARC-AGI-2/blob/main/changelog.md) | 2026-05-09 | Public task release and public-evaluation update record. |
| Leaderboard, dashboard, or results page | [ARC Prize 2025 Kaggle competition](https://www.kaggle.com/competitions/arc-prize-2025) | 2026-05-09 | Official competition page linked from ARC Prize; content did not render text in this environment, so details remain a gap here. |
| Contextual literature | `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`; `markdown/Papers/betterbench.md`; `markdown/Papers/Measuring_what_Matters.md`; `markdown/Papers/A_Definition_of_AGI.md` | 2026-05-09 | Used only for MESA Part B rating criteria and broad-claim caution. |

Other materials/comments: Official ARC pages link the ARC Prize testing policy and competition infrastructure; this pilot records them as official artifacts but does not rely on inaccessible page details.

### 1.3 Benchmark Information

| Prompt | Response |
| :--- | :--- |
| Benchmark name | Abstraction and Reasoning Corpus for Artificial General Intelligence v2 |
| Short name or acronym | ARC-AGI-2 |
| Benchmark version, edition, or release | ARC-AGI-2 public release; changelog records a 2025-03-24 release of 1,360 tasks and public-evaluation updates on 2025-04-14 and 2025-04-17. |
| Original benchmark name, if this is an adaptation | Successor to ARC-AGI-1 / original ARC. |
| Benchmark creators or authors | Francois Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard are listed on arXiv. ARC Prize, Inc. hosts the official materials. |
| Current maintainers | ARC Prize / `arcprize` GitHub organization. |
| Host organization, publisher, or distributor | ARC Prize, Inc.; GitHub task repository; Kaggle competition infrastructure; arXiv technical report. |
| Date of original release | Official changelog records ARC-AGI-2 release on 2025-03-24. |
| Date of current release or revision | Public task changelog updates are dated 2025-04-14 and 2025-04-17; arXiv v2 is dated 2026-01-15. |
| License or access terms | ARC-AGI-2 task repository lists Apache-2.0 license. Official benchmarking repository lists MIT license. Kaggle and ARC Prize testing terms require separate review. |
| Persistent identifier, citation, or DOI | arXiv identifier `2505.11831` and DOI `10.48550/arXiv.2505.11831`. |

Review notes: The benchmark is explicitly positioned as AGI-relevant and as a general-fluid-intelligence measure. This creates a high validity burden in Part B.

### 1.4 Public Artifacts

| Artifact | URL or location | Access status | Review detail |
| :--- | :--- | :--- | :--- |
| Paper or technical report | [arXiv:2505.11831](https://arxiv.org/abs/2505.11831); [technical report page](https://arcprize.org/blog/arc-agi-2-technical-report) | Public | Technical report and official summary are available. |
| Benchmark website | [ARC-AGI-2 official page](https://arcprize.org/arc-agi/2) | Public | Documents goals, task structure, calibration, efficiency, and links. |
| Code repository | [arcprize/ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) | Public | Contains public training/evaluation JSON tasks, README, license, and changelog. |
| Evaluation harness | [arcprize/arc-agi-benchmarking](https://github.com/arcprize/arc-agi-benchmarking) | Public | Provides CLI, provider adapters, random baseline, scoring, sample tasks, and config path. |
| Dataset or task set | `data/training` and `data/evaluation` in the public GitHub repository | Public plus hidden/private components | Public repository contains 1,000 training tasks and 120 public evaluation tasks; semi-private and private sets are not public. |
| Prompt set | Benchmarking repository and technical report context | Partially public | ARC itself is grid input/output; model prompting details depend on harness/model adapter. |
| Rubric or scoring guide | README task-success criterion and benchmarking scoring code | Public, with inconsistency | Exact-grid success is clear, but official materials conflict between two-trial and three-trial wording. |
| Leaderboard or result display | [ARC Prize leaderboard](https://arcprize.org/leaderboard); Kaggle competition link | Public/hosted | Public page has ARC-AGI-2 tab and cost/performance framing; current ARC-AGI-2 entries were not text-extracted here. |
| Release log or changelog | [changelog.md](https://github.com/arcprize/ARC-AGI-2/blob/main/changelog.md) | Public | Records release and public-evaluation task fixes. |
| Contact, issue channel, or feedback route | GitHub issues; ARC Prize website/community links | Public | Repository issue channel and ARC Prize community links exist. |

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

| Component | Description |
| :--- | :--- |
| Claimed construct or phenomenon | Abstract reasoning and problem solving at higher levels of fluid intelligence, with AGI-progress relevance. |
| Construct subcomponents | Few-shot grid transformation induction, symbolic interpretation, compositional reasoning, contextual rule application, efficient search/generalization, and output-grid construction. |
| Task families or subdomains | ARC-style colored-grid tasks with demonstration input/output pairs and hidden test input grids. Official examples highlight symbolic interpretation, compositional reasoning, and contextual rule application. |
| Task sampling or selection logic | Tasks are designed to require minimal prior knowledge/Core Knowledge priors, be feasible for humans, resist brute-force search, and challenge current AI systems. |
| Splits or partitions | 1,000 public training tasks, 120 public evaluation tasks, 120 semi-private evaluation tasks, and 120 private evaluation tasks. |
| Primary score | Task success / accuracy under an exact-grid criterion, with pass@2 wording in official page and two-trial wording in README. |
| Subscores | Public, semi-private, private, leaderboard/competition scores, and cost/performance views. |
| Derived or aggregate scores | Efficiency/cost metrics are part of official reporting; leaderboard filters and cost-per-task framing are used. |
| Qualitative labels or bands | The official page asks whether a system can reach 85% accuracy; this is a challenge/competition target rather than a validated psychometric band. |
| Claim boundaries or caveats | ARC-AGI-2 is a grid-abstraction benchmark. It is AGI-relevant by author framing, but it does not measure full AGI breadth such as language, memory, embodiment, social cognition, tool autonomy, broad knowledge, or real-world planning. |

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

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing | Status detail |
| :--- | :---: | :---: | :---: | :--- |
| Language support | - [x] | - [ ] | - [ ] | Tasks are primarily visual/grid based; language may be used by LLM prompts but is not the target task content. |
| Context length | - [ ] | - [x] | - [ ] | Tasks are small JSON grids; no long-context requirement is central. |
| Multimodal input support | - [ ] | - [x] | - [ ] | Systems must perceive or parse grid patterns. |
| Structured output support | - [ ] | - [x] | - [ ] | Output grids must be exact. |
| Tool access | - [ ] | - [x] | - [ ] | Solver architecture may use search/code/tools; competition contexts may constrain this. |
| Browser or internet access | - [x] | - [ ] | - [ ] | Not required for task solving; browser only supports human interface and hosted pages. |
| Code execution | - [ ] | - [x] | - [ ] | Programmatic solvers and benchmarking harnesses require code execution. |
| Memory or persistent state | - [ ] | - [ ] | - [x] | Training/adaptation assumptions vary; persistent state policy is not fully specified in all contexts. |
| API compatibility | - [ ] | - [x] | - [ ] | Benchmarking harness supports multiple provider APIs and custom adapters. |
| Latency or time budget | - [ ] | - [ ] | - [x] | Time/cost constraints vary by leaderboard and competition context. |
| Cost or compute budget | - [ ] | - [x] | - [ ] | Official reporting emphasizes cost; leaderboard notes cost-related display constraints. |

Other requirements/comments: Systems need reliable grid parsing, grid generation, and exact-output submission. Human interface use is not the same as model-harness evaluation.

Review notes: Efficiency is part of the ARC-AGI-2 concept, so compute and cost are measurement-relevant rather than incidental.

### 2.8 Evaluation Conditions

| Condition | Description |
| :--- | :--- |
| Prompting protocol | Depends on solver/harness adapter. Official benchmarking repository documents model configs and provider adapters. |
| System prompt | Not a core ARC task concept; may vary by LLM harness. |
| Few-shot examples | Each task includes demonstration input/output pairs, typically three train pairs. |
| Sampling settings | Model-specific in the benchmarking harness; not uniform across all solvers. |
| Tool permissions | Competition and benchmark contexts may allow algorithmic search or code; exact constraints vary by platform and require separate review. |
| Time limits | Not fully specified in public task repository; competition constraints require Kaggle/testing-policy review. |
| Human intervention rules | Human testing was controlled for task calibration; model submissions should not leak evaluation-set information into development. |
| Hardware or hosted service | Public task repository supports local use; benchmarking harness supports API providers; Kaggle competition uses hosted submission infrastructure. |
| Network requirements | Required for API-based benchmarking and hosted leaderboard/competition use, not for local task files. |
| Sandbox or security constraints | Kaggle and competition contexts likely impose constraints; details were not text-accessible here. |
| Special administration conditions | Public, semi-private, and private evaluation sets are calibrated and used for different leakage/competition purposes. |

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

| Prompt | Response |
| :--- | :--- |
| Total public items or tasks | 1,120 public tasks in the repository: 1,000 training and 120 public evaluation. |
| Total private or hidden items | 240 non-public evaluation tasks: 120 semi-private and 120 private, according to official page/changelog. |
| Development or example items | Training set contains 1,000 public tasks used to demonstrate format and Core Knowledge priors. |
| Test items | Public evaluation set has 120 tasks; semi-private and private sets each have 120 tasks. |
| Dynamic or generated tasks | Tasks are static JSON files; leaderboard/competition evaluation may be dynamic in submission timing, not item generation. |
| Episodes, trials, or measurement points | Each task includes 1-2 test pairs typically; task success requires all test outputs correct. Attempt count is inconsistently stated as two/pass@2 versus three trials. |
| Item count uncertainty | Counts are clear across official page and changelog; attempt rule is unclear. |

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

| Technology | A | R | Status detail |
| :--- | :---: | :---: | :--- |
| API access | - [x] | - [ ] | Benchmarking repo supports API providers; not required for all solvers. |
| Local inference | - [x] | - [ ] | Public task data and custom solvers can run locally. |
| GPU | - [ ] | - [ ] | Depends on solver; not inherent to the benchmark. |
| CPU-only execution | - [x] | - [ ] | Simple solvers and scoring can run CPU-side. |
| Docker or container | - [ ] | - [ ] | Not documented as a primary path in reviewed materials. |
| Python package or CLI | - [x] | - [ ] | Official benchmarking repository provides CLI and Python package configuration. |
| Browser | - [x] | - [ ] | Human play/testing interface uses browser. |
| External tools | - [x] | - [ ] | Solvers may use program search/code; constraints vary. |
| Internet access | - [x] | - [ ] | Needed for hosted/API and leaderboard use. |
| Proprietary platform | - [x] | - [ ] | Kaggle and API model providers may be used. |

Other technologies/comments: Benchmarking repository has model adapters, provider config, pricing fields, sample tasks, random baseline, and scoring scripts.

### 2.14 Time and Resource Requirements

| Activity | Time, compute, or cost estimate |
| :--- | :--- |
| Setup | Official benchmarking repository provides quickstart but not a universal setup-time estimate. |
| Model inference or task completion | Human testing average reported around 2.3 minutes per task on candidate tasks in the technical-report page. |
| Scoring | Exact-grid scoring is scriptable; no full scoring-time estimate is stated. |
| Human adjudication | Controlled human testing involved 400+ participants and 1,417 unique tasks according to official technical-report page. |
| Analysis or reporting | Not specified as a time budget. |
| Full benchmark run | Depends on solver and split; not specified universally. |
| API or compute cost | Official reporting emphasizes cost/performance; leaderboard shows cost-related constraints, but complete cost rules require separate review. |

Other requirements/comments: Cost is not just operational overhead; it is part of ARC-AGI-2's intended efficiency interpretation.

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant | Purpose | Equivalence claim | Status |
| :--- | :--- | :--- | :--- |
| Public training set | Demonstrate task format and Core Knowledge priors; can be used for training/prototyping. | Not intended as final evaluation. | Public, 1,000 tasks. |
| Public evaluation set | Public testing for systems not developed against those tasks. | Official page says calibrated with semi-private/private sets. | Public, 120 tasks. |
| Semi-private evaluation set | Live contest and ARC Prize leaderboard for remotely hosted commercial models with low leakage probability. | Official page says calibrated to public/private difficulty. | Hidden, 120 tasks. |
| Private evaluation set | Final Kaggle contest leaderboard for self-contained models with near-zero leakage probability. | Official page says calibrated to public/semi-private difficulty. | Hidden, 120 tasks. |
| ARC-AGI-1 predecessor | Earlier benchmark and continuity reference. | Not equivalent; ARC-AGI-2 is harder and redesigned. | Public predecessor. |

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

### 2.18 Broad Claim and CHC/AGI Cautions

| Prompt | Response |
| :--- | :--- |
| Broad claim term used | "Artificial General Intelligence," "general artificial intelligence benchmark," "psychometric intelligence test," "general fluid intelligence," "human-like AI capabilities," and "true AGI" appear in official materials. |
| Claimed breadth across domains | Claimed breadth is about abstract reasoning/generalization under minimal prior knowledge, not many real-world domains. |
| Claimed depth or proficiency level | Official page asks whether a system can reach 85% accuracy; technical-report page says top models were below 5% at report publication while humans can solve the tasks. |
| Sub-abilities explicitly covered | Grid abstraction, few-shot induction, symbolic interpretation, compositional rule use, contextual rule application, exact output construction, efficient solving. |
| Sub-abilities explicitly excluded or not tested | Broad language, semantic world knowledge, long-term memory, social cognition, agency, open-ended planning, tool autonomy, physical embodiment, scientific discovery, broad CHC knowledge abilities, and real-world transfer. |
| Coverage across modalities, tools, memory, planning, or speed | Visual/structured grids and efficiency/cost are covered; broad multimodality, memory, and agency are not central. |
| Stated AGI, autonomy, or agency caveats | Official materials frame ARC-AGI-2 as signal on AGI progress but do not provide a full AGI construct map. |
| Relation to CHC-like broad/narrow abilities, if claimed | No explicit CHC mapping is provided. A cautious reviewer would map it most closely to narrow induction/fluid reasoning tasks, not a full CHC profile. |
| Descriptive caution for Part B | Treat ARC-AGI-2 as strong evidence about ARC-style abstract grid reasoning and weak standalone evidence for broad AGI. |

Review notes: Broad AGI/fluid-intelligence language is the central validity stress point for this pilot.

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
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [x] Leaderboard service scoring
- [ ] Manual adjudication

Other scoring methods/comments: Human testing is used to calibrate tasks and baselines, not to score AI submissions.

Review notes: The scoring method is exact-grid comparison. Attempt-count wording is inconsistent across official materials.

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or metric | Definition | Aggregation | Interpretation stated by authors |
| :--- | :--- | :--- | :--- |
| Primary score | Task success / accuracy under exact grid matching. | A task is solved when all test output grids are correct within the allowed attempts. | Measures ARC-style abstract reasoning and problem solving. |
| Subscore | Public, semi-private, private, leaderboard, competition, and model/system categories. | Split or leaderboard grouping. | Supports public research, live leaderboard, and final competition evaluation. |
| Derived score | Cost/efficiency, including cost-per-task framing. | Depends on benchmark/leaderboard configuration and model pricing/runtime. | Efficiency is treated as central to intelligence measurement. |
| Qualitative band | 85% challenge target appears on official page. | Not a validated psychometric band. | Competition/AGI-progress target, not standalone proof of AGI. |

Treatment of invalid, missing, malformed, or refused responses: Benchmarking repository scoring expects submission directories with output grids. Leaderboard page says remaining tasks are marked incorrect when models cannot produce full test outputs.

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

| Comparator or baseline | Construction method | Intended interpretation |
| :--- | :--- | :--- |
| Random or chance baseline | Benchmarking repo includes random baseline sample; exact random success is near-zero for grid tasks. | Demonstrates a trivial floor. |
| Human baseline | Official materials report 400+ participants, 1,417 unique tasks, minimum two-human solvability, and average public-eval human performance in README. | Anchors "easy for humans, hard for AI" and split calibration. |
| Expert baseline | Not the main comparator; general public human testing is emphasized. | Not used as expert norming. |
| Model cohort | Technical-report page and leaderboard report current AI system performance, with top systems below 5% at report publication. | Demonstrates challenge difficulty for contemporary AI. |
| Prior benchmark or version | ARC-AGI-1 is predecessor and comparison point; official materials state ARC-AGI-2 is designed to address saturation/progress. | Places ARC-AGI-2 as harder, more fine-grained successor. |
| Criterion threshold or floor/ceiling | 85% challenge target, pass@2 task solvability, cost constraints, and expected split comparability. | Supports competition framing, not validated broad-AGI threshold by itself. |

Review notes: Baseline structure is unusually strong for AI benchmarks, but attempt-rule ambiguity and broad-claim scope limit interpretation.

### 3.6 Score Uncertainty and Stability

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [x] Sensitivity analyses
- [ ] Not reported

Other uncertainty/stability comments: Official page states eval sets are calibrated and scores are expected to be comparable across sets within less than 1 percentage point assuming no overfitting. Full statistical details are in/behind the technical report rather than fully captured on the page.

Review notes: Split-equivalence support is useful. AI run-to-run variance remains underdocumented.

### 3.7 Metric-to-Claim Linkage

| Prompt | Response |
| :--- | :--- |
| Why the primary metric was chosen | Exact grid matching fits ARC's task definition: infer transformation and construct correct output grid. |
| Whether metric floors or ceilings are documented | Random floor is practically near-zero; human and AI performance contrasts are documented; leaderboard cost filters are documented. |
| Whether the metric may reward non-target behavior named by the benchmark | Official materials explicitly seek to reduce brute-force search and emphasize efficiency to avoid rewarding exhaustive compute. |
| Whether parsing, judge, or scorer validation is documented | Exact scorer and CLI are public; parser/harness behavior is documented in code but not fully reviewed here. |
| Whether score uncertainty affects claim interpretation | Yes. Split calibration helps, but AI run variance and current leaderboard uncertainty require caution. |
| Whether score differences are interpreted statistically | Official page states expected split comparability; broader statistical comparison methods are not fully public in reviewed page text. |
| Whether benchmark reports state what users should not infer | Official materials emphasize AGI relevance but do not provide a complete non-use statement for broad AGI interpretation. |

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

| Output | Description | Public/private |
| :--- | :--- | :--- |
| ARC Prize leaderboard | Public cost/performance leaderboard with ARC-AGI version tabs and verification caveats. | Public web output. |
| Technical report results | Human testing and AI performance context. | Public paper/report output. |
| Kaggle competition leaderboard | ARC Prize 2025 competition page linked from official materials. | Hosted; not text-accessible in this review environment. |
| Benchmarking repo results | Local outputs from official harness, including sample random baseline. | User-generated public-tool output. |

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

## Section 5. Supply Arrangements and Materials

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

| Requirement type | Requirement |
| :--- | :--- |
| Technical skill | Ability to parse ARC JSON tasks, build output grids, run Python CLI/scoring, and manage solver submissions. |
| Model access | Either local solver access or API access through supported/custom harness adapters. |
| Dataset access | Public GitHub access for training/evaluation; controlled access for semi-private/private sets. |
| Compute or budget | Cost matters for official interpretation; leaderboard notes cost display limits and competition constraints require separate review. |
| Human expertise | Interpretation requires understanding ARC task format, exact-grid scoring, search/program-synthesis confounds, and AGI claim limits. |
| Account, license, or competition eligibility | GitHub public access for tasks; Kaggle/ARC Prize accounts and terms for competition/leaderboard submission. |
| Ethical, safety, or data-use obligations | Avoid leaking public evaluation tasks into model development; respect private-set and competition rules. |

Other requirements/comments: The public evaluation set should not become an iterative training feedback loop, per README warning.

### 5.4 Dataset and Item Access

| Component | Public | Restricted | Hidden | Not available | Status detail |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Training or development items | - [x] | - [ ] | - [ ] | - [ ] | 1,000 public training tasks. |
| Public evaluation items | - [x] | - [ ] | - [ ] | - [ ] | 120 public evaluation tasks. |
| Private or held-out evaluation items | - [ ] | - [x] | - [x] | - [ ] | 120 semi-private and 120 private tasks are not in the repository. |
| Answer keys or reference solutions | - [x] | - [x] | - [x] | - [ ] | Public answers exist in JSON for public tasks; hidden answers exist for competition splits. |
| Metadata or annotations | - [ ] | - [ ] | - [ ] | - [x] | Full task metadata and human-testing annotations are not public in reviewed materials. |
| Raw model outputs or logs | - [ ] | - [ ] | - [ ] | - [x] | Public raw outputs/traces for official model runs are not documented. |

Other access/comments: The public repository is strong for task access; hidden splits are necessary for integrity but limit independent inspection.

### 5.5 Provenance and Contamination Documentation

| Topic | Documented | Partially documented | Not documented | Status detail |
| :--- | :---: | :---: | :---: | :--- |
| Data origin or task creation | - [x] | - [ ] | - [ ] | ARC principles and ARC-AGI-2 design goals are described. |
| Author or contributor qualifications | - [x] | - [ ] | - [ ] | Technical report authors and ARC Prize organization are identified. |
| Deduplication or overlap checks | - [ ] | - [x] | - [ ] | Brute-force susceptible tasks and prior contest-solved tasks were removed, but full overlap metrics are limited. |
| Public/private split rationale | - [x] | - [ ] | - [ ] | Semi-private/private split functions are clearly described. |
| Contamination screening | - [x] | - [ ] | - [ ] | Leakage probabilities, private sets, public-eval warning, and competition split are documented. |
| Canary strings or training-data warnings | - [ ] | - [x] | - [ ] | README warns not to leak evaluation tasks into algorithms; no canary string identified. |
| Refresh or rotation policy | - [ ] | - [x] | - [ ] | Public changelog exists; longer-term refresh policy is not fully documented. |
| Reporting of known leaks or retired items | - [ ] | - [x] | - [ ] | Changelog records task corrections; leak reporting policy is not comprehensive. |

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
- [x] Continuous integration or test suite

Other reproducibility comments: Raw outputs are available for user-generated harness runs, not necessarily for official leaderboard systems. CI/test suite is inferred from the benchmarking repository's test configuration and contribution guidance; exact CI status was not fully reviewed.

### 5.7 Maintenance and Versioning

| Topic | Response |
| :--- | :--- |
| Maintainer identity | ARC Prize / `arcprize` GitHub organization. |
| Version naming or release tags | ARC-AGI-2 main release; no repository release tag reviewed. |
| Changelog or update record | Public changelog records release and public-evaluation corrections. |
| Issue or feedback process | GitHub issues and pull requests are public. |
| Item correction process | Public changelog records minor corrections to public evaluation tasks. |
| Deprecated item handling | Brute-force susceptible and prior-solved tasks were removed before release; public post-release corrections documented. |
| Private-set refresh policy | Not fully documented. |
| Score comparability across versions | Official page claims public/semi-private/private eval sets are calibrated and comparable within less than 1 percentage point expected, assuming no overfitting. |
| Long-term archival plan | Not documented. |

Review notes: Changelog discipline is a strength. Versioned score comparability still requires careful handling because public evaluation tasks changed after release.

---

## Appendix A. General Description of the Benchmark

ARC-AGI-2 is the second Abstraction and Reasoning Corpus for Artificial General Intelligence benchmark. It consists of colored-grid transformation tasks in which a solver infers a rule from demonstration input/output pairs and produces output grids for test inputs. The public repository contains 1,000 training tasks and 120 public evaluation tasks; official materials also describe 120 semi-private and 120 private evaluation tasks. ARC-AGI-2 is designed to be easy for humans but difficult for current AI systems, resistant to brute-force search, calibrated across public/private splits, and reported with cost/efficiency metrics. Its narrowest defensible interpretation is performance on ARC-style abstract grid reasoning tasks under exact-grid scoring and specified attempt/cost conditions. Its broad AGI/general-fluid-intelligence interpretation requires substantial caution because the task family is narrow relative to full cognitive breadth.

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether ARC-AGI-2 is adequate as a measurement instrument for its intended use. Ratings use Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Rationale and construct definition | No usable basis. | Purpose or construct is vague. | Purpose is usable with limits. | Purpose and construct are clear for intended use. | Rationale is comprehensive and theoretically grounded. |
| Phenomenon-task-metric-claim chain | No usable basis. | Linkage is missing or weak. | Basic linkage is plausible. | Linkage is explicit and mostly supported. | Linkage is comprehensive and tested for confounds. |
| Task/item development quality | No usable basis. | Development is weak or opaque. | Basic process and expertise are documented. | Strong process with quality checks. | Comprehensive development record with expert and quantitative checks. |
| Documentation and procedural instructions | No usable basis. | Documentation is insufficient for qualified use. | Core documentation supports cautious use. | Documentation is clear across setup, scoring, and interpretation. | Documentation is comprehensive, current, and source-linked. |

### 6.2 Rationale, Documentation, and Task Quality Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 6.1 Rationale and construct definition | `3` |
| 6.2 Phenomenon-task-metric-claim chain | `2` |
| 6.3 Development process and task/item quality | `3` |
| 6.4 Documentation available to users | `3` |
| 6.5 Procedural instructions for administration, scoring, and interpretation | `2` |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality | `2` |

Review notes:

6.1 basis: ARC-AGI-2 has a clear rationale rooted in ARC's theory of abstract reasoning, Core Knowledge priors, and human-easy/AI-hard task design. Gap: the AGI/general-fluid-intelligence construct is not decomposed into a broad cognitive model. Rationale: good for ARC-style grid reasoning, less complete for broad AGI. Caution: a strong ARC rationale is not a complete theory of AGI measurement.

6.2 basis: The task-to-metric chain is explicit: infer transformation, produce exact grid, score success/cost. Gap: the metric-to-AGI-claim chain is underdeveloped. Rationale: adequate overall because the narrow chain is strong but the broad claim is ambitious. Caution: exact-grid success does not by itself validate broad fluid intelligence.

6.3 basis: Official materials describe new task design, removal of brute-force-susceptible tasks, controlled human testing, split calibration, and public task corrections. Gap: full item-development metadata, human-testing data, and quantitative task diagnostics are not all public. Rationale: task-quality process is good. Caution: public task corrections show maintenance but also require version awareness.

6.4 basis: Official page, technical-report page, arXiv report, task repository, changelog, leaderboard, and benchmarking repository provide strong documentation. Gap: Kaggle page content and some leaderboard values were not text-accessible here. Rationale: documentation is good for technical users. Caution: competition/leaderboard claims need platform-specific policy review.

6.5 basis: Task format, exact scoring, harness CLI, and data splits are documented. Gap: attempt-rule wording conflict, competition constraints, and cost methodology details remain incomplete. Rationale: procedural support is adequate but not fully clean. Caution: attempt-count ambiguity should be resolved before using scores for official comparison.

Other comments: Section 6 ratings are pulled downward by broad-claim scope and official wording inconsistency, not by lack of task artifacts.

---

## Section 7. Quality of Benchmark Materials and Usability

### 7.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Materials availability | No usable basis. | Key materials are missing or inaccessible. | Core materials are available or described. | Most materials are available with clear access limits. | Complete materials are versioned, licensed, and linked. |
| Evaluation harness and scoring tools | No usable basis. | Harness or scorer is absent, opaque, or unusable. | Basic scoring path is documented. | Runnable harness or scorer has clear setup examples. | Harness is robust, tested, documented, and reproducible. |
| Prompts, rubrics, and response formats | No usable basis. | Instructions or rubrics are ambiguous. | Core prompts and rubrics are documented. | Instructions and format handling are clear. | Prompts, rubrics, parsers, and constraints are validated. |
| Accessibility and usability | No usable basis. | Materials are difficult to use or exclude relevant systems without explanation. | Usable by skilled reviewers with constraints. | Good usability with support paths. | Excellent usability across intended users and system classes. |

### 7.2 Benchmark Materials and Usability Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 7.1 Dataset, task set, or environment availability | `3` |
| 7.2 Prompts, instructions, rubrics, and response format | `2` |
| 7.3 Evaluation harness, scorer, and implementation usability | `3` |
| 7.4 Accessibility across relevant modalities, languages, and system types | `2` |
| 7.5 Licensing, usage requirements, and sensitive-content warnings | `2` |
| 7.6 Overall quality of benchmark materials | `3` |

Review notes:

7.1 basis: Public training/evaluation tasks, hidden split descriptions, and task changelog are available. Gap: semi-private/private tasks and full human-testing data are not public. Rationale: materials availability is good for open research. Caution: public evaluation exposure can invite overfitting.

7.2 basis: JSON task format and exact grid output are clear. Gap: LLM prompt conventions, attempt rule, and malformed-output treatment vary by harness/leaderboard context. Rationale: adequate but not flawless. Caution: prompt/adapter differences can change system performance.

7.3 basis: Official benchmarking repository has quickstart, adapters, scoring, sample tasks, random baseline, pricing config, and tests. Gap: no published releases and no fully reviewed CI status. Rationale: strong harness usability compared with many benchmarks. Caution: leaderboard replication still requires matching private platform conditions.

7.4 basis: Tasks require minimal language and use a simple symbolic grid format. Gap: visual-grid interface and exact output format may favor systems with specific perception/serialization abilities; human sample demographics are only summarized. Rationale: adequate accessibility for technical users and many system types. Caution: grid-specific skill is not broad multimodal or cognitive fairness.

7.5 basis: Apache-2.0 task license and MIT harness license are public. Gap: Kaggle rules, ARC Prize testing policy details, and sensitive-content warnings were not fully reviewed. Rationale: legal/use documentation is adequate for public repository use, incomplete for competition use. Caution: competition claims require platform terms.

Other comments: Section 7 is strong because materials and harness are public and usable. Hidden split opacity is expected but should be clearly governed.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline construction | No usable basis. | Baselines are absent or unsupported. | Basic baselines are documented. | Baselines are meaningful and relevant. | Baselines are comprehensive and uncertainty-aware. |
| Human/expert comparators | No usable basis. | Human or expert claims lack method. | Comparison is described but limited. | Comparator procedures are well documented. | Comparator support is rigorous and representative. |
| Model comparators | No usable basis. | Cohort is poorly specified. | Model comparisons are documented with limits. | Cohort, versions, and conditions are well specified. | Comparisons are comprehensive, current, and uncertainty-aware. |
| Floors, ceilings, thresholds | No usable basis. | Floors, ceilings, or thresholds are ignored despite relevance. | Some relevant anchors are documented. | Anchors and saturation risks are explained. | Anchors are empirically supported and integrated into interpretation. |

### 8.2 Baselines and Reference Interpretation Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 8.1 Random, chance, floor, and ceiling baselines | `3` |
| 8.2 Human or expert baselines | `3` |
| 8.3 Model comparator cohort | `2` |
| 8.4 Criterion thresholds or score bands | `2` |
| 8.5 Overall adequacy of baselines and reference interpretation | `3` |

Review notes:

8.1 basis: Random baseline tooling exists, exact-grid random success is extremely low, and official materials discuss difficulty and brute-force resistance. Gap: full random/search baselines by task and compute budget are not all public. Rationale: good baseline support. Caution: brute-force resistance should be periodically retested.

8.2 basis: Official human testing involved 400+ people and 1,417 tasks, with every included task solved by at least two humans under pass@2/two-attempt criteria. Gap: full human data, sampling details, and score uncertainty are not all public in the reviewed page text. Rationale: good human baseline for feasibility and calibration. Caution: San Diego public testing is not a universal human norm.

8.3 basis: Technical-report page reports leading model performance below 5% at publication and leaderboard exists. Gap: current ARC-AGI-2 leaderboard entries and exact model conditions were not text-extracted here. Rationale: adequate model comparator support but date-sensitive. Caution: do not cite current rankings without a fresh leaderboard snapshot.

8.4 basis: 85% challenge target, cost constraints, pass@2 solvability, and split calibration are documented. Gap: 85% is not validated as a psychometric AGI threshold; attempt-rule inconsistency remains. Rationale: adequate competition thresholds, weak broad-intelligence threshold. Caution: reaching a competition target would not alone establish AGI.

Other comments: Baseline design is one of ARC-AGI-2's strengths.

---

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Run stability and uncertainty | No usable basis. | Known stochasticity is not addressed. | Some uncertainty or repeat-run basis is provided. | Stability is assessed across relevant settings. | Comprehensive stability support covers main interpretations. |
| Scorer, judge, or rater reliability | No usable basis. | Judgmental scoring lacks validation. | Basic validation or agreement is provided. | Strong validation of scorers, judges, raters, or parsers. | Comprehensive reliability support across domains and edge cases. |
| Form, version, and prompt stability | No usable basis. | Forms or prompts are mixed without equivalence support. | Basic conditions are documented. | Stability or equivalence is tested for important versions or prompts. | Strong equivalence and drift support is available. |
| Statistical comparison quality | No usable basis. | Differences are reported without uncertainty where it matters. | Some uncertainty or variance information is available. | Comparisons include useful uncertainty methods. | Comparisons are uncertainty-aware and statistically justified. |

### 9.2 Reliability, Precision, and Score Stability Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 9.1 Run-to-run stability, seeds, and sampling settings | `2` |
| 9.2 Score uncertainty, confidence intervals, or standard errors | `2` |
| 9.3 Human rater, scorer, parser, or model-judge agreement | `2` |
| 9.4 Prompt, form, version, and environment stability | `2` |
| 9.5 Overall reliability and precision | `2` |

Review notes:

9.1 basis: Exact-grid scoring is deterministic once submissions exist, and benchmarking configs can specify model parameters. Gap: stochastic model repeat runs and seed policies are not comprehensively reported. Rationale: adequate reliability for deterministic solvers, limited for LLM systems. Caution: repeated LLM runs may vary.

9.2 basis: Official page states cross-split calibration and expected comparability within less than 1 percentage point, assuming no overfitting. Gap: detailed statistical intervals and model comparison uncertainty are not fully public in reviewed page text. Rationale: adequate but not comprehensive. Caution: current leaderboard differences should be interpreted with uncertainty.

9.3 basis: Scoring is exact reference matching, reducing rater ambiguity. Human testing supports solvability. Gap: malformed-output parser reliability and human calibration agreement details are incomplete. Rationale: exact scoring is a strength. Caution: LLM adapter parsing can still create avoidable scoring errors.

9.4 basis: Public/semi-private/private split calibration and changelog support form/version control. Gap: public task corrections after release and attempt-rule inconsistency complicate version stability. Rationale: adequate but needs stricter version labels. Caution: scores before/after public task fixes may not be fully comparable.

Other comments: Reliability is stronger than HLE on scorer determinism but still limited for stochastic models and broad leaderboard comparisons.

---

## Section 10. Validity Evidence

### 10.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Content and representativeness | No usable basis. | Task sample is poorly justified. | Content coverage is plausible and partly documented. | Content support is strong with stated limits. | Content support is comprehensive and representative. |
| Metric and scoring validity | No usable basis. | Metric likely rewards non-target behavior or is opaque. | Metric is plausible but has unresolved confounds. | Metric choice is justified and some confounds are tested or mitigated. | Metric, scorer, aggregation, and interpretation are validated. |
| Relations with other support | No usable basis. | Comparisons are absent or misleading. | Some relevant comparisons are provided. | Comparisons and criteria are meaningful and cautious. | Strong convergent, discriminant, criterion, or ecological support is provided. |
| Contamination and gameability | No usable basis. | Contamination or gameability risks are ignored. | Basic controls or caveats are documented. | Strong controls, audits, private splits, or release rules are used. | Comprehensive contamination/gameability strategy supports ongoing use. |
| Claim proportionality, including AGI/agency | No usable basis. | Claims exceed task, metric, or support. | Claims are mostly bounded. | Claims are well bounded and broad-claim cautions are explicit. | Claims are fully proportional or broad claims are explicitly rejected. |

### 10.2 Validity Evidence Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 10.1 Content validity and task representativeness | `2` |
| 10.2 Internal structure, subscores, or dimensionality | `1` |
| 10.3 Metric, scorer, and aggregation validity | `3` |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings | `2` |
| 10.5 Contamination, leakage, and gameability controls | `3` |
| 10.6 Claim proportionality and broad-capability cautions | `1` |
| 10.7 Overall validity support | `2` |

Review notes:

10.1 basis: ARC tasks are carefully designed around abstract grid reasoning, symbolic interpretation, composition, contextual rules, human feasibility, and minimal priors. Gap: task representativeness for broad fluid intelligence or AGI is not established. Rationale: adequate overall because content is strong for ARC but narrow for claims. Caution: grid abstraction is a narrow slice of cognition.

10.2 basis: Official materials identify challenge types but do not validate subscales. Gap: no dimensionality analysis or subscore reliability. Rationale: weak internal-structure support. Caution: symbolic/compositional/contextual examples should not be treated as validated latent dimensions.

10.3 basis: Exact-grid scoring directly matches task success, and cost/efficiency addresses brute-force confounding. Gap: attempt-rule inconsistency and malformed-output handling remain. Rationale: metric validity is good for narrow task success. Caution: cost estimates and attempts must be standardized.

10.4 basis: Human baseline, ARC-AGI-1 comparison, model cohort difficulty, and leaderboard provide relational support. Gap: limited convergent/discriminant validation against non-ARC cognitive tasks and real-world adaptive behavior. Rationale: adequate relations for challenge difficulty, not broad cognitive validity. Caution: "hard for AI, easy for humans" is not enough to establish AGI.

10.5 basis: Semi-private/private splits, leakage rationale, competition structure, public-eval warning, and brute-force-resistant task design are strong controls. Gap: full private governance and ongoing leak metrics are not public. Rationale: good contamination/gameability support. Caution: public eval should not be used iteratively for development feedback.

10.6 basis: Official materials explicitly use AGI and general-fluid-intelligence language. Gap: no broad cognitive ability battery, no CHC mapping, no evidence across language, memory, knowledge, agency, embodiment, or social cognition. Rationale: broad claim proportionality is inadequate if scores are read as general AGI measurement. Caution: ARC-AGI-2 can be AGI-relevant without being a full AGI test.

Other comments: ARC-AGI-2 is strong as an ARC-style abstract reasoning benchmark and weak as standalone broad-intelligence measurement.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cross-system comparability | No usable basis. | Conditions are unclear or likely unfair. | Core conditions support cautious comparison. | Conditions are well specified and important differences are handled. | Comparability is actively supported across intended system classes. |
| Domain, language, modality, and subgroup coverage | No usable basis. | Coverage gaps are ignored. | Coverage and major limits are documented. | Coverage is analyzed and tied to interpretation. | Coverage support is strong across relevant domains and groups. |
| Access, compute, and usability fairness | No usable basis. | Access or compute requirements distort use without warning. | Requirements are documented with caveats. | Requirements and constraints are clear for intended users. | Access paths support fair replication and comparison. |
| Appropriate-use guidance | No usable basis. | Public guidance invites overinterpretation. | Basic intended-use and non-use guidance is available. | Guidance is clear and tied to limits. | Guidance comprehensively supports responsible interpretation. |

### 11.2 Fair Use, Comparability, and Appropriate Use Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 11.1 Cross-system and evaluation-condition comparability | `2` |
| 11.2 Domain, language, modality, and subgroup fairness | `2` |
| 11.3 Access, compute, tooling, and API/local comparability | `2` |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance | `2` |
| 11.5 Overall fair use and comparability | `2` |

Review notes:

11.1 basis: Exact scoring, calibrated splits, and benchmarking configs support comparison. Gap: attempt-rule inconsistency, cost-estimation variation, and hidden-platform constraints remain. Rationale: adequate comparison support. Caution: compare systems only under matched attempts, cost, and split conditions.

11.2 basis: Low language dependence and controlled human demographic survey are strengths. Gap: human sample representativeness, visual-grid accessibility, and non-grid cognitive coverage are limited. Rationale: adequate for ARC task use, not broad fairness. Caution: grid tasks may disadvantage systems or humans with visual/spatial interface constraints.

11.3 basis: Public data and harness support local/API evaluation; leaderboard cost framing improves transparency. Gap: private competition infrastructure, API pricing changes, and compute budgets require current review. Rationale: adequate access fairness. Caution: cost-aware scores are only fair when pricing and runtime are standardized.

11.4 basis: Public-eval leakage warning, private splits, testing policy links, and leaderboard caveats exist. Gap: Kaggle content did not render here, and broad AGI non-use guidance is incomplete. Rationale: adequate but not comprehensive. Caution: public AGI framing may invite overinterpretation.

Other comments: Fair use is good for technical competition/research contexts and weaker for public AGI interpretation.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Rating Anchors

| Criterion | `0` Cannot rate | `1` Inadequate | `2` Adequate | `3` Good | `4` Excellent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Report scope and granularity | No usable basis. | Reports omit essential scores or overstate detail. | Reports provide core scores with limited granularity. | Reports provide useful aggregate and subscore detail. | Reports provide comprehensive, interpretable, uncertainty-aware detail. |
| Leaderboard or dashboard quality | No usable basis. | Rankings are opaque or unstable without caveats. | Basic ranking or result display is available. | Versioned and interpretable result display is available. | Display is robust, reproducible, uncertainty-aware, and clear about updates. |
| Report reliability and validity | No usable basis. | Reports or claims diverge from what scores support. | Reports are mostly linked to scores. | Reports explain score-to-claim links and limits. | Reports clearly communicate defensible interpretations, uncertainty, and non-uses. |
| Public communication and acceptability | No usable basis. | Public claims encourage overinterpretation. | Public claims include basic caveats. | Public claims are mostly proportional. | Communication is transparent, cautious, accessible, and aligned with support. |

### 12.2 Reports, Leaderboards, and Public Claims Ratings

| Criterion | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| 12.1 Report, leaderboard, dashboard, or result artifact scope | `3` |
| 12.2 Score granularity, uncertainty, and version labeling | `2` |
| 12.3 Linkage from scores to public claims | `2` |
| 12.4 Raw outputs, per-item data, or trace availability | `1` |
| 12.5 Overall quality of reports and public claims | `2` |

Review notes:

12.1 basis: Official page, technical report, arXiv, public leaderboard, Kaggle link, repository, and harness outputs provide broad reporting coverage. Gap: current ARC-AGI-2 leaderboard values and competition details were not fully text-accessible here. Rationale: report scope is good. Caution: score-specific claims need a current snapshot.

12.2 basis: Split counts, human/AI contrast, cost framing, and leaderboard categories are documented. Gap: uncertainty intervals, raw score distributions, and detailed version labels are incomplete. Rationale: adequate granularity. Caution: public task corrections and hidden splits require version discipline.

12.3 basis: Reports link scores to ARC-style reasoning and AGI progress. Gap: broad AGI claim limits are not sufficiently explicit. Rationale: adequate for narrow task claims, weak for broad public claims. Caution: leaderboard movement should not be equated with general intelligence.

12.4 basis: Public task files and local user-generated outputs are available; official raw model outputs/traces are not documented. Gap: raw official submissions, traces, and per-item model outcomes. Rationale: limited trace availability. Caution: independent error analysis of leaderboard systems is constrained.

Other comments: The reporting ecosystem is mature but public communication should more sharply distinguish ARC task success from broad AGI.

---

## Final Evaluation

### Evaluative Report of the Benchmark

ARC-AGI-2 is a strong benchmark for ARC-style abstract grid reasoning. It has a clear task format, public data, hidden competition splits, controlled human testing, explicit attention to efficiency, an official benchmarking harness, a public changelog, and a leaderboard ecosystem. Its strongest measurement qualities are task clarity, exact scoring, human feasibility testing, split calibration, contamination controls, and public reproducibility materials.

Its main weakness is claim proportionality. Official materials repeatedly use AGI, general artificial intelligence, psychometric intelligence test, and general fluid intelligence language. ARC-AGI-2 provides meaningful evidence about a narrow family of visual/structured abstraction tasks, but it does not cover the breadth of abilities normally needed for broad AGI or CHC-style cognitive interpretation: language, knowledge, memory, planning, agency, social cognition, embodiment, and real-world transfer are mostly outside scope. The two-versus-three-trial inconsistency also needs correction because it affects success criteria and human/model comparability.

### Conclusions

ARC-AGI-2 can support cautious claims about performance on exact-grid abstraction tasks designed to be easy for humans and difficult for current AI systems. It can also be an AGI-relevant research signal if interpreted as one narrow component of a broader evaluation portfolio. It should not be used alone as proof of AGI, general fluid intelligence, human-like cognition, or broad cognitive versatility.

### Recommendations

Use ARC-AGI-2 for abstract reasoning research, competition benchmarking, and cost-aware solver comparison under matched evaluation conditions. Report split, attempt count, cost assumptions, model configuration, solver type, data version, and leaderboard date. Maintainers should resolve the attempt-rule inconsistency, publish clearer non-use guidance for AGI claims, provide more transparent current leaderboard exports, and document private-set governance and score uncertainty.

### Summary of Ratings

| Section | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| Section 6. Rationale, documentation, and task/item quality | `2` |
| Section 7. Benchmark materials and usability | `3` |
| Section 8. Baselines and comparators | `3` |
| Section 9. Reliability and precision | `2` |
| Section 10. Validity support | `2` |
| Section 11. Fair use and comparability | `2` |
| Section 12. Reports, leaderboards, and public claims | `2` |

Review notes: Overall quality would be `3` for narrow ARC-style grid reasoning alone. It is `2` for the benchmark's broader AGI/general-fluid-intelligence framing because the construct scope exceeds the task family.

### Gap Register

| Gap | Affected rating(s) | Why it matters | Needed for a higher rating |
| :--- | :--- | :--- | :--- |
| Official attempt rule conflicts between pass@2/two trials and three trials | 3, 6, 8, 9, 10, 11, final | Changes task success and comparability between humans and AI systems. | Single authoritative attempt rule across official page, README, harness, Kaggle, and leaderboard. |
| Broad AGI/general-fluid-intelligence construct is not fully mapped | 2.18, 10, 12, final | Prevents standalone broad-intelligence interpretation. | Explicit construct map, non-use guidance, and validation across broader ability domains. |
| Current ARC-AGI-2 leaderboard values were not text-accessible here | 8, 12 | Limits date-specific model comparison. | Downloadable or text-accessible leaderboard snapshot with model/config/cost metadata. |
| Kaggle competition page did not render reviewable text in this environment | 1.2, 5, 11, 12 | Competition rules can affect valid interpretation. | Reviewable copy of rules, compute limits, submissions, scoring, and split use. |
| Raw official model outputs and traces are not public | 9, 10, 12 | Limits error analysis and scorer/harness validation. | Public or controlled audit access to outputs, submissions, logs, and per-task outcomes. |
| Human-testing details are summarized rather than fully inspectable | 8, 9, 10, 11 | Human baseline strength depends on sampling and procedures. | Full human-study methods, demographics, attempt logs, uncertainty, and item-level solve data. |

Other gaps/comments: These gaps do not erase ARC-AGI-2's value as an abstract-reasoning benchmark. They limit the broader AGI interpretation.

### Reviewer Caution Statement

The narrowest defensible interpretation is: ARC-AGI-2 measures system performance on exact-grid abstraction tasks requiring few-shot transformation induction under specified split, attempt, and cost conditions. It is useful AGI-relevant evidence only as one narrow reasoning component inside a broader evaluation portfolio. It is not, by itself, a validated measure of AGI, general fluid intelligence, human-like cognition, or broad cross-domain cognitive ability.
