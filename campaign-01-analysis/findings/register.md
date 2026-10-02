# Harvested findings register

Structured records are in [`findings.json`](findings.json). Every entry has status, claim, quantitative result, artifact links, confidence, alternatives, limitations, falsifiers, novelty position, and follow-up requirements. The archive is the primary source for campaign facts; source-code statements remain conditional on the dirty-source provenance limitation in [`evidence/PROVENANCE.md`](../evidence/PROVENANCE.md).

| ID | Status | Short claim | Confidence | Primary evidence |
|---|---|---|---|---|
| F-01 | `OBSERVED` | Archive identity/config hashes; source marked dirty | High on archive facts | `audit.json`, `config_hash_audit.csv`, `archive_inventory.csv` |
| F-02 | `OBSERVED` | 194 scored cases plus 24 explicit omissions | High | `campaign_report.json`, `campaign_exclusions.csv`, `case_results.csv` |
| F-03 | `OBSERVED` | Two terminal provider-coded results; denominator sensitivity | High on notes, medium on exclusion rule | Both final JSONs, campaign report, `failure_details.csv` |
| F-04 | `OBSERVED` | 72 reference-labeled vs 122 compile-only; only one env-level public oracle self-test | High | `campaign_report.json`, `instance_oracles.json`, `oracle_preflight.json` |
| F-05 | `OBSERVED` | Seven epistemic cases recorded under `ml_debugging` | High on label; medium on intent | `suite_checkpoint.json`, source `core.py`, family summaries |
| F-06 | `OBSERVED` | Heterogeneous, sometimes nonmonotone axis outcomes | High on outcomes; low on causality | `axis_summary.csv`, `case_results.csv`, final JSONs |
| F-07 | `OBSERVED` | Seven exact Bayesian policy-inference cases pass; not recursive ToM | High on cases/source comparator | Epistemic final JSONs and `core.py`/`judge.py` |
| F-08 | `OBSERVED` | Category/compositional track is heterogeneous and judge-mode mixed | High on counts; medium on source attribution | Family/environment summaries, case table, instance-oracle records |
| F-09 | `OBSERVED` | Scalar labels collapse distinct patch/protocol/source/runtime events | High on terminal notes | `failure_taxonomy.csv`, `failure_details.csv`, raw patches/finals |
| F-10 | `OBSERVED` | Weird-machine tasks show local outcome patterns, not a general surface/depth law | High on outcomes; low on causality | `axis_summary.csv`, source configs/judges |
| F-11 | `OBSERVED` | Recurrent-depth family passes are mixed-mode and include syntax/runtime failures | High on outcomes; low on depth mechanism | Recurrent environment/axis summaries and final JSONs |
| F-12 | `OBSERVED` | Source-semantic ML-debug subset is 9/30, not the recorded 16/37 group | High on counts; medium on track intent | Raw track table and corrected analysis-family table |
| F-13 | `OBSERVED` | Retry counters and reasoning-mode metadata conflict | High on archived fields | `audit.json`, run manifests, API/error/usage logs |
| F-14 | `INFERRED` | Ten category-axis controls lack direct template references in the clean comparator | High on static scan; medium on executed run | `axis_placeholder_audit.csv`, scan script, dirty-source caveat |
| F-15 | `OBSERVED` | Selected category prompt/judge contracts differ in key examples | High on comparator; medium on executed run | Source paths/line references in implementation audit |
| F-16 | `INFERRED` | Publish a descriptive task/failure map, not a general scalar ability score | High as reporting recommendation | Mode/family/failure/axis summaries |
| F-17 | `OBSERVED` | Targeted prior work preempts broad novelty claims | High on cited references; not exhaustive | [`sources/references.md`](../sources/references.md) |
| F-18 | `SPECULATIVE` | Class names or hard-level hint may have mattered more than tested length in the regex pilot | Low; explicitly untested | Regex final JSONs, prompt/config comparator, `axis_summary.csv` |

## Claim ceilings

- **Safe as archive facts:** identity/hash, timestamps, recorded case counts, explicit omissions, per-case status/score/mode, final notes, run logs, response-usage counters, and exact source-template observations with their dirty-source qualifier.
- **Safe with an explicit denominator and scope:** `131/194` raw PASS, `131/193` excluding only the report-listed outage, and `131/192` excluding both provider-coded terminal notes; mode-specific counts; per-environment outcomes; seven `epistemic_games` answers.
- **Interpretation only:** local nonmonotonicity, source/judge mismatch implications, failure-layer implications, or the possibility that some axes are no-ops. Mark as `INFERRED` and keep alternatives visible.
- **Not justified by this campaign:** recursive ToM or strategic reasoning; category-theory mastery; a general weird-machine capability; a common latent difficulty scale; provider-independent model capability; a causal surface-deception law; or a validated aggregate across compile-only and behavioral-reference cases.

## Post-to-finding map

- POST-01: F-01, F-02, F-04, F-05, F-06, F-10, F-11, F-12, F-16.
- POST-02: F-04, F-05, F-07, F-17.
- POST-03: F-01, F-04, F-08, F-14, F-15, F-17.
- POST-04: F-02, F-03, F-04, F-05, F-09, F-13, F-16, F-17.
- POST-05: F-06, F-10, F-14, F-15, F-17, F-18 (`SPECULATIVE` claim).
