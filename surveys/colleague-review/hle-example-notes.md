# HLE worked example — source and comparison notes

Prepared 18 October 2026 from the HLE passage and primary-source records inspected on 7 October 2026. No fresh benchmark run or new source inspection is claimed.

The 25 answers are reviewer judgments for a teaching example. They are not EFPA ratings, an expert consensus, a correct-answer key or a validated replacement for the long review. The participant form now leaves ARC-AGI-2 and DesignQA unanswered.

## Comparison with supporting detailed reviews

The example retains the detailed reviews’ central limits: unvalidated AI judging, limited evidence of repeated-run stability, deliberately difficult academic sampling, constrained comparisons and unsupported interpretation as general intelligence or independent research. It does not mechanically translate numerical ratings into choices.

Where an existing review refers to answer-key error percentages, this example uses the supplied paper’s expert-disagreement statement rather than calling disagreement confirmed error. Where a full review criticizes missing headline uncertainty reporting, the example also records that the inspected code calculates an approximate confidence range; these concern different reporting contexts. Missing evidence of a study yields Not sure where the question asks whether that study happened. Describing a process can earn Yes without validating that process. These distinctions prevent apparent agreement from overriding the inspected facts.

## Selected responses and source records

| Question | Answer | Why | Sources |
| --- | --- | --- | --- |
| 1 | Yes | The passage identifies original HLE and its 2,500 questions. A judging AI compares responses with reference answers, and accuracy is the percentage marked correct, so both the test and its scoring method are described. | HP, HW |
| 2 | Yes | HLE tests academic knowledge and reasoning in AI systems that handle text or text and images. Its scores are intended to compare these systems on academic questions; they do not by themselves establish research ability or general intelligence. | HP |
| 3 | Yes | The AI receives a question, sometimes with an image, and selects an option or gives a short answer. The evaluation software asks for an explanation, a final answer and a percentage stating confidence. | HP |
| 4 | Partly | The software describes the instructions and a temperature setting of zero to reduce randomness. However, the line that sends that setting is disabled in the inspected code, so the description does not establish that it was used. | HM, HR |
| 5 | Yes | An AI judge compares each final answer with a reference, accepting equivalent meanings. The code reports the percentage marked correct, a confidence range and how stated confidence compares with accuracy; describing these calculations does not establish that they work well. | HJ |
| 6 | Yes | The paper uses specialist academic questions with definite answers to test knowledge and reasoning that existing AI models struggle with. This explains the choice of tasks, but does not establish coverage of every academic ability. | HP |
| 7 | Partly | Experts contributed questions, and questions that selected AI models could already answer were screened out. This explains how difficulty was chosen, but does not show that the resulting set represents academic work more generally. | HP |
| 8 | Yes | Expert review and organizer approval were followed by two checks of 200 questions each, examining questions and reference answers. The reported 15.4% expert disagreement limits confidence in the answers, but does not negate that checking occurred. | HP |
| 9 | Partly | The questions span many subjects but emphasize mathematics and require definite answers. This covers some academic knowledge and reasoning, while creative work and research without a fixed answer fall outside the format. | HP |
| 10 | Partly | The judge accepts responses that mean the same thing as the reference answer, allowing differences in wording. However, it compares answers without independently solving the problem, so a mistaken reference or judging decision can affect the score. | HJ, HP |
| 11 | Partly | Every question counts equally toward accuracy, so subjects with more questions contribute more to the total. Results are also reported by subject, but the supplied material does not establish that these subject scores measure separate abilities. | HP, HJ |
| 12 | Not sure | The code shows how the AI judge compares responses with reference answers, but no full comparison with expert marking is supplied. Expert checks of the questions do not establish whether this judge marks AI responses correctly and consistently. | HJ, HP |
| 13 | Partly | The paper compares AI models on the full question set and separately on questions using only text. These provide context, but no matched group of people takes the whole exam under the same conditions, limiting comparisons with human performance. | HP |
| 14 | Not sure | The paper acknowledges that an AI can answer differently on separate attempts. The supplied sources do not establish repeated testing of the same systems for the main comparisons, so the size of score changes remains unknown. | HP, HM |
| 15 | Not sure | The supplied sources do not establish systematic tests of reworded instructions or changes to the judging AI. Describing one instruction and testing setup does not show how much scores change when those conditions change. | HP, HJ, HM |
| 16 | Partly | The code estimates a 95% confidence range from the number of questions and the fraction marked correct. It does not measure changes from rerunning the AI or replacing the judge, so it covers only some uncertainty in comparisons. | HJ |
| 17 | Partly | Contributors were asked to avoid questions answered by a simple lookup and could update questions answered through faulty reasoning. These checks address some shortcuts, but guessing remains possible and the supplied material does not measure every route to points. | HP |
| 18 | Partly | HLE keeps some questions private, marks public test data and warns against using it for training. These measures help limit data contamination, but the supplied information does not show whether an AI was trained on any of the public questions or answers. | HP, HR |
| 19 | Not sure | The instructions discourage training on test questions. However, the supplied material lacks a complete policy covering repeated submissions, access to feedback and reporting systems trained for HLE, leaving insufficient information to judge whether the rules support the intended comparisons. | HR |
| 20 | Not sure | The supplied passage reports no measured relationship between HLE scores and success on independent scientific projects. Academic question scores therefore leave that broader claim unresolved; missing evidence does not prove that an AI cannot conduct research. | HP |
| 21 | Partly | Results using only text are labelled separately from results that include images. This helps compare systems receiving similar information, but English questions, unequal subject coverage and missing studies across languages leave other fairness claims unresolved. | HP |
| 22 | Partly | The instructions and marking code are public, allowing readers to inspect the procedure. Downloading questions requires accepting access conditions, and a separate private question set is withheld, so not all materials are available to examine or repeat every result. | HR, HC, HJ |
| 23 | Partly | The dataset and code list MIT licences, access requires accepting conditions, and the paper describes excluding dangerous content. However, the dataset also asks users not to redistribute questions, leaving some reuse expectations unclear alongside the licence. | HC, HL, HP |
| 24 | Not sure | HLE-Rolling records removed and restored questions, but it is separate from original HLE. The supplied material does not establish how changes to original HLE affect comparisons between earlier and later scores. | HW, HU |
| 25 | Partly | The paper says high scores alone do not establish general intelligence or independent research ability. However, the title “Humanity’s Last Exam” can suggest broader coverage than a set of academic questions with definite answers supports. | HP |

Source IDs resolve through `packet.json`. Detailed reviews remain unchanged in `reviews/`; the original DesignQA example remains unchanged in `proposals/mesa-25/`.


Version 2.3, 26 October 2026: explanations expanded using the supplied passages. Answer selections and source inspection dates are unchanged. Version 2.2 is archived; frozen model study examples remain unchanged.


Version 2.4, 26 October 2026: Q18 now separates measures limiting exposure from knowledge of an AI’s training. Participant wording uses ability and abilities, matching `paper_chase.tex`. Source titles, original records, question texts and answer selections are unchanged. Version 2.3 is archived.

Version 2.8, 26 October 2026: Current survey text uses data contamination in place of exposure. HLE judgments and source inspection dates are unchanged; historical notes retain their wording.

Version 2.9, 26 October 2026: Natural reading passages and questions with official source tables; unhyphenated common terminology. HLE judgments and source inspection dates are unchanged; historical notes retain their wording.
