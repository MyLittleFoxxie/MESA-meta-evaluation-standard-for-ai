# MESA-25: a short benchmark review

Draft 0.2 · 2026-10-01 · Experimental, not validated

**25 questions: 5 descriptive and 20 evaluative, grouped into six domains.** The wording follows the direct question style of the final Q-SSP checklist. Explanations and answer definitions are in the [guide](guide.md).

Choose one answer per question: **Yes / Partly / No / Not sure / Not applicable**. Comments are optional. No written explanation, evidence, citations or closing summary is required. Q1–Q5 concern whether the basic description is provided; Q6–Q25 concern the benchmark’s methods and claims.

**Yes:** the question is satisfied. **Partly:** only some parts are satisfied. **No:** the question is not satisfied. **Not sure:** there is not enough information to decide. **Not applicable:** the issue does not apply to this benchmark. Missing information alone is not a No. For questions about whether a check was performed, Yes means it was performed, not that its result was favourable. There is no total score.

## Before you begin

**What this questionnaire reviews.** It reviews an AI benchmark: a test made up of problems, instructions and scoring rules used to assess AI systems. It asks whether the test and the claims made from its scores are well supported.

**AI system or model.** The software taking the test. Depending on the benchmark, this may be a model on its own or a model using tools such as a web browser.

**Test problem or task.** Something the AI is asked to solve or do, such as answering a question or writing code. Here, “task” does not mean the reviewer’s work.

**Score and ability.** A score is a recorded test result, such as the percentage of correct answers. An ability is what the AI can do. A high score alone does not prove a broad ability.

**Evidence and intended use.** Evidence is information that supports a judgment, such as study results, documented methods or inspected software. The intended use is the decision the scores are meant to support. Missing evidence means the issue is unresolved; it does not by itself show failure.

**The examples.** DesignQA tests whether AI can understand engineering rules and vehicle drawings. The examples use its 2024 paper and June 2026 MESA review. Each illustrates part of a question, not a complete answer or rating. A review gap describes what was missing then, not a new check of the benchmark.

[Example sources and qualifications](example-sources.md).

## Description

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q1 | Are the benchmark version, set of test problems and method for calculating scores identified? | A version is a particular release of the benchmark. A set of test problems may be a named part of a larger collection, such as a public test set. The scoring method includes the rules and any software used to assign points. | DesignQA: 2024 paper, public test questions and software that calculates scores. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q2 | Are the ability being tested, the intended AI systems and the intended uses described? | An ability is something an AI system can do, such as solving maths problems. An intended use is a decision the scores are meant to inform, such as choosing an AI system for a particular job. | DesignQA tests AI understanding of engineering rules and drawings. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q3 | Are the test problems, the information provided and the required answers or actions described? | A problem may ask for a written answer, a completed picture, computer code or an action. Provided information may include instructions, documents or images. | DesignQA asks whether a pictured vehicle part meets a rule. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q4 | Are the instructions, resources and limits for taking the test described? | Test conditions include access to tools or documents, time limits, the number of attempts and any human help. Settings that affect how the AI generates answers also belong here. | DesignQA tests AI systems without showing them worked examples. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q5 | Is it described how answers or actions become scores and how results are presented? | Scoring may count correct answers, award partial credit or use human or AI judgments. Results may show an overall score, scores for different types of problems, comparisons with other systems and an estimate of how much scores might vary. | DesignQA scores yes/no answers as correct or incorrect. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

## Purpose and development

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q6 | Is it explained why the test problems measure the ability the benchmark claims to test? | The explanation connects what the AI must do in the problems to the claimed ability. A hard test is not necessarily a test of the intended ability. | DesignQA tests applying engineering rules by asking whether vehicle designs meet them. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q7 | Are the origins and choice of test problems justified for the benchmark’s intended use? | This includes where the problems came from and why their number, topics and difficulty levels suit the intended use. Expert involvement can help explain these choices. | DesignQA uses real racing rules and student-built vehicle designs. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q8 | Were the test problems and the answers used to mark them checked for errors during development? | Answers used for marking are often called reference answers or answer keys. Development checks can include expert review, trial runs and correction of mistakes. | DesignQA used two extra reviewers for human-written questions, with some exceptions. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q9 | Is there evidence that the test problems cover the relevant parts of the ability being claimed? | Coverage means including the kinds of problems, skills and difficulty levels needed for the claim. Success on one narrow skill does not establish a broader ability. | DesignQA covers six kinds of problems from one racing rulebook. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

## Scoring and comparisons

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q10 | Is there evidence that the way points are awarded reflects the ability the benchmark is meant to measure? | The scoring rule determines what earns credit. It can distort results if, for example, a correct answer loses points for harmless wording or punctuation when those details are not part of the ability being tested. | DesignQA answers can lose points for missing commas. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q11 | Is there evidence supporting how scores are combined and what any separate scores are said to measure? | A combined score brings results from several problems together; weighting gives some results more influence. Separate scores, sometimes called subscores, cover different parts of a test. Their labels do not by themselves prove that they measure distinct abilities. | DesignQA review: relationships between scores for its six types of problems were untested. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q12 | Was the marking process tested to see whether it awards the right scores consistently? | Marking may use software, people or another AI system. Accuracy means assigning appropriate scores; consistency means agreeing on comparable answers. Software that always repeats the same mistake is consistent but not accurate. | DesignQA review: software-generated explanation scores lacked checks against human marking. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q13 | Are the comparison points used to explain the scores justified for the claims being made? | Comparison points may be human performance, other AI systems, random guessing, earlier results or a pass mark. Their test conditions and relevance affect what a comparison means. | DesignQA review: no human scores were available for comparison. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

## Consistency of results

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q14 | Was it tested how much the same AI system’s score changes when the benchmark is run more than once? | Score stability means how similar scores remain across repeated tests. Repeats under the same conditions help separate random variation from changes caused by different test conditions. | DesignQA tested one AI model five times, changing the supplied rule passages. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q15 | Was it tested how much scores change when instructions, presentation or the testing setup change? | This is called score sensitivity. Instructions given to an AI are often called prompts. Presentation includes wording and layout; the setup includes tools, software versions and the environment where the test runs. | DesignQA compared results with and without added image labels. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q16 | Are estimates of how much scores could vary provided in enough detail to support the comparisons or decisions being made? | Score uncertainty is the uncertainty in an estimate of performance, not the AI’s confidence in an answer. It can arise from which problems were selected or from variation between runs. A reported range with an explanation of how it was calculated helps judge whether a score difference is dependable. | DesignQA review: main results lacked estimates of how much the scores could vary. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

## Meaning and fairness

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q17 | Were ways of earning points without using the ability being tested investigated? | These are called shortcuts. They include guessing from accidental clues or exploiting the marking rules. A shortcut matters when it raises the score without demonstrating the claimed ability. | DesignQA: always answering “yes” works for drawings with scale bars (lines showing distance). | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q18 | Was the risk that AI systems had already seen the test problems or answers assessed and addressed? | Prior exposure can let a system recall answers instead of solving new problems. Public availability alone does not prove exposure. Using documents deliberately provided during the test is different from having seen the test answers beforehand. | DesignQA used new vehicle images, but publicly available competition rules. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q19 | Are the rules on training specifically for this test and repeatedly submitting results justified for the intended use? | Test-specific tuning means changing an AI system or its instructions to improve on this particular test. Repeated submissions may reveal which changes earn more points. Whether this is acceptable depends on what the benchmark claims to measure and what competing systems are allowed to do. | DesignQA’s paper suggests training AI on its questions about finding rules. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q20 | Is there evidence for any claim that the scores show how well an AI system will perform beyond the problems in this test? | Such claims may concern other tests, related abilities or real work. Realistic-looking problems alone do not show that test scores predict success elsewhere. This question may not apply if the claim is limited to the tested problems. | DesignQA’s paper says performance on other rulebooks remains unknown. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q21 | Is there evidence that comparisons are fair across the AI systems and situations the benchmark is meant to cover? | Relevant differences include access to tools or information, languages, types of input and available computing resources. Different conditions can be justified, but their effects on comparisons need evidence. A score difference alone does not prove unfairness. | DesignQA’s AI systems received either the whole rulebook or selected passages. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

## Use and reporting

| No. | Question | Meaning | Example | Answer | Comments (optional) |
| --- | --- | --- | --- | --- | --- |
| Q22 | Are the test materials and methods available in enough detail for someone else to repeat the evaluation or examine how it was done? | Materials include problems, instructions, answers used for marking, software, settings and recorded results. Restricted materials may be available through a controlled review process. Publishing materials is different from showing that someone has successfully repeated the evaluation. | DesignQA provides public questions and software that calculates scores. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q23 | Are the rules for accessing and reusing the benchmark, and the protections needed for responsible use, stated? | These can include permission to reuse material, required expertise, privacy protections and warnings about sensitive content. The relevant protections depend on the benchmark and its intended use. | DesignQA’s June 2026 review found no license stating permission to reuse the shared materials. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q24 | Are changes to the benchmark recorded, including how they affect comparisons between old and new scores? | Changes to problems, answer keys, marking software or testing services can change scores. Version names and a record of changes help identify what was tested. A benchmark that stays fixed still needs an identifiable version. | DesignQA’s June 2026 review found no formally labeled releases or record of changes. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |
| Q25 | Do the published claims stay within what the evidence supports? | Claims may appear in papers, websites, rankings or headlines. Their scope should match the tested problems, conditions and limits of the results, including uncertainty and missing evidence. | DesignQA’s paper acknowledges that its six kinds of problems omit other engineering tasks. | ☐ Yes · ☐ Partly · ☐ No · ☐ Not sure · ☐ Not applicable | |

[Guide](guide.md) · [Changes and limits](README.md) · [Source mapping](coverage-map.md) · [Checks](checks.md)
