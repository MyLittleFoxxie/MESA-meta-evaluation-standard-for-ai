# Method reporting for the accessibility-guidance experiment

This study extends the project’s [ACM SIGSOFT standards assessment](../../../simulation-study/analyst/standards-assessment.md). It uses the General and Engineering Research standards, and relevant Benchmarking attributes for an automated, repeatable comparison. It does not claim to be a human usability experiment or quantitative simulation of people.

| Concern | Implementation and limit |
| --- | --- |
| Research purpose | Test a specified guidance package for the unchanged questionnaire; accessibility is an intended human benefit, not measured here. |
| System and workload | One requested language model with four instruction packages; fixed published-benchmark passages and 16 constructed cases, 32 claims. These tasks do not run the benchmarked AI systems. |
| Fair comparison | Same benchmark evidence, intended uses, neutral instruction and five repetitions. Original and revised MESA differ only in help, comment prompts and reminders. Only MESA has the HLE example; other packages differ in length and output requirements. |
| Measures | Expected-answer matches by conversation and family, a predefined indicator of unjustified support for particular negative claims, paired-case responses, categorical MESA distributions and repeated-choice matches. No total benchmark-quality score. |
| Repetition | Five independent conversation contexts per batch and method; shared model, passages and case claims prevent treating their answers as independent participants. No statistical-power or long-term-stability claim. |
| Reproducibility | Frozen prompts, keys, source fingerprints, model request, exposed settings, raw outputs, execution events and failures. Backend revision, temperature and generation seed unavailable. Scheduling seed is separate. |
| Construct limits | Matching assistant-prepared answers on constructed cases does not establish complete review correctness. Case construction reused known conceptual difficulties; the same assistant designed and interpreted the study. A perfect result cannot distinguish methods. |
| Review illustrations | Eight fixed first responses read in full against a predefined checklist. Invalid formats are labeled and not replaced. These interpretations are not independent expert judgments or general omission rates. |
| Human claims | No measured human duration, comprehension, usefulness, perceived ease, accessibility compliance or decision benefit. HTML behavior checks verify interface mechanics only. |
| Transparency | Raw malformed responses and failures retained; structured-analysis exclusions follow the frozen protocol. No pooling with earlier series. Equal or worse results reported. |

The revised MESA text contains more explanation than the original. Shorter than the EFPA-TRM source is not equivalent to easier than the original MESA guidance. The static prototype permits help to remain closed, whereas model conversations receive the complete text. These are different questions for future human research.
