# Completed response exclusions

All 40 conversations completed, with no infrastructure failures or retries. Nine completed benchmark-review responses failed the frozen structure. They were retained without repair or replacement. All 20 test-case responses were usable. These exclusions concern format, not correctness of review content.

| Run | Format requirement not met |
| --- | --- |
| real-mesa_original-neutral-3 | documented_problems must be list of strings; missing_information must be list of strings; reinterpretations must be list of strings; supported_claims must be list of strings |
| real-mesa_revised-neutral-1 | reinterpretations must be list of strings |
| real-mesa_revised-neutral-3 | documented_problems must be list of strings; missing_information must be list of strings; reinterpretations must be list of strings; supported_claims must be list of strings |
| real-mesa_revised-neutral-4 | reinterpretations must be list of strings |
| real-efpa-neutral-1 | documented_problems must be list of strings; instrument_review must be string; missing_information must be list of strings; reinterpretations must be list of strings; supported_claims must be list of strings |
| real-efpa-neutral-2 | instrument_review must be string; reinterpretations must be list of strings |
| real-efpa-neutral-3 | instrument_review must be string |
| real-efpa-neutral-4 | instrument_review must be string; reinterpretations must be list of strings |
| real-efpa-neutral-5 | instrument_review must be string |
