grok 4.5:

```markdown
# CLAIM KILLER REPORT — POST-04: How Mercury Fails: Observed Failure Patterns in Mercury-2.5

**Verifier role:** Independent Claim Killer  
**Evidence ground truth:** F-007, F-002, F-009 (restatement), F-005, judge-guarantee split (189/227=416), single-model/single-seed/dirty-repo/no-replication constraints, “several” companion-file overfits (batchnorm_ema/model.py example), unquantified success conditions.  
**Blueprint base:** fable 5.1 + selective imports from opus 5 (share_of_eligible_failures caveat, 76-coincidence flag, F-009 restatement, emoji scrub).  
**Removals mandated:** “mostly behavioural” binary, “patch that runs” as fact, “shortcut” causal language, “failures disappear” as established, “unscored cases flatter rates” directional claim, “beyond noise”/“not expect from noise alone” for visible-proxy gap, Wilson intervals.  
**Qualifications mandated:** “several” companion cases, success conditions as hypotheses only, judge-guarantee composition (no cross-tab), visible-test-heavy/multi-file as descriptive/hypotheses.  
**Retentions:** F-007 exact counts + 78.1%/21.9%, F-002 numbers with denominators, 7/76 flips, multi-part caveats, evidence tiers, Figure 5 (F-007, n=128 eligible), Figure 6 (n=4 degenerate, no causal).  

**Scope note:** opus 5 is primarily a meta-resolution summary + process notes (not full prose); fable 5.1 is the full ~2,400-word essay draft. Both are covered. Bracketed tokens ([d-word] etc.) are intentional author substitutions and are **not** flagged.  

---

## Claim-by-Claim Verification Table (≥40 rows)

| # | Claim (atomic, paraphrased for precision) | Draft | Status | Evidence Basis | Notes / Blueprint Alignment |
|---|-------------------------------------------|-------|--------|----------------|-----------------------------|
| 1 | 128 FAIL verdicts total | both | SUPPORTED | F-007 | Exact; share_of_eligible_failures field. |
| 2 | 51 labelled underfit | both | SUPPORTED | F-007 | Exact. |
| 3 | 49 labelled overfit_visible_tests | both | SUPPORTED | F-007 | Exact. |
| 4 | 11 runtime_error + 9 source_invalid + 5 invalid_action + 3 training_failure | both | SUPPORTED | F-007 | Exact; sum of mechanical = 28. |
| 5 | 51+49=100; 100/128 = 78.1% | both | SUPPORTED | F-007 arithmetic | Retain. |
| 6 | 28/128 = 21.9% | both | SUPPORTED | F-007 arithmetic | Retain. |
| 7 | Six counts sum exactly to 128 | both | SUPPORTED | F-007 | Retain. |
| 8 | Labels are judge-assigned | both | SUPPORTED | Packet + F-007 | Explicit. |
| 9 | Taxonomy field is share_of_eligible_failures; 128 are *eligible* failures under unstated criterion | opus | SUPPORTED | F-007 | Import mandatory; cannot reconcile to 416 or 331. |
| 10 | 128 cannot be reconciled against 416 selected or 331 base | opus | SUPPORTED | Packet structure | Import; shares are of 128 only. |
| 11 | “Mostly behavioural, not infrastructural” is an editorial gloss, not a data field | both | SUPPORTED (as retraction) | No such axis in taxonomy | Correctly retired; binary removed. |
| 12 | One-in-five (28/128) mechanical is not a rounding error | fable | SUPPORTED | Arithmetic | Safe descriptive. |
| 13 | “Usually produces a patch that runs; it just does not solve the task” is unsupported | both | SUPPORTED (as withdrawal) | F-007 is labels, not execution status | Correctly withdrawn; 108 inference flagged. |
| 14 | Tempting to infer 108 non-runtime/source_invalid executed cleanly, but taxonomy does not say so | fable | QUALIFIED | Inference only; underfit may hide crashes | Correctly flagged as inference. |
| 15 | Dominant verdict when failing: underfit or overfit_visible_tests | fable | SUPPORTED | F-007 dominance | Narrow, safe. |
| 16 | Figure 5 shows failure-mode counts across 128 FAIL; labels judge-assigned (F-007) | fable | SUPPORTED | F-007 | Cite n=128 eligible failures. |
| 17 | overfit_visible_tests invites “gamed visible tests” reading | fable | QUALIFIED | Label name only | OK as invitation; not assertion. |
| 18 | In at least some / several cases the gaming reading is wrong | both | SUPPORTED | Packet: “several” trusted_score 1.0 + missing companion | Retain “several”. |
| 19 | trusted_score 1.0 but FAIL due to missing companion file | both | SUPPORTED | Packet + batchnorm_ema/model.py | Documented. |
| 20 | batchnorm_ema is the documented example (model.py missing) | both | SUPPORTED | Packet | Exact. |
| 21 | How many of the 49 are companion-file artifacts is unknown | both | SUPPORTED | Packet says “several”; no audit | Correct. |
| 22 | “several” could be 3/49 (6.1%) or 20/49 (40.8%) | opus | QUALIFIED | Bounds consistent with “several” | Explicit bound OK; 49 = upper bound on pure visible-test gaming. |
| 23 | 49 is an upper bound on visible-test overfitting proper, with unquantified companion-file component | both | QUALIFIED | Packet | Mandatory qualification. |
| 24 | Multi-file deliverables harder than single-file is a hypothesis from one example | both | QUALIFIED | One case (batchnorm_ema); no multi-file counts | Tier 2/3; not measured pattern. |
| 25 | Base pass rate 228/331 = 0.69 | both | SUPPORTED | F-002 | Exact; retain with denominator. |
| 26 | visible_proxy 8/27 = 0.30 | both | SUPPORTED | F-002 | Exact. |
| 27 | reward_proxy 1/4 = 0.25 | both | SUPPORTED | F-002 | Exact. |
| 28 | visible_proxy n=27 is small but not degenerate | fable | QUALIFIED | n=27 vs n=4 | Descriptive OK; avoid stronger claims. |
| 29 | Drop 0.69→0.30 on 27 cases is a difference “one would not expect from noise alone” | fable | UNSUPPORTED / FORBIDDEN | No CI computed; no matching; single seed; blueprint forbids “beyond noise” | Remove entirely. |
| 30 | No confidence interval computed; no difficulty matching performed | fable | SUPPORTED | Packet | Correct caveat. |
| 31 | reward_proxy n=4 is not a stable estimate; +1 pass → 0.50 | both | SUPPORTED | F-002 arithmetic | Label degenerate; do not quote as rate. |
| 32 | reward_proxy interval (e.g. rough 0.05–0.70) contains base rate (opus) | opus | QUALIFIED | Own derivation; small-n | Blueprint removes Wilson; treat as unusable. |
| 33 | 7 pass→fail flips within 76 shared latent specs | both | SUPPORTED | F-002 | Exact; retain 7/76. |
| 34 | Flip rate ≈9% or 9.2% or roughly one in eleven | both | SUPPORTED | 7/76 arithmetic | OK with “roughly”. |
| 35 | Flip count is within-spec (more informative than cross-population) but still single-seed | fable | QUALIFIED | Packet | Correct. |
| 36 | F-009 is a restatement of F-002, not a replication; one measurement only | both | SUPPORTED | Packet (F-009 = F-002) | Mandatory import/flag. |
| 37 | Figure 6: pass rates Base 228/331, visible 8/27, reward 1/4 (F-002); reward too small | fable | SUPPORTED | F-002 | Label n=4 degenerate; no causal language. |
| 38 | “Shortcut that the model takes” is a process claim; data contain no process observation | both | SUPPORTED (as withdrawal) | No process data | Correctly replaced by correlational + alternatives. |
| 39 | Five enumerated alternatives (shortcut, difficulty confounding, distraction/complexity, grading-surface, sampling noise) | both | QUALIFIED | Consistent with data; none ruled out | Retain list; correlational only. |
| 40 | Lowest statement supportable: pass rate lower with proxy channel; ~1/11 flips on shared specs | fable | SUPPORTED | F-002 | Safe. |
| 41 | Quantified tier: visible_proxy associated with lower pass rate (0.30 vs 0.69; n=27 vs 331) | fable | SUPPORTED | F-002 | One measurement, no replication. |
| 42 | Quantified tier: 7 flips / 76 shared | fable | SUPPORTED | F-002 | Retain. |
| 43 | Descriptive tier: companion-file FAILs with trusted_score 1.0 (batchnorm_ema); count among 49 unknown | fable | SUPPORTED | Packet | OK. |
| 44 | “Visible-test-heavy grading” and “multi-file edits” as general risk factors = generalisations/hypotheses from small set | fable | QUALIFIED | Packet failure conditions listed descriptively; no counts | Blueprint: descriptive only. |
| 45 | Success conditions (single-file specs + exact oracles) unquantified; no pass-rate stratum in packet | both | SUPPORTED | Packet (unquantified) | Correct. |
| 46 | “Failures disappear” under single-file/exact-oracle is not established; circularity risk (easiest cases) | both | SUPPORTED (as demotion) | No data; blueprint forbids as established | Hypothesis for future only. |
| 47 | 416 selected = 189 behavioral_reference + 227 compile_only | both | SUPPORTED | Packet | Exact. |
| 48 | Taxonomy counts do not stratify by guarantee; share of each label by judge type unknown | both | SUPPORTED | No cross-tab in packet | Mandatory caveat. |
| 49 | compile_only judge cannot assign some labels with same confidence | fable | QUALIFIED | By construction | OK. |
| 50 | 11 unscored: 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting (F-005) | both | SUPPORTED | F-005 | Exact. |
| 51 | 11 unscored excluded from 128 failures and from pass rates | both | SUPPORTED | Packet | Correct. |
| 52 | Omission of 11 “slightly flatters every rate reported here” | fable | UNSUPPORTED / FORBIDDEN (directional) | Blueprint explicitly removes “unscored cases flatter rates” directional claim | Delete directional language; flag as non-ignorable exclusions only. |
| 53 | 56/132 twin cases unverified = 42% or 42.4% | both | SUPPORTED | F-005 | Exact. |
| 54 | 132−56=76 numerically matches the 76 shared latent specs used for flips | both | SUPPORTED | Arithmetic + F-002/F-005 | Flag as possible coincidence / unverified identity. |
| 55 | Whether the 76 are the same set has not been confirmed; if same, flips rest on verified twins (correct subset) but identity needs checking | both | QUALIFIED | Packet | Mandatory coincidence flag (import from opus). |
| 56 | Single seed per cell; single model/provider (mercury-2.5); no replication | both | SUPPORTED | Packet | Core limitation. |
| 57 | Dirty repository (uncommitted/uncontrolled state); which cases affected unknown | both | SUPPORTED | Packet | Core limitation. |
| 58 | Intervention cases not difficulty-matched to base | both | SUPPORTED | Packet | Carry-over caveat. |
| 59 | No manual audit of individual verdicts performed | both | SUPPORTED | Packet | Explicit. |
| 60 | Everything is correlational; nothing causal | both | SUPPORTED | Design | Epistemic-status + body. |
| 61 | Title “conditions” overclaimed; reframed to “Observed Patterns” + disclaimer paragraph | both | SUPPORTED (meta) | Blueprint | Correct. |
| 62 | Wilson intervals computed by author; rest on unsupported independence assumption; shown only for precision gap n=331 vs n=4 | opus | UNSUPPORTED / FORBIDDEN | Blueprint removes Wilson intervals; single-seed invalidates | Do not include. |
| 63 | Six-part (or five-part) Limitations section covers judge composition, unscored, twins, single-seed, dirty, non-matched | both | SUPPORTED (structure) | Aligns with retain 5-part caveats | fable has 5 + carry-overs; opus notes 6. |
| 64 | Original ideas / synthesis / prose / certainty / importance dl statements | fable | QUALIFIED | Meta | Certainty “low-to-moderate” + listed limits OK. |
| 65 | Emojis 👹 and 🤥 appear in fable body | fable | PRODUCTION ARTIFACT | N/A | Mandatory scrub (blueprint). |
| 66 | “Patch that runs” converted to named flagged inference; 108 cannot license it | opus | SUPPORTED (resolution) | Aligns with withdrawal | Good. |
| 67 | Success conditions demoted to Tier 3 hypotheses; note no single-file/exact-oracle pass rate exists | opus | SUPPORTED | Packet | Good. |
| 68 | Overgeneralisation from batchnorm_ema flagged; general multi-file claim rests on one case; no multi-file counts | opus | SUPPORTED | Packet | Good. |
| 69 | 7 events is seven events (small absolute count) | fable | SUPPORTED | Arithmetic | Humility OK. |
| 70 | Failure conditions listed in packet (proxy, visible-test-heavy, multi-file, companion) are observational only | both | QUALIFIED | Packet | Do not elevate to causal conditions. |

**Table total: 70 rows.** Coverage is exhaustive for factual/numeric/inferential claims in both drafts. Meta-process claims in opus 5 (e.g., “all nine blocking issues addressed”) are treated as internal and not re-litigated beyond the resolutions that affect content.

---

## 1. SAFE CLAIM SET
(Claims that can appear verbatim or near-verbatim without further hedging)

- Exact F-007 counts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128 FAIL (share_of_eligible_failures).
- 100/128 = 78.1%; 28/128 = 21.9%.
- F-002 rates with denominators: base 228/331 (0.69), visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25).
- 7 pass→fail flips within 76 shared latent specs.
- F-009 is a restatement of F-002 (one measurement, not two).
- 11 unscored breakdown (F-005: 6/4/1).
- 56/132 = 42% (or 42.4%) unverified twins.
- Judge split: 189 behavioral_reference + 227 compile_only = 416.
- Single model (mercury-2.5), single seed per cell, dirty repo, no replication.
- batchnorm_ema example: trusted_score 1.0 but missing model.py companion.
- Labels are judge-assigned; taxonomy does not contain a behavioural/infrastructural axis.
- Figure 5 caption: Failure-mode counts across 128 FAIL verdicts (F-007).
- Figure 6 caption: Pass rates by intervention tag with explicit n=4 too-small call-out (F-002).
- All results correlational only.
- 128 are eligible failures; shares are of 128 only (cannot reconcile to 416/331).

## 2. QUALIFIED CLAIM SET
(May appear only with explicit hedging, denominators, “hypothesis”, “unknown fraction”, “one example”, “upper bound”, “coincidence flag”, or enumerated alternatives)

- “Several” companion-file cases inside the 49 overfit_visible_tests (bounds 3–20 illustrative only; 49 = upper bound on pure visible-test gaming).
- Multi-file / companion-file / visible-test-heavy as descriptive observations or hypotheses, not measured general risk factors.
- visible_proxy association (0.30 vs 0.69) is one unreplicated measurement on unmatched cells; n=27 small.
- Flip rate “roughly 9%” or “one in eleven” on the 76, with single-seed and possible twin-identity caveats.
- Five (or more) non-exclusive explanations for the proxy gap (shortcut-taking, difficulty confounding, spec complexity, grading-surface change, sampling variance); none ruled out.
- Success conditions (single-file + exact oracles) offered strictly as unquantified hypotheses for future stratified analysis; circularity risk noted.
- Judge-guarantee composition caveat: no cross-tab; compile_only vs behavioral_reference confidence differences by construction.
- 76 numerical match to verified twins may be coincidence; identity unconfirmed.
- Any inference that non-runtime/source_invalid cases “ran cleanly” (flagged as inference only).
- “Dominant labels describe patches judged against hidden behaviour” (narrow reading only).

## 3. FORBIDDEN CLAIM SET
(Must not appear in any form — delete or rewrite to elimination)

- “Mostly behavioural, not infrastructural” (or any binary split presented as data).
- “Usually produces a patch that runs; it just does not solve the task” (or 108-as-fact).
- Causal “shortcut that the model takes” / process/intent claims.
- “Failures disappear” (or any established success-condition claim) under single-file/exact-oracle specs.
- Directional “unscored cases flatter rates” / “slightly flatters every rate”.
- “Beyond noise” / “one would not expect from noise alone” / any significance or anti-noise claim for the 0.69→0.30 gap.
- Wilson intervals or any author-derived CI presented in the article.
- Any claim that F-009 constitutes replication.
- Any cross-tab or stratified claim by judge guarantee (none exists).
- Any quantified multi-file or companion-file rate beyond “several” + one named example.
- Any reconciliation of the 128 against 416 or 331 as if they share a denominator.
- Causal language around Figure 6 or proxy pattern.
- Over-precise claims about the 49 (e.g., treating all as gaming).

## 4. MANDATORY DELETIONS
(Specific phrases/paragraphs/sections)

- From fable 5.1:  
  – Entire sentence/clause: “a drop from 0.69 to 0.30 on 27 cases is a difference one would not expect from noise alone, though no confidence interval has been computed…” → delete the “not expect from noise alone” core.  
  – “their omission slightly flatters every rate reported here” → delete directional flatter claim; retain only “excluded… non-ignorable exclusions”.  
  – Any residual “mostly behavioural” if present in stubs.  
  – Emojis: 👹 and 🤥 (and any others).  
  – Any “shortcut” causal phrasing if not already fully replaced.  
  – “Failures disappear” if any affirmative remnant survives the hypothesis demotion.

- From opus 5 (if any prose leaks into final):  
  – All Wilson-interval discussion and numbers.  
  – Any presentation of Wilson as evidence rather than discarded author derivation.

- General: Any title or heading that restores “conditions” in the counterfactual/causal sense without the “A note on the title” disclaimer.

## 5. MANDATORY ADDITIONS
(Specific caveats/qualifications that must be present)

- share_of_eligible_failures explicit call-out: 128 = eligible failures; shares are of 128 only; cannot be reconciled to 416 selected or 331 base (import from opus).  
- F-009 restatement flag (one measurement).  
- 76 shared-specs vs 132−56=76 twins: numerical match flagged as unverified coincidence; identity needs checking; if identical, flips rest on verified subset.  
- “Several” companion-file bound language + 49 as upper bound on pure overfitting + batchnorm_ema as sole documented case.  
- Judge split (189/227) + explicit “no cross-tab / no stratification by guarantee” + confidence difference by construction.  
- 11 unscored as non-ignorable exclusions (no flatter language).  
- Full single-seed / single-model / dirty-repo / no-replication / no difficulty-matching / no manual-audit list.  
- Evidence-tier structure (Quantified / Descriptive-from-few / Not-measured) with success conditions strictly in Not-measured/hypothesis.  
- Opening “A note on the title” (or equivalent) disclaiming causal/conditional reading.  
- Figure 5: “n=128 eligible failures (F-007)”.  
- Figure 6: explicit “reward_proxy n=4 degenerate / too small to interpret as a rate”; no causal caption language.  
- Correlational-only + five-alternatives list for proxy pattern.  
- Epistemic-status certainty remains low-to-moderate with the listed constraints.

## 6. PRODUCTION FIXES

- **Emoji scrub:** Remove 👹 and 🤥 (and any others) from fable 5.1 body. Replace with plain prose or delete the decorative clause.  
- **Figure hygiene:**  
  – fig5_failure_modes.svg: caption must cite F-007 and “n=128 eligible failures”.  
  – fig6_pairwise_intervention.svg: caption must list exact fractions, flag n=4 as degenerate, zero causal language.  
  – Ensure relative paths and alt text remain clean.  
- **House style:** Retain YAML front matter, epistemic-status `<dl>`, icon-self byline, numbered figure captions, closing caveats. No house_style.md was present; conventions already reconstructed correctly in fable.  
- **Bracketed tokens:** Leave [d-word], [ac-word], etc. untouched (intentional).  
- **Word-count / tone:** Final article should stay ~2,200–2,500 words; keep the weaker “patterns” framing.  
- **Import checklist (opus → fable base):** share_of_eligible_failures caveat, 76-coincidence flag, F-009 restatement, emoji scrub. Do **not** import Wilson.  
- **Arithmetic hygiene:** All percentages shown with raw counts (e.g., 100/128 = 78.1%). Flip rate as 7/76.  
- **Final summary paragraph:** Must restate only safe + properly qualified claims; end on “correlational, singly measured, admits several explanations” and “conditions under which failures disappear have not been measured”.

---

**Overall verdict on drafts:**  
fable 5.1 is the correct base (already implements most retirements, tiers, and caveats). It requires only the noise-claim deletion, flatter-claim deletion, emoji scrub, plus the three opus imports (eligible-share, 76-flag, F-009). opus 5 supplies useful resolution language and the three imports but must not contribute Wilson intervals or become the prose base. After the listed deletions/additions/fixes, the article will be fully aligned with the evidence packet and Stage C blueprint.

**No remaining blocking unsupported claims once the FORBIDDEN set and MANDATORY DELETIONS are executed.**
```

&&&&&&&&&&&&&

gemini 3.1 pro grounding:

Here is the detailed Claim Killer verification of the two candidate drafts (`opus 5` and `fable 5.1`) evaluated against the verified evidence packet and Stage C Blueprint decisions. 

### Claim-by-Claim Verification Table

| Row | Draft | Claim / Inference | Status | Evidence Basis / Notes |
|:---|:---|:---|:---|:---|
| 1 | Opus 5 | Dominant labels account for 100/128 (78.1%) failures. | SUPPORTED | F-007: 51 underfit + 49 overfit_visible_tests = 100. 100/128 = 78.1%. |
| 2 | Opus 5 | Mechanical error labels account for 28/128 (21.9%). | SUPPORTED | F-007: 11+9+5+3 = 28. 28/128 = 21.9%. |
| 3 | Opus 5 | "Mostly behavioural" phrasing was imposed, not in data. | SUPPORTED | Blueprint mandates removal of "mostly behavioural" binary classification. |
| 4 | Opus 5 | "Patch that runs" converted to flagged inference. | QUALIFIED | Blueprint mandates removal of "patch that runs" as fact. Fable 5.1 correctly flags it as inference, as F-007 records labels, not execution status. |
| 5 | Opus 5 | "Several" bounded to 3/49 (6.1%) or 20/49 (40.8%). | UNSUPPORTED | The evidence packet simply states "several" and does not contain numeric bounds. The bounds are arbitrary author insertions. |
| 6 | Opus 5 | `reward_proxy` cell interval contains base rate. | UNSUPPORTED | Derived via Wilson intervals, which the blueprint explicitly bans. |
| 7 | Opus 5 | 7/76 pass-to-fail flips equals roughly 9.2%. | SUPPORTED | F-002 confirms 7 flips within 76 shared specs. |
| 8 | Opus 5 | No single-file or exact-oracle pass rates exist. | SUPPORTED | Success conditions are noted as unquantified in the packet. |
| 9 | Opus 5 | No multi-file counts exist in the evidence. | SUPPORTED | Packet notes failure conditions but provides no quantified counts for multi-file cases. |
| 10 | Opus 5 | 189/227 judge-guarantee split. | SUPPORTED | Packet explicitly lists 189 behavioral_reference and 227 compile_only. |
| 11 | Opus 5 | 11 unscored exclusions. | SUPPORTED | F-005 lists exactly 11 unscored cases. |
| 12 | Opus 5 | 56/132 (42.4%) unverified twins. | SUPPORTED | F-005 lists 56/132 unverified twins. |
| 13 | Opus 5 | 132-56=76 numeric coincidence is flagged. | QUALIFIED | Validated by blueprint requirement to import the "76 coincidence flag". Identity between the remaining 76 twins and the 76 shared specs is unverified. |
| 14 | Opus 5 | 128 failures is `share_of_eligible_failures`. | SUPPORTED | F-007 uses the precise taxonomy field `share_of_eligible_failures`. |
| 15 | Opus 5 | F-009 is a restatement of F-002. | SUPPORTED | Explicitly stated in the evidence packet. |
| 16 | Opus 5 | Computed nominal Wilson intervals. | UNSUPPORTED | Explicitly banned by blueprint ("Remove: ... Wilson intervals"). |
| 17 | Fable 5.1 | Certainty is low-to-moderate. | SUPPORTED | Valid inference given single seed, single model, and dirty repo. |
| 18 | Fable 5.1 | Model is mercury-2.5 from single provider. | SUPPORTED | Packet explicitly defines: "Single model/provider (mercury-2.5)". |
| 19 | Fable 5.1 | Single seed per cell, dirty repository. | SUPPORTED | Matches exact constraints in the evidence packet. |
| 20 | Fable 5.1 | 128 FAIL verdicts total. | SUPPORTED | F-007 totals exactly 128 failures. |
| 21 | Fable 5.1 | 51 `underfit` failures. | SUPPORTED | Matches F-007. |
| 22 | Fable 5.1 | 49 `overfit_visible_tests` failures. | SUPPORTED | Matches F-007. |
| 23 | Fable 5.1 | 11 `runtime_error` failures. | SUPPORTED | Matches F-007. |
| 24 | Fable 5.1 | 9 `source_invalid` failures. | SUPPORTED | Matches F-007. |
| 25 | Fable 5.1 | 5 `invalid_action` failures. | SUPPORTED | Matches F-007. |
| 26 | Fable 5.1 | 3 `training_failure` failures. | SUPPORTED | Matches F-007. |
| 27 | Fable 5.1 | 108 cases not labelled runtime_error/source_invalid. | SUPPORTED | 128 - 11 - 9 = 108. Arithmetic is correct. |
| 28 | Fable 5.1 | Dominant verdict is doing visible part but not hidden. | SUPPORTED | Accurately describes the nature of `overfit_visible_tests` and `underfit`. |
| 29 | Fable 5.1 | Several overfit cases scored `trusted_score` 1.0. | SUPPORTED | Packet directly corroborates this behavior. |
| 30 | Fable 5.1 | `batchnorm_ema` case scored 1.0 but missing `model.py`. | SUPPORTED | Evidence packet identifies `batchnorm_ema/model.py` as the exact culprit. |
| 31 | Fable 5.1 | Multi-file specs are harder for Mercury-2.5. | QUALIFIED | Correctly presented as a hypothesis from a single example. |
| 32 | Fable 5.1 | Base cases pass 228 of 331 (0.69). | SUPPORTED | Matches F-002 exactly. |
| 33 | Fable 5.1 | `visible_proxy` cases pass 8 of 27 (0.30). | SUPPORTED | Matches F-002 exactly. |
| 34 | Fable 5.1 | `reward_proxy` cases pass 1 of 4 (0.25). | SUPPORTED | Matches F-002 exactly. |
| 35 | Fable 5.1 | visible-proxy drop is one "would not expect from noise alone." | UNSUPPORTED | Banned explicitly by blueprint ("Remove... 'beyond noise' claim for visible-proxy gap"). |
| 36 | Fable 5.1 | reward_proxy cell at n=4 is not a stable estimate. | SUPPORTED | Supported by low sample size; matches blueprint instruction to label n=4 degenerate. |
| 37 | Fable 5.1 | 7 pass-to-fail flips across 76 shared latent specs. | SUPPORTED | Matches F-002 exactly. |
| 38 | Fable 5.1 | Proxy effect has 5 possible correlational explanations. | QUALIFIED | Fulfills blueprint mandate to remove "shortcut" causal language and replace with correlational framing. |
| 39 | Fable 5.1 | Failures disappear under single-file / exact oracles. | QUALIFIED | Blueprint mandates qualifying this as an unmeasured hypothesis, which the draft successfully does. |
| 40 | Fable 5.1 | 416 selected split: 189 behavioral_reference, 227 compile_only. | SUPPORTED | Matches judge-guarantees in the packet exactly. |
| 41 | Fable 5.1 | 11 unscored: 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting. | SUPPORTED | Matches F-005 list exactly. |
| 42 | Fable 5.1 | Omission of unscored "flatters every rate reported here". | UNSUPPORTED | Banned by blueprint ("Remove... 'unscored cases flatter rates' directional claim"). |
| 43 | Fable 5.1 | 56 of 132 twin cases unverified. | SUPPORTED | Matches F-005 exactly. |
| 44 | Fable 5.1 | Identity of the remaining 76 coincidence needs checking. | SUPPORTED | Satisfies blueprint mandate to flag the "76 coincidence" regarding the latent specs. |
| 45 | Fable 5.1 | Nothing is causal; everything is correlational. | SUPPORTED | Strongly mandated by the blueprint and the evidence restrictions. |

---

### 1. SAFE CLAIM SET
*Claims that can appear in the final article without qualification.*
- F-007 taxonomy metrics: 128 FAIL verdicts total, split across `underfit` (51), `overfit_visible_tests` (49), `runtime_error` (11), `source_invalid` (9), `invalid_action` (5), and `training_failure` (3). The 78.1% vs 21.9% distribution arithmetic.
- F-002 intervention pass rates with denominators: base 228/331 (0.69), `visible_proxy` 8/27 (0.30), `reward_proxy` 1/4 (0.25). 
- F-002 spec metrics: 7 pass-to-fail flips within 76 shared latent specs.
- Judge composition: 416 selected cases comprised of 189 `behavioral_reference` and 227 `compile_only`.
- Unscored case counts: exactly 11 unscored (split 6, 4, 1 as defined by F-005).
- Twin verification counts: 56 of 132 twins are unverified.
- Evidence conditions: F-009 is a restatement of F-002, not a replication. The run relied on a single model/provider (mercury-2.5), a single seed per cell, no replication, and a dirty repository.

### 2. QUALIFIED CLAIM SET
*Claims that can appear but only with explicit hedging.*
- **"Several" Companion-File Failures:** Must be strictly qualified as an unknown subset of the 49 overfit cases where a `trusted_score` of 1.0 was given despite a missing file (e.g., `batchnorm_ema/model.py`).
- **Success/Failure Conditions:** Claims about multi-file edits, visible-test-heavy grading, single-file specifications, and exact oracles must be explicitly qualified as *hypotheses* based on unquantified cases.
- **Judge-Label Composition:** Any discussion of judge verdicts must include the caveat that failure modes were not cross-tabbed against the specific judge guarantee (`behavioral_reference` vs `compile_only`).
- **The "76" Coincidence:** Must be flagged. The 132 total twins minus 56 unverified equals 76, numerically matching the 76 shared latent specs, but the identity of the two sets is unverified.

### 3. FORBIDDEN CLAIM SET
*Claims that must not appear in any form.*
- Framing failures as a "mostly behavioural, not infrastructural" binary.
- Stating "the patch runs" as a proven execution fact rather than a correlational inference.
- Using causal language asserting the proxy channel operates as a "shortcut the model takes".
- Claiming that failures "disappear" as an established fact under single-file or exact oracle conditions.
- Directional claims asserting that the exclusion of unscored cases "flatters rates".
- Statistical assertions that the `visible_proxy` drop is "beyond noise" or something "one would not expect from noise alone".
- Supplying derived bounds for "several" (e.g., 3/49 or 20/49).
- Any presentation of Wilson Intervals or confidence bounds. 

### 4. MANDATORY DELETIONS
*Items that must be excised from Fable 5.1.*
1. Delete the phrase: *"a difference one would not expect from noise alone"* (Paragraph under "The one quantified intervention pattern").
2. Delete the phrase: *"and their omission slightly flatters every rate reported here"* (Bullet 2 under "Caveats").

### 5. MANDATORY ADDITIONS
*Items that must be inserted into Fable 5.1 based on Blueprint and Opus 5.*
1. Import the `share_of_eligible_failures` caveat from Opus 5. State explicitly near the top that the 128 count is a share of eligible failures under an unstated criterion and cannot be linearly reconciled against the 416 selected or 331 base cases. 
2. Update the **Figure 5** caption to explicitly cite: *"n=128 eligible failures"* (rather than "128 FAIL verdicts").
3. Update the **Figure 6** caption to explicitly label the n=4 reward_proxy cell as *"degenerate"*.

### 6. PRODUCTION FIXES
1. **Emoji Scrub:** Remove the unicode emojis `👹` and `🤥` from Fable 5.1's body text.
2. **Author Tokens:** Ensure bracketed meta-variables inserted by the author (e.g., `[d-word]`) remain untouched. Do not flag them as errors.
