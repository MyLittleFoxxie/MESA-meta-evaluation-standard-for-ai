# Comparison with prior REFSQ technical papers

Reviewed on 9 November 2026. This is an assistant review, not a conference decision or evidence from readers. It compares the current `mesa_paper.tex` and `paper2.tex` with two accepted REFSQ Technical design papers. No manuscript, protocol, rating form, or experiment was changed. Current manuscript layout and page length remain unchecked.

## Sources and scope

Both papers appear as **Technical design** in the [official REFSQ 2024 research track](https://conf.researchr.org/track/refsq-2024/refsq-2024-papers). They are research track papers, not workshop papers or research previews. I read their full public manuscripts, including methods, findings, limitations, and references. Page numbers below refer to those manuscripts, which can differ from the published chapters.

1. Rebekka Wohlrab, Michael Vierhauser, and Erik Nilsson. **What Impact Do My Preferences Have? A Framework for Explanation-Based Elicitation of Quality Objectives for Robotic Mission Planning** (2024). [Author manuscript](https://rebekkaa.github.io/files/2024_REFSQ_OBJUST.pdf); [official paper and track record](https://2024.refsq.org/details/refsq-2024-papers/6/What-Impact-do-my-Preferences-Have-A-Framework-for-Explanation-Based-Elicitation-of-); [published chapter](https://doi.org/10.1007/978-3-031-57327-9_7).

   Pages 3–4 introduce a planning example before the framework. Section 3 explains the research process; Section 4 connects requirements to implementation. Figures 2–4 separate architecture, domain model, and interface. Section 5 reports seven evaluation participants. Sections 6–7 state limits and future evaluation. The introduction lists three contributions. This is a useful comparison for explaining an artifact and its evaluation, not a license to claim human benefits without a human study.

2. Quim Motger, Xavier Franch, Vincenzo Gervasi, and Jordi Marco. **Unveiling Competition Dynamics in Mobile App Markets Through User Reviews** (2024). [Full manuscript](https://arxiv.org/pdf/2312.01981); [institutional publication record](https://upcommons.upc.edu/entities/publication/fff86114-814c-4298-96bd-496440ac9854); [published chapter](https://doi.org/10.1007/978-3-031-57327-9_16).

   Sections 2.1–2.3 state the question, stakeholders, and case before Section 3 presents the approach. Figure 1 gives a four stage overview. Section 4 separates design from results; Section 5.1 returns to the question and distinguishes correlation from cause. Page 3 uses a shaded RQ callout. Page 8 boxes an output example. These two pages were inspected visually. This is a useful comparison for connecting a technical method to an RE activity and preserving the limits of inference.

The conference required four abstract parts and LNCS formatting in 2024. Both examples use those abstract parts and numbered sections. Historical submission limits and published chapter lengths are not evidence of the rules for the intended submission year. Two accepted papers also cannot establish which presentation choice caused acceptance. Neither paper is a template whose claims or wording should be copied.

## Changes ranked by value

### 1. Make the evidence boundary consistent before polishing

In [paper2.tex](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:352), the discussion says the gate prevents premature acceptance and protects procurement. The conclusion at line 386 says its effect remains untested. Present the gate's behavior as a property of the rules; reserve claims about better decisions for observations that test them. The 17 exploit findings also need their issue scope restriction wherever cited: only six are counted as task defects in the current forms, as explained at line 245.

In [mesa_paper.tex](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:271), “never confused” claims more than recording a qualifier can establish. State that the record distinguishes an absence from a finding of a defect. A reviewer or reader can still misunderstand it. This correction matters more than changing boxes or captions.

### 2. Introduce one example before the terminology and reuse it

For MESA, introduce a benchmark review item where no check is reported, alongside an item where a check found a defect. Carry those records through mapping, evidence level, check outcome, and verdict. Only later show what each would mean for a requirement. This would give the terms at [line 134](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:134) a referent before the reader meets the ten term introduction, which currently contains eleven bullets.

For Paper 2, retain the requirement at [line 41](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:41), then move the task explanation from line 232 forward. Follow one explicitly constructed case from tests passed to the interval and evidence status. Use the existing case at line 220 as a starting point. Do not invent an experimental result to complete the example.

### 3. Shorten the abstract without removing study status

A rough whitespace count after removing LaTeX command names gives 361 words for MESA and 511 for Paper 2, excluding keywords. These are editing estimates, not typeset word counts or a submission compliance check.

In [MESA's abstract](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:25), keep the decision problem, mapping and rubric, study scope, one or two findings, and the limit on requirements claims. Move the architecture vocabulary to the method.

In [Paper 2's abstract](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:25), keep the gap, executable method, completed checks, and explicit statement that study sessions have not run. Move the session budget, all numerical acceptance cutoffs, and the catalogue of record checks to the evaluation. Correct the last sentence saying rating observations remain future work when rating runs are already described as completed. Aim first for about 250–300 words, then check the intended year's rules; this target is editorial advice, not a verified limit.

### 4. Show the procedure before its implementation controls

Add one overview to each manuscript. For MESA: source items → comparison concerns → review records → framework comparisons and rubric ratings. Mark the requirements application as a proposal outside the completed evaluation. For Paper 2: requirement and task sets → checks and reviews → recorded forms → score and evidence status → comparison with the direct test.

At [paper2.tex:227](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:227), keep sample sizes, phase ordering, invalid session handling, and who authorizes phases. Move exclusive file creation, command launch mechanics, and detailed slot bookkeeping to the runbook or supplement, with a pointer. Preserve every control in the research records. This is a presentation change, not a protocol change.

### 5. Give each question an answer and its limit

In [mesa_paper.tex:256](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:256), organize results by the three stated questions. State what “unification” was checked and what remains a design claim; counting allocations is not proof that all meanings were preserved. Separate agreement between framework verdicts from repeatability of rubric ratings.

For Paper 2, prepare RQ1 and RQ2 result tables without filling them from simulations. RQ1 should distinguish a changed score decision, a withheld decision, and a caveat. RQ2 should report both cases, including inconclusive or withheld outcomes, rather than imply a validation rate. Keep the simulation under its assumptions. Neither comparison paper establishes that every result section must be titled with an RQ; that is a recommendation for these manuscripts because their claims currently span several sections.

### 6. Use emphasis to identify questions or records, not enlarge claims

There is observed REFSQ precedent for an RQ callout, so the current RQ boxes need not be removed merely for being boxes. The comparison does not establish a convention requiring them. Prefer one consistent style and remove the redundant “Research Questions Summary” line if it adds no content.

The prior papers' text does not use a practitioner mandate box like [paper2.tex:361](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:361). Replace its “Never” instruction with a paragraph explaining what the rules require and what the study has not tested. The findings box at line 254 should separate executed checks from the calculation; sample size uncertainty is not an observed benchmark vulnerability. Retain emphasis only where it helps identify an input, output, or bounded result.

## Proposed order before Paper 2 execution

1. Settle each paper's contribution in one paragraph: MESA compares review practices and defines records; Paper 2 implements requirements decisions and tests their relationship to a direct test.
2. Correct claims and counts that change the reader's interpretation, especially six versus 17 task defects, completed versus pending ratings, and withholding versus improvement.
3. Add the example and overview, then reduce abstract and implementation detail. Preserve the protocol and saved outputs.
4. Map each RQ to its input, analysis, output, and limit. Confirm that already known withholding under both policies still leaves the proposed experiment able to answer its stated questions. If that requires a procedure change, amend the protocol and runbook before signing or freezing.
5. Perform manuscript checks without compiling LaTeX. Leave layout and page length unchecked. Signing, freezing, and experiment authorization are subsequent actions, not outcomes of this comparison.
