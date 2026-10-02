# Evidence provenance and reconstruction rules

## 1. Primary archive identity

| Item | Value | Evidence |
|---|---|---|
| Repository reference | `origin/main:atria-campaign-state-62.zip` | User-designated archive reference |
| ZIP SHA-256 | `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd` | Computed from the archived ZIP bytes |
| Git blob SHA-1 | `c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3` | `campaign-01-analysis/evidence/generated/audit.json` and archive reference |
| ZIP size | 6,698,206 bytes | Computed from the ZIP |
| ZIP members | 2,968, including archived directory/member entries | `archive_inventory.csv` |
| Root-level members | 20 | `audit.json` |
| Campaign source commit | `d7357092493f311f649a0742889b301d796911b5` | `campaign_ref.txt`, pilot/run manifests |
| Source dirty flag | `true` | Archived repository metadata; exact executed task/judge source is therefore not fully established by the clean commit alone |

The archive was read as a ZIP in place. No source member was changed, re-packed, or copied into this workstream. The archive SHA-256 is calculated by `reconstruct_campaign.py`; every member receives its own SHA-256 in `archive_inventory.csv`. The case and run tables point back to member paths in that archive.

## 2. Evidence sources and linkage

The reconstruction script reads these root members directly:

- `campaign_report.json`: completion status, judge-guarantee totals, explicit omissions, and the report's provider-outage counter.
- `suite_checkpoint.json`: selected result rows, scoring modes, execution settings, timestamps, and per-result attempt/runtime fields.
- `pilot_manifest.json`: selected case manifest, repository commit/dirty flag, environment count, and configuration hashes.
- `instance_oracles.json`: per-instance calibration records and the compile-only list.
- `oracle_preflight.json`: environment-level preflight and behavioral self-test status.
- `campaign_progress.json`, `campaign_intent.json`, `campaign_telemetry.json`, `coverage.json`, and related root records: execution state, provider authorization metadata, progress counters, and complementary run metadata.
- `episodes/<case_id>/<run_id>/...`: `manifest.json`, `final.json`, `model_responses.jsonl`, `trace.jsonl`, `api_errors.jsonl`, `environment-events.jsonl`, `submission.patch`, `workspace.diff`, and judge stdout/stderr where present.

`case_results.csv` contains the selected case ID, task/environment, recorded track, analysis-family label (when corrected), config hash, scoring guarantee, status, verdict, score, failure label, and raw member paths for its checkpoint row, final result, run manifest, model responses, and final run directory. `trace_index.csv` joins each selected case to the final-run trace, response log, API-error log, patch, workspace diff, judge output, result JSON, and instance-oracle record where present; it records checksums, byte sizes, and record counts, not response/reasoning text. Earlier/superseded runs are inventoried in `run_attempts.csv` and the full archive index.

`failure_details.csv` contains only final judge notes/metrics for failed rows. It does not copy the model's reasoning content. No `reasoning_content` text is emitted by the reconstruction script or included in generated evidence tables.

## 3. Case coverage and exclusions

- The result manifest and checkpoint agree on the same 194 selected case IDs. All 194 checkpoint statuses are `scored`; all selected rows have a final archived JSON result.
- These results cover 33 of the 34 environments in the recorded registry. The 194 cases comprise 72 rows labeled `behavioral_reference` and 122 `compile_only` rows before provider-terminal exclusions.
- `campaign_report.json#/campaign_omissions` lists 17 `rope` case IDs omitted because provider input modality was unsupported (`provider_input_modality_unsupported`, text-only provider). The full IDs and reason are in `campaign_exclusions.csv`.
- `campaign_report.json#/known_gate_blocked_omissions` lists 7 case IDs omitted before provider access, with `provider_calls_before_omission=0`. The report gives case-specific calibration classes, including reference-vector coverage failures, a MoCo oracle assumption, a negative-control issue, and a reference that does not solve its own instance. The full IDs/classes are in `campaign_exclusions.csv`.
- Thus the ZIP explicitly names 218 case IDs as either scored or omitted (194 + 17 + 7). The 24 omissions are not failures and are not included in result denominators.
- `campaign_report.json` explicitly says compile-only verdicts are exploratory and excluded from a validated aggregate. A combined pass fraction is therefore shown only as a descriptive mixed-mode count, never as a single uniform benchmark score.

### Provider-terminal exclusion rule

The official report's provider-outage counter names only `ts_trajectory__witness_status=broken_representation=reflective__seed-0`, with 8 retries, 3,300 seconds waited, and a 600-second last backoff. Independently reading every selected `final.json` reveals a second terminal note with the exact text `provider transient failure after bounded retries` for `sheaf_physical_constraints__naming=easy_symptom_mask=easy__seed-0`. Both selected final-run API logs contain retryable timeout/provider-transient events. The report does not list the second case in its outage counter.

The reconstruction therefore preserves the raw 194 result rows and labels both provider-attributed terminal failures as ineligible for model-performance summaries. This is an explicit analysis exclusion based on the archived terminal judge note, not an assertion that `campaign_report.json` recognized two campaign-level outage episodes. Results are shown under both scopes:

| Scope | Cases | PASS | FAIL | Use |
|---|---:|---:|---:|---|
| Raw checkpoint | 194 | 131 | 63 | Exact archive result count; includes both provider-coded terminal failures |
| Exclude only report-listed `ts_trajectory` outage | 193 | 131 | 62 | Sensitivity matching the report's single listed case |
| Exclude both final rows explicitly attributed to provider transient | 192 | 131 | 61 | Primary analysis performance set; excludes all terminal provider-coded cases |

## 4. Scoring guarantees and oracle records

| Recorded mode | Raw rows | Raw PASS/FAIL | After provider exclusions | Meaning |
|---|---:|---:|---:|---|
| `behavioral_reference` | 72 | 56 / 16 | 72; 56 / 16 | Case-level campaign label backed by `instance_oracles.json`; not a blanket claim of independent oracle validation |
| `compile_only` | 122 | 75 / 47 | 120; 75 / 45 | Judge has no behavioral reference on that exact selected instance; explicitly designated exploratory in the campaign report |

`instance_oracles.json` contains 72 per-instance records; each calibrated instance contains no-op, plausible-wrong, and reference variants. This does not turn the judge into an independent evaluator. Separately, `oracle_preflight.json` reports an environment-level public Bayesian oracle self-test only for `epistemic_games` (`public_bayes_oracle`, passed, no provider calls). Other environment entries report `judge_reference_compile` with `reference_self_test=not_configured`. Keep those preflight facts distinct from the campaign's case-level `judge_guarantee` labels.

## 5. Track-label correction for analysis

The campaign checkpoint assigns all seven `epistemic_games` cases to recorded track `ml_debugging`. The task configuration, renderer, `core.py`, and judge implement symbolic Bayesian inference, not an ML debugging task. `case_results.csv` preserves the recorded `track` and adds `analysis_family=epistemic_games`; `track_summary.csv` reproduces the recorded grouping, while `analysis_family_summary.csv` uses the source-semantic grouping. The correction does not alter any result row or raw campaign label.

## 6. Run, token, time, and retry reconstruction

### Successful-response usage and runtime

- All 268 archived run directories: 4,061 successful response rows, 4,023 unique turn IDs summed within runs, 8,877,965 prompt tokens, 569,277 completion tokens, 9,447,242 total tokens.
- The 194 selected final runs: 3,538 successful response rows, 3,500 unique turn IDs summed by case, 8,159,188 prompt tokens, 514,333 completion tokens, 8,673,521 total tokens.
- Campaign wall elapsed from checkpoint timestamps: 261,135.03 seconds (~72 h 32 min). Selected result `elapsed_seconds` sum: 82,907.013; median 334.079; mean 427.356; nearest-rank p95 1,029.117; max 1,945.064. Selected final-run manifest elapsed sum and all-run manifest elapsed sum are separate counters in `audit.json`.
- The campaign run settings record Atria / `Atria-Dawn-Preview`, paid mode, maximum 20 steps, 8,192 tokens per call, temperature 1.0, top-p 0.95, and `reasoning_enabled=false`.
- `api_cost_or_spend` is not present in the exported archive; no spend estimate is inferred.

### Retry/HTTP attempt counters (do not collapse)

| Archived source/scope | Count |
|---|---:|
| `api_errors.jsonl` event rows across all run directories | 4,883: 4,061 `success`, 576 `timeout`, 171 `http_error`, 57 `provider_transient`, 18 `provider_error` |
| Embedded attempt-log rows in successful response records | 4,443 |
| Sum of all run-manifest `http_attempts_used` | 4,778 |
| Selected final-run manifests | 3,869 |
| Selected suite result rows | 4,319 |
| Suite checkpoint | 6,172 observed + 240 unknown upper bound = 6,412 |
| Campaign progress | 6,412 |

The counts have different scopes and do not reconcile from the ZIP. Report each source and scope; do not present one as the reconciled number of provider attempts.

### Reasoning metadata discrepancy

Across all run directories, archived successful-response usage reports 325,785 reasoning tokens and 2,710 rows with a nonempty `reasoning_content` field, despite the recorded run setting `reasoning_enabled=false`. Only presence/count metadata are reported here; reasoning content is neither copied nor reproduced.

## 7. Failure taxonomy

For the 192-case primary performance set, the recorded final-failure labels sum to 61:

| Recorded label | Count | Cross-check from final result artifacts |
|---|---:|---|
| `patch_invalid` | 24 | Every one has a final note that the patch file is empty |
| `underfit` | 20 | Partial/failed task checks or judge-trusted score; inspect `failure_details.csv` per case |
| `source_invalid` | 10 | Syntax errors or disallowed imports caught by source validation |
| `runtime_error` | 3 | Target/judge execution error notes |
| `invalid_action` | 2 | One malformed patch/action JSON and one invalid JSON action; provider-coded cases are separately excluded |
| `overfit_visible_tests` | 2 | Both final notes instead identify missing required cross-context files; the label is not direct evidence of visible-test overfitting |

The two provider-terminal rows are `invalid_action` in the raw 194 results and are kept in `failure_details.csv`, but excluded from the performance-set taxonomy above. Thus all raw failures still sum to 63: the 61 eligible failures plus those 2 provider-attributed rows.

## 8. Configuration-hash and source-snapshot boundary

`config_hash_audit.csv` compares all 33 selected config hashes in the case manifest with the optional clean source snapshot passed to the script; this reconstruction found 33/33 matches. The source snapshot path used for this comparison was `/tmp/rl_eval_generator_base`, identified as the clean source snapshot at commit `d7357092493f311f649a0742889b301d796911b5`. The snapshot itself is outside this workstream and the campaign recorded `repository.dirty=true`; consequently, the check supports configuration identity, not byte-for-byte provenance of every rendered task, visible test, judge, or runtime helper used in every paid episode.

The human-readable task/judge audit names each inspected file and specific code behavior. `audit_config_axes.py` can regenerate `generated/axis_placeholder_audit.csv` from the same source snapshot and selected-config list; this is a static reference scan, not execution or a complete proof of generated workspace identity. For example, write the `config_path` column of `generated/config_hash_audit.csv` (excluding its header) to a newline-separated temporary file, then run:

```bash
python campaign-01-analysis/evidence/audit_config_axes.py \
  --source /path/to/clean/rl_eval_generator-at-d735709 \
  --config-list /path/to/selected-configs.txt \
  --out campaign-01-analysis/evidence/generated/axis_placeholder_audit.csv \
  --source-revision d7357092493f311f649a0742889b301d796911b5
```

Treat source findings as comparator observations and do not elevate them to proven executed-source identity absent the campaign's dirty diff/source snapshot.

## 9. Regeneration

The script is `campaign-01-analysis/evidence/reconstruct_campaign.py` and uses only the Python standard library. It reads the archive, hashes the ZIP and members, links checkpoint cases to selected run directories, retains superseded run attempts, parses response usage without emitting message content, and writes CSV/JSON summaries. It makes no network calls, provider requests, or edits to campaign evidence.

```bash
python campaign-01-analysis/evidence/reconstruct_campaign.py \
  --archive /tmp/atria-campaign-state-62.zip \
  --out campaign-01-analysis/evidence/generated \
  --archive-ref origin/main:atria-campaign-state-62.zip \
  --git-blob c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3 \
  --generator-source /path/to/rl_eval_generator-at-d735709
```

The `--generator-source` argument is optional; without it, the campaign config hashes remain recorded but no clean-snapshot comparison is performed.
