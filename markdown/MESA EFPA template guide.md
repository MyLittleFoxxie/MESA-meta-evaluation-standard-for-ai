# MESA EFPA Template User Guide

This guide explains how to use `markdown/MESA EFPA template.md`. It is a companion document, not a replacement for the template. Use the same section numbers to move between the two files.

MESA treats an AI benchmark as a measurement instrument. Part A describes what the benchmark is and what the sources say. Part B evaluates whether the benchmark supports its stated interpretation. Keep those two activities separate: do not put ratings in Part A, and do not make unsupported judgments in Part B.

Examples use Humanity's Last Exam (HLE) where the local pilot review provides evidence. Generic examples are included for benchmark types HLE does not cover, such as coding, tool-use, safety, multimodal, agentic, and hosted leaderboard benchmarks.

## Core Reviewer Rules

### Documentation Status Options

| Option | Meaning | Select when | Do not select when | Example |
| :--- | :--- | :--- | :--- | :--- |
| Documented | The source gives enough information to record the field confidently. | The official paper, repository, documentation, dataset card, or maintainer statement states the fact directly. | You inferred the fact from examples, screenshots, or common practice. | HLE documents a public set of 2,500 questions. |
| Partially documented | Some information is present, but important details are missing or internally incomplete. | The source names a private set but omits its size, access process, or selection method. | The source is simply silent. | HLE states a private held-out set exists but the local pilot notes that its count is not documented. |
| Not documented | The available sources do not state the information. | No reviewed source gives the license, repository, random seeds, or run cost. | The issue is irrelevant to this benchmark type. | If no source states a leaderboard, mark leaderboard status as not documented rather than assuming one exists. |
| Not applicable | The field does not apply to the benchmark or intended use. | A text-only benchmark has no audio-output requirement. | The field could apply but evidence is missing. | "Video output" is not applicable for a multiple-choice text benchmark. |
| Unclear from available sources | The sources contain ambiguity, conflict, or wording that prevents a confident classification. | Two sections give different judge model versions, or a website implies but does not state a submission process. | The evidence is merely incomplete but not ambiguous. | The HLE pilot treats exact scorer-version evidence as partly unclear because local source statements differ. |

### Part A vs Part B

Part A records claims and evidence. "The benchmark reports category accuracy" is Part A. "The category accuracy is too coarse for the claim" is Part B.

Part B rates adequacy. Each rating must include evidence used, missing evidence, reviewer rationale, and interpretation caution. Missing documentation is an evidence gap. It is not proof of poor benchmark quality unless a source-grounded defect is shown.

### Broad Claims and Narrow Evidence

If a benchmark claims "general intelligence", "AGI", "reasoning", "agency", "autonomy", or "expert capability", record the term in Part A and check what domains, sub-abilities, modalities, tools, planning, memory, and speed are actually measured. HLE is a useful example: it can support a narrow description of expert-level closed-ended academic performance, but the pilot records explicit caution against treating HLE accuracy alone as proof of AGI or autonomous research ability.

### Available vs Required

"Available" means the benchmark supports or permits something. "Required" means the benchmark cannot be run as intended without it. A coding benchmark might make Docker available for convenience but require Python. A hosted agent benchmark might require browser access and internet access.

### Public, Restricted, Hidden, and Not Available

| Access label | Meaning | Example |
| :--- | :--- | :--- |
| Public | Anyone can inspect or download the component under stated terms. | Public example tasks in a repository. |
| Restricted | Access exists but requires approval, account access, payment, license agreement, or submitter status. | A dataset available through gated hosting. |
| Hidden | The component exists but is intentionally concealed to protect evaluation integrity. | A private holdout set used for leaderboard scoring. |
| Not available | The component is not released or no source indicates it exists. | Raw outputs from reported models are not provided. |

### Baseline, Comparator, Threshold, Floor, and Ceiling

| Term | Meaning | Example |
| :--- | :--- | :--- |
| Baseline | A reference performance level used to interpret scores. | Random-choice accuracy on multiple-choice questions. |
| Comparator | A system, human group, benchmark version, or cohort used for comparison. | GPT-4O, Claude, expert humans, or a prior benchmark. |
| Threshold | A decision boundary or score band with an intended interpretation. | "Pass" at 80 percent or "expert-level" above a validated cutoff. |
| Floor | The lowest expected performance level under trivial or chance behavior. | A four-option multiple-choice benchmark has a non-zero chance floor. |
| Ceiling | The upper end where the benchmark stops distinguishing systems well. | A saturated benchmark where frontier models score near 100 percent. |

## Information Sources

Use this table to record the evidence base before filling the template.

| Source type | Meaning and use | Example |
| :--- | :--- | :--- |
| Official paper or technical report | Main author-provided description of purpose, data, methods, scoring, and results. Prefer this before commentary. | HLE paper in `markdown/Papers/Humanitys_Last_Exam.md`. |
| Benchmark website | Public landing page, documentation hub, access portal, or official result page. | `https://lastexam.ai`, if independently reviewed. |
| Repository | Code, issues, releases, examples, scripts, and maintenance activity. | A GitHub repository with an evaluation harness. |
| Dataset card or data host | Dataset metadata, splits, licenses, provenance, access restrictions, and versioning. | Hugging Face dataset card for public tasks. |
| Leaderboard or results page | Ranking, submission rules, public scores, update dates, and system metadata. | Hosted leaderboard with model submissions. |
| Evaluation harness or package | Runnable code, package, CLI, scorer, or platform used for evaluation. | `lm-eval-harness`, a benchmark-specific Python package, or hosted API. |
| Documentation or user guide | Setup, submission, interpretation, scoring, and troubleshooting instructions. | `docs/`, README, quick start, or API docs. |
| Release notes or changelog | Version history, refresh policy, retired tasks, score comparability notes. | HLE-Rolling notes or GitHub releases. |
| Maintainer statements | Authoritative clarifications from issues, discussions, papers, or official posts. | A maintainer issue comment explaining hidden test policy. |
| Independent sources used for context | Non-official sources used to interpret background, not to replace official facts. | A critique paper explaining contamination concerns. |

## Part B Rating Scale

| Rating | Meaning | Use carefully |
| :--- | :--- | :--- |
| `n/a` | The criterion is not applicable to this benchmark or intended use. | Use only when the criterion truly does not apply, not when evidence is missing. |
| `0` | Cannot rate because available evidence is insufficient. | Use for evidence gaps. Do not treat this as a quality defect by itself. |
| `1` | Inadequate evidence or practice for the intended interpretation. | Use when evidence shows weak, unsuitable, or misleading practice. |
| `2` | Adequate for cautious use within a clearly bounded interpretation. | Use when the benchmark can support limited use but has notable gaps. |
| `3` | Good evidence or practice with meaningful but non-fatal gaps. | Use when evidence is strong enough for intended use, while caveats remain. |
| `4` | Excellent evidence or practice, comprehensive and well matched to intended use. | Reserve for broad, current, well-documented, and independently usable evidence. |

Every Part B row has five required concepts: the criterion being rated, the rating, evidence used, missing evidence, reviewer rationale, and interpretation caution. A bare number is not a MESA rating.

# Part A. Description of the Benchmark

## Section 1. Factual Description

### 1.1 Review Information

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Reviewer | Person or team completing the review. | "MESA reviewer" or named reviewers. |
| Date of current review | Date the evidence was reviewed, not necessarily publication date. | `2026-05-04`. |
| Date of previous review, if applicable | Earlier review date if this is an update. | `2026-05-01` for an HLE pilot refresh. |
| Review scope | Boundary of the review. State whether it covers Part A only, full Part A/B, local sources only, or external verification. | "Descriptive Part A review using local markdown only." |
| Sources reviewed | Short list or pointer to the Information Sources table. | "HLE paper; no external verification." |

### 1.2 Benchmark Information

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark name | Full official name. | "Humanity's Last Exam." |
| Short name or acronym | Abbreviation used in papers, leaderboards, or code. | "HLE." |
| Benchmark version, edition, or release | Version number, release tag, edition, date-stamped release, or note that no version is stated. | "Original public set; no version number documented." |
| Original benchmark name, if this is an adaptation | Source benchmark if this review covers a translated, modified, or domain-specific version. | "MMLU-Pro adaptation" for a derivative benchmark. |
| Benchmark creators or authors | Original authors, organizers, contributors, or institution. | HLE organizing team. |
| Current maintainers | People or group responsible now. | Repository maintainers, benchmark organization, or "not documented." |
| Host organization, publisher, or distributor | Entity distributing the benchmark or platform. | University lab, Scale AI, Hugging Face, Papers with Code. |
| Date of original release | First public release date. | Paper publication date or repository release. |
| Date of current release or revision | Date of the version reviewed. | Latest GitHub release date. |
| License or access terms | Legal usage terms, dataset license, submission rules, or "not documented." | Apache-2.0, CC BY, gated research license. |
| Persistent identifier, citation, or DOI | DOI, arXiv ID, citation, permanent URL, or dataset identifier. | arXiv ID for a benchmark paper. |

### 1.3 Public Artifacts

Use this table to separate artifact existence from artifact quality. Part B evaluates adequacy later.

| Artifact | Means | Access status examples | Notes example |
| :--- | :--- | :--- | :--- |
| Paper or technical report | Formal benchmark description and results. | Available, missing, restricted. | "Available locally." |
| Benchmark website | Official public site or documentation hub. | Stated but not verified, available, missing. | "Website named in paper." |
| Code repository | Source code for data, evaluation, or scoring. | Public, private, not documented. | "No repository in supplied markdown." |
| Evaluation harness | Runnable evaluator, package, or hosted submission system. | Public package, hosted only, not documented. | "Scorer described but harness not released." |
| Dataset or task set | Prompts, items, episodes, environments, or tasks. | Public, restricted, hidden, partially documented. | "Public 2,500-question set." |
| Prompt set | Exact prompts or prompt templates. | Included in paper, in repo, not documented. | "Evaluation prompt in appendix." |
| Rubric or scoring guide | Answer keys, grading rubrics, judge prompts, unit tests. | Available, partially documented, hidden. | "Model-judge prompt documented." |
| Leaderboard | Public or private ranking and submission record. | Public leaderboard, paper tables only, not documented. | "HLE pilot records no formal leaderboard in local source." |
| Changelog or release notes | Version history and update policy. | GitHub releases, paper appendix, missing. | "HLE-Rolling notes." |
| Contact or issue channel | Maintainer contact, issue tracker, email, forum. | GitHub issues, email, not documented. | "Issue channel not found." |

## Section 2. Classification

### 2.1 Claimed Capability Domains

Select only domains claimed or clearly implied by benchmark documentation. Use "Other" for a named domain not listed. If the benchmark name implies a domain but the paper never states it, note that ambiguity.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No clear capability claim is stated. | A dataset release gives tasks but no capability framing. |
| General capability or intelligence | The benchmark claims broad overall capability, intelligence, or AGI-relevant performance. | A benchmark marketed as "general AI capability." |
| Reasoning | Tasks claim inference, logic, multi-step problem solving, or abstract reasoning. | Math word problems or theorem proofs. |
| Knowledge | Tasks test factual, academic, professional, or world knowledge. | HLE academic questions. |
| Language understanding | Tasks test reading, comprehension, entailment, summarization, or linguistic interpretation. | Reading-comprehension benchmark. |
| Writing or generation quality | Tasks judge style, coherence, creativity, helpfulness, or long-form generation. | Essay-writing evaluation. |
| Mathematics | Tasks target arithmetic, algebra, proof, contest math, or quantitative reasoning. | GSM-style math benchmark. |
| Coding or software engineering | Tasks target code generation, repair, tests, repositories, or software tasks. | SWE-bench-style issue resolution. |
| Scientific or technical expertise | Tasks require STEM expertise or technical domain knowledge. | HLE physics, chemistry, biology, engineering items. |
| Domain-specific professional expertise | Tasks target law, medicine, finance, cybersecurity, or other professional domains. | Medical licensing question benchmark. |
| Multimodal perception | Tasks require interpreting images, charts, diagrams, or mixed media. | HLE image questions, visual QA. |
| Audio or speech | Input or output requires speech, audio events, transcription, or spoken interaction. | Speech recognition benchmark. |
| Video understanding | Tasks require interpreting temporal visual content. | Video QA benchmark. |
| Tool use | Systems must call calculators, search, APIs, code tools, or other external tools. | Tool-calling benchmark with API traces. |
| Planning or agency | Tasks require multi-step goal pursuit, state tracking, delegation, or autonomous action. | Agent benchmark with long-horizon tasks. |
| Web or browser interaction | Systems navigate websites or browser UIs. | Web task benchmark. |
| Embodied or simulated environment interaction | Systems act in games, robotics simulators, or virtual environments. | Minecraft or robotics simulation benchmark. |
| Safety, refusal, or policy compliance | Tasks evaluate harmful-content handling, refusal, jailbreak robustness, or policy adherence. | Safety red-team benchmark. |
| Robustness | Tasks test performance under perturbations, distribution shift, adversarial prompts, or stressors. | Prompt-injection robustness benchmark. |
| Calibration or uncertainty | Scores include confidence, uncertainty, abstention, or calibration. | HLE reports RMS calibration error. |
| Other | A documented domain is not represented above. | "Legal contract review" if treated separately. |

### 2.2 Area of Use

This section records what users are expected to do with results.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | The source does not state intended use. | A dataset card only lists files. |
| Model comparison | Compare systems under similar conditions. | Comparing GPT, Claude, Gemini, and open-weight models. |
| Leaderboard ranking | Rank submitted systems publicly or privately. | Hosted benchmark leaderboard. |
| Capability profiling | Identify strengths and weaknesses across domains. | Category scores for math, coding, and science. |
| Research diagnostics | Study model behavior, failure modes, or measurement properties. | Error analysis in a paper. |
| Safety evaluation | Assess risk, compliance, misuse, or refusal behavior. | Jailbreak or harmful-advice benchmark. |
| Deployment gating | Decide whether a system may be shipped or used. | Internal minimum safety threshold. |
| Procurement or vendor comparison | Support buying, vendor, or enterprise model-selection decisions. | Enterprise evaluation of API providers. |
| Internal regression testing | Track model changes across releases. | Nightly benchmark suite for a product model. |
| Public communication or marketing | Communicate model capability to the public. | Blog post headline using benchmark rank. |
| Policy or governance analysis | Inform standards, regulation, audits, or public-interest analysis. | HLE source mentions scientists, policymakers, and the broader public. |
| Other | Any documented use outside the list. | Education placement, competition scoring. |

### 2.3 Intended AI Systems

Record systems stated or clearly implied by the benchmark. Avoid expanding intended systems merely because a model could technically run.

| Option | Meaning and when to select | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No target system class is stated. | A benchmark lists tasks but no model target. |
| Frontier general-purpose language models | Current high-capability general LLMs are target systems. | HLE evaluates frontier LLMs. |
| Chat or instruction-following models | The evaluation assumes dialogue or instruction following. | Benchmarks using system/user prompts. |
| Base language models | Raw next-token models without chat alignment are target systems. | Perplexity or completion benchmark. |
| Code models | Systems specialized for programming tasks. | Code repair or unit-test benchmark. |
| Multimodal models | Systems process more than one input modality, especially text plus images/audio/video. | HLE full-set evaluation with images. |
| Audio or speech models | Speech-to-text, text-to-speech, audio QA, or spoken agents. | Audio understanding benchmark. |
| Agentic systems | Systems that plan and act over multiple steps. | Autonomous web-task benchmark. |
| Tool-using systems | Systems expected to call external tools. | Calculator or search-enabled benchmark. |
| Retrieval-augmented systems | Systems combine generation with retrieved documents. | Open-book QA with retrieval pipeline. |
| Domain-specialized models | Systems trained or adapted for a domain. | Medical, legal, or cybersecurity model benchmark. |
| Open-weight local models | Locally runnable released-weight models are in scope. | Llama-family evaluations. |
| API-hosted models | Proprietary or hosted model APIs are in scope. | OpenAI, Anthropic, Google, or other API models. |
| Other | Another target class is documented. | Robotics policy models. |

### 2.4 Intended Users of Benchmark Outputs

Select who is supposed to interpret or act on outputs.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | No intended output users are named. | A repo with only tasks and scores. |
| Benchmark creators or maintainers | Users who maintain, refresh, debug, or improve the benchmark. | HLE-Rolling maintainers. |
| AI researchers | Academic or industry researchers studying model capability or measurement. | Researchers comparing reasoning models. |
| Model developers | Teams training, tuning, or evaluating models. | Lab evaluation team. |
| Product teams | Builders deciding product behavior or readiness. | Assistant product team checking regressions. |
| Safety evaluators | Reviewers focused on harmful behavior or risk. | Internal or external safety audit team. |
| Policy or governance actors | Regulators, standards bodies, auditors, public-interest groups. | Policymakers mentioned in HLE framing. |
| Procurement or enterprise decision-makers | Buyers choosing vendors or systems. | Enterprise AI platform selection. |
| Educators or academic reviewers | Course, exam, or scholarly assessment users. | Academic review of a benchmark paper. |
| Public leaderboard users | General audience interpreting ranks. | Users reading a public benchmark leaderboard. |
| Other | Any other intended recipient. | Competition organizers. |

### 2.5 Task Families, Subdomains, and Scores

This table makes the construct-to-score structure explicit.

| Component | Meaning | HLE or generic example |
| :--- | :--- | :--- |
| Claimed construct or phenomenon | What the benchmark says it measures. | HLE: expert-level closed-ended academic capability. |
| Construct subcomponents | Named parts of the construct. | Knowledge, reasoning, multimodal item comprehension, calibration. |
| Task families or subdomains | Item categories or task groups. | Math, biology/medicine, physics, computer science/AI. |
| Task sampling or selection logic | How tasks were chosen from a larger possible space. | Expert submissions, review, audits, searchability checks. |
| Splits or partitions | Public/private, train/dev/test, easy/hard, domains, versions. | Public HLE set and private held-out set. |
| Primary score | Main metric used for interpretation. | Accuracy percentage. |
| Subscores | Scores for components, domains, or task types. | Category accuracy. |
| Derived or aggregate scores | Computed metrics beyond raw primary scores. | Calibration error or cost-adjusted score. |
| Qualitative labels or bands | Labels attached to score ranges. | "Expert", "pass", "high risk", if defined. |
| Claim boundaries or caveats | Limits stated by authors. | HLE does not by itself establish AGI or autonomous research. |

### 2.6 Model Response Mode

This records what the model must produce.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Response format is not described. | No prompt or submission schema. |
| Multiple choice | Choose one or more options. | HLE includes multiple-choice questions. |
| Short text | Produce a brief answer, phrase, or value. | Exact-answer science question. |
| Long-form text | Produce a paragraph, essay, report, or explanation. | Writing-quality benchmark. |
| Structured output, such as JSON or XML | Output must follow a schema. | `{"answer":"B","confidence":0.72}`. |
| Code | Output source code, patches, SQL, or scripts. | Coding benchmark. |
| Mathematical expression | Output formula, proof expression, or symbolic answer. | Algebra benchmark. |
| Tool call | Emit tool-call syntax or structured tool invocation. | Function-calling benchmark. |
| Browser or web action | Click, type, navigate, or inspect web pages. | Web-agent benchmark. |
| File, document, or artifact generation | Produce files such as reports, spreadsheets, slides, or apps. | Office-document generation benchmark. |
| Image output | Generate or edit images. | Image generation evaluation. |
| Audio output | Generate speech, music, or audio. | Text-to-speech evaluation. |
| Video output | Generate or edit video. | Video generation benchmark. |
| Interaction in a simulated environment | Act in a game, simulator, or virtual world. | Minecraft agent task. |
| Interaction in a real or external environment | Act in real services, robots, or live systems. | Real browser purchasing task, robotics task. |
| Other | Any documented response mode not listed. | Database transaction, email draft. |

### 2.7 Prerequisites for Evaluated Systems

Each row asks whether a capability is irrelevant, documented as needed, or missing.

| Requirement | Meaning | Example |
| :--- | :--- | :--- |
| Language support | Languages the system must understand or produce. | English-only benchmark, multilingual benchmark. |
| Context length | Required prompt, document, or episode length. | Long-document QA needing 100k tokens. |
| Multimodal input support | Need to process images, audio, video, or files. | HLE full-set image questions. |
| Structured output support | Need to follow exact JSON/XML/schema/format. | Judge parser requires JSON. |
| Tool access | Need calculators, code tools, APIs, search, or domain tools. | Agent benchmark with tool calls. |
| Browser or internet access | Need live web browsing or network access. | Web navigation benchmark. |
| Code execution | Need to run generated code or tests. | Unit-test scoring benchmark. |
| Memory or persistent state | Need state across tasks or sessions. | Long-horizon agent benchmark. |
| API compatibility | Need a specific API interface or model-serving protocol. | OpenAI-compatible chat completions. |
| Latency or time budget | Need to respond within time limits. | Interactive benchmark with 30-second limit. |
| Cost or compute budget | Need a budget constraint for fair comparison. | Cost-adjusted leaderboard. |

### 2.8 Evaluation Conditions

Record the conditions required to run the benchmark as intended.

| Condition | Meaning | Example |
| :--- | :--- | :--- |
| Prompting protocol | How prompts are presented and whether zero-shot, few-shot, chain-of-thought, or other protocols are used. | HLE pilot records zero-shot chain-of-thought prompts. |
| System prompt | Required system/developer instruction. | "You are a helpful assistant; answer with JSON." |
| Few-shot examples | Examples included before test items. | Three solved examples before each task. |
| Sampling settings | Temperature, top-p, seed, max tokens, decoding. | Temperature 0 or specified model settings. |
| Tool permissions | Which tools may be used and under what rules. | Browser allowed, calculator banned. |
| Time limits | Per-task or full-run limits. | 10 minutes per task. |
| Human intervention rules | Whether humans can help, select retries, adjudicate, or repair outputs. | HLE uses human experts in item construction, not routine model answering. |
| Hardware or hosted service | Required GPU, local machine, cloud service, hosted platform. | Hosted private evaluator. |
| Network requirements | Need for internet, offline operation, or restricted network. | Browser-agent benchmark requiring live web. |
| Sandbox or security constraints | Isolation rules for code, tools, files, or external actions. | Code tasks run in Docker sandbox. |
| Other special conditions | Any other required condition. | Private holdout evaluation. |

### 2.9 Task and Response Types

Selection-based responses ask the model to choose among given options.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Multiple choice, single correct answer | One option is correct. | Four-choice science item. |
| Multiple choice, multiple correct answers | More than one option may be correct. | "Select all that apply." |
| Ranking | Order options by preference, quality, risk, or relevance. | Rank retrieval passages. |
| Classification | Assign a label. | Toxic/non-toxic, bug type, topic label. |
| Pairwise preference | Choose better of two outputs or actions. | RLHF-style answer comparison. |

Production-based responses require generated content.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Open-ended text | Free-form answer or explanation. | Essay or short answer. |
| Code generation | Source code, patch, tests, or scripts. | Function implementation. |
| Proof, derivation, or explanation | Step-by-step reasoning or justification. | Mathematical proof. |
| Structured data | Schema-constrained output. | JSON extraction. |
| Generated media | Image, audio, video, or other media. | Image generation task. |
| Artifact production | File or larger artifact. | Spreadsheet, report, app, or slide deck. |

Interaction-based responses involve actions across steps.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Tool use | Calls external tools. | Calculator or search calls. |
| Browser or web navigation | Uses web UI actions. | Clicks through a shopping site. |
| API interaction | Calls APIs or services. | REST API task. |
| Computer-use interaction | Operates a desktop or GUI. | File manager task. |
| Simulated environment task | Acts inside simulated environment. | Game or robotics simulator. |
| Real or external environment task | Interacts with live external systems. | Real web form submission. |

Process data options record auxiliary evidence rather than final answers.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Response latency | Time to answer. | Seconds per item. |
| Token usage | Prompt, completion, or total tokens. | HLE reports average completion token counts. |
| Cost | API or compute cost. | Dollars per successful task. |
| Tool traces | Sequence of tool calls and outputs. | Browser actions or code execution logs. |
| Intermediate reasoning traces | Recorded reasoning or scratchpad traces. | Chain-of-thought trace, if collected. |
| Execution logs | Runtime logs from code, environment, or evaluator. | Unit-test output. |
| Other | Other process evidence. | Memory state, retry count. |

### 2.10 Input Stimulus Type

Record what the benchmark gives to the system.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Input type is unclear. | No prompt examples. |
| Text | Natural language prompt or passage. | HLE text questions. |
| Code | Source code, diffs, repositories, logs. | Code repair task. |
| Tables or structured data | CSV, JSON, database, table, chart data. | Table QA. |
| Images | Pictures, diagrams, screenshots, charts. | HLE image items. |
| Audio | Speech, sound, music, acoustic signal. | Speech QA. |
| Video | Moving visual input. | Video understanding task. |
| Documents | PDFs, Word files, slides, spreadsheets. | Document QA benchmark. |
| Web pages | HTML pages or browser-rendered pages. | Web navigation benchmark. |
| APIs or tools | Tool schemas, API endpoints, external services. | Function-calling benchmark. |
| Dynamic environment | State changes as the model acts. | Game or simulator task. |
| Other | Any other stimulus. | Sensor stream. |

### 2.11 Number of Items or Measurement Points

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Total public items or tasks | Count inspectable by users. | HLE public 2,500 questions. |
| Total private or hidden items | Count concealed from public. | Private held-out set count, if known. |
| Development or example items | Items intended for practice, tuning, or format familiarization. | Dev set examples. |
| Test items | Items used for reported scores. | Public test set or hidden leaderboard set. |
| Dynamic or generated tasks | Number or range of generated tasks. | Procedural tasks per run. |
| Episodes, trials, or measurement points | Repeated tasks, runs, trials, or environment episodes. | 100 agent episodes. |
| Notes on item count uncertainty | Ambiguities, changing counts, or missing split counts. | "Private count not documented." |

### 2.12 Mode of Evaluation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not indicated | Mode is not stated. | Paper reports results but no procedure. |
| Local batch evaluation | User runs the benchmark locally over many items. | Python script evaluates a local model. |
| Hosted benchmark platform | Evaluation happens on an official platform. | Platform accepts model endpoint. |
| Leaderboard submission | Users submit outputs or systems for ranked scoring. | Public leaderboard upload. |
| Private controlled evaluation | Maintainers evaluate hidden items or controlled conditions. | HLE private held-out evaluation. |
| Public open evaluation | Anyone can run the benchmark on public materials. | Public dataset plus scorer. |
| Interactive agent evaluation | Model acts step by step in an environment. | Browser-agent task. |
| Human-in-the-loop evaluation | Human input is part of evaluation. | Human rater scores open-ended answers. |
| Continuous or rolling evaluation | Tasks or results update over time. | HLE-Rolling or live leaderboard. |
| Other | Any other mode. | Competition event. |

Identity and condition controls:

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No control over submitted systems | Maintainers cannot verify model identity or conditions. | Users self-report scores. |
| Some control over submitted systems | Some metadata or submission checks exist. | Leaderboard requires model card and logs. |
| Controlled model access or audit | Evaluators can inspect or control model endpoint/version. | Private audit with fixed API access. |
| Controlled evaluation center or private harness | Evaluation happens in a controlled environment. | Hosted hidden test harness. |
| Not documented | Control mechanisms are not stated. | No submission policy found. |

### 2.13 Technological Arrangements

Mark `A` if available and `R` if required.

| Technology | Meaning | Example |
| :--- | :--- | :--- |
| API access | Benchmark supports or requires hosted model APIs. | API-hosted frontier model evaluation. |
| Local inference | Benchmark supports or requires local model serving. | Open-weight model run. |
| GPU | GPU required or supported. | Local multimodal model inference. |
| CPU-only execution | Can be run without GPU or requires CPU-only path. | Small text benchmark scorer. |
| Docker or container | Containerized environment exists or is required. | Code execution benchmark. |
| Python package or CLI | Package or command-line evaluator exists or is required. | `pip install` benchmark runner. |
| Browser | Browser use is supported or required. | Web-agent benchmark. |
| External tools | Calculators, search, compilers, databases, APIs. | Tool-use benchmark. |
| Internet access | Live network access is supported or required. | Web search benchmark. |
| Proprietary platform | Official closed platform or private service. | Hosted leaderboard evaluator. |
| Other | Any other technology. | Robotics simulator. |

### 2.14 Time and Resource Requirements

| Activity | Meaning | Example |
| :--- | :--- | :--- |
| Setup | Installation, data download, account setup, environment prep. | Docker build time. |
| Model inference or task completion | Time or compute for answering tasks. | Hours for full model run. |
| Scoring | Time to parse, judge, execute tests, or aggregate results. | Unit tests over generated code. |
| Human adjudication | Time for raters, experts, or reviewers. | Human judging of essays. |
| Analysis or reporting | Time to generate tables, dashboards, or error analysis. | Report script runtime. |
| Full benchmark run | End-to-end total. | Full public benchmark cost and time. |
| API or compute cost | Monetary or compute budget. | Dollars per run, GPU-hours. |

### 2.15 Benchmark Forms, Versions, and Variants

Use this table when the benchmark has public/private forms, short forms, language versions, domain subsets, rolling versions, or deprecated versions.

| Field | Meaning | Example |
| :--- | :--- | :--- |
| Form or variant | Name of the version or subset. | Public HLE set, private held-out set, HLE-Rolling. |
| Purpose | Why that form exists. | Hidden set for gaming/overfitting checks. |
| Equivalence claim | Whether scores across forms are claimed comparable. | "Similar difficulty" or "not specified." |
| Status | Active, planned, deprecated, hidden, public, archived. | Public release, planned dynamic fork. |
| Source | Where this is documented. | Paper appendix or release notes. |

### 2.16 Static or Dynamic Task Determination

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static fixed task set | Same fixed items are used. | Public HLE set. |
| Random sample from fixed pool | Each run samples from a fixed item pool. | Random 500 tasks from 10,000. |
| Hidden test set selected by maintainers | Maintainers select concealed items. | Private leaderboard holdout. |
| Procedurally generated tasks | Tasks are generated by rules or programs. | Random math problem generator. |
| Adaptive routing based on performance | Later tasks depend on earlier performance. | Harder tasks after correct answers. |
| Dynamic environment generation | Environment changes or is generated for each run. | Agent simulator with random maps. |
| Rolling or periodically refreshed task set | Items are updated over time. | HLE-Rolling. |
| Not explicitly stated | Task selection method is not described. | Paper omits sampling method. |
| Other | Other documented method. | Human-curated competition rounds. |

### 2.17 Evidence Sources Used in Scoring

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Model final answer | Final response is scored. | HLE final answer. |
| Model intermediate trace | Reasoning or scratchpad affects scoring. | Process-supervision benchmark. |
| Tool-use trace | Tool calls or logs affect score. | Agent trajectory scoring. |
| Code execution result | Code is run and outcome scored. | Unit tests for coding task. |
| Environment state | Final or intermediate environment state is scored. | Game score or completed web state. |
| Reference answer | Answer key is used. | Exact or rubric answer. |
| Unit test | Tests decide correctness. | Pass/fail code tests. |
| Human judge | Human rater scores output. | Essay quality benchmark. |
| Model judge | AI judge scores or extracts correctness. | HLE model-judge scoring. |
| Ensemble or panel adjudication | Multiple judges or raters are combined. | Human panel for safety tasks. |
| External verifier | Independent tool or system checks correctness. | Theorem prover, compiler, database. |
| Other | Other evidence. | Peer review score. |

### 2.18 Broad Claim and CHC/AGI Cautions

Complete this when broad terms appear in the title, paper, website, leaderboard, or publicity.

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Broad claim term used | Exact broad wording. | "AGI", "general intelligence", "expert capability." |
| Claimed breadth across domains | Range of domains claimed. | HLE spans many academic subjects. |
| Claimed depth or proficiency level | Claimed difficulty or expertise level. | Expert-level closed-ended academic questions. |
| Sub-abilities explicitly covered | Abilities actually measured. | Knowledge, closed-ended reasoning, some multimodal comprehension. |
| Sub-abilities explicitly excluded or not tested | Abilities the source excludes or does not measure. | Autonomous research, open-ended creativity, long-term planning. |
| Evidence across modalities, tools, memory, planning, or speed | Whether broader ability components are represented. | HLE includes some images but not standard tool-use or agency tasks. |
| Stated AGI, autonomy, or agency caveats | Author caveats about overinterpretation. | HLE paper cautions against AGI inference from HLE alone. |
| Relation to CHC-like broad/narrow abilities, if claimed | Any explicit or reviewer-noted mapping to broad/narrow abilities. | "No explicit CHC mapping" for HLE. |
| Descriptive caution for Part B | A note to later evaluators about claim scope. | Rate against narrow expert academic capability unless broader evidence is supplied. |

## Section 3. Measurement and Scoring

### 3.1 Scoring Procedure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not explicitly stated | Scoring process is not described. | Scores are reported without scorer details. |
| Automated exact-match scoring | String, option, or value is matched to an answer key. | Multiple-choice accuracy. |
| Automated semantic or embedding-based scoring | Automated similarity or semantic metric scores responses. | Embedding similarity for short answers. |
| Unit-test or execution-based scoring | Output is executed or tested. | Code passes unit tests. |
| Rule-based scoring | Deterministic rules parse or score outputs. | Regex checks for valid format. |
| Human rating | Human raters judge output quality or correctness. | Expert scoring of explanations. |
| Model-as-judge scoring | A model scores, extracts, or adjudicates outputs. | HLE uses a model judge in the pilot. |
| Pairwise preference scoring | Outputs are compared pairwise. | Which answer is better. |
| Hybrid automated and human scoring | Automated scoring plus human review. | Model judge with human adjudication of disputes. |
| Leaderboard service scoring | Official service scores submissions. | Hidden hosted evaluator. |
| Manual adjudication | Humans resolve ambiguous or failed scoring cases. | Review malformed outputs. |
| Other | Other scoring method. | External theorem prover. |

Describe the scoring pipeline in order: input, model output, parser, judge or scorer, aggregation, invalid-response handling, and result reporting.

### 3.2 Scores and Metrics

| Score or metric | Meaning | Example |
| :--- | :--- | :--- |
| Primary score | Main score used to summarize benchmark performance. | HLE accuracy. |
| Subscore | Score for domain, task family, modality, or condition. | HLE category accuracy. |
| Derived score | Computed secondary metric. | RMS calibration error, cost-adjusted score. |
| Qualitative band | Score label or interpretation category. | "Pass", "expert", "unsafe" if defined. |

For invalid, missing, malformed, or refused responses, record whether they are scored as incorrect, excluded, retried, manually reviewed, or handled by a special parser.

### 3.3 Scale or Metric Types

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Raw score | Count or untransformed total. | 73 correct items. |
| Accuracy | Proportion or percent correct. | HLE accuracy percentage. |
| Success rate | Percent of tasks completed successfully. | Web tasks completed. |
| Pass rate or pass@k | Whether at least one of k attempts passes. | Coding pass@1, pass@10. |
| Unit-test pass rate | Percent of tests passed. | 18/20 tests pass. |
| Win rate | Percent of pairwise comparisons won. | Preferred over baseline 62 percent. |
| Elo or ranking score | Relative rating from pairwise or competition results. | Arena-style ranking. |
| Pairwise preference score | Score from head-to-head preference comparisons. | Human preference benchmark. |
| Reward or return | Accumulated environment reward. | Game or RL task score. |
| Cost-adjusted score | Performance adjusted by cost. | Accuracy per dollar. |
| Calibration or uncertainty score | Measures confidence-quality relationship. | HLE RMS calibration error. |
| Percentile or normalized score | Score transformed relative to group or scale. | 90th percentile among models. |
| Threshold or decision index | Score used for pass/fail or categorization. | Deployment-gating index. |
| Other | Benchmark-specific metric. | Exact F1, BLEU, ROUGE, risk score. |

### 3.4 Score Transformation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No transformation | Report raw metric directly. | Percent correct. |
| Linear transformation | Apply linear scaling. | Convert 0-1 to 0-100. |
| Non-linear transformation | Apply non-linear formula. | Log-scaled reward. |
| Normalization against baseline | Compare or scale relative to reference. | Score above random baseline. |
| Weighting across subdomains | Domains contribute unequally. | 40 percent coding, 30 percent math, 30 percent safety. |
| Aggregation formula documented | Formula is fully stated. | Mean of domain accuracies with weights listed. |
| Aggregation formula partially documented | Some formula details missing. | HLE pilot notes category weighting details are not fully specified in local source. |
| Aggregation formula not documented | Aggregation is used but formula is absent. | Leaderboard total appears without method. |
| Not applicable | No transformation or aggregation issue applies. | Single unaggregated task score. |

### 3.5 Reference Groups, Baselines, and Comparators

| Option | Meaning | Example |
| :--- | :--- | :--- |
| No baseline or comparator documented | No reference performance is stated. | Standalone score only. |
| Random or chance baseline | Expected performance from random behavior. | Multiple-choice chance floor. |
| Human baseline | Non-expert or general human performance. | Crowdworker accuracy. |
| Expert human baseline | Qualified expert performance. | Domain expert score distribution. |
| Model baseline | One or more model scores used as reference. | GPT-4 baseline. |
| Previous model cohort | Earlier generation of models. | 2023 model cohort. |
| Commercial system comparator | Proprietary production systems. | API-hosted model set. |
| Open-weight model comparator | Released-weight local models. | Llama-family models. |
| Domain-specific reference group | Specialized systems or experts. | Medical board-certified physicians. |
| Other | Other comparator. | Prior benchmark version. |

For each comparator, record construction method, intended interpretation, and source. HLE compares several frontier models and references expert-level academic capability, but the pilot records limited quantified expert score-distribution evidence.

The comparator-construction table also has rows for `Prior benchmark or version` and `Criterion threshold or floor/ceiling`. Use `Prior benchmark or version` when the benchmark is interpreted against an earlier benchmark, previous release, or saturation claim. Use `Criterion threshold or floor/ceiling` when a score is interpreted against a pass level, chance floor, maximum score, saturation point, or other boundary.

### 3.6 Score Uncertainty and Stability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Confidence intervals | Interval estimates around scores. | 95 percent CI for accuracy. |
| Standard errors | Standard error of score estimate. | SE for domain accuracy. |
| Bootstrap intervals | Resampling-based uncertainty estimates. | Bootstrap CI over items. |
| Multiple runs or seeds | Repeated runs under same or varied seeds. | Temperature-sensitive model repeated 5 times. |
| Judge agreement statistics | Agreement among model judges or judge variants. | Cohen's kappa for judges. |
| Human inter-rater agreement | Agreement among human raters. | Krippendorff's alpha. |
| Sensitivity analyses | Checks for prompt, parser, model version, or condition sensitivity. | Prompt variant comparison. |
| Not reported | No uncertainty or stability evidence is reported. | Single score table only. |
| Other | Other stability evidence. | HLE pilot records expert disagreement rates and model non-determinism caveat. |

### 3.7 Metric-to-Claim Linkage

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Why the primary metric was chosen | Rationale for metric fit. | Accuracy fits closed-ended HLE questions. |
| Whether metric floors or ceilings are documented | Chance levels, saturation, max/min behavior. | HLE notes non-zero multiple-choice floor. |
| Whether the metric may reward non-target behavior named by the source | Source-stated shortcuts or confounds. | Formatting, memorization, search, or judge artifacts. |
| Whether parsing, judge, or scorer validation is documented | Evidence scorer measures intended thing. | Judge prompt plus validation study. |
| Whether score uncertainty affects claim interpretation | Whether uncertainty changes conclusions. | Confidence intervals overlap. |
| Whether score differences are interpreted statistically | Whether rankings or differences use significance/uncertainty. | Statistical comparison of two models. |
| Whether benchmark reports state what users should not infer | Explicit non-use or caveat statements. | HLE says high score alone does not imply AGI. |

## Section 4. Benchmark Outputs and Reports

### 4.1 Output Availability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Public leaderboard available | Ranked results are publicly accessible. | Hosted leaderboard. |
| Public aggregate scores available | Overall scores are public. | Paper table with overall accuracy. |
| Public per-domain scores available | Domain or category scores are public. | HLE category results. |
| Public per-item scores available | Item-level correctness is public. | CSV with each question result. |
| Public raw model outputs available | Actual model responses are released. | JSONL completions. |
| Public traces or logs available | Tool, reasoning, execution, or environment logs are public. | Agent trajectory logs. |
| Private reports available only to submitters | Results are returned privately. | Hosted audit report. |
| No formal report or leaderboard documented | Only informal or no reporting is found. | Results mentioned without artifact. |

### 4.2 Output Name or Description

Use one row per output artifact. Include paper tables, dashboards, downloadable files, leaderboards, private submitter reports, and API responses. "Public/private" should state who can see it.

### 4.3 Output Design or Presentation

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Static text report | Narrative report. | PDF or paper section. |
| Tables | Tabular scores. | HLE result tables. |
| Graphs or visualizations | Charts or figures. | Calibration plot. |
| Leaderboard | Ranked list of systems. | Public hosted leaderboard. |
| Interactive dashboard | Filterable or dynamic UI. | Dashboard by model and domain. |
| Downloadable CSV or JSON | Machine-readable result files. | `results.csv`. |
| API output | Results returned by API. | Evaluation endpoint response. |
| Paper-only results | Results exist only in paper. | No downloadable results. |
| Other | Other presentation. | Notebook, slide deck. |

### 4.4 Output Structure

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Aggregate-score based | Organized around total scores. | Overall accuracy ranking. |
| Capability-domain based | Organized by capability areas. | Math, coding, safety. |
| Task-family based | Organized by task type. | Browser, API, file tasks. |
| Criterion-threshold based | Organized by pass/fail or score bands. | Deployment gate. |
| Pairwise-comparison based | Organized by head-to-head outcomes. | Arena win matrix. |
| Rank based | Emphasizes ordering. | Leaderboard rank. |
| Cost or efficiency adjusted | Includes cost, latency, or token efficiency. | Accuracy per dollar. |
| Error-analysis based | Includes error categories. | Failure taxonomy. |
| Trace or process based | Includes trajectories or logs. | Tool trace report. |
| Other | Other structure. | Qualitative audit memo. |

### 4.5 Sensitivity to Context

| Option | Meaning | Example |
| :--- | :--- | :--- |
| One output format for all contexts | Same report for all users or uses. | Single public table. |
| User-definable output contexts | Users can customize report scope or audience. | Dashboard filters for domains. |
| Pre-defined versions adapted to audience or use | Different fixed reports for different audiences. | Technical report plus executive scorecard. |
| Context sensitivity not documented | No source says whether reports differ by use. | Paper-only results. |

### 4.6 Development of Outputs

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Based on benchmark authors' design | Authors chose report fields and formats. | Paper tables designed by benchmark authors. |
| Based on empirical or actuarial relationships | Report content follows statistical or empirical score relationships. | Validated risk bands. |
| Based on expert judgment | Experts shape interpretation or categories. | Expert-defined domain labels. |
| Based on human annotation | Human labels or judgments feed reports. | Human-rated answer categories. |
| Based on model-as-judge outputs | AI judge produces score or labels shown in report. | Model-judge correctness extraction. |
| Automatically generated by benchmark platform | Platform generates report. | Submitter dashboard. |
| Other | Other source of report content. | Community-maintained leaderboard. |

### 4.7 Modifiability

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Not modifiable | Users cannot change report contents. | Fixed paper table. |
| Limited modification by submitter or user | Users can filter, export, or add metadata. | Dashboard filters. |
| Fully user-generated reports possible | Users can create custom reports from released data. | Public raw outputs and item scores. |
| Not documented | Modifiability is not stated. | Unknown platform behavior. |

### 4.8 Transparency

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Clear linkage between tasks, scores, and reported claims | Reports explain how tasks and metrics support claims. | Scorecard links each claim to task family and metric. |
| Partial linkage between tasks, scores, and reported claims | Some links are clear, others unexplained. | Domain scores shown but broad headline unexplained. |
| Linkage is not obvious from available documentation | User cannot tell how score supports claim. | Ranking only. |
| Mixture of clear and concealed linkage | Some details public, some hidden for integrity or platform reasons. | Public aggregate with hidden item-level scoring. |
| Not documented | No evidence about linkage. | No report documentation. |

### 4.9 Output Content

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Capability descriptions | Text explaining what scores indicate. | "Measures closed-ended academic performance." |
| Aggregate rankings | Overall rank or total score. | Leaderboard rank. |
| Subdomain comparisons | Domain or category differences. | HLE category results. |
| Error categories | Types of failures. | Parsing error, hallucination, unsafe compliance. |
| Examples of successes or failures | Sample outputs. | Correct/incorrect responses. |
| Cost, latency, or efficiency data | Runtime, token, cost, compute. | HLE completion token counts. |
| Process traces | Tool calls, logs, reasoning traces. | Agent trajectory. |
| Recommendations or interpretation notes | Guidance on using results. | Suggested non-use cases. |
| Warnings or caveats | Limits and risks. | AGI caveat. |
| Other | Other content. | Confidence histograms. |

### 4.10 Intended Recipients

Use the same logic as Section 2.4, but focus on report recipients rather than intended users of the benchmark generally. A benchmark might be built for researchers but publish a simplified public leaderboard.

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Benchmark maintainers | People who maintain tasks, scoring, reports, or platform outputs. | Maintainers using results to identify benchmark saturation. |
| Model developers | Teams building or improving evaluated systems. | Lab teams checking regressions. |
| AI researchers | Researchers studying model capabilities or benchmark behavior. | Academic comparison study. |
| Safety evaluators | Users focused on safety, refusal, harm, or risk. | Safety audit report. |
| Policy or governance actors | Users making governance, standards, or policy judgments. | Policy memo using benchmark evidence. |
| Product or deployment teams | Teams deciding product behavior, release readiness, or deployment constraints. | Product launch readiness review. |
| Procurement teams | Buyers or enterprise evaluators comparing vendors. | Vendor-selection scorecard. |
| Public audience | General readers of public results or leaderboards. | Public-facing leaderboard users. |
| Other: | Another documented recipient. | Competition judges, educators, domain boards. |

## Section 5. Supply Arrangements and Materials

### 5.1 Supporting Information Provided

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Technical report | Formal methods/results document. | Benchmark paper. |
| User guide | Practical instructions for running or interpreting. | Documentation site. |
| Repository README | Repo-level usage and overview. | GitHub README. |
| API documentation | API endpoint or schema instructions. | Hosted evaluator API docs. |
| Dataset card | Dataset metadata, license, splits, provenance. | Hugging Face card. |
| Model submission instructions | Rules for submitting systems or outputs. | Leaderboard submission guide. |
| Scoring documentation | Scoring method, formula, parser, judge, tests. | HLE scorer prompt and scoring notes. |
| Rubric or annotation guide | Human or judge scoring rubric. | Safety severity rubric. |
| Evaluation examples | Sample tasks, submissions, expected outputs. | Example JSONL submission. |
| FAQ or discussion forum | Support and clarifications. | GitHub Discussions. |
| Changelog or release notes | Version and update history. | HLE-Rolling notes. |
| Other | Other support material. | Video tutorial. |

### 5.2 Methods of Publication

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Academic paper | Published or preprint paper. | arXiv benchmark paper. |
| Benchmark website | Official website. | Benchmark landing page. |
| Git repository | Code-hosting repository. | GitHub repo. |
| Package registry | Installable package. | PyPI package. |
| Dataset hosting platform | Hosted dataset. | Hugging Face dataset. |
| Leaderboard platform | Hosted ranking/submission site. | Eval platform leaderboard. |
| Downloadable documents | PDFs, CSVs, guides, spreadsheets. | PDF technical report. |
| Private distribution | Materials shared only with approved users. | Private holdout or gated audit. |
| Other | Other publication path. | Conference competition portal. |

### 5.3 User Requirements or Qualifications

| Requirement type | Meaning | Example |
| :--- | :--- | :--- |
| Technical expertise | Skills needed to run or interpret. | Python, Docker, API use. |
| Compute or infrastructure | Hardware or hosted services. | GPU, cloud account. |
| Account or access approval | Login, API keys, approval, NDA. | Leaderboard account. |
| Legal or license terms | Usage, redistribution, research-only terms. | Non-commercial dataset license. |
| Cost or fee | Monetary cost. | Paid API or platform fee. |
| Security or privacy requirements | Handling sensitive data or sandboxing. | No exfiltration, private data policy. |
| Other | Any other requirement. | Domain certification for human raters. |

### 5.4 Dataset and Item Access

| Component | Meaning | Example |
| :--- | :--- | :--- |
| Training or example data | Practice or development examples. | Public examples. |
| Development set | Data for tuning prompts or systems. | Dev split. |
| Test set | Data used for evaluation scores. | HLE public test questions. |
| Private holdout set | Hidden test material. | HLE private held-out set. |
| Prompt templates | Exact prompt formatting. | System/user prompt templates. |
| Reference answers | Answer keys or expected outputs. | Correct multiple-choice letters. |
| Rubrics | Criteria for scoring open or ambiguous outputs. | Human judge rubric. |

Mark each component as public, restricted, hidden, or not available. A component may be hidden by design; describe the reason if stated.

### 5.5 Provenance and Contamination Documentation

This section records documentation only.

| Topic | Meaning | Example |
| :--- | :--- | :--- |
| Data source provenance | Where items/data came from. | Expert submissions, public web data, synthetic generator. |
| Collection procedure | How data was gathered. | Contributor process and submission rules. |
| Filtering or quality control | How bad, duplicate, invalid, or unsuitable items were removed. | Expert review, audits. |
| Licensing or rights | Rights to distribute and evaluate. | Contributor license or dataset license. |
| Deduplication | Duplicate-removal methods. | Exact or semantic dedupe. |
| Contamination controls | Steps to reduce training-data exposure. | Private split, delayed release. |
| Searchability or source-exposure checks | Whether items can be found online or in source data. | HLE searchability checks. |
| Canary, GUID, encryption, or anti-scraping method | Technical markers or protections for leakage detection. | Canary strings in hidden set. |
| Training-on-test diagnostic task | Tests designed to detect memorization of benchmark items. | Diagnostic prompts. |
| Public/private split rationale | Why some data is public and some hidden. | HLE private set for overfitting/gaming checks. |
| Update or refresh policy | How items are added, retired, or refreshed. | Rolling benchmark. |
| Release rules or anti-gaming terms | Rules limiting leakage, tuning, scraping, or submissions. | No training on test set. |

### 5.6 Reproducibility Materials

| Option | Meaning | Example |
| :--- | :--- | :--- |
| Complete evaluation code | End-to-end runnable evaluator. | Repo script for full benchmark. |
| Scoring scripts | Code for scoring outputs. | Judge parser or unit-test scorer. |
| Environment file or dependency list | Requirements needed to recreate runtime. | `requirements.txt`, `environment.yml`. |
| Container or reproducible runtime | Docker image or equivalent. | Dockerfile. |
| Prompt templates | Exact prompts used. | HLE evaluation prompt. |
| Example submissions | Sample outputs in expected format. | JSONL example. |
| Raw outputs from reported models | Model responses used for reported results. | Released completions. |
| Random seeds | Seeds for sampling or task generation. | Seed list. |
| Configuration files | Model, scorer, prompt, or environment configs. | YAML run configs. |
| Expected outputs or tests | Tests that verify setup and scoring. | Golden outputs. |
| Result replication script | Script that regenerates paper/leaderboard results. | `reproduce_results.py`. |
| Build status or continuous integration check | CI showing code works. | Passing GitHub Actions badge. |
| None documented | No reproducibility materials are documented. | Paper-only benchmark. |

### 5.7 Maintenance and Versioning

| Prompt | Meaning | Example |
| :--- | :--- | :--- |
| Current maintenance status | Active, inactive, archived, planned, unclear. | Active rolling updates. |
| Latest documented release | Most recent version/date. | GitHub release tag. |
| Changelog available | Whether changes are documented. | Release notes. |
| Versioning scheme | How versions are named. | Semantic versioning, dated releases. |
| Deprecated versions | Retired or superseded versions. | Old public set. |
| Issue tracker or feedback channel | Where users report problems. | GitHub Issues. |
| Response policy for user feedback | How maintainers respond. | Triage SLA or no policy. |
| Known planned updates | Roadmap or announced refresh. | HLE-Rolling. |
| Retirement or archival plan | How benchmark will be retired. | Archive after saturation. |
| Archival status | Whether data/code are preserved. | DOI, Zenodo, archived repo. |

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
| Construct validity | Construct definition and claim scope. | HLE: closed-ended academic capability, not AGI proof. |
| Task or item quality | Development process, expert review, item audits. | Expert submissions and audits. |
| Scoring validity | Metric, parser, judge, rubric, scorer validation. | Model-judge prompt and validation evidence if available. |
| Reliability or run stability | Repeats, seeds, uncertainty, rater agreement. | Expert disagreement rates, confidence intervals. |
| Baselines and comparators | Human, expert, chance, model, prior versions. | Frontier model cohort. |
| Fairness or comparability | Conditions across systems, domains, languages, modalities. | Text-only versus full-set distinction. |
| Reproducibility | Data, code, prompts, configs, raw outputs. | Evaluation code and raw outputs. |
| Contamination and gameability | Public/private split, search checks, anti-gaming rules. | Private holdout. |
| Maintenance and benchmark drift | Versioning, changelog, refresh, retirement. | Rolling updates. |
| Interpretation limits | Stated caveats and non-use cases. | Do not infer AGI from HLE alone. |
| Leaderboard or public-claim risk | Reports, ranks, public messaging. | Leaderboard caveats and version labels. |
| Other | Benchmark-specific issue. | Safety-sensitive content handling. |

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
| Rationale and construct definition | Whether the target phenomenon is defined and bounded. | Vague "reasoning" or "intelligence" claim with no definition. | Clear construct, subcomponents, exclusions, and intended uses. |
| Phenomenon-task-metric-claim chain | Whether the source links phenomenon, task, metric, and claim. | Accuracy on narrow tasks used to claim broad agency without argument. | Explicit chain with confounds and safeguards. |
| Task/item development quality | How tasks were designed, reviewed, sampled, and revised. | No item source or review process. | Expert review, structured criteria, audits, revision history. |
| Documentation and procedural instructions | Whether users can administer, score, and interpret correctly. | Incomplete setup and scoring instructions. | Current, source-linked, complete user documentation. |

### 6.2 Section 6 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 6.1 Rationale and construct definition | Adequacy of the purpose and construct definition. | HLE defines closed-ended academic challenge better than broad AGI. |
| 6.2 Phenomenon-task-metric-claim chain | Fit among claim, tasks, metric, and interpretation. | Accuracy fits closed-ended items, but broader claims need caution. |
| 6.3 Development process and task/item quality | Evidence about item creation, expertise, review, and quality control. | Expert submissions and audits. |
| 6.4 Documentation available to users | Availability and completeness of user-facing documentation. | Paper plus missing repository or license details. |
| 6.5 Procedural instructions for administration, scoring, and interpretation | Whether run, scoring, and interpretation instructions are sufficient. | Prompt documented, exact harness missing. |
| 6.6 Overall adequacy of rationale, documentation, and task/item quality | Reviewer synthesis of Section 6. | Do not mechanically average rows. |

## Section 7. Quality of Benchmark Materials and Usability

Section 7 rates whether the actual materials can be obtained, understood, and used correctly.

### 7.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Materials availability | Whether datasets, prompts, rubrics, and task materials exist and are accessible. | Key materials missing. | Complete, versioned, licensed materials. |
| Evaluation harness and scoring tools | Whether users can run and reproduce scoring. | Opaque hosted-only or absent scorer. | Runnable, tested harness with examples. |
| Prompts, rubrics, and response formats | Whether instructions and formats are clear and validated. | Ambiguous prompts or fragile parser. | Documented prompts, rubrics, parser tests. |
| Accessibility and usability | Whether intended users and systems can use materials. | Requirements exclude relevant systems without warning. | Quick starts, support, modality/language access notes. |

### 7.2 Section 7 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 7.1 Dataset, task set, or environment availability | Availability of tasks, data, or environments. | Public tasks available, private holdout hidden. |
| 7.2 Prompts, instructions, rubrics, and response format | Clarity and access to prompts/rubrics/formats. | HLE prompt and judge instructions. |
| 7.3 Evaluation harness, scorer, and implementation usability | Ability to run scorer correctly. | Complete CLI versus paper-only scoring description. |
| 7.4 Accessibility across relevant modalities, languages, and system types | Whether relevant systems can participate fairly. | Text-only subset for models lacking image input. |
| 7.5 Licensing, usage requirements, and sensitive-content warnings | Legal and safety instructions for use. | License documented or missing. |
| 7.6 Overall quality of benchmark materials | Reviewer synthesis of material quality. | Consider access restrictions and intended use. |

## Section 8. Baselines, Comparators, and Reference Interpretation

Section 8 adapts EFPA norms into AI benchmark baselines, floors, ceilings, human/expert comparisons, model cohorts, and thresholds.

### 8.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Baseline construction | Whether reference levels are meaningful and documented. | No baseline where one is needed. | Representative, uncertainty-aware baselines. |
| Human/expert comparators | Whether human claims have methods. | "Expert-level" with no expert procedure. | Documented qualifications, sampling, conditions. |
| Model comparators | Whether model comparisons are current and specified. | Cherry-picked or version-ambiguous cohort. | Versions, settings, and conditions clear. |
| Floors, ceilings, thresholds | Whether chance, saturation, and decision levels are handled. | Chance floor ignored. | Floors, ceilings, thresholds empirically integrated. |

### 8.2 Section 8 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 8.1 Random, chance, floor, and ceiling baselines | Chance levels, lower bounds, saturation, score ceilings. | HLE notes non-zero multiple-choice floor. |
| 8.2 Human or expert baselines | Human performance and expert comparison methods. | Expert contributors are not the same as a quantified expert baseline. |
| 8.3 Model comparator cohort | Model selection, versions, and evaluation conditions. | Frontier model table with model versions. |
| 8.4 Criterion thresholds or score bands | Pass/fail or interpretive cutoffs. | Deployment threshold, if validated. |
| 8.5 Overall adequacy of baselines and reference interpretation | Synthesis of reference interpretation quality. | Explain usable reference points and missing anchors. |

## Section 9. Reliability, Precision, and Score Stability

Section 9 rates whether scores are stable and precise enough for the intended use.

### 9.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Run stability and uncertainty | Repeated runs, seeds, uncertainty intervals, stochasticity. | Single scores despite known variability. | Comprehensive repeat-run and uncertainty evidence. |
| Scorer, judge, or rater reliability | Reliability of scorers, parsers, raters, judges. | Model judge with no validation. | Agreement and validation across edge cases. |
| Form, version, and prompt stability | Comparability across prompts, versions, forms, environments. | Mixed versions without equivalence evidence. | Drift and equivalence tested. |
| Statistical comparison quality | Whether score differences are statistically interpretable. | Ranks without uncertainty. | Comparisons use uncertainty/significance methods. |

### 9.2 Section 9 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 9.1 Run-to-run stability, seeds, and sampling settings | Stability across runs and decoding. | Multiple seeds or non-determinism caveat. |
| 9.2 Score uncertainty, confidence intervals, or standard errors | Quantified uncertainty. | Confidence intervals over items. |
| 9.3 Human rater, scorer, parser, or model-judge agreement | Agreement evidence for judgmental or parsing steps. | Human inter-rater agreement, judge validation. |
| 9.4 Prompt, form, version, and environment stability | Sensitivity to prompt, benchmark version, form, environment. | Public/private equivalence evidence. |
| 9.5 Overall reliability and precision | Synthesis of score stability. | State whether comparisons are stable enough for intended use. |

## Section 10. Validity Evidence

Section 10 is the core MESA validity section: does evidence support the intended interpretation of scores?

### 10.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Content and representativeness | Whether tasks represent intended capability space. | Narrow sample used for broad claim. | Systematic coverage with stated limits. |
| Metric and scoring validity | Whether the metric rewards intended capability. | Metric rewards formatting, memorization, or judge artifacts. | Metric, parser, scorer, aggregation validated. |
| Relations with other evidence | Convergent, discriminant, criterion, ecological evidence. | Comparisons absent or misleading. | Relevant comparisons interpreted cautiously. |
| Contamination and gameability | Leakage, public exposure, tuning, gaming controls. | Risks ignored despite public tasks. | Private splits, canaries, audits, release rules. |
| Claim proportionality, including AGI/agency | Whether claims match measurement breadth and depth. | AGI claim from narrow task score. | Broad claims supported across relevant sub-abilities or explicitly rejected. |

### 10.2 Section 10 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 10.1 Content validity and task representativeness | Coverage and sampling of intended domain. | HLE broad academic domains, but not all cognitive abilities. |
| 10.2 Internal structure, subscores, or dimensionality | Whether subscores/dimensions behave as claimed. | Category scores require support if interpreted as dimensions. |
| 10.3 Metric, scorer, and aggregation validity | Fit and validation of scoring. | Accuracy for closed-ended questions; judge validation gap. |
| 10.4 Relations with other benchmarks, humans, criteria, or realistic settings | External comparisons and ecological relevance. | Comparison to prior saturated benchmarks. |
| 10.5 Contamination, leakage, and gameability controls | Controls against exposure and gaming. | Searchability checks and private holdout. |
| 10.6 Claim proportionality and broad-capability cautions | Whether public claims stay within evidence. | HLE caveat against AGI inference. |
| 10.7 Overall validity evidence | Synthesis of validity for intended use. | Usually the most important Part B judgment. |

## Section 11. Fair Use, Comparability, and Appropriate Use

Section 11 rates whether benchmark use is fair and comparable across relevant systems, modalities, languages, domains, access modes, and user contexts.

### 11.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Cross-system comparability | Whether conditions are comparable across systems. | Different tools/prompts/settings without caveat. | Conditions controlled and differences handled. |
| Domain, language, modality, and subgroup coverage | Whether coverage supports intended comparisons. | English-only benchmark used for multilingual claim. | Coverage analyzed and limits tied to interpretation. |
| Access, compute, and usability fairness | Whether access or compute requirements distort comparison. | Proprietary platform excludes relevant systems without warning. | Inclusive, documented access paths. |
| Appropriate-use guidance | Whether guidance prevents overinterpretation. | Marketing encourages unsupported claims. | Prominent non-use and limitation guidance. |

### 11.2 Section 11 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 11.1 Cross-system and evaluation-condition comparability | Prompt, model access, settings, tools, and scoring fairness. | Same prompt/settings across compared models. |
| 11.2 Domain, language, modality, and subgroup fairness | Coverage across relevant domains/languages/modalities/groups. | HLE text-only versus full-set reporting. |
| 11.3 Access, compute, tooling, and API/local comparability | Whether resource requirements affect comparability. | API-only benchmark versus open-weight local models. |
| 11.4 Release rules, sensitive-content warnings, and appropriate-use guidance | Rules and warnings for responsible use. | Anti-gaming terms, sensitive-content notices. |
| 11.5 Overall fair use and comparability | Synthesis of fair-use evidence. | State which comparisons are safe or limited. |

## Section 12. Quality of Reports, Leaderboards, Dashboards, and Public Claims

Section 12 rates whether benchmark outputs communicate results accurately, clearly, and proportionally.

### 12.1 Rating Anchors

| Criterion | What to evaluate | Low rating pattern | High rating pattern |
| :--- | :--- | :--- | :--- |
| Report scope and granularity | Whether reports show enough detail for claims. | Aggregate only despite domain claims. | Aggregate, subscores, uncertainty, caveats. |
| Leaderboard or dashboard quality | Versioning, ranking clarity, update policy, reproducibility. | Opaque rankings. | Versioned, documented, uncertainty-aware display. |
| Report reliability and validity | Whether reports accurately reflect scores and limits. | Public claims diverge from score support. | Score-to-claim links and limits explained. |
| Public communication and acceptability | Whether public messaging is cautious and audience-appropriate. | Headline overclaims. | Transparent, accessible, evidence-aligned communication. |

### 12.2 Section 12 Ratings

| Criterion | Meaning | Example rating evidence |
| :--- | :--- | :--- |
| 12.1 Report, leaderboard, dashboard, or result artifact scope | Whether outputs cover relevant results. | Paper tables, leaderboard, dashboard. |
| 12.2 Score granularity, uncertainty, and version labeling | Detail, uncertainty, version clarity. | Category scores plus missing CIs. |
| 12.3 Linkage from scores to public claims | Whether claims follow from scores. | AGI caveat included or absent. |
| 12.4 Raw outputs, per-item data, or trace availability | Inspectability of underlying outputs. | Released model completions or logs. |
| 12.5 Overall quality of reports and public claims | Synthesis of reporting quality. | State public interpretation risks. |

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
