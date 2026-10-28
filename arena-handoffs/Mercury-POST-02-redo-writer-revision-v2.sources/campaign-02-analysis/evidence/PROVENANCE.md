# Evidence provenance and reconstruction rules (Mercury)

## 1. Primary archive identity

| Item | Value |
|---|---|
| Archive | `mercury-pairwise-state-38873207827.zip` |
| Git blob SHA-1 | `b96d00d3206929da5089ca63b75b667639e87ebc` (verified) |
| ZIP size | 10,580,748 bytes |
| ZIP SHA-256 | `ece98bcf1cfd53dd24625c43da5e647aa63a5fac645603976c1213bdbd9af389` |
| ZIP members | 5,129 |
| Root-level members | 29 |
| Campaign source commit | `ea827277d42a714d4cd9760f4a4930ab5237e6de` (dirty=true) |
| Model | `mercury-2.5` (reasoning_effort=high, reasoning_enabled=true) |
| Provider | mercury / https://api.inceptionlabs.ai/v1 |

The archive was read in place; no member changed. SHA-256 computed by `reconstruct_campaign.py`.

## 2. Reconstruction

Script: `campaign-02-analysis/evidence/reconstruct_campaign.py` (adapted from Atria's `campaign-01-analysis/evidence/reconstruct_campaign.py`; run_dir prefix changed to `runs/mercury_pairwise_campaign/`, unscored cases handled, Mercury fields `pair_id`, `interventions`, `generation_id` carried).

Generated tables in `evidence/generated/`: archive_inventory.csv, campaign_exclusions.csv, case_results.csv, run_attempts.csv, trace_index.csv, failure_details.csv, environment_summary.csv, track_summary.csv, analysis_family_summary.csv, axis_summary.csv, failure_taxonomy.csv, config_hash_audit.csv, audit.json.

## 3. Scope

- 416 selected case IDs; 405 scored, 11 infrastructure_unscored.
- 189 behavioral_reference (gated), 227 compile_only.
- Omissions: 10 rope cases (provider input modality unsupported), 24 known gate-blocked cases, 56 intervention-twin omissions (unverified).
- Provider outage: one recorded case `ts_parse_only__witness_status=broken_representation=flat__seed-0` (1 retry, 60s).

## 4. Limits

- Source repository dirty at run; config hashes not compared (no clean source snapshot available in this environment) — config_hash_audit.csv has 0 checked.
- Reasoning content not copied (only counts).
- No independent rerun of the campaign; all figures reproduced from archived records.
