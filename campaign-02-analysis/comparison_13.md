openhard 3.0 cot 1015:

# Editorial Blueprint — POST-03: *Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)*

## 1. Executive verdict

**Use Draft B (GPT 6.1 “sol max”) as the structural base.** It is the more complete, defensible manuscript: it explicitly separates units of analysis, handles the F-006 count discrepancy, distinguishes source-validation failure from semantic failure, addresses missingness/provenance, and ends with concrete requirements for a credible transition claim.

**Use Draft A as a prose and compression source.** Draft A has a stronger opening, a cleaner epistemic-status block, sharper figure captions, and a more economical treatment of the illustrative null calculation. Its main weakness is that it is too short to fully discharge the Stage A blockers; it also contains several copy-level artifacts that must be removed.

The final article should preserve Draft B’s argumentative skeleton while importing Draft A’s tighter framing, figure program, and selected phrasing. The target thesis remains:

> The archive records three suggestive sequences, but it does **not** establish a non-monotonic difficulty curve, validate a common ordinal difficulty axis, or locate a capability threshold.

This is a measurement paper, not a discovery paper.

---

## 2. Comparative evaluation

### Draft A strengths
- Strong lead: “A middle setting fails; the settings on either side pass.”
- Excellent epistemic-status header, especially the certainty statement.
- Correctly frames 0.684 as conditional on scored cases.
- Correctly refuses to count the unscored F-006 environment as a zero-pass environment.
- Good compact table for the three sequences.
- Clear warning that lines in figures are visual connectors, not fitted curves.
- Useful explicit statement that the examples cannot estimate prevalence because no exhaustive sweep denominator exists.
- Good follow-up paragraph on freezing executed source, tasks, validators, limits, and replication.

### Draft A weaknesses
- Contains accidental intrusive wording (“task fuckingly presented,” “what was fuckingly judged”) that is not one of the approved bracketed tokens and must be deleted.
- Treatment of judge guarantees is present but underdeveloped.
- Missingness of the 11 unscored cases is noted, but the possibility of outcome-dependent missingness is not developed.
- Does not fully spell out the distinction between:
  1. ordered task parameter,
  2. evaluator coverage,
  3. source-validity stage,
  4. estimated success probability.
- The follow-up design is good but not converted into explicit acceptance criteria.
- Does not explicitly state that the archive neither validates nor disproves a latent monotonic difficulty scale.
- Figure 1 is described but its exact encoding and inclusion rule need tightening.

### Draft B strengths
- Best overall logical architecture.
- Explicitly distinguishes cases, matrix rows, and matched sweeps as different units.
- Handles all three sequences with appropriate asymmetry rather than treating them as three equivalent binary zigzags.
- Correctly resolves the CSS issue: partial score is not silently mapped to PASS/FAIL.
- Correctly avoids attaching an unsupported SQL surface qualifier.
- Includes the regex axis without inventing a regex outcome sequence.
- Gives the null calculation with full assumptions and explicitly labels it non-calibrated.
- Strong section on “First ask what failed,” separating source-validation rejection from semantic failure.
- Strong treatment of provenance, dirty repository, judge guarantees, and single-seed limitation.
- Includes a concrete prespecified analysis recipe for a future credible study.
- Ends at the right level of claim: observations worth auditing, not a detected capability valley.

### Draft B weaknesses
- Longer and somewhat repetitive; several points are restated across sections.
- Uses `[d-word]` intentionally; retain as directed, but ensure usage is consistent and not overused.
- The opening is effective but slightly less immediate than Draft A.
- No explicit figure program in the draft text; figures need to be inserted with disciplined captions.
- A few sentences can be tightened to avoid sounding as though the archive disproves a difficulty scale; the correct position is **validation absent, not refutation established**.
- The phrase “bimodal environment difficulty” should be qualified: F-006 describes a bimodal pattern, but the packet summary and count discrepancy do not justify a strong distributional claim.

---

## 3. Base selection and import plan

### Base
**Draft B**, using its section order and argument progression.

### Import from Draft A
1. **Epistemic-status block**
   - Use Draft A’s five-field structure:
     - Original ideas
     - Synthesis
     - Prose
     - Certainty
     - Importance
   - Merge in Draft B’s sharper claim wording.

2. **Opening hook**
   - Import Draft A’s first two sentences, then immediately qualify with Draft B’s warning that these are selected single-seed observations.

3. **Figure captions and visual discipline**
   - Import Draft A’s rule:
     > Lines connect recorded outcomes for legibility; they are not fitted pass-rate curves.
   - Import the grey = unscored, not zero-pass encoding rule.

4. **Compact sequence table**
   - Use Draft A’s table format, but populate it with Draft B’s more precise qualifications.

5. **Concise null paragraph**
   - Use Draft A’s compact calculation, then retain Draft B’s longer list of violated assumptions immediately afterward.

6. **Closing sentence cadence**
   - Draft A’s final line is strong:
     > They do not locate where a model’s ability breaks. Before a difficulty transition can be measured, difficulty has to name a controlled change, and each outcome has to say what was judged.
   - Adapt it, removing the accidental profanity.

### Do not import from Draft A
- Any phrasing that treats CSS as a clean binary pass/fail/pass sequence.
- Any implicit suggestion that the three examples are a representative sample.
- The uncorrected profanity artifacts.

---

## 4. Claim ledger: retain, qualify, remove

### Retain as written
- 416 selected, 405 scored, 277 PASS, 128 FAIL, scored pass share 0.684.
- 11 selected-but-unscored cases; unscored ≠ FAIL.
- 38 environments.
- 340 environment × difficulty-tuple rows.
- One seed-0 run per selected cell; no replication.
- Dirty repository; clean checkout alone does not reconstruct executed state.
- MoCo: PASS → FAIL → PASS at successive visible-test levels.
- CSS: partial score → source-validation failure → PASS at 3/4/5 bits, easy surface.
- SQL: PASS → source-validation failure → PASS at chain lengths 6/12/25.
- F-006 names six zero-rate environments; the claimed seven includes an unscored entry that must not be converted to a measured zero.
- Environment pass rates span 0.00 to 1.00.
- Illustrative zigzag probability under flat independent binary model: \(p(1-p)\), with \(p=277/405\), ≈0.216.
- Source-validation failure is not equivalent to demonstrated semantic-task failure.
- No exhaustive eligible-sweep denominator is supplied.
- No model capability threshold is located.

### Qualify carefully
1. **“Non-monotonic difficulty transitions”**
   - This is the title and topic, not an established empirical result.
   - Use phrasing: *reported non-monotonic sequences*, *apparent transitions*, *candidate reversals*.
   - Do not title-claim that a true non-monotonic transition has been measured.

2. **“Bimodal environment difficulty”**
   - Say: F-006 characterizes the environment pattern as bimodal, with rates spanning 0.00–1.00.
   - Do not assert a validated bimodal distribution from the summary alone, especially with the count discrepancy.

3. **MoCo failure**
   - Say the middle outcome is FAIL in the supplied record.
   - Do not claim its failure stage unless the packet specifies it.
   - Do not assume it was a source-validation failure.

4. **CSS sequence**
   - Explicitly state it is **not** a binary P/F/P sequence.
   - The first point is partial; the middle is source-validation failure.
   - No documented mapping from partial score to campaign binary accounting.

5. **SQL sequence**
   - Endpoint PASS, middle source-validation failure.
   - Lengths 6, 12, 25 are sparse samples; they do not localize a boundary.
   - Do not attach an easy-surface or other surface qualifier unsupported by F-008.

6. **Axis interpretation**
   - Bits, chain lengths, and string lengths are numerically ordered parameters.
   - Their effect on model success probability is uncalibrated.
   - Visible-test level changes evaluator coverage, not necessarily task construction difficulty.

7. **Truncation hypothesis**
   - Keep it as one plausible explanation, not favored.
   - State that longer-task success does not rule it in or out because emitted source length need not track nominal task size.

8. **Judge guarantees**
   - Say mixed guarantees exist and must be audited.
   - Do not claim a guarantee change caused any reversal, because the packet does not show one along the quoted sequences.

9. **Latent difficulty scale**
   - Correct position:
     - The archive does not validate a common ordinal latent-difficulty scale.
     - It also does not disprove every possible monotonic latent scale.
     - Single outcomes can zigzag even if underlying success probability is monotonic.

10. **Pooled 0.684**
    - It is a descriptive scored-case fraction.
    - It is not a universal per-cell pass probability and not a calibrated null parameter.

### Remove or forbid
- Any claim that reversals are unusually frequent.
- Any prevalence estimate for zigzags.
- Any statement that CSS contributes one binary reversal.
- Any invented regex pass sequence.
- Any unsupported SQL surface label.
- Any claim that the middle SQL point locates a threshold.
- Any causal attribution of source-validation failures to output truncation.
- Any assertion that dirty repository *caused* an anomaly.
- Any treatment of unscored cases as failures.
- Any treatment of the 340 rows as 340 independent sweep opportunities.
- The accidental non-bracketed profanity insertions in Draft A.
- Any phrase implying the paper ran new cases, inspected artifacts, or enumerated sweeps.

### Bracketed tokens
Retain intentional tokens such as `[d-word]` exactly as supplied. Do not edit, expand, or flag them.

---

## 5. Figure placement and numbering

Use **two figures**, consistent with Draft A, but tighten their scope.

### Figure 1 — Environment × difficulty-tuple overview
**Placement:** after the campaign-accounting section, before the three-sequence deep dive.

**Content rules:**
- Show selected environment × difficulty-tuple rows.
- Encode:
  - numerator/denominator pass labels,
  - grey = unscored,
  - distinct hatching or color for source-validation-heavy cells if feasible.
- **Do not** imply this displays all eligible three-level sweeps.
- Caption must state:
  1. unit is matrix row,
  2. grey means unscored, not zero,
  3. display is for locating recorded outcomes,
  4. no curve fitting.

**Caption skeleton:**
> Figure 1. Selected environment × difficulty-tuple rows. Cell labels show passes over scored cases; grey denotes unscored cases, not zero passes. The figure locates recorded outcomes and does not enumerate all eligible matched sweeps.

### Figure 2 — The three recorded sequences
**Placement:** immediately after the sequence table / “Three sequences, not three curves” section.

**Preferred design:**
- Three small panels, one per environment, rather than only MoCo.
- Panel A: MoCo, binary PASS/FAIL/PASS.
- Panel B: CSS, with distinct markers for partial, source-validation failure, PASS.
- Panel C: SQL, with PASS, source-validation failure, PASS at 6/12/25.
- Use broken or categorical x-axes where spacing is not semantically uniform.
- Connect points only with faint light-grey lines.

**Caption skeleton:**
> Figure 2. Recorded outcomes for the three F-008 contrasts. Markers distinguish PASS, partial score, and source-validation failure. Connectors are visual aids only. With one seed-0 outcome per selected cell, these are not estimated pass-rate curves, and the sparse SQL samples do not locate a boundary.

If production constraints allow only one MoCo figure, retain Draft A’s Figure 2 but move CSS and SQL entirely into the table; do not visually imply all three are binary curves.

### Figure hygiene requirements
- No interpolated smoothing.
- No continuous fitted response curve.
- No equal-spacing implication for 6/12/25 unless x-axis is explicitly numeric.
- Partial score must use a separate marker, not FAIL.
- Source-validation failure must use a separate marker from semantic FAIL where possible.

---

## 6. Final section structure

Use this seven-section structure, based on Draft B with Draft A compression.

### 1. Epistemic header + opening
- Epistemic-status definition list.
- Opening hook: pass–fail–pass looks like recovery.
- Thesis: these are selected single-cell records, not measured curves.

### 2. What the campaign recorded
- F-004 counts.
- 416 / 405 / 277 / 128 / 0.684.
- 11 unscored.
- 340 matrix rows.
- Units distinction: selected cases, scored cases, matrix rows, matched sweeps.
- Figure 1.

### 3. Three sequences, not three curves
- Sequence table.
- MoCo, CSS, SQL treated asymmetrically.
- Explicit note: only MoCo is a clean binary zigzag in the supplied record.
- Figure 2.

### 4. Why an observed zigzag is not a measured reversal
- Illustrative flat-null calculation.
- Derive \(p(1-p)\).
- State ≈21.6%.
- List why this is not calibrated:
  - pooled heterogeneous environments,
  - independence unverified,
  - no sweep denominator,
  - selection rule not exhaustive,
  - CSS not binary.
- Explain monotonic underlying probabilities can still produce non-monotonic single outcomes.

### 5. What the axes actually change
- MoCo: test coverage.
- CSS: bit count at fixed easy surface; class-name axis noted but not the swept axis in the quoted sequence.
- SQL: graph-chain length.
- Regex: input lengths 32/128/512, but no outcome sequence supplied.
- Ordered parameter ≠ calibrated difficulty scale.
- Nested-test caveat for MoCo: nested suites constrain a fixed submission, not independently generated submissions.

### 6. First ask what failed
- Source validation vs semantic evaluation.
- Validation failure is a real contract failure, but not direct evidence of inability on the underlying task.
- Truncation as unresolved hypothesis.
- Missing artifacts, logs, output budgets, validator diagnostics.
- Judge guarantees as audit item, not established cause.
- F-006 count discrepancy and environment heterogeneity.
- Missingness and dirty-repo provenance.

### 7. What would make a transition claim credible
- Prespecified eligible-sweep definition.
- Exhaustive enumeration before example selection.
- Fixed non-varied tuple components.
- Replication across seeds/instances.
- Separate accounting for source validity, semantic result, partial, unscored.
- Artifact preservation and validator diagnostics.
- Frozen executed source and full model/harness manifest.
- Denser sampling around SQL length 12.
- Explicit denominator and uncertainty estimation.

### Closing paragraph
- Restrict conclusion to audit-worthy observations.
- End on measurement: parameter, evaluator setting, and success probability are distinct.
- No located breakpoint.

### Evidence scope footnote
- F-004, F-006, F-008, matrix description.
- Explicitly state no new sweep enumeration, artifact inspection, or replication.

---

## 7. Additional corrections and copy edits

1. **Remove intrusive profanity**
   - “task fuckingly presented” → “task as presented”
   - “what was fuckingly judged” → “what was judged”
   These are not approved bracketed placeholders.

2. **Normalize terminology**
   Use consistently:
   - *recorded sequence*
   - *candidate reversal*
   - *source-validation failure*
   - *semantic failure*
   - *scored-case pass share*
   - *matched sweep*
   - *unscored*, never “zero”

3. **Avoid overclaiming bimodality**
   - Use “F-006 describes a bimodal pattern” rather than “the distribution is bimodal.”

4. **CSS accounting**
   - Do not reconcile partial score into PASS/FAIL.
   - State only that the packet does not document the reconciliation.

5. **Regex**
   - Mention only axis lengths.
   - No inferred outcomes.

6. **SQL**
   - No surface qualifier.
   - No threshold language.

7. **MoCo**
   - Visible-test level = coverage manipulation.
   - Do not call it task-size scaling.

8. **Null model wording**
   - Call it “illustrative flat independent binary model.”
   - Never call it the null hypothesis for Mercury-2.5.

9. **Repository wording**
   - Dirty repo blocks exact reconstruction from a clean commit.
   - It does not by itself invalidate recorded counts.

10. **Seed wording**
    - seed-0 gives one realization per selected cell.
    - Do not claim what source of variation the seed controls without evidence.

11. **Numerical verification ledger**
    All numbers in the final text should be checked against the packet:
    - 416 selected
    - 405 scored
    - 277 PASS
    - 128 FAIL
    - 0.684 scored pass share
    - 11 unscored selected cases
    - 38 environments
    - 340 matrix rows
    - 6 named zero-rate environments
    - 7 claimed in F-006, with discrepancy
    - SQL lengths 6, 12, 25
    - CSS bits 3, 4, 5
    - Regex lengths 32, 128, 512
    - \(277/405 \approx 0.684\)
    - \(p(1-p)\approx0.216\)

    The 21.6% is a derived illustration, not a packet fact; label it as such.

---

## 8. Response-to-review table: Stage A blocking issues

| Blocking issue | Draft A handling | Draft B handling | Final resolution |
|---|---|---|---|
| **1. Null hypothesis uncomputed** | Provides crude flat-model calculation and says it is not calibrated. | Provides same calculation, derives \(p^2(1-p)+p(1-p)^2=p(1-p)\), and enumerates assumption failures. | **Keep Draft B version, compressed with Draft A wording.** State no calibrated null was computed; 21.6% is only an illustration. Do not present it as a significance test. |
| **2. Selection effect / no denominator** | Explicitly says no prespecified search rule and no exhaustive count; examples cannot establish prevalence. | Stronger: distinguishes cases, rows, sweeps; specifies how an exhaustive enumeration should be done. | **Retain and foreground.** No prevalence claim. State F-008 supplies selected examples, not a sampled set. Future work must enumerate eligible matched sweeps before selection. |
| **3. Source-validation failures** | Notes CSS and SQL middle failures are validation-stage, not behavioral semantic failures; says artifacts/diagnostics are absent. | Dedicates a full section; distinguishes contract failure from competence evidence; treats truncation as unresolved. | **Use Draft B treatment.** Keep both statements: validation failure is a legitimate benchmark failure, but it is not direct evidence of semantic inability. Do not assign cause. |
| **4. Causal overreach** | Avoids causal claims; says axes change different properties and do not explain within-environment reversals. | Explicitly separates axis heterogeneity, failure stage, judge guarantees, provenance; refuses truncation attribution. | **Retain strict causal discipline.** No claim that difficulty caused failure, truncation caused rejection, or dirty repo caused anomaly. Use “consistent with,” “unresolved,” “would require audit.” |
| **5. Latent difficulty / ordinal scale unsupported** | States difficulty settings are not a validated ordinal scale. | Strongest version: axes differ; ordered parameter ≠ measured performance effect; archive neither validates nor disproves a latent scale. | **Use Draft B nuanced formulation.** Do not say no latent scale exists; say it is unvalidated. Monotonic underlying probabilities can still yield one-shot zigzags. |

### Supplementary Stage A factual issues

| Review issue | Resolution |
|---|---|
| Regex pass claim | Do not claim any regex pass sequence. Mention only 32/128/512 as an axis definition. |
| SQL surface qualifier | Remove any unsupported surface label. |
| CSS axis mis-description | State the quoted contrast is bit count 3→4→5 at fixed easy surface; do not conflate with class-name variation. |
| “Hardest label” framing | Remove. The paper is not validating a hardest-label ranking. |
| Partial-score reconciliation | Do not force partial into PASS/FAIL. State packet gives no documented mapping. |
| F-006 count | Six named zero-rate environments; seventh entry is unscored. Do not call it seven measured zeros. |

---

## 9. Acceptance criteria for final resubmission

The final article should satisfy all nine:

1. **No calibrated null claim**
   - The 21.6% figure is explicitly labeled hypothetical and derived under flat independent binary assumptions.

2. **No prevalence claim**
   - No statement that reversals are common, rare, enriched, or surprising relative to baseline.

3. **Complete denominator hygiene**
   - 416 selected, 405 scored, 11 unscored kept distinct.
   - 340 rows not equated with 340 sweeps.

4. **Sequence asymmetry preserved**
   - MoCo = binary reversal.
   - CSS = mixed-status sequence.
   - SQL = endpoint PASS around validation rejection.

5. **Source-validation distinction maintained**
   - Validation failure is not silently rewritten as semantic failure.

6. **No unsupported causal explanation**
   - Truncation, judge changes, and repo state remain hypotheses or audit items, not causes.

7. **Axis construct validity stated**
   - Difficulty labels are not treated as a validated common ordinal scale.
   - The paper neither validates nor disproves such a scale.

8. **Provenance and replication limits explicit**
   - seed-0 only, no replication, dirty repository, incomplete manifest.

9. **No invented evidence**
   - No new enumeration, artifact inspection, regex outcomes, or SQL surface qualifier.
   - Evidence scope footnote included.

---

## 10. Recommended synthesis note

The final piece should read as a **constructive audit**, not a debunking. Its strongest contribution is methodological:

- A numeric parameter order is not a performance scale.
- A selected triplet is not a response curve.
- A validation-stage rejection is not the same observation as a semantic failure.
- A pooled pass fraction is not a per-cell probability.
- A single seed cannot estimate variability.

Draft B supplies the architecture; Draft A supplies the sharpness. Merge them, remove the copy artifacts, keep figures non-inferential, and end at the narrow supported conclusion: **these are cases to audit, not a located breakpoint in Mercury-2.5 capability.**

Need me to produce the **merged full draft** directly from this blueprint?

&&&&&&&&&&&&&&&&


grok 4.5:

**EDITORIAL BLUEPRINT: POST-03 — Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)**

**Base draft recommendation:** Use **Draft 2 (gpt 6.1 sol max)** as the structural and prose base.  
It is tighter on claim discipline, has superior section architecture (clear progression from records → axes → reversals as observations → failure layers → denominators/provenance → credibility criteria → measurement finding), more explicit separation of units (cases vs rows vs sweeps), stronger handling of judge guarantees/mixed acceptance criteria, attrition/missingness, and a forward-looking “what would make a transition claim credible” checklist. It better resists causal overreach and selection-effect inflation while remaining readable. Epistemic-status block is more claim/evidence-oriented (preferable for this series).

**Draft 1 (gpt 6)** strengths to import (do not use as base):  
- Figure concepts and captions (matrix overview + MoCo trace). Integrate and number them.  
- “Three sequences, not three curves” framing and table compactness.  
- Especially careful F-006 bookkeeping language (“I do not count an unscored environment as one with a zero pass rate”).  
- Concise closing cadence and some intro/transition sentences.  
- Explicit “selection rule is simple: report the three contrasts explicitly identified in F-008” + “packet gives neither a prespecified search rule nor an exhaustive count.”  
- Dirty-repo + freeze-executed-source follow-up language (merge into Draft 2’s provenance and checklist).  
- Certain phrasings on partial-score non-reconciliation with binary totals and on why a shared easy-to-hard x-axis is unjustified.

Draft 1 is slightly more essayistic/personal in epistemic block and shorter; Draft 2 is more systematic and complete against Stage A. Hybrid length target: Draft 2 body + imported figures + selective tightening from Draft 1 (aim ~compact long-form, not padded).

**Overall stance to preserve (both drafts align well with evidence packet + Stage A):**  
The piece is a measurement/methodology critique, **not** a claim that Mercury-2.5 has non-monotonic capability or a “valley.” Core finding: difficulty labels are not a validated ordinal scale of model performance; the three F-008 sequences are single-seed selected observations (with source-validation and partial-score complications), not estimated curves or located thresholds. Retain high certainty on recorded counts/sequences; low certainty / no claim on difficulty *effects* or capability breaks. Single-seed-per-cell, dirty repo, no replication, heterogeneous axes/judges, and incomplete sweep enumeration are first-class limitations.

**Bracketed tokens ([d-word], etc.):** Retain exactly as intentional author replacements. Do not expand or flag.  
**“fuckingly”:** Treat as draft artifact/placeholder (contextually “actually”). Replace all instances with “actually” in the final (Draft 1: “task actually presented”, “what was actually judged”; Draft 2: “What was actually recorded”). No other profanity or tone issues.

### 1. Claims: Retain / Remove / Qualify

**Retain (core, evidence-aligned):**  
- Campaign accounting exactly as F-004: 416 selected / 405 scored / 277 PASS / 128 FAIL / 0.684 *among scored* / 38 environments / 11 unscored. Emphasize scored-only denominator; unscored ≠ FAIL; missingness mechanism unknown (possibly outcome-dependent).  
- 340-row environment × difficulty-tuple matrix as location aid, not replicated curves. Each selected cell = seed-0 only.  
- F-008 sequences *verbatim descriptions only*:  
  – MoCo visible-test levels: PASS → FAIL → PASS (binary zigzag; axis = test coverage).  
  – CSS state machine, easy-surface, bits 3→4→5: partial score → source-validation failure → PASS (not binary; partial unmapped to campaign PASS/FAIL totals).  
  – SQL fixed points, graph-chain 6→12→25: PASS → source-validation failure → PASS (sparse samples; middle = source-val, not demonstrated semantic/behavioral fail).  
- Heterogeneous axes (MoCo: coverage; CSS: bit count at fixed easy surface + possible class names elsewhere; SQL: chain length; Regex lengths 32/128/512 mentioned only as axis existence, **no outcome sequence claimed or inferred**). Numerical order ≠ validated difficulty order for the model.  
- Crude illustrative null: under i.i.d. binary p ≈ 0.684, P(zigzag either direction) = p(1-p) ≈ 21.6%. **Explicitly not calibrated, not a campaign null, pools unlike things, ignores partials/source-val, no sweep denominator.** Oscillation not surprising under flat model; single outcomes can zigzag even under monotonic latent p.  
- Source-validation failures ≠ semantic/task failure (diagnosis, not excuse). Truncation/length/validator/malformed hypotheses unresolved (no artifacts, lengths, limits, diagnostics in packet). Longer setting PASS does not refute truncation.  
- F-006: pass rates 0.00–1.00; bimodal flavor; zero-rate claim internally inconsistent (names 6: glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory; +1 unscored epistemic_silence/type_games). Do **not** convert unscored to zero or force “7”.  
- Judge guarantees differ; pooled PASS not identical certification. Dirty repo + incomplete model/harness/task/evaluator manifest + single seed → provenance and variability limits.  
- No common latent difficulty scale validated (nor every possible scale disproved). Within-env reversal does not prove/disprove monotonic latent. Nested tests (if true) constrain fixed submissions, not separately generated ones.  
- Finding = measurement: ordered parameter ≠ evaluator setting ≠ P(success). Sequences identify audit targets; do not locate where ability “breaks.”  
- Forward checklist (Draft 2 bullets, enriched by Draft 1 freeze-source language).

**Remove / do not introduce:**  
- Any implication of prevalence, enrichment, or “where Mercury breaks” as capability claim.  
- Regex pass/all-pass sequence or any inferred regex outcomes (both drafts already clean; keep negative mention only).  
- SQL surface-setting qualifier or any unsubstantiated matching of other tuple components.  
- CSS axis as anything but bit count at easy-surface (Drafts correct; avoid prior mis-descriptions).  
- “Hardest label” or any global ordering framing.  
- Silent reconciliation of partial score into binary PASS/FAIL or of source-val rows into scored-FAIL totals.  
- Causal language (“encountered a pocket then recovered”, “capability threshold”, “model’s ability breaks”) except to reject it.  
- Unqualified “bimodal” as precise shape; treat as descriptive summary only.  
- New numbers, new sweeps, artifact claims, or replications (none exist).  
- Over-strong “null hypothesis uncomputed” residual: both compute the crude version *with full caveats*—this satisfies the spirit; do not claim a proper design-based null.

**Qualify hard (already mostly done; enforce uniformly):**  
- All sequences = selected, single-seed, non-exhaustive. No prespecified search rule or full matched-sweep denominator in packet → cannot speak to prevalence.  
- 0.684 and 21.6% = descriptive/illustrative only.  
- Middle failures (CSS/SQL) limit competence inferences.  
- Environment heterogeneity + judge mix + attrition make pooled stats poor stand-ins.  
- Title parenthetical “(Mercury-2.5)” and one-campaign scope.  
- Importance: configuration sweep cannot locate threshold until axis, outcomes, and variation are properly measured.

**Numbers verification (all must match packet; both drafts mostly clean):**  
Confirm/retain only: 416/405/277/128/0.684/11/38/340; p≈0.684; p(1-p)≈0.216; bits 3/4/5; lengths 6/12/25; named zeros (exactly the 6); Regex lengths if mentioned (32/128/512) solely as axis. Flag any drift in final copy-edit. No other invented counts.

### 2. Figure placement and numbering
Import and refine Draft 1’s concepts (Draft 2 has none explicit). Place after relevant text. Use real rendered figures in production; captions must stress limitations.

- **Figure 1** (after “What was actually recorded” / campaign counts + matrix mention): Selected environment × difficulty-tuple rows (or schematic of the 340-row matrix). Cell labels = passes/scored; grey = unscored (not zero). Caption: “Cell labels give passes over scored cases; grey denotes unscored cases, not zero passes. Display does not enumerate all eligible three-level sweeps. Single seed-0 per selected cell.”  
- **Figure 2** (after sequences table or in “A reversal is an observation…”): MoCo visible-test sequence (and optionally schematic of the other two). Lines for legibility only. Caption: “Lines connect recorded outcomes for legibility; with seed-0 alone in each selected cell, they are not fitted pass-rate curves. Only MoCo is an unambiguous binary zigzag in the supplied description.”

No other figures. If matrix is too large, show illustrative subset or heatmap schematic with clear “not exhaustive” note. Number sequentially; reference in text.

### 3. Recommended final section structure (hybrid)
Keep Draft 2’s flow; inject Draft 1’s table framing and figures. Use clean headings. Epistemic block first (Draft 2 style, lightly enriched).

```
---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)"
date: 2026-10-16
layout: post
---
*by <span class="icon-self">StrangeTcy</span>*

[Epistemic-status dl — Draft 2 base:
- Claim: campaign does not validate difficulty labels as ordinal scale; sequences do not establish curves.
- Evidence: F-004, F-006, F-008 + matrix/axes descriptions.
- Certainty: one campaign; seed-0 per cell; no replication; dirty repo.
- Importance: separates task parameters, evaluator coverage, source validity, P(success).]

Intro (2 short paras): Inviting PASS-FAIL-PASS shape vs. reality (selected single-seed obs, some source-val). Narrower methodological finding. (Merge best sentences from both.)

## What was actually recorded
F-004 counts + scored-only caveat + 11 unscored. 340-row matrix description (units distinction). 
[Table: the three F-008 sequences — use Draft 1’s clearer “What the sequence does not establish” column or Draft 2’s “Qualification”; prefer hybrid compactness. Explicitly: only three contrasts from F-008; no exhaustive count.]
Figure 1 here.

## An axis is not a common unit of difficulty
Heterogeneous interventions (bullet or short paras: MoCo coverage, CSS bits@easy, SQL chain, Regex lengths as axis only). Order ≠ measured difficulty. Heterogeneity explains why no shared scale; does *not* explain within-env reversals. Nested-test implication limited to fixed submissions.

## A reversal is an observation, not a curve
Crude p(1-p)≈21.6% illustration + full caveats (not calibrated null, no denominator, partials, selection, heterogeneity). Prevalence unknowable without enumeration. SQL sparsity. Figure 2 (MoCo) here.
(Import Draft 1 “How surprising is a zigzag?” title spirit if desired.)

## First ask what failed
Source-val vs semantic. Unresolved truncation/etc. Judge guarantees as audit item (not established cause). Partial-score mapping absent.

## The denominator and the provenance matter
F-006 range + zero-count inconsistency (name the 6; unscored separate). Unscored missingness. One-campaign + dirty repo + incomplete manifest + single seed-0. (Merge Draft 1 freeze-source language.)

## What would make a transition claim credible?
Draft 2 checklist (5 bullets), enriched: declare qualifying sweeps in advance; freeze executed source (incl. uncommitted) + model/harness/tasks/tests/validators/limits; denser sampling around anomalies (e.g. SQL ~12) + inspect rejected source; keep source-validity / behavioral / unscored distinct with explicit denominators; replicate seeds/instances; hold other tuple elements/judges fixed or stratify.

## The finding is about measurement
Short close: sequences worth auditing; do not locate capability break. Difficulty must name a controlled change; outcomes must say what was actually judged. (Best closing sentences from both.)

*Evidence scope/note* (Draft 2 style, precise).
```

Minor heading polish OK (“Three sequences, not three curves” as subhead under recorded if it fits). Preserve definition-list epistemic. Keep HTML/icon as in drafts.

### 4. Additional corrections / production notes
- Title: Prefer Draft 2’s with “(Mercury-2.5)”.  
- Consistent “seed-0” / “single seed per selected cell” / “no replication”.  
- Table: Ensure CSS “easy-surface” and bit counts exact; SQL lengths exact; MoCo “visible-test level”; columns highlight non-establishment. Do not force binary on CSS.  
- Math: Keep the short derivation; label purely illustrative.  
- Tone: Maintain precise, non-triumphal, audit-oriented voice. Avoid anthropomorphism of the model.  
- Length/scannability: Draft 2 is longer—tighten redundant caveats slightly while retaining every limitation. Short paras, one table, two figures.  
- Final evidence note: Explicit “No additional cases were run. No new sweep enumeration, artifact inspection, or replication claimed.”  
- Copy-edit pass: Replace “fuckingly” → “actually”; verify all F- numbers; ensure no prior factual errors (regex pass, SQL surface, CSS mis-axis, hardest-label, partial reconciliation, forced F-006=7) reappear.  
- Acceptance: Meets the spirit of the 9 resubmission criteria by construction (enumeration caveats, failure-layer separation, provenance, etc.). 11 numbers are the verified packet counts above—no extras.

### 5. Response-to-review table (Stage A blocking issues → draft handling → final blueprint)

| Stage A Blocking Issue | How Draft 1 addresses | How Draft 2 addresses | Blueprint resolution (final article) |
|---|---|---|---|
| Null hypothesis uncomputed | Crude p(1-p)≈21.6% with strong caveats (not calibrated, pools unlike, binary only, no denominator) | Identical calculation + explicit “not a measured reversal rate or calibrated null”; assumptions listed | Retain illustrative calc + full caveats in “A reversal…” section. State clearly it is *not* a design-based or campaign null. Satisfies by showing why a proper one is still absent. |
| Selection effect | “Selection rule simple: report the three from F-008”; no prespecified/exhaustive count; cannot speak to prevalence | “Selected… not supplied through declared exhaustive… neither sweep denominator nor basis for unusually frequent”; calls for full matrix enumeration | Stronger of both: explicit F-008-only reporting + “prevalence unknowable”; checklist requires publish-all-eligible-sweeps before claims. No prevalence language. |
| Source-validation failures | Distinguished; not behavioral; unresolved causes (truncation etc.); PASS at larger does not settle length hyp; no artifacts | Dedicated “First ask what failed”; source-val ≠ semantic; truncation unresolved; inspect artifacts in follow-up; judge guarantees | Dedicated section + checklist item “Separate failure layers… inspect artifacts”. Never equate to task-competence failure. |
| Causal overreach | “Do not locate where a model’s ability breaks”; “not estimates of a response curve”; “before a difficulty transition can be measured…” | Title irony + “does not establish… curves”; “not that harder problems secretly become easier”; “do not yet tell us where… breaks”; checklist for credible claim | Title retained as hook; body relentlessly measurement-focused. All capability/threshold/valley language rejected or heavily qualified. Closing: audit targets only. |
| Latent difficulty | Labels not validated ordinal; axes change different things; numerical order ≠ difficulty for model; shared x-axis unjustified | “Archive does not establish… validated ordinal scale”; axes different mechanisms; “neither validates common latent… nor disproves every possible”; order without measured effect | Core claim in epistemic + dedicated axes section + closing. “Difficulty” must name controlled change. No latent-scale assertion. |

**Unsupported / other Stage A notes addressed:** Both drafts (and blueprint) avoid the listed factual errors. Numbers are packet-grounded. Draft 2’s checklist + Draft 1’s freeze/provenance language directly support the 9 acceptance criteria for any resubmission/follow-up. No new evidence claimed.

**Final synthesis directive:** Produce the article from Draft 2 base + imported figures/table framing/F-006 precision/freeze language from Draft 1 + the section order and claim filters above. After draft, perform a numbers + limitation audit against the evidence packet. The result will be a high-certainty accounting piece that correctly reframes “non-monotonic transitions” as a caution about unvalidated axes and single-seed observations. 

This blueprint resolves all blocking issues, preserves intentional tokens, and yields a coherent, evidence-strict final post.

&&&&&&&&&&&&&&&&&&&

gemini 3.1 pro grounding:

Here is the editorial blueprint for the final article, combining the rigorous analytical framing of Draft B with the tighter prose and visual structure of Draft A.

### 1. Base Draft Selection
**Draft B (gpt 6.1 sol max) should be the base draft.** 
Draft B handles the Stage A blocking issues and factual errors much more rigorously. It explicitly refuses to infer a regex outcome sequence, correctly identifies that SQL has no documented surface setting, refuses to force the CSS partial score into a binary `PASS/FAIL` bucket, and explicitly deconstructs the `[d-word]` sweep denominator problem.

### 2. Elements to Import from Draft A
While Draft B is methodologically superior, Draft A contains structural elements that should be ported over:
*   **The Opening Hook:** Import Draft A’s punchy opening paragraph ("A middle setting fails; the settings on either side pass. Connect the points and it looks as though Mercury-2.5 encountered a pocket of difficulty...").
*   **The Figure Program:** Draft B lacks explicit figure calls. Import Draft A’s `Figure 1` and `Figure 2` placements, including their excellent, heavily qualified captions (e.g., "Lines connect recorded outcomes for legibility... they are not fitted pass-rate curves").
*   **The Epistemic Status Formatting:** Draft A's definition-list format for the Epistemic Status block is slightly cleaner and less repetitive. Combine Draft A's layout with Draft B's content.

### 3. Claims to Retain, Remove, or Qualify
**Retain:**
*   All 11 verified numbers: 416 selected cases, 405 scored, 277 `PASS`, 128 `FAIL`, 0.684 rate, 38 environments, 340 matrix rows, 11 unscored cases, 7 bimodal claim vs. 6 named zeros, and the 21.6% calculation.
*   The fundamental distinction between a *source-validation failure* (pipeline rejection) and a *semantic failure* (failing to solve the task).
*   The bracketed intentional tokens (e.g., `[d-word]`). *Do not remove or alter these.*

**Remove:**
*   **Profanity:** Both drafts contain accidental intrusive profanity ("fuckingly"). Remove this from Draft A’s body text ("task fuckingly presented", "what was fuckingly judged") and Draft B’s section header ("What was fuckingly recorded").
*   **Causal Attribution:** Remove any lingering implication that the middle settings caused the failures. The single-seed (seed-0) constraint makes this unprovable.

**Qualify:**
*   **The 21.6% Null Calculation:** Keep Draft B’s extremely strict qualification. The 21.6% figure is a *hypothetical illustration* to show that flat probabilities can generate zigzags; it is **not** a calibrated null hypothesis for the campaign.
*   **The F-006 Discrepancy:** Maintain Draft B’s precise handling of the environment count. The campaign claims 7 bimodal zeroes, but only names 6, with the 7th being *unscored*. It must remain strictly qualified that an unscored case is not a measured zero.

### 4. Figure Placement and Numbering
*   **Figure 1 (Matrix rows vs. sweeps):** Place in the first main section ("What the campaign recorded"). Use Draft A's caption to emphasize that grey cells denote *unscored* cases, not zero passes, and that the matrix is for locating outcomes, not displaying enumerated sweeps.
*   **Figure 2 (The three sequences):** Place immediately after the sequence table. Use Draft A's caption warning that these lines are visual connectors, not statistical trendlines.

### 5. Section Structure
The final piece should follow this merged structure:
1.  **Header & Epistemic Status** (Draft A layout + Draft B content).
2.  **Introduction** (Draft A hook + Draft B thesis on ordinal scales).
3.  **What the Campaign Recorded** (Cleaned header from Draft B; include 416/405 stats, 340 rows, and Figure 1).
4.  **Three Sequences, Not Three Curves** (Draft B's sequence table showing "Qualification" instead of Draft A's broader text). Include Figure 2.
5.  **An Axis is Not a Common Unit of Difficulty** (Draft B's breakdown of test coverage vs. bit counts vs. chain lengths, avoiding the regex/SQL surface errors).
6.  **A Reversal is an Observation, Not a Curve** (The 21.6% math and the lack of a `[d-word]` denominator).
7.  **First Ask What Failed** (Draft B's excellent handling of source validation vs. semantic test failure).
8.  **The Denominator and Provenance Matter** (F-006 bimodal discrepancy, 11 unscored cases, dirty repo context).
9.  **What Would Make a Transition Claim Credible?** (Draft B's bulleted checklist for future audits).

### 6. Additional Corrections Needed
*   **CSS and SQL Guardrails:** Ensure Draft B's strict parameters survive the edit. CSS must be framed as a *mixed-status* sequence (partial $\rightarrow$ source-validation failure $\rightarrow$ PASS), not a binary pass/fail curve. SQL must *not* be assigned a surface-level qualifier.
*   **Tone Check:** Ensure the article reads as a methodological audit of *measurement frameworks*, rather than a debunking of the model's capabilities. 

***

### 7. Response-to-Review Table

| Stage A Blocking Issue | Draft A Approach | Draft B Approach | Final Synthesis Plan |
| :--- | :--- | :--- | :--- |
| **1. Null hypothesis uncomputed** | Computes 21.6% flat-rate probability and notes it is an "artificial no-level-effect model." | Computes 21.6%, explicitly calls it out as *not* a calibrated null, and lists assumptions violated (heterogeneity, independence). | Use Draft B's rigorous breakdown. Present the math as a hypothetical proof-of-concept, not a baseline finding. |
| **2. Selection effect** | Notes that the 3 sweeps were "explicitly identified" with no prespecified search rule or denominator. | States there is no `[d-word]` sweep denominator and no exhaustive matched sweep procedure was followed. | Use Draft B. Emphasize that finding 3 reversals out of 340 rows without a pre-registered search rule is an observation, not a prevalence metric. |
| **3. Source-validation failures** | Identifies CSS/SQL middle points as pipeline failures, not behavioral task failures. | Dedicates a section ("First ask what failed") to separate contract failures (rejection) from competence/semantic failures. | Use Draft B. Highlight the "truncation/length" hypothesis as plausible but unverified due to missing artifact diagnostics. |
| **4. Causal overreach** | Notes that the single seed-0 run gives no estimate of whether a result would recur. | Explicitly warns against attributing middle-case failures directly to "difficulty" or truncation without controlled reproduction. | Use Draft B. Emphasize that single-seed, un-replicated results with mixed judge guarantees preclude causal claims. |
| **5. Latent difficulty scale unsupported** | States the axis changes test coverage/size/surface, explaining why a shared x-axis is unjustified. | Argues an ordered parameter (bits, length) does not automatically map to a measured probability of model success. | Merge both. Use Draft A's specific examples (test coverage vs. surface) paired with Draft B's conceptual framing of ordinal parameters. |

&&&&&&&&&&&&&&&&&&&&&&&


fable 5.1:

# Editorial Blueprint — POST-03 "Where Mercury Breaks"

*Note on the packet as received: the two drafts were spliced into the middle of the Stage A findings list (between "latent difficulty" and "unsupported"), and the `[CANDIDATE DRAFTS]` block was empty. I have read the drafts from where they landed and reconstructed the fifth blocking issue as "latent difficulty unsupported." If that reconstruction is wrong, the response-to-review table needs one row revised.*

---

## 1. Verdict: base draft

**Use Draft 2 (gpt 6.1) as the base. Import figures, the epistemic-status block, and several sentences from Draft 1 (gpt 6). Cut Draft 2 by roughly 25–30%.**

| Criterion | Draft 1 (gpt 6) | Draft 2 (gpt 6.1) |
|---|---|---|
| Coverage of 5 blocking issues | 4 of 5 handled; judge-guarantee confound and MNAR missingness only glanced at | All 5 handled in dedicated sections |
| Six Stage A factual errors | All avoided (regex, SQL surface, CSS axis, "hardest label", partial score, F-006 count) | All avoided, and most are *explicitly* corrected rather than silently omitted |
| Figures | Two (image embeds broken — see §6) | None |
| Length / discipline | ~1,100 words, tight | ~2,000 words, repetitive (single-seed caveat stated ~6 times) |
| Epistemic-status block | Better: "Certainty" gives an actual confidence split (high for counts, low for effects) | Weaker: "Certainty" lists limitations instead of a level |
| Title | Omits "(Mercury-2.5)" | Matches POST-03 spec |
| Strongest unique content | Visible-test coverage "has no direction" argument; explicit selection-rule statement; closing cadence | Nested-test-suite / fixed-submission argument; "contract failure ≠ semantic failure" distinction; MNAR hedge; enumeration recipe; follow-up checklist |

Draft 2 wins on completeness against a review that produced 5 blocking issues and 9 acceptance criteria; the cost is verbosity, which is cheaper to fix than missing coverage.

---

## 2. Elements to import from Draft 1 into the Draft 2 base

| Import | Where it goes | Why |
|---|---|---|
| `<dl>` epistemic-status block (fields: Original ideas / Synthesis / Prose / Certainty / Importance) — keep D1's **Certainty** text verbatim; replace D1's "Original ideas" text with D2's "Claim" sentence | Front matter | D1's certainty split is the honest statement; D2's "Claim" sentence is the better thesis |
| "Visible-test coverage does not even specify a direction without knowing how the changed tests affect the information available to the solver and the conditions checked." | §4 (axis section), MoCo bullet | Sharpest single point in either draft; D2 lacks it |
| "For this essay, the selection rule is simple: report the three contrasts explicitly identified in F-008. The packet gives neither a prespecified search rule nor an exhaustive count…" | §3 opening | D2 says the procedure was undeclared but never states what rule *this post* uses; Stage A's selection-effect issue needs that explicit |
| Table column "What the sequence does **not** establish" | §3 table — merge with D2's "Qualification" column | D1's negative-space framing is more disciplined |
| "Even if an environment's *underlying* chance of success decreased steadily… one outcome per setting could still zigzag. The MoCo trace neither proves nor rules out such a decrease." | §5 | Cleaner than D2's equivalent |
| "A pass at the larger CSS bit count or SQL chain length does not settle a response-length hypothesis, because generated source length need not increase with the nominal task-size setting." | §6 | D2 says this in two sentences; D1 in one |
| "Denser SQL lengths around 12 and the rejected source itself would be better evidence about that case than a line drawn from 6 through 12 to 25." | §8 or close | Concrete, memorable |
| Closing two sentences ("…identify cases worth auditing. They do not locate where a model's ability breaks…") | §9 | Better cadence than D2's ending; pair with D2's "an ordered parameter, an evaluator setting, and an estimated probability of success are different things" |
| Figures 1 and 2 (rebuilt — see §5) | §2 and §3 | D2 has none |

---

## 3. Claims: retain / qualify / remove

### Retain as-is (both drafts agree, consistent with packet)
- 416 selected / 405 scored / 277 PASS / 128 FAIL / 0.684 **among scored** / 38 environments; 11 unscored = 416 − 405.
- 340-row environment × difficulty-tuple matrix; rows ≠ cases ≠ eligible sweeps.
- The three F-008 sequences, with CSS described as *partial → source-validation failure → PASS*, not as a binary zigzag.
- Only MoCo is an unambiguous binary reversal.
- No SQL surface qualifier; no regex outcome sequence inferred.
- F-006: six named zero-rate environments plus one unscored entry; the "seven" is not seven measured zeros; unscored ≠ zero.
- p(1−p) ≈ 21.6% crude calculation, labelled as not a calibrated null.
- Dirty repo: a clean commit reference does not reconstruct executed source.
- Seed-0 only: no replicated variability estimate.

### Qualify / tighten
| Claim | Action |
|---|---|
| The 21.6% figure | Add the one-sided number: P(PASS→FAIL→PASS specifically) = p²(1−p) ≈ **14.8%**. State both. Add one sentence that, because F-006 shows bimodal environment rates, the *within-environment* p is what matters: an environment near p≈0.5 produces a zigzag 25% of the time, one near 0.95 about 5%. If the matrix supplies MoCo's own scored pass rate, use it as the secondary p (see verification list). |
| "The packet does not identify the middle failure's stage" (MoCo, D2) | The matrix has a `failure_modes` field. **Before publication, look up the MoCo FAIL row and the CSS/SQL middle rows.** If the field is populated, report it; if not, keep the sentence and say the field was empty for that row. Do not publish "not identified" without having checked. |
| "CSS varies class names and bit counts"; "Regex: 32, 128, 512 characters" | Both drafts assert these axis definitions; neither is in the evidence packet summary I was given. Verify against the packet's axis descriptions. If unverifiable, drop class names and the regex lengths entirely (the regex mention adds nothing once no outcome sequence is claimed). |
| `epistemic_silence/type_games` as the seventh F-006 entry (D2 only) | Verify the name against F-006. If confirmed, keep (it's more useful than D1's anonymous "an additional entry"). |
| "The campaign has mixed [judge] guarantees" (D2) | Verify from the matrix `judge_guarantees` field that values actually vary. If they do, keep D2's hedge that no guarantee is shown to change *along any quoted sequence*. |
| "potentially missing not at random" (D2) | Keep, but cut to one sentence. The hedge is correct; the paragraph is long. |
| Truncation / output-budget hypothesis | Keep as one named hypothesis among others (malformed source, validator interaction). Both drafts already do this correctly. |
| Title "Where Mercury Breaks" | The post argues against the title's literal reading. Keep the title (POST-03 slug) but make the lede disclaim it within three sentences, as D2 does. Optional: author may add a question mark. Flag for author decision. |

### Remove
- D2: "Preserving the CSS description does not add another category to those totals; it acknowledges…" — compress to one clause inside the table's qualification cell.
- D2: "No probabilistic threshold is detected here." — ambiguous; delete.
- D2: "These are proposed checks, not analyses already completed. Their purpose is to turn…" — redundant with the section heading; delete.
- D2: "Nor do the examples, by themselves, establish that every other component of each difficulty tuple was matched." — true but already implied by the enumeration recipe; move into a parenthetical there.
- D2: at least four of the six restatements of "single seed / no replication." Keep it in the epistemic status, once in §2, once in §7, and once in the close.
- D1: "Lines connect recorded outcomes for legibility" (Figure 2 caption) — don't draw lines you then have to disclaim. See §5.

---

## 4. Section structure for the final

Target ≈ 1,600–1,800 words plus figures.

0. **Front matter** — D2 title (with "(Mercury-2.5)"), date, D1 `<dl>` block with hybrid fields.
1. **Lede (3 paragraphs max)** — D2's "Pass, fail, pass is an inviting shape" opening, then the thesis sentence (D2's bolded "does not establish that its difficulty labels form a validated ordinal scale"), then D1's "narrower finding is more useful" paragraph. Cut D2's fourth and fifth lede paragraphs.
2. **What the campaign recorded** — counts; scored-only denominator; matrix structure; rows ≠ sweeps. **Figure 1** here.
3. **Three sequences, not three curves** — D1's explicit selection rule; merged table (Environment / Setting varied / Recorded sequence / What it does not establish); "only MoCo is a binary zigzag"; CSS partial-score note. **Figure 2** here.
4. **An axis is not a common unit of difficulty** — D2's bullets minus unverified axes; D1's "no direction" sentence under MoCo; D2's nested-suite / fixed-submission paragraph; "neither validates nor disproves."
5. **How surprising is a zigzag?** — the calculation (21.6% two-sided, 14.8% one-sided); why pooled p is wrong given bimodality; D1's "underlying decrease could still zigzag"; D2's enumeration recipe; no denominator → no prevalence claim. **Figure 3 (optional)** here.
6. **First ask what failed** — D2's section trimmed by half; contract-failure-is-still-a-failure point; truncation hypothesis unresolved; `failure_modes` lookup result; judge-guarantee confound as audit item, not explanation.
7. **The denominator and the provenance** — F-006 tally; 11 unscored with one-sentence MNAR hedge; dirty repo; seed-0; model label ≠ checkpoint manifest.
8. **What would make a transition claim credible** — D2's five bullets, each cut to two sentences; end with D1's "denser SQL lengths around 12" sentence.
9. **Close** — D2's "ordered parameter / evaluator setting / estimated probability are different things" + D1's final two sentences.
— *Evidence-scope footer*: D2's italic footer, verbatim.

---

## 5. Figures: placement, numbering, and redesign

| Fig. | Placement | Content | Required changes vs. Draft 1 |
|---|---|---|---|
| **1** | End of §2 | Environment × difficulty-tuple heatmap or per-environment strip of scored pass rate | (a) State the row-selection rule in the caption, or show all 38 environments (38 rows is displayable). (b) Use **three** visual states: pass fraction, measured 0.00, and *unscored* — the caption must not let grey be read as 0.00, because the F-006 tally dispute is exactly about that. (c) Cell labels as `passes/scored` (D1's convention is good). |
| **2** | End of §3 | Three small panels — MoCo, CSS, SQL — categorical markers on an x-axis of the varied setting | (a) **No connecting lines.** Markers only, with distinct glyphs for PASS / FAIL / source-validation failure / partial score. (b) SQL x-axis at true spacing (6, 12, 25), not evenly spaced, so the sparse sampling is visible. (c) Caption: "One seed-0 outcome per cell; these are observations, not curves." |
| **3** (optional) | §5 | Curve of p(1−p) and p²(1−p) over p ∈ [0,1], with 0.684 marked | Cheap, and makes the "zigzag is unremarkable near p=0.5" point without prose. Drop if the post is running long. |

Both D1 image embeds are broken (`!` on its own line — the `![alt](path)` collapsed). Rebuild from source data, not from the D1 markdown.

---

## 6. Additional corrections

1. **Unbracketed substitution artifact.** The string "fuckingly" appears three times (D1: "task fuckingly presented," "what was fuckingly judged"; D2: heading "What was fuckingly recorded"). Context in all three implies the original word was *fuckingly*. This is **not** in the author's bracketed `[x-word]` convention, so I'm flagging it as a probable find-and-replace artifact rather than an intentional token. Either restore the word or convert to the bracketed form — author's call, but it cannot ship as-is in a heading. (`[d-word]` ×2 in D2 is left untouched per instructions.)
2. **D2 epistemic "Certainty" field** describes limitations, not a confidence level. Replace with D1's text.
3. **Table heading in D2**, "Reported ordering" → "Setting varied" (D1), since "ordering" presupposes the thing the post disputes.
4. **D1 Figure 2 caption** says "comparisons" (plural) for what F-008 presents as one sequence. Verify the number of MoCo visible-test sequences in the matrix; if there is only one, singular.
5. **Consistency of outcome vocabulary.** Settle on `PASS` / `FAIL` (code-formatted) for the campaign's binary categories and plain "source-validation failure" / "partial score" for the non-binary ones, throughout. D2 mixes "PASS–FAIL–PASS" and "pass–fail–pass."
6. **Numbers requiring verification before publication** (reconstructing Stage A's list of 11 from what the drafts assert):

| # | Number | Source claimed | Status |
|---|---|---|---|
| 1 | 416 selected | F-004 | packet ✓ |
| 2 | 405 scored | F-004 | packet ✓ |
| 3 | 277 PASS | F-004 | packet ✓ |
| 4 | 128 FAIL | F-004 | packet ✓ (277+128=405 ✓) |
| 5 | 0.684 | F-004 | 277/405 = 0.6840 ✓ |
| 6 | 38 environments | F-004 | packet ✓ |
| 7 | 340 matrix rows | packet | ✓ |
| 8 | 11 unscored | derived | 416−405 ✓ |
| 9 | 3/4/5 bits; 6/12/25 lengths | F-008 | packet ✓ |
| 10 | 32/128/512 regex lengths | drafts | **not in packet summary — verify or drop** |
| 11 | 21.6% (and 14.8%) | derived | 0.684×0.316=0.216 ✓; 0.684²×0.316=0.148 ✓ |
| + | 6 named zero envs + `epistemic_silence/type_games` | F-006 | names of six are in both drafts; seventh name **verify** |
| + | 0.00–1.00 range | F-006 | packet ✓ |
| + | "mixed judge guarantees" | matrix | **verify field varies** |

---

## 7. Response-to-review table (Stage A blocking issues)

| Stage A blocking issue | Draft 1 | Draft 2 | Blueprint resolution |
|---|---|---|---|
| **1. Null hypothesis uncomputed** | Computes p(1−p) ≈ 21.6%; labels it "deliberately crude," "not calibrated." Notes no denominator of eligible sweeps. | Same calculation with the algebra shown; same disclaimer; adds that independence and binary-ness are unverified. | Keep the calculation; add the one-sided 14.8%; add the within-environment-p point tied to F-006 bimodality; add optional Fig. 3. State plainly that a *real* null requires the sweep enumeration, which was not done. |
| **2. Selection effect** | Explicit: "the selection rule is simple: report the three contrasts in F-008"; no prespecified search; prevalence unknowable. | Says examples were "not supplied through a declared exhaustive selection procedure"; gives the enumeration recipe (fix env + non-varied tuple components, enumerate all orderings, retain incomplete/unscored groups). | Import D1's explicit rule sentence into §3; keep D2's recipe in §5. Add the parenthetical that even "complete scored triples only" would itself be a selection on missingness. |
| **3. Source-validation failures** | "Failures of the end-to-end pipeline, not observations that valid code failed a behavioral check"; truncation one hypothesis among several; no artifacts to adjudicate. | Full section: contract failure is still a failure, but ≠ semantic failure; truncation unresolved in both directions; artifact inspection is the follow-up. | Use D2's section cut by half; import D1's "source length need not increase with task size" sentence. **Add the `failure_modes` lookup result** for the three middle rows. |
| **4. Causal overreach** | "Explains why a shared axis is unjustified. It does **not** explain why the middle MoCo cell failed." Closing: cases "worth auditing," not a located break. | "Heterogeneity does not explain the within-environment reversals"; judge guarantees are "a possible confound to audit — not an established explanation"; "the failure label identifies a category, not its cause." | Keep all three D2 sentences; use D1's closing. Title retained with immediate disclaimer in lede; author may add "?". No sentence in the final may attribute any middle-cell outcome to a cause. |
| **5. Latent difficulty unsupported** | Bits/lengths/characters have numerical order, but whether they impose increasing difficulty *on this model* is unmeasured; visible-test coverage has no inherent direction. | "An axis is not a common unit"; nested-suite implication holds only for a fixed submission, not across separately generated ones; archive "neither validates a common latent difficulty scale nor disproves every possible one." | §4 = D2's structure + D1's direction sentence + D2's fixed-submission paragraph. Remove unverified axis definitions (class names, regex lengths) so the section asserts only what the packet documents. |

**Six Stage A factual errors — status in both drafts:** regex pass claim (absent in both ✓), SQL surface qualifier (absent in D1, explicitly denied in D2 ✓), CSS axis (both correctly say bit count at fixed easy surface ✓), "hardest label" framing (absent in both ✓), partial-score reconciliation (both refuse to map it to PASS/FAIL ✓), F-006 count (both separate six zeros from one unscored ✓). None need re-correction; the final should keep D2's explicit denials rather than D1's silent omissions, since the review will check for them.

---

## 8. One-line summary for the author

Draft 2's skeleton and its five-issue coverage, Draft 1's figures, epistemic block, selection-rule sentence, "no direction" argument, and ending; cut 500 words of repetition; fix the three "fuckingly" artifacts and the broken image embeds; verify the regex lengths, the CSS class-name axis, the seventh F-006 name, and the judge-guarantee variation before anything ships; and check the matrix's `failure_modes` field for the three middle cells so the post doesn't claim ignorance of something the data records.
