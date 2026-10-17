some model:

# Claim Killer report: POST-01, "The Model's Belief Is Right; Its Decision Is Fragile" (Mercury-2.5)

**Inputs:** the evidence packet (ground truth), the Stage C blueprint, Draft A (gpt 6 sol max) and Draft B (gpt 6.1 sol max).
**Not flagged:** [ac-word], [d-word] and [m-word] are intentional and stay. Both 👹 glyphs are flagged, and in each case the slot is where [m-word] belongs.

---

## 0. Four places where the blueprint and the packet disagree

The blueprint says to remove three items as "unverified." The packet, which is the verified ground truth, states all three. One more blueprint "Add" item can't be met from the packet at all. These need a ruling from the editor before the final pass.

| # | Item | Blueprint says | Packet says | Recommendation |
|---|---|---|---|---|
| C1 | `reasoning_effort=high` | Remove | Limitations list it: "mercury-2.5, reasoning_effort=high" | Keep. The packet outranks the blueprint unless the editor has newer provenance. |
| C2 | "latent specification" | Remove | Proxy section: "76 intervention cases sharing latent spec with base" | Keep, using the packet's exact wording. |
| C3 | Game intervention types (evidence/presentation/prior) | Remove | Games entry: "base + evidence/presentation/prior interventions" | Keep the types. Don't add any claim about what each intervention did (see row 31). |
| C4 | "Add per-cell flip distribution" and "Add pre-specification of T1" | Add | **Not in the packet** | Can't be met from the evidence. Either get the data, or state plainly that it isn't available. Don't invent it. |

---

## 1. Claim-by-claim verification table (82 rows)

### 1a. T1 paired-presentation probe

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 1 | A, B | 36 matched pairs; 6 cells × 6 seeds | SUPPORTED | T1: 6 × 6 = 36 | Keep |
| 2 | A, B | Three fact counts (3, 4, 5) × two priors (1/2, 1/3) = six cells | SUPPORTED | T1 | Keep |
| 3 | A, B | One prompt uses canonical bullet order; the other reverses the facts as a numbered list | SUPPORTED | T1: "Canonical bullet order vs reversed numbered order" | Keep |
| 4 | A, B | Within a pair the facts and prior are the same | SUPPORTED | T1 name "same_fact_presentation" | Keep |
| 5 | A, B | Reported posterior identical in all 36 pairs (0/36 changed) | SUPPORTED | T1: 0/36 belief flips | Keep |
| 6 | A, B | Terminal answer changed in 5 pairs | SUPPORTED | T1: 5/36 | Keep the count. Prefer "differed" to "changed", since "changed" suggests a direction and a cause (rows 46–47). |
| 7 | A, B | All five answer changes were correctness changes (right in one presentation, wrong in the other) | SUPPORTED | T1: "all correctness flips" | Keep |
| 8 | A, B | Diagnostic choice differed in 17 pairs | SUPPORTED | T1: 17/36 | Keep |
| 9 | A, B | The diagnostic choice is about "which evidence to inspect or request next" | NEEDS-CHECK | The packet says only "diagnostic-choice divergences" and never defines the choice | Confirm the task definition. Otherwise say "diagnostic choice" without describing it. |
| 10 | A | "The model is asked for a posterior, a terminal answer, and a diagnostic choice" | SUPPORTED (implied) | All three readouts appear in T1 | Keep |
| 11 | A, B | The task has an exact oracle | SUPPORTED | T1: "Oracle is exact" | Keep |
| 12 | A | "Five of 36 is about 14%" | CORRECT-ARITHMETIC | 5/36 = 13.9% | Keep |
| 13 | A, B | "17 of 36 is about 47%" | CORRECT-ARITHMETIC | 17/36 = 47.2% | Keep |
| 14 | A | "72 presentations" | CORRECT-ARITHMETIC | 36 × 2 | Keep |
| 15 | A | "The other 31 pairs might contain two right answers or two wrong ones" | CORRECT-ARITHMETIC; logically sound | 36 − 5 = 31 | Keep |
| 16 | A | Flip counts don't give total accuracy or say which presentation was more often correct | SUPPORTED (correct non-claim) | The packet gives no per-presentation accuracy | Keep |
| 17 | A | The overlap between answer flips and diagnostic divergences isn't specified, so don't add the counts | SUPPORTED (correct non-claim) | No overlap figure in the packet | Keep |
| 18 | A | The results don't say whether any flip fell in the 4-fact, 1/3 cell | SUPPORTED (correct non-claim) | No per-cell breakdown in the packet | Keep. This is the [h-word] handling of C4. |
| 19 | B | "Nor does it mean that only one in seven changed answers was wrong" | UNSUPPORTED (garbled fraction) | 5/36 is about 1 in 7 *pairs*. Every changed answer involved a wrong answer, so the sentence contradicts itself. Blueprint: remove "one in seven." | **Delete** |
| 20 | B | "These are descriptive counts from a small probe, without confidence intervals" | SUPPORTED | Limitations: "36 pairs, no CIs" | Keep |
| 21 | A, B | The swap changes sequence *and* format, so order can't be separated from formatting | SUPPORTED | T1 design | Keep. This is a strength of both drafts. |

### 1b. Epistemic games

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 22 | A, B | 23 games; reported posterior matched the true posterior in every case | SUPPORTED | Games: 23/23 exact | Keep |
| 23 | A, B | Posterior error was zero in all 23 | SUPPORTED | Games: zero posterior error | Keep |
| 24 | A | "and the verdict was correct in all 23" | **UNSUPPORTED** | Not in the packet. Blueprint: remove. | **Delete** |
| 25 | A | "The games check posterior accuracy and verdicts" | **UNSUPPORTED** (verdict part) | Same as row 24 | Change to "check posterior accuracy" |
| 26 | A | "The games' 23 correct verdicts neither erase the five paired answer flips…" | **UNSUPPORTED** | Same as row 24 | Change to "The 23 exact posterior matches neither erase…" |
| 27 | A, B | The games cover base scenarios plus evidence, presentation and prior interventions | SUPPORTED by packet (blueprint conflict C1–C3) | Games entry | Keep pending the ruling |
| 28 | A | "*Right* is established by… 23 oracle-scored epistemic games" | NARROW | The games establish accuracy *in the games*. Nothing establishes T1 posterior correctness. A hedges this in the next sentence. | Change "established" to "supported, for a related task set" |
| 29 | A, B | The games don't show that the posteriors in the 5 flipped T1 pairs were oracle-correct | SUPPORTED (correct non-claim) | No T1 posterior-accuracy data in the packet | Keep. This is required. |
| 30 | A, B | The games and T1 are related, not independent replications; don't pool the denominators | SUPPORTED | Limitations: "No independent replication." Disjointness isn't stated anywhere. | Keep |
| 31 | B | "It was not merely stable while ignoring the task's quantities" | NEEDS-CHECK | This holds only if the evidence and prior interventions actually *changed* the true posterior. The packet doesn't say they did. | Qualify: "if the interventions altered the true posterior…", or confirm and keep |
| 32 | B | "Stated belief tracked content" | NARROW | Same dependency as row 31 | Add the qualifier in the same sentence |
| 33 | B | "Zero posterior flips is not the same as zero posterior error. A model could report the same incorrect probability twice." | SUPPORTED (logic) | Correct reasoning | **Keep.** This is the couplet the blueprint imports. |
| 34 | A | The model "can report exactly correct posteriors under varied inputs" | SUPPORTED | 23/23 under interventions | Keep |

### 1c. Proxy interventions

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 35 | A, B | Base 228/331, about 69% (0.69) | SUPPORTED; CORRECT-ARITHMETIC | 228/331 = 0.689 | Keep |
| 36 | A | "Among **scored** base cases, 228 of 331" | NEEDS-CHECK | The packet doesn't say 331 means scored. It's plausible, but see row 42. | Confirm, or drop "scored" |
| 37 | A, B | Visible-proxy 8/27, about 30% (0.30) | SUPPORTED; CORRECT-ARITHMETIC | 8/27 = 0.296 | Keep |
| 38 | A, B | Reward-proxy 1/4 = 25% | SUPPORTED; CORRECT-ARITHMETIC | Packet | Keep |
| 39 | A, B | 7 pass→fail among 76 intervention cases sharing a latent spec with base | SUPPORTED | Packet | Keep (C2) |
| 40 | A, B | 4 of the 7 carried the visible-proxy tag | SUPPORTED | Packet | Keep |
| 41 | A, B | No fail→pass count is given, so 7/76 isn't a probability that passes turn into fails | SUPPORTED (correct non-claim) | Packet gives one direction only | Keep. Don't print 7/76 = 9.2% as a rate. |
| 42 | — (neither) | Category accounting: 331 + 27 + 4 = 362 of 405 scored, leaving **43 cases uncategorized**. Also 405 − 331 = 74 scored non-base cases, but the paired subset is **76**. | NEEDS-CHECK | Arithmetic on packet numbers. The 76 must include unscored cases, or the categories overlap. | Reconcile before publishing. B's "no complete crosswalk" covers this qualitatively; neither draft quantifies it. |
| 43 | A, B | Intervention cases aren't difficulty-matched to base cases | SUPPORTED | Limitations | Keep |
| 44 | B | "The differences are substantial in these observations" | NARROW | Descriptive only: no CIs, n = 4 and n = 27, confounded | Add "descriptively" or "before accounting for difficulty" in the same sentence |
| 45 | A, B | The proxy results aren't a second measurement of the T1 dissociation | SUPPORTED (correct non-claim) | Different endpoints | Keep. Both drafts do this well. |

### 1d. Causal inferences and interpretation (main risk area)

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 46 | A | "'Presentation sensitivity' is therefore the [d-word] description" | NARROW (causal claim goes beyond the evidence) | **There is no sampling-noise null.** The packet has no same-presentation re-run baseline. If each presentation is independently right with probability p, pairs differ in correctness with probability 2p(1−p). At p ≈ 0.925 that is 0.139, which is exactly 5/36. Noise alone could produce the observed count. | Add the null in the same paragraph. Say "differences between presentations", not "sensitivity to presentation", unless a re-run baseline exists. |
| 47 | B | "It therefore establishes sensitivity to that bundled presentation change" | NARROW (causal) | Same as row 46 | Change "establishes sensitivity" to "shows differences under" and add the noise caveat |
| 48 | B | "This endpoint establishes sensitivity, not seventeen additional failures" (diagnostic) | NARROW (causal) | **No chance-agreement baseline.** With k equally likely options, random divergence is 1 − 1/k. For k = 2 that is 50%, or 18/36, and 17/36 is at chance. k isn't in the packet. | Change to "divergence" and add the chance-agreement caveat |
| 49 | A | Diagnostic divergence is "choice variability, not a 17-of-36 error rate" | SUPPORTED (non-claim) but incomplete | Same chance issue as row 48 | Keep, and add the chance baseline |
| 50 | B | "There is a behavioral dissociation here" | NARROW | It's a dissociation only if the answer variation isn't explained by sampling noise or extraction (rows 46, 60) | Keep the thesis (the blueprint adopts it), with the noise and extraction caveats in the same paragraph |
| 51 | A, B | 0/36 posterior flips presented as meaningful invariance | NARROW | **Floor effect.** The model gets posteriors exactly right in 23/23 games. If computing the posterior is easy for it, invariance is expected, which makes it weak evidence of robustness. | Add the floor-effect framing (blueprint "Add") |
| 52 | A | "The answer is not determined by the reported posterior in a presentation-invariant way" | NARROW | Logically valid from the outputs: same posterior, different answers. It depends on extraction being correct, and **the packet never defines how the answer should follow from the posterior.** | Keep, plus the extraction caveat and a statement that the answer–posterior relationship is undefined |
| 53 | B | "Nor does it establish that the reported posterior is what determines the terminal answer" | SUPPORTED (correct non-claim) | No relationship defined | Keep. It meets part of the blueprint "Add". |
| 54 | A | "The posterior's invariance makes a simple 'it received different evidence' account less satisfying" | NARROW | Weakened by the floor effect (row 51) | Hedge with the floor effect |
| 55 | A, B | Identical reported posteriors don't prove identical parsing or internal computation; no "belief module" or "decision module" | SUPPORTED (correct non-claim) | The probe records outputs only | Keep. The "outputs, not modules" heading comes from B. |
| 56 | B | "The reported posterior stayed fixed while the terminal answer sometimes crossed **from correct to incorrect**" | NARROW | The packet gives no direction (canonical→reversed or the reverse) | Change to "differed in correctness between presentations" |
| 57 | B | "A posterior-only account would have missed **real** correctness reversals" | NARROW | "Real" overstates, given possibly brittle extraction | Change to "recorded" |
| 58 | B | "Specific outputs have different stability properties" | NARROW | Not established without a noise null | Add "in this probe, before a re-run baseline" |
| 59 | Title | "The Model's Belief Is Right; Its Decision Is Fragile" | NARROW | "Right" isn't established for the T1 posteriors. "Fragile" assumes the variation isn't noise. | Keep the title (blueprint). The first section must define "belief" as the stated posterior and limit "right" to the games. A does this best. |
| 60 | A, B | Terminal-answer extraction may be brittle | SUPPORTED | Limitations | Keep. Both handle it well. |
| 61 | A | "An exact oracle tells us which answer is correct if the recorded answer is what the model gave" | SUPPORTED (logic) | Oracle exact plus extraction caveat | Keep |
| 62 | — (neither) | T1 was pre-specified | NEEDS-CHECK | Not in the packet (C4) | Get the status, or write "whether T1 was pre-specified isn't recorded in the available results" |

### 1e. Campaign and provenance

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 63 | A, B | 416 selected | SUPPORTED | Campaign | Keep |
| 64 | A, B | "across **38 environments**" | **UNSUPPORTED** | Not in the packet. Blueprint: remove. | **Delete** from both |
| 65 | A, B | 405 scored, 11 unscored | SUPPORTED; CORRECT-ARITHMETIC | 405 + 11 = 416 | Keep |
| 66 | A, B | 277 PASS, 128 FAIL | SUPPORTED; CORRECT-ARITHMETIC | 277 + 128 = 405 | Keep |
| 67 | A, B | Pass fraction 68.4% (0.684) | CORRECT-ARITHMETIC | 277/405 = 0.6840 | Keep |
| 68 | A, B | 189 behavioral-reference + 227 compile-only = **416 selected, not 405 scored** | SUPPORTED; CORRECT-ARITHMETIC | Campaign. Blueprint: don't attach to 405. | Keep. Both attach it correctly. |
| 69 | B | The guarantees "partition the selected cases" | SUPPORTED | The sum equals 416 exactly | Keep |
| 70 | A, B | 56 of 132 twin cases unverified | SUPPORTED | Campaign | Keep |
| 71 | B | "about 42%" | CORRECT-ARITHMETIC | 56/132 = 42.4% | Keep |
| 72 | A | Twin cases can't be treated as "fully checked replications" | NEEDS-CHECK | The packet doesn't define twin cases as replications | Change to "can't be treated as verified" |
| 73 | A, B | Single seed per selected cell in the main campaign | SUPPORTED | Campaign | Keep |
| 74 | A, B | The T1 probe used six seeds per cell, distinct from the campaign | SUPPORTED | T1 vs campaign | Keep |
| 75 | B | "Campaign-wide single-seed results do not establish run-to-run stability" | SUPPORTED (logic) | Single seed | Keep. It's a natural place to raise the noise null. |
| 76 | A, B | Repo dirty at run time; this doesn't by itself show contamination | SUPPORTED; hedge correct | Campaign | Keep |
| 77 | A, B | Single model/provider; no independent replication | SUPPORTED | Limitations | Keep |
| 78 | A, B | mercury-2.5 with reasoning effort high | SUPPORTED by packet (blueprint conflict C1) | Limitations | Keep pending the ruling |

### 1f. Production and figures

| # | Draft | Item | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 79 | A | 👹 in "the very examples where it 👹" | Production artifact | Blueprint: remove the glyph | Replace with [m-word] |
| 80 | B | 👹 in "The distinction 👹 because" | Production artifact | Same | Replace with [m-word] |
| 81 | A | Figure 1 SVG: 360 px = 36 pairs, bars 0, 50 and 170 px | CORRECT-ARITHMETIC | 10 px per pair matches 0/5/17 | Keep as Figure 1 (blueprint) |
| 82 | B | "!" placeholder labeled "Figure 1" (campaign) | Broken, and the numbering is wrong | Blueprint: Figure 1 = endpoints, Figure 2 = campaign denominators | Build a new Figure 2 SVG: 416 → 405 scored (277 P / 128 F) + 11 unscored; separate bar 416 = 189 BR + 227 CO. Caption must tie the guarantees to 416. |

**Checked and absent:** "pass rates from 0.00 to 1.00" doesn't appear in either draft. Neither draft misattaches the judge guarantees to 405.

---

## 2. Blueprint "Add" items: where the drafts stand

| Add item | A | B | What the final article needs |
|---|---|---|---|
| Sampling-noise null | Missing | Missing (row 75 comes close) | Required. Include the 2p(1−p) illustration, clearly labeled as hypothetical, since per-presentation accuracy and decoding temperature aren't known. |
| Chance agreement for diagnostic choices | Missing | Missing | Required. Note that the number of options k is unknown, and that k = 2 gives about 18/36 by chance. |
| Posterior invariance as a floor effect | Missing | Partial (row 33) | Required |
| Answer–posterior relationship undefined | Partial (row 52) | Yes (row 53) | Use B's sentence |
| Per-cell flip distribution | Says the data isn't available (row 18) | Missing | Not in the packet. Get it, or state that it's unavailable. |
| T1 pre-specification | Missing | Missing | Not in the packet. Get it, or state that it's unknown. |

---

## 3. Safe claim set (can be stated without qualification)

1. The paired probe had 36 matched pairs: 3 fact counts (3, 4, 5) × 2 priors (1/2, 1/3) = 6 cells, with 6 seeds each.
2. Within each pair the facts and prior were identical. One presentation used canonical bullet order and the other reversed the facts as a numbered list.
3. The task has an exact oracle.
4. The reported posterior was identical across presentations in 36 of 36 pairs.
5. The recorded terminal answer differed in 5 of 36 pairs (about 14%), and each of the five was a correctness difference.
6. The diagnostic choice differed in 17 of 36 pairs (about 47%).
7. In 23 epistemic-game cases, the reported posterior equaled the true posterior every time, with zero posterior error.
8. Base cases passed 228/331 (0.69), visible-proxy 8/27 (0.30), reward-proxy 1/4 (0.25).
9. Among 76 intervention cases sharing a latent specification with a base case, 7 were recorded as pass→fail, 4 of them visible-proxy.
10. The campaign selected 416 cases. 405 were scored (277 PASS, 128 FAIL, 0.684) and 11 were unscored.
11. 189 behavioral-reference + 227 compile-only = 416 selected cases (not 405).
12. 56 of 132 twin cases are unverified (about 42%).
13. The main campaign used a single seed per selected cell, and the repository was dirty at run time.
14. Everything comes from one model and provider configuration (mercury-2.5, reasoning_effort=high, pending ruling C1), with no independent replication.
15. Zero posterior flips is not the same as zero posterior error.
16. The order-plus-format swap can't separate order effects from formatting effects.

## 4. Qualified claim set (the caveat goes in the same sentence)

1. **The behavioral dissociation:** the stated posterior was invariant while recorded answers differed in 5 pairs, *but there's no same-presentation re-run baseline, and sampling noise alone could produce a count this size.*
2. **"Presentation" as the cause of answer differences:** *only as differences observed between presentations, not shown to be caused by presentation, absent a noise null.*
3. **Diagnostic divergence (17/36):** *divergence, not error, and not shown to exceed chance, because the number of options isn't known.*
4. **Posterior invariance:** *could reflect a floor effect, given that posteriors were exactly right in 23/23 games.*
5. **"Right" in the title:** *supported for the 23 games only. T1 posterior correctness, including in the five flipped pairs, isn't established.*
6. **Same posterior, different answer, so the answer isn't a function of the posterior alone:** *assuming extraction was correct, and noting that the expected answer–posterior relationship isn't defined.*
7. **The five correctness flips:** *as recorded under the existing extraction procedure, which may be brittle.*
8. **Stated belief "tracked content" (B):** *only if the evidence and prior interventions changed the true posterior, which the packet doesn't confirm.*
9. **Proxy-tagged cases passed less often:** *descriptively, without difficulty matching, with n = 4 for reward-proxy and an unreconciled category accounting (43 uncategorized scored cases; 76 vs 74).*
10. **7 pass→fail of 76:** *one direction only, not a transition probability.*
11. **The dirty repo:** *a provenance caveat, not evidence of contamination.*
12. **T1 per-cell distribution and pre-specification:** *not available in the recorded results.*

## 5. Deletions (unsupported or garbled)

- "verdict correct in all 23" and both follow-ons (A: rows 24–26)
- "across 38 environments" (A and B: row 64)
- "only one in seven changed answers was wrong" (B: row 19)
- Both 👹 glyphs, replaced with [m-word] (rows 79–80)
- B's "!" figure placeholder, replaced with a new Figure 2 SVG (row 82)

&&&&&&&&&&&&&&&&&&&&&&


fable 5.1:

# Claim Killer Report — POST-01 (Mercury-2.5)

**Verification basis:** every claim checked against the Evidence Packet only. Blueprint decisions are treated as editorial constraints, not as evidence. Where the packet and the blueprint disagree, I say so explicitly rather than silently siding with either.

**Arithmetic re-computed:** 5/36 = 0.139; 17/36 = 0.472; 228/331 = 0.689; 8/27 = 0.296; 1/4 = 0.25; 277/405 = 0.6840; 277+128 = 405; 405+11 = 416; 189+227 = 416; 56/132 = 0.424; 3×2×6 = 36; 36×2 = 72; 36−5 = 31; 331+27+4 = 362 (≠ 405); 27+4 = 31 (< 76). All arithmetic in both drafts is correct; the only numerical problem is one garbled fraction (row 27).

---

## Section 1 — Front matter and framing

| # | Draft | Claim (as written) | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 1 | A, B | Title: "The Model's Belief Is Right; Its Decision Is Fragile" | NARROW | "Right" is supported only by epistemic games (23/23); T1 does not score posterior correctness. "Decision" connotes a mechanism; packet records outputs only. | Keep title; both drafts already de-fuse it in the opening. Ensure the operational definition of "belief" and the games/T1 split appear within the first two paragraphs of the final. |
| 2 | A, B | date 2026-10-16; author StrangeTcy | NEEDS-CHECK | Not in packet (metadata). | Editor confirms. |
| 3 | A | "The reported counts are specific; the interpretation is bounded by 36 matched pairs, possible extraction errors, and no independent replication." | SUPPORTED | Limitations: 36 pairs, no CIs; extraction may be brittle; no replication. | Keep. |
| 4 | B | "One model and provider configuration. The presentation probe has 36 matched pairs and no confidence intervals. Proxy comparisons are not difficulty-matched." | SUPPORTED | Limitations block, verbatim. | Keep (import into A's epistemic-status if A is base). |
| 5 | A | "Written from verified aggregate results, without access to individual prompt-and-response transcripts" | NEEDS-CHECK | Consistent with packet (aggregates only) but the author's access is a process claim. | Editor confirms. |
| 6 | B | "AI-drafted from the archived evidence; no new measurements or independent replication." | SUPPORTED (process) / NEEDS-CHECK (AI-drafted disclosure) | No replication is in packet. | Editor decides disclosure wording. |

## Section 2 — T1 paired-presentation probe

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 7 | A, B | 36 matched pairs | SUPPORTED | T1: 6 cells × 6 seeds = 36. | Keep. |
| 8 | A, B | 0/36 reported-posterior flips | SUPPORTED | T1: 0/36 belief flips. | Keep. |
| 9 | A, B | 5/36 terminal-answer flips | SUPPORTED | T1: 5/36. | Keep. |
| 10 | A, B | All 5 answer flips were correctness flips (one right, one wrong) | SUPPORTED | T1: "all correctness flips." | Keep. |
| 11 | A, B | 17/36 diagnostic-choice divergences | SUPPORTED | T1: 17/36. | Keep. |
| 12 | A, B | Three fact counts (3, 4, 5) × two priors (1/2, 1/3) = 6 cells | SUPPORTED + CORRECT-ARITHMETIC | T1 design line. | Keep. |
| 13 | A, B | Six seeds per cell | SUPPORTED | T1. | Keep. |
| 14 | A, B | Canonical bullet order vs. reversed numbered order | SUPPORTED | T1. | Keep. |
| 15 | A, B | Oracle is exact | SUPPORTED | T1: "Oracle is exact." | Keep. |
| 16 | A, B | Diagnostic choice = "which evidence to inspect or request next" | NEEDS-CHECK | Packet says only "diagnostic-choice divergences"; the inspect/request gloss is not in the packet. | Either verify against the probe spec or reduce to "a diagnostic choice (which evidence to examine next)" flagged as paraphrase. Do not describe the choice menu. |
| 17 | A | "Five of 36 is about 14%; 17 of 36 is about 47%" | CORRECT-ARITHMETIC | 0.139, 0.472. | Keep, with "descriptive, no CI" caveat (both drafts have it). |
| 18 | B | "approximately 14%" / "approximately 47%" | CORRECT-ARITHMETIC | Same. | Keep. |
| 19 | A | "Nor should the two counts be added: the available results do not specify how answer flips and diagnostic-choice divergences overlap." | SUPPORTED (absence) | Packet gives no overlap/joint table. | Keep. This is a required caveat. |
| 20 | A | "The results available to me do not say whether any of the five answer flips occurred in that particular cell." | SUPPORTED (absence) | No per-cell breakdown in packet. | Keep. Satisfies blueprint "per-cell flip distribution" only as a statement of absence — the final cannot add numbers. |
| 21 | A | "That does not tell us the model's total answer accuracy across all 72 presentations." | SUPPORTED + CORRECT-ARITHMETIC | 36×2 = 72; packet gives no accuracy total. | Keep. |
| 22 | A | "The other 31 pairs might contain two right answers or two wrong ones" | SUPPORTED + CORRECT-ARITHMETIC | 36−5 = 31; packet silent on non-flipped pairs' correctness. | Keep. |
| 23 | A, B | "It does not tell us whether the canonical or reversed version was more often correct." | SUPPORTED (absence) | No direction-of-flip data in packet. | Keep. |
| 24 | A, B | Manipulation changes both order and format; cannot isolate order from numbering | SUPPORTED (design inference) | T1: bullet-canonical vs numbered-reversed — two features co-vary. | Keep. Prefer "presentation sensitivity" over "order sensitivity" throughout. |
| 25 | A, B | A different diagnostic choice is not necessarily a wrong choice; 17/36 is not an error rate | SUPPORTED (absence) | Packet scores diagnostic choices only as divergences, not correctness. | Keep. |
| 26 | B | T1 three-endpoint table | SUPPORTED | Matches packet exactly. | Import into final per blueprint. |
| 27 | B | "nor does it mean that only one in seven changed answers was wrong" | UNSUPPORTED / GARBLED | 5/36 ≈ 1/7 of *pairs* changed; "one in seven changed answers was wrong" is not a meaningful quantity. Blueprint flags for removal. | **Delete the clause.** Keep "not a 14% overall error rate." |
| 28 | A | Figure 1 SVG: bar widths 50 px (5) and 170 px (17) on a 360 px = 36-pair axis | CORRECT-ARITHMETIC | 10 px/pair. | Keep. |
| 29 | A | Figure 1 desc/caption: "All five answer changes changed correctness … the counts do not establish which presentation was better overall." | SUPPORTED | T1. | Keep. |
| 30 | A | "Mercury-2.5 did not always oblige" / "I would have expected so" | NARROW (rhetorical) | Framing, not a claim. | Keep. |
| 31 | — | Sampling-noise null (would answer flip between two seeds under the *same* presentation?) | ABSENT in both drafts | Packet contains no same-presentation repeat comparison; blueprint requires adding it. | **Add** a sentence: the probe lacks a same-presentation re-run baseline, so the 5 flips cannot be distinguished from within-condition sampling variability without a null comparison. |
| 32 | — | Chance agreement for diagnostic choices | ABSENT in both drafts | Packet does not give the size of the choice set; blueprint requires adding. | **Add**: without the number of available diagnostic options, the expected divergence rate under independent sampling is unknown; 17/36 cannot be compared to chance. |
| 33 | — | Posterior invariance as a floor effect | ABSENT in both drafts | Blueprint requires. The oracle is exact and the games show 23/23 exact matches — a posterior that is simply computed correctly every time will trivially be invariant. | **Add**: 0/36 may reflect that the posterior is an easy, deterministic computation, not robustness per se. |
| 34 | — | Answer–posterior relationship undefined | PARTIAL in A ("the answer is not determined by the reported posterior in a presentation-invariant way") | Packet does not specify whether the terminal answer is supposed to be a function of the posterior (e.g., a threshold decision). | **Add** explicitly: the task spec available here does not define how the terminal answer should relate to the posterior, so "belief vs decision" is a labelling of two outputs, not a tested functional link. |
| 35 | — | Pre-specification of T1 | ABSENT in both drafts | Packet silent. | **Add** one sentence: whether T1's cells, seeds, and endpoints were fixed before running is not recorded in the evidence available here. |

## Section 3 — Interpretation of the dissociation

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 36 | A | "At minimum, the answer is not determined by the reported posterior in a presentation-invariant way in this task." | SUPPORTED (logical) | Same reported posterior + different answer ⇒ answer is not a function of reported posterior alone. | Keep, but pair with row 34. |
| 37 | A, B | Identical reported posteriors do not prove identical parsing / internal representations / a belief module + decision module | SUPPORTED (as a limitation) | Packet records outputs only. | Keep. Core of the "outputs not modules" thesis. |
| 38 | A | "Different processing paths could produce the same stated number." | NARROW (speculative, hedged "could") | No internal data in packet. | Keep only as hedged possibility; do not elevate. |
| 39 | A | "The posterior's invariance makes a simple 'it received different evidence' account less satisfying" | NARROW (inference) | Reasonable: a mis-parsed fact set would ordinarily change the posterior — but see row 33: an easy posterior could be robust to partial mis-parsing. | Keep with "less satisfying," not "rules out." |
| 40 | A, B | Terminal-answer extraction may be brittle; exact oracle does not validate the extractor | SUPPORTED | Limitations: "Terminal-answer extraction may be brittle." | Keep. Required caveat on the 5 flips. |
| 41 | B | "Perhaps the model forms the same internal belief and uses it inconsistently." | NARROW (explicitly labelled as the tempting over-reach) | Not asserted. | Keep as foil only. |
| 42 | B | "Zero posterior flips is not the same as zero posterior error." | SUPPORTED (logical couplet) | Packet: T1 measures flips; games measure error. | Import into final per blueprint. |
| 43 | A, B | Posterior in the 5 flipped pairs is not established to be oracle-correct | SUPPORTED (absence) | T1 reports no posterior-correctness scoring. | Keep. Must be in the same paragraph as any use of "right." |
| 44 | B | "It was not merely stable while ignoring the task's quantities." | NARROW — risk of cross-contamination | True of the 23 games; reads as if it were true of T1. | Rephrase: "In the games, it was not merely stable…" |
| 45 | A | "A probability report may also conceal distinctions that matter to a later answer." | NARROW (hedged) | No evidence either way. | Keep as "may." |

## Section 4 — Epistemic games

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 46 | A, B | 23/23 exact posterior match; posterior_reported = posterior_true; zero posterior error | SUPPORTED | Epistemic games line. | Keep. |
| 47 | A, B | Games span base + evidence / presentation / prior interventions | SUPPORTED BY PACKET — **BLUEPRINT CONFLICT** | Packet: "base + evidence/presentation/prior interventions." Blueprint: remove "game intervention types (unverified)." | Editor must reconcile. Conservative path: write "base scenarios and several intervention types" without naming them. Nothing essential is lost. |
| 48 | A | "…and the verdict was correct in all 23." | UNSUPPORTED | Packet records posterior match only; no verdict field. Blueprint flags removal. | **Delete.** Also delete A's later "verdicts" in "The games check posterior accuracy and verdicts" and "The games' 23 correct verdicts." |
| 49 | A | "oracle-scored epistemic games" | SUPPORTED (paraphrase) | posterior_true implies oracle. | Keep. |
| 50 | A, B | Games are not an independent replication of T1; disjointness of cases/procedures not established | SUPPORTED (absence) | Packet lists them as separate measurements; no overlap info. | Keep. |
| 51 | A, B | Do not add 23 and 36 into one denominator | SUPPORTED (methodological) | Different endpoints. | Keep. |
| 52 | B | "A *related* epistemic-game suite" | NARROW | Relation = same campaign/packet; procedural relation not specified. | Keep "related" only in the sense of "from the same campaign." |

## Section 5 — Proxy interventions

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 53 | A, B | Base 228/331 ≈ 0.69 | SUPPORTED + CORRECT-ARITHMETIC | Proxy line. | Keep. |
| 54 | A, B | Visible proxy 8/27 ≈ 0.30 | SUPPORTED + CORRECT-ARITHMETIC | Proxy line. | Keep. |
| 55 | A, B | Reward proxy 1/4 = 0.25 | SUPPORTED + CORRECT-ARITHMETIC | Proxy line. | Keep. |
| 56 | B | Table header "Passing / scored" | NEEDS-CHECK (minor) | Packet gives 228/331 but does not label 331 as "scored base." Note 331+27+4 = 362 ≠ 405, so these categories do not partition the scored set. | Keep header; add footnote that categories are non-exhaustive (both drafts already say this in prose). |
| 57 | A, B | 7 pass→fail transitions among 76 intervention cases sharing latent spec with base; 4 of 7 visible-proxy | SUPPORTED | Proxy line. | Keep numbers. |
| 58 | A, B | Term "latent specification" | SUPPORTED BY PACKET — **BLUEPRINT CONFLICT** | Packet: "sharing latent spec with base." Blueprint: remove "latent specification (unverified)." | Editor must reconcile. Conservative path: "76 intervention cases paired with a base case by shared specification." |
| 59 | A, B | Not difficulty-matched; difficulty could explain part or all of the gap | SUPPORTED | Limitations. | Keep. Required caveat in same sentence as any pass-rate comparison. |
| 60 | A | "The packet does not provide a corresponding fail→pass count or the number of paired base cases that passed. Seven out of 76 is therefore not an estimated probability…" | SUPPORTED (absence) + valid inference | Only pass→fail direction given. | Keep. |
| 61 | B | "Nor does this directional count supply a complete account of all paired transitions." | SUPPORTED (absence) | Same. | Keep. |
| 62 | A, B | Four reward-proxy cases are too few for fine comparison | SUPPORTED (n=4) | Proxy line. | Keep. |
| 63 | A, B | Intervention taxonomy incomplete; no crosswalk between types, proxy categories, and the 76-case subset | SUPPORTED (absence) | 27+4 = 31 < 76, so other intervention types exist but are unnamed. | Keep. |
| 64 | A, B | Proxy results do not measure the T1 dissociation; cannot explain the 5 flips | SUPPORTED (methodological) | Proxy cases carry pass/fail only. | Keep. |
| 65 | B | "The differences are substantial in these observations." | NARROW | No CI; n=4 and n=27. | Keep only with "in these observations… also confounded" (B has this). |
| 66 | B | Sharing a latent spec "does not, by itself, hold difficulty … constant" | SUPPORTED | Limitations. | Keep. |

## Section 6 — Campaign coverage

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 67 | A, B | 416 selected; 405 scored; 277 PASS; 128 FAIL; 0.684; 11 unscored | SUPPORTED + CORRECT-ARITHMETIC | Campaign line. 277+128 = 405; 405+11 = 416; 277/405 = 0.684. | Keep. |
| 68 | A, B | "across 38 environments" | UNSUPPORTED | Not in packet. Blueprint flags removal. | **Delete** from both. |
| 69 | A, B | 189 behavioral_reference + 227 compile_only = 416 (selected, not scored) | SUPPORTED + CORRECT-ARITHMETIC | Campaign line. Both drafts correctly attach to 416. | Keep. Blueprint's "misattached to 405" error is absent from both drafts — confirmed. |
| 70 | A, B | Single seed per selected cell (campaign) vs six seeds per cell (T1) | SUPPORTED | Campaign + T1 lines. | Keep. |
| 71 | B | "Campaign-wide single-seed results do not establish run-to-run stability." | SUPPORTED (inference) | Single seed ⇒ no within-cell variance estimate. | Keep. |
| 72 | A, B | 56 of 132 twin cases unverified | SUPPORTED | Campaign line. | Keep. |
| 73 | B | "about 42%" | CORRECT-ARITHMETIC | 56/132 = 0.424. | Keep. |
| 74 | B | "These are cases, not 56 unverified groups" | SUPPORTED | Packet says "twin cases." | Keep. |
| 75 | A, B | Repo dirty at run time; this alone does not show a result was contaminated | SUPPORTED + hedged inference | Campaign line "Dirty repo." | Keep. |
| 76 | A | "A commit identifier alone might therefore be insufficient to reconstruct the exact working tree" | NARROW (hedged) | Follows from "dirty." | Keep as "might." |
| 77 | A, B | mercury-2.5 with reasoning_effort=high | SUPPORTED BY PACKET — **BLUEPRINT CONFLICT** | Packet Limitations: "(mercury-2.5, reasoning_effort=high)." Blueprint: remove "reasoning effort high (unverified)." | Editor must reconcile. Conservative path: "one model and one provider configuration (mercury-2.5)." |
| 78 | A, B | No independent replication | SUPPORTED | Limitations. | Keep. |
| 79 | A | "its 36 pairs should not be silently treated as 36 representative draws from the 405 scored campaign cases" | SUPPORTED (methodological) + NEEDS-CHECK | Packet does not state whether T1 cases are inside or outside the 405. | Keep; add "whether T1 is counted within the 405 is not specified here." |
| 80 | B | Figure 1 rendered as "!" | BROKEN ARTIFACT | Blueprint requires a new campaign-denominators SVG (Figure 2 in final). | **Replace** with SVG: 416 → 405 scored (277/128) + 11 unscored; 416 → 189 + 227 judge guarantees as a parallel partition. |
| 81 | B | Figure caption: judge guarantees "partition the selected cases; … not a breakdown restricted to scored cases" | SUPPORTED | 189+227 = 416. | Keep as the Figure 2 caption. |
| 82 | — | "pass rates from 0.00 to 1.00" | ABSENT (confirmed) | Blueprint flagged; neither draft contains it. | No action; do not reintroduce. |

## Section 7 — Next tests and conclusions

| # | Draft | Claim | Verdict | Evidence | Required action |
|---|---|---|---|---|---|
| 83 | A, B | Proposed follow-ups: audit the 5 flipped pairs' raw responses blind to presentation; factor order × format; more seeds; second model; difficulty-matched proxy comparison with both transition directions | SUPPORTED (as proposals — each targets a packet-listed gap) | Limitations. | Keep. |
| 84 | A | "Was the reported probability both unchanged and correct when the answer changed?" | SUPPORTED (as the open question) | T1 lacks posterior-correctness scoring. | Keep. |
| 85 | A, B | Closing: unchanged stated posterior did not guarantee unchanged terminal answer | SUPPORTED | T1: 0/36 vs 5/36. | Keep — this is the safe thesis sentence. |
| 86 | A, B | "They do not tell me what internal mechanism produced the gap" / "not enough to tell us which internal mechanism failed" | SUPPORTED (limitation) | Outputs only. | Keep. |
| 87 | B | "A posterior-only summary would have missed real correctness reversals under the recorded scoring procedure." | SUPPORTED | T1; "under the recorded scoring procedure" correctly carries the extraction caveat. | Keep. |
| 88 | A, B | 👹 glyph ("where it 👹" / "The distinction 👹 because") | ARTIFACT | Blueprint: remove. The slot is where "matters" would go. | **Replace** with `[m-word]` (a kept, intentional token) or restructure the sentence. |
| 89 | A, B | `[ac-word]`, `[d-word]` tokens | INTENTIONAL | Per instructions. | Do not touch. |

---

## Packet ↔ Blueprint conflicts requiring an editorial ruling

Three items the blueprint labels "unverified" are literally present in the packet labelled "verified ground truth":

1. **reasoning_effort=high** (row 77) — packet Limitations line.
2. **latent spec** (row 58) — packet Proxy line.
3. **evidence / presentation / prior intervention types for the games** (row 47) — packet Epistemic games line.

I cannot resolve this from the materials given. If the blueprint's flags postdate the packet (i.e., a later verification pass found these fields unsupported in the raw logs), follow the blueprint. If the packet postdates the blueprint, the claims are usable. **Recommendation:** remove all three regardless — none is load-bearing for the thesis, and the article is strictly safer without them. If the editor keeps them, cite the packet line.

---

## Safe claim set (may be stated without in-sentence qualification)

1. In 36 matched pairs (3 fact counts × 2 priors × 6 seeds), the reported posterior was identical across the two presentations in 0 pairs' worth of change — 0/36 flips.
2. The terminal answer differed in 5/36 pairs.
3. All 5 terminal-answer differences were correctness flips under an exact oracle.
4. The diagnostic choice differed in 17/36 pairs.
5. The two presentations were canonical bullet order vs. reversed numbered order (two co-varying features).
6. In 23 epistemic-game cases, posterior_reported equalled posterior_true in every case (zero posterior error).
7. Pass counts: base 228/331; visible-proxy 8/27; reward-proxy 1/4.
8. Among 76 intervention cases paired with a base case, 7 were pass→fail; 4 of those 7 were visible-proxy.
9. Campaign: 416 selected, 405 scored (277 PASS / 128 FAIL, 0.684), 11 unscored.
10. Judge guarantees 189 behavioral_reference + 227 compile_only = 416 selected cases.
11. Campaign used a single seed per selected cell; T1 used six seeds per cell.
12. 56 of 132 twin cases are unverified.
13. The repository was dirty at run time; there is no independent replication; T1 has no confidence intervals; intervention cases are not difficulty-matched; terminal-answer extraction may be brittle.
14. The arithmetic: 5/36 ≈ 14%, 17/36 ≈ 47%, 56/132 ≈ 42%.
15. An unchanged reported posterior did not guarantee an unchanged terminal answer in this probe.

## Qualified claim set (caveat must appear in the same sentence)

| Claim | Required in-sentence caveat |
|---|---|
| "The model's belief is right" | …*in the 23 epistemic games*; T1 did not score posterior correctness, including in the 5 flipped pairs. |
| "Its decision is fragile" | …*as a behavioral output*; no internal decision mechanism is identified. |
| Posterior invariance is informative | …but may be a floor effect for an exactly computable quantity. |
| 5 flips are correctness reversals | …*under the recorded extraction and scoring procedure*, which is not independently audited. |
| 17/36 diagnostic divergence | …is sensitivity, not error; no chance-agreement baseline is available. |
| 5/36 and 17/36 as percentages | …descriptive of this probe only; no CI; the two counts cannot be added or assumed to overlap. |
| Proxy-tagged cases pass less often | …in a comparison that is not difficulty-matched and where the categories are non-exhaustive. |
| 7/76 pass→fail | …one direction only; fail→pass and the number of passing paired bases are not reported, so this is not a transition probability. |
| Reward-proxy 0.25 | …n = 4. |
| 0.684 campaign pass rate | …pools two judge-guarantee types and says nothing about posterior accuracy or presentation robustness. |
| "Presentation sensitivity" | …order and format co-vary; neither is isolated. |
| Games corroborate T1 | …they are related campaign evidence with different endpoints, not an independent replication, and case overlap is unspecified. |
| Dirty repo | …a provenance caveat, not evidence that any result was contaminated. |
| T1 vs. campaign relationship | …whether T1's 36 pairs are inside the 405 scored cases is not specified. |
| Pre-specification | …whether T1's design was fixed in advance is not recorded in the available evidence. |

## Mandatory deletions / replacements for the final

- "verdict was correct in all 23" and both later uses of "verdicts" (A).
- "38 environments" (A and B).
- "nor does it mean that only one in seven changed answers was wrong" (B).
- 👹 glyph → `[m-word]` (A and B).
- B's "!" figure → new campaign-denominators SVG.
- Row 44 rephrase (B) so the games' accuracy is not read onto T1.
- Pending editor ruling: "reasoning effort high," "latent specification," named game intervention types (rows 47, 58, 77).
- Additions required by blueprint and absent from both drafts: sampling-noise null, chance agreement for diagnostic choices, floor-effect note, answer–posterior relationship undefined, per-cell distribution stated as unavailable, pre-specification not recorded (rows 31–35).

&&&&&&&&&&&&&&&&&&&&&&&


gpt 6 sol max:

## Verification basis

This is a **packet-only audit**. “Unsupported” means *not established by the supplied ground truth*, not necessarily false. Repeated statements within a draft are covered together. Evidence keys: **T1** = paired-presentation probe; **Games** = 23 epistemic games; **Proxy** = proxy interventions; **Campaign** = campaign totals and judge guarantees; **Limits** = stated limitations; **Blueprint** = accepted editorial decisions.

There is a conflict to resolve rather than conceal: the packet explicitly gives `reasoning_effort=high`, names the game-intervention types, and says the 76 intervention cases shared a latent specification with a base case. The blueprint nevertheless orders those details removed as “unverified.” They are **supported by this packet**, but the final article should follow the removal decision unless the editor reconciles the discrepancy.

### Draft A — gpt 6 sol max

| # | Claim as written | Verdict | Evidence source | Required action for final article |
|---:|---|---|---|---|
| A1 | “The Model's Belief Is Right; Its Decision Is Fragile” | NARROW | Games establishes accuracy in 23 cases; T1 establishes flips in different observations. | If retained, explain immediately that *belief* means a reported posterior and that its accuracy is **not established for the five flipped T1 pairs**. |
| A2 | `date: 2026-10-16` | NEEDS-CHECK | No publication metadata in packet. | Confirm publication date editorially. |
| A3 | “by … StrangeTcy” | NEEDS-CHECK | No authorship record in packet. | Confirm attribution. |
| A4 | “a narrow dissociation between a stated posterior and the responses given alongside it” | SUPPORTED | T1: 0 belief flips; 5 answer flips; 17 diagnostic divergences. | Keep as a **behavioral, recorded-output** dissociation, not a claim about internal components. |
| A5 | “Draws on the archived paired probe, epistemic games, proxy-intervention results, and campaign coverage. These are treated as distinct measurements.” | NARROW | The four results are in the packet; “archived” provenance is not. | Keep the distinction; delete or verify “archived.” |
| A6 | “Written from verified aggregate results, without access to individual prompt-and-response transcripts for this essay.” | NEEDS-CHECK | The supplied packet contains aggregates, not transcripts; the writer’s access is unknown. | Say “The supplied packet does not include individual transcripts,” unless access is verified. |
| A7 | “bounded by 36 matched pairs, possible extraction errors, and no independent replication” | SUPPORTED | T1; Limits. | Keep. |
| A8 | “A stable probability report did not guarantee a stable answer in this probe.” | SUPPORTED | T1: 0 recorded belief flips alongside 5 answer flips. | Keep “in this probe”; do not infer a general decision mechanism. |
| A9 | “a task with an exact oracle” | SUPPORTED | T1: oracle is exact. | Keep for T1; do not silently extend this guarantee to other scoring procedures. |
| A10 | “In 36 matched pairs, its reported posterior was identical across the two presentations in every pair.” | SUPPORTED | T1: 36 pairs, 0 belief flips. | Describe the **recorded belief/posterior endpoint**; add that zero flips is a floor, not an accuracy check. |
| A11 | “Its terminal answer changed in five pairs. Each of those five changes was also a correctness change” | SUPPORTED | T1: 5/36 answer flips, all correctness flips. | Keep as **recorded/scored** answer changes; retain the extraction caveat. |
| A12 | “one presentation elicited the right answer and the other the wrong one” | SUPPORTED | T1 exact oracle and all five correctness flips. | Keep for the recorded answers, conditional on faithful extraction. |
| A13 | “Its choice of what evidence to inspect or request next differed in 17 pairs.” | NARROW | T1 verifies 17 *diagnostic-choice* divergences, not the precise content of the choices. | Say “diagnostic choice differed”; verify the prompts before specifying inspection or requests. |
| A14 | “*Belief* means the posterior the model stated, not an internal state I can inspect.” | SUPPORTED | Operational distinction consistent with T1 and Games. | Keep prominently. |
| A15 | “*Right* is established by a related set of 23 oracle-scored epistemic games, in which every reported posterior matched the true posterior.” | NARROW | Games: 23/23 exact matches; T1 alone explicitly guarantees an exact oracle. | Say “In 23 epistemic games, reported and true posteriors matched”; do not use this to certify T1’s five pairs or assume identical oracle procedures. |
| A16 | “does **not** tell me that the stated posterior was oracle-correct in each of the five paired-presentation trials whose answers flipped” | SUPPORTED | T1 gives flips, not pair-level posterior-versus-truth results. | Keep. |
| A17 | “three fact counts—three, four, and five—with two priors, 1/2 and 1/3. That makes six cells, each tested with six seeds: 36 matched pairs.” | SUPPORTED | T1: 3 × 2 cells; 6 seeds each. | Keep. |
| A18 | “Within a pair, the facts and prior stay the same. One prompt puts the facts in a canonical bullet order; the other reverses them in a numbered list.” | SUPPORTED | T1 presentation definition. | Keep. |
| A19 | “The model is asked for a posterior, a terminal answer, and a diagnostic choice about which evidence to inspect or request next.” | NEEDS-CHECK | T1 identifies measured endpoints, not the exact wording or structure of the prompt. | Say the probe **records** three endpoints; verify prompts before saying what was asked. |
| A20 | “With four facts and a prior of 1/3, each of its six pairs compares two presentations of those same four facts.” | SUPPORTED | T1 crossed cells and six seeds. | Keep as an illustrative cell, not a reconstructed transcript. |
| A21 | “The results available to me do not say whether any of the five answer flips occurred in that particular cell.” | SUPPORTED | T1 supplies no per-cell flip distribution. | Keep; request the distribution for the final analysis if available. |
| A22 | “It changes **both sequence and format**” | SUPPORTED | T1: canonical bullets versus reversed numbered items. | Keep. |
| A23 | “cannot, by itself, assign the difference specifically to position in the list rather than numbering, or to an interaction” | SUPPORTED | T1 bundles order and format. | Keep; also acknowledge an unmeasured same-prompt sampling-noise baseline. |
| A24 | Figure 1’s “0/36,” “5/36,” and “17/36” bars | CORRECT-ARITHMETIC | T1; drawn widths are 0, 50 and 170 pixels out of 360, exactly proportional to 0, 5 and 17 out of 36. | Keep Figure 1 and its endpoint labels. |
| A25 | “A different diagnostic choice is not necessarily an incorrect choice.” | SUPPORTED | T1 reports divergence, not diagnostic correctness. | Keep; add that chance agreement and the choice-set baseline are unknown. |
| A26 | “the counts do not establish which presentation was better overall” | SUPPORTED | T1 gives no direction of the five correctness flips or total accuracy by condition. | Keep. |
| A27 | “Five of 36 is about 14% of these pairs; 17 of 36 is about 47%.” | CORRECT-ARITHMETIC | T1: 13.89% and 47.22%. | Keep as sample descriptions. |
| A28 | “not estimates of how often Mercury-2.5 would err on arbitrary problems” | SUPPORTED | T1’s limited sample, endpoints and absence of CIs. | Keep; a flip fraction is not an overall error rate. |
| A29 | “the available results do not specify how answer flips and diagnostic-choice divergences overlap” | SUPPORTED | No pair-level overlap in T1 packet. | Keep; do not add the counts. |
| A30 | “total answer accuracy across all 72 presentations” is unknown | CORRECT-ARITHMETIC | T1: 36 pairs × 2 presentations = 72; accuracy totals absent. | Keep. |
| A31 | “It does not tell us whether the canonical or reversed version was more often correct.” | SUPPORTED | T1 gives no flip directions. | Keep. |
| A32 | “The other 31 pairs might contain two right answers or two wrong ones” | CORRECT-ARITHMETIC | 36 − 5 = 31; unchanged answers to the same oracle-scored problem have the same correctness. | Keep as a possibility, not a reported breakdown. |
| A33 | “a changed answer as evidence that the model had read different facts. But that explanation predicts more than the observations show.” | UNSUPPORTED | T1 has no internal-reading measure; an unchanged reported posterior could coexist with different parsing or readout. | Remove the purported prediction. Say internal readings cannot be determined. |
| A34 | “the answer is not determined by the reported posterior in a presentation-invariant way in this task” | NARROW | T1 observes identical reported values with different answers; it does **not** specify the answer–posterior rule or measure same-prompt variability. | Say the reported posterior **did not uniquely predict the recorded answer in these pairs**; do not assert a causal presentation effect or failed decision rule. |
| A35 | “The two endpoints need not travel together.” | SUPPORTED | T1’s three endpoint counts. | Keep as an observation about these outputs. |
| A36 | “Identical reported posteriors do not prove identical parsing, identical intermediate calculations, or a discrete ‘belief module’” | SUPPORTED | T1 measures outputs, not internal states. | Keep. |
| A37 | “Different processing paths could produce the same stated number. A probability report may also conceal distinctions” | NARROW | Plausible alternatives, not measured by T1. | Keep explicitly as possibilities, not findings. |
| A38 | “This experiment records outputs; it does not locate a failure inside the computation.” | SUPPORTED | T1 design and Limits. | Keep. |
| A39 | “Terminal-answer extraction may be brittle.” | SUPPORTED | Limits explicitly identifies this possibility. | Keep “may”; do not claim extraction actually failed. |
| A40 | “An exact oracle tells us which answer is correct **if the recorded answer is what the model gave**.” | SUPPORTED | T1 exact oracle; Limits extraction caveat. | Keep. |
| A41 | “Without the individual transcripts here, I cannot adjudicate that possibility” | NARROW | No transcripts in packet; the writer’s other access is unknown. | Say “The supplied packet does not permit an extraction audit.” |
| A42 | “The posterior’s invariance makes a simple ‘it received different evidence’ account less satisfying” | NARROW | T1 holds *prompted* facts fixed but does not test internal parsing; zero flips could mask differences. | Remove the evidential ranking or state it as an intuition, not a ruled-out explanation. |
| A43 | “it does not rule out readout artifacts or subtler presentation effects” | SUPPORTED | Limits and T1’s bundled manipulation. | Keep, with “possible” for presentation effects. |
| A44 | “evidence of **choice variability**, not a 17-of-36 diagnostic error rate” | SUPPORTED | T1 reports 17 divergences without choice correctness. | Keep; add the missing chance-agreement/repeat baseline. |
| A45 | “23 cases spanning base scenarios and evidence, presentation, and prior interventions” | SUPPORTED | Games explicitly lists these interventions. | **Editorial conflict:** blueprint orders the intervention-type detail removed; omit unless reconciled. |
| A46 | “`posterior_reported` equaled `posterior_true` every time. Posterior error was zero in all 23” | SUPPORTED | Games: 23/23 exact matches, zero error. | Keep, restricted to the 23 cases. |
| A47 | “the verdict was correct in all 23”; “The games’ 23 correct verdicts” | UNSUPPORTED | Games reports posterior accuracy only; no verdict count. Blueprint explicitly rejects this claim. | Delete both occurrences and any implication that game verdicts were verified. |
| A48 | “its stated probability tracked the oracle despite the tested variations” | NARROW | Games confirms 23 exact matches; neither the range of true values nor a mechanism of tracking is supplied. | Say “matched the true posterior in those 23 cases.” |
| A49 | “I cannot treat the 23 games as an independent replication of the 36 pairs”; their cases or procedures are not established as disjoint | SUPPORTED | Limits: no independent replication; packet gives no disjointness record. | Keep; never pool 23 and 36. |
| A50 | “The games check posterior accuracy and verdicts on their tested scenarios” | UNSUPPORTED | Games verifies posterior accuracy, not verdicts. | Remove “and verdicts.” |
| A51 | “Adding their denominators would manufacture a single experiment that was never run.” | SUPPORTED | T1 and Games have different reported endpoints and units. | Keep. |
| A52 | “Among scored base cases, 228 of 331 passed, about 69%.” | CORRECT-ARITHMETIC | Proxy: 228/331 = 68.88%. | Keep “recorded base cases”; do not infer comparability of case difficulty. |
| A53 | “**visible-proxy**, 8 of 27 passed, about 30%; … **reward-proxy**, 1 of 4 passed, 25%.” | CORRECT-ARITHMETIC | Proxy: 29.63% and 25%. | Keep the denominators, especially the four-case reward group. |
| A54 | “seven of 76 were recorded as a passing base case becoming a failing intervention case. Four of those seven carry the visible-proxy tag.” | SUPPORTED | Proxy: seven pass→fail among 76 base-linked cases; four visible-proxy. | Keep directional wording. Blueprint orders “latent specification” terminology removed despite packet support. |
| A55 | “A pass on a proxy-intervention case is not interchangeable with a stable posterior, a terminal-answer flip, or a diagnostic-choice divergence.” | SUPPORTED | Proxy records pass/fail; T1 records three other endpoints. | Keep; no single “decision-layer” explanation. |
| A56 | “Intervention and base cases are **not difficulty-matched**.” | SUPPORTED | Proxy limitation. | Keep in the same discussion as the rate comparison. |
| A57 | “Sharing a latent specification does not guarantee equal task difficulty.” | SUPPORTED | Proxy says shared specification and not difficulty-matched. | Keep the inference if needed; resolve blueprint’s terminology-removal instruction. |
| A58 | “the packet does not provide a corresponding fail→pass count or the number of paired base cases that passed. Seven out of 76 is therefore not an estimated probability that a passing base case will fail” | SUPPORTED | Proxy supplies only seven directional transitions among all 76 intervention cases. | Keep; **76 is not the number of base cases that passed**. |
| A59 | “Four reward-proxy cases … are too few to support a fine comparison” | NARROW | Proxy n = 4; precision was not measured. | Keep as a caution, not a numerical significance claim. |
| A60 | “The intervention taxonomy is incomplete in the evidence available here.” | SUPPORTED | Proxy packet supplies labels and counts, not a full taxonomy or crosswalk. | Keep the restriction “in the evidence available here”; do not assert the underlying study lacked one. |
| A61 | “They are not, on their own, a causal estimate of a proxy’s effect” | SUPPORTED | Proxy groups are not difficulty-matched. | Keep. |
| A62 | “selected 416 cases” | SUPPORTED | Campaign selected = 416. | Keep. |
| A63 | “across 38 environments” | UNSUPPORTED | No environment count in packet; blueprint explicitly rejects 38. | Delete. |
| A64 | “405 were scored: 277 PASS and 128 FAIL, for a recorded pass fraction of 68.4%. Eleven were unscored.” | CORRECT-ARITHMETIC | Campaign: 277 + 128 = 405; 277/405 = 0.68395; 416 − 405 = 11. | Keep with the **405 scored** denominator. |
| A65 | “189 *behavioral-reference* cases and 227 *compile-only* cases. Those categories sum to **416 selected cases**, not 405 scored cases.” | CORRECT-ARITHMETIC | Campaign judge guarantees: 189 + 227 = 416. | Keep; use these only as a selected-case split. |
| A66 | “I should not attach the guarantee split to the scored denominator” or treat the pooled PASS fraction as one uniform check | SUPPORTED | Campaign gives no guarantee-by-scored-case crosswalk. | Keep. |
| A67 | “56 of 132 twin cases unverified” | SUPPORTED | Campaign. | Keep as *cases*, not unverified groups or verified replications. |
| A68 | “single seed per selected cell”; paired probe “six seeds in each of its six cells” | SUPPORTED | Campaign; T1. | Keep the designs distinct; do not call T1 a representative subsample of 405. |
| A69 | “The source repository was dirty at run time. A commit identifier alone might therefore be insufficient to reconstruct the exact working tree” | NARROW | Campaign says “dirty repo”; no timestamp, commit record, or affected-file inventory. | Say “The repository was marked dirty; commit-only provenance may be insufficient.” Do not imply changed files affected results. |
| A70 | “‘dirty’ does not establish that a relevant file changed during execution or that any outcome was contaminated” | SUPPORTED | Campaign supplies no such incident. | Keep. |
| A71 | “There is no independent replication on a second model or provider configuration.” | SUPPORTED | Limits: single model/provider; no independent replication. | Keep. |
| A72 | “mercury-2.5 with reasoning effort set to high” | SUPPORTED | Limits explicitly says `mercury-2.5, reasoning_effort=high`. | **Editorial conflict:** blueprint orders “reasoning effort high” removed; omit pending reconciliation, not because packet contradicts it. |
| A73 | “That would test … *Was the reported probability both unchanged and correct when the answer changed?*” | SUPPORTED | T1 accuracy on the five pairs is unreported; proposed audit addresses it. | Keep as a **proposed test**, not a present finding; obtain pair-level truth and raw responses. |
| A74 | “Repeating those comparisons across more seeds would show … whether one component accounts for them.” | NARROW | Current T1 bundles factors; Limits gives no same-prompt repeat baseline. | Add repeated **identical-prompt** runs and a factorial order × format comparison before attributing flips to a component. |
| A75 | “In a controlled 36-pair presentation probe” | NARROW | T1 matches facts/prior, but sampling noise, order and format are not separately controlled. | Prefer “matched 36-pair probe”; avoid implying a measured causal effect. |
| A76 | “Together these findings make me unwilling to infer a stable answer from a stable stated probability.” | NARROW | T1 alone establishes the observed mismatch; Proxy is a different endpoint. | Ground this conclusion in T1, not in a presumed common proxy mechanism. |
| A77 | “They do not tell me what internal mechanism produced the gap—or whether the gap will survive the next … test.” | SUPPORTED | Limits; no replication or mechanistic measurement. | Keep. |

**A production fixes:** Remove the 👹 glyph. Keep intentional bracketed tokens. Figure 1’s data and SVG bar arithmetic check out; add the blueprint’s **Figure 2 campaign-denominators SVG**. Neither figure should imply that the judge-guarantee split applies only to the 405 scored cases.

### Draft B — gpt 6.1 sol max

| # | Claim as written | Verdict | Evidence source | Required action for final article |
|---:|---|---|---|---|
| B1 | “The Model's Belief Is Right; Its Decision Is Fragile” | NARROW | Games verifies posterior accuracy; T1 verifies answer variability, not posterior accuracy in its five flipped pairs. | Apply A1’s immediate operational qualification. |
| B2 | `date: 2026-10-16`; “by … StrangeTcy” | NEEDS-CHECK | No publication or authorship metadata in packet. | Confirm date and attribution. |
| B3 | “AI-drafted from the archived evidence; no new measurements or independent replication.” | NARROW | The drafts are AI candidates; Limits says no independent replication; archival status and complete provenance are not documented. | Say “Drafted from the supplied aggregate packet; no independent replication.” Verify any stronger provenance claim. |
| B4 | “One model and provider configuration. The presentation probe has 36 matched pairs and no confidence intervals. Proxy comparisons are not difficulty-matched.” | SUPPORTED | Limits; T1; Proxy. | Keep. |
| B5 | “A posterior-only summary would miss observed terminal-answer correctness reversals.” | SUPPORTED | T1: 0 belief flips and 5 recorded correctness flips. | Keep “observed/recorded”; do not infer their internal cause. |
| B6 | “the same probability under two presentations of the same facts, yet gives a correct answer in one presentation and an incorrect answer in the other” | SUPPORTED | T1 exact oracle and correctness flips. | Specify that this is the **recorded** result, subject to extraction audit. |
| B7 | “it knew the answer but failed to use it” | UNSUPPORTED | Neither T1 nor Games observes internal knowledge or establishes a posterior-to-answer rule. | It is explicitly introduced and rejected as an instinct; **do not promote it into a finding**. |
| B8 | “In a 36-pair presentation probe, Mercury-2.5’s reported posterior never changed … terminal answer changed in five pairs … diagnostic choices changed in seventeen.” | SUPPORTED | T1: 0/36, 5/36, 17/36. | Keep as recorded endpoint counts; repeat the answer-extraction caveat. |
| B9 | “a behavioral dissociation here: the measured belief output was invariant while other outputs were not” | SUPPORTED | T1. | Keep “measured” and “behavioral”; do not call it proof of distinct modules or a causal format effect. |
| B10 | “campaign-level proxy interventions show lower pass rates than base cases” | SUPPORTED | Proxy: 8/27 and 1/4 versus 228/331. | Keep **observed rates**, alongside the difficulty confound. |
| B11 | “three fact counts—3, 4, and 5—with two priors—1/2 and 1/3. That makes six cells, with six seeds per cell: 36 matched pairs.” | SUPPORTED | T1. | Keep. |
| B12 | “One presentation uses canonical bullet order. The other reverses the facts and presents them as a numbered list.” | SUPPORTED | T1. | Keep; facts and prior are fixed within a pair. |
| B13 | “The model supplies an elicited posterior, a terminal answer, and diagnostic choices about which evidence to inspect or request next.” | NEEDS-CHECK | T1 verifies endpoints, not the precise request or choice wording. | Name the recorded endpoints; verify prompts before describing choice content. |
| B14 | Table: “Reported posterior \| 0/36 \| No observed posterior sensitivity” | NARROW | T1 verifies **zero recorded flips**, not insensitivity of latent belief or a tested causal null. | Replace explanation with “No recorded reported-belief change”; note the zero-flip floor. |
| B15 | Table: “Terminal answer \| 5/36 \| Five correctness reversals” | SUPPORTED | T1. | Keep as recorded/scored reversals. |
| B16 | Table: “Diagnostic choices \| 17/36 \| Different evidence-selection choices, not necessarily worse ones” | NARROW | T1 verifies 17 divergences and no error count; “evidence-selection” detail is unverified. | Say “Different diagnostic choices, not necessarily errors”; add chance-agreement baseline caveat. |
| B17 | “The task has an exact oracle, and all five answer flips were correctness flips” | SUPPORTED | T1 exact oracle; all five correctness flips. | Keep, without treating the oracle as validation of answer extraction. |
| B18 | “Five of 36 is approximately 14% of the observed pairs.” | CORRECT-ARITHMETIC | T1: 5/36 = 13.89%. | Keep as the observed **flip fraction**, not error rate. |
| B19 | “That is **not** a 14% overall error rate” | SUPPORTED | T1 lacks total answer accuracy across 72 presentations. | Keep. |
| B20 | “nor does it mean that only one in seven changed answers was wrong” | UNSUPPORTED | **Denominator/logic error:** about one in seven *pairs* flipped; each flipped pair has one recorded right and one wrong answer. Blueprint rejects this wording. | Delete the sentence fragment; retain B19 and B21. |
| B21 | “The flip counts alone do not tell us the overall accuracy of either presentation.” | SUPPORTED | T1 lacks nonflipped-pair correctness and flip directions. | Keep. |
| B22 | “Seventeen pairs—approximately 47%” | CORRECT-ARITHMETIC | T1: 17/36 = 47.22%. | Keep as an observed divergence fraction. |
| B23 | “Two requests could be equally useful” | NARROW | T1 supplies no utility scores or diagnostic choice-set definition. | Keep only as a **possibility**, not an assessment that the observed alternatives were equal. |
| B24 | “This endpoint establishes sensitivity, not seventeen additional failures.” | NARROW | T1 establishes divergence, not diagnostic failures; causal sensitivity is unseparated from sampling noise. | Say “records 17 divergences, not 17 established errors.” |
| B25 | “The comparison changes both order and list format” and “does not isolate an order effect from a formatting effect” | SUPPORTED | T1 presentation definitions. | Keep. |
| B26 | “It therefore establishes sensitivity to that bundled presentation change.” | NARROW | T1 has paired different presentations but no identical-prompt repeat/noise baseline. | Say divergences were **observed across** the bundled change; a causal effect is not yet isolated. |
| B27 | “descriptive counts from a small probe, without confidence intervals … not estimates with demonstrated precision across arbitrary prompts or tasks” | SUPPORTED | T1 n = 36; Limits says no CIs and no independent replication. | Keep. |
| B28 | “the reported posterior stayed fixed **while** the terminal answer sometimes crossed from correct to incorrect” | SUPPORTED | T1 recorded endpoints and exact oracle. | Keep as an observed conjunction, with extraction caveat. |
| B29 | “If I retained only the posterior column, I would lose that conjunction.” | SUPPORTED | T1’s distinct endpoint counts. | Keep. |
| B30 | “It does not establish a sequence in which the model first computes a belief and then passes it to a distinct decision mechanism.” | SUPPORTED | T1 does not observe computation. | Keep. |
| B31 | “Perhaps the model forms the same internal belief and uses it inconsistently.” | UNSUPPORTED | No internal-belief measure; answer–posterior relationship undefined. | Keep, if at all, as the **explicitly rejected hypothesis** it is in B; never assert it. |
| B32 | “equality of reported numbers does not establish equality of internal representations, interpretation, or computation” | SUPPORTED | T1 records reports only. | Keep. |
| B33 | “Nor does it establish that the reported posterior is what determines the terminal answer.” | SUPPORTED | Packet provides no answer–posterior decision rule. | Keep; state this missing relationship explicitly. |
| B34 | “I cannot rule out parsing explanations merely because the posterior did not move.” | SUPPORTED | T1; Limits. | Keep. |
| B35 | “An exact oracle settles the mathematical target; it does not, by itself, validate the procedure that extracts an answer from generated text.” | SUPPORTED | T1 oracle; Limits extraction caveat. | Keep. |
| B36 | “The recorded result is five correctness flips under the existing extraction and scoring procedure.” | SUPPORTED | T1. | Keep this careful formulation. |
| B37 | “posterior reporting and terminal-answer correctness behaved differently … [but] cannot locate the cause ‘downstream of belief’” | SUPPORTED | T1 observed endpoints; no mechanistic evidence. | Keep as behavioral observation plus limitation. |
| B38 | “Zero posterior flips is not the same as zero posterior error.” | SUPPORTED | T1 checks invariance; Games separately checks accuracy. | Keep. |
| B39 | “Across 23 cases—including base scenarios and evidence, presentation, and prior interventions” | SUPPORTED | Games explicitly lists those types. | **Editorial conflict:** omit type list per blueprint unless reconciled. |
| B40 | “the reported posterior exactly matched the true posterior in every case. Posterior error was zero throughout that set.” | SUPPORTED | Games: 23/23, zero error. | Keep, scoped to those 23 cases. |
| B41 | “stated belief tracked content: under the tested evidence and prior conditions, the model reported the oracle posterior” | NARROW | Games establishes exact matches, but supplies no distribution of true values or process evidence; exact-oracle guarantee is explicit for T1. | Say “reported posteriors matched the true posteriors in the 23 tested cases.” |
| B42 | “It was not merely stable while ignoring the task’s quantities.” | UNSUPPORTED | Games gives no posterior values, variation range or internal method; accurate reports alone do not establish *how* they arose. | Delete. |
| B43 | “The presentation probe establishes posterior **invariance** … The epistemic games establish posterior **accuracy**” | SUPPORTED | T1 versus Games. | Keep those endpoints and denominators separate. |
| B44 | “invariance alone does not establish that every posterior in the presentation probe was correct” | SUPPORTED | No T1 pair-level accuracy breakdown. | Keep; especially for the five flipped pairs. |
| B45 | “The title uses ‘belief’ operationally, to mean an elicited posterior—not privileged access to a hidden belief state.” | SUPPORTED | Measured endpoints only. | Keep near the title. |
| B46 | “not independent replications”; “Their different units should not be added” | SUPPORTED | Limits; T1 and Games measure different questions. | Keep. |
| B47 | “The 23 exact matches make accurate posterior reporting an observed capability here; they do not independently replicate the five terminal correctness reversals.” | SUPPORTED | Games 23/23; T1 5/36; no independent replication. | Keep “here,” not a general capability guarantee. |
| B48 | “Specific outputs have different stability properties” | NARROW | T1 reports different flip counts, but no repeat baseline or population stability estimate. | Say “the recorded outputs had different flip counts in this probe.” |
| B49 | Table: “Base \| 228/331 \| 0.69” | CORRECT-ARITHMETIC | Proxy: 228/331 = 0.68882. | Keep as rounded observed rate. |
| B50 | Table: “Visible proxy \| 8/27 \| 0.30” | CORRECT-ARITHMETIC | Proxy: 8/27 = 0.29630. | Keep as rounded observed rate. |
| B51 | Table: “Reward proxy \| 1/4 \| 0.25” | CORRECT-ARITHMETIC | Proxy: 1/4 = 0.25. | Keep n = 4 visible. |
| B52 | “The differences are substantial in these observations. They are also confounded.” | NARROW | Proxy rates differ descriptively; groups are not difficulty-matched. | “Substantial” may describe the sample gap, not a precise or causal effect. |
| B53 | “Differences in difficulty could explain part or all of the pass-rate gap.” | NARROW | Proxy establishes lack of difficulty matching, not the actual explanation. | Retain as a **possibility**, not a demonstrated cause. |
| B54 | “The reward-proxy category has only four cases” | SUPPORTED | Proxy: 1/4. | Keep; avoid fine comparisons or precision claims. |
| B55 | “Among 76 intervention cases sharing a latent specification with a base case, seven changed a passing base result into a failure. Four of those seven carried the visible-proxy tag.” | SUPPORTED | Proxy gives precisely these counts and linkage. | Keep pass→fail direction; blueprint orders latent-specification wording removed pending reconciliation. |
| B56 | “Sharing a latent specification … does not, by itself, hold difficulty or every other relevant feature constant.” | SUPPORTED | Proxy says cases are not difficulty-matched. | Keep caution; follow the blueprint’s terminology decision. |
| B57 | “this directional count [does not] supply a complete account of all paired transitions” | SUPPORTED | Proxy gives no fail→pass count or full transition table. | Keep; do not turn 7/76 into a conditional failure probability. |
| B58 | “available counts do not provide a complete crosswalk … [or] an exhaustive partition” | SUPPORTED | Proxy packet lacks category/subset crosswalk. | Keep “available counts”; do not assert no crosswalk exists elsewhere. |
| B59 | “The proxy results do not show an unchanged posterior paired with a changed terminal decision.” | NARROW | Proxy packet reports pass/fail, not that posterior–answer pair; it does not establish what was never measured elsewhere. | Say “The **supplied proxy results do not report** such a paired measurement.” |
| B60 | “Calling it further evidence for one fragile ‘decision layer’ would make the narrative smoother by making the evidence less faithful.” | SUPPORTED | Proxy and T1 measure distinct endpoints; no internal layer is observed. | Keep the substantive caution. |
| B61 | “selected 416 cases” | SUPPORTED | Campaign. | Keep. |
| B62 | “across 38 environments” | UNSUPPORTED | No environment count in packet; blueprint rejects it. | Delete. |
| B63 | “405 were scored and 11 were unscored. The scored cases contain 277 passes and 128 failures, for an aggregate pass rate of 0.684.” | CORRECT-ARITHMETIC | Campaign: 277 + 128 = 405; 277/405 = 0.68395; 416 − 405 = 11. | Keep the scored denominator. |
| B64 | “not a posterior-accuracy estimate, a presentation-sensitivity estimate, or an estimate of a proxy effect” | SUPPORTED | Campaign PASS pools checks; distinct endpoints lack a common denominator. | Keep. |
| B65 | “189 cases labeled behavioral-reference and 227 labeled compile-only. Those counts sum to **416 selected cases**, not 405 scored cases.” | CORRECT-ARITHMETIC | Campaign judge guarantees: 189 + 227 = 416. | Keep; do not attach them to scored cases. |
| B66 | “judge guarantees partition the selected cases; they are not a breakdown restricted to scored cases” | SUPPORTED | Campaign specifies the 416 selected-case guarantee split. | Keep the denominator explicit. |
| B67 | `!` followed by “*Figure 1. Campaign coverage.*” | NEEDS-CHECK | B contains a placeholder, not a figure; Blueprint specifies Figure 1 for T1 and Figure 2 for denominators. | Replace `!` with **Figure 1: three T1 endpoints SVG**, then **Figure 2: campaign-denominators SVG**; renumber caption. |
| B68 | “Different judge guarantees are another reason not to turn the aggregate pass rate into a general statement about ‘reasoning.’” | SUPPORTED | Campaign has behavioral-reference and compile-only checks, without scored-case crosswalk. | Keep; do not infer equivalent validation across cases. |
| B69 | “broader campaign used a single seed per selected cell … presentation probe’s six seeds per cell”; single-seed results do not establish run-to-run stability | SUPPORTED | Campaign; T1; Limits. | Keep designs distinct; request identical-prompt repeats for the noise null. |
| B70 | “56 unverified twin cases out of 132—about 42%. These are cases, not 56 unverified groups” | CORRECT-ARITHMETIC | Campaign: 56/132 = 42.42%; unit is cases. | Keep; do not equate the remaining 76 twin cases with the *separate* 76 intervention cases without evidence. |
| B71 | “`mercury-2.5` with high reasoning effort” | SUPPORTED | Limits explicitly supplies model and effort. | **Editorial conflict:** omit effort setting pending reconciliation; keep the single-model limitation. |
| B72 | “There is no independent replication.” | SUPPORTED | Limits. | Keep. |
| B73 | “The source repository was dirty at run time”; that alone does not establish any result is invalid | NARROW | Campaign says “dirty repo,” without timestamp or affected-file history; no invalidation is shown. | Say “repository was marked dirty”; retain the non-invalidation caution. |
| B74 | “A comparison that independently varies fact order and list format could distinguish sensitivity to order, formatting, and their combination.” | NARROW | T1 currently bundles both. | Keep as a **proposed** factorial test; add identical-prompt repeats to separate presentation effects from sampling noise. |
| B75 | “If those reversals survive an extraction audit, the behavioral interpretation becomes firmer.” | SUPPORTED | Limits identifies extraction brittleness as possible. | Keep as a conditional proposal, not an audit result. |
| B76 | “If the hypothesis concerns a dissociation … under proxy cues, then both endpoints need to be elicited and scored in that same controlled comparison.” | SUPPORTED | Proxy packet lacks T1-style paired posterior/answer results. | Keep as a study-design proposal. |
| B77 | “A posterior-only summary omits observed behavior; a single combined score would also discard the distinction” | SUPPORTED | T1 has three differently behaving endpoints. | Keep for this probe, not as a rule for every evaluation. |
| B78 | “stated belief track[s] content while its decisions remain fragile”; “The archived evidence supports a qualified answer.” | NARROW | Games establishes 23 matches; T1 establishes five recorded correctness flips, without accuracy for those five posteriors or a noise baseline. | Replace “tracked content” with the exact two-sample observations; verify or drop “archived.” |
| B79 | “The proxy interventions add a separate association with lower pass rates, not another measurement of that same dissociation.” | SUPPORTED | Proxy rates and nonmatched difficulty; no proxy posterior–answer pairing reported. | Keep. |
| B80 | “a posterior-only account would have missed real correctness reversals under the recorded scoring procedure” | NARROW | T1 records reversals, but Limits warns extraction may be brittle. | Say “**recorded** correctness reversals”; do not use “real” to pre-empt the proposed audit. |
| B81 | “It is not enough to tell us which internal mechanism failed.” | SUPPORTED | No mechanistic measurement or independent replication. | Keep; avoid presupposing that an identified internal mechanism failed. |

**B production fix:** Remove the 👹 glyph. Bracketed tokens are intentional and should remain.

**Arithmetic audit:** The stated percentages and A’s SVG proportions are correct. The numerical defect is B’s **“one in seven changed answers” denominator/interpretation**, not its calculation that 5/36 is approximately 14%. Both drafts’ **“38 environments”** and A’s **“23 correct verdicts”** lack packet support.

## Safe claim set

These are the claims the article can state directly, with the named sample and denominator:

1. T1 compared canonical bullet order with reversed numbered order while holding the fact set and prior fixed within each matched pair.
2. T1 had **six cells**—fact counts 3, 4 and 5 crossed with priors 1/2 and 1/3—and **six seeds per cell**, yielding **36 matched pairs**.
3. T1 recorded **0/36 belief/posterior flips, 5/36 terminal-answer flips and 17/36 diagnostic-choice divergences**.
4. Under T1’s exact oracle, **all five recorded terminal-answer flips were correctness flips**.
5. In the epistemic games, **`posterior_reported = posterior_true` in 23/23 cases**, with zero reported posterior error.
6. The observed pass counts were **228/331 base, 8/27 visible-proxy and 1/4 reward-proxy**.
7. Among **76 recorded base-linked intervention cases**, there were **seven pass→fail transitions**, four tagged visible-proxy.
8. The campaign selected **416** cases; **405** were scored, with **277 PASS and 128 FAIL**; **11** were unscored. The scored pass fraction was **277/405 ≈ 0.684**.
9. Judge-guarantee counts were **189 behavioral-reference and 227 compile-only**, totaling **416 selected cases**, not 405 scored cases.
10. The campaign used **one seed per selected cell**; T1 used **six seeds per cell**.
11. **56 of 132 twin cases were unverified.** The packet reports a dirty repository, one model/provider and no independent replication.
12. The supplied packet gives **no per-cell flip distribution, pair-level transcript, T1 pre-specification record, or same-prompt repeat baseline**.

## Claims requiring a caveat **in the same sentence**

- “The model’s belief was right” **only insofar as reported posteriors matched truth in the 23 games; their accuracy in the five flipped T1 pairs is not established**.
- “Answers were presentation-sensitive” **only as an observed difference across a bundled order-and-format comparison; same-prompt sampling variability was not measured**.
- “Five of 36 pairs flipped” **describes this sample’s flip fraction, not an overall error rate or a population estimate with a reported CI**.
- “Seventeen diagnostic choices diverged” **does not mean 17 errors or a measured presentation effect; valid alternatives and chance agreement have no supplied baseline**.
- “An unchanged posterior accompanied a wrong answer” **describes recorded outputs, not proof that a correct internal belief was misused; the answer–posterior relationship and extraction fidelity are unverified**.
- “Proxy-tagged cases passed less often” **is a descriptive association across cases that were not difficulty-matched, with only four reward-proxy cases**.
- “Seven of 76 changed pass→fail” **uses all 76 intervention cases as its denominator, not the unknown number whose base cases passed; reverse transitions are unreported**.
- “The repository was dirty” **is a provenance limitation, not evidence that a changed file affected the run or invalidated a result**.

Finally, the blueprint calls for **pre-specification of T1**. The packet does **not** establish whether T1 was pre-specified: report that uncertainty, rather than calling the probe pre-registered or post hoc.
