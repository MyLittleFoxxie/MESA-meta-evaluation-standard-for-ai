# Benchmark audit experiment protocol

Prepared before main sessions on 30 October 2026. The user authorized Codex execution and left Claude pending. The Codex study comprises three benchmarks, two access conditions and two repetitions: twelve main sessions. Two pilot sessions are separate. All attempts, including permitted infrastructure retries, must remain at or below sixteen. No per session token, output, tool call or time ceilings are imposed by this study.

## Instrument and scope

The instrument is the MESA benchmark audit rubric, research revision mesa-audit-10-v3, with ten criteria and criterion specific anchors. Ratings 0, 5, 10 and 15 are not an interval scale and are not averaged. Insufficient evidence and not applicable use null ratings. This revises the earlier questionnaire; its prior findings do not validate these criteria. The live survey is not an input.

## Source selection

The full paper text and top level README are supplied to every session. Repository sessions additionally receive list_files and read_file tools confined to the benchmark snapshot. The complete repository archive is retained, but only UTF-8 text files are readable through the tool; images, compressed files and other binary content cannot be inspected. This restricts the review of multimodal materials. Paper text extraction does not preserve all figures and layout.

Sources are the official HumanEval, TruthfulQA and DesignQA repositories at the commits in sources.json, and the corresponding arXiv PDFs as retrieved. PDF hashes identify the retrieved documents; source paper editions and repository revisions can differ. In particular, the current TruthfulQA README includes a later multiple choice revision. The review targets the interpretation stated in the paper, bounded by its reported tasks; reviewers must report version inconsistencies rather than assume equivalence.

The source acquisition program never executes downloaded code. The file tool supplies text, not a shell. No new benchmark scores are produced.

## Model and isolation

Requested model: gpt-6-luna; reasoning effort: medium. Codex CLI version is recorded for every attempt. Standard service tier is requested. The locally cached model catalog exposes that model and effort; this is not independent confirmation of an underlying model snapshot. If returned events do not identify the serving model, report only the requested identifier.

Each session starts in an empty temporary directory using ephemeral execution, ignored user configuration and rules, a replacement system instruction file and zero project instruction bytes. Shell, image viewing, browser, apps, plugins, multi-agent tools and memory features are disabled. Host skill discovery is disabled and known host skill paths are explicitly disabled. No secret or authentication material is included in prompts or exported records. Codex authenticates through the existing local account; no API billing switch is made.

Documents sessions receive no configured source tools. Repository sessions receive only a confined file server with read only annotations and per-tool automatic approval for listing and reading. File paths are resolved and rejected if they escape the snapshot. No source tool has network, write or execution functionality. The agent never receives analyst references, project history or other outputs. Event records are checked for tool violations; emitted events do not expose the entire initial server request, so full prompt isolation cannot be independently proven from them alone.

## Pilot and harness changes

The documents pilot and repository pilot both returned parseable ten criterion responses. The repository pilot's listing call was refused because tool approval was required. It therefore did not exercise repository reading and is retained as a condition delivery failure, not replaced or counted in the main study. Both pilots also emitted a warning that tools.view_image was unrecognized. Before main execution, that setting was corrected to features.view_image, and the file tools received read only annotations and automatic approval. Copies of the pilot runner and server are retained under analyst/. No rubric changes were made in response to pilot judgments. Direct fixture tests check traversal and symlink rejection, valid reading and response validation. There is no additional model pilot after the fix; the first main repository session will establish whether the delivery correction worked. A failed delivery is retained and excluded from the access contrast, never repaired.

## Reference preparation

Sixty assistant prepared reference records were created before main execution, with proposed judgments and alternatives. No human checker or independent reference panel exists. Every record is provisional or contested; none is a settled correctness label. Therefore the main analysis reports evidence, judgment changes and repeatability. Any matches to assistant references are labeled as agreement with assistant proposals and kept separate from accuracy. No expert accuracy claim, weighted agreement with experts or human validity result is permitted.

## Allocation and stopping

jobs.json fixes the twelve main jobs, with order randomized within repetition blocks using seeds 20261031 and 20261032. Sessions run sequentially. Each receives the same rubric and fictional teaching example. One session reviews one benchmark. The two access conditions differ only in the source tool instruction and availability of the repository server.

One manual retry may be scheduled for a failure before generation, within a total pool of two additional attempts. Completed invalid or condition delivery failure responses are not retried or replaced. The runner does not automatically retry. Stop on an account usage limit, model unavailability or unexpected runner failure. Do not poll or restart indefinitely. Preserve all attempts and resume only unstarted jobs if the limit permits and the user requests continuation.

## Reporting

Report planned, attempted, completed, structurally usable and condition delivered counts. A schema-compliant response is not necessarily supported. File existence and quotation matching are mechanical checks; whether evidence supports a rating is assistant interpretation. Record that distinction. No aggregate benchmark quality score, human survey result or model superiority claim is produced. Claude remains pending with no fabricated observations. Human evaluation is outside CHASE and deferred for a possible REFSQ extension.
