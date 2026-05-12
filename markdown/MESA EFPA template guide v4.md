# MESA EFPA Template User Guide v4

This guide explains how to use `markdown/MESA EFPA template v2.md`. It is a companion document, not a replacement for the template. Use the same section numbers to move between the two files.

MESA treats an AI benchmark as a measurement instrument. Part A describes what the benchmark is and what the sources say. Part B evaluates whether the benchmark supports its stated interpretation. Keep those two activities separate: do not put ratings in Part A, and do not make unsupported judgments in Part B.

V4 keeps the fixed example bank, adds supplemental anchors for newer benchmark surfaces, and makes each template section's purpose explicit. Inline examples use short source tags from the Benchmark Example Bank or Supplemental Anchor Bank below. Rankings, model counts, live leaderboard positions, and current model names are date-sensitive; use them only when the review date and source snapshot are recorded. Part B rating examples are illustrative patterns only, not new review ratings for the named benchmarks.

## Benchmark Example Bank

Use these compact profiles to keep option tables readable. The tag in the first column is the short source tag used in later examples.

| Tag | Benchmark profile | Stable facts to reuse | Source anchor |
| :--- | :--- | :--- | :--- |
| HLE | Humanity's Last Exam | Public repository documents HLE as a multimodal closed-ended academic benchmark with 2,500 questions across dozens of subjects, multiple-choice and short-answer formats, a Hugging Face dataset link, MIT license, canary string, simple evaluation scripts, contact channel, and accuracy plus calibration reporting. The local HLE pilot remains the strongest source for MESA caution examples about expert-level academic claims and AGI overinterpretation. | https://github.com/centerforaisafety/hle |
| ARC-AGI-2 | ARC-AGI-2 | Grid-based abstract-reasoning tasks ask systems to infer transformations from demonstrations and apply them to novel test inputs, with pass@2-style scoring. Epoch summarizes 1,360 tasks total: 1,000 training tasks and 360 evaluation tasks split evenly across public, semi-private, and private sets. ARC Prize describes first-party human testing, public/private/semi-private calibration goals, and AGI-relevant claims that require broad-claim caution. | https://arcprize.org/blog/arc-agi-2-technical-report; https://epoch.ai/benchmarks/arc-agi-2 |
| MMMU-Pro | MMMU-Pro | Robust multimodal academic benchmark derived from its predecessor by filtering text-only-answerable questions, augmenting candidate options, and adding a vision-only input setting where questions are embedded in images. Useful for image/text integration, robust multimodal understanding, and harder academic VQA examples. | https://huggingface.co/papers/2409.02813 |
| ScreenSpot-Pro | ScreenSpot-Pro | Public repository describes GUI grounding for professional high-resolution computer use, with paper, Hugging Face dataset, leaderboard link, evaluation scripts, shell runners, and MIT license. Useful for high-resolution UI perception, coordinate/click-style grounding, GUI terminology, and computer-use accessibility notes. | https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding |
| Video-MMMU | Video-MMMU | Project page describes 300 expert-level educational videos, 900 human-annotated questions across six disciplines, three stage-aligned tracks (Perception, Comprehension, Adaptation), and a knowledge-gain metric for improvement after watching relevant videos. Useful for temporal input, video-as-knowledge-source, and stage-specific subscores. | https://videommmu.github.io/ |
| SWE-Bench Verified | SWE-Bench Verified | Official page describes a human-filtered subset of 500 SWE-Bench Verified instances created with OpenAI, with annotators checking problem clarity, test-patch correctness, and solvability. It supports coding-agent examples involving real repositories, issue resolution, patches, hidden tests, agent scaffolds, and leaderboard/version notes. | https://www.swebench.com/verified.html |
| tau2-bench | t2-bench / tau2-bench | The tau-bench paper evaluates tool-agent-user interaction through dynamic user-agent conversations, API tools, policy guidelines, and final database-state comparison to an annotated goal state. tau2-bench adds a dual-control setting where both user and agent can act with tools in a shared dynamic environment. The GitHub repository provides docs, domains, CLI, leaderboard submission paths, changelog, and MIT license. | https://github.com/sierra-research/tau2-bench; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2506.07982 |
| Vending-Bench 2 | Vending-Bench 2 | Andon Labs describes a one-year simulated vending-machine business where agents start with a $500 balance, pay a $2 daily fee, search/contact suppliers, manage orders, inventory, pricing, deliveries, storage, and customer sales, and are scored by final bank balance averaged across runs. Useful for long-horizon agency, stateful decisions, tool use, memory, and economic-environment caveats. | https://andonlabs.com/evals/vending-bench-2 |
| FACTS | FACTS Benchmark Suite | Google DeepMind describes a four-part factuality suite covering Grounding v2, Parametric, Search, and Multimodal factuality, with public and private held-out sets, Kaggle management, public leaderboard, and a suite score averaged across the four benchmarks. The public FACTS Grounding examples include context-grounded long-form tasks and evaluation prompts. | https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/; https://www.kaggle.com/datasets/deepmind/FACTS-grounding-examples |
| Global PIQA | Global PIQA | Hugging Face paper page describes a participatory physical-commonsense benchmark covering 116 language varieties across five continents, 14 language families, and 23 writing systems, constructed by 335 researchers from 65 countries. The non-parallel split emphasizes local foods, customs, traditions, and culturally specific commonsense. | https://huggingface.co/papers/2510.24081 |
| WritingBench | Generative writing, style/format/length criteria, writing domains. | Open-source writing benchmark with real-world writing queries across multiple domains and criteria-aware scoring. | https://github.com/X-PLUG/WritingBench |
| Doolittle | Academic writing formalization and text-style transfer. | EMNLP benchmark/corpus for paragraph-level academic writing formalization. | https://aclanthology.org/2023.emnlp-main.809/ |
| SafetyBench | Text safety, bilingual safety categories, risk-oriented multiple choice. | Benchmark for LLM safety evaluation across safety concern categories in Chinese and English. | https://github.com/thu-coai/SafetyBench |
| OmniSafetyBench | Audio-visual or cross-modal safety. | Safety benchmark for omni-modal models across text, image, video, audio, and modality combinations. | https://omni-safetybench.github.io/ |
| ERQA | Embodied reasoning, spatial reasoning, robotics-oriented VQA. | Multimodal embodied reasoning questions focused on real-world robotics scenarios. | https://github.com/embodiedreasoning/ERQA |
| WorldArena | Embodied world models and functional/perceptual world-model evaluation. | Benchmark for evaluating embodied world models across perceptual and functional dimensions. | https://world-arena.ai/ |
| WorldPrediction | World modeling and long-horizon procedural planning. | Video-based benchmark for high-level world modeling and procedural planning through action selection. | https://huggingface.co/papers/2506.04363 |
| NESTFUL | Nested API/tool-call sequencing. | Benchmark for executable nested sequences of API calls where outputs feed later calls. | https://research.ibm.com/publications/nestful-a-benchmark-for-evaluating-llms-on-nested-sequences-of-api-calls |
| Nested Learning | Continual learning, memory updates, nested optimization concepts. | Google Research describes nested learning as a continual-learning paradigm with nested optimization processes. | https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/ |

## Core Reviewer Rules

### Documentation Status Options

| Option | Meaning | Select when | Do not select when | Example |
| :--- | :--- | :--- | :--- | :--- |
| Documented | The source gives enough information to record the field confidently. | The official paper, repository, documentation, dataset card, or maintainer statement states the fact directly. | You inferred the fact from examples, screenshots, or common practice. | HLE documents a public set of 2,500 questions. [HLE] |
| Partially documented | Some information is present, but important details are missing or internally incomplete. | The source names a private set but omits its size, access process, or selection method. | The source is simply silent. [HLE] | HLE states a private held-out set exists but the local pilot notes that its count is not documented. [HLE] |
| Not documented | The available sources do not state the information. | No reviewed source gives random seeds, run cost, or a formal leaderboard. | The issue is irrelevant to this benchmark type. [HLE] | If no reviewed source states a leaderboard, mark leaderboard status as not documented rather than assuming one exists; HLE sources document paper-style result tables but no formal leaderboard. [HLE] |
| Not applicable | The field does not apply to the benchmark or intended use. | A text-only benchmark has no audio-output requirement. | The field could apply but evidence is missing. | "Video output" is not applicable for HLE multiple-choice text questions. [HLE] |
| Unclear from available sources | The sources contain ambiguity, conflict, or wording that prevents a confident classification. | Two sections give different judge model versions, or a website implies but does not state a submission process. | The evidence is merely incomplete but not ambiguous. | The HLE pilot treats exact scorer-version evidence as partly unclear because local source statements differ. [HLE] |

### Part A vs Part B

Part A records claims and evidence. "The benchmark reports category accuracy" is Part A. "The category accuracy is too coarse for the claim" is Part B.

Part B rates adequacy. Each rating must include evidence used, missing evidence, reviewer rationale, and interpretation caution. Missing documentation is an evidence gap. It is not proof of poor benchmark quality unless a source-grounded defect is shown.

### Broad Claims and Narrow Evidence

If a benchmark claims "general intelligence", "AGI", "reasoning", "agency", "autonomy", or "expert capability", record the claim in the relevant Part A fields, especially 2.1, 2.5, 3.7, Appendix A, and source notes. Do not use a separate broad-claim screen in v4. Part B validity and final evaluation should later judge whether the measured domains, sub-abilities, modalities, tools, planning, memory, and speed support the broad interpretation. HLE is a useful example: it can support a narrow description of expert-level closed-ended academic performance, but the pilot records explicit caution against treating HLE accuracy alone as proof of AGI or autonomous research ability.

### Available vs Required

"Available" means the benchmark supports or permits something. "Required" means the benchmark cannot be run as intended without it. SWE-Bench Verified uses coding-agent harnesses and environment setup, ScreenSpot-Pro needs high-resolution GUI screenshots and grounding output, and tau2-bench requires domain tools for agent actions. [SWE-Bench Verified; ScreenSpot-Pro; tau2-bench]

### Public, Restricted, Hidden, and Not Available

| Access label | Meaning | Example |
| :--- | :--- | :--- |
| Public | Anyone can inspect or download the component under stated terms. | SWE-Bench Verified public dataset and evaluation harness. [SWE-Bench Verified] |
| Restricted | Access exists but requires approval, account access, payment, license agreement, or submitter status. | FACTS private leaderboard evaluation is managed through Kaggle rather than fully downloadable for independent inspection. [FACTS] |
| Hidden | The component exists but is intentionally concealed to protect evaluation integrity. | ARC-AGI-2 includes private and semi-private evaluation sets. [ARC-AGI-2] |
| Not available | The component is not released or no source indicates it exists. | HLE reviewed sources do not document public raw model outputs. [HLE] |

### Baseline, Comparator, Threshold, Floor, and Ceiling

| Term | Meaning | Example |
| :--- | :--- | :--- |
| Baseline | A reference performance level used to interpret scores. | ARC-AGI-2 reports first-party human testing as a reference point for task solvability. [ARC-AGI-2] |
| Comparator | A system, human group, benchmark version, or cohort used for comparison. | GPT-4O, Claude, expert humans, or a prior benchmark. [HLE] |
| Threshold | A decision boundary or score band with an intended interpretation. | Structural note: use this only when the reviewed source defines a cutoff or score band; safety thresholds need a safety source. |
| Floor | The lowest expected performance level under trivial or chance behavior. | HLE four-choice questions have a non-zero chance floor. [HLE] |
| Ceiling | The upper end where the benchmark stops distinguishing systems well. | HLE is motivated by saturation of earlier academic benchmarks; record a ceiling only when the reviewed HLE source documents it. [HLE] |

## Information Sources

Purpose: build the evidence inventory before filling the review. This table answers "what did the reviewer inspect?" It should not duplicate every detail later recorded in Section 1; it should provide enough source traceability that later facts, gaps, and ratings can be checked.

Use this table to record the evidence base before filling the template.

| Source type | Meaning and use | Example |
| :--- | :--- | :--- |
| Official paper or technical report | Main author-provided description of purpose, data, methods, scoring, and results. Prefer this before commentary. | HLE paper linked from the HLE GitHub repository. [HLE] |
| Benchmark website | Public landing page, documentation hub, access portal, or official result page. | FACTS Benchmark Suite blog, Kaggle pages, or leaderboard page. [FACTS] |
| Repository | Code, issues, releases, examples, scripts, and maintenance activity. | SWE-Bench Verified GitHub repository with evaluation harness and Docker setup. [SWE-Bench Verified] |
| Dataset card or data host | Dataset metadata, splits, licenses, provenance, access restrictions, and versioning. | HLE Hugging Face dataset card or FACTS public examples on Kaggle. [HLE; FACTS] |
| Leaderboard or results page | Ranking, submission rules, public scores, update dates, and system metadata. | FACTS leaderboard with model submissions. [FACTS] |
| Evaluation harness or package | Runnable code, package, CLI, scorer, or platform used for evaluation. | tau2-bench CLI commands or HLE simple evaluation scripts. [tau2-bench; HLE] |
| Documentation or user guide | Setup, submission, interpretation, scoring, and troubleshooting instructions. | SWE-Bench Verified docs and README quick-start/evaluation pages. [SWE-Bench Verified] |
| Release notes or changelog | Version history, refresh policy, retired tasks, score comparability notes. | HLE-Rolling notes or tau2-bench changelog/version history. [HLE; tau2-bench] |
| Maintainer statements | Authoritative clarifications from issues, discussions, papers, or official posts. | SWE-Bench Verified page notes about bash-only setup and mini-SWE-agent release comparability. [SWE-Bench Verified] |
| Independent sources used for context | Non-official sources used to interpret background, not to replace official facts. | Structural note: use BetterBench-style critique literature for contamination or maintenance context, not as a substitute for official benchmark facts. |

## Part B Rating Scale

| Rating | Meaning | Use carefully |
| :--- | :--- | :--- |
| `n/a` | The criterion is not applicable to this benchmark or intended use. | Use only when the criterion truly does not apply, such as audio-output quality for HLE. [HLE] |
| `0` | Cannot rate because available evidence is insufficient. | Use for evidence gaps. Do not treat this as a quality defect by itself. [HLE] |
| `1` | Inadequate evidence or practice for the intended interpretation. | Use when evidence shows weak, unsuitable, or misleading practice. [HLE] |
| `2` | Adequate for cautious use within a clearly bounded interpretation. | Use when the benchmark can support limited use but has notable gaps. [HLE] |
| `3` | Good evidence or practice with meaningful but non-fatal gaps. | Use when evidence is strong enough for intended use, while caveats remain. [HLE] |
| `4` | Excellent evidence or practice, comprehensive and well matched to intended use. | Reserve for broad, current, well-documented, and independently usable evidence. [HLE] |

Every Part B row has five required concepts: the criterion being rated, the rating, evidence used, missing evidence, reviewer rationale, and interpretation caution. A bare number is not a MESA rating.

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Information

Purpose: identify the review event, not the benchmark itself. Keep this section to reviewer identity, review dates, review scope, and a pointer to the Information Sources table.

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Reviewer | Person or team completing the review. | "MESA reviewer" or named reviewers. Structural field, not benchmark-specific. |
| Date of current review | Date the evidence was reviewed, not necessarily publication date. | `2026-05-04`. [HLE] |
| Date of previous review, if applicable | Earlier review date if this is an update. | `2026-05-01` for an HLE pilot refresh. [HLE] |
| Review scope | Boundary of the review. State whether it covers Part A only, full Part A/B, local working copies, or online artifact verification. | "Full Part A/B review using the HLE GitHub repository plus a local paper-equivalent working copy." [HLE] |
| Sources reviewed | Short list or pointer to the Information Sources table. | "HLE GitHub repository; HLE paper-equivalent working copy for evidence extraction." [HLE] |

### 1.2 Benchmark Information

Purpose: identify the benchmark's official identity, provenance, ownership, version, release status, and citation record. Do not use this section for artifact access details; those belong in 1.3.

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark name | Full official name. | "Humanity's Last Exam." [HLE] |
| Short name or acronym | Abbreviation used in papers, leaderboards, or code. | "HLE." [HLE] |
| Benchmark version, edition, or release | Version number, release tag, edition, date-stamped release, or note that no version is stated. | "Original public set; no version number documented." [HLE] |
| Original benchmark name, if this is an adaptation | Source benchmark if this review covers a translated, modified, or domain-specific version. | "HLE-Pro adaptation" for a derivative benchmark. [HLE] |
| Benchmark creators or authors | Original authors, organizers, contributors, or institution. | HLE organizing team. [HLE] |
| Current maintainers | People or group responsible now. | Repository maintainers, benchmark organization, or "not documented." [SWE-Bench Verified] |
| Host organization, publisher, or distributor | Entity distributing the benchmark or platform. | University lab, Scale AI, Hugging Face, Papers with Code. [HLE] |
| Date of original release | First public release date. | Paper publication date or repository release. [SWE-Bench Verified] |
| Date of current release or revision | Date of the version reviewed. | Latest GitHub release date. [HLE] |
| License or access terms | Legal usage terms, dataset license, submission rules, or "not documented." | MIT license documented in the HLE GitHub repository. [HLE] |
| Persistent identifier, citation, or DOI | DOI, arXiv ID, citation, permanent URL, or dataset identifier. | arXiv ID for a HLE benchmark paper. [HLE] |

### 1.3 Public Artifacts

Purpose: separate artifact existence and access status from quality. Record what materials exist, where they are, and whether they are public, restricted, hidden, unavailable, or unclear. Part B later evaluates adequacy.

Use this table to separate artifact existence from artifact quality. Part B evaluates adequacy later.

| Artifact | Means | Access status examples | Notes example |
| :--- | :--- | :--- | :--- |
| Paper or technical report | Formal benchmark description and results. | Available, missing, restricted. [HLE] | "Local paper-equivalent working copy used for review; cite the public repository or paper link." [HLE] |
| Benchmark website | Official public site or documentation hub. | Stated but not verified, available, missing. [FACTS] | "Website named in paper." [FACTS] |
| Code repository | Source code for data, evaluation, or scoring. | Public, private, not documented. [SWE-Bench Verified] | "Repository not identified in reviewed sources." [SWE-Bench Verified] |
| Evaluation harness | Runnable evaluator, package, or hosted submission system. | Public package, hosted only, not documented. [HLE] | "Simple evaluation scripts are public in the HLE repository; full published-score replication still needs caution." [HLE] |
| Dataset or task set | Prompts, items, episodes, environments, or tasks. | Public, restricted, hidden, partially documented. [HLE] | "Public 2,500-question set." [HLE] |
| Prompt set | Exact prompts or prompt templates. | Included in paper, in repo, not documented. [HLE] | "Evaluation prompt in appendix." [HLE] |
| Rubric or scoring guide | Answer keys, grading rubrics, judge prompts, unit tests. | Available, partially documented, hidden. [SWE-Bench Verified] | "Model-judge prompt documented." [SWE-Bench Verified] |
| Leaderboard | Public or private ranking and submission record. | Public leaderboard, paper tables only, not documented. [FACTS] | "HLE sources reviewed document paper-style result tables but no formal leaderboard." [HLE] |
| Changelog or release notes | Version history and update policy. | GitHub releases, paper appendix, missing. [SWE-Bench Verified] | "HLE-Rolling notes." [SWE-Bench Verified] |
| Contact or issue channel | Maintainer contact, issue tracker, email, forum. | GitHub issues, email, not documented. [SWE-Bench Verified] | "Issue channel not found." [SWE-Bench Verified] |

## Section 2. Classification

Purpose: classify the benchmark's claimed measurement target, intended use, intended systems, users, tasks, inputs, response modes, evaluation conditions, technology, versions, and scoring evidence sources. Classification is descriptive. Do not decide whether the choices are good until Part B.

### 2.1 Claimed Capability Domains

Purpose: record the capability or phenomenon the benchmark claims to measure. Select only domains claimed or clearly implied by benchmark documentation. If a broad term such as "AGI", "general intelligence", "reasoning", or "agency" appears, record the actual measured sub-abilities here and reserve adequacy judgments for Part B validity.

Use "Other" only for a documented domain that does not fit the list. If the benchmark name implies a domain but the paper never states it, note that ambiguity.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No clear capability claim is stated. | A dataset release gives tasks but no capability framing. [HLE] |
| General capability or intelligence | The benchmark claims broad overall capability, intelligence, AGI-relevant performance, or cross-domain cognitive breadth. | Abstract-reasoning tasks framed as AGI-relevant; Part B must still check breadth and depth. [ARC-AGI-2] |
| Broad knowledge | Tasks test factual, academic, commonsense, cultural, scientific, social, historical, or world knowledge. | Academic subject questions across many fields. [HLE] |
| Reading and language understanding | Tasks test reading, comprehension, entailment, summarization, grounding, or linguistic interpretation. | Long-context user requests whose answers must follow the provided document. [FACTS] |
| Writing or generation quality | Tasks judge style, coherence, creativity, rhetoric, helpfulness, domain writing, or long-form generation. | Real-world writing queries scored with instance-specific criteria. [WritingBench] |
| Mathematics | Tasks target arithmetic, algebra, geometry, proof, probability, calculus, contest math, or quantitative reasoning. | Mathematics subject questions or math problem solving. [HLE] |
| On-the-spot reasoning | Tasks claim inference, deduction, induction, puzzle solving, theory of mind, planning, or novel problem solving without relying only on memorized schemas. | Grid abstraction tasks requiring inferred transformations. [ARC-AGI-2] |
| Working memory | Tasks require maintaining, manipulating, or updating information across text, audio, visual, or cross-modal input within an episode. | Long video or multi-turn tasks that require tracking prior details. [Video-MMMU] |
| Long-term memory storage or retrieval | Tasks require durable learning from prior experience, personalization, episodic recall, retrieval fluency, or hallucination-resistant recall. | Continual-learning or personalization evaluations should name the memory mechanism and time scale. [Nested Learning] |
| Speed or processing fluency | Tasks claim latency, throughput, reaction time, perceptual speed, reading speed, writing speed, or movement/pointer fluency as part of the capability. | Speed-sensitive computer-use or reaction-time tasks should report timing conditions. [ScreenSpot-Pro] |
| Coding or software engineering | Tasks target code generation, repair, tests, repositories, or software tasks. | SWE-Bench Verified-style issue resolution. [SWE-Bench Verified] |
| Scientific, engineering, or technical expertise | Tasks require STEM, engineering, laboratory, technical system, or scientific-method expertise. Use this when the domain is technical rather than professional-service oriented. | Physics, chemistry, biology, engineering, or research-method tasks. [HLE] |
| Domain-specific professional expertise | Tasks target law, medicine, finance, cybersecurity, business, clinical, or other professional practice domains. Use this when the benchmark frames the domain as a profession or applied role. | Medical, legal, financial, or cybersecurity task families. [HLE] |
| Requirements engineering or specification work | Tasks evaluate eliciting, checking, repairing, translating, or validating requirements, specifications, acceptance criteria, or formal/technical requirements. | Requirements verification or specification-repair tasks. [Structural anchor] |
| Multimodal perception | Tasks require interpreting images, charts, diagrams, documents, screens, or mixed media. | Image/text integration and a vision-only setting. [MMMU-Pro] |
| Visual or spatial processing | Tasks target visual reasoning, mental rotation, spatial scanning, navigation memory, multi-view reasoning, embodied perspective shifts, or spatial awareness. | Embodied reasoning questions about trajectories, actions, and spatial state. [ERQA] |
| Audio or speech | Input or output requires speech, audio events, transcription, voice, rhythm, music, spoken dialogue, or auditory reasoning. | Audio-visual safety tasks or speech-recognition tasks. [OmniSafetyBench] |
| Video understanding | Tasks require interpreting temporal visual content. | Video-MMMU video question answering. [Video-MMMU] |
| Tool use | Systems must call calculators, search, APIs, code tools, or other external tools. | tau2-bench evaluates agents that use domain API tools in conversation. [tau2-bench] |
| Nested tool or API sequencing | Tasks specifically require multi-step tool calls where outputs from earlier calls feed later calls. | Executable nested API-call sequences. [NESTFUL] |
| Planning, agency, or long-horizon reasoning | Tasks require multi-step goal pursuit, state tracking, delegation, autonomous action, long-horizon planning, or delayed consequences. | Stateful business decisions over a simulated year. [Vending-Bench 2] |
| Web or browser interaction | Systems navigate websites or browser UIs. | ScreenSpot-Pro uses GUI screenshots and grounding targets for computer-use perception. [ScreenSpot-Pro] |
| Embodied, robotic, or simulated environment interaction | Systems act in games, robotics simulators, virtual environments, physical robots, or real/external environments through sensors and actuators. | Robotics-oriented embodied reasoning or simulated business/environment interaction. [ERQA; Vending-Bench 2] |
| World modeling or environment dynamics | Tasks evaluate prediction of world state, action-conditioned dynamics, physical plausibility, future scene generation, or procedural planning in an environment. | Video-based world modeling and long-horizon procedural planning. [WorldPrediction] |
| Continual learning or adaptation | Tasks evaluate learning new information or policies over time without catastrophic forgetting, across episodes, versions, or nested update loops. | Nested learning and memory-update concepts. [Nested Learning] |
| Safety, risk, refusal, or policy compliance | Tasks evaluate harmful-content handling, risk recognition, refusal, jailbreak robustness, cross-modal safety, or policy adherence. | Safety concern categories or audio-visual harmful-input handling. [SafetyBench; OmniSafetyBench] |
| Robustness | Tasks test performance under perturbations, distribution shift, adversarial prompts, prompt permutations, noisy audio, visual transformations, or other stressors. | Candidate-option augmentation, text-only filtering, and vision-only settings designed to reduce shortcut solving. [MMMU-Pro] |
| Calibration or uncertainty | Scores include confidence, uncertainty, abstention, or calibration. | HLE reports RMS calibration error. [HLE] |
| Other: | A documented domain is not represented above. | "Molecular design" or another named domain, if the source treats it as distinct. |

### 2.2 Area of Use

Purpose: record what the benchmark outputs are meant to be used for. This differs from 2.4, which records who interprets or acts on those outputs.

Select only documented or clearly implied use contexts. Do not treat publicity around a benchmark as an intended measurement use unless the benchmark documentation explicitly frames it that way.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | The source does not state intended use. | A bare dataset card lists files without intended-use framing. [HLE] |
| Model comparison | Compare systems under similar conditions. | Comparing GPT, Claude, Gemini, and open-weight models. [HLE] |
| Leaderboard ranking | Rank scored systems, submitted outputs, or endpoints publicly or privately. | FACTS public ranking table. [FACTS] |
| Capability profiling | Identify strengths and weaknesses across domains. | Category scores for math, coding, and science. [HLE] |
| Research diagnostics | Study model behavior, failure modes, or measurement properties. | FACTS supports analysis of factuality, grounding, retrieval, and multimodal factual QA failures. [FACTS] |
| Safety or risk evaluation | Assess risk, compliance, misuse, refusal behavior, jailbreak vulnerability, or harmful-content handling. | Bilingual or multimodal safety concern categories. [SafetyBench; OmniSafetyBench] |
| Release or deployment readiness gate | Decide whether a system is ready for release, deployment, or restricted access. Select only when the benchmark source explicitly supports gating; do not infer it from a leaderboard. | A release checklist that requires passing a documented safety or capability threshold. |
| Procurement or vendor comparison | Support buying, vendor, or enterprise model-selection decisions. | FACTS-style multi-provider vendor evaluation. [FACTS] |
| Internal regression testing | Track model changes across releases. | SWE-Bench Verified release-version regression suite for a product model. [SWE-Bench Verified] |
| Requirements engineering or specification support | Evaluate AI support for requirements elicitation, validation, traceability, specification repair, acceptance criteria, or formal requirements work. | Requirements verification or specification support studies. [Structural anchor] |
| Policy or governance analysis | Inform standards, regulation, independent audits, public-interest research, systemic-risk analysis, or institutional oversight. | Policy-facing use should be tied to documented claims and caveats, not headline rank alone. [HLE] |
| Other: | Any documented use outside the list. | Competition scoring, educational placement, benchmark construction research. |

### 2.3 Intended AI Systems

Purpose: record the systems for which the benchmark is intended, not every system that could technically be forced through the interface. Avoid expanding intended systems merely because a model could technically run.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No target system class is stated. | A benchmark lists tasks but no model target. [HLE] |
| Frontier general-purpose language models | Current high-capability general LLMs are target systems. | HLE evaluates frontier LLMs. [HLE] |
| Chat or instruction-following models | The evaluation assumes dialogue or instruction following. | Benchmarks using system/user prompts. [HLE] |
| Code models | Systems specialized for programming tasks. | SWE-Bench Verified evaluates coding agents and language models on issue resolution. [SWE-Bench Verified] |
| Multimodal models | Systems process more than one input modality, especially text plus images/audio/video. | HLE full-set evaluation with images. [HLE] |
| Audio or speech models | Speech-to-text, text-to-speech, audio QA, or spoken agents. | Mark only if the reviewed source evaluates audio or speech systems. [OmniSafetyBench] |
| Agentic systems | Systems that plan and act over multiple steps. | Vending-Bench 2 and tau2-bench both require agents to act across stateful interactions. [Vending-Bench 2; tau2-bench] |
| Tool-using systems | Systems expected to call external tools. | tau2-bench agents use domain API tools. [tau2-bench] |
| Embodied or robotic systems | Systems that perceive or act through physical or simulated sensors, actuators, robot policies, or embodied control loops. | Robotics-oriented embodied reasoning. [ERQA] |
| World models or environment simulators | Systems that predict, generate, or roll out environment dynamics, world states, scenes, or action-conditioned futures. | Embodied world-model or procedural-planning evaluation. [WorldArena; WorldPrediction] |
| Continual-learning or memory-augmented systems | Systems with persistent memory, online adaptation, personalization, nested update loops, or learning across episodes. | Continual-learning architectures or nested-learning systems. [Nested Learning] |
| Retrieval-augmented systems | Systems combine generation with retrieved documents. | FACTS Search evaluates factuality with a standardized search tool. [FACTS] |
| Domain-specialized models | Systems trained or adapted for a domain. | Structural note: HLE has domain-specific tasks, but only mark domain-specialized models if the source targets such systems. [HLE] |
| Open-weight local models | Locally runnable released-weight models are in scope. | Global PIQA reports cross-model comparisons that include open model families. [Global PIQA] |
| API-hosted models | Proprietary or hosted model APIs are in scope. | HLE evaluates named API-hosted frontier models in the local pilot. [HLE] |
| Other: | Another target class is documented. | Name the specific target system class when it falls outside the listed types. |

### 2.4 Intended Users of Benchmark Outputs

Purpose: record who is supposed to interpret or act on benchmark outputs. This differs from 2.2: 2.2 is the use context, while 2.4 is the user or stakeholder group.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No intended output users are named. | A repo with only tasks and scores. [HLE] |
| Benchmark creators or maintainers | Users who maintain, refresh, debug, or improve the benchmark. | HLE-Rolling maintainers. [HLE] |
| AI researchers | Academic or industry researchers studying model capability or measurement. | HLE researchers comparing graduate-level science reasoning performance. [HLE] |
| Model developers | Teams training, tuning, or evaluating models. | Lab evaluation team. [FACTS] |
| Product teams | Builders deciding product behavior or readiness. | SWE-Bench Verified release-version checks for code-model regressions. [SWE-Bench Verified] |
| Safety evaluators | Reviewers focused on harmful behavior, misuse, refusal, safeguards, or risk. | Safety benchmark users assessing risk categories or cross-modal safety behavior. [SafetyBench; OmniSafetyBench] |
| Policy or governance actors | Regulators, standards bodies, auditors, public-interest groups. | Policymakers mentioned in HLE framing. [HLE] |
| Procurement or enterprise decision-makers | Buyers choosing vendors or systems. | Enterprise AI platform selection. [HLE] |
| Educators or academic reviewers | Course, exam, or scholarly assessment users. | Academic review of a HLE benchmark paper. [HLE] |
| Public leaderboard users | General audience interpreting ranks. | Users reading a FACTS public leaderboard. [FACTS] |
| Other: | Any other intended recipient. | Competition organizers, domain boards, standards committees. |

### 2.5 Task Families, Subdomains, and Scores

Purpose: make the construct-to-task-to-score structure explicit. This section prevents vague capability labels from floating free of the actual task families, dataset partitions, metrics, and claim boundaries.

| Component | Meaning | Example |
| :--- | :--- | :--- |
| Claimed construct or phenomenon | What the benchmark says it measures. | Expert-level closed-ended academic capability. [HLE] |
| Construct subcomponents | Named parts of the construct. | Knowledge, reasoning, multimodal item comprehension, calibration. [HLE] |
| Task families or subdomains | Item categories or task groups. | Math, biology/medicine, physics, computer science/AI. [HLE] |
| Task sampling or selection logic | How tasks were chosen from a larger possible space. | Expert submissions, review, audits, searchability checks. [HLE] |
| Dataset/task partitions | Public/private, train/dev/test, easy/hard, domain, version, language, environment, or generated-task partitions. | Public set and private held-out set. [HLE] |
| Primary score | Main metric used for interpretation. | Accuracy percentage. [FACTS] |
| Subscores | Scores for components, domains, or task types. | Category accuracy. [HLE] |
| Derived or aggregate scores | Computed metrics beyond raw primary scores. | HLE calibration error or FACTS suite score. [HLE; FACTS] |
| Qualitative labels or bands | Labels attached to score ranges. | Structural note: use only if the source defines labels such as pass, expert, or risk bands. |
| Claim boundaries or caveats | Limits stated by authors. | HLE does not by itself establish AGI or autonomous research. [HLE] |

### 2.6 Model Response Mode

Purpose: record what the evaluated system must produce or do. For embodied, agentic, or world-model benchmarks, the response may be an action, trajectory, control signal, API sequence, generated scene, or environment state rather than a text answer.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Response format is not described. | No prompt or submission schema. [HLE] |
| Multiple choice | Choose one or more options. | HLE includes multiple-choice questions. [HLE] |
| Short text | Produce a brief answer, phrase, or value. | HLE includes short-answer questions with known solutions. [HLE] |
| Long-form text | Produce a paragraph, essay, report, or explanation. | FACTS Grounding evaluates long-form factual responses against provided context. [FACTS] |
| Structured output, such as JSON or XML | Output must follow a schema. | HLE prompts require structured answer and confidence fields, and the judge uses structured extraction. [HLE] |
| Code | Output source code, patches, SQL, or scripts. | SWE-Bench Verified issue-resolution benchmark. [SWE-Bench Verified] |
| Mathematical expression | Output formula, proof expression, or symbolic answer. | HLE can include closed-ended mathematical expressions as answers. [HLE] |
| Tool call | Emit tool-call syntax or structured tool invocation. | API tool call or nested function-call sequence. [tau2-bench; NESTFUL] |
| Browser or web action | Click, type, navigate, or inspect web pages. | ScreenSpot-Pro is a GUI grounding example where models identify UI targets for computer-use actions. [ScreenSpot-Pro] |
| File, document, or artifact generation | Produce files such as reports, spreadsheets, slides, or apps. | Name the reviewed artifact benchmark if applicable. |
| Image output | Generate or edit images. | Structural note: MMMU-Pro uses images as input; do not mark image output unless the reviewed benchmark asks the model to generate images. |
| Audio output | Generate speech, music, audio, or spoken interaction. | Voice or speech-generation evaluation. [OmniSafetyBench] |
| Video output | Generate or edit video. | Structural note: Video-MMMU is video understanding, not video generation. |
| Interaction in a simulated environment | Act in a game, simulator, robot simulator, world model, virtual environment, or synthetic business environment. | Simulated environment actions with final-state scoring. [Vending-Bench 2; WorldArena] |
| Interaction in a real or external environment | Act in real services, robots, live systems, external tools, or sensor/actuator loops. | Robot policy actions or live-service operations should be recorded only when explicitly part of the benchmark. [ERQA] |
| Sensorimotor or control output | Produce control signals, trajectories, spatial targets, actuator commands, or robot-action choices. | Embodied reasoning about trajectories or manipulation-relevant actions. [ERQA] |
| Other: | Any documented response mode not listed. | Database transaction, email draft, route plan, formal specification. [tau2-bench] |

### 2.7 Prerequisites for Evaluated Systems

Purpose: record prerequisites that affect whether a system can be evaluated as intended. These are not ratings; they document whether the source states needed capabilities, interfaces, or resources.

| Requirement | Meaning | Example |
| :--- | :--- | :--- |
| Language support | Languages the system must understand or produce. | HLE review instructions require English; Global PIQA is multilingual and culturally grounded. [HLE; Global PIQA] |
| Context length | Required prompt, document, or episode length. | FACTS Grounding uses context-grounded long-form tasks; record exact context limits only if the source states them. [FACTS] |
| Multimodal input support | Need to process images, audio, video, or files. | HLE full-set image questions. [HLE] |
| Audio or speech I/O | Need speech recognition, audio understanding, voice generation, or spoken interaction. | Cross-modal safety examples with audio inputs. [OmniSafetyBench] |
| Structured output support | Need to follow exact JSON/XML/schema/format. | Judge parser requires JSON. [HLE] |
| Tool access | Need calculators, code tools, APIs, search, or domain tools. | tau2-bench requires agents to act through domain tools. [tau2-bench] |
| Browser or internet access | Need live web browsing or network access. | FACTS Search uses a standardized search tool; Vending-Bench 2 lets agents search for suppliers. [FACTS; Vending-Bench 2] |
| Code execution | Need to run generated code or tests. | SWE-Bench Verified evaluates issue-resolution patches against tests. [SWE-Bench Verified] |
| Memory or persistent state | Need state across tasks or sessions. | Vending-Bench 2 requires state tracking over a simulated year. [Vending-Bench 2] |
| Continual-learning or update mechanism | Need online learning, memory consolidation, personalization, or nested update loops beyond ordinary context use. | Continual-learning systems should document what updates and what is held fixed. [Nested Learning] |
| Sensor access | Need cameras, microphones, proprioception, logs, telemetry, or environment observations. | Embodied or robotics benchmarks may require visual observations or sensor streams. [ERQA] |
| Actuator or control interface | Need robot actions, pointer movement, simulated controls, physical actuation, or action-policy APIs. | Computer-use, robot, or simulator tasks may require controlled actions rather than text answers. [ScreenSpot-Pro; ERQA] |
| Simulator or world-model interface | Need a specific simulator, environment, scene generator, physics engine, or world-model rollout interface. | Environment-dynamics or world-model benchmarks. [WorldArena; WorldPrediction] |
| API compatibility | Need a specific API interface or model-serving protocol. | OpenAI-compatible chat completions. [SWE-Bench Verified] |
| Latency or time budget | Need to respond within time limits. | Interactive benchmark with 30-second limit. [HLE] |
| Cost or compute budget | Need a budget constraint for fair comparison. | Cost-adjusted leaderboard. [FACTS] |
| Other: | Any other documented prerequisite. | Domain license, specialist hardware, private evaluator account. |

### 2.8 Evaluation Conditions

Purpose: record the conditions under which benchmark scores are produced. This includes prompts and sampling settings for language benchmarks, but also tools, simulators, sensors, actuators, safety constraints, and live-service boundaries for interactive or embodied evaluations.

| Condition | Meaning | Example |
| :--- | :--- | :--- |
| Prompting protocol | How prompts are presented and whether zero-shot, few-shot, chain-of-thought, or other protocols are used. | HLE pilot records zero-shot chain-of-thought prompts. [HLE] |
| System prompt | Required system/developer instruction. | "You are a helpful assistant; answer with JSON." [SWE-Bench Verified] |
| Few-shot examples | Examples included before test items. | Three solved examples before each task. [HLE] |
| Sampling settings | Temperature, top-p, seed, max tokens, decoding. | Temperature 0 or specified model settings. [SWE-Bench Verified] |
| Tool permissions | Which tools may be used and under what rules. | Browser allowed, calculator banned. [tau2-bench] |
| Sensor and observation rules | Which camera, microphone, file, screen, telemetry, or environment observations are available. | Robotics or embodied tasks should state what the system can perceive. [ERQA] |
| Actuator or action rules | Which robot, pointer, browser, API, simulator, or external actions are permitted. | Live-service or embodied actions should specify allowed controls and stopping conditions. [ScreenSpot-Pro; ERQA] |
| Time limits | Per-task or full-run limits. | 10 minutes per task. [HLE] |
| Human intervention rules | Whether humans can help, select retries, adjudicate, or repair outputs. | HLE uses human experts in item construction, not routine model answering. [SWE-Bench Verified] |
| Hardware or hosted service | Required GPU, local machine, cloud service, hosted platform. | SWE-Bench Verified Multimodal private test split evaluator. [SWE-Bench Verified] |
| Network requirements | Need for internet, offline operation, or restricted network. | FACTS Search uses a standardized search tool; Vending-Bench 2 may require web search for supplier discovery. [FACTS; Vending-Bench 2] |
| Real-world or live-service boundary | Whether actions occur in a sandbox, simulated service, private test service, public web, robot lab, or production-like environment. | Record live external effects only when the benchmark explicitly permits them. [tau2-bench] |
| Sandbox or security constraints | Isolation rules for code, tools, files, or external actions. | Code tasks run in Docker sandbox. [SWE-Bench Verified] |
| Safety or risk constraints | Harmful-content warnings, safe-completion rules, no-real-harm constraints, privacy controls, or restricted action policies. | Safety benchmarks should state whether refusals, compliance, or risk recognition are expected. [SafetyBench; OmniSafetyBench] |
| Other special conditions | Any other required condition. | Private holdout evaluation, hidden evaluator, special simulator version. [HLE] |

### 2.9 Task and Response Types

Selection-based responses ask the model to choose among given options.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Multiple choice, single correct answer | One option is correct. | HLE and Video-MMMU both include closed-ended choice items. [HLE; Video-MMMU] |
| Multiple choice, multiple correct answers | More than one option may be correct. | Structural note: select this only when the reviewed benchmark has true multi-answer items. |
| Ranking | Order options by preference, quality, risk, or relevance. | Safety or preference benchmarks may use ranked choices when the source states it. |
| Classification | Assign a label. | FACTS judge outputs can classify response eligibility and groundedness. [FACTS] |
| Pairwise preference | Choose better of two outputs or actions. | Use only when the task is explicitly pairwise. |

Production-based responses require generated content.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Open-ended text | Free-form answer or explanation. | FACTS Grounding evaluates long-form grounded responses. [FACTS] |
| Code generation | Source code, patch, tests, or scripts. | Function implementation. [SWE-Bench Verified] |
| Proof, derivation, or explanation | Step-by-step reasoning or justification. | Mathematical proof. [HLE] |
| Structured data | Schema-constrained output. | JSON extraction. [HLE] |
| Generated media | Image, audio, video, or other media. | Image generation task. [MMMU-Pro] |
| Artifact production | File or larger artifact. | Spreadsheet, report, app, or slide deck. [HLE] |

Interaction-based responses involve actions across steps.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Tool use | Calls external tools. | Calculator or search calls. [tau2-bench] |
| Browser or web navigation | Uses web UI actions. | Structural note: ScreenSpot-Pro covers GUI grounding; mark live navigation only if the reviewed benchmark requires it. [ScreenSpot-Pro] |
| API interaction | Calls APIs or services. | REST API task. [tau2-bench] |
| Computer-use interaction | Operates a desktop or GUI. | ScreenSpot-Pro evaluates GUI grounding for computer-use perception. [ScreenSpot-Pro] |
| Simulated environment task | Acts inside simulated environment. | Vending-Bench 2 simulates a vending-machine business. [Vending-Bench 2] |
| Real or external environment task | Interacts with live external systems. | Record only when the benchmark explicitly includes live services, robots, or external actions. |

Process data options record auxiliary evidence rather than final answers.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Response latency | Time to answer. | Structural note: record latency only if the source reports per-task or end-to-end timing. |
| Token usage | Prompt, completion, or total tokens. | HLE reports average completion token counts. [HLE] |
| Cost | API or compute cost. | Dollars per successful task. [tau2-bench] |
| Tool traces | Sequence of tool calls and outputs. | Browser actions or code execution logs. [tau2-bench] |
| Intermediate reasoning traces | Recorded reasoning or scratchpad traces. | Chain-of-thought trace, if collected. [HLE] |
| Execution logs | Runtime logs from code, environment, or evaluator. | Unit-test output. [HLE] |
| Other | Other process evidence. | Memory state, retry count. [HLE] |

### 2.10 Input Stimulus Type

Purpose: record what the benchmark gives to the system. Include files, screens, tools, environment state, sensor streams, or simulator observations when they are part of the task input.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Input type is unclear. | No prompt examples. [HLE] |
| Text | Natural language prompt or passage. | HLE text questions. [HLE] |
| Code | Source code, diffs, repositories, logs. | Code repair task. [SWE-Bench Verified] |
| Tables or structured data | CSV, JSON, database, table, chart data. | Table QA. [MMMU-Pro] |
| Images | Pictures, diagrams, screenshots, charts. | MMMU-Pro image/text tasks and ScreenSpot-Pro GUI screenshots. [MMMU-Pro; ScreenSpot-Pro] |
| Audio | Speech, sound, music, acoustic signal. | Audio or speech safety and recognition inputs. [OmniSafetyBench] |
| Video | Moving visual input. | Video understanding task. [Video-MMMU] |
| Documents | PDFs, Word files, slides, spreadsheets. | FACTS uses long context documents; artifact-heavy benchmarks should be named when reviewed. [FACTS] |
| Web pages | HTML pages or browser-rendered pages. | FACTS Search and Vending-Bench 2 may require web/search access; ScreenSpot-Pro covers UI screenshots rather than live page navigation. [FACTS; Vending-Bench 2; ScreenSpot-Pro] |
| APIs or tools | Tool schemas, API endpoints, external services. | tau2-bench tool-use benchmark. [tau2-bench] |
| Dynamic environment | State changes as the model acts. | Simulator, game, business environment, or world-model rollout. [Vending-Bench 2; WorldArena] |
| Sensor or actuator state | Camera, microphone, proprioceptive, telemetry, control, or robot-state input. | Embodied or robotics-oriented observations. [ERQA] |
| Other: | Any other stimulus. | Laboratory instrument stream, formal specification, CAD file. |

### 2.11 Number of Items or Measurement Points

Purpose: record the size of the measurement sample. For dynamic benchmarks, include episodes, generated tasks, trials, runs, or other measurement points instead of forcing a single item count.

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Total public items or tasks | Count inspectable by users. | HLE public 2,500 questions. [HLE] |
| Total private or hidden items | Count concealed from public. | Private held-out set count, if known. [HLE] |
| Development or example items | Items intended for practice, tuning, demonstration, prompt selection, or format familiarization. | Public examples used to show task format and expected submission structure. [FACTS] |
| Test items | Items used for reported scores. | Public test set or hidden leaderboard set. [FACTS] |
| Dynamic or generated tasks | Number or range of generated tasks. | A generator samples 200 tasks per run from a documented task grammar. [tau2-bench] |
| Episodes, trials, or measurement points | Repeated tasks, runs, trials, environment episodes, simulator rollouts, or robot trials. | 100 environment episodes or five repeated runs per task. [Vending-Bench 2] |
| Notes on item count uncertainty | Ambiguities, changing counts, or missing split counts. | "Private count not documented." [HLE] |

### 2.12 Mode of Evaluation

Purpose: record how evaluation is conducted and how much control the benchmark has over systems, outputs, traces, or endpoints submitted for scoring. Identity control means confidence that the evaluated model/version/system is what it claims to be. Condition control means confidence that prompts, tools, settings, hardware, timing, and environment match the intended protocol.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not indicated | Mode is not stated. | Paper reports results but no procedure. [HLE] |
| Local batch evaluation | User runs the benchmark locally over many items. | Python script evaluates a local model. [SWE-Bench Verified] |
| Hosted benchmark platform | Evaluation happens on an official platform. | FACTS accepts public models through its hosted process. [FACTS] |
| Leaderboard submission | Users submit systems, outputs, traces, endpoints, or metadata for ranked scoring. | Public leaderboard upload. [FACTS] |
| Private controlled evaluation | Maintainers evaluate hidden items or controlled conditions. | HLE private held-out evaluation. [HLE] |
| Public open evaluation | Anyone can run the benchmark on public materials. | Public dataset plus scorer. [HLE] |
| Interactive agent evaluation | Model acts step by step in a tool, browser, simulator, robot, world-model, or live-service environment. | Conversation/tool episodes or long-horizon simulated business runs. [tau2-bench; Vending-Bench 2] |
| Human-in-the-loop evaluation | Human input is part of evaluation. | HLE uses human expert review and audit during item development. [HLE] |
| Continuous or rolling evaluation | Tasks or results update over time. | HLE-Rolling or live leaderboard. [HLE] |
| Other: | Any other mode. | Competition event, private audit, physical lab run. |

Identity and condition controls:

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No control over systems, outputs, traces, or endpoints submitted for scoring | Maintainers cannot verify model identity, version, output provenance, or evaluation conditions. | Users self-report scores. [HLE] |
| Some control over systems, outputs, traces, or endpoints submitted for scoring | Some metadata, logs, submission checks, endpoint checks, or output-format checks exist. | Leaderboard requires model card, endpoint metadata, and run logs. [FACTS] |
| Controlled model access or audit | Evaluators can inspect or control model endpoint/version. | Private audit with fixed API access. [tau2-bench] |
| Controlled evaluation center or private harness | Evaluation happens in a controlled environment with fixed prompts, tools, settings, hardware, and hidden tasks. | Hosted hidden test harness. [HLE] |
| Not documented | Control mechanisms are not stated. | No submission policy found. [HLE] |

### 2.13 Technological Arrangements

Purpose: record the technology the benchmark supports and the technology it requires. Mark `A` when the technology is available or supported. Mark `R` when the benchmark cannot be run as intended without it. Some rows can be both available and required.

| Technology | Meaning | Example |
| :--- | :--- | :--- |
| API access | Benchmark supports or requires hosted model APIs. | FACTS multi-provider hosted API evaluation. [FACTS] |
| Local inference | Benchmark supports or requires local model serving. | Open-weight model run. [HLE] |
| GPU | GPU required or supported. | Local multimodal model inference. [MMMU-Pro] |
| CPU-only execution | Can be run without GPU or requires CPU-only path. | Small text benchmark scorer. [HLE] |
| Docker or container | Containerized environment exists or is required. | Code execution benchmark. [SWE-Bench Verified] |
| Python package or CLI | Package or command-line evaluator exists or is required. | `pip install` benchmark runner. [SWE-Bench Verified] |
| Browser | Browser use is supported or required. | Structural note: ScreenSpot-Pro covers GUI grounding from screenshots; mark live browser only if the reviewed benchmark requires it. [ScreenSpot-Pro] |
| External tools | Calculators, search, compilers, databases, APIs. | tau2-bench tool-use benchmark. [tau2-bench] |
| Internet access | Live network access is supported or required. | FACTS Search uses a standardized search tool; Vending-Bench 2 agents may search for suppliers. [FACTS; Vending-Bench 2] |
| Simulator or environment runtime | A game, robot simulator, world-model runtime, environment server, or domain simulation is supported or required. | Simulated business or embodied world-model evaluation. [Vending-Bench 2; WorldArena] |
| Sensors or media capture | Cameras, microphones, screen capture, telemetry, or observation streams are supported or required. | Embodied reasoning or audio-visual safety tasks. [ERQA; OmniSafetyBench] |
| Actuators or control interface | Robot controller, GUI pointer, browser action API, or simulated actuator interface is supported or required. | Computer-use, embodied, or simulator tasks. [ScreenSpot-Pro; ERQA] |
| Proprietary platform | Official closed platform or private service. | FACTS public ranking platform. [FACTS] |
| Other: | Any other technology. | Name the specific simulator, API, platform, device, or formal verifier. |

Example A/R use: if a benchmark provides a Docker image but also allows manual local setup, mark Docker as `A` and explain it is optional. If the official scorer only runs inside Docker, mark Docker as `A` and `R`. If a hosted evaluator is the only accepted submission path, mark proprietary platform as `A` and `R`.

### 2.14 Time and Resource Requirements

Purpose: record documented estimates, not guesses. If the source gives only qualitative guidance, quote or summarize that guidance. If no estimate is stated, write "not documented."

| Activity | Meaning | Example |
| :--- | :--- | :--- |
| Setup | Installation, data download, account setup, environment prep. | "Docker image build takes about 20 minutes on the documented host" or "not documented." [SWE-Bench Verified] |
| Model inference or task completion | Time or compute for answering tasks. | "500 tasks at 30 seconds maximum each" or "full-run duration not documented." |
| Scoring | Time to parse, judge, execute tests, or aggregate results. | "Unit-test scoring averages 2 minutes per instance" or "scoring time not documented." [SWE-Bench Verified] |
| Human adjudication | Time for raters, experts, or reviewers. | "Two expert review rounds; reviewer-hours not documented." [HLE] |
| Analysis or reporting | Time to generate tables, dashboards, or error analysis. | "Leaderboard refresh runs nightly" or "report generation time not documented." [FACTS] |
| Full benchmark run | End-to-end total. | "Five repeated runs over 100 episodes" plus total wall time if stated. [Vending-Bench 2] |
| API or compute cost | Monetary or compute budget. | "Estimated API cost per full run: not documented" or "GPU-hours reported by source." |

### 2.15 Benchmark Forms, Versions, and Variants

Purpose: record benchmark forms, versions, and variants in free text. Mention public/private forms, development/test splits, short or long forms, language versions, modality-specific versions, domain subsets, rolling versions, deprecated versions, hidden forms, and archived forms when documented.

Useful prompts: What is each form called? Why does it exist? Are scores across forms claimed to be comparable? Is it active, planned, deprecated, hidden, public, or archived? Where is it documented? If equivalence is not stated, write "equivalence claim not documented" rather than inferring it.

### 2.16 Static or Dynamic Task Determination

Purpose: record how tasks are selected or generated. This is descriptive; Part B later evaluates whether the task determination supports comparability, contamination control, and intended interpretation.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static fixed task set | Same fixed items are used. | Public HLE set. [HLE] |
| Random sample from fixed pool | Each run samples from a fixed item pool. | Random 500 tasks from 10,000. [HLE] |
| Hidden test set selected by maintainers | Maintainers select concealed items. | Private leaderboard holdout. [FACTS] |
| Procedurally generated tasks | Tasks are generated by rules or programs. | tau2-bench includes a compositional task generator for diverse verifiable tasks. [tau2-bench] |
| Adaptive routing based on performance | Later tasks depend on earlier performance. | Use only when the task sequence actually adapts to model behavior. |
| Dynamic environment generation | Environment changes or is generated for each run. | Vending-Bench 2 has state that changes across simulated business days. [Vending-Bench 2] |
| World-model or simulator rollout | Task states are produced by action-conditioned simulator or world-model rollouts. | World-model benchmarks may generate future states or next-scene tasks. [WorldArena; WorldPrediction] |
| Continual-learning sequence | Tasks are ordered to test learning, adaptation, retention, or forgetting across time. | Continual-learning or nested-learning evaluations. [Nested Learning] |
| Rolling or periodically refreshed task set | Items are updated over time. | HLE-Rolling. [HLE] |
| Not explicitly stated | Task selection method is not described. | Paper omits sampling method. [HLE] |
| Other: | Other documented method. | Human-curated competition rounds. [HLE] |

### 2.17 Evidence Sources Used in Scoring

Purpose: record what evidence the scorer uses. This may be a final answer, trace, tool log, unit test, environment state, sensor/action log, human judgment, model judgment, or external verifier.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Model final answer | Final response is scored. | HLE final answer. [HLE] |
| Model intermediate trace | Reasoning or scratchpad affects scoring. | Record traces only when they are captured or scored. |
| Tool-use trace | Tool calls or logs affect score. | Agent trajectory scoring. [tau2-bench] |
| Nested API-call sequence | Ordered function calls, arguments, and dependencies among calls affect score. | Full-sequence match or executable call-sequence evaluation. [NESTFUL] |
| Code execution result | Code is run and outcome scored. | Unit tests for coding task. [SWE-Bench Verified] |
| Environment state | Final or intermediate environment state is scored. | tau-bench compares final database state to the annotated goal state; Vending-Bench 2 scores final bank balance. [tau2-bench; Vending-Bench 2] |
| Sensor, action, or trajectory log | Observations, actions, control outputs, spatial targets, or robot/simulator trajectories affect score. | Embodied or computer-use evaluations may score trajectories or target selection. [ERQA; ScreenSpot-Pro] |
| World-model rollout | Predicted future scene, state transition, physical plausibility, or generated environment dynamics are scored. | World-model or procedural-planning evaluations. [WorldArena; WorldPrediction] |
| Reference answer | Answer key is used. | HLE answer keys support automated grading. [HLE] |
| Unit test | Tests decide correctness. | Pass/fail code tests. [SWE-Bench Verified] |
| Human judge | Human rater scores output. | HLE uses human expert reviewers and auditors during item quality review. [HLE] |
| Model judge | AI judge scores or extracts correctness. | HLE model-judge scoring. [HLE] |
| Ensemble or panel adjudication | Multiple judges or raters are combined. | HLE item audits route disagreements among organizers, original authors, and auditors. [HLE] |
| External verifier | Independent tool or system checks correctness. | Theorem prover, compiler, database. [tau2-bench] |
| Other: | Other evidence. | Peer review score, formal proof artifact, safety incident label. |

## Section 3. Measurement and Scoring

Purpose: describe how benchmark inputs and model behavior become scores. Record the scoring pipeline, metrics, scale types, transformations, baselines, uncertainty, and documented metric-to-claim linkage. This section can describe missing evidence but should not rate adequacy.

### 3.1 Scoring Procedure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Scoring process is not described. | Scores are reported without scorer details. [HLE] |
| Automated exact-match scoring | String, option, or value is matched to an answer key. | HLE multiple-choice or exact-answer accuracy. [HLE] |
| Automated semantic or embedding-based scoring | Automated similarity or semantic metric scores responses. | Cite the actual scorer if used. |
| Unit-test or execution-based scoring | Output is executed or tested. | Code passes unit tests. [SWE-Bench Verified] |
| Rule-based scoring | Deterministic rules parse or score outputs. | Regex checks for valid format. [HLE] |
| Human rating | Human raters judge output quality or correctness. | Expert scoring of explanations. [HLE] |
| Model-as-judge scoring | A model scores, extracts, or adjudicates outputs. | HLE uses a model judge in the pilot. [HLE] |
| Pairwise preference scoring | Outputs are compared pairwise. | Which answer is better. [SWE-Bench Verified] |
| Hybrid automated and human scoring | Automated scoring plus human review. | Model judge with human adjudication of disputes. [HLE] |
| Leaderboard service scoring | Official service scores submissions. | Hidden hosted evaluator. [FACTS] |
| Manual adjudication | Humans resolve ambiguous or failed scoring cases. | Review malformed outputs. [HLE] |
| Other | Other scoring method. | External theorem prover. [HLE] |

Describe the scoring pipeline in order: input, model output, parser, judge or scorer, aggregation, invalid-response handling, and result reporting.

### 3.2 Scores and Metrics

| Score or metric | Meaning | Example |
| :--- | :--- | :--- |
| Primary score | Main score used to summarize benchmark performance. | HLE accuracy. [HLE] |
| Subscore | Score for domain, task family, modality, or condition. | HLE category accuracy. [HLE] |
| Derived score | Computed secondary metric. | HLE RMS calibration error or FACTS suite score. [HLE; FACTS] |
| Qualitative band | Score label or interpretation category. | Structural note: do not invent qualitative bands unless the benchmark source defines them. |

For invalid, missing, malformed, or refused responses, record whether they are scored as incorrect, excluded, retried, manually reviewed, or handled by a special parser.

### 3.3 Scale or Metric Types

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Raw score | Count or untransformed total. | 73 correct items. [HLE] |
| Accuracy | Proportion or percent correct. | HLE accuracy percentage. [HLE] |
| Success rate | Percent of tasks completed successfully. | ScreenSpot-Pro tasks completed. [ScreenSpot-Pro] |
| Pass rate or pass@k | Whether at least one of k attempts passes. | Coding pass@1, pass@10. [SWE-Bench Verified] |
| Unit-test pass rate | Percent of tests passed. | SWE-Bench Verified evaluates generated patches against tests. [SWE-Bench Verified] |
| Win rate | Percent of pairwise comparisons won. | Use only when pairwise comparison is part of the benchmark. |
| Elo or ranking score | Relative rating from pairwise or competition results. | Do not recast ordinary leaderboard rank as Elo. |
| Pairwise preference score | Score from head-to-head preference comparisons. | Use only when head-to-head preference comparisons are documented. |
| Reward or return | Accumulated environment reward. | Vending-Bench 2 uses final bank balance as a business-outcome score. [Vending-Bench 2] |
| Cost-adjusted score | Performance adjusted by cost. | Structural note: use only if the reviewed source reports cost-adjusted performance. |
| Rubric or criteria-aware score | Score from a rubric, dimension-specific criteria, or instance-specific criteria. | Writing quality scored against style, format, length, or query-specific criteria. [WritingBench] |
| Safety or risk score | Score for harmfulness, refusal, attack success, risk recognition, or safety consistency. | Conditional attack success, refusal, or safety-score style metrics. [OmniSafetyBench] |
| World-model, trajectory, or environment-dynamics score | Score for action-conditioned prediction, physical plausibility, final state, trajectory quality, or rollout utility. | Future-state prediction or environment-dynamics scoring. [WorldArena; WorldPrediction] |
| Calibration or uncertainty score | Measures confidence-quality relationship. | HLE RMS calibration error. [HLE] |
| Percentile or normalized score | Score transformed relative to group or scale. | Structural note: use only if the source defines the reference group or normalization method. |
| Threshold or decision index | Score used for pass/fail or categorization. | ARC-AGI-2 uses pass-style scoring; do not convert that into a deployment threshold without separate validation. [ARC-AGI-2] |
| Other | Benchmark-specific metric. | Video-MMMU includes a knowledge-gain metric for adaptation after watching videos. [Video-MMMU] |

### 3.4 Score Transformation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No transformation | Report raw metric directly. | Percent correct. [FACTS] |
| Linear transformation | Apply linear scaling. | Convert 0-1 to 0-100. [HLE] |
| Non-linear transformation | Apply non-linear formula. | Log-scaled reward. [HLE] |
| Normalization against baseline | Compare or scale relative to reference. | Score above random baseline. [HLE] |
| Weighting across subdomains | Domains contribute unequally. | FACTS top-level aggregation across documented scenarios or metrics. [FACTS] |
| Aggregation formula documented | Formula is fully stated. | Mean of domain accuracies with weights listed. [HLE] |
| Aggregation formula partially documented | Some formula details missing. | HLE pilot notes category weighting details are not fully specified in local source. [HLE] |
| Aggregation formula not documented | Aggregation is used but formula is absent. | Leaderboard total appears without method. [FACTS] |
| Not applicable | No transformation or aggregation issue applies. | Single unaggregated task score. [HLE] |

### 3.5 Reference Groups, Baselines, and Comparators

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No baseline or comparator documented | No reference performance is stated. | Standalone score only; record this as an evidence gap rather than inventing a comparator. Structural field. |
| Random or chance baseline | Expected performance from random behavior. | HLE four-choice chance floor. [HLE] |
| Human baseline | Non-expert or general human performance. | ARC-AGI-2 reports first-party human testing as a human reference. [ARC-AGI-2] |
| Expert human baseline | Qualified expert performance. | Video-MMMU includes a human expert comparison row in its public results. [Video-MMMU] |
| Model baseline | One or more model scores used as reference. | HLE reports a model comparator table with documented model versions in the local pilot. [HLE] |
| Previous model cohort | Earlier generation of models. | SWE-Bench Verified pages note versioned agent releases whose scores should not be compared across incompatible setups. [SWE-Bench Verified] |
| Commercial system comparator | Proprietary production systems. | FACTS reports results for multiple contemporary frontier systems through its leaderboard/suite. [FACTS] |
| Open-weight model comparator | Released-weight local models. | Global PIQA reports comparisons that include open and proprietary model families. [Global PIQA] |
| Domain-specific reference group | Specialized systems or experts. | HLE item development depends on subject-matter experts across academic domains. [HLE] |
| Other | Other comparator. | FACTS Grounding v2, Parametric, Search, and Multimodal can be compared as sub-benchmarks within the suite. [FACTS] |

For each `Comparator or baseline` row, record construction method, intended interpretation, and source. The template rows include `Random or chance baseline`, `Human baseline`, `Expert baseline`, `Model cohort`, `Prior benchmark or version`, and `Criterion threshold or floor/ceiling`. HLE compares several frontier models and references expert-level academic capability, but the pilot records limited quantified expert score-distribution evidence.

The comparator-construction table also has rows for `Prior benchmark or version` and `Criterion threshold or floor/ceiling`. Use `Prior benchmark or version` when the benchmark is interpreted against an earlier benchmark, previous release, or saturation claim. Use `Criterion threshold or floor/ceiling` when a score is interpreted against a pass level, chance floor, maximum score, saturation point, or other boundary.

### 3.6 Score Uncertainty and Stability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Confidence intervals | Interval estimates around scores. | 95 percent CI for accuracy. [HLE] |
| Standard errors | Standard error of score estimate. | SE for domain accuracy. [HLE] |
| Bootstrap intervals | Resampling-based uncertainty estimates. | Bootstrap CI over items. [HLE] |
| Multiple runs or seeds | Repeated runs under same or varied seeds. | Temperature-sensitive model repeated 5 times. [HLE] |
| Judge agreement statistics | Agreement among model judges or judge variants. | Cohen's kappa for judges. [HLE] |
| Human inter-rater agreement | Agreement among human raters. | Krippendorff's alpha. [HLE] |
| Sensitivity analyses | Checks for prompt, parser, model version, or condition sensitivity. | Prompt variant comparison. [SWE-Bench Verified] |
| Not reported | No uncertainty or stability evidence is reported. | Single score table only. [FACTS] |
| Other | Other stability evidence. | HLE pilot records expert disagreement rates and model non-determinism caveat. [HLE] |

### 3.7 Metric-to-Claim Linkage

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Why the primary metric was chosen | Rationale for metric fit. | Accuracy fits closed-ended HLE questions. [HLE] |
| Whether metric floors or ceilings are documented | Chance levels, saturation, max/min behavior. | HLE notes non-zero multiple-choice floor. [HLE] |
| Whether the metric may reward non-target behavior named by the source | Source-stated shortcuts or confounds. | Formatting, memorization, search, or judge artifacts. [tau2-bench] |
| Whether parsing, judge, or scorer validation is documented | Evidence scorer measures intended thing. | Judge prompt plus validation study. [HLE] |
| Whether score uncertainty affects claim interpretation | Whether uncertainty changes conclusions. | Confidence intervals overlap. [HLE] |
| Whether score differences are interpreted statistically | Whether rankings or differences use significance/uncertainty. | Statistical comparison of two models. [HLE] |
| Whether benchmark reports state what users should not infer | Explicit non-use or caveat statements. | HLE says high score alone does not imply AGI. [HLE] |

## Section 4. Benchmark Outputs and Reports

Purpose: describe what benchmark users see after evaluation: paper tables, leaderboards, dashboards, private reports, scorecards, raw outputs, logs, traces, caveats, and audience-specific reports. Record report design and transparency descriptively; Part B later evaluates whether reports support defensible interpretation.

### 4.1 Output Availability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Public leaderboard available | Ranked results are publicly accessible. | FACTS public ranking table. [FACTS] |
| Public aggregate scores available | Overall scores are public. | Paper table with overall accuracy. [HLE] |
| Public per-domain scores available | Domain or category scores are public. | HLE category results. [HLE] |
| Public per-item scores available | Item-level correctness is public. | CSV with each question result. [HLE] |
| Public raw model outputs available | Actual model responses are released. | JSONL completions. [SWE-Bench Verified] |
| Public traces or logs available | Tool, reasoning, execution, or environment logs are public. | Agent trajectory logs. [tau2-bench] |
| Private reports available only to submitters | Results are returned privately. | Hosted audit report. [HLE] |
| No formal report or leaderboard documented | Only informal or no reporting is found. | Results mentioned without artifact. [FACTS] |

### 4.2 Output Name or Description

Use one row per output artifact. Include paper tables, dashboards, downloadable files, leaderboards, private submitter reports, and API responses. "Public/private" should state who can see it.

### 4.3 Output Design or Presentation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static text report | Narrative report. | PDF or paper section. [HLE] |
| Tables | Tabular scores. | HLE result tables. [HLE] |
| Graphs or visualizations | Charts or figures. | Calibration plot. [HLE] |
| Leaderboard | Ranked list of systems. | FACTS public ranking table. [FACTS] |
| Interactive dashboard | Filterable or dynamic UI. | Dashboard by model and domain. [FACTS] |
| Downloadable CSV or JSON | Machine-readable result files. | `results.csv`. [HLE] |
| API output | Results returned by API. | Evaluation endpoint response. [tau2-bench] |
| Paper-only results | Results exist only in paper. | No downloadable results. [HLE] |
| Other | Other presentation. | Notebook, slide deck. [HLE] |

### 4.4 Output Structure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Aggregate-score based | Organized around total scores. | Overall accuracy ranking. [FACTS] |
| Capability-domain based | Organized by capability areas. | HLE subject categories, MMMU-Pro disciplines, or FACTS sub-benchmarks. [HLE; MMMU-Pro; FACTS] |
| Task-family based | Organized by task type. | Browser, API, file tasks. [tau2-bench] |
| Criterion-threshold based | Organized by pass/fail or score bands. | ARC-AGI-2 pass-style task success; record only the benchmark's stated threshold. [ARC-AGI-2] |
| Pairwise-comparison based | Organized by head-to-head outcomes. | Use only when reports are actually pairwise. |
| Rank based | Emphasizes ordering. | Leaderboard rank. [FACTS] |
| Cost or efficiency adjusted | Includes cost, latency, or token efficiency. | Structural note: use only if the source reports cost, latency, token, or resource-adjusted outputs. |
| Error-analysis based | Includes error categories. | Failure taxonomy. [HLE] |
| Trace or process based | Includes trajectories or logs. | Tool trace report. [tau2-bench] |
| Other | Other structure. | Qualitative audit memo. [HLE] |

### 4.5 Sensitivity to Context

| Option | Meaning | Example |
| :--- | :--- | :--- |
| One output format for all contexts | Same report for all users or uses. | Single public table. [HLE] |
| User-definable output contexts | Users can customize report scope or audience. | Dashboard filters for domains. [FACTS] |
| Pre-defined versions adapted to audience or use | Different fixed reports for different audiences. | Technical report plus executive scorecard. [HLE] |
| Context sensitivity not documented | No source says whether reports differ by use. | Paper-only results. [HLE] |

### 4.6 Development of Outputs

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Based on benchmark authors' design | Authors chose report fields and formats. | Paper tables designed by benchmark authors. [HLE] |
| Based on empirical or actuarial relationships | Report content follows statistical or empirical score relationships. | Validated risk bands. [HLE] |
| Based on expert judgment | Experts shape interpretation or categories. | Expert-defined domain labels. [HLE] |
| Based on human annotation | Human labels or judgments feed reports. | Video-MMMU uses human-annotated questions; HLE uses human review/audit in item development. [Video-MMMU; HLE] |
| Based on model-as-judge outputs | AI judge produces score or labels shown in report. | Model-judge correctness extraction. [HLE] |
| Automatically generated by benchmark platform | Platform generates report. | Submitter dashboard. [FACTS] |
| Other | Other source of report content. | Community-maintained leaderboard. [FACTS] |

### 4.7 Modifiability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not modifiable | Users cannot change report contents. | Fixed paper table. [HLE] |
| Limited modification by submitter or user | Users can filter, export, or add metadata. | Dashboard filters. [FACTS] |
| Fully user-generated reports possible | Users can create custom reports from released data. | Public raw outputs and item scores. [HLE] |
| Not documented | Modifiability is not stated. | Unknown platform behavior. [HLE] |

### 4.8 Transparency

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Clear linkage between tasks, scores, and reported claims | Reports explain how tasks and metrics support claims. | Scorecard links each claim to task family and metric. [FACTS] |
| Partial linkage between tasks, scores, and reported claims | Some links are clear, others unexplained. | Domain scores shown but broad headline unexplained. [HLE] |
| Linkage is not obvious from available documentation | User cannot tell how score supports claim. | Ranking only. [FACTS] |
| Mixture of clear and concealed linkage | Some details public, some hidden for integrity or platform reasons. | Public aggregate with hidden item-level scoring. [HLE] |
| Not documented | No evidence about linkage. | Mark not documented when the source gives no report evidence. Structural field. |

### 4.9 Output Content

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Capability descriptions | Text explaining what scores indicate. | "Measures closed-ended academic performance." [HLE] |
| Aggregate rankings | Overall rank or total score. | Leaderboard rank. [FACTS] |
| Subdomain comparisons | Domain or category differences. | HLE category results. [HLE] |
| Error categories | Types of failures. | FACTS factuality and grounding errors, or HLE parsing/judge extraction failures if documented. [FACTS; HLE] |
| Examples of successes or failures | Sample outputs. | Correct/incorrect responses. [HLE] |
| Cost, latency, or efficiency data | Runtime, token, cost, compute. | HLE completion token counts. [HLE] |
| Process traces | Tool calls, logs, reasoning traces. | Agent trajectory. [tau2-bench] |
| Recommendations or interpretation notes | Guidance on using results. | Suggested non-use cases. [HLE] |
| Warnings or caveats | Limits and risks. | AGI caveat. [HLE] |
| Other | Other content. | Confidence histograms. [HLE] |

### 4.10 Intended Recipients

Use the same logic as Section 2.4, but focus on report recipients rather than intended users of the benchmark generally. A benchmark might be built for researchers but publish a simplified public leaderboard.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark maintainers | People who maintain tasks, scoring, reports, or platform outputs. | Maintainers using results to identify benchmark saturation. [HLE] |
| Model developers | Teams building or improving evaluated systems. | Lab teams checking regressions. [FACTS] |
| AI researchers | Researchers studying model capabilities or benchmark behavior. | HLE research comparison of science reasoning performance. [HLE] |
| Safety evaluators | Users focused on safety, refusal, harm, or risk. | Use this recipient when the benchmark source names safety users or risks. [SafetyBench; OmniSafetyBench] |
| Policy or governance actors | Users making governance, standards, or policy judgments. | Policy memo using benchmark evidence. [HLE] |
| Product or deployment teams | Teams deciding product behavior, release readiness, or deployment constraints. | Product launch readiness review. [HLE] |
| Procurement teams | Buyers or enterprise evaluators comparing vendors. | Vendor-selection scorecard. [HLE] |
| Public audience | General readers of public results or leaderboards. | Public-facing leaderboard users. [FACTS] |
| Other: | Another documented recipient. | Competition judges, educators, domain boards. [HLE] |

## Section 5. Supply Arrangements and Materials

Purpose: describe the materials and access arrangements needed to inspect, run, reproduce, submit to, or maintain the benchmark. This includes documentation, publication channels, user requirements, data access, provenance, contamination controls, reproducibility materials, maintenance, and versioning.

### 5.1 Supporting Information Provided

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Technical report | Formal methods/results document. | HLE benchmark paper. [HLE] |
| User guide | Practical instructions for running or interpreting. | Documentation site. [FACTS] |
| Repository README | Repo-level usage and overview. | GitHub README. [SWE-Bench Verified] |
| API documentation | API endpoint or schema instructions. | Hosted evaluator API docs. [tau2-bench] |
| Dataset card | Dataset metadata, license, splits, provenance. | Hugging Face card. [HLE] |
| Model submission instructions | Rules for submitting systems or outputs. | Leaderboard submission guide. [FACTS] |
| Scoring documentation | Scoring method, formula, parser, judge, tests. | HLE scorer prompt and scoring notes. [HLE] |
| Rubric or annotation guide | Human or judge scoring rubric. | HLE human review instructions and FACTS evaluation prompts. [HLE; FACTS] |
| Evaluation examples | Sample tasks, submissions, expected outputs. | Example JSONL submission. [SWE-Bench Verified] |
| FAQ or discussion forum | Support and clarifications. | GitHub Discussions. [SWE-Bench Verified] |
| Changelog or release notes | Version and update history. | HLE-Rolling notes. [SWE-Bench Verified] |
| Other | Other support material. | Video tutorial. [Video-MMMU] |

### 5.2 Methods of Publication

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Academic paper | Published or preprint paper. | arXiv HLE benchmark paper. [HLE] |
| Benchmark website | Official website. | Benchmark landing page. [HLE] |
| Git repository | Code-hosting repository. | GitHub repo. [SWE-Bench Verified] |
| Package registry | Installable package. | PyPI package. [HLE] |
| Dataset hosting platform | Hosted dataset. | Hugging Face dataset. [HLE] |
| Leaderboard platform | Hosted ranking/submission site. | Eval platform leaderboard. [FACTS] |
| Downloadable documents | PDFs, CSVs, guides, spreadsheets. | PDF technical report. [HLE] |
| Private distribution | Materials shared only with approved users. | Private holdout or gated audit. [HLE] |
| Other | Other publication path. | Conference competition portal. [HLE] |

### 5.3 User Requirements or Qualifications

| Requirement type | Meaning | Example |
| :--- | :--- | :--- |
| Technical expertise | Skills needed to run or interpret. | Python, Docker, API use. [SWE-Bench Verified] |
| Compute or infrastructure | Hardware or hosted services. | GPU, cloud account. [HLE] |
| Account or access approval | Login, API keys, approval, NDA. | Leaderboard account. [tau2-bench] |
| Legal or license terms | Usage, redistribution, research-only terms. | Non-commercial dataset license. [HLE] |
| Cost or fee | Monetary cost. | Paid API or platform fee. [tau2-bench] |
| Security or privacy requirements | Handling sensitive data or sandboxing. | No exfiltration, private data policy. [HLE] |
| Other | Any other requirement. | Domain certification for human raters. [HLE] |

### 5.4 Dataset and Item Access

| Component | Meaning | Example |
| :--- | :--- | :--- |
| Training or example data | Practice or development examples. | Public examples. [FACTS] |
| Development set | Data for tuning prompts or systems. | Dev split. [FACTS] |
| Test set | Data used for evaluation scores. | HLE public test questions. [HLE] |
| Private holdout set | Hidden test material. | HLE private held-out set. [HLE] |
| Prompt templates | Exact prompt formatting. | System/user prompt templates. [HLE] |
| Reference answers | Answer keys or expected outputs. | Correct multiple-choice letters. [SWE-Bench Verified] |
| Rubrics | Criteria for scoring open or ambiguous outputs. | Human judge rubric. [HLE] |

Mark each component as public, restricted, hidden, or not available. A component may be hidden by design; describe the reason if stated.

### 5.5 Provenance and Contamination Documentation

This section records documentation only.

| Topic | Meaning | Example |
| :--- | :--- | :--- |
| Data source provenance | Where items/data came from. | Expert submissions, public web data, synthetic generator. [HLE] |
| Collection procedure | How data was gathered. | Contributor process and submission rules. [HLE] |
| Filtering or quality control | How bad, duplicate, invalid, or unsuitable items were removed. | Expert review, audits. [HLE] |
| Licensing or rights | Rights to distribute and evaluate. | Contributor license or dataset license. [HLE] |
| Deduplication | Duplicate-removal methods. | Exact or semantic dedupe. [HLE] |
| Contamination controls | Steps to reduce training-data exposure. | HLE and ARC-AGI-2 use public/private split logic for overfitting or integrity concerns. [HLE; ARC-AGI-2] |
| Searchability or source-exposure checks | Whether items can be found online or in source data. | HLE documents searchability checks. [HLE] |
| Canary, GUID, encryption, or anti-scraping method | Technical markers or protections for leakage detection. | HLE repository documents a canary string. [HLE] |
| Training-on-test diagnostic task | Tests designed to detect memorization of benchmark items. | Diagnostic prompts. [HLE] |
| Public/private split rationale | Why some data is public and some hidden. | HLE private set for overfitting/gaming checks. [HLE] |
| Update or refresh policy | How items are added, retired, or refreshed. | HLE-Rolling and FACTS private/public suite updates show refresh or versioning issues to record. [HLE; FACTS] |
| Release rules or anti-gaming terms | Rules limiting leakage, tuning, scraping, or submissions. | ARC-AGI-2 and FACTS use private or semi-private components to limit gaming. [ARC-AGI-2; FACTS] |

### 5.6 Reproducibility Materials

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Complete evaluation code | End-to-end runnable evaluator. | SWE-Bench Verified and tau2-bench provide runnable evaluation paths; record any scope limitations. [SWE-Bench Verified; tau2-bench] |
| Scoring scripts | Code for scoring outputs. | Judge parser or unit-test scorer. [HLE] |
| Environment file or dependency list | Requirements needed to recreate runtime. | `requirements.txt`, `environment.yml`. [HLE] |
| Container or reproducible runtime | Docker image or equivalent. | Dockerfile. [SWE-Bench Verified] |
| Prompt templates | Exact prompts used. | HLE evaluation prompt. [HLE] |
| Example submissions | Sample outputs in expected format. | JSONL example. [SWE-Bench Verified] |
| Raw outputs from reported models | Model responses used for reported results. | Released completions. [SWE-Bench Verified] |
| Random seeds | Seeds for sampling or task generation. | Seed list. [SWE-Bench Verified] |
| Configuration files | Model, scorer, prompt, or environment configs. | YAML run configs. [SWE-Bench Verified] |
| Expected outputs or tests | Tests that verify setup and scoring. | Golden outputs. [SWE-Bench Verified] |
| Result replication script | Script that regenerates paper/leaderboard results. | `reproduce_results.py`. [SWE-Bench Verified] |
| Build status or continuous integration check | CI showing code works. | Passing GitHub Actions badge. [SWE-Bench Verified] |
| None documented | No reproducibility materials are documented. | paper-only benchmark scope with HLE as a cautionary example. [HLE] |

### 5.7 Maintenance and Versioning

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Current maintenance status | Active, inactive, archived, planned, unclear. | Active rolling updates. [SWE-Bench Verified] |
| Latest documented release | Most recent version/date. | GitHub release tag. [HLE] |
| Changelog available | Whether changes are documented. | Release notes. [FACTS] |
| Versioning scheme | How versions are named. | Semantic versioning, dated releases. [HLE] |
| Deprecated versions | Retired or superseded versions. | Old public set. [HLE] |
| Issue tracker or feedback channel | Where users report problems. | GitHub Issues. [HLE] |
| Response policy for user feedback | How maintainers respond. | Triage SLA or no policy. [HLE] |
| Known planned updates | Roadmap or announced refresh. | HLE-Rolling. [HLE] |
| Retirement or archival plan | How benchmark will be retired. | Archive after saturation. [HLE] |
| Archival status | Whether data/code are preserved. | DOI, Zenodo, archived repo. [HLE] |

## Appendix A. General Description of the Benchmark

Write a concise, non-evaluative summary. Include claim, domains, intended systems, administration, scoring, outputs, materials, versions, variants, and major documentation gaps. Do not criticize here. Say "not documented in reviewed sources" rather than "poorly documented."

Example pattern: "HLE is described as a benchmark of expert-level closed-ended academic capability for frontier language models. It includes a public set of 2,500 questions and a private held-out set, reports accuracy and calibration-related outputs, and includes caveats against interpreting HLE accuracy alone as AGI evidence."

## Appendix B. EFPA-to-MESA Adaptation Notes

Use this when the human-testing origin of a field needs explanation in an AI benchmark review.

| EFPA concept | MESA meaning | Use when |
| :--- | :--- | :--- |
| Instrument | Benchmark | Explaining why the benchmark is reviewed as a measurement system. |
| Test taker | AI system under evaluation | Clarifying that the evaluated entity is model, agent, or system. |
| Test user | Benchmark output user | Identifying who interprets scores. |
| Administration | Evaluation protocol | Translating testing conditions into prompts, tools, settings, and infrastructure. |
| Scales and scores | Metrics, subscores, and aggregate indices | Translating psychometric score fields into benchmark metrics. |
| Norms | Baselines, comparators, or reference groups | Explaining chance, human, model, or threshold references. |
| Reports | Leaderboards, scorecards, dashboards, traces, or paper tables | Explaining benchmark outputs. |
| Test materials | Dataset, prompts, rubrics, code, harness, and documentation | Explaining materials needed for use and review. |

## Appendix C. Part B Evidence Preparation Notes

Use Appendix C as a bridge from Part A facts to Part B ratings. Do not assign ratings here.

| Part B area | What to gather | Example evidence |
| :--- | :--- | :--- |
| Construct validity | Construct definition and claim scope. | HLE: closed-ended academic capability, not AGI proof. [HLE] |
| Task or item quality | Development process, expert review, item audits. | Expert submissions and audits. [HLE] |
| Scoring validity | Metric, parser, judge, rubric, scorer validation. | Model-judge prompt and validation evidence if available. [FACTS] |
| Reliability or run stability | Repeats, seeds, uncertainty, rater agreement. | Expert disagreement rates, confidence intervals. [SWE-Bench Verified] |
| Baselines and comparators | Human, expert, chance, model, prior versions. | FACTS multi-provider model cohort. [SWE-Bench Verified] |
| Fairness or comparability | Conditions across systems, domains, languages, modalities. | Text-only versus full-set distinction. [HLE] |
| Reproducibility | Data, code, prompts, configs, raw outputs. | Evaluation code and raw outputs. [FACTS] |
| Contamination and gameability | Public/private split, search checks, anti-gaming rules. | Private holdout. [tau2-bench] |
| Maintenance and benchmark drift | Versioning, changelog, refresh, retirement. | Rolling updates. [SWE-Bench Verified] |
| Interpretation limits | Stated caveats and non-use cases. | Do not infer AGI from HLE alone. [HLE] |
| Leaderboard or public-claim risk | Reports, ranks, public messaging. | Leaderboard caveats and version labels. [SWE-Bench Verified] |
| Other | Benchmark-specific issue. | Safety-sensitive content handling. [SWE-Bench Verified] |

# Part B. Evaluation of the Benchmark

Part B turns evidence into judgment. Use Part A as the factual base and cite outside literature only when needed to interpret benchmark quality.

## Part B Information Sources

| Source type | Use |
| :--- | :--- |
| Part A evidence | Primary factual base for ratings. |
| EFPA Part B source | Structural source for rating sections 6-12. |
| BetterBench | Lifecycle, reproducibility, implementation, usability, contamination, maintenance. |
| Measuring what Matters | Construct validity and phenomenon-task-metric-claim chain. |
| AGI/CHC source | Broad intelligence, AGI, and cross-domain ability caution. |
| Benchmark-specific sources | Official benchmark evidence beyond Part A if needed. |
| Other local sources | Contextual sources used with caution. |

## Rating Record Template

Use for extra item-level ratings when the main section tables are not granular enough.

| Field | Meaning |
| :--- | :--- |
| Criterion | What quality question is being rated. |
| Rating | `n/a` or `0`-`4`. |
| Evidence used | Source-grounded support for the judgment. |
| Missing evidence | What evidence would reduce uncertainty or support a higher rating. |
| Reviewer rationale | Why the evidence and gaps lead to the rating. |
| Interpretation caution | How users should limit interpretation of the rating. |

## Section 6. Quality of Rationale, Development, Documentation, and Task/Item Quality

Section 6 asks whether the benchmark explains what it is measuring, why its tasks and metrics fit that target, how tasks were developed, and whether users have enough documentation.

### 6.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Rationale and construct definition | Whether the target phenomenon is defined and bounded. | Vague "reasoning" or "intelligence" claim with no definition. [HLE] | Clear construct, subcomponents, exclusions, and intended uses. [HLE] |
| Phenomenon-task-metric-claim chain | Whether the source links phenomenon, task, metric, and claim. | Accuracy on narrow tasks used to claim broad agency without argument. [FACTS] | Explicit chain with confounds and safeguards. [FACTS] |
| Task/item development quality | How tasks were designed, reviewed, sampled, and revised. | No item source or review process. [HLE] | Expert review, structured criteria, audits, revision history. [HLE] |
| Documentation and procedural instructions | Whether users can administer, score, and interpret correctly. | Incomplete setup and scoring instructions. [FACTS] | Current, source-linked, complete user documentation. [FACTS] |

### 6.2 Section 6 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 6.1 Rationale and construct definition | Adequacy of the purpose and construct definition. | HLE defines closed-ended academic challenge better than broad AGI. [HLE] |
| 6.2 Phenomenon-task-metric-claim chain | Fit among claim, tasks, metric, and interpretation. | Accuracy fits closed-ended items, but broader claims need caution. [HLE] |
| 6.3 Development process and task/item quality | Evidence about item creation, expertise, review, and quality control. | Expert submissions and audits. [HLE] |
| 6.4 Documentation available to users | Availability and completeness of user-facing documentation. | Paper plus missing repository or license details. [SWE-Bench Verified] |
| 6.5 Procedural instructions for administration, scoring, and interpretation | Whether run, scoring, and interpretation instructions are sufficient. | Prompt documented, exact harness missing. [HLE] |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality | Reviewer synthesis of Section 6. | Do not mechanically average rows. Structural field. |

## Section 7. Quality of Benchmark Materials and Usability

Section 7 rates whether the actual materials can be obtained, understood, and used correctly.

### 7.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Materials availability | Whether datasets, prompts, rubrics, and task materials exist and are accessible. | Key materials missing. [HLE] | Complete, versioned, licensed materials. [HLE] |
| Evaluation harness and scoring tools | Whether users can run and reproduce scoring. | Opaque hosted-only or absent scorer. [tau2-bench] | Runnable, tested harness with examples. [tau2-bench] |
| Prompts, rubrics, and response formats | Whether instructions and formats are clear and validated. | Ambiguous prompts or fragile parser. [HLE] | Documented prompts, rubrics, parser tests. [HLE] |
| Accessibility and usability | Whether intended users and systems can use materials. | Requirements exclude relevant systems without warning. [HLE] | Quick starts, support, modality/language access notes. [HLE] |

### 7.2 Section 7 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 7.1 Dataset, task set, or environment availability | Availability of tasks, data, or environments. | Public tasks available, private holdout hidden. [HLE] |
| 7.2 Prompts, instructions, rubrics, and response format | Clarity and access to prompts/rubrics/formats. | HLE prompt and judge instructions. [HLE] |
| 7.3 Evaluation harness, scorer, and implementation usability | Ability to run scorer correctly. | Complete CLI versus paper-only scoring description. [HLE] |
| 7.4 Accessibility across relevant modalities, languages, and system types | Whether relevant systems can participate fairly. | Text-only subset for models lacking image input. [MMMU-Pro] |
| 7.5 Licensing, usage requirements, and sensitive-content warnings | Legal and safety instructions for use. | HLE and ScreenSpot-Pro document MIT licenses; record missing or restricted terms where the source lacks them. [HLE; ScreenSpot-Pro] |
| 7.6 Overall quality of benchmark materials | Reviewer synthesis of material quality. | Consider access restrictions and intended use. Structural field. |

## Section 8. Baselines, Comparators, and Reference Interpretation

Section 8 adapts EFPA norms into AI benchmark baselines, floors, ceilings, human/expert comparisons, model cohorts, and thresholds.

### 8.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Baseline construction | Whether reference levels are meaningful and documented. | No baseline where one is needed. [HLE] | Representative, uncertainty-aware baselines. [HLE] |
| Human/expert comparators | Whether human claims have methods. | "Expert-level" with no expert procedure. [HLE] | Documented qualifications, sampling, conditions. [HLE] |
| Model comparators | Whether model comparisons are current and specified. | Cherry-picked or version-ambiguous cohort. [HLE] | Versions, settings, and conditions clear. [HLE] |
| Floors, ceilings, thresholds | Whether chance, saturation, and decision levels are handled. | Chance floor ignored. [HLE] | Floors, ceilings, thresholds empirically integrated. [HLE] |

### 8.2 Section 8 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 8.1 Random, chance, floor, and ceiling baselines | Chance levels, lower bounds, saturation, score ceilings. | HLE notes non-zero multiple-choice floor. [HLE] |
| 8.2 Human or expert baselines | Human performance and expert comparison methods. | Expert contributors are not the same as a quantified expert baseline. [HLE] |
| 8.3 Model comparator cohort | Model selection, versions, and evaluation conditions. | FACTS model table with provider/version details. [FACTS] |
| 8.4 Criterion thresholds or score bands | Pass/fail or interpretive cutoffs. | ARC-AGI-2 pass-style scoring is descriptive; deployment thresholds would require separate validation. [ARC-AGI-2] |
| 8.5 Overall adequacy of baselines and reference interpretation | Synthesis of reference interpretation quality. | Explain usable reference points and missing anchors. [HLE] |

## Section 9. Reliability, Precision, and Score Stability

Section 9 rates whether scores are stable and precise enough for the intended use.

### 9.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Run stability and uncertainty | Repeated runs, seeds, uncertainty intervals, stochasticity. | Single scores despite known variability. [HLE] | Comprehensive repeat-run and uncertainty evidence. [HLE] |
| Scorer, judge, or rater reliability | Reliability of scorers, parsers, raters, judges. | Model judge with no validation. [HLE] | Agreement and validation across edge cases. [HLE] |
| Form, version, and prompt stability | Comparability across prompts, versions, forms, environments. | Mixed versions without equivalence evidence. [SWE-Bench Verified] | Drift and equivalence tested. [SWE-Bench Verified] |
| Statistical comparison quality | Whether score differences are statistically interpretable. | Ranks without uncertainty. [HLE] | Comparisons use uncertainty/significance methods. [HLE] |

### 9.2 Section 9 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 9.1 Run-to-run stability, seeds, and sampling settings | Stability across runs and decoding. | Multiple seeds or non-determinism caveat. [HLE] |
| 9.2 Score uncertainty, confidence intervals, or standard errors | Quantified uncertainty. | Confidence intervals over items. [HLE] |
| 9.3 Human rater, scorer, parser, or model-judge agreement | Agreement evidence for judgmental or parsing steps. | Human inter-rater agreement, judge validation. [HLE] |
| 9.4 Prompt, form, version, and environment stability | Sensitivity to prompt, benchmark version, form, environment. | Public/private equivalence evidence. [HLE] |
| 9.5 Overall reliability and precision | Synthesis of score stability. | State whether comparisons are stable enough for intended use. [HLE] |

## Section 10. Validity Evidence

Section 10 is the core MESA validity section: does evidence support the intended interpretation of scores?

### 10.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Content and representativeness | Whether tasks represent intended capability space. | Narrow sample used for broad claim. [HLE] | Systematic coverage with stated limits. [HLE] |
| Metric and scoring validity | Whether the metric rewards intended capability. | Metric rewards formatting, memorization, or judge artifacts. [FACTS] | Metric, parser, scorer, aggregation validated. [FACTS] |
| Relations with other evidence | Convergent, discriminant, criterion, ecological evidence. | Comparisons absent or misleading. [HLE] | Relevant comparisons interpreted cautiously. [HLE] |
| Contamination and gameability | Leakage, public exposure, tuning, gaming controls. | Risks ignored despite public tasks. [SWE-Bench Verified] | Private splits, canaries, audits, release rules. [SWE-Bench Verified] |
| Claim proportionality, including AGI/agency | Whether claims match measurement breadth and depth. | AGI claim from narrow task score. [HLE] | Broad claims supported across relevant sub-abilities or explicitly rejected. [HLE] |

### 10.2 Section 10 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 10.1 Content validity and task representativeness | Coverage and sampling of intended domain. | HLE broad academic domains, but not all cognitive abilities. [HLE] |
| 10.2 Internal structure, subscores, or dimensionality | Whether subscores/dimensions behave as claimed. | Category scores require support if interpreted as dimensions. [HLE] |
| 10.3 Metric, scorer, and aggregation validity | Fit and validation of scoring. | Accuracy for closed-ended questions; judge validation gap. [HLE] |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings | External comparisons and ecological relevance. | Comparison to prior saturated benchmarks. [HLE] |
| 10.5 Contamination, leakage, and gameability controls | Controls against exposure and gaming. | Searchability checks and private holdout. [SWE-Bench Verified] |
| 10.6 Claim proportionality and broad-capability cautions | Whether public claims stay within evidence. | HLE caveat against AGI inference. [HLE] |
| 10.7 Overall validity evidence | Synthesis of validity for intended use. | Usually the most important Part B judgment. [HLE] |

## Section 11. Fair Use, Comparability, and Appropriate Use

Section 11 rates whether benchmark use is fair and comparable across relevant systems, modalities, languages, domains, access modes, and user contexts.

### 11.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Cross-system comparability | Whether conditions are comparable across systems. | Different tools/prompts/settings without caveat. [tau2-bench] | Conditions controlled and differences handled. [tau2-bench] |
| Domain, language, modality, and subgroup coverage | Whether coverage supports intended comparisons. | English-only benchmark used for multilingual claim. [HLE] | Global PIQA-style language and cultural coverage is documented and tied to interpretation limits. [Global PIQA] |
| Access, compute, and usability fairness | Whether access or compute requirements distort comparison. | Proprietary platform excludes relevant systems without warning. [HLE] | Inclusive, documented access paths. [HLE] |
| Appropriate-use guidance | Whether guidance prevents overinterpretation. | Marketing encourages unsupported claims. [HLE] | Prominent non-use and limitation guidance. [HLE] |

### 11.2 Section 11 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 11.1 Cross-system and evaluation-condition comparability | Prompt, model access, settings, tools, and scoring fairness. | Same prompt/settings across compared models. [tau2-bench] |
| 11.2 Domain, language, modality, and subgroup fairness | Coverage across relevant domains/languages/modalities/groups. | Global PIQA documents language varieties and culturally grounded item construction. [Global PIQA] |
| 11.3 Access, compute, tooling, and API/local comparability | Whether resource requirements affect comparability. | API-only benchmark versus open-weight local models. [tau2-bench] |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance | Rules and warnings for responsible use. | Anti-gaming terms, sensitive-content notices. [HLE] |
| 11.5 Overall fair use and comparability | Synthesis of fair-use evidence. | State which comparisons are safe or limited. [HLE] |

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

Section 12 rates whether benchmark outputs communicate results accurately, clearly, and proportionally.

### 12.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Report scope and granularity | Whether reports show enough detail for claims. | Aggregate only despite domain claims. [HLE] | Aggregate, subscores, uncertainty, caveats. [HLE] |
| Leaderboard or dashboard quality | Versioning, ranking clarity, update policy, reproducibility. | Opaque rankings. [FACTS] | Versioned, documented, uncertainty-aware display. [FACTS] |
| Report reliability and validity | Whether reports accurately reflect scores and limits. | Public claims diverge from score support. [HLE] | Score-to-claim links and limits explained. [HLE] |
| Public communication and acceptability | Whether public messaging is cautious and audience-appropriate. | Headline overclaims. [HLE] | Transparent, accessible, evidence-aligned communication. [HLE] |

### 12.2 Section 12 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 12.1 Report, leaderboard, dashboard, or result artifact scope | Whether outputs cover relevant results. | Paper tables, leaderboard, dashboard. [FACTS] |
| 12.2 Score granularity, uncertainty, and version labeling | Detail, uncertainty, version clarity. | Category scores plus missing CIs. [SWE-Bench Verified] |
| 12.3 Linkage from scores to public claims | Whether claims follow from scores. | AGI caveat included or absent. [HLE] |
| 12.4 Raw outputs, per-item data, or trace availability | Inspectability of underlying outputs. | Released model completions or logs. [SWE-Bench Verified] |
| 12.5 Overall quality of reports and public claims | Synthesis of reporting quality. | State public interpretation risks. Structural field. |

## Final Evaluation

### Evaluative Report of the Benchmark

Write a concise, source-grounded judgment about benchmark quality for its stated purpose. Include strengths, evidence gaps, and appropriate-use limits. Do not average section ratings mechanically.

### Conclusions

Summarize what uses the benchmark can support, which uses require caution, and what expertise is needed to interpret results responsibly.

### Summary of Ratings

Use this as a compact map of Part B. Each row should name the rating, reviewer comments, and the critical evidence gap.

| Section or area | Meaning |
| :--- | :--- |
| Section 6. Rationale, documentation, and task/item quality | Quality of construct definition, development, and documentation. |
| Section 7. Benchmark materials and usability | Availability and usability of data, prompts, scorers, harnesses, materials. |
| Section 8. Baselines and comparators | Strength of reference interpretation. |
| Section 9. Reliability and precision | Stability, uncertainty, rater/judge/scorer reliability. |
| Section 10. Validity evidence | Strength of score interpretation and claim support. |
| Section 11. Fair use and comparability | Fair, comparable, appropriate use across relevant systems and contexts. |
| Section 12. Reports, leaderboards, and public claims | Quality and proportionality of outputs and public communication. |
| Construct definition and claim scope | Cross-cutting adequacy of construct and claim boundaries. |
| Scoring validity | Cross-cutting adequacy of metrics, scorers, and aggregation. |
| Reproducibility and implementation transparency | Cross-cutting ability to independently inspect or rerun evaluation. |
| Contamination and gameability controls | Cross-cutting leakage and gaming risk controls. |
| Maintenance and versioning | Cross-cutting update, drift, saturation, archival evidence. |
| Overall claim-bounded measurement quality | Final judgment about quality for the narrowest defensible interpretation. |

### Evidence Gap Register

Use this to track missing evidence that matters most. Each row should say why the gap matters and what evidence would support a higher rating. Do not list every missing detail, only consequential gaps.

### Reviewer Caution Statement

State the narrowest defensible interpretation of scores, the main overclaim risks, and when ratings should be revisited. For HLE, a caution pattern is: scores are best interpreted as evidence about closed-ended academic task performance under documented conditions, not as standalone proof of AGI, autonomous research ability, or general agency.

## Appendix D. Template Validation Checklist

Use this checklist after completing a review or revising the template.

| Checklist item | Meaning |
| :--- | :--- |
| EFPA traceability: every major EFPA Part B section 6-12 has a MESA equivalent. | Check that Sections 6-12 remain mapped to EFPA's evaluative structure. |
| Literature coverage: each major MESA criterion is linked to EFPA, BetterBench, Measuring what Matters, or AGI/CHC literature where relevant. | Check that criteria have a source rationale, especially for lifecycle, construct-validity, and broad-claim cautions. |
| Descriptive/evaluative separation: Part A contains no ratings and Part B contains no unsupported claims. | Check that descriptive facts and reviewer judgments are not mixed. |
| Rating usability: each Part B rating has evidence, missing evidence, reviewer rationale, and interpretation caution. | Check that no Part B row contains only a number. |
| Missing-evidence handling: missing documentation is treated as an evidence gap, not automatic proof of poor quality. | Check that gaps are not turned into defects without source-grounded evidence. |
| Claim proportionality: broad intelligence, AGI, autonomy, agency, or cross-domain claims receive breadth/depth scrutiny. | Check that broad claims are compared against the actual task, domain, modality, tool, memory, planning, and speed evidence. |
| Reproducibility coverage: data, prompts, harness, scorer, environment, raw outputs, and versioning are considered. | Check that independent inspection or rerun evidence is recorded. |
| Contamination coverage: public/private split, searchability, canaries, release rules, and refresh policy are considered where applicable. | Check that leakage and gaming risks are considered descriptively in Part A and evaluatively in Part B. |
| HLE fit or pilot fit: the template can express known issues without forcing false precision. | Check that pilot examples can be recorded with gaps and caveats rather than forced certainty. |
| Reviewer judgment: overall ratings are justified by evidence rather than mechanically averaged. | Check that final ratings explain judgment rather than averaging section numbers. |

## Cross-Cutting "Other:" Option

Many template sections include `Other:`. Use it only when a source documents an option that does not fit the listed categories. Always name the option after the colon and add a note. Do not use `Other:` to avoid choosing a close listed option or to record a reviewer concern that belongs in notes.
