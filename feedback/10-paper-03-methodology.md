# Feedback — `10-paper-03-methodology` (`paper.tex:92-139`)

Unit reviewed: Methodology — scope paragraph (:94), pipeline figure (:96-101), source-inventory
table (:105-124), and subsections III-A Framework Construction (:126-128), III-B Adaptation and
Evidence Integration (:130-134), III-C Intended Empirical Validation Strategy (:136-138).

III-C is the section's strongest part: it cleanly separates feasibility (this study) from
validation (future panels), names concrete measurands (inter-rater agreement, training effect,
panel-vs-pipeline comparison), and closes Reviewer 2's request — no findings there. The
preserve/rename/replace/add rule set is a good, honest adaptation methodology, and the
norms→reference-points and reports→leaderboards mappings verify against the delivered template
(Sections 8 and 4/12 respectively). The section's defects are one large duplication and one
missing procedure.

---

### F-10-paper-03-1 — [Major] The four adaptation rules and the added-fields list appear twice, nearly verbatim, in adjacent subsections
- **Axis:** repetition
- **Where:** `paper.tex:128` (III-A) and `paper.tex:132` (III-B)
- **Quote:** > ...following four rules: \emph{preserve} fields whose review function transfers directly to AI benchmarking; \emph{rename} fields when the function transfers but where the previous human-centric terminology is misleading; \emph{replace} fields when the original assumes human-assessment conditions incompatible with AI benchmarks; and \emph{add} AI-specific fields where the EFPA model would otherwise overlook a material benchmark dependency. *(:128)* — then — > The structural adaptation followed four foundational rules. First, preserve fields whose underlying review function transfers directly to AI benchmarking. Second, rename fields when the core function transfers but the human-centric terminology is misleading in the context of AI. Third, replace fields when the original framework assumes human-assessment conditions that are incompatible with AI benchmarks. Fourth, add AI-specific fields where the EFPA model would otherwise overlook a material benchmark dependency. *(:132)*
- **Why it fails a user:** ~95 words of :132 restate :128 with trivial rewording, and both paragraphs then repeat the identical eight-item engineering list ("prompt templates, hidden data splits, scorer code execution, model-as-judge behaviors, API runtime conditions, contamination controls, software versioning, leaderboard governance") — :132 even appends "and more" to the same list. This is the single largest verbatim redundancy in the paper, in the section a methods reviewer reads most carefully, and it is exactly the verbosity Reviewer 1 flagged. It also reveals a structural problem: III-A and III-B describe the same activity under two names.
- **Fix:** Delete the first two sentences of :132 (the rules restatement and the duplicated list, ~110 words); III-B then opens at "AI benchmark-quality literature was then integrated into the EFPA-derived structure." Alternatively merge III-A and III-B into one subsection "Framework Construction and Evidence Integration" — the surviving text already fits that title.
- **EFPA link:** The rules themselves are MESA-original methodology anchored on EFPA; the cut removes a duplicate statement, not the EFPA link, which survives at :128.

### F-10-paper-03-2 — [Major] How the 15 benchmarks produced template requirements is never stated
- **Axis:** vagueness
- **Where:** `paper.tex:128` (also :103 and the Table I title at :106)
- **Quote:** > As illustrated in Figure~\ref{fig:mesa-methodology-pipeline}, 15 benchmarks acted as input sources to help form a structural model adapted from the EFPA Test Review Model.
- **Why it fails a user:** The section claims a "rigorous and replicable review model" (:94), and the table is titled "Benchmarks Used as Source For Template Requirements" — but no sentence says what was done with the 15 benchmarks. Examined their documentation for review-relevant properties? Extracted failure modes? Piloted draft fields against them? A methods reader cannot replicate, or even assess, this step; "acted as input sources to help form" is not a procedure. Two competent readers would give different accounts of what happened.
- **Fix:** One or two sentences stating the actual procedure, e.g.: "For each benchmark we examined the official paper, repository, and leaderboard documentation, recording every property a reviewer would need to describe or judge the benchmark (task format, scoring pathway, access conditions, versioning, reported uncertainty). Properties not already covered by an EFPA field became candidates for the \emph{add} rule." Adjust to whatever was actually done — the fix is stating it, not embellishing it.
- **EFPA link:** MESA-original (the benchmark-inventory step has no EFPA counterpart), which is precisely why it needs explicit description.

### F-10-paper-03-3 — [Minor] "Verify ... comprehensive in coverage, and useful in practice" overclaims against III-C's own caveat
- **Axis:** claim support
- **Where:** `paper.tex:94`
- **Quote:** > The case studies are designed to verify that MESA is feasible to apply, comprehensive in coverage, and useful in practice, not to draw generalized conclusions...
- **Why it fails a user:** Three LLM-assisted case studies cannot *verify* comprehensiveness or practical usefulness, and :138 says so itself ("it does not yet validate MESA as a measurement instrument"). The section opener and closer disagree; a careful reviewer will quote them against each other.
- **Fix:** "The case studies are designed to demonstrate that MESA is feasible to apply and to probe its coverage and practical usefulness, not to draw generalized conclusions..." — aligning :94 with :138's calibrated claim.
- **EFPA link:** n/a — paper prose.

### F-10-paper-03-4 — [Nit] Table and cross-reference polish
- **Axis:** verbosity (polish)
- **Where:** `paper.tex:103, :106, :121`
- **Quote:** > Table~\ref{tab:benchmark-source-inventory} lists the benchmarks and primary evaluation focus used as the source for the template requirements. *(:103)* — > Modern AI Benchmarks Used as Source For Template Requirements *(:106)* — > OCR document analyzing *(:121)*
- **Why it fails a user:** Three small blemishes in the section's most-scanned artifacts: :103 reads as if the "focus" is the source; the table title capitalizes "For" and needs the plural; "OCR document analyzing" is not idiomatic.
- **Fix:** ":103 → "Table~\ref{...} lists the 15 benchmarks, and their primary evaluation focus, used as sources for the template requirements."; title → "Modern AI Benchmarks Used as Sources for Template Requirements"; cell → "OCR document analysis".
- **EFPA link:** n/a.

---

## Verdict
- **Disposition:** Trim (delete the :132 duplication; add the one missing procedure statement; consider merging III-A/III-B)
- **Items:** 6 prose paragraphs → 5 (≈ −110 words net, +2 sentences of procedure)
- **Rationale:** III-C is exemplary and the adaptation rules are sound, but the rules are stated twice in full while the one thing a methods reader actually needs — what was done with the 15 benchmarks — is never stated at all.
