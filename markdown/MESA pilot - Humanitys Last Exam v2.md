# MESA Pilot Review: Humanity's Last Exam v2

This pilot applies `markdown/MESA EFPA template v5.md` to Humanity's Last Exam (HLE). It uses current official HLE materials available on 2026-05-09 and keeps the Part A / Part B boundary explicit. Part A describes what the official materials state. Part B assigns ratings using Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

Before completing the review, inspect the most authoritative available materials. Prefer official benchmark papers, websites, repositories, data hosts, leaderboards, harnesses, changelogs, and maintainer statements. Independent commentary should be used only for context, external critique, or disputed claims, and should not replace official benchmark facts.

Documentation status summary for Part A:

- [x] Documented: benchmark name, public 2,500-question set, expert-contributor model, response formats, prompt template, model-judge scoring path, calibration output, public repository, MIT license, Hugging Face dataset entry, canary string, public website, Nature publication, arXiv record, and HLE-Rolling change log.
- [x] Partially documented: private held-out set details, exact replication conditions for published model results, score uncertainty for published comparisons, HLE-Rolling comparability policy, formal leaderboard governance, and end-to-end scorer validation.
- [x] Not documented: random seeds for published runs, raw model outputs for reported results, full judge validation statistics, complete public/private set comparability statistics, and formal statistical significance testing for model differences.

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
| Date of previous review, if applicable | 2026-05-04 for the earlier local HLE pilot |
| Review scope | Full Part A/B pilot refresh using current official online HLE materials. |
| Review boundary | Official HLE materials first; independent commentary excluded except local MESA literature used for Part B criteria. |

Review notes: This v2 pilot does not overwrite the prior HLE pilot. It updates artifact status and wording for the current official publication and web materials.

### 1.2 Information Sources Reviewed

| Material type | Artifact reviewed | Access date | Role in review |
| :--- | :--- | :--- | :--- |
| Official paper or technical report | [Nature article: *Humanity's Last Exam*](https://www.nature.com/articles/s41586-025-09962-4) | 2026-05-09 | Primary official publication for benchmark purpose, construction, results, and interpretation limits. |
| Official paper or technical report | [arXiv:2501.14249](https://arxiv.org/abs/2501.14249) | 2026-05-09 | Preprint record and versioned paper access. |
| Benchmark website or documentation hub | [lastexam.ai](https://lastexam.ai/) | 2026-05-09 | Official website, publication links, dataset links, HLE-Rolling, and live submission entry point. |
| Repository | [centerforaisafety/hle](https://github.com/centerforaisafety/hle) | 2026-05-09 | Official repository for README, evaluation scripts, license, canary, requirements, citation, and rolling change file. |
| Dataset card, data host, or task host | [cais/hle on Hugging Face](https://huggingface.co/datasets/cais/hle) | 2026-05-09 | Public task-set distribution and access conditions. |
| Repository | [cais/hle organization page](https://github.com/cais/hle) | 2026-05-09 | Checked as an official alias/redirect context for the public HLE repository. |
| Release log, changelog, or maintenance record | [hle-rolling-changes.txt](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt) | 2026-05-09 | Official record of HLE-Rolling additions and fixes. |
| Contextual literature | `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`; `markdown/Papers/betterbench.md`; `markdown/Papers/Measuring_what_Matters.md`; `markdown/Papers/A_Definition_of_AGI.md` | 2026-05-09 | Used only for MESA Part B rating criteria and broad-claim caution. |

Other materials/comments: The official website links the Nature article, arXiv paper, Hugging Face task set, GitHub repository, feedback form, and HLE-Rolling submission dashboard. This review does not rely on third-party commentary.

### 1.3 Benchmark Information

| Prompt | Response |
| :--- | :--- |
| Benchmark name | Humanity's Last Exam |
| Short name or acronym | HLE |
| Benchmark version, edition, or release | Public 2,500-question HLE set plus HLE-Rolling as a maintained rolling variant. The repository does not expose a conventional semantic version release tag in the reviewed snapshot. |
| Original benchmark name, if this is an adaptation | Not applicable. |
| Benchmark creators or authors | Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, Michael Choi, Anish Agrawal, Arnav Chopra, Adam Khoja, Ryan Kim, Richard Ren, Jason Hausenloy, Oliver Zhang, Mantas Mazeika, Summer Yue, Alexandr Wang, Dan Hendrycks, and a large contributor group listed in the official paper. |
| Current maintainers | Center for AI Safety and Scale AI are the organizing entities named in official materials; repository maintenance occurs under `centerforaisafety/hle`. |
| Host organization, publisher, or distributor | Nature publishes the article; Center for AI Safety hosts the GitHub repository; Hugging Face hosts the public task set; lastexam.ai hosts official web links. |
| Date of original release | Public materials date the paper/preprint to 2025 and the Nature article to 2026. The website states the final 2,500-question public set was available as of 2025-04-03. |
| Date of current release or revision | HLE-Rolling was announced on the official website as launched on 2025-10-08; the reviewed repository main branch is the current public artifact snapshot. |
| License or access terms | MIT license in the GitHub repository. Hugging Face access requires user acknowledgement of benchmark-data terms including not using the set for training or fine-tuning. |
| Persistent identifier, citation, or DOI | Nature article DOI link via `https://doi.org/10.1038/s41586-025-09962-4`; arXiv identifier `2501.14249`; repository citation file. |

Review notes: The official HLE ecosystem is now clearer than the earlier local pilot because Nature, arXiv, GitHub, Hugging Face, and lastexam.ai are all public anchors.

### 1.4 Public Artifacts

| Artifact | URL or location | Access status | Review detail |
| :--- | :--- | :--- | :--- |
| Paper or technical report | [Nature article](https://www.nature.com/articles/s41586-025-09962-4); [arXiv:2501.14249](https://arxiv.org/abs/2501.14249) | Public article page and arXiv record; Nature full text may depend on access route | Official publication and preprint establish the benchmark rationale and reported results. |
| Benchmark website | [lastexam.ai](https://lastexam.ai/) | Public | Provides links to final public set, HLE-Rolling, Nature, arXiv, GitHub, and Hugging Face. |
| Code repository | [centerforaisafety/hle](https://github.com/centerforaisafety/hle) | Public | Includes README, `hle_eval`, `requirements.txt`, MIT license, canary, citation, and rolling change file. |
| Evaluation harness | `hle_eval` in the GitHub repository | Public simple harness | README documents model prediction and judge result scripts using OpenAI-compatible API access. |
| Dataset or task set | [cais/hle](https://huggingface.co/datasets/cais/hle) | Public with access acknowledgement | Hugging Face hosts the final 2,500 public questions with images where applicable. |
| Prompt set | README and paper appendix | Public | Response prompt asks for answer and confidence; judge prompt is documented. |
| Rubric or scoring guide | Paper methods/appendix; repository judge script | Public, partially implementation-specific | Human review rubrics and model-judge criteria are described. |
| Leaderboard or result display | Nature result tables; lastexam.ai HLE-Rolling live submission dashboard | Public/hosted, partly live | Paper-level results are public. HLE-Rolling has a submission dashboard, but formal score governance is only partly documented. |
| Release log or changelog | [hle-rolling-changes.txt](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt) | Public | Records rolling updates and fixes; score comparability policy is limited. |
| Contact, issue channel, or feedback route | GitHub issues; lastexam.ai feedback link | Public | Repository and website provide feedback mechanisms. |

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

| Component | Description |
| :--- | :--- |
| Claimed construct or phenomenon | Expert-level closed-ended academic performance by frontier AI systems. |
| Construct subcomponents | Advanced knowledge, domain-specific reasoning, mathematical/scientific problem solving, image-conditioned academic questions, answer confidence, and calibration. |
| Task families or subdomains | The official paper describes 2,500 questions across over 100 subject areas, including mathematics, science, engineering, humanities, social science, law, medicine/biology, computer science/AI, and other specialized domains. |
| Task sampling or selection logic | Questions were expert-contributed, reviewed, revised, audited, and selected for difficulty and non-searchability under official rubrics. |
| Splits or partitions | Public 2,500-question set; private held-out set; text-only subset; HLE-Rolling maintained variant. |
| Primary score | Accuracy / percent correct over evaluated items. |
| Subscores | Category/domain accuracy and text-only versus full-set reporting in official results. |
| Derived or aggregate scores | Calibration-related reporting, including model confidence and RMS calibration error in the paper; simple evaluator outputs include aggregate accuracy and related summary statistics. |
| Qualitative labels or bands | Human-review labels during item development, such as keep/revise/discard-style judgments; not model score bands. |
| Claim boundaries or caveats | Official discussion cautions against interpreting HLE accuracy alone as AGI, autonomous research ability, or open-ended creative scientific capability. |

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

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing | Status detail |
| :--- | :---: | :---: | :---: | :--- |
| Language support | - [ ] | - [x] | - [ ] | English academic questions are the public-set norm. |
| Context length | - [ ] | - [ ] | - [x] | Item prompts are finite, but no general context-length threshold is specified. |
| Multimodal input support | - [ ] | - [x] | - [ ] | Needed for the full benchmark because a minority of items include images. |
| Structured output support | - [ ] | - [x] | - [ ] | Expected for answer/confidence extraction. |
| Tool access | - [x] | - [ ] | - [ ] | Standard HLE answering does not use tools. |
| Browser or internet access | - [x] | - [ ] | - [ ] | Standard evaluation is intended to avoid web lookup. |
| Code execution | - [x] | - [ ] | - [ ] | Not part of standard evaluated system behavior. |
| Memory or persistent state | - [x] | - [ ] | - [ ] | No persistent-state requirement is described. |
| API compatibility | - [ ] | - [x] | - [ ] | Repository examples use OpenAI-compatible API calls. |
| Latency or time budget | - [ ] | - [ ] | - [x] | No model response time budget is specified. |
| Cost or compute budget | - [ ] | - [ ] | - [x] | Token counts are reported, but full cost/compute budgets are not specified. |

Other requirements/comments: Full-set participation requires image input support; text-only comparisons should not be treated as equivalent to full-set comparisons.

Review notes: The benchmark is designed around API-evaluable language/multimodal systems, but the official materials do not fully document local-inference equivalence.

### 2.8 Evaluation Conditions

| Condition | Description |
| :--- | :--- |
| Prompting protocol | Official prompt asks for a final answer and confidence; paper reports standardized prompting and model evaluation conditions. |
| System prompt | Documented in official materials for the evaluation protocol; adapted when systems do not support system prompts. |
| Few-shot examples | Not documented as part of the standard HLE protocol. |
| Sampling settings | Paper reports model-specific temperature settings; most deterministic-capable models are evaluated at low/zero temperature. |
| Tool permissions | No tool use for model answering; search tools used by maintainers for searchability auditing. |
| Time limits | Not documented. |
| Human intervention rules | Humans contribute, review, and audit items; no human intervention is described during model answering. |
| Hardware or hosted service | Official results use named hosted frontier models; repository examples use API calls. |
| Network requirements | Required for Hugging Face download and API-hosted model calls in repository examples. |
| Sandbox or security constraints | Not documented. |
| Special administration conditions | Private held-out set and HLE-Rolling support integrity and maintenance beyond the public static set. |

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

| Prompt | Response |
| :--- | :--- |
| Total public items or tasks | 2,500 final public questions. |
| Total private or hidden items | Private held-out set documented, but exact count and access process are not fully public. |
| Development or example items | Example questions are shown in the paper and website; full development-item count is not separately specified. |
| Test items | Public 2,500-question set plus private/rolling components. |
| Dynamic or generated tasks | HLE-Rolling is a maintained rolling variant, not procedurally generated tasks in the standard public set. |
| Episodes, trials, or measurement points | One score opportunity per question in standard scoring; repeat-run protocol for reliability is not fully specified. |
| Item count uncertainty | Public count is clear; private and rolling counts are partially documented. |

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

| Technology | A | R | Status detail |
| :--- | :---: | :---: | :--- |
| API access | - [x] | - [x] | Repository examples use model API calls. |
| Local inference | - [ ] | - [ ] | Not a primary documented path. |
| GPU | - [ ] | - [ ] | Not required for API evaluation; local requirements not specified. |
| CPU-only execution | - [ ] | - [ ] | Scoring scripts may run locally, but full local model evaluation is not documented. |
| Docker or container | - [ ] | - [ ] | Not documented. |
| Python package or CLI | - [x] | - [ ] | Python scripts and requirements are provided. |
| Browser | - [x] | - [ ] | Browser needed for web dashboard, not model answering. |
| External tools | - [ ] | - [ ] | Not used in standard model answers. |
| Internet access | - [x] | - [x] | Needed for API and hosted data/download paths. |
| Proprietary platform | - [x] | - [ ] | Published comparisons use proprietary frontier models; benchmark itself is not only proprietary. |

Other technologies/comments: Hugging Face access and API credentials are practical requirements for common use.

### 2.14 Time and Resource Requirements

| Activity | Time, compute, or cost estimate |
| :--- | :--- |
| Setup | Repository setup is documented through Python requirements, but full setup time is not estimated. |
| Model inference or task completion | Token counts are reported in the paper; wall-clock or API-cost estimates are not fully specified. |
| Scoring | Repository judge script exists; time/cost estimate not specified. |
| Human adjudication | Item development involved expert review, but user-side adjudication is not part of standard scoring. |
| Analysis or reporting | Not documented. |
| Full benchmark run | Not documented as a time/cost budget. |
| API or compute cost | Not documented as a budget; depends on model provider and item subset. |

Other requirements/comments: Cost and runtime can be material for 2,500 expert questions, especially if explanations and judge calls are used.

### 2.15 Benchmark Forms, Versions, and Variants

| Form or variant | Purpose | Equivalence claim | Status |
| :--- | :--- | :--- | :--- |
| Public HLE 2,500-question set | Main public static evaluation set. | Baseline public form for current review. | Public with Hugging Face acknowledgement. |
| Private held-out set | Assess overfitting and gaming beyond the public set. | Intended integrity check; equivalence details are limited. | Hidden/private. |
| Text-only subset | Permit comparison of non-multimodal systems. | Not equivalent to full set because image items are excluded. | Public subset derivable from item metadata. |
| HLE-Rolling | Maintain freshness through rolling submissions/updates. | Score comparability with static set is partially documented. | Hosted/maintained variant. |

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

### 2.18 Broad Claim and CHC/AGI Cautions

| Prompt | Response |
| :--- | :--- |
| Broad claim term used | "Humanity's Last Exam"; expert-level academic capability; frontier of model performance. |
| Claimed breadth across domains | Broad academic breadth across over 100 subject areas. |
| Claimed depth or proficiency level | Expert-level and difficult enough to challenge frontier models. |
| Sub-abilities explicitly covered | Closed-ended academic knowledge, domain-specific reasoning, mathematical/scientific problem solving, visual interpretation for image items, confidence reporting. |
| Sub-abilities explicitly excluded or not tested | Open-ended research, autonomous tool use, long-horizon planning, interactive agency, sustained memory, real-world experimentation, social collaboration, embodied action. |
| Coverage across modalities, tools, memory, planning, or speed | Text and image input are covered; tools, memory, planning, speed, and agency are not core evaluated dimensions. |
| Stated AGI, autonomy, or agency caveats | Official discussion cautions that high HLE accuracy alone would not establish AGI or autonomous research ability. |
| Relation to CHC-like broad/narrow abilities, if claimed | No explicit CHC mapping is claimed. Reviewer mapping would treat HLE as broad academic-content sampling, not a full CHC ability battery. |
| Descriptive caution for Part B | Evaluate HLE as a difficult closed-ended academic benchmark, not as a standalone AGI or agency measure. |

Review notes: AGI/CHC caution is required because broad academic coverage can be misread as broad cognitive coverage.

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
- [ ] Pairwise preference scoring
- [x] Hybrid automated and human scoring
- [x] Leaderboard service scoring
- [ ] Manual adjudication

Other scoring methods/comments: Hybrid here means human review is used for item development and automated/model-judge methods are used for routine scoring; it does not mean every model answer receives human adjudication.

Review notes: Pipeline details appear below in Section 3.2.

### 3.2 Scores and Metrics

Describe the scoring pipeline, including how model responses, logs, judge decisions, reference answers, unit tests, or platform outputs become global and partial scores.

| Score or metric | Definition | Aggregation | Interpretation stated by authors |
| :--- | :--- | :--- | :--- |
| Primary score | Accuracy / percent correct. | Correct items divided by evaluated items, reported overall and in selected subsets. | Higher score indicates better performance on difficult closed-ended academic questions under HLE conditions. |
| Subscore | Domain/category accuracy; text-only subset accuracy. | Items grouped by official category or subset. | Helps compare strengths across broad academic areas and modality constraints. |
| Derived score | RMS calibration error and confidence summaries. | Model-reported confidence compared against correctness. | Indicates calibration of confidence against answer accuracy. |
| Qualitative band | No official proficiency bands documented for model scores. | Not applicable. | Avoid treating arbitrary percentages as validated proficiency thresholds. |

Treatment of invalid, missing, malformed, or refused responses: Repository scripts and judge scoring handle answer extraction, but full malformed/refusal policy and parser validation are not comprehensively documented.

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

| Comparator or baseline | Construction method | Intended interpretation |
| :--- | :--- | :--- |
| Random or chance baseline | Non-zero floor for multiple-choice questions; not a full formal random baseline across all item types. | Prevents interpreting all near-zero scores as equally below chance. |
| Human baseline | Not fully documented as a benchmark-taking sample. | Not available for norm-like interpretation. |
| Expert baseline | Domain experts created and reviewed questions; paper frames items as expert-level. | Supports item difficulty and target level, not a full human norm. |
| Model cohort | Named frontier model results in official paper and current HLE materials. | Supports contemporaneous model comparison. |
| Prior benchmark or version | HLE motivated by saturation of prior academic benchmarks; HLE-Rolling updates are documented. | Provides context for difficulty and maintenance. |
| Criterion threshold or floor/ceiling | No validated proficiency threshold; saturation/rolling concerns documented. | Avoid arbitrary pass/fail interpretation. |

Review notes: HLE has meaningful model comparators and expert item-development context, but not full human norming or uncertainty-aware thresholds.

### 3.6 Score Uncertainty and Stability

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [ ] Sensitivity analyses
- [x] Not reported

Other uncertainty/stability comments: Some repository sample outputs include aggregate uncertainty-style fields, but the official model comparisons do not provide a complete uncertainty and repeat-run framework.

Review notes: This is a major limitation for interpreting small differences between model scores.

### 3.7 Metric-to-Claim Linkage

| Prompt | Response |
| :--- | :--- |
| Why the primary metric was chosen | Accuracy fits closed-ended answerability, where a final answer can be judged correct or incorrect. |
| Whether metric floors or ceilings are documented | Multiple-choice floor and benchmark saturation concerns are discussed, but floors/ceilings are not fully quantified across item types. |
| Whether the metric may reward non-target behavior named by the benchmark | The official materials discuss non-searchability and benchmark gaming/contamination risk; model-judge and formatting issues remain possible non-target contributors. |
| Whether parsing, judge, or scorer validation is documented | Judge prompt and scoring scripts are public; comprehensive scorer validation is not documented. |
| Whether score uncertainty affects claim interpretation | Yes, because published scores are point estimates without full repeat-run uncertainty. |
| Whether score differences are interpreted statistically | Formal significance testing is not documented in the reviewed official materials. |
| Whether benchmark reports state what users should not infer | Yes. Official discussion cautions against AGI/autonomous research inference from HLE score alone. |

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

| Output | Description | Public/private |
| :--- | :--- | :--- |
| Nature/paper result tables and figures | Overall, category, text-only/full-set, token, and calibration-related results. | Public article/preprint context. |
| Repository evaluator output | Local/API evaluator summary output. | Public tool output, generated by user. |
| HLE-Rolling live submission dashboard | Hosted rolling submission/results context linked from lastexam.ai. | Public/hosted, governance partly documented. |

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

## Section 5. Supply Arrangements and Materials

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

| Requirement type | Requirement |
| :--- | :--- |
| Technical skill | Ability to run Python scripts, manage API credentials, and handle Hugging Face datasets. |
| Model access | API access or compatible model endpoint for evaluated systems. |
| Dataset access | Hugging Face access acknowledgement for public task set. |
| Compute or budget | Not specified; API cost depends on chosen model and subset. |
| Human expertise | Needed for responsible interpretation and any manual audit of item or scorer behavior. |
| Account, license, or competition eligibility | Hugging Face account/acknowledgement may be required; HLE-Rolling hosted submission may have platform-specific requirements. |
| Ethical, safety, or data-use obligations | Public task set should not be used for training or fine-tuning, according to dataset access terms and repository warnings. |

Other requirements/comments: Users should preserve the non-training warning when redistributing or citing HLE materials.

### 5.4 Dataset and Item Access

| Component | Public | Restricted | Hidden | Not available | Status detail |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Training or development items | - [ ] | - [ ] | - [ ] | - [x] | HLE is not primarily released as a train/dev/test suite. |
| Public evaluation items | - [x] | - [x] | - [ ] | - [ ] | Public 2,500 set via Hugging Face with access acknowledgement. |
| Private or held-out evaluation items | - [ ] | - [ ] | - [x] | - [ ] | Private set described for overfitting/gaming checks. |
| Answer keys or reference solutions | - [x] | - [x] | - [ ] | - [ ] | Available as part of evaluation materials; access follows dataset terms. |
| Metadata or annotations | - [x] | - [x] | - [ ] | - [ ] | Public metadata exists, but full item-development metadata is not public. |
| Raw model outputs or logs | - [ ] | - [ ] | - [ ] | - [x] | Published model-run raw outputs are not documented as public. |

Other access/comments: Public access is meaningful but not fully open in the sense of unrestricted anonymous download.

### 5.5 Provenance and Contamination Documentation

| Topic | Documented | Partially documented | Not documented | Status detail |
| :--- | :---: | :---: | :---: | :--- |
| Data origin or task creation | - [x] | - [ ] | - [ ] | Expert-contributed and reviewed questions. |
| Author or contributor qualifications | - [x] | - [ ] | - [ ] | Contributor and author information is extensive. |
| Deduplication or overlap checks | - [ ] | - [x] | - [ ] | Searchability and audit procedures are described; formal deduplication metrics are limited. |
| Public/private split rationale | - [ ] | - [x] | - [ ] | Rationale is documented; size and comparability details are limited. |
| Contamination screening | - [x] | - [ ] | - [ ] | Non-searchability checks, search-enabled audit, private holdout, canary, and non-training warning are documented. |
| Canary strings or training-data warnings | - [x] | - [ ] | - [ ] | Repository includes canary and warning against inclusion in training corpora. |
| Refresh or rotation policy | - [ ] | - [x] | - [ ] | HLE-Rolling exists; full comparability policy remains limited. |
| Reporting of known leaks or retired items | - [ ] | - [x] | - [ ] | Rolling change file records updates/fixes; leak reporting policy is not comprehensive. |

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
- [ ] Continuous integration or test suite

Other reproducibility comments: Reproducibility is adequate for independent reruns of the public set, but not for exact replication of published model tables.

### 5.7 Maintenance and Versioning

| Topic | Response |
| :--- | :--- |
| Maintainer identity | Center for AI Safety / Scale AI ecosystem; GitHub repository under `centerforaisafety/hle`. |
| Version naming or release tags | No conventional release tags reviewed; public final set and HLE-Rolling are the main version concepts. |
| Changelog or update record | HLE-Rolling change file is public. |
| Issue or feedback process | GitHub issues and website feedback/submission links. |
| Item correction process | Rolling update file suggests corrections/additions, but detailed process is limited. |
| Deprecated item handling | Partially documented through rolling changes. |
| Private-set refresh policy | Not fully documented. |
| Score comparability across versions | Partially documented; HLE-Rolling may improve freshness but complicates longitudinal comparison. |
| Long-term archival plan | Not documented. |

Review notes: HLE-Rolling is a strength for maintenance, but versioned score interpretation needs more detail.

---

## Appendix A. General Description of the Benchmark

Humanity's Last Exam is an expert-level closed-ended academic benchmark for frontier AI systems. The current official public set contains 2,500 questions across over 100 subject areas, including text-only and image-containing items. Models answer questions and provide confidence; scoring reports accuracy and calibration-related outputs. The benchmark was built through expert contribution, review, auditing, and non-searchability checks, and it now has a Nature article, arXiv preprint, public GitHub repository, Hugging Face task set, official website, and HLE-Rolling maintained variant. Its narrowest defensible interpretation is performance on difficult closed-ended academic questions under documented HLE conditions, not standalone evidence of AGI or autonomous research capability.

---

# Part B. Evaluation of the Benchmark

Part B evaluates whether HLE is adequate as a measurement instrument for its intended use. Ratings use Part A plus EFPA, BetterBench, Measuring what Matters, and AGI/CHC caution principles.

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
| 6.2 Phenomenon-task-metric-claim chain | `3` |
| 6.3 Development process and task/item quality | `3` |
| 6.4 Documentation available to users | `3` |
| 6.5 Procedural instructions for administration, scoring, and interpretation | `2` |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality | `3` |

Review notes:

6.1 basis: HLE clearly defines a narrow purpose: difficult closed-ended academic questions for frontier AI systems. Gap: no formal psychometric construct definition or CHC-style ability map. Rationale: strong for expert-level academic performance, weaker for any broad cognitive reading. Caution: do not treat the name or breadth of subjects as a validated general-intelligence construct.

6.2 basis: The task and metric fit closed-ended academic answering: questions have reference answers, model answers are judged, and accuracy is reported. Gap: full scorer validation and construct-irrelevant variance analysis are incomplete. Rationale: the phenomenon-task-metric-claim chain is plausible and mostly explicit. Caution: accuracy can still reflect formatting, judge behavior, item exposure, or answer-equivalence issues.

6.3 basis: Expert contributions, review rubrics, auditing, non-searchability checks, and public feedback/rolling maintenance support item quality. Gap: quantitative item statistics, item-level difficulty/discrimination metadata, and representativeness analysis are limited. Rationale: item-development quality is good for a public AI benchmark. Caution: expert-authored breadth is not the same as systematic sampling of all academic domains.

6.4 basis: Nature, arXiv, GitHub, Hugging Face, website, and changelog materials provide substantial documentation. Gap: exact replication package, raw outputs, and complete private-set details remain absent. Rationale: documentation is good enough for qualified public use. Caution: users need technical judgment to avoid overinterpreting what is not documented.

6.5 basis: Prompts, scripts, requirements, and judge instructions are available. Gap: malformed/refusal handling, seed policy, exact API conditions, and published-run replication details are incomplete. Rationale: procedural instructions support cautious reruns but not exact published-score reproduction. Caution: small score differences should not be treated as precise without stronger procedure and uncertainty support.

Other comments: Section 6 is HLE's strongest area because official materials explain why the benchmark exists and how the task set was created.

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
| 7.2 Prompts, instructions, rubrics, and response format | `3` |
| 7.3 Evaluation harness, scorer, and implementation usability | `2` |
| 7.4 Accessibility across relevant modalities, languages, and system types | `2` |
| 7.5 Licensing, usage requirements, and sensitive-content warnings | `2` |
| 7.6 Overall quality of benchmark materials | `2` |

Review notes:

7.1 basis: Public 2,500-question set, repository, scripts, website, and hosted data are available. Gap: private set, raw outputs, and full development metadata are not public. Rationale: material availability is good for public research use. Caution: public-set availability increases contamination risk over time.

7.2 basis: Prompts, answer/confidence format, judge prompt, and human review rubrics are documented. Gap: parser and judge validation are incomplete. Rationale: response requirements are clear enough for intended users. Caution: strict formatting or judge interpretation may introduce non-target variance.

7.3 basis: GitHub provides simple evaluation scripts and requirements. Gap: no container, CI, full replication script, seed policy, or robust local-model pathway. Rationale: usability is adequate, not reproducibility-grade. Caution: independent results may differ by model endpoint, API behavior, and judge configuration.

7.4 basis: Full set includes images, text-only subset exists, and official results distinguish modalities. Gap: English-only coverage, no accessibility accommodation analysis, and limited local/open-weight comparability. Rationale: system coverage is adequate for frontier API models, weaker for broader system classes. Caution: full-set scores should not be compared directly to text-only scores.

7.5 basis: MIT license and non-training warnings are documented. Gap: downstream data-host terms and sensitive-content warnings are not fully analyzed in official materials. Rationale: licensing and use obligations are usable but incomplete. Caution: users should distinguish repository license from dataset access conditions.

Other comments: HLE's material quality is materially stronger than the earlier local-only pilot, but implementation validation remains the limiting factor.

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
| 8.1 Random, chance, floor, and ceiling baselines | `1` |
| 8.2 Human or expert baselines | `2` |
| 8.3 Model comparator cohort | `3` |
| 8.4 Criterion thresholds or score bands | `1` |
| 8.5 Overall adequacy of baselines and reference interpretation | `2` |

Review notes:

8.1 basis: The official materials recognize multiple-choice floors and benchmark saturation concerns. Gap: no comprehensive random baseline by item type, score distribution, or ceiling analysis. Rationale: limited support. Caution: near-zero scores and small differences need floor/uncertainty context.

8.2 basis: Experts authored and reviewed items, making expert performance relevant. Gap: no published expert benchmark-taking norm group with procedures and score distributions. Rationale: adequate only for item target, not human norming. Caution: "expert-level" should not be read as a calibrated human percentile.

8.3 basis: Official paper reports named frontier model comparisons with model versions and subsets. Gap: no raw outputs, full API condition reproducibility, or repeat-run uncertainty. Rationale: good contemporaneous comparator cohort. Caution: model rankings age quickly and may not replicate exactly.

8.4 basis: Accuracy and calibration are reported. Gap: no validated proficiency threshold, pass/fail score band, or minimum meaningful difference. Rationale: weak threshold interpretation. Caution: do not make deployment or procurement decisions from arbitrary HLE cutoffs.

Other comments: Section 8 is adequate for cautious research comparison but not for norm-like score interpretation.

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
| 9.1 Run-to-run stability, seeds, and sampling settings | `1` |
| 9.2 Score uncertainty, confidence intervals, or standard errors | `1` |
| 9.3 Human rater, scorer, parser, or model-judge agreement | `1` |
| 9.4 Prompt, form, version, and environment stability | `1` |
| 9.5 Overall reliability and precision | `1` |

Review notes:

9.1 basis: Temperature/model-version conditions are partly reported. Gap: no systematic repeated-run variance, seeds, provider drift assessment, or prompt sensitivity analysis. Rationale: reliability support remains weak. Caution: small differences between models should not be overinterpreted.

9.2 basis: Aggregate score reporting exists, and simple evaluator output may compute summary intervals. Gap: published model comparisons lack comprehensive confidence intervals, standard errors, or statistical tests. Rationale: limited precision support. Caution: point estimates should not be treated as precise ranks.

9.3 basis: Human review supports item creation and judge prompt is public. Gap: model-judge validation, parser agreement, human-vs-judge comparison, and adjudication reliability are not fully documented. Rationale: scoring reliability is under-evidenced. Caution: judge errors may differ across domains and answer formats.

9.4 basis: Static public set and HLE-Rolling are documented. Gap: alternate-form equivalence, rolling-version comparability, and environment stability are not fully demonstrated. Rationale: versioning exists but stability is not yet established. Caution: rolling updates may improve freshness while weakening longitudinal comparability.

Other comments: Reliability and precision remain HLE's largest measurement-quality constraint.

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
| 10.1 Content validity and task representativeness | `3` |
| 10.2 Internal structure, subscores, or dimensionality | `1` |
| 10.3 Metric, scorer, and aggregation validity | `2` |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings | `2` |
| 10.5 Contamination, leakage, and gameability controls | `3` |
| 10.6 Claim proportionality and broad-capability cautions | `3` |
| 10.7 Overall validity support | `2` |

Review notes:

10.1 basis: Broad subject coverage, expert contributors, multi-stage review, audits, and non-searchability checks support content quality. Gap: no complete sampling frame, representativeness analysis, or item-level psychometric metadata. Rationale: strong content support for a closed-ended academic stress test. Caution: broad academic content is not full cognitive breadth.

10.2 basis: Domain and text-only/full-set subscores are reported. Gap: no dimensionality analysis, subscore reliability, or internal-structure validation. Rationale: subscores are descriptive, not validated latent dimensions. Caution: do not infer stable academic ability factors from category scores alone.

10.3 basis: Accuracy fits closed-ended answerable items, and calibration adds useful confidence information. Gap: judge validation, parser validation, malformed answer handling, and metric sensitivity tests are incomplete. Rationale: metric validity is adequate for cautious use. Caution: scoring can conflate target ability with formatting and judge behavior.

10.4 basis: HLE is compared with prior saturated benchmarks, expert difficulty expectations, and frontier model cohorts. Gap: direct human benchmark-taking distributions, convergent/discriminant validation, and ecological links to real research capability are limited. Rationale: relations support benchmark difficulty more than broad external validity. Caution: HLE should not be treated as a proxy for autonomous scientific productivity.

10.5 basis: Public/private split, non-searchability requirements, search-enabled audit, canary, non-training warning, feedback route, and HLE-Rolling are meaningful controls. Gap: private-set details, ongoing leak metrics, and full release-rule governance are incomplete. Rationale: controls are good but not exhaustive. Caution: the public set will become more exposed over time.

10.6 basis: Official materials explicitly caution against AGI/autonomous research interpretation from HLE score alone. Gap: no CHC-style breadth/depth validity argument for broad intelligence claims. Rationale: claim proportionality is relatively strong because the authors state limits. Caution: third-party communication may strip caveats.

Other comments: HLE's validity case is content-heavy and claim-bounded. Its strongest support does not remove the need for scoring and reliability validation.

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
| 11.3 Access, compute, tooling, and API/local comparability | `1` |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance | `2` |
| 11.5 Overall fair use and comparability | `2` |

Review notes:

11.1 basis: Standard prompts, model-version reporting, text-only/full-set distinctions, and category scores support cautious comparison. Gap: provider drift, seed policy, run variance, and local/API equivalence are incomplete. Rationale: adequate for paper-level comparison, not exact operational ranking. Caution: multimodal and text-only systems should be compared separately.

11.2 basis: HLE documents broad domains and image subset. Gap: English dominance, domain-level reliability, accessibility accommodations, and cultural/language coverage analyses are limited. Rationale: coverage is broad but fairness support is basic. Caution: domain breadth does not ensure equal measurement quality across domains.

11.3 basis: Public repository and hosted data support access for skilled users. Gap: API costs, local model path, compute budgets, and exact service conditions are under-specified. Rationale: access comparability is weak. Caution: users with different model access may not be evaluating under comparable conditions.

11.4 basis: Official materials include non-training warnings, contamination controls, and AGI interpretation caveats. Gap: formal release rules, sensitive-content analysis, and public communication policy are incomplete. Rationale: guidance is adequate but not comprehensive. Caution: public summaries should repeat the authors' limitations.

Other comments: HLE is reasonably fair for frontier API-model research comparisons but not for broad procurement, deployment, or policy decisions without additional analysis.

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
| 12.1 Report, leaderboard, dashboard, or result artifact scope | `2` |
| 12.2 Score granularity, uncertainty, and version labeling | `2` |
| 12.3 Linkage from scores to public claims | `3` |
| 12.4 Raw outputs, per-item data, or trace availability | `0` |
| 12.5 Overall quality of reports and public claims | `2` |

Review notes:

12.1 basis: Nature article, arXiv paper, website, repository sample output, and HLE-Rolling dashboard provide multiple report surfaces. Gap: no full public raw-output archive or complete formal leaderboard specification. Rationale: adequate reporting scope. Caution: hosted rolling reports should be date-stamped.

12.2 basis: Aggregate, category, text-only/full-set, token, and calibration outputs are reported. Gap: uncertainty, significance testing, per-item reporting, and exact version labels are incomplete. Rationale: granularity is useful but not precision-aware. Caution: rankings may be fragile.

12.3 basis: Official materials link scores to closed-ended academic capability and caution against AGI/autonomous research overclaims. Gap: third-party reporting guidance is limited. Rationale: score-to-claim linkage is good when official caveats are preserved. Caution: public use may exaggerate the claim.

12.4 basis: Public raw model outputs, judge logs, per-item outcomes for reported runs, and traces are not documented as available. Gap: complete raw outputs and logs. Rationale: cannot rate as present from available materials. Caution: independent error analysis is limited.

Other comments: HLE reports results responsibly, but reporting infrastructure remains weaker than the paper-level presentation.

---

## Final Evaluation

### Evaluative Report of the Benchmark

HLE is a strong content-driven benchmark for the narrow construct of expert-level closed-ended academic question answering by frontier AI systems. Its strongest support comes from expert item development, broad academic coverage, public release of the final 2,500-question set, clear answer-confidence evaluation, official paper and repository documentation, and explicit caution against AGI or autonomous research interpretation. The Nature publication and HLE-Rolling materials make the benchmark more mature than the earlier local pilot suggested.

The main constraints are reliability, precision, scorer validation, and reproducibility-grade reporting. The official materials still do not provide a complete uncertainty framework for published model comparisons, repeated-run variance, judge validation, raw outputs, full private-set details, or exact replication conditions. These are gaps, not proof of poor benchmark quality, but they materially limit fine-grained rankings, high-stakes use, and broad public claims.

### Conclusions

HLE can support cautious research claims about performance on difficult, closed-ended, mostly academic questions under HLE conditions. It should not be used alone as a measure of AGI, autonomous research capability, open-ended scientific creativity, long-horizon planning, or general cognitive breadth. Users should treat HLE as a high-quality academic stress test with meaningful contamination controls and strong caveats, not as a complete measurement theory of intelligence.

### Recommendations

Use HLE for source-bound frontier model comparison and academic stress testing. Report model versions, prompts, API/provider conditions, data snapshot, judge configuration, and date. Preserve the official caveats. Maintainers or future reviewers should prioritize judge validation, repeat-run uncertainty, raw-output release or audit access, versioned HLE-Rolling comparability policy, and more explicit score interpretation guidance.

### Summary of Ratings

| Section or area | Rating (`n/a`, `0`-`4`) |
| :--- | :---: |
| Section 6. Rationale, documentation, and task/item quality | `3` |
| Section 7. Benchmark materials and usability | `2` |
| Section 8. Baselines and comparators | `2` |
| Section 9. Reliability and precision | `1` |
| Section 10. Validity support | `2` |
| Section 11. Fair use and comparability | `2` |
| Section 12. Reports, leaderboards, and public claims | `2` |
| Construct definition and claim scope | `3` |
| Scoring validity | `2` |
| Reproducibility and implementation transparency | `2` |
| Contamination and gameability controls | `3` |
| Maintenance and versioning | `2` |
| Overall claim-bounded measurement quality | `2` |

Review notes: The overall rating is not a mechanical average. Strong rationale and content support are constrained by weaker reliability, scorer-validation, and reporting support.

### Gap Register

| Gap | Affected rating(s) | Why it matters | Needed for a higher rating |
| :--- | :--- | :--- | :--- |
| No comprehensive repeat-run uncertainty for published comparisons | 8, 9, 12, overall | Limits fine-grained rankings and statistical interpretation. | Repeated runs, seed/temperature details, confidence intervals, and comparison tests. |
| Model-judge and parser validation are incomplete | 7, 9, 10, scoring validity | Scoring errors can affect domain and format comparisons. | Human-judge comparison sample, parser error audit, adjudication rules, and agreement statistics. |
| Public/private and rolling comparability are partially documented | 5, 10, 11, 12, maintenance | Hidden and rolling forms support integrity but complicate longitudinal interpretation. | Version policy, linking study, update rules, and archive plan. |
| Raw outputs and per-item results for reported runs are not public | 7, 9, 12, reproducibility | Limits independent error analysis and replication. | Raw response archive or controlled audit access with model, prompt, and judge metadata. |
| Broad intelligence mapping is absent | 2.18, 10, final | Prevents broad cognitive interpretation. | CHC/AGI-style breadth/depth analysis or continued explicit narrow caveats. |

Other gaps/comments: The gaps are mostly about precision and interpretation, not about the existence of usable public benchmark materials.

### Reviewer Caution Statement

The narrowest defensible interpretation is: HLE measures model performance on difficult closed-ended academic questions, including some image-conditioned items, under official HLE prompting and scoring conditions. It is not a standalone measure of AGI, autonomous research ability, broad agency, or open-ended scientific creativity. Ratings should be revisited when HLE-Rolling governance, scorer validation, repeat-run uncertainty, raw-output access, and private-set comparability are better documented.
