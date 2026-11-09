# CHASE v2 implementation record

> Historical record. Manuscript targets and commands below describe earlier work. See the [3 November 2026 consolidation record](../../provenance/manuscript-consolidation-2026-11-03.md) for Git retrieval and the current entry point.

29 October 2026. The first manuscript draft is implemented in [paper_chase_v2.tex](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase_v2.tex). Its document class, packages, author block, title and bibliography style match the original CHASE manuscript. The initial draft was checked without compilation. On 29 October 2026, the user requested a compiler check for the open document; the desktop compiler succeeded after the terminology revision. Page length and visual layout remain unchecked.

## Content

The draft centres approachability as the purpose, retains EFPA as the adaptation basis, explains OECD correspondences and omissions, and distinguishes the proposed studies from completed research. It contains the three research questions, the two model comparisons, reference-answer rules, tables illustrating the method, study limitations, assistant disclosure and the existing human survey as future Study 3. New empirical results are marked pending in the abstract and each study.

Only two bibliography entries were added: OECD Chapter 6 and ECBD. Existing entries were preserved. Bibliographic details were checked against the OECD chapter and original PDF, and the ACL Anthology record and source paper, on 29 October 2026. Sources:

- [OECD chapter](https://www.oecd.org/en/publications/ai-and-the-future-of-skills-volume-2_a9fe53cb-en/full-report/component-9.html), Cohn and Hernández-Orallo, 2023, pp. 99–118; chapter DOI 10.1787/f585066f-en.
- [ECBD](https://aclanthology.org/2024.acl-long.861/), ACL 2024, pp. 16349–16365, DOI 10.18653/v1/2024.acl-long.861. The bibliography uses the fuller author name printed in the paper for Jackie Chi Kit Cheung.

## Study preparation

The [new preparation folder](../../surveys/colleague-review/mesa-study/chase-v2/README.md) contains a snapshot of packet 2.9, 24 draft fictional cases with separate proposed labels, 50 real-reference records awaiting source checking, a paragraph audit register, condition definitions, a response schema and a protocol draft. None is presented as a frozen or validated experiment.

The live packet is now version 2.9. Older prose in README and human planning documents describes earlier versions. This draft cites its own snapshot and does not rewrite those records or infer participant collection status. The human extension must report the packet version actually used by participants.

The original source-passage packet, real reference answers, source audit and author review remain to be completed. Isolated reviewer execution has not been established. No reviewers were launched, no human responses were retrieved and no submissions were sent. Source summaries, gap claims and conceptual correspondences still require the author review specified in the literature record.

## Preservation and verification

Protected-file hashes are recorded in [source-snapshot.json](../../surveys/colleague-review/mesa-study/chase-v2/preparation/source-snapshot.json). The original manuscripts, live packet, survey and existing study guide were not changed. The bibliography addition is append-only.

Historical invocation (checker retired): `python3 tools/check-chase-v2.py` for source checks without LaTeX compilation. The check covers bibliography keys, references, braces/environments, formatting preservation, packet counts, preparation records and protected-file hashes. It does not validate source interpretations, reference labels, experimental isolation or page layout.

The [recorded check](CHASE-v2-verification.json) passed with no errors: 12 citation keys, 25 questions, 24 fictional cases and 50 pending real reference records. Thirty model sessions are planned; none has been executed. The [preparation manifest](../../surveys/colleague-review/mesa-study/chase-v2/preparation/preparation-manifest.json) identifies the current draft files and explicitly does not claim a protocol freeze.

## Amendment: ten fictional cases

On 29 October 2026, the user requested ten rather than 24 fictional cases. The manuscript, plan, protocol, active case files and checker now use ten. The 24-case draft is preserved in the preparation archive. All six distinctions remain; two have only one example. No results informed the selection and no experiment was run.

## Amendment: restore 24 cases

Later on 29 October 2026, the user reverted the reduction. The active paper, plan, materials and checker again specify 24 cases. The ten-case draft remains archived, and no responses informed the reversal.

## Continued preparation and terminology

At the user's request, the new manuscript, plan and protocol use “approachability” for MESA's purpose. This names support for understanding questions, finding relevant information, explaining answers and recognising uncertainty. It is an operational definition for this paper, not a claim that approachability is already measured or that accessibility has only one meaning. Earlier research and archived records retain their terminology.

The 50 summary reference proposals now have reasons; 30 are flagged as contested. None has author approval. Original-passage choices remain unset. The source audit records DesignQA table discrepancies and ARC source qualifications. These findings concern supplied materials, not reviewer performance. The existing packet remains preserved.

A draft schedule records all 30 sessions. The analysis plan specifies denominators, missing answers, disputed references, source checks and separate model reporting. There are 1,188 planned answer opportunities, not independent observations. The original passage packet, input assembly, author checking, packet version decision and isolation checks remain outstanding. No experiments were launched.

## Heading revision

At the user’s request, the manuscript title is now “Making Artificial Intelligence Benchmark Review More Approachable”. Section headings use words rather than acronyms. The original title is no longer a preservation requirement for this revision; the document format and author block remain unchanged. The source checker now checks for acronyms in headings.
