# DesignQA — completed MESA-25 example

**Date:** 2026-10-06. **Status:** Source-checked worked example; not a validated questionnaire.

Original DesignQA benchmark: the 2024 v2 paper and public scoring implementation at commit dd909455afb9a6023917b3b68fc88dab943721a1. Intended use: research diagnosis and comparison of AI performance on engineering-documentation tasks, with broader claims assessed separately.

AI-assisted reviewer application of the 25-question checklist. Original reviews were already known; this is an unblinded comparison, not independent validation. Detailed comments and citations are supplied for this worked example only and remain optional for ordinary respondents.

The comments preserve the original reviews’ central diagnosis: realistic, well-motivated tasks and useful research materials, with incomplete support for precise rankings or broad engineering competence. Primary-source checks also require corrections to several original statements. Retained as a checked teaching example, not as proof that 25 choices replace a full MESA review.

[Comparison with the original reviews](designqa-comparison.md) · [Blank questionnaire](questionnaire.md)

## Source inventory

Access/inspection date for this application: 2026-10-06. Primary files and the comparison reviews are fingerprinted in [the source manifest](designqa-source-manifest.json). Historical review claims are not silently treated as current facts. The code commit predates the June 2026 reviews, but their exact inspected commit was not recorded here.

### Source P

[DesignQA paper, arXiv v2 (23 August 2024)](../../literature/DesignQA.md)

Primary source. Read the local transcription: introduction, dataset and scoring sections, evaluation, discussion, limitations and appendices. Used for task construction, reported experiments and claims. No new model runs; PDF tables were not independently re-extracted.

### Source R

[Repository README](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/README.md)

Primary source, inspected at the pinned commit. Used for setup, averaging, dataset paths and the submission procedure. The README gives an approximate rulebook length that differs from the paper; the example uses the paper’s 140-page description.

### Source C1

[Evaluation driver](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/full_evaluation.py)

Primary code inspection. Checked optional subset arguments, the six-score average and results-file output. No end-to-end model evaluation was run.

### Source C2

[Metric implementations](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/metrics/metrics.py)

Primary code inspection. Checked answer normalization, comma-separated rule parsing, component synonyms, yes/no extraction and explanation metrics. Inspection is not a complete scorer validation.

### Source ENV

[Dependencies](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/requirements.txt)

Lists nltk, rouge, pandas and sentence_transformers without version pins. This documents scoring dependencies, not a frozen model-running environment.

### Source TREE

[Repository file inventory, tags and releases](https://github.com/anniedoris/design_qa/tree/dd909455afb9a6023917b3b68fc88dab943721a1)

Recursive GitHub tree inspected at the commit; tags and releases endpoints returned empty lists on 2026-10-06. No license or changelog file was found in this inventory. This is a bounded file/document check, not a legal conclusion or proof that no policies exist elsewhere.

### Source OUT

[Released LLaVA retrieval predictions](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/rule_extraction/retrieval_evaluation_llava-13b.csv)

CSV inspected: 1,190 rows, with question, ground_truth and model_prediction columns. Establishes that some predictions are available. Its row count differs from the paper’s 1,192 retrieval questions, so it is not assumed to be a complete, exact paper-run archive.

### Source FIX

[Presence-scoring test data](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/metrics/eval_metric_test_presence.csv)

Seven rows inspected, including prediction, answer and category columns. The metrics file also contains commented test calls. Test data exist; no executed assertion suite or published scorer error rate was established.

### Source WEB

[Official project website](https://design-qa.github.io/)

Landing-page text was readable on 2026-10-06. The web extractor did not expose a leaderboard table or its rules. This access limit is not proof that the leaderboard is absent or broken.

### Source M1

[Original ChatGPT reviewer 1](../../reviews/chatgpt_reviewer1/DesignQA.md)

Historical full MESA comparison source. Used its descriptive fields, relevant Sections 6–12, conclusions and gap register. These are reviewer judgments, not independent primary benchmark evidence.

### Source M2

[Original Claude reviewer 2](../../reviews/claude_reviewer2/DesignQA.md)

Historical full MESA comparison source, dated 2026-06-28. Its judgments sometimes differ from M1; these differences are preserved below.

### Source ME

[Original Gemini supervising editor](../../reviews/gemini_supervising_editor/DesignQA.md)

Historical reconciled MESA comparison source, dated 2026-06-28. It synthesizes the other reviews, so agreement with it is not a third independent validation.

## Completed questionnaire

One selected choice per question. Comments are detailed here because this is a worked reviewer example. They are not a new requirement for other respondents.

### Description

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q1. Are the benchmark version, set of test problems and method for calculating scores identified? | **Partly** | The paper identifies the original DesignQA benchmark and its question families, and the public repository identifies the scoring files. This example pins repository commit dd909455afb9. However, the published paper results are not tied here to an exact code and data snapshot, and there are no release tags in the inspected repository metadata. A reviewer can pin today’s code by commit even without a named release. That does not establish that this commit exactly reproduces the paper. | P §§3–4; R; C1; TREE |
| Q2. Are the ability being tested, the intended AI systems and the intended uses described? | **Yes** | The stated target is AI understanding and application of engineering requirements, using both text and images. The paper presents the benchmark as a research tool for identifying strengths and weaknesses in such systems. It does not claim to measure general intelligence. These purposes are described clearly enough for this descriptive item; whether results support use beyond these problems is considered separately in Q9 and Q20. | P §§1, 3, 6 |
| Q3. Are the test problems, the information provided and the required answers or actions described? | **Yes** | The paper describes 1,451 question-answer pairs in six groups: Retrieval 1,192, Compilation 30, Definition 31, Presence 62, Dimension 120 and Functional Performance 16. It describes the supplied rules, vehicle images or drawings, expected text or yes/no answers, and explanations where requested. These are paper counts, not counts independently verified across the entire repository. The released prediction sample inspected for Q22 has fewer retrieval rows. | P §3.1; OUT |
| Q4. Are the instructions, resources and limits for taking the test described? | **Partly** | Prompts, model versions, model settings and document-delivery conditions are described. Some systems receive the whole rulebook; others receive selected passages found by retrieval software. This distinction matters because the same AI can score differently with different information. The inspected sources do not provide a fully frozen environment and a complete run manifest linking every paper result to its exact code, settings and inputs. The basic procedure is visible, but exact repetition remains incomplete. | P §§3.1, 4.1.2–4.1.3, Appendix A; ENV |
| Q5. Is it described how answers or actions become scores and how results are presented? | **Yes** | Scoring methods and subset results are described. Some scores measure overlap between the produced answer and the reference; yes/no tasks use correctness, while explanations also receive text-similarity scores. The repository driver additionally prints an overall score by adding the six subset scores and dividing by six. That calculation is transparent, but its interpretation and behavior with omitted subsets need the cautions in Q11. This Yes means the scoring is described, not that every scoring choice is valid. | P §3.2; C1; C2 |
### Purpose and development

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q6. Is it explained why the test problems measure the ability the benchmark claims to test? | **Yes** | The paper connects three stages of engineering work to its questions: finding rules, understanding terms and drawings, and applying rules to designs. For example, identifying a relevant requirement is a prerequisite for judging whether a drawing meets it. This is an explicit rationale, not just a difficult collection of questions. It explains the intended link; it does not by itself prove that all scores isolate engineering ability. | P §3.1 |
| Q7. Are the origins and choice of test problems justified for the benchmark’s intended use? | **Partly** | The source materials are justified by a real student engineering competition and actual vehicle designs and test data. Authors include domain practitioners, industry and academic contributors. This supports relevance for Formula SAE-style work. The sample is nevertheless constrained by available material, uses one rulebook and has highly uneven group sizes. It is not a representative survey of engineering-documentation work across industries, nor is a statistical sample-size justification established for close model comparisons. | P §3.1 and Limitations |
| Q8. Were the test problems and the answers used to mark them checked for errors during development? | **Partly** | The paper reports two additional reviewers for manually generated questions, except derivative questions and Rule Compliance explanations. For the explanations, it reports a limited check that they support the yes/no answer, rather than extensive review. This is meaningful quality control, but it is not the same as every item and explanation being independently verified twice. No numerical estimate of reviewer agreement or remaining answer errors is established in the inspected sources. | P §3.1, especially Rule Compliance |
| Q9. Is there evidence that the test problems cover the relevant parts of the ability being claimed? | **Partly** | The six groups cover plausible parts of finding, interpreting and applying requirements. The paper’s expert design argument supports this limited content coverage. It also explicitly acknowledges only one rulebook and six task types. There is no demonstrated coverage of all engineering standards, design activities or work settings. The positive answer is therefore partial for the broad claim of engineering-documentation understanding, rather than an objection that every narrow benchmark must test everything. | P §3.1 and Limitations |
### Scoring and comparisons

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q10. Is there evidence that the way points are awarded reflects the ability the benchmark is meant to measure? | **Partly** | The metrics have an understandable connection to the required responses, especially correct yes/no judgments. However, the paper documents answers losing credit for missing commas and for including valid child rules absent from the reference. The inspected compilation scorer splits predictions at comma-plus-space, which explains why formatting can affect credit. Similar-looking explanations need not be correct engineering explanations. I would use these scores as indicators requiring interpretation, not as a complete measure of understanding. | P §3.2 and Limitations; C2 eval_compilation_qa |
| Q11. Is there evidence supporting how scores are combined and what any separate scores are said to measure? | **Partly** | Task groups have a sensible designed meaning, but their scores have not been shown here to measure separate underlying abilities or to form one validated overall ability. The driver gives each of six groups equal weight despite different sizes and metrics. It also accepts missing subset paths while still dividing by six: if only one supplied subset scores 1, the printed overall value is 1/6, not that subset’s score. This is a code-derived illustration, not a rerun of model results. Overall scores therefore require the full, same subset coverage and an explicit justification for combining them. | P §3.1; C1 main; M1 §10.2.1 |
| Q12. Was the marking process tested to see whether it awards the right scores consistently? | **Partly** | The paper identifies scoring failure cases, and the repository contains small scoring test CSVs and commented manual test calls. That is limited checking, so it would be inaccurate to say no scoring checks or test data exist. However, I did not establish an executed assertion suite, an error-rate study or comparison of explanation scores with expert correctness judgments. Repeating a calculation reliably does not show it gives the right mark. This answer recognizes informal checking without treating it as a completed validation study. | P Limitations; C2; FIX |
| Q13. Are the comparison points used to explain the scores justified for the claims being made? | **Partly** | The paper supplies random-answer baselines and a named group of contemporary AI models, which help interpret performance within the study. It does not report a human-engineer performance baseline. Thus the scores can describe differences from simple guessing or the tested systems, but cannot establish human-level engineering performance. Different document access conditions further limit comparisons. The absence of a human baseline is especially important for a human-comparison claim, not automatically fatal to research diagnosis. | P §§4.1.1–4.1.3; M1/M2/ME §8.1.2 |
### Consistency of results

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q14. Was it tested how much the same AI system’s score changes when the benchmark is run more than once? | **Partly** | The paper tests LLaVA with five separately generated sets of relevant rule passages and reports variation across them. This provides some repeated-evaluation information. The supplied passages change, so it is not a clean estimate of randomness under otherwise identical conditions. Comparable repeated-run results are not established for the main model cohort. The limited diagnostic should not be treated as a general demonstration that all benchmark scores are stable. | P §5 Impact of RAG System, Table 3, Appendix B |
| Q15. Was it tested how much scores change when instructions, presentation or the testing setup change? | **Partly** | The paper compares whole-rulebook and retrieved-passage setups, direct dimensions and scale bars, and images with versus without highlighting and accompanying component names. These are actual tests of changes in supplied information and presentation. They do not form a comprehensive study of prompt rewording, response formats, software versions or all model settings. Partly captures measured sensitivity with limited coverage, rather than treating the issue as wholly untested. | P §5, including Tables 3–5 and Effect of Additional Context |
| Q16. Are estimates of how much scores could vary provided in enough detail to support the comparisons or decisions being made? | **No** | For the main comparisons, the reported information is not sufficient to judge the dependability of close score differences. The five-context LLaVA diagnostic has a measure of spread, but the principal model comparisons do not provide comparable uncertainty intervals or repeated-run estimates. A single correct answer changes the 16-item Functional Performance accuracy by 6.25 percentage points. This is a resolution calculation, not proof that any observed difference is statistically insignificant. Uncertainty must be estimated for the relevant score and comparison. | P §§4–5 and Limitations; M1/M2/ME §9.2.2 |
### Meaning and fairness

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q17. Were ways of earning points without using the ability being tested investigated? | **Partly** | The paper discusses score effects from formatting, explanation wording, retrieval quality and component familiarity, so irrelevant influences are not wholly ignored. It does not provide a comprehensive test of strategies that earn credit without engineering understanding. All scale-bar drawings in the described Dimension construction are compliant: always saying yes would earn the yes/no credit on that portion. This is an inferred shortcut from the item design, not evidence that the evaluated models used it, and it says nothing about their explanation scores. | P §§3.1.4, 5 and Limitations |
| Q18. Was the risk that AI systems had already seen the test problems or answers assessed and addressed? | **Partly** | The authors discuss the novelty of their vehicle imagery and possible prior exposure to similar component images. New source images can reduce one kind of exposure risk, but this is not a direct audit of each model’s training data. The rulebook and released questions are public, and no systematic overlap study or protected evaluation set is established in the inspected material. Deliberately supplying the rulebook during the test is part of the task, not itself answer leakage. Exposure remains a risk, not a demonstrated explanation of the scores. | P §§1, 3.1, 5; TREE |
| Q19. Are the rules on training specifically for this test and repeatedly submitting results justified for the intended use? | **Not sure** | The README describes submitting results and evaluation code for manual verification, but I did not find a clear policy about training on the questions, repeated submissions or separating such results from untuned systems. The paper recommends training on Retrieval questions as one possible improvement path. That creates a comparison concern, but permitted adaptation is not inherently improper: it depends on the claim. With the live leaderboard rules not exposed by the available extractor, I cannot judge the justification of all applicable rules. | P §5 Future Work; R Leaderboard; WEB |
| Q20. Is there evidence for any claim that the scores show how well an AI system will perform beyond the problems in this test? | **Not sure** | The paper explicitly says it is unknown how results would change with a different technical document. Real vehicle material and realistic questions support relevance, but do not demonstrate prediction of performance on other standards or real engineering projects. No external performance study is established in the inspected sources. For a claim of general engineering competence the evidence is insufficient; this is not proof that scores fail to predict such performance. If the intended claim were strictly confined to these exact problems, this item could instead be Not applicable. | P Limitations; M1/M2/ME §10.4 |
| Q21. Is there evidence that comparisons are fair across the AI systems and situations the benchmark is meant to cover? | **Partly** | Named models, prompts and context-delivery labels make some comparisons interpretable. The paper also investigates retrieval effects. However, whole-rulebook and retrieved-passage systems are evaluated with different information; API restrictions and cost constraints affect which conditions were tested. Such comparisons describe the combined model-and-setup performance. They do not cleanly isolate the model alone. Fair comparisons are supported only within suitably matched conditions; the sources do not establish equivalent measurement across all systems and contexts. | P §§4.1–5 |
### Use and reporting

| Question | Answer | Comments | Sources |
| --- | --- | --- | --- |
| Q22. Are the test materials and methods available in enough detail for someone else to repeat the evaluation or examine how it was done? | **Partly** | Public questions, instructions, scorer code and some prediction files support inspection and partial reproduction. The inspected LLaVA retrieval CSV contains 1,190 predictions, compared with 1,192 retrieval questions in the paper; its completeness and exact association with a reported run remain unresolved. Requirements are unpinned, and I did not reconstruct the historical APIs or reproduce the paper’s full results. The correct distinction is partial auditability versus a complete reproducible archive, not public code versus no access. | R; C1; C2; ENV; OUT; TREE |
| Q23. Are the rules for accessing and reusing the benchmark, and the protections needed for responsible use, stated? | **Partly** | The repository explains how to obtain materials and run scoring, and the paper states important limits on interpretation. I found no license file in the pinned tree and no complete responsible-use policy in the inspected sources. Thus access instructions exist, while reuse permissions and safeguards are incomplete in this source set. This does not establish that reuse is prohibited, and it is not a legal opinion. A separate repository or maintainer policy could change the finding. | R; TREE; P Limitations |
| Q24. Are changes to the benchmark recorded, including how they affect comparisons between old and new scores? | **Partly** | Git history supplies identifiable commits, so this example can pin the inspected code. The tags and releases endpoints were empty, and no changelog explaining effects on scores was found in the inspected tree. A commit history alone does not establish that scores from different states are equivalent or explain which old results need recomputation. I therefore record partial change traceability, rather than either full version governance or a total absence of version information. | TREE; C1 |
| Q25. Do the published claims stay within what the evidence supports? | **Partly** | The paper is candid about one rulebook, limited task types, metric problems and uncertain generalization. That is a strength. Broader language about engineering-documentation understanding can still be overread, and precise-looking rankings are not accompanied by sufficient uncertainty for fine distinctions. I could inspect the website’s landing text but not a live leaderboard table, so this answer does not certify all public claims. Supported interpretation: diagnosis of performance on these tasks under stated conditions, not proof of broad engineering competence. | P §§5–6 and Limitations; WEB; M1/M2/ME §12 |

## Interpretation

The comments preserve the original reviews’ central diagnosis: realistic, well-motivated tasks and useful research materials, with incomplete support for precise rankings or broad engineering competence. Primary-source checks also require corrections to several original statements. Retained as a checked teaching example, not as proof that 25 choices replace a full MESA review.

No overall numerical score or EFPA-rating conversion is calculated. A Yes to a procedural question means the procedure is described or performed, not that its results prove quality. Not sure denotes unresolved support, not a demonstrated defect.
