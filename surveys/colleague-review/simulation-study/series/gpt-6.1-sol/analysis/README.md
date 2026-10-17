# Analysis export refinement

After inspecting response placement, analysis now retains each complete real-case review in `instrument_reviews.csv` (`full_review_json` and `combined_all_fields`). Existing `numbered_ids` and `numbered_id_count` describe `instrument_review` only. Detailed EFPA discussion can occur in conclusion arrays; summary-field counts cannot establish review completeness.

`efpa_source_id_inventory.csv` lists hierarchical numeric identifiers found at the start of source extraction lines, with their lines for manual checking. This mechanical inventory can include numeric artifacts and omits headings without recognizable numeric labels. `efpa_id_mentions.csv` locates explicit inventory identifiers throughout every review field and expands only ascending numeric ranges with the same parent. Grouped references, parent references, paraphrases, and ambiguous ranges are not resolved. Numeric coincidences may be false matches. The unmentioned-ID list is a manual-audit aid, never a semantic completeness or quality judgment. Text and parsed JSON content are preserved; original response files retain original formatting.

`physical_attempts.csv` retains every recorded execution and its original status/errors. `runs.csv` has one row per planned job and identifies its selected attempt. A second attempt may replace only an original process failure with no completed turn or response; completed invalid responses cannot be replaced. Unsupported retry directories are reported as protocol violations.

This is a post-freeze descriptive export refinement; no prompts, raw responses, eligibility criteria, or expected answers were changed by this refinement.
