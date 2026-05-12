# MESA EFPA Coherence Audit Memo

Date: 2026-05-06

## Scope

This memo assesses whether `markdown/MESA EFPA template.md` and
`markdown/MESA EFPA template guide v3.md` form a coherent, usable adaptation of
the EFPA test-review model for AI benchmark review. The user-supplied filled
review of the Emotional Processing Scale (EPS) is used as an answer-style
reference: it shows how an older EFPA/BPS test review is actually completed in
practice, but it is not treated as a source structure that supersedes
`markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`.

The audit focuses on coherence and usability, not on rewriting the template or
assigning new Part B ratings. It asks whether reviewers can plausibly enter the
kinds of facts, missing-information markers, ratings, comments, and final
recommendations that filled EFPA reviews require, while also capturing the
additional evidence needed for AI benchmark review.

## Evidence Base

The main sources inspected were:

- `markdown/Papers/EFPA_Test_Review_Model_2025_Markdown.md`
- `markdown/MESA EFPA template.md`
- `markdown/MESA EFPA template guide v3.md`
- `markdown/MESA EFPA adaptation map.md`
- `markdown/MESA EFPA traceability matrix.md`
- `markdown/MESA Part B literature synthesis.md`
- `markdown/MESA pilot - Humanitys Last Exam.md`
- User-supplied filled EPS review PDF

The filled EPS review provides a useful behavioral model for the audit. It uses
a practical mix of short factual entries, checklist selections, explicit
missing-information markers, `n/a` ratings, reviewer comments, and a final
recommendation about appropriate use. It also shows that a completed EFPA-style
review is not just a numeric grid: the prose comments are where many of the
most important interpretive cautions appear.

## Overall Judgment

The MESA template and guide are mostly coherent as an AI-benchmark adaptation
of EFPA. The core EFPA sequence is preserved: first describe the instrument,
then evaluate the quality of evidence for interpretation and use. MESA
successfully translates the human-testing concepts into benchmark-native
concepts without losing the logic of the review model. The result is heavier
than the filled EPS example, especially in Part B, but the added weight is
mostly justified by the complexity of AI benchmark evidence.

The strongest coherence feature is the explicit boundary between Part A and
Part B. Part A is used to record source-grounded facts and documentation gaps.
Part B is used to make reviewer judgments tied to evidence, missing evidence,
rationale, and interpretation caution. This boundary is consistent with the
repository guidance and with the role played by the descriptive and evaluative
parts of the EPS review.

The main usability risk is not structural incoherence, but reviewer burden.
MESA asks reviewers to complete more fields, more evidence columns, and more
AI-specific caveat screens than an older EFPA-style test review. That is
appropriate for high-stakes or broad-claim benchmark audits, but it may feel
overbuilt for small, narrow, or early-stage benchmarks unless the guide
continues to emphasize proportional completion.

## Strengths

### 1. EFPA Spine Is Preserved

MESA keeps EFPA's descriptive-first architecture. The template moves from
factual description, classification, scoring, outputs, and materials into
evaluative sections on rationale, materials, baselines, reliability, validity,
fair use, reporting, and final evaluation. This maps cleanly to the EFPA 2025
source structure and to the practical shape of the EPS review.

The adaptation map and traceability matrix make this preservation auditable.
They document how EFPA concepts such as test takers, response modes, norms,
test materials, reliability, validity, fair use, and generated reports become
AI-benchmark concepts such as evaluated systems, response formats, baselines,
harnesses, score stability, construct validity, comparability, and
leaderboards.

### 2. The Part A / Part B Boundary Is Clear

The template repeatedly states that Part A records what sources say and marks
missing documentation, while Part B contains evidence-grounded reviewer
judgment. This is coherent with the filled EPS review. In the EPS example, the
descriptive section records facts such as item count, scale names, response
mode, scoring, materials, costs, and user qualifications. The evaluative
section then comments on documentation quality, material quality, norms,
reliability, validity, and appropriate use.

MESA's improvement is that it makes the boundary harder to blur. It instructs
reviewers not to treat missing documentation as proof of poor quality and not
to assign Part B ratings without evidence. That is especially important for AI
benchmarks, where absent public documentation can mean many things: a hidden
test set, a hosted evaluator, an unpublished implementation detail, or a real
documentation gap.

### 3. AI Benchmark Evidence Is Well Covered

The MESA template adds fields that EFPA needs for AI benchmarks but could not
have specified in human-test terms. These include:

- Public artifacts, repositories, datasets, prompts, rubrics, and evaluation
  harnesses.
- Model response modes, tool use, structured outputs, process traces, and
  multimodal inputs.
- Baselines, model comparator cohorts, human or expert comparators, chance
  floors, ceilings, and thresholds.
- Score uncertainty, seed or prompt sensitivity, judge reliability, scorer
  validation, and version stability.
- Dataset provenance, contamination controls, searchability, private splits,
  reproducibility materials, and maintenance status.
- Leaderboards, scorecards, raw outputs, dashboards, public claims, and
  score-to-claim linkage.

These additions are coherent because they preserve EFPA functions rather than
merely adding topics. For example, EFPA norms become MESA baselines and
comparators. EFPA test materials become datasets, prompts, rubrics, and
harnesses. EFPA digitally generated reports become leaderboards, paper tables,
dashboards, scorecards, and public claims.

### 4. The Guide and Template Align

From `# Part A. Description of the Benchmark` onward, the guide and template
use the same heading sequence. The guide adds explanatory content and a
cross-cutting `Other:` rule, but it does not appear to describe a different
template. This is a strong coherence point: a reviewer can move between the
blank template and the guide without having to reconcile incompatible section
numbers.

The guide also gives useful examples from a fixed benchmark bank. This helps
reviewers interpret abstract fields such as "broad claim," "reference
groups," "contamination controls," and "metric-to-claim linkage." The examples
are especially useful because many AI benchmark concepts are less settled than
traditional test-review concepts.

### 5. The HLE Pilot Confirms Practical Answerability

`markdown/MESA pilot - Humanitys Last Exam.md` shows that the adapted template
can be filled in for a real AI benchmark. It records the source inventory,
artifact status, claimed capability domains, intended systems, task families,
scoring, output formats, reproducibility gaps, contamination controls, and
Part B evidence. The pilot also demonstrates the intended caution pattern for
broad claims: high performance on a closed-ended academic benchmark can be
reviewed as evidence about that bounded task space without being treated as
standalone proof of AGI, autonomous research ability, or general agency.

This matters because a template can be structurally elegant yet unusable in
practice. The HLE pilot suggests MESA's answer fields are usable, though
dense.

## Coherence and Usability Risks

### 1. Part B Is Heavier Than the EPS Answer Style

The filled EPS review uses ratings and narrative comments, but it does not
require every rated row to carry separate evidence, missing evidence, reviewer
rationale, and interpretation caution. MESA does. This is coherent with the
project's evidence-gap discipline, but it increases reviewer workload.

The risk is that reviewers may either leave fields thin or repeat the same
evidence across many rows. That could make a completed MESA review look more
mechanical than the EPS example, where prose comments synthesize several
related judgments at once.

Recommendation: keep the current rating discipline, but add or retain guidance
that low-risk rows may be brief when the key evidence and caution are already
captured in the section comments. The principle should be "auditable, not
bloated."

### 2. Some AI-Specific Rows May Force False Precision

Some benchmarks will not have meaningful evidence for every MESA row. For
example, a small static text benchmark may not support rich discussion of
dynamic task determination, maintenance policy, raw traces, public leaderboard
quality, or cross-system API/local comparability. The template already includes
`Not applicable`, `Not documented`, and `Unclear from available sources`, so
the structure can handle this. The usability risk is that reviewers may feel
they must fill every row with a substantive judgment.

Recommendation: strengthen the guide's framing that `n/a`, `0`, and
documentation-status labels are valid answers when used carefully. A coherent
review does not need every field to be information-rich; it needs every
important inference to be traceable.

### 3. Guide Examples Could Be Misread As Ratings

The guide's benchmark example bank is useful, but it also introduces a subtle
risk. If examples mention named benchmarks in rating contexts, reviewers might
mistake illustrative patterns for settled ratings. The guide already says Part
B examples are illustrative patterns only, not new review ratings. That
warning is important and should remain prominent.

Recommendation: whenever the guide gives an example near rating anchors, keep
the language clearly illustrative: "example evidence pattern" rather than
"benchmark receives." This protects the guide from becoming an informal set of
ratings.

### 4. The EPS Review Shows the Value of Narrative Comments

In the EPS review, the most useful judgments are often in reviewer comments:
the discussion of theoretical foundation, documentation strengths, missing
minority-group data, interpretation of extreme scores, test-retest limitations,
and validity-study caveats. MESA includes reviewer-comment fields after each
Part B section, which is good. The risk is that the expanded row-level tables
could crowd out those synthesis comments.

Recommendation: treat section comments as essential, not optional decoration.
They should do what the EPS comments do: explain the practical meaning of the
ratings, identify the main evidence gaps, and state how cautious users should
interpret the benchmark.

### 5. Broad-Claim Screens Are Coherent But Need Careful Use

MESA's broad claim and CHC/AGI caution fields are well motivated for AI
benchmarks. They are coherent additions because AI benchmarks often make
claims about reasoning, general intelligence, agency, autonomy, or expert
capability that exceed the task sample. However, these fields could drift into
reviewer speculation if a benchmark does not itself make broad claims.

Recommendation: use the broad-claim screen only when the benchmark title,
paper, website, leaderboard, or publicity actually invokes broad terms or
clearly implies them. If reviewers add a CHC-like mapping, it should be marked
as reviewer interpretation rather than an author claim.

## EPS Answerability Test

| EPS-style answer pattern | Can MESA express it? | Coherence assessment |
| :--- | :--- | :--- |
| Short factual identity fields such as name, authors, publisher, date, and review metadata | Yes, in Section 1.1, Section 1.2, and the Information Sources table | Strong fit. MESA adds benchmark artifacts and maintainers without disrupting the EFPA identity function. |
| Classification checkboxes for domains, intended use, populations, users, response mode, and item format | Yes, in Sections 2.1-2.13 | Strong fit. MESA translates human populations into intended AI systems and response mode into model output modes. |
| Missing-information markers for test-taker demands such as language, vision, or hearing | Yes, through documentation status options and requirement tables | Strong fit. MESA's distinction among `Not documented`, `Unclear`, and `Not applicable` is more precise than the EPS pattern. |
| `n/a` for irrelevant sections such as computer-generated reports or inter-rater reliability | Yes, in Part B rating scale and row-level ratings | Strong fit, as long as reviewers reserve `n/a` for true non-applicability rather than missing evidence. |
| Narrative comments on documentation, norms, reliability, and validity | Yes, through reviewer comments after Sections 6-12 and final evaluation prose | Strong fit, but comments should remain central so the review does not become a sparse rating grid. |
| Final recommendation about suitable use by qualified users | Yes, through Final Evaluation, Conclusions, Summary of Ratings, Evidence Gap Register, and Reviewer Caution Statement | Strong fit. MESA appropriately shifts from user qualifications to claim-bounded benchmark use and interpretation expertise. |

Overall, the answerability test is positive. MESA can express the practical
answer types found in the EPS review, and it can also express AI-specific
evidence that the EPS form did not need. The main difference is density: MESA
requires more explicit audit scaffolding around evidence and gaps.

## Prioritized Recommendations

1. Preserve the current structure.

   The EFPA-to-MESA adaptation is coherent at the level of section mapping,
   Part A/Part B sequencing, and major review functions. No structural redesign
   is warranted based on this audit.

2. Keep emphasizing proportional completion.

   Add or preserve guide language that reviewers should complete fields at the
   level of detail justified by the benchmark's scope, claim breadth, and risk.
   A narrow benchmark can have many concise `n/a`, `0`, or documentation-gap
   entries without making the review incoherent.

3. Protect the narrative reviewer-comment fields.

   The EPS example shows that prose synthesis is where important practical
   interpretation happens. MESA should continue to require evidence-rich rows,
   but section comments and final cautions should be treated as central review
   outputs.

4. Clarify example status in the guide.

   The benchmark examples are helpful and should remain, but any examples near
   rating language should be framed as illustrative answer patterns, not
   benchmark ratings.

5. Add a short "minimum viable review" note if future users find the template
   heavy.

   A useful addition would be a guide note saying that a minimal coherent MESA
   review must include source inventory, Part A factual description, evidence
   gaps, Part B ratings only where requested, and a claim-bounded caution
   statement. This would reduce reviewer anxiety without weakening the full
   framework.

## Conclusion

The MESA EFPA template and guide v3 are coherent adaptations of EFPA for AI
benchmark review. They preserve the core EFPA review logic while adding the
AI-specific evidence categories needed to audit benchmarks as measurement
instruments. The filled EPS review supports this conclusion because MESA can
represent the same broad classes of answers: factual description, selected
options, missing information, `n/a`, ratings, reviewer comments, and final
recommendations.

The main issue is usability load, not conceptual fit. MESA's expanded Part B
rating discipline is defensible for AI benchmarks, especially when public
claims are broad or consequential. Still, the guide should continue helping
reviewers avoid false precision and table fatigue. The best next revisions
would be small usability clarifications, not changes to the underlying
adaptation.

