# HLE worked example — source and comparison notes

Prepared 18 October 2026 from the HLE passage and primary-source records inspected on 7 October 2026. No fresh benchmark run or new source inspection is claimed.

The 25 answers are reviewer judgments for a teaching example. They are not EFPA ratings, an expert consensus, a correct-answer key or a validated replacement for the long review. The participant form now leaves ARC-AGI-2 and DesignQA unanswered.

## Comparison with supporting detailed reviews

The example retains the detailed reviews’ central limits: unvalidated AI judging, limited evidence of repeated-run stability, deliberately difficult academic sampling, constrained comparisons and unsupported interpretation as general intelligence or independent research. It does not mechanically translate numerical ratings into choices.

Where an existing review refers to answer-key error percentages, this example uses the supplied paper’s expert-disagreement statement rather than calling disagreement confirmed error. Where a full review criticizes missing headline uncertainty reporting, the example also records that the inspected code calculates an approximate confidence range; these concern different reporting contexts. Missing evidence of a study yields Not sure where the question asks whether that study happened. Describing a process can earn Yes without validating that process. These distinctions prevent apparent agreement from overriding the inspected facts.

## Selected responses and source records

| Question | Answer | Why | Sources |
| --- | --- | --- | --- |
| 1 | Yes | The passage identifies original HLE, its 2,500 questions and the inspected scoring software. This tells readers which test and scoring method the example concerns. | HP, HW |
| 2 | Yes | HLE describes difficult academic knowledge and reasoning, the AI systems it targets and the comparisons it is intended to support. | HP |
| 3 | Yes | The passage describes short-answer and multiple-choice questions, images when needed, and the answers the AI must return. | HP |
| 4 | Partly | The instructions and software are described, but the advertised setting to reduce randomness is disabled in the inspected code. A reader cannot assume that setting was used. | HM, HR |
| 5 | Yes | The public code explains how a judging AI marks answers and how accuracy and confidence-related results are calculated. Describing these rules does not establish that they work well. | HJ |
| 6 | Yes | The paper explains why hard, specialist questions with definite answers are used to assess academic knowledge and reasoning. Whether they cover the full claim is a separate question. | HP |
| 7 | Partly | Experts contributed questions and the authors explain the difficulty screening. However, selecting questions that AI systems struggle with does not show that the set represents academic work more generally. | HP |
| 8 | Yes | Expert review and later checks examined the questions and supplied answers. Remaining expert disagreement limits confidence in those answers, but does not undo the evidence that checking occurred. | HP |
| 9 | Partly | The questions cover many subjects, but emphasize mathematics and require definite answers. They therefore cover some academic skills while leaving creative work and open-ended research outside the format. | HP |
| 10 | Partly | The judging AI accepts answers with the same meaning as the reference. However, a wrong reference or an incorrect judging decision can still affect the mark, so understanding is not the only possible influence. | HJ, HP |
| 11 | Partly | Each question counts equally, so the subject mix affects the overall score. The inspected material does not establish that the subject scores are separate measures of distinct skills. | HP, HJ |
| 12 | Not sure | The judging code is public, but no full comparison of its marks with expert marks is supplied. Checking the questions is different from checking whether the judging AI marks responses correctly. | HJ, HP |
| 13 | Partly | Named AI models provide useful comparison points, and text-only results are labelled. However, there is no matched group of people taking the whole test under the AI conditions. | HP |
| 14 | Not sure | The paper notes that answers can change between attempts, but the supplied sources do not establish a repeated-run study for the main comparisons. That leaves the amount of variation unclear. | HP, HM |
| 15 | Not sure | The supplied sources do not establish systematic tests of reworded instructions or changes to the judging AI. A standard instruction alone does not show what happens when the setup changes. | HP, HJ, HM |
| 16 | Partly | The code calculates an approximate confidence range, but it does not cover changes from repeating the run or changing the judge. It therefore describes only some of the uncertainty relevant to comparisons. | HJ |
| 17 | Partly | Contributors were asked to avoid easy lookups and could revise questions answered through faulty reasoning. These checks address some ways to gain points, but do not measure every possible route. | HP |
| 18 | Partly | A private set, a training-data marker and warnings help address prior exposure. They do not establish which questions a particular AI has already seen. | HP, HR |
| 19 | Not sure | Training on the test is discouraged, but the supplied material lacks a complete policy on repeated submissions and feedback. There is not enough information to judge whether those rules are suitable. | HR |
| 20 | Not sure | The passage supplies no measured link between HLE scores and success on independent scientific projects. This leaves wider performance claims unresolved rather than proving they are false. | HP |
| 21 | Partly | Text-only results are distinguished from results using images, which helps readers compare like with like. Unequal subject coverage and limited checks across languages leave other comparisons less well supported. | HP |
| 22 | Partly | Instructions and marking code are public, but the dataset is gated and the private set is unavailable. These materials support inspection without providing everything needed to examine all results. | HR, HC, HJ |
| 23 | Partly | Licences, access conditions and harmful-content precautions are described. The combination of a licence and a request not to redistribute the data leaves some reuse expectations less clear to readers. | HC, HL, HP |
| 24 | Not sure | Changes to HLE-Rolling are described, but that is a separate test. The supplied material does not establish how changes to original HLE affect comparisons of old and new scores. | HW, HU |
| 25 | Partly | The paper explicitly limits claims about general intelligence and independent research. However, the broad title can suggest more than the definite-answer academic questions establish. | HP |

Source IDs resolve through `packet.json`. Detailed reviews remain unchanged in `reviews/`; the original DesignQA example remains unchanged in `proposals/mesa-25/`.
