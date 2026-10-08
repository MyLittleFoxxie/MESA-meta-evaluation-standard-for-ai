# Guide to MESA-25

Draft 0.2, 2026-10-01. The [questionnaire](questionnaire.md) contains direct questions, short explanations, real examples and answer spaces. This guide adds interpretation rules.

## Answers

Choose one answer for each of the 25 questions. Q1–Q5 ask whether basic descriptions are provided. Q6–Q25 ask about methods and claims. An optional Comments field is available for each question. No written explanations, evidence notes, citations or final review summary are required.

| Answer | Meaning |
| --- | --- |
| Yes | The question is satisfied. |
| Partly | Some parts are satisfied, but not all. |
| No | The question is not satisfied. |
| Not sure | There is not enough information to decide. |
| Not applicable | The issue does not apply to this benchmark. |

A missing description can justify No when the question asks whether that description is provided. When it is unclear whether a procedure actually happened, Not sure is appropriate. Missing information alone does not prove that a procedure failed or never happened.

The answer follows the question: Yes to “Was it tested?” means a test was performed; it does not mean the result was favourable. Yes to “Is there evidence supporting…?” means there is supporting evidence. Respondents select an answer without supplying that evidence in this survey.

This is a checklist, not the full MESA review. The choices are not EFPA ratings and have no numerical conversion or total score. The questionnaire has not been validated.

## Meanings by domain

### Description

| Question | Meaning |
| --- | --- |
| Q1 | A version is a particular release of the benchmark. A set of test problems may be a named part of a larger collection, such as a public test set. The scoring method includes the rules and any software used to assign points. |
| Q2 | An ability is something an AI system can do, such as solving maths problems. An intended use is a decision the scores are meant to inform, such as choosing an AI system for a particular job. |
| Q3 | A problem may ask for a written answer, a completed picture, computer code or an action. Provided information may include instructions, documents or images. |
| Q4 | Test conditions include access to tools or documents, time limits, the number of attempts and any human help. Settings that affect how the AI generates answers also belong here. |
| Q5 | Scoring may count correct answers, award partial credit or use human or AI judgments. Results may show an overall score, scores for different types of problems, comparisons with other systems and an estimate of how much scores might vary. |

### Purpose and development

| Question | Meaning |
| --- | --- |
| Q6 | The explanation connects what the AI must do in the problems to the claimed ability. A hard test is not necessarily a test of the intended ability. |
| Q7 | This includes where the problems came from and why their number, topics and difficulty levels suit the intended use. Expert involvement can help explain these choices. |
| Q8 | Answers used for marking are often called reference answers or answer keys. Development checks can include expert review, trial runs and correction of mistakes. |
| Q9 | Coverage means including the kinds of problems, skills and difficulty levels needed for the claim. Success on one narrow skill does not establish a broader ability. |

### Scoring and comparisons

| Question | Meaning |
| --- | --- |
| Q10 | The scoring rule determines what earns credit. It can distort results if, for example, a correct answer loses points for harmless wording or punctuation when those details are not part of the ability being tested. |
| Q11 | A combined score brings results from several problems together; weighting gives some results more influence. Separate scores, sometimes called subscores, cover different parts of a test. Their labels do not by themselves prove that they measure distinct abilities. |
| Q12 | Marking may use software, people or another AI system. Accuracy means assigning appropriate scores; consistency means agreeing on comparable answers. Software that always repeats the same mistake is consistent but not accurate. |
| Q13 | Comparison points may be human performance, other AI systems, random guessing, earlier results or a pass mark. Their test conditions and relevance affect what a comparison means. |

### Consistency of results

| Question | Meaning |
| --- | --- |
| Q14 | Score stability means how similar scores remain across repeated tests. Repeats under the same conditions help separate random variation from changes caused by different test conditions. |
| Q15 | This is called score sensitivity. Instructions given to an AI are often called prompts. Presentation includes wording and layout; the setup includes tools, software versions and the environment where the test runs. |
| Q16 | Score uncertainty is the uncertainty in an estimate of performance, not the AI’s confidence in an answer. It can arise from which problems were selected or from variation between runs. A reported range with an explanation of how it was calculated helps judge whether a score difference is dependable. |

### Meaning and fairness

| Question | Meaning |
| --- | --- |
| Q17 | These are called shortcuts. They include guessing from accidental clues or exploiting the marking rules. A shortcut matters when it raises the score without demonstrating the claimed ability. |
| Q18 | Prior exposure can let a system recall answers instead of solving new problems. Public availability alone does not prove exposure. Using documents deliberately provided during the test is different from having seen the test answers beforehand. |
| Q19 | Test-specific tuning means changing an AI system or its instructions to improve on this particular test. Repeated submissions may reveal which changes earn more points. Whether this is acceptable depends on what the benchmark claims to measure and what competing systems are allowed to do. |
| Q20 | Such claims may concern other tests, related abilities or real work. Realistic-looking problems alone do not show that test scores predict success elsewhere. This question may not apply if the claim is limited to the tested problems. |
| Q21 | Relevant differences include access to tools or information, languages, types of input and available computing resources. Different conditions can be justified, but their effects on comparisons need evidence. A score difference alone does not prove unfairness. |

### Use and reporting

| Question | Meaning |
| --- | --- |
| Q22 | Materials include problems, instructions, answers used for marking, software, settings and recorded results. Restricted materials may be available through a controlled review process. Publishing materials is different from showing that someone has successfully repeated the evaluation. |
| Q23 | These can include permission to reuse material, required expertise, privacy protections and warnings about sensitive content. The relevant protections depend on the benchmark and its intended use. |
| Q24 | Changes to problems, answer keys, marking software or testing services can change scores. Version names and a record of changes help identify what was tested. A benchmark that stays fixed still needs an identifiable version. |
| Q25 | Claims may appear in papers, websites, rankings or headlines. Their scope should match the tested problems, conditions and limits of the results, including uncertainty and missing evidence. |

## Limits

Not applicable differs from Not sure: an irrelevant issue is different from an unanswered one. A benchmark without separate or combined scores may make Q11 inapplicable. The absence of an AI judge does not make Q12 inapplicable if software or people still mark the answers.

The full MESA template remains available for a detailed review. Its evidence notes and closing summary are not requirements of this checklist.
