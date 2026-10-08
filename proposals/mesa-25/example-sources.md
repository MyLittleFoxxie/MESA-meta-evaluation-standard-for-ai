# Sources for the DesignQA examples

These are short factual illustrations, not complete answers or ratings. Review gaps describe the material inspected for the June 2026 review; they do not establish current conditions.

- [Paper: DesignQA (2024)](../../literature/DesignQA.md).
- [MESA review: DesignQA (June 2026)](../../reviews/gemini_supervising_editor/DesignQA.md).

| Question | Example | Source section |
| --- | --- | --- |
| Q1 | DesignQA: 2024 paper, public test questions and software that calculates scores. | Review: 1.2 |
| Q2 | DesignQA tests AI understanding of engineering rules and drawings. | Paper: 1 Introduction |
| Q3 | DesignQA asks whether a pictured vehicle part meets a rule. | Paper: 3.1.4 |
| Q4 | DesignQA tests AI systems without showing them worked examples. | Paper: 1 Introduction (zero-shot evaluation) |
| Q5 | DesignQA scores yes/no answers as correct or incorrect. | Paper: 3.2 Evaluation Metrics |
| Q6 | DesignQA tests applying engineering rules by asking whether vehicle designs meet them. | Paper: 3.1.4 |
| Q7 | DesignQA uses real racing rules and student-built vehicle designs. | Paper: 3.1 The Dataset |
| Q8 | DesignQA used two extra reviewers for human-written questions, with some exceptions. | Paper: 3.1 The Dataset |
| Q9 | DesignQA covers six kinds of problems from one racing rulebook. | Paper: 3.1 The Dataset; Limitations |
| Q10 | DesignQA answers can lose points for missing commas. | Paper: Limitations |
| Q11 | DesignQA review: relationships between scores for its six types of problems were untested. | Review: 10.2.1 |
| Q12 | DesignQA review: software-generated explanation scores lacked checks against human marking. | Review: 10.3.1 |
| Q13 | DesignQA review: no human scores were available for comparison. | Review: 8.1.2 |
| Q14 | DesignQA tested one AI model five times, changing the supplied rule passages. | Paper: 5 Discussion, Effect of RAG Implementation |
| Q15 | DesignQA compared results with and without added image labels. | Paper: 5 Discussion, Effect of Additional Context |
| Q16 | DesignQA review: main results lacked estimates of how much the scores could vary. | Review: 9.2.2 |
| Q17 | DesignQA: always answering “yes” works for drawings with scale bars (lines showing distance). | Paper: 3.1.4 |
| Q18 | DesignQA used new vehicle images, but publicly available competition rules. | Paper: 1 Introduction; 3.1 The Dataset |
| Q19 | DesignQA’s paper suggests training AI on its questions about finding rules. | Paper: Future Work: Recommendations for Models for This Benchmark |
| Q20 | DesignQA’s paper says performance on other rulebooks remains unknown. | Paper: Limitations |
| Q21 | DesignQA’s AI systems received either the whole rulebook or selected passages. | Paper: 4.1.3 RAG |
| Q22 | DesignQA provides public questions and software that calculates scores. | Review: 5.7; 7.1.4 |
| Q23 | DesignQA’s June 2026 review found no license stating permission to reuse the shared materials. | Review: 1.2; 7.1.8 |
| Q24 | DesignQA’s June 2026 review found no formally labeled releases or record of changes. | Review: 5.8 |
| Q25 | DesignQA’s paper acknowledges that its six kinds of problems omit other engineering tasks. | Paper: Limitations |

Q8: the paper excludes derivative questions and Rule Compliance explanations from its two-reviewer procedure. Q14: the five runs varied the supplied rule context; they were not five identical-condition repeats. Q17: the design fact is documented; calling it a possible shortcut is an inference, not evidence that models used it. Q15: the added context included both image highlighting and component names.
