# MESA Review: Humanity's Last Exam

Review status: full Part A + Part B MESA review  
Reviewed entity: finalized static Humanity's Last Exam benchmark, including the public 2,500-question release, documented private held-out set, official scoring materials, official reporting surfaces, and contextual HLE-Rolling/HLE-Verified materials where relevant  
Reviewer profile: `.codex/agents/benchmark-reviewer.md`  
Date of current review: 2026-05-17

## Source Registry

| ID | Source | Access date | Use in this review |
| :-- | :-- | :-- | :-- |
| S01 | HLE official site, [lastexam.ai](https://lastexam.ai/) | 2026-05-17 | Benchmark identity, public result surface, HLE-Rolling/current-status context, official links. |
| S02 | CAIS, [HLE GitHub repository](https://github.com/centerforaisafety/hle) | 2026-05-17 | Repository materials, MIT license, canary string, evaluation scripts, source links. |
| S03 | Phan et al., [Humanity's Last Exam](https://arxiv.org/abs/2501.14249), arXiv:2501.14249 and local transcription `literature/Humanitys_Last_Exam.md` | 2026-05-17 | Main benchmark paper, item construction, subject coverage, scoring, calibration, private-set rationale, caveats. |
| S04 | Phan et al., [Humanity's Last Exam](https://www.nature.com/articles/s41586-025-09962-4), Nature | 2026-05-17 | Peer-reviewed paper surface and later published version of the benchmark report. |
| S05 | Hugging Face, [cais/hle dataset](https://huggingface.co/datasets/cais/hle) | 2026-05-17 | Public dataset hosting, access terms, metadata, image/text fields, answer fields. |
| S06 | Scale AI / SEAL, [Humanity's Last Exam leaderboard page](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-05-17 | Official/partner reporting surface, score table, rank upper bound and calibration-oriented presentation. |
| S07 | CAIS, [simple-evals HLE evaluator](https://github.com/centerforaisafety/simple-evals) | 2026-05-17 | Current evaluator route and judge implementation context. |
| S08 | CAIS HLE repository, `hle_eval/run_model_predictions.py` | 2026-05-17 | Official answer/confidence prompting and prediction workflow. |
| S09 | CAIS HLE repository, `hle_eval/run_judge_results.py` | 2026-05-17 | Official model-judge scoring path and calibration-error computation. |
| S10 | CAIS HLE repository, [`hle-rolling-changes.txt`](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt) | 2026-05-17 | HLE-Rolling update context; not treated as the primary reviewed entity. |
| S11 | Shankar et al., [Humanity's Last Exam is Still Hard to Pass](https://arxiv.org/abs/2602.13964), arXiv:2602.13964 | 2026-05-17 | Supporting critique and HLE-Verified context; not official HLE source facts. |
| S12 | MESA template, `MESA EFPA template official.md` | 2026-05-17 | Required review structure, field guidance, rating style, checkboxes, and tables. |
| S13 | BetterBench, `literature/betterbench.md` | 2026-05-17 | Benchmark lifecycle, documentation, reproducibility, contamination, usability, and maintenance criteria. |
| S14 | Measuring what Matters, `literature/Measuring_what_Matters.md` | 2026-05-17 | Construct-validity chain: phenomenon, task, metric, claim. |
| S15 | A Definition of AGI, `literature/A_Definition_of_AGI.md` | 2026-05-17 | CHC/AGI breadth framing for broad intelligence and cognitive-domain cautions. |
| S16 | Repository report, `reports/benchmark_official_documentation_inventory.md` | 2026-05-17 | Local source-inventory starting point for HLE. |

## Short Stand-Alone Non-Evaluative Benchmark Description

Humanity's Last Exam (HLE) is a public benchmark of 2,500 difficult closed-ended academic questions across more than one hundred subjects. The paper describes HLE as a multimodal benchmark at the frontier of human knowledge, with multiple-choice and short-answer items suitable for automated grading, a private held-out set for overfitting checks, and official prompting that asks models for an explanation, final answer, and confidence. The strongest descriptive classification is expert-level closed-ended academic question answering, including a text-plus-image subset and calibration/error reporting.

# Part A. Description of the Benchmark

Part A is descriptive. It records what the available sources state or make inspectable. Evaluative judgments are reserved for Part B.

## Section 1. Factual Description

### 1.1 Review Administration

| Prompt | Description |
| :-- | :-- |
| Reviewer Name | MESA review generated under `.codex/agents/benchmark-reviewer.md`. |
| Date of Current Review | 2026-05-17 |
| Date of Previous Review _(if applicable)_ | n/a |

Reviewer comments: Full Part A + Part B review requested by the user. The review uses the active MESA template structure and preserves checkbox/table/rating formats where the template uses them [S12].

### 1.2 Benchmark Identity & Provenance

| Prompt | Description |
| :-- | :-- |
| Reviewed Entity Name | Humanity's Last Exam, finalized static public benchmark release. |
| Short Name / Acronym | HLE |
| Entity Type | Original AI benchmark with a public dataset, official evaluation scripts, partner leaderboard/reporting surfaces, and a documented private held-out set. |
| Parent / Source Benchmark | n/a. HLE is not a derived subset of another benchmark, although the paper positions it relative to saturated academic benchmarks such as MMLU and GPQA [S03]. |
| Exact Version / Release Split | Finalized static HLE public set of 2,500 questions, with a private held-out set documented for overfitting/gaming checks. HLE-Rolling is treated as contextual, not the reviewed entity [S03, S10]. |
| Implementation / Scorer Version | Official CAIS HLE repository as accessed on 2026-05-17, including `hle_eval` scripts. Paper evaluation used a standardized answer/confidence prompt and an o3-mini-2025-01-31 judge; current simple-evals materials provide a maintained evaluator route [S02, S07, S08, S09]. |
| Creators & Current Maintainers | Organizing team led by Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, Michael Choi, Anish Agrawal, Arnav Chopra, Adam Khoja, Ryan Kim, Richard Ren, Jason Hausenloy, Oliver Zhang, Mantas Mazeika, Summer Yue, Alexandr Wang, and Dan Hendrycks; CAIS and Scale AI are the principal organizing/maintaining institutions in official materials [S03]. |
| Host Organization / Repository Owner | Center for AI Safety / `centerforaisafety` GitHub organization; dataset hosted on Hugging Face as `cais/hle`; result surface hosted by Scale/SEAL [S02, S05, S06]. |
| Release Dates | Initial public release is documented in early 2025 sources; the paper's arXiv record is 2025-01-23 and the Nature publication is 2025 [S03, S04]. |
| License & Access Terms | GitHub repository specifies MIT license. Hugging Face dataset access is public but requires accepting dataset terms/contact sharing before access; private held-out items are not public [S02, S05]. |
| Persistent Identifier / DOI / Citation | arXiv:2501.14249; Nature article page for the peer-reviewed version [S03, S04]. |

Reviewer comments: The reviewed entity is the static finalized HLE release. HLE-Rolling, HLE-Verified, and third-party result surfaces are context for lifecycle and criticism, not the primary benchmark entity.

### 1.3 Materials, Sources, & Access Tracking

| Material / Source Type | URL, Location, or Identifier | Access Date |
| :-- | :-- | :-- |
| Paper / Technical Report | https://arxiv.org/abs/2501.14249 and https://www.nature.com/articles/s41586-025-09962-4 | 2026-05-17 |
| Website / Documentation Hub | https://lastexam.ai/ | 2026-05-17 |
| Code Repository | https://github.com/centerforaisafety/hle | 2026-05-17 |
| Dataset / Task / Prompt Set | https://huggingface.co/datasets/cais/hle | 2026-05-17 |
| Evaluation Harness / Runner | `hle_eval` in the HLE repository; https://github.com/centerforaisafety/simple-evals | 2026-05-17 |
| Leaderboard / Results Portal | https://labs.scale.com/leaderboard/humanitys_last_exam | 2026-05-17 |
| Guides _(User/Scoring/Rubric)_ | Paper appendices and `hle_eval` scripts in the HLE repository | 2026-05-17 |
| Changelog / Release Logs | https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt | 2026-05-17 |
| Official Announcements | Official HLE site and repository links | 2026-05-17 |
| Contextual Literature | BetterBench, Measuring what Matters, A Definition of AGI, HLE-Verified | 2026-05-17 |
| Feedback / Contact Channels | GitHub issues and Hugging Face dataset contact/access workflow | 2026-05-17 |

Reviewer comments: Official HLE facts come first from the paper, official site, repository, dataset card, and official/partner result surface. HLE-Verified is used only as supporting critique for item-quality risk and not as a replacement for official HLE documentation.

## Section 2. Classification

### 2.1 Claimed Capability Domains

Specify the capabilities, phenomena, or qualities the benchmark claims to measure.

- [ ] Not explicitly stated
- [x] General Knowledge (K)
- [x] Reading and Writing Ability (RW)
- [x] Mathematical Ability (M)
- [x] On-the-Spot Reasoning (R)
- [ ] Working Memory (WM)
- [ ] Long-Term Memory Storage (MS)
- [x] Long-Term Memory Retrieval (MR)
- [x] Visual Processing (V)
- [ ] Auditory Processing (A)
- [ ] Speed (S)
- [x] Coding or software engineering
- [x] Specialized scientific or technical expertise
- [x] Domain-specific professional expertise
- [ ] Tool use
- [ ] Agency or autonomy
- [ ] Web or browser interaction
- [ ] Embodied or simulated environment interaction
- [x] Factuality or grounding
- [ ] Multilingual or cross-cultural capability
- [ ] Safety, refusal, or policy compliance
- [ ] Robustness
- [x] Calibration or uncertainty

Reviewer comments: Basis: HLE is described as broad closed-ended academic question answering across many subjects, including mathematics, humanities, natural sciences, computer science/AI, medicine, engineering, and image-conditioned questions [S03]. Calibration is directly elicited through confidence scores and reported through RMS calibration error [S03, S08, S09]. Caution: these boxes classify HLE's task demands and claims; they do not imply HLE covers the full breadth of general intelligence or autonomous research.

### 2.2 Area of Use

Select all documented use contexts.

- [ ] Not explicitly stated
- [x] Model comparison
- [x] Leaderboard ranking
- [x] Capability profiling
- [x] Research diagnostics
- [x] Safety evaluation
- [ ] Deployment gating
- [ ] Procurement or vendor comparison
- [ ] Internal regression testing
- [x] Public communication or marketing
- [x] Policy or governance analysis

Reviewer comments: Basis: HLE is presented as a common reference point for scientists, policymakers, and the public to assess frontier model capabilities on difficult closed-ended academic questions [S03]. Caution: no official deployment-gating or procurement threshold was identified.

### 2.3 Intended AI Systems

Only record systems stated or clearly implied by benchmark documentation.

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
- [x] Open-weight local models
- [x] API-hosted models

Reviewer comments: Basis: the paper evaluates frontier LLMs and multimodal models, while non-multimodal models are evaluated on the text-only subset [S03]. The official scripts support API/provider-style model calls and local output processing [S02, S07, S08, S09]. Caution: HLE is not an agent, tool-use, or retrieval benchmark unless a third-party evaluator changes the administration conditions.

### 2.4 Intended Users of Benchmark Outputs

Select all that apply.

- [ ] Not explicitly stated
- [x] Benchmark creators or maintainers
- [x] AI researchers
- [x] Model developers
- [ ] Product teams
- [x] Safety evaluators
- [x] Policy or governance actors
- [ ] Procurement or enterprise decision-makers
- [x] Educators or academic reviewers
- [x] Public leaderboard users

Reviewer comments: Basis: the paper explicitly frames HLE as useful for research, governance, and public understanding of model capabilities [S03]. Caution: public leaderboard users need stronger caveats than expert reviewers because the score is easy to overread as a broad capability or AGI proxy.

### 2.5 Task Families, Subdomains, and Scores

| Component | Description |
| :-- | :-- |
| Capability, phenomenon, or quality the benchmark claims to measure | Advanced closed-ended academic capabilities at the frontier of human knowledge, including difficult expert questions across many academic domains [S03]. |
| Definition of the capability or quality being measured | The paper operationalizes the target through precise, unambiguous, verifiable questions that require graduate-level or highly specialized knowledge and cannot be quickly answered by simple internet retrieval [S03]. |
| Subcomponents of the claimed capability, phenomenon, or quality | Mathematics, humanities, natural sciences, computer science/AI, medicine/biology, chemistry, engineering, social science, and many other subject labels; text-only and text-plus-image forms; multiple-choice and exact-match short-answer forms [S03, S05]. |
| Excluded scope or non-target abilities | Open-ended research, autonomous research capability, agency, long-horizon planning, tool use, web search, audio/video understanding, embodied interaction, and full AGI/general intelligence are not directly tested by the static HLE task format [S03, S15]. |
| Benchmark item, prompt, episode, environment, or interaction families or subdomains | Each item is an academic question with an answer specification; approximately 24% are multiple choice and the rest are exact-match/short-answer; approximately 14% require both text and image comprehension [S03]. |
| Sources for benchmark items, prompts, episodes, environments, or interactions | Global expert contributors, mostly professors, researchers, and graduate degree holders; original work or non-trivial syntheses of published information; each submission included a question, answer specification, solution rationale, subject, and contributor identity/affiliation [S03]. |
| Sampling method for benchmark items, prompts, episodes, environments, or interactions | Curated expert submission, model-difficulty screening, multi-stage expert review, organizer approval, community feedback, audits, and searchability checks rather than random sampling from a defined universe of academic tasks [S03]. |
| Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions | Submissions were screened for model difficulty, closed-endedness, precision, non-searchability, unambiguous answers, and expert/organizer approval; some post-release issues were handled through bug bounty and audit processes [S03]. |
| Splits or partitions | Public 2,500-question release plus a private held-out set documented for overfitting and public-benchmark gaming checks; HLE-Rolling is a dynamic fork and is not the primary entity reviewed here [S03, S10]. |
| Primary score | Accuracy: proportion of questions judged correct [S03, S06, S09]. |
| Subscores | Category/subject-level results and text-only versus multimodal distinctions are discussed in official materials; the dataset includes subject/category metadata [S03, S05]. |
| Derived scores or scores combined from item, task-family, or subscore results | RMS calibration error is reported from model confidence and correctness; the Scale/SEAL surface also presents rank-related metrics such as upper-bound presentation [S03, S06, S09]. |
| Qualitative score ranges such as low/medium/high or novice/expert | No stable qualitative bands were identified. The paper cautions that small inflections near the low-score floor are not strongly indicative of progress [S03]. |
| Boundaries or caveats for interpretations made from benchmark scores | The paper states that high HLE accuracy would suggest expert-level performance on closed-ended, verifiable academic questions, but not autonomous research capability or AGI by itself [S03]. |

Reviewer comments: HLE's core phenomenon-task-metric-claim chain is relatively clear for difficult closed-ended academic question answering. Its broader public name and frontier framing require Part B claim-proportionality review.

### 2.6 Model Response Mode

- [ ] Not explicitly stated
- [x] Multiple choice
- [x] Short text
- [ ] Long-form text
- [ ] Structured output, such as JSON or XML
- [ ] Code
- [x] Mathematical expression
- [ ] Tool call
- [ ] Browser or web action
- [ ] File, document, or other output generation
- [ ] Image output
- [ ] Audio output
- [ ] Video output
- [ ] Interaction in a simulated environment
- [ ] Interaction in a real or external environment

Reviewer comments: Basis: HLE uses multiple-choice answers and exact-match/short-answer final responses, often including mathematical notation or concise technical expressions [S03, S05, S08]. Explanation text is elicited but the scored response is the final answer judged against the answer key [S08, S09].

### 2.7 Prerequisites for Evaluated Systems

| Requirement | Irrelevant or not necessary | Necessary information given | Information missing |
| :-- | :--: | :--: | :--: |
| Language support | [ ] | [x] | [ ] |
| Context length | [ ] | [ ] | [x] |
| Multimodal input support | [ ] | [x] | [ ] |
| Structured output support | [ ] | [x] | [ ] |
| Exact format, schema, or parser compatibility | [ ] | [x] | [ ] |
| Retry, repair, or correction-loop support for malformed outputs | [x] | [ ] | [ ] |
| Tool access | [x] | [ ] | [ ] |
| Browser or internet access | [x] | [ ] | [ ] |
| Code execution | [x] | [ ] | [ ] |
| External API or tool credentials | [ ] | [x] | [ ] |
| Memory or persistent state | [x] | [ ] | [ ] |
| Environment, simulator, or task-registry compatibility | [x] | [ ] | [ ] |
| API compatibility | [ ] | [x] | [ ] |
| Latency or time budget | [x] | [ ] | [ ] |
| Cost or compute budget | [ ] | [ ] | [x] |

Reviewer comments: Full HLE requires English text comprehension and multimodal image support for the image subset. The official prompt gives a required answer/confidence format [S08]. Text-only results for non-multimodal systems are documented, but full comparability between text-only and multimodal runs requires clear subset labels [S03].

### 2.8 Evaluation Conditions

| Condition | Description |
| :-- | :-- |
| Prompting protocol | Official paper and repository use a standardized prompt asking for `Explanation`, `Answer`, and `Confidence` from 0% to 100% [S03, S08]. |
| System prompt | Paper says models that do not support a system prompt receive the instruction as a separate user prompt [S03]. |
| Few-shot examples | No official few-shot examples were identified for the primary HLE evaluation prompt [S03, S08]. |
| Sampling settings | The repository prediction script exposes model and sampling configuration, but the public review did not identify a complete reproducibility table for every published model run [S08]. |
| Tool permissions | The static HLE evaluation is closed-book and does not require web, browser, external tools, code execution, or retrieval. Searchability checks were used in benchmark construction, not as a normal model-evaluation condition [S03]. |
| Tool/API credential policy | Users running scripts must provide API credentials for the models they evaluate; dataset access may require accepting Hugging Face terms [S05, S08]. |
| Time limits | No per-question or full-run time limit was identified for public evaluation. |
| Human intervention rules | Official model evaluation is automated; human review was part of item construction, audit, and correction, not normal model answering [S03]. |
| Official rerun, retry, or repair policy | No standardized retry/repair policy for malformed model answers was identified beyond the judge/parser behavior [S09]. |
| Hardware or hosted service | No required hardware for scoring public outputs; API-hosted evaluation depends on provider access [S08]. |
| Network requirements | Internet/API access is needed to call hosted models during evaluation, but the task itself is not a web/search task [S08]. |
| Sandbox or security constraints | No required sandbox was identified for the static benchmark. |
| Model identity and version-label requirements | Paper tables identify specific model names and versions where available; consistent public result labeling depends on the reporting surface [S03, S06]. |
| Special administration conditions | Non-multimodal systems may be evaluated on the text-only subset, and HLE-Rolling/current results should be labeled separately from the finalized static set [S03, S10]. |

Reviewer comments: The main administration condition is the answer/confidence prompt plus automated judging. Exact replication of published results requires the precise model version, API behavior, sampling settings, prompt placement, dataset version, and judge model.

### 2.9 Task Interaction and Observable Evidence Types

Selection or judgment tasks:

- [x] Multiple choice, single correct answer
- [ ] Multiple choice, multiple correct answers
- [ ] Ranking
- [ ] Classification
- [ ] Pairwise preference

Production or construction tasks:

- [x] Open-ended text
- [ ] Code generation
- [ ] Proof, derivation, or explanation
- [ ] Structured data
- [ ] Generated media
- [ ] Deliverable production
- [ ] Patch or repository modification
- [ ] Coordinate, bounding target, or GUI-grounding target
- [ ] Document parsing, layout reconstruction, or OCR-style extraction

Interaction or environment tasks:

- [ ] Tool use
- [ ] Browser or web navigation
- [ ] API interaction
- [ ] Computer-use interaction
- [ ] Simulated environment task
- [ ] Real or external environment task
- [ ] Terminal, shell, or filesystem task
- [ ] User-simulator interaction
- [ ] Long-horizon episode or stateful task

Observable evidence or process data:

- [ ] Response latency
- [ ] Token usage
- [ ] Cost
- [ ] Tool traces
- [ ] Search or retrieval transcript
- [ ] User-simulator actions
- [x] Intermediate reasoning traces
- [x] Execution logs
- [ ] Unit-test, patch, or verifier result
- [ ] Environment or simulator state
- [x] Leaderboard submission metadata
- [x] Raw output or audit trace under controlled access

Reviewer comments: The official prompt asks for explanation and confidence, but the explanation is not the primary scored object [S08, S09]. Raw model outputs can be collected by the scripts, but comprehensive public raw-output access for all official results was not identified.

### 2.10 Input Stimulus Type

- [ ] Not explicitly stated
- [x] Text
- [ ] Code
- [ ] Tables or structured data
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

Reviewer comments: Basis: HLE includes text-only questions and a text-plus-image subset. The paper reports about 14% image-conditioned items [S03].

### 2.11 Number of Items or Measurement Points

| Prompt | Response |
| :-- | :-- |
| Total public items or tasks | 2,500 public questions [S03, S05]. |
| Total private or hidden items | Private held-out set documented, count not clearly public in the primary sources reviewed [S03]. |
| Development or example items | Public dataset can be used for public evaluation; no separate train/dev split was identified for the finalized static set. |
| Test items | 2,500 public items in the static public release; private held-out set used for overfitting checks where available [S03]. |
| Dynamic or generated tasks | n/a for static HLE. HLE-Rolling is a separate dynamic fork/context [S10]. |
| Episodes, trials, or measurement points | One model answer per question in the standard evaluation path, plus confidence; repeated runs are possible but not a standard published unit [S08, S09]. |
| Counts by split, form, or variant | Public 2,500; private held-out set count unresolved; HLE-Rolling is separate. |
| Counts by language, culture, or locale | English questions; no full multilingual count identified. |
| Counts by claimed capability domain | The paper reports top subject categories and broad subject coverage across more than one hundred subjects; full count table by every capability-domain mapping is not a MESA-native evidence source [S03]. |
| Counts by context-length bin | Not documented in reviewed sources. |
| Counts by difficulty band | Items were selected for frontier-model difficulty, but no stable ordinal difficulty-band count was identified [S03]. |
| Counts by public, private, hidden, or controlled-access status | 2,500 public; private held-out set documented but not publicly inspectable [S03, S05]. |
| Item count uncertainty | Public count is stable at 2,500 for the reviewed static release. Private held-out count remains unresolved from inspected public sources. |

Reviewer comments: The public item count is clear. The private held-out set is described, but public documentation of its exact count, access process, and score use is less complete.

### 2.12 Mode of Evaluation

- [ ] Not indicated
- [x] Local batch evaluation
- [ ] Hosted benchmark platform
- [x] Leaderboard submission
- [x] Private controlled evaluation
- [x] Public open evaluation
- [ ] Interactive agent evaluation
- [ ] Human-in-the-loop evaluation
- [x] Continuous or rolling evaluation
- [ ] Benchmark suite or sub-leaderboard
- [ ] Competition or challenge submission
- [x] Third-party evaluator implementation
- [ ] Registry-hosted task pack

Control of evaluated systems:

- [x] No control over submitted systems
- [x] Some control over submitted systems
- [ ] Controlled model access or audit
- [x] Controlled evaluation center or private harness
- [ ] Not documented

Reviewer comments: Public HLE can be evaluated locally or through maintained evaluator scripts. HLE-Rolling and Scale/SEAL result surfaces are contextual reporting/evaluation routes, not the core reviewed static dataset [S06, S07, S10].

### 2.13 Technological Arrangements

| Technology | A | R |
| :-- | :-: | :-: |
| API access | [x] | [ ] |
| Local inference | [x] | [ ] |
| GPU | [ ] | [ ] |
| CPU-only execution | [x] | [ ] |
| Docker or container | [ ] | [ ] |
| Python package or CLI | [x] | [x] |
| Browser | [ ] | [ ] |
| External tools | [ ] | [ ] |
| Internet access | [x] | [ ] |
| Proprietary platform | [x] | [ ] |
| Hosted scoring service | [x] | [ ] |
| Benchmark registry or task environment | [ ] | [ ] |

Reviewer comments: A = available route; R = required route. Public scoring can be done with scripts once model outputs exist, while producing model outputs requires whatever API/local model route the evaluator chooses [S08, S09].

### 2.14 Time and Resource Requirements

| Resource or burden | Description |
| :-- | :-- |
| Model inference or task completion | Depends on model, provider, reasoning setting, and full versus text-only subset. No universal runtime budget was identified. |
| Scoring | Automated judge scoring requires calling the judge model for exact-match equivalence on short-answer outputs, unless an evaluator substitutes a deterministic scorer for multiple-choice/exact cases [S09]. |
| Human adjudication | Human expert review and audit were part of benchmark construction and correction; not required for ordinary public model evaluation [S03]. |
| Full benchmark run | Full public run covers 2,500 questions and may be costly for frontier API models. Exact cost depends on provider/model settings and judge use [S08, S09]. |

Reviewer comments: HLE is easy to understand as a dataset but can be expensive to run at scale with frontier models, especially if explanations and judge calls are retained.

### 2.15 Benchmark Forms, Versions, and Variants

| Form, version, or variant | Description |
| :-- | :-- |
| HLE static public set | Reviewed primary entity: public 2,500-question dataset [S03, S05]. |
| HLE private held-out set | Documented private set to assess overfitting and gaming on the public benchmark; not inspectable in reviewed public materials [S03]. |
| HLE-Rolling | Dynamic fork intended to address feedback and add questions over time; update log exists [S10]. |
| HLE-Verified | Independent/supporting critique and revised/verified subset proposal; not official HLE source facts for this review [S11]. |
| Third-party leaderboards/evaluators | Treated as contextual unless they document a specific HLE implementation under review [S06, S07]. |

Reviewer comments: Results should be labeled by form/version. Static HLE, HLE-Rolling, HLE-Verified, and any evaluator-specific HLE slice should not be conflated.

### 2.16 Static or Dynamic Task Determination

| Determination question | Response |
| :-- | :-- |
| Static or dynamic? | Static for the reviewed HLE public set; dynamic for HLE-Rolling context. |
| Who determines items? | Original HLE organizers, expert contributors, reviewers, auditors, and maintainers determined the static set [S03]. |
| Item-generation route | Expert-submitted questions filtered through model-difficulty checks and human review, not runtime generation [S03]. |
| Update route | HLE-Rolling is regularly updated with public change notes; static HLE should be treated as a fixed release unless a source explicitly says otherwise [S10]. |

Reviewer comments: The static release supports stable reproduction but increases public-exposure and contamination risk over time. HLE-Rolling mitigates some staleness while reducing direct temporal comparability.

### 2.17 Evidence Sources Used in Scoring

| Evidence source | Description |
| :-- | :-- |
| Reference answers | Public dataset includes correct answer information for public items [S05]. |
| Model final answer | Official prompt asks for final answer in a fixed field [S08]. |
| Model confidence | Official prompt asks for confidence from 0% to 100%; judge extracts confidence, using 100 if no confidence is available [S08, S09]. |
| Model explanation | Elicited as part of the prompt, but scoring focuses on answer equivalence [S08, S09]. |
| Judge model output | Judge extracts final answer, reasoning, correctness, and confidence for scoring [S09]. |
| Human review/audit evidence | Used for item development, quality control, and post-release correction, not ordinary run-time scoring [S03]. |

Reviewer comments: Scoring is not purely deterministic for all items because short-answer equivalence is mediated by a model judge. Multiple-choice scoring is simpler, but the official evaluation path still uses structured extraction/judging.

### 2.18 Broad-Claim Flags for Later Evaluation

| Broad-claim field | Descriptive record |
| :-- | :-- |
| Broad terms used | Frontier human knowledge, broad academic capabilities, expert-level academic questions, model capabilities, research and policymaking, and public understanding of AI progress [S03]. |
| Stated AGI, autonomy, or agency caveats | The paper states that high HLE accuracy would not alone suggest autonomous research capability or AGI [S03]. |
| Capability domains directly sampled | Closed-ended academic knowledge, reasoning, problem solving, short-answer/multiple-choice response, some image-conditioned understanding, and confidence calibration. |
| Capability domains not directly sampled | Long-horizon agency, autonomous research workflow, tool use, web search, planning across environments, long-term memory storage, auditory processing, embodied action, and many CHC-style broad/narrow abilities [S15]. |
| Public interpretation risk | The name "Humanity's Last Exam" and frontier framing can invite broader claims than the task format supports. |
| Part B implication | Validity review should distinguish "expert-level closed-ended academic question answering under HLE conditions" from AGI, autonomous research, or broad cognitive versatility. |

Reviewer comments: Broad-claim analysis is required even though the HLE paper includes explicit caveats, because public score surfaces and the benchmark name can still encourage overgeneralization.

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

| Scoring component | Description |
| :-- | :-- |
| Response collection | Model is prompted to provide explanation, answer, and confidence [S08]. |
| Answer extraction | Judge extracts the final exact answer; if no exact final answer is extractable, the judge can record `None` [S09]. |
| Correctness decision | Judge compares the extracted final answer to the correct answer and marks correct yes/no, allowing only meaningful equivalence or small numerical tolerance where appropriate [S09]. |
| Confidence extraction | Judge extracts confidence from the model response, and uses 100 when no confidence is available [S09]. |
| Aggregate accuracy | Correct answers divided by total questions evaluated [S03, S09]. |
| Calibration error | RMS calibration error computed from confidence and correctness [S03, S09]. |

Reviewer comments: The scoring procedure is well documented at the prompt/judge level, but model-judge validation remains an important evaluative issue for Part B.

### 3.2 Scores and Metrics

| Score or metric | Description |
| :-- | :-- |
| Accuracy | Main score: proportion/percentage of questions judged correct [S03, S06, S09]. |
| RMS calibration error | Calibration metric comparing stated confidence to observed correctness [S03, S09]. |
| Category-level accuracy | Paper reports accuracy by category/subject group in supplementary materials [S03]. |
| Text-only subset accuracy | Used for models that are not multimodal and for subset comparison [S03]. |
| Rank or rank upper bound | Scale/SEAL surface reports leaderboard/rank-oriented results and uncertainty-oriented upper-bound information [S06]. |

Reviewer comments: Accuracy is interpretable for closed-ended items. Calibration error is a useful second metric because HLE is designed to reveal confident wrong answers.

### 3.3 Scale or Metric Types

| Metric | Scale type | Notes |
| :-- | :-- | :-- |
| Accuracy | Bounded proportion/percentage | 0%-100%, simple aggregate over evaluated items [S09]. |
| RMS calibration error | Bounded error percentage | Lower is better; depends on confidence extraction and correctness labels [S09]. |
| Subject/category accuracy | Bounded proportion/percentage | Depends on category metadata and item counts [S03, S05]. |
| Rank | Ordinal | Depends on reporting surface, model cohort, and date [S06]. |

Reviewer comments: The paper cautions that low-score floor effects mean small inflections near zero should not be overinterpreted [S03].

### 3.4 Score Transformation

| Transformation | Description |
| :-- | :-- |
| Accuracy aggregation | Simple mean/proportion of correct items. |
| Calibration aggregation | RMS calibration error over confidence/correctness pairs [S09]. |
| Confidence interval / upper-bound reporting | Official/partner reporting surfaces include uncertainty-oriented presentation for leaderboard interpretation [S06]. |
| Norming or psychometric scaling | No IRT, normed score, equating model, or formal psychometric scale transformation identified. |

Reviewer comments: HLE's primary score is easy to compute and explain, but its meaning still depends on item quality, judge reliability, and construct scope.

### 3.5 Documented Reference Groups, Baselines, and Comparators

| Comparator type | Documentation |
| :-- | :-- |
| Frontier model cohort | Paper reports multiple frontier model results and calibration errors, including text-only handling for non-multimodal models [S03]. |
| Chance/random baseline | Multiple-choice items have an implicit chance floor from five or more answer choices; exact-match items have no meaningful simple random baseline [S03]. |
| Expert human frontier | Item development relies on expert contributors/reviewers and questions are intended to require graduate-level or specialized expertise [S03]. |
| Saturated benchmark context | Paper compares motivation to MMLU and other saturated benchmarks [S03]. |
| Public current leaderboard cohort | Scale/SEAL page reports current model results and rank-oriented outputs as a public reporting surface [S06]. |
| HLE-Verified critique | Independent paper proposes a verified/revised subset and reports item-quality concerns, used here as supporting critique [S11]. |

Reviewer comments: HLE has strong model-comparator evidence and expert-development evidence. It has weaker direct human-performance baseline evidence than benchmarks with a complete controlled human solve cohort.

### 3.6 Score Uncertainty and Stability

| Topic | Description |
| :-- | :-- |
| Model stochasticity | Paper notes non-determinism and low but non-zero accuracy near the floor [S03]. |
| Confidence intervals | Repository scoring includes a Wald 95% half-width calculation, and the Scale/SEAL reporting surface includes uncertainty-oriented rank presentation [S06, S09]. |
| Run-to-run variance | No comprehensive repeated-run variance or seed-sensitivity table was identified for the published model cohort. |
| Judge stability | Judge model and prompt are documented, but systematic model-judge reliability/validation evidence is limited in reviewed official materials [S09]. |
| Item disagreement | Paper reports estimated expert disagreement rates from audits, including 15.4% for the public set and about 18% for a biology/chemistry/health subset [S03]. |

Reviewer comments: HLE acknowledges item and score uncertainty more than many benchmarks, but the official reproducibility package does not fully resolve run variance, judge variance, or fine-grained comparison uncertainty.

### 3.7 Documented Metric Rationale and Stated Score Interpretation

| Metric rationale field | Description |
| :-- | :-- |
| Accuracy rationale | Closed-ended questions with known answers make accuracy a plausible primary metric [S03]. |
| Calibration rationale | Low performance with high confidence is treated as important evidence of hallucination/confabulation risk [S03]. |
| Model-judge rationale | Short-answer equivalence requires more flexible checking than strict string equality, motivating model-judge extraction/equivalence checks [S09]. |
| Stated interpretation | High HLE accuracy supports claims about expert-level closed-ended academic question answering, not AGI or autonomous research by itself [S03]. |

Reviewer comments: The phenomenon-task-metric chain is strongest for "difficult closed-ended academic question answering under HLE prompt and scoring conditions."

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

| Output record | Availability |
| :-- | :-- |
| Paper result tables | Public in paper/arXiv/Nature [S03, S04]. |
| Dataset and public answer keys | Public through Hugging Face after access terms [S05]. |
| Official scripts | Public in HLE repository [S02, S08, S09]. |
| Current result/leaderboard surface | Public through Scale/SEAL HLE page [S06]. |
| Raw outputs for all published evaluations | Not comprehensively identified as public. |

Reviewer comments: Users can compute their own outputs, but fully reproducing every published score requires model access, version details, API behavior, and judge configuration.

### 4.2 Output Name or Description

| Output name | Description |
| :-- | :-- |
| HLE accuracy | Percentage/proportion of public or specified subset questions answered correctly [S03, S09]. |
| RMS calibration error | Calibration error from confidence and correctness [S03, S09]. |
| Category result | Accuracy by subject/category where reported [S03]. |
| Text-only result | Score on text-only subset, especially for non-multimodal models [S03]. |
| Leaderboard rank / rank upper bound | Public result ordering and uncertainty-oriented rank interpretation on Scale/SEAL surface [S06]. |

Reviewer comments: Output names must include dataset/form and modality/subset labels to avoid mixing static HLE, HLE-Rolling, and text-only/multimodal conditions.

### 4.3 Output Design or Presentation

| Design element | Description |
| :-- | :-- |
| Paper tables | Report model accuracy and calibration error, including text-only notes for non-multimodal models [S03]. |
| Public leaderboard | Shows current model results and rank-oriented information [S06]. |
| Repository scripts | Produce correctness and calibration outputs from model predictions and judge results [S08, S09]. |
| Dataset host | Provides item data and metadata for public evaluation [S05]. |

Reviewer comments: HLE output presentation is stronger when accuracy and calibration are read together. Accuracy-only reporting loses a major part of HLE's intended interpretation.

### 4.4 Output Structure

| Field | Description |
| :-- | :-- |
| Item-level model response | Explanation, answer, confidence generated under official prompt [S08]. |
| Item-level judge output | Extracted answer, judge reasoning, correctness, confidence extraction [S09]. |
| Aggregate report | Accuracy and calibration error, plus confidence interval helper in the repository scorer [S09]. |
| Public result surface | Leaderboard/rank-oriented model comparison [S06]. |

Reviewer comments: The template for output structure is clear in code, but raw outputs and judge rationales for all official published runs are not uniformly public.

### 4.5 Sensitivity to Context

| Context factor | Why it matters |
| :-- | :-- |
| Model version and provider behavior | Frontier models change rapidly and may not be reproducible under the same name. |
| Prompt placement | Paper notes system prompt fallback as user prompt for models without system-prompt support [S03]. |
| Sampling settings | Temperature/seed/provider settings can affect answer and confidence outputs. |
| Multimodal support | Full HLE and text-only HLE are not the same evaluation [S03]. |
| Judge model/version | Correctness and confidence extraction depend on the judge model and prompt [S09]. |
| Public exposure | Public 2,500-question release increases contamination risk over time [S03, S05]. |

Reviewer comments: HLE score interpretation is sensitive to both test form and evaluation implementation. Results should state all run conditions.

### 4.6 Development of Outputs

| Output-development component | Description |
| :-- | :-- |
| Accuracy | Developed from closed-ended answer specifications and automated judge checks [S03, S09]. |
| Calibration | Developed from official confidence prompt and RMS calibration error computation [S03, S09]. |
| Category/subset outputs | Supported by dataset subject/category metadata and paper-level reporting [S03, S05]. |
| Leaderboard outputs | Maintained through Scale/SEAL result surface and related reporting [S06]. |

Reviewer comments: Output development is tied to the paper's central claim that HLE should reveal both low accuracy and overconfidence on frontier expert questions.

### 4.7 Modifiability

| Output element | Modifiability |
| :-- | :-- |
| Local reports | Users can modify local evaluation scripts and reporting from public outputs [S02]. |
| Public dataset | Static public dataset should not be silently modified if used for comparable HLE scores. |
| Official/partner leaderboard | Controlled by maintainers/operators [S06]. |
| HLE-Rolling | Intended to change over time and must be labeled as rolling [S10]. |

Reviewer comments: Modifiability supports experimentation but makes score labels and version control critical.

### 4.8 Documented Linkage Status Between Tasks, Scoring, and Report Labels

| Linkage | Status |
| :-- | :-- |
| Task to score | Clear: item answer compared to reference answer through judge/scorer [S09]. |
| Score to academic QA interpretation | Strongly documented for difficult closed-ended academic questions [S03]. |
| Score to calibration interpretation | Documented through confidence prompt and RMS calibration error [S03, S09]. |
| Score to AGI/autonomous research | Explicitly limited by the paper's caveat; not supported as a direct inference [S03, S15]. |
| Static HLE to HLE-Rolling | Needs explicit labeling; rolling updates are not directly interchangeable with static HLE [S10]. |

Reviewer comments: The narrow score linkage is defensible. Broad capability linkage requires caveats and additional evidence.

### 4.9 Output Content

| Content type | Included or documented |
| :-- | :-- |
| Aggregate accuracy | Yes [S03, S06, S09]. |
| Calibration error | Yes [S03, S09]. |
| Subject/category results | Yes in paper/supporting materials [S03]. |
| Text-only/multimodal distinction | Yes [S03]. |
| Confidence intervals/uncertainty | Partially: repository scorer and result surface support some uncertainty-oriented presentation [S06, S09]. |
| Raw outputs and judge rationales | Partially available through local runs; not comprehensively public for all reported models. |
| Non-use caveats | Yes in paper for AGI/autonomous research; should be carried into public reporting [S03]. |

Reviewer comments: Reports are most informative when they include accuracy, calibration error, subset/form labels, model version, and judge/scoring configuration.

### 4.10 Intended Recipients

| Recipient | Output need |
| :-- | :-- |
| AI researchers | Source-grounded model comparison, score reproduction, item-quality caveats. |
| Model developers | Diagnostic weaknesses by domain, answer format, multimodality, and calibration. |
| Safety evaluators | Capability and overconfidence evidence with explicit non-use cautions. |
| Policy/governance actors | Narrow supported interpretation and warning against AGI/autonomy overclaims. |
| Public leaderboard users | Simple score/rank plus visible uncertainty and version labels. |
| Benchmark maintainers | Item error reports, contamination signals, model saturation signals, and rolling-update needs. |

Reviewer comments: Different users need different levels of methodological caveat. The same score is not sufficient evidence for all recipient groups.

## Section 5. Benchmark Access, Materials, and Lifecycle

### 5.1 Distribution and Access Model

Select all that apply.

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

Reviewer comments: The paper appendices document submission/review criteria and prompts; the repository provides scripts; the Hugging Face card provides dataset access; HLE-Rolling change log documents dynamic updates [S02, S03, S05, S10].

### 5.2 Distribution and Access Model

Select all that apply.

- [x] Fully public materials
- [x] Public materials with restricted answer keys or hidden tests
- [x] Controlled-access dataset or task host
- [x] Private or held-out evaluation service
- [ ] Hosted scoring service
- [x] Leaderboard-only submission route
- [ ] Benchmark registry or task-pack distribution
- [ ] Competition or challenge distribution
- [x] Private maintainer-mediated distribution
- [ ] Retired or archived materials available
- [ ] Access model not documented

Reviewer comments: Public materials are broad but not complete: the static public data are available after dataset access terms, while the private held-out set is not publicly inspectable [S03, S05].

### 5.3 Methods of Publication

Select all that apply.

- [x] Academic paper
- [x] Benchmark website
- [x] Git repository
- [ ] Package registry
- [x] Dataset hosting platform
- [x] Leaderboard platform
- [ ] Hosted evaluation service
- [ ] Benchmark registry
- [ ] Contest organizer source
- [x] Controlled-access data host
- [ ] Downloadable documents
- [x] Private distribution

Reviewer comments: The benchmark is published through paper, site, GitHub, Hugging Face, and leaderboard/reporting surfaces [S01-S06].

### 5.4 User Requirements or Qualifications

| Requirement type | Requirement |
| :-- | :-- |
| Technical skill | Ability to run Python/evaluation scripts, call model APIs or local models, handle image inputs, and inspect outputs [S08, S09]. |
| Model access | API-hosted or local model access; multimodal model access needed for full HLE [S03, S08]. |
| Dataset access | Hugging Face dataset access terms for public data; private held-out set not public [S03, S05]. |
| Compute or budget | Depends on model and provider. Full public evaluation can be costly because it includes 2,500 items and optional judge calls [S08, S09]. |
| Tool/API credentials | Provider API credentials required for API model runs; no external tools required by the task [S08]. |
| Hosted submission or leaderboard account | Needed only for relevant public leaderboard/reporting routes; not required for local public evaluation [S06]. |
| Human expertise | Needed for item creation/audit and substantive interpretation, not for routine automated scoring [S03]. |
| Account, license, or competition eligibility | MIT repository license; Hugging Face access terms/contact sharing for dataset [S02, S05]. |
| Ethical, safety, or data-use obligations | Avoid training on public benchmark data if using HLE for evaluation; respect dataset terms and contamination warnings/canary [S02, S05]. |

Reviewer comments: Ordinary model evaluation is technically straightforward but high-quality interpretation requires domain and measurement expertise.

### 5.5 Dataset and Item Access

| Component | Public | Restricted | Hidden | Not available |
| :-- | :--: | :--: | :--: | :--: |
| Training or development items | [ ] | [ ] | [ ] | [x] |
| Public evaluation items | [x] | [x] | [ ] | [ ] |
| Private or held-out evaluation items | [ ] | [x] | [x] | [ ] |
| Secret, encrypted, or reserve evaluation items | [ ] | [ ] | [x] | [ ] |
| Private leaderboard set | [ ] | [x] | [x] | [ ] |
| Retired or archived evaluation items | [ ] | [ ] | [ ] | [x] |
| Answer keys or reference solutions | [x] | [x] | [ ] | [ ] |
| Metadata or annotations | [x] | [x] | [ ] | [ ] |
| Human annotations or verification labels | [ ] | [x] | [ ] | [ ] |
| Raw model outputs or logs | [ ] | [x] | [ ] | [ ] |
| Model submissions and traces | [ ] | [x] | [ ] | [ ] |
| Hosted scoring service | [ ] | [x] | [ ] | [ ] |
| Simulator or environment state | [ ] | [ ] | [ ] | [x] |
| Task registry entry | [ ] | [ ] | [ ] | [x] |
| Tool/API credentials or configuration | [ ] | [x] | [ ] | [ ] |

Reviewer comments: Public HLE is a test-style dataset rather than a train/dev/test suite. Public items include answers, which supports auditability but increases contamination risk [S03, S05].

### 5.6 Provenance and Contamination Documentation

| Topic | Documented | Partially documented | Not documented |
| :-- | :--: | :--: | :--: |
| Data origin or task creation | [x] | [ ] | [ ] |
| Source-material release date | [ ] | [x] | [ ] |
| Contest or problem-source timing | [ ] | [ ] | [x] |
| Persistent dataset or benchmark-material identifier | [x] | [ ] | [ ] |
| Author or contributor qualifications | [x] | [ ] | [ ] |
| Deduplication or overlap checks | [ ] | [x] | [ ] |
| Rationale for public items and hidden or restricted evaluation items | [x] | [ ] | [ ] |
| Screening for prior model exposure to benchmark items, answers, or sources | [ ] | [x] | [ ] |
| Canary strings or training-data warnings | [x] | [ ] | [ ] |
| Diagnostic task for performance driven by prior exposure to items or answers | [ ] | [ ] | [x] |
| Pre-exposure or source-material searchability checks | [x] | [ ] | [ ] |
| Public-source searchability | [x] | [ ] | [ ] |
| Post-release contamination risk | [ ] | [x] | [ ] |
| Training-use prohibition | [ ] | [x] | [ ] |
| Private-set owner | [ ] | [x] | [ ] |
| Leak response policy | [ ] | [ ] | [x] |
| Rerun or replacement trigger | [ ] | [x] | [ ] |
| Hash commitments, signatures, or tamper-evident audit logs | [ ] | [ ] | [x] |
| Encrypted, secret, or controlled-release item reserve | [ ] | [x] | [ ] |
| Rules for updating, rotating, replacing, or adding benchmark items over time | [ ] | [x] | [ ] |
| Reporting of known unintended disclosures or deprecated/archived items | [ ] | [x] | [ ] |

Reviewer comments: HLE has unusually explicit model-difficulty filtering, searchability checks, public bug bounty/audit discussion, and a canary string. Remaining gaps concern formal contamination diagnostics, leak response, private-set details, and long-term version comparability [S02, S03, S10, S13].

### 5.7 Reproducibility Materials

Select all that apply.

- [x] Complete task data
- [x] Complete prompt templates
- [x] Code or platform that administers tasks, collects outputs, and often runs scoring
- [x] Scoring code
- [x] Environment file or dependency list
- [ ] Container or reproducible environment
- [ ] Container image
- [ ] Task environment registry
- [ ] Simulator or user simulator version
- [x] Evaluation adapter
- [x] Judge model and prompt version
- [ ] Version pinning
- [ ] Random seeds or deterministic settings
- [ ] Model responses, traces, logs, judge rationales, or per-item data
- [ ] Reproduction script for published results
- [ ] Push-button replication script or single documented command
- [ ] Expected-output fixtures or smoke-test example
- [ ] Scorer fixtures
- [ ] Known-good baseline run
- [x] Task-level expected outputs
- [ ] Continuous integration or test suite
- [ ] Public build status or equivalent passing-test signal

Reviewer comments: Public data, prompts, and scoring scripts support independent use. Exact replication of published results remains limited by model access, model version drift, sampling settings, judge dependency, and missing raw-output bundles.

### 5.8 Maintenance and Versioning

| Topic | Response |
| :-- | :-- |
| Maintainer identity | CAIS / HLE repository maintainers and Scale/SEAL result surface operators [S02, S06]. |
| Private or held-out set owner | HLE organizers/maintainers; exact governance details for private held-out set are partial in reviewed public materials [S03]. |
| Leaderboard operator | Scale AI / SEAL for the reviewed public result surface [S06]. |
| Submission eligibility rules | Not comprehensively specified for all public result routes in reviewed materials. |
| Rerun policy | Not fully specified for static HLE; HLE-Rolling update route exists [S10]. |
| Stale-score policy | Partially handled through current result pages and rolling context; no full stale-score policy identified. |
| Model-version update policy | Public result surfaces identify model names, but full alias/version update rules are not consolidated. |
| Scorer, judge, parser, or harness versioning | Paper and scripts identify judge path; ongoing simple-evals route may differ and should be labeled [S07, S09]. |
| Cohort or evaluation-window labels | Static public set and HLE-Rolling/current result contexts need separate labels [S06, S10]. |
| Public/private score aggregation policy | Not fully documented from inspected public sources. |
| Retirement and archival policy | Not identified for static HLE. |
| Documented release names, tags, changes, and score-comparability implications | HLE-Rolling change log provides update records; static HLE comparability implications are partly documented [S10]. |
| Changelog or update record | HLE-Rolling change log public [S10]. |
| Issue or feedback process | GitHub issues and community feedback/bug bounty process documented [S02, S03]. |
| Item correction process | Paper documents community feedback, bug bounty, manual verification, author feedback, audits, and removal/revision of problem items [S03]. |
| Deprecated item handling | Partially documented through HLE-Rolling change log and paper discussion [S03, S10]. |
| Rules for updating, rotating, replacing, or adding hidden evaluation items over time | Partially documented; private-set refresh and HLE-Rolling policy are not fully specified in one place [S03, S10]. |
| Last code-usability or harness health check | Not identified as an explicit health-check date. |
| Build, CI, or smoke-test status | No public CI/build status identified. |
| Score-ceiling threshold or criteria for deprecating, archiving, or ending use | Paper states HLE-Rolling is intended as a migration path once frontier models approach ceiling performance on original HLE [S03]. |
| Policy for deprecating, archiving, or ending use of items, versions, leaderboards, or the benchmark | Partial; no comprehensive retirement policy identified. |
| Retired-item publication or audit policy | Not identified. |
| Score comparability across versions | Static HLE scores should be comparable when the same data/scorer/prompt are used; HLE-Rolling/current variants require separate labels [S10]. |
| Policy for comparing scores across dates, cohorts, refreshes, or rolling windows | Partial and should be made explicit for HLE-Rolling and current leaderboard results [S06, S10]. |
| Long-term archival plan | GitHub, Hugging Face, arXiv, and Nature provide durable surfaces; no formal long-term archive/retirement plan identified [S02-S05]. |

Reviewer comments: Maintenance is active enough to show updates and feedback response, but benchmark users still need clearer versioning, stale-score, private-set, and retirement policies.

## Appendix A. General Description of the Benchmark

Humanity's Last Exam is best described as a difficult, closed-ended academic question-answering benchmark for frontier language and multimodal models. It samples expert-created questions across a wide range of academic domains, asks models to give a final answer and confidence, and scores outputs through answer-equivalence judging. HLE is strongest as evidence about performance on difficult, verifiable academic questions under HLE prompting and scoring conditions. It is not by itself a benchmark of autonomous research, open-ended scientific discovery, tool-using agency, long-horizon planning, or complete AGI.

# Part B. Evaluation of the Benchmark

Part B is evaluative. Ratings use the MESA `n/a` and `0`-`4` scale and are based on the evidence recorded in Part A plus cited contextual literature.

## Information Sources

| Source group | Sources used |
| :-- | :-- |
| Official HLE facts | S01-S10 |
| Supporting critique | S11 |
| MESA template and rating guidance | S12 |
| Benchmark-quality literature | S13 |
| Construct-validity literature | S14 |
| AGI/CHC breadth literature | S15 |
| Local inventory | S16 |

## Explanation of Ratings

Ratings follow the active MESA template: `n/a` means the criterion is not applicable to the reviewed entity; `0` means no usable evidence or serious unsupportedness; `1` means very limited support; `2` means cautious/partial support with important gaps; `3` means generally adequate support with manageable gaps; `4` means comprehensive support for the intended use.

## General Guidance on Assigning Ratings

Missing documentation is treated as an evidence gap, not as proof of poor quality. Ratings are not mechanically averaged. The overall rating in each section reflects the strength of evidence for HLE's intended score meaning: difficult closed-ended academic question answering under documented HLE conditions.

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

### 6.1 Rationale and Development

#### 6.1.1 Rationale and construct definition

- Rating: 3
- Evidence: The paper defines HLE as a benchmark of difficult closed-ended academic questions at the frontier of human knowledge, motivated by saturation of prior benchmarks [S03].
- Missing evidence: A formal construct definition separating knowledge, reasoning, retrieval, image understanding, and calibration is not fully decomposed into MESA-style subconstructs.
- Rationale: The target is clear enough for the narrow interpretation of expert academic QA.
- Reviewer caution: Do not treat the benchmark title as a definition of general intelligence.

#### 6.1.2 Summary of prior research and benchmark context

- Rating: 3
- Evidence: The paper situates HLE against MMLU, GPQA-style expert QA, multimodal benchmarks, and benchmark saturation [S03].
- Missing evidence: Comparisons to broader cognitive, agentic, and real-world research benchmarks are selective rather than systematic.
- Rationale: Prior benchmark context is adequate for explaining why harder closed-ended academic QA was developed.
- Reviewer caution: Saturation of older academic QA benchmarks does not by itself prove that HLE captures broader AI capability.

#### 6.1.3 Phenomenon-task-metric-claim chain

- Rating: 3
- Evidence: Phenomenon is difficult academic QA; task is closed-ended expert questions; metric is judged correctness plus calibration; claim is model performance at the expert academic question frontier [S03, S08, S09].
- Missing evidence: Formal validation that the judge/scorer and item sample isolate the intended ability from format, retrieval, memorization, and domain-distribution effects is incomplete.
- Rationale: The chain is defensible for the narrow score interpretation.
- Reviewer caution: The chain is not sufficient for autonomous research or AGI claims [S14, S15].

#### 6.1.4 Task or item design

- Rating: 3
- Evidence: Items were required to be precise, unambiguous, closed-ended, verifiable, non-searchable, and supported by answer specifications and rationales [S03].
- Missing evidence: Complete public item-level review/audit status and item difficulty metadata are not fully visible for all items.
- Rationale: Design rules are strong for closed-ended academic questions.
- Reviewer caution: Even strong design rules do not eliminate expert disagreement or label noise in frontier academic tasks.

#### 6.1.5 Procedures for developing task or item content

- Rating: 3
- Evidence: HLE used global expert contributors, model-difficulty filtering, multiple review rounds, organizer/expert approval, community feedback, audits, and searchability checks [S03].
- Missing evidence: Full reviewer assignment data, reviewer training outcomes, and per-item review trails are not public.
- Rationale: The development process is unusually detailed for an AI benchmark.
- Reviewer caution: Paper notes review limits, including that reviewers were not expected to fully verify every solution rationale if that would take more than five minutes [S03].

#### 6.1.6 Thoroughness of the final task or item selection process

- Rating: 3
- Evidence: Questions were filtered for model difficulty and expert review, and later refined through public feedback, bug bounty, targeted audits, and searchability checks [S03].
- Missing evidence: Full acceptance/rejection data and final per-item audit status are not public.
- Rationale: Selection is well documented and multi-stage, but not fully auditable from public materials.
- Reviewer caution: The HLE-Verified critique indicates that item-quality concerns remained important after release [S11].

#### 6.1.7 Quantitative evidence of task or item quality

- Rating: 2
- Evidence: The paper reports expert disagreement estimates, including 15.4% for the public set and about 18% for a biology/chemistry/health subset [S03].
- Missing evidence: Public item-level reliability, difficulty, discrimination, and verified-label status are incomplete.
- Rationale: Quantitative quality evidence exists, but it points to non-trivial uncertainty.
- Reviewer caution: The disagreement rates should be interpreted as an evidence gap and caution signal, not as proof that HLE is unusable.

#### 6.1.8 Adaptation, translation, source reuse, derived entity, or benchmark slice

- Rating: n/a
- Evidence: HLE is an original expert-submitted benchmark rather than a translated or derived slice of a prior benchmark [S03].
- Missing evidence: n/a.
- Rationale: The criterion does not apply to the primary reviewed entity.
- Reviewer caution: Individual questions may synthesize published information, but the benchmark is not a reused human-exam source.

#### 6.1.9 Overall quality of rationale, development, and task or item quality

- Rating: 3
- Evidence: Strong rationale, expert construction, filtering, review, feedback, and documented caveats [S03].
- Missing evidence: Full public item audit trails, private-set documentation, and complete item-quality psychometrics.
- Rationale: Strong support for a cautious expert academic QA benchmark.
- Reviewer caution: Item disagreement and post-release verification debates should accompany high-stakes interpretations.

### 6.2 Adequacy of Documentation Available to Users

#### 6.2.1 Documentation of benchmark purpose and intended use

- Rating: 3
- Evidence: The paper explains HLE's purpose, intended frontier-model use, and non-AGI caveat [S03].
- Missing evidence: A consolidated user-facing "appropriate uses and non-uses" page was not identified.
- Rationale: Purpose is clear in the paper.
- Reviewer caution: Public users may encounter score surfaces without reading the full paper.

#### 6.2.2 Documentation of development process

- Rating: 3
- Evidence: The paper documents contributor qualifications, submission criteria, model screening, review rounds, audits, and bug bounty [S03].
- Missing evidence: Complete per-item workflow records and reviewer assignment data are not public.
- Rationale: The development process is documented at a high level with useful quantitative details.
- Reviewer caution: The process description does not allow full independent reconstruction of every item decision.

#### 6.2.3 Documentation of scoring and metrics

- Rating: 3
- Evidence: The prompt, judge format, accuracy calculation, confidence extraction, and RMS calibration error are documented [S03, S08, S09].
- Missing evidence: Comprehensive validation of judge accuracy and malformed-response handling is limited.
- Rationale: Metric documentation is usable for implementation and audit.
- Reviewer caution: Model-judge dependence should be disclosed with every score report.

#### 6.2.4 Documentation of reliability, stability, and uncertainty

- Rating: 2
- Evidence: The paper discusses model non-determinism, low-score floor issues, expert disagreement, and calibration error; scorer code includes confidence interval helper [S03, S09].
- Missing evidence: Repeated-run variance, prompt sensitivity, judge stability, and standard error reporting for all published results are incomplete.
- Rationale: Some reliability evidence exists, but major sources of score variation remain underdocumented.
- Reviewer caution: Close model comparisons should be treated cautiously.

#### 6.2.5 Documentation of validity evidence

- Rating: 2
- Evidence: The paper provides a rationale linking expert-created closed-ended academic questions to expert academic QA capability [S03].
- Missing evidence: External validity, predictive relevance, discriminant validity, and broad cognitive-domain validation are limited.
- Rationale: Validity support is adequate for the narrow construct but incomplete for broader claims.
- Reviewer caution: Broad academic coverage is not the same as broad cognitive coverage [S14, S15].

#### 6.2.6 Documentation of fair use and comparability

- Rating: 2
- Evidence: The paper distinguishes text-only and multimodal evaluation, describes public/private sets, and cautions against AGI/autonomy interpretation [S03].
- Missing evidence: Full comparability rules for model versions, private/public/rolling forms, reruns, and leaderboard submissions are distributed or incomplete.
- Rationale: Some fair-use guidance exists, but it is not consolidated.
- Reviewer caution: Static HLE and HLE-Rolling/current leaderboards should not be mixed without labels.

#### 6.2.7 Documentation of maintenance and versioning

- Rating: 2
- Evidence: HLE-Rolling change log and repository provide update context [S02, S10].
- Missing evidence: Static HLE retirement, stale-score, rerun, hidden-set rotation, and archive policies are incomplete.
- Rationale: Maintenance evidence exists but is not comprehensive.
- Reviewer caution: Time-sensitive comparisons require explicit form/date/source labels.

#### 6.2.8 Adequacy of documentation available to users

- Rating: 3
- Evidence: Paper, dataset card, repository, scripts, result surface, and rolling change log provide substantial documentation [S01-S10].
- Missing evidence: Documentation is distributed across sources, and private-set and judge-validation details remain incomplete.
- Rationale: Users can understand and run HLE, but not fully audit every score condition.
- Reviewer caution: Documentation adequacy is stronger for public static HLE than for private/rolling/current result interpretations.

### 6.3 Quality of Procedural Instructions

#### 6.3.1 Evaluation setup and administration

- Rating: 3
- Evidence: Official prompt and repository scripts document the basic evaluation setup [S08, S09].
- Missing evidence: A single push-button reproduction path for all paper results is not public.
- Rationale: Instructions are adequate for competent technical users.
- Reviewer caution: Exact published-score replication requires more than the prompt.

#### 6.3.2 Scoring procedure and error handling

- Rating: 2
- Evidence: Judge prompt defines answer extraction, equivalence judgment, confidence extraction, and missing-confidence behavior [S09].
- Missing evidence: Comprehensive malformed-output, abstention, refusal, numeric tolerance, and judge-disagreement policy is incomplete.
- Rationale: Core scoring is documented, but edge handling is not fully specified.
- Reviewer caution: Parser/judge choices can change scores on short-answer items.

#### 6.3.3 Interpretation and reporting guidance

- Rating: 3
- Evidence: Paper explains low-score floor interpretation and states HLE is not evidence of AGI/autonomous research by itself [S03].
- Missing evidence: Public result surfaces do not always foreground all interpretation caveats.
- Rationale: Interpretation guidance is strong in the paper.
- Reviewer caution: Leaderboard users may still overread ranks.

#### 6.3.4 Restrictions, prerequisites, and appropriate use

- Rating: 2
- Evidence: Dataset access terms, MIT license, canary string, multimodal/text-only distinction, and public/private-set rationale are documented [S02, S03, S05].
- Missing evidence: A concise operational policy for training-use prohibition, private-set access, and score-reporting requirements is incomplete.
- Rationale: Requirements are partially documented across surfaces.
- Reviewer caution: Public HLE items should not be used for model training if later HLE evaluation is intended.

#### 6.3.5 Technical support and implementation guidance

- Rating: 3
- Evidence: Repository scripts and maintained evaluator route support implementation [S02, S07, S08, S09].
- Missing evidence: CI/build status, smoke tests, and explicit health-check date are not identified.
- Rationale: Technical users have enough material to run HLE.
- Reviewer caution: Dependency/provider changes can affect long-term usability.

#### 6.3.6 References and supporting materials

- Rating: 3
- Evidence: Paper includes extensive references and appendices; repository and dataset link evaluation resources [S02-S05].
- Missing evidence: Some operational details remain split across repository, dataset card, and leaderboard.
- Rationale: Supporting materials are substantial.
- Reviewer caution: Reviewers should cite exact materials, not just the benchmark name.

#### 6.3.7 Quality of procedural instructions

- Rating: 3
- Evidence: HLE provides prompts, scripts, source paper, and dataset access [S02, S03, S05, S08, S09].
- Missing evidence: Edge cases, version pinning, and full reproduction path need more detail.
- Rationale: Good but not comprehensive procedural guidance.
- Reviewer caution: Different HLE implementations may not be directly comparable.

### 6.4 Overall Adequacy of Rationale and Documentation

- Rating: 3
- Evidence: HLE has strong rationale, development documentation, public materials, and explicit score-caveat language [S02-S05].
- Missing evidence: Complete reliability evidence, private-set governance, item-level audit trails, and judge validation are not public.
- Rationale: Documentation is generally adequate for cautious public use.
- Reviewer caution: Use HLE as a high-quality but imperfect academic QA stress test, not as a complete capability certificate.

## Section 7. Quality and Usability of Benchmark Materials

### 7.1 Quality of Benchmark Materials

#### 7.1.1 Dataset, task set, or evaluation environment availability

- Rating: 3
- Evidence: Public 2,500-question dataset is available through Hugging Face, with official repository links [S02, S05].
- Missing evidence: Private held-out set is not public; full data-card standardization and private access details are limited.
- Rationale: Public material availability is strong.
- Reviewer caution: Public answers increase auditability and contamination risk simultaneously.

#### 7.1.2 Prompts, instructions, and input materials

- Rating: 3
- Evidence: Official answer/confidence prompt and judge prompt are documented in paper/repository [S03, S08, S09].
- Missing evidence: Prompt-sensitivity experiments and all published-run prompt placements are not comprehensively listed.
- Rationale: Prompt materials are clear enough for reproduction attempts.
- Reviewer caution: Prompt changes can affect answer format, confidence, and judge extraction.

#### 7.1.3 Rubrics, reference answers, and response format requirements

- Rating: 3
- Evidence: Public data include answer specifications; paper describes contributor rationales and response requirements [S03, S05].
- Missing evidence: Full solution rationales and complete per-item rubric/audit histories are not necessarily public for all items.
- Rationale: Reference answers support automated scoring.
- Reviewer caution: Short-answer equivalence needs careful judge validation.

#### 7.1.4 Evaluation harness, scorer, and implementation quality

- Rating: 2
- Evidence: HLE repository and simple-evals provide runnable scoring/evaluation paths [S02, S07, S08, S09].
- Missing evidence: CI/build status, containerized environment, locked dependencies, and known-good baseline fixtures are incomplete.
- Rationale: Usable implementation exists, but reproducibility engineering is partial.
- Reviewer caution: Provider API and judge-model changes can shift results.

#### 7.1.5 Interface and workflow usability

- Rating: 3
- Evidence: Dataset, repository scripts, and result surface are accessible to technical users [S02, S05, S06].
- Missing evidence: Non-technical user guide and one-command reproduction are limited.
- Rationale: Workflow is usable for ML researchers.
- Reviewer caution: Public leaderboard simplicity may hide evaluation-condition differences.

#### 7.1.6 Accessibility across modalities, languages, and system types

- Rating: 2
- Evidence: Text-only subset allows non-multimodal models to be reported separately; full benchmark includes images [S03].
- Missing evidence: Multilingual support, accessibility alternatives, and cross-system fairness studies are limited.
- Rationale: HLE supports text and multimodal evaluation but not broad modality/language accessibility.
- Reviewer caution: Full HLE and text-only HLE scores should not be compared as equivalent.

#### 7.1.7 Licensing, use requirements, and risk warnings

- Rating: 3
- Evidence: Repository has MIT license; dataset host documents access terms; canary string warns against training contamination [S02, S05].
- Missing evidence: A consolidated responsible-use and contamination policy would improve clarity.
- Rationale: Core legal/access information is available.
- Reviewer caution: License permissiveness does not remove benchmark-validity concerns from training on the public set.

#### 7.1.8 Overall quality of benchmark materials

- Rating: 3
- Evidence: Public data, prompts, scripts, answers, paper, result surface, and change log are available [S01-S10].
- Missing evidence: Private materials, CI, environment locking, raw outputs, and complete score reproduction packages are incomplete.
- Rationale: Benchmark-material quality is good for public evaluation and audit.
- Reviewer caution: Official static, rolling, and third-party materials must be labeled separately.

## Section 8. Baselines, Comparators, and Reference Interpretation

### 8.1 Baseline and Comparator Interpretation

#### 8.1.1 Random, chance, floor, and ceiling baselines

- Rating: 2
- Evidence: Multiple-choice items have chance floor; paper discusses low-score floor and benchmark saturation risk [S03].
- Missing evidence: Formal random baseline across mixed MC/exact-match items and ceiling guidance are incomplete.
- Rationale: Some baseline interpretation exists, but mixed item formats complicate simple chance baselines.
- Reviewer caution: Near-floor score changes are not necessarily meaningful progress.

#### 8.1.2 Human or expert baselines

- Rating: 2
- Evidence: Items were created and reviewed by expert contributors, and intended to require graduate-level or specialized expertise [S03].
- Missing evidence: A standardized full human baseline across all 2,500 public questions is not identified.
- Rationale: Expert involvement is strong, but not the same as a controlled human performance baseline.
- Reviewer caution: "Expert-level" should be interpreted as item-source and item-difficulty framing, not a full normed human comparison.

#### 8.1.3 Model comparator cohort

- Rating: 3
- Evidence: Paper reports multiple frontier model results and calibration errors; Scale/SEAL reports current model comparisons [S03, S06].
- Missing evidence: Complete raw outputs, exact model configurations, and repeated-run variance are incomplete.
- Rationale: Model comparator evidence is good for broad frontier-model comparison.
- Reviewer caution: Model rankings can change quickly and depend on exact evaluation conditions.

#### 8.1.4 Historical, version, or benchmark-family comparators

- Rating: 3
- Evidence: Paper motivates HLE through saturation of earlier benchmarks and compares it to frontier academic benchmark landscape [S03].
- Missing evidence: Formal longitudinal score bridging across HLE static, HLE-Rolling, and verified subsets is incomplete.
- Rationale: Historical context is adequate.
- Reviewer caution: HLE-Rolling and HLE-Verified should not be treated as direct replacements without bridging evidence.

#### 8.1.5 Criterion thresholds, score bands, or performance categories

- Rating: 2
- Evidence: Paper states high accuracy would suggest expert-level performance on closed-ended academic questions and cautions against small near-floor inflections [S03].
- Missing evidence: Stable threshold bands for novice/expert/saturation are not specified.
- Rationale: Qualitative interpretation exists but is not operationalized into robust bands.
- Reviewer caution: A percentage score alone does not establish a capability category.

#### 8.1.6 Representativeness of reference groups

- Rating: 2
- Evidence: Contributors were broad across institutions/countries and subject areas [S03].
- Missing evidence: Full analysis of domain balance, contributor selection, cultural/language representativeness, and expert population comparability is incomplete.
- Rationale: Breadth is impressive but not a representative sample in a statistical sense.
- Reviewer caution: HLE samples expert academic questions, not the full universe of human knowledge or intelligence.

#### 8.1.7 Currency and maintenance of baseline evidence

- Rating: 3
- Evidence: Current result surfaces and HLE-Rolling context keep model results and item updates visible [S06, S10].
- Missing evidence: Versioned stale-score policy and retest schedule are incomplete.
- Rationale: Baseline currency is actively maintained but not fully governed.
- Reviewer caution: Scores need access date, dataset form, and evaluator labels.

### 8.2 Overall Adequacy of Baselines and Reference Interpretation

- Rating: 2
- Evidence: HLE provides model comparators, expert-development context, calibration metrics, and low-score caveats [S03, S06].
- Missing evidence: Full human baseline, formal chance model for mixed item types, score-band thresholds, and statistical comparison guidance are incomplete.
- Rationale: Reference interpretation supports cautious use, not definitive ranking or human-equivalence claims.
- Reviewer caution: Leaderboard ranks should be read with uncertainty, form labels, and score-condition labels.

## Section 9. Reliability, Precision, and Score Stability

### 9.1 Data Provided About Reliability, Precision, and Stability

#### 9.1.1 Coverage of reliability and stability evidence

- Rating: 2
- Evidence: Paper discusses expert disagreement, model non-determinism, confidence calibration, and low-score floor; scorer computes confidence interval helper [S03, S09].
- Missing evidence: Comprehensive reliability design across runs, prompts, judges, models, and forms is incomplete.
- Rationale: Important reliability topics are acknowledged but not exhaustively measured.
- Reviewer caution: Reliability evidence is better for item-audit discussion than for fine-grained model rank differences.

### 9.2 Run-to-Run Stability and Uncertainty

#### 9.2.1 Run-to-run stability, seeds, and sampling settings

- Rating: 2
- Evidence: Paper notes model inference noise and low but non-zero accuracy after model-difficulty filtering [S03].
- Missing evidence: Published repeated-run studies, seed variance, temperature sensitivity, and prompt sensitivity tables are incomplete.
- Rationale: Run instability is acknowledged but not fully quantified.
- Reviewer caution: Single-run HLE scores should not be treated as exact model capabilities.

#### 9.2.2 Score uncertainty, confidence intervals, or standard errors

- Rating: 2
- Evidence: Repository scorer includes a Wald 95% confidence interval half-width calculation; Scale/SEAL reports rank upper-bound style information [S06, S09].
- Missing evidence: Standard errors/confidence intervals are not consistently foregrounded for all published scores and subgroups.
- Rationale: Some uncertainty machinery exists but reporting is not comprehensive.
- Reviewer caution: Close score differences need explicit uncertainty intervals.

### 9.3 Scorer, Judge, Parser, and Rater Reliability

#### 9.3.1 Automated scorer or parser reliability

- Rating: 2
- Evidence: Judge prompt specifies extraction and correctness criteria, including confidence extraction [S09].
- Missing evidence: Independent parser accuracy, scorer fixtures, adversarial malformed-output tests, and item-type-specific judge reliability are incomplete.
- Rationale: Scorer is inspectable but not fully validated.
- Reviewer caution: Short-answer score reliability depends on model-judge behavior.

#### 9.3.2 Human rater or expert scorer agreement

- Rating: 2
- Evidence: Paper reports estimated expert disagreement and describes audit/rebuttal processes [S03].
- Missing evidence: Comprehensive inter-rater agreement across all items and reviewer demographics/training details are incomplete.
- Rationale: Agreement evidence is valuable but also indicates non-trivial disagreement.
- Reviewer caution: Expert disagreement should temper high-stakes item-level conclusions.

#### 9.3.3 Model-as-judge reliability and validity checks

- Rating: 2
- Evidence: Paper and repository document judge model/prompt and structured judge output [S03, S09].
- Missing evidence: Systematic validation of judge decisions against human adjudication for all item types is incomplete.
- Rationale: The judge design is transparent but validation is partial.
- Reviewer caution: Judge upgrades should be versioned and may break score comparability.

### 9.4 Form, Version, Prompt, and Environment Stability

#### 9.4.1 Prompt, instruction, or formatting sensitivity

- Rating: 1
- Evidence: Official prompt is documented [S08].
- Missing evidence: Prompt-sensitivity and format-sensitivity experiments are not identified.
- Rationale: HLE depends on extracting answer/confidence from a specific format, but sensitivity is underreported.
- Reviewer caution: Prompt variants may change both accuracy and calibration error.

#### 9.4.2 Form, split, version, or refresh equivalence

- Rating: 2
- Evidence: Static public set, private held-out set, and HLE-Rolling are documented as distinct contexts [S03, S10].
- Missing evidence: Formal equating across public/private/rolling/verified forms is incomplete.
- Rationale: Forms are named but not fully bridged.
- Reviewer caution: HLE-Rolling and HLE static scores should not be directly pooled.

#### 9.4.3 Execution environment and dependency stability

- Rating: 2
- Evidence: Public scripts exist [S02, S08, S09].
- Missing evidence: Container, version lock, CI/build status, and health-check date were not identified.
- Rationale: The environment is likely usable for technical users but not fully reproducibility-hardened.
- Reviewer caution: Provider and dependency drift can undermine exact replication.

### 9.5 Statistical Comparison Quality

#### 9.5.1 Meaningfulness of score differences

- Rating: 2
- Evidence: Paper cautions against interpreting small changes near the floor; scorer includes confidence interval helper [S03, S09].
- Missing evidence: Minimum meaningful difference rules, multiple-comparison controls, and subgroup power analyses are incomplete.
- Rationale: Some statistical caution exists, but comparison guidance is partial.
- Reviewer caution: Do not overinterpret small leaderboard gaps.

### 9.6 Overall Reliability, Precision, and Score Stability

- Rating: 2
- Evidence: HLE reports calibration error, acknowledges low-score/floor issues, documents judge prompt, and reports expert disagreement [S03, S09].
- Missing evidence: Run-to-run, prompt, judge, and environment stability evidence remains limited.
- Rationale: Reliability support is adequate for broad directional conclusions, weak for precise rank claims.
- Reviewer caution: Use HLE for broad capability stress testing, not fine-grained score separation without uncertainty analysis.

## Section 10. Validity Evidence

### 10.1 Validity Evidence Based on Benchmark Content

#### 10.1.1 Content validity and task representativeness

- Rating: 3
- Evidence: HLE includes 2,500 expert-created questions across more than one hundred subjects, with explicit precision/non-searchability criteria [S03].
- Missing evidence: Statistical representativeness of academic knowledge domains is not established.
- Rationale: Content breadth and expert sourcing support closed-ended academic QA validity.
- Reviewer caution: Curated expert difficulty is not the same as representative coverage of all academic practice.

#### 10.1.2 Construct breadth and capability-domain coverage

- Rating: 2
- Evidence: HLE covers many academic domains and a small multimodal subset [S03].
- Missing evidence: It does not cover many AGI/CHC domains such as long-term memory storage, auditory processing, agency, embodied interaction, or speed [S15].
- Rationale: Broad academic content does not equal broad cognitive capability coverage.
- Reviewer caution: HLE should not be used alone as a general intelligence benchmark.

### 10.2 Validity Evidence Based on Internal Structure

#### 10.2.1 Internal structure, subscores, or dimensionality

- Rating: 2
- Evidence: Subject/category metadata and text-only/multimodal distinctions are available and reported [S03, S05].
- Missing evidence: Factor structure, item clustering, category reliability, and dimensionality analysis are incomplete.
- Rationale: Internal categories support descriptive profiling but not a validated measurement model.
- Reviewer caution: Category scores should be treated as descriptive, not psychometrically equated subscales.

#### 10.2.2 Item or task behavior across the score scale

- Rating: 2
- Evidence: Paper describes model-difficulty filtering, low frontier scores, and low-score floor interpretation [S03].
- Missing evidence: Item-level difficulty, discrimination, and behavior over future model score ranges are incomplete.
- Rationale: HLE is deliberately hard now, but measurement behavior near higher score ranges is uncertain.
- Reviewer caution: As models improve, ceiling and item-discrimination evidence will need updating.

#### 10.2.3 Failure modes and error analysis

- Rating: 2
- Evidence: Paper discusses overconfidence/hallucination via calibration error and notes model non-determinism [S03].
- Missing evidence: Full qualitative/quantitative taxonomy of model failure modes across subjects and item types is incomplete.
- Rationale: Calibration analysis is useful but not a comprehensive error analysis.
- Reviewer caution: Failure on HLE may reflect knowledge gaps, reasoning gaps, image perception, formatting, or judge effects.

### 10.3 Validity Evidence Based on Metrics and Scoring

#### 10.3.1 Metric, scorer, and aggregation validity

- Rating: 2
- Evidence: Accuracy is appropriate for closed-ended answerable questions, and calibration error is aligned with confidence claims [S03, S09].
- Missing evidence: Model-judge validation and aggregation robustness are incomplete.
- Rationale: Metrics have face validity but important scorer threats remain.
- Reviewer caution: Accuracy is only as valid as item labels, answer equivalence, and judge extraction.

#### 10.3.2 Sensitivity to shortcuts and construct-irrelevant variance

- Rating: 2
- Evidence: HLE used non-searchability criteria, searchability audits, model-difficulty filtering, private held-out set, and canary warning [S02, S03].
- Missing evidence: Post-release contamination diagnostics and format/prompt confound studies are incomplete.
- Rationale: Shortcut controls are meaningful but not complete.
- Reviewer caution: Public item exposure and answer keys become larger validity threats over time.

### 10.4 Validity Evidence Based on Relations to Other Variables

#### 10.4.1 Relations with other benchmarks, humans, criteria, or realistic settings

- Rating: 2
- Evidence: Paper relates HLE to saturated benchmarks and frontier model results [S03].
- Missing evidence: Strong external criterion validation against real academic research performance or controlled human performance is incomplete.
- Rationale: External relations are discussed but not fully validated.
- Reviewer caution: HLE is not direct evidence of performance in open-ended research settings.

#### 10.4.2 Convergent and discriminant evidence

- Rating: 2
- Evidence: HLE is positioned relative to other difficult academic QA and multimodal benchmarks [S03].
- Missing evidence: Systematic convergent/discriminant analyses are not identified.
- Rationale: Conceptual comparison exists, empirical discriminant evidence is limited.
- Reviewer caution: High HLE score may converge with academic QA ability but should be discriminated from agency and tool-use skill.

#### 10.4.3 Ecological or predictive relevance

- Rating: 2
- Evidence: HLE aims to inform research and policy by measuring difficult academic question answering [S03].
- Missing evidence: Predictive evidence for downstream scientific productivity, research autonomy, deployment outcomes, or governance thresholds is not provided.
- Rationale: Ecological relevance is plausible for academic QA stress testing, limited for broader outcomes.
- Reviewer caution: Closed-ended questions are a narrow proxy for real expert work.

### 10.5 Contamination, Leakage, and Gameability

#### 10.5.1 Contamination and leakage controls

- Rating: 3
- Evidence: HLE documents original/non-trivial synthesis requirements, non-searchability criteria, searchability audits, private held-out set, and canary string [S02, S03].
- Missing evidence: Ongoing public contamination monitoring and leak-response policy are incomplete.
- Rationale: Contamination controls are stronger than many public benchmarks.
- Reviewer caution: Public release of questions and answers means static HLE contamination risk increases over time.

#### 10.5.2 Gameability and benchmark-specific tuning controls

- Rating: 2
- Evidence: Private held-out set and HLE-Rolling are intended to mitigate overfitting/gaming [S03, S10].
- Missing evidence: Complete hidden-set governance, retest rules, and benchmark-specific tuning detection are incomplete.
- Rationale: Some controls exist, but public static HLE remains gameable after release.
- Reviewer caution: Public leaderboard use should distinguish public-data evaluation from private/rolling evaluation.

### 10.6 Claim Proportionality

#### 10.6.1 Proportionality of stated benchmark claims

- Rating: 3
- Evidence: Paper explicitly states that high HLE accuracy suggests expert-level closed-ended academic performance, not AGI or autonomous research by itself [S03].
- Missing evidence: This caveat should be consistently surfaced across all public result contexts.
- Rationale: The official paper's main caveat is appropriately proportional.
- Reviewer caution: Benchmark name and public discourse can still invite stronger interpretations.

#### 10.6.2 Broad intelligence, AGI, agency, or autonomy claims

- Rating: 3
- Evidence: Official paper includes explicit non-AGI/non-autonomous-research caveat, while AGI/CHC literature indicates broad intelligence requires many domains HLE does not test [S03, S15].
- Missing evidence: Comprehensive broad cognitive battery validation is not part of HLE.
- Rationale: HLE handles broad claims responsibly in the paper, but it remains vulnerable to public overclaiming.
- Reviewer caution: HLE should be paired with broader cognitive, agentic, tool-use, and real-world benchmarks before making AGI-adjacent claims.

### 10.7 Overall Validity Support

- Rating: 2
- Evidence: Strong content rationale and scoring face validity for closed-ended academic QA; explicit caveats against AGI/autonomy inference [S03, S09].
- Missing evidence: Judge validation, external predictive evidence, dimensionality, prompt sensitivity, and broader cognitive coverage remain incomplete.
- Rationale: Validity support is good for the narrow intended interpretation and only partial for broader capability narratives.
- Reviewer caution: The defensible statement is: HLE measures performance on difficult closed-ended academic questions under HLE conditions.

## Section 11. Fair Use, Comparability, and Appropriate Use

### 11.1 Rationale and Documentation for Fair Use

#### 11.1.1 Relevance of the construct across systems, groups, and contexts

- Rating: 3
- Evidence: Difficult academic QA is relevant to frontier language and multimodal models, and text-only subset handling is documented [S03].
- Missing evidence: Relevance for non-English systems, tool-using agents, retrieval systems, and domain-specialized systems is not fully addressed.
- Rationale: Construct relevance is strong for general-purpose frontier LLMs.
- Reviewer caution: Do not extend relevance to all AI system types.

#### 11.1.2 Documentation of fair-use considerations

- Rating: 2
- Evidence: Paper describes public/private sets, text-only handling, and non-AGI caveats [S03].
- Missing evidence: Consolidated fair-use policy for leaderboard reporting, training contamination, and subset comparability is incomplete.
- Rationale: Fair-use evidence exists but is distributed.
- Reviewer caution: Users need explicit labels for dataset form, modality subset, and evaluator implementation.

### 11.2 Development, Design, and Accessibility

#### 11.2.1 Inclusive and accessible benchmark design

- Rating: 2
- Evidence: Contributors came from many institutions and countries, and subjects are broad [S03].
- Missing evidence: Accessibility analysis for languages, cultures, disabilities, non-Western academic traditions, and image accessibility is limited.
- Rationale: Contributor breadth helps, but accessibility evidence is partial.
- Reviewer caution: English academic expert questions may privilege specific educational and cultural pathways.

#### 11.2.2 Domain, language, modality, and subgroup coverage

- Rating: 2
- Evidence: More than one hundred subjects and a text-plus-image subset are documented [S03].
- Missing evidence: Detailed subgroup/domain balance, category reliability, and multilingual coverage are incomplete.
- Rationale: Domain breadth is strong, but representativeness and subgroup fairness are underdocumented.
- Reviewer caution: Subject coverage should not be read as demographic, cultural, or linguistic fairness evidence.

### 11.3 Cross-System and Evaluation-Condition Comparability

#### 11.3.1 Cross-system comparability

- Rating: 2
- Evidence: Common prompt and scoring path allow broad comparison across frontier models [S03, S08, S09].
- Missing evidence: Equalized compute, reasoning settings, API versions, and multimodal/text-only comparability are incomplete.
- Rationale: Comparability is adequate for broad benchmarking but not perfect.
- Reviewer caution: Different provider settings can change scores and confidence calibration.

#### 11.3.2 Access, compute, tooling, and API or local comparability

- Rating: 2
- Evidence: HLE can be run with API or local models, and non-multimodal text-only results are documented [S03, S08].
- Missing evidence: Compute/cost normalization and API/local equivalence rules are incomplete.
- Rationale: Access routes are flexible but not fully comparable.
- Reviewer caution: Full-HLE multimodal scores and text-only scores answer different questions.

#### 11.3.3 Temporal comparability for rolling or live benchmarks

- Rating: 2
- Evidence: Static HLE and HLE-Rolling are distinct, and HLE-Rolling has change logs [S10].
- Missing evidence: Formal bridging and stale-score policies are incomplete.
- Rationale: Temporal comparability is manageable only with strict labels.
- Reviewer caution: Do not compare HLE-Rolling results across dates without change context.

### 11.4 Evidence for Fairness and Bias

#### 11.4.1 Differential performance or bias analysis

- Rating: 1
- Evidence: Subject/category results and broad contributor demographics are partially documented [S03].
- Missing evidence: Systematic differential performance/bias analysis by culture, language, subject area, image status, question format, and model family is incomplete.
- Rationale: Fairness/bias evidence is limited.
- Reviewer caution: Absence of bias evidence is not evidence of fairness.

#### 11.4.2 Reliability and validity across relevant subgroups or contexts

- Rating: 1
- Evidence: Expert disagreement is reported, including higher rates in health-related domains [S03].
- Missing evidence: Reliability/validity evidence across all subject domains, item formats, contributor groups, and model families is incomplete.
- Rationale: Subgroup/context evidence remains thin.
- Reviewer caution: Domain-specific HLE comparisons need stronger reliability evidence.

### 11.5 Appropriate Use and Restrictions

#### 11.5.1 Appropriate-use guidance and non-use cases

- Rating: 3
- Evidence: Paper explicitly cautions that HLE is not standalone evidence of AGI or autonomous research [S03].
- Missing evidence: Non-use guidance should be consolidated into dataset card and leaderboard surfaces.
- Rationale: Appropriate-use guidance is strong in the paper.
- Reviewer caution: HLE should not be used alone for deployment, procurement, or governance decisions.

#### 11.5.2 Release rules and sensitive-content handling

- Rating: 3
- Evidence: Paper documents WMD exclusion in submission criteria, public/private split rationale, bug bounty/audits, searchability checks, and canary warning [S02, S03].
- Missing evidence: Full private-set and leak-response rules are incomplete.
- Rationale: Release and integrity controls are good for a public academic QA benchmark.
- Reviewer caution: Static public release requires ongoing contamination monitoring.

### 11.6 Overall Fair Use, Comparability, and Appropriate Use

- Rating: 2
- Evidence: HLE includes explicit caveats, public/private rationale, text-only handling, and contamination controls [S02, S03].
- Missing evidence: Consolidated fair-use policy, subgroup analyses, compute normalization, and rolling/static comparability rules are incomplete.
- Rationale: Responsible use is partly supported, but important comparison contexts remain unclear.
- Reviewer caution: Always report form, subset, evaluator, date, model version, and judge configuration.

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

### 12.1 Scope and Coverage

#### 12.1.1 Report, leaderboard, dashboard, or reporting-material scope

- Rating: 3
- Evidence: HLE has paper results, official site, Scale/SEAL result surface, dataset, and scripts [S01-S09].
- Missing evidence: One consolidated reporting specification for all HLE result surfaces is incomplete.
- Rationale: Reporting ecosystem is substantial.
- Reviewer caution: Distinguish paper results, current leaderboard results, static HLE, and HLE-Rolling.

#### 12.1.2 Score granularity and level of detail

- Rating: 3
- Evidence: Paper reports accuracy, calibration error, category results, and text-only distinctions; scripts support item-level scoring outputs [S03, S09].
- Missing evidence: Public raw outputs and judge rationales for all model runs are incomplete.
- Rationale: Report detail is good for aggregate interpretation.
- Reviewer caution: Aggregate accuracy can hide subject, format, and judge effects.

### 12.2 Reliability and Traceability of Reports

#### 12.2.1 Uncertainty, version labeling, and evaluation-condition labeling

- Rating: 2
- Evidence: Paper identifies model versions where available; scorer includes confidence intervals; Scale/SEAL includes uncertainty-oriented rank presentation [S03, S06, S09].
- Missing evidence: Complete version, prompt, sampling, judge, and confidence interval labels are not uniform across all result surfaces.
- Rationale: Traceability is partial.
- Reviewer caution: Public ranks should not be read without method labels.

#### 12.2.2 Reproducibility and traceability of reported scores

- Rating: 2
- Evidence: Public data and scripts allow independent runs [S02, S05, S08, S09].
- Missing evidence: Exact raw outputs, provider states, seeds, and full reproduction scripts for published results are incomplete.
- Rationale: Reproduction is possible in spirit but not exact for all reported scores.
- Reviewer caution: Future API/model changes may prevent exact result recreation.

### 12.3 Relevance and Validity of Reports

#### 12.3.1 Linkage from scores to interpretations and public claims

- Rating: 3
- Evidence: Paper clearly links HLE scores to closed-ended academic QA and states AGI/autonomy limits [S03].
- Missing evidence: Caveats should be more prominent across all public result surfaces.
- Rationale: Score-to-claim linkage is mostly appropriate.
- Reviewer caution: Public reporting should repeat the narrow supported interpretation.

#### 12.3.2 Raw outputs, per-item data, or trace availability

- Rating: 2
- Evidence: Local evaluation scripts can produce per-item predictions and judge outputs [S08, S09].
- Missing evidence: Complete public raw outputs/traces for all official leaderboard/paper results are not identified.
- Rationale: Traceability exists for user-run evaluations, but not comprehensively for published results.
- Reviewer caution: Auditing reported results may require rerunning models or obtaining controlled traces.

### 12.4 Fairness, Acceptability, and Public Communication

#### 12.4.1 Fairness and freedom from bias in reports

- Rating: 2
- Evidence: Reports include category-level and text-only/multimodal distinctions [S03].
- Missing evidence: Dedicated fairness/bias reporting is limited.
- Rationale: Some subgroup-relevant detail exists, but fairness is not a central reporting dimension.
- Reviewer caution: Category breakdowns are not a substitute for bias analysis.

#### 12.4.2 Acceptability and usability for intended audiences

- Rating: 3
- Evidence: Paper, official site, dataset card, repository, and leaderboard are usable by researchers and technical evaluators [S01-S06].
- Missing evidence: Non-technical caveats are not always presented where public ranks appear.
- Rationale: Usability is good.
- Reviewer caution: Public audiences need interpretation limits more visibly than repository users.

#### 12.4.3 Public communication and leaderboard governance

- Rating: 3
- Evidence: Official site and Scale/SEAL page provide public results; paper states interpretation limits; HLE-Rolling update context is public [S01, S03, S06, S10].
- Missing evidence: Complete governance rules for submissions, stale scores, private-set use, and version comparability are incomplete.
- Rationale: Public communication is active and useful but not fully governed.
- Reviewer caution: Public HLE communication should consistently separate score, confidence, form, and claim limits.

### 12.5 Overall Quality of Reports, Leaderboards, Dashboards, and Public Claims

- Rating: 3
- Evidence: HLE reports accuracy, calibration error, category distinctions, and current model comparisons, with explicit AGI/autonomy caveats in the paper [S03, S06].
- Missing evidence: More complete raw traces, uncertainty labels, versioning, and public caveat repetition are needed.
- Rationale: Reporting quality is good for intended academic QA interpretation.
- Reviewer caution: Reports should not reduce HLE to a single rank or use it as standalone AGI evidence.

## Final Evaluation

### Evaluative Report of the Benchmark

Humanity's Last Exam is a strong benchmark for difficult closed-ended academic question answering under specified prompting and scoring conditions. Its main strengths are expert construction, broad academic content, public dataset access, explicit answer/confidence prompting, calibration reporting, public evaluation scripts, contamination-aware design choices, and explicit caveats against AGI or autonomous-research inference.

Its main weaknesses are reliability and validity gaps around item disagreement, model-judge scoring, prompt sensitivity, private-set documentation, exact reproduction of published runs, public contamination over time, and formal statistical comparison. These gaps do not show that HLE is poor. They define the limits of what HLE scores should be used to claim.

### Conclusions

| Conclusion | Reviewer judgment |
| :-- | :-- |
| Best-supported use | Comparing frontier language/multimodal systems on difficult closed-ended academic questions under documented HLE conditions. |
| Cautious secondary use | Diagnosing overconfidence, calibration failure, and domain-level weaknesses in expert academic QA. |
| Unsupported or weakly supported use | Standalone AGI measurement, autonomous research assessment, open-ended scientific creativity, agency, tool-use competence, deployment readiness, or broad cognitive versatility. |
| Overall MESA judgment | Strong public academic QA benchmark with good rationale/materials and meaningful caveats; validity and reliability are partial for fine-grained model ranking and broad capability claims. |

### Recommendations

1. Publish a consolidated score-reporting specification requiring dataset form, HLE variant, model version, prompt, sampling settings, judge model, and text-only/full-modality label.
2. Publish or summarize judge-validation evidence against human adjudication, including item-type-specific error rates and malformed-output handling.
3. Add repeated-run, prompt-sensitivity, and judge-sensitivity experiments for representative model cohorts.
4. Provide clearer private held-out-set governance: count, access model, usage policy, leak response, refresh policy, and score-reporting rules.
5. Make non-use guidance prominent on the dataset card and leaderboard: HLE is not standalone AGI, autonomy, or open-ended research evidence.
6. Maintain a versioned item-quality register that tracks corrected, disputed, retired, rolling, and verified items.
7. Report confidence intervals or minimum meaningful differences for leaderboard comparisons and category-level results.

### Summary of Ratings

| Section | Overall Rating (`n/a`, `0`-`4`) |
| :-- | :--: |
| Section 6. Rationale, documentation, and task/item quality | 3 |
| Section 7. Benchmark materials and usability | 3 |
| Section 8. Reference points and documented comparison groups | 2 |
| Section 9. Reliability and precision | 2 |
| Section 10. Validity support | 2 |
| Section 11. Fair use and comparability | 2 |
| Section 12. Reports, leaderboards, and public score claims | 3 |

### Gap Register

| Missing or inaccessible information needed for interpretation | Affected entity or reporting surface | Affected capability domain or score interpretation | Affected rating(s) | Why it matters | Needed for a higher rating |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Complete private held-out-set documentation | HLE private set and any private/public score reporting | Contamination control, overfitting checks, score comparability | 5.5, 5.8, 10.5, 11.3 | Hidden sets improve integrity but reduce auditability unless governance is clear. | Public count, access policy, leak response, refresh rules, and score-use rules. |
| Model-judge validation against human adjudication | HLE scorer/judge path | Accuracy and calibration validity | 6.2, 7.1, 9.3, 10.3 | Short-answer correctness can depend on judge behavior. | Item-type-specific validation, scorer fixtures, disagreement analysis, and judge-version policy. |
| Repeated-run and prompt-sensitivity evidence | Public HLE evaluation and leaderboard results | Reliability, rank interpretation, confidence calibration | 9.2, 9.4, 12.2 | Model answers and confidence can vary across prompts/settings. | Repeated runs, prompt variants, seed/sampling records, and minimum meaningful difference guidance. |
| Full raw outputs and trace bundles for published scores | Paper result tables and Scale/SEAL page | Reproducibility and auditability | 7.1, 9.3, 12.2, 12.3 | Users cannot fully audit every reported model score. | Versioned raw outputs, judge outputs, prompts, model versions, and run configs. |
| Per-item quality and verification status | Public 2,500-item dataset | Item quality, subject/category subscores, expert disagreement | 6.1, 9.3, 10.1, 10.2 | Expert disagreement and HLE-Verified critique indicate non-trivial item uncertainty. | Item-level audit status, difficulty/discrimination metadata, corrected/disputed item register. |
| Formal human baseline | HLE reference interpretation | Expert-level claims and human-model comparison | 8.1, 10.4 | Expert contribution is not equivalent to a controlled full human performance baseline. | Controlled human solve cohort, human uncertainty, and domain/subset baselines. |
| Static/rolling/version comparability policy | Static HLE, HLE-Rolling, current leaderboard | Temporal comparability and maintenance | 5.8, 9.4, 11.3, 12.1 | Rolling updates can change score meaning over time. | Version labels, changelog semantics, bridging studies, stale-score policy. |
| Public-facing non-use guidance across all surfaces | Dataset card, official site, leaderboard | AGI/autonomy interpretation and public claims | 10.6, 11.5, 12.3, 12.4 | Paper caveats may not reach leaderboard users. | Prominent caveats on result surfaces and dataset cards. |

## Bibliography

1. CAIS and Scale AI. "Humanity's Last Exam." https://lastexam.ai/. Accessed 2026-05-17.
2. Center for AI Safety. "HLE GitHub repository." https://github.com/centerforaisafety/hle. Accessed 2026-05-17.
3. Long Phan et al. "Humanity's Last Exam." arXiv:2501.14249. https://arxiv.org/abs/2501.14249. Accessed 2026-05-17.
4. Long Phan et al. "Humanity's Last Exam." Nature. https://www.nature.com/articles/s41586-025-09962-4. Accessed 2026-05-17.
5. Hugging Face. "cais/hle." https://huggingface.co/datasets/cais/hle. Accessed 2026-05-17.
6. Scale AI / SEAL. "Humanity's Last Exam." https://labs.scale.com/leaderboard/humanitys_last_exam. Accessed 2026-05-17.
7. Center for AI Safety. "simple-evals." https://github.com/centerforaisafety/simple-evals. Accessed 2026-05-17.
8. Center for AI Safety. "hle-rolling-changes.txt." https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt. Accessed 2026-05-17.
9. Tanishq Shankar et al. "Humanity's Last Exam is Still Hard to Pass." arXiv:2602.13964. https://arxiv.org/abs/2602.13964. Accessed 2026-05-17.
10. MESA repository. `MESA EFPA template official.md`. Accessed 2026-05-17.
11. MESA repository literature corpus. `literature/betterbench.md`, `literature/Measuring_what_Matters.md`, and `literature/A_Definition_of_AGI.md`. Accessed 2026-05-17.
