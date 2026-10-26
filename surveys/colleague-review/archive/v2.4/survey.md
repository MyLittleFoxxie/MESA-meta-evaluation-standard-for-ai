# MESA: Adapting and Testing an EFPA-Based Framework for AI Benchmark Review

Guided colleague survey

## 1. Introduction

This survey introduces MESA, the Meta-Evaluation Standard for AI Benchmarks. MESA helps people review how an AI test is designed and what its scores can tell us. You will first describe your familiarity with a few relevant ideas, then read an answered example about Humanity’s Last Exam. After that, you will make your own judgments about ARC-AGI-2 and DesignQA.

You review the tests rather than solve their problems. Read the supplied passages and make your own judgments. Complete 25 questions each for ARC-AGI-2 and DesignQA. Comments are optional; evidence notes and citations are not required.

## How to choose an answer

Choose one option for each question.

- **Yes:** Information supports the whole condition.

- **Partly:** Supports some parts but not all.

- **No:** Information shows the condition is not met.

- **Not sure:** Information is missing, unclear, or insufficient.

- **Not applicable:** The issue does not apply.

When information is missing, choose Not sure rather than No.

For a question asking whether checking or testing occurred, Yes means the stated checks occurred for all parts of the question, not that results were favourable or every error was eliminated. Partly means that only some of those checks or parts are supported. Describe limits in coverage in an optional comment; do not lower an answer solely because checking found errors or disagreement.

Each answer records your judgment about one part of the benchmark. The answers are not added together to produce a total quality score.

No name or email is requested. Please avoid identifying details in comments. The online form sends familiarity ratings, both benchmark evaluations, feedback, survey identifier and fingerprint, and completion time to the organizer through FormSubmit; the external service may process technical request information.

The online form supplies definitions beside relevant words. In this printable companion, the same definitions appear in a reference section at the end.

## 2. Your familiarity

These are your own descriptions, not a knowledge test. Choose one response to each question.

**How familiar are you with AI?**

Think about your experience using or learning about AI, such as a chatbot. This is your own description, not a knowledge test.

- ☐ 1 — New to me: I have little or no experience with AI.
- ☐ 2 — A little familiar: I have heard about or tried AI.
- ☐ 3 — Somewhat familiar: I use AI sometimes and understand its basic purpose.
- ☐ 4 — Familiar: I use AI regularly and understand some of its limits.
- ☐ 5 — Very familiar: I can explain how AI is used and discuss its limits confidently.

**How familiar are you with AI benchmarks?**

An AI benchmark is a test used to assess an AI system. Think about how familiar this idea was before reading this survey.

- ☐ 1 — New to me: I had not heard of AI benchmarks.
- ☐ 2 — A little familiar: I had heard the term but could not explain it.
- ☐ 3 — Somewhat familiar: I knew that benchmarks test AI and produce scores.
- ☐ 4 — Familiar: I knew how some benchmark problems and scores are used.
- ☐ 5 — Very familiar: I could explain benchmarks and discuss what their scores can and cannot show.

**How confident are you about interpreting AI test scores?**

Interpreting a score means deciding what a result tells us, such as whether two AI systems can be compared fairly. Choose how confident you feel now.

- ☐ 1 — Not confident: I would need help understanding a test score.
- ☐ 2 — Slightly confident: I understand a simple score but need help comparing results.
- ☐ 3 — Moderately confident: I can explain a basic score and recognize some limits.
- ☐ 4 — Confident: I can compare results and explain important limits.
- ☐ 5 — Very confident: I can explain why a comparison is fair or uncertain and what evidence is needed.

## 3. HLE — answered example

This completed example shows one reviewer’s judgments based on the supplied reading and inspected sources. It is a teaching example, not a correct-answer key or a validated assessment of HLE.

Imagine a very difficult exam assembled by specialists from many subjects. The AI must select an answer or give a short answer; some questions also include an image. A separate AI marks the response against a supplied answer. HLE aims to measure advanced academic knowledge and reasoning. You do not need to know the subject answers to evaluate how this test is built, marked and interpreted.

**Which test this survey covers:** The original 2,500-question HLE described in the supplied paper, with the simple public evaluation code inspected on 7 October 2026. This survey does not cover HLE-Rolling, HLE-Diamond or their evaluations with extra tools.

**How to interpret its scores:** Using scores to compare AI systems on difficult academic questions, and considering claims about academic expertise beyond the exact questions.

### Reading passage

![Humanity’s Last Exam logo](images/hle-logo.svg)

#### What the AI is asked to do

Humanity’s Last Exam, or HLE, aims to assess advanced academic knowledge and reasoning in AI systems that handle text or text and images. This survey focuses on **the original HLE, which contains 2,500 difficult questions**, rather than the separate HLE-Rolling and HLE-Diamond versions. About **24% of its questions are multiple-choice**, while the rest require short answers, and about **14% include an image**. A published biology example asks for a number about the anatomy of a hummingbird bone. You do not need to solve that problem to complete this survey; it illustrates the kind of specialist question the AI receives. Across these formats, HLE asks for specific answers rather than the completion of an open-ended research project. Sources: [HP](#source-HP) [HW](#source-HW).

**A real HLE image question**

![Official HLE classics example: a drawing of an ancient tombstone inscription, with Latin lettering above a line of Palmyrene script.](images/hle-classics.png)

In this example, the AI receives an image of an ancient inscription and is asked to translate the Palmyrene writing along the bottom. The image provides information needed to answer the question; you do not need to translate it for this survey.

Official classics example from the Humanity’s Last Exam website. The question is summarized here. [Source figure](https://lastexam.ai/_next/static/media/classics.81111c73.png).

#### How the questions were chosen and checked

Experts from many institutions contributed questions covering a range of subjects, with particular emphasis on mathematics. Before expert review, questions that selected AI models could already answer were screened out, so the resulting set was **deliberately chosen to be difficult**, rather than randomly drawn from everyday academic work. HLE’s creators describe their development process in a research paper, which reports expert review and organizer approval, followed by two further checks of 200 questions each. After the second check, the authors estimated an **expert-disagreement rate of 15.4%**. That figure concerns disagreements about questions or answers; it should not be read as the percentage confirmed to be wrong. Because the test requires specific answers, it also leaves creative work and open-ended research outside its answer format. Sources: [HP](#source-HP).

#### Instructions and marking

HLE’s public evaluation software gives the AI each question, includes an image when needed, and asks it to return an explanation, a final answer and a percentage stating its confidence. The instructions for that software describe a default “temperature” of zero, a setting intended to reduce randomness, but the line that sends this setting is **disabled in the inspected code**. Once a response is produced, a separate **AI judge compares the final answer with the supplied reference answer**, accepting different wording when the meaning is the same. Because the judge is instructed to compare answers rather than solve the problem independently, agreement does not establish that the reference itself is correct. The judging code is public, but the inspected sources contain no full study comparing its marks with expert marks. The expert reviews of the questions described earlier therefore do not, by themselves, establish that the automatic marking is accurate. Sources: [HM](#source-HM) [HR](#source-HR) [HJ](#source-HJ) [HP](#source-HP).

**How an HLE answer is marked**

1. **Receive a question** — Text, sometimes with an image; choose an option or give a short answer.
2. **Give a response** — The AI provides an explanation, a final answer and its stated confidence.
3. **Compare with the reference** — A separate AI judge checks the final answer against the supplied answer. Equivalent meanings can count.

Process diagram based on the simple evaluation code. The judge is not asked to solve the question independently.

#### What the reported numbers mean

HLE reports **accuracy as the percentage of answers marked correct**, with each question counting equally. As a result, the mix of subjects affects the total score. The paper also reports results by subject, although the inspected material does not establish that these are separate measures of distinct abilities. Alongside accuracy, the public scoring software calculates an **approximate 95% confidence range** using the number of questions and the fraction marked correct. This range describes score uncertainty under the calculation’s assumptions; it does not measure the effects of repeating the AI run or changing the judge. A separate calculation compares the AI’s stated confidence with how often its answers are correct, so **confidence in an answer and uncertainty in a test score refer to different things**. Sources: [HP](#source-HP) [HJ](#source-HJ).

**Three different numbers in the results**

1. **Accuracy** — What percentage of answers were marked correct?
2. **Score range** — How uncertain is that percentage under the calculation used? This is not a repeated-run test.
3. **Confidence check** — Does how confident the AI says it is match how often it is correct?

These are separate summaries of the answers. None substitutes for measuring changes across repeated runs.

#### Comparisons and repeated testing

To put results in context, the paper compares named AI models and reports scores for both the full question set and text-only questions. Although experts helped create the questions, this packet contains **no matched group of people taking the whole exam under the AI testing conditions**. The paper also notes that an AI can answer differently on different attempts, but the inspected sources do not provide a repeated-run study covering the main comparisons. Nor do they provide a systematic study of reworded instructions or changes to the judging AI. Using a fixed setting or a standard instruction therefore does not, on its own, establish how stable the reported scores are. Sources: [HP](#source-HP) [HM](#source-HM) [HJ](#source-HJ).

#### Prior exposure and ways to earn points

To reduce easy ways of gaining points, contributors were asked to avoid questions answerable by a simple lookup and could revise questions when an AI guessed correctly through faulty reasoning. Multiple-choice questions still allow guessing, however, and the supplied material does not measure every possible way of earning points without the intended knowledge or reasoning. The authors also retain a **private test set** to help assess whether improvements are specific to the public questions. For the public data, a distinctive text marker helps people identify material to exclude from future AI training, while the instructions warn against training on the test. These precautions do not establish what a particular AI has already seen. The packet also lacks a complete original-HLE policy covering repeated submissions, access to feedback and the reporting of systems trained specifically on the test. Sources: [HP](#source-HP) [HR](#source-HR).

#### Access, fair comparisons and updates

Fair comparisons depend partly on which questions each system receives. Systems that use images and those that only use text do not necessarily answer the same set, so the paper labels text-only results. The questions are in English and subjects are not equally represented; the supplied material contains no comprehensive study of comparisons across languages or populations. Public instructions and marking code allow some inspection, but downloading the dataset requires accepting contact-sharing conditions, and the private set is not released. The dataset page lists an MIT licence and asks users not to redistribute test data, while the code also has an MIT licence. The authors describe excluding certain kinds of dangerous content during collection. The survey preparer inspected the available documentation without downloading the gated questions or rerunning the AI evaluations. When comparing results over time, the edition also matters: HLE-Rolling has its own record of removed and restored questions, and **those changes do not automatically describe original HLE**. No study establishing equivalent scores across original HLE, HLE-Rolling and HLE-Diamond is supplied here. Sources: [HP](#source-HP) [HR](#source-HR) [HC](#source-HC) [HJ](#source-HJ) [HL](#source-HL) [HW](#source-HW) [HU](#source-HU).

#### What the findings cover

HLE’s title suggests a final exam at the edge of human knowledge, but the paper limits its interpretation to difficult academic questions with definite answers. It explicitly states that **a high score alone does not establish general intelligence or the ability to conduct independent research**. Consistent with that limit, this packet contains no measured relationship between HLE scores and success on independent scientific projects. Such gaps leave broader claims unresolved; they do not, by themselves, show that the benchmark fails. Sources: [HP](#source-HP).

### Answered questions

### Description

**Example Q1. Are the benchmark version, set of test problems and method for calculating scores identified?**

**Meaning:** Identify the edition of the benchmark, the problems used, and the scoring method. This asks whether all three are stated, not whether they are good choices.

**Answer: Yes**

Why: The passage identifies original HLE and its 2,500 questions. A judging AI compares responses with reference answers, and accuracy is the percentage marked correct, so both the test and its scoring method are described. Sources: [HP](#source-HP) [HW](#source-HW).

**Example Q2. Are the ability being tested, the intended AI systems and the intended uses described?**

**Meaning:** Look for the ability being tested, which AI systems the test is intended for, and the proposed uses of its scores. A description of these aims is different from evidence that the test achieves them.

**Answer: Yes**

Why: HLE tests academic knowledge and reasoning in AI systems that handle text or text and images. Its scores are intended to compare these systems on academic questions; they do not by themselves establish research ability or general intelligence. Sources: [HP](#source-HP).

**Example Q3. Are the test problems, the information provided and the required answers or actions described?**

**Meaning:** The description should say what the AI receives and what it must produce or do. You do not need to solve the problems yourself.

**Answer: Yes**

Why: The AI receives a question, sometimes with an image, and selects an option or gives a short answer. The evaluation software asks for an explanation, a final answer and a percentage stating confidence. Sources: [HP](#source-HP).

**Example Q4. Are the instructions, resources and limits for taking the test described?**

**Meaning:** Testing conditions include instructions, tools, supplied documents, time, allowed attempts, and AI settings. This asks whether relevant conditions are described, not whether every possible condition was studied.

**Answer: Partly**

Why: The software describes the instructions and a temperature setting of zero to reduce randomness. However, the line that sends that setting is disabled in the inspected code, so the description does not establish that it was used. Sources: [HM](#source-HM) [HR](#source-HR).

**Example Q5. Is it described how answers or actions become scores and how results are presented?**

**Meaning:** Look for the rules that turn responses into points, any averaging or weighting, and how results are shown. Describing a scoring rule does not establish that it is accurate or appropriate.

**Answer: Yes**

Why: An AI judge compares each final answer with a reference, accepting equivalent meanings. The code reports the percentage marked correct, a confidence range and how stated confidence compares with accuracy; describing these calculations does not establish that they work well. Sources: [HJ](#source-HJ).

### Purpose and development

**Example Q6. Is it explained why the test problems measure the ability the benchmark claims to test?**

**Meaning:** The explanation should link the problems to the claimed ability. Being difficult or requiring specialist knowledge does not by itself establish that a task measures reasoning.

**Answer: Yes**

Why: The paper uses specialist academic questions with definite answers to test knowledge and reasoning that existing AI models struggle with. This explains the choice of tasks, but does not establish coverage of every academic ability. Sources: [HP](#source-HP).

**Example Q7. Are the origins and choice of test problems justified for the benchmark’s intended use?**

**Meaning:** Look for reasons for the sources, number, topics, and difficulty of problems in relation to the intended use. Availability alone is not a reason that these problems represent the ability.

**Answer: Partly**

Why: Experts contributed questions, and questions that selected AI models could already answer were screened out. This explains how difficulty was chosen, but does not show that the resulting set represents academic work more generally. Sources: [HP](#source-HP).

**Example Q8. Were the test problems and the answers used to mark them checked for errors during development?**

**Meaning:** This asks whether both the problems and the supplied answers used to mark them were examined for mistakes during development. It is separate from testing how new AI responses are marked. Evidence that examination occurred does not establish that every answer is correct; note limits in its coverage when relevant.

**Answer: Yes**

Why: Expert review and organizer approval were followed by two checks of 200 questions each, examining questions and reference answers. The reported 15.4% expert disagreement limits confidence in the answers, but does not negate that checking occurred. Sources: [HP](#source-HP).

**Example Q9. Is there evidence that the test problems cover the relevant parts of the ability being claimed?**

**Meaning:** An ability may have several relevant parts. Look for evidence that the selected problems cover the parts included in the claim. A narrow set of problems may fit a narrow claim but not a broader one.

**Answer: Partly**

Why: The questions span many subjects but emphasize mathematics and require definite answers. This covers some academic knowledge and reasoning, while creative work and research without a fixed answer fall outside the format. Sources: [HP](#source-HP).

### Scoring and comparisons

**Example Q10. Is there evidence that the way points are awarded reflects the ability the benchmark is meant to measure?**

**Meaning:** Look for evidence that earning more points means doing better at the intended ability. A fixed scoring rule can work exactly as written while rewarding formatting or other features unrelated to that ability.

**Answer: Partly**

Why: The judge accepts responses that mean the same thing as the reference answer, allowing differences in wording. However, it compares answers without independently solving the problem, so a mistaken reference or judging decision can affect the score. Sources: [HJ](#source-HJ) [HP](#source-HP).

**Example Q11. Is there evidence supporting how scores are combined and what any separate scores are said to measure?**

**Meaning:** Look for reasons for combining results, weighting groups, and naming any separate abilities. Averaging scores is a calculation; it does not by itself establish that the total measures one ability.

**Answer: Partly**

Why: Every question counts equally toward accuracy, so subjects with more questions contribute more to the total. Results are also reported by subject, but the supplied material does not establish that these subject scores measure separate abilities. Sources: [HP](#source-HP) [HJ](#source-HJ).

**Example Q12. Was the marking process tested to see whether it awards the right scores consistently?**

**Meaning:** Marking can be done by people, fixed software rules, or another AI. This asks whether that process was tested for correct and consistent marks. Testing that found mistakes still counts as testing. Fixed software rules alone do not show that tests occurred, and evidence of some testing does not establish complete marking accuracy.

**Answer: Not sure**

Why: The code shows how the AI judge compares responses with reference answers, but no full comparison with expert marking is supplied. Expert checks of the questions do not establish whether this judge marks AI responses correctly and consistently. Sources: [HJ](#source-HJ) [HP](#source-HP).

**Example Q13. Are the comparison points used to explain the scores justified for the claims being made?**

**Meaning:** A comparison point is a human score, another AI score, or a guessing result used to interpret a score. Ask whether it fits the stated claim and conditions. Comparing particular systems does not establish a ranking among all systems or a justified score cutoff for a decision.

**Answer: Partly**

Why: The paper compares AI models on the full question set and separately on questions using only text. These provide context, but no matched group of people takes the whole exam under the same conditions, limiting comparisons with human performance. Sources: [HP](#source-HP).

### Consistency of results

**Example Q14. Was it tested how much the same AI system’s score changes when the benchmark is run more than once?**

**Meaning:** This asks whether the same AI was evaluated repeatedly under the same conditions and score changes were measured. One reported evaluation does not establish whether other evaluations occurred; an explicit statement that only one occurred rules out repetition for that evaluation. Neither establishes that repeated scores would be unstable.

**Answer: Not sure**

Why: The paper acknowledges that an AI can answer differently on separate attempts. The supplied sources do not establish repeated testing of the same systems for the main comparisons, so the size of score changes remains unknown. Sources: [HP](#source-HP) [HM](#source-HM).

**Example Q15. Was it tested how much scores change when instructions, presentation or the testing setup change?**

**Meaning:** This asks whether effects of changed instructions, presentation, or settings were measured. Repeating identical conditions is different from changing conditions. Findings about one change need not cover every possible change.

**Answer: Not sure**

Why: The supplied sources do not establish systematic tests of reworded instructions or changes to the judging AI. Describing one instruction and testing setup does not show how much scores change when those conditions change. Sources: [HP](#source-HP) [HJ](#source-HJ) [HM](#source-HM).

**Example Q16. Are estimates of how much scores could vary provided in enough detail to support the comparisons or decisions being made?**

**Meaning:** Look for a range or other estimate of possible score differences, how it was calculated, and whether it supports the intended comparison. An estimate based on the number of problems need not measure changes across repeated evaluations; small score differences may remain unresolved.

**Answer: Partly**

Why: The code estimates a 95% confidence range from the number of questions and the fraction marked correct. It does not measure changes from rerunning the AI or replacing the judge, so it covers only some uncertainty in comparisons. Sources: [HJ](#source-HJ).

### Meaning and fairness

**Example Q17. Were ways of earning points without using the ability being tested investigated?**

**Meaning:** A shortcut earns points without the intended ability, for example through accidental clues. This asks whether such routes were investigated. Identifying a possible shortcut does not establish that a tested AI used it; an investigation that found a problem still occurred.

**Answer: Partly**

Why: Contributors were asked to avoid questions answered by a simple lookup and could revise questions answered through faulty reasoning. These checks address some shortcuts, but guessing remains possible and the supplied material does not measure every route to points. Sources: [HP](#source-HP).

**Example Q18. Was the risk that AI systems had already seen the test problems or answers assessed and addressed?**

**Meaning:** Look for both an assessment of earlier exposure to questions or answers and steps to address the risk. Public availability may create a risk without proving that a particular model saw the material. Protective measures do not establish that exposure was impossible.

**Answer: Partly**

Why: HLE keeps some questions private, marks public test data and warns against using it for training. These measures help limit exposure, but the supplied information does not show whether an AI was trained on any of the public questions or answers. Sources: [HP](#source-HP) [HR](#source-HR).

**Example Q19. Are the rules on training specifically for this test and repeatedly submitting results justified for the intended use?**

**Meaning:** Look for rules about training specifically for the test and repeatedly submitting results, with reasons linked to the intended use. A rule being absent from the supplied description is different from evidence that the rule is unsuitable.

**Answer: Not sure**

Why: The instructions discourage training on test questions. However, the supplied material lacks a complete policy covering repeated submissions, access to feedback and reporting systems trained for HLE, leaving insufficient information to judge whether the rules support the intended comparisons. Sources: [HR](#source-HR).

**Example Q20. Is there evidence for any claim that the scores show how well an AI system will perform beyond the problems in this test?**

**Meaning:** This concerns claims about new problems or real work beyond the benchmark. Look for evidence covering that broader claim. A stated ambition alone is not such evidence; if no broader claim or use arises, consider Not applicable.

**Answer: Not sure**

Why: The supplied passage reports no measured relationship between HLE scores and success on independent scientific projects. Academic question scores therefore leave that broader claim unresolved; missing evidence does not prove that an AI cannot conduct research. Sources: [HP](#source-HP).

**Example Q21. Is there evidence that comparisons are fair across the AI systems and situations the benchmark is meant to cover?**

**Meaning:** Look for evidence that differences in information, tools, tasks, resources, or settings do not make the intended comparison misleading. Findings about differences between people do not by themselves establish fair comparisons between AI systems.

**Answer: Partly**

Why: Results using only text are labelled separately from results that include images. This helps compare systems receiving similar information, but English questions, unequal subject coverage and missing studies across languages leave other fairness claims unresolved. Sources: [HP](#source-HP).

### Use and reporting

**Example Q22. Are the test materials and methods available in enough detail for someone else to repeat the evaluation or examine how it was done?**

**Meaning:** Look for enough problems, scoring details, instructions, and software to repeat or inspect the evaluation. Public access to some files does not necessarily reproduce hidden test results or earlier software versions.

**Answer: Partly**

Why: The instructions and marking code are public, allowing readers to inspect the procedure. Downloading questions requires accepting access conditions, and a separate private question set is withheld, so not all materials are available to examine or repeat every result. Sources: [HR](#source-HR) [HC](#source-HC) [HJ](#source-HJ).

**Example Q23. Are the rules for accessing and reusing the benchmark, and the protections needed for responsible use, stated?**

**Meaning:** Look for access and reuse rules and relevant safeguards, such as protecting hidden answers. A missing permission statement does not establish that reuse is prohibited. This asks whether relevant rules are stated, not whether all materials must be public.

**Answer: Partly**

Why: The dataset and code list MIT licences, access requires accepting conditions, and the paper describes excluding dangerous content. However, the dataset also asks users not to redistribute questions, leaving some reuse expectations unclear alongside the licence. Sources: [HC](#source-HC) [HL](#source-HL) [HP](#source-HP).

**Example Q24. Are changes to the benchmark recorded, including how they affect comparisons between old and new scores?**

**Meaning:** Look for a record of changes to problems, answers, or scoring and an explanation of their effects on old and new scores. A new version number alone does not explain whether scores can be compared.

**Answer: Not sure**

Why: HLE-Rolling records removed and restored questions, but it is separate from original HLE. The supplied material does not establish how changes to original HLE affect comparisons between earlier and later scores. Sources: [HW](#source-HW) [HU](#source-HU).

**Example Q25. Do the published claims stay within what the evidence supports?**

**Meaning:** Compare what is publicly claimed with the tasks, conditions, and results actually reported. A claim about these tasks may be justified even when a broader claim is not. Missing evidence for a broad claim does not prove that the AI lacks the ability.

**Answer: Partly**

Why: The paper says high scores alone do not establish general intelligence or independent research ability. However, the title “Humanity’s Last Exam” can suggest broader coverage than a set of academic questions with definite answers supports. Sources: [HP](#source-HP).

## 4. ARC-AGI-2

Each puzzle shows several before-and-after grids of coloured squares. The AI must infer the hidden rule and produce outputs for new inputs. Public development tasks are available for practice; separate tasks are used for evaluation. You do not need to solve the puzzles to complete this survey.

**Which test this survey covers:** ARC-AGI-2 public test problems, the official scoring software, and ARC Prize’s rules for tests that it runs or verifies. Sources were inspected on 7 October 2026. Other competitions and community results may use different rules.

**How to interpret its scores:** Using scores to compare AI systems’ ability to solve unfamiliar grid problems, and considering the creators’ broader claims about reasoning.

### Reading passage

![ARC Prize logo](images/arc-prize-logo.svg)

#### What the AI is asked to do

ARC-AGI-2 is a test developed by ARC Prize Foundation staff and partners to assess whether an AI can **work out a new rule from examples**. Each problem presents pairs of coloured grids, showing a starting grid alongside its correct finished grid. Using those examples, the AI must work out how to complete a new starting grid and return an answer with the right size and colour in every square. The creators designed these problems to require little specialist knowledge while encouraging the AI to combine ideas. Their aim is to study reasoning that goes beyond recalling facts or trying large numbers of possible programs, which they connect to progress toward more general, human-like AI. Sources: [AR](#source-AR) [AB](#source-AB) [AP](#source-AP).

**A real ARC-AGI-2 problem**

![Official ARC-AGI-2 problem e3721c99: two worked examples show starting grids with grey shapes and their coloured outputs. A new test input appears below beside a question mark for the missing output.](images/arc-agi-2-e3721c99.png)

The two pairs at the top show starting grids (“Input”) and completed grids (“Output”). The AI uses these examples to work out the missing output at the bottom. You do not need to solve it.

Official Figure 1, ARC-AGI-2 technical report, François Chollet and colleagues. Problem e3721c99. [Source figure](https://arxiv.org/html/2505.11831v2/arc-agi-task-e3721c99.png).

#### How the problems were chosen

ARC-AGI-2’s developers began with a collection of newly written grid puzzles and puzzles prepared for earlier ARC work that had not been used. To help decide which puzzles to include and how difficult they were, the developers **conducted a study in which people tried solving them**. This involved **407 people taking part in 515 paid, 90-minute sessions**. The puzzles used in that study formed a larger pool than the final test, so the results do not all describe the final set. The developers also reviewed puzzles themselves and removed ones they judged could be solved by the same rule. The released benchmark contains **1,000 problems for practice and AI development**, along with **three test sets of 120 problems each**. These sets are called public, semi-private and private because access to their problems differs. Using the human participants’ results, the developers selected the three test sets to have similar difficulty for people. After release, they continued correcting the materials; a public change record lists fixes to some coloured squares and unclear examples. Sources: [AC](#source-AC) [AP](#source-AP).

#### How answers earn points

The AI is allowed **two attempts for each new input grid**, and it earns credit for that input only if an attempt matches the supplied answer in both size and every square’s colour. A nearly correct grid therefore receives no credit. A problem can contain several new inputs, however, so the official scoring software inspected for this survey calculates the fraction solved within each problem before averaging the problem scores. Solving one of two inputs, for example, earns **0.5 for that problem**. This differs from calling the whole problem “fully solved,” which the instructions published with the problems reserve for cases where every input is correct. The software does not provide separate scores established as measures of distinct abilities. Its public tests cover correct answers, wrong sizes, changed squares and missing outputs; the survey preparer inspected those tests without independently testing the whole marking system. Sources: [AR](#source-AR) [AS](#source-AS) [AT](#source-AT).

**Example: a problem with two new input grids**

1. **Input 1: solved** — At least one permitted attempt matches the entire answer grid: 1.
2. **Input 2: unsolved** — Neither permitted attempt matches the entire answer grid: 0.
3. **Problem score: 0.5** — The inspected software calculates (1 + 0) ÷ 2. It then averages problem scores.

Illustration of the inspected software, not an observed AI result. A partly correct grid gets no credit. The dataset description calls the whole problem solved only when both inputs are correct.

#### Testing conditions and changes in scores

ARC Prize, the organization running the verified evaluations, specifies AI settings and a spending limit for the tests it verifies, although other testing routes may use different conditions. Its verified-testing policy uses **one run, rather than an average of repeated runs**. A technical report describing ARC-AGI-2’s development gives AI scores, but the materials reviewed here do not provide estimates or ranges showing how much the same AI’s score changes when the same test is repeated. Although the running software allows settings to be changed, those materials also contain no systematic study of the effects of changing instructions, grid presentation or software. Matching the test sets for human difficulty addresses a separate issue and does not measure these changes in AI scores. Sources: [AR](#source-AR) [POL](#source-POL) [AP](#source-AP) [AM](#source-AM).

#### Prior exposure and ways to earn points

The creators tried to limit ways of earning points without the intended reasoning by designing problems that resist searches through large numbers of possible programs and by checking for repeated solution rules. These steps do not establish that every such route to a high score has been ruled out. Prior exposure is another concern because anyone can see the public problems. For hidden tests sent to AI providers, ARC Prize describes agreements against retaining the data and monitoring of possible exposure, while acknowledging that information could still escape. To keep development separate from evaluation, **training on development problems is allowed, while changing a system specifically to improve on evaluation problems is discouraged**. ARC Prize also says its verified tests are not a service for repeatedly improving systems through its feedback. Sources: [AB](#source-AB) [AP](#source-AP) [POL](#source-POL) [AR](#source-AR).

#### Comparisons, access and updates

In the puzzle-solving study described above, the developers found no clear statistical relationship between performance and recorded background factors such as work and technical experience. For AI comparisons, verified tests record the settings used, though other testing routes may differ. Researchers can inspect **public problems, running software and marking tests**, while access to hidden problems is controlled. ARC Prize says it also releases public testing outputs, costs, times and problem scores, but the survey preparer did not check the complete archive. The public data use an Apache 2.0 licence; hidden-data rules address confidentiality, provider handling and code review for selected submissions. To help track revisions, a dated change record identifies corrected problems and exact code changes. It does not, however, recalculate every affected AI score, and ARC-AGI-1 and ARC-AGI-2 remain separate test versions. Sources: [AP](#source-AP) [POL](#source-POL) [AM](#source-AM) [AT](#source-AT) [AL](#source-AL) [AC](#source-AC).

#### What the findings cover

Although the creators connect ARC-AGI-2 to abstract reasoning and broader intelligence, the studies supplied here concern **two-dimensional grid problems**. This packet contains no study showing how scores predict success in language, social interaction or other real-world work, and it supplies no measure covering every kind of intelligence. These are **limits of the information available for this survey**: they leave those broader relationships unresolved, rather than showing that such relationships are impossible. Sources: [AB](#source-AB).

### Questions about ARC-AGI-2

Use the passage to make your own judgments. Choose one response per question. Comments are optional.

### Description

**Q1. Are the benchmark version, set of test problems and method for calculating scores identified?**

**Meaning:** Identify the edition of the benchmark, the problems used, and the scoring method. This asks whether all three are stated, not whether they are good choices.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The passage identifies original HLE and its 2,500 questions. A judging AI compares responses with reference answers, and accuracy is the percentage marked correct, so both the test and its scoring method are described.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q2. Are the ability being tested, the intended AI systems and the intended uses described?**

**Meaning:** Look for the ability being tested, which AI systems the test is intended for, and the proposed uses of its scores. A description of these aims is different from evidence that the test achieves them.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: HLE tests academic knowledge and reasoning in AI systems that handle text or text and images. Its scores are intended to compare these systems on academic questions; they do not by themselves establish research ability or general intelligence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q3. Are the test problems, the information provided and the required answers or actions described?**

**Meaning:** The description should say what the AI receives and what it must produce or do. You do not need to solve the problems yourself.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The AI receives a question, sometimes with an image, and selects an option or gives a short answer. The evaluation software asks for an explanation, a final answer and a percentage stating confidence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q4. Are the instructions, resources and limits for taking the test described?**

**Meaning:** Testing conditions include instructions, tools, supplied documents, time, allowed attempts, and AI settings. This asks whether relevant conditions are described, not whether every possible condition was studied.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The software describes the instructions and a temperature setting of zero to reduce randomness. However, the line that sends that setting is disabled in the inspected code, so the description does not establish that it was used.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q5. Is it described how answers or actions become scores and how results are presented?**

**Meaning:** Look for the rules that turn responses into points, any averaging or weighting, and how results are shown. Describing a scoring rule does not establish that it is accurate or appropriate.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: An AI judge compares each final answer with a reference, accepting equivalent meanings. The code reports the percentage marked correct, a confidence range and how stated confidence compares with accuracy; describing these calculations does not establish that they work well.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Purpose and development

**Q6. Is it explained why the test problems measure the ability the benchmark claims to test?**

**Meaning:** The explanation should link the problems to the claimed ability. Being difficult or requiring specialist knowledge does not by itself establish that a task measures reasoning.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The paper uses specialist academic questions with definite answers to test knowledge and reasoning that existing AI models struggle with. This explains the choice of tasks, but does not establish coverage of every academic ability.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q7. Are the origins and choice of test problems justified for the benchmark’s intended use?**

**Meaning:** Look for reasons for the sources, number, topics, and difficulty of problems in relation to the intended use. Availability alone is not a reason that these problems represent the ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Experts contributed questions, and questions that selected AI models could already answer were screened out. This explains how difficulty was chosen, but does not show that the resulting set represents academic work more generally.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q8. Were the test problems and the answers used to mark them checked for errors during development?**

**Meaning:** This asks whether both the problems and the supplied answers used to mark them were examined for mistakes during development. It is separate from testing how new AI responses are marked. Evidence that examination occurred does not establish that every answer is correct; note limits in its coverage when relevant.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: Expert review and organizer approval were followed by two checks of 200 questions each, examining questions and reference answers. The reported 15.4% expert disagreement limits confidence in the answers, but does not negate that checking occurred.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q9. Is there evidence that the test problems cover the relevant parts of the ability being claimed?**

**Meaning:** An ability may have several relevant parts. Look for evidence that the selected problems cover the parts included in the claim. A narrow set of problems may fit a narrow claim but not a broader one.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The questions span many subjects but emphasize mathematics and require definite answers. This covers some academic knowledge and reasoning, while creative work and research without a fixed answer fall outside the format.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Scoring and comparisons

**Q10. Is there evidence that the way points are awarded reflects the ability the benchmark is meant to measure?**

**Meaning:** Look for evidence that earning more points means doing better at the intended ability. A fixed scoring rule can work exactly as written while rewarding formatting or other features unrelated to that ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The judge accepts responses that mean the same thing as the reference answer, allowing differences in wording. However, it compares answers without independently solving the problem, so a mistaken reference or judging decision can affect the score.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q11. Is there evidence supporting how scores are combined and what any separate scores are said to measure?**

**Meaning:** Look for reasons for combining results, weighting groups, and naming any separate abilities. Averaging scores is a calculation; it does not by itself establish that the total measures one ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Every question counts equally toward accuracy, so subjects with more questions contribute more to the total. Results are also reported by subject, but the supplied material does not establish that these subject scores measure separate abilities.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q12. Was the marking process tested to see whether it awards the right scores consistently?**

**Meaning:** Marking can be done by people, fixed software rules, or another AI. This asks whether that process was tested for correct and consistent marks. Testing that found mistakes still counts as testing. Fixed software rules alone do not show that tests occurred, and evidence of some testing does not establish complete marking accuracy.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The code shows how the AI judge compares responses with reference answers, but no full comparison with expert marking is supplied. Expert checks of the questions do not establish whether this judge marks AI responses correctly and consistently.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q13. Are the comparison points used to explain the scores justified for the claims being made?**

**Meaning:** A comparison point is a human score, another AI score, or a guessing result used to interpret a score. Ask whether it fits the stated claim and conditions. Comparing particular systems does not establish a ranking among all systems or a justified score cutoff for a decision.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The paper compares AI models on the full question set and separately on questions using only text. These provide context, but no matched group of people takes the whole exam under the same conditions, limiting comparisons with human performance.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Consistency of results

**Q14. Was it tested how much the same AI system’s score changes when the benchmark is run more than once?**

**Meaning:** This asks whether the same AI was evaluated repeatedly under the same conditions and score changes were measured. One reported evaluation does not establish whether other evaluations occurred; an explicit statement that only one occurred rules out repetition for that evaluation. Neither establishes that repeated scores would be unstable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The paper acknowledges that an AI can answer differently on separate attempts. The supplied sources do not establish repeated testing of the same systems for the main comparisons, so the size of score changes remains unknown.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q15. Was it tested how much scores change when instructions, presentation or the testing setup change?**

**Meaning:** This asks whether effects of changed instructions, presentation, or settings were measured. Repeating identical conditions is different from changing conditions. Findings about one change need not cover every possible change.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The supplied sources do not establish systematic tests of reworded instructions or changes to the judging AI. Describing one instruction and testing setup does not show how much scores change when those conditions change.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q16. Are estimates of how much scores could vary provided in enough detail to support the comparisons or decisions being made?**

**Meaning:** Look for a range or other estimate of possible score differences, how it was calculated, and whether it supports the intended comparison. An estimate based on the number of problems need not measure changes across repeated evaluations; small score differences may remain unresolved.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The code estimates a 95% confidence range from the number of questions and the fraction marked correct. It does not measure changes from rerunning the AI or replacing the judge, so it covers only some uncertainty in comparisons.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Meaning and fairness

**Q17. Were ways of earning points without using the ability being tested investigated?**

**Meaning:** A shortcut earns points without the intended ability, for example through accidental clues. This asks whether such routes were investigated. Identifying a possible shortcut does not establish that a tested AI used it; an investigation that found a problem still occurred.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Contributors were asked to avoid questions answered by a simple lookup and could revise questions answered through faulty reasoning. These checks address some shortcuts, but guessing remains possible and the supplied material does not measure every route to points.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q18. Was the risk that AI systems had already seen the test problems or answers assessed and addressed?**

**Meaning:** Look for both an assessment of earlier exposure to questions or answers and steps to address the risk. Public availability may create a risk without proving that a particular model saw the material. Protective measures do not establish that exposure was impossible.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: HLE keeps some questions private, marks public test data and warns against using it for training. These measures help limit exposure, but the supplied information does not show whether an AI was trained on any of the public questions or answers.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q19. Are the rules on training specifically for this test and repeatedly submitting results justified for the intended use?**

**Meaning:** Look for rules about training specifically for the test and repeatedly submitting results, with reasons linked to the intended use. A rule being absent from the supplied description is different from evidence that the rule is unsuitable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The instructions discourage training on test questions. However, the supplied material lacks a complete policy covering repeated submissions, access to feedback and reporting systems trained for HLE, leaving insufficient information to judge whether the rules support the intended comparisons.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q20. Is there evidence for any claim that the scores show how well an AI system will perform beyond the problems in this test?**

**Meaning:** This concerns claims about new problems or real work beyond the benchmark. Look for evidence covering that broader claim. A stated ambition alone is not such evidence; if no broader claim or use arises, consider Not applicable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The supplied passage reports no measured relationship between HLE scores and success on independent scientific projects. Academic question scores therefore leave that broader claim unresolved; missing evidence does not prove that an AI cannot conduct research.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q21. Is there evidence that comparisons are fair across the AI systems and situations the benchmark is meant to cover?**

**Meaning:** Look for evidence that differences in information, tools, tasks, resources, or settings do not make the intended comparison misleading. Findings about differences between people do not by themselves establish fair comparisons between AI systems.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Results using only text are labelled separately from results that include images. This helps compare systems receiving similar information, but English questions, unequal subject coverage and missing studies across languages leave other fairness claims unresolved.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Use and reporting

**Q22. Are the test materials and methods available in enough detail for someone else to repeat the evaluation or examine how it was done?**

**Meaning:** Look for enough problems, scoring details, instructions, and software to repeat or inspect the evaluation. Public access to some files does not necessarily reproduce hidden test results or earlier software versions.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The instructions and marking code are public, allowing readers to inspect the procedure. Downloading questions requires accepting access conditions, and a separate private question set is withheld, so not all materials are available to examine or repeat every result.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q23. Are the rules for accessing and reusing the benchmark, and the protections needed for responsible use, stated?**

**Meaning:** Look for access and reuse rules and relevant safeguards, such as protecting hidden answers. A missing permission statement does not establish that reuse is prohibited. This asks whether relevant rules are stated, not whether all materials must be public.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The dataset and code list MIT licences, access requires accepting conditions, and the paper describes excluding dangerous content. However, the dataset also asks users not to redistribute questions, leaving some reuse expectations unclear alongside the licence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q24. Are changes to the benchmark recorded, including how they affect comparisons between old and new scores?**

**Meaning:** Look for a record of changes to problems, answers, or scoring and an explanation of their effects on old and new scores. A new version number alone does not explain whether scores can be compared.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: HLE-Rolling records removed and restored questions, but it is separate from original HLE. The supplied material does not establish how changes to original HLE affect comparisons between earlier and later scores.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q25. Do the published claims stay within what the evidence supports?**

**Meaning:** Compare what is publicly claimed with the tasks, conditions, and results actually reported. A claim about these tasks may be justified even when a broader claim is not. Missing evidence for a broad claim does not prove that the AI lacks the ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The paper says high scores alone do not establish general intelligence or independent research ability. However, the title “Humanity’s Last Exam” can suggest broader coverage than a set of academic questions with definite answers supports.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

## 5. DesignQA

The AI receives written engineering rules, vehicle images or drawings and must answer questions about them. It may need to find a rule, explain a technical term, identify a part, or check whether a design meets a requirement. The questions draw on Formula SAE, a competition in which university students design and build racing cars. You do not need engineering knowledge or to solve these problems to review this test.

**Which test this survey covers:** The original DesignQA benchmark described in the 2024 paper, together with its public scoring software. Sources were inspected on 6 October 2026. Later changes to the questions or software may affect results.

**How to interpret its scores:** Using scores to compare how well AI systems find and apply engineering rules and understand vehicle drawings, while considering how far these results support claims about understanding other engineering documents.

### Reading passage

#### What the AI is asked to do

DesignQA was created by researchers and engineers working with materials from **Formula SAE, a competition in which university students design and build racing cars**. Their aim was to test whether an AI can find engineering rules, understand technical terms and drawings, and apply rules to a design. The paper describes **1,451 question-and-answer pairs in six groups**. These ask the AI to find an individual rule, gather related rules, explain a technical term, identify whether a component is present, check dimensions, or assess performance against a requirement. Depending on the question, the AI receives written rules, a vehicle image or a drawing and must give a text answer or a yes/no answer, sometimes with an explanation. These tasks follow parts of an engineer’s work, which is the authors’ reason for using them to assess understanding of engineering documents. Sources: [DQ-P](#source-DQ-P).

#### How the questions were chosen and checked

The developers used a real competition rulebook, vehicle designs and test data, drawing on contributions from engineering practitioners and researchers. This gives the questions a clear connection to practical work, but the benchmark uses **one rulebook and a limited range of tasks**, rather than a representative sample of engineering work across industries. The groups are also very uneven: finding individual rules accounts for 1,192 questions, while checking functional performance accounts for only 16. The paper reports that two additional reviewers checked manually written questions, with exceptions for questions derived from others and some explanations. Those explanations received a more limited check that they supported the yes/no answer. The reviewed sources do not establish how often reviewers disagreed or how many errors remained. Sources: [DQ-P](#source-DQ-P).

#### How answers earn points

DesignQA uses several marking methods because its questions require different kinds of answers. Some methods compare the wording of an AI answer with a supplied answer, while yes/no questions receive credit for the correct decision and may also have their explanations scored for text similarity. These rules are described, but **wording and formatting can affect credit**: the paper gives examples involving missing commas and valid related rules that were absent from the supplied answer. The public software also produces an overall score by giving each of the six question groups equal weight, despite their different sizes and marking methods. The reviewed material does not show that this overall number, or the separate group scores, measures a distinct underlying ability. Small marking-test files and discussion of scoring problems show some checking, but do not establish a complete study of marking accuracy and consistency. Sources: [DQ-P](#source-DQ-P) [DQ-C1](#source-DQ-C1) [DQ-C2](#source-DQ-C2) [DQ-FIX](#source-DQ-FIX).

#### Testing conditions and comparisons

The paper names the AI systems tested and describes instructions and settings, but **not every system receives the same information**. Some receive the whole rulebook, while others receive passages selected by search software. Their results therefore describe the AI together with its information supply, which matters when comparing systems. The authors include results from random guessing and other AI systems, but no reported baseline from human engineers taking the test. They also examine changes in the supplied passages, dimension labels, scale bars and highlighted images. One AI is tested with five different sets of rule passages, providing some information about variation. Because the passages change, this does not isolate variation when an identical test is repeated. For the main model comparisons, the reported information is insufficient to judge small score differences confidently. In the 16-question performance group, for example, one additional correct answer changes accuracy by 6.25 percentage points. Sources: [DQ-P](#source-DQ-P).

#### Prior exposure and unintended ways to earn points

The authors discuss influences such as formatting, wording, the quality of retrieved passages and familiarity with components. This shows attention to some factors beyond engineering understanding, but the reviewed material does not fully test ways of gaining points without that understanding. For example, the described drawings with scale bars all comply with the relevant rule. A reviewer can therefore infer that always answering “yes” would earn the yes/no credit on that portion, although this **does not show that any tested AI used that strategy**. The authors also discuss the novelty of their vehicle images and possible exposure to similar images, without directly checking every AI’s training data. The rulebook and released questions are public, and a protected test set or systematic overlap check was not established in the review. Clear enough rules on training on the questions and repeatedly submitting results were also not available in the sources examined. Sources: [DQ-P](#source-DQ-P) [DQ-R](#source-DQ-R) [DQ-TREE](#source-DQ-TREE) [DQ-WEB](#source-DQ-WEB).

#### Available materials and later changes

Public questions, instructions, scoring code and some AI responses allow researchers to inspect parts of the evaluation. However, they do not provide **a complete record for repeating every result in the paper**: the exact historical software, settings and inputs are not fully linked to each result. One released answer file also contains fewer rows than the corresponding question count in the paper. Code history makes revisions identifiable, but the reviewer did not find a clear change record explaining their effects on scores, a licence file, or complete rules for responsible reuse. These findings describe limits of the materials inspected; they do not establish that permission is unavailable elsewhere or that reuse is prohibited. Sources: [DQ-R](#source-DQ-R) [DQ-ENV](#source-DQ-ENV) [DQ-OUT](#source-DQ-OUT) [DQ-TREE](#source-DQ-TREE).

#### What the results can support

DesignQA’s paper acknowledges the limits of using one rulebook, a small set of task types and imperfect marking methods. It also says that **performance on a different technical document remains uncertain**. Real vehicle materials make the test relevant to engineering, but they do not demonstrate that its scores predict success on other standards or real engineering projects. The completed review below therefore treats the benchmark as a way to examine performance on these tasks under stated conditions. Broader claims about engineering competence, or fine distinctions between closely ranked systems, require more support. Sources: [DQ-P](#source-DQ-P) [DQ-WEB](#source-DQ-WEB).

### Questions about DesignQA

Use the passage to make your own judgments. Choose one response per question. Comments are optional.

### Description

**Q1. Are the benchmark version, set of test problems and method for calculating scores identified?**

**Meaning:** Identify the edition of the benchmark, the problems used, and the scoring method. This asks whether all three are stated, not whether they are good choices.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The passage identifies original HLE and its 2,500 questions. A judging AI compares responses with reference answers, and accuracy is the percentage marked correct, so both the test and its scoring method are described.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q2. Are the ability being tested, the intended AI systems and the intended uses described?**

**Meaning:** Look for the ability being tested, which AI systems the test is intended for, and the proposed uses of its scores. A description of these aims is different from evidence that the test achieves them.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: HLE tests academic knowledge and reasoning in AI systems that handle text or text and images. Its scores are intended to compare these systems on academic questions; they do not by themselves establish research ability or general intelligence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q3. Are the test problems, the information provided and the required answers or actions described?**

**Meaning:** The description should say what the AI receives and what it must produce or do. You do not need to solve the problems yourself.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The AI receives a question, sometimes with an image, and selects an option or gives a short answer. The evaluation software asks for an explanation, a final answer and a percentage stating confidence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q4. Are the instructions, resources and limits for taking the test described?**

**Meaning:** Testing conditions include instructions, tools, supplied documents, time, allowed attempts, and AI settings. This asks whether relevant conditions are described, not whether every possible condition was studied.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The software describes the instructions and a temperature setting of zero to reduce randomness. However, the line that sends that setting is disabled in the inspected code, so the description does not establish that it was used.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q5. Is it described how answers or actions become scores and how results are presented?**

**Meaning:** Look for the rules that turn responses into points, any averaging or weighting, and how results are shown. Describing a scoring rule does not establish that it is accurate or appropriate.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: An AI judge compares each final answer with a reference, accepting equivalent meanings. The code reports the percentage marked correct, a confidence range and how stated confidence compares with accuracy; describing these calculations does not establish that they work well.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Purpose and development

**Q6. Is it explained why the test problems measure the ability the benchmark claims to test?**

**Meaning:** The explanation should link the problems to the claimed ability. Being difficult or requiring specialist knowledge does not by itself establish that a task measures reasoning.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: The paper uses specialist academic questions with definite answers to test knowledge and reasoning that existing AI models struggle with. This explains the choice of tasks, but does not establish coverage of every academic ability.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q7. Are the origins and choice of test problems justified for the benchmark’s intended use?**

**Meaning:** Look for reasons for the sources, number, topics, and difficulty of problems in relation to the intended use. Availability alone is not a reason that these problems represent the ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Experts contributed questions, and questions that selected AI models could already answer were screened out. This explains how difficulty was chosen, but does not show that the resulting set represents academic work more generally.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q8. Were the test problems and the answers used to mark them checked for errors during development?**

**Meaning:** This asks whether both the problems and the supplied answers used to mark them were examined for mistakes during development. It is separate from testing how new AI responses are marked. Evidence that examination occurred does not establish that every answer is correct; note limits in its coverage when relevant.

<details><summary>HLE example</summary>

**Answer: Yes**

Why: Expert review and organizer approval were followed by two checks of 200 questions each, examining questions and reference answers. The reported 15.4% expert disagreement limits confidence in the answers, but does not negate that checking occurred.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q9. Is there evidence that the test problems cover the relevant parts of the ability being claimed?**

**Meaning:** An ability may have several relevant parts. Look for evidence that the selected problems cover the parts included in the claim. A narrow set of problems may fit a narrow claim but not a broader one.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The questions span many subjects but emphasize mathematics and require definite answers. This covers some academic knowledge and reasoning, while creative work and research without a fixed answer fall outside the format.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Scoring and comparisons

**Q10. Is there evidence that the way points are awarded reflects the ability the benchmark is meant to measure?**

**Meaning:** Look for evidence that earning more points means doing better at the intended ability. A fixed scoring rule can work exactly as written while rewarding formatting or other features unrelated to that ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The judge accepts responses that mean the same thing as the reference answer, allowing differences in wording. However, it compares answers without independently solving the problem, so a mistaken reference or judging decision can affect the score.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q11. Is there evidence supporting how scores are combined and what any separate scores are said to measure?**

**Meaning:** Look for reasons for combining results, weighting groups, and naming any separate abilities. Averaging scores is a calculation; it does not by itself establish that the total measures one ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Every question counts equally toward accuracy, so subjects with more questions contribute more to the total. Results are also reported by subject, but the supplied material does not establish that these subject scores measure separate abilities.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q12. Was the marking process tested to see whether it awards the right scores consistently?**

**Meaning:** Marking can be done by people, fixed software rules, or another AI. This asks whether that process was tested for correct and consistent marks. Testing that found mistakes still counts as testing. Fixed software rules alone do not show that tests occurred, and evidence of some testing does not establish complete marking accuracy.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The code shows how the AI judge compares responses with reference answers, but no full comparison with expert marking is supplied. Expert checks of the questions do not establish whether this judge marks AI responses correctly and consistently.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q13. Are the comparison points used to explain the scores justified for the claims being made?**

**Meaning:** A comparison point is a human score, another AI score, or a guessing result used to interpret a score. Ask whether it fits the stated claim and conditions. Comparing particular systems does not establish a ranking among all systems or a justified score cutoff for a decision.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The paper compares AI models on the full question set and separately on questions using only text. These provide context, but no matched group of people takes the whole exam under the same conditions, limiting comparisons with human performance.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Consistency of results

**Q14. Was it tested how much the same AI system’s score changes when the benchmark is run more than once?**

**Meaning:** This asks whether the same AI was evaluated repeatedly under the same conditions and score changes were measured. One reported evaluation does not establish whether other evaluations occurred; an explicit statement that only one occurred rules out repetition for that evaluation. Neither establishes that repeated scores would be unstable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The paper acknowledges that an AI can answer differently on separate attempts. The supplied sources do not establish repeated testing of the same systems for the main comparisons, so the size of score changes remains unknown.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q15. Was it tested how much scores change when instructions, presentation or the testing setup change?**

**Meaning:** This asks whether effects of changed instructions, presentation, or settings were measured. Repeating identical conditions is different from changing conditions. Findings about one change need not cover every possible change.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The supplied sources do not establish systematic tests of reworded instructions or changes to the judging AI. Describing one instruction and testing setup does not show how much scores change when those conditions change.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q16. Are estimates of how much scores could vary provided in enough detail to support the comparisons or decisions being made?**

**Meaning:** Look for a range or other estimate of possible score differences, how it was calculated, and whether it supports the intended comparison. An estimate based on the number of problems need not measure changes across repeated evaluations; small score differences may remain unresolved.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The code estimates a 95% confidence range from the number of questions and the fraction marked correct. It does not measure changes from rerunning the AI or replacing the judge, so it covers only some uncertainty in comparisons.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Meaning and fairness

**Q17. Were ways of earning points without using the ability being tested investigated?**

**Meaning:** A shortcut earns points without the intended ability, for example through accidental clues. This asks whether such routes were investigated. Identifying a possible shortcut does not establish that a tested AI used it; an investigation that found a problem still occurred.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Contributors were asked to avoid questions answered by a simple lookup and could revise questions answered through faulty reasoning. These checks address some shortcuts, but guessing remains possible and the supplied material does not measure every route to points.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q18. Was the risk that AI systems had already seen the test problems or answers assessed and addressed?**

**Meaning:** Look for both an assessment of earlier exposure to questions or answers and steps to address the risk. Public availability may create a risk without proving that a particular model saw the material. Protective measures do not establish that exposure was impossible.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: HLE keeps some questions private, marks public test data and warns against using it for training. These measures help limit exposure, but the supplied information does not show whether an AI was trained on any of the public questions or answers.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q19. Are the rules on training specifically for this test and repeatedly submitting results justified for the intended use?**

**Meaning:** Look for rules about training specifically for the test and repeatedly submitting results, with reasons linked to the intended use. A rule being absent from the supplied description is different from evidence that the rule is unsuitable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The instructions discourage training on test questions. However, the supplied material lacks a complete policy covering repeated submissions, access to feedback and reporting systems trained for HLE, leaving insufficient information to judge whether the rules support the intended comparisons.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q20. Is there evidence for any claim that the scores show how well an AI system will perform beyond the problems in this test?**

**Meaning:** This concerns claims about new problems or real work beyond the benchmark. Look for evidence covering that broader claim. A stated ambition alone is not such evidence; if no broader claim or use arises, consider Not applicable.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: The supplied passage reports no measured relationship between HLE scores and success on independent scientific projects. Academic question scores therefore leave that broader claim unresolved; missing evidence does not prove that an AI cannot conduct research.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q21. Is there evidence that comparisons are fair across the AI systems and situations the benchmark is meant to cover?**

**Meaning:** Look for evidence that differences in information, tools, tasks, resources, or settings do not make the intended comparison misleading. Findings about differences between people do not by themselves establish fair comparisons between AI systems.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: Results using only text are labelled separately from results that include images. This helps compare systems receiving similar information, but English questions, unequal subject coverage and missing studies across languages leave other fairness claims unresolved.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

### Use and reporting

**Q22. Are the test materials and methods available in enough detail for someone else to repeat the evaluation or examine how it was done?**

**Meaning:** Look for enough problems, scoring details, instructions, and software to repeat or inspect the evaluation. Public access to some files does not necessarily reproduce hidden test results or earlier software versions.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The instructions and marking code are public, allowing readers to inspect the procedure. Downloading questions requires accepting access conditions, and a separate private question set is withheld, so not all materials are available to examine or repeat every result.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q23. Are the rules for accessing and reusing the benchmark, and the protections needed for responsible use, stated?**

**Meaning:** Look for access and reuse rules and relevant safeguards, such as protecting hidden answers. A missing permission statement does not establish that reuse is prohibited. This asks whether relevant rules are stated, not whether all materials must be public.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The dataset and code list MIT licences, access requires accepting conditions, and the paper describes excluding dangerous content. However, the dataset also asks users not to redistribute questions, leaving some reuse expectations unclear alongside the licence.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q24. Are changes to the benchmark recorded, including how they affect comparisons between old and new scores?**

**Meaning:** Look for a record of changes to problems, answers, or scoring and an explanation of their effects on old and new scores. A new version number alone does not explain whether scores can be compared.

<details><summary>HLE example</summary>

**Answer: Not sure**

Why: HLE-Rolling records removed and restored questions, but it is separate from original HLE. The supplied material does not establish how changes to original HLE affect comparisons between earlier and later scores.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

**Q25. Do the published claims stay within what the evidence supports?**

**Meaning:** Compare what is publicly claimed with the tasks, conditions, and results actually reported. A claim about these tasks may be justified even when a broader claim is not. Missing evidence for a broad claim does not prove that the AI lacks the ability.

<details><summary>HLE example</summary>

**Answer: Partly**

Why: The paper says high scores alone do not establish general intelligence or independent research ability. However, the title “Humanity’s Last Exam” can suggest broader coverage than a set of academic questions with definite answers supports.

</details>

☐ Yes ☐ Partly ☐ No ☐ Not sure ☐ Not applicable

Comments (optional): __________________________________________

## 6. Review and submit

Check that all three familiarity questions and all 50 benchmark questions have a response. The online form submits everything in one response. Email-service acceptance does not prove inbox delivery.

### Feedback (required)

**How easy or difficult was it to understand the questions?**

- ☐ Very difficult
- ☐ Difficult
- ☐ Neither easy nor difficult
- ☐ Easy
- ☐ Very easy
- ☐ Cannot judge

**How easy or difficult was it to distinguish the five answer choices?**

- ☐ Very difficult
- ☐ Difficult
- ☐ Neither easy nor difficult
- ☐ Easy
- ☐ Very easy
- ☐ Cannot judge

**How manageable was the amount of reading and answering?**

- ☐ Very unmanageable
- ☐ Unmanageable
- ☐ Neither manageable nor unmanageable
- ☐ Manageable
- ☐ Very manageable
- ☐ Cannot judge

**How well did MESA help you understand what to look for when reviewing an AI benchmark?**

- ☐ Not at all well
- ☐ Slightly well
- ☐ Moderately well
- ☐ Very well
- ☐ Extremely well
- ☐ Cannot judge

**How confident did you feel using MESA to review these two AI benchmarks?**

- ☐ Not at all confident
- ☐ Slightly confident
- ☐ Moderately confident
- ☐ Very confident
- ☐ Extremely confident
- ☐ Cannot judge

Which question, explanation, or example was difficult to use, and why? (optional)

__________________________________________________

## 7. Confirmation

The online form confirms service acceptance after submission.

## Definitions for the printable copy

- **AI:** Software that can perform tasks such as answering questions or working with text and images. The software taking a test may also use extra tools.
- **AI benchmark:** A test used to assess an AI system. It contains problems, a way to mark answers and rules for interpreting results.
- **Benchmark version:** A particular edition of a test. Its problems, answers or marking rules may differ from another edition, so the edition matters when comparing scores.
- **Test problem:** One question or puzzle that the AI must answer or solve.
- **Ability:** Something an AI is meant to be able to do, such as finding a pattern or answering a science question. Doing well on one ability does not establish others.
- **Score:** The result of marking answers, such as the percentage correct. A score has meaning only in relation to the test and the conditions used.
- **Scoring:** The rules or software that turn an AI’s answers into points or a result.
- **Reference answer:** The supplied answer against which the AI’s response is marked. It can be wrong, so agreement with it is not proof that it is correct.
- **Prompt:** The directions and information given to the AI before it answers.
- **Score uncertainty:** How much a score estimate could vary under the assumptions of a calculation. It differs from the AI saying it is confident about an answer.
- **Intended use:** The comparison, claim or decision that a score is meant to support.
- **AI judge:** Another AI that marks a response by following instructions, often by comparing it with a supplied answer. Its marking can also make mistakes.
- **Comparison point:** A result used to help interpret a score, such as random guessing, a person’s score or another AI’s score.
- **Repeated testing:** Running the same test more than once to see whether the scores change.
- **Prior exposure:** The possibility that an AI encountered a test question or answer before taking the test, for example during its training.
- **Development:** The process of creating, selecting and checking the test problems and scoring rules.
- **Training:** The process in which an AI learns from data before it is used. If test answers are included, later test scores may reflect earlier exposure.
- **Evaluation set:** The collection of problems used to assess an AI. It may be separate from problems available for practice.
- **Open-ended research:** Work where the answer or next step is not fixed in advance, such as investigating a new scientific question.
- **General intelligence:** A broad ability to handle many different kinds of problems. A high score on one test does not establish this by itself.
- **Published:** Made available for others to read, for example in a paper, website or report. Publication alone does not mean the information has been checked.
- **Claim:** Something stated about what a benchmark measures or what its results show. For example, that a score shows an AI can reason.
- **Evidence:** Information used to judge whether a claim is supported, such as results from tests, comparisons or checks. Evidence can have limits and does not always settle the question.
- **Comparison:** Looking at results side by side, such as scores from two AI systems, to see how they differ. Differences in test questions or testing conditions can affect what the comparison tells us.
- **Protection:** Measures intended to prevent harm when accessing or using a benchmark, such as protecting private information or restricting access to content that could cause harm.
- **Test materials:** The questions, images, files and reference answers used in the benchmark.
- **Methods:** The procedures used to run the benchmark, mark responses and calculate results.
- **Situation:** The circumstances in which an AI is tested or used, such as the language, subject area, available tools or testing conditions.
- **Repeatedly submitting results:** Sending results for the same benchmark more than once, for example after changing an AI system. If feedback guides those changes, later scores may reflect adaptation to that test.

## Sources and links

You do not need to open these documents to answer the survey.

<a id="source-AP"></a>

- **AP** [ARC-AGI-2 technical report, v2, 15 January 2026](https://arxiv.org/html/2505.11831v2). §§4–5: human testing and task selection. The paper contains several differently aggregated human percentages; none is presented here as a universal human score.

<a id="source-AB"></a>

- **AB** [ARC Prize technical-report summary, 20 May 2025](https://arcprize.org/blog/arc-agi-2-technical-report). Design goals and the connection between grid puzzles and the claimed reasoning ability.

<a id="source-AR"></a>

- **AR** [ARC-AGI-2 dataset description](https://github.com/arcprize/ARC-AGI-2/blob/f3283f727488ad98fe575ea6a5ac981e4a188e49/readme.md). Public data, task format, permitted development data and success criterion.

<a id="source-AC"></a>

- **AC** [ARC-AGI-2 change record](https://github.com/arcprize/ARC-AGI-2/blob/f3283f727488ad98fe575ea6a5ac981e4a188e49/changelog.md). Release counts and dated task corrections.

<a id="source-AL"></a>

- **AL** [ARC-AGI-2 license](https://github.com/arcprize/ARC-AGI-2/blob/f3283f727488ad98fe575ea6a5ac981e4a188e49/LICENSE). Apache 2.0 for the public repository.

<a id="source-AS"></a>

- **AS** [ARC benchmarking scorer](https://github.com/arcprize/arc-agi-benchmarking/blob/9e2828fb5bd3ab43f6b9fc545595b82b67473b93/src/arc_agi_benchmarking/scoring/scoring.py). Exact grid checks and aggregation over test pairs and tasks. Inspected, not executed on benchmark models.

<a id="source-AT"></a>

- **AT** [ARC scorer tests](https://github.com/arcprize/arc-agi-benchmarking/blob/9e2828fb5bd3ab43f6b9fc545595b82b67473b93/src/arc_agi_benchmarking/tests/test_scoring.py). Test cases for correctness, dimensions, pixels and missing outputs. Existence is distinguished from independently verified test execution.

<a id="source-AM"></a>

- **AM** [ARC runner instructions](https://github.com/arcprize/arc-agi-benchmarking/blob/9e2828fb5bd3ab43f6b9fc545595b82b67473b93/README.md). Local execution, saved outputs and model configuration.

<a id="source-POL"></a>

- **POL** [ARC Prize verified-testing policy](https://arcprize.org/policy). Policy read on 7 October 2026. Applies to the verified-testing context described here, not a claim that all competition or community results follow the same protocol.

<a id="source-HP"></a>

- **HP** [HLE paper: repository’s supplied transcription](https://arxiv.org/abs/2501.14249). §§1, 3–5 and Appendix B.3. This is the supplied local paper snapshot, fingerprinted in the source manifest; no unstated arXiv version is assigned to it. The public article may have later revisions; the supplied transcription is the snapshot used here.

<a id="source-HR"></a>

- **HR** [HLE evaluation instructions](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/README.md). Original cais/hle test split, configuration instructions and training-exclusion marker. The README’s illustrative output uses a different item count from its 2,500-question description; it is not used as a current result.

<a id="source-HJ"></a>

- **HJ** [HLE answer judge and metrics](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/hle_eval/run_judge_results.py). Judge instructions and accuracy, confidence range and confidence-calibration calculations.

<a id="source-HM"></a>

- **HM** [HLE prediction script](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/hle_eval/run_model_predictions.py). Input construction and generation settings. The temperature argument exists, but its use in the API call is commented out.

<a id="source-HC"></a>

- **HC** [HLE dataset access page](https://huggingface.co/datasets/cais/hle). MIT label and contact-sharing gate observed on 7 October 2026. Gated question files were not downloaded.

<a id="source-HL"></a>

- **HL** [HLE code license](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/LICENSE). MIT license for code.

<a id="source-HU"></a>

- **HU** [HLE-Rolling change record](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/hle-rolling-changes.txt). Dated removed/re-added item identifiers for the separate rolling version.

<a id="source-HW"></a>

- **HW** [HLE official website](https://lastexam.ai/). Original HLE finalization and separate Rolling/Diamond announcements; no current model ranking is used.

<a id="source-DQ-P"></a>

- **DQ-P** [DesignQA: DesignQA paper, arXiv v2 (23 August 2024)](https://arxiv.org/abs/2404.07917v2). Primary source. Read the local transcription: introduction, dataset and scoring sections, evaluation, discussion, limitations and appendices. Used for task construction, reported experiments and claims. No new model runs; PDF tables were not independently re-extracted.

<a id="source-DQ-R"></a>

- **DQ-R** [DesignQA: Repository README](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/README.md). Primary source, inspected at the pinned commit. Used for setup, averaging, dataset paths and the submission procedure. The README gives an approximate rulebook length that differs from the paper; the example uses the paper’s 140-page description.

<a id="source-DQ-C1"></a>

- **DQ-C1** [DesignQA: Evaluation driver](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/full_evaluation.py). Primary code inspection. Checked optional subset arguments, the six-score average and results-file output. No end-to-end model evaluation was run.

<a id="source-DQ-C2"></a>

- **DQ-C2** [DesignQA: Metric implementations](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/metrics/metrics.py). Primary code inspection. Checked answer normalization, comma-separated rule parsing, component synonyms, yes/no extraction and explanation metrics. Inspection is not a complete scorer validation.

<a id="source-DQ-ENV"></a>

- **DQ-ENV** [DesignQA: Dependencies](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/requirements.txt). Lists nltk, rouge, pandas and sentence_transformers without version pins. This documents scoring dependencies, not a frozen model-running environment.

<a id="source-DQ-TREE"></a>

- **DQ-TREE** [DesignQA: Repository file inventory, tags and releases](https://github.com/anniedoris/design_qa/tree/dd909455afb9a6023917b3b68fc88dab943721a1). Recursive GitHub tree inspected at the commit; tags and releases endpoints returned empty lists on 2026-10-06. No license or changelog file was found in this inventory. This is a bounded file/document check, not a legal conclusion or proof that no policies exist elsewhere.

<a id="source-DQ-OUT"></a>

- **DQ-OUT** [DesignQA: Released LLaVA retrieval predictions](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/rule_extraction/retrieval_evaluation_llava-13b.csv). CSV inspected: 1,190 rows, with question, ground_truth and model_prediction columns. Establishes that some predictions are available. Its row count differs from the paper’s 1,192 retrieval questions, so it is not assumed to be a complete, exact paper-run archive.

<a id="source-DQ-FIX"></a>

- **DQ-FIX** [DesignQA: Presence-scoring test data](https://github.com/anniedoris/design_qa/blob/dd909455afb9a6023917b3b68fc88dab943721a1/eval/metrics/eval_metric_test_presence.csv). Seven rows inspected, including prediction, answer and category columns. The metrics file also contains commented test calls. Test data exist; no executed assertion suite or published scorer error rate was established.

<a id="source-DQ-WEB"></a>

- **DQ-WEB** [DesignQA: Official project website](https://design-qa.github.io/). Landing-page text was readable on 2026-10-06. The web extractor did not expose a leaderboard table or its rules. This access limit is not proof that the leaderboard is absent or broken.

<a id="source-ABRAND"></a>

- **ABRAND** [ARC Prize official website and logo](https://arcprize.org/). The ARC-AGI-2 header uses the official ARC Prize organization logo. The HLE header logo and classics example come from the official HLE website (HW). Images are included for identification and explanation.
