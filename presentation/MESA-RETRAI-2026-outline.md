# MESA — RE RETRAI Workshop 2026

**Slide-by-slide build specification for a 10-minute talk**

| | |
|---|---|
| Talk | MESA: Requirements-Oriented Review of AI Benchmarks as Measurement Instruments |
| Presenters | Vitor Raposo & Dr. Sanaa Alwidian — Ontario Tech University, ARiSE Lab |
| Venue | RE RETRAI Workshop, August 18, 2026 |
| Slot | 10 minutes |
| Content source | `paper_old.tex` (authoritative; `paper.tex` has diverged) |
| Visual source | ARiSE Lab template as used in A. Nwosu, *RADAR* defense deck |
| Deck size | 15 slides (13 content) + 8 backup |
| Spoken length | ≈1,386 words · **10:40** at 130 wpm |

> This document specifies content and layout. It is not the deck. Every slide names both the format
> it uses and the RADAR slide that format comes from.

**The deck runs ~40 seconds over the slot.** Accepted, but this is now the largest overrun so far and
the trim list matters. Slide 3 at 1:03 is the longest slide in the deck — deliberately, since it is
the example everything else leans on. See the [build checklist](#build-checklist).

**Figures.** Both diagrams exist and have been reviewed. They are not committed to the repository —
there is no `figures/` directory — so export them from wherever they were authored before building
slides 7 and 11. Their contents are specified inline on those slides.

---

## The arc

> Benchmarks are used as evidence *(2)* → here is one failing concretely *(3)* → here is what others
> built *(4)* → **here is what none of them brought across, and what I take from each** *(5)* →
> MESA *(6–10)* → what it found *(11–13)* → what it means *(14)*

---

## Part 1 — Conventions

### Format palette

Format follows content. Every option below already appears in the RADAR deck.

| Format | Use when | RADAR |
|---|---|---|
| **Cards** | Items are parallel and independent | 2, 21, 22 |
| **Comparison matrix** | Several things judged on the same dimensions | 3 |
| **Flow / chain** | The content has a sequence or causal order | 9, 27 |
| **Transfer diagram** | Two worlds, and something crossing between them | *new* |
| **Before → after table** | Every item is a transformation | 15 |
| **Tinted data table** | Numbers, where the pattern across cells is the finding | 18, 20 |
| **Big stat + rows** | Composition, counts, provenance | 10, 26 |
| **Console box** | A verbatim artifact worth showing raw | 17 |
| **Figure band** | An existing diagram, full slide width | 8, 9 |
| **Split contrast panel** | One problem set against one answer | 4, 15 |
| **Scale strip** | An ordinal scale — drawn as a scale | *new* |

### Text density

| Element | Rule |
|---|---|
| Slide title | ≤ 6 words |
| Card / column header | ≤ 4 words after the number |
| Labelled item | Bold label of 1–3 words, then one line of ≤ 8 words |
| Items per card or column | 4 maximum; 5 only where content resists grouping |
| Sentences | None in slide bodies. Fragments only |
| Banner | One line, ≤ 15 words |
| Footnote | ≤ 20 words |

Name lists, section numbering, and per-benchmark detail live on backup slides.

### Canvas & chrome

- **16:9.** Full-width dark navy header band, top ~15%; title white bold, left-aligned, ~36–40 pt.
- **Slide number** bottom-right, small gray. **Logos** bottom-left: Ontario Tech mark + ARiSE Lab.
- **Title slide**: OT Engineering wordmark top-left, blue swoosh right, title reversed out of a navy
  band across the bottom third.
- **Body background** near-white (#F7F9FB).

### Color

| Token | Hex | Meaning |
|---|---|---|
| Navy | #00437B | Headers, structure |
| Blue | #1A5FA8 / #EAF3FB | Concept, definition |
| Green | #1E7A4B / #EAF7EF | Process, "can be used for" |
| Amber | #8A5A00 / #FDF6E3 | Outcome, key finding |
| Red | #9B1B1B / #FDEDED | Problem, "cannot be used for" |
| Banner gray | #EEF2F6 | Bottom banner |

### Footnotes

Superscript after the term; note at the slide foot in the small bold-blue band RADAR uses for
citations. **Numbering restarts per slide, three maximum, each term defined once** — see the
[Glossary](#glossary). Where a slide has both notes and a citation, notes come first.

---

## Part 2 — Format per slide

| # | Slide | Format | Why this format | Time |
|---|---|---|---|---|
| 1 | Title | Title | — | 0:15 |
| 2 | Background | Card + **chain with breaks** | The chain and where it breaks is one causal story | 0:49 |
| 3 | Motivating example | **Narrative flow** | A sequence, not three parallel things | 1:03 |
| 4 | Related work | **Comparison matrix** | Three literatures, same three dimensions | 0:43 |
| 5 | **The Gap** | **Transfer diagram** | Two worlds, and what did — and didn't — cross | 0:43 |
| 6 | Proposed approach | Single panel + RQ strip | The gap is already stated; this slide only answers it | 0:35 |
| 7 | Source base | **Big stat + rows + figure** | Composition data | 0:44 |
| 8 | Adapting the standard | **Before → after table** | Every item is a transformation | 0:48 |
| 9 | The MESA model | **Two-stage flow** | The order *is* the point | 0:50 |
| 10 | Rating logic | **Scale strip + 3-card contrast** | One distinction, shown by contrast rather than asserted | 0:51 |
| 11 | Case-study design | **Comparison table + figure** | Three benchmarks, same attributes | 0:44 |
| 12 | Results | **Tinted data table** | The pattern across cells is the finding | 0:52 |
| 13 | Supported use | **Can / Cannot matrix** | One comparison, not three | 0:52 |
| 14 | Contributions | **Cards** | Genuinely parallel and independent | 0:38 |
| 15 | Thank you | Closing | — | 0:11 |

---

## Slide 1 — Title

**Format:** Title (RADAR 1).

> **MESA: Requirements-Oriented Review of AI Benchmarks as Measurement Instruments**
>
> Vitor Raposo & Dr. Sanaa Alwidian · Ontario Tech University · ARiSE Lab
> RE RETRAI Workshop, Aug. 18th, 2026

### Script — ≈33 words · 0:15

Good morning. I'm Vitor Raposo, from the ARiSE Lab at Ontario Tech, with Dr. Sanaa Alwidian. Our
work asks a simple question: when a benchmark score becomes requirements evidence, who reviews the
benchmark?

---

## Slide 2 — Background

**Format:** one card (left third) + **chain with break-points** (right two thirds).
**Why:** the assumed chain and where it fails is a single causal story. Three parallel lists hid
that; a broken chain shows it.
**Source:** `paper_old.tex` §Introduction.

**Left card — `01. BENCHMARK SCORE USAGE`**

> **Marketing**
> Selling the model to the user
>
> **AI model differentiation**
> Comparison of performance
>
> **Buying decisions**
> Which vendor a company chooses
>
> **Capability claims**
> What a model can and can't do

**Right — the chain.** Four navy boxes, left to right, joined by arrows. Caption above:
`WHAT WE ASSUME`

```text
Real ability  →  Task  →  Score  →  Claim
```

**Break markers.** Red tags dropping beneath the links they damage:

| Hangs under | Label | Line |
|---|---|---|
| Task | **Leaked questions** | Test items sit in training data <sup>1</sup> |
| Score | **Fragile scores** | Reword the question, the score moves |
| Score | **Ceiling effects** | Top models bunch together <sup>2</sup> |
| Claim | **Dropped caveats** | Leaderboard omits the paper's own limits |

**Banner:** `Goal:` A high score can mean a weak test, not a strong model. <sup>3</sup>

**Footnote band**

> <sup>1</sup> Called *contamination*. <sup>2</sup> Called *saturation*. <sup>3</sup> A *construct
> validity* problem: whether a test measures what it claims to measure.
>
> N. Jo and A. Wilson, arXiv:2509.19590, 2025 · S. Singh *et al.*, "The Leaderboard Illusion,"
> arXiv:2504.20879, 2025.

### Script — ≈106 words · 0:49

Benchmark scores are already doing requirements work. They decide which model a team builds on,
whether a system is ready to ship, which vendor gets paid, what goes in the press release, and what
gets claimed to a regulator. We assume a score traces from a real ability, through the task and the
metric, to the claim. In practice, test questions leak into training data, scores move when you
reword the question, top models bunch near the ceiling, and what the benchmark measures is often
never stated. So a high score can mean the test is narrow or leaky — not that the system is capable.

*Transition:* "Let me make that concrete."

---

## Slide 3 — Motivating Example

**Format:** **narrative flow**, left to right, ending in a red verdict.
**Why:** this is a story with an order — requirement, evidence, what the evidence hides, verdict.
**Source:** `paper_old.tex` §Case Study Results / DesignQA.

Four boxes left to right, then a red verdict band running under all four. Stages 2 and 3 exist so a
first-time viewer never meets an unexplained name or an unexplained claim.

**Small tag under the slide title, in gray:** *Illustrative scenario. The DesignQA facts are from the
paper; the requirement, the threshold, and the answer pair are ours.* — a talk arguing for honest
measurement should not blur what is reported and what is invented, and it protects you in Q&A.

**Stage 1** (navy) `THE REQUIREMENT`

> *"The system shall interpret
> engineering requirements
> correctly"*

**→**

**Stage 2** (blue) `THE TEST CHOSEN`

> **DesignQA**
> ~1,450 questions on a real
> engineering rulebook
>
> The model reads the rules,
> then answers

**→**

**Stage 3** (blue) `SO IT IS "VERIFIED"`

> The score clears the
> team's bar
>
> Requirement ticked off **✔**

**→**

**Stage 4** (red, widest) `WHAT THE TICK RESTS ON`

Lead with the concrete case — it is what makes the whole slide land. Set the two quoted lines in
monospace, the differing words in red:

> **Same meaning. Different words. Marked wrong.** <sup>1</sup>
>
> ```text
> Rulebook says   ...must not extend beyond the rear tires
> Model answers   ...shall not project past the back tyres
>                 → few matching words → scored 0
> ```

Then three short lines beneath:

> **Tiny subsets** — 16 questions; one moves the score 6.25 points
> **Public test set** — fully released, and tunable on
> **No human baseline** — nobody knows what good looks like

**Verdict band** (red, full width, beneath all four)

> **Verification void** — engineering competence claimed from a word match

**Banner:** `Key Idea:` Verified — by an instrument that cannot carry the claim.

**Footnote band**

> <sup>1</sup> Graded by word overlap against a single reference answer.
>
> A. C. Doris *et al.*, "DesignQA," arXiv:2404.07917, 2024.

### Script — ≈136 words · 1:03

Here is a requirement any of us might write: the system shall interpret engineering requirements
correctly. To verify it, the team picks a benchmark — DesignQA, about fifteen hundred questions on a
real engineering rulebook. The model reads the rules, answers the questions, clears the team's bar,
and the requirement gets ticked off. Now look at what that tick rests on. Answers are graded by word
overlap against one reference answer. So the rulebook says the wing must not extend beyond the rear
tires, the model says it shall not project past the back tyres — same meaning, different words — and
that is scored zero. One subset has sixteen questions, so a single question moves the score six
points. The test set is fully public. And no human ever sat this test, so nobody knows what a good
score looks like.

*Transition:* "So why doesn't existing work already solve this?"

---

## Slide 4 — Related Work

**Format:** **comparison matrix** (RADAR 3).
**Why:** three literatures assessed on identical dimensions — that is a matrix, not three cards.
**Source:** `paper_old.tex` §Related Work.

| | `CRITIQUE` | `STANDARDS` | `TEST REVIEW` <sup>1</sup> |
|---|---|---|---|
| 🔍 **Focus** | What benchmarks really measure | How to build and report one | The instrument itself |
| ✔ **Strength** | Names real failures | Concrete and checkable | Describes before judging |
| ✖ **Limitation** | Diagnoses, no procedure | For builders, not readers | Predates prompts and leaderboards |

**Banner:** `Goal:` None say what an existing score is allowed to mean.

**Footnote band.** Every column is attributed. Set in the smallest type in the deck — this band is
for the record and for anyone photographing the slide, not for reading aloud.

> <sup>1</sup> *Psychometrics* — measurement science for human testing. EFPA = European Federation of
> Psychologists' Associations.
>
> **Critique** — S. Singh *et al.*, "The Leaderboard Illusion," arXiv:2504.20879, 2025 · J. Fodor,
> "Line Goes Up?", arXiv:2502.14318, 2025 · N. Jo and A. Wilson, "What Does Your Benchmark Really
> Measure?", arXiv:2509.19590, 2025 · O. Alonso and K. Church, "Evaluating the Evaluations," ACM
> SIGIR Forum 58(2), 2024 · Z. Cheng *et al.*, "Benchmarking is Broken," NeurIPS 2025
>
> **Standards** — A. Reuel *et al.*, "BetterBench," NeurIPS 2024 · T. Gebru *et al.*, "Datasheets for
> Datasets," CACM 64(12), 2021 · M. Mitchell *et al.*, "Model Cards for Model Reporting," FAT* 2019
>
> **Test review** — EFPA, *Test Review Model — Version 2025* · AERA/APA/NCME, *Standards for
> Educational and Psychological Testing*, 2014 · A. M. Bean *et al.*, "Measuring what Matters,"
> NeurIPS 2025

*(Full reference list for the whole talk is on backup B8.)*

### Script — ≈94 words · 0:43

Critique work shows what benchmarks really measure and how leaderboards distort it — but it
diagnoses; it doesn't give you a procedure. Documentation standards — Datasheets, Model Cards,
BetterBench — give real criteria for design, implementation, and upkeep. They are written for the
person building the benchmark, not the person reading the score. Test review in psychology is the
one tradition that reviews the instrument itself, but it was never written for prompts, graders, or
leaderboards. What none of them give a requirements engineer is a structure for deciding what an
existing score is allowed to mean.

*Transition:* "So here is the gap."

---

## Slide 5 — The Gap

**Format:** **transfer diagram** — two worlds, converging into MESA.
**Why:** the gap is not "nobody thought about this." It is that *one specific thing* crossed from
human testing into AI and *another did not*. A diagram shows the asymmetry; a list would flatten it.
**Source:** `paper_old.tex` §Introduction (line 58), §Benchmarking standards across the fields.

**Left column — `HUMAN TESTING`** *(blue)*

> **EFPA Test Review Model**
> Describe, then evaluate
> *Informed by the AERA/APA/NCME Standards* <sup>1</sup>
>
> **CHC model**
> Intelligence as a profile of domains <sup>2</sup>

**Right column — `AI BENCHMARKING`**

> **A Definition of AGI** *(green)*
> CHC adapted to AI — a breadth-weighted profile
>
> **BetterBench** *(amber)*
> Lifecycle, reproducibility, upkeep
>
> **No review standard** *(red)*
> Scores used. The test itself unexamined.

**Converging arrows from both columns → `MESA`** *(navy box, centred beneath)*

> Review the benchmark as a measurement instrument

**Banner:** `Novel Contribution:` The ability model crossed over to AI. The review model never did.

**Footnote band**

> <sup>1</sup> AERA/APA/NCME *Standards for Educational and Psychological Testing*, 2014 — the
> American counterpart to EFPA. <sup>2</sup> *Cattell–Horn–Carroll* — intelligence as a profile
> across many ability domains.
>
> D. Hendrycks *et al.*, "A Definition of AGI," arXiv:2510.18212, 2025 · A. Reuel *et al.*,
> "BetterBench," NeurIPS 2024 · EFPA, *Test Review Model 2025*.

### Script — ≈94 words · 0:43

So here is the gap. Educational and psychological testing has spent decades building a way to review
a test as an instrument — the EFPA Test Review Model, informed by the American Standards for
Educational and Psychological Testing. And the ability model has already crossed over: A Definition
of AGI takes Cattell-Horn-Carroll into AI as a breadth-weighted profile of domains. BetterBench
brought quality criteria to benchmarks. But nobody brought the review architecture across. AI
benchmarks measure intelligence capabilities, and no standard asks whether the benchmark itself is a
sound instrument. That is what MESA is.

*Transition:* "So this is what we built."

---

## Slide 6 — Proposed Approach

**Format:** single panel + RQ strip. Deliberately sparse — mostly whitespace.
**Why:** slide 5 just stated the gap. Repeating it here would be conspicuous, so this slide only
answers it.
**Source:** `paper_old.tex` §Introduction.

**Panel** (blue, wide)

> `MESA`
> **Meta-Evaluation Standard for AI Benchmarks**
>
> **Two parts**
> Describe, then evaluate
>
> **Reviews**
> The benchmark, not the model
>
> **Written for**
> The person reading the score
>
> **Produces**
> What a score can and cannot support

**RQ strip** — three narrow boxes beneath:

> **RQ1** · Adapt the standard  **RQ2** · Minimum evidence needed  **RQ3** · What it reveals

**Banner:** `Goal:` From citing a score to auditing the evidence behind it.

### Script — ≈76 words · 0:35

MESA is the Meta-Evaluation Standard for AI Benchmarks. Two parts: describe the benchmark, then
evaluate whether it supports what people claim from it. The thing under review is the benchmark, not
the model. And it is written for the person reading the score, not the person building the test.
Three questions drive the paper: how to adapt the standard; what evidence a trustworthy
interpretation needs at minimum; and what MESA finds across three very different benchmarks.

*Transition:* "First, where the content comes from."

---

## Slide 7 — Source Base

**Format:** **big stat + source rows** (RADAR 26) above a **figure band** (RADAR 8).
**Why:** provenance is composition data — counts and origins, not parallel concepts.
**Source:** Table `tab:benchmark-source-inventory`, Figure `fig:mesa-methodology-pipeline`; corpus
counted from `literature/`.

**The figure exists.** It shows five input arrows feeding the MESA Review Model box — *15 modern AI
benchmarks*, *Supporting Literature around AI and RE* (which branches into *Software Engineering
Practices*, *AI Cognitive Abilities Mapping*, and *Construct Validity Measurement*), and the *EFPA
Test Review Model (2025 Edition)* — with the model's twelve numbered sections inside, then an
`Applied to` arrow out to *Test cases*.

**Left — stat block**

> # 15
> benchmarks read
>
> # 13
> source documents
>
> # 21
> works cited

**Right — what each source gave.** These rows mirror the figure's five input arrows one-for-one, so
the table and the diagram beneath it use the same names. Do not use a second taxonomy here.

| Source | Gave MESA |
|---|---|
| **15 modern AI benchmarks** | What current benchmarks actually do |
| **Software engineering practices** | Upkeep, reproducibility, leak controls |
| **AI cognitive abilities mapping** | Coverage, and flags for sweeping claims <sup>1</sup> |
| **Construct validity measurement** | Ability → task → score → claim |
| **EFPA Test Review Model (2025)** | The two-part structure and the rating scale |

*(Benchmark names and critique titles are on backup B2 — off this slide.)*

**Lower band:** `figures/mesa-methodology-pipeline.png`, full width.

> **Watch the overlap with slide 9.** The figure contains all twelve numbered sections, and slide 9
> presents them grouped into four and four. Shown small here that is fine — the eye reads the arrows
> on the left, not the boxes. But do not zoom or highlight the twelve boxes on this slide, or slide 9
> lands as a repeat and the differing counts read as an inconsistency.

**Banner:** `Objective:` Every field traces to a named source.

**Footnote band**

> <sup>1</sup> *Claim proportionality*: one task family is narrow evidence for a broad claim.

### Script — ≈96 words · 0:44

MESA's fields are not invented; they are sourced. Fifteen current benchmarks — from Humanity's Last
Exam and ARC-AGI-2 to SWE-Bench and Global PIQA — were read as raw material. Alongside them, thirteen
source documents, each feeding a specific part of the review. The psychology test standard supplies
the structure and the rating scale. BetterBench supplies the upkeep questions — reproducibility, and
leaked test data. Six critique papers supply the question of whether a claim matches its evidence.
Measuring What Matters supplies the chain from ability, to task, to score, to claim. Every field
traces back to a named source.

*Transition:* "That standard gives the skeleton — but it was written for people."

---

## Slide 8 — Adapting the Standard

**Format:** **before → after table**.
**Why:** every row is a transformation. Four cards showed one side at a time; the table shows both.
**Source:** `paper_old.tex` §Framework Construction.

Column heads: `HUMAN TESTING` **→** `AI BENCHMARK`. Rule tags color-coded on the left edge.

| Rule | Human testing | AI benchmark |
|---|---|---|
| `KEEP` *(blue)* | Job transfers unchanged | Leave it alone |
| `RENAME` *(green)* | Test taker | The AI system |
| `RENAME` *(green)* | Target population | Model class |
| `RENAME` *(green)* | Score report | Paper · dashboard · leaderboard |
| `REPLACE` *(amber)* | Population norms | Guessing baseline · human results · other models · cut-offs |
| `ADD` *(red)* | — | Prompt templates · secret splits · grading code · model-as-judge <sup>1</sup> · leak controls · leaderboard governance |

**Banner:** `Novel Contribution:` Fields carry over by what they do, not what they are called.

**Footnote band**

> <sup>1</sup> *Model-as-judge*: one AI model grades another model's answers.

### Script — ≈105 words · 0:48

The adaptation was about function, not wording — four rules. Keep a field when its job transfers
directly. Rename it when the job transfers but the human wording misleads: the person taking the test
becomes the AI system being evaluated. Replace a field when it assumes a human sitting an exam:
population norms become reference points — the score you'd get by guessing, how humans and experts
did, pass-fail cut-offs. And add fields the original would miss entirely: prompt templates, secret
question sets, the grading code, model-as-judge behaviour, controls against leaked test data, and who
governs the leaderboard. That last group is what makes this an AI benchmark review.

*Transition:* "Here is the resulting model."

---

## Slide 9 — The MESA Model

**Format:** **two-stage flow** — Part A, big arrow, Part B.
**Why:** the order is the contribution. Two side-by-side cards imply they are simultaneous; an arrow
says describe *then* judge.
**Source:** Table `tab:mesa-review-structure`.

> **Use the figure's colours.** `mesa-methodology-pipeline.png` already codes Part A blue and Part B
> green. Slide 9 uses the same blue #EAF3FB and green #EAF7EF, so the figure on slide 7 and this
> slide read as one system rather than two diagrams of the same thing. The yellow *Final Review* box
> in the figure has no home on this slide — it is covered by slide 10's "no averaging" rule.

**Stage A** (blue block, left) `PART A · DESCRIBE`

> **Identity** — What it is, who made it
> **Claims** — What it says it measures
> **Scoring** — How behaviour becomes a number
> **Materials** — Data, splits, licences, upkeep
>
> *Never judges. Missing is recorded as a gap* <sup>1</sup>

**→** *(large arrow)*

**Stage B** (green block, right) `PART B · EVALUATE`

Phrased as the question each group actually asks — a noun alone ("Stability") does not tell a
first-time viewer what is being checked.

> **Quality** — Is the benchmark well made?
> **Comparison** — Is there anything to compare against?
> **Stability** — Would the score come out the same again?
> **Meaning** — Does the score mean what it claims?

**Callout beneath, full width** `WHAT "STABILITY" MEANS` *(amber)*

Stability is the least intuitive of the four and the one that bottoms out for all three benchmarks on
slide 12, so it gets the space. Numbers illustrative — see below.

> Same model. Same questions. Run it twice.
> **71%** … then **68%** — and nothing about the model changed.
>
> **So a two-point gap between two models may be noise.**
>
> MESA checks this across: runs · prompt wording · graders · versions · machines

> **Why the numbers are invented.** No benchmark reviewed here publishes its run-to-run variance —
> that absence *is* the finding, and it is why Stability is rated 1 across the board on slide 12.
> Tag the pair as illustrative, the same way slide 3 is tagged.

**Banner:** `Key Idea:` Describe before judging. Missing is not the same as bad.

**Footnote band**

> <sup>1</sup> MESA calls this an *evidence gap* — information absent, rather than inadequate.

*(The full §1–§12 section list with numbering is on backup B1.)*

### Script — ≈109 words · 0:50

The model has two parts, and the order matters. Part A, sections one to five, only describes: what
the benchmark is, where it came from, how behaviour turns into a score, and what materials exist.
Part A never judges — if something is missing, it is recorded as a gap rather than guessed at. Part B
then asks the evaluative questions. Stability is the one people find slippery, so take it concretely:
same model, same questions, run it twice, and the score moves. Nothing about the model changed. So a
two-point gap on a leaderboard may be nothing at all. Not one of the three benchmarks we reviewed
publishes that number.

*Transition:* "So how does a rating actually get assigned?"

---

## Slide 10 — Rating Logic

**Format:** **scale strip** across the top + **three-card contrast** below.
**Why:** the whole slide exists to teach one distinction — 0 versus 1. A block of text asserts it;
three cards showing the *same question* answered three ways lets the audience see it. The ratings
become self-explanatory by contrast.
**Source:** `paper_old.tex` §The MESA Test Review Model, §Case Study Design.

**Scale strip** — one horizontal band, six segments, callouts on the two that matter:

```text
 n/a  │  0  │  1  │  2  │  3  │  4
         ▲     ▲                  ▲
```

> **0** — Applies. No information.
> **1** — Evidence exists. Not good enough.
> **2 · 3 · 4** — Adequate · good · excellent.

*The paper defines 0 and 1 precisely; 2–4 follow the EFPA convention. Keep this wording identical to
slide 12's legend.*

**One line across the slide, above the cards** — the same question, asked of three benchmarks:

> ### *"Would the score come out the same again?"*

**Three cards beneath it.** Same question, three states of evidence, three ratings. Each card leads
with an oversized numeral in its own colour, so the row reads as a gradient before anyone reads a
word. Deliberately the stability question carried over from slide 9, so nobody has to learn a new
dimension here.

| | `0` *(red)* | `1` *(amber)* | `3` *(green)* |
|---|---|---|---|
| **What you find** | Nothing. The benchmark never mentions running anything twice | A margin of error, buried in the grading code | Repeat runs published · error bars on every score · reworded prompts tested |
| **So the rating is** | **Silence — not bad quality** | **An answer that doesn't cover the use** | **Good** |
| **Why** | Nothing to judge | Ranked by fractions of a percent — this is not enough for that | Score differences can be trusted |

Beneath card 3, in small grey type: *No benchmark reviewed here reached this.*

**Thin strip beneath all three** `NO AVERAGING`

> Ratings are never summed. The final judgement states what the score can support, what it cannot,
> and what must be held fixed for a comparison to mean anything.

**Banner:** `Key Idea:` Zero is silence. One is evidence that does not cover how the score is used.

### Script — ≈110 words · 0:51

Ratings run from not-applicable, then zero to four, and one distinction does most of the work. Take
a single question — would the score come out the same if you ran it again? A zero means the benchmark
says nothing at all. That is silence, not bad quality. A one means there is something — say a margin
of error buried in the grading code — but no repeat runs, and no test of whether rewording changes
the answer. For a leaderboard ranking models by fractions of a percent, that is not enough. A three
would mean repeat runs published and error bars on every score. None of the three benchmarks we
reviewed got there.

*Transition:* "We ran this on three benchmarks."

---

## Slide 11 — Case-Study Design

**Format:** **comparison table** above a **figure band**.
**Why:** three benchmarks compared on identical attributes. A table makes the contrast readable in
one pass; three cards force the eye to jump.
**Source:** `paper_old.tex` §Case Study Design, Figure `fig:mesa-test-case-pipeline`.

**The figure exists** and matches this slide's claim exactly: *MESA Test Review Model + HLE,
ARC-AGI-2 and DesignQA source data* → fed in parallel to *Reviewer 1 (ChatGPT 5.5)* and *Reviewer 2
(Claude Opus 4.7)*, each writing its own MESA reviews → both fed to the *Supervising Editor
(Gemini 3.1 Pro)*, which removes discrepancies → *Final MESA Evaluations*. The two reviewer branches
are visually symmetric, which is the point — neither drafts first.

| | `HLE` | `ARC-AGI-2` | `DESIGNQA` |
|---|---|---|---|
| **Task** | Academic questions | Grid puzzles | Engineering rulebook <sup>1</sup> |
| **Size** | 2,500 public | 120 evaluation tasks | 1,451 questions |
| **Grading** | Another AI model | Exact grid match | Word overlap |
| **Setting** | Official prompt | Fixed compute budget | Rules given, or searched <sup>2</sup> |
| **Framing** | Expert-level | Progress toward AGI | No broad claims |

**Lower band:** `figures/mesa-test-case-pipeline.png` — two reviewer models (ChatGPT 5.5, Claude
Opus 4.7) drafting independently, reconciled by an editor (Gemini 3.1 Pro) against the sources.

**Banner:** `Objective:` Workable and complete. Not a validation study.

**Footnote band**

> <sup>1</sup> The Formula SAE rulebook — technical rules for a student engineering competition.
> <sup>2</sup> *Retrieval-augmented*: the model finds the rules itself, so the two settings are not
> comparable.

### Script — ≈96 words · 0:44

We applied MESA to three benchmarks chosen to be as different as possible. Humanity's Last Exam: hard
academic questions, graded automatically by another AI model. ARC-AGI-2: visual grid puzzles with
secret test sets, publicly framed as progress toward general intelligence. DesignQA: questions about
a real engineering rulebook and CAD data — the closest of the three to actual requirements work. To
limit single-reviewer bias, two models drafted each review independently, and a supervising editor
reconciled every disagreement against the sources. This shows MESA is workable and covers what it
should. It is not a validation study.

*Transition:* "Here is what came out."

---

## Slide 12 — Results

**Format:** **tinted data table** (RADAR 20) + one finding block.
**Why:** the pattern across the cells *is* the finding. Tint the cells and the floor is visible
before a word is spoken.
**Source:** Table `tab:pilot-ratings`.

**Scale legend — put this above the table.** Nothing else on the slide says what a 2 is, and by this
point the scale was last seen two slides ago.

> `SCALE`  **n/a** not applicable · **0** no information · **1** some, not enough ·
> **2** adequate · **3** good · **4** excellent
>
> *Only 1, 2 and 3 were ever used across the three reviews.*

**Row labels carry the question they stand for.** A bare noun — "Comparators," "Meaning" — tells a
first-time viewer nothing. Bold label, then the plain question beneath it in the same cell.

**Cell tint:** `1` light red · `2` light amber · `3` light green.

| Part B asks | HLE | ARC-AGI-2 | DesignQA |
|---|---|---|---|
| **Purpose and tasks** — Is it clear what is measured? | 2 | 3 | 3 |
| **Materials** — Can you get it and run it? | 3 | 3 | 2 |
| **Comparators** — Anything to compare against? | 2 | 3 | 2 |
| **Stability** — Same score if you run it again? | **1** | **1** | **1** |
| **Meaning** — Does it measure what it claims? | **1** | **2** | **2** |
| **Fair use** — Are systems compared on equal terms? | 2 | 2 | 2 |
| **Reporting** — Do leaderboards state the limits? | 2 | 2 | 2 |

*These seven rows are Part B §6–12. They are the four groups from slide 9 opened up: Quality covers
the first two, Comparison covers Comparators and Fair use, Stability is its own, and Meaning covers
the last two. Say this only if asked — do not spend slide space on it.*

**Finding block, right** (amber)

> `★ THE FLOOR`
> **Stability and Meaning bottom out.** All three benchmarks.
> Missing evidence — not bad construction.

**Banner:** `Interpretation:` Ratings are evidence-grounded judgements, never averages.

### Script — ≈113 words · 0:52

These are the reconciled ratings — same scale you just saw, where one means evidence exists but
doesn't cover the use. Read down the two highlighted rows: one, one, one — and one, two, two. That is
the floor, across all three benchmarks. Notice nothing scored zero, and nothing scored four. The
pattern is not about bad construction. It reflects missing measurement evidence: almost no reporting
of how much a score could shift, and incomplete checking of what a score difference actually means.
For the first two, the public framing outruns what the tasks can show. DesignQA claims less, but its
test set is fully public, its licence unclear, and there is no human baseline.

*Transition:* "Which brings me to the output that actually matters."

---

## Slide 13 — Supported Use

**Format:** **can / cannot matrix** — three columns, two banded rows.
**Why:** this is one comparison, not three independent findings. The green band and the red band
each read straight across.
**Source:** the three "MESA therefore supports…" paragraphs.

| | `HLE` | `ARC-AGI-2` | `DESIGNQA` |
|---|---|---|---|
| ✔ **CAN** *(green band)* | Closed-book academic performance · Spotting overconfidence | Rule induction under stated conditions · Identical setups only <sup>1</sup> | Group-by-group diagnosis · Gaps above 10–15 points |
| ✖ **CANNOT** *(red band)* | Position-by-position ranking · "Expert-equivalent" · General intelligence | Standalone AGI claims · Human-level versatility | Fine-grained ranking · Buying decisions · Cross-setting comparison |

**Banner:** `Overall Observation:` All three support a narrower reading than their framing suggests.

**Footnote band**

> <sup>1</sup> Setup includes the code wrapped around the model — often called *scaffolding*. Same
> model, different wrapper, different score.

### Script — ≈113 words · 0:52

This is the output that matters — not a grade, but a boundary. Humanity's Last Exam supports
measuring performance on closed-book academic questions under the official setup, and spotting when a
model is overconfident. It does not support ranking models position by position, or calling anything
expert-equivalent. ARC-AGI-2 supports measuring whether a system can work out a rule from a few
examples — under stated conditions, and comparable only across identical setups. It does not support
standalone claims about general intelligence. DesignQA supports diagnosis group by group, with the
setting held fixed. It does not support buying decisions or broad claims about engineering
competence. All three support a narrower reading than their public framing suggests.

*Transition:* "Let me close."

---

## Slide 14 — Contributions

**Format:** **cards** (RADAR 22).
**Why:** three genuinely parallel, independent things. This is what cards are for.
**Source:** `paper_old.tex` §Discussion, §Limitations, §Future Work.

**Card 1 — `CONTRIBUTION`** *(blue)*

> **Discipline**
> Describe before judging
>
> **Framing**
> Benchmark use as traceability
>
> **Vocabulary**
> Drops into a specification

**Card 2 — `MINIMUM EVIDENCE`** *(green — this answers RQ2)*

> **Defined target** — With stated non-uses
> **Checked grading** — Including AI graders
> **Reference points** — Measured the same way
> **Published ranges** — How much scores move
> **Leak controls** — And version tracking

**Card 3 — `LIMITS & NEXT`** *(amber)*

> **Drafted by models** — A demonstration, not adjudication
> **Judgement-based** — By design
> **Three benchmarks** — More will follow
>
> ↓
> Multi-reviewer validation · Compact scorecard

**Banner:** `Contribution Summary:` A claim backed by a score is only as strong as the evidence
behind it.

### Script — ≈82 words · 0:38

To close: the contribution is the discipline of describing a benchmark before judging it, plus a
vocabulary — gaps in evidence, claims that outrun evidence, statements of what a score may and may
not be used for — that drops straight into a requirements specification. The limits are real: the
reviews were drafted by models, the ratings are judgements, and there are only three benchmarks. Next
is multi-reviewer validation and a compact scorecard. The direction is benchmark audits feeding
assurance cases and buying decisions.

---

## Slide 15 — Thank You

**Format:** closing (RADAR 24).

> **Everything is open**
> `github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai`
> Template · three full reviews · manuscript source
>
> **References**
> EFPA, *Test Review Model 2025* · Reuel *et al.*, *BetterBench*, NeurIPS 2024 ·
> Bean *et al.*, *Measuring what Matters*, NeurIPS 2025 · Hendrycks *et al.*,
> *A Definition of AGI*, 2025
>
> **Vitor Raposo** · Supervised by **Dr. Sanaa Alwidian**
> Ontario Tech University · ✉ vitor.raposo@ontariotechu.net
>
> **Questions welcome.**

### Script — ≈23 words · 0:11

The template, the three full reviews, and the paper source are all open in the repository. Thank you
— I'm happy to take questions.

---

## Glossary

Each term defined **once**, on the slide listed.

| Slide | # | Term | Footnote wording |
|---|---|---|---|
| 2 | 1 | contamination | Called *contamination*. |
| 2 | 2 | saturation | Called *saturation*. |
| 2 | 3 | construct validity | A *construct validity* problem: whether a test measures what it claims to measure. |
| 3 | 1 | word-overlap grading | Graded by word overlap against a single reference answer. |
| 4 | 1 | psychometrics / EFPA | *Psychometrics* — measurement science for human testing. EFPA = European Federation of Psychologists' Associations. |
| 5 | 1 | AERA/APA/NCME Standards | *Standards for Educational and Psychological Testing*, 2014 — the American counterpart to EFPA. |
| 5 | 2 | Cattell–Horn–Carroll | Intelligence as a profile across many ability domains. |
| 7 | 1 | claim proportionality | One task family is narrow evidence for a broad claim. |
| 9 | 1 | evidence gap | Information absent, rather than inadequate. |
| 8 | 1 | model-as-judge | One AI model grades another model's answers. |
| 11 | 1 | Formula SAE | Technical rules for a student engineering competition. |
| 11 | 2 | retrieval-augmented | The model finds the rules itself, so the two settings are not comparable. |
| 13 | 1 | scaffolding | The code wrapped around the model. Same model, different wrapper, different score. |
| B3 | 1 | pass@2 | A task counts as solved if either of two attempts is right. |

Fourteen notes. Maximum on any slide is three (slide 2). Slides 1, 6, 10, 12, 14, 15 carry none.

*"Confidence interval" no longer appears in the deck — slide 10 says "error bars" instead, which
needs no footnote.*

---

## Anticipated questions

**"You criticise model-as-judge, but your own reviews were drafted by models."**
Fair, and it is why the paper calls this a feasibility demonstration rather than a validation study.
Two differences: MESA's drafts were produced independently by two models and reconciled by a third
against the sources, with every judgement traceable to quoted evidence — and the output is
human-inspectable prose, not a number on a leaderboard. The declared next step is exactly the fix:
multi-reviewer human panels with inter-rater agreement. Slide 14 says this on the record.

**"Isn't this just BetterBench with extra steps?"**
BetterBench scores a benchmark against best practice for its builders. MESA asks a different
question, for a different reader: given this score, what may I claim? That is why the output is a
supported-use and non-use statement rather than a quality score.

**"Why psychometrics? AI isn't human cognition."**
MESA does not claim benchmarks measure human cognition. It borrows the *review architecture* —
describe before judging, tie every judgement to evidence, state what a score cannot support. That
architecture is about instruments, not about people.

**"Three benchmarks is a small sample."**
Correct, and the paper says so. They were chosen for contrast, not coverage — different task
formats, scoring procedures, and public framing — to test whether the template holds across them.

---

## Backup slides

After the thank-you, RADAR 25–27 convention. Pull up on demand.

| # | Slide | Holds |
|---|---|---|
| B1 | Full review structure | Table `tab:mesa-review-structure` — all 12 sections **with their numbering**, plus the general description and final judgement. The detail compressed out of slide 9. Also carries the deliberate-overlap point: one prompt template is recorded in Part A, then re-examined in §7 as usability, §9 as a stability risk, §10 as a threat to meaning, and §12 as an interpretation condition — each section asking a different question of the same artifact |
| B2 | Full source list | All 15 benchmark names and the 6 critique titles — see below. Compressed out of slide 7 |
| B3 | ARC-AGI-2 detail | 407 people tested, 515 sessions, 13,405 attempts, two independent solves required per task · 120 tasks, so 1% is about one task · offline sandbox with a 12-hour budget on four GPUs versus hosted interfaces · a two-versus-three attempt inconsistency against the official rule <sup>1</sup> · no per-task category labels |
| B4 | DesignQA detail | Six question groups · smallest has 16 questions, so one question moves the score 6.25 points · test set fully public, and the paper discusses training on part of it · exact-format grading against one reference answer · no human baseline, no licence file, no versioned releases |
| B5 | Threats to validity | Threats to what MESA measures, how consistently it is applied, how far it generalises · the template is a living document, so pin the version used |
| B6 | MESA on itself | Ability → task → score → claim turned back on MESA · why it refuses to emit one overall quality number |
| B7 | HLE detail | Displaced from the earlier motivating example: 2,500 public questions plus a held-back set · graded by another AI model, never checked against human graders · experts disagree on 15–18% of items · an independent re-check found up to 30% of chemistry and biology answers likely wrong · no repeat runs · no human baseline under the benchmark's own no-tools rules · leaderboard drops the paper's non-AGI caveats |
| B8 | Full references | Every work named anywhere in the talk — see below |

### B8 contents — full reference list

**Benchmark critique**
S. Singh *et al.*, "The Leaderboard Illusion," arXiv:2504.20879, 2025 ·
J. Fodor, "LINE GOES UP? Inherent Limitations of Benchmarks for Evaluating LLMs," arXiv:2502.14318, 2025 ·
N. Jo and A. Wilson, "What Does Your Benchmark Really Measure?", arXiv:2509.19590, 2025 ·
O. Alonso and K. Church, "Evaluating the Evaluations: A Perspective on Benchmarks," ACM SIGIR Forum 58(2), 2024 ·
Z. Cheng *et al.*, "Benchmarking is Broken — Don't Let AI be its Own Judge," NeurIPS 2025

**Documentation and benchmark-quality standards**
A. Reuel *et al.*, "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices," NeurIPS 2024 ·
T. Gebru *et al.*, "Datasheets for Datasets," CACM 64(12), 2021 ·
M. Mitchell *et al.*, "Model Cards for Model Reporting," FAT* 2019

**Measurement and test review**
EFPA, *Test Review Model — Version 2025* ·
AERA/APA/NCME, *Standards for Educational and Psychological Testing*, 2014 ·
A. M. Bean *et al.*, "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," NeurIPS 2025 ·
D. Hendrycks *et al.*, "A Definition of AGI," arXiv:2510.18212, 2025 ·
G. L. Canivez and E. A. Youngstrom, "Challenges to the Cattell-Horn-Carroll Theory," *Applied Measurement in Education* 32(3), 2019

**Requirements engineering for AI**
U. Habiba *et al.*, "How Mature Is Requirements Engineering for AI-Based Systems?", *Requirements Engineering* 29, 2024

**The three reviewed benchmarks**
L. Phan *et al.*, "Humanity's Last Exam," arXiv:2501.14249, 2025 ·
F. Chollet *et al.*, "ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems," arXiv:2505.11831, 2025 ·
A. C. Doris *et al.*, "DesignQA: A Multimodal Benchmark for Evaluating LLMs' Understanding of Engineering Documentation," arXiv:2404.07917, 2024 ·
M. Skarlinski *et al.*, "About 30% of Humanity's Last Exam Chemistry/Biology Answers are Likely Wrong," FutureHouse, 2025

### B2 contents — the lists taken off slide 7

**The 15 benchmarks read as source material** (`tab:benchmark-source-inventory`)

| Benchmark | Tests | Benchmark | Tests |
|---|---|---|---|
| Humanity's Last Exam | Academic reasoning | Video-MMMU | Learning from video |
| ARC-AGI-2 | Visual reasoning puzzles | LiveCodeBench Pro | Competitive coding |
| DesignQA | Engineering requirements | SWE-Bench Verified | Agentic coding |
| GPQA Diamond | Scientific knowledge | tau2-bench | Agentic tool use |
| AIME 2025 | Mathematics | Vending-Bench 2 | Long-horizon agency |
| MathArena Apex | Contest mathematics | MMMLU | Multilingual QA |
| MMMU-Pro | Multimodal reasoning | Global PIQA | Cross-cultural commonsense |
| OmniDocBench 1.5 | Document OCR | | |

**The 6 critique papers** — The Leaderboard Illusion · Line Goes Up? · What Does Your Benchmark
Really Measure? · Evaluating the Evaluations · PeerBench · Prioritization First

---

## Build checklist

1. **Export the two figures.** Both exist and are correct. `figures/mesa-methodology-pipeline.png`
   (slide 7) and `figures/mesa-test-case-pipeline.png` (slide 11) are referenced by `paper_old.tex`
   but are not committed — there is no `figures/` directory. Export at presentation resolution and
   commit them, so the deck and the paper draw on the same asset.
2. **Build the six new formats first** — they have no RADAR slide to copy verbatim: the broken chain
   (slide 2), the narrative flow (slide 3), **the transfer diagram (slide 5)**, the two-stage flow
   (slide 9), and the scale strip plus three-card contrast (slide 10). Everything else duplicates an
   existing RADAR layout.
3. **Slide 5 is the argument.** Both columns must be readable as a pair, and the converging arrows
   must land on MESA. If the layout gets crowded, drop the CHC box's sub-line before dropping any of
   the three named foundations.
4. **Tint the cells on slide 12.** The heatmap is doing the argument's work; without it the table is
   just numbers.
5. **Check item counts.** Four per card or column, five only on slide 14's minimum-evidence card and
   slide 11's attribute table.
6. **Check footnotes** against the [Glossary](#glossary) — three maximum, each term defined once.
7. **Rehearse against the word counts.** ≈1,386 words, **10:40** at 130 wpm — about 40 seconds over
   the slot. If the chair is strict, cut in this order for ~29 seconds: the last sentence of slide 2's
   script (it repeats the banner) · the Datasheets/Model Cards enumeration on slide 4 · "That last
   group…" on slide 8 · "chosen to be as different as possible" on slide 11 · "The pattern is not
   about bad construction" on slide 12. That lands at ~10:11 — still over, so a sixth and seventh cut
   are needed. Take them from slide 12's closing DesignQA sentence and slide 13's opening line, not
   from slide 3.
   Do **not** cut stages 2 and 3 of slide 3, or the rulebook/tyres example — they are what make the
   whole talk's premise legible to a first-time viewer.
8. **Confirm the ARC-AGI-2 and DesignQA numbers** against `reviews/` before the talk.
