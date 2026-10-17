# MESA Talk Speech

**Talk:** MESA: Requirements-Oriented Review of AI Benchmarks as Measurement Instruments
**Speaker:** Vitor Raposo (solo) · Ontario Tech University · ARiSE Lab
**Venue:** RE RETRAI Workshop, Aug. 18th, 2026
**Slot:** 10 minutes · **Target spoken length:** ~11:00 (~1,700 words) - over; see the trims below to land under 10:00
**Delivery pace:** ~120-130 wpm, with a beat of silence on each slide transition

> Slide numbers and titles match the presentation deck (15 slides, after adding the requirements checklist and the two-part Worked Example, and merging the two Research Methodology slides into one). Times are targets, not hard limits. Slides 9-11 include drop-in slide content to paste into the deck.

---

## Slide 1 - Title (~0:20)

Good morning. I'm Vitor Raposo, from the ARiSE Lab at Ontario Tech University, working with my supervisor Dr. Sanaa Alwidian. Our work starts from a simple question: when a benchmark score becomes the evidence for a requirement, who reviews the benchmark itself?

## Slide 2 - Background Overview (~0:50)

Benchmark scores are already doing requirements work. They decide which model a team builds on, whether a system is ready to ship, which vendor gets paid, and what gets claimed in a press release or to a regulator. The assumption is that a score traces cleanly from a real-world ability, through the task and the metric, to a capability claim. But in reality that chain breaks: test questions leak into training data, scores shift when you reword a question, top models bunch near the ceiling, and what the benchmark actually measures is often never stated. So a high score can mean a weak or leaky test - not a strong model. That's a construct validity problem.

## Slide 3 - The Gap (~0:30)

Which brings us to the gap. If we're treating AI as a form of intelligence, and measuring it, why don't we borrow from the decades of work that human-intelligence research has already done on how to evaluate a test? Mature fields don't just score people - they review the tests themselves. AI benchmarking has no equivalent practice.

## Slide 4 - Related Work (~0:50)

Three bodies of work get us close. Benchmark critiques show what benchmarks really measure and how leaderboards distort results - but they diagnose problems; they don't give you a procedure. New standards for benchmarks, like BetterBench and reporting guidelines, give real criteria - but they're written for the people building a benchmark, not the person reading the score. And the social-science counterparts - the EFPA and APA test-review models, and the CHC model of intelligence - review the instrument itself, but were never written for prompts, graders, or leaderboards. None of them tells a requirements engineer what an existing score is allowed to mean.

## Slide 5 - Proposal (~0:35)

So that's what we built: MESA, a Requirements-Oriented Review Model for AI benchmarks as measurement instruments. It's a test review model in two parts - description and evaluation - that reviews the instrument and the technical evidence behind it, with a focus on requirements and traceability. It's adapted from the established human-intelligence standards - EFPA, APA, and the CHC model - and it's fully open source, so it can support benchmarks, policy-making, and future standards.

## Slide 6 - Research Questions (~0:55)

Three research questions drive the work, and they build on each other. The first is about structure: how can the EFPA test review model - a standard refined over decades for human psychological and educational testing - be adapted into a requirements-oriented quality model for benchmark-based AI capability claims? These are two very different worlds, so the real question is which parts carry over unchanged, which need renaming, and which have no equivalent and must be added. The second is about evidence: what benchmark materials and construct-validity support does a score actually need before a requirements engineer can trust the interpretation placed on it - in other words, what is the minimum bar? And the third is empirical: what interpretation risks and evidence gaps does MESA actually reveal when we apply it to three deliberately contrasting benchmarks - Humanity's Last Exam, ARC-AGI-2, and DesignQA? Together they take us from adapting the standard, to defining the evidence it demands, to testing what it surfaces in practice. The goal throughout is a single framework that evaluates benchmarks on requirements, quality, and traceability.

## Slide 7 - Research Methodology, Part A / Part B (~0:55)

Here's how the model is structured, and the order matters. Part A only describes the benchmark: what it is and who made it, what it claims to measure, how behaviour becomes a score, and what materials exist. Crucially, Part A never judges - if something is missing, it's recorded as an evidence gap, not guessed at. Part B then evaluates: is the benchmark well made, is there a baseline to compare against, would the score come out the same on another run, and does the score actually mean what it claims?

And the fields in MESA aren't invented - they're sourced. We read fifteen modern benchmarks as raw material, alongside software-engineering practices, the construct-validity literature, an AI cognitive-abilities mapping, and the EFPA model itself. Each feeds a specific part of the review: the psychology standard supplies the two-part structure and the rating scale, BetterBench supplies the upkeep and contamination questions, and the validity work supplies the chain from ability, to task, to score, to claim. Every field traces back to a named source.

## Slide 8 - What MESA Requires of an Ideal Benchmark (~0:45)

**Slide content (drop-in):** four requirement cards, headed by the same four plain-language questions used on the Results slide, each with a small `Part A -> Part B` tag showing where it is measured.

- **Clear what's measured** · `Part A (Sec 1-3) -> Part B (Sec 6-7)` - defined target construct and explicit non-use caveats; open, documented, runnable materials.
- **Comparable** · `Part A (Sec 3) -> Part B (Sec 8)` - real reference points: a guessing floor, and human or expert scores under identical conditions.
- **Repeatable** · `Part A (Sec 3, 5) -> Part B (Sec 9)` - published uncertainty: run-to-run variance, prompt-sensitivity, grader validation.
- **Means what it claims** · `Part A (Sec 2, 4) -> Part B (Sec 10, 12)` - contamination controls, version tracking, reporting that keeps limits next to headline scores.

Footer strip: *Part A records it; Part B judges it. The checklist is fixed - how well each item is met stays a 0-4 evidence-grounded judgment.*

**Script:**
Before the example, here is what MESA actually requires of a benchmark. Because the sections are fixed, MESA is really a standard checklist of requirements, under the same four questions we'll use throughout - and each one is measured in two places: Part A first records the facts, then Part B judges them. To be clear about what's measured, Part A captures the target and scoring, and Part B judges whether the construct and materials hold up. To be comparable, Part A records the baselines and Part B judges them - a guessing floor, and human or expert scores under the same conditions. To be repeatable, Part A logs the uncertainty and materials, and Part B judges how much scores move across reruns, wording, and graders. And to mean what it claims, Part A records the claims and reporting surfaces, and Part B judges validity and whether limits sit next to the headline numbers. The checklist is fixed; what stays a judgment is how well each is met.

## Slide 9 - Worked Example 1/2: MESA applied to DesignQA (~0:40)

**Slide content (drop-in):** left rail = INPUT materials; then Part A -> Part B columns, reusing the four requirement groups from slide 9, filled in with DesignQA specifics.

- **INPUT (left rail):** DesignQA paper · dataset · grading/scoring code · public leaderboard.
- **Part A - describes:** engineering-requirements QA over the Formula SAE rulebook; word-overlap scoring against one reference answer.
- **Part B - checks the four groups:** Clear what's measured (largely yes) · Comparable (only partly - no human baseline) · Repeatable (open question) · Means what it claims (open question).

**Script:**
Now let's run that checklist on one benchmark - DesignQA. We feed in its materials: the paper, the dataset, the grading code, and the leaderboard. Part A records what it is and how it's scored, and Part B walks the same four questions. Is it clear what's measured? Largely yes. Is there a baseline? Only partly. Is it repeatable? And does the score mean what it claims? Those are where it gets interesting - which is exactly what the report on the next slide shows.

## Slide 10 - Worked Example 2/2: the MESA report (~0:45)

**Slide content (drop-in):** the report MESA emits for DesignQA - a rated checklist plus the feedback block, paying off slide 9's questions in the same order.

- **Ratings (0-4):** each requirement rated; DesignQA bottoms out on Repeatable.
- **Evidence gaps (with section):** no run-to-run variance `Sec 9` · no human baseline + unclear licence `Sec 8` · fully public/tunable test set `Sec 10`.
- **Recommendations:** publish error bars / repeat runs · add a human baseline · versioned releases + licence · report by subset.
- **Bottom line:** Supported use - subset-level diagnostic for FSAE requirements QA · Non-use - fine-grained ranking, procurement.

**Script:**
And here's what comes out - the MESA report. Each requirement gets a rating from zero to four, and for DesignQA the weak spot is repeatability. MESA lists the evidence gaps and exactly where they sit - no repeat-run variance, no human baseline, an unclear licence, and a fully public test set - and turns each into a recommendation: publish error bars, add a human baseline, ship versioned releases, and report by subset. It ends with the bottom line: DesignQA is a solid subset-level diagnostic for engineering-requirements QA, but it can't support fine-grained ranking or a procurement decision. That is MESA's value - materials in, an auditable requirements report out.

## Slide 11 - Case-Studies (~0:50)

We applied MESA to three benchmarks chosen to be as different as possible. Humanity's Last Exam: hard academic questions, graded automatically by another AI model. ARC-AGI-2: visual grid puzzles with hidden test sets, publicly framed as progress toward general intelligence. And DesignQA: questions about a real engineering rulebook - the closest of the three to actual requirements work. To limit single-reviewer bias, two models drafted each review independently, and a supervising editor reconciled every disagreement against the sources. This is a feasibility demonstration - not yet a validation study.

## Slide 12 - Results (~1:00)

Here are the reviews, in plain words instead of scores. We checked four things, and two rows tell the story. First - would you get the same score if you ran it again? For all three benchmarks, the evidence is insufficient. Second - does the score mean what it claims? Weak again, especially for Humanity's Last Exam. And that's not because the tests are badly built; it's because the evidence is simply missing. So each score supports a narrower claim than its headline: Humanity's Last Exam measures hard closed-book academic questions, not general intelligence; ARC-AGI-2 measures pattern induction under fixed conditions, not human-like flexibility; and DesignQA diagnoses topic by topic, but can't guide a purchasing decision.

### Presenter notes - justifications for each cell (reference; do not read aloud)

Plain-word to rating: `Some, not enough` = 1 · `OK` = 2 · `Good` = 3. Cells map to the reconciled reviews in `reviews/gemini_supervising_editor/`. Use these to defend any cell in Q&A.

**Row 1 - Is it clear what's measured, and can you run it?** *(Sec 6 rationale/documentation + Sec 7 materials)*

- **HLE - Good.** ~2,500 closed-ended questions from ~1,000 expert contributors with two rounds of human review; public dataset on Hugging Face, an open harness, and a pinned judge (`o3-mini-2025-01-31`); a clean two-step predict->judge CLI. *Watch-out:* construct is defined by adversarial difficulty rather than a cohesive capability, and no item-quality stats (difficulty/discrimination) are published.
- **ARC-AGI-2 - Good.** Clearly defined construct (compositional grid-puzzle generalization); 1,000 training + 120 public-eval tasks under Apache-2.0; a deterministic exact-match scorer; offline Kaggle sandbox. *Watch-out:* the README carries a documented 2-trial vs 3-trial inconsistency.
- **DesignQA - OK (not Good).** Bounded, clear construct (locate / recognize / check FSAE rules) with full CSVs, CAD images, an open scorer, and a runnable command - but materials are held to a 2 by **no LICENSE file** (`license: null`, so reuse is legally undefined), no dependency lockfile or container, single-reference explanation keys, and strict-format scoring that zeroes correct-but-differently-worded answers.

**Row 2 - Is there a baseline (like a human score) to compare against?** *(Sec 8)*

- **HLE - OK.** Has a frontier + open-weight model cohort, an implicit ~25% multiple-choice floor, and MMLU/GPQA framing - but **no controlled human baseline**. "Expert-level" only means experts *wrote* the items; nobody sat the test under timed, no-tool conditions. Severe gap given the title "Humanity's Last Exam," so held at 2.
- **ARC-AGI-2 - Good.** One of the strongest human baselines in any current benchmark: 407 participants, 515 sessions, 13,405 attempts; every retained task solved by >=2 independent testers within two attempts; calibrated to ~1% of human difficulty. Plus interpretable v1->v2 deltas (o3-medium ~53% -> 3%). Only limit: no uncertainty margins on the model cohorts.
- **DesignQA - OK.** Naive baselines computed per subset (random rule selection, random words, 50% guessing) and a five-model cohort (GPT-4o, GPT-4, Claude-Opus, Gemini-1.0, LLaVA-1.5) - but **no human/expert accuracy baseline**, so scores can't be anchored to human engineering competence.

**Row 3 - Same score if you run it again?** *(Sec 9 - all three rated 1)*

- **HLE.** Only a Wald 95% interval buried in the scorer code, never on the leaderboard; no run-to-run variance for stochastic reasoning models (o1, Gemini Thinking) even at temperature 0; no prompt-sensitivity study; and the `o3-mini` judge is unvalidated against human adjudication. With ~2,500 items a 1-2% gap is within binomial noise, yet ranks are shown as exact.
- **ARC-AGI-2.** The exact-match scorer itself is perfectly reliable, but there are no confidence intervals, no multi-seed/multi-run data, and no prompt-sensitivity study. On a 120-task split one task = ~0.83 points, and pass@2 is an attempt-allowance, not a stability measurement. Treat models within a few points as tied.
- **DesignQA.** Multi-run standard deviation is reported only for the LLaVA GuaranteedRAG diagnostic - nothing for the main cohort; no seeds; on the 16-item Functional Performance subset a single item moves the score 6.25 points; and API/embedding drift is uninsulated (no lockfile).

**Row 4 - Does the score mean what it claims?** *(Sec 10)*

- **HLE - Some, not enough (weakest, rated 1).** The headline metric depends entirely on an **unvalidated LLM judge**; documented answer-key noise (the paper's own 15.4-18% expert disagreement; FutureHouse's ~29% in text-only chem/bio) acts as a noisy ceiling; no dimensionality or discrimination checks; near-zero ecological relevance (closed-book, no-tool vs real deployment that uses search/code/multi-turn); and the `agi.safe.ai` URL and title over-extrapolate narrow evidence into an AGI claim.
- **ARC-AGI-2 - OK (2).** Strong metric-construct alignment (exact match) and strong contamination controls (public/semi-private/private splits + offline sandbox), but the task surface is narrow - only 3 of 10 CHC domains (On-the-Spot Reasoning, Visual Processing, Working Memory) - with no internal-structure or convergent/discriminant validity, and "AGI" branding that outruns the evidence (a "necessary but not sufficient" caveat is not a validity argument).
- **DesignQA - OK (2).** Strong content validity (real FSAE rules + MIT Motorsports CAD, expert cross-review) and disciplined claims (no AGI claims; framed as a diagnostic "first step"), but construct-irrelevant variance from format/verbosity, single-reference BLEU/ROUGE explanations never validated against human ratings, a fully public test set with authors **recommending fine-tuning on the Retrieval QAs** (optimizing on test), and no convergent/discriminant/predictive validity.

**"Narrower claim than the headline" - supported vs non-use (per benchmark):**

- **HLE.** Supports: cautious comparison on hard closed-ended academic QA under HLE conditions, and overconfidence/calibration diagnosis. Non-use: fine-grained ranking by small margins; AGI/agency/tool-use/research claims; human-equivalent expert performance.
- **ARC-AGI-2.** Supports: tracking frontier progress on abstract, localized compositional grid reasoning under controlled conditions. Non-use: AGI/general intelligence; human-like flexibility; high-stakes cross-system comparison mixing compute-bounded and cost-bounded cohorts.
- **DesignQA.** Supports: subset-level diagnostic of FSAE requirements-QA strengths and weaknesses, for large gaps only. Non-use: fine-grained ranking; procurement/buying decisions; comparing across setups (AllRules vs RAG); broad engineering competence.

## Slide 13 - Answering the Research Questions (~0:45)

So, back to our three questions. RQ1 - can a human-test review model fit AI benchmarks? Yes, with support from related work like the adapted CHC model, via four rules: keep, rename, replace, and add. RQ2 - what does a score need to be trusted? Enough evidence that it's real: not luck, not data leaks, and a clearly defined target. And RQ3 - what did we find? All three benchmarks are weakest on repeatability and construct validity, so each supports a narrower claim than it makes.

## Slide 14 - Conclusion (~0:45)

To conclude: MESA's contributions are a framework for score traceability, a reusable vocabulary of evidence gaps and supported-use statements that drops straight into a requirements spec, and an open, replicable artifact. The limitations are real - the reviews were drafted by models, the ratings are subjective by design, and a full review takes time. And the future work is the fix: human expert validation, a compact scorecard, and more case studies to surface recurring weaknesses. One future thread we're especially keen on is constructive validation - acting on MESA's own evidence gaps to produce an improved benchmark like DesignQA, then measuring the improvement independently, through an expert re-rating and real run-to-run variance, rather than just re-scoring it with MESA.

## Slide 15 - Thank You (~0:20)

That's MESA. The template, the three full reviews, and the paper source are all open in the repository, so you can test the model yourself. Thank you - and I'm happy to take questions.

---

## If you're running long, cut these first

The deck is ~11:00 with the three new slides (9-11) and the expanded RQ script. To get back under 10:00, in order:

1. **Collapse the two Worked Example slides (10-11) into one** - keep the DesignQA report (slide 11) and drop the walkthrough script on slide 10, letting the report speak for itself. Saves ~0:40.
2. **Slide 6 (Research Questions)** - revert to the concise three-question version: state each RQ in one line and drop the per-question motivation. Saves ~0:20.
3. **Slide 9** - keep the `Part A -> Part B` tags on the slide, but say them aloud for only the first requirement; list the other three as plain requirements. Saves ~0:15.
4. **Slide 9 (deeper cut)** - demote the requirements checklist to a backup slide and let slide 10 introduce the four groups as it applies them to DesignQA.
5. **Slide 13 (Results)** - shorten the three per-benchmark clauses to one: "each supports a narrower claim than its headline."
6. **Slide 4** - drop the "BetterBench and reporting guidelines" parenthetical.
7. **Slide 12 (Case-Studies)** - drop "chosen to be as different as possible."

Do **not** cut the Part A / Part B ordering (slide 7) or the input -> output payoff (slides 9-11) - they carry the argument.

---

## What is EFPA? (reference - do not read aloud)

**EFPA** = the **European Federation of Psychologists' Associations**. Its **Test Review Model** (current edition 2025) is a standardized framework expert reviewers use to *describe and evaluate a psychological or educational test as a measurement instrument* - the instrument is reviewed, not the person taking it. It is the primary structural source MESA adapts.

- **Part A - Description (non-evaluative):** factual identity, classification, measurement & scoring, digitally generated reports, supply arrangements & materials. Records facts; never judges.
- **Part B - Evaluation (rated):** documentation, test materials, norms, reliability/precision, validity, fair use, computer-generated reports - ending in a **global evaluation**. Reviewers exercise judgment; ratings are not mechanically averaged.
- **Two defining principles MESA inherits:** *describe before you judge*, and *tie every judgment to evidence* (information that is absent is recorded as an evidence gap, not treated as failure).
- **What MESA takes from it:** the two-part structure, the 0-4 rating scale, and the "missing = gap" convention - renamed and extended for prompts, graders, secret splits, and leaderboards, which EFPA predates.

One-line version for Q&A: *EFPA is the decades-old European standard for reviewing human tests as instruments; MESA carries its "describe, then evaluate" architecture over to AI benchmarks.*

---

## Anticipated questions (reference - do not read aloud)

**"You criticise model-as-judge, but your own reviews were drafted by models."**
Fair, and it's why the paper calls this a feasibility demonstration rather than a validation study. Two differences: MESA's drafts were produced independently by two models and reconciled by a third against the sources, with every judgement traceable to quoted evidence - and the output is human-inspectable prose, not a number on a leaderboard. The declared next step is exactly the fix: multi-reviewer human panels with inter-rater agreement.

**"Isn't this just BetterBench with extra steps?"**
BetterBench scores a benchmark against best practice, for its builders. MESA asks a different question, for a different reader: given this score, what may I claim? That's why the output is a supported-use and non-use statement rather than a quality score.

**"Why psychometrics? AI isn't human cognition."**
MESA doesn't claim benchmarks measure human cognition. It borrows the review architecture - describe before judging, tie every judgement to evidence, state what a score cannot support. That architecture is about instruments, not about people.

**"Three benchmarks is a small sample."**
Correct, and the paper says so. They were chosen for contrast, not coverage - different task formats, scoring procedures, and public framing - to test whether the template holds across them.

**"How does MESA actually use BetterBench?"**
BetterBench is a checklist for building a good benchmark - things like: is there a licence, is it version-tracked, can you run it again, can the test questions leak. MESA takes that checklist and points it at a different question: not "is this well built" but "can I trust the score." A clear example is DesignQA - it has no licence file at all, and the authors actually suggest training on the test questions. BetterBench tells us those are real problems; MESA turns each one into a rating and a plain limit on what the score can be used for.

**"How does MESA use the CHC model / A Definition of AGI?"**
A Definition of AGI breaks intelligence into ten basic skill areas - things like general knowledge, reading, maths, reasoning, memory, and vision. MESA uses that list twice: first to write down what a benchmark says it measures, then to check whether a big claim is backed up. ARC-AGI-2 is the clearest case - it has "AGI" in its name, but it only touches three of the ten areas: reasoning, vision, and short-term memory. So the verdict writes itself - it's a solid test of puzzle-solving, not proof of general intelligence. It turns an argument about "is this AGI" into a simple count.

**"Does anything from the AI side feed in, or is it all psychology?"**
Both. The overall shape - describe first, then judge, and back every judgment with evidence - comes from the human-testing standard. But the actual questions are filled in from AI work: BetterBench gives the practical checks like licences, repeat runs, and leaked questions, and A Definition of AGI gives the ten skill areas we use to catch oversized intelligence claims. So it's an old, trusted structure filled with up-to-date AI content.
