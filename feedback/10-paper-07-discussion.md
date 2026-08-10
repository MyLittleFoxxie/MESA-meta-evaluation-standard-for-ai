# Feedback — `10-paper-07-discussion` (`paper.tex:266-279`)

Unit reviewed: Discussion — five paragraphs: traceability reframing (:268), selection/acceptance
use (:270), trustworthy-AI positioning (:272), RQ2 answer (:274), contribution statement (:276),
RE vocabulary (:278).

The section does real work: :268 finally cashes the Introduction's traceability framing (the
term survives, answering the Cross-cutting log's watch); :276's unsupported-criticism /
unsupported-endorsement dichotomy is the paper's sharpest formulation of what MESA is for; and
:274 answers RQ2 with a concrete, checkable criteria list that traces back to the observed
case-study gaps. Findings concern the two RQs that never get such treatment and one uncited
load-bearing claim.

---

### F-10-paper-07-1 — [Minor] RQ2 is answered explicitly; RQ1 and RQ3 never are
- **Axis:** complexity and cognitive load
- **Where:** `paper.tex:274` (the only "\emph{Answering RQ...}" marker in the paper)
- **Quote:** > \emph{Answering RQ2}, the three test applications converged on a minimum set of criteria...
- **Why it fails a user:** The Introduction promises three research questions (:63-68). Only RQ2 receives an explicit answer marker; a reader (or reviewer) auditing RQ coverage must reconstruct that Section IV answers RQ1 and Section VI answers RQ3. The asymmetry reads as an oversight precisely because the RQ2 treatment is so clean.
- **Fix:** Two one-line additions: at the end of Section IV's overview (:142 block or :175), "\emph{Answering RQ1}, the preserve/rename/replace/add adaptation summarized above constitutes the mapping." At the head of the Overall-ratings discussion (:260 or :262), "\emph{Answering RQ3}, the interpretation risks and evidence gaps concentrate in reliability and validity..." — reusing sentences that already exist there.
- **EFPA link:** n/a — paper structure.

### F-10-paper-07-2 — [Minor] The regulatory-dependence claim is uncited
- **Axis:** claim support
- **Where:** `paper.tex:272`
- **Quote:** > This matters most for trustworthy AI, where fairness, robustness, reliability, and capability requirements increasingly depend on benchmark scores in both procurement and emerging regulatory frameworks.
- **Why it fails a user:** "Emerging regulatory frameworks" is the paragraph's factual anchor and the paper's strongest bid for policy relevance, yet it cites nothing — the same pattern as the Introduction's uncited ¶53 (F-10-paper-01-5). A skeptical reader asks *which* frameworks.
- **Fix:** Either cite (EU AI Act's benchmarking/GPAI evaluation provisions are the natural reference, if a suitable entry exists or can be added to `references.bib`) or make the claim self-supporting by example: "...in procurement and in emerging regulatory frameworks such as the EU AI Act's evaluation requirements for general-purpose models."
- **EFPA link:** n/a — paper prose.

### F-10-paper-07-3 — [Nit] The hold-fixed conditions list re-enumerates :177's, and :268 drops a serial comma
- **Axis:** repetition (polish)
- **Where:** `paper.tex:270` (first enumeration at `:177`); comma at `:268`
- **Quote:** > ...specify the benchmark version, split, prompt or harness, scorer, threshold, comparator, and non-use caveats... *(:270; :177 has "benchmark version, split, prompt, harness, scorer, comparator cohort, uncertainty, and run conditions")* — > ...must reason reliably, answer expert-level questions or act autonomously... *(:268)*
- **Why it fails a user:** The two seven-item condition lists differ just enough (threshold vs uncertainty; caveats vs run conditions) to make a careful reader wonder if they are different requirements. And :268 needs the serial comma before "or act autonomously".
- **Fix:** Align the :270 list verbatim with :177's (or truncate: "...specify the score conditions enumerated in Section IV and the non-use caveats..."); add the comma at :268.
- **EFPA link:** n/a.

---

## Verdict
- **Disposition:** Keep as-is (two small insertions, one alignment)
- **Items:** 5 paragraphs → unchanged (+2 sentences for RQ1/RQ3 markers)
- **Rationale:** The Discussion earns its length — traceability cashes out, the two-error dichotomy is the paper's best paragraph — but the RQ scaffolding erected in the Introduction is only one-third dismantled here.
