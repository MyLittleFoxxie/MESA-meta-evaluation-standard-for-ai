# MESA EFPA Template v3

This template applies an EFPA-inspired review structure to AI benchmark review. Part A describes the benchmark as a measurement instrument. Part B evaluates how well the benchmark supports its stated interpretation using `[n/a]` and `0`-`4` ratings.

Keep the boundary explicit: Part A records what the available sources state and marks missing documentation; Part B contains reviewer judgments, each tied to source-grounded reviewer comments.

Use `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md` as the source structure, `markdown/MESA Part B literature synthesis.md` as the local synthesis for Part B, and `markdown/MESA EFPA template guide v5.md` as the field-level reviewer guide.

## Information Sources

Purpose: inventory the evidence base before filling the review. Use this table to record what was inspected; later sections should cite or point back to these sources rather than duplicating the full inventory.

Record the sources used for this review. Prefer official benchmark materials before independent commentary.

| Source type | Source details | Access date | Notes |
| :--- | :--- | :--- | :--- |
| Official paper or technical report |  |  |  |
| Benchmark website |  |  |  |
| Repository |  |  |  |
| Dataset card or data host |  |  |  |
| Leaderboard or results page |  |  |  |
| Evaluation harness or package |  |  |  |
| Documentation or user guide |  |  |  |
| Release notes or changelog |  |  |  |
| Maintainer statements |  |  |  |
| Independent sources used for context |  |  |  |

Documentation status options used throughout:

- [ ] Documented
- [ ] Partially documented
- [ ] Not documented
- [ ] Not applicable
- [ ] Unclear from available sources

Part B ratings are defined in the Part B key to ratings. Do not mechanically average section ratings.

---

# Part A. Description of the Benchmark

## Section 1. Factual Description

Purpose: identify the review, the benchmark, and the public artifacts. Keep descriptive facts here; do not evaluate adequacy.

### 1.1 Review Information

Purpose: identify the review event. Keep benchmark identity and artifacts in 1.2 and 1.3.

| Prompt | Response |
| :--- | :--- |
| Reviewer |  |
| Date of current review |  |
| Date of previous review, if applicable |  |
| Review scope |  |
| Sources reviewed |  |

### 1.2 Benchmark Information

Purpose: identify the benchmark's official name, provenance, version, release status, ownership, and citation record.

| Prompt | Response |
| :--- | :--- |
| Benchmark name |  |
| Short name or acronym |  |
| Benchmark version, edition, or release |  |
| Original benchmark name, if this is a variant or derivative |  |
| Benchmark creators or authors |  |
| Current maintainers |  |
| Host organization, publisher, or distributor |  |
| Date of original release |  |
| Date of current release or revision |  |
| License or access terms |  |
| Persistent identifier, citation, or DOI |  |

### 1.3 Public Artifacts

Purpose: record artifact existence and access status. Artifact quality is evaluated later in Part B.

| Artifact | URL or location | Access status | Notes |
| :--- | :--- | :--- | :--- |
| Paper or technical report |  |  |  |
| Benchmark website |  |  |  |
| Code repository |  |  |  |
| Evaluation harness |  |  |  |
| Dataset or task set |  |  |  |
| Prompt set |  |  |  |
| Rubric or scoring guide |  |  |  |
| Leaderboard |  |  |  |
| Changelog or release notes |  |  |  |
| Contact or issue channel |  |  |  |

---

## Section 2. Classification

Purpose: classify what the benchmark claims to measure, what it is used for, which systems and users it targets, and how tasks, responses, inputs, conditions, technology, versions, and scoring evidence are structured. This section is descriptive only.

### 2.1 Claimed Capability Domains

Purpose: record the claimed capability or phenomenon. Select only domains claimed or clearly implied by benchmark documentation. Broad claims such as AGI, general intelligence, agency, autonomy, or expert capability should be documented here and evaluated later in Part B validity, not in a separate Part A screen.

- [ ] Not explicitly stated
- [ ] General capability or intelligence
- [ ] Broad knowledge
- [ ] Reading and language understanding
- [ ] Writing or generation quality
- [ ] Mathematics
- [ ] On-the-spot reasoning
- [ ] Working memory
- [ ] Persistent memory, retrieval, continual learning, or adaptation over time
- [ ] Speed or processing fluency
- [ ] Coding or software engineering
- [ ] Scientific, engineering, or technical expertise
- [ ] Domain-specific professional expertise
- [ ] Requirements engineering or specification work
- [ ] Multimodal perception
- [ ] Visual or spatial processing
- [ ] Audio or speech
- [ ] Video understanding
- [ ] Tool use
- [ ] Nested tool or API sequencing
- [ ] Planning, agency, or long-horizon reasoning
- [ ] Web or browser interaction
- [ ] Embodied, robotic, or simulated environment interaction
- [ ] World modeling or environment dynamics
- [ ] Safety, risk, refusal, or policy compliance
- [ ] Robustness
- [ ] Other:

Reviewer notes:

### 2.2 Area of Use

Purpose: record what benchmark outputs are intended to be used for. This differs from 2.4, which records who interprets or acts on those outputs. Select all documented use contexts.

- [ ] Not explicitly stated
- [ ] Model comparison
- [ ] Leaderboard ranking
- [ ] Capability profiling
- [ ] Research diagnostics
- [ ] Safety or risk evaluation
- [ ] Release or deployment readiness gate
- [ ] Procurement or vendor comparison
- [ ] Internal regression testing
- [ ] Requirements engineering or specification support
- [ ] Policy or governance analysis
- [ ] Other:

Reviewer notes:

### 2.3 Intended AI Systems

Purpose: record the system classes the benchmark is intended to evaluate. Only record systems stated or clearly implied by benchmark documentation.

- [ ] Not explicitly stated
- [ ] Frontier general-purpose language models
- [ ] Chat or instruction-following models
- [ ] Code models
- [ ] Multimodal models
- [ ] Audio or speech models
- [ ] Agentic systems
- [ ] Tool-using systems
- [ ] Embodied or robotic systems
- [ ] World models or environment simulators
- [ ] Continual-learning or memory-augmented systems
- [ ] Retrieval-augmented systems
- [ ] Domain-specialized models
- [ ] Open-weight local models
- [ ] API-hosted models
- [ ] Other:

Free text description:

### 2.4 Intended Users of Benchmark Outputs

Purpose: record who is supposed to interpret or act on benchmark outputs. This is separate from 2.2's use context. Select all that apply.

- [ ] Not explicitly stated
- [ ] Benchmark creators or maintainers
- [ ] AI researchers
- [ ] Model developers
- [ ] Product teams
- [ ] Safety evaluators
- [ ] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [ ] Educators or academic reviewers
- [ ] Public leaderboard users
- [ ] Other:

Reviewer notes:

### 2.5 Task Families, Subdomains, and Scores

Purpose: make the construct-to-task-to-score structure explicit. Describe the number and meaning of task families, subdomains, dataset/task partitions, score families, aggregate metrics, subscores, or derived outputs.

| Component | Description | Source |
| :--- | :--- | :--- |
| Claimed construct or phenomenon |  |  |
| Construct subcomponents |  |  |
| Task families or subdomains |  |  |
| Task sampling or selection logic |  |  |
| Dataset/task partitions |  |  |
| Primary score |  |  |
| Subscores |  |  |
| Derived or aggregate scores |  |  |
| Qualitative labels or bands |  |  |
| Claim boundaries or caveats |  |  |

### 2.6 Model Response Mode

Purpose: record what the evaluated system must produce or do. Responses may be answers, text, code, media, tool calls, trajectories, control signals, files, or environment actions. Select all that apply.

- [ ] Not explicitly stated
- [ ] Multiple choice
- [ ] Short text
- [ ] Long-form text
- [ ] Structured output, such as JSON or XML
- [ ] Code
- [ ] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or artifact generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment
- [ ] Sensorimotor or control output
- [ ] Other:

Required output format, if any:

### 2.7 Prerequisites for Evaluated Systems

Purpose: record prerequisites needed for fair or intended evaluation. Classify each requirement based on benchmark documentation.

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Language support | - [ ] | - [ ] | - [ ] |  |
| Context length | - [ ] | - [ ] | - [ ] |  |
| Multimodal input support | - [ ] | - [ ] | - [ ] |  |
| Audio or speech I/O | - [ ] | - [ ] | - [ ] |  |
| Structured output support | - [ ] | - [ ] | - [ ] |  |
| Tool access | - [ ] | - [ ] | - [ ] |  |
| Browser or internet access | - [ ] | - [ ] | - [ ] |  |
| Code execution | - [ ] | - [ ] | - [ ] |  |
| Memory or persistent state | - [ ] | - [ ] | - [ ] |  |
| Continual-learning or update mechanism | - [ ] | - [ ] | - [ ] |  |
| Sensor access | - [ ] | - [ ] | - [ ] |  |
| Actuator or control interface | - [ ] | - [ ] | - [ ] |  |
| Simulator or world-model interface | - [ ] | - [ ] | - [ ] |  |
| API compatibility | - [ ] | - [ ] | - [ ] |  |
| Latency or time budget | - [ ] | - [ ] | - [ ] |  |
| Cost or compute budget | - [ ] | - [ ] | - [ ] |  |

Other requirements:

### 2.8 Evaluation Conditions

Purpose: record the conditions required to run the benchmark as intended, including prompts, tools, simulators, sensors, actuators, timing, security, and safety constraints.

| Condition | Description | Source |
| :--- | :--- | :--- |
| Prompting protocol |  |  |
| System prompt |  |  |
| Few-shot examples |  |  |
| Sampling settings |  |  |
| Tool permissions |  |  |
| Sensor and observation rules |  |  |
| Actuator or action rules |  |  |
| Time limits |  |  |
| Human intervention rules |  |  |
| Hardware or hosted service |  |  |
| Network requirements |  |  |
| Real-world or live-service boundary |  |  |
| Sandbox or security constraints |  |  |
| Safety or risk constraints |  |  |
| Other special conditions |  |  |

### 2.9 Task and Response Types

Purpose: classify the task interaction surface. Select all that apply.

Selection-based responses:

- [ ] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [ ] Ranking
- [ ] Classification
- [ ] Pairwise preference

Production-based responses:

- [ ] Open-ended text
- [ ] Code generation
- [ ] Proof, derivation, or explanation
- [ ] Structured data
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
- [ ] Token usage
- [ ] Cost
- [ ] Tool traces
- [ ] Intermediate reasoning traces
- [ ] Execution logs
- [ ] Other:

### 2.10 Input Stimulus Type

Purpose: record what the benchmark gives to the system, including files, screens, APIs, tools, environment state, or sensor streams. Select all that apply.

- [ ] Not explicitly stated
- [ ] Text
- [ ] Code
- [ ] Tables or structured data
- [ ] Images
- [ ] Audio
- [ ] Video
- [ ] Documents
- [ ] Web pages
- [ ] APIs or tools
- [ ] Dynamic environment
- [ ] Sensor or actuator state
- [ ] Other:

### 2.11 Number of Items or Measurement Points

Purpose: record sample size. Where the benchmark is dynamic, record minimum, maximum, and typical task counts, episodes, trials, simulator rollouts, or measurement points.

| Prompt | Response |
| :--- | :--- |
| Total public items or tasks |  |
| Total private or hidden items |  |
| Development or example items |  |
| Test items |  |
| Dynamic or generated tasks |  |
| Episodes, trials, or measurement points |  |
| Notes on item count uncertainty |  |

### 2.12 Mode of Evaluation

Purpose: record how evaluation is conducted and how much control exists over systems, outputs, traces, or endpoints submitted for scoring. Identity control concerns model/version authenticity. Condition control concerns prompts, tools, settings, hardware, timing, and environment.

Select all that apply.

- [ ] Not indicated
- [ ] Local batch evaluation
- [ ] Hosted benchmark platform
- [ ] Leaderboard submission
- [ ] Private controlled evaluation
- [ ] Public open evaluation
- [ ] Interactive agent evaluation
- [ ] Human-in-the-loop evaluation
- [ ] Continuous or rolling evaluation
- [ ] Other:

Identity and condition controls:

- [ ] No control over systems, outputs, traces, or endpoints submitted for scoring
- [ ] Some control over systems, outputs, traces, or endpoints submitted for scoring
- [ ] Controlled model access or audit
- [ ] Controlled evaluation center or private harness
- [ ] Not documented

### 2.13 Technological Arrangements

Purpose: record supported and required technology. Mark `A` when a technology is available or supported. Mark `R` when the benchmark cannot be run as intended without it. A row may be both `A` and `R`.

| Technology | A | R | Notes |
| :--- | :---: | :---: | :--- |
| API access | - [ ] | - [ ] |  |
| Local inference | - [ ] | - [ ] |  |
| GPU | - [ ] | - [ ] |  |
| CPU-only execution | - [ ] | - [ ] |  |
| Docker or container | - [ ] | - [ ] |  |
| Python package or CLI | - [ ] | - [ ] |  |
| Browser | - [ ] | - [ ] |  |
| External tools | - [ ] | - [ ] |  |
| Internet access | - [ ] | - [ ] |  |
| Simulator or environment runtime | - [ ] | - [ ] |  |
| Sensors or media capture | - [ ] | - [ ] |  |
| Actuators or control interface | - [ ] | - [ ] |  |
| Proprietary platform | - [ ] | - [ ] |  |
| Other: | - [ ] | - [ ] |  |

### 2.14 Time and Resource Requirements

Purpose: record documented estimates, not guesses. If a source gives only qualitative guidance, quote or summarize it. Write "not documented" when no estimate is stated.

| Activity | Time, compute, or cost estimate | Source |
| :--- | :--- | :--- |
| Setup |  |  |
| Model inference or task completion |  |  |
| Scoring |  |  |
| Human adjudication |  |  |
| Analysis or reporting |  |  |
| Full benchmark run |  |  |
| API or compute cost |  |  |

### 2.15 Benchmark Forms, Versions, and Variants

Purpose: record benchmark forms, versions, and variants in free text. Include public/private forms, development/test forms, rolling versions, language or modality variants, domain subsets, short forms, deprecated versions, hidden forms, and archived forms when documented.

Free text:

Source notes:

### 2.16 Static or Dynamic Task Determination

Purpose: record how tasks are selected or generated. Select all that apply.

- [ ] Static fixed task set
- [ ] Random sample from fixed pool
- [ ] Hidden test set selected by maintainers
- [ ] Procedurally generated tasks
- [ ] Adaptive routing based on performance
- [ ] Dynamic environment generation
- [ ] World-model or simulator rollout
- [ ] Continual-learning sequence
- [ ] Rolling or periodically refreshed task set
- [ ] Not explicitly stated
- [ ] Other:

Describe task selection method:

### 2.17 Evidence Sources Used in Scoring

Purpose: record what evidence the scorer uses. Select all that apply.

- [ ] Model final answer
- [ ] Model intermediate trace
- [ ] Tool-use trace
- [ ] Nested API-call sequence
- [ ] Code execution result
- [ ] Environment state
- [ ] Sensor, action, or trajectory log
- [ ] World-model rollout
- [ ] Reference answer
- [ ] Unit test
- [ ] Human judge
- [ ] Model judge
- [ ] Ensemble or panel adjudication
- [ ] External verifier
- [ ] Other:

Reviewer notes:

---

## Section 3. Measurement and Scoring

Purpose: describe how benchmark inputs and model behavior become scores. Record the scoring pipeline, metrics, transformations, baselines, uncertainty, and documented metric-to-claim linkage without evaluating adequacy.

### 3.1 Scoring Procedure

Purpose: identify scoring methods and summarize the pipeline from model output to reported result. Select all that apply.

- [ ] Not explicitly stated
- [ ] Automated exact-match scoring
- [ ] Automated semantic or embedding-based scoring
- [ ] Unit-test or execution-based scoring
- [ ] Rule-based scoring
- [ ] Human rating
- [ ] Model-as-judge scoring
- [ ] Pairwise preference scoring
- [ ] Hybrid automated and human scoring
- [ ] Leaderboard service scoring
- [ ] Manual adjudication
- [ ] Other:

Describe the scoring pipeline:

### 3.2 Scores and Metrics

Purpose: describe how global, partial, derived, or qualitative scores are produced.

| Score or metric | Definition | Aggregation | Interpretation stated by authors |
| :--- | :--- | :--- | :--- |
| Primary score |  |  |  |
| Subscore |  |  |  |
| Derived score |  |  |  |
| Qualitative band |  |  |  |

Treatment of invalid, missing, malformed, or refused responses:

### 3.3 Scale or Metric Types

Purpose: classify the reported metric types. Select all that apply.

- [ ] Raw score
- [ ] Accuracy
- [ ] Success rate
- [ ] Pass rate or pass@k
- [ ] Unit-test pass rate
- [ ] Win rate
- [ ] Elo or ranking score
- [ ] Pairwise preference score
- [ ] Reward or return
- [ ] Cost-adjusted score
- [ ] Rubric or criteria-aware score
- [ ] Safety or risk score
- [ ] World-model, trajectory, or environment-dynamics score
- [ ] Calibration or uncertainty score
- [ ] Percentile or normalized score
- [ ] Threshold or decision index
- [ ] Other:

### 3.4 Score Transformation

Purpose: record whether and how raw scores are transformed, normalized, weighted, or aggregated. Select all that apply.

- [ ] No transformation
- [ ] Linear transformation
- [ ] Non-linear transformation
- [ ] Normalization against baseline
- [ ] Weighting across subdomains
- [ ] Aggregation formula documented
- [ ] Aggregation formula partially documented
- [ ] Aggregation formula not documented
- [ ] Not applicable

Formula or transformation notes:

### 3.5 Reference Groups, Baselines, and Comparators

Purpose: record the reference points used to interpret scores. Select all that apply.

- [ ] No baseline or comparator documented
- [ ] Random or chance baseline
- [ ] Human baseline
- [ ] Expert human baseline
- [ ] Model baseline
- [ ] Previous model cohort
- [ ] Commercial system comparator
- [ ] Open-weight model comparator
- [ ] Domain-specific reference group
- [ ] Other:

Describe comparator construction and source:

| Comparator or baseline | Construction method | Intended interpretation | Source |
| :--- | :--- | :--- | :--- |
| Random or chance baseline |  |  |  |
| Human baseline |  |  |  |
| Expert baseline |  |  |  |
| Model cohort |  |  |  |
| Prior benchmark or version |  |  |  |
| Criterion threshold or floor/ceiling |  |  |  |

### 3.6 Score Uncertainty and Stability

Purpose: record whether uncertainty, statistical comparison, or run-to-run stability is reported. This remains descriptive in Part A.

- [ ] Confidence intervals
- [ ] Standard errors
- [ ] Bootstrap intervals
- [ ] Multiple runs or seeds
- [ ] Judge agreement statistics
- [ ] Human inter-rater agreement
- [ ] Sensitivity analyses
- [ ] Not reported
- [ ] Other:

Notes:

### 3.7 Metric-to-Claim Linkage

Purpose: record the documented link between metric behavior and benchmark claims. This remains descriptive in Part A.

| Prompt | Response | Source |
| :--- | :--- | :--- |
| Why the primary metric was chosen |  |  |
| Whether metric floors or ceilings are documented |  |  |
| Whether the metric may reward non-target behavior named by the source |  |  |
| Whether parsing, judge, or scorer validation is documented |  |  |
| Whether score uncertainty affects claim interpretation |  |  |
| Whether score differences are interpreted statistically |  |  |
| Whether benchmark reports state what users should not infer |  |  |

---

## Section 4. Benchmark Outputs and Reports

Purpose: describe what benchmark users see after evaluation: reports, leaderboards, dashboards, scorecards, raw outputs, logs, traces, caveats, and audience-specific outputs.

### 4.1 Output Availability

Purpose: record which output artifacts are available.

- [ ] Public leaderboard available
- [ ] Public aggregate scores available
- [ ] Public per-domain scores available
- [ ] Public per-item scores available
- [ ] Public raw model outputs available
- [ ] Public traces or logs available
- [ ] Private reports available only to submitters
- [ ] No formal report or leaderboard documented

### 4.2 Output Name or Description

Purpose: list each output artifact and who can see it.

| Output | Description | Public/private | Source |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

### 4.3 Output Design or Presentation

Purpose: classify the presentation format. Select all that apply.

- [ ] Static text report
- [ ] Tables
- [ ] Graphs or visualizations
- [ ] Leaderboard
- [ ] Interactive dashboard
- [ ] Downloadable CSV or JSON
- [ ] API output
- [ ] Paper-only results
- [ ] Other:

### 4.4 Output Structure

Purpose: classify how outputs are organized. Select all that apply.

- [ ] Aggregate-score based
- [ ] Capability-domain based
- [ ] Task-family based
- [ ] Criterion-threshold based
- [ ] Pairwise-comparison based
- [ ] Rank based
- [ ] Cost or efficiency adjusted
- [ ] Error-analysis based
- [ ] Trace or process based
- [ ] Other:

### 4.5 Sensitivity to Context

Purpose: record whether reports change by user, context, or intended use. Select one.

- [ ] One output format for all contexts
- [ ] User-definable output contexts
- [ ] Pre-defined versions adapted to audience or use
- [ ] Context sensitivity not documented

List available contexts:

### 4.6 Development of Outputs

Purpose: record how report content was designed or generated. Select all that apply.

- [ ] Based on benchmark authors' design
- [ ] Based on empirical or actuarial relationships
- [ ] Based on expert judgment
- [ ] Based on human annotation
- [ ] Based on model-as-judge outputs
- [ ] Automatically generated by benchmark platform
- [ ] Other:

Describe source of report content:

### 4.7 Modifiability

Purpose: record whether users can modify, filter, export, or generate reports. Select one.

- [ ] Not modifiable
- [ ] Limited modification by submitter or user
- [ ] Fully user-generated reports possible
- [ ] Not documented

### 4.8 Transparency

Purpose: record whether outputs explain the link between tasks, scores, and claims. Select one.

- [ ] Clear linkage between tasks, scores, and reported claims
- [ ] Partial linkage between tasks, scores, and reported claims
- [ ] Linkage is not obvious from available documentation
- [ ] Mixture of clear and concealed linkage
- [ ] Not documented

Notes:

### 4.9 Output Content

Purpose: record what kinds of information appear in outputs. Select all that apply.

- [ ] Capability descriptions
- [ ] Aggregate rankings
- [ ] Subdomain comparisons
- [ ] Error categories
- [ ] Examples of successes or failures
- [ ] Cost, latency, or efficiency data
- [ ] Process traces
- [ ] Recommendations or interpretation notes
- [ ] Warnings or caveats
- [ ] Other:

### 4.10 Intended Recipients

Purpose: record report recipients, which may differ from general benchmark users in 2.4. Select all that apply.

- [ ] Benchmark maintainers
- [ ] Model developers
- [ ] AI researchers
- [ ] Safety evaluators
- [ ] Policy or governance actors
- [ ] Product or deployment teams
- [ ] Procurement teams
- [ ] Public audience
- [ ] Other:

---

## Section 5. Supply Arrangements and Materials

Purpose: describe materials and access arrangements needed to inspect, run, reproduce, submit to, or maintain the benchmark.

### 5.1 Supporting Information Provided

Purpose: record supporting documentation and guidance. Select all that apply.

- [ ] Technical report
- [ ] User guide
- [ ] Repository README
- [ ] API documentation
- [ ] Dataset card
- [ ] Model submission instructions
- [ ] Scoring documentation
- [ ] Rubric or annotation guide
- [ ] Evaluation examples
- [ ] FAQ or discussion forum
- [ ] Changelog or release notes
- [ ] Other:

### 5.2 Methods of Publication

Purpose: record where benchmark materials are published or distributed. Select all that apply.

- [ ] Academic paper
- [ ] Benchmark website
- [ ] Git repository
- [ ] Package registry
- [ ] Dataset hosting platform
- [ ] Leaderboard platform
- [ ] Downloadable documents
- [ ] Private distribution
- [ ] Other:

### 5.3 User Requirements or Qualifications

Purpose: describe any requirements specified for running, submitting to, or interpreting the benchmark.

| Requirement type | Requirement | Source |
| :--- | :--- | :--- |
| Technical expertise |  |  |
| Compute or infrastructure |  |  |
| Account or access approval |  |  |
| Legal or license terms |  |  |
| Cost or fee |  |  |
| Security or privacy requirements |  |  |
| Other |  |  |

### 5.4 Dataset and Item Access

Purpose: record public, restricted, hidden, or unavailable access for data, prompts, answers, and rubrics.

| Component | Public | Restricted | Hidden | Not available | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Training or example data | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Development set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Test set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Private holdout set | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Prompt templates | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Reference answers | - [ ] | - [ ] | - [ ] | - [ ] |  |
| Rubrics | - [ ] | - [ ] | - [ ] | - [ ] |  |

### 5.5 Provenance and Contamination Documentation

Purpose: record provenance and contamination documentation only. It does not evaluate adequacy.

| Topic | Documented | Partially documented | Not documented | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Data source provenance | - [ ] | - [ ] | - [ ] |  |
| Collection procedure | - [ ] | - [ ] | - [ ] |  |
| Filtering or quality control | - [ ] | - [ ] | - [ ] |  |
| Licensing or rights | - [ ] | - [ ] | - [ ] |  |
| Deduplication | - [ ] | - [ ] | - [ ] |  |
| Contamination controls | - [ ] | - [ ] | - [ ] |  |
| Searchability or source-exposure checks | - [ ] | - [ ] | - [ ] |  |
| Canary, GUID, encryption, or anti-scraping method | - [ ] | - [ ] | - [ ] |  |
| Training-on-test diagnostic task | - [ ] | - [ ] | - [ ] |  |
| Public/private split rationale | - [ ] | - [ ] | - [ ] |  |
| Update or refresh policy | - [ ] | - [ ] | - [ ] |  |
| Release rules or anti-gaming terms | - [ ] | - [ ] | - [ ] |  |

### 5.6 Reproducibility Materials

Purpose: record materials that support independent inspection or reruns. Select all that are available.

- [ ] Complete evaluation code
- [ ] Scoring scripts
- [ ] Environment file or dependency list
- [ ] Container or reproducible runtime
- [ ] Prompt templates
- [ ] Example submissions
- [ ] Raw outputs from reported models
- [ ] Random seeds
- [ ] Configuration files
- [ ] Expected outputs or tests
- [ ] Result replication script
- [ ] Build status or continuous integration check
- [ ] None documented

Access or setup notes:

### 5.7 Maintenance and Versioning

Purpose: record current maintenance status, versioning, feedback channels, planned updates, and retirement or archival status.

| Prompt | Response |
| :--- | :--- |
| Current maintenance status |  |
| Latest documented release |  |
| Changelog available |  |
| Versioning scheme |  |
| Deprecated versions |  |
| Issue tracker or feedback channel |  |
| Response policy for user feedback |  |
| Known planned updates |  |
| Retirement or archival plan |  |
| Archival status |  |

---

# Part B. Evaluation of the Benchmark

Part B evaluates how well the benchmark supports its stated purpose and score interpretation. Use Part A evidence as the factual base. Add outside literature only when needed to interpret benchmark quality, and cite it in reviewer comments.

## Key to Ratings

| Rating | Explanation |
| :--- | :--- |
| `[n/a]` | This attribute is not applicable to this benchmark. |
| `0` | Not possible to rate because no, or insufficient, information is provided. |
| `1` | Inadequate. |
| `2` | Adequate. |
| `3` | Good. |
| `4` | Excellent. |

Reviewer comments should explain the evidence used, important missing evidence, and the reason for the rating. Missing documentation is an evidence gap, not proof of poor benchmark quality unless source-grounded evidence shows a defect. Do not mechanically average ratings.

---

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

This section evaluates whether the benchmark explains what it is designed to measure, why the task and metric are appropriate, how task or item content was developed, and whether documentation supports qualified use.

### 6.1 Rationale and Development

Overall rating for 6.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `6.1.1` | Rationale and construct definition |  |
| `6.1.2` | Summary of relevant research or evidence |  |
| `6.1.3` | Development procedure and task/item design |  |
| `6.1.4` | Content validity and task sampling |  |
| `6.1.5` | Item/task quality evidence and analysis |  |

Reviewer comments:

### 6.2 Documentation Available to Users

Overall rating for 6.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `6.2.1` | Explanation of rationale and intended measurement target |  |
| `6.2.2` | Explanation of development process |  |
| `6.2.3` | Explanation of scoring, metrics, and score interpretation |  |
| `6.2.4` | Explanation of reliability, validity, and limitations evidence |  |
| `6.2.5` | Clarity, currency, and accessibility of user documentation |  |

Reviewer comments:

### 6.3 Procedural Instructions

Overall rating for 6.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `6.3.1` | Administration or evaluation setup instructions |  |
| `6.3.2` | Scoring and result-production instructions |  |
| `6.3.3` | Interpretation and reporting instructions |  |
| `6.3.4` | Restrictions on use and qualified-user guidance |  |
| `6.3.5` | Technical support, references, and troubleshooting |  |

Reviewer comments:

### 6.4 Overall Adequacy of Rationale and Documentation

Overall rating for 6.4: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `6.4.1` | Overall adequacy of rationale, development, documentation, and task/item quality |  |

Reviewer comments:

---

## Section 7. Quality of Benchmark Materials and Usability

This section evaluates whether the benchmark materials can be obtained, understood, and used correctly.

### 7.1 Benchmark Materials and Interfaces

Overall rating for 7.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `7.1.1` | Dataset, task set, or environment availability |  |
| `7.1.2` | Prompt, instruction, rubric, and response-format quality |  |
| `7.1.3` | Evaluation harness, scorer, and implementation quality |  |
| `7.1.4` | Interface, tool, simulator, or environment material quality |  |
| `7.1.5` | Licensing, usage requirements, and sensitive-content notices |  |

Reviewer comments:

### 7.2 Usability and Accessibility

Overall rating for 7.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `7.2.1` | Ease of setup for intended users |  |
| `7.2.2` | Ease with which evaluated systems can provide required responses |  |
| `7.2.3` | Accessibility across relevant modalities, languages, and system types |  |
| `7.2.4` | Examples, quick starts, support paths, and troubleshooting |  |

Reviewer comments:

### 7.3 Overall Quality of Benchmark Materials

Overall rating for 7.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `7.3.1` | Overall quality of benchmark materials and usability |  |

Reviewer comments:

---

## Section 8. Baselines, Comparators, and Reference Interpretation

This section evaluates the reference points used to interpret benchmark scores: baselines, floors, ceilings, human or expert comparisons, model cohorts, and thresholds.

### 8.1 Baselines, Floors, Ceilings, and Thresholds

Overall rating for 8.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `8.1.1` | Random, chance, or trivial baselines |  |
| `8.1.2` | Floors, ceilings, saturation evidence, or refresh policy |  |
| `8.1.3` | Criterion thresholds or score bands |  |
| `8.1.4` | Link between reference points and intended interpretation |  |

Reviewer comments:

### 8.2 Human, Expert, and Model Comparators

Overall rating for 8.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `8.2.1` | Human baseline or comparison method |  |
| `8.2.2` | Expert baseline or expert-level claim support |  |
| `8.2.3` | Model comparator cohort selection |  |
| `8.2.4` | Model version, setting, and evaluation-condition documentation |  |

Reviewer comments:

### 8.3 Overall Adequacy of Reference Interpretation

Overall rating for 8.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `8.3.1` | Overall adequacy of baselines, comparators, and reference interpretation |  |

Reviewer comments:

---

## Section 9. Reliability, Precision, and Score Stability

This section evaluates whether scores are stable and precise enough for the intended use.

### 9.1 Run Stability and Uncertainty

Overall rating for 9.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `9.1.1` | Run-to-run stability, seeds, and stochastic settings |  |
| `9.1.2` | Score uncertainty, confidence intervals, or standard errors |  |
| `9.1.3` | Statistical comparison quality for reported differences |  |

Reviewer comments:

### 9.2 Scoring and Form Stability

Overall rating for 9.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `9.2.1` | Human rater, scorer, parser, or model-judge agreement |  |
| `9.2.2` | Prompt, form, version, and environment stability |  |
| `9.2.3` | Equivalence evidence across public/private splits or variants |  |

Reviewer comments:

### 9.3 Overall Reliability and Precision

Overall rating for 9.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `9.3.1` | Overall reliability, precision, and score stability |  |

Reviewer comments:

---

## Section 10. Validity Evidence

This section evaluates whether the evidence supports the intended interpretation of benchmark scores. The central validity question is whether the phenomenon-task-metric-claim chain is justified.

### 10.1 Construct Representation and Internal Structure

Overall rating for 10.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `10.1.1` | Content validity and task representativeness |  |
| `10.1.2` | Internal structure, subscores, or dimensionality |  |
| `10.1.3` | Coverage of intended domains, modalities, or sub-abilities |  |

Reviewer comments:

### 10.2 Metric, Scoring, and External Evidence

Overall rating for 10.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `10.2.1` | Metric, scorer, and aggregation validity |  |
| `10.2.2` | Relations with other benchmarks, humans, criteria, or realistic settings |  |
| `10.2.3` | Ecological or predictive relevance for intended use |  |

Reviewer comments:

### 10.3 Contamination, Gameability, and Claim Proportionality

Overall rating for 10.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `10.3.1` | Contamination, leakage, and gameability controls |  |
| `10.3.2` | Claim proportionality and broad-capability claims |  |
| `10.3.3` | Non-use cases and limits on score interpretation |  |

Reviewer comments:

### 10.4 Overall Validity Evidence

Overall rating for 10.4: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `10.4.1` | Overall validity evidence for intended score interpretation |  |

Reviewer comments:

---

## Section 11. Fair Use, Comparability, and Appropriate Use

This section evaluates whether benchmark use and interpretation are fair and comparable across relevant systems, modalities, domains, languages, access modes, and user contexts.

### 11.1 Fair and Comparable Evaluation Conditions

Overall rating for 11.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `11.1.1` | Cross-system and evaluation-condition comparability |  |
| `11.1.2` | Access, compute, tooling, and API/local comparability |  |
| `11.1.3` | Domain, language, modality, and subgroup coverage |  |

Reviewer comments:

### 11.2 Appropriate Use and Release Rules

Overall rating for 11.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `11.2.1` | Intended-use and restriction guidance |  |
| `11.2.2` | Release rules, anti-gaming rules, and sensitive-content warnings |  |
| `11.2.3` | Guidance for public, policy, product, or procurement interpretation |  |

Reviewer comments:

### 11.3 Overall Fair Use and Comparability

Overall rating for 11.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `11.3.1` | Overall fair use, comparability, and appropriate use |  |

Reviewer comments:

---

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

This section evaluates whether benchmark outputs communicate results accurately, clearly, and proportionally.

### 12.1 Report and Result Artifact Quality

Overall rating for 12.1: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `12.1.1` | Report, leaderboard, dashboard, or result artifact scope |  |
| `12.1.2` | Score granularity, uncertainty, and version labeling |  |
| `12.1.3` | Raw outputs, per-item data, or trace availability |  |

Reviewer comments:

### 12.2 Score-to-Claim Communication

Overall rating for 12.2: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `12.2.1` | Linkage from scores to public claims |  |
| `12.2.2` | Clarity about limitations, uncertainty, and update status |  |
| `12.2.3` | Audience-appropriate language and presentation |  |

Reviewer comments:

### 12.3 Overall Quality of Reports and Public Claims

Overall rating for 12.3: 

| Criterion | Name | Rating |
| :--- | :--- | :---: |
| `12.3.1` | Overall quality of reports, leaderboards, dashboards, and public claims |  |

Reviewer comments:


## Final Evaluation

### Evaluative Report of the Benchmark

Provide a concise, source-grounded judgment about the benchmark for its stated purpose. Identify strengths, evidence gaps, and appropriate-use limits. Do not mechanically average ratings; explain the judgment.

Draft:

### Conclusions

Summarize the quality of the benchmark as a measurement instrument, the uses it can support, the uses requiring caution, and the expertise needed to interpret it responsibly.

Draft:

### Summary of Ratings

| Section or area | Rating (`[n/a]`, `0`-`4`) | Reviewer comments | Critical evidence gap |
| :--- | :---: | :--- | :--- |
| Section 6. Rationale, documentation, and task/item quality |  |  |  |
| Section 7. Benchmark materials and usability |  |  |  |
| Section 8. Baselines and comparators |  |  |  |
| Section 9. Reliability and precision |  |  |  |
| Section 10. Validity evidence |  |  |  |
| Section 11. Fair use and comparability |  |  |  |
| Section 12. Reports, leaderboards, and public claims |  |  |  |
| Construct definition and claim scope |  |  |  |
| Scoring validity |  |  |  |
| Reproducibility and implementation transparency |  |  |  |
| Contamination and gameability controls |  |  |  |
| Maintenance and versioning |  |  |  |
| Overall claim-bounded measurement quality |  |  |  |

### Evidence Gap Register

| Evidence gap | Affected rating(s) | Why it matters | Evidence needed for a higher rating |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

### Reviewer Caution Statement

State the narrowest defensible interpretation of the benchmark scores, the main overclaim risks, and the conditions under which ratings should be revisited.

Draft:


---

## Appendix A. General Description of the Benchmark

Write a 200-600 word non-evaluative description of the benchmark. The description should summarize the benchmark's stated purpose, claimed capability domain, intended systems, intended users, task families, input and response formats, evaluation conditions, scoring procedure, reported outputs, available materials, versions or variants, and major documentation gaps.

Keep this appendix descriptive. Do not assign ratings, criticize design choices, or infer quality from missing evidence. Use wording such as "not documented in reviewed sources" when a factual detail is missing. If the benchmark makes broad claims such as general intelligence, agency, autonomy, or expert capability, describe the claim and the documented task evidence without evaluating whether the claim is justified.

Draft:



---

## Final Appendix. Template Validation Checklist

Use this checklist to validate an applied MESA review or a future template revision.

- [ ] EFPA traceability: every major EFPA Part B section 6-12 has a MESA equivalent.
- [ ] Literature coverage: each major benchmark-review criterion is linked to EFPA, BetterBench, Measuring what Matters, or AGI/CHC literature where relevant.
- [ ] Descriptive/evaluative separation: Part A contains no ratings and Part B contains no unsupported claims.
- [ ] Rating usability: each Part B rating has a reviewer comment explaining evidence, consequential gaps, and reasoning.
- [ ] Missing-evidence handling: missing documentation is treated as an evidence gap, not automatic proof of poor quality.
- [ ] Claim proportionality: broad intelligence, AGI, autonomy, agency, or cross-domain claims receive breadth/depth scrutiny.
- [ ] Reproducibility coverage: data, prompts, harness, scorer, environment, raw outputs, and versioning are considered.
- [ ] Contamination coverage: public/private split, searchability, canaries, release rules, and refresh policy are considered where applicable.
- [ ] Pilot fit: the template can express known issues without forcing false precision.
- [ ] Reviewer judgment: overall ratings are justified by evidence rather than mechanically averaged.
