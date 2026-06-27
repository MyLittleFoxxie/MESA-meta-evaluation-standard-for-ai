# Part 1: Original Review Comments

Below is the complete text of the feedback received for the paper.tex of MESA from the RETRAI 2026 workshop peer reviewers:

```text
----------------------- REVIEW 1 ---------------------
SCORE: 2 (accept)
----- TEXT:
# Summary:
The paper proposes MESA, a meta-evaluation approach for benchmarks. The paper argues that reviewing and evaluating benchmarks should simulate evaluating human cognitive abilities. It therefore adapts European Federation of Psychologists’ Associations test review model to offer two parts: (i) descriptive characterizing what the benchmark is, what it claims, how it operates, etc. and (ii) evaluative, assessing whether the available scores and documentation adequately justify the benchmark’s intended interpretations.

# Strengths
+ interesting topic that is probably new to the RE community
+ a replication package is shared with MIT license

# Weaknesses
- It appears that none of the benchmarks used for constructing MESA are directly from the RE and only few are from the SE, also the benchmarks used in the evaluation, making the connection to RE somewhat weak
- Missing threats to validity
- The first part of MESA assumes that benchmarks have available descriptions which I believe is not always the case
- insufficient engagement with the existing literature in AI, e.g., check "Evaluating the Evaluations: A Perspective on Benchmarks. Omar Alonso and Kenneth Church. SIGIR 25", "Reuel, A., et al. Betterbench: Assessing ai benchmarks, uncovering issues, and establishing best practices. Neurips 2024"

# Comments:
* The introduction will benefit from additional citations

# minor:
* The paper is verbose in some parts
* Missing space in abstract (before “rather than”)
* It adapts (1) -> it (1) adapts

----------------------- REVIEW 2 ---------------------
SCORE: 3 (strong accept)
----- TEXT:
The paper presents a framework for evaluating AI benchmarks before using them as evidence for claims, thereby enabling empirically validated benchmark-based claims. The review model is structured into two parts: (A) describing the benchmark and its materials and (B) evaluating what interpretations are supported by the benchmark’s score.

This work addresses the highly relevant problem of AI benchmark scores being used as evidence for capability (e.g., AGI) and trustworthiness claims without a thorough prior review of the benchmark itself to know whether it is even capable/designed to carry the stated claims.

The paper is very well structured, and all expected sections are present. The authors are very transparent about the methodology, and the limitations of the study are discussed in a good way. Figures and tables are used effectively to support the arguments.

Opportunities for improvement:
-       It seems odd to me that the entire framework is explained in the methodology section. I think a separate section with a meaningful title would add to the structure and help the reader. As of now, the methodology section is disproportionately long.
-       Even though the planned ideal evaluation is described in the future work section, it would make sense in a methodology section to also briefly describe the intended (future) evaluation.

----------------------- REVIEW 3 ---------------------
SCORE: 2 (accept)
----- TEXT:
## Summary
This paper introduces MESA, a framework for auditing AI benchmarks as measurement instruments. The key idea is that benchmark scores should not be treated as direct evidence of model capability unless the benchmark is reviewed for validity, reliability, comparability, documentation, and claim proportionality. The paper applies MESA to Humanity’s Last Exam and ARC-AGI-2, arguing that both support narrower claims than their public framing often suggests.

## Strengths
The paper’s strongest contribution is its framing of benchmarks as measurement tools. This is obvious in principle but often ignored in practice.
The paper is also timely. As major AI labs increasingly compete for attention, funding, and credibility through benchmark results, the field needs stronger controls around what goes into benchmarks, how scores are produced, and what claims those scores can support.
I especially like the supported-use / non-use distinction. It gives benchmark users a concrete way to say what a score can legitimately justify and where interpretation should stop.

## Challenges
My main concern is the audit process itself. A third-party benchmark audit cannot really be outsourced to LLMs if it is meant to be trusted. This is a difficult and central part of the proposal, and a useful audit likely requires domain experts, benchmark designers, model evaluators, and assurance specialists. LLMs may help structure the review, but they should not replace expert judgment.

A second concern is that the paper puts most of the burden of the claimed capability on the benchmark. In practice, the meaning of a score also depends on the model. For example, if a model trained only on text generalizes to ARC-style abstract grid tasks, that may support a broader claim about generalization than the benchmark alone would imply.

This may be more about communicating results than measuring them. The benchmark may directly measure only a narrow task family, but broader claims can sometimes be supported by combining benchmark evidence with evidence about the model’s training, prior capabilities, and intended use. The framework would be stronger if it made this distinction more explicit.
```

---

# Part 2: Actionable LaTeX Work Plan

This plan organizes the necessary revisions into structurally bounded tasks, indicating the precise location of text edits, table insertions, and conceptual adjustments.

## Task 1: Structural Reorganization (Reviewer 2)

_Extract MESA Framework description from Section III (Methodology) into its own dedicated section to balance section lengths._

1. **Extract Section III-D (MESA Review Model)**:
   - Move the text describing Part A, Part B, Table II, and the template coherence from `Section III` to a new section: `\section{The MESA Review Model}` (placed as Section IV).
   - Renumber subsequent sections accordingly (Test Application Findings becomes Section V, Discussion becomes Section VI).
2. **Incorporate the Intended Empirical Validation**:
   - Add a subsection in the Methodology section (`\subsection{Intended Empirical Validation Strategy}`) describing the planned human-expert user study.

```latex
% Place in Section III (Methodology) before Section IV
\subsection{Intended Empirical Validation Strategy}
While this study establishes technical feasibility using a structured multi-LLM pipeline (Section V), the proposed long-term validation strategy for MESA centers on human-in-the-loop consensus panels. Future empirical work will deploy MESA in a controlled user study where independent requirements engineers, model evaluators, or domain experts audit the same benchmark cohorts..
```

---

## Task 2: Strengthen RE/SE Context (Reviewer 1)

_Address the criticism that none of the evaluated benchmarks are native to RE/SE, weakening the domain connection._

1. **Leverage SE Benchmarks in Table I**:
   - Point out that Table I contains major software-engineering and programming agent benchmarks (SWE-Bench Verified, Terminal-Bench 2.0, LiveCodeBench Pro).
2. **Bridge to SE/RE Workloads**:
   - Add a paragraph in the Introduction or Discussion explaining how software engineering benchmarks fit MESA, demonstrating that checking the "V&V" tools of RE (which software agents are scored on) is an RE prerequisite.

```latex
% Insert into the Introduction (Section I)
In Requirements Engineering (RE) for AI agents, software engineering benchmarks—such as SWE-Bench Verified or Terminal-Bench 2.0 (Table I)—serve as the foundational verification and validation (V&V) mechanisms to certify system requirements. For instance, if an agent is specified to independently resolve repository-level issues, engineers rely on SWE-Bench scores as verification evidence. MESA's role is to ensure these underlying test suites are robust, reproducible, and free from execution bias, making benchmark auditing a key phase of the RE pipeline.
```

---

## Task 3: Integrate SOTA Benchmarking Literature (Reviewer 1)

_Thoroughly integrate BetterBench (Reuel et al., 2024) and "Evaluating the Evaluations" (Alonso & Church, 2024)._

1. **Integrate Alonso & Church in Section II-B**:
   - Focus on their principles of realistic workloads, robust statistical aggregation (using geometric means relative to baselines, similar to the SPEC CPU standard), and the dangers of benchmark repurposing (using the Penn Treebank example).
2. **Expand BetterBench's Role**:
   - Elaborate on their lifecycle findings (Implementation and Maintenance as weak spots across 24 assessed benchmarks) and connect MESA's Part A/B structure to their 46 best-practice criteria.

```latex
% Insert into Section II-B (AI Benchmark Quality and Validity)
Recent work by Alonso and Church \cite{alonso_church_sigir} advocates for "evaluating the evaluations," proposing that AI benchmarks must follow structured software engineering principles similar to the SPEC CPU benchmarks. They emphasize the necessity of designing for realistic workloads, documenting data preprocessing choices, and calculating geometric means relative to baselines rather than simple arithmetic averages. Crucially, they highlight the risks of arbitrary benchmark repurposing through the example of the Penn Treebank (PTB) \cite{marcus_etal_1993_building}, which was designed for syntax parsing but downstream repurposed for perplexity. In this transition, inappropriate vocabulary reduction (replacing rare words with a generic \texttt{<unk>} token) rendered perplexity estimations structurally trivial and disconnected from real-world utility.

This concern with benchmark lifecycle quality is shared by Reuel et al. \cite{reuel_betterbench}, whose BetterBench framework audits 24 benchmarks across five lifecycle stages (Design, Implementation, Documentation, Maintenance, and Retirement). Their analysis reveals that the implementation stage is globally the weakest, with 17 out of 24 benchmarks failing to provide replication scripts. MESA maps these technical software concerns (such as metadata standards, licenses, and replication packages) to Part B's evaluative categories, combining them with a formal psychometric lens to assess the validity of the resulting capability claims.
```

---

## Task 4: Address Auditing Subjectivity & LLM Limits (Reviewer 3)

_Clarify the role of LLMs as assistive drafting tools rather than authoritative judges, and address how score interpretation is codependent on model training._

1. **De-emphasize LLM Autonomy**:
   - Explain that the LLM consensus pipeline is a feasibility trial for automated parsing, but actual high-stakes MESA audits must be finalized by human domain experts.
2. **Model-Side Contextualization**:
   - Add a paragraph on how score validity depends on the interaction between the instrument (benchmark) and the test-taker (model's training set, pre-training priors, and scaffolding).

```latex
% Insert in Section III-D (or the newly created Section IV)
While MESA outlines a structured format for auditing benchmarks, the scoring process is not a replacement for human expert judgment. The multi-LLM consensus pipeline demonstrated in our test applications (Section V) serves strictly as an assistive tool to accelerate raw document ingestion, schema mapping, and draft generation. For critical assurance arguments, safety-case certifications, or procurement decisions, the final validation of MESA reviews must be adjudicated by human expert panels.
```

```latex
% Insert in Section VI (Discussion) as a new subsection
\subsection{Construct Validity at the Instrument-Evaluand Interface}
As highlighted by Reviewer 3, the interpretability of a benchmark score is highly codependent on the model's architectural characteristics, pre-training history, and runtime scaffolding. A text-only model that achieves high accuracy on the spatial grid tasks of ARC-AGI-2 demonstrates a significantly stronger generalization claim than a model pre-trained directly on programmatic grid layouts. Consequently, MESA's auditing of the measurement instrument must be interpreted alongside model-side metadata, such as Model Cards \cite{mitchell_model_cards_2019}. The ultimate capability claim is verified not by the benchmark score alone, but by the score in direct context of the evaluand's technical boundaries.
```

---

## Task 5: Document the Threats to Validity (Reviewer 1)

_Address empirical research threats to validity by adding a dedicated subsection._

1. **Insert Section VII (Threats to Validity)**:
   - Construct Validity: Is MESA capturing benchmark quality?
   - Internal Validity: Subjectivity of rating categories and LLM evaluation limits.
   - External Validity: Generalizability across different model modalities (e.g., live agent loops, security benchmarks).

```latex
\section{Threats to Validity}

\subsection{Construct Validity}
Construct threats concern whether MESA accurately measures the quality of an AI benchmark. We mitigated this risk by grounding MESA's categories in the EFPA Test Review Model \cite{efpa_test_review_model_2025}, which has undergone decades of refinement in educational testing. To ensure compatibility with software systems, we integrated concrete technical metrics from BetterBench \cite{reuel_betterbench} and workload-relevance principles from Alonso and Church \cite{alonso_church_sigir}.

\subsection{Internal Validity}
Internal validity concerns the subjectivity of MESA's categorical scoring. A reviewer might score Section 9 (Reliability) differently based on their tolerance for variance. We mitigate this subjectivity by requiring every Part B rating to be explicitly justified by documented evidence or flagged as an "unknown" evidence gap, steering the framework toward reproducible documentation rather than arbitrary scoring. Furthermore, our reliance on LLMs for the pilot test applications introduces potential generation bias. We addressed this by enforcing strict textual grounding rules and manual human reconciliation.

\subsection{External Validity}
External validity threats concern the generalizability of our findings. While MESA was applied to two highly prominent benchmarks (HLE and ARC-AGI-2) that represent distinct modalities, these cases may not fully capture the engineering constraints of live-evaluation systems (e.g., LMSYS Chatbot Arena) or reinforcement learning environments. Future work will expand MESA's application scope to validate its utility across wider benchmarking paradigms.
```

---

## Task 6: Minor Textual Polish (Reviewer 1)

_Fix all minor typos, spacing, and grammar errors._

1. **Spacing in Abstract**:
   - Change: `academic question-answering benchmark,rather than a standalone`
   - To: `academic question-answering benchmark, rather than a standalone`
2. **Grammar in Abstract**:
   - Change: `Our analysis reveals revealed that HLE...`
   - To: `Our analysis revealed that HLE...`
3. **Typos in Section I**:
   - Change: `It adapts (1) ->`
   - To: `Specifically, it (1) adapts...`
4. **General Verbosity Pass**:
   - Condense redundant explanations of psychometrics in the intro and methodology sections.

---

# Part 3: Updated `references.bib`

This was already done.
