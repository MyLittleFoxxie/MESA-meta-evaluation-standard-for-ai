# MESA EFPA Template User Guide v2

This guide explains how to use `markdown/MESA EFPA template.md`. It is a companion document, not a replacement for the template. Use the same section numbers to move between the two files.

MESA treats an AI benchmark as a measurement instrument. Part A describes what the benchmark is and what the sources say. Part B evaluates whether the benchmark supports its stated interpretation. Keep those two activities separate: do not put ratings in Part A, and do not make unsupported judgments in Part B.

V2 replaces generic examples with named benchmark examples wherever a stable, source-grounded example is available. Inline examples use short source tags from the Benchmark Example Bank below. Rankings, model counts, and live leaderboard positions are date-sensitive; use them only when the review date and source snapshot are recorded. Part B rating examples are illustrative patterns only, not new review ratings for the named benchmarks.

## Benchmark Example Bank

Use these compact profiles to keep option tables readable. The tag in the first column is the short source tag used in later examples.

| Tag | Benchmark profile | Stable facts to reuse | Source anchor |
| :--- | :--- | :--- | :--- |
| HLE | Humanity's Last Exam | Public repository documents HLE as a 2,500-question multimodal closed-ended academic benchmark with a Hugging Face dataset link, MIT license, canary string, simple evaluation scripts, and contact channel. The local paper-equivalent working copy and pilot review were used internally for evidence extraction and cautionary examples, not as public citation anchors. | https://github.com/centerforaisafety/hle |
| SWE-bench | SWE-bench | Real GitHub software issues; given a codebase and issue, a model generates a patch. Public docs describe a Docker-based evaluation harness, multiple variants including Lite, Verified, and Multimodal, and public leaderboard resources. | https://www.swebench.com/SWE-bench/; https://github.com/SWE-bench/SWE-bench |
| HumanEval | HumanEval | OpenAI code-generation benchmark with 164 handwritten Python problems, function signatures/docstrings, unit-test based functional correctness, pass@k reporting, and safety warnings for executing generated code. | https://github.com/openai/human-eval; https://huggingface.co/datasets/openai/openai_humaneval |
| LiveCodeBench | LiveCodeBench | Continuously updated code benchmark using contest problems from LeetCode, AtCoder, and Codeforces; covers code generation, self-repair, code execution, and test-output prediction; records release dates and dataset versions for contamination-aware evaluation. | https://livecodebench.github.io/; https://github.com/LiveCodeBench/LiveCodeBench |
| MMLU | MMLU | 57-task multitask academic/professional multiple-choice benchmark for world knowledge and problem solving; classic reference point for broad language-model knowledge but often treated as saturated or succeeded by harder variants. | https://arxiv.org/abs/2009.03300; https://github.com/hendrycks/test |
| GPQA | GPQA | 448 graduate-level multiple-choice questions written by domain experts in biology, physics, and chemistry; includes expert and skilled non-expert reference performance in the paper abstract. | https://arxiv.org/abs/2311.12022 |
| MMMU | MMMU | 11.5K multimodal college-level questions from exams, quizzes, and textbooks across six disciplines, 30 subjects, 183 subfields, and heterogeneous image types; evaluates expert-level multimodal perception plus reasoning. | https://github.com/MMMU-Benchmark/MMMU |
| Video-MME | Video-MME | 900 videos, 254 total hours, and 2,700 human-annotated QA pairs; covers short, medium, and long videos plus subtitles/audio; license restricts academic research use. | https://github.com/MME-Benchmarks/Video-MME |
| AudioBench | AudioBench | AudioLLM evaluation repository with ASR, speech translation, speech QA, audio-scene QA, emotion/accent/gender recognition, music understanding, leaderboard, and metrics such as WER, BLEU, accuracy, and model-judge scores. | https://github.com/AudioLLMs/AudioBench |
| GAIA | GAIA | 466 real-world assistant questions requiring reasoning, multimodality, web browsing, and tool use; releases questions while withholding answers to 300 for a leaderboard. | https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants/ |
| WebArena | WebArena | Standalone, self-hostable web environment for autonomous agents; includes browser interaction, self-hosted websites, 812 examples, trajectories, and functional correctness validation. | https://github.com/web-arena-x/webarena; https://webarena.dev/og/ |
| HarmBench | HarmBench | Standardized automated red-teaming and robust-refusal framework; compares red-teaming methods and target LLMs/defenses, supports an evaluation pipeline, open-source code, and safety-focused attack/defense use cases. | https://www.microsoft.com/en-us/research/publication/harmbench-a-standardized-evaluation-framework-for-automated-red-teaming-and-robust-refusal/; https://github.com/centerforaisafety/HarmBench |
| TruthfulQA | TruthfulQA | 817 questions across 38 categories designed to test whether models avoid false answers based on human misconceptions; OpenAI page reports model and human truthfulness comparisons from the original study. | https://openai.com/index/truthfulqa/ |
| HELM | HELM | Stanford CRFM framework and leaderboards for transparent, reproducible, multi-metric evaluation; supports standardized datasets/scenarios, multiple providers, web UI, leaderboard, and metrics beyond accuracy. | https://github.com/stanford-crfm/helm; https://crfm.stanford.edu/2022/11/17/helm.html |
| Chatbot Arena | Chatbot Arena | Live community-driven pairwise preference platform; publishes periodic leaderboards and policies for open-source infrastructure, transparency, vote collection, and public model listing. | https://www.lmsys.org/blog/2024-03-01-policy/ |

## Core Reviewer Rules

### Documentation Status Options

| Option | Meaning | Select when | Do not select when | Example |
| :--- | :--- | :--- | :--- | :--- |
| Documented | The source gives enough information to record the field confidently. | The official paper, repository, documentation, dataset card, or maintainer statement states the fact directly. | You inferred the fact from examples, screenshots, or common practice. | HLE documents a public set of 2,500 questions. [HLE] |
| Partially documented | Some information is present, but important details are missing or internally incomplete. | The source names a private set but omits its size, access process, or selection method. | The source is simply silent. [HLE] | HLE states a private held-out set exists but the local pilot notes that its count is not documented. [HLE] |
| Not documented | The available sources do not state the information. | No reviewed source gives random seeds, run cost, or a formal leaderboard. | The issue is irrelevant to this benchmark type. [HLE] | If no reviewed source states a leaderboard, mark leaderboard status as not documented rather than assuming one exists; HLE sources document paper-style result tables but no formal leaderboard. [HLE] |
| Not applicable | The field does not apply to the benchmark or intended use. | A text-only benchmark has no audio-output requirement. | The field could apply but evidence is missing. | "Video output" is not applicable for MMLU multiple-choice text questions. [MMLU] |
| Unclear from available sources | The sources contain ambiguity, conflict, or wording that prevents a confident classification. | Two sections give different judge model versions, or a website implies but does not state a submission process. | The evidence is merely incomplete but not ambiguous. | The HLE pilot treats exact scorer-version evidence as partly unclear because local source statements differ. [HLE] |

### Part A vs Part B

Part A records claims and evidence. "The benchmark reports category accuracy" is Part A. "The category accuracy is too coarse for the claim" is Part B.

Part B rates adequacy. Each rating must include evidence used, missing evidence, reviewer rationale, and interpretation caution. Missing documentation is an evidence gap. It is not proof of poor benchmark quality unless a source-grounded defect is shown.

### Broad Claims and Narrow Evidence

If a benchmark claims "general intelligence", "AGI", "reasoning", "agency", "autonomy", or "expert capability", record the term in Part A and check what domains, sub-abilities, modalities, tools, planning, memory, and speed are actually measured. HLE is a useful example: it can support a narrow description of expert-level closed-ended academic performance, but the pilot records explicit caution against treating HLE accuracy alone as proof of AGI or autonomous research ability.

### Available vs Required

"Available" means the benchmark supports or permits something. "Required" means the benchmark cannot be run as intended without it. SWE-bench makes Docker part of its reproducible evaluation harness, while WebArena requires browser/web-environment access for autonomous browser tasks. [SWE-bench; WebArena]

### Public, Restricted, Hidden, and Not Available

| Access label | Meaning | Example |
| :--- | :--- | :--- |
| Public | Anyone can inspect or download the component under stated terms. | HumanEval public dataset and evaluation harness. [HumanEval] |
| Restricted | Access exists but requires approval, account access, payment, license agreement, or submitter status. | Video-MME data use is restricted to academic research. [Video-MME] |
| Hidden | The component exists but is intentionally concealed to protect evaluation integrity. | GAIA withholds answers to 300 questions for leaderboard scoring. [GAIA] |
| Not available | The component is not released or no source indicates it exists. | HLE reviewed sources do not document public raw model outputs. [HLE] |

### Baseline, Comparator, Threshold, Floor, and Ceiling

| Term | Meaning | Example |
| :--- | :--- | :--- |
| Baseline | A reference performance level used to interpret scores. | GPQA expert and skilled non-expert reference performance. [GPQA] |
| Comparator | A system, human group, benchmark version, or cohort used for comparison. | GPT-4O, Claude, expert humans, or a prior benchmark. [GPQA] |
| Threshold | A decision boundary or score band with an intended interpretation. | HarmBench refusal/safety gate only if a user validates the cutoff for deployment use. [HarmBench] |
| Floor | The lowest expected performance level under trivial or chance behavior. | MMLU four-choice questions have a non-zero chance floor. [MMLU] |
| Ceiling | The upper end where the benchmark stops distinguishing systems well. | MMLU saturation concerns motivate harder successor variants. [MMLU] |

## Information Sources

Use this table to record the evidence base before filling the template.

| Source type | Meaning and use | Example |
| :--- | :--- | :--- |
| Official paper or technical report | Main author-provided description of purpose, data, methods, scoring, and results. Prefer this before commentary. | HLE paper linked from the HLE GitHub repository. [HLE] |
| Benchmark website | Public landing page, documentation hub, access portal, or official result page. | `https://lastexam.ai`, if independently reviewed. [HELM] |
| Repository | Code, issues, releases, examples, scripts, and maintenance activity. | SWE-bench GitHub repository with evaluation harness and Docker setup. [SWE-bench] |
| Dataset card or data host | Dataset metadata, splits, licenses, provenance, access restrictions, and versioning. | HumanEval Hugging Face dataset card with 164 test samples. [HumanEval] |
| Leaderboard or results page | Ranking, submission rules, public scores, update dates, and system metadata. | Chatbot Arena leaderboard with model submissions. [Chatbot Arena] |
| Evaluation harness or package | Runnable code, package, CLI, scorer, or platform used for evaluation. | HELM `helm-run` and `helm-summarize` commands. [HELM] |
| Documentation or user guide | Setup, submission, interpretation, scoring, and troubleshooting instructions. | SWE-bench docs and README quick-start/evaluation pages. [SWE-bench] |
| Release notes or changelog | Version history, refresh policy, retired tasks, score comparability notes. | LiveCodeBench release versions and dated problem windows. [LiveCodeBench] |
| Maintainer statements | Authoritative clarifications from issues, discussions, papers, or official posts. | SWE-bench README notes about private test split evaluation for SWE-bench Multimodal. [SWE-bench] |
| Independent sources used for context | Non-official sources used to interpret background, not to replace official facts. | A critique paper explaining contamination concerns. [LiveCodeBench] |

## Part B Rating Scale

| Rating | Meaning | Use carefully |
| :--- | :--- | :--- |
| `n/a` | The criterion is not applicable to this benchmark or intended use. | Use only when the criterion truly does not apply, not when evidence is missing. [No real example appropriate] |
| `0` | Cannot rate because available evidence is insufficient. | Use for evidence gaps. Do not treat this as a quality defect by itself. [HLE] |
| `1` | Inadequate evidence or practice for the intended interpretation. | Use when evidence shows weak, unsuitable, or misleading practice. [HLE] |
| `2` | Adequate for cautious use within a clearly bounded interpretation. | Use when the benchmark can support limited use but has notable gaps. [HLE] |
| `3` | Good evidence or practice with meaningful but non-fatal gaps. | Use when evidence is strong enough for intended use, while caveats remain. [HLE] |
| `4` | Excellent evidence or practice, comprehensive and well matched to intended use. | Reserve for broad, current, well-documented, and independently usable evidence. [HLE] |

Every Part B row has five required concepts: the criterion being rated, the rating, evidence used, missing evidence, reviewer rationale, and interpretation caution. A bare number is not a MESA rating.

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Information

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Reviewer | Person or team completing the review. | "MESA reviewer" or named reviewers. [AudioBench] |
| Date of current review | Date the evidence was reviewed, not necessarily publication date. | `2026-05-04`. [HLE] |
| Date of previous review, if applicable | Earlier review date if this is an update. | `2026-05-01` for an HLE pilot refresh. [HLE] |
| Review scope | Boundary of the review. State whether it covers Part A only, full Part A/B, local working copies, or online artifact verification. | "Full Part A/B review using the HLE GitHub repository plus a local paper-equivalent working copy." [HLE] |
| Sources reviewed | Short list or pointer to the Information Sources table. | "HLE GitHub repository; HLE paper-equivalent working copy for evidence extraction." [HLE] |

### 1.2 Benchmark Information

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark name | Full official name. | "Humanity's Last Exam." [HLE] |
| Short name or acronym | Abbreviation used in papers, leaderboards, or code. | "HLE." [HLE] |
| Benchmark version, edition, or release | Version number, release tag, edition, date-stamped release, or note that no version is stated. | "Original public set; no version number documented." [HLE] |
| Original benchmark name, if this is an adaptation | Source benchmark if this review covers a translated, modified, or domain-specific version. | "MMLU-Pro adaptation" for a derivative benchmark. [MMLU] |
| Benchmark creators or authors | Original authors, organizers, contributors, or institution. | HLE organizing team. [HLE] |
| Current maintainers | People or group responsible now. | Repository maintainers, benchmark organization, or "not documented." [SWE-bench] |
| Host organization, publisher, or distributor | Entity distributing the benchmark or platform. | University lab, Scale AI, Hugging Face, Papers with Code. [HLE] |
| Date of original release | First public release date. | Paper publication date or repository release. [SWE-bench] |
| Date of current release or revision | Date of the version reviewed. | Latest GitHub release date. [HLE] |
| License or access terms | Legal usage terms, dataset license, submission rules, or "not documented." | MIT license documented in the HLE GitHub repository. [HLE] |
| Persistent identifier, citation, or DOI | DOI, arXiv ID, citation, permanent URL, or dataset identifier. | arXiv ID for a GPQA benchmark paper. [GPQA] |

### 1.3 Public Artifacts

Use this table to separate artifact existence from artifact quality. Part B evaluates adequacy later.

| Artifact | Means | Access status examples | Notes example |
| :--- | :--- | :--- | :--- |
| Paper or technical report | Formal benchmark description and results. | Available, missing, restricted. [HLE] | "Local paper-equivalent working copy used for review; cite the public repository or paper link." [HLE] |
| Benchmark website | Official public site or documentation hub. | Stated but not verified, available, missing. [HELM] | "Website named in paper." [HELM] |
| Code repository | Source code for data, evaluation, or scoring. | Public, private, not documented. [SWE-bench] | "Repository not identified in reviewed sources." [SWE-bench] |
| Evaluation harness | Runnable evaluator, package, or hosted submission system. | Public package, hosted only, not documented. [HLE] | "Simple evaluation scripts are public in the HLE repository; full published-score replication still needs caution." [HLE] |
| Dataset or task set | Prompts, items, episodes, environments, or tasks. | Public, restricted, hidden, partially documented. [HLE] | "Public 2,500-question set." [HLE] |
| Prompt set | Exact prompts or prompt templates. | Included in paper, in repo, not documented. [HLE] | "Evaluation prompt in appendix." [HLE] |
| Rubric or scoring guide | Answer keys, grading rubrics, judge prompts, unit tests. | Available, partially documented, hidden. [SWE-bench] | "Model-judge prompt documented." [SWE-bench] |
| Leaderboard | Public or private ranking and submission record. | Public leaderboard, paper tables only, not documented. [Chatbot Arena] | "HLE sources reviewed document paper-style result tables but no formal leaderboard." [HLE] |
| Changelog or release notes | Version history and update policy. | GitHub releases, paper appendix, missing. [SWE-bench] | "HLE-Rolling notes." [SWE-bench] |
| Contact or issue channel | Maintainer contact, issue tracker, email, forum. | GitHub issues, email, not documented. [SWE-bench] | "Issue channel not found." [SWE-bench] |

## Section 2. Classification

### 2.1 Claimed Capability Domains

Select only domains claimed or clearly implied by benchmark documentation. Use "Other" for a named domain not listed. If the benchmark name implies a domain but the paper never states it, note that ambiguity.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No clear capability claim is stated. | A dataset release gives tasks but no capability framing. [HLE] |
| General capability or intelligence | The benchmark claims broad overall capability, intelligence, or AGI-relevant performance. | GAIA framed as general AI assistant capability. [GAIA] |
| Reasoning | Tasks claim inference, logic, multi-step problem solving, or abstract reasoning. | GPQA graduate-level science reasoning questions. [GPQA] |
| Knowledge | Tasks test factual, academic, professional, or world knowledge. | HLE academic questions. [HLE] |
| Language understanding | Tasks test reading, comprehension, entailment, summarization, or linguistic interpretation. | TruthfulQA misconception-prone natural-language questions. [TruthfulQA] |
| Writing or generation quality | Tasks judge style, coherence, creativity, helpfulness, or long-form generation. | Essay-writing evaluation. [HLE] |
| Mathematics | Tasks target arithmetic, algebra, proof, contest math, or quantitative reasoning. | MMLU elementary mathematics subject questions. [LiveCodeBench] |
| Coding or software engineering | Tasks target code generation, repair, tests, repositories, or software tasks. | SWE-bench-style issue resolution. [SWE-bench] |
| Scientific or technical expertise | Tasks require STEM expertise or technical domain knowledge. | HLE physics, chemistry, biology, engineering items. [HLE] |
| Domain-specific professional expertise | Tasks target law, medicine, finance, cybersecurity, or other professional domains. | MMLU professional medicine subject questions. [MMLU] |
| Multimodal perception | Tasks require interpreting images, charts, diagrams, or mixed media. | HLE image questions, visual QA. [HLE] |
| Audio or speech | Input or output requires speech, audio events, transcription, or spoken interaction. | AudioBench ASR task. [AudioBench] |
| Video understanding | Tasks require interpreting temporal visual content. | Video-MME video question answering. [Video-MME] |
| Tool use | Systems must call calculators, search, APIs, code tools, or other external tools. | GAIA assistant tasks requiring tools or web browsing. [GAIA] |
| Planning or agency | Tasks require multi-step goal pursuit, state tracking, delegation, or autonomous action. | WebArena long-horizon browser tasks. [WebArena] |
| Web or browser interaction | Systems navigate websites or browser UIs. | WebArena browser-task benchmark. [WebArena] |
| Embodied or simulated environment interaction | Systems act in games, robotics simulators, or virtual environments. | no banked embodied benchmark; name the reviewed simulator benchmark. [No real example appropriate] |
| Safety, refusal, or policy compliance | Tasks evaluate harmful-content handling, refusal, jailbreak robustness, or policy adherence. | HarmBench red-team/refusal benchmark. [HarmBench] |
| Robustness | Tasks test performance under perturbations, distribution shift, adversarial prompts, or stressors. | HarmBench attack/defense robustness tasks. [HarmBench] |
| Calibration or uncertainty | Scores include confidence, uncertainty, abstention, or calibration. | HLE reports RMS calibration error. [HLE] |
| Other | A documented domain is not represented above. | "Legal contract review" if treated separately. [HLE] |

### 2.2 Area of Use

This section records what users are expected to do with results.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | The source does not state intended use. | A bare dataset card lists files without intended-use framing. [HLE] |
| Model comparison | Compare systems under similar conditions. | Comparing GPT, Claude, Gemini, and open-weight models. [HLE] |
| Leaderboard ranking | Rank submitted systems publicly or privately. | Chatbot Arena public ranking table. [Chatbot Arena] |
| Capability profiling | Identify strengths and weaknesses across domains. | Category scores for math, coding, and science. [HLE] |
| Research diagnostics | Study model behavior, failure modes, or measurement properties. | TruthfulQA analysis of false answers that mimic human misconceptions. [TruthfulQA] |
| Safety evaluation | Assess risk, compliance, misuse, or refusal behavior. | Jailbreak or harmful-advice benchmark. [HarmBench] |
| Deployment gating | Decide whether a system may be shipped or used. | HarmBench internal safety threshold. [HarmBench] |
| Procurement or vendor comparison | Support buying, vendor, or enterprise model-selection decisions. | HELM-style multi-provider vendor evaluation. [HELM] |
| Internal regression testing | Track model changes across releases. | LiveCodeBench release-version regression suite for a product model. [LiveCodeBench] |
| Public communication or marketing | Communicate model capability to the public. | Blog post headline using benchmark rank. [Chatbot Arena] |
| Policy or governance analysis | Inform standards, regulation, audits, or public-interest analysis. | HLE source mentions scientists, policymakers, and the broader public. [HLE] |
| Other | Any documented use outside the list. | Education placement, competition scoring. [HLE] |

### 2.3 Intended AI Systems

Record systems stated or clearly implied by the benchmark. Avoid expanding intended systems merely because a model could technically run.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No target system class is stated. | A benchmark lists tasks but no model target. [HLE] |
| Frontier general-purpose language models | Current high-capability general LLMs are target systems. | HLE evaluates frontier LLMs. [HLE] |
| Chat or instruction-following models | The evaluation assumes dialogue or instruction following. | Benchmarks using system/user prompts. [HLE] |
| Base language models | Raw next-token models without chat alignment are target systems. | Perplexity or completion benchmark. [HumanEval] |
| Code models | Systems specialized for programming tasks. | Code repair or unit-test benchmark. [HLE] |
| Multimodal models | Systems process more than one input modality, especially text plus images/audio/video. | HLE full-set evaluation with images. [HLE] |
| Audio or speech models | Speech-to-text, text-to-speech, audio QA, or spoken agents. | Audio understanding benchmark. [AudioBench] |
| Agentic systems | Systems that plan and act over multiple steps. | Autonomous web-task benchmark. [HLE] |
| Tool-using systems | Systems expected to call external tools. | Calculator or search-enabled benchmark. [GAIA] |
| Retrieval-augmented systems | Systems combine generation with retrieved documents. | Open-book QA with retrieval pipeline. [HLE] |
| Domain-specialized models | Systems trained or adapted for a domain. | Medical, legal, or cybersecurity model benchmark. [HLE] |
| Open-weight local models | Locally runnable released-weight models are in scope. | Llama-family evaluations. [HLE] |
| API-hosted models | Proprietary or hosted model APIs are in scope. | HELM uses multiple hosted provider APIs through a unified interface. [HELM] |
| Other | Another target class is documented. | Robotics policy models. [HLE] |

### 2.4 Intended Users of Benchmark Outputs

Select who is supposed to interpret or act on outputs.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No intended output users are named. | A repo with only tasks and scores. [HLE] |
| Benchmark creators or maintainers | Users who maintain, refresh, debug, or improve the benchmark. | HLE-Rolling maintainers. [HLE] |
| AI researchers | Academic or industry researchers studying model capability or measurement. | GPQA researchers comparing graduate-level science reasoning performance. [GPQA] |
| Model developers | Teams training, tuning, or evaluating models. | Lab evaluation team. [Chatbot Arena] |
| Product teams | Builders deciding product behavior or readiness. | LiveCodeBench release-version checks for code-model regressions. [LiveCodeBench] |
| Safety evaluators | Reviewers focused on harmful behavior or risk. | Internal or external safety audit team. [AudioBench] |
| Policy or governance actors | Regulators, standards bodies, auditors, public-interest groups. | Policymakers mentioned in HLE framing. [HLE] |
| Procurement or enterprise decision-makers | Buyers choosing vendors or systems. | Enterprise AI platform selection. [HLE] |
| Educators or academic reviewers | Course, exam, or scholarly assessment users. | Academic review of a GPQA benchmark paper. [GPQA] |
| Public leaderboard users | General audience interpreting ranks. | Users reading a Chatbot Arena public leaderboard. [Chatbot Arena] |
| Other | Any other intended recipient. | Competition organizers. [HLE] |

### 2.5 Task Families, Subdomains, and Scores

This table makes the construct-to-score structure explicit.

| Component | Meaning | HLE or generic example |
| :--- | :--- | :--- |
| Claimed construct or phenomenon | What the benchmark says it measures. | HLE: expert-level closed-ended academic capability. [HLE] |
| Construct subcomponents | Named parts of the construct. | Knowledge, reasoning, multimodal item comprehension, calibration. [HLE] |
| Task families or subdomains | Item categories or task groups. | Math, biology/medicine, physics, computer science/AI. [MMLU] |
| Task sampling or selection logic | How tasks were chosen from a larger possible space. | Expert submissions, review, audits, searchability checks. [GPQA] |
| Splits or partitions | Public/private, train/dev/test, easy/hard, domains, versions. | Public HLE set and private held-out set. [HLE] |
| Primary score | Main metric used for interpretation. | Accuracy percentage. [HELM] |
| Subscores | Scores for components, domains, or task types. | Category accuracy. [HLE] |
| Derived or aggregate scores | Computed metrics beyond raw primary scores. | Calibration error or cost-adjusted score. [HLE] |
| Qualitative labels or bands | Labels attached to score ranges. | "Expert", "pass", "high risk", if defined. [GPQA] |
| Claim boundaries or caveats | Limits stated by authors. | HLE does not by itself establish AGI or autonomous research. [HLE] |

### 2.6 Model Response Mode

This records what the model must produce.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Response format is not described. | No prompt or submission schema. [HLE] |
| Multiple choice | Choose one or more options. | HLE includes multiple-choice questions. [MMLU] |
| Short text | Produce a brief answer, phrase, or value. | Exact-answer science question. [SWE-bench] |
| Long-form text | Produce a paragraph, essay, report, or explanation. | Chatbot Arena free-form preference benchmark. [Chatbot Arena] |
| Structured output, such as JSON or XML | Output must follow a schema. | `{"answer":"B","confidence":0.72}`. [SWE-bench] |
| Code | Output source code, patches, SQL, or scripts. | SWE-bench issue-resolution benchmark. [SWE-bench] |
| Mathematical expression | Output formula, proof expression, or symbolic answer. | Algebra benchmark. [SWE-bench] |
| Tool call | Emit tool-call syntax or structured tool invocation. | GAIA tool-use benchmark. [GAIA] |
| Browser or web action | Click, type, navigate, or inspect web pages. | WebArena click, type, and navigation actions. [WebArena] |
| File, document, or artifact generation | Produce files such as reports, spreadsheets, slides, or apps. | no banked office-artifact benchmark; name the reviewed artifact benchmark. [No real example appropriate] |
| Image output | Generate or edit images. | Image generation evaluation. [MMMU] |
| Audio output | Generate speech, music, or audio. | Text-to-speech evaluation. [AudioBench] |
| Video output | Generate or edit video. | no banked video-generation benchmark; Video-MME is understanding, not generation. [No real example appropriate] |
| Interaction in a simulated environment | Act in a game, simulator, or virtual world. | Minecraft agent task. [WebArena] |
| Interaction in a real or external environment | Act in real services, robots, or live systems. | Real browser purchasing task, robotics task. [WebArena] |
| Other | Any documented response mode not listed. | Database transaction, email draft. [GAIA] |

### 2.7 Prerequisites for Evaluated Systems

Each row asks whether a capability is irrelevant, documented as needed, or missing.

| Requirement | Meaning | Example |
| :--- | :--- | :--- |
| Language support | Languages the system must understand or produce. | English-only benchmark, multilingual benchmark. [HLE] |
| Context length | Required prompt, document, or episode length. | Long-document QA needing 100k tokens. [HLE] |
| Multimodal input support | Need to process images, audio, video, or files. | HLE full-set image questions. [HLE] |
| Structured output support | Need to follow exact JSON/XML/schema/format. | Judge parser requires JSON. [HLE] |
| Tool access | Need calculators, code tools, APIs, search, or domain tools. | GAIA assistant questions requiring web browsing and tool use. [GAIA] |
| Browser or internet access | Need live web browsing or network access. | WebArena browser navigation tasks in a self-hosted web environment. [WebArena] |
| Code execution | Need to run generated code or tests. | Unit-test scoring benchmark. [HLE] |
| Memory or persistent state | Need state across tasks or sessions. | Long-horizon WebArena browser tasks. [WebArena] |
| API compatibility | Need a specific API interface or model-serving protocol. | OpenAI-compatible chat completions. [HumanEval] |
| Latency or time budget | Need to respond within time limits. | Interactive benchmark with 30-second limit. [HLE] |
| Cost or compute budget | Need a budget constraint for fair comparison. | Cost-adjusted leaderboard. [Chatbot Arena] |

### 2.8 Evaluation Conditions

Record the conditions required to run the benchmark as intended.

| Condition | Meaning | Example |
| :--- | :--- | :--- |
| Prompting protocol | How prompts are presented and whether zero-shot, few-shot, chain-of-thought, or other protocols are used. | HLE pilot records zero-shot chain-of-thought prompts. [HLE] |
| System prompt | Required system/developer instruction. | "You are a helpful assistant; answer with JSON." [SWE-bench] |
| Few-shot examples | Examples included before test items. | Three solved examples before each task. [HLE] |
| Sampling settings | Temperature, top-p, seed, max tokens, decoding. | Temperature 0 or specified model settings. [LiveCodeBench] |
| Tool permissions | Which tools may be used and under what rules. | Browser allowed, calculator banned. [GAIA] |
| Time limits | Per-task or full-run limits. | 10 minutes per task. [HLE] |
| Human intervention rules | Whether humans can help, select retries, adjudicate, or repair outputs. | HLE uses human experts in item construction, not routine model answering. [SWE-bench] |
| Hardware or hosted service | Required GPU, local machine, cloud service, hosted platform. | SWE-bench Multimodal private test split evaluator. [SWE-bench] |
| Network requirements | Need for internet, offline operation, or restricted network. | WebArena requires configured self-hosted site URLs rather than uncontrolled live public web. [WebArena] |
| Sandbox or security constraints | Isolation rules for code, tools, files, or external actions. | Code tasks run in Docker sandbox. [SWE-bench] |
| Other special conditions | Any other required condition. | Private holdout evaluation. [HLE] |

### 2.9 Task and Response Types

Selection-based responses ask the model to choose among given options.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Multiple choice, single correct answer | One option is correct. | Four-choice science item. [SWE-bench] |
| Multiple choice, multiple correct answers | More than one option may be correct. | "Select all that apply." [SWE-bench] |
| Ranking | Order options by preference, quality, risk, or relevance. | Rank retrieval passages. [HarmBench] |
| Classification | Assign a label. | Toxic/non-toxic, bug type, topic label. [HarmBench] |
| Pairwise preference | Choose better of two outputs or actions. | RLHF-style answer comparison. [SWE-bench] |

Production-based responses require generated content.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Open-ended text | Free-form answer or explanation. | Essay or short answer. [AudioBench] |
| Code generation | Source code, patch, tests, or scripts. | Function implementation. [SWE-bench] |
| Proof, derivation, or explanation | Step-by-step reasoning or justification. | Mathematical proof. [HLE] |
| Structured data | Schema-constrained output. | JSON extraction. [HLE] |
| Generated media | Image, audio, video, or other media. | Image generation task. [MMMU] |
| Artifact production | File or larger artifact. | Spreadsheet, report, app, or slide deck. [HLE] |

Interaction-based responses involve actions across steps.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Tool use | Calls external tools. | Calculator or search calls. [GAIA] |
| Browser or web navigation | Uses web UI actions. | Clicks through a shopping site. [WebArena] |
| API interaction | Calls APIs or services. | REST API task. [GAIA] |
| Computer-use interaction | Operates a desktop or GUI. | File manager task. [HLE] |
| Simulated environment task | Acts inside simulated environment. | Game or robotics simulator. [HLE] |
| Real or external environment task | Interacts with live external systems. | Real web form submission. [HLE] |

Process data options record auxiliary evidence rather than final answers.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Response latency | Time to answer. | Seconds per item. [AudioBench] |
| Token usage | Prompt, completion, or total tokens. | HLE reports average completion token counts. [HLE] |
| Cost | API or compute cost. | Dollars per successful task. [GAIA] |
| Tool traces | Sequence of tool calls and outputs. | Browser actions or code execution logs. [GAIA] |
| Intermediate reasoning traces | Recorded reasoning or scratchpad traces. | Chain-of-thought trace, if collected. [HLE] |
| Execution logs | Runtime logs from code, environment, or evaluator. | Unit-test output. [HLE] |
| Other | Other process evidence. | Memory state, retry count. [HLE] |

### 2.10 Input Stimulus Type

Record what the benchmark gives to the system.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Input type is unclear. | No prompt examples. [HLE] |
| Text | Natural language prompt or passage. | HLE text questions. [HLE] |
| Code | Source code, diffs, repositories, logs. | Code repair task. [SWE-bench] |
| Tables or structured data | CSV, JSON, database, table, chart data. | Table QA. [MMMU] |
| Images | Pictures, diagrams, screenshots, charts. | HLE image items. [MMMU] |
| Audio | Speech, sound, music, acoustic signal. | Speech QA. [AudioBench] |
| Video | Moving visual input. | Video understanding task. [Video-MME] |
| Documents | PDFs, Word files, slides, spreadsheets. | No banked document-question-answering example; name the actual document benchmark if reviewed. [No real example appropriate] |
| Web pages | HTML pages or browser-rendered pages. | Web navigation benchmark. [WebArena] |
| APIs or tools | Tool schemas, API endpoints, external services. | GAIA tool-use benchmark. [GAIA] |
| Dynamic environment | State changes as the model acts. | Game or simulator task. [WebArena] |
| Other | Any other stimulus. | Sensor stream. [WebArena] |

### 2.11 Number of Items or Measurement Points

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Total public items or tasks | Count inspectable by users. | HLE public 2,500 questions. [HLE] |
| Total private or hidden items | Count concealed from public. | Private held-out set count, if known. [HLE] |
| Development or example items | Items intended for practice, tuning, or format familiarization. | Dev set examples. [Chatbot Arena] |
| Test items | Items used for reported scores. | Public test set or hidden leaderboard set. [Chatbot Arena] |
| Dynamic or generated tasks | Number or range of generated tasks. | Procedural tasks per run. [HLE] |
| Episodes, trials, or measurement points | Repeated tasks, runs, trials, or environment episodes. | 100 agent episodes. [HLE] |
| Notes on item count uncertainty | Ambiguities, changing counts, or missing split counts. | "Private count not documented." [HLE] |

### 2.12 Mode of Evaluation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not indicated | Mode is not stated. | Paper reports results but no procedure. [HLE] |
| Local batch evaluation | User runs the benchmark locally over many items. | Python script evaluates a local model. [HumanEval] |
| Hosted benchmark platform | Evaluation happens on an official platform. | Chatbot Arena accepts public models through its hosted process. [Chatbot Arena] |
| Leaderboard submission | Users submit outputs or systems for ranked scoring. | Public leaderboard upload. [Chatbot Arena] |
| Private controlled evaluation | Maintainers evaluate hidden items or controlled conditions. | HLE private held-out evaluation. [HLE] |
| Public open evaluation | Anyone can run the benchmark on public materials. | Public dataset plus scorer. [HLE] |
| Interactive agent evaluation | Model acts step by step in an environment. | Browser-agent task. [WebArena] |
| Human-in-the-loop evaluation | Human input is part of evaluation. | Human rater scores open-ended answers. [AudioBench] |
| Continuous or rolling evaluation | Tasks or results update over time. | HLE-Rolling or live leaderboard. [HLE] |
| Other | Any other mode. | Competition event. [HLE] |

Identity and condition controls:

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No control over submitted systems | Maintainers cannot verify model identity or conditions. | Users self-report scores. [HLE] |
| Some control over submitted systems | Some metadata or submission checks exist. | Leaderboard requires model card and logs. [Chatbot Arena] |
| Controlled model access or audit | Evaluators can inspect or control model endpoint/version. | Private audit with fixed API access. [GAIA] |
| Controlled evaluation center or private harness | Evaluation happens in a controlled environment. | Hosted hidden test harness. [HLE] |
| Not documented | Control mechanisms are not stated. | No submission policy found. [HLE] |

### 2.13 Technological Arrangements

Mark `A` if available and `R` if required.

| Technology | Meaning | Example |
| :--- | :--- | :--- |
| API access | Benchmark supports or requires hosted model APIs. | HELM multi-provider hosted API evaluation. [HELM] |
| Local inference | Benchmark supports or requires local model serving. | Open-weight model run. [HLE] |
| GPU | GPU required or supported. | Local multimodal model inference. [MMMU] |
| CPU-only execution | Can be run without GPU or requires CPU-only path. | Small text benchmark scorer. [HLE] |
| Docker or container | Containerized environment exists or is required. | Code execution benchmark. [SWE-bench] |
| Python package or CLI | Package or command-line evaluator exists or is required. | `pip install` benchmark runner. [HumanEval] |
| Browser | Browser use is supported or required. | WebArena browser-agent environment. [WebArena] |
| External tools | Calculators, search, compilers, databases, APIs. | GAIA tool-use benchmark. [GAIA] |
| Internet access | Live network access is supported or required. | GAIA assistant tasks can require web browsing; WebArena uses configured self-hosted sites. [GAIA; WebArena] |
| Proprietary platform | Official closed platform or private service. | Chatbot Arena public ranking platform. [Chatbot Arena] |
| Other | Any other technology. | Robotics simulator. [HLE] |

### 2.14 Time and Resource Requirements

| Activity | Meaning | Example |
| :--- | :--- | :--- |
| Setup | Installation, data download, account setup, environment prep. | Docker build time. [SWE-bench] |
| Model inference or task completion | Time or compute for answering tasks. | Hours for full model run. [HumanEval] |
| Scoring | Time to parse, judge, execute tests, or aggregate results. | Unit tests over generated code. [HumanEval] |
| Human adjudication | Time for raters, experts, or reviewers. | Human judging of essays. [GPQA] |
| Analysis or reporting | Time to generate tables, dashboards, or error analysis. | Report script runtime. [HELM] |
| Full benchmark run | End-to-end total. | SWE-bench full-run resource cost and time. [SWE-bench] |
| API or compute cost | Monetary or compute budget. | Dollars per run, GPU-hours. [GAIA] |

### 2.15 Benchmark Forms, Versions, and Variants

Use this table when the benchmark has public/private forms, short forms, language versions, domain subsets, rolling versions, or deprecated versions.

| Field | Meaning | Example |
| :--- | :--- | :--- |
| Form or variant | Name of the version or subset. | Public HLE set, private held-out set, HLE-Rolling. [HLE] |
| Purpose | Why that form exists. | Hidden set for gaming/overfitting checks. [HLE] |
| Equivalence claim | Whether scores across forms are claimed comparable. | "Similar difficulty" or "not specified." [HLE] |
| Status | Active, planned, deprecated, hidden, public, archived. | Public release, planned dynamic fork. [HLE] |
| Source | Where this is documented. | Paper appendix or release notes. [HLE] |

### 2.16 Static or Dynamic Task Determination

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static fixed task set | Same fixed items are used. | Public HLE set. [HLE] |
| Random sample from fixed pool | Each run samples from a fixed item pool. | Random 500 tasks from 10,000. [HLE] |
| Hidden test set selected by maintainers | Maintainers select concealed items. | Private leaderboard holdout. [Chatbot Arena] |
| Procedurally generated tasks | Tasks are generated by rules or programs. | Random math problem generator. [HLE] |
| Adaptive routing based on performance | Later tasks depend on earlier performance. | Harder tasks after correct answers. [AudioBench] |
| Dynamic environment generation | Environment changes or is generated for each run. | Agent simulator with random maps. [MMMU] |
| Rolling or periodically refreshed task set | Items are updated over time. | HLE-Rolling. [HLE] |
| Not explicitly stated | Task selection method is not described. | Paper omits sampling method. [HLE] |
| Other | Other documented method. | Human-curated competition rounds. [HLE] |

### 2.17 Evidence Sources Used in Scoring

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Model final answer | Final response is scored. | HLE final answer. [HLE] |
| Model intermediate trace | Reasoning or scratchpad affects scoring. | Process-supervision benchmark. [HLE] |
| Tool-use trace | Tool calls or logs affect score. | Agent trajectory scoring. [GAIA] |
| Code execution result | Code is run and outcome scored. | Unit tests for coding task. [HumanEval] |
| Environment state | Final or intermediate environment state is scored. | Game score or completed web state. [WebArena] |
| Reference answer | Answer key is used. | Exact or rubric answer. [AudioBench] |
| Unit test | Tests decide correctness. | Pass/fail code tests. [HumanEval] |
| Human judge | Human rater scores output. | Essay quality benchmark. [HLE] |
| Model judge | AI judge scores or extracts correctness. | HLE model-judge scoring. [HLE] |
| Ensemble or panel adjudication | Multiple judges or raters are combined. | Human panel for safety tasks. [HarmBench] |
| External verifier | Independent tool or system checks correctness. | Theorem prover, compiler, database. [GAIA] |
| Other | Other evidence. | Peer review score. [HLE] |

### 2.18 Broad Claim and CHC/AGI Cautions

Complete this when broad terms appear in the title, paper, website, leaderboard, or publicity.

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Broad claim term used | Exact broad wording. | "AGI", "general intelligence", "expert capability." [GPQA] |
| Claimed breadth across domains | Range of domains claimed. | HLE spans many academic subjects. [MMLU] |
| Claimed depth or proficiency level | Claimed difficulty or expertise level. | Expert-level closed-ended academic questions. [GPQA] |
| Sub-abilities explicitly covered | Abilities actually measured. | Knowledge, closed-ended reasoning, some multimodal comprehension. [MMMU] |
| Sub-abilities explicitly excluded or not tested | Abilities the source excludes or does not measure. | Autonomous research, open-ended creativity, long-term planning. [GAIA] |
| Evidence across modalities, tools, memory, planning, or speed | Whether broader ability components are represented. | HLE includes some images but not standard tool-use or agency tasks. [MMMU] |
| Stated AGI, autonomy, or agency caveats | Author caveats about overinterpretation. | HLE paper cautions against AGI inference from HLE alone. [HLE] |
| Relation to CHC-like broad/narrow abilities, if claimed | Any explicit or reviewer-noted mapping to broad/narrow abilities. | "No explicit CHC mapping" for HLE. [AudioBench] |
| Descriptive caution for Part B | A note to later evaluators about claim scope. | Rate against narrow expert academic capability unless broader evidence is supplied. [GPQA] |

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Scoring process is not described. | Scores are reported without scorer details. [HLE] |
| Automated exact-match scoring | String, option, or value is matched to an answer key. | Multiple-choice accuracy. [AudioBench] |
| Automated semantic or embedding-based scoring | Automated similarity or semantic metric scores responses. | Embedding similarity for short answers. [AudioBench] |
| Unit-test or execution-based scoring | Output is executed or tested. | Code passes unit tests. [HumanEval] |
| Rule-based scoring | Deterministic rules parse or score outputs. | Regex checks for valid format. [HLE] |
| Human rating | Human raters judge output quality or correctness. | Expert scoring of explanations. [GPQA] |
| Model-as-judge scoring | A model scores, extracts, or adjudicates outputs. | HLE uses a model judge in the pilot. [HLE] |
| Pairwise preference scoring | Outputs are compared pairwise. | Which answer is better. [SWE-bench] |
| Hybrid automated and human scoring | Automated scoring plus human review. | Model judge with human adjudication of disputes. [HLE] |
| Leaderboard service scoring | Official service scores submissions. | Hidden hosted evaluator. [Chatbot Arena] |
| Manual adjudication | Humans resolve ambiguous or failed scoring cases. | Review malformed outputs. [HLE] |
| Other | Other scoring method. | External theorem prover. [HLE] |

Describe the scoring pipeline in order: input, model output, parser, judge or scorer, aggregation, invalid-response handling, and result reporting.

### 3.2 Scores and Metrics

| Score or metric | Meaning | Example |
| :--- | :--- | :--- |
| Primary score | Main score used to summarize benchmark performance. | HLE accuracy. [HLE] |
| Subscore | Score for domain, task family, modality, or condition. | HLE category accuracy. [HLE] |
| Derived score | Computed secondary metric. | RMS calibration error, cost-adjusted score. [HELM] |
| Qualitative band | Score label or interpretation category. | "Pass", "expert", "unsafe" if defined. [GPQA] |

For invalid, missing, malformed, or refused responses, record whether they are scored as incorrect, excluded, retried, manually reviewed, or handled by a special parser.

### 3.3 Scale or Metric Types

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Raw score | Count or untransformed total. | 73 correct items. [HLE] |
| Accuracy | Proportion or percent correct. | HLE accuracy percentage. [HLE] |
| Success rate | Percent of tasks completed successfully. | WebArena tasks completed. [WebArena] |
| Pass rate or pass@k | Whether at least one of k attempts passes. | Coding pass@1, pass@10. [HumanEval] |
| Unit-test pass rate | Percent of tests passed. | 18/20 tests pass. [HLE] |
| Win rate | Percent of pairwise comparisons won. | Preferred over baseline 62 percent. [Chatbot Arena] |
| Elo or ranking score | Relative rating from pairwise or competition results. | Arena-style ranking. [Chatbot Arena] |
| Pairwise preference score | Score from head-to-head preference comparisons. | Human preference benchmark. [Chatbot Arena] |
| Reward or return | Accumulated environment reward. | Game or RL task score. [HLE] |
| Cost-adjusted score | Performance adjusted by cost. | Accuracy per dollar. [HLE] |
| Calibration or uncertainty score | Measures confidence-quality relationship. | HLE RMS calibration error. [HLE] |
| Percentile or normalized score | Score transformed relative to group or scale. | 90th percentile among models. [HLE] |
| Threshold or decision index | Score used for pass/fail or categorization. | Deployment-gating index. [HLE] |
| Other | Benchmark-specific metric. | Exact F1, BLEU, ROUGE, risk score. [AudioBench] |

### 3.4 Score Transformation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No transformation | Report raw metric directly. | Percent correct. [HELM] |
| Linear transformation | Apply linear scaling. | Convert 0-1 to 0-100. [HLE] |
| Non-linear transformation | Apply non-linear formula. | Log-scaled reward. [HLE] |
| Normalization against baseline | Compare or scale relative to reference. | Score above random baseline. [HLE] |
| Weighting across subdomains | Domains contribute unequally. | HELM top-level aggregation across documented scenarios or metrics. [HELM] |
| Aggregation formula documented | Formula is fully stated. | Mean of domain accuracies with weights listed. [HLE] |
| Aggregation formula partially documented | Some formula details missing. | HLE pilot notes category weighting details are not fully specified in local source. [HLE] |
| Aggregation formula not documented | Aggregation is used but formula is absent. | Leaderboard total appears without method. [Chatbot Arena] |
| Not applicable | No transformation or aggregation issue applies. | Single unaggregated task score. [HLE] |

### 3.5 Reference Groups, Baselines, and Comparators

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No baseline or comparator documented | No reference performance is stated. | Standalone score only; record this as an evidence gap rather than inventing a comparator. [No real example appropriate] |
| Random or chance baseline | Expected performance from random behavior. | MMLU four-choice chance floor. [MMLU] |
| Human baseline | Non-expert or general human performance. | GPQA skilled non-expert validator accuracy. [GPQA] |
| Expert human baseline | Qualified expert performance. | GPQA domain expert performance. [GPQA] |
| Model baseline | One or more model scores used as reference. | GPQA paper's GPT-4 based baseline. [GPQA] |
| Previous model cohort | Earlier generation of models. | LiveCodeBench dated release windows for older/newer code-model comparisons. [LiveCodeBench] |
| Commercial system comparator | Proprietary production systems. | HELM hosted-provider model set. [HELM] |
| Open-weight model comparator | Released-weight local models. | HELM open-weight model entries when configured. [HELM] |
| Domain-specific reference group | Specialized systems or experts. | GPQA domain experts in biology, physics, and chemistry. [GPQA] |
| Other | Other comparator. | LiveCodeBench prior benchmark release version. [LiveCodeBench] |

For each `Comparator or baseline` row, record construction method, intended interpretation, and source. HLE compares several frontier models and references expert-level academic capability, but the pilot records limited quantified expert score-distribution evidence.

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
| Sensitivity analyses | Checks for prompt, parser, model version, or condition sensitivity. | Prompt variant comparison. [LiveCodeBench] |
| Not reported | No uncertainty or stability evidence is reported. | Single score table only. [HELM] |
| Other | Other stability evidence. | HLE pilot records expert disagreement rates and model non-determinism caveat. [GPQA] |

### 3.7 Metric-to-Claim Linkage

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Why the primary metric was chosen | Rationale for metric fit. | Accuracy fits closed-ended HLE questions. [HLE] |
| Whether metric floors or ceilings are documented | Chance levels, saturation, max/min behavior. | HLE notes non-zero multiple-choice floor. [HLE] |
| Whether the metric may reward non-target behavior named by the source | Source-stated shortcuts or confounds. | Formatting, memorization, search, or judge artifacts. [GAIA] |
| Whether parsing, judge, or scorer validation is documented | Evidence scorer measures intended thing. | Judge prompt plus validation study. [HLE] |
| Whether score uncertainty affects claim interpretation | Whether uncertainty changes conclusions. | Confidence intervals overlap. [GPQA] |
| Whether score differences are interpreted statistically | Whether rankings or differences use significance/uncertainty. | Statistical comparison of two models. [GPQA] |
| Whether benchmark reports state what users should not infer | Explicit non-use or caveat statements. | HLE says high score alone does not imply AGI. [HLE] |

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Public leaderboard available | Ranked results are publicly accessible. | Chatbot Arena public ranking table. [Chatbot Arena] |
| Public aggregate scores available | Overall scores are public. | Paper table with overall accuracy. [HLE] |
| Public per-domain scores available | Domain or category scores are public. | HLE category results. [HLE] |
| Public per-item scores available | Item-level correctness is public. | CSV with each question result. [HLE] |
| Public raw model outputs available | Actual model responses are released. | JSONL completions. [HumanEval] |
| Public traces or logs available | Tool, reasoning, execution, or environment logs are public. | Agent trajectory logs. [GAIA] |
| Private reports available only to submitters | Results are returned privately. | Hosted audit report. [HLE] |
| No formal report or leaderboard documented | Only informal or no reporting is found. | Results mentioned without artifact. [Chatbot Arena] |

### 4.2 Output Name or Description

Use one row per output artifact. Include paper tables, dashboards, downloadable files, leaderboards, private submitter reports, and API responses. "Public/private" should state who can see it.

### 4.3 Output Design or Presentation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static text report | Narrative report. | PDF or paper section. [HLE] |
| Tables | Tabular scores. | HLE result tables. [HLE] |
| Graphs or visualizations | Charts or figures. | Calibration plot. [HLE] |
| Leaderboard | Ranked list of systems. | Chatbot Arena public ranking table. [Chatbot Arena] |
| Interactive dashboard | Filterable or dynamic UI. | Dashboard by model and domain. [HELM] |
| Downloadable CSV or JSON | Machine-readable result files. | `results.csv`. [HLE] |
| API output | Results returned by API. | Evaluation endpoint response. [GAIA] |
| Paper-only results | Results exist only in paper. | No downloadable results. [HLE] |
| Other | Other presentation. | Notebook, slide deck. [HLE] |

### 4.4 Output Structure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Aggregate-score based | Organized around total scores. | Overall accuracy ranking. [Chatbot Arena] |
| Capability-domain based | Organized by capability areas. | Math, coding, safety. [HarmBench] |
| Task-family based | Organized by task type. | Browser, API, file tasks. [GAIA] |
| Criterion-threshold based | Organized by pass/fail or score bands. | Deployment gate. [HLE] |
| Pairwise-comparison based | Organized by head-to-head outcomes. | Arena win matrix. [Chatbot Arena] |
| Rank based | Emphasizes ordering. | Leaderboard rank. [Chatbot Arena] |
| Cost or efficiency adjusted | Includes cost, latency, or token efficiency. | Accuracy per dollar. [HELM] |
| Error-analysis based | Includes error categories. | Failure taxonomy. [HLE] |
| Trace or process based | Includes trajectories or logs. | Tool trace report. [GAIA] |
| Other | Other structure. | Qualitative audit memo. [HLE] |

### 4.5 Sensitivity to Context

| Option | Meaning | Example |
| :--- | :--- | :--- |
| One output format for all contexts | Same report for all users or uses. | Single public table. [HLE] |
| User-definable output contexts | Users can customize report scope or audience. | Dashboard filters for domains. [HELM] |
| Pre-defined versions adapted to audience or use | Different fixed reports for different audiences. | Technical report plus executive scorecard. [HLE] |
| Context sensitivity not documented | No source says whether reports differ by use. | Paper-only results. [HLE] |

### 4.6 Development of Outputs

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Based on benchmark authors' design | Authors chose report fields and formats. | Paper tables designed by benchmark authors. [HLE] |
| Based on empirical or actuarial relationships | Report content follows statistical or empirical score relationships. | Validated risk bands. [HLE] |
| Based on expert judgment | Experts shape interpretation or categories. | Expert-defined domain labels. [GPQA] |
| Based on human annotation | Human labels or judgments feed reports. | Human-rated answer categories. [AudioBench] |
| Based on model-as-judge outputs | AI judge produces score or labels shown in report. | Model-judge correctness extraction. [HLE] |
| Automatically generated by benchmark platform | Platform generates report. | Submitter dashboard. [HELM] |
| Other | Other source of report content. | Community-maintained leaderboard. [Chatbot Arena] |

### 4.7 Modifiability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not modifiable | Users cannot change report contents. | Fixed paper table. [HLE] |
| Limited modification by submitter or user | Users can filter, export, or add metadata. | Dashboard filters. [HELM] |
| Fully user-generated reports possible | Users can create custom reports from released data. | Public raw outputs and item scores. [HLE] |
| Not documented | Modifiability is not stated. | Unknown platform behavior. [HLE] |

### 4.8 Transparency

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Clear linkage between tasks, scores, and reported claims | Reports explain how tasks and metrics support claims. | Scorecard links each claim to task family and metric. [HELM] |
| Partial linkage between tasks, scores, and reported claims | Some links are clear, others unexplained. | Domain scores shown but broad headline unexplained. [HLE] |
| Linkage is not obvious from available documentation | User cannot tell how score supports claim. | Ranking only. [Chatbot Arena] |
| Mixture of clear and concealed linkage | Some details public, some hidden for integrity or platform reasons. | Public aggregate with hidden item-level scoring. [HLE] |
| Not documented | No evidence about linkage. | mark not documented when the source gives no report evidence. [No real example appropriate] |

### 4.9 Output Content

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Capability descriptions | Text explaining what scores indicate. | "Measures closed-ended academic performance." [HLE] |
| Aggregate rankings | Overall rank or total score. | Leaderboard rank. [Chatbot Arena] |
| Subdomain comparisons | Domain or category differences. | HLE category results. [HLE] |
| Error categories | Types of failures. | Parsing error, hallucination, unsafe compliance. [HarmBench] |
| Examples of successes or failures | Sample outputs. | Correct/incorrect responses. [HLE] |
| Cost, latency, or efficiency data | Runtime, token, cost, compute. | HLE completion token counts. [HLE] |
| Process traces | Tool calls, logs, reasoning traces. | Agent trajectory. [GAIA] |
| Recommendations or interpretation notes | Guidance on using results. | Suggested non-use cases. [HLE] |
| Warnings or caveats | Limits and risks. | AGI caveat. [HLE] |
| Other | Other content. | Confidence histograms. [HLE] |

### 4.10 Intended Recipients

Use the same logic as Section 2.4, but focus on report recipients rather than intended users of the benchmark generally. A benchmark might be built for researchers but publish a simplified public leaderboard.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark maintainers | People who maintain tasks, scoring, reports, or platform outputs. | Maintainers using results to identify benchmark saturation. [HLE] |
| Model developers | Teams building or improving evaluated systems. | Lab teams checking regressions. [Chatbot Arena] |
| AI researchers | Researchers studying model capabilities or benchmark behavior. | GPQA research comparison of science reasoning performance. [GPQA] |
| Safety evaluators | Users focused on safety, refusal, harm, or risk. | Safety audit report. [HarmBench] |
| Policy or governance actors | Users making governance, standards, or policy judgments. | Policy memo using benchmark evidence. [HLE] |
| Product or deployment teams | Teams deciding product behavior, release readiness, or deployment constraints. | Product launch readiness review. [HLE] |
| Procurement teams | Buyers or enterprise evaluators comparing vendors. | Vendor-selection scorecard. [HLE] |
| Public audience | General readers of public results or leaderboards. | Public-facing leaderboard users. [Chatbot Arena] |
| Other: | Another documented recipient. | Competition judges, educators, domain boards. [HLE] |

## Section 5. Supply Arrangements and Materials

### 5.1 Supporting Information Provided

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Technical report | Formal methods/results document. | GPQA benchmark paper. [GPQA] |
| User guide | Practical instructions for running or interpreting. | Documentation site. [HELM] |
| Repository README | Repo-level usage and overview. | GitHub README. [SWE-bench] |
| API documentation | API endpoint or schema instructions. | Hosted evaluator API docs. [GAIA] |
| Dataset card | Dataset metadata, license, splits, provenance. | Hugging Face card. [HLE] |
| Model submission instructions | Rules for submitting systems or outputs. | Leaderboard submission guide. [Chatbot Arena] |
| Scoring documentation | Scoring method, formula, parser, judge, tests. | HLE scorer prompt and scoring notes. [HELM] |
| Rubric or annotation guide | Human or judge scoring rubric. | Safety severity rubric. [HarmBench] |
| Evaluation examples | Sample tasks, submissions, expected outputs. | Example JSONL submission. [HumanEval] |
| FAQ or discussion forum | Support and clarifications. | GitHub Discussions. [SWE-bench] |
| Changelog or release notes | Version and update history. | HLE-Rolling notes. [LiveCodeBench] |
| Other | Other support material. | Video tutorial. [Video-MME] |

### 5.2 Methods of Publication

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Academic paper | Published or preprint paper. | arXiv GPQA benchmark paper. [GPQA] |
| Benchmark website | Official website. | Benchmark landing page. [HLE] |
| Git repository | Code-hosting repository. | GitHub repo. [SWE-bench] |
| Package registry | Installable package. | PyPI package. [HLE] |
| Dataset hosting platform | Hosted dataset. | Hugging Face dataset. [HLE] |
| Leaderboard platform | Hosted ranking/submission site. | Eval platform leaderboard. [Chatbot Arena] |
| Downloadable documents | PDFs, CSVs, guides, spreadsheets. | PDF technical report. [HLE] |
| Private distribution | Materials shared only with approved users. | Private holdout or gated audit. [HLE] |
| Other | Other publication path. | Conference competition portal. [HLE] |

### 5.3 User Requirements or Qualifications

| Requirement type | Meaning | Example |
| :--- | :--- | :--- |
| Technical expertise | Skills needed to run or interpret. | Python, Docker, API use. [SWE-bench] |
| Compute or infrastructure | Hardware or hosted services. | GPU, cloud account. [HLE] |
| Account or access approval | Login, API keys, approval, NDA. | Leaderboard account. [GAIA] |
| Legal or license terms | Usage, redistribution, research-only terms. | Non-commercial dataset license. [HLE] |
| Cost or fee | Monetary cost. | Paid API or platform fee. [GAIA] |
| Security or privacy requirements | Handling sensitive data or sandboxing. | No exfiltration, private data policy. [HLE] |
| Other | Any other requirement. | Domain certification for human raters. [HLE] |

### 5.4 Dataset and Item Access

| Component | Meaning | Example |
| :--- | :--- | :--- |
| Training or example data | Practice or development examples. | Public examples. [Chatbot Arena] |
| Development set | Data for tuning prompts or systems. | Dev split. [Chatbot Arena] |
| Test set | Data used for evaluation scores. | HLE public test questions. [HLE] |
| Private holdout set | Hidden test material. | HLE private held-out set. [HLE] |
| Prompt templates | Exact prompt formatting. | System/user prompt templates. [HLE] |
| Reference answers | Answer keys or expected outputs. | Correct multiple-choice letters. [SWE-bench] |
| Rubrics | Criteria for scoring open or ambiguous outputs. | Human judge rubric. [HLE] |

Mark each component as public, restricted, hidden, or not available. A component may be hidden by design; describe the reason if stated.

### 5.5 Provenance and Contamination Documentation

This section records documentation only.

| Topic | Meaning | Example |
| :--- | :--- | :--- |
| Data source provenance | Where items/data came from. | Expert submissions, public web data, synthetic generator. [GPQA] |
| Collection procedure | How data was gathered. | Contributor process and submission rules. [HLE] |
| Filtering or quality control | How bad, duplicate, invalid, or unsuitable items were removed. | Expert review, audits. [GPQA] |
| Licensing or rights | Rights to distribute and evaluate. | Contributor license or dataset license. [HLE] |
| Deduplication | Duplicate-removal methods. | Exact or semantic dedupe. [HLE] |
| Contamination controls | Steps to reduce training-data exposure. | Private split, delayed release. [LiveCodeBench] |
| Searchability or source-exposure checks | Whether items can be found online or in source data. | HLE searchability checks. [GAIA] |
| Canary, GUID, encryption, or anti-scraping method | Technical markers or protections for leakage detection. | Canary strings in hidden set. [GAIA] |
| Training-on-test diagnostic task | Tests designed to detect memorization of benchmark items. | Diagnostic prompts. [HLE] |
| Public/private split rationale | Why some data is public and some hidden. | HLE private set for overfitting/gaming checks. [HLE] |
| Update or refresh policy | How items are added, retired, or refreshed. | LiveCodeBench rolling benchmark. [LiveCodeBench] |
| Release rules or anti-gaming terms | Rules limiting leakage, tuning, scraping, or submissions. | No training on test set. [LiveCodeBench] |

### 5.6 Reproducibility Materials

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Complete evaluation code | End-to-end runnable evaluator. | Repo script for full benchmark. [HLE] |
| Scoring scripts | Code for scoring outputs. | Judge parser or unit-test scorer. [HLE] |
| Environment file or dependency list | Requirements needed to recreate runtime. | `requirements.txt`, `environment.yml`. [HLE] |
| Container or reproducible runtime | Docker image or equivalent. | Dockerfile. [SWE-bench] |
| Prompt templates | Exact prompts used. | HLE evaluation prompt. [HLE] |
| Example submissions | Sample outputs in expected format. | JSONL example. [HumanEval] |
| Raw outputs from reported models | Model responses used for reported results. | Released completions. [HumanEval] |
| Random seeds | Seeds for sampling or task generation. | Seed list. [LiveCodeBench] |
| Configuration files | Model, scorer, prompt, or environment configs. | YAML run configs. [LiveCodeBench] |
| Expected outputs or tests | Tests that verify setup and scoring. | Golden outputs. [HumanEval] |
| Result replication script | Script that regenerates paper/leaderboard results. | `reproduce_results.py`. [HumanEval] |
| Build status or continuous integration check | CI showing code works. | Passing GitHub Actions badge. [SWE-bench] |
| None documented | No reproducibility materials are documented. | paper-only benchmark scope with MMLU as a cautionary example. [MMLU] |

### 5.7 Maintenance and Versioning

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Current maintenance status | Active, inactive, archived, planned, unclear. | Active rolling updates. [LiveCodeBench] |
| Latest documented release | Most recent version/date. | GitHub release tag. [HLE] |
| Changelog available | Whether changes are documented. | Release notes. [Chatbot Arena] |
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
| Task or item quality | Development process, expert review, item audits. | Expert submissions and audits. [GPQA] |
| Scoring validity | Metric, parser, judge, rubric, scorer validation. | Model-judge prompt and validation evidence if available. [HELM] |
| Reliability or run stability | Repeats, seeds, uncertainty, rater agreement. | Expert disagreement rates, confidence intervals. [LiveCodeBench] |
| Baselines and comparators | Human, expert, chance, model, prior versions. | HELM multi-provider model cohort. [LiveCodeBench] |
| Fairness or comparability | Conditions across systems, domains, languages, modalities. | Text-only versus full-set distinction. [HLE] |
| Reproducibility | Data, code, prompts, configs, raw outputs. | Evaluation code and raw outputs. [HELM] |
| Contamination and gameability | Public/private split, search checks, anti-gaming rules. | Private holdout. [GAIA] |
| Maintenance and benchmark drift | Versioning, changelog, refresh, retirement. | Rolling updates. [LiveCodeBench] |
| Interpretation limits | Stated caveats and non-use cases. | Do not infer AGI from HLE alone. [HLE] |
| Leaderboard or public-claim risk | Reports, ranks, public messaging. | Leaderboard caveats and version labels. [LiveCodeBench] |
| Other | Benchmark-specific issue. | Safety-sensitive content handling. [SWE-bench] |

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
| Phenomenon-task-metric-claim chain | Whether the source links phenomenon, task, metric, and claim. | Accuracy on narrow tasks used to claim broad agency without argument. [HELM] | Explicit chain with confounds and safeguards. [HELM] |
| Task/item development quality | How tasks were designed, reviewed, sampled, and revised. | No item source or review process. [GPQA] | Expert review, structured criteria, audits, revision history. [GPQA] |
| Documentation and procedural instructions | Whether users can administer, score, and interpret correctly. | Incomplete setup and scoring instructions. [HELM] | Current, source-linked, complete user documentation. [HELM] |

### 6.2 Section 6 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 6.1 Rationale and construct definition | Adequacy of the purpose and construct definition. | HLE defines closed-ended academic challenge better than broad AGI. [HLE] |
| 6.2 Phenomenon-task-metric-claim chain | Fit among claim, tasks, metric, and interpretation. | Accuracy fits closed-ended items, but broader claims need caution. [HLE] |
| 6.3 Development process and task/item quality | Evidence about item creation, expertise, review, and quality control. | Expert submissions and audits. [GPQA] |
| 6.4 Documentation available to users | Availability and completeness of user-facing documentation. | Paper plus missing repository or license details. [SWE-bench] |
| 6.5 Procedural instructions for administration, scoring, and interpretation | Whether run, scoring, and interpretation instructions are sufficient. | Prompt documented, exact harness missing. [HLE] |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality | Reviewer synthesis of Section 6. | Do not mechanically average rows. [AudioBench] |

## Section 7. Quality of Benchmark Materials and Usability

Section 7 rates whether the actual materials can be obtained, understood, and used correctly.

### 7.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Materials availability | Whether datasets, prompts, rubrics, and task materials exist and are accessible. | Key materials missing. [HLE] | Complete, versioned, licensed materials. [HLE] |
| Evaluation harness and scoring tools | Whether users can run and reproduce scoring. | Opaque hosted-only or absent scorer. [GAIA] | Runnable, tested harness with examples. [GAIA] |
| Prompts, rubrics, and response formats | Whether instructions and formats are clear and validated. | Ambiguous prompts or fragile parser. [HLE] | Documented prompts, rubrics, parser tests. [HLE] |
| Accessibility and usability | Whether intended users and systems can use materials. | Requirements exclude relevant systems without warning. [HLE] | Quick starts, support, modality/language access notes. [HLE] |

### 7.2 Section 7 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 7.1 Dataset, task set, or environment availability | Availability of tasks, data, or environments. | Public tasks available, private holdout hidden. [HLE] |
| 7.2 Prompts, instructions, rubrics, and response format | Clarity and access to prompts/rubrics/formats. | HLE prompt and judge instructions. [HLE] |
| 7.3 Evaluation harness, scorer, and implementation usability | Ability to run scorer correctly. | Complete CLI versus paper-only scoring description. [HLE] |
| 7.4 Accessibility across relevant modalities, languages, and system types | Whether relevant systems can participate fairly. | Text-only subset for models lacking image input. [MMMU] |
| 7.5 Licensing, usage requirements, and sensitive-content warnings | Legal and safety instructions for use. | License documented or missing. [HarmBench] |
| 7.6 Overall quality of benchmark materials | Reviewer synthesis of material quality. | Consider access restrictions and intended use. [AudioBench] |

## Section 8. Baselines, Comparators, and Reference Interpretation

Section 8 adapts EFPA norms into AI benchmark baselines, floors, ceilings, human/expert comparisons, model cohorts, and thresholds.

### 8.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Baseline construction | Whether reference levels are meaningful and documented. | No baseline where one is needed. [HLE] | Representative, uncertainty-aware baselines. [HLE] |
| Human/expert comparators | Whether human claims have methods. | "Expert-level" with no expert procedure. [GPQA] | Documented qualifications, sampling, conditions. [GPQA] |
| Model comparators | Whether model comparisons are current and specified. | Cherry-picked or version-ambiguous cohort. [HLE] | Versions, settings, and conditions clear. [HLE] |
| Floors, ceilings, thresholds | Whether chance, saturation, and decision levels are handled. | Chance floor ignored. [HLE] | Floors, ceilings, thresholds empirically integrated. [HLE] |

### 8.2 Section 8 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 8.1 Random, chance, floor, and ceiling baselines | Chance levels, lower bounds, saturation, score ceilings. | HLE notes non-zero multiple-choice floor. [HLE] |
| 8.2 Human or expert baselines | Human performance and expert comparison methods. | Expert contributors are not the same as a quantified expert baseline. [GPQA] |
| 8.3 Model comparator cohort | Model selection, versions, and evaluation conditions. | HELM model table with provider/version details. [HELM] |
| 8.4 Criterion thresholds or score bands | Pass/fail or interpretive cutoffs. | Deployment threshold, if validated. [HLE] |
| 8.5 Overall adequacy of baselines and reference interpretation | Synthesis of reference interpretation quality. | Explain usable reference points and missing anchors. [HLE] |

## Section 9. Reliability, Precision, and Score Stability

Section 9 rates whether scores are stable and precise enough for the intended use.

### 9.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Run stability and uncertainty | Repeated runs, seeds, uncertainty intervals, stochasticity. | Single scores despite known variability. [HLE] | Comprehensive repeat-run and uncertainty evidence. [HLE] |
| Scorer, judge, or rater reliability | Reliability of scorers, parsers, raters, judges. | Model judge with no validation. [HLE] | Agreement and validation across edge cases. [HLE] |
| Form, version, and prompt stability | Comparability across prompts, versions, forms, environments. | Mixed versions without equivalence evidence. [LiveCodeBench] | Drift and equivalence tested. [LiveCodeBench] |
| Statistical comparison quality | Whether score differences are statistically interpretable. | Ranks without uncertainty. [GPQA] | Comparisons use uncertainty/significance methods. [GPQA] |

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
| Metric and scoring validity | Whether the metric rewards intended capability. | Metric rewards formatting, memorization, or judge artifacts. [HELM] | Metric, parser, scorer, aggregation validated. [HELM] |
| Relations with other evidence | Convergent, discriminant, criterion, ecological evidence. | Comparisons absent or misleading. [HLE] | Relevant comparisons interpreted cautiously. [HLE] |
| Contamination and gameability | Leakage, public exposure, tuning, gaming controls. | Risks ignored despite public tasks. [LiveCodeBench] | Private splits, canaries, audits, release rules. [LiveCodeBench] |
| Claim proportionality, including AGI/agency | Whether claims match measurement breadth and depth. | AGI claim from narrow task score. [HLE] | Broad claims supported across relevant sub-abilities or explicitly rejected. [HLE] |

### 10.2 Section 10 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 10.1 Content validity and task representativeness | Coverage and sampling of intended domain. | HLE broad academic domains, but not all cognitive abilities. [HLE] |
| 10.2 Internal structure, subscores, or dimensionality | Whether subscores/dimensions behave as claimed. | Category scores require support if interpreted as dimensions. [HLE] |
| 10.3 Metric, scorer, and aggregation validity | Fit and validation of scoring. | Accuracy for closed-ended questions; judge validation gap. [HLE] |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings | External comparisons and ecological relevance. | Comparison to prior saturated benchmarks. [HLE] |
| 10.5 Contamination, leakage, and gameability controls | Controls against exposure and gaming. | Searchability checks and private holdout. [LiveCodeBench] |
| 10.6 Claim proportionality and broad-capability cautions | Whether public claims stay within evidence. | HLE caveat against AGI inference. [HLE] |
| 10.7 Overall validity evidence | Synthesis of validity for intended use. | Usually the most important Part B judgment. [HLE] |

## Section 11. Fair Use, Comparability, and Appropriate Use

Section 11 rates whether benchmark use is fair and comparable across relevant systems, modalities, languages, domains, access modes, and user contexts.

### 11.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Cross-system comparability | Whether conditions are comparable across systems. | Different tools/prompts/settings without caveat. [GAIA] | Conditions controlled and differences handled. [GAIA] |
| Domain, language, modality, and subgroup coverage | Whether coverage supports intended comparisons. | English-only benchmark used for multilingual claim. [HLE] | Coverage analyzed and limits tied to interpretation. [HLE] |
| Access, compute, and usability fairness | Whether access or compute requirements distort comparison. | Proprietary platform excludes relevant systems without warning. [HLE] | Inclusive, documented access paths. [HLE] |
| Appropriate-use guidance | Whether guidance prevents overinterpretation. | Marketing encourages unsupported claims. [HLE] | Prominent non-use and limitation guidance. [HLE] |

### 11.2 Section 11 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 11.1 Cross-system and evaluation-condition comparability | Prompt, model access, settings, tools, and scoring fairness. | Same prompt/settings across compared models. [GAIA] |
| 11.2 Domain, language, modality, and subgroup fairness | Coverage across relevant domains/languages/modalities/groups. | HLE text-only versus full-set reporting. [HLE] |
| 11.3 Access, compute, tooling, and API/local comparability | Whether resource requirements affect comparability. | API-only benchmark versus open-weight local models. [GAIA] |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance | Rules and warnings for responsible use. | Anti-gaming terms, sensitive-content notices. [HLE] |
| 11.5 Overall fair use and comparability | Synthesis of fair-use evidence. | State which comparisons are safe or limited. [HLE] |

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

Section 12 rates whether benchmark outputs communicate results accurately, clearly, and proportionally.

### 12.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Report scope and granularity | Whether reports show enough detail for claims. | Aggregate only despite domain claims. [HLE] | Aggregate, subscores, uncertainty, caveats. [HLE] |
| Leaderboard or dashboard quality | Versioning, ranking clarity, update policy, reproducibility. | Opaque rankings. [Chatbot Arena] | Versioned, documented, uncertainty-aware display. [Chatbot Arena] |
| Report reliability and validity | Whether reports accurately reflect scores and limits. | Public claims diverge from score support. [HLE] | Score-to-claim links and limits explained. [HLE] |
| Public communication and acceptability | Whether public messaging is cautious and audience-appropriate. | Headline overclaims. [HLE] | Transparent, accessible, evidence-aligned communication. [HLE] |

### 12.2 Section 12 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 12.1 Report, leaderboard, dashboard, or result artifact scope | Whether outputs cover relevant results. | Paper tables, leaderboard, dashboard. [Chatbot Arena] |
| 12.2 Score granularity, uncertainty, and version labeling | Detail, uncertainty, version clarity. | Category scores plus missing CIs. [LiveCodeBench] |
| 12.3 Linkage from scores to public claims | Whether claims follow from scores. | AGI caveat included or absent. [HLE] |
| 12.4 Raw outputs, per-item data, or trace availability | Inspectability of underlying outputs. | Released model completions or logs. [HumanEval] |
| 12.5 Overall quality of reports and public claims | Synthesis of reporting quality. | State public interpretation risks. [HarmBench] |

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

