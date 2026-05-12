
# Part A. Description of the Benchmark

## Information sources

In this part, unless otherwise indicated, record the benchmark as described by its creators, maintainers, documentation, technical reports, leaderboard materials, and associated evaluation code. Where benchmark claims are unclear, indicate this explicitly and infer cautiously from the available materials. Where benchmark claims seem overstated or inappropriate, these concerns should be addressed later in the evaluation sections. This follows the same descriptive-first logic as the EFPA model.

---

## Section 1. Factual description

### General information

| Prompt                                                       | Response  |
| ------------------------------------------------------------ | --------- |
| Reviewer                                                     | Free Text |
| Date of current review                                       | Free Text |
| Date of previous review (if applicable)                      | Free Text |
| Benchmark name                                               | Free Text |
| Short name / acronym                                         | Free Text |
| Original benchmark name (if adapted, forked, or re-released) | Free Text |
| Benchmark authors / creators                                 | Free Text |
| Organisation(s) maintaining benchmark                        | Free Text |
| Distributor / hosting platform                               | Free Text |
| Date of current benchmark version                            | Free Text |
| Date of original release                                     | Free Text |
| Current version identifier                                   | Free Text |
| License / terms of use                                       | Free Text |
| Primary documentation source                                 | Free Text |
| Evaluation code repository                                   | Free Text |
| Database repository                                          | Free Text |
| Leaderboard or reporting site                                | Free Text |

---

## Section 2. Classification

### 2.1 Claimed capability domains

- Specify what the benchmark claims to measure using up to 3 keywords.
- [ ] Not explicitly stated
- General reasoning
- Knowledge / recall
- Mathematical reasoning
- Scientific reasoning
- Coding / program synthesis
- Language understanding
- Planning
- Tool use
- Agentic task performance
- Multimodal understanding
- Long-context processing
- Social / interactive reasoning
- Safety / policy compliance
- General intelligenc
- Speed
-  Other (describe): Free Text
    

---

### 2.2 Area of use

- Select all that apply:    
-  Not explicitly stated
-  Frontier model evaluation
-  General model comparison
-  Capability tracking over time
-  Safety evaluation
-  External reporting / publicity
-  Research benchmarking
    
-  Procurement or model selection
    
-  Deployment readiness assessment
    
-  Academic study of intelligence
    
-  Policy or governance use
    
-  Other (describe): Free Text
    

---

### 2.3 Systems for which the benchmark is intended

- Describe the model classes or systems the benchmark is intended to evaluate. Only the stated target systems should be described here.
    
- Free Text
    

Examples:

- frontier LLMs
    
- open-weight models
    
- multimodal foundation models
    
- tool-using agents
    
- code models
    
- general-purpose chat assistants
    

---

### 2.4 Main intended users

- Select all that apply:
    
-  Not explicitly stated
    
-  AI researchers
    
-  Benchmark developers
    
-  Model developers
    
-  Safety researchers
    
-  Policy analysts
    
-  Procurement / evaluation teams
    
-  Journalists / public communicators
    
-  General public
    
-  Other (describe): Free Text
    

---

### 2.5 Number of task families / subscales and brief description of variables measured

- Indicate the number of sub-benchmarks, task families, categories, or reported subscores. Briefly describe each if the meaning is not clear from its name.
    
- Free Text
    

---

### 2.6 Response mode required from the AI system

- Describe the response format expected from the evaluated system.
    
- Select all that apply:
    
-  Not explicitly stated
    
-  Multiple-choice selection
    
-  Short free-text response
    
-  Long-form generation
    
-  Code generation
    
-  Structured output / JSON
    
-  Tool call / API action
    
-  Interactive multi-turn behaviour
    
-  Ranking
    
-  Classification label
    
-  Image generation or interpretation
    
-  Audio / speech output
    
-  Other (describe): Free Text
    

---

### 2.7 Demands on the evaluated system

- Which capabilities or conditions are necessary for the system to complete the benchmark as intended and allow fair interpretation of benchmark scores?
    

| Capability / condition                        | Irrelevant / not necessary | Necessary and documented | Necessary but insufficiently documented |
| --------------------------------------------- | -------------------------- | ------------------------ | --------------------------------------- |
| Instruction following                         | - [ ]                      | - [ ]                    | - [ ]                                   |
| Fluency in benchmark language                 | - [ ]                      | - [ ]                    | - [ ]                                   |
| Domain knowledge                              | - [ ]                      | - [ ]                    | - [ ]                                   |
| Chain-of-thought or latent reasoning capacity | - [ ]                      | - [ ]                    | - [ ]                                   |
| Tool use                                      | - [ ]                      | - [ ]                    | - [ ]                                   |
| Code execution                                | - [ ]                      | - [ ]                    | - [ ]                                   |
| Web access                                    | - [ ]                      | - [ ]                    | - [ ]                                   |
| Vision capability                             | - [ ]                      | - [ ]                    | - [ ]                                   |
| Audio capability                              | - [ ]                      | - [ ]                    | - [ ]                                   |
| Long-context capacity                         | - [ ]                      | - [ ]                    | - [ ]                                   |
| Agentic planning                              | - [ ]                      | - [ ]                    | - [ ]                                   |
| API orchestration                             | - [ ]                      | - [ ]                    | - [ ]                                   |

- Other (describe): Free Text
    

---

### 2.8 Special evaluation conditions

- Describe any specific evaluation conditions required, such as closed-book vs open-book, time limits, tool restrictions, context limits, hidden system prompts, sandboxing, safety filters, or human supervision.
    
- Free Text
    

---

### 2.9 Item / task response types

- Selection-based responses
    
    -  Multiple choice (single answer)
        
    -  Multiple choice (multiple answer)
        
    -  Ranking
        
    -  Binary decision
        
- Production-based responses
    
    -  Open text
        
    -  Code
        
    -  Mathematical derivation
        
    -  Structured output
        
- Interaction-based responses
    
    -  Multi-turn dialogue
        
    -  Interactive computer environment
        
    -  Tool-mediated task completion
        
    -  Simulated real-world task
        
- Process data collection
    
    -  Latency
        
    -  Number of turns
        
    -  Token usage
        
    -  Tool-use trace
        
    -  Action sequence
        
    -  Other (describe): Free Text
        

---

### 2.10 Input / stimulus type

- Select all that apply:
    
-  Not explicitly stated
    
-  Text
    
-  Images
    
-  Tables
    
-  Audio
    
-  Video
    
-  Code
    
-  Web environment
    
-  Interactive software environment
    
-  Dynamic / sequential stimuli
    
-  Other (describe): Free Text
    

---

### 2.11 Total number of items / tasks

- Where the benchmark is not static, indicate minimum, maximum, and typical number of items, episodes, or evaluation instances.
    
- Free Text
    

---

### 2.12 Intended mode of administration

#### 2.12.1 Intended evaluation unit

- Suitable for:
    
-  Single model snapshot
    
-  Multiple model comparison
    
-  Repeated longitudinal tracking
    
-  Agent system evaluation
    
-  Not indicated
    

---

#### 2.12.2 Intended mode of use

- Select all that apply:
    
-  Fully automated evaluation
    
-  Controlled but unsupervised evaluation
    
-  Supervised evaluation by expert operators
    
-  Human-in-the-loop scoring
    
-  Third-party platform evaluation only
    
-  Not clearly stated
    

---

### 2.13 Technological arrangements available / required

- Mark A (available) / R (required) against each option:
    
-  API access
    
-  Local inference
    
-  GPU / accelerator hardware
    
-  External tools
    
-  Internet access
    
-  Sandbox / container
    
-  Human judges
    
-  Model-specific wrappers
    
-  Proprietary platform
    
-  Other (describe): Free Text
    

---

### 2.14 Evaluator time required

- In many cases, only approximate estimates are possible.
    
- Preparation  
    Time required to prepare benchmark instances, environment, credentials, prompts, or scoring scripts.
    
    - Free Text
        
- Administration  
    Time required to execute one full benchmark run.
    
    - Free Text
        
- Scoring  
    Time required to compute raw metrics or collect judged outputs.
    
    - Free Text
        
- Analysis  
    Time required to aggregate scores, compute uncertainty, compare models, and interpret findings.
    
    - Free Text
        
- Reporting  
    Time required to prepare benchmark reports, leaderboard entries, or stakeholder summaries.
    
    - Free Text
        

---

### 2.15 Different forms / variants

- Are there alternative benchmark versions, hidden sets, lite versions, multilingual variants, domain-specific forms, or interactive vs static versions?
    
- Describe whether these are equivalent alternate forms or meaningfully different instruments.
    
- Free Text
    

---

### 2.16 Static or dynamic task determination

- How is the content presented to the system determined?
    
- Static benchmark
    
    -  Fixed task set
        
    -  Fixed prompt set
        
    -  Fixed scoring key
        
- Dynamic benchmark
    
    -  Randomized task sampling
        
    -  Parameterized instance generation
        
    -  Adaptive item selection
        
    -  Interactive environment changes in response to system behaviour
        
    -  Judge-dependent follow-up prompts
        
    -  Other (describe): Free Text
        

---

### 2.17 Source of benchmark information

- What is the source of the information used to generate benchmark scores?
    
- Select all that apply:
    
-  Benchmark-authored questions/tasks
    
-  Curated human-generated items
    
-  Web-sourced materials
    
-  Expert-authored tasks
    
-  Synthetic / model-generated items
    
-  Simulated environments
    
-  Human judges
    
-  Automatic evaluators
    
-  External APIs or tools
    
-  Other (describe): Free Text
    

---

## Section 3. Measurement and scoring

### 3.1 Scoring procedure

- Select all that apply:
    
-  Not explicitly stated
    
-  Exact-match automatic scoring
    
-  Rule-based scoring
    
-  Model-as-judge scoring
    
-  Human scoring
    
-  Hybrid human + automatic scoring
    
-  Execution-based scoring
    
-  Environment success / task completion scoring
    
-  Pairwise preference scoring
    
-  Other (describe): Free Text
    

---

### 3.2 Scores

- Brief description of the scoring system used to obtain total and partial scores, including aggregation rules, penalties, weighting, judge procedures, and uncertainty estimates.
    
- Free Text
    

---

### 3.3 Scales used

- Raw benchmark outputs
    
    -  Accuracy
        
    -  Pass rate
        
    -  Exact match
        
    -  F1
        
    -  Precision / recall
        
    -  AUC / ROC
        
    -  Calibration score
        
    -  Win rate
        
    -  Human preference score
        
    -  Cost efficiency
        
    -  Latency
        
    -  Robustness measure
        
    -  Other (describe)
        
- Standardized or transformed scores
    
    -  Normalized composite score
        
    -  Percentile rank against reference systems
        
    -  Human-relative score
        
    -  Expert-relative score
        
    -  Baseline-relative improvement
        
    -  Other (describe)
        

---

### 3.4 Score transformation

-  Scores reported directly from raw metric values
    
-  Scores transformed linearly
    
-  Scores transformed non-linearly
    
-  Composite index created from multiple metrics
    
-  Thresholded categories derived from continuous scores
    
-  Not applicable
    

---

### 3.5 Reference interpretation procedures

-  Human baselines provided
    
-  Expert baselines provided
    
-  Prior-model baselines provided
    
-  Random / heuristic baselines provided
    
-  Threshold-based interpretations provided
    
-  No explicit reference framework provided
    

---

## Section 4. Automatically generated reports and benchmark outputs

### 4.1 Are automatically generated reports available?

-  Yes
    
-  No
    

---

### 4.2 Name or description of report

- Free Text
    

---

### 4.3 Design or presentation

- Select all that apply:
    

Static report

-  Text only
    
-  Tables only
    
-  Graphics only
    
-  Integrated text and graphics
    

Interactive report

-  Dashboard
    
-  Filterable leaderboard
    
-  Drill-down by task/category
    
-  Trace viewer / response browser
    

Other

-  Video / demo output
    
-  Other (describe)
    

---

### 4.4 Structure

-  Metric-based
    
-  Capability-based
    
-  Task-family-based
    
-  Model-comparison-based
    
-  Error-analysis-based
    
-  Risk-based
    
-  Other (describe): Free Text
    

---

### 4.5 Sensitivity to context

-  One version for all audiences
    
-  User-definable views
    
-  Different reports for different audiences (researchers, policymakers, public, developers)
    

---

### 4.6 Development of the report

-  Generated directly from benchmark metrics
    
-  Includes expert commentary
    
-  Includes model-generated narrative summaries
    
-  Includes statistical uncertainty summaries
    
-  Other (describe)
    

---

### 4.7 Modifiability

-  Not modifiable
    
-  Limited modification
    
-  Fully configurable
    

---

### 4.8 Transparency

-  Clear linkage between responses, metrics, and report outputs
    
-  Linkage not obvious (black box)
    
-  Mixture of clear and concealed linkage
    

---

### 4.9 Type of content

-  Score summaries
    
-  Capability profiles
    
-  Error analyses
    
-  Benchmark ranking / leaderboard position
    
-  Interpretation notes
    
-  Cautions or limitations
    
-  Recommended uses
    
-  Others (describe)
    

---

### 4.10 Intended recipients

-  Benchmark experts
    
-  Model developers
    
-  Policymakers / governance actors
    
-  Journalists / communicators
    
-  Procurement / deployment teams
    
-  General public
    
-  Other (describe)
    

---

## Section 5. Supply arrangements and materials

### 5.1 Supporting information provided to users

- Select all that apply:
    
-  Technical report
    
-  User guide
    
-  Evaluation code
    
-  Dataset documentation
    
-  Scoring documentation
    
-  Example outputs
    
-  Baseline results
    
-  Change log / version history
    
-  Discussion forum / issue tracker
    
-  Other (describe)
    

---

### 5.2 Methods of publication

- Select all that apply:
    
-  Website
    
-  Git repository
    
-  Downloadable dataset
    
-  API
    
-  Paper / preprint
    
-  Leaderboard platform
    
-  Other (describe)
    

---

### 5.3 Qualifications or requirements for benchmark use

- Describe any expertise, access, or infrastructure requirements the creators specify for proper use.
    
- Examples:
    
    - advanced ML engineering competence
        
    - access to proprietary models
        
    - secure evaluation environment
        
    - human annotation expertise
        
    - statistics / psychometrics competence
        
    - policy evaluation expertise
        
- Where requirements are unclear, state this explicitly.
    
- Free Text
    

---

## Appendix A: General description of the benchmark

Provide a concise non-evaluative description of the benchmark. This should give a clear account of what the benchmark claims to be, what capability areas it covers, how it is administered, how it is scored, who it is intended to evaluate, and who it is intended to inform. It should also note major versions, variants, and any unusual features. This description should stand alone and may repeat some details from Part A.

Recommended length:

- simple benchmark: 200–300 words
    
- complex benchmark suite: 300–600 words
    

---

## Notes on what changed from EFPA to MESA Part A

The main adaptations are:

- **test → benchmark**
    
- **test taker → AI system / model / agent**
    
- **administrator → evaluator / benchmark operator**
    
- **items → tasks / prompts / episodes**
    
- **norms → reference interpretations / baselines**
    
- **digitally generated reports → automated benchmark reports / dashboards**
    
- **human capability demands → system capability requirements**
    

The biggest conceptual shift is that Part A no longer describes a human assessment instrument for people; it describes an evaluation instrument for AI systems while preserving EFPA’s emphasis on intended use, administration conditions, score production, and interpretive context.

Next, I can turn this into a cleaner **publication-ready markdown template** with consistent checkbox syntax and reviewer fill-in fields only.