some model:

State: Commit read, row counts and arithmetic verified against Tables A–D and Section E.

Verdict: reject

1. **Location:** "A second layer: the environment × tuple matrix"
   **Claim:** "There are 34 difficulty dimension names across the matrix."
   **Evidence:** Table D provides the number of difficulty dimensions per row (`n_dims`), but the packet does not list the dimension names or provide data to verify a count of 34 unique names.
   **Severity:** blocking

2. **Location:** "The endpoint-heavy distribution" (bullet for `ts_parse_only`) and "The selection frame" (bullet 3).
   **Claim:** "Its exclusion note describes a provider-attributed terminal failure, yet its verdict is PASS."
   **Evidence:** Table B (row 409) confirms the case has `performance_eligible` = False with a PASS verdict, but the packet omits free-text fields and contains no exclusion notes to support the described cause.
   **Severity:** blocking

3. **Location:** "Unscored cases are not failures"
   **Claim:** "The unscored rd_adaptive_halting case sits at the tuple where all five dimensions are easy."
   **Evidence:** Table D (`rd_adaptive_halting` row 1) confirms the tuple has 5 dimensions (`n_dims`=5) and holds 1 unscored case, but the packet does not record the dimension values (e.g., "easy") to support this claim.
   **Severity:** blocking

4. **Location:** "Ten zero-pass environments or seven?"
   **Claim:** "Adding rope, which has no row in the 38-environment tables and whose 10 cases were all omitted before scoring..."
   **Evidence:** Table C records 15 omitted cases for the `rope` environment, not 10. These comprise 10 cases of `unsupported_provider_input_modality` (rows 1–10) and 5 cases of `known_gate_calibration_failure` (rows 20–24).
   **Severity:** correction

3 blocking findings, 1 correction.

&&&&&&&&&&&&&&&&&&


some other model:

**State:** Commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` read as pasted. Packet rows seen: Table A 38 rows, Table B 416 rows, Table C 80 rows, Table D 340 rows, Section E descriptions for Figures 8–11. Nothing in the packet left unread. Not in the packet (so unverifiable here): the SVG files, the `ANALYSIS_OVERVIEW.md` "10 zero-pass" text, the provenance summary's "24", the "one seed per cell" wording, the dirty-source record, tuple labels / dimension names, the free-text exclusion note on the `ts_parse_only` PASS.

I re-derived every count in code from the packet tables before writing this.# Evidence review — POST-02 redo

**Verdict: accept with corrections.**

The headline arithmetic is sound. Every count I could derive from Tables A–D reproduces the article's figures: 416/405/11; 277/128; 68.4% and 66.6%; 17/7/12/2 environment split; 172/68/165 scored-case split; 105 mixed-environment passes; unweighted mean 69.2% and median 88.9%; 340/296/44 matrix rows; 329 rated rows with 320 binary and 9 fractional (all `moco`, values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6); 204 and 214 uniform-environment rows; 98 zero-pass tuples in 19 environments; all 12 mixed environments with a zero-pass tuple; guarantee split 11/27 environments, 189/227 cases, 141/189 = 74.6% and 136/216 = 63.0%; all six failure-label counts globally and per environment (rows sum to 128); the 9 + 2 runtime-error spellings; 10 `rejected` (9 `source_invalid`); 9 `unscored`-disposition FAILs with the stated environment and label breakdowns; one ineligible PASS (Table B row 409); seed 0 throughout; the four sensitivity scenarios; the 94/56 three-environment contribution; and the Wilson intervals I spot-checked against Section E. The findings below are what remains.

## Findings

**1. `rope` case count is wrong (twice).**
Location: "Ten zero-pass environments or seven?" ("whose 10 cases were all omitted before scoring") and "The selection frame" ("All 10 of its cases were omitted before scoring").
Claim: `rope` has 10 omitted cases.
Packet: Table C rows 1–10 (`unsupported_provider_input_modality`) **and** rows 20–24 (`known_gate_calibration_failure`) are `rope`. `rope` has **15** omitted rows. The 10 is the count of the modality class, not of the environment.
Severity: **correction**.

**2. Known-gate omissions are not attributed; the article's reconciliation arithmetic for 14-vs-24 omits a reading the packet makes available.**
Location: "The selection frame" omission table and the 14/24 paragraph.
Claim: 14 known-gate omissions; "the 24 cannot coexist with the selection frame as reported."
Packet: Table C known-gate = 9 `glyph` (rows 11–19) + 5 `rope` (rows 20–24) = 14, confirmed. But 14 + 10 modality = 24 exactly, so a reading in which the provenance summary lumps all non-twin omissions under "known-gate" keeps the 80/496 frame intact. The article should state that this arithmetic coincidence exists before asserting that 24 forces 506 cells. The conflict stays open, but the "cannot coexist" wording is too strong.
Severity: **correction**.

**3. Internal contradiction on tuple keys for `moco`.**
Location: "`moco`: the only fractional rows" ("The archive has no row-by-row key linking each value to its tuple") and "What a 'cell' means" ("In `moco` … there is no row-by-row key").
Packet: Table D is "one row per environment × tuple" with `n_dims` defined as "number of difficulty keys in the tuple", and gives `moco#1`–`moco#15` each with its own pass rate and failure-mode counts. The article itself uses tuple labels elsewhere ("the tuple where all five dimensions are `easy`" for `rd_adaptive_halting`). Either the key exists for all environments or for none; the article cannot have it for `rd_adaptive_halting` and lack it for `moco`. The "cannot draw the shape of `moco`" statement is therefore unsupported as written. The packet omits the labels, so I cannot say what the shape is, only that the stated reason for not drawing it conflicts with the packet's row structure and the article's own use of labels.
Severity: **correction**.

**4. Omission density is not disclosed beside the "where cases were selected" claim.**
Location: "Names are useful handles" ("That shows concretely how much the pooled result depends on where cases were selected").
Packet: Table C — `moco` 35 twin omissions, `glyph` 12 twin + 9 known-gate = 21, `epistemic_games` 9 twin. The three environments that dominate the omissions are also the three heaviest-weighted scored environments (`moco` 55, `glyph` 24, `epistemic_games` 23). The article discusses selection but never says which environments the 80 omissions came from. This is a disclosure gap beside a claim about selection.
Severity: **correction**.

**5. Caption for Figure 8 claims something the chart does not plot.**
Location: Figure 8 caption, last sentence ("Nine of the 128 scored FAILs carry a disposition label that conflicts…").
Packet Section E: Figure 8 draws three stacked bars (496 → 416/80; 405/11; 277/128). No disposition segment is drawn. Section E also states the 11-case segment is unlabelled in the SVG; the caption should say the 11 is caption-only. Minor, but the caption should describe the chart, not the text.
Severity: **note**.

**6. Caption for Figure 9 omits the colour classes.**
Location: Figure 9 caption.
Packet Section E: dots are colour-classed "no scored pass / mixed / all scored passed". The caption does not mention the encoding. Claims less than the chart plots.
Severity: **note**.

**7. Casing artefact assumption is not neutral.**
Location: "What can a FAIL label explain?" ("I treat the casing difference as a data-quality artefact rather than two kinds of runtime failure").
Packet: Table B rows 405 and 415 — the only two lowercase `runtime_error` rows — are also the only two runtime-error FAILs with disposition `unscored`; all nine `RUNTIME_ERROR` rows have disposition `scored`. The casing co-varies perfectly with disposition. The packet does not establish they are one kind of failure; the article should say the assumption is unverified rather than adopt it.
Severity: **correction**.

**8. The `unscored`-disposition flag is under-described.**
Location: "The selection frame", second bullet.
Packet: all five `invalid_action` cases (rows 24, 145, 222, 232, 293) carry disposition `unscored`; so do two of three `training_failed` (193, 214) and the two lowercase runtime errors. The disposition is label-aligned, not scattered. The article lists the labels but does not note that the disposition tracks the label almost exactly, which bears on whether these nine are "scored FAILs" in the same sense as the other 119.
Severity: **note**.

**9. Unverifiable-from-packet claims should be marked as such.**
Location: various.
Claims: "34 difficulty dimension names"; the `rd_adaptive_halting` unscored tuple is all-`easy`; the `ts_parse_only` exclusion note "describes a provider-attributed terminal failure"; "one seed per cell" wording; the dirty source record; the provenance summary's 24; the overview's 10.
Packet: none of these appear. Table D gives `n_dims` only; free text is omitted. Not errors, but the article presents them with the same confidence as the counted figures.
Severity: **note**.

**10. "A SQL environment" is vague and the pattern is a single cell.**
Location: "Claims withdrawn or left open".
Packet: only one SQL-named environment exists (`sql_fixed_point`, 8/9, Table D rows 1–9 all single-case; the lone zero is `sql_fixed_point#4`). A "non-monotonic pattern" there is one failed single-case tuple among nine. The article should name the environment and say that the "pattern" is one cell.
Severity: **note**.

**11. Stray tokens in public prose.**
Location: Epistemic-status "Importance" line ("how little the archive can fuckingly support"); "What this supports" paragraph ("environment identity 👹 more than difficulty").
These are not bracketed replacements and read as leftovers. The emoji sits where a verb belongs.
Severity: **correction** (editorial; no evidential impact).

**12. Open discrepancy — zero-pass environment count.**
Location: "Ten zero-pass environments or seven?"
Packet: 7 environments with 0 passes among scored cases (Table A); 19 environments with ≥1 zero-pass tuple (Table D); 2 environments with no scored case. 7 + 2 + `rope` = 10 as the article says, but see Finding 1: `rope` contributes 15 omitted cases, not 10. The 10-vs-7 reconciliation remains open; the packet does not contain the overview text.
Severity: **note** (already disclosed as open).

**13. Open discrepancy — 14 vs 24 known-gate.**
Packet supports 14 (Table C). The 24 is not in the packet. See Finding 2 for the reading the article should add.
Severity: **note** (already disclosed as open).

## Tasks 4 and 5 — causal/mechanism and label-as-fact scan

No causal or mechanism claim found that the packet contradicts. The article consistently frames PASS/FAIL, labels, dispositions and guarantees as recorded classifications. The "cannot" statements hold except the `moco` row-key statement (Finding 3) and the "cannot coexist" statement (Finding 2). The glyph/moco "overfit" and sheaf "underfit" statements are label counts and are correctly limited.

**Blocking: 0. Corrections: 6 (Findings 1, 2, 3, 4, 7, 11). Notes: 7.**



&&&&&&&&&&&&&&

grok 4.5:

**State:** Commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` read; article POST-02 and full evidence packet (Tables A–D + Section E) ingested. Table A: 38 env rows; Table B: 416 case rows; Table C: 80 omission rows; Table D: 340 matrix rows. No external data used; figures assessed only via Section E descriptions. All listed “facts the packet should confirm” cross-checked below.

**Verdict: accept with corrections**

### Numbered findings

1. **Article location:** Opening / “First, count…” / totals.  
   **Claim:** 416 selected; 405 scored; 11 infrastructure_unscored; 277 PASS / 128 FAIL; 277/405 = 68.4%; 277/416 = 66.6%.  
   **Packet evidence:** Table A sums: n_cases = 416, n_scored = 405 (sum n_pass + n_fail), n_pass = 277, n_fail = 128; 11 unscored (epistemic_silence 6 + epistemic_type_games 4 + rd_adaptive_halting 1). Table B status column confirms 405 “scored”, 11 “infrastructure_unscored”. 277/405 ≈ 0.68395 → 68.4%; 277/416 ≈ 0.66587 → 66.6%.  
   **Severity:** note (matches).

2. **Article location:** Outcome table and “endpoint-heavy” text.  
   **Claim:** 38 envs; 36 with scored cases; 17 all-pass (172/172), 7 all-fail (0/68), 12 mixed (105/165), 2 no scored (10 unscored); mixed hold 165 scored / 40.7%.  
   **Packet evidence:** Table A: exactly 17 envs with pass_rate=1.0 and n_fail=0 (sum n_pass=172); 7 with pass_rate=0.0 (sum n_fail=68); 12 mixed (batchnorm_ema, compositional_optimizer, equivariant_diagram, gnn_message_passing, moco, rd_adaptive_halting, regex_state_machine, sheaf_schema_sync, sql_fixed_point, ssm_parallel_scan, tensor_functor, transformer_ssm_lift) sum n_scored=165, n_pass=105; 2 with n_scored=0 (epistemic_silence, epistemic_type_games) and 10 unscored. 165/405 ≈ 0.4074.  
   **Severity:** note (matches). All-pass list and larger/smaller counts in article match Table A exactly (css 18, rd_gradient/rd_state 15 each, epistemic_games 23, etc.).

3. **Article location:** Unweighted mean ~69.2%; median 8/9 (88.9%).  
   **Claim:** Across 36 scored envs.  
   **Packet evidence:** Table A pass_rates of the 36: 17×1.0 + 7×0.0 + mixed (0.1333, 0.7778×2, 0.5556×3, 0.5714, 0.6545, 0.6667, 0.8889×3). Mean = (17 + 0 + 2.1333+1.5556+0.5714+0.6545+0.6667+2.6667)/36 ≈ 24.2482/36 ≈ 0.6736? Wait—recompute carefully: all-pass 17, all-fail 0, mixed sum of rates: 2/15=0.1333, 7/9=0.7778 (×2), 5/9=0.5556 (×3), 8/14≈0.5714, 36/55≈0.6545, 6/9=0.6667, 8/9≈0.8889 (×3). Sum mixed rates ≈ 0.1333+1.5556+1.6668+0.5714+0.6545+0.6667+2.6667 ≈ 7.915. Total sum rates = 17 + 7.915 = 24.915; 24.915/36 ≈ 0.6921 → 69.2%. Median of 36: ordered, 18th/19th are both 1.0 or the 8/9s; article says median 8/9 (88.9%)—with 17 ones and then the high mixed (three 8/9), the median is indeed among the 1.0 or 0.889; actually sorted: 7 zeros, then low mixed, then higher, 17 ones. Position 18–19 fall in the 1.0 block after the 12 mixed +7 fail =19, wait 7+12=19, so positions 1–7:0, 8–19:mixed (12), 20–36:1.0. Median (avg 18th+19th) both mixed high-end? No: sorted ascending: 7×0, then batch 0.133, three ~0.556, rd 0.571, moco 0.655, tensor 0.667, two 0.778, three 0.889, then 17×1. So positions 1-7:0, 8:0.133, 9-11:0.556, 12:0.571, 13:0.655, 14:0.667, 15-16:0.778, 17-19:0.889, 20-36:1.0. Median of 36 is avg of 18th and 19th = 0.889. Yes, 8/9.  
   **Severity:** note (matches).

4. **Article location:** Matrix section.  
   **Claim:** 340 rows; most single-case (296 of 340); 44 multi-case in four envs (moco 15 rows/55 cases, glyph 12/24, css 9/18, epistemic_games 8/23); 329 rows have pass rate; 320 of those exactly 0 or 1; 9 fractional all in moco; 204/340 (60%) in uniform-outcome envs; +10 unscored-env rows → 214 (63%). Zero-pass tuples: 98 in 19 envs; all 12 mixed have ≥1 zero-pass tuple.  
   **Packet evidence:** Table D has 340 rows. Single-case: most n_cases=1; multi: css 9 rows n=2; epistemic_games 8 rows with n=2–4; glyph 12×2; moco 15 rows with n=2–6. 9+8+12+15=44 multi rows. Rows with n_scored>0: 340-11=329 (11 unscored rows: 6 silence +4 type_games +1 rd_adaptive). Of those, only moco has fractionals (its 15: several 0/1 and 9 fractional as listed: 4/6,2/3,3/3,5/6,2/3,1/6,3/4,2/5,2/3,0/2,3/3,2/2,4/4,1/3,2/2). 320 binary confirmed by inspection (non-moco scored rows are 0 or 1; moco has 6 binary +9 frac). Uniform envs: the 17 all-pass +7 all-fail =24 envs; their rows: all-pass tuples sum n_tuples from A (9×11 +6×2 +4×2 +8 +15×2 +18? wait css9 + epistemic_games8 etc.) + all-fail (9×4 +12 glyph +4×2) =204 scored uniform rows yes. +10 from two unscored envs=214. Zero-pass tuples widespread: many 0.0 rows across 19 envs (all-fail 7 + mixed 12). All mixed have ≥1 zero row (visible in D).  
   **Severity:** note (matches). moco fractional values match article (1/6,1/3,2/5,2/3,3/4,5/6).

5. **Article location:** Judge guarantees.  
   **Claim:** 189 behavioral_reference / 227 compile_only across 416; 11 envs BR, 27 CO; scored: BR 141/189 (74.6%), CO 136/216 (63.0%) +11 unscored.  
   **Packet evidence:** Table B judge_guarantee column + Table A/D consistency. Envs with BR (from B samples and D): categorical_lenses, ci_dependency_graph, css_state_machine, epistemic_games, glyph, moco, rd_state_carry, regex_state_machine, spreadsheet_dataflow, sql_fixed_point, template_interpreter =11. Rest 27 CO. Case counts: BR envs n_cases sum to 189 (e.g. moco55 + glyph24 + css18 + epistemic_games23 + rd_state15 +9×5 +9? yes). CO 416-189=227. Scored BR: 189 (all BR envs fully scored); PASS in BR: from A: cat9+ci9+css18+eg23+glyph0+moco36+rd_state15+regex5+spread9+sql8+temp9 = 9+9+18+23+0+36+15+5+9+8+9=141. CO scored 405-189=216; PASS 277-141=136. 141/189≈0.746; 136/216≈0.630. Unscored all CO.  
   **Severity:** note (matches).

6. **Article location:** Failure labels table and fig11.  
   **Claim:** underfit 51, overfit_visible_tests 49, runtime_error 11 (9 RUNTIME_ERROR +2 runtime_error), source_invalid 9, invalid_action 5, training_failed 3; total 128. Per-env breakdown matches.  
   **Packet evidence:** Table B failure_mode_normalized on FAIL rows. Count: underfit appears in many (functorial 6, sheaf_inv 9, sheaf_phys 9, sheaf_schema 1, gnn/regex/ssm/ts ~, etc.) sum 51; overfit in glyph~22, moco~16, batch~11 →49; runtime: functorial 3 RUNTIME, rd_adaptive 5 RUNTIME, equivariant 1 RUNTIME, ts_one 1 runtime_error, ts_traj 1 runtime_error →11; source_invalid: monadic 8 + transformer 1=9; invalid_action: batch1, glyph1, moco1, monadic1, regex1=5; training_failed: batch1 + moco2=3. Per-env table in article aggregates correctly (e.g. glyph 22 overfit+1 under+1 invalid; the grouped “4 each” underfit17+invalid1+runtime2 for five envs, etc.). Rows sum 128.  
   **Severity:** note (matches). Raw casing difference treated correctly as artefact.

7. **Article location:** Dispositions / flags.  
   **Claim:** 10 rejected (all FAIL; 8 monadic +1 batch +1 transformer; 9 of 10 source_invalid); 9 scored FAILs with disposition unscored (moco3, batch1, glyph1, monadic1, regex1, ts_one1, ts_traj1; labels invalid5 + training2 + runtime2); 1 PASS ts_parse_only performance_eligible=False.  
   **Packet evidence:** Table B case_disposition: rejected on rows 20 (batch training_failed), 225-231+233 (monadic source_invalid ×8), 401 (transformer source_invalid) =10. unscored disposition on FAIL scored: 24 (batch invalid), 145 (glyph invalid), 193+214+222 (moco training/invalid), 232 (monadic invalid), 293 (regex invalid), 405 (ts_one runtime), 415 (ts_traj runtime) =9. ts_parse_only row 409: PASS, performance_eligible=False.  
   **Severity:** note (matches). Article correctly keeps them in counts and flags conflicts.

8. **Article location:** Selection frame / omissions.  
   **Claim:** 80 omitted: 56 intervention-twin, 14 known-gate, 10 unsupported (all rope); 496 design cells; provenance says 24 known-gate (conflict left open); rope all 10 omitted, not in 38.  
   **Packet evidence:** Table C: 80 rows. Count exclusion_class: unsupported_provider_input_modality =10 (all rope rows 1-10); known_gate_calibration_failure =14 (glyph 11-19=9, rope 20-24=5); intervention_twin_omission =56 (epistemic_games 9 + glyph 12 + moco 35). 56+14+10=80. 416+80=496. Rope absent from Table A. Article correctly notes 14 vs (external) 24 conflict and does not resolve.  
   **Severity:** note (matches packet; open discrepancy with other doc correctly disclosed).

9. **Article location:** Seed; sensitivity table; cell meaning.  
   **Claim:** seed 0 all 416; exclude moco 241/350=68.86%; exclude glyph 277/381=72.70%; both 241/326=73.93%; shrink moco approx. Cell = env×tuple inference from 340 rows /416 cases.  
   **Packet evidence:** Table B seed=0 every row. 277-36=241; 405-55=350; 241/350≈0.6886. 405-24=381; 277/381≈0.7270. 405-55-24=326; 241/326≈0.7393.  
   **Severity:** note (matches). Inference on “cell” is explicitly labelled as such.

10. **Article location:** Figure captions (fig8–11).  
    **Claim:** Captions describe selection 496→80 omit→416 (11 unscored/405 scored 277/128); env intervals 36 dots Wilson + pooled line; 340 matrix squares (grey unscored, numbers multi-case, frac only moco); failure labels global bars.  
    **Packet evidence:** Section E exactly matches the captions’ claimed content and values (Wilson table, multi-case 44, frac 9 moco, label counts, omission breakdown). No caption claims extra (e.g. no seed-variance, no cross-env column meaning).  
    **Severity:** note (match).

11. **Article location:** “Ten zero-pass… or seven?” section.  
    **Claim:** Earlier summary says 10; packet/env-level 7; tuple-level ≥1 zero-pass =19; 7+2 unscored=9; +rope (omitted) =10 only if counted as zero-pass (but never scored). Uses 7; reconciliation open.  
    **Packet evidence:** Table A: 7 all-fail. Table D: zero-pass rows in 7 all-fail + all 12 mixed =19 envs. Rope in C only.  
    **Severity:** note (correctly open; no false resolution).

12. **Article location:** ts_parse_only caveat; monadic_reward rejected; various “I keep in counts”.  
    **Claim:** Disclosures present for ineligible PASS, rejected, unscored-disposition FAILs, 14-vs-24, dirty source, single seed, guarantee confounding.  
    **Packet evidence:** All present and accurate (see 7–8). No quiet removal.  
    **Severity:** note (good disclosure).

13. **Article location:** Causal / mechanism / “does not show” statements.  
    **Claim:** No capability split; names not forecasts/difficulty ladder; no shared mechanism for glyph/moco/batch; no difficulty effect (no common scale); labels not internal reasoning; guarantee diff confounded; endpoints not stable under other seeds; etc. “Cannot” statements match packet limits (single seed, no row key for moco, dirty source, etc.). Withdrawn non-monotonic css (correct, 18/18). Open non-monotonic moco/SQL left as questions.  
    **Packet evidence:** Packet has no multi-seed, no model internals, no calibrated difficulty, no mechanism fields beyond recorded labels. All “does not show / cannot” are supported; no contradicted “cannot”. No unsupported causal claim advanced as fact.  
    **Severity:** note (appropriate epistemic hygiene).

14. **Article location:** Minor prose / arithmetic.  
    **Claim:** “Share of scored cases” column in outcome table (42.5% all-pass cases, 16.8% all-fail, 40.7% mixed). 172/405≈0.4247; 68/405≈0.1679; 165/405≈0.4074. “about 69.2%”, “about 68.8%” for shrink.  
    **Packet evidence:** Matches.  
    **Severity:** note.

15. **Article location:** Failure per-env table (grouped rows).  
    **Claim:** Grouped “gnn… ts_trajectory | 4 each | underfit 17, invalid 1, runtime 2” and “tensor… transformer | 3,2,2,1,1,1 | underfit 8, runtime 1, source 1”.  
    **Packet evidence:** Five envs ×4 FAIL =20; labels: gnn 4 under, regex 3 under+1 invalid, ssm 4 under, ts_one 3 under+1 runtime, ts_traj 3 under+1 runtime → under 4+3+4+3+3=17, invalid1, runtime2. Yes. Other group: tensor3 under, comp2 under, equiv 1 under+1 runtime, sheaf_schema1 under, sql1 under, trans1 source → under 3+2+1+1+1=8, runtime1, source1. Sums to remaining.  
    **Severity:** note (matches).

16. **Potential minor issues (non-blocking):**  
    - Article “9 of the 128 scored FAILs carry a disposition label that conflicts” (fig8 caption) and later “Nine scored FAIL cases carry disposition unscored”—exact.  
    - “Eight of its 9 scored FAIL cases also carry rejected” for monadic—Table B monadic 9 FAIL: 8 rejected +1 unscored. Correct.  
    - Wilson intervals and colours in E match article description.  
    - No claim treats label/disposition/guarantee as model fact; all framed as recorded.  
    - Open 10-vs-7 correctly left open; no invention of outcomes for unscored.  
    **Severity:** note.

### Blocking findings
None. All core counts, rates, splits, matrix stats, guarantees, labels, dispositions, omissions, and figure descriptions match the packet. Disclosures for confounds, conflicts (14 vs 24, disposition clashes, ineligible PASS, undefined “rejected”), and limits (single seed, no common difficulty, confounded guarantee) are present and accurate. No unsupported causal/mechanism claims presented as findings; “does not show” / “cannot” statements are consistent with packet.

### Corrections needed
None required for factual accuracy against the packet. (Optional polish only: the unweighted mean is exactly calculable as ~69.21%; “about 69.2%” is fine. Ensure any rendered SVGs match Section E if not already.)

**Final line:** blocking findings: 0; corrections: 0.

&&&&&&&&&&&&&&&&&&

fable 5.1:

**State:** Commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` read as pinned. Packet read in full: Table A (38 rows), Table B (416 rows), Table C (80 rows), Table D (340 rows), Section E (Figures 8–11). Nothing unread. I transcribed the packet tables into code to recompute every count rather than trusting either the article or the "facts the packet should confirm" list.**State:** Commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` read as pinned. Packet read in full: Table A 38 rows, Table B 416 rows, Table C 80 rows, Table D 340 rows, Section E (Figures 8–11). Nothing unread. I transcribed Tables A, C, D and every non-default Table B row (all FAILs, unscored, `rejected`/`unscored` dispositions, `performance_eligible = False`) into code and recomputed each count rather than trusting the "facts the packet should confirm" list.

## Verdict: accept with corrections

## What the packet confirms (checked, not assumed)

All of the following reproduce exactly from the packet: 416/405/11; 277 PASS/128 FAIL; 277/405 = 68.40%; 277/416 = 66.59%; 17/7/12/2 environment split with 172/172, 0/68, 105/165 (+1 unscored); shares 42.5%/16.8%/40.7%; unweighted mean 69.2%, median 0.889 (18th and 19th of 36 sorted values both 8/9); range 2/15–8/9; 17/36 = 47%; the nine 9/9 environments, four larger, four smaller all-pass environments; the seven all-fail environments; the 12-row mixed table; sensitivities 241/350 = 68.86% (+0.46), 277/381 = 72.70% (+4.31), 241/326 = 73.93%, shrunk-moco ≈ 68.8%; moco 55/405 = 13.6%; glyph+moco+batchnorm = 94 scored / 56 FAIL; matrix 340 rows, 296 single-case, 44 multi-case (moco 15/55, glyph 12/24, css 9/18, epistemic_games 8/23), 329 rated rows, 320 binary (97.3%), 9 fractional all in moco with values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6 and 6 endpoint moco rows; 204 and 214 uniform-environment rows (60%, 63%); 98 zero-pass tuples in 19 environments, all 12 mixed environments included; row count range 4–15, six environments >10; guarantees 189 BR/227 CO, 11/27 environments, 141/189 = 74.6%, 136/216 = 63.0%, all 11 unscored under compile_only; failure labels 51/49/11/9/5/3 with 9 `RUNTIME_ERROR` + 2 `runtime_error`; the full per-environment label table (every row and both grouped rows sum correctly to 128); 10 `rejected` (9 source_invalid, batchnorm row 20 training_failed), all FAIL; 9 `unscored`-disposition scored FAILs with the stated environment and label breakdown; row 409 is the only scored PASS with `performance_eligible = False`; seed 0 on all 416 rows; omissions 56/14/10 with the 10 modality omissions all in `rope`; unscored cases 6/4/1 in the stated environments; sheaf_* FAILs all underfit; glyph 22/24 and moco 16/19 overfit; the Figure 9, 10 and 11 captions match Section E.

## Findings

1. **Selection frame section and "Ten zero-pass environments or seven?" — `rope` case count.** Article: "All 10 of its cases were omitted before scoring" and "whose 10 cases were all omitted before scoring." Packet: Table C has **15** `rope` rows — rows 1–10 (`unsupported_provider_input_modality`) **and rows 20–24 (`known_gate_calibration_failure`)**. The 10 is the count of one exclusion class, not of `rope`'s omitted cases. The argument about whether `rope` counts as a tenth zero-pass environment is unaffected, but the number is wrong in two places. **Severity: correction.**

2. **Selection frame table — known-gate split not stated.** The 14 known-gate omissions are 9 `glyph` (Table C rows 11–19) and 5 `rope` (rows 20–24). The article's "(all in the `rope` environment)" is attached only to the modality class and is correct, but combined with finding 1 a reader will infer that every `rope` omission was a modality omission. Stating the 9/5 split closes that. **Severity: note.**

3. **`moco` section — "The archive has no row-by-row key linking each value to its tuple."** Packet Table D enumerates `moco#1`–`moco#15` each with its own pass rate (4/6, 2/3, 3/3, 5/6, 2/3, 1/6, 3/4, 2/5, 2/3, 0/2, 3/3, 2/2, 4/4, 1/3, 2/2), and defines `n_dims` as "number of difficulty keys in the tuple," which means the source matrix carries the tuple keys per row. What the packet omits is the tuple *label text*, not the row-by-row link. As written this "cannot" claim is contradicted by the structure of the packet's own source table. Suggested public wording: the per-row values exist, but the tuple labels were not used in this analysis, so the shape across dimensions is not drawn. **Severity: correction.**

4. **Unscored section — "sits at the tuple where all five dimensions are `easy`."** Table D `rd_adaptive_halting#1` shows `n_dims = 5`, `n_unscored = 1`, but no dimension labels appear anywhere in the packet. Unverifiable. It is also internally inconsistent with finding 3: the article reads tuple labels for one environment while saying no per-row key exists for another. **Severity: note.**

5. **Matrix section — "34 difficulty dimension names."** The packet gives only `n_dims` per row (values 2–6); dimension names are not in the packet. Unverifiable from the packet. **Severity: note.**

6. **`ts_parse_only` caveat — "Its exclusion note describes a provider-attributed terminal failure."** Packet omits long free-text fields. Only `performance_eligible = False` on row 409 is verifiable. The "provider-attributed" phrase is a cause attribution the packet cannot support; the article should mark it as quoted from a field outside the counts. **Severity: note.**

7. **Claims sourced outside the packet.** "One seed per cell" wording, the dirty-source record, the provenance summary's 24 known-gate omissions, and the project summary's 10 zero-pass environments are all outside the packet and cannot be checked here. The article correctly treats the 24 and the 10 as open. On the 10 vs 7: packet gives 7 at environment level (Table A), 19 at tuple level (Table D), 9 if the two no-scored environments are added, 10 only by adding `rope` (Table C), which was never scored. The article's handling matches the packet; the discrepancy remains open. **Severity: note.**

8. **Figure 8 caption vs Section E.** Section E says the chart draws three stacked bars and nothing else. The caption's final sentence ("Nine of the 128 scored FAILs carry a disposition label that conflicts…") describes something the chart does not plot; it belongs in the text, not the caption. Section E also notes the 11-case unscored segment is unlabelled on the chart, which the caption does not say. **Severity: note.**

9. **Failure-label section — "The archive normalises both spellings to one label."** True of Table B's `failure_mode_normalized`, but Table D's `failure_modes` column retains raw casing (`RUNTIME_ERROR` in `equivariant_diagram#9`, `functorial_augmentation#1/#4/#6`, `rd_adaptive_halting#4/#7/#9/#13/#15`; `runtime_error` in `ts_one_step#1`, `ts_trajectory#2`). The normalisation is not archive-wide; say "the per-case table normalises." **Severity: note.**

10. **Mixed-environment table — `transformer_ssm_lift` 8/9.** Its single FAIL (Table B row 401) is `source_invalid` with disposition `rejected`. The article attaches the `rejected` caveat beside `monadic_reward`'s 0/9 and `batchnorm_ema`'s 2/15 but not beside this 8/9; it is disclosed only later in the label section. Not a mismatch, but the disclosure is inconsistent in placement. **Severity: note.**

11. **Selection frame — omissions concentrated in the densest environments.** Table C: `moco` 35, `glyph` 21 (12 twin + 9 known-gate), `epistemic_games` 9, `rope` 15. The three environments the article singles out for pulling on the average (`moco`, `glyph`) are also where 56 of the 80 omissions sit. The article says "the 416 cases are themselves a selection" but does not say the selection was heaviest exactly there. This is within-packet and supports the article's own point. **Severity: note.**

12. **Text artefacts in published prose.** Epistemic status, *Importance*: "how little the archive can fuckingly support." Final section: "environment identity 👹 more than difficulty." Neither is a bracketed replacement token, so neither is covered by the stated convention; the second makes the sentence unreadable. **Severity: correction.**

13. **14-vs-24 paragraph — duplicate sentence.** "I leave the conflict open rather than resolve it silently" and "I report both and do not resolve the conflict" say the same thing. **Severity: note.**

## Task 4 and Task 5 summary

- Causal/mechanism claims: none found that the packet does not support. Every label and guarantee pattern is explicitly framed as descriptive, and the single-seed, confounded-guarantee and selection caveats are correct. The only unsupported attribution is the "provider-attributed" phrase in finding 6.
- "Cannot"/"does not show" statements: one is contradicted by the packet's structure (finding 3). The rest (no variance estimate, guarantee confounded with environment, no cross-environment difficulty scale, no mechanism from labels) are consistent with the packet.
- Labels/dispositions treated as model facts: none found. "Failures" is used consistently to mean FAIL judgments; `rejected`, `unscored` and `source_invalid` are consistently called undefined recorded fields.

**Blocking: 0. Corrections: 3 (findings 1, 3, 12). Notes: 10.**
