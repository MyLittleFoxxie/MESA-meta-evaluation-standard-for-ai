# MESA Thesis Plan

Updated: 2026-09-25. This plan guides a master’s thesis, with no fixed deadline or current access to experts. The first revision is recorded below.

## Writing rules

Apply these rules to this plan, future edits to it, and the thesis revisions:

- Be brief. Use familiar words and short sentences.
- Say what to do, why it matters, and what to record.
- Avoid promotional language and vague phrases such as “systematically” or “evidence changes.” Describe the actual action.
- Explain necessary technical terms when first used. Use a small example when it helps.
- Distinguish planned work from completed work, and findings from assumptions.

## Thesis aim

Explain how EFPA was adapted for reviewing AI benchmarks, then test what works and what needs improvement.

MESA should help a reviewer answer: **What do this benchmark’s scores allow us to conclude, and what remains uncertain?**

The thesis can examine this through the author’s own applications. Showing that other reviewers can use MESA easily and reach similar ratings requires a later study with participants. Agree on the thesis scope with the supervisor.

Possible title: **MESA: Adapting and Testing an EFPA-Based Framework for AI Benchmark Review**.

## Research questions

1. How should EFPA’s questions be adapted to AI benchmarks, and why?
2. What works, what is unclear, and what takes too much effort when applying MESA?
3. Does the revised MESA work as expected on new benchmarks and small examples designed to test specific questions?

## Steps

### 1. Define the purpose

Write one page stating who MESA is for, what decisions it helps with, and what a finished review contains. Explain what the thesis will test and what would count as a problem.

**Result:** an agreed purpose and research questions.

### 2. Record what already exists

List the versions of the template, scorecard, and reviews. Keep the original reviews unchanged.

HLE, ARC-AGI-2, and DesignQA helped shape MESA. They show how it was developed, but cannot also serve as independent tests. Their reviews used an earlier template version.

Distinguish reasons recorded during development from explanations written now.

**Result:** a short record of versions and past work.

### 3. Check why each question belongs in MESA

Start with Section 9 on reliability, then apply the same check to the rest. For each question, record:

- Where it came from: EFPA, BetterBench, another paper, or the author.
- What changed from the source and why.
- What the reviewer needs to read and how the answer helps their conclusion.
- When it applies and whether another question repeats the same judgment.
- Whether to keep, clarify, combine, or remove it.

A narrow benchmark does not need to measure general intelligence. Requirements should match the claim being reviewed.

**Result:** a table explaining the questions and proposed changes.

### 4. Learn from the existing reviews

Compare the original reviewer drafts with the final reviews. Identify disagreements, unclear instructions, missing information, repeated work, and conclusions unsupported by their sources.

For example, if one reviewer gave a 1 and another a 2, check whether they used different facts or understood the rating instructions differently. The editor choosing one rating does not prove that the instructions were clear.

Record cases where MESA supports a benchmark’s claims as well as cases where it finds problems. Connect each proposed change to an observed problem. Label this as an analysis of past work; do not invent timing data from memory.

**Result:** a list of lessons and reasons for revising MESA.

### 5. Make MESA easier to use

Shorten repeated instructions, separate optional explanations from required answers, and reuse source notes across questions. Keep item numbers stable.

Treat the 40-question scorecard as a draft to test. Do not assume it is short enough or that it retains every important question.

During new applications, record time spent finding sources, making judgments, and writing. Note confusion and omissions too. The author’s times will not represent an unfamiliar reviewer’s experience.

**Result:** a revised version and a record of effort and difficulties.

### 6. Test that version

Keep the version unchanged during testing. Before starting, write down the examples, expected results, reasons for those expectations, and what would count as failure.

Try two different benchmarks outside the 15 used to develop MESA, if possible. Explain the choices and any prior familiarity. Two cases cannot represent all benchmarks.

Also use a few clearly labeled fictional examples:

- Keep a science quiz unchanged, but change its claim from “science knowledge” to “general reasoning.” Does MESA ask for stronger support for the broader claim?
- Add a study showing that an automated scorer agrees with qualified human graders. Does the relevant judgment improve for a clear reason?
- Compare “no information about repeated runs” with “repeated runs showed unstable scores.” Does MESA distinguish uncertainty from a demonstrated problem?
- Include a benchmark with good support for its narrow claim. Can MESA recognize that support?

Check the reasons behind judgments, not just whether numbers match your expectations. Report failures and unclear results. Record later fixes as a new version. Examples designed and judged by the author provide limited checks, not independent validation.

**Result:** a report of what passed, failed, or remains uncertain.

### 7. Revise the paper

Explain how MESA was built, what the applications taught you about it, and what the new tests showed. State which work was done by the author and which used AI. Testing the AI review process itself is a separate project.

Keep benchmark findings as examples, but make the evaluation of MESA a main result. Answer each research question with the work actually completed.

Revisit these claims in `paper.tex`:

| Current wording | Revision needed |
| --- | --- |
| “Replicable quality standard” | Describe the proposed framework and what was actually tested. |
| “Help ensure” robustness or freedom from contamination | Say it checks the available information; it cannot guarantee these properties. |
| “Establishes feasibility and coverage” | State where MESA was applied and which questions it could address. |
| “No two items now share a role” | Report the specific repetitions found and removed. |
| “Accelerates” | Remove unless a comparison shows time saved. |
| “Minimum set of criteria” | Describe what the cases suggest and when each criterion applies. |
| “Measures the quality” | Explain that MESA helps judge whether particular uses of scores are supported. |

Describe the scorecard as already available, while making clear that its usefulness still needs testing.

**Result:** a paper whose claims match its findings.

## What this study can establish

It can explain the adaptation, show how MESA works in the tested cases, and identify problems and improvements. It cannot establish that different people agree, that MESA is better than other methods, or that it is ready for certification. Expert review and studies with other users remain future work.

## Progress on 2026-09-25

- Wrote the [purpose statement](thesis/purpose.md) and revised the paper’s research questions.
- Recorded starting versions and preserved all nine original reviews.
- Mapped the active questions to related sources; listed unresolved design choices.
- Compared the pilot ratings and reasons, then clarified the framework instructions.
- Added a short guide and regenerated the scorecard. No human time saving has been measured.
- Recorded four fictional checks and two partial real-case applications, performed by the AI assistant.
- Revised the paper’s methods, results, claims and limitations to match that work.

**Still needed:** the author’s check of the new source mapping and findings, full applications to the two new benchmarks, and recorded human review effort. Supervisor agreement and independent reviewer studies have not occurred. The plan is therefore partly completed; the limited AI checks do not replace the remaining research.

**Next action:** the author should read [thesis/README.md](thesis/README.md), check the proposed source mappings, and perform a full application while recording effort.

## Method references

- [FEDS](https://doi.org/10.1057/ejis.2014.36): planning evaluations that help improve a framework and test its use.
- [Kane](https://doi.org/10.1111/jedm.12000): choosing validation evidence based on what the ratings are intended to mean and how they will be used.

These sources guide the approach; they do not prescribe the proposed number of cases.
