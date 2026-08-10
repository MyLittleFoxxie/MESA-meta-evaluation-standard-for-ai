# Feedback — `10-paper-01-introduction` (`paper.tex:51-71`)

Unit reviewed: Introduction — six paragraphs (:53, :55, :57, :59, :61, :70) and the three
research questions (:63-68).

Claim-support check (axis 7) passes on the load-bearing claims: the three declared sources of
MESA (:61) all correspond to verified template reality — EFPA structure (Part A/B, confirmed
throughout the Part A review), BetterBench-informed lifecycle fields (template :927 cites it
explicitly), and CHC-based capability domains (template :153-166, verified faithful to
`A_Definition_of_AGI.md:18-38`). The EFPA sentence (:57) correctly attributes the model's
lineage to the AERA Standards, matching `EFPA_Test_Review_Model_2025_Markdown.md:11`. The RE
bridge paragraph (:59) and DesignQA in RQ3 (:67) close Reviewer 1's RE-connection criticism
(critique_plan Task 2). No Major findings; what remains is sentence-level.

---

### F-10-paper-01-1 — [Minor] Two broken "where" clauses in the weaknesses paragraph
- **Axis:** vagueness (grammar)
- **Where:** `paper.tex:55`
- **Quote:** > ...prompt sensitivity (where scores varying significantly when prompt wording changes)... These problems threaten construct validity, where a model may score well because the benchmark is narrow, fragile, leaky, or poorly governed...
- **Why it fails a user:** "where scores varying" is ungrammatical, and "threaten construct validity, where a model may score well" attaches the "where" clause to nothing — the sentence that introduces the paper's key technical concept reads as broken English in the paragraph most likely to be quoted.
- **Fix:** "...prompt sensitivity (scores shift significantly when prompt wording changes)..." and "These problems threaten construct validity: a model may score well because the benchmark is narrow, fragile, leaky, or poorly governed rather than because the model is genuinely capable."
- **EFPA link:** n/a — paper prose.

### F-10-paper-01-2 — [Minor] "construct validity" reaches its first body use still undefined
- **Axis:** terminology
- **Where:** `paper.tex:55`
- **Quote:** > These problems threaten construct validity, where a model may score well because the benchmark is narrow...
- **Why it fails a user:** The sentence describes a *consequence* of failed construct validity but never says what the term means. An RE reader who knows "threats to validity" from empirical-SE checklists still may not know the psychometric sense. This is the flagged first body use from the abstract review (F-10-paper-00-5 context; Cross-cutting log entry) — the definition belongs exactly here.
- **Fix:** **Keep + define** (the term is load-bearing and EFPA/Standards-traceable): "These problems threaten construct validity — whether the benchmark actually measures the capability it claims to measure: a model may score well because the benchmark is narrow, fragile, leaky, or poorly governed..." One clause, then the existing consequence text follows naturally.
- **EFPA link:** EFPA Part B validity section (`EFPA_Test_Review_Model_2025_Markdown.md:613` context) — retained concept; the inline definition preserves traceability while serving non-psychometricians.

### F-10-paper-01-3 — [Minor] The traceability definition is circular and its follow-on sentence carries doubled qualifiers
- **Axis:** verbosity
- **Where:** `paper.tex:59`
- **Quote:** > The core operational requirement for benchmark use is \textit{traceability}, which reflects that a score interpretation should be traceable from claimed capability to task design, metric, score, comparison basis, and intended use. A score, however, is only as trustworthy as the measurement system that produced it, and that system's tasks, prompts, access conditions, scoring rules, baselines, and reporting surfaces may be poorly specified, unstable, or misaligned with the capability claim it is being used to support..., silently propagating undetected measurement weaknesses into safety, fairness, and reliability decisions.
- **Why it fails a user:** "Traceability ... reflects that ... should be traceable" defines the word with itself, and the 62-word second sentence stacks two six-item lists plus the redundant pair "silently propagating undetected" (silent and undetected say the same thing). The paragraph introduces the paper's central requirement; the reader should not have to parse it twice.
- **Fix:** "The core operational requirement for benchmark use is \textit{traceability}: every score interpretation should be traceable from claimed capability through task design, metric, and comparison basis to intended use. A score, however, is only as trustworthy as the measurement system that produced it — and that system's tasks, scoring rules, and reporting surfaces may be poorly specified, unstable, or misaligned with the claim they support \cite{...}, silently propagating measurement weaknesses into safety, fairness, and reliability decisions." (−18 words, one list per sentence.)
- **EFPA link:** MESA-original framing; no EFPA dependency.

### F-10-paper-01-4 — [Minor] "capability-area perspectives" and "execution bias" — two off-canon coinages in the contribution sentence
- **Axis:** terminology
- **Where:** `paper.tex:61`
- **Quote:** > ...applies Cattell-Horn-Carroll theory inspired construct-validity and capability-area perspectives... — and — > ...robust, reproducible, and free from execution or contamination bias...
- **Why it fails a user:** The template and CLAUDE.md's terminology list say "capability domain" (template 2.1 is titled "Claimed Capability Domains"); "capability-area" is a one-off variant in the very sentence that names MESA's third pillar, so a reader cross-referencing the template searches for the wrong term. "Execution bias" is undefined anywhere in the paper or template — a reader cannot tell if it means harness variance, implementation error, or something else. "Cattell-Horn-Carroll theory inspired" also lacks the hyphens the compound modifier needs.
- **Fix:** **Substitute both:** "...(3) applies construct-validity and capability-domain perspectives inspired by Cattell-Horn-Carroll (CHC) theory to discipline the inferential chain from phenomenon to task, metric, score, and claim" — and — "...robust, reproducible, and free from contamination and unstable-implementation artifacts".
- **EFPA link:** n/a — paper prose; the CHC pillar itself is MESA-original and correctly cited.

### F-10-paper-01-5 — [Minor] The opening paragraph's empirical claims carry no citations — the one Reviewer-1 comment still open
- **Axis:** claim support
- **Where:** `paper.tex:53`
- **Quote:** > In practice, benchmark scores are often treated as direct indicators of capability and reused as evidence for model selection, procurement, safety claims, and public narratives about what AI systems can do.
- **Why it fails a user:** Reviewer 1's comment "The introduction will benefit from additional citations" was addressed for ¶55 (jo_wilson) and ¶59 (leaderboard illusion, line goes up), but ¶53 — the paragraph making the paper's motivating empirical claim about how scores are *used* — still cites nothing. A camera-ready reviewer checking whether their comment was handled lands here first.
- **Fix:** Attach existing bibliography entries to the "in practice" sentence — `\cite{singh_leaderboard_illusion}` for leaderboard-driven interpretation and `\cite{alonso_church_sigir}` (or `reuel_betterbench`) for score reuse in evaluation practice. No new references needed.
- **EFPA link:** n/a — paper prose.

### F-10-paper-01-6 — [Minor] RQ1 restates the "RE-oriented" claim the artifact does not carry (extends F-10-paper-00-6)
- **Axis:** claim support
- **Where:** `paper.tex:65`
- **Quote:** > \textbf{RQ1}: How can the EFPA Test Review Model be adapted into an RE-oriented quality model for benchmark-based AI capability claims?
- **Why it fails a user:** Same gap as the title finding (F-10-paper-00-6): the delivered template is domain-general — no RE role in its audience list (template :9), no RE-specific items — so a reader who takes RQ1 literally will judge the answer (Section IV) as not RE-oriented. The RE orientation genuinely lives in the use context (V&V evidence, DesignQA), not in the instrument.
- **Fix:** Reword RQ1 to match what the paper actually answers: "How can the EFPA Test Review Model be adapted into a quality model for the benchmark-based capability claims used in RE for AI?" — orientation moves from the model to the claims, which is accurate.
- **EFPA link:** MESA-original framing; consistency issue with the artifact, not with EFPA.

### F-10-paper-01-7 — [Nit] Broken parallelism in the closing sentence
- **Axis:** verbosity (grammar)
- **Where:** `paper.tex:70`
- **Quote:** > ...judge which benchmark claims are supported, which are evidence gaps, and how benchmark scores should or should not be used.
- **Why it fails a user:** Claims are not gaps; the middle element breaks the series.
- **Fix:** "...judge which benchmark claims are supported, where the evidence gaps lie, and how benchmark scores should or should not be used."
- **EFPA link:** n/a — paper prose.

---

## Verdict
- **Disposition:** Trim (light copyedit; no structural change)
- **Items:** 6 paragraphs + 3 RQs → unchanged (≈ −8% words via F-1/F-3 rewrites)
- **Rationale:** The introduction's argument and its three-pillar contribution claim are accurate against the delivered template; the residual defects are two broken clauses, two off-canon coinages, one still-uncited motivating claim, and RQ1's inherited "RE-oriented" framing.
