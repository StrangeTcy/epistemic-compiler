# Campaign 03 — reasoning Atria pairwise campaign (analysis workstream)

**Status: pipeline prepared; campaign record is INCOMPLETE (paused at 415 of 416 episodes). No posts are drafted or approved.**

## What is here

| Path | Purpose | State |
|---|---|---|
| `evidence/PROVENANCE.md` | Archive identity, SHA-256, completion status, verification, open discrepancies | Complete for reconstruction |
| `evidence/reconstruct_campaign.py` | Stdlib ZIP reader; adapted from campaign-02 with run prefix and archive ref as arguments | Run successfully |
| `evidence/summarize.py` | Recomputes headline counts from generated tables | Run successfully |
| `evidence/generated/` | Generated evidence tables and `audit.json` | Generated from archive |
| `evidence/generated/headline_counts.csv` | Recomputed headline numbers | Generated |
| `findings/` | Reserved for claim register (not started) | Not started |
| `posts/POST_PLAN.md` | Candidate post set, inspired by the normal Atria posts | Plan only |
| `post-production/pipeline_state.json` | Stage state per planned post | All stages not started |
| `post-production/handoffs/` | Stage prompts | Stage A prompt prepared |
| `followups/` | Reserved | Empty |

## Headline (recorded cases only, recomputed)

- 415 recorded cases: 290 PASS / 125 FAIL → 69.9% of recorded cases.
- 414 performance-eligible cases (one provider-outage FAIL excluded): 290/414 = 70.0%.
- Judge split: behavioral reference 131/189 PASS; compile-only 159/226 PASS (exploratory per the campaign report).
- Failure labels (125 FAIL): underfit 38, patch_invalid 45, source_invalid 17, training_failed 11, overfit_visible_tests 7, invalid_action 6, runtime_error 1.

These figures describe the recorded record only. The 416th manifest case was never run, and the campaign is marked non-resumable.

## Open items (must be resolved or disclosed before any post)

1. Campaign is paused (`max_tokens_total`, not resumable); 1 of 416 manifest cases unrecorded.
2. 18 rows marked `unscored` disposition still carry FAIL verdicts; the report counts them as scored.
3. 62 `rejected` disposition rows: term undefined in the archive.
4. Performance-eligibility rule for the provider-outage FAIL needs a stated reason in the post.
5. Config-hash audit not run (no clean comparator supplied).
6. Source-tree cleanliness of this campaign not yet checked.
7. Case-set overlap with the Mercury campaign (415 shared IDs) is an observation only; no cross-model comparison is in scope yet.

## Boundaries (carried over from the project's standing rules)

- No campaign rerun, no provider calls, no paid API use.
- Normal-Atria blog posts are used as **method precedent only**; their numbers (194 scored, 131 PASS) are a different archive and must not be cited as evidence about this campaign.
- Mercury results are not evidence about this campaign, and Mercury denominators are not imposed here.
- Nothing is pushed or published externally. Drafts are for human review.
