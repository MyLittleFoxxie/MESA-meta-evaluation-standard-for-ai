# MESA Pilot Review: Humanity's Last Exam v3

This v3 pilot now applies the targeted `markdown/MESA EFPA template v6.md` modifications to the prior HLE v2/v5 migration. It uses the same official HLE materials available on 2026-05-09 and does not perform a new online source refresh. Part A describes what the official materials state. Part B assigns ratings using Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

Before completing the review, inspect the most authoritative available materials. Prefer official benchmark papers, websites, repositories, data hosts, leaderboards, harnesses, changelogs, and maintainer statements. Independent commentary should be used only for context, external critique, or disputed claims, and should not replace official benchmark facts.

Documentation status summary for Part A:

- [x] Documented: benchmark name, public 2,500-question set, expert-contributor model, response formats, prompt template, model-judge scoring path, calibration output, public repository, MIT license, Hugging Face dataset entry, canary string, public website, Nature publication, arXiv record, HLE-Rolling change log, and basic answer/confidence extraction path.
- [x] Partially documented: private held-out set details, exact replication conditions for published model results, score uncertainty for published comparisons, HLE-Rolling comparability policy, formal leaderboard governance, end-to-end scorer validation, malformed-response handling, parser fallback, prompt or response-format sensitivity, and retirement readiness.
- [x] Not documented: random seeds for published runs, raw model outputs for reported results, full judge validation statistics, complete public/private set comparability statistics, formal statistical significance testing for model differences, tamper-evident audit logs, formal benchmark retirement criteria, and perturbation-sensitivity metrics.

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

| Prompt                                 | Response                                                                                                                           |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| Reviewer                               | MESA pilot reviewer                                                                                                                |
| Date of current review                 | 2026-05-09                                                                                                                         |
| Date of previous review, if applicable | 2026-05-09 for HLE v2 source review; 2026-05-04 for the earlier local HLE pilot                                                    |
| Review scope                           | Targeted v6 update of the HLE v3 pilot, preserving the 2026-05-09 source base and adding the new v6 fields and equivalent answers. |
| Review boundary                        | Official HLE materials first; independent commentary excluded except local MESA literature used for Part B criteria.               |

Review notes: This v3 pilot does not overwrite prior HLE pilots. It preserves the HLE v2 evidence base and updates the applied structure from v5 to the targeted v6 modifications.

### 1.2 Information Sources Reviewed

| Material type                                 | Artifact reviewed                                                                                     | Access date | Role in review                                                                                                        |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :---------- | :-------------------------------------------------------------------------------------------------------------------- |
| Official paper or technical report            | [Nature article: _Humanity's Last Exam_](https://www.nature.com/articles/s41586-025-09962-4)          | 2026-05-09  | Primary official publication for benchmark purpose, construction, results, and interpretation limits.                 |
| Official paper or technical report            | [arXiv:2501.14249](https://arxiv.org/abs/2501.14249)                                                  | 2026-05-09  | Preprint record and versioned paper access.                                                                           |
| Benchmark website or documentation hub        | [lastexam.ai](https://lastexam.ai/)                                                                   | 2026-05-09  | Official website, publication links, dataset links, HLE-Rolling, and live submission entry point.                     |
| Repository                                    | [centerforaisafety/hle](https://github.com/centerforaisafety/hle)                                     | 2026-05-09  | Official repository for README, evaluation scripts, license, canary, requirements, citation, and rolling change file. |
| Dataset card, data host, or task host         | [cais/hle on Hugging Face](https://huggingface.co/datasets/cais/hle)                                  | 2026-05-09  | Public task-set distribution and access conditions.                                                                   |
| Repository                                    | [cais/hle organization page](https://github.com/cais/hle)                                             | 2026-05-09  | Checked as an official alias/redirect context for the public HLE repository.                                          |
| Release log, changelog, or maintenance record | [hle-rolling-changes.txt](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt) | 2026-05-09  | Official record of HLE-Rolling additions and fixes.                                                                   |

Other materials/comments: The official website links the Nature article, arXiv paper, Hugging Face task set, GitHub repository, feedback form, and HLE-Rolling submission dashboard. This review does not rely on third-party commentary.

### 1.3 Benchmark Information

| Prompt                                                             | Response                                                                                                                                                                                                                                                                                                                                                                  |
| :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Benchmark name                                                     | Humanity's Last Exam                                                                                                                                                                                                                                                                                                                                                      |
| Short name or acronym                                              | HLE                                                                                                                                                                                                                                                                                                                                                                       |
| Benchmark version, edition, or release                             | Public 2,500-question HLE set plus HLE-Rolling as a maintained rolling variant. The repository does not expose a conventional semantic version release tag in the reviewed snapshot.                                                                                                                                                                                      |
| Original benchmark name, if this is an adaptation                  | Not applicable.                                                                                                                                                                                                                                                                                                                                                           |
| Benchmark creators or authors                                      | Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, Michael Choi, Anish Agrawal, Arnav Chopra, Adam Khoja, Ryan Kim, Richard Ren, Jason Hausenloy, Oliver Zhang, Mantas Mazeika, Summer Yue, Alexandr Wang, Dan Hendrycks, and a large contributor group listed in the official paper. |
| Current maintainers                                                | Center for AI Safety and Scale AI are the organizing entities named in official materials; repository maintenance occurs under `centerforaisafety/hle`.                                                                                                                                                                                                                   |
| Host organization, platform host, repository owner, or distributor | Nature publishes the article; Center for AI Safety hosts the GitHub repository; Hugging Face hosts the public task set; lastexam.ai hosts official web links.                                                                                                                                                                                                             |
| Date of original release                                           | Public materials date the paper/preprint to 2025 and the Nature article to 2026. The website states the final 2,500-question public set was available as of 2025-04-03.                                                                                                                                                                                                   |
| Date of current release or revision                                | HLE-Rolling was announced on the official website as launched on 2025-10-08; the reviewed repository main branch is the current public artifact snapshot.                                                                                                                                                                                                                 |
| License or access terms                                            | MIT license in the GitHub repository. Hugging Face access requires user acknowledgement of benchmark-data terms including not using the set for training or fine-tuning.                                                                                                                                                                                                  |
| Persistent identifier, citation, or DOI                            | Nature article DOI link via `https://doi.org/10.1038/s41586-025-09962-4`; arXiv identifier `2501.14249`; repository citation file.                                                                                                                                                                                                                                        |

Review notes: The official HLE ecosystem is now clearer than the earlier local pilot because Nature, arXiv, GitHub, Hugging Face, and lastexam.ai are all public anchors.

### 1.4 Public Artifacts

| Artifact                                  | URL or location                                                                                                            | Access status                                                                     | Review detail                                                                                                                  |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Paper or technical report                 | [Nature article](https://www.nature.com/articles/s41586-025-09962-4); [arXiv:2501.14249](https://arxiv.org/abs/2501.14249) | Public article page and arXiv record; Nature full text may depend on access route | Official publication and preprint establish the benchmark rationale and reported results.                                      |
| Benchmark website                         | [lastexam.ai](https://lastexam.ai/)                                                                                        | Public                                                                            | Provides links to final public set, HLE-Rolling, Nature, arXiv, GitHub, and Hugging Face.                                      |
| Code repository                           | [centerforaisafety/hle](https://github.com/centerforaisafety/hle)                                                          | Public                                                                            | Includes README, `hle_eval`, `requirements.txt`, MIT license, canary, citation, and rolling change file.                       |
| Evaluation harness                        | `hle_eval` in the GitHub repository                                                                                        | Public simple harness                                                             | README documents model prediction and judge result scripts using OpenAI-compatible API access.                                 |
| Dataset or task set                       | [cais/hle](https://huggingface.co/datasets/cais/hle)                                                                       | Public with access acknowledgement                                                | Hugging Face hosts the final 2,500 public questions with images where applicable.                                              |
| Prompt set                                | README and paper appendix                                                                                                  | Public                                                                            | Response prompt asks for answer and confidence; judge prompt is documented.                                                    |
| Rubric or scoring guide                   | Paper methods/appendix; repository judge script                                                                            | Public, partially implementation-specific                                         | Human review rubrics and model-judge criteria are described.                                                                   |
| Leaderboard or result display             | Nature result tables; lastexam.ai HLE-Rolling live submission dashboard                                                    | Public/hosted, partly live                                                        | Paper-level results are public. HLE-Rolling has a submission dashboard, but formal score governance is only partly documented. |
| Release log or changelog                  | [hle-rolling-changes.txt](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt)                      | Public                                                                            | Records rolling updates and fixes; score comparability policy is limited.                                                      |
| Contact, issue channel, or feedback route | GitHub issues; lastexam.ai feedback link                                                                                   | Public                                                                            | Repository and website provide feedback mechanisms.                                                                            |

Other artifacts/comments: Private held-out materials are described but not released, which is appropriate for integrity but limits independent inspection.

---

## Section 2. Classification

Section 2 classifies the benchmark's intended measurement domain, target systems, users, task structure, and administration conditions.

### 2.1 Claimed Capability Domains

- [ ] Not explicitly stated
- [ ] General capability or intelligence
- [x] Reasoning
- [x] Knowledge
- [ ] Language understanding
- [ ] Writing or generation quality
- [x] Mathematics
- [ ] Coding or software engineering
- [x] Scientific or technical expertise
- [x] Domain-specific professional expertise
- [x] Multimodal perception
- [ ] Audio or speech
- [ ] Video understanding
- [ ] Tool use
- [ ] Planning or agency
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [x] Calibration or uncertainty

Other domains/comments: The official materials frame HLE as expert-level closed-ended academic evaluation across broad domains, not as a standalone AGI or autonomous-agency test.

Review notes: "Humanity's Last Exam" and frontier-model framing create broad public salience, but the official interpretive caveat is narrower than a general-intelligence claim.

### 2.2 Area of Use

- [ ] Not explicitly stated
- [x] Model comparison
- [ ] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [ ] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison
- [ ] Internal regression testing
- [x] Public communication or marketing
- [x] Policy or governance analysis

Other areas/comments: HLE-Rolling introduces a live submission context, but the reviewed materials do not define deployment, procurement, or gating use.

Review notes: The strongest supported use is research comparison under documented conditions.

### 2.3 Intended AI Systems

- [ ] Not explicitly stated
- [x] Frontier general-purpose language models
- [x] Chat or instruction-following models
- [ ] Base language models
- [ ] Code models
- [x] Multimodal models
- [ ] Audio or speech models
- [ ] Agentic systems
- [ ] Tool-using systems
- [ ] Retrieval-augmented systems
- [ ] Domain-specialized models
- [ ] Open-weight local models
- [x] API-hosted models

Other systems/comments: Text-only systems can be evaluated on text-only subsets, but the full benchmark includes image questions.

Free text description: The official results focus on frontier LLMs and multimodal LLMs accessed through model APIs. Standard evaluation does not require web browsing, tool use, persistent memory, or autonomous task execution.

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

Other users/comments: The Nature paper and website target scientists, policymakers, and a broader public audience interested in frontier model progress.

Review notes: Procurement and deployment decision-makers would need additional validation not supplied by the benchmark alone.

### 2.5 Task Families, Subdomains, and Scores

| Component                                                                                    | Description                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Claimed construct or phenomenon                                                              | Expert-level closed-ended academic performance by frontier AI systems.                                                                                                                                                          |
| Claimed capability definition                                                                | Ability to answer difficult expert-written academic questions, including some image-conditioned items, with correctness and confidence under HLE prompting and scoring conditions.                                              |
| Construct subcomponents                                                                      | Advanced knowledge, domain-specific reasoning, mathematical/scientific problem solving, image-conditioned academic questions, answer confidence, and calibration.                                                               |
| Excluded scope or non-target abilities                                                       | Open-ended scientific discovery, autonomous research, long-horizon agency, tool use, broad CHC/AGI breadth, and real-world deployment performance are not measured directly.                                                    |
| Task families or subdomains                                                                  | The official paper describes 2,500 questions across over 100 subject areas, including mathematics, science, engineering, humanities, social science, law, medicine/biology, computer science/AI, and other specialized domains. |
| Task sources, including reused datasets or adapted benchmarks                                | Expert-contributed HLE questions, with public Hugging Face distribution, official paper examples, and HLE-Rolling additions or fixes; not presented as a random sample from existing benchmark datasets.                        |
| Task sampling method, such as random, stratified, criterion, targeted, convenience, or mixed | Mixed expert/criterion/targeted sampling: questions were selected for expert difficulty, answerability, and non-searchability rather than statistical representativeness of all academic knowledge.                             |
| Task selection or filtering logic                                                            | Questions were expert-contributed, reviewed, revised, audited, and selected for difficulty and non-searchability under official rubrics.                                                                                        |
| Splits or partitions                                                                         | Public 2,500-question set; private held-out set; text-only subset; HLE-Rolling maintained variant.                                                                                                                              |
| Primary score                                                                                | Accuracy / percent correct over evaluated items.                                                                                                                                                                                |
| Subscores                                                                                    | Category/domain accuracy and text-only versus full-set reporting in official results.                                                                                                                                           |
| Derived or aggregate scores                                                                  | Calibration-related reporting, including model confidence and RMS calibration error in the paper; simple evaluator outputs include aggregate accuracy and related summary statistics.                                           |
| Qualitative labels or bands                                                                  | Human-review labels during item development, such as keep/revise/discard-style judgments; not model score bands.                                                                                                                |
| Claim boundaries or caveats                                                                  | Official discussion cautions against interpreting HLE accuracy alone as AGI, autonomous research ability, or open-ended creative scientific capability.                                                                         |

Review notes: HLE has strong descriptive coverage of item-development intent, but not a formal psychometric construct map across cognitive subabilities.

### 2.6 Model Response Mode

- [ ] Not explicitly stated
- [x] Multiple choice
- [x] Short text
- [ ] Long-form text
- [x] Structured output, such as JSON or XML
- [ ] Code
- [x] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or artifact generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment

Other response modes/comments: The standard response includes an answer and confidence; explanations may be requested as part of the prompting protocol.

Required output format, if any: The repository and paper document answer/confidence formatting; model-judge scoring expects parseable final answers.

### 2.7 Prerequisites for Evaluated Systems

| Requirement                                                     | Irrelevant or not necessary | Necessary information given | Information missing | Evidence / notes                                                                                                |
| :-------------------------------------------------------------- | :-------------------------: | :-------------------------: | :-----------------: | :-------------------------------------------------------------------------------------------------------------- |
| Language support                                                |            - [ ]            |            - [x]            |        - [ ]        | English academic questions are the public-set norm.                                                             |
| Context length                                                  |            - [ ]            |            - [ ]            |        - [x]        | Item prompts are finite, but no general context-length threshold is specified.                                  |
| Multimodal input support                                        |            - [ ]            |            - [x]            |        - [ ]        | Needed for the full benchmark because a minority of items include images.                                       |
| Structured output support                                       |            - [ ]            |            - [x]            |        - [ ]        | Expected for answer/confidence extraction.                                                                      |
| Exact format, schema, or parser compatibility                   |            - [ ]            |            - [x]            |        - [x]        | Answer/confidence formatting and extraction are documented, but parser edge cases and validation are limited.   |
| Retry, repair, or correction-loop support for malformed outputs |            - [ ]            |            - [ ]            |        - [x]        | A standardized retry, repair, fallback, or manual-adjudication policy for malformed model outputs is not clear. |
| Tool access                                                     |            - [x]            |            - [ ]            |        - [ ]        | Standard HLE answering does not use tools.                                                                      |
| Browser or internet access                                      |            - [x]            |            - [ ]            |        - [ ]        | Standard evaluation is intended to avoid web lookup.                                                            |
| Code execution                                                  |            - [x]            |            - [ ]            |        - [ ]        | Not part of standard evaluated system behavior.                                                                 |
| Memory or persistent state                                      |            - [x]            |            - [ ]            |        - [ ]        | No persistent-state requirement is described.                                                                   |
| API compatibility                                               |            - [ ]            |            - [x]            |        - [ ]        | Repository examples use OpenAI-compatible API calls.                                                            |
| Latency or time budget                                          |            - [ ]            |            - [ ]            |        - [x]        | No model response time budget is specified.                                                                     |
| Cost or compute budget                                          |            - [ ]            |            - [ ]            |        - [x]        | Token counts are reported, but full cost/compute budgets are not specified.                                     |

Other requirements/comments: Full-set participation requires image input support; text-only comparisons should not be treated as equivalent to full-set comparisons.

Review notes: The benchmark is designed around API-evaluable language/multimodal systems, but the official materials do not fully document local-inference equivalence.

### 2.8 Evaluation Conditions

| Condition                         | Description                                                                                                                   |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| Prompting protocol                | Official prompt asks for a final answer and confidence; paper reports standardized prompting and model evaluation conditions. |
| System prompt                     | Documented in official materials for the evaluation protocol; adapted when systems do not support system prompts.             |
| Few-shot examples                 | Not documented as part of the standard HLE protocol.                                                                          |
| Sampling settings                 | Paper reports model-specific temperature settings; most deterministic-capable models are evaluated at low/zero temperature.   |
| Tool permissions                  | No tool use for model answering; search tools used by maintainers for searchability auditing.                                 |
| Time limits                       | Not documented.                                                                                                               |
| Human intervention rules          | Humans contribute, review, and audit items; no human intervention is described during model answering.                        |
| Hardware or hosted service        | Official results use named hosted frontier models; repository examples use API calls.                                         |
| Network requirements              | Required for Hugging Face download and API-hosted model calls in repository examples.                                         |
| Sandbox or security constraints   | Not documented.                                                                                                               |
| Special administration conditions | Private held-out set and HLE-Rolling support integrity and maintenance beyond the public static set.                          |

Other conditions/comments: Published result replication requires exact model versions, prompts, judge configuration, API behavior, and data snapshot.

Review notes: The main evaluation conditions are documented enough for cautious reruns, but not enough for high-precision reproduction of all published comparisons.

### 2.9 Task and Response Types

Selection-based responses:

- [x] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [ ] Ranking
- [ ] Classification
- [ ] Pairwise preference

Production-based responses:

- [x] Open-ended text
- [ ] Code generation
- [x] Proof, derivation, or explanation
- [x] Structured data
- [ ] Generated media
- [ ] Artifact production

Interaction-based responses:

- [ ] Tool use
- [ ] Browser or web navigation
- [ ] API interaction
- [ ] Computer-use interaction
- [ ] Simulated environment task
- [ ] Real or external environment task

Process data:

- [ ] Response latency
- [x] Token usage
- [ ] Cost
- [ ] Tool traces
- [ ] Intermediate reasoning traces
- [ ] Execution logs

Other task/response types: Model-reported confidence is part of the evaluation output.

Review notes: The benchmark is primarily closed-ended QA, not an interaction or agent benchmark.

### 2.10 Input Stimulus Type

- [ ] Not explicitly stated
- [x] Text
- [ ] Code
- [ ] Tables or structured data
- [x] Images
- [ ] Audio
- [ ] Video
- [ ] Documents
- [ ] Web pages
- [ ] APIs or tools
- [ ] Dynamic environment

Other stimulus types/comments: Mathematical notation, scientific notation, and discipline-specific diagrams or figures occur in the item set.

### 2.11 Number of Items or Measurement Points

| Prompt                                  | Response                                                                                                            |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| Total public items or tasks             | 2,500 final public questions.                                                                                       |
| Total private or hidden items           | Private held-out set documented, but exact count and access process are not fully public.                           |
| Development or example items            | Example questions are shown in the paper and website; full development-item count is not separately specified.      |
| Test items                              | Public 2,500-question set plus private/rolling components.                                                          |
| Dynamic or generated tasks              | HLE-Rolling is a maintained rolling variant, not procedurally generated tasks in the standard public set.           |
| Episodes, trials, or measurement points | One score opportunity per question in standard scoring; repeat-run protocol for reliability is not fully specified. |
| Item count uncertainty                  | Public count is clear; private and rolling counts are partially documented.                                         |

Review notes: Public-set count is stable; rolling and private components require date-stamped review.

### 2.12 Mode of Evaluation

- [ ] Not indicated
- [x] Local batch evaluation
- [x] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [ ] Interactive agent evaluation
- [ ] Human-in-the-loop evaluation
- [x] Continuous or rolling evaluation

Other modes/comments: Public users can run repository scripts locally/API-side; HLE-Rolling provides hosted submission context.

Identity and condition controls:

- [ ] No control over submitted systems
- [x] Some control over submitted systems
- [ ] Controlled model access or audit
- [x] Controlled evaluation center or private harness
- [ ] Not documented

Review notes: Hosted/private components improve integrity but their governance is not fully specified in public materials.

### 2.13 Technological Arrangements

| Technology            |   A   |   R   | Evidence / notes                                                                                 |
| :-------------------- | :---: | :---: | :----------------------------------------------------------------------------------------------- |
| API access            | - [x] | - [x] | Repository examples use model API calls.                                                         |
| Local inference       | - [ ] | - [ ] | Not a primary documented path.                                                                   |
| GPU                   | - [ ] | - [ ] | Not required for API evaluation; local requirements not specified.                               |
| CPU-only execution    | - [ ] | - [ ] | Scoring scripts may run locally, but full local model evaluation is not documented.              |
| Docker or container   | - [ ] | - [ ] | Not documented.                                                                                  |
| Python package or CLI | - [x] | - [ ] | Python scripts and requirements are provided.                                                    |
| Browser               | - [x] | - [ ] | Browser needed for web dashboard, not model answering.                                           |
| External tools        | - [ ] | - [ ] | Not used in standard model answers.                                                              |
| Internet access       | - [x] | - [x] | Needed for API and hosted data/download paths.                                                   |
| Proprietary platform  | - [x] | - [ ] | Published comparisons use proprietary frontier models; benchmark itself is not only proprietary. |

Other technologies/comments: Hugging Face access and API credentials are practical requirements for common use.

### 2.14 Time and Resource Requirements

| Activity                           | Time, compute, or cost estimate                                                                      |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------- |
| Setup                              | Repository setup is documented through Python requirements, but full setup time is not estimated.    |
| Model inference or task completion | Token counts are reported in the paper; wall-clock or API-cost estimates are not fully specified.    |
| Scoring                            | Repository judge script exists; time/cost estimate not specified.                                    |
| Human adjudication                 | Item development involved expert review, but user-side adjudication is not part of standard scoring. |
| Analysis or reporting              | Not documented.                                                                                      |
| Full benchmark run                 | Not documented as a time/cost budget.                                                                |
| API or compute cost                | Not documented as a budget; depends on model provider and item subset.                               |

Other requirements/comments: Cost and runtime can be material for 2,500 expert questions, especially if explanations and judge calls are used.

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant               | Purpose                                                 | Equivalence claim                                            | Status                                      |
| :---------------------------- | :------------------------------------------------------ | :----------------------------------------------------------- | :------------------------------------------ |
| Public HLE 2,500-question set | Main public static evaluation set.                      | Baseline public form for current review.                     | Public with Hugging Face acknowledgement.   |
| Private held-out set          | Assess overfitting and gaming beyond the public set.    | Intended integrity check; equivalence details are limited.   | Hidden/private.                             |
| Text-only subset              | Permit comparison of non-multimodal systems.            | Not equivalent to full set because image items are excluded. | Public subset derivable from item metadata. |
| HLE-Rolling                   | Maintain freshness through rolling submissions/updates. | Score comparability with static set is partially documented. | Hosted/maintained variant.                  |

Other forms/comments: The official website states that the final public set superseded the earlier public preview.

### 2.16 Static or Dynamic Task Determination

- [x] Static fixed task set
- [ ] Random sample from fixed pool
- [x] Hidden test set selected by maintainers
- [ ] Procedurally generated tasks
- [ ] Adaptive routing based on performance
- [ ] Dynamic environment generation
- [x] Rolling or periodically refreshed task set
- [ ] Not explicitly stated

Other task selection/comments: HLE combines a static public set, hidden/private integrity material, and rolling maintenance.

Describe task selection method: Expert-contributed questions were reviewed and audited for difficulty, answerability, precision, and non-searchability before inclusion.

### 2.17 Evidence Sources Used in Scoring

- [x] Model final answer
- [ ] Model intermediate trace
- [ ] Tool-use trace
- [ ] Code execution result
- [ ] Environment state
- [x] Reference answer
- [ ] Unit test
- [ ] Human judge
- [x] Model judge
- [ ] Ensemble or panel adjudication
- [ ] External verifier

Other scoring inputs/comments: Model confidence is used for calibration-related outputs.

Review notes: Human experts are central to item development, but standard scoring is automated/model-judge based.

---

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

- [ ] Not explicitly stated
- [x] Automated exact-match scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] Unit-test or execution-based scoring
- [x] Rule-based scoring
- [ ] Human rating
- [x] Model-as-judge scoring
- [x] Output parser or extractor
- [x] Fuzzy, schema-aware, or admissible-variant parsing
- [ ] Pairwise preference scoring
- [x] Hybrid automated and human scoring
- [x] Leaderboard service scoring
- [ ] Manual adjudication

Other scoring methods/comments: Hybrid here means human review is used for item development and automated/model-judge methods are used for routine scoring; it does not mean every model answer receives human adjudication.

Review notes: Pipeline details appear below in Section 3.2.

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or metric  | Definition                                                 | Aggregation                                                                         | Interpretation stated by authors                                                                             |
| :--------------- | :--------------------------------------------------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| Primary score    | Accuracy / percent correct.                                | Correct items divided by evaluated items, reported overall and in selected subsets. | Higher score indicates better performance on difficult closed-ended academic questions under HLE conditions. |
| Subscore         | Domain/category accuracy; text-only subset accuracy.       | Items grouped by official category or subset.                                       | Helps compare strengths across broad academic areas and modality constraints.                                |
| Derived score    | RMS calibration error and confidence summaries.            | Model-reported confidence compared against correctness.                             | Indicates calibration of confidence against answer accuracy.                                                 |
| Qualitative band | No official proficiency bands documented for model scores. | Not applicable.                                                                     | Avoid treating arbitrary percentages as validated proficiency thresholds.                                    |

Treatment of invalid, missing, malformed, or refused responses: Repository scripts and judge scoring handle answer extraction, but full malformed/refusal policy and parser validation are not comprehensively documented.

Response-format retry, repair, parser fallback, or manual adjudication policy: Not comprehensively documented. The reviewed materials expect parseable answer/confidence outputs, but do not specify a standardized retry, repair, relaxed-parser fallback, or human adjudication path for malformed responses in routine scoring.

Review notes: HLE scoring is plausible for closed-ended items but depends on answer extraction and judge behavior that require stronger validation for high-stakes comparisons.

### 3.3 Scale or Metric Types

- [ ] Raw score
- [x] Accuracy
- [ ] Success rate
- [ ] Pass rate or pass@k
- [ ] Unit-test pass rate
- [ ] Win rate
- [ ] Elo or ranking score
- [ ] Pairwise preference score
- [ ] Reward or return
- [ ] Cost-adjusted score
- [x] Calibration or uncertainty score
- [ ] Percentile or normalized score
- [ ] Threshold or decision index

Other metric types/comments: The repository simple evaluator can output aggregate summary statistics, but the official interpretive metric remains accuracy plus calibration-related reporting.

### 3.4 Score Transformation

- [x] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against baseline
- [ ] Weighting across subdomains
- [x] Aggregation formula documented
- [ ] Aggregation formula partially documented
- [ ] Aggregation formula not documented
- [ ] Not applicable

Formula or transformation comments: Accuracy is a simple proportion/percentage. Category and subset scores are descriptive aggregates.

### 3.5 Reference Groups, Baselines, and Comparators

- [ ] No baseline or comparator documented
- [x] Random or chance baseline
- [ ] Human baseline
- [x] Expert human baseline
- [x] Model baseline
- [x] Previous model cohort
- [x] Commercial system comparator
- [ ] Open-weight model comparator
- [x] Domain-specific reference group

Other comparators/comments: Multiple-choice items create a chance floor; expert humans are involved in item creation/review but full expert benchmark-taking distributions are not public.

| Comparator or baseline               | Construction method                                                                                    | Intended interpretation                                             |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Random or chance baseline            | Non-zero floor for multiple-choice questions; not a full formal random baseline across all item types. | Prevents interpreting all near-zero scores as equally below chance. |
| Human baseline                       | Not fully documented as a benchmark-taking sample.                                                     | Not available for norm-like interpretation.                         |
| Expert baseline                      | Domain experts created and reviewed questions; paper frames items as expert-level.                     | Supports item difficulty and target level, not a full human norm.   |
| Model cohort                         | Named frontier model results in official paper and current HLE materials.                              | Supports contemporaneous model comparison.                          |
| Prior benchmark or version           | HLE motivated by saturation of prior academic benchmarks; HLE-Rolling updates are documented.          | Provides context for difficulty and maintenance.                    |
| Criterion threshold or floor/ceiling | No validated proficiency threshold; saturation/rolling concerns documented.                            | Avoid arbitrary pass/fail interpretation.                           |

Review notes: HLE has meaningful model comparators and expert item-development context, but not full human norming or uncertainty-aware thresholds.

### 3.6 Score Uncertainty and Stability

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Hierarchical, clustered, or item-level bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [ ] Sensitivity analyses
- [ ] Prompt, input-perturbation, or response-format sensitivity metrics
- [ ] IRT, adaptive testing, or item-parameter precision estimates
- [x] Not reported

Other uncertainty/stability comments: Some repository sample outputs include aggregate uncertainty-style fields, but the official model comparisons do not provide a complete uncertainty and repeat-run framework.

Review notes: This is a major limitation for interpreting small differences between model scores.

### 3.7 Metric-to-Claim Linkage

| Prompt                                                                   | Response                                                                                                                                                                                                                   |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why the primary metric was chosen                                        | Accuracy fits closed-ended answerability, where a final answer can be judged correct or incorrect.                                                                                                                         |
| Whether metric floors or ceilings are documented                         | Multiple-choice floor and benchmark saturation concerns are discussed, but floors/ceilings are not fully quantified across item types.                                                                                     |
| Whether the metric may reward non-target behavior named by the benchmark | The official materials discuss non-searchability and benchmark gaming/contamination risk; model-judge and formatting issues remain possible non-target contributors.                                                       |
| Whether parsing, judge, or scorer validation is documented               | Judge prompt and scoring scripts are public; comprehensive scorer validation is not documented.                                                                                                                            |
| Whether response-format burden is separated from the target capability   | Partially. The answer/confidence format is explicit, but the reviewed materials do not fully test whether formatting, extraction, refusal handling, or judge behavior affects scores independently of academic capability. |
| Whether perturbation or prompt-sensitivity evidence affects the claim    | Not documented. Official prompting is described, but no systematic prompt, input-perturbation, or response-format sensitivity evidence is reported.                                                                        |
| Whether score uncertainty affects claim interpretation                   | Yes, because published scores are point estimates without full repeat-run uncertainty.                                                                                                                                     |
| Whether score differences are interpreted statistically                  | Formal significance testing is not documented in the reviewed official materials.                                                                                                                                          |
| Whether benchmark reports state what users should not infer              | Yes. Official discussion cautions against AGI/autonomous research inference from HLE score alone.                                                                                                                          |

Review notes: The metric-to-claim link is strongest for closed-ended academic performance and weakens for broad public interpretations.

---

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

- [x] Public leaderboard available
- [x] Public aggregate scores available
- [x] Public per-domain scores available
- [ ] Public per-item scores available
- [ ] Public raw model outputs available
- [ ] Public traces or logs available
- [ ] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

Other output availability/comments: HLE-Rolling includes a live submission dashboard; the static paper provides aggregate and category reporting but not raw outputs.

### 4.2 Output Name or Description

| Output                                 | Description                                                                    | Public/private                               |
| :------------------------------------- | :----------------------------------------------------------------------------- | :------------------------------------------- |
| Nature/paper result tables and figures | Overall, category, text-only/full-set, token, and calibration-related results. | Public article/preprint context.             |
| Repository evaluator output            | Local/API evaluator summary output.                                            | Public tool output, generated by user.       |
| HLE-Rolling live submission dashboard  | Hosted rolling submission/results context linked from lastexam.ai.             | Public/hosted, governance partly documented. |

Review notes: Reported outputs are useful but not a full reproducibility-grade result archive.

### 4.3 Output Design or Presentation

- [x] Static text report
- [x] Tables
- [x] Graphs or visualizations
- [x] Leaderboard
- [x] Interactive dashboard
- [ ] Downloadable CSV or JSON
- [ ] API output
- [ ] Paper-only results

Other presentation/comments: The paper and website provide several output surfaces; raw result downloads are not documented.

### 4.4 Output Structure

- [x] Aggregate-score based
- [x] Capability-domain based
- [x] Task-family based
- [ ] Criterion-threshold based
- [ ] Pairwise-comparison based
- [x] Rank based
- [ ] Cost or efficiency adjusted
- [ ] Error-analysis based
- [ ] Trace or process based

Other output structure/comments: Token count reporting exists, but no cost-adjusted score is defined.

### 4.5 Sensitivity to Context

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [x] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts: Static public paper results, public set evaluation, text-only subset, full multimodal set, private held-out evaluation, and rolling hosted evaluation.

Review notes: The context labels are meaningful, but score comparability across static, private, and rolling settings needs further documentation.

### 4.6 Development of Outputs

- [x] Based on benchmark authors' design
- [ ] Based on empirical or actuarial relationships
- [x] Based on expert judgment
- [ ] Based on human annotation
- [x] Based on model-as-judge outputs
- [x] Automatically generated by benchmark platform

Other development basis/comments: Expert judgment shapes item selection; automated/model-judge scoring shapes output.

Describe origin of report content: Paper report content is author-generated from official evaluation runs; repository output is generated by scripts; HLE-Rolling output is hosted.

### 4.7 Modifiability

- [ ] Not modifiable
- [x] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

Review notes: Users can run scripts and create local outputs; official paper and rolling outputs are controlled by maintainers/platform.

### 4.8 Transparency

- [ ] Clear linkage between tasks, scores, and reported claims
- [x] Partial linkage between tasks, scores, and reported claims
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Review notes: The score-to-claim link is transparent at a high level, but item-level results, raw outputs, scorer validation, and uncertainty are missing.

### 4.9 Output Content

- [x] Capability descriptions
- [x] Aggregate rankings
- [x] Subdomain comparisons
- [ ] Error categories
- [x] Examples of successes or failures
- [x] Cost, latency, or efficiency data
- [ ] Process traces
- [ ] Recommendations or interpretation notes
- [x] Warnings or caveats

Other output content/comments: Token count is reported; cost and latency are not fully reported.

### 4.10 Intended Recipients

- [x] Benchmark maintainers
- [x] Model developers
- [x] AI researchers
- [x] Safety evaluators
- [x] Policy or governance actors
- [ ] Product or deployment teams
- [ ] Procurement teams
- [x] Public audience

Other recipients/comments: The Nature article broadens the audience beyond technical benchmark users.

---

## Section 5. Benchmark Access, Artifacts, and Lifecycle

### 5.1 Supporting Information Provided

- [x] Technical report
- [ ] User guide
- [x] Repository README
- [ ] API documentation
- [x] Dataset card
- [ ] Model submission instructions
- [x] Scoring documentation
- [x] Rubric or annotation guide
- [x] Evaluation examples
- [ ] FAQ or discussion forum
- [x] Changelog or release notes

Other supporting materials/comments: HLE-Rolling dashboard and website add operational materials beyond the original paper.

### 5.2 Methods of Publication

- [x] Academic paper
- [x] Benchmark website
- [x] Git repository
- [ ] Package registry
- [x] Dataset hosting platform
- [x] Leaderboard platform
- [x] Downloadable documents
- [ ] Private distribution

Other publication methods/comments: Private held-out materials are intentionally not publicly distributed.

### 5.3 User Requirements or Qualifications

| Requirement type                             | Requirement                                                                                                                  |
| :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Technical skill                              | Ability to run Python scripts, manage API credentials, and handle Hugging Face datasets.                                     |
| Model access                                 | API access or compatible model endpoint for evaluated systems.                                                               |
| Dataset access                               | Hugging Face access acknowledgement for public task set.                                                                     |
| Compute or budget                            | Not specified; API cost depends on chosen model and subset.                                                                  |
| Human expertise                              | Needed for responsible interpretation and any manual audit of item or scorer behavior.                                       |
| Account, license, or competition eligibility | Hugging Face account/acknowledgement may be required; HLE-Rolling hosted submission may have platform-specific requirements. |
| Ethical, safety, or data-use obligations     | Public task set should not be used for training or fine-tuning, according to dataset access terms and repository warnings.   |

Other requirements/comments: Users should preserve the non-training warning when redistributing or citing HLE materials.

### 5.4 Dataset and Item Access

| Component                                      | Public | Restricted | Hidden | Not available | Evidence / notes                                                                                        |
| :--------------------------------------------- | :----: | :--------: | :----: | :-----------: | :------------------------------------------------------------------------------------------------------ |
| Training or development items                  | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | HLE is not primarily released as a train/dev/test suite.                                                |
| Public evaluation items                        | - [x]  |   - [x]    | - [ ]  |     - [ ]     | Public 2,500 set via Hugging Face with access acknowledgement.                                          |
| Private or held-out evaluation items           | - [ ]  |   - [ ]    | - [x]  |     - [ ]     | Private set described for overfitting/gaming checks.                                                    |
| Secret, encrypted, or reserve evaluation items | - [ ]  |   - [ ]    | - [x]  |     - [ ]     | Private reserve materials are described, but cryptographic or proctored reserve details are not public. |
| Retired or archived evaluation items           | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | HLE-Rolling changes are public, but a systematic retired-item archive was not documented.               |
| Answer keys or reference solutions             | - [x]  |   - [x]    | - [ ]  |     - [ ]     | Available as part of evaluation materials; access follows dataset terms.                                |
| Metadata or annotations                        | - [x]  |   - [x]    | - [ ]  |     - [ ]     | Public metadata exists, but full item-development metadata is not public.                               |
| Raw model outputs or logs                      | - [ ]  |   - [ ]    | - [ ]  |     - [x]     | Published model-run raw outputs are not documented as public.                                           |

Other access/comments: Public access is meaningful but not fully open in the sense of unrestricted anonymous download.

### 5.5 Provenance and Contamination Documentation

| Topic                                                      | Documented | Partially documented | Not documented | Evidence / notes                                                                                                      |
| :--------------------------------------------------------- | :--------: | :------------------: | :------------: | :-------------------------------------------------------------------------------------------------------------------- |
| Data origin or task creation                               |   - [x]    |        - [ ]         |     - [ ]      | Expert-contributed and reviewed questions.                                                                            |
| Persistent dataset or artifact identifier                  |   - [x]    |        - [ ]         |     - [ ]      | DOI/arXiv, Hugging Face dataset entry, GitHub repository, and citation metadata provide stable public anchors.        |
| Author or contributor qualifications                       |   - [x]    |        - [ ]         |     - [ ]      | Contributor and author information is extensive.                                                                      |
| Deduplication or overlap checks                            |   - [ ]    |        - [x]         |     - [ ]      | Searchability and audit procedures are described; formal deduplication metrics are limited.                           |
| Public/private split rationale                             |   - [ ]    |        - [x]         |     - [ ]      | Rationale is documented; size and comparability details are limited.                                                  |
| Contamination screening                                    |   - [x]    |        - [ ]         |     - [ ]      | Non-searchability checks, search-enabled audit, private holdout, canary, and non-training warning are documented.     |
| Canary strings or training-data warnings                   |   - [x]    |        - [ ]         |     - [ ]      | Repository includes canary and warning against inclusion in training corpora.                                         |
| Memorization or `training_on_test_set` diagnostic task     |   - [ ]    |        - [ ]         |     - [x]      | Canary and non-training warnings exist, but no dedicated memorization diagnostic task was documented.                 |
| Pre-exposure or source-material searchability checks       |   - [x]    |        - [ ]         |     - [ ]      | Official materials describe non-searchability checks and search-enabled auditing.                                     |
| Hash commitments, signatures, or tamper-evident audit logs |   - [ ]    |        - [ ]         |     - [x]      | No hash commitment, signature, or tamper-evident public audit-log mechanism was documented.                           |
| Encrypted, secret, or controlled-release item reserve      |   - [ ]    |        - [x]         |     - [ ]      | Private held-out materials are described, but access-control, encryption, and release mechanics are not fully public. |
| Refresh or rotation policy                                 |   - [ ]    |        - [x]         |     - [ ]      | HLE-Rolling exists; full comparability policy remains limited.                                                        |
| Reporting of known leaks or retired items                  |   - [ ]    |        - [x]         |     - [ ]      | Rolling change file records updates/fixes; leak reporting policy is not comprehensive.                                |

Other provenance/contamination comments: HLE has stronger contamination documentation than many public benchmarks, but ongoing public exposure remains a risk.

### 5.6 Reproducibility Materials

- [x] Complete task data
- [x] Complete prompt templates
- [x] Evaluation harness
- [x] Scoring code
- [x] Environment file or dependency list
- [ ] Container or reproducible environment
- [ ] Version pinning
- [ ] Random seeds or deterministic settings
- [ ] Raw outputs
- [ ] Reproduction script for published results
- [ ] Push-button replication script or single documented command
- [ ] Expected-output fixtures or smoke-test example
- [ ] Continuous integration or test suite
- [ ] Public build status or equivalent passing-test signal

Other reproducibility comments: Reproducibility is adequate for independent reruns of the public set, but not for exact replication of published model tables.

### 5.7 Maintenance and Versioning

| Topic                                                    | Response                                                                                                             |
| :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Maintainer identity                                      | Center for AI Safety / Scale AI ecosystem; GitHub repository under `centerforaisafety/hle`.                          |
| Version naming or release tags                           | No conventional release tags reviewed; public final set and HLE-Rolling are the main version concepts.               |
| Changelog or update record                               | HLE-Rolling change file is public.                                                                                   |
| Issue or feedback process                                | GitHub issues and website feedback/submission links.                                                                 |
| Item correction process                                  | Rolling update file suggests corrections/additions, but detailed process is limited.                                 |
| Deprecated item handling                                 | Partially documented through rolling changes.                                                                        |
| Private-set refresh policy                               | Not fully documented.                                                                                                |
| Last code-usability or harness health check              | Not documented in the reviewed materials.                                                                            |
| Build, CI, or smoke-test status                          | Not documented.                                                                                                      |
| Saturation threshold or retirement criteria              | Saturation motivates HLE-Rolling, but formal retirement criteria are not documented.                                 |
| Retirement, deprecation, or archival policy              | Not documented.                                                                                                      |
| Retired-item publication or audit policy                 | Partially documented through the rolling change file; no full retired-item audit policy was reviewed.                |
| Score comparability across versions                      | Partially documented; HLE-Rolling may improve freshness but complicates longitudinal comparison.                     |
| Cohort, rolling-window, or temporal comparability policy | Partially documented through HLE-Rolling, but cohort labels, stale-score handling, and linking/equating are limited. |
| Long-term archival plan                                  | Not documented.                                                                                                      |

Review notes: HLE-Rolling is a strength for maintenance, but versioned score interpretation needs more detail.

---

## Appendix A. General Description of the Benchmark

Humanity's Last Exam is an expert-level closed-ended academic benchmark for frontier AI systems. The current official public set contains 2,500 questions across over 100 subject areas, including text-only and image-containing items. Models answer questions and provide confidence; scoring reports accuracy and calibration-related outputs. The benchmark was built through expert contribution, review, auditing, and non-searchability checks, and it now has a Nature article, arXiv preprint, public GitHub repository, Hugging Face task set, official website, and HLE-Rolling maintained variant. Its narrowest defensible interpretation is performance on difficult closed-ended academic questions under documented HLE conditions, not standalone evidence of AGI or autonomous research capability.

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether HLE is adequate as a measurement instrument for its intended use.

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
- Review note: Basis: HLE defines a narrow purpose around difficult closed-ended academic questions for frontier AI systems. Gap: no formal psychometric construct definition or CHC-style ability map. Rationale: good for expert-level academic performance. Caution: the benchmark name and subject breadth should not be read as validated general intelligence.

#### 6.1.2 Summary of prior research and benchmark context

- Rating: `3`
- Review note: Basis: The official paper situates HLE against saturated academic and frontier-model benchmarks. Gap: the prior-benchmark critique is not a complete measurement-theory review. Rationale: context is clear enough for intended research use. Caution: benchmark novelty does not itself establish validity.

#### 6.1.3 Phenomenon-task-metric-claim chain

- Rating: `3`
- Review note: Basis: Questions, answer extraction, model judging, accuracy, and calibration outputs form a plausible task-to-metric chain. Gap: scorer validation and construct-irrelevant variance analysis are incomplete. Rationale: linkage is mostly explicit for closed-ended academic answering. Caution: formatting, memorization, and judge behavior may affect scores.

#### 6.1.4 Task or item design

- Rating: `3`
- Review note: Basis: Text and image-containing closed-ended items, answer confidence, and domain coverage are documented. Gap: some scoring and administration decisions are not fully justified quantitatively. Rationale: task design fits the stated academic stress-test purpose. Caution: item difficulty and domain breadth are not equivalent to cognitive breadth.

#### 6.1.5 Procedures for developing task or item content

- Rating: `3`
- Review note: Basis: Expert contribution, review rubrics, auditing, and non-searchability checks are documented. Gap: full reviewer records and inclusion/exclusion metadata are not public. Rationale: the development procedure is strong for a public AI benchmark. Caution: unavailable process detail limits independent audit.

#### 6.1.6 Thoroughness of the final task or item selection process

- Rating: `3`
- Review note: Basis: The final public set reflects review, revision, auditing, and selection for difficulty and answerability. Gap: full item-selection trace and rejected-item analysis are not public. Rationale: selection appears careful and documented at a useful level. Caution: representativeness across all academic domains remains partly inferential.

#### 6.1.7 Quantitative evidence of task or item quality

- Rating: `1`
- Review note: Basis: Official results report model performance and calibration outputs. Gap: item-level difficulty, discrimination, redundancy, and domain-level psychometric diagnostics are limited. Rationale: quantitative item-quality evidence is underdeveloped. Caution: domain and item behavior should not be overinterpreted without stronger diagnostics.

#### 6.1.8 Adaptation, translation, or benchmark version derivation

- Rating: `2`
- Review note: Basis: HLE-Rolling and public/private variants are documented. Gap: rolling-update equivalence and comparability with the public set are only partly specified. Rationale: adequate for cautious interpretation of maintained variants. Caution: longitudinal comparisons need explicit version labels.

#### 6.1.9 Overall quality of rationale, development, and task or item quality

- Rating: `3`
- Review note: Basis: Rationale, expert development, and task quality are well documented for a closed-ended academic benchmark. Gap: quantitative item evidence and broad construct modeling remain incomplete. Rationale: overall support is good for the bounded interpretation. Caution: this rating is not a broad intelligence endorsement.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- Rating: `3`
- Review note: Basis: Official materials explain HLE's purpose, intended frontier-model context, and important non-AGI caveats. Gap: non-use cases are not developed as a formal user guide. Rationale: purpose documentation is good. Caution: public summaries may omit the caveats.

#### 6.2.2 Documentation of development process

- Rating: `3`
- Review note: Basis: The paper and repository describe expert contribution, review, auditing, and non-searchability checks. Gap: complete item provenance and reviewer workflow metadata are unavailable. Rationale: development documentation is mostly complete for qualified users. Caution: independent reconstruction is limited.

#### 6.2.3 Documentation of scoring and metrics

- Rating: `3`
- Review note: Basis: Accuracy, confidence, calibration, answer prompts, and judge prompts are documented. Gap: malformed-output handling and full judge validation are incomplete. Rationale: scoring is understandable. Caution: exact reproduction of published scores requires additional run metadata.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- Rating: `1`
- Review note: Basis: Some evaluation settings are reported. Gap: repeat-run variance, seeds, prompt sensitivity, provider drift, and statistical uncertainty are not comprehensively documented. Rationale: reliability documentation is weak. Caution: small score differences should not be treated as stable.

#### 6.2.5 Documentation of validity evidence

- Rating: `2`
- Review note: Basis: Content support, item-development rationale, and claim caveats are provided. Gap: no full validity argument across internal structure, external criteria, scorer validity, and uncertainty. Rationale: adequate for cautious use. Caution: validity is content-heavy rather than comprehensive.

#### 6.2.6 Documentation of fair use and comparability

- Rating: `2`
- Review note: Basis: Text-only/full-set distinctions, standard prompts, and intended-system framing support fair comparison. Gap: language, accessibility, local/API comparability, and subgroup coverage are limited. Rationale: fair-use documentation is adequate but incomplete. Caution: compare only matched modalities and conditions.

#### 6.2.7 Documentation of maintenance and versioning

- Rating: `2`
- Review note: Basis: HLE-Rolling change records and public artifacts document maintenance. Gap: formal versioning, deprecation, and comparability policy are limited. Rationale: maintenance is visible but not fully governed. Caution: rolling changes complicate score comparison.

#### 6.2.8 Adequacy of documentation available to users

- Rating: `3`
- Review note: Basis: Nature, arXiv, GitHub, Hugging Face, website, and changelog materials provide substantial documentation. Gap: exact replication package, raw outputs, and private-set details remain absent. Rationale: good enough for qualified public use. Caution: users need technical judgment to avoid overinterpretation.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- Rating: `2`
- Review note: Basis: Repository examples document prompt and API-based evaluation steps. Gap: environment locking, seeds, provider drift, credentials, and failure handling are incomplete. Rationale: setup is adequate for skilled reruns. Caution: it is not a full reproduction protocol.

#### 6.3.2 Scoring procedure and error handling

- Rating: `2`
- Review note: Basis: The judge script and scoring path are public. Gap: parser failures, malformed outputs, refusals, missing responses, and overrides are not fully specified. Rationale: scoring procedure supports cautious use. Caution: edge-case handling can affect model comparisons.

#### 6.3.3 Interpretation and reporting guidance

- Rating: `2`
- Review note: Basis: Official materials explain accuracy, calibration, text-only/full-set distinctions, and AGI caveats. Gap: no full guide to meaningful differences, uncertainty, or high-stakes interpretation. Rationale: interpretation support is adequate. Caution: avoid treating ranks as precise.

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- Rating: `2`
- Review note: Basis: Non-training warnings, modality distinctions, and standard no-tool answering are described. Gap: unsupported systems, API/local equivalence, and response-time or cost assumptions are incomplete. Rationale: restrictions are usable but not comprehensive. Caution: deviations should be reported.

#### 6.3.5 Technical support and implementation guidance

- Rating: `2`
- Review note: Basis: Requirements and scripts are available. Gap: no container, full CI evidence, troubleshooting matrix, or exact published-run replay instructions. Rationale: implementation guidance is adequate for technical users. Caution: independent results may vary by endpoint and judge configuration.

#### 6.3.6 References and supporting materials

- Rating: `3`
- Review note: Basis: Official paper, arXiv record, repository, dataset host, website, citation, and changelog are linked. Gap: some validation and raw-output materials are absent. Rationale: supporting references are good. Caution: contextual literature should not replace official facts.

#### 6.3.7 Quality of procedural instructions

- Rating: `2`
- Review note: Basis: Administration, scoring, and interpretation instructions exist. Gap: reproducibility-grade setup, error handling, and uncertainty guidance are incomplete. Rationale: procedural quality is adequate but not strong. Caution: users should document all run conditions.

### 6.4 Overall Adequacy of Rationale and Documentation

#### 6.4 Overall adequacy of rationale and documentation

- Rating: `3`
- Review note: Basis: HLE provides strong rationale, public documentation, and expert-development evidence. Gap: reliability, scorer validation, and exact reproduction support are weaker. Rationale: overall Section 6 support remains good for bounded academic answering. Caution: do not mechanically average this with later validity and reliability gaps.

Review notes:

Section 6 is HLE's strongest area because official materials explain why the benchmark exists and how the task set was created.

---

## Section 7. Quality and Usability of Benchmark Artifacts

MESA evaluates benchmark artifacts: datasets, task files, prompts, rubrics, scoring code, harnesses, interfaces, access routes, setup instructions, accessibility, and usability. Artifact quality includes both what is available and whether intended users can run or inspect it without hidden procedural knowledge.

### 7.1 Quality of Benchmark Artifacts

#### 7.1.1 Dataset, task set, or evaluation environment availability

- Rating: `3`
- Review note: Basis: The public 2,500-question set, repository, hosted data, website, and scripts are available. Gap: private artifacts and full development metadata are not public. Rationale: dataset availability is good for public research. Caution: public availability increases contamination risk over time.

#### 7.1.2 Prompts, instructions, and input artifacts

- Rating: `3`
- Review note: Basis: Prompt templates, answer/confidence instructions, and judge prompts are documented. Gap: model-specific prompt adaptation and parser validation remain incomplete. Rationale: input artifacts are clear for intended users. Caution: prompt differences should be reported.

#### 7.1.3 Rubrics, reference answers, and response format requirements

- Rating: `3`
- Review note: Basis: Reference-answer style scoring, human review rubrics, confidence reporting, and model-judge criteria are described. Gap: full answer-equivalence and adjudication validation are incomplete. Rationale: response requirements are clear. Caution: strict formatting can introduce non-target variance.

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- Rating: `2`
- Review note: Basis: GitHub provides simple evaluation and judge scripts. Gap: no robust containerized harness, full tests, CI evidence, or local-model pathway. Rationale: implementation quality is adequate, not reproducibility-grade. Caution: endpoint and dependency differences may change results.

#### 7.1.5 Interface and workflow usability

- Rating: `2`
- Review note: Basis: Skilled users can use the repository and hosted data. Gap: workflow documentation, troubleshooting, and dashboard governance are limited. Rationale: usability is adequate for technical reviewers. Caution: casual users may misrun or misread the benchmark.

#### 7.1.6 Accessibility across modalities, languages, and system types

- Rating: `2`
- Review note: Basis: A text-only subset exists and image-containing items are identified. Gap: English-only coverage, accessibility accommodations, and local/open-weight comparability are limited. Rationale: accessibility is adequate for frontier API-model research. Caution: full-set and text-only scores should not be mixed.

#### 7.1.7 Licensing, use requirements, and risk warnings

- Rating: `2`
- Review note: Basis: The repository has an MIT license and the dataset host uses non-training acknowledgements. Gap: downstream data-host terms and sensitive-content warnings are not fully analyzed. Rationale: use requirements are usable but incomplete. Caution: users should distinguish repository license from dataset access conditions.

#### 7.1.8 Overall quality of benchmark artifacts

- Rating: `2`
- Review note: Basis: Core artifacts are public and usable. Gap: implementation validation, raw outputs, and full replication packaging remain limited. Rationale: overall artifact quality supports cautious use. Caution: artifact availability is stronger than reproducibility assurance.

Review notes:

HLE's artifact quality is stronger than the earlier local-only pilot, but implementation validation remains the limiting factor.

---

## Section 8. Baselines, Comparators, and Reference Interpretation

EFPA Section 8 evaluates norms. MESA translates this into baselines, comparator cohorts, reference groups, score bands, floors and ceilings, and guidance about what score comparisons mean.

#### Figure 2: Structure of Section 8 on Baselines, Comparators, and Reference Interpretation

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- Rating: `1`
- Review note: Basis: Multiple-choice floors and saturation concerns are recognized. Gap: no comprehensive random baseline by item type, score distribution, or ceiling analysis. Rationale: floor and chance support is limited. Caution: near-zero scores and small differences need more context.

#### 8.1.2 Human or expert baselines

- Rating: `2`
- Review note: Basis: Experts authored and reviewed items, making expert performance relevant. Gap: no published expert norm group with benchmark-taking procedures and score distributions. Rationale: human baseline support is adequate for item targeting. Caution: expert-level should not be read as a calibrated percentile.

#### 8.1.3 Model comparator cohort

- Rating: `3`
- Review note: Basis: Official reports include named frontier model comparisons with versions and subsets. Gap: raw outputs, exact API conditions, and repeat-run uncertainty are missing. Rationale: comparator cohort is good for the publication context. Caution: rankings age quickly.

#### 8.1.4 Historical, version, or benchmark-family comparators

- Rating: `2`
- Review note: Basis: HLE is framed against prior saturated benchmarks and now has HLE-Rolling as a maintained variant. Gap: systematic historical linking and rolling-version equivalence are incomplete. Rationale: historical comparator support is adequate. Caution: comparisons across benchmark families remain qualitative.

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- Rating: `1`
- Review note: Basis: Accuracy and calibration are reported. Gap: no validated proficiency threshold, pass/fail category, or minimum meaningful difference. Rationale: score-band interpretation is weak. Caution: do not create deployment or procurement cutoffs from HLE scores alone.

#### 8.1.6 Representativeness of reference groups

- Rating: `2`
- Review note: Basis: Expert authorship and frontier-model cohorts provide some reference context. Gap: reference groups are not sampled or normed like psychometric populations. Rationale: representativeness is adequate only for cautious research use. Caution: reference groups should not be treated as normative populations.

#### 8.1.7 Currency and maintenance of baseline evidence

- Rating: `2`
- Review note: Basis: HLE-Rolling and public materials show ongoing maintenance. Gap: baseline refresh policy and comparator currency rules are incomplete. Rationale: maintenance evidence is adequate but not strong. Caution: cite leaderboard or rolling results with dates.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

#### 8.2 Overall adequacy of baselines and reference interpretation

- Rating: `2`
- Review note: Basis: Model comparators and expert-development context are meaningful. Gap: chance, human norming, thresholds, uncertainty, and baseline maintenance are limited. Rationale: baseline support is adequate for cautious comparison. Caution: scores are not norm-like measurements.

Review notes:

Section 8 is adequate for cautious research comparison but not for norm-like score interpretation.

---

## Section 9. Reliability, Precision, and Score Stability

EFPA Section 9 evaluates reliability and precision. MESA applies this to run-to-run stability, prompt and environment sensitivity, scorer or judge reliability, parser behavior, uncertainty reporting, and whether reported differences are meaningful.

#### Figure 3: Structure of Section 9 on Reliability, Precision, and Score Stability

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- Rating: `1`
- Review note: Basis: Some model settings and evaluation outputs are documented. Gap: systematic evidence for reliability, precision, scorer stability, and prompt sensitivity is sparse. Rationale: reliability coverage is weak. Caution: reliability should be revisited before high-stakes use.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- Rating: `1`
- Review note: Basis: Temperature and model-version conditions are partly reported. Gap: no systematic repeated-run variance, seed policy, provider drift assessment, or prompt sensitivity analysis. Rationale: run stability support remains weak. Caution: repeated evaluations may vary.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- Rating: `1`
- Review note: Basis: Aggregate score reporting exists. Gap: published comparisons lack comprehensive confidence intervals, standard errors, or statistical tests. Rationale: precision evidence is limited. Caution: point estimates should not be treated as precise ranks.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- Rating: `1`
- Review note: Basis: Automated judge and parser paths exist in the repository. Gap: parser error rates, answer-equivalence checks, and scorer agreement statistics are not fully documented. Rationale: automated scorer reliability is under-evidenced. Caution: scoring errors may differ by answer format.

#### 9.3.2 Human rater or expert scorer agreement

- Rating: `1`
- Review note: Basis: Human review supports item creation. Gap: human rater agreement and adjudication reliability statistics are not fully reported. Rationale: rater reliability is weakly documented. Caution: item quality review does not equal scoring reliability.

#### 9.3.3 Model-as-judge reliability and validity checks

- Rating: `1`
- Review note: Basis: The judge prompt is public. Gap: model-judge validation, human-vs-judge comparison, and calibration across domains are incomplete. Rationale: model-as-judge reliability is weak. Caution: judge errors can affect domain and format comparisons.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- Rating: `1`
- Review note: Basis: Standard prompts are documented. Gap: prompt, instruction, and formatting sensitivity are not systematically tested. Rationale: prompt stability support is weak. Caution: prompt deviations can change scores.

#### 9.4.2 Form, split, version, or refresh equivalence

- Rating: `1`
- Review note: Basis: Static public set and HLE-Rolling are documented. Gap: public/private and rolling-form equivalence are not fully demonstrated. Rationale: version stability evidence is limited. Caution: rolling updates trade freshness for comparability risk.

#### 9.4.3 Execution environment and dependency stability

- Rating: `1`
- Review note: Basis: Requirements and API-based scripts exist. Gap: environment, dependency, provider, and endpoint stability are not comprehensively controlled. Rationale: execution stability support is weak. Caution: exact reproduction requires more run metadata.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- Rating: `1`
- Review note: Basis: Scores are reported for multiple models. Gap: uncertainty, significance testing, and minimum meaningful difference guidance are missing. Rationale: statistical comparison quality is limited. Caution: small model differences should not drive conclusions.

### 9.6 Overall Reliability, Precision, and Score Stability

#### 9.6 Overall reliability, precision, and score stability

- Rating: `1`
- Review note: Basis: Some procedural and scoring information exists. Gap: repeat-run uncertainty, scorer validation, version equivalence, and statistical precision are weak. Rationale: reliability and precision remain HLE's largest measurement-quality constraint. Caution: rankings should be interpreted coarsely.

Review notes:

Reliability and precision remain HLE's largest measurement-quality constraint.

---

## Section 10. Validity Evidence

EFPA Section 10 evaluates validity. MESA focuses on the phenomenon-task-metric-claim chain: whether the benchmark content, internal structure, scoring, relations with other evidence, contamination controls, and public claims support the intended interpretation.

#### Figure 4: Structure of Section 10 on Validity Evidence

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- Rating: `3`
- Review note: Basis: Broad subject coverage, expert contribution, review, auditing, and non-searchability checks support content quality. Gap: no complete sampling frame or representativeness analysis. Rationale: content support is strong for closed-ended academic stress testing. Caution: academic breadth is not full cognitive breadth.

#### 10.1.2 Construct breadth and sub-ability coverage

- Rating: `2`
- Review note: Basis: HLE covers many academic domains and some image-conditioned items. Gap: no CHC-style breadth/depth model or sub-ability validation. Rationale: construct breadth is adequate for academic coverage but not broad intelligence. Caution: domain labels should not be treated as validated ability factors.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- Rating: `1`
- Review note: Basis: Domain and text-only/full-set subscores are reported. Gap: no dimensionality analysis or validated subscale structure. Rationale: internal-structure support is weak. Caution: category scores are descriptive.

#### 10.2.2 Item or task behavior across the score scale

- Rating: `1`
- Review note: Basis: Aggregate and category performance are available. Gap: item behavior across difficulty, discrimination, redundancy, and score scale is not comprehensively reported. Rationale: item-behavior evidence is limited. Caution: ceiling, floor, and domain behavior remain uncertain.

#### 10.2.3 Failure modes and error analysis

- Rating: `1`
- Review note: Basis: Official materials report aggregate/category behavior and discuss some item-audit concerns. Gap: no systematic error analysis separates intended academic difficulty from formatting, parser, judge, memorization, refusal, or domain artifacts. Rationale: failure-mode evidence is weak. Caution: observed model failures should not automatically be attributed to the intended capability.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- Rating: `2`
- Review note: Basis: Accuracy fits closed-ended answerable items and calibration adds useful confidence information. Gap: judge validation, parser validation, malformed-answer handling, and aggregation sensitivity are incomplete. Rationale: metric validity is adequate for cautious use. Caution: scoring may conflate ability with formatting or judge behavior.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- Rating: `2`
- Review note: Basis: Non-searchability checks and answer formats reduce some shortcuts. Gap: formatting effects, memorization, public exposure, and judge-specific artifacts are not fully tested. Rationale: shortcut sensitivity is partially addressed. Caution: public-set use should account for contamination and tuning risk.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- Rating: `2`
- Review note: Basis: HLE is compared with prior benchmarks, expert difficulty expectations, and frontier model cohorts. Gap: direct human benchmark-taking distributions and real-world research criteria are limited. Rationale: relational evidence supports difficulty more than external validity. Caution: HLE is not a proxy for autonomous scientific productivity.

#### 10.4.2 Convergent and discriminant evidence

- Rating: `2`
- Review note: Basis: Comparisons with other benchmarks and model cohorts provide some convergent context. Gap: discriminant validation and systematic relations with external constructs are limited. Rationale: adequate but incomplete relational evidence. Caution: similarity to other hard benchmarks does not establish broad construct validity.

#### 10.4.3 Ecological or predictive relevance

- Rating: `1`
- Review note: Basis: The benchmark is academically meaningful. Gap: predictive links to real research, long-horizon reasoning, or open-ended scientific work are not established. Rationale: ecological and predictive relevance is weakly evidenced. Caution: do not infer real-world scientific agency from HLE alone.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- Rating: `3`
- Review note: Basis: Public/private split, non-searchability requirements, search-enabled audit, canary, and non-training warning are meaningful controls. Gap: private-set details and ongoing leak metrics are incomplete. Rationale: contamination control is good. Caution: the public set becomes more exposed over time.

#### 10.5.2 Gameability and benchmark-specific tuning controls

- Rating: `3`
- Review note: Basis: Non-training warnings, private materials, feedback routes, and HLE-Rolling help reduce gaming. Gap: formal release-rule governance and tuning-monitoring evidence are incomplete. Rationale: gameability controls are good but not exhaustive. Caution: public leaderboard use should preserve release rules.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- Rating: `3`
- Review note: Basis: Official materials link scores to closed-ended academic capability and caution against broader interpretations. Gap: third-party public communication may strip caveats. Rationale: stated claims are mostly proportional. Caution: title-level public salience can invite overclaiming.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- Rating: `3`
- Review note: Basis: Official materials explicitly caution against AGI or autonomous research interpretation from HLE score alone. Gap: no broad CHC/AGI validity argument is supplied. Rationale: broad-claim handling is good because limits are explicit. Caution: HLE should be one evidence source, not an AGI measure.

### 10.7 Overall Validity Support

#### 10.7 Overall validity support

- Rating: `2`
- Review note: Basis: HLE has strong content support and claim-bounded official framing. Gap: internal structure, failure-mode analysis, scorer validation, reliability, and ecological evidence are incomplete. Rationale: overall validity support is adequate for cautious academic benchmarking. Caution: validity support is not strong enough for high-stakes ranking or broad cognitive claims.

Review notes:

HLE's validity case is content-heavy and claim-bounded. Its strongest support does not remove the need for scoring and reliability validation.

---

## Section 11. Fair Use, Comparability, and Appropriate Use

EFPA Section 11 evaluates fairness and acceptability. MESA applies this to cross-system comparability, access conditions, language, domain and modality coverage, evaluation-condition fairness, and guidance about appropriate use and non-use.

#### Figure 5: Relevant Ratings for Fair Use, Comparability, and Appropriate Use from Other Sections

This applied pilot preserves the v6 section structure; the full template figure is not repeated here.

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- Rating: `2`
- Review note: Basis: The construct is relevant to frontier academic question answering and multimodal academic tasks. Gap: relevance across local models, languages, modalities, and non-academic contexts is limited. Rationale: construct relevance is adequate for intended research use. Caution: broader users need separate justification.

#### 11.1.2 Documentation of fair-use considerations

- Rating: `2`
- Review note: Basis: Modality distinctions, non-use caveats, and source limits are documented. Gap: fairness, accessibility, and cross-system comparability guidance is incomplete. Rationale: fair-use documentation is adequate. Caution: public communication should repeat limitations.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- Rating: `2`
- Review note: Basis: Text-only and full-set distinctions improve accessibility across system capabilities. Gap: English dominance, image accessibility, and accommodation analysis are limited. Rationale: inclusive design support is adequate but incomplete. Caution: full-set scores favor systems with image support.

#### 11.2.2 Domain, language, modality, and subgroup coverage

- Rating: `2`
- Review note: Basis: The benchmark documents broad academic domains and image-containing items. Gap: language, cultural, domain-level reliability, and subgroup coverage analyses are limited. Rationale: coverage is broad but fairness support is basic. Caution: breadth does not guarantee equal measurement quality across domains.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- Rating: `2`
- Review note: Basis: Standard prompts, model-version reporting, and text-only/full-set distinctions support cautious comparison. Gap: provider drift, seed policy, run variance, and local/API equivalence are incomplete. Rationale: cross-system comparability is adequate for paper-level comparison. Caution: compare matched modalities and conditions.

#### 11.3.2 Access, compute, tooling, and API or local comparability

- Rating: `1`
- Review note: Basis: Public repository and hosted data support access for skilled users. Gap: API costs, local-model pathways, compute budgets, and service conditions are under-specified. Rationale: access comparability is weak. Caution: unequal model access can distort comparisons.

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- Rating: `2`
- Review note: Basis: HLE-Rolling and the rolling change file provide some temporal maintenance evidence. Gap: cohort identifiers, stale-score handling, item-retirement rules, score linking, and direct-comparison limits across rolling windows are only partly documented. Rationale: temporal comparability is adequate for cautious date-stamped interpretation. Caution: do not directly compare rolling scores without version/date context.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- Rating: `1`
- Review note: Basis: Domain and modality reporting give limited context. Gap: differential performance or bias analyses across domains, languages, or system groups are not fully documented. Rationale: bias evidence is weak. Caution: fairness claims should be avoided.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- Rating: `1`
- Review note: Basis: Some category scores are reported. Gap: reliability and validity across subgroups, domains, or modalities are not established. Rationale: subgroup stability evidence is weak. Caution: domain-level differences may reflect measurement artifacts.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- Rating: `2`
- Review note: Basis: Official materials include non-training warnings and AGI interpretation caveats. Gap: formal non-use cases for procurement, deployment, or policy decisions are incomplete. Rationale: appropriate-use guidance is adequate. Caution: high-stakes uses require additional validation.

#### 11.5.2 Release rules and sensitive-content handling

- Rating: `2`
- Review note: Basis: Public/private materials, non-training terms, canary, feedback routes, and HLE-Rolling exist. Gap: formal release governance and sensitive-content analysis are incomplete. Rationale: release and use restrictions are adequate but not comprehensive. Caution: data access conditions should be followed precisely.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

#### 11.6 Overall fair use, comparability, and appropriate use

- Rating: `2`
- Review note: Basis: HLE supports cautious frontier API-model research comparisons. Gap: cross-system, language, accessibility, subgroup, and access-equity evidence is incomplete. Rationale: fair use and comparability are adequate. Caution: not suitable for broad procurement, deployment, or policy decisions without additional analysis.

Review notes:

HLE is reasonably fair for frontier API-model research comparisons but not for broad procurement, deployment, or policy decisions without additional analysis.

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

EFPA Section 12 evaluates digitally generated reports. MESA applies that logic to AI benchmark outputs: paper tables, scorecards, leaderboards, dashboards, downloadable result files, raw traces, public claims, and score interpretations.

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or result artifact scope

- Rating: `2`
- Review note: Basis: Nature article, arXiv paper, website, repository sample outputs, and HLE-Rolling dashboard provide multiple report surfaces. Gap: no complete formal leaderboard specification or raw-output archive. Rationale: reporting scope is adequate. Caution: hosted rolling reports should be date-stamped.

#### 12.1.2 Score granularity and level of detail

- Rating: `2`
- Review note: Basis: Aggregate, category, text-only/full-set, token, and calibration outputs are reported. Gap: per-item data, uncertainty, and meaningful-difference support are limited. Rationale: score detail is useful but not precision-aware. Caution: do not infer more granularity than scores support.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- Rating: `2`
- Review note: Basis: Some model versions, subsets, and evaluation conditions are reported. Gap: uncertainty, exact version labeling, prompts/settings, and run dates are incomplete for all outputs. Rationale: trace labeling is adequate but incomplete. Caution: rankings may be fragile.

#### 12.2.2 Reproducibility and traceability of reported scores

- Rating: `1`
- Review note: Basis: Papers and code link some scores to public methods. Gap: raw outputs, judge logs, exact run configs, and sufficient audit summaries are not public. Rationale: traceability is limited. Caution: independent replication of reported scores is constrained.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- Rating: `3`
- Review note: Basis: Official reports link scores to closed-ended academic capability and caution against AGI/autonomous research overclaims. Gap: third-party reporting guidance is limited. Rationale: score-to-claim linkage is good when official caveats are preserved. Caution: public use may exaggerate the claim.

#### 12.3.2 Raw outputs, per-item data, or trace availability

- Rating: `0`
- Review note: Basis: Public raw model outputs, judge logs, per-item outcomes for reported runs, and traces are not documented as available. Gap: complete raw outputs and logs. Rationale: this artifact class cannot be rated as present. Caution: independent error analysis is limited.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- Rating: `2`
- Review note: Basis: Official reports include modality distinctions and interpretive caveats. Gap: report-level bias and coverage-limit analysis is incomplete. Rationale: report fairness is adequate. Caution: category differences should be interpreted cautiously.

#### 12.4.2 Acceptability and usability for intended audiences

- Rating: `2`
- Review note: Basis: Reports are usable for technical readers and public audiences. Gap: uncertainty and non-use guidance are not always prominent. Rationale: acceptability and usability are adequate. Caution: non-expert readers may overread rankings.

#### 12.4.3 Public communication and leaderboard governance

- Rating: `2`
- Review note: Basis: HLE-Rolling and official pages provide public reporting and caveats. Gap: leaderboard governance, update rules, eligibility, and third-party communication policy are incomplete. Rationale: public communication is adequate but not comprehensive. Caution: public claims should preserve official caveats.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

#### 12.5 Overall quality of reports, leaderboards, dashboards, and public claims

- Rating: `2`
- Review note: Basis: HLE reports results responsibly in papers and public artifacts. Gap: uncertainty, raw traces, full governance, and reproducibility-grade reporting are limited. Rationale: overall reporting quality is adequate. Caution: reporting infrastructure is weaker than the paper-level presentation.

Review notes:

HLE reports results responsibly, but reporting infrastructure remains weaker than the paper-level presentation.

---

## Final Evaluation

### Evaluative Report of the Benchmark

HLE is a strong content-driven benchmark for the narrow construct of expert-level closed-ended academic question answering by frontier AI systems. Its strongest support comes from expert item development, broad academic coverage, public release of the final 2,500-question set, clear answer-confidence evaluation, official paper and repository documentation, and explicit caution against AGI or autonomous research interpretation. The Nature publication and HLE-Rolling materials make the benchmark more mature than the earlier local pilot suggested.

The main constraints are reliability, precision, scorer validation, and reproducibility-grade reporting. The official materials still do not provide a complete uncertainty framework for published model comparisons, repeated-run variance, judge validation, raw outputs, full private-set details, or exact replication conditions. These are gaps, not proof of poor benchmark quality, but they materially limit fine-grained rankings, high-stakes use, and broad public claims.

Known ongoing development is represented by HLE-Rolling and the public rolling change file. Those materials support maintenance and freshness, but they also make versioned comparability, stale-score handling, and retired-item governance important future review priorities.

### Conclusions

HLE can support cautious research claims about performance on difficult, closed-ended, mostly academic questions under HLE conditions. It should not be used alone as a measure of AGI, autonomous research capability, open-ended scientific creativity, long-horizon planning, or general cognitive breadth. Users should treat HLE as a high-quality academic stress test with meaningful contamination controls and strong caveats, not as a complete measurement theory of intelligence. Responsible use requires technical benchmark literacy, familiarity with model evaluation and scoring pipelines, and enough measurement-validity expertise to distinguish HLE's supported closed-ended academic interpretation from broader unsupported claims.

### Recommendations

Use HLE for source-bound frontier model comparison and academic stress testing. Report model versions, prompts, API/provider conditions, data snapshot, judge configuration, and date. Preserve the official caveats. Maintainers or future reviewers should prioritize judge validation, repeat-run uncertainty, raw-output release or audit access, versioned HLE-Rolling comparability policy, and more explicit score interpretation guidance.

### Summary of Ratings

| Section                                                    | Rating (`n/a`, `0`-`4`) |
| :--------------------------------------------------------- | :---------------------: |
| Section 6. Rationale, documentation, and task/item quality |           `3`           |
| Section 7. Benchmark artifacts and usability               |           `2`           |
| Section 8. Baselines and comparators                       |           `2`           |
| Section 9. Reliability and precision                       |           `1`           |
| Section 10. Validity support                               |           `2`           |
| Section 11. Fair use and comparability                     |           `2`           |
| Section 12. Reports, leaderboards, and public claims       |           `2`           |

Review notes: The overall rating is not a mechanical average. Strong rationale and content support are constrained by weaker reliability, scorer-validation, and reporting support.

### Gap Register

| Gap                                                               | Affected rating(s)         | Why it matters                                                                         | Needed for a higher rating                                                                                     |
| :---------------------------------------------------------------- | :------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| No comprehensive repeat-run uncertainty for published comparisons | 8, 9, 12, overall          | Limits fine-grained rankings and statistical interpretation.                           | Repeated runs, seed/temperature details, confidence intervals, and comparison tests.                           |
| Model-judge and parser validation are incomplete                  | 7, 9, 10, scoring validity | Scoring errors can affect domain and format comparisons.                               | Human-judge comparison sample, parser error audit, adjudication rules, and agreement statistics.               |
| Public/private and rolling comparability are partially documented | 5, 10, 11, 12, maintenance | Hidden and rolling forms support integrity but complicate longitudinal interpretation. | Version policy, linking study, update rules, cohort labels, stale-score handling, and archive/retirement plan. |
| Raw outputs and per-item results for reported runs are not public | 7, 9, 12, reproducibility  | Limits independent error analysis and replication.                                     | Raw response archive or controlled audit access with model, prompt, and judge metadata.                        |
| Broad intelligence mapping is absent                              | 2.18, 10, final            | Prevents broad cognitive interpretation.                                               | CHC/AGI-style breadth/depth analysis or continued explicit narrow caveats.                                     |

Other gaps/comments: The gaps are mostly about precision and interpretation, not about the existence of usable public benchmark artifacts.

### Reviewer Caution Statement

The narrowest defensible interpretation is: HLE measures model performance on difficult closed-ended academic questions, including some image-conditioned items, under official HLE prompting and scoring conditions. It is not a standalone measure of AGI, autonomous research ability, broad agency, or open-ended scientific creativity. Ratings should be revisited when HLE-Rolling governance, scorer validation, repeat-run uncertainty, raw-output access, and private-set comparability are better documented.
