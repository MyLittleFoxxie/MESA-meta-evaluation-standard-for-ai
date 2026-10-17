# ACM SIGSOFT Empirical Standards assessment

Prepared 14 October 2026 after three real runs completed and before the remaining scheduled runs completed. This reporting assessment does not amend frozen prompts or expectations. It is not a retrospective preregistration claim.

Sources: [General and Benchmarking](https://www2.sigsoft.org/EmpiricalStandards/docs/standards?standard=Benchmarking) and [Engineering Research](https://www2.sigsoft.org/EmpiricalStandards/docs/standards?standard=EngineeringResearch), accessed 14 October 2026. IEEE is the paper format; ACM SIGSOFT standards guide research methods independently of formatting.

## Applicability

The contribution proposes a method (engineering research) and compares configurations of a language-model review system on fixed workloads (benchmarking). The actual system is run; it is not replaced by a calibrated simulation of that system. The persona descriptions do not constitute validated quantitative models of people, and the human-experiment standard is not claimed. No workplace organization is observed, so the real benchmark passages are application examples, not organizational case studies.

## Essential attributes and implementation

| Attribute | Implementation | Limit or status |
|---|---|---|
| Defined purpose and proposed artifact | Three RQs, 25 exact questions, categorical meanings and domain mapping | Human usefulness remains untested |
| Justified existing task selection | ARC-AGI-2 contrasts grid reasoning with engineering-document tasks in DesignQA; both have fixed participant-facing passages | Purposive selection of only two benchmarks; not representative |
| Quality and measures | Selected evidence distinctions: per-session matches to 17 predefined statements; response completeness; categorical repeat agreement | No total benchmark-quality score; not human correctness or usability |
| Repeatable workload | Immutable 120 input files, role prompts, original EFPA source, source hashes | Text extraction and text-only figure descriptions may omit visual information |
| Fair comparisons | Same reviewed passages, intended uses, model, effort and common conclusions; credible ordinary-review prompt; full EFPA source and complete item coverage requested | MESA alone includes a teaching example; comparison is between packages. Dense short passages may favor concise review. Coverage failures must not be hidden |
| No artificial disadvantage | No instrument-specific wall-clock/output cap; common runner timeout 1,200 seconds; original EFPA all 90 pages provided; grouping allowed only with explicit IDs and rationale | All methods restricted to supplied passages because that is the defined task; no claim about unrestricted source gathering. Report any timeout/truncation |
| Repetitions and stability | Five fresh repeats per condition/role/batch, individual outputs and exact agreement retained | Five is an exploratory budget choice, not a proven sufficient sample. Report variation and avoid long-run stability or significance claims |
| Construct validity | Distinguish supported claims, documented problems and missing information; separate mere repetition from favorable stability; compare changed and unchanged evidence | Fictional cases authored by the same assistant; explicit cues, narrow coverage and ceiling effects possible. They are diagnostic checks, not a validated quality benchmark |
| Conceptual evaluation | Explain transfer, combination, simplification, omissions and AI-specific additions from EFPA | Correspondence is argued, not independently certified |
| Relevant comparison | Original EFPA and competent ordinary review alongside MESA | EFPA is not a gold standard for AI; do not map numerical ratings to categories |
| Raw results and offline analysis | Inputs, event logs, responses, metadata, exact key and deterministic analysis files saved | No aggregate-only collection; missing/invalid outputs separate |
| Transparent problems | Process exit, parsing/format errors, tool violations and missing jobs recorded | Infrastructure failures are not benchmark judgments |
| Explicit assumptions | Fixed order, same-model dependence, role instructions, no use of human labels as real participant attributes | No human generalization or independent-model replication claim |

## Desirable properties

The materials and scripts are stored in the repository in reusable form; an anonymized artifact copy is still needed before submission. Second-model confirmation and independent replication are unperformed. There is no independent maintenance organization or demonstrated user community. Absence of those properties is reported without claiming it alone invalidates a new method.

## Antipattern checks

- Do not tune cases or key after observing answers, or select favorable runs. Frozen inputs remain unchanged.
- The simple fictional cases cannot carry the entire evaluation. Report their scope alongside the real reviews, not as broad evidence of quality.
- Do not claim the benchmark is independent of MESA's design: its diagnostic distinctions were chosen to examine the adaptation. General evidence distinctions and a credible ordinary-review control reduce but do not eliminate this concern.
- Do not infer human workload savings from question counts or model execution time.
- Do not conceal unresolved standards limitations behind a statement of blanket compliance.

## Final execution status, 15 October 2026

Sol completed all 120 planned jobs through 125 physical attempts, retaining five infrastructure failures and their single retries. Two completed EFPA responses failed the required conclusion structure; 118 sessions enter structured analysis. All 60 controlled sessions matched all 1,020 expected labels, producing a ceiling across conditions. All 20 MESA real sessions produced 1,000 selections, with variation in 12 of 50 question–benchmark combinations. These observations do not resolve independent validation, broader workload coverage, sufficient long-run repetition, human usefulness, or complete original-EFPA coverage. The additional Astra series remains incomplete (14 completed, 106 failed) and is reported separately.
