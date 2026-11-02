"""Write questions.json: every question of the seven existing benchmark review frameworks.

Transcriptions are verbatim where the source gives a sentence; items marked
"paraphrase" are reworded from prose because the source gives no sentence.
Run from the repository root: python3 v4/mapping/build_questions.py
No network access; the sources are cited by location.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "questions.json"

FRAMEWORKS = {
    "BB": {
        "name": "BetterBench",
        "citation": "Reuel et al., BetterBench, NeurIPS 2024 Datasets and Benchmarks; arXiv 2411.12990",
        "source": "Appendix I.1 template and the public database page (betterbench.stanford.edu/database.html), criterion names as shown per benchmark",
        "answer_scale": "0 not acknowledged and not addressed; 5 acknowledged but not addressed; 10 partially addressed; 15 fully addressed; n/a not relevant (Appendix F)",
        "missing_information_rule": "A criterion that is neither acknowledged nor addressed receives 0; mentioned but not provided receives 5; not relevant receives n/a and is excluded from averages (Appendix F).",
        "reuse_terms": "Assessments released under CC BY 4.0 (Appendix I.2). Paper text under arXiv terms; criterion names are short phrases.",
        "applied_to": ["humaneval", "truthfulqa", "hle", "tau-bench"],
    },
    "ECBD": {
        "name": "ECBD worksheet",
        "citation": "Liu et al., ECBD: Evidence-Centered Benchmark Design for NLP, ACL 2024; arXiv 2406.08723",
        "source": "template_worksheet/ECBD_worksheet_template.md in github.com/isle-dev/ECBD",
        "answer_scale": "Free text per question; questions come in describe, justify, support triples per module",
        "missing_information_rule": "No scoring. A describe question records what the creators state; a justify question records their reasons; a support question records the validity evidence offered. Absence of evidence is recorded as absence, not as a score.",
        "reuse_terms": "No license file in the repository. Repository file may be used with the authors' permission (given to the author, 31 October 2026); verbatim text may appear in prompts and in the public package with attribution. Nothing beyond the repository files was shared.",
        "applied_to": ["humaneval", "truthfulqa", "hle", "tau-bench"],
    },
    "SC": {
        "name": "Scorecard of AI Benchmark Quality",
        "citation": "San Joaquin, Gipiskis and Chin, EvalEval 2026, pages 128 to 160; DOI 10.18653/v1/2026.evaleval-1.25",
        "source": "Appendix A.2 Quality Dimensions (final version); local text literature/slr-2026-10-28/texts/R097.txt",
        "answer_scale": "Each item satisfied, unsatisfied or not applicable, with a justification; each dimension scored 1 to 4 from the severity of unsatisfied items; classes A to E from dimension scores (Appendix A.1, Section 5)",
        "missing_information_rule": "Vague or absent documentation can make an item unsatisfied; a baseline item unsatisfied makes the dimension unscorable and the evaluation invalid (Appendix A.1). Not applicable is allowed with a reason.",
        "reuse_terms": "ACL Anthology publication; check the PDF footer for the license before copying item text.",
        "applied_to": ["humaneval", "truthfulqa", "hle", "tau-bench"],
    },
    "H2B": {
        "name": "How2Bench",
        "citation": "Cao et al., How Should I Build A Benchmark? Revisiting Code-Related Benchmarks For LLMs; later titled Position: Code Benchmarks Should Prioritize Rigor, Reliability, and Reproducibility; arXiv 2501.10711",
        "source": "Printable checklist Figures/How2Bench-full-new.pdf and Figures/new_checklist/1-5.png in the arXiv source; 55 numbered criteria with priority stars",
        "answer_scale": "Checkbox per criterion; priority three stars highly important, two stars important, one star optional. In the authors' profiling study each criterion was labelled present or not mentioned (Section 7.3).",
        "missing_information_rule": "A benchmark is labelled as not considering a step unless the paper contains explicit textual evidence of it; not mentioned is grouped with not done (Sections 4.2 and 7.3).",
        "reuse_terms": "arXiv paper; the checklist is a figure. Check the arXiv license statement on the abstract page before copying.",
        "applied_to": ["humaneval"],
    },
    "ABC": {
        "name": "Agentic Benchmark Checklist",
        "citation": "Zhu et al., Establishing Best Practices for Building Rigorous Agentic Benchmarks, NeurIPS 2025; arXiv 2507.02825",
        "source": "ABC.md in github.com/uiuc-kang-lab/agentic-benchmarks (item wording) and Section 4 of the paper (identifiers T, O, R)",
        "answer_scale": "1 point if satisfied, 0 otherwise (Section 5.1)",
        "missing_information_rule": "An item the benchmark does not document or address receives 0 with a short reason (Appendix D reports). No separate category for missing information.",
        "reuse_terms": "No license file in the repository; arXiv paper. Repository file may be used with the authors' permission (given to the author, 31 October 2026); verbatim text may appear in prompts and in the public package with attribution. Nothing beyond the repository files was shared. The two paraphrased items (T.6, O.f.1) come from the paper, not the repository file.",
        "applied_to": ["tau-bench"],
    },
    "CAL": {
        "name": "Benchmark Caliper",
        "citation": "Corona, Truong, Trager and others; repository github.com/aims-foundations/benchmark-caliper; paper listed as Uplifting Human Decision Making in AI Evaluation by Automating Benchmark Validity Analysis (ICML 2026 workshop) and in the framework file as Validity Analysis when Porting Benchmarks Across Cultures and Regions",
        "source": "framework.yaml in the repository: six dimensions, each with definition, checklist items and a 1 to 5 scoring rubric",
        "answer_scale": "1 to 5 per dimension: 1 major validity violations; 2 significant concerns; 3 partially addressed; 4 well addressed; 5 fully addressed. Item scoring returns Unknown when evidence is insufficient.",
        "missing_information_rule": "Unknown is returned when evidence is insufficient for an item; at dimension level the rubric scores documented awareness, so silence lowers the score.",
        "reuse_terms": "No license file in the repository. Repository file may be used with the authors' permission (given to the author, 31 October 2026); verbatim text may appear in prompts and in the public package with attribution. Nothing beyond the repository files was shared.",
        "applied_to": [],
        "note": "Every item presumes a stated target deployment context. Mapped for coverage only after HELM was removed on 31 October 2026.",
    },
    "OECD": {
        "name": "OECD facets",
        "citation": "Cohn and Hernandez-Orallo, A framework for characterising evaluation instruments of AI performance, chapter 6 of AI and the Future of Skills, Volume 2, OECD 2023, DOI 10.1787/a9fe53cb-en; earlier Cohn et al., A Framework for Categorising AI Evaluation Instruments, IJCAI-ECAI 2022 workshop, CEUR-WS Vol-3169 paper 3, CC BY 4.0",
        "source": "Chapter 6, section Characterising AI evaluation instruments; local text literature/slr-2026-10-28/texts/S05.txt lines 4520 to 4590",
        "answer_scale": "One categorical value per facet from the listed values; some values require a free text specification",
        "missing_information_rule": "Reliability allows N/A when the testing methodology or common use is not clear. Other facets have no missing value; raters choose from the listed values.",
        "reuse_terms": "OECD publication terms for the chapter; the 2022 workshop paper is CC BY 4.0.",
        "applied_to": ["humaneval", "truthfulqa", "hle", "tau-bench"],
        "note": "A classification. Only facets with a preferred value enter agreement and missing information results; the others are reported as a description and feed the new rubric's description part.",
    },
}

# answerability: "yes" from paper text, README and repository text files;
# "no" needs information outside those inputs; "partly" with the reason.
A_YES = "yes"


def bb():
    items = [
        ("design", "Tested capability or concept is defined", A_YES),
        ("design", "How tested capability or concept translates to benchmark task is described", A_YES),
        ("design", "How knowing about the tested capability or concept is helpful in the real world is described", A_YES),
        ("design", "How benchmark scores should or shouldn't be interpreted or used is described", A_YES),
        ("design", "Domain experts are involved", A_YES),
        ("design", "Use cases or user personas are described", A_YES),
        ("design", "Domain literature is integrated", A_YES),
        ("design", "Informed performance metric choice", A_YES),
        ("design", "Metric floors and ceilings are included", A_YES),
        ("design", "Human performance level is included", A_YES),
        ("design", "Random performance level is included", A_YES),
        ("design", "Has validated automatic evaluation", A_YES),
        ("design", "Differences to related benchmarks are explained", A_YES),
        ("design", "Input sensitivity is addressed", A_YES),
        ("implementation", "Evaluation code is available", A_YES),
        ("implementation", "Evaluation data or generation mechanism is accessible", A_YES),
        ("implementation", "Evaluation of models via API is supported", A_YES),
        ("implementation", "Evaluation of local models is supported", A_YES),
        ("implementation", "A globally unique identifier is added or evaluation instances are encrypted", A_YES),
        ("implementation", "Task to identify if model is trained on benchmark data is included", A_YES),
        ("implementation", "Script to replicate results is included", A_YES),
        ("implementation", "Statistical significance or uncertainty quantification of benchmark results is reported", A_YES),
        ("implementation", "Need for warnings for sensitive/harmful content is assessed", A_YES),
        ("implementation", "Build status (or equivalent) is implemented", "partly: a badge or workflow file may be in the repository text, but the live status is not"),
        ("implementation", "Release requirements are specified", A_YES),
        ("documentation", "Requirements file or equivalent is available", A_YES),
        ("documentation", "Quick-start guide or demo is available", A_YES),
        ("documentation", "In-line code comments are used", A_YES),
        ("documentation", "Code documentation is available", A_YES),
        ("documentation", "Accompanying paper is accepted at peer-reviewed venue", "partly: only if the paper text names its venue"),
        ("documentation", "Benchmark construction process is documented", A_YES),
        ("documentation", "Test tasks & rationale are documented", A_YES),
        ("documentation", "Assumptions of normative properties are documented", A_YES),
        ("documentation", "Limitations are documented", A_YES),
        ("documentation", "Data collection process, test environment design, or prompt design process is documented", A_YES),
        ("documentation", "Evaluation metric is documented", A_YES),
        ("documentation", "Applicable license is specified", A_YES),
        ("documentation", "Globally unique, persistent identifier for dataset and metadata is provided", A_YES),
        ("documentation", "Standardized metadata is included", A_YES),
        ("documentation", "Data sources and how the data was collected is documented", A_YES),
        ("documentation", "Data preprocessing steps taken are documented", A_YES),
        ("documentation", "Data annotation process is documented (if applicable)", A_YES),
        ("documentation", "Representativeness of the data is explained (if applicable)", A_YES),
        ("documentation", "Documentation follows recognized standard", A_YES),
        ("maintenance", "Code usability was checked within the last year", "no: needs the maintainers' activity outside the snapshot"),
        ("maintenance", "Maintained feedback channel for users is available", "no: needs the live issue tracker or channel, not the snapshot"),
        ("maintenance", "Contact person is listed", A_YES),
    ]
    return [
        {"id": f"BB-{i:02d}", "framework": "BB", "group": g, "text": t, "verbatim": True,
         "source_location": "database page criterion name; Appendix I.1 template", "answerable_from_inputs": a}
        for i, (g, t, a) in enumerate(items, 1)
    ]


def ecbd():
    q = [
        ("Intended Use", "Q1", "Who/What are the intended objects of evaluation?", "describe"),
        ("Intended Use", "Q2", "What is the intended use of the benchmark? Who are the intended users of the benchmark?", "describe"),
        ("Capability", "Q3", "DESCRIBE: i) What are the capabilities of interest? ii) How is each one defined, and under what context is each one defined?", "describe"),
        ("Capability", "Q4", "JUSTIFY: How are the capabilities of interest connected to the intended use of the benchmark (specified in Q2)? Are the capabilities theoretically attainable by the objects to be evaluated?", "justify"),
        ("Capability", "Q5", "SUPPORT: What validity evidence do the benchmark creators offer to support the choice and definition of capabilities of interest?", "support"),
        ("Content", "Q6", "DESCRIBE: i) Characterize the test items. ii) Which capabilities of interest does each test item aim to capture?", "describe"),
        ("Content", "Q7", "JUSTIFY: How does each test item elicit evidence about its target capabilities? Justify via the characteristics of the test items (Q6).", "justify"),
        ("Content", "Q8", "SUPPORT: What evidence do the benchmark creators offer to support content validity of the test items?", "support"),
        ("Adaptation", "Q9", "DESCRIBE: Given an input, how are the objects of evaluation adapted or instructed to provide the output?", "describe"),
        ("Adaptation", "Q10", "JUSTIFY: Elaborate on the suitability of the adaptation methods for all intended objects of evaluation.", "justify"),
        ("Adaptation", "Q11", "SUPPORT: What validity evidence do benchmark designers offer that supports the choice of the adaptation methods?", "support"),
        ("Assembly", "Q12", "DESCRIBE: How many test items are chosen to assemble the subset used for evaluation? What factors inform this selection?", "describe"),
        ("Assembly", "Q13", "JUSTIFY: How does the described assembly method ensure that the produced subset elicits sufficient evidence for all capabilities of interest?", "justify"),
        ("Assembly", "Q14", "SUPPORT: What validity evidence do the benchmark creators offer to support the choice of assembly methods?", "support"),
        ("Evidence extraction", "Q15", "DESCRIBE: For each test item, i) What responses are captured and used for evidence extraction? ii) How is evidence extracted and represented?", "describe"),
        ("Evidence extraction", "Q16", "JUSTIFY: How does the extracted evidence capture the capabilities of interest?", "justify"),
        ("Evidence extraction", "Q17", "SUPPORT: What validity evidence do the benchmark creators offer to support the choice of evidence extraction method?", "support"),
        ("Evidence accumulation", "Q18", "DESCRIBE: How is the evidence accumulated to draw insights about the objects of evaluation in terms of capabilities of interest?", "describe"),
        ("Evidence accumulation", "Q19", "JUSTIFY: How does the method of accumulating evidence capture capabilities of interest?", "justify"),
        ("Evidence accumulation", "Q20", "SUPPORT: What validity evidence do the benchmark creators offer to support the choice of evidence accumulation method?", "support"),
    ]
    return [
        {"id": f"ECBD-{k}", "framework": "ECBD", "group": g, "text": t, "kind": kind, "verbatim": True,
         "source_location": "ECBD_worksheet_template.md", "answerable_from_inputs": A_YES}
        for g, k, t, kind in q
    ]


def sc():
    # (dimension, principle, bullet or None, text)
    rows = [
        ("Construct Validity", "Define the phenomenon", None, "Define the phenomenon"),
        ("Construct Validity", "Define the phenomenon", 1, "Precise and operational definition for the target phenomenon"),
        ("Construct Validity", "Define the phenomenon", 2, "Specify scope"),
        ("Construct Validity", "Define the phenomenon", 3, "If the target phenomenon has distinct facets (e.g. factual accuracy vs. tone), score each facet independently rather than collapsing them into a single metric"),
        ("Construct Validity", "Build a representative dataset", None, "Build a representative dataset"),
        ("Construct Validity", "Build a representative dataset", 1, "Define and document the intended task space, including its full range of difficulty and variation"),
        ("Construct Validity", "Build a representative dataset", 2, "Verify that sampled items cover the full range of the documented task space"),
        ("Construct Validity", "Build a representative dataset", 3, "Especially for automated generations, have a robust algorithm for verifying that each item actually tests the target phenomenon"),
        ("Construct Validity", "Build a representative dataset", 4, "Include edge-case inputs that probe boundary conditions and known model sensitivities"),
        ("Construct Validity", "If reusing datasets, acknowledge limitations", None, "If reusing datasets, acknowledge limitations"),
        ("Construct Validity", "If reusing datasets, acknowledge limitations", 1, "Analyze effects of adapting prior work, including comparing new benchmark against original"),
        ("Construct Validity", "If reusing datasets, acknowledge limitations", 2, "Explain modifications to reused dataset"),
        ("Construct Validity", "Use statistical methods to compare models", None, "Use statistical methods to compare models"),
        ("Construct Validity", "Use statistical methods to compare models", 1, "Report sample size and justify statistical power"),
        ("Construct Validity", "Use statistical methods to compare models", 2, "Report uncertainty estimates at least for primary scores"),
        ("Construct Validity", "Use statistical methods to compare models", 3, "If using human raters, document rater instructions and training materials"),
        ("Construct Validity", "Use statistical methods to compare models", 4, "If using human raters, identify and mitigate potential demographic biases among raters (i.e. whether rater demographics skew which outputs are judged as correct)"),
        ("Construct Validity", "Use statistical methods to compare models", 5, "Use metrics that preserve label variability (e.g. inter-annotator agreement distributions)"),
        ("Construct Validity", "Use statistical methods to compare models", 6, "Do not reduce subjective labels to single-point aggregates (e.g. simple mean)"),
        ("Construct Validity", "Conduct an error analysis", None, "Conduct an error analysis"),
        ("Construct Validity", "Conduct an error analysis", 1, "Analyze whether model failures are caused by confounds (e.g. formatting, language complexity, prompt length) rather than the capability under test"),
        ("Construct Validity", "Conduct an error analysis", 2, "Identify and analyze common failure modes of models on the evaluation"),
        ("Construct Validity", "Justify construct validity", None, "Justify construct validity"),
        ("Construct Validity", "Justify construct validity", 1, "Provide rationale for tasks and metrics chosen"),
        ("Construct Validity", "Justify construct validity", 2, "Demonstrate how this evaluation differs from or improves upon existing evaluations measuring the same or similar constructs, addressing gaps or limitations in prior work"),
        ("Construct Validity", "Justify construct validity", 3, "Provide a clear rationale for design choices, including their limitations and how strong performance on the evaluation would predict real-world capability"),
        ("Internal Validity", "Only measure the phenomenon", None, "Only measure the phenomenon"),
        ("Internal Validity", "Only measure the phenomenon", 1, "Verify that the evaluation design handles unavoidable secondary capabilities needed for the target phenomenon (e.g. reading comprehension in a numeracy test)"),
        ("Internal Validity", "Only measure the phenomenon", 2, "Identify any construct overlap between the target phenomenon and related phenomena"),
        ("Internal Validity", "Only measure the phenomenon", 3, "Quantify the extent of that overlap and describe mitigation steps taken"),
        ("Internal Validity", "Only measure the phenomenon", 4, "Test whether output format requirements (e.g. response length limits, structured output schemas, JSON formatting) independently affect model scores, and report these effects"),
        ("Internal Validity", "Only measure the phenomenon", 5, "Test whether small, semantically irrelevant changes to prompt wording (e.g. punctuation, synonym substitution) produce large swings in model scores; report sensitivity as a variance measure"),
        ("Internal Validity", "Only measure the phenomenon", 6, "Test for systematic parsing bias across different output types (i.e. whether the parser systematically favours or penalises particular response formats independent of correctness)"),
        ("Internal Validity", "Ground truth access", None, "Describe the mechanisms used to ensure the model cannot access ground truth labels or answer keys during evaluation, and document any residual leakage risk"),
        ("Internal Validity", "Ground truth access", 1, "Confirm that the model being evaluated and any model used as a rater or judge were not trained on data that overlaps with the evaluation's test set"),
        ("Internal Validity", "Environment stability", None, "If the evaluation environment changes over time (e.g. API versions, live web data), document each change and re-validate affected results, or use a static snapshot"),
        ("Internal Validity", "Residual state", None, "Residual data / state are cleared between evaluation runs"),
        ("Internal Validity", "Chance", None, "The chance of randomly arriving at the correct answer is minimized"),
        ("Internal Validity", "Chance", 1, "Avoid MCQs, unless mitigations are in place to reduce gaming through guessing"),
        ("External Validity", "Domain experts and users", None, "Involve domain experts / real users in defining evaluation scenarios and acceptance criteria"),
        ("External Validity", "Expert content review", None, "Have domain experts review evaluation content for accuracy and relevance"),
        ("External Validity", "Prompting settings", None, "Takes different prompting/elicitation settings into account"),
        ("External Validity", "Stress conditions", None, "Non-IID testing under a variety of stress conditions and severities"),
        ("External Validity", "Application-centric evaluation", None, "If applicable, models deployed to particular applications should have application-centric evaluations"),
        ("External Validity", "Application-centric evaluation", 1, "Evaluate under the system configuration (model and environment setup) expected in real deployment"),
        ("External Validity", "Application-centric evaluation", 2, "Test whether the model can be manipulated into passing via adversarial inputs or misuse scenarios"),
        ("External Validity", "Application-centric evaluation", 3, "Document how the test environment differs from real deployment, including missing variability (user diversity, platform differences, adversarial inputs), and interpret results in light of those gaps"),
        ("Reliability", "Replicability", None, "Replicability: re-run the exact evaluation, get the same result"),
        ("Reliability", "Replicability", 1, "Fully document all environment variables (hyperparameters, software versions, OS, hardware) such that an independent third party can reproduce results on different infrastructure"),
        ("Reliability", "Replicability", 2, "Have an independent third party reproduce the results on different infrastructure."),
        ("Reliability", "Flaw mitigation", None, "Flaw mitigation"),
        ("Reliability", "Flaw mitigation", 1, "Describe steps to prevent, identify, and correct for flaws in evaluation"),
        ("Reliability", "Flaw mitigation", 2, "For each unavoidable flaw: (a) explain qualitatively what it is and which direction it likely biases results, (b) quantify its impact where possible (e.g. ground truth noise), and (c) provide explicit guidance on which conclusions from the evaluation remain valid despite the flaw and which do not"),
        ("Reliability", "Interpretation of methodology and results", None, "Interpretation of methodology and results"),
        ("Reliability", "Interpretation of methodology and results", 1, "Report relevant baselines, especially human baselines for human-centric tasks"),
        ("Reliability", "Interpretation of methodology and results", 2, "Report performance of minimal baselines (e.g. random selection, majority-class prediction, zero-shot naive models) to establish a lower bound and give context for model scores"),
        ("Correctness", "Ground truth verification", None, "Annotated ground truth is verified robustly, whether annotated by humans or AI"),
        ("Correctness", "Ground truth verification", 1, "If using model rater(s), document evidence that ratings correlate with human judgments; design the rater to resist adversarial inputs and reward hacking; verify consistency of model rater across repeated identical inputs; identify and mitigate systematic biases in the model rater"),
        ("Correctness", "Ground truth verification", 2, "Multiple annotators label each item independently, with inter-annotator agreement reported (e.g. Cohen's kappa >= 0.7), or a programmatic verification method with documented accuracy is used"),
        ("Correctness", "Verified end state", None, "Each task has a verified end state, whether it is solvable or not"),
        ("Correctness", "Verified end state", 1, "Classify each task as solvable or intentionally unsolvable, and document the expected model behavior for each type"),
        ("Correctness", "Verified end state", 2, "For solvable tasks, provide verified ground-truth solutions"),
        ("Correctness", "Verified end state", 3, "Enumerate all valid solution forms, or specify acceptance criteria broad enough to recognize equivalent correct answers"),
        ("Correctness", "Scoring not exploitable", None, "The scoring implementation must not be exploitable through shortcuts such as outputting trigger strings, exploiting parser edge cases, or matching answer patterns without completing the underlying task"),
        ("Correctness", "Scoring not exploitable", 1, "Scoring rules are well-specified and handle edge-case outputs such as partial answers, correct answers in unexpected formats, and refusals"),
        ("Correctness", "Scoring not exploitable", 2, "Validate that the automated output parser produces consistent results on identical inputs"),
        ("Correctness", "Scoring not exploitable", 3, "Measure parser accuracy against a set of manually verified outputs"),
        ("Correctness", "Scoring not exploitable", 4, "Conduct adversarial testing of the scoring pipeline to verify it cannot be gamed without the model completing the task"),
    ]
    out = []
    n = 0
    for dim, principle, bullet, text in rows:
        n += 1
        out.append({
            "id": f"SC-{n:02d}", "framework": "SC", "group": dim, "principle": principle,
            "level": "principle" if bullet is None else "bullet", "text": text, "verbatim": True,
            "source_location": "Appendix A.2 Quality Dimensions",
            "answerable_from_inputs": "partly: a third party reproduction (Replicability bullet 2) cannot be seen from the inputs" if "third party reproduce" in text else A_YES,
        })
    return out


def h2b():
    items = [
        (1, "Design", 3, "Consider whether the benchmark can fill the gap in related research."),
        (2, "Design", 3, "Consider what is the expected scope of the benchmark set (e.g., what natural languages, programming languages, task granularity)."),
        (3, "Design", 3, "Consider the expected application scenario of this benchmark (e.g., programming assistant, automated tester)."),
        (4, "Design", 3, "Consider the LLMs' capabilities (e.g., understanding, reasoning, calculation) and domain knowledge (e.g., OOP, memory management, fault localization, process scheduling) that the benchmark hopes to evaluate."),
        (5, "Construction", 1, "Consider whether the data source of the benchmark is traceable."),
        (6, "Construction", 2, "Consider whether the data source of the benchmark is of high quality (e.g., stars, downloads, last update times, number of forks)."),
        (7, "Construction", 1, "Consider whether the benchmark's data source is representative (e.g., choose an open-source community or code hosting platform that matches the task, capability, and scope under study)"),
        (8, "Construction", 1, "Consider data contamination issues during the benchmark collection (e.g., considering the upload time of the source code or checking whether the data source is included in the training data of LLMs)."),
        (9, "Construction", 1, "If data sampling is needed, consider whether the choice of sample size is scientific (e.g., considering the confidence level/margin of error/sampling proportion, etc.)."),
        (10, "Construction", 1, "If data sampling is needed, consider whether the sampling process is rigorous (e.g., random sampling, stratified sampling, etc.)."),
        (11, "Construction", 1, "Ensure each data point in the benchmark falls into the targeted scope (e.g., checking each data point's evaluated capabilities or domain knowledge)."),
        (12, "Construction", 3, "Consider whether the data in the benchmark can cover the studied capabilities/domain knowledge/application scenarios."),
        (13, "Construction", 2, "Consider whether there is a standard answer for each sample in the benchmark (such as reference code, etc.)."),
        (14, "Construction", 1, "For code, consider whether the code is compilable/executable."),
        (15, "Construction", 2, "Consider the possibility of noise in the data and perform denoise."),
        (16, "Construction", 2, "Consider the possibility of duplication in the data and deduplicate them."),
        (17, "Construction", 2, "Clean the sensitive information (such as data desensitization and anonymization) unless the benchmark is deliberately designed so."),
        (18, "Construction", 2, "Manually review some or all of the data in the benchmark to ensure its quality."),
        (19, "Construction", 1, "Use LLMs to review some or all of the data in the benchmark to ensure its quality."),
        (20, "Construction", 3, "Design appropriate output validation methods for the benchmark (e.g., using exact matching or designing test cases)."),
        (21, "Construction", 3, "Design appropriate evaluation metrics for the evaluation set (e.g., precision, accuracy, pass@K, recall)."),
        (22, "Construction", 3, "Consider the adequacy of the evaluation metrics (e.g., is the code coverage high enough)."),
        (23, "Construction", 1, "Consider if there are any other evaluation perspectives (e.g., readability, efficiency, safety, security)."),
        (24, "Evaluation", 1, "Consider whether sufficient LLMs are evaluated."),
        (25, "Evaluation", 1, "Consider whether representative LLMs (e.g., covering latest/classical LLM families, small/large LLMs, and open-/closed-source LLMs) are evaluated."),
        (26, "Evaluation", 3, "Consider whether the prompt is of high quality (e.g., the instruction and intent are clear)."),
        (27, "Evaluation", 1, "The prompts have been validated by humans or LLMs (e.g., evaluated or discussed by participants or preliminarily tried out on several LLMs)."),
        (28, "Evaluation", 1, "Try different paraphrases of the prompt."),
        (29, "Evaluation", 2, "Try different prompting strategies to observe the impact on the evaluation results (e.g., in-context learning, chain-of-thought)."),
        (30, "Evaluation", 3, "Pay attention to the hardware environment (such as GPU card, storage size, etc.) of the experiment."),
        (31, "Evaluation", 3, "Pay attention to the operating system and software environment (e.g. operating system, version, etc.) used for the experiment."),
        (32, "Evaluation", 2, "Pay attention to the off-the-shelf platforms, frameworks, or libraries for LLM evaluation (e.g., fast chat, vllm, huggingface) that are used."),
        (33, "Evaluation", 1, "Repeat the experiment multiple times to reduce the impact of randomness on the evaluation."),
        (34, "Evaluation", 2, "Consider various randomization strategies (e.g., trying various temperature parameters) to reduce the impact of parameter configuration on the evaluation."),
        (35, "Evaluation", 3, "Record the experimental process in detail (e.g., parameter settings, running time, input/output pairs, etc.)."),
        (36, "Analysis", 2, "Observe the difficulty of the benchmark, checking if the benchmark is too hard or too easy for LLMs (i.e., most LLMs score too high/low)."),
        (37, "Analysis", 1, "Consider whether the benchmark can distinguish the pros and cons of different LLMs."),
        (38, "Analysis", 1, "If the experiment is repeated several times, consider the stability of the benchmark (i.e., whether the experimental results vary too much in the repeated experiments)."),
        (39, "Analysis", 2, "Analyze the correlation between the data and their score. For example, if there is a correlation between the data (such as similar difficulty and knowledge required), then the scores should also be correlated."),
        (40, "Analysis", 1, "Compare the performance of LLMs on this benchmark with their performance on other related benchmarks."),
        (41, "Analysis", 3, "Consider presenting the experiment results in an appropriate way (e.g., table, line graph, pie chart, etc.)."),
        (42, "Analysis", 3, "Consider presenting the experiment results clearly (e.g., distinguishable colors/labels/shapes, etc.)."),
        (43, "Analysis", 3, "Explain the experiment results."),
        (44, "Analysis", 1, "Observe correlations via multiple perspectives from the experimental results (e.g., performance is correlated with model size or amount of context)."),
        (45, "Release", 1, "The analysis of the evaluation results will be inspiring (e.g., shed light on future direction, make actionable advice, etc.)."),
        (46, "Release", 3, "Set the appropriate license for the benchmark."),
        (47, "Release", 3, "Review the released benchmark or other artifacts to ensure they do NOT contain sensitive information (e.g., API keys, usernames, passwords, etc.)."),
        (48, "Release", 3, "Review the released benchmark or other artifacts to ensure they do NOT contain toxicity information (e.g., abusive comments/identifiers)."),
        (49, "Release", 3, "Make sure the benchmark is open-accessible."),
        (50, "Release", 3, "Make sure the test cases or reference data are open and accessible."),
        (51, "Release", 3, "Provide prompts used in the experiment to ensure the experiments are reproducible."),
        (52, "Release", 3, "Disclose the experimental environment (e.g., hardware, operating system, software version, framework platform) to ensure the reproducibility of the experiment."),
        (53, "Release", 3, "Make the detailed experimental results public for verification."),
        (54, "Release", 2, "Ensure the quality of the user manual such as README (e.g., it contains necessary benchmark introduction, executable scripts, etc.)."),
        (55, "Release", 2, "Provide convenient evaluation interfaces for the released benchmark (e.g., providing a command line interface, docker, etc.)."),
    ]
    out = []
    for n, phase, stars, text in items:
        ans = A_YES
        if n == 45:
            ans = "no: a judgment of future influence, not a fact in the inputs"
        if n in (41, 42):
            ans = "partly: figure quality is lost in text extraction"
        out.append({"id": f"H2B-{n:02d}", "framework": "H2B", "group": phase, "priority_stars": stars, "text": text,
                    "verbatim": True, "source_location": f"printable checklist, criterion {n}", "answerable_from_inputs": ans})
    return out


def abc():
    items = [
        ("T.1", "Task validity: tool", "Versions of all tools (e.g., Python) are clearly specified.", True),
        ("T.2", "Task validity: tool", "All required API tools are consistently accessible to agents during evaluation.", True),
        ("T.3", "Task validity: tool", "Evaluation process terminates or handles errors appropriately if an API becomes inaccessible.", True),
        ("T.4", "Task validity: environment", "Residual data or state are fully cleared between runs.", True),
        ("T.5", "Task validity: environment", "Agent is completely isolated from any ground truth information.", True),
        ("T.6", "Task validity: environment", "The environment setup is fully reproducible and frozen at the time of benchmark release, without reliance on dynamic external resources.", False),
        ("T.7", "Task validity: implementation", "Annotated ground truth is verified for correctness.", True),
        ("T.8", "Task validity: implementation", "Each task is verified to be solvable.", True),
        ("T.9", "Task validity: implementation", "Benchmark includes an Oracle solver that can automatically solve all challenges.", True),
        ("T.10", "Task validity: implementation", "Outliers in pilot experiments are inspected to identify implementation bugs, impossible tasks or shortcuts.", False),
        ("O.a.1", "Outcome validity: whole string matching", "Considers expressions semantically equivalent to ground truth.", True),
        ("O.a.2", "Outcome validity: whole string matching", "Handles redundant words used by agents.", True),
        ("O.b.1", "Outcome validity: substring matching", "Handles negation modifiers used by agents.", True),
        ("O.b.2", "Outcome validity: substring matching", "Is robust against systematically listing all possible answers.", True),
        ("O.b.3", "Outcome validity: substring matching", "Ground truth is sufficiently complex to prevent guessing.", True),
        ("O.c.1", "Outcome validity: LLM as a judge", "Demonstrates documented or experimental evidence of the judge's accuracy, self-consistency, and agreement with human.", True),
        ("O.c.2", "Outcome validity: LLM as a judge", "Is designed to resist adversarial inputs and reward hacking.", True),
        ("O.d.1", "Outcome validity: unit testing", "Verifies test cases for correctness and quality (e.g., by human).", True),
        ("O.d.2", "Outcome validity: unit testing", "Measures quality of test cases using objective metrics (e.g., code coverage, cyclomatic complexity control).", True),
        ("O.e.1", "Outcome validity: fuzz testing", "Addresses potential edge cases.", True),
        ("O.e.2", "Outcome validity: fuzz testing", "Ensures comprehensive coverage of all relevant input variations (e.g., data types, memory layouts, value ranges).", True),
        ("O.e.3", "Outcome validity: fuzz testing", "Generates inputs that the code under testing is sensitive to.", True),
        ("O.f.1", "Outcome validity: end to end testing", "Covers all possible branches of user workflows.", False),
        ("O.f.2", "Outcome validity: end to end testing", "Exercises all relevant parts of the code being tested.", True),
        ("O.f.3", "Outcome validity: end to end testing", "Prevents non-deterministic (\"flaky\") test results.", True),
        ("O.g.1", "Outcome validity: state matching", "Ground truth includes all states achievable after success.", True),
        ("O.g.2", "Outcome validity: state matching", "Checks relevant and irrelevant states for the challenge.", True),
        ("O.g.3", "Outcome validity: state matching", "Ground truth is complex to prevent trivial state modifications.", True),
        ("O.h.1", "Outcome validity: answer matching", "Specifies required answer formats in challenge descriptions.", True),
        ("O.h.2", "Outcome validity: answer matching", "Minimizes the possibility of success by random guessing.", True),
        ("O.i.1", "Outcome validity: quality measure", "Designs quality metrics that prevent exploitation (e.g., achieving high scores by reward hacking)", True),
        ("R.1", "Reporting: transparency and validity", "Is fully or at least partially open-sourced.", True),
        ("R.2", "Reporting: transparency and validity", "Offers an open-source evaluation harness for users.", True),
        ("R.3", "Reporting: transparency and validity", "Includes measures to prevent data contamination, such as a private, held-out test set, or a lively updated dataset.", True),
        ("R.4", "Reporting: transparency and validity", "Includes measures or plans to consistently update challenges over time to avoid overfitting.", True),
        ("R.5", "Reporting: transparency and validity", "Clearly states the relationship between the agent capabilities it aims to evaluate and the constructs or outcomes it measures.", True),
        ("R.6", "Reporting: transparency and validity", "Clearly states the evaluation subjective of the benchmark (e.g., a model or an agent framework).", True),
        ("R.7", "Reporting: flaw mitigation", "Describes steps taken to prevent, identify, and correct flaws.", True),
        ("R.8", "Reporting: flaw mitigation", "Includes qualitative discussions of the potential impact of unavoidable flaws.", True),
        ("R.9", "Reporting: flaw mitigation", "Includes quantitative analysis to assess the impact of unavoidable flaws (e.g., noise of ground truth).", True),
        ("R.10", "Reporting: interpretation", "Reports metrics about statistical significance, such as confidence intervals.", True),
        ("R.11", "Reporting: interpretation", "Provides guidance on interpreting results with eval flaws.", True),
        ("R.12", "Reporting: interpretation", "Reports results of non-AI baselines (e.g., human experts).", True),
        ("R.13", "Reporting: interpretation", "Reports results of trivial agents (e.g., one that does nothing).", True),
    ]
    out = []
    for pid, group, text, verbatim in items:
        out.append({"id": f"ABC-{pid}", "framework": "ABC", "group": group, "text": text, "verbatim": verbatim,
                    "source_location": "ABC.md in the repository" if verbatim else "paraphrase of Section 4 prose; the repository file has no sentence for this identifier",
                    "answerable_from_inputs": "partly: pilot experiment inspection is reported only if the paper says so" if pid == "T.10" else A_YES})
    return out


def cal():
    dims = [
        ("Input Ontology", "IO", [
            "Identify test case categories required for regional deployment.",
            "Check if source benchmark's taxonomy omits regionally-relevant categories.",
            "Check if source benchmark includes categories irrelevant to regional context.",
            "Document category gaps that would harm content validity."]),
        ("Input Content", "IC", [
            "Determine if input queries require region-specific cultural, geographic, or dialectal knowledge.",
            "Assess whether culturally sensitive content aligns with target deployment culture.",
            "Flag inputs requiring Western-specific knowledge that may not transfer.",
            "Recruit regional annotators to identify culturally sensitive instances if resources permit.",
            "Document content issues that would harm content validity."]),
        ("Input Form", "IF", [
            "Compare signal distributions (e.g., image resolution, MRI field strength) between source and target contexts.",
            "Check if regional infrastructure supports the same data capture specifications.",
            "Identify domain-specific form differences relevant to the intended use case.",
            "Document form mismatches that would harm external validity."]),
        ("Output Ontology", "OO", [
            "Review output label categories for regional relevance.",
            "Identify missing categories specific to regional contexts (e.g., autorickshaws in Indian driving data).",
            "Flag categories that encode non-regional values or assumptions.",
            "Consider stakeholder-driven taxonomy redesign if significant misalignment exists.",
            "Document taxonomy issues that would harm structural validity and content validity."]),
        ("Output Content", "OC", [
            "Determine if ground truth labels reflect regional stakeholder perspectives.",
            "Assess potential disagreement between original annotators and regional population.",
            "Review annotator demographics in benchmark documentation (Datasheets, Data Statements).",
            "Consider label re-annotation by representative regional annotator pool.",
            "Review aggregation methods for potential erasure of minority perspectives.",
            "Document label issues that would harm convergent validity and external validity."]),
        ("Output Form", "OF", [
            "Check if expected output modality matches regional deployment needs.",
            "Assess text-to-speech availability for speech-based output requirements.",
            "Consider literacy rates and accessibility requirements in target population.",
            "Document form mismatches that would harm external validity."]),
    ]
    out = []
    for name, code, items in dims:
        for i, text in enumerate(items, 1):
            ans = "with a declared target context: the item asks about a deployment region the inputs do not name"
            if "Recruit" in text or "re-annotation" in text or "redesign" in text:
                ans = "no: an action for the porting team, not a fact about the benchmark"
            out.append({"id": f"CAL-{code}-{i}", "framework": "CAL", "group": name, "text": text, "verbatim": True,
                        "source_location": "framework.yaml checklist", "answerable_from_inputs": ans})
    return out


def oecd():
    facets = [
        ("Validity", "Capability", ["TASK-PERFORMANCE (specify)", "CAPABILITY (specify)"], None,
         "does the evaluation instrument just measure observed (aggregated) performance on a TASK (e.g. protein folding, credit scoring) or can the evaluation instrument also measure a CAPABILITY (e.g. object permanence, dealing with negation)?", "judgment"),
        ("Validity", "Coverage", ["BIASED (specify)", "REPRESENTATIVE"], "REPRESENTATIVE",
         "does the evaluation instrument cover a BIASED or unbiased (REPRESENTATIVE) distribution of what is meant to be measured?", "judgment"),
        ("Validity", "Purpose", ["RESEARCH", "CONFORMITY", "OTHER (specify)"], None,
         "is the benchmark meant to foster research or development, or to certify whether an AI system conforms with some level or standard?", "description"),
        ("Validity", "Realism", ["TOY", "GAMIFIED", "REALISTIC", "REAL-LIFE"], None,
         "to what extent is the evaluation instrument a toy problem or a complex gamified problem? Is it a realistic setting (e.g. a simulated scenario, a lab or testing facility) or is the evaluation itself happening in real life?", "description"),
        ("Validity", "Reference", ["ABSOLUTE", "RELATIVE (specify)"], None,
         "are results reported as an absolute metric (criterion-referenced) or are they reported as a relative (percentage) metric to a reference (norm referenced), e.g. human performance?", "description"),
        ("Validity", "Specificity", ["SPECIFIC", "CONTAMINATED"], "SPECIFIC",
         "are the results precisely aligned with what is meant to be measured or contaminated by other skills or tasks?", "judgment"),
        ("Consistency", "Adjustability", ["UNSTRUCTURED", "ABLATABLE", "ADAPTIVE"], None,
         "is the analysis of results on the set of instances unstructured?; has the evaluation instrument identified a set of meta-features such as difficulty or dimension that could be used to analyse the results by these dimensions (ablatable)?; or are these meta-features used to adaptively or adversarially choose the instances to test more informatively (adaptive)?", "judgment"),
        ("Consistency", "Containedness", ["FULLY-CONTAINED", "PARTIAL-INTERFERENCE (specify)", "NOT-CONTAINED (specify)"], "FULLY-CONTAINED",
         "Once started, is the testing isolated from external factors or interference possibly affecting results (human participants, online data, weather, etc.)?; is there some partial interference not affecting the results significantly?; or is it dependent on external resources and conditions?", "description"),
        ("Consistency", "Judgeability", ["MANUAL", "AUTOMATED", "MIXED"], None,
         "is scoring manual (e.g. through human questionnaires or judges) or automated (e.g. correct answers or optimality function) or a mixture?", "description"),
        ("Consistency", "Reliability", ["RELIABLE", "NON-RELIABLE", "N/A"], "RELIABLE",
         "does the evaluation present sufficient repetitions, episode length or number of instances to give low variance for the same subject when applied again (test-retest reliability)? If the testing methodology or the common use of the evaluation instrument is not clear, then N/A may be the most appropriate facet value.", "judgment with evidence"),
        ("Consistency", "Reproducibility", ["NON-REPRODUCIBLE", "STOCHASTIC", "EXACT"], "EXACT",
         "is the evaluation non-reproducible, with results biased or spoiled if repeated?; does the evaluation instrument have stochastic components leading to different interactions?; or are the results completely reproducible, i.e. can the same exact test (inputs, interaction, etc.) be generated again for another (or the same) competitor?", "judgment with evidence"),
        ("Consistency", "Variation", ["FIXED", "ALTERED", "PROCEDURAL"], None,
         "is the evaluation based on fixed datasets?; have the instances been altered by adding post-processing variations (noise, rotations, etc.)?; or have the instances been created (e.g. using procedural generation)?", "description"),
        ("Fairness", "Ambition", ["SHORT", "LONG"], None,
         "when the evaluation instrument was created, was it aiming at the short term (improving on the state of the art) or long term (more ambitious goals)?", "judgment"),
        ("Fairness", "Antecedents", ["CREATED", "RETROFITTED (specify)"], None,
         "is it devised purposely for AI or adapted from tests designed to test humans?", "description"),
        ("Fairness", "Autonomy", ["AUTONOMOUS", "COUPLED (specify)", "COMPONENT"], None,
         "is it measuring an autonomous system, coupled with other systems (e.g. humans) or as an isolated component?", "description"),
        ("Fairness", "Objectivity", ["LOOSE", "CUSTOMISED", "FULLY-INDEPENDENT"], "FULLY-INDEPENDENT",
         "is it loosely defined, customised to each participant or does the evaluation instrument have a predetermined independent specification?", "description"),
        ("Fairness", "Partiality", ["PARTIAL (specify)", "IMPARTIAL"], "IMPARTIAL",
         "does the evaluation instrument favour particular technologies, conditions or cultures that should not have an influence on the result of the evaluation?", "judgment with evidence"),
        ("Fairness", "Progression", ["STATIC", "DEVELOPMENTAL"], None,
         "Is the score measuring a capability at one moment or is it evaluating the development of the capability of the system within the test?", "description"),
    ]
    agreement = {"Coverage", "Specificity", "Reliability", "Reproducibility", "Partiality"}
    low_agreement_2023 = {"Capability", "Coverage", "Specificity", "Adjustability", "Ambition"}
    out = []
    for group, facet, values, preferred, text, kind in facets:
        out.append({
            "id": f"OECD-{facet}", "framework": "OECD", "group": group, "text": text, "values": values,
            "preferred_value": preferred, "kind": kind,
            "enters_agreement": facet in agreement,
            "rater_agreement_2023": "low" if facet in low_agreement_2023 else ("consistent" if facet in {"Progression", "Autonomy", "Purpose", "Judgeability", "Containedness", "Objectivity"} else "moderate"),
            "verbatim": True, "source_location": "chapter 6, list of 18 facets",
            "answerable_from_inputs": A_YES if kind != "judgment" else "partly: the 2023 raters needed literature beyond the specification for Coverage and Specificity",
        })
    return out


def main():
    items = bb() + ecbd() + sc() + h2b() + abc() + cal() + oecd()
    data = {"frameworks": FRAMEWORKS, "items": items, "counts": {k: sum(1 for i in items if i["framework"] == k) for k in FRAMEWORKS}}
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(data["counts"]))


if __name__ == "__main__":
    main()
