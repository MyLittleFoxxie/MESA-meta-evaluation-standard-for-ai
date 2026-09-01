# Feedback — `10-paper-08-limitations` (`paper.tex:280-301`)

Unit reviewed: Limitations and Threats to Validity — Construct Validity (:284-286), Internal
Validity (:288-290), External Validity (:292-294), Open-Source Artifact (:296-300).

Construct and Internal Validity are in good shape: :286 honestly concedes that "another
adaptation might make differently", and :290 correctly distinguishes judgment-based ratings
(EFPA-consistent, by design) from generation bias (mitigated but not eliminated — "may still
share LLM blind spots" is the right hedge). These two subsections close Reviewer 1's
missing-threats criticism properly. The External Validity subsection, by contrast, appears to
have escaped editing entirely.

---

### F-10-paper-08-1 — [Major] The External Validity paragraph is unedited draft prose
- **Axis:** vagueness (grammar and register)
- **Where:** `paper.tex:294`
- **Quote:** > MESA was applied to three benchmarks chosen for contrast---HLE, ARC-AGI-2, and DesignQA--- and based of 15 benchmarks from widespread fields. While this is a very big span of possibilities, the ever-growing field of AI will no doubt lead to benchmarks that might fall out of the MESA's current scope.
- **Why it fails a user:** Five defects in two sentences: "based of" (for "built from"), a stray space after the em-dash, "a very big span of possibilities" (colloquial register far below the rest of the paper), "no doubt ... might" (certainty and doubt in the same clause), and "the MESA's" (article error). Worse, the paragraph lost the concreteness the remediation plan drafted for it (critique_plan.md Task 5 named live-evaluation systems and RL environments as the specific out-of-scope paradigms). This is the subsection reviewers read to gauge the authors' rigor about their own work.
- **Fix:** Rewrite: "External threats concern generalization. MESA was applied to three benchmarks chosen for contrast---HLE, ARC-AGI-2, and DesignQA---and its structure was derived from a 15-benchmark source inventory spanning diverse task families (Table~I). These cases nonetheless cannot represent every benchmarking paradigm: live-evaluation arenas, reinforcement-learning environments, and long-horizon agentic loops may stress MESA's sections in ways not yet observed, and the field will continue to produce benchmarks outside MESA's current scope."
- **EFPA link:** n/a — paper prose.

### F-10-paper-08-2 — [Minor] "Open-Source Artifact" is not a threat, and its closing sentence is promotional copy inside a limitations section
- **Axis:** complexity and cognitive load (structure)
- **Where:** `paper.tex:296-300`
- **Quote:** > \subsection{Open-Source Artifact} [...] Despite these threats, MESA offers an immediate, practical contribution: an open-source, replicable artifact that requirements engineers can apply today...
- **Why it fails a user:** The subsection sits under "Limitations and Threats to Validity" but its first paragraph states a reproducibility caveat (snapshot instability — genuinely a limitation) while its second paragraph rebuts the whole section ("Despite these threats..."). A structure-conscious reviewer (Reviewer 2 praised exactly this) will note that the section ends by advertising rather than limiting. The pin-the-commit guidance is valuable and should stay.
- **Fix:** Retitle the subsection "Artifact Evolution" and keep :298 (the snapshot/pinning caveat). Move :300's "immediate, practical contribution" sentence to the Conclusion, where it belongs and where its content is likely already echoed.
- **EFPA link:** n/a — paper structure.

---

## Verdict
- **Disposition:** Trim (rewrite one paragraph, relocate one sentence)
- **Items:** 4 subsections → 4 (≈ −15 words in :294, :300 moved)
- **Rationale:** Three of four subsections do their job well; the External Validity paragraph's draft-level prose is the paper's single worst passage and sits exactly where reviewers assess the authors' self-scrutiny.
