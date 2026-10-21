# R-POST-02 — EVIDENCE PACKET (authoritative)

**Slot:** R-POST-02 — "Hard" does not reliably make tasks harder.
**Series:** *Reasoning-Atria* (campaign 03). Slot map: 01 environment dominates · **02 the difficulty dial (this)** · 03 the floor · 04 the ceiling · 05 partial credit.
**Snapshot:** `atria-campaign-state-62.zip` → `coverage.json` (`updated_at` 2026-10-02T14:44:58Z). Completed campaign: `campaign_report.json` reports `status: completed`, `resumable: false`.
**Status:** verified row-by-row against `coverage.json`. Every count below is reproducible from Appendix A.
**Authority:** this file is the single source of truth. If a prompt, a draft, or the earlier `comparison_41.md` disagrees with it, this file wins.

Writers and reviewers may not introduce a number that is not here. If an argument needs one, the argument is cut.

---

## 1. Campaign identity

| Field | Value |
|---|---|
| Event | `atria_covering_campaign` |
| Provider / mode | `atria`, paid, `text_only` |
| Case manifest sha256 | `c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d` |
| Source commit under test | `d7357092493f311f649a0742889b301d796911b5` |
| Cases recorded / scored | 194 / 194 |
| Paused cases | 0 |
| Seeds | `0` everywhere; one seed per cell, no reruns |
| `reasoning_enabled` | `false` on all 194 rows |

The provider outage in the report (3,300 s, 8 retries) is history, not status. The campaign completed. Do not describe it as paused or "193 scored".

---

## 2. The two judge guarantees

Guarantee is fixed per family: **11 behavioral-reference, 22 compile-only.** No family mixes them.

| Bucket | Scored | PASS | FAIL | Pass rate |
|---|---:|---:|---:|---:|
| `behavioral_reference` | 72 | 56 | 16 | 0.778 |
| `compile_only` | 122 | 75 | 47 | 0.615 |
| Total | 194 | 131 | 63 | — |

Never pool the buckets. The campaign report's own aggregate note forbids it. Any rate in the article is a per-bucket rate, or it is labelled a bookkeeping total with both denominators in the same sentence.

---

## 3. The headline aggregate — and why it is not the article

| Set | Cases | PASS | Pass rate |
|---|---:|---:|---:|
| Cases with ≥1 `hard` dimension | 73 | 53 | 0.726 |
| Cases with no `hard` dimension | 121 | 78 | 0.645 |

Split by guarantee:

| Bucket | hard: cases / pass / rate | no hard: cases / pass / rate |
|---|---|---|
| `behavioral_reference` | 26 / 21 / **0.808** | 46 / 35 / **0.761** |
| `compile_only` | 47 / 32 / **0.681** | 75 / 43 / **0.573** |

Read this before you write: the pooled comparison (0.726 vs 0.645) is **exactly the cross-bucket stitched rate the campaign report forbids**, and the same direction appears inside both buckets only because compile-only cases are both more likely to contain a `hard` cell and more likely to fail. The per-bucket gaps (0.047 and 0.108) are small, from one seed, with no interval. **The article's argument must not rest on this table.** It is context, not evidence, and if a draft leads with it the reviewer will strike it.

A fourth of the archive has no `easy/medium/hard` cells at all — see §6.

---

## 4. The pair design (the article's real evidence)

Within a family, two cells whose difficulty strings differ in exactly one position, with values `easy` and `hard`. All other positions identical. **73 such pairs across 20 families.**

| Outcome of the flip | Pairs |
|---|---:|
| both PASS | **42** |
| both FAIL | **13** |
| easy passes → hard fails (**expected direction**) | **7** |
| easy fails → hard passes (**counterintuitive direction**) | **11** |
| **Total** | **73** |

Two facts sit above every interpretation:

1. **55 of 73 pairs (75%) cannot speak to direction at all.** In 42 the family was already saturated at pass; in 13 it was already floored at fail. Only the 18 discordant pairs carry directional information.
2. **Among those 18, the split is 11 counterintuitive vs 7 expected.** An exact two-sided sign test on 11/18 gives **p ≈ 0.48**. The counterintuitive majority is not distinguishable from a coin flip at this n. Do not describe it as a trend, a pattern, or "hard helps".

### 4.1 The 11 counterintuitive pairs

| Family | Position flipped | easy cell | hard cell | Guarantee |
|---|---|---:|---:|---|
| `css_state_machine` | 1 | FAIL 0.417 | PASS 1.000 | behavioral-reference |
| `css_state_machine` | 2 | FAIL 0.417 | PASS 1.000 | behavioral-reference |
| `compositional_optimizer` | 1 | FAIL 0.000 | PASS 1.000 | compile-only |
| `compositional_optimizer` | 2 | FAIL 0.000 | PASS 1.000 | compile-only |
| `functorial_augmentation` | 2 | FAIL 0.417 | PASS 1.000 | compile-only |
| `sheaf_schema_sync` | 2 | FAIL 0.000 | PASS 1.000 | compile-only |
| `rd_adaptive_halting` | 1 | FAIL 0.000 | PASS 1.000 | compile-only |
| `rd_adaptive_halting` | 2 | FAIL 0.000 | PASS 1.000 | compile-only |
| `rd_adaptive_halting` | 3 | FAIL 0.000 | PASS 1.000 | compile-only |
| `rd_adaptive_halting` | 4 | FAIL 0.000 | PASS 1.000 | compile-only |
| `rd_adaptive_halting` | 5 | FAIL 0.000 | PASS 1.000 | compile-only |

**9 of the 11 are compile-only** — the bucket the campaign report calls exploratory. Only `css_state_machine`'s two pairs carry the oracle guarantee.

`rd_adaptive_halting` contributes 5 of the 11 on its own: its all-easy cell fails at 0.000 and every single-`hard` variant passes at 1.000. That is one family's base cell behaving differently from its five neighbours, repeated five times, not five independent observations. A writer may say this; a writer may not count it as five findings.

### 4.2 The 7 expected-direction pairs

| Family | Position flipped | easy cell | hard cell | Guarantee |
|---|---|---:|---:|---|
| `categorical_lenses` | 2 | PASS 1.000 | FAIL 0.000 | behavioral-reference |
| `moco` | 6 | PASS 1.000 | FAIL 0.000 | behavioral-reference |
| `regex_state_machine` | 1 | PASS 1.000 | FAIL 0.208 | behavioral-reference |
| `monadic_reward` | 1 | PASS 1.000 | FAIL 0.000 | compile-only |
| `monadic_reward` | 2 | PASS 1.000 | FAIL 0.000 | compile-only |
| `neuro_symbolic_parser` | 1 | PASS 1.000 | FAIL 0.000 | compile-only |
| `tensor_functor` | 2 | PASS 1.000 | FAIL 0.000 | compile-only |

**3 behavioral-reference, 4 compile-only.** `regex_state_machine` is the only expected-direction pair whose failing score is neither 0.000 nor 1.000; it is 0.208.

Family counts: **5 families** contain at least one counterintuitive pair (`css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, `rd_adaptive_halting`); **6 families** contain at least one expected pair (`categorical_lenses`, `moco`, `regex_state_machine`, `monadic_reward`, `neuro_symbolic_parser`, `tensor_functor`).

### 4.3 Pairs that differ in score but not verdict

Exactly **one** of the 55 same-verdict pairs moves at all: `sheaf_physical_constraints` position 2, FAIL 0.000 → FAIL 0.278. Every one of the 42 both-pass pairs is identical at 1.000/1.000. The flips do not nudge performance; they either cross the verdict line or do nothing.

---

## 5. What the pairs mean — and the three things they do not

The defensible thesis:

> **Flipping one difficulty dimension from `easy` to `hard`, holding the string otherwise fixed, does not reliably produce a failure.** In this campaign it produced failures in 7 pairs, passes in 11, and no change of verdict in 55.

Not licensed by the packet:

1. **"Hard makes tasks easier."** 11 vs 7 with p ≈ 0.48 is a directionless coin. The counterintuitive cases are worth reporting; they are not a finding about difficulty.
2. **"Difficulty does not matter."** Seven pairs show a clean pass→fail conversion, three of them under the oracle guarantee.
3. **"A label flip is a verified intervention."** See §7. The pair design holds the *string* constant, not the rendered task.

---

## 6. The dial is not the same dial everywhere

- Only **3 of the 18 distinct dimension values** in the archive are `easy`, `medium`, `hard`. The others: `narrative`, `report`, `trap`, `ambiguous`, `strong`, `weak`, `balanced`, `skewed`, `solo`, `paired`, `bare_table`, `broken`, `valid`, `flat`, `reflective`.
- Difficulty strings have **three different lengths**: 2 dimensions (124 cases), 5 dimensions (51), 6 (19). A "position 2" flip is not the same kind of change across lengths.
- **29 of 33 families** contain at least one `hard` cell; 4 contain none.
- In the mixed-evidence families (`epistemic_games`, `ts_one_step`, `ts_trajectory`) the axes are not ordered difficulty at all, so no `easy`→`hard` pair exists there and none is counted in §4.

The 73 pairs are therefore 73 comparisons of *labels*, drawn from families whose labels mean different things. That is the reason the article is about the unreliability of the label, not about the magnitude of a difficulty effect.

---

## 7. External context — cite as prior audit, never as this packet's data

A prior source audit of the clean comparator behind this campaign (published separately) found ten advertised control or variable axes across nine category-family environments with **no implementation reference** in the inspected templates. If that reading holds for the executed workspaces, some label flips changed nothing any agent or judge could see — which would be one mechanical explanation for "no change of verdict" pairs.

The packet does not establish this for this campaign, and no draft may assert it as a cause. It may be cited, once, clearly attributed, as the reason a label flip is not automatically an intervention. The audit's premise is itself limited: it inspected a clean comparator, not the executed tree.

---

## 8. Limitations (state them; do not perform them)

- One provider, one model, text-only, **one seed per cell**, no reruns: no variance, no interval, no population estimate. The 73 pairs are 73 single draws.
- The pairing holds other dimensions constant in the *label string* only. Nothing in the archive shows the rendered tasks differed in exactly that one respect.
- Pair counts are not independent observations: `rd_adaptive_halting` (5 pairs) and `moco` (5 pairs) each reuse a single base cell.
- `compile_only` verdicts are exploratory by the campaign's own note; 9 of the 11 counterintuitive pairs live there.
- The archive records verdicts and scores, not causes. Nothing here says why a flip changed an outcome.
- Retry volume is inconsistent inside the export: `campaign_progress.json` reports `http_attempts: 6412`; the per-row `http_attempts` sum to 4,319. Cite neither, or cite both as a conflict.

---

## 9. Corrections to the earlier draft (`comparison_41.md`) — do not repeat

1. **"Five counterintuitive pairs, four intuitive pairs"** — the true counts are **11 and 7**. The draft listed one pair per family and dropped `regex_state_machine` position 1 and `neuro_symbolic_parser` position 1 entirely.
2. **"Five environments, four environments"** — the family counts are **5** and **6**.
3. **The pooled 0.726 vs 0.650 comparison** — cross-bucket, forbidden by the report's own aggregate note, and 0.650 is a state-56 figure (state-62 gives 0.645 with n = 121). Report per bucket or not at all.
4. **"The campaign is paused / 193 scored / one paused case"** — stale. Completed, 194 scored.
5. **"The effect direction depends on the environment family"** — stated as a conclusion, but the comparison is 11 vs 7 with p ≈ 0.48, and 55 of 73 pairs are saturated or floored. The honest version: direction is inconsistent and the inconsistency is not resolvable at this n.
6. **No mention that 9 of 11 counterintuitive pairs are compile-only** — the single most important caveat for this slot, and it was absent.
7. **"Near-zero scores" / "unsolvable" language** — inapplicable here and banned series-wide.

---

## Appendix A — provenance

All figures derive from `coverage.json` (194 rows):

- §2: `judge_guarantee` counts, cross-checked against `campaign_report.json` → `results_by_judge_guarantee`.
- §3: `hard in difficulty.split(',')` over rows, per bucket.
- §4: for each family, index cells by `tuple(difficulty.split(','))`; take all unordered pairs differing in exactly one index whose values are `{easy, hard}`; classify by `verdict`, then read `score`. Recomputed count: 73 pairs, 42 both-pass, 13 both-fail, 7 expected, 11 counterintuitive, 18 discordant.
- §4.3: same pairs, comparing `score` where verdicts match; 1 difference.
- §6: `Counter` over `len(difficulty.split(','))` and over all values.
- §8: `campaign_progress.json` `http_attempts` vs `sum(coverage.http_attempts)`.

Sign test: exact binomial, two-sided, n = 18, k = 11 → p = 0.4807.
