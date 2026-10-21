# R-POST-03 — EVIDENCE PACKET (authoritative)

**Slot:** R-POST-03 — a zero-pass-rate environment family is not a capability verdict.
**Series:** *Reasoning-Atria* (campaign 03). Slot map: 01 environment dominates · 02 the floor (this) · 03 the difficulty dial · 04 the ceiling · 05 partial credit.
**Snapshot:** `atria-campaign-state-62.zip` → `coverage.json` (`updated_at` 2026-10-02T14:44:58Z). This is the **completed** campaign. `campaign_report.json` reports `status: completed`, `resumable: false`.
**Status:** verified against row-level `coverage.json`. Every count below is reproducible from the fields in Appendix A.
**Authority:** this file is the single source of truth. If a prompt, a draft, or an earlier packet disagrees with it, this file wins.

Writers and reviewers may not introduce any number that is not in this packet. If an argument needs a number the packet lacks, the argument is cut, not estimated.

---

## 1. Campaign identity

| Field | Value |
|---|---|
| Event | `atria_covering_campaign` |
| Provider / mode | `atria`, paid execution, `text_only` input modality |
| Case manifest sha256 | `c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d` |
| Source commit under test | `d7357092493f311f649a0742889b301d796911b5` |
| Intent recorded | 2026-09-29T13:34:39Z |
| Cases recorded / scored | 194 / 194 |
| Paused cases | 0 |
| Seeds | `0` on all 194 rows; one seed per cell, no reruns |
| `reasoning_enabled` | `false` on all 194 rows |
| Sum of per-case elapsed | ≈ 23.03 h (shortest case 27.7 s, longest 1,945.1 s ≈ 32 min) |
| Provider outage (report field) | 3,300 s waited, 8 retries, last case `ts_trajectory__witness_status=broken_representation=reflective__seed-0` |

The outage is **history, not status**: the campaign finished after it. Do not describe the campaign as paused, incomplete, or "193 scored".

---

## 2. The two judge guarantees

Guarantee is fixed per environment: **11 families are behavioral-reference, 22 are compile-only.** No family mixes the two.

| Bucket | Scored | PASS | FAIL | Pass rate | What the campaign report says |
|---|---:|---:|---:|---:|---|
| `behavioral_reference` | 72 | 56 | 16 | 0.778 | exact-instance oracle carried |
| `compile_only` | 122 | 75 | 47 | 0.615 | exploratory; excluded from any validated aggregate |
| **Total** | **194** | **131** | **63** | — | report per bucket only |

Never stitch the buckets into one rate. "131/194" may be used only as a bookkeeping total with both denominators named in the same sentence.

---

## 3. Shape of the distribution (33 families)

| Group | Families | Cases | Guarantee split |
|---|---:|---:|---|
| All-pass (14) | 14 | 84 | 5 behavioral-reference, 9 compile-only |
| Zero-pass (6) | 6 | 35 | 1 behavioral-reference (`glyph`), 5 compile-only |
| Mixed (13) | 13 | 75 | 5 behavioral-reference, 8 compile-only |

The all-pass families: `architecture_naturality`, `ci_dependency_graph`, `epistemic_games`, `equivariant_diagram`, `rd_gradient_credit`, `rd_state_carry`, `semiring_unification`, `sheaf_invariant_gluing`, `spreadsheet_dataflow`, `ssm_parallel_scan`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`, `transformer_ssm_lift`.

The all-pass guarantee split matters for R-POST-04, not for this post; it is included so no writer borrows "14 solved" without its composition.

Track totals (all 194): category-theoretic/compositional 57/85 · ML debugging 16/37 · recurrent depth 31/33 · weird machine 25/30 · trajectory 2/9.

---

## 4. The six zero-pass families — case ledger (35 cases, 0 passes)

Zero pass rate, and nothing else in common. Mean family scores: `glyph` 0.000 · `ts_trajectory` 0.000 · `batchnorm_ema` 0.086 · `sheaf_physical_constraints` 0.111 · `ts_one_step` 0.333 · `gnn_message_passing` 0.417.

| Family | Guarantee | Difficulty string | Score | `failure_mode` |
|---|---|---|---:|---|
| `batchnorm_ema` | compile-only | easy,easy,easy,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | hard,easy,easy,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | medium,easy,easy,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,hard,easy,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,medium,easy,easy,easy | 0.9500 | `overfit_visible_tests` |
| `batchnorm_ema` | compile-only | easy,easy,hard,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,easy,medium,easy,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,easy,easy,hard,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,easy,easy,medium,easy | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,easy,easy,easy,hard | 0.0000 | `patch_invalid` |
| `batchnorm_ema` | compile-only | easy,easy,easy,easy,medium | 0.0000 | `invalid_action` |
| `glyph` | behavioral-reference | easy,easy,easy,easy,easy,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | medium,easy,easy,easy,easy,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,medium,easy,easy,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,easy,hard,easy,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,easy,medium,easy,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,easy,easy,hard,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,easy,easy,medium,easy | 0.0000 | `patch_invalid` |
| `glyph` | behavioral-reference | easy,easy,easy,easy,easy,medium | 0.0000 | `patch_invalid` |
| `gnn_message_passing` | compile-only | easy,easy | 0.4167 | `underfit` |
| `gnn_message_passing` | compile-only | hard,easy | 0.4167 | `underfit` |
| `gnn_message_passing` | compile-only | medium,easy | 0.4167 | `underfit` |
| `gnn_message_passing` | compile-only | easy,hard | 0.4167 | `underfit` |
| `gnn_message_passing` | compile-only | easy,medium | 0.4167 | `underfit` |
| `sheaf_physical_constraints` | compile-only | easy,easy | 0.0000 | `invalid_action` |
| `sheaf_physical_constraints` | compile-only | hard,easy | 0.0000 | `invalid_action` |
| `sheaf_physical_constraints` | compile-only | medium,easy | 0.2778 | `underfit` |
| `sheaf_physical_constraints` | compile-only | easy,hard | 0.2778 | `underfit` |
| `sheaf_physical_constraints` | compile-only | easy,medium | 0.0000 | `patch_invalid` |
| `ts_one_step` | compile-only | broken,flat | 0.2857 | `underfit` |
| `ts_one_step` | compile-only | valid,flat | 0.7143 | `underfit` |
| `ts_one_step` | compile-only | broken,reflective | 0.0000 | `source_invalid` |
| `ts_trajectory` | compile-only | broken,flat | 0.0000 | `runtime_error` |
| `ts_trajectory` | compile-only | valid,flat | 0.0000 | `runtime_error` |
| `ts_trajectory` | compile-only | broken,reflective | 0.0000 | `invalid_action` |

The difficulty strings are the ordered dimension **values** only. The archive does not record which dimension name each position holds, so no writer may attach names to positions. `ts_one_step` and `ts_trajectory` use two-valued strings (`broken`/`valid`, `flat`/`reflective`).

---

## 5. Layer split inside the six families

| Layer | Cases | What the record shows |
|---|---:|---|
| `patch_invalid` (empty patch) | 18 | `patch_found: true`, `patch_valid: false`, `sources_valid: false`; note reads `Patch validation failed: FAIL: Patch file is empty` |
| `invalid_action` (unreadable action) | 4 | the submitted action was not parseable; all four are compile-only |
| `source_invalid` (rejected before running) | 1 | `ts_one_step` `broken,reflective` |
| `runtime_error` (failed while running) | 2 | both `ts_trajectory`; the campaign's third runtime failure is recorded as `RUNTIME_ERROR` in capitals in `rd_adaptive_halting`, a mixed family, and is not counted here |
| `underfit` (ran, scored below the bar) | 9 | `gnn_message_passing` 5 × 0.4167; `sheaf_physical_constraints` 2 × 0.2778; `ts_one_step` 0.7143 and 0.2857 |
| `overfit_visible_tests` | 1 | `batchnorm_ema` at 0.95 (see §7) |
| **Total** | **35** | |

**25 of the 35 stopped before any judge scored behaviour. 10 reached a scored judgement.** The 25 are 18 empty patches, 4 unreadable actions, 1 source rejection, 2 runtime failures.

Scores recorded inside these "zero" families: `0.0000, 0.2778, 0.2857, 0.4167, 0.7143, 0.9500`.

---

## 6. Where the zero is not uniform

- **`gnn_message_passing` — five cases, one number.** All five records carry score `0.416667`, `raw_accuracy 0.5`, `trusted_score 0.5`, and an identical check profile (`patch_valid: true`, `sources_valid: true`, `hidden_metric_passed: false`, `anti_gaming_passed: true`, `required_multifile_edit: true`, `basic_run: false`, `permutation_equivariance: true`, `training_completed: false`, `artifact_found: false`). Changing a difficulty dimension did not move the score at all. This is a ceiling, not variance.
- **`ts_one_step` — three cases spanning the widest range in the campaign's zero families:** 0.7143, 0.2857, 0.0000. A 0% family contains the campaign's highest-scoring failure by margin (0.7143); its third case never ran because source validation rejected it.
- **`glyph` — 8 of 8 at exactly 0.0000**, every one an empty patch, under the strictest guarantee in the campaign (behavioral-reference). This is the only zero-pass family whose 0% rests on the oracle guarantee, and its 0% is a statement about the submitted patch file, not about a judged behaviour.
- **`batchnorm_ema` — 11 cases: 9 empty patches, 1 unreadable action, 1 record at 0.95.**

---

## 7. Two record conflicts that a careful reader must not flatten

| Case | Verdict | Score | `trusted_score` | `missing_required_files` | Note |
|---|---|---:|---:|---|---|
| `batchnorm_ema` `easy,medium,easy,easy,easy` | FAIL | 0.95 | 1.0 | `["train.py"]` | "Patch does not touch all required cross-context files; missing: train.py"; also `hidden_metric_passed: false`, `anti_gaming_passed: false` |
| `moco` `easy,easy,easy,easy,medium,easy` (not in the six; a mixed family) | FAIL | 0.95 | 1.0 | `["moco_model.py"]` | same note shape, plus the unexplained flag `temperature_cancelled` |

The label is `overfit_visible_tests`; the fields describe a missing file and a full trusted score. The archive does not establish whether the submission, the task, or the pipeline produced that. The packet supports "the label and the record disagree"; it does not support "the model overfit" or "the model was correct".

---

## 8. Campaign context for the 63 failures

| `failure_mode` | Total | behavioral-reference / compile-only |
|---|---:|---|
| `patch_invalid` | 24 | 9 / 15 |
| `underfit` | 20 | 3 / 17 |
| `source_invalid` | 10 | 3 / 7 |
| `invalid_action` | 4 | 0 / 4 |
| `runtime_error` (+ `RUNTIME_ERROR` casing variant) | 2 + 1 | 0 / 3 |
| `overfit_visible_tests` | 2 | 1 / 1 |
| **Total** | **63** | 16 / 47 |

- The six families hold **35 of the 63 failures (55.6%)** and **35 of the 194 cases (18.0%)**.
- **18 of the campaign's 24 empty patches** are in these six families; **all 4** `invalid_action` failures are.
- Failures carrying a non-zero score across the whole campaign: 18 rows, ranging 0.2083 to 0.9500.

---

## 9. Limitations (state these, do not perform them)

- One provider, one model, text-only modality, one seed per cell (`seed 0`), no reruns: no variance, no confidence intervals, no population estimates.
- The campaign record and the per-case rows disagree on retry volume: `campaign_progress.json` reports `http_attempts: 6412`, while per-row `http_attempts` sum to 4,319. Cite neither, or cite both as a conflict.
- Snapshot sensitivity: state-56 recorded compile-only as 121 scored + 1 paused; state-62 records 122 scored. This packet uses state-62.
- The archive holds the verdict and the layer, not a cause. Nothing in it says why a patch was empty or an action unreadable.
- Family labels are labels. Nothing in the packet says the six families share a construct, a difficulty, or a mechanism.

---

## 10. What the evidence supports / does not support

**Supports (the defensible thesis):** a zero pass rate is a description of outcomes, and in this campaign it is produced by at least four different stopping layers. Within six families that passed nothing, 25 of 35 cases never reached a judge that scores behaviour; the ones that did score spread from 0.0000 to 0.7143. So "0%" cannot be read as one kind of evidence, and cannot be read as a capability verdict, until the layer is attached.

**Does not support:**
- that these six tasks are unsolvable, impossible, or broken;
- that the model cannot do the underlying work;
- that an empty patch means the model gave up, produced nothing, or refused (the record says `patch_found: true`);
- any causal claim about why a family is at zero;
- any mechanism claim about the model;
- any ranking of these families against each other;
- general evaluation prescriptions beyond "record the layer and the denominator";
- extrapolation to another provider, modality, or seed;
- any stitched aggregate pass rate across the two guarantees.

---

## 11. Corrections to earlier drafts (do not repeat these errors)

1. **"Five uniformly unsolvable families"** — there are **six**. `gnn_message_passing` (0/5) is missing from every prior list. Its absence makes the arithmetic work by accident ("remaining 14 environments").
2. **"The remaining 14 environments"** — the mixed set is **13** (33 − 14 − 6).
3. **"near-zero scores"** — the range inside the zero families is 0.0000 to 0.9500, and `ts_one_step` averages 0.333 with a 0.7143 case. "Near-zero" is false for `gnn_message_passing` (0.4167) and `ts_one_step`.
4. **"The campaign is paused at provider_error / 193 scored"** — stale state-56 language. State-62 is completed with 194 scored.
5. **The 0.726 vs 0.650 aggregate** (cases with any `hard` dimension vs none) — that is a stitched cross-bucket rate and must not appear in this post. Per bucket it is 0.808 vs 0.761 (behavioral-reference) and 0.681 vs 0.573 (compile-only); that belongs to R-POST-03, not here.
6. **`comparison_44.md`'s opening line "some model:"** — a placeholder left in a draft. No draft may contain tool labels, model names, or placeholder headers.

---

## Appendix A — field provenance

Every figure in this packet derives from `coverage.json` (194 rows) with:

- family ledger: `groupby(environment)` → `verdict`, `score`, `failure_mode`, `difficulty`, `judge_guarantee`, `track`;
- layer split: `failure_mode` on the 35 zero-pass rows, joined to the `final.checks` / `final.notes` objects embedded in `stdout_tail`;
- guarantee split: `judge_guarantee` counts, verified against `campaign_report.json` → `results_by_judge_guarantee` (72 / 122, 56/16 and 75/47);
- campaign identity: `campaign_intent.json`, `campaign_report.json`, `campaign_progress.json`;
- retry conflict: `campaign_progress.json` `http_attempts` vs `sum(coverage.http_attempts)`.

Recomputation is two `json.load` calls and a `Counter`. If a writer cannot reproduce a number this way, the number is not in the packet and does not go in the article.
