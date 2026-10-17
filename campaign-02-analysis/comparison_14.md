some model:

# Claim Killer: POST-03, "Where Mercury Breaks" (Mercury-2.5)

**Attribution.** A = "gpt 6 sol max". B = "gpt 6.1 sol max", which the blueprint uses as the base.
**Arithmetic checked.** 277+128 = 405 ✔. 416−405 = 11 ✔. 277/405 = 0.68395, which rounds to 0.684 ✔. p(1−p) = 35456/164025 = 0.2162, which rounds to 21.6% ✔. p²(1−p) = 0.1478, which rounds to 14.8%. Neither draft uses 14.8%; it is the probability of PASS→FAIL→PASS alone. Arithmetic errors found: **none**.

**Summary.** The arithmetic is clean. The real risks are:
- **Unverified details added by the drafts:** that judge guarantees are "mixed", that regex lengths are measured in "characters", and that class names were held fixed in the CSS sequence.
- **A unit problem in the packet:** "one seed per cell" versus 416 cases in 340 rows.
- **Blueprint items still present in base B:** the regex "all-pass" leftover, the SQL surface qualifier, the partial-score reconciliation paragraph, the long F-006 discussion, and the profanity artifact.

---

## 1. Campaign accounting (F-004)

| # | Claim (draft) | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 1 | "selected 416 cases across 38 environments and scored 405" (A, B) | SUPPORTED | F-004 | Keep. |
| 2 | "277 PASS, 128 FAIL" (A, B) | SUPPORTED | F-004 | Keep. |
| 3 | Pass share 0.684 "among scored cases" (A, B) | CORRECT-ARITHMETIC | 277/405 = 0.68395 | Keep, and always say "among scored cases". Do not write 0.684 without a denominator. |
| 4 | "The other 11 selected cases were unscored, not failures" (A); "11 … derived as 416−405" (B) | CORRECT-ARITHMETIC | 416−405 | Keep. B's statement that 11 is derived is the better wording. |
| 5 | "The packet does not establish whether scoring omissions are independent of environment or difficulty" (A) | SUPPORTED (packet is silent) | F-004 gives no missingness data | Keep. |
| 6 | Missingness "could be outcome-dependent—potentially missing not at random" (B) | NARROW | No data on why cases went unscored | Keep only as "unverified". Cut "MNAR" jargon to a single clause. |
| 7 | "0.684 is a conditional result among scored cases, not an established unconditional success rate" (B) | SUPPORTED | F-004 | Keep. One mention is enough, since #3 already covers it. |
| 8 | "These are campaign totals … not results specific to the transition examples" (B) | SUPPORTED | F-004 vs F-008 | Keep. |
| 9 | Pooled 0.684 is "a poor stand-in for the probability of passing any particular task" (A) | SUPPORTED (inference) | F-006 range 0.00–1.00 | Keep. |

## 2. Difficulty matrix and replication

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 10 | Matrix "contains 340 rows" keyed by environment × difficulty tuple (A, B) | SUPPORTED | Matrix description | Keep. |
| 11 | Fields include case counts, scored counts, pass/fail counts, pass rates, failure modes and judge guarantees (B; A lists a subset) | SUPPORTED | Matrix columns | Keep. |
| 12 | "each selected cell used seed-0, with no rerun" (A); "one seed-0 run per selected cell" (B) | SUPPORTED, but see #13 | Packet: single seed per selected cell | Keep the wording. Do not write "one case per row". |
| 13 | Implied: cell = matrix row | **NEEDS-CHECK** | 416 cases across 340 rows means an average of about 1.22 cases per row. So rows ≠ single-seed cells, or rows group several instances (n_cases column). | Do not equate "cell" with "row". Add an audit note: confirm what a "selected cell" is relative to a row. |
| 14 | "Cases, matrix rows, and matched difficulty sweeps are different units; the row count is not a count of independent opportunities to observe a reversal" (B) | SUPPORTED (inference) | Matrix description; #13 | Keep. This is the key point for denominator hygiene. |
| 15 | "It is a way to locate recorded outcomes, not a collection of replicated difficulty curves" (A) | SUPPORTED | Single seed, no replication | Keep. |
| 16 | "The judge guarantees also differ across the campaign" (A); "the campaign has mixed guarantees" (B) | **UNSUPPORTED** | The packet only says a `judge_guarantees` column exists. It does not say the values differ. | Rewrite: "The matrix records a judge-guarantees field; whether guarantees differ, including along any quoted sequence, is an audit item." |
| 17 | "pooled PASS labels need not certify the same kind of success" (A) | NARROW | This depends on #16 | Keep only as a conditional ("if guarantees differ…"). |
| 18 | "The packet does not show that a guarantee changed along any particular quoted sequence … a possible confound to audit" (B) | SUPPORTED | Packet is silent | Keep. This is the blueprint's "audit item" framing. |

## 3. Environment spread (F-006)

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 19 | Environment pass rates "span 0.00 to 1.00" (A, B) | SUPPORTED | F-006 | Keep. |
| 20 | "F-006 describes the environment pattern as bimodal" (B) | SUPPORTED as the packet's label; the shape itself is NEEDS-CHECK | The F-006 title says bimodal, but no distribution is given | Attribute the word to F-006 and don't adopt "bimodal" as the article's own claim. B already says "does not … validate a precise distributional shape". |
| 21 | Six named zero-rate environments: glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory (A, B) | SUPPORTED | F-006 | Keep. |
| 22 | The seventh entry `epistemic_silence/type_games` is unscored (B; A says "an additional entry") | SUPPORTED | F-006 | Keep. B's naming is fine. |
| 23 | "Its claimed total of seven is therefore not established as seven measured zeros" (B); "I do not count an unscored environment as one with a zero pass rate" (A) | SUPPORTED | F-006 count discrepancy | **The blueprint conflicts with itself here:** it lists "F-006 count discrepancy" under both Remove and Qualify. Resolve it this way: delete B's two-paragraph discussion and keep one clause, e.g. "six named environments score 0.00; a seventh entry counted with them is unscored." |
| 24 | "An unscored entry must not be converted into a zero to make the tally work" (B) | SUPPORTED | F-006 | Merge into the single clause from #23. |

## 4. F-008 sequences

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 25 | MoCo visible-test levels: PASS → FAIL → PASS (A, B) | SUPPORTED | F-008 | Keep. Don't invent numeric level values; the packet gives none. |
| 26 | "packet does not identify the middle [MoCo] failure's stage" (B) | SUPPORTED (packet is silent) | F-008 | Keep. |
| 27 | "Only the MoCo sequence is an unambiguous binary zigzag in the supplied description" (A) | SUPPORTED | F-008 | Keep. |
| 28 | CSS easy-surface, 3 → 4 → 5 bits: partial score → source-validation failure → PASS (A, B) | SUPPORTED | F-008 | Keep. |
| 29 | SQL graph-chain 6 → 12 → 25: PASS → source-validation failure → PASS (A, B) | SUPPORTED | F-008 | Keep. |
| 30 | "No corresponding SQL surface setting is established by the packet, so none is assumed here" (B) | SUPPORTED, but blueprint says **remove** | The blueprint removes the SQL surface qualifier | Delete the sentence. |
| 31 | The CSS partial score "has no supplied mapping to the campaign's binary accounting" (B table); "not documented as a binary PASS" (A) | SUPPORTED | F-008 vs F-004 | Keep one short table note: "first outcome is a partial score, not a binary result". |
| 32 | "The campaign totals contain PASS and FAIL, not a separate partial-score category… the packet does not explain how that local score was reconciled" (B); "packet does not reconcile those row-level descriptions with its scored-FAIL and unscored totals" (A) | SUPPORTED, but blueprint says **remove** | Partial-score reconciliation is on the remove list | Delete B's paragraph and A's sentence. Keep only #31. |
| 33 | "Nor do the examples … establish that every other component of each difficulty tuple was matched" (B) | SUPPORTED (packet is silent) | F-008 | Keep. This supports construct validity. |
| 34 | SQL lengths "are separated sampled lengths, not a dense sweep or a located boundary" (B); "[not] a threshold between the sparsely sampled lengths" (A) | SUPPORTED | Only lengths 6, 12 and 25 are given | Keep. |
| 35 | "Success at 6 and 25 … does not establish where performance changes … or that an underlying success probability changes at all" (B) | SUPPORTED | Single seed | Keep. |
| 36 | Selection rule: "report the three contrasts explicitly identified in F-008"; no prespecified rule or exhaustive count (A) | SUPPORTED | F-008; no enumeration in the packet | Keep (blueprint import). |
| 37 | "These examples therefore cannot tell us how prevalent reversals are" (A); "neither a [d-word] sweep denominator nor a basis for claiming that reversals are unusually frequent" (B) | SUPPORTED | No enumeration | Keep. **Leave [d-word] as written.** |

## 5. Chance calculation

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 38 | p = 277/405 ≈ 0.684 (A, B) | CORRECT-ARITHMETIC | F-004 | Keep. |
| 39 | p²(1−p) + p(1−p)² = p(1−p) (B) | CORRECT-ARITHMETIC | Algebra | Keep. |
| 40 | P(PFP or FPF) ≈ 21.6% (A, B) | CORRECT-ARITHMETIC | 0.2162 | Keep, with the qualifier "illustrative, not calibrated" in the same sentence. |
| 41 | 14.8% (blueprint only; in neither draft) | CORRECT-ARITHMETIC if defined as P(PFP) only = p²(1−p) = 0.1478 | Algebra | If added, define it explicitly as "PASS-FAIL-PASS specifically" and give it the same illustrative caveat. |
| 42 | "not a calibrated null hypothesis" / "not a measured reversal rate" (A, B) | SUPPORTED | Pooled environments, unestablished independence, no denominator | Keep. Acceptance criterion 1. |
| 43 | "An oscillation is not, by itself, unlikely under that artificial no-level-effect model" (A); a flat probability "can readily produce an apparently interesting shape" (B) | SUPPORTED (conditional on the model) | Arithmetic | Keep, tied to the hypothetical model. |
| 44 | "Even monotonically declining success probabilities can produce non-monotonic sequences of individual outcomes" (A, B) | SUPPORTED (mathematical fact) | — | Keep. |
| 45 | "The observations are examples worth investigating, not evidence of enrichment over chance" (B) | SUPPORTED | No denominator | Keep. |

## 6. Axis definitions and construct validity

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 46 | "MoCo visible-test level changes test coverage" (A, B) | SUPPORTED as the packet's description; NEEDS-CHECK as fact | Packet axis list; the blueprint calls axis definitions unverified | Qualify: "according to the packet's axis description". |
| 47 | Visible-test coverage "does not even specify a direction" without knowing the effect on solver information (A) | SUPPORTED (inference) | — | Keep (blueprint's "no direction" import). |
| 48 | "CSS varies class names and bit counts" (B) | NARROW, **misdescribed** | The packet says CSS *surface labels* change class names **and** bit counts | Restate exactly: "CSS surface labels change class names and bit counts." |
| 49 | "bit count changes while the recorded surface label remains easy; CSS configurations can also alter class names, but that is not the axis swept" (A) | **UNSUPPORTED** in part | The packet does not say class names were held fixed across 3/4/5 bits. There is also a tension: if the surface label sets bit count, the packet doesn't explain how bits vary *within* easy-surface. | Remove "not the axis swept" (CSS axis misdescription). Flag as an audit item: how bit count relates to the surface label. |
| 50 | "SQL varies graph-chain length" (A, B) | SUPPORTED as the packet's description | Packet | Keep, with the general axis-unverified qualifier. |
| 51 | Regex input lengths "32, 128, and 512 characters" (A, B) | **NEEDS-CHECK** | The packet gives 32/128/512 with no unit | Drop "characters", or write "length 32/128/512 (unit unspecified)". |
| 52 | "the supplied evidence does not establish an accompanying all-pass sequence" (B) | UNSUPPORTED framing (leftover from the regex pass claim) | No regex outcomes in the packet | Replace with A's wording: "the packet supplies no regex outcome sequence." The words "all-pass" must not appear. |
| 53 | Heterogeneous axes explain why a shared "easy to hard" axis is unjustified, but "does not explain why the middle MoCo cell failed" / "does not explain the within-environment reversals" (A, B) | SUPPORTED | — | Keep. Acceptance criterion 6. |
| 54 | "even proof that test suites were nested would establish an implication only for a fixed submission" (B) | SUPPORTED (conditional logic); nesting itself is unverified | The packet doesn't say whether suites are nested | Keep as hypothetical and mark nesting as unknown. |
| 55 | "neither validates a common latent difficulty scale nor disproves every possible one" (B) | SUPPORTED | — | Keep. |
| 56 | "Some settings change test coverage, others change task size or surface form" (A) | NARROW | Calling bits and chain length "task size" is interpretation | Acceptable. Prefer the packet's terms (bit count, chain length, surface label). |

## 7. Source-validation failures and causal hypotheses

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 57 | The CSS and SQL middle cases are source-validation failures, "not reported semantic-test failures" (B); not observations that valid code failed a behavioural check (A) | SUPPORTED | F-008 | Keep. Acceptance criterion 5. |
| 58 | "neither source-validation failure tells us how valid code would have performed" (A) | SUPPORTED (inference) | — | Keep. |
| 59 | "A source-validation rejection can still be a legitimate benchmark failure when valid source is part of the contract" (B) | SUPPORTED (conditional) | — | Keep. |
| 60 | "Truncated or length-limited output is one possible explanation; malformed source or a validator interaction is another" (A); "truncation or length hypothesis is unresolved" (B) | NARROW (hypothesis only) | No artifacts, limits or diagnostics in the packet | Keep only as explicitly unresolved hypotheses. Never say "likely". |
| 61 | "A pass at the larger … setting does not settle a response-length hypothesis … source length need not increase with the nominal task-size setting" (A, B) | SUPPORTED (logic) | — | Keep. |
| 62 | Are source-validation failures counted inside the 128 FAIL or the 11 unscored? (implicit in both) | NEEDS-CHECK | The packet does not map them | Don't assign them to either denominator. Do this silently, without the reconciliation paragraph (see #32). |

## 8. Provenance

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 63 | The repository was dirty; a clean checkout or commit alone would not reconstruct the executed source (A, B) | SUPPORTED (fact + inference) | Packet: dirty repo | Keep. |
| 64 | "That does not show that the recorded counts are wrong or that an uncommitted change caused an anomaly" (B) | SUPPORTED | — | Keep. Blocks a causal overreach. |
| 65 | The model name does not specify a checkpoint, inference settings or harness revision (A); there is no complete model-and-harness manifest (B) | SUPPORTED (packet is silent) | — | Keep, phrased as "the packet does not supply…". |
| 66 | "This is one campaign … not a demonstrated property of every deployment bearing that name" (B) | SUPPORTED | — | Keep. |
| 67 | "No additional cases were run" / "no new sweep enumeration, artifact inspection, or replication is claimed" (A, B) | SUPPORTED | — | Keep. Acceptance criterion 9. |

## 9. Figures and metadata

| # | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|
| 68 | Fig. 1: "Cell labels give passes over scored cases; grey denotes unscored" (A) | NEEDS-CHECK | The figure isn't supplied (placeholder "!") | Build it only from the 340-row matrix. Check that the grey and zero encodings match the data. |
| 69 | Fig. 2: "Selected MoCo visible-test **comparisons**" (A) | NEEDS-CHECK | F-008 gives one MoCo sequence with unnamed levels | Use the singular, or justify more than one. Don't invent level values. Keep the caption "not fitted pass-rate curves". |
| 70 | Epistemic status: "High for the recorded counts and sequences; low for any claim about difficulty effects" (A) | SUPPORTED | — | Keep (blueprint import). |

## Blueprint compliance (non-claim edits)

- **Remove "fuckingly"**: A has "task fuckingly presented" and "was fuckingly judged"; B has the heading "What was fuckingly recorded". These are not bracketed tokens.
- **Retain** B's "[d-word] finding" and "[d-word] sweep denominator" exactly as written. Add no other bracketed tokens.
- **"Hardest label" framing**: not present in either draft. Make sure the merge doesn't bring it back.
- **Remove** #30 (SQL surface), #32 (partial-score reconciliation) and #52 (regex all-pass). Correct #48 and #49 (CSS axis). Shorten #23 and #24 (F-006).

---

## Safe claim set (no qualification needed)

1. The campaign selected 416 cases across 38 environments, scored 405, and recorded 277 PASS and 128 FAIL.
2. 11 selected cases were unscored (416 − 405). They are not failures.
3. The pass rate among scored cases is 0.684 (277/405).
4. The environment × difficulty-tuple matrix has 340 rows. Its fields include case, scored, pass and fail counts, pass rate, failure modes and judge guarantees.
5. Each selected cell was run with a single seed (seed-0), and nothing was replicated.
6. The source repository was dirty at run time.
7. Environment pass rates range from 0.00 to 1.00.
8. MoCo across visible-test levels recorded PASS → FAIL → PASS.
9. CSS state machine (easy surface, 3 → 4 → 5 bits) recorded partial score → source-validation failure → PASS.
10. SQL fixed points (graph-chain lengths 6 → 12 → 25) recorded PASS → source-validation failure → PASS.
11. The two middle CSS and SQL outcomes are source-validation failures, not reported semantic-test failures.
12. The packet supplies no regex outcome sequence.
13. These three sequences are the ones F-008 identifies. The packet gives no exhaustive enumeration of eligible sweeps.
14. A non-monotonic sequence of single outcomes is compatible with a monotonically declining success probability.
15. Cases, matrix rows and matched sweeps are different units.

## Qualified claim set (caveat in the same sentence)

1. **21.6%** = p(1−p) with p = 277/405, the chance of either zigzag *under an illustrative model with independent, equal-probability binary outcomes; it is not a calibrated null hypothesis or a measured rate.* (14.8% = PASS-FAIL-PASS only, with the same caveat.)
2. **Axis meanings**: MoCo visible-test level changes test coverage; CSS surface labels change class names and bit counts; SQL changes graph-chain length; regex changes input length 32/128/512 — *all as described by the packet; not independently verified, unit for regex unspecified.*
3. **F-006 zero tally**: six named environments score 0.00; *a seventh entry counted with them (epistemic_silence/type_games) is unscored, not a measured zero.*
4. **"Bimodal"**: *F-006's characterization, not a verified distributional shape.*
5. **Judge guarantees**: *recorded per row; whether they vary across the campaign or along any quoted sequence is unverified and is an audit item.*
6. **Truncation or length limits** as a cause of the source-validation failures: *one unresolved hypothesis among others (malformed source, validator interaction); the packet has no artifacts, budgets or diagnostics to test it.*
7. **0.684 as a success rate**: *conditional on being scored; why the 11 cases went unscored is unknown and may not be random.*
8. **CSS partial score**: *not a binary result, so the CSS sequence cannot be counted as a pass/fail/pass reversal.*
9. **"One seed per cell"**: *how a "selected cell" relates to a matrix row (416 cases vs 340 rows) needs confirming.*
10. **Heterogeneous axes** make a shared difficulty scale unjustified, *but do not explain any individual middle-level failure.*


&&&&&&&&&&&&&&&&

opus 5:

# CLAIM KILLER REPORT — POST-03 "Where Mercury Breaks"

**Scope:** Draft A = `gpt 6 sol max` (first draft). Draft B = `gpt 6.1 sol max` (blueprint base).
**Arithmetic re-run:** 277/405 = 0.68395; 277+128 = 405 ✓; 416−405 = 11 ✓; p(1−p) = 21.616%; p²(1−p) = 14.784%; (1−p)²p = 6.832%; 340/38 = 8.95 avg rows/env.

**Verdict key:** SUPPORTED (packet asserts it) · NARROW (true only in a restricted reading; needs in-sentence limiter) · UNSUPPORTED (packet does not establish it) · CORRECT-ARITHMETIC (math checks out; interpretation may still need a caveat) · NEEDS-CHECK (not derivable from the packet; verify against artifact/figure/front-matter).

---

## TABLE 1 — DRAFT A (gpt 6 sol max)

| # | Claim (as written, Draft A) | Verdict | Evidence source | Required action for final article |
|---|---|---|---|---|
| A1 | "selected 416 cases across 38 environments and scored 405 of them: 277 `PASS`, 128 `FAIL`" | SUPPORTED | F-004 verbatim | Keep. Attribute to F-004 inline. |
| A2 | "a pass share of 0.684 **among scored cases**" | CORRECT-ARITHMETIC | F-004; 277/405 = 0.68395 | Keep. Denominator qualifier "among scored" must stay in the same sentence (AC: denominator hygiene). |
| A3 | "The other 11 selected cases were unscored, not failures." | CORRECT-ARITHMETIC / NARROW | 416−405 = 11; F-004 records no outcome for them | Reword to "not recorded as failures." As written it edges toward asserting their true outcome. |
| A4 | "The packet does not establish whether scoring omissions are independent of environment or difficulty setting" | SUPPORTED (absence claim) | Packet silent on attrition mechanism | Keep. |
| A5 | "so the scored-only share need not describe every selected case" | SUPPORTED (inference) | Follows from A3–A4 | Keep. |
| A6 | "The environment × difficulty-tuple matrix contains 340 rows, with case and score counts, failure modes, and judge guarantees" | SUPPORTED | Packet: 340 rows; fields n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees | Keep. Consider naming the fields exactly as in the packet. |
| A7 | "each selected cell used seed-0, with no rerun at that setting" | SUPPORTED | Packet: single seed per selected cell (seed-0); no replication | Keep. |
| A8 | "The judge guarantees **also differ across the campaign**" | **UNSUPPORTED as stated** | Packet establishes a `judge_guarantees` *field* exists; it does not state guarantees vary | **Downgrade:** "the matrix records a per-row `judge_guarantees` field, so comparability across rows is an open audit item." Blueprint explicitly lists judge guarantees as *audit item*, not established heterogeneity. |
| A9 | "so pooled `PASS` labels need not certify the same kind of success" | NARROW | Conditional on A8 | Keep only in conditional form ("if guarantees differ…"). |
| A10 | "Environment pass rates in the packet span 0.00 to 1.00 (F-006)" | SUPPORTED | F-006 | Keep. |
| A11 | "another reason the pooled 0.684 is a poor stand-in for the probability of passing any particular task" | SUPPORTED (inference) | F-006 spread + F-004 pooling | Keep. |
| A12 | "F-006 calls seven environments zero-scoring but names six … while describing an additional entry as unscored" | SUPPORTED | F-006 discrepancy is in the packet | Keep. Blueprint requires disclosure, not assertion of "7 zero-rate environments." |
| A13 | Named list `glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory` | SUPPORTED | F-006 (6 named) | Keep verbatim; spelling must match packet exactly. |
| A14 | Omits naming `epistemic_silence/type_games` as the unscored entry | NEEDS-CHECK (completeness) | F-006 names it | Add the name; Draft B does this correctly. |
| A15 | "I do not count an unscored environment as one with a zero pass rate." | SUPPORTED (method statement) | Packet marks it unscored | Keep. |
| A16 | Fig. 1 caption: "Cell labels give passes over scored cases; grey denotes unscored cases, not zero passes." | NEEDS-CHECK | Figure content not in packet | Verify the rendered figure actually encodes grey = unscored and label = n_pass/n_scored before publishing. |
| A17 | Fig. 1 caption: "The display does not enumerate all eligible three-level sweeps." | SUPPORTED | Packet gives no sweep enumeration | Keep (protects AC: no prevalence claim). |
| A18 | "the selection rule is simple: report the three contrasts explicitly identified in F-008" | SUPPORTED | F-008 | Keep — this is the blueprint's mandated selection-rule sentence. Import into B. |
| A19 | "The packet gives neither a prespecified search rule nor an exhaustive count of complete, comparable three-level sweeps" | SUPPORTED | Packet silent | Keep. |
| A20 | "These examples therefore cannot tell us how prevalent reversals are." | SUPPORTED (inference) | A19 | Keep. |
| A21 | MoCo row: "Visible-test level … `PASS` → `FAIL` → `PASS`" | SUPPORTED | F-008 | Keep. |
| A22 | MoCo row implies three *ordered/adjacent* levels | NEEDS-CHECK | F-008 says "visible-test levels yield pass/fail/pass"; adjacency, direction and level values are not given | Say "three recorded visible-test levels (values not supplied)"; do not imply monotone increasing coverage. |
| A23 | CSS row: "Bit count, at the easy-surface label: 3 → 4 → 5 bits" | SUPPORTED | F-008: easy-surface cases over 3/4/5 bits | Keep. This is the corrected axis description (blueprint: remove CSS axis mis-description). |
| A24 | CSS row: "Partial score → source-validation failure → `PASS`" | SUPPORTED | F-008 | Keep. |
| A25 | SQL row: "Graph-chain length: 6 → 12 → 25 … `PASS` → source-validation failure → `PASS`" | SUPPORTED | F-008 | Keep. Note packet gives pass at 6 and 25, source-validation failure at 12 — ordering is numeric, not necessarily run order. |
| A26 | Draft A does **not** attach a surface qualifier to SQL | SUPPORTED (compliance) | Blueprint removal item | Keep this absence. |
| A27 | "Only the MoCo sequence is an unambiguous binary zigzag in the supplied description." | SUPPORTED (inference) | F-008 CSS = partial/validation; SQL middle = validation | Keep. |
| A28 | "neither source-validation failure tells us how valid code would have performed on the task" | SUPPORTED (logical) | F-008 failure-stage distinction | Keep — satisfies AC: source-validation distinction. |
| A29 | "The packet also does not reconcile those row-level descriptions with its scored-`FAIL` and unscored totals, so I do not silently assign them to either denominator." | SUPPORTED | Packet silent | Keep one sentence only; blueprint removes extended partial-score reconciliation. |
| A30 | Fig. 2 caption: "Selected MoCo visible-test **comparisons**" (plural) | NEEDS-CHECK | Packet supplies exactly one MoCo sequence | Singularize or confirm the figure shows only the one F-008 sequence; plural implies unreported MoCo data. |
| A31 | Fig. 2 caption: "with seed-0 alone in each selected cell, they are not fitted pass-rate curves" | SUPPORTED | Packet: single seed | Keep. |
| A32 | "suppose each level independently produced a binary pass with the campaign-wide probability p = 277/405, approximately 0.684" | CORRECT-ARITHMETIC | 0.68395 | Keep; label "illustrative" in the same sentence. |
| A33 | "`PASS/FAIL/PASS` or `FAIL/PASS/FAIL` with probability p(1−p), approximately **21.6%**" | CORRECT-ARITHMETIC | p(1−p) = 21.616% | Keep, but **add**: the specific observed shape PASS–FAIL–PASS alone is p²(1−p) ≈ **14.8%**. Blueprint requires both to be flagged illustrative, not calibrated. |
| A34 | "An oscillation is not, by itself, unlikely under that artificial no-level-effect model." | SUPPORTED (conditional) | Follows from A33 | Keep with "under that artificial model" attached. |
| A35 | "That is **not** a calibrated null hypothesis for Mercury-2.5." | SUPPORTED (required disclaimer) | AC #1 | Mandatory. Keep. |
| A36 | "It pools unlike environments and judge guarantees; it applies to binary outcomes, unlike the CSS record" | SUPPORTED | F-006 spread; F-008 CSS partial | Keep. |
| A37 | "the packet supplies no denominator of eligible sweeps" | SUPPORTED | Packet silent | Keep. |
| A38 | "Even if an environment's underlying chance of success decreased steadily …, one outcome per setting could still zigzag." | SUPPORTED (probability logic) | Single-seed design | Keep. |
| A39 | "The two intermediate source-validation failures … are failures of the end-to-end submission pipeline" | NARROW | Packet says "source validation failure"; "end-to-end submission pipeline" is the author's model of the stack | Reword to the packet's own term: "failures recorded at the source-validation stage." |
| A40 | "Truncated or length-limited output is one possible explanation; malformed source or a validator interaction is another." | SUPPORTED **only as unselected hypotheses** | Packet supplies no diagnostics | Keep in explicitly hypothetical voice; never collapse to one cause (AC: no unsupported causal explanation). |
| A41 | "The packet provides no generated files, output lengths, limits, or validator diagnostics" | SUPPORTED (absence) | Packet contents | Keep. |
| A42 | "A pass at the larger CSS bit count or SQL chain length does not settle a response-length hypothesis, because generated source length need not increase with the nominal task-size setting." | SUPPORTED (reasoning) | No artifact data | Keep — this is a strong anti-overclaim sentence; import to final. |
| A43 | "In MoCo, the visible-test setting changes test coverage." | SUPPORTED-as-reported | Packet axis list | Attribute: "the packet states…"; construct validity unverified (AC #7). |
| A44 | "CSS configurations can also alter class names, but that is not the axis swept in the table." | SUPPORTED | Packet: CSS surface labels change class names and bit counts; F-008 holds surface at easy | Keep. |
| A45 | "SQL varies graph-chain length." | SUPPORTED-as-reported | Packet axis list | Keep with attribution. |
| A46 | "**Regex state machines** provide input-string lengths of 32, 128, and 512 characters" | NEEDS-CHECK (naming) | Packet says "regex changes input-string length (32/128/512)"; the environment is not named "regex state machines" | Use the packet's label ("the regex environment"). Lengths themselves SUPPORTED. |
| A47 | "the supplied packet gives no corresponding regex outcome sequence, so none is inferred here" | SUPPORTED (compliance) | Blueprint: remove regex pass claim | Keep. |
| A48 | "Bits, graph-chain lengths, and characters have numerical orders. Whether they put *this model* under increasing difficulty is a different, unmeasured proposition." | SUPPORTED (inference) | No calibration in packet | Keep. Core thesis sentence. |
| A49 | "Visible-test coverage does not even specify a direction …" | SUPPORTED (argument) | Axis description only | Keep — blueprint's mandated "no direction" argument. |
| A50 | "This cross-environment mismatch explains why a shared 'easy to hard' x-axis is unjustified. It does **not** explain why the middle MoCo cell failed." | SUPPORTED | Logical separation | Keep verbatim; strongest anti-causal guard in either draft. |
| A51 | "The campaign repository was dirty, so a clean checkout alone would not establish that it reproduces the task templates or judges used in the run" | SUPPORTED | Packet: dirty repo | Keep. Do **not** extend to "results are wrong." |
| A52 | "the supplied model name likewise does not specify a checkpoint, inference settings, or harness revision" | SUPPORTED (absence) | Packet | Keep. |
| A53 | "a change in the task **fuckingly** presented" / "what was **fuckingly** judged" | ARTIFACT | Blueprint removal item | **Delete both.** (Distinct from `[d-word]`, which is intentional and stays.) |
| A54 | "Denser SQL lengths around 12 and the rejected source itself would be better evidence …" | SUPPORTED (recommendation) | Framed as follow-up | Keep; label as proposal, not completed work. |
| A55 | "the three recorded sequences identify cases worth auditing. They do not locate where a model's ability breaks." | SUPPORTED | Whole packet | Keep — blueprint's closing cadence. |
| A56 | Evidence-base footer attributing F-004/F-006/F-008 + matrix | SUPPORTED | Matches packet | Keep; merge with B's fuller scope note. |
| A57 | Structure: 4 sections, 2 figures | NON-COMPLIANT (editorial) | Blueprint: 7 sections | Expand to 7 per blueprint; retain both figures. |
| A58 | Front matter `date: 2026-10-16`, title, byline | NEEDS-CHECK | Not in packet | Verify against site conventions; not an evidentiary claim. |

---

## TABLE 2 — DRAFT B (gpt 6.1 sol max — blueprint base)

| # | Claim (as written, Draft B) | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| B1 | Epistemic block: "The campaign does not validate its difficulty labels as an ordinal scale" | SUPPORTED | No calibration evidence anywhere in packet | Keep. |
| B2 | Epistemic block: "One Mercury-2.5 campaign; one seed-0 run per selected cell; no replication; dirty source repository." | SUPPORTED | Packet provenance items | Keep. Reformat to Draft A's five-field epistemic-status block per blueprint import. |
| B3 | "Pass, fail, pass is an inviting shape. It suggests a model that succeeds on a small problem, breaks … then recovers when the problem grows." | NARROW (framing) | MoCo axis is test coverage, not problem size | Keep only as the *naïve reading being rebutted*; add "on the naïve reading" or similar, since MoCo's axis is not a size axis. |
| B4 | "The Mercury evidence packet contains that sequence in MoCo, alongside related sequences in CSS state machines and SQL fixed points" | SUPPORTED | F-008 | Keep. |
| B5 | "these are selected, single-seed observations, not estimates of a difficulty curve" | SUPPORTED | F-008 + seed-0 design | Keep. |
| B6 | "Some of the recorded failures concern source validation rather than demonstrated failure on the task's semantic requirements." | SUPPORTED | F-008 | Keep (AC #5). |
| B7 | "The **[d-word]** finding is methodological…" | N/A — INTENTIONAL TOKEN | Blueprint: retain ×2 | **Do not touch.** |
| B8 | "## What was **fuckingly** recorded" (heading) | ARTIFACT | Blueprint removal item | **Delete the artifact word**; retitle (e.g., "What was recorded"). |
| B9 | "selected **416 cases**, scored **405**, recorded **277 PASS** and **128 FAIL**, for a scored-case pass rate of **0.684** across **38 environments**" | SUPPORTED / CORRECT-ARITHMETIC | F-004; 277+128 = 405 ✓ | Keep. |
| B10 | "That rate describes scored cases, not every selected case. The **11** selected-but-unscored cases remain outside its denominator." | CORRECT-ARITHMETIC + SUPPORTED | 416−405 = 11 | Keep (AC #3). |
| B11 | "These are campaign totals from F-004, not results specific to the transition examples." | SUPPORTED | F-004 scope | Keep — prevents the 0.684 from being read as a per-sweep rate. |
| B12 | "The environment difficulty matrix has **340 rows**, each identified by an environment and a difficulty tuple." | SUPPORTED | Packet | Keep. |
| B13 | Field list: "case counts, scored counts, pass and fail counts, pass rates, failure modes, and judge guarantees" | SUPPORTED | Packet field list | Keep. |
| B14 | "Cases, matrix rows, and matched difficulty sweeps are therefore different units; the row count is not a count of independent opportunities to observe a reversal." | SUPPORTED (inference) | 340 rows ≠ enumerated sweeps | Keep (AC #2/#3). |
| B15 | "F-008 supplies the following examples. Each inherits the campaign's single-seed limitation." | SUPPORTED | F-008 + seed-0 | Keep; add Draft A's explicit selection-rule sentence (A18) here. |
| B16 | Table/MoCo: "Successive visible-test levels" | NEEDS-CHECK | F-008 does not state levels are successive/adjacent | Change to "visible-test levels (values not supplied)". |
| B17 | Table/MoCo: "PASS → FAIL → PASS" | SUPPORTED | F-008 | Keep. |
| B18 | Table/MoCo: "the packet does not identify the middle failure's stage" | SUPPORTED (absence) | F-008 gives no stage for MoCo | Keep. |
| B19 | Table/CSS: "Bit counts **3 → 4 → 5**, at the easy surface setting" | SUPPORTED | F-008 | Keep. |
| B20 | Table/CSS: "Partial score → source-validation failure → PASS" | SUPPORTED | F-008 | Keep. |
| B21 | Table/CSS: "The partial score has no supplied mapping to the campaign's binary accounting." | SUPPORTED (absence) | Packet silent | Keep. |
| B22 | Table/SQL: "Graph-chain lengths **6 → 12 → 25**" + "PASS → source-validation failure → PASS" | SUPPORTED | F-008 | Keep. |
| B23 | Table/SQL: "These are separated sampled lengths, not a dense sweep or a located boundary." | SUPPORTED (inference) | Gaps 6→12→25 | Keep. |
| B24 | "MoCo supplies a reported binary reversal, although its failed stage is unspecified." | SUPPORTED | F-008 | Keep (AC #4: sequence asymmetry). |
| B25 | "SQL supplies endpoint successes around a source-validation rejection." | SUPPORTED | F-008 | Keep. |
| B26 | "CSS supplies a mixed-status sequence … it cannot simply be entered into a binary reversal count." | SUPPORTED | F-008 + no mapping | Keep. |
| B27 | "The campaign totals contain PASS and FAIL, not a separate partial-score category." | NARROW | F-004 reports only PASS/FAIL counts; packet does not state no third category exists in the scoring scheme | Soften: "F-004 reports only PASS and FAIL counts." |
| B28 | "Preserving the CSS description does not add another category to those totals; it acknowledges that the packet does not explain how that local score was reconciled with them." | REMOVE (blueprint) | Blueprint: remove partial-score reconciliation | Cut this paragraph; keep only B21/B26. |
| B29 | "The easy-surface qualifier belongs to the CSS example. No corresponding SQL surface setting is established by the packet, so none is assumed here." | SUPPORTED (compliance) | Blueprint: remove SQL surface qualifier | Keep (may compress to one clause). |
| B30 | "Nor do the examples … establish that every other component of each difficulty tuple was matched." | SUPPORTED (absence) | Tuple structure given; matching not stated | Keep — important and unique to B. |
| B31 | "**MoCo visible-test level changes test coverage.** … it is not automatically a measure of how difficult the submission was to construct." | SUPPORTED-as-reported + SUPPORTED inference | Packet axis list | Keep; attribute axis definition to the packet (unverified construct). |
| B32 | "**CSS varies class names and bit counts.** The quoted sequence concerns bit count at a fixed easy surface setting" | SUPPORTED | Packet axis list + F-008 | Keep. |
| B33 | "**SQL varies graph-chain length.** … the packet does not calibrate that parameter against a replicated success probability." | SUPPORTED | Packet; no replication | Keep. |
| B34 | "**Regex varies input-string length: 32, 128, and 512 characters.** … the supplied evidence does not establish an accompanying all-pass sequence." | SUPPORTED (compliance) | Packet axis list; no regex outcomes | Keep — correctly kills the regex pass claim. |
| B35 | "the packet's axis definitions" treated as given facts about the harness | NEEDS-CHECK (construct validity) | Axis definitions are packet descriptions, not verified against code (dirty repo) | Add one sentence: axis definitions are as described in the packet and were not independently verified against the executed source (AC #7). |
| B36 | "Calling these settings 'difficulty' does not make them measurements of the same quantity." | SUPPORTED (inference) | Heterogeneous axes | Keep. |
| B37 | "That heterogeneity does **not** explain the within-environment reversals." | SUPPORTED | Logical | Keep (AC #6). |
| B38 | "even monotonically declining success probabilities can produce non-monotonic sequences of individual outcomes" | SUPPORTED (probability logic) | Single-draw design | Keep. |
| B39 | "even proof that test suites were nested would establish an implication only for a **fixed submission**" | SUPPORTED (conditional reasoning) | Hypothetical, flagged as such | Keep; ensure "nested" is visibly hypothetical — the packet never states nesting. |
| B40 | "The archive therefore neither validates a common latent difficulty scale nor disproves every possible one." | SUPPORTED | Packet | Keep. |
| B41 | "Suppose, purely as an illustration, that three binary outcomes were independent and had the same pass probability p" | SUPPORTED (assumption, declared) | — | Keep. |
| B42 | "p²(1−p) + p(1−p)² = p(1−p)" | CORRECT-ARITHMETIC (algebra verified) | Factorisation exact | Keep. |
| B43 | "p = 277/405 ≈ 0.684, gives approximately **21.6%**" | CORRECT-ARITHMETIC | 21.616% | Keep; **add the 14.8% figure** for PASS–FAIL–PASS alone (p²(1−p) = 14.784%), since that is the shape actually observed, and mark both illustrative per blueprint. |
| B44 | "That percentage is a hypothetical calculation derived from F-004, **not a measured reversal rate or a calibrated null model**" | SUPPORTED (required) | AC #1 | Mandatory. Keep in the same paragraph as the number. |
| B45 | "independence is not established; the examples were not supplied through a declared exhaustive selection procedure" | SUPPORTED (absence) | Packet | Keep. |
| B46 | "The actual prevalence question cannot be answered from the supplied examples." | SUPPORTED | No sweep denominator | Keep (AC #2). |
| B47 | "We consequently have neither a **[d-word]** sweep denominator nor a basis for claiming that reversals are unusually frequent." | SUPPORTED (+ intentional token) | Packet | Keep token untouched. |
| B48 | "An exhaustive analysis would start with the matrix, fix an environment and all non-varied tuple components, and enumerate every eligible ordering…" | SUPPORTED (proposal) | Framed as not done | Keep; "That enumeration is not reported here" must stay. |
| B49 | "Success at **6** and **25**, with a validation failure at **12**, does not establish where performance changes between those settings—or that an underlying success probability changes at all." | SUPPORTED | F-008 + no replication | Keep. |
| B50 | "The CSS middle case and the SQL middle case are explicitly described as **source-validation failures**, not reported semantic-test failures." | SUPPORTED | F-008 | Keep (AC #5). |
| B51 | "A source-validation rejection can still be a legitimate benchmark failure when valid source is part of the contract." | NARROW (normative) | Packet does not define the scoring contract | Mark as the author's position, not a packet fact: "if valid source is part of the contract — which the packet does not specify —". |
| B52 | "Separating it from a semantic failure is diagnosis, not forgiveness." | SUPPORTED (rhetorical, non-evidentiary) | — | Keep. |
| B53 | "The truncation or length hypothesis is unresolved … the packet does not supply submitted artifacts, termination reasons, output budgets, or validator diagnostics" | SUPPORTED (absence) | Packet | Keep (AC #6). |
| B54 | "The SQL success at the longer chain does not rule truncation out: task size need not map directly to emitted-source length" | SUPPORTED (reasoning) | No artifact data | Keep. |
| B55 | "Equally, the middle rejection does not establish truncation. The failure label identifies a category, not its cause." | SUPPORTED | F-008 | Keep — best single anti-causal sentence in B. |
| B56 | "The matrix records a `judge_guarantees` field, **and the campaign has mixed guarantees**" | **UNSUPPORTED (second clause)** | Packet establishes the field only | **Cut or downgrade** to: "whether guarantees vary across rows is not reported." Same defect as A8. |
| B57 | "a PASS therefore should not be assumed to certify an identical property everywhere" | NARROW | Conditional on B56 | Keep as conditional ("if guarantees vary…"). |
| B58 | "The packet does not show that a guarantee changed along any particular quoted sequence, so changing guarantees are a possible confound to audit—not an established explanation" | SUPPORTED | Packet silent | Keep. This is the blueprint-mandated "audit item" framing. |
| B59 | "F-006 describes the environment pattern as bimodal and reports pass rates spanning **0.00 to 1.00**" | SUPPORTED | F-006 | Keep. |
| B60 | "its zero-rate tally is internally inconsistent … names six … while `epistemic_silence/type_games` is marked unscored. Its claimed total of seven is therefore not established as seven measured zeros." | SUPPORTED | F-006 discrepancy (6 named + 1 unscored = 7 claimed) | Keep. Do **not** assert "7 environments scored 0.00" anywhere. |
| B61 | "The reported range supplies context for heterogeneity; it does not, from this summary alone, validate a precise distributional shape." | SUPPORTED (inference) | F-006 gives a label + range only | Keep; this correctly declines to endorse "bimodal" as a measured shape. |
| B62 | "An unscored entry must not be converted into a zero to make the tally work." | SUPPORTED (method) | F-006 | Keep. |
| B63 | "The **11 unscored selected cases**, derived as 416−405" | CORRECT-ARITHMETIC | ✓ | Keep. |
| B64 | "They are missing scores, not an additional set of recorded failures." | SUPPORTED | F-004 | Keep. |
| B65 | "If score availability depends on case properties …, the missingness could be outcome-dependent—potentially missing not at random. That mechanism remains unverified." | SUPPORTED **as flagged hypothesis** | Packet silent on attrition | Keep with the "remains unverified" clause attached. |
| B66 | "**0.684 is a conditional result among scored cases**, not an established unconditional success rate" | SUPPORTED | F-004 | Keep (AC #3). |
| B67 | "retaining only complete scored triples could select a different subset from all requested comparisons" | SUPPORTED (inference) | Attrition + sweep selection | Keep. |
| B68 | "This is one campaign under the **Mercury-2.5** label, not a demonstrated property of every deployment bearing that name." | SUPPORTED | Single campaign | Keep (AC #8). |
| B69 | "The supplied packet does not establish a complete model-and-harness manifest …" | SUPPORTED (absence) | Packet | Keep. |
| B70 | "The repository was also dirty. That does not show that the recorded counts are wrong or that an uncommitted change caused an anomaly" | SUPPORTED | Packet: dirty repo | Keep — correctly refuses the causal leap. |
| B71 | "Reproduction requires the relevant working-tree changes or an equivalent frozen snapshot." | SUPPORTED (inference) | Dirty repo | Keep. |
| B72 | "one seed-0 run per selected cell provides no replicated seed-level estimate of variability" | SUPPORTED | Packet | Keep (AC #8). |
| B73 | "Without clarity about what the seed controls, it should not be treated as a substitute for documenting either task variation or model-generation variation." | SUPPORTED (absence) | Packet does not define seed scope | Keep. |
| B74 | "**No probabilistic threshold is detected here.**" | SUPPORTED | Whole packet | Keep. |
| B75 | Five "what would make it credible" bullets | SUPPORTED (proposals) | Explicitly labelled "proposed checks, not analyses already completed" | Keep that labelling sentence; it is what makes the section safe. |
| B76 | "The archive records MoCo's pass–fail–pass sequence, CSS's partial-score–validation-failure–pass sequence, and SQL's successes around a validation rejection" | SUPPORTED | F-008 | Keep. |
| B77 | "none establishes a non-monotonic difficulty curve" | SUPPORTED (conclusion) | Single seed + unvalidated axes | Keep. |
| B78 | "Mercury's labels have not been validated as a common ordinal scale … These observations tell us where to audit the measurement." | SUPPORTED | Packet | Keep; merge with A55 closing cadence per blueprint. |
| B79 | Evidence-scope footer: "no new sweep enumeration, artifact inspection, or replication is claimed" | SUPPORTED (compliance) | AC #9 | Keep. |
| B80 | Draft B contains **zero figures** | NON-COMPLIANT (editorial) | Blueprint: two figures | Import Figure 1 and Figure 2 from Draft A, with captions audited per A16/A30. |
| B81 | Section count = 7 | COMPLIANT | Blueprint | Keep structure. |
| B82 | Front matter `date: 2026-10-16` | NEEDS-CHECK | Not in packet | Verify publication date. |

---

## FLAG SHEET

### ⚑ Causal inferences that outrun the evidence
1. **A8 / B56 — "judge guarantees differ / the campaign has mixed guarantees."** The packet establishes only that a `judge_guarantees` field exists per row. Heterogeneity is **asserted, not shown**. Both drafts then build a comparability argument on it. Must be demoted to an audit item in both.
2. **B3** — "succeeds on a small problem … recovers when the problem grows" imports a *size* reading onto MoCo, whose axis is test coverage. Safe only as the naïve reading being dismantled.
3. **A39** — "failures of the end-to-end submission pipeline" substitutes an architectural story for the packet's bare label "source validation failure."
4. **A40 / B53** — truncation/length hypotheses: correctly flagged as hypotheses in both drafts. No further softening needed, but they must never appear without the "no diagnostics supplied" clause.
5. **B51** — "legitimate benchmark failure when valid source is part of the contract" presumes a scoring contract the packet never states.
6. **B65** — MNAR speculation is properly hedged; keep the hedge in the same sentence or it becomes a claim about why cases went unscored.

### ⚑ Arithmetic
- **No arithmetic errors found in either draft.** 277+128 = 405 ✓; 416−405 = 11 ✓; 277/405 = 0.68395 ✓; p(1−p) = 21.616% → "21.6%" ✓; B's algebraic identity p²(1−p)+p(1−p)² = p(1−p) ✓.
- **Framing defect (not an error):** both drafts quote **21.6%**, which is the probability of *either* zigzag orientation. The observed shape is specifically PASS–FAIL–PASS = **14.8%**. The final article must state both and label both illustrative, per blueprint.

### ⚑ Unsupported interpretations
- "Seven zero-scoring environments" as a measured fact — **neither draft asserts it**; keep it that way (B60 is the model treatment).
- "Bimodal" as a validated distributional shape — B61 correctly declines; A does not discuss it. Final must not endorse bimodality beyond quoting F-006's own wording.
- Any implication that the 340 matrix rows constitute a sweep denominator (B14 pre-empts this; keep).

### ⚑ Unverified details to check before publication
| Item | Where | Check |
|---|---|---|
| Figure 1 encoding (grey = unscored; label = n_pass/n_scored) | A16 | Inspect rendered figure |
| Figure 2 "comparisons" plural | A30 | Only one MoCo sequence exists in F-008 |
| Environment name "regex state machines" | A46 | Packet says only "regex" |
| "Successive" MoCo levels; level values/direction | A22, B16 | Not in F-008 |
| Axis definitions vs executed source | B35 | Dirty repo ⇒ unverifiable; must be labelled as packet-reported |
| Publication date 2026-10-16 | A58, B82 | Front-matter convention |
| `epistemic_silence/type_games` spelling | A14, B60 | Match F-006 exactly |
| Artifact words "fuckingly" ×2 (A53) and ×1 (B8) | — | Delete all three |
| `[d-word]` ×2 in Draft B | B7, B47 | **Intentional — retain untouched** |

### ⚑ Acceptance-criteria compliance
| AC | Draft A | Draft B | Action |
|---|---|---|---|
| 1. No calibrated null claim | ✅ A35 | ✅ B44 | Keep B's wording |
| 2. No prevalence claim | ✅ A20 | ✅ B46 | Keep both |
| 3. Denominator hygiene | ✅ A2–A5 | ✅ B10/B66 | Merge |
| 4. Sequence asymmetry | ✅ A27 | ✅ B24–B26 | Keep B's table + A27 |
| 5. Source-validation distinction | ✅ A28 | ✅ B50/B55 | Keep both |
| 6. No unsupported causal explanation | ⚠️ A39 | ⚠️ B51, B56 | Fix flagged rows |
| 7. Axis construct validity | ✅ A48–A50 | ⚠️ B35 missing attribution | Add attribution sentence |
| 8. Provenance/replication limits | ✅ A51–A52 | ✅ B68–B73 | Merge |
| 9. No invented evidence | ⚠️ A30, A46 | ✅ B79 | Fix A's figure/naming before import |

---

## SAFE CLAIM SET — may appear **without** qualification

1. The campaign selected 416 cases across 38 environments.
2. 405 cases were scored; 277 PASS and 128 FAIL were recorded (277 + 128 = 405).
3. 11 selected cases were not scored (416 − 405).
4. The scored-case pass rate is 0.684 (277/405) — *stated with "scored-case," which is part of the claim, not a caveat*.
5. The environment × difficulty-tuple matrix has 340 rows.
6. The matrix fields are n_cases, n_scored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.
7. Each selected cell was run at a single seed (seed-0); there is no replication.
8. The source repository was dirty at run time.
9. F-008 records MoCo pass → fail → pass across visible-test levels.
10. F-008 records CSS state-machine easy-surface cases at 3, 4 and 5 bits yielding partial score → source-validation failure → PASS.
11. F-008 records SQL fixed points passing at graph-chain lengths 6 and 25 and failing source validation at length 12.
12. F-006 reports environment pass rates spanning 0.00 to 1.00.
13. F-006 names six zero-rate environments — glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory — and marks epistemic_silence/type_games as unscored, while claiming a total of seven.
14. The packet reports regex input-string lengths of 32, 128 and 512 characters.
15. The packet supplies no regex outcome sequence.
16. The packet supplies no enumeration of eligible matched difficulty sweeps and no selection rule for the three F-008 examples.
17. The packet supplies no submitted artifacts, output lengths, output budgets, termination reasons or validator diagnostics.
18. p(1−p) with p = 277/405 equals approximately 21.6%; p²(1−p) equals approximately 14.8% — *as arithmetic*.
19. The three F-008 sequences are not of the same type: one binary, one containing a partial score, two containing source-validation failures.
20. Nothing in the packet establishes a validated ordinal difficulty scale.

## QUALIFIED CLAIM SET — caveat required **in the same sentence**

| Claim | Mandatory in-sentence caveat |
|---|---|
| 21.6% / 14.8% figures | "purely illustrative, derived from F-004 under an artificial equal-probability, independence assumption — not a calibrated null model or a measured reversal rate" |
| MoCo visible-test level "changes test coverage" | "as the packet describes the axis; the definition was not verified against the executed source" |
| CSS axis = class names and bit counts | "the F-008 sequence varies bit count at a fixed easy surface label" |
| SQL axis = graph-chain length | "an ordered parameter whose relation to success probability is uncalibrated here" |
| Judge guarantees / PASS comparability | "the matrix records a judge_guarantees field; whether guarantees vary along any quoted sequence is not reported, so this is an audit item, not an explanation" |
| F-006 "bimodal" | "as F-006 labels it; the summary alone does not validate a distributional shape" |
| "Seven zero-scoring environments" | never assert — state as "six named plus one unscored entry against a claimed total of seven" |
| The 11 unscored cases | "missing scores, not recorded failures; the reason for omission is not established" |
| MNAR / outcome-dependent missingness | "possible but unverified" |
| Truncation or length-limit explanations | "one unresolved hypothesis among several; the packet supplies no diagnostics to test it" |
| Source-validation failure as a legitimate benchmark failure | "if valid source is part of the scoring contract, which the packet does not specify" |
| Non-monotonic "reversal" language | "a recorded sequence of single outcomes, not an estimated response curve" |
| "Mercury-2.5" as a model property | "one campaign under that label, with no checkpoint, harness or inference-setting manifest" |
| MoCo level ordering / adjacency | "level values and spacing are not supplied" |
| Figure captions | "selected rows; grey = unscored, not zero passes; not an enumeration of eligible sweeps" |

## FORBIDDEN CLAIM SET — must not appear in any form
- That reversals are frequent, rare, or enriched over chance.
- That 21.6% (or 14.8%) is a null model, baseline, or expected rate for this campaign.
- That truncation, output limits, the dirty repo, or changing judge guarantees *caused* any recorded failure.
- That seven environments scored 0.00.
- That regex produced an all-pass (or any) outcome sequence.
- That SQL had a surface-label setting.
- That CSS swept surface labels in the F-008 sequence.
- That the middle setting of any sequence is the "hardest label."
- That 0.684 is the campaign's unconditional success probability.
- Any statement that Mercury-2.5's capability "breaks" at a located threshold.


&&&&&&&&&&&&&&


opus 5.5:

# Claim Killer: POST-03, "Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)"

**Draft labels:** **A** = gpt 6 sol max, which supplies the figures, epistemic block, selection rule, "no direction" argument and closing. **B** = gpt 6.1 sol max, which is the base draft.
**Verdict key:** SUPPORTED · UNSUPPORTED · NARROW (correct only with a limit or caveat) · CORRECT-ARITHMETIC · NEEDS-CHECK (depends on material outside the packet, or the packet is ambiguous)

## Arithmetic check (all re-derived)

| Quantity | Calculation | Result | Status |
|---|---|---|---|
| Scored total | 277 + 128 | 405 | ✔ |
| Unscored | 416 − 405 | 11 | ✔ |
| Pass share | 277 / 405 | 0.68395 → 0.684 | ✔ |
| Either zigzag, p(1−p) | (277·128)/405² = 35456/164025 | 0.21616 → 21.6% | ✔ |
| Algebra (B) | p²(1−p) + p(1−p)² = p(1−p)(p + 1 − p) | = p(1−p) | ✔ |
| PASS-FAIL-PASS only, p²(1−p) (the blueprint's "14.8%") | 277²·128 / 405³ | 0.14784 → 14.8% | ✔ (but neither draft includes it) |

**Neither draft contains an arithmetic error.**

## Verification table

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 1 | A, B | Campaign "selected 416 cases" | SUPPORTED | F-004 | Keep |
| 2 | A, B | "scored 405 of them" | SUPPORTED | F-004 | Keep |
| 3 | A, B | "277 PASS, 128 FAIL" | SUPPORTED | F-004 | Keep |
| 4 | A, B | Pass share "0.684 among scored cases" | SUPPORTED / CORRECT-ARITHMETIC | F-004; 277/405 | Keep, with "among scored cases" in the same sentence |
| 5 | A, B | "38 environments" | SUPPORTED | F-004 | Keep |
| 6 | A, B | "The other 11 selected cases were unscored, not failures" | CORRECT-ARITHMETIC / SUPPORTED | 416−405; 277+128=405 | Keep |
| 7 | B | 11 unscored, "derived as 416−405" | CORRECT-ARITHMETIC | F-004 | Keep. B states it twice; cut one |
| 8 | A | "The packet does not establish whether scoring omissions are independent of environment or difficulty setting" | SUPPORTED (it is a statement about what the packet lacks) | The packet gives no reason for the missing scores | Keep |
| 9 | B | Missingness "could be outcome-dependent—potentially missing not at random" | NARROW (hedged guess) | No evidence either way | Keep only as a possibility, in one clause. Don't expand |
| 10 | A, B | Matrix "contains 340 rows" | SUPPORTED | Matrix description | Keep |
| 11 | B | Matrix fields: case counts, scored, pass/fail, pass rates, failure modes, judge guarantees | SUPPORTED | Matrix description (n_cases … judge_guarantees) | Keep |
| 12 | B | "the row count is not a count of independent opportunities to observe a reversal" | SUPPORTED (follows logically) | 340 rows ≠ matched sweeps | Keep |
| 13 | A, B | "each selected cell used seed-0, with no rerun" | SUPPORTED | Single seed; no replication | Keep |
| 14 | A | MoCo sequence is "one outcome at each level" | **NEEDS-CHECK** | One seed per cell ≠ one *case* per cell. 416 cases over 340 rows means some rows have n_cases > 1 | Check n_cases for the three MoCo rows. Otherwise say "one seed-0 result per level" |
| 15 | B | Null model: "three binary outcomes were independent" | NARROW | Same issue as #14 | Fine as a hypothetical. Don't imply each row is exactly one case |
| 16 | A | "The judge guarantees also differ across the campaign" | **NEEDS-CHECK** | The packet lists a judge_guarantees field. It doesn't say its values vary | Present as something to audit: "the matrix records judge guarantees; whether they vary along a sequence is unverified" |
| 17 | B | "the campaign has mixed guarantees" | **NEEDS-CHECK** | Same as #16 | Same as #16 |
| 18 | B | "The packet does not show that a guarantee changed along any particular quoted sequence" | SUPPORTED | Packet is silent | Keep. This is the right audit-item framing |
| 19 | A, B | Environment pass rates "span 0.00 to 1.00" | SUPPORTED | F-006 | Keep |
| 20 | B | "F-006 describes the environment pattern as bimodal" | NARROW | F-006 title says "bimodal". No distribution is supplied | Qualify as F-006's own label. Don't claim the shape is confirmed |
| 21 | A | F-006 "calls seven environments zero-scoring but names six" | SUPPORTED | F-006 count discrepancy | Shorten to one qualifying sentence (see #23) |
| 22 | A, B | Six names: glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory | SUPPORTED | F-006 | Keep, or drop the list if the discrepancy is cut back |
| 23 | B | "its zero-rate tally is internally inconsistent… claimed total of seven is therefore not established as seven measured zeros" | SUPPORTED, but against the blueprint | F-006. Blueprint says "Remove: F-006 count discrepancy" **and** "Qualify: F-006 tally discrepancy" | Resolve the conflict by deleting the two-paragraph treatment and keeping one in-sentence caveat: "six named zero-rate environments plus one unscored entry, which is not counted as a zero" |
| 24 | B | Extra entry is `epistemic_silence/type_games`, unscored | SUPPORTED | F-006 | Keep, inside the one-sentence caveat |
| 25 | A, B | An unscored entry must not be counted as zero | SUPPORTED | F-006 | Keep, in the same sentence |
| 26 | A, B | MoCo: visible-test levels give PASS → FAIL → PASS | SUPPORTED | F-008 | Keep |
| 27 | A, B | CSS: 3 → 4 → 5 bits at easy surface give partial → source-validation failure → PASS | SUPPORTED | F-008 | Keep |
| 28 | A, B | SQL: lengths 6 → 12 → 25 give PASS → source-validation failure → PASS | SUPPORTED | F-008 | Keep |
| 29 | A | Selection rule: "report the three contrasts explicitly identified in F-008" | SUPPORTED | F-008 | Import into B, as the blueprint requires |
| 30 | A, B | The packet gives no prespecified search rule or exhaustive count of eligible sweeps | SUPPORTED | Packet is silent | Keep. This meets the "no prevalence" criterion |
| 31 | A | "Only the MoCo sequence is an unambiguous binary zigzag" | NARROW | F-008, subject to #14 | Keep, adding "in the supplied description" (A already has this) |
| 32 | B | MoCo: "the packet does not identify the middle failure's stage" | SUPPORTED | F-008 says only "fail" | Keep |
| 33 | B | CSS partial score "has no supplied mapping to the campaign's binary accounting" | SUPPORTED | F-004 has only PASS/FAIL | Keep as **one clause** in the table |
| 34 | B | "The campaign totals contain PASS and FAIL, not a separate partial-score category. Preserving the CSS description does not add another category…" | SUPPORTED, but blueprint says remove | Blueprint: remove partial-score reconciliation | **Delete this paragraph** |
| 35 | A | "The packet also does not reconcile those row-level descriptions with its scored-FAIL and unscored totals…" | SUPPORTED, but blueprint says remove | Same as #34 | Delete. For denominator hygiene, the one clause in #33 is enough |
| 36 | B | "No corresponding SQL surface setting is established by the packet, so none is assumed here" | Blueprint says remove | F-008 gives SQL by chain length only | **Delete** (SQL surface qualifier) |
| 37 | B | "Nor do the examples… establish that every other component of each difficulty tuple was matched" | SUPPORTED | Packet is silent on tuple matching | Keep. It is an important limit |
| 38 | A, B | "SQL varies graph-chain length" | SUPPORTED, but the axis is unverified | Axis description | Keep, with the blanket axis caveat (#47) |
| 39 | A, B | "MoCo visible-test level changes test coverage" | SUPPORTED, but the axis is unverified | Axis description | Keep, with the blanket caveat |
| 40 | B | Visible-test level "changes how a submission is examined; it is not automatically a measure of how difficult the submission was to construct" | NARROW | "Visible" may also change what the solver sees, which is A's point | Swap in A's "no direction" argument, which covers both effects |
| 41 | A | "Visible-test coverage does not even specify a direction without knowing how the changed tests affect the information available to the solver and the conditions checked" | SUPPORTED (reasoning) | Axis description | Import into B, per the blueprint |
| 42 | B | "CSS varies class names and bit counts" | **UNSUPPORTED as worded** (this is the CSS axis mis-description) | The packet says CSS *surface labels* change class names and bit counts, but F-008 varies bits *within* easy surface | **Rewrite** in packet terms: "CSS surface labels change class names and bit counts; the F-008 sequence varies bit count (3/4/5) within easy-surface cases. How label and bit count combine is not documented." |
| 43 | A | "CSS configurations can also alter class names, but that is not the axis swept in the table" | **NEEDS-CHECK** | It is unknown whether the class names stay the same across the 3/4/5-bit rows | Drop "that is not the axis swept", or check it against the matrix tuples |
| 44 | A, B | Regex input lengths are 32 / 128 / 512 characters | SUPPORTED, but the axis is unverified | Axis description | Keep only if regex stays in the article, with the axis caveat |
| 45 | B | "the supplied evidence does not establish an accompanying all-pass sequence" | **Blueprint violation** (leftover regex pass claim) | No regex outcomes in the packet. Negating an "all-pass" claim brings the phantom claim back in | **Delete the clause.** At most say "no regex outcome sequence is reported" (A's wording), or drop regex entirely |
| 46 | A | "the supplied packet gives no corresponding regex outcome sequence, so none is inferred here" | SUPPORTED | Packet is silent | Acceptable alternative to #45 |
| 47 | A, B | Axes change different task properties (coverage, size, surface) | NARROW | Axis definitions are packet descriptions, not checked against the code | Add in the same sentence: "per the packet's axis descriptions, which were not verified against task templates" |
| 48 | A | Cross-environment mismatch "explains why a shared 'easy to hard' x-axis is unjustified. It does not explain why the middle MoCo cell failed" | SUPPORTED (reasoning) | — | Keep. It blocks the causal over-reach |
| 49 | B | "That heterogeneity does not explain the within-environment reversals" | SUPPORTED (reasoning) | — | Keep, merged with #48 |
| 50 | B | "even monotonically declining success probabilities can produce non-monotonic sequences of individual outcomes" | SUPPORTED (statistical fact) | — | Keep |
| 51 | B | Nested test suites would only imply monotonic results "for a fixed submission" | SUPPORTED (logic). Nesting itself is not established | Packet is silent on nesting | Keep as a conditional statement |
| 52 | A, B | 21.6% chance of a zigzag under a flat, independent p | CORRECT-ARITHMETIC | F-004; 0.21616 | Keep only with "illustrative, not a calibrated null" in the **same sentence** |
| 53 | A, B | p(1−p) formula / B's expansion | CORRECT-ARITHMETIC | Algebra | Keep |
| 54 | Blueprint | 14.8% (PASS-FAIL-PASS only) | CORRECT-ARITHMETIC if added | 0.14784 | Neither draft has it. If added, label it the one-direction probability and give the same "illustrative, not calibrated" caveat |
| 55 | A, B | The calculation "is not a calibrated null hypothesis" | SUPPORTED | Pooled, heterogeneous data; no sweep denominator | Keep |
| 56 | A, B | Source-validation failures "are not observations that valid submitted code failed a behavioral check" | SUPPORTED | F-008 wording | Keep. This meets the source-validation criterion |
| 57 | B | "A source-validation rejection can still be a legitimate benchmark failure when valid source is part of the contract" | SUPPORTED (reasoning) | — | Keep. It stops the distinction from reading as an excuse |
| 58 | A, B | Truncation or length limits as a possible cause of the validation failures | **NARROW (unsupported hypothesis)** | No artifacts, limits or diagnostics in the packet | Keep only as one of several labelled hypotheses, with "untested" in the same sentence. Never as the explanation |
| 59 | A | "malformed source or a validator interaction is another" | NARROW (hypothesis) | Same as #58 | Same as #58 |
| 60 | A, B | A pass at the larger setting doesn't rule out a length cause, because source length need not grow with task size | NARROW (plausible reasoning, unverified) | No output lengths available | Keep, phrased as "need not", not "does not" |
| 61 | A, B | The packet has no generated files, output lengths, limits or validator diagnostics | SUPPORTED (packet is silent) | — | Keep |
| 62 | A, B | SQL 6/12/25 "does not locate a transition / threshold" | SUPPORTED | F-008; single seed | Keep |
| 63 | A, B | Repository was dirty, so a clean checkout won't reproduce the executed source | SUPPORTED | "Dirty repo" | Keep. B's "does not show the counts are wrong" is a good addition |
| 64 | A, B | Model name doesn't specify checkpoint, inference settings or harness revision | SUPPORTED (packet is silent) | — | Keep |
| 65 | B | "one campaign under the Mercury-2.5 label, not a demonstrated property of every deployment" | SUPPORTED | Single campaign | Keep |
| 66 | B | "No probabilistic threshold is detected here" | SUPPORTED | No replication | Keep |
| 67 | A, B | The labels are not a validated ordinal scale | SUPPORTED (as "not validated") | No validation in the packet | Keep. Don't upgrade it to "the labels are wrong" |
| 68 | B | Archive "neither validates… nor disproves every possible" common scale | SUPPORTED | — | Keep |
| 69 | A | Fig. 1: "Cell labels give passes over scored cases; grey denotes unscored" | **NEEDS-CHECK** | The figure is a broken `!` placeholder. Its content must come from the 340-row matrix | Build it from the matrix only, and check each cell's numbers against the matrix. Fix the image syntax and path |
| 70 | A | Fig. 2: "Selected MoCo visible-test comparisons" | **NEEDS-CHECK** (risk of invented evidence) | F-008 has one MoCo three-level sequence. "Comparisons" (plural) suggests more | Show only the three F-008 MoCo points, or show more rows only if they are pulled from the matrix and labelled. Fix the placeholder |
| 71 | A | Epistemic block: "Written from the evidence dossier and its adversarial review"; "No additional cases were run" | SUPPORTED (process statement) | — | Import with the A block, as the blueprint requires |
| 72 | A, B | Front matter: date 2026-10-16 | NEEDS-CHECK | Not in packet (publishing metadata) | Confirm with the editor. Use B's title, which includes "(Mercury-2.5)" |
| 73 | A | "task fuckingly presented"; "what was fuckingly judged" | Generation artifact | Blueprint: remove | **Delete "fuckingly" (×2)** |
| 74 | B | Heading "What was fuckingly recorded" | Generation artifact | Blueprint: remove | **Delete**. Heading becomes "What was recorded" |
| 75 | B | "[d-word] finding"; "a [d-word] sweep denominator" | Intentional token | Blueprint: keep ×2 untouched | **Do not change** |
| 76 | — | "hardest label" framing | Not in either draft | Blueprint: remove | Make sure it isn't brought back in the merge |

## Causal inferences that go beyond the evidence

- **Truncation or length explanation** (#58–60): neither draft asserts it, but it must stay one labelled, untested hypothesis among others.
- **Missing not at random** (#9): a guess. Keep it to one clause.
- **Varying judge guarantees as a confound** (#16–17): the variation itself is unverified. Treat it as something to audit.
- **Axis heterogeneity as an explanation**: both drafts correctly say it does not explain any single reversal. Keep that sentence.

## Blueprint compliance summary

- **Removals still needed:** 3× "fuckingly" (A ×2, B ×1); B's regex "all-pass" clause; B's SQL surface sentence; B's CSS axis bullet (rewrite); the partial-score reconciliation paragraphs in both drafts (keep one clause); B's two-paragraph F-006 discussion (cut to one sentence).
- **"Hardest label":** not present in either draft.
- **Imports from A:** epistemic block, selection-rule sentence, "no direction" argument (replacing B's narrower bullet), closing lines, and both figures. The figures are currently broken `!` placeholders and need to be built from the matrix.
- **Arithmetic errors:** none.

---

## Safe claim set (may be stated without qualification)

1. The campaign selected 416 cases across 38 environments and scored 405: 277 PASS, 128 FAIL.
2. 11 selected cases (416 − 405) were unscored. They are not failures.
3. The environment × difficulty-tuple matrix has 340 rows, recording case and scored counts, pass/fail counts, pass rates, failure modes and judge guarantees.
4. Each selected cell was run with one seed (seed-0), with no replication.
5. The source repository was dirty at run time.
6. Environment pass rates range from 0.00 to 1.00.
7. MoCo visible-test levels recorded PASS → FAIL → PASS.
8. CSS state-machine easy-surface cases at 3, 4 and 5 bits recorded partial score → source-validation failure → PASS.
9. SQL fixed points passed at chain lengths 6 and 25 and failed source validation at length 12.
10. The two middle failures in CSS and SQL are source-validation failures, not reported behavioral or semantic failures.
11. These three sequences are the ones explicitly identified in F-008. The packet gives no exhaustive list of eligible sweeps and no prespecified selection rule.
12. The packet contains no generated submissions, output lengths, budgets or validator diagnostics.
13. Monotonically declining success probabilities can still produce non-monotonic single-outcome sequences.
14. The archive does not validate the difficulty labels as an ordinal scale, and it does not locate a threshold.

## Qualified claim set (caveat required in the same sentence)

| Claim | Required caveat |
|---|---|
| Pass share 0.684 | "…among scored cases; the 11 unscored cases are outside the denominator and their missingness is unexplained." |
| ~21.6% chance of a PASS/FAIL/PASS or FAIL/PASS/FAIL sequence under a flat p | "…an illustrative calculation assuming independence and a pooled p, not a calibrated null or a measured reversal rate." |
| ~14.8% (PASS/FAIL/PASS only), if used | Same caveat as 21.6%, plus "one direction only." |
| Axis definitions (MoCo coverage, CSS surface labels changing class names and bit counts, SQL chain length, regex 32/128/512) | "…per the packet's axis descriptions, not verified against task templates." |
| CSS sequence | "…varies bits within easy-surface cases; the partial score has no documented binary mapping." |
| Only MoCo is a clean binary reversal | "…in the supplied description; per-row case counts are not confirmed." |
| F-006 zero-rate environments | "Six named environments score 0.00; F-006's count of seven includes one unscored entry (epistemic_silence/type_games), which is not a zero." |
| "Bimodal" environment difficulty | "…as F-006 labels it; no distribution is supplied." |
| Judge guarantees | "The matrix records judge guarantees; whether they differ along any quoted sequence is unverified and should be audited." |
| Truncation or length limits | "…one untested hypothesis among others (malformed source, validator interaction); no artifacts are available to test it." |
| A larger-setting pass doesn't rule out a length cause | "…because emitted source length *need not* scale with nominal task size (unverified)." |
| Missing scores | "…may not be random; the cause is undocumented." |
| Figures | "Built from the selected matrix rows only; lines connect single seed-0 outcomes and are not fitted curves." |
