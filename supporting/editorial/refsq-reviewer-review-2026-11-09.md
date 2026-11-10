# REFSQ reviewer assessment of both papers

Date: 9 November 2026. This is an assistant review in the role requested by the author, not a conference decision or human validation. Reviewed the working copies, including changes already present. No manuscript, study record, signature, protocol, or code was changed. No experiment or LaTeX compilation was run. Layout and page length are unchecked.

The assessment uses the [REFSQ 2027 research track criteria](https://2027.refsq.org/track/refsq-2027-research-papers). Technical design submissions require an artifact addressing a requirements problem and some evaluation. The ordered criteria concern novelty, relevance, soundness, verifiability, and presentation. This category does not impose a general requirement for a human study. The absence of human validation limits claims about people; it does not by itself require rejection.

## Acceptance assessment

| Paper | Recommendation in its present state | Reason | Route toward acceptance |
|---|---|---|---|
| MESA | Weak reject as a technical design paper | The mapping and review records address a research problem, but the opening claims go beyond the evidence, the derivation is too compressed, and the requirements application is presented with more authority than its evaluation warrants. | Make the contribution the comparison method and rubric; establish its traceability to source frameworks; align every claim with the model study; present the requirements application as a proposal. |
| Paper 2 | Reject as a completed technical design submission | The engine and checks provide a basis for a paper, but the main questions have no session results, and the chosen case already forces MESA to withhold every decision. Completing the sessions alone will not establish improved decisions. | Either report a bounded case demonstration of what the engine can and cannot conclude, or plan a separate evaluation with variation in evidence states that can test decision value. Keep existing records and do not tune policies to obtain decisions. |

These are judgments about the current argument and evidence, not probabilities of acceptance. A reviewer could weigh the contributions differently.

## What each paper contributes

MESA's gap is the difficulty of comparing reviews that ask different questions and treat absent information differently. The artifact comprises an item mapping, recoding rules, and a rubric that records the evidence behind a rating. The 18 framework sessions show what comparison under that mapping reveals; the eight rubric sessions show repeatability and source support under one model configuration. This has RE relevance when a team must assess evidence offered for a capability requirement. It does not establish how requirements engineers actually use the artifact.

Paper 2's gap is the missing operational step from a benchmark review to a decision about a specified requirement. The contribution that survives scrutiny is a set of records and executable checks that separate input integrity, evidence status, and statistical uncertainty, with reasons that can be inspected. The exploit checks and comparison with an audit are evidence about this case. Hash validation, signatures, a Wilson interval, and a checklist are not individually new; the paper must show what their integration makes possible that cited assurance and verification methods do not already provide.

The distinction between the papers can work: MESA defines how reviews can be represented and compared; Paper 2 applies a requirement specific profile and executes the decision procedure. Neither paper should claim the other's contribution as if it had independently established it.

## Findings to resolve before relying on the papers

### 1. MESA turns findings about model records into claims about engineers and software defects

Locations: [abstract](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:28), [introduction](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:44), [results definitions](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:269).

The introduction says engineers encounter contradictory verdicts and that existing protocols confuse missing paperwork with broken software. The results explicitly say the 210 answers pool unmet reporting requirements with unobserved practices, and do not establish that a framework was wrong to score them. The 13 are answer instances recording contradictions, not 13 independently confirmed software defects. The abstract's causal wording for the 92 disagreements also exceeds the later qualification that these are assistant interpretations under the mapping.

Change the headline claims to observations about recorded answers under this model configuration. Report the distinction between an unmet reporting obligation and an unknown practice. Keep the causal coding as an interpretation. This is a claim correction using saved evidence; no new experiment is needed.

### 2. MESA does not give enough method to assess the mapping and recoding

Locations: [mapping method](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:150), [study design](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:248), [aggregation](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:266).

The main contribution needs a reproducible account of framework inclusion, concern construction, author revision, item splitting, outcome recoding, and aggregation. The paper says the items were mapped from the source items but supplies little of that procedure. Its headline agreement pools comparisons of equivalent, overlapping, and grouped demands, although these have different meanings. Later sensitivity analysis helps but cannot make those demands equivalent.

Bring the actual derivation and operator into Methods. Use the author revision record in `v4/mapping/mapping-summary.md`; it records 100 differences from the assistant draft and their resolution, not coder agreement. Give one traced example from source item to concern, answer, and comparison verdict. Explain the uneven framework by benchmark coverage and the restricted repeat checks. If a distinction between comparison types has not been coded, do not imply that results have already been stratified by it.

I recomputed all five stage rows from `v4/mapping/mapping.csv`: the coverage table's 386 total is correct. The sentence that Caliper concentrates all its items on B23 needs qualification: every Caliper item maps there, but some also map to other concerns, as the table shows.

### 3. The source audit and repeatability summaries hide findings that matter for the contribution

Locations: [MESA abstract](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:30), [repeatability and audit](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:276).

The abstract ends with none unsupported, omitting 29 ratings with weaker support and six absence claims contradicted by the sources. This can be read as an error free audit although the detailed results show otherwise. Level plus outcome repeated on 83 of 124 pairs, which matters more to decision rules than level alone on 99 pairs. The pooled Part A alpha and the assumed Part B ordering also require care; evidence presence and a negative finding do not form a natural quality scale.

Report the audit categories together, foreground level plus outcome agreement, retain the ordinal result only as a sensitivity analysis, and distinguish quote matching from the assistant's interpretation of support. State that the audit is not an independent human check.

### 4. Paper 2 cannot answer an effectiveness reading of RQ2 in the selected case

Locations: [research questions](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:68), [analysis plan](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:287), [known outcomes](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:290).

Both policies already withhold MESA decisions for both agents because B28a fails. ABC's decision equals the raw score rule by design; its added output is caveats. The study can show how outputs differ and why MESA abstains. It cannot observe agreement between an issued MESA acceptance decision and the direct test because no such MESA decision will exist. A decision calculated before the gate is useful for explanation but is not MESA's issued decision. Two configurations are two cases, not a decision accuracy sample.

Before running sessions, decide whether RQ2 is a case comparison that explicitly includes noncomparability when MESA abstains, or a future effectiveness question requiring another design. The current sessions can still reveal score shifts, task removal effects, validity failures, and counterfactual decisions. Do not relax the gate after seeing those results. More repetitions of the same blocked case will not resolve this limitation.

### 5. Paper 2 omits the criteria that would justify its claim about transfer

Locations: [omitted criteria](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:103), [rationale](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:189), [transfer check](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:185).

Defining the target ability does not establish that benchmark tasks cover it. The engine checks that a transfer justification exists and matches scope; it does not assess its argument. RQ2 checks a later sample but is not a substitute for the evidence needed when the decision is made. Consequently this is an implementation of a restricted profile, not validation of MESA's full requirements assurance proposal.

Give the profile this bounded interpretation throughout. Separate structural validation of the argument record from support for its substance. If the full transfer claim is retained, it needs a documented assessment of task coverage and transfer, not only a signature.

### 6. The direct test is a comparison measurement, not ground truth

Locations: [requirement](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:42), [task selection](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:234), [analysis](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:287).

The target tests can also miss behaviors; their construction establishes before and after eligibility, not complete bug resolution. Source and target samples differ in dates, environments, and likely difficulty. The paper already notes some of these limits. Agreement, including two inconclusive outputs, cannot establish that a decision is correct. The literal requirement to pass maintainer tests is narrower than the surrounding adoption claims.

Keep the operational requirement and explain its boundary. Report agreement as agreement, disclose inconclusive and withheld outcomes separately, and avoid treating the direct test as an oracle for deployment suitability. This is a framing correction; new target audits would be a separate design choice requiring records.

### 7. Paper 2's discussion claims protection that its own simulation does not establish

Locations: [simulation interpretation](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:344), [discussion](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:352), [limitations](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:371).

The discussion says MESA prevents premature acceptance and protects procurement from false acceptance. Yet the simulation says most reduction comes from abstention, retained decisions can still be wrong, and no loss model establishes improvement. Also, 17 of 20 is the mechanical exploit result; only six satisfy the study's issue scope criterion. Neither those checks nor future session completion establishes procurement benefit.

Say the engine withholds decisions under the chosen conditions. Use six when referring to defects admitted under the study rule, and 17 only with its mechanical definition. Treat simulation as behavior under assumptions, not an estimate of MESA's accuracy. Add decision probabilities for the actual sample sizes 14, 18, and 20 if these calculations are to motivate the empirical design; the current table omits them.

### 8. Current state and independence claims need a record based correction

Locations: [pending observations](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:32), [pending signatures](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:224), [rating runs](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:243), [internal validity](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:374).

The abstract says rating observations remain future work despite reporting completed rating runs. The manuscript says signatures are pending, but the working tree contains a completed signed requirement and nine completed signed form records. The parent reviewer also found no frozen manifest or study ledger entries. These are existing records; this review created none.

The internal validity paragraph calls the rating runs independent and mentions ground truth criteria. The runbook records shared scratch interaction between the first runs and an ABC run that read the MESA prompt; the replacement run and retained earlier records require disclosure. Separate sessions and an author's signature do not establish independence or correctness. Restore those limits and reconcile the manuscript and runbook with the existing state before any next action. Do not sign again or overwrite records to make the text true.

### 9. State the novelty without universal absence claims or a claim to standard status

Locations: [MESA contribution](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/mesa_paper.tex:46), [Paper 2 gap](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:57), [related work conclusion](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2.tex:110).

Neither manuscript documents a search sufficient to establish that no prior study or approach addresses its stated gap. The related work supports a comparison with named approaches. It does not establish a universal absence. MESA is a proposed standard, with no evidence of community adoption or endorsement. Paper 2's executable integration should be distinguished from existing assurance contracts and test specification tools through a concrete example of input, rule, and output.

Use bounded claims about the compared approaches. Reserve MESA's contribution for mapping, evidence representation, and model observations. Reserve Paper 2's for implementation, case behavior, and transfer comparison. Reduce duplicated formalization and remove advice that sounds established when it is still a proposal.

## Other corrections

- Paper 2 calls its comparison five methods while listing raw score, audit only, ABA, MESA with two policies, and ABC. Use a stable grouping and label policies separately.
- MESA calls its terminology list ten terms but lists eleven.
- MESA describes all four benchmarks as Python benchmarks or runners. HumanEval is code generation; TruthfulQA and HLE are not thereby Python capability benchmarks. Describe their tasks and the Python implementation separately.
- Both Data Availability sections contain an unfilled anonymous package statement. Restore the repository link required by the project instructions and state what is actually accessible. Do not invent a review package or introduce a new anonymization task.
- Paper 2 calls sandbox checks verification of isolation early but later distinguishes settings from observations. Keep the limits of each check in both places.

## Recommended order before experiments

1. Reconcile existing signatures, forms, and freeze state without changing research records.
2. Decide and write the bounded purpose of Paper 2: case demonstration or a separate design for testing decision value. Preserve the current case regardless.
3. Correct claim inflation, rating independence, audit summaries, and task defect denominators.
4. Make MESA's mapping and recoding procedure inspectable and clarify the two papers' contribution boundary.
5. Check the requirement profile, transfer argument, and planned reporting of withheld and inconclusive outcomes before freezing any changed protocol.
6. Run only the authorized next phase under the recorded procedure; retain failures and deviations. Fill results from those records, without changing rules to improve the narrative.
7. Reassess acceptance from the resulting evidence. Passing implementation tests or completing all sessions will not alone settle relevance, novelty, or decision validity.
