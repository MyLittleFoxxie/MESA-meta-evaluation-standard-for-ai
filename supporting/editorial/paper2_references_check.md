# Paper 2 references check, 12 November 2026

Files checked: `paper2.tex`, `references.bib`, and `references_review_2026_11.md` (the record from 11 November 2026). Neither `paper2.tex` nor `references.bib` was changed.

## 1. Keys and entries

- `paper2.tex` cites 40 distinct keys. All 40 have an entry in `references.bib`, so no key is missing.
- No key appears twice in `references.bib`, which holds 119 entries.
- Two works have two entries each, under different keys. Paper 2 cites only one key of each pair, so nothing prints twice in Paper 2:
  - `goswami_assurance_envelopes_2026` (cited) and `coding_agent_assurance_envelopes_2025` (not cited) are the same arXiv paper, 2609.16302.
  - `mukhopadhyay_nalla_evidence_reuse_2026` (cited) and `ai_evidence_reuse_2026` (not cited) are the same arXiv paper, 2610.27672.
- The record lists `newcombe_difference_1998` as cited in Paper 2 in round 1, but `paper2.tex` does not cite it. The paper reports Newcombe intervals in Section 4.2 (exposure probes) and in Section 5.2 (RQ2) without a source.

## 2. Table

"Record" means the 11 November record. "Now" means checked on 12 November 2026.

| Key | Exists | Source checked | Bib errors | Fit to the citing sentence |
|---|---|---|---|---|
| `aleithan_swebench_plus_2024` | yes | Record: arXiv 2410.06992 | none found | Fits (Section 2, "Empirical audits of SWE-bench"). |
| `anonymous_companion_2027` | not searched (own work) | bib entry only: "Reviewing AI Benchmarks as Evidence for Requirements: One Rubric from Seven Frameworks", note "Companion paper under review" | n/a | Fits (Introduction, companion work). |
| `anonymous_companion_method_2027` | not searched (own work) | bib entry only: "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method", note "Companion paper under review" | n/a | Fits (Introduction, companion work). |
| `arief_vnvspec_2026` | yes | Record: arXiv 2607.17686; now: abstract | none found | **Mismatch.** Section 2 cites it for evidence that "fails defined validity conditions", where a claim is withheld. The paper links requirements to tests with a traceability graph and gives verdicts. Its abstract says nothing about withholding a claim. |
| `badertdinov_swe_rebench_2025` | yes | Record: arXiv 2505.20411 (listing names NeurIPS 2025) | The entry gives arXiv only, while the listing names NeurIPS 2025. You can keep it as is or add the venue. | Fits (dynamic benchmark that draws newer issues). |
| `berry_re4ai_2022` | yes | Record: Springer chapter page | none found | Partial fit (Introduction, sentence 1). Berry argues that evaluation measures and thresholds form the requirements of an AI system. He does not say that requirements engineers use coding leaderboards to select assistants. See `lewis_quality_model_ml_2026`. |
| `ding_spec_oracle_gaps_2026` | yes | Record: arXiv 2610.30635; now: abstract | none found | **Mismatch in name (Section 2):** the paper does not call its audit "SpecOracle". Partial fit in the Introduction: it studies SWE-Milestone and four benchmarks it does not name, not SWE-bench Verified, so it does not support "Independent audits of SWE-bench Verified". |
| `el_yaniv_selective_classification_2010` | yes | Now: JMLR page v11/el-yaniv10a | none found (JMLR 11, 1605 to 1641, 2010) | Fits (selective classification withholds a claim). |
| `ghosh_evaluation_cards_2026` | yes | Record: arXiv 2606.09809 | none found | Fits. |
| `goswami_assurance_envelopes_2026` | yes | Record: arXiv 2609.16302; now: abstract | Duplicate of `coding_agent_assurance_envelopes_2025` | Fits. When the evidence cannot re-establish a required property, the method reports that no envelope exists. |
| `gotel_traceability_1994` | yes | Now: Crossref 10.1109/ICRE.1994.292398 | none found (ICRE 1994, 94 to 101, IEEE Computer Society Press) | Fits, in a broad sense (requirements assurance). |
| `habiba_re4ai_maturity_2024` | yes | Record: Crossref 10.1007/s00766-024-00432-3 | none found | Partial fit (Introduction, sentence 1). It maps requirements engineering practice for AI-based systems. It does not show that coding leaderboards are used as evidence. |
| `hawkins_amlas_2021` | yes | Record: arXiv 2102.01564 | none found | Fits (requirements assurance perspective). |
| `hou_llm4se_survey_2024` | yes | Now: Monash and PolyU repository pages; Crossref 10.1145/3695988 | **DOI wrong:** the bib has 10.1145/3689498, and the correct DOI is 10.1145/3695988. **Missing:** volume 33, number 8, article 220. | **Mismatch.** Section 2 cites it among "Empirical audits of SWE-bench", but it is a broad literature review of language models in software engineering, not an audit of SWE-bench. |
| `jimenez_swebench_2024` | yes | Record: arXiv 2310.06770 | none found | Fits (Introduction and Section 3.1). |
| `kane_validation` | yes | Record: Crossref 10.1111/jedm.12000 | none found | Fits (validity of score interpretation). |
| `lawford_safety_case_impact_2017` | yes | Record: Crossref 10.1007/978-3-319-66266-4_5 | The key names the fourth author; first author is Kokaly. This does not print. | **Mismatch.** Section 2 cites it for "assurance contracts". The paper assesses how changes to a system affect its safety case. `sljivo_assurance_contracts_2014` is the work on safety contracts. |
| `lewis_quality_model_ml_2026` | yes | Record: arXiv 2602.05043; now: abstract | none found | **Mismatch** (Introduction, sentence 1). It is a quality model for ML components and does not mention leaderboards, benchmarks or coding assistants. |
| `liang_swebench_illusion_2025` | yes | Record: arXiv 2506.12286 | none found | Fits (training exposure). |
| `liu_ecbd_2024` | yes | Record: Crossref 10.18653/v1/2024.acl-long.861 | none found | **Mismatch.** Section 2 names it among "dynamic benchmarks ... [that] address contamination by drawing newer issues". ECBD is a framework for benchmark design. |
| `mohl_transcript_flaws_2026` | yes | Record: arXiv 2607.27518; now: abstract | none found | Partial fit (Introduction). It finds flaws in agentic benchmarks from Inspect Evals (ground truth access, tool failure) and names SWE-bench Verified only as earlier work. It does not support "Independent audits of SWE-bench Verified". |
| `mukhopadhyay_nalla_evidence_reuse_2026` | yes | Record: arXiv 2610.27672; now: abstract | Duplicate of `ai_evidence_reuse_2026` | Fits (validity conditions and a release gate that fails closed). |
| `nist_ai_800_2_2026` | yes | Record: NIST PDF | none found | Fits. |
| `openai_swebench_audit_2026` | yes | Record and now: OpenAI page "Separating signal from noise in coding evaluations" | **Month not confirmed:** the bib gives `jul`, and the page shows no date. | **Mismatch in three places.** The page audits SWE-bench Pro and does not list sympy-18199. (1) Introduction: "Independent audits of SWE-bench Verified ... overspecified tests". (2) Section 2: "OpenAI's February 2026 audit". The February page is `openai_swebench_verified_contamination_2025`. (3) Section 4.4: "listing sympy\_\_sympy-18199 as a task defect". That task is on the February page. |
| `openai_swebench_verified_2024` | yes | Now: OpenAI page "Introducing SWE-bench Verified" (13 August 2024) | none found. The page names its authors, while the bib uses "OpenAI" as the author. That is acceptable. | Fits (Introduction). |
| `openai_swebench_verified_contamination_2025` | yes | Record and now: OpenAI page (23 February 2026) | The key says 2025, while the entry gives 2026. This does not print. | Fits (training exposure). It is also the right source for the three sentences listed under `openai_swebench_audit_2026`. The page reports "narrow" tests that reject correct solutions, and it uses sympy-18199 as its example. |
| `picardi_transfer_assurance_2023` | yes | Record: CEUR volume 3381 | none found | Fits (transfer arguments). |
| `pizarro_beyond_the_hype_2026` | yes | Record and now: Crossref 10.1016/j.scico.2026.103530 (Science of Computer Programming 254, 103530) | none found | **Fit not confirmed.** No abstract could be read. From its title, it is about evaluating LLMs to inform adoption in industry, not about construct validity, which is the claim the sentence cites it for (Section 2). |
| `reuel_betterbench` | yes | Record: local copy | none found | Fits. |
| `singh_damsa_sms_2026` | yes | Record and now: MDPI page | none found | Partial fit. It drops candidates that violate hard constraints and reports a conditional shortlist. It does not withhold the decision. |
| `singh_leaderboard_illusion` | yes | Record and now: arXiv 2504.20879 | none found | **Mismatch.** Section 2 cites it among "Empirical audits of SWE-bench", but it studies Chatbot Arena. |
| `sljivo_assurance_contracts_2014` | yes | Record: Crossref 10.1007/978-3-319-10506-2_12 | none found | Fits where it is now (requirements assurance perspective). It would fit better as the citation for "assurance contracts". |
| `tu_benchguard_2026` | yes | Record: arXiv 2604.24955; now: abstract | none found | Fits. It finds evaluation scripts that penalize valid approaches, though in science and bioinformatics benchmarks, not SWE-bench. |
| `wang_auto_benchmark_audit_2026` | yes | Record: arXiv 2605.26079; now: abstract | none found | **Name wrong in the text** (Section 2): the paper calls its method "Auto Benchmark Audit (ABA)", not "AutoBenchmarkAudit". Otherwise it fits, and it covers SWE-bench Verified. |
| `wang_benchjack_2026` | yes | Record: arXiv 2605.12673; now: abstract | none found | Fits. It finds reward hacking exploits in 10 agent benchmarks, including software engineering ones. The abstract does not name editing of evaluation scripts specifically. |
| `wang_solved_issues_2026` | yes | Record: arXiv 2503.15223; now: ICSE 2026 program page and Crossref 10.1145/3744916.3764576 | none found. You can add pages 169 to 181 (ICSE 2026, the 48th edition). | Fits (Introduction and Section 2). |
| `whitfill_metr_merge_2026` | yes | Record and now: METR page (10 March 2026) | none found | **Mismatch.** Section 2 cites it for "Our study operationalizes those checks together inside one frozen contract". The note finds that maintainers would not merge about half of the patches that pass the SWE-bench Verified grader. |
| `yu_utboost_2025` | yes | Now: ACL Anthology 2025.acl-long.189 | Venue confirmed: ACL 2025, Volume 1 (Long Papers). You can add pages 3762 to 3774 and DOI 10.18653/v1/2025.acl-long.189. | Fits (Introduction and Section 2). |
| `zhang_swebench_live_2025` | yes | Record: arXiv 2505.23419 | none found | Fits. |
| `zhu_agentic_benchmark_checklist_2025` | yes | Record: NeurIPS 2025 page and arXiv 2507.02825 | none found (the title follows the NeurIPS proceedings) | Fits. The names of the three ABC parts given in Section 2 (T, O, R) were not checked against the paper. |

## 3. Actions

1. Fix the DOI of `hou_llm4se_survey_2024` to 10.1145/3695988, and add volume 33, number 8, article 220.
2. Replace `openai_swebench_audit_2026` with `openai_swebench_verified_contamination_2025` in the Introduction ("overspecified tests that reject valid solutions") and in Section 4.4 (sympy-18199). In Section 2, either cite `openai_swebench_verified_contamination_2025` for "OpenAI's February 2026 audit", or keep the current key and change the text to "OpenAI's audit of SWE-bench Pro".
3. Confirm or remove `month = jul` in `openai_swebench_audit_2026`. The page shows no date.
4. Remove `liu_ecbd_2024` from the Section 2 sentence on "dynamic benchmarks". Cite it only where the paper discusses how benchmarks are designed, or drop it from Paper 2.
5. Remove `hou_llm4se_survey_2024` and `singh_leaderboard_illusion` from "Empirical audits of SWE-bench". Hou et al. can go in a sentence on research on language models in software engineering. Singh et al. can go in a sentence on leaderboards in general.
6. Remove `whitfill_metr_merge_2026` from "Our study operationalizes those checks together inside one frozen contract". Move it to the claim that passing tests is narrower than code review, for example in the Limitations section or with "tests may accept incomplete patches" in the Introduction.
7. Section 2, "assurance contracts": cite `sljivo_assurance_contracts_2014` there in place of `lawford_safety_case_impact_2017`. Kokaly et al. can stay in the "requirements assurance perspective" group or be removed.
8. Section 2, "withhold a claim whenever supporting evidence fails defined validity conditions": remove `arief_vnvspec_2026` and move it to the "requirements assurance perspective" group, next to `gotel_traceability_1994` (requirements linked to tests).
9. Introduction, sentence 1: none of the three citations shows that requirements engineers use coding leaderboards to select assistants. Either reword the sentence to what Berry says (evaluation measures and thresholds as requirements of an AI system) and remove `lewis_quality_model_ml_2026`, or find a source for the claim as written.
10. Section 2: change "SpecOracle" to a description such as "Ding's specification-oracle audit", and "AutoBenchmarkAudit" to "Auto Benchmark Audit".
11. Introduction, "Independent audits of SWE-bench Verified": `ding_spec_oracle_gaps_2026` and `mohl_transcript_flaws_2026` did not audit SWE-bench Verified. Either widen the sentence to "coding and agent benchmarks", or move those two citations to the Section 2 group.
12. Check whether `pizarro_beyond_the_hype_2026` supports "construct validity" (Section 2). If it does not, remove it there. It may fit the Introduction's sentence on industry adoption.
13. Add `\cite{newcombe_difference_1998}` where Newcombe intervals are first reported (Section 4.2). The entry is already in the bib.
14. Optional: add pages and DOI to `yu_utboost_2025`, and pages 169 to 181 to `wang_solved_issues_2026`. Remove the uncited duplicates `coding_agent_assurance_envelopes_2025` and `ai_evidence_reuse_2026`, after you check that the MESA paper does not cite them.
