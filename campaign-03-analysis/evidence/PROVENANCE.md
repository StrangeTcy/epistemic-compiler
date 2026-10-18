# Evidence provenance — reasoning Atria pairwise campaign

## 1. Archive identity (verified locally; no campaign rerun)

| Item | Value |
|---|---|
| Archive | `reasoning-atria-pairwise-state-39028365163.zip` (repository root) |
| Committed blob | `cb682350a0f8c8f0ce44910b4bb8a9b734126005` (matches `git ls-tree HEAD`) |
| ZIP size | 12,710,048 bytes |
| ZIP SHA-256 | `2daf0e24cf2a38702f3e1182153627aa28b51b71f67744c50febd3741cea231f` |
| ZIP members | 5,129 (28 root-level) |
| Integrity | `zipfile.testzip()` returns None |
| Campaign ref member | `9ec2d919726ba39aded2e1d011a8274f938fb7ba` (campaign repository commit) |

The archive was read in place; no member was extracted into the repository.

## 2. Campaign identity (from archived metadata)

- Campaign name: `reasoning_atria_pairwise_campaign`
- Provider: Atria; model `Atria-Dawn-Preview`; wire API `responses`
- Reasoning: `reasoning_effort = high` (controlled responses reasoning mode)
- Execution mode recorded: `paid`
- Model API base is recorded in the archive; it is not reproduced here.

## 3. Completion status — NOT COMPLETE

- `campaign_report.json`: `status = paused`, `pause_reason = max_tokens_total`, `resumable = false`.
- `campaign_progress.json`: `episodes_completed = 415`, `episodes_total = 416`.
- The one manifest case with no recorded result is `ts_trajectory__witness_status=valid_representation=reflective__seed-0`.
- Remaining job seconds recorded at pause: 3384.5.

All analysis in this workstream describes the 415 recorded cases only. The campaign is treated as an incomplete record. It must not be described as a finished 416-case evaluation.

## 4. Reconstruction

- Script: `evidence/reconstruct_campaign.py`. Adapted from the campaign-02 (Mercury) script with the run-directory prefix and archive ref made into arguments. Logic otherwise unchanged. Invocation:

  ```
  python3 campaign-03-analysis/evidence/reconstruct_campaign.py \
    --archive reasoning-atria-pairwise-state-39028365163.zip \
    --out campaign-03-analysis/evidence/generated \
    --git-blob cb682350a0f8c8f0ce44910b4bb8a9b734126005 \
    --archive-ref "HEAD:reasoning-atria-pairwise-state-39028365163.zip" \
    --run-prefix "runs/reasoning_atria_pairwise_campaign/"
  ```

- Summary: `evidence/summarize.py` recomputes headline counts from the generated tables into `evidence/generated/headline_counts.csv`.
- Generated tables: `evidence/generated/` (archive_inventory, case_results, campaign_exclusions, run_attempts, trace_index, failure_details, environment_summary, track_summary, analysis_family_summary, axis_summary, failure_taxonomy, config_hash_audit, audit.json).

## 5. Verification checks performed

| Check | Result |
|---|---|
| Recorded cases = report `recorded_cases` | 415 = 415 |
| PASS/FAIL totals = report per-judge totals | 290 PASS / 125 FAIL = (131+159) / (58+67) ✓ |
| Judge split = report | behavioral_reference 189 (131/58) ✓; compile_only 226 (159/67) ✓ |
| Manifest cases (416) minus recorded (415) | exactly one case: `ts_trajectory…valid_representation=reflective…seed-0` ✓ |
| Omissions | 80 outside manifest: 56 intervention-twin, 14 known-gate, 10 unsupported modality (rope) ✓ |
| Case-ID overlap with campaign-02 (Mercury) | 415 of 415 recorded IDs are in the Mercury 416-case set; the one Mercury-only ID is the same unrecorded case above |
| Config hashes vs clean comparator | 38 unique config paths selected; 38 checked against a clean checkout of `StrangeTcy/rl_eval_generator` at `9ec2d919726ba39aded2e1d011a8274f938fb7ba`; 38 match. This shows the config files match the clean commit. It does not show the executed code matches, because the run tree was dirty (see §6.6). |

## 6. Open discrepancies (do not resolve silently)

1. **`case_disposition` vs verdict.** 18 rows carry `case_disposition = unscored` but have FAIL verdicts (failure modes `training_failed` 11, `invalid_action` 6, `runtime_error` 1). The campaign report counts all 415 rows as scored. Which reading is correct is unresolved.
2. **`rejected` disposition.** 62 FAIL rows (`patch_invalid` 45, `source_invalid` 17) carry `case_disposition = rejected`. The archive does not define the term. The stage statuses show these stopped at patch or source validation, before behavioral evaluation.
3. **Performance-ineligible case.** One FAIL (`sheaf_schema_sync__naming=hard_symptom_mask=medium__seed-0`, `patch_invalid`) is marked `performance_eligible = False`; its final note attributes the failure to a provider transient after bounded retries. The report's provider-outage counter names the same case.
4. **Environment count.** The pilot manifest lists 39 environments; 38 have recorded cases. The 39th is `rope`, fully omitted before scoring (10 manifest-listed omissions).
5. **Config-hash audit (run).** Selected config paths: 38; checked against the clean checkout: 38; matches: 38; mismatches: none. Outputs: `evidence/generated/config_hash_audit.csv` and `audit.json`. Limit: this checks configuration files only, not the code that executed.
6. **Source-tree cleanliness (open).** `pilot_manifest.json` records the generator repository at commit `9ec2d91` with `dirty: true`, and `audit.json` records `repository_dirty_at_run: true`. The archive does not list which files were dirty, so the executed source cannot be verified against the clean commit. Any source-level claim must carry this caveat. (Separately, Campaign-02 Mercury provenance also recorded `dirty=true`.)

## 7. What this provenance does not establish

- It does not establish that the executed task, judge, or helper code matched any clean snapshot.
- It does not establish why any repair failed; labels are the archive's recorded labels.
- It does not license cross-model or cross-campaign comparison; any such comparison is a separate, explicitly scoped analysis.
