# Colleague survey: organizer notes

Send colleagues **survey.html**. It contains the instructions, all 50 question instances, reading passages and response controls in one file. It opens directly in a modern browser without a server or internet connection. The companion [survey.md](survey.md) is a printable/text alternative. The original MESA-25 questionnaire and completed DesignQA example remain separate.

## What participants do

Participants answer the same 25 questions for ARC-AGI-2 and original HLE. Each benchmark has an overview and a continuous reading passage before its 25 questions. Participants interpret the passage and may return to it while answering. Questions contain only a brief explanation of their meaning, five unselected choices and an optional comment field; ARC-AGI-2 and HLE facts stay in the preceding passages; DesignQA examples appear under the explanations. The packet names the benchmark version and intended use. It omits ARC-AGI-2 and HLE reviewer answers. At the user’s request, each question includes a short DesignQA worked example with its existing selected answer, a brief reason and source links.

Participants can save and load a draft in their browser. Response download and file-import controls have been removed; completed benchmarks are submitted by email. After answering all 25 items for either benchmark, participants enter their name and press Finish & email responses. FormSubmit processes the name, that benchmark’s answers/comments, completion time and submission ID for email delivery to vitorraposo2@gmail.com. This is not anonymous. The recipient must activate FormSubmit before collecting responses. Downloads remain available as backup; browser drafts are not encrypted. The completed response is saved locally after a send attempt when browser storage is available.

Unanswered is stored as null, distinct from No, Not sure and Not applicable. Drafts may contain unanswered items; submission requires all 25 selections for that benchmark. No numerical total or EFPA conversion is generated. Saved drafts must match the survey fingerprint and allowed response schema.

## Scope and source choices

The packet was prepared on 7 October 2026. Exact repository commits and source fingerprints appear in [source-manifest.json](source-manifest.json); statement-to-source references and passage coverage mappings are in [packet.json](packet.json). Factual statements come from primary papers, documentation and public code, not inherited MESA scores. Some documentary gaps remain unresolved. Source files were inspected; benchmark models were not run and gated HLE questions were not downloaded.

ARC-AGI-2 is described with its public evaluation data and the current official runner/verified-testing documentation. Historical Kaggle constraints are not mixed into current verified-testing rules. A relevant distinction is supplied neutrally: the dataset description defines full task success as solving every test input, whereas the inspected scoring implementation averages solved test inputs within a task. Existing runner test cases are acknowledged. A policy statement about published results is not represented as an independently checked complete archive.

HLE means the original 2,500-question test described in the supplied paper transcription. HLE-Rolling and HLE-Diamond are separate variants. The local paper transcription is fingerprinted rather than assigned an unverified paper revision number. Original evaluation code is described at the inspected commit. The temperature argument exists but is commented out in the actual request; the README default is not asserted to have been enforced. The scoring code's approximate confidence interval is distinguished from confidence calibration and repeated-run reliability. The paper's expert-disagreement estimate is not called a confirmed error rate. HLE's dataset page is gated; only its publicly visible metadata/access statements were inspected.

Summaries are selected information, not a claim that every possible source was exhaustively searched. “No study identified in the inspected sources” is explicitly bounded. It must not be interpreted as proof that no study exists. Respondents can select Not sure. Source notes are supplied for traceability but no external reading is necessary for the packet-based judgments requested.

## Interpretation limits

This is a **packet-based pilot** of the questionnaire. It examines judgments made from the information supplied here; it does not establish the outcome of a full independent benchmark audit. Selection and compression of information can influence answers. Question wording is retained from the existing checklist, with shorter help text; the evidence packet is new. Readers may disagree over Partly versus Not sure or over the scope of a claim. Such disagreements should be examined, not scored as respondent errors.

ARC-AGI-2 appears first and HLE second; order is not randomized or counterbalanced. No completion-time estimate or validated scale is claimed. Comparing responses can inform a later validation study, but agreement in this pilot does not by itself validate the questionnaire. Comments are optional, so information retained by a long commented review must not be assumed to survive in choices alone.

For a consistent run, give everyone the same HTML file and ask them to rely on the supplied packet. If the organizer changes facts, questions or instructions, make a new version before circulating it. Existing drafts and imports are checked against the packet fingerprint. Archive the circulated file along with returned responses.

## Maintenance

`packet.json` is the content source. `template.html` supplies the self-contained interface. Run `python3 surveys/colleague-review/build.py` after edits and update the manifest fingerprint. `verify.py` checks structure, source references, question consistency and the embedded packet; it cannot establish factual completeness or scientific validity. The original sources, full MESA reviews and existing blank checklist are unchanged.

Packet 1.1 moves the facts into preceding reading passages. The original statement records remain in `packet.json` for provenance; `reading` defines the prose shown to participants. Every original fact ID is mapped to one passage paragraph. The packet ID and fingerprint distinguish these responses from the earlier per-question layout.

Packet 1.2 rewrites passages in plain language, highlights selected facts and limits, and adds four explanatory diagrams. Diagrams explain processes and calculations; they are not official test items or observed model results. Paragraph and diagram citations lead to a visible reference list at the end. The HLE article link accompanies the retained local source snapshot; it does not imply that all later article revisions are identical. The exact mathematics percentage was omitted because the supplied transcription does not preserve a readable percentage in its chart; its explicit emphasis on mathematics is retained. Question wording and blank response choices are unchanged. Emphasis and diagrams are additional presentation choices that could affect responses in a pilot.

Packet 1.3 labels all question help as “Meaning” and uses explanatory statements instead of additional questions. A shared glossary defines benchmark version and ability in plain terms. The 25 DesignQA examples retain the selections in `proposals/mesa-25/designqa-example.json`; reasons are shortened and primary-source links retained. These examples are visible teaching aids, so participant judgments are no longer made without exposure to a completed example of a different benchmark. The existing review is not an answer key or independent validation, and the participant responses remain unfilled.

Both reading passages were also edited into connected prose, with transitions explaining how the facts relate. The source mappings, factual limits, diagrams and question wording remain in place.

Packet 1.4 introduces the developers and the human puzzle-solving study before discussing its findings. It also includes the unchanged official Figure 1 (problem e3721c99) from the ARC-AGI-2 v2 technical report, with attribution and a descriptive caption. The image is embedded in the HTML for offline use and stored separately for the Markdown companion; it is not a generated or reconstructed puzzle.

Packet 1.5 removes the respondent-code field from the interface, saved drafts and response exports. Reader-facing descriptions omit commit identifiers, while source links and the organizer’s manifest retain exact source traceability. A separate DesignQA example tab presents all 25 existing answers and short reasons as read-only reference material. These entries do not contribute to progress or exports.

Packet 1.6 removes the redundant ARC process diagram, adds the official HLE classics-question image and official project logos, and restyles both figures with separate explanations, credits and enlarge/download controls. ARC uses the ARC Prize organization logo, labelled accordingly. All image files are unchanged and embedded for offline use.

## Email delivery setup

The submission endpoint is configured in `packet.json`. FormSubmit requires the recipient to confirm an activation email. Before inviting colleagues, activate the endpoint and verify a complete test message in the recipient inbox. Service acceptance is not proof of inbox delivery. The page preserves answers and saves a browser draft on errors when storage is available; a retry retains its submission ID for manual deduplication, but the provider does not guarantee idempotency. Completion times come from the participant’s device, with UTC and local time zone in the email; they are not independently verified server timestamps. Offline copies support reading and browser drafts; sending requires the hosted HTTP(S) page and internet access.

Packet 1.7 aligns the overview and reading panels, places each logo beside its title, and adds a desktop contents sidebar. The name field replaces no respondent code: it is collected specifically for the newly requested email delivery. Automated submission tests mock the provider and cannot prove real email delivery.

The current interface uses the full paper title and introduces MESA in the opening instructions. It provides a saved light/dark preference, places the DesignQA example before ARC-AGI-2 and HLE, and groups completion controls in a distinct green card. Sources are collapsed until opened or followed from a citation. The removal of response downloads and imports supersedes the earlier version notes describing those controls.

The DesignQA tab now includes a source-linked reading passage before its existing 25 reviewer answers. The passage summarizes the existing review’s facts and limitations, including explicit attribution of the scale-bar shortcut as a reviewer inference, not observed model behaviour. The introductory “How the examples work” block has been removed. No separate DesignQA logo was found on its official project site; institutional logos were not substituted for a benchmark logo.
