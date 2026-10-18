# Reasoning Atria campaign — post plan (drafts not started)

Method precedent: the normal-Atria posts on strangetcy.github.io (October 2026). Used for structure only: an explicit denominator discussion, labelled sensitivity views, a clean-source boundary, plain-language readings of recorded labels, and a closing statement of what the post does not show. Their numbers, labels, and findings are about a different archive and are not carried over.

Every number in a post must trace to `evidence/generated/headline_counts.csv` or a named generated table. Limitations sit beside the claim they limit.

## R-POST-01 — A Paused Campaign Is Not a Finished Evaluation
- Question: what does the record support when the campaign stopped one case short?
- Evidence: PROVENANCE §3; `campaign_progress.json` values (415/416); `pause_reason = max_tokens_total`; non-resumable.
- Claims: 415 recorded cases; 290 PASS / 125 FAIL (69.9%); the unrecorded case is named.
- Limit: the 416th case is absent, not failed. The denominator is the recorded set.

## R-POST-02 — A Rejected Patch Is Not a Failed Repair Attempt
- Question: how much of the FAIL count stopped at patch or source validation, before judging?
- Evidence: `case_results.csv` disposition × failure_mode; stage_statuses.
- Claims: 62 `rejected` (patch_invalid 45, source_invalid 17); the archive does not define "rejected".
- Limit: stage statuses describe the recorded pipeline, not the model's reasoning.

## R-POST-03 — Two Judges, One Pass Mark
- Question: what do the two judge modes each establish?
- Evidence: judge_guarantee split; campaign-report statement that compile-only is exploratory.
- Claims: behavioral reference 131/189; compile-only 159/226 (exploratory).
- Limit: the two pools are not averaged; the 18 `unscored`-disposition rows must be stated.

## Deferred — R-POST-04 — Same Manifest, Different Model
- The reasoning archive's recorded cases share 415 of 416 case IDs with the Mercury archive. Any comparison is a separate analysis, scoped and approved separately, with no Mercury denominators imposed here.

## Required before any draft moves past Stage A
1. Resolve or disclose the 18 `unscored`-disposition rows that carry FAIL verdicts.
2. State a reason for the performance-eligibility exclusion (the provider-outage FAIL).
3. Run the config-hash audit against a clean comparator, or state that it was not run.
4. Check the campaign's source-tree status from the archived report.
