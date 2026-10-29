grok 4.5:
I will now assemble the full evidence review from all four parts, beginning with required Web Search checks on provenance and any external claims.State. Pinned commit 6ed48cb1c4447d4f902d1fbc8a908a56185e34ed (StrangeTcy/epistemic-compiler). Read in full: WRITER_PAIR (both drafts verbatim), COMPLETE_EVIDENCE_PACKET (Table A 38 env rows, Table B 416 case rows, Table C 80 omission rows, Table D 340 matrix rows, Section E chart descriptions), COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with full difficulty_tuple keys), CAMPAIGN_PROVENANCE, EARLIER_ANALYSIS_OVERVIEW, INELIGIBLE_PASS_CSV_EXCERPT, and the 2026-10-29 supporting local check. Web Search accessed Inception Labs/OpenRouter/etc. pages confirming Mercury-2.5 existence and specs (no campaign data or public StrangeTcy/epistemic-compiler repo/commit retrieved; limitation noted, embedded sources used exclusively). Calculations performed: row sums (277 PASS/128 FAIL/405 scored/11 unscored; 17/7/12/2 env split; 172/68/165; omission 56+14+10; failure-label totals; 296/44/329/320/9/98 matrix; unweighted mean ≈69.2%; 214 vs 204+10 uniform; moco fractions and keys; guarantee 189/227; rejected/unscored disposition counts). Unverifiable/unread: actual SVG binary renders (descriptions only), exact dirty working-tree state, clean-source comparison, public origin of overview’s “10”, any external campaign data.

1. Draft gpt 6 luna max
Verdict: accept with corrections

Confirmed-arithmetic table (matches Tables A/B/C/D + local check):

Quantity	Value
Selected / scored / unscored	416 / 405 / 11
PASS / FAIL	277 / 128
277/405	68.4%
277/416	66.6%
Env split (all-pass / zero-pass scored / mixed / unscored-only)	17 (172) / 7 (68) / 12 (105/165 +1) / 2 (10)
Matrix rows / singleton / multi	340 / 296 / 44
Rows with rate / endpoint / fractional	329 / 320 / 9 (all moco)
Zero-pass tuples	98 (19 env)
Unweighted mean / median (36 scored env)	~69.2% / 8/9 = 88.9%
Failures (underfit / overfit_visible_tests / runtime consolidated / source_invalid / invalid_action / training_failed)	51 / 49 / 11 / 9 / 5 / 3
Guarantees	189 behavioral_reference / 227 compile_only
Omissions	80 (56 twin / 14 known-gate / 10 modality all rope)
Rejected FAILs	10 (8 monadic_reward +1 batchnorm_ema +1 transformer_ssm_lift)

Numbered findings:

Location: moco subsection / “Claims withdrawn…”. Claim: “The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across moco’s dimensions.” Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV supplies full difficulty_tuple JSON keys for all 15 moco rows (e.g. distractors/naming/queue_math/… mapped to 1/6, 1/3, 2/5, 2/3, 3/4, 5/6 etc.). Compact Table D omits the strings; complete matrix does not. Verdict: incorrect (keys exist). Severity: correction. Action: Replace with statement that keys are present in the complete matrix and optionally list the nine fractional mappings; do not claim unavailability.

Location: “The environment-by-tuple matrix” (214 rows). Claim: “A total of 214 rows—63% of the matrix—sit in environments where every row has the same outcome.” Evidence: Local check + matrix: 214 only when blanks (unscored) are treated as uniform; supported split is 204 rows in environments with uniform scored outcomes + 10 rows in the two fully unscored environments (epistemic_silence 6 + epistemic_type_games 4). Verdict: imprecise. Severity: correction. Action: Narrow to “204 rows in uniform-scored-outcome environments + 10 in fully unscored environments (or 214 if shared absence of scored outcomes is grouped)”.

Location: “Ten zero-pass environments or seven?” + overview cross-ref. Claim: Correctly uses 7 scored zero-pass and leaves “10” unresolved. Evidence: Table A shows exactly 7 (functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, ts_trajectory, glyph); overview states 10; tuple view yields 19. Unscored-only envs are not zero-pass. Verdict: correct handling. Severity: note. Action: Retain; do not reconcile.

Location: Omission / provenance. Claim: Reports both 14 (exclusion record) and 24 (provenance) known-gate; leaves open; does not present 14+10=24 as verified. Evidence: Table C = 14 known-gate (9 glyph +5 rope) +10 modality +56 twin; provenance prose “24 known gate-blocked”. Verdict: correct. Severity: note. Action: Keep both figures and open status.

Location: Failure labels / dispositions. Claim: Global tallies only; runtime consolidated 9+2; 10 rejected kept in FAIL; archive undefined. Also notes unscored dispositions implicitly via counts. Evidence: Table B + local check: labels sum 128; exactly 10 rejected; 9 scored-FAIL with disposition unscored. Verdict: correct on globals and rejected; slightly incomplete on the 9. Severity: note. Action: Optionally flag the 9 scored/FAIL/unscored disposition cases explicitly as recorded but undefined operationally.

Location: ts_parse_only / ineligible. Claim: Keeps the PASS in 277; flags performance-ineligible and provider-attributed terminal failure vs PASS verdict. Evidence: INELIGIBLE_PASS_CSV_EXCERPT + Table B row 409: verdict PASS, performance_eligible=False, exclusion_reason provider-outage/transient. Verdict: correct; attribution is the recorded field, not independent causation. Severity: note. Action: Retain flag; do not elevate exclusion_reason to proven cause.

Location: Figure 2 caption. Claim: Lollipop of observed pass rates across 36 scored envs; read fraction with case count; not stability. Evidence: Section E describes related interval/lollipop-style env plot (Fig 9) with Wilson intervals and same 36; drafts’ Fig 2 path/units match data but numbering/caption differ from packet’s 8–11. No SVG rendered here. Verdict: substantively aligned, numbering mismatch. Severity: note. Action: Align caption/number to packet or note descriptive match only; do not claim rendered SVG content beyond description.

Location: Seed / dirty / selection / guarantees. Claims: All seed 0, no second seed, dirty source [m-word], 80 omitted, guarantees not interchangeable, no env-by-guarantee cross-tab. Evidence: Table B all seed=0; provenance dirty=true, no clean snapshot; Table C 80; guarantees 189/227 total only. Verdict: correct limits. Severity: note. Action: None beyond retaining.

Location: Public prose / brackets. Claim: Uses [m-word]; no accidental paths, broken MD, or ungrounded authorship. Evidence: Intentional per rules; required fig URLs absent or clean. Verdict: clean. Severity: note.

Blocking-finding count: 0
Correction count: 2 (moco keys; 214 wording)
Note count: 7

2. Draft opus 5
Verdict: accept with corrections

Confirmed-arithmetic table: Identical to the table above (all core denominators, splits, matrix stats, labels, guarantees, omissions, rejected match Tables A–D + local check). Additional verified sensitivities (ex-moco 241/350≈68.86%, ex-glyph 277/381≈72.70%, etc.) are pure arithmetic on existing rows, not new analysis.

Numbered findings:

Location: moco subsection. Claim: “the fractional values are recorded, but no row-by-row key links each value back to its tuple. So I can say that moco is the only environment where outcomes vary within tuples, and I cannot say which tuples those are…” Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV provides the exact keys for every moco row (including the nine fractionals). Verdict: incorrect (keys exist). Severity: correction. Action: Same as gpt #1 — acknowledge complete-matrix keys and map if desired; drop “cannot”.

Location: Matrix section (214 / 63%). Claim: “214 of 340 rows (63%) sit in environments where every row has the same outcome.” Evidence: Same local-check distinction (204 uniform-scored + 10 fully unscored). Verdict: imprecise. Severity: correction. Action: Identical narrowing as gpt #2.

Location: “Ten zero-pass…”. Claim: Uses 7; leaves 10 open; tuple view 19. Evidence: Table A =7; overview =10. Verdict: correct. Severity: note. Action: Retain.

Location: Selection frame / provenance. Claim: 14 vs 24 known-gate both reported, unresolved; 10 modality all rope; does not treat 14+10 as verified reconciliation. Evidence: Table C vs provenance. Verdict: correct. Severity: note. Action: Keep.

Location: Failure labels. Claim: Globals only; “No environment-by-label breakdown is available here”; runtime casing consolidated without over-reading; 10 rejected kept. Evidence: Packet supplies globals; complete matrix has per-row failure_modes but no pre-aggregated env×label table in compact form. Local check notes 9 scored/FAIL/unscored disposition. Verdict: mostly correct (globals accurate; “no breakdown” is true for compact packet, overstated if complete matrix counts are allowed). Severity: correction (mild). Action: Soften to “no pre-built env-by-label cross-tab in the compact packet; per-row modes exist in matrix for counting if needed”; explicitly note the 9 disposition cases.

Location: ts_parse_only ineligible + guarantees. Claim: Keeps in 277, flags inconsistency; guarantees not interchangeable, no env-by-guarantee. Evidence: Excerpt + totals. Verdict: correct. Severity: note. Action: Retain.

Location: Density/sensitivity arithmetic. Claim: Excluding moco/glyph etc. shifts. Evidence: Direct from Table A (55 moco, 24 glyph). Verdict: supported verification. Severity: note. Action: Keep as arithmetic illustration only.

Location: Figure caption / embed. Claim: Markdown image to ../figures/fig2_environment_outcome_lollipop.svg + caption matching 36 scored envs, fractions + counts. Evidence: Section E Fig-style data match; path is required figure URL (not leakage); no binary render. Verdict: acceptable reference. Severity: note. Action: Confirm path resolves in final; caption OK.

Location: Seed/dirty/selection/confounds / [m-word]. Claims: Accurate limits; intentional bracket. Evidence: Matches provenance/Table B. Verdict: clean. Severity: note.

Blocking-finding count: 0
Correction count: 3 (moco keys; 214; mild env-by-label availability)
Note count: 6

3. Shared unresolved source discrepancies

Bounded by supplied records: 14 (Table C) vs 24 (provenance) known-gate omissions — both figures exist; Table C rows detail 9 glyph +5 rope; no row-level support for 24 inside the exclusion CSV. 7 scored zero-pass env (Table A) vs overview “10” — overview list enumerates only the 7; origin of 10 unreconciled here (not the 2 unscored-only, not the 19 tuple envs). 214 uniform rows — resolvable as 204+10 once blanks included (local check). moco keys — available in complete CSV, absent from compact Table D. 9 scored/FAIL/unscored disposition cases + 10 rejected — exact IDs in local JSON/Table B; definitions absent.
Cannot be reconciled here: Exact dirty working-tree state or causal effect; clean-source counterfactual; seed-variance (only seed 0); whether overview “10” derives from an earlier filter; any env×label or env×guarantee controlled comparison beyond raw counts that can be tallied from matrix; base rate of apparent non-monotonicity; independent causation behind exclusion_reason text (recorded attribution only). Arithmetic coincidences (e.g. 14+10) are not documented explanations.

4. Handoff for the editorial critic
Exact corrections to carry:

Both drafts: Insert that complete difficulty-matrix CSV supplies difficulty_tuple keys for all rows (including moco’s nine fractionals); remove or rewrite any “no key / cannot map / unavailable” claim. Optionally publish the nine mappings as descriptive.
Both: Re-word 214/63% to distinguish 204 uniform-scored-outcome rows + 10 fully-unscored-environment rows (or explicitly define inclusion of blank pass_rate).
Opus (and optionally gpt): Soften “no environment-by-label breakdown” to reflect that per-row failure_modes exist for aggregation; note the 9 scored/FAIL/disposition=unscored cases alongside the 10 rejected.
Retain: 277/405=68.4% as scored pass rate; 7 (not 10) scored zero-pass envs; dual 14/24 known-gate reporting as open; ineligible ts_parse_only PASS kept in numerator with flag; all seed-0 / dirty / selection / guarantee / single-seed limits; no causal or common-scale claims; intentional [m-word].
Newly available fields for critic: full tuple keys, per-row failure_modes/judge_guarantees, exact disposition flags (9+10), local-check uniform split, INELIGIBLE exclusion_reason text, matrix-derived env totals.
Evidence limits: No new model fits, no causal estimates, no imported campaigns, no SVG pixel claims, no fabrication of missing clean snapshot or second seeds. Overview vs Table A “10 vs 7” and provenance vs Table C “24 vs 14” stay open. Web Search found no public archive contradicting the pinned embedded records.

No prose rewrite, no winner choice, no claim that later stages are complete.

&&&&&&&&

claude fable 5.1:
Both drafts and all source blocks are now assembled; before writing the review I will verify the arithmetic against the supplied tables and run the required Web Search for provenance.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
# Mercury POST-02 — evidence review of gpt 6 luna max and opus 5

State. Pinned commit 6ed48cb1c4447d4f902d1fbc8a908a56185e34ed in StrangeTcy/epistemic-compiler. Read in full: WRITER_PAIR (both drafts, verbatim order); COMPLETE_EVIDENCE_PACKET — Table A (38 rows), Table B (416 rows), Table C (80 rows), Table D (340 rows), Section E (Figures 8–11); COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with difficulty_tuple keys, raw failure labels, judge guarantees); CAMPAIGN_PROVENANCE; EARLIER_ANALYSIS_OVERVIEW; INELIGIBLE_PASS_CSV_EXCERPT (1 row); and the 2026-10-29 supporting local check. Calculations performed in Python from Table A and the env-level guarantee assignment in Table B/D: denominators, group totals, shares, unweighted mean/median, tuple-row sums, sensitivity scenarios, Wilson intervals, guarantee cross-tabs (all reproduced below). Web Search accessed: the repository landing page https://github.com/StrangeTcy/epistemic-compiler exists and is public; search results could not retrieve the pinned commit, the four CSVs, or their hashes, so file-level provenance remains verified only against the embedded sources. External context: Mercury 2.5 is a publicly announced Inception model (https://www.baseten.co/library/mercury-25/, https://www.businesswire.com/news/home/20260908593295/en/Inception-Launches-Mercury-2.5-the-Next-Tier-of-Intelligence-for-Diffusion-LLMs); none of the campaign's numbers are checked against those pages. Unverifiable: no SVG was rendered; Section E describes Figures 8–11 only, and neither draft's "Figure 2" lollipop chart is described there. No evidence/generated/environment_summary.csv or the supporting check's JSON was supplied.

Confirmed arithmetic (both drafts, identical numbers)
Claim	Derivation / source	Status
416 selected / 405 scored / 11 unscored; 277 PASS / 128 FAIL	Table A sums; Table B statuses	✓
277/405 = 68.4%; 277/416 = 66.6%	68.395%, 66.587%	✓
17 all-pass (172/172, 42.5%); 7 zero-pass (0/68, 16.8%); 12 mixed (105/165, 40.7%, +1 unscored); 2 no-scored (10 unscored)	Table A grouping; 42.47/16.79/40.74	✓
24 of 36 scored environments at an endpoint; endpoints rest on 4 to 23/24 cases	17+7; ts_* n=4, epistemic_games 23, glyph 24	✓
Unweighted mean ≈ 69.2%; median 8/9 = 88.9%	69.208%; sorted positions 18–19 both 0.889	✓
All environment fractions listed in both drafts (incl. 9 envs at 9/9; mixed table)	Table A	✓
glyph+moco+batchnorm_ema = 94/405 cases, 56/128 FAILs	24+55+15; 24+19+13	✓
340 tuple rows; 4–15 per env; six envs >10; 296 singleton / 44 multi-case in moco 15/55, glyph 12/24, css 9/18, epistemic_games 8/23	Table A n_tuples sum = 340; Table D	✓
329 rows with pass rate; 320 (97.3%) at 0/1; 9 fractional, all moco; moco 6 endpoint rows; distinct values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6	Table D moco#1–15	✓
34 difficulty dimension names	counted in full matrix	✓
98 zero-pass tuples in 19 environments; all 12 mixed envs have ≥1	Table D (13+2+2+9+12+4+1+9+6+4+9+9+1+1+4+3+1+4+4)	✓
css_state_machine 9 rows all 2/2	Table D	✓
Unscored: 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting; latter at all-easy tuple	Table B 109–118, 243; full matrix rd_adaptive_halting row 1	✓
Failure labels 51/49/11/9/5/3 = 128; runtime = 9 RUNTIME_ERROR + 2 runtime_error	Table B/D raw labels	✓
189 behavioral_reference / 227 compile_only across 416	Table B; provenance §3	✓
10 rejected FAILs: 8 monadic_reward (225–231, 233), batchnorm_ema 20, transformer_ssm_lift 401	Table B	✓
Omissions 56/14/10 = 80; all 10 modality omissions in rope; provenance says 24 known-gate	Table C; provenance §3	✓ (discrepancy correctly reported)
All 416 cases seed 0; source dirty; no clean snapshot	Table B; provenance §1, §4	✓
ts_parse_only row 409 PASS, performance_eligible False, exclusion note attributes terminal failure to provider	Table B; INELIGIBLE_PASS_CSV_EXCERPT	✓
opus only: 241/350 = 68.86% (+0.46), 277/381 = 72.70% (+4.31), 241/326 = 73.93%, moco→9 cases ≈ 68.8%	recomputed	✓
1. Draft gpt 6 luna max — verdict: accept with corrections

Section "moco: the only fractional rows". Claim: "The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across moco's dimensions." Also "Claims withdrawn": "the missing row-by-row tuple key also prevents reconstructing the pattern." Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV, all 15 moco rows carry a full difficulty_tuple (e.g. the 1/6 row is distractors=hard, naming=easy, queue_math=easy, symptom_mask=hard, temperature=hard, visible_tests=easy). Verdict: false as a statement about the record. Severity: blocking. Action: replace with "the compact packet omits the keys; the complete matrix records them." The keys' existence does not license a difficulty-effect reading — keep the moco pattern "open".

Section "Failure labels and judge guarantees". Claim: "The counts are global only; they do not show which environments produced which labels." Evidence: Table D failure_modes and Table B give per-environment labels (e.g. all 9 source_invalid are monadic_reward ×8 + transformer_ssm_lift ×1; all 5 RUNTIME_ERROR in rd_adaptive_halting). Verdict: unsupported "cannot". Severity: correction. Action: state the breakdown is recorded; keep the separate, valid point that labels are classifications, not mechanisms.

Same section. Claim: "The totals alone do not show how outcomes are distributed by environment and guarantee, so I cannot compare environment results under one common judging standard." Evidence: Table D judge_guarantees — every environment has a single guarantee; BR 141/189 scored, CO 136/216 scored. Verdict: first half unsupported (the cross-tab exists); second half supportable only because guarantee is confounded with environment (no within-environment variation), not because the data are missing. Severity: correction. Action: reword to the confound.

Section "The environment-by-tuple matrix" (and conclusion). Claim: "A total of 214 rows—63% of the matrix—sit in environments where every row has the same outcome." Evidence: uniform-scored environments hold 148 (all-pass) + 56 (zero-pass) = 204 rows; the 214 includes the 10 rows of epistemic_silence/epistemic_type_games, which have no outcome (supporting check, uniform_scored_environment_rows). Verdict: arithmetic reproducible only by counting blank pass rates as an "outcome". Severity: correction. Action: "204 of 340 (60%) in environments with a uniform scored outcome, plus 10 in entirely unscored environments."

Final figure block. Text: a bare "!" line followed by "Figure 2: Lollipop chart of observed pass rates across the 36 environments…". Evidence: Section E describes Figures 8, 9, 10, 11 only; the nearest match is Figure 9 (dots + 95% Wilson bars + pooled line, 36 environments). Verdict: broken image embed (malformed Markdown) and unverifiable chart number/type; caption omits the interval bars and reference line if Figure 9 is the intended asset. Severity: correction. Action: repair the embed; either reference a Section-E-described figure with a caption matching its contents (fractions, Wilson 95% intervals and their binomial-independence assumption, pooled 68.4% line, no unscored environments drawn) or supply a verifiable description for "Figure 2."

Section "What a 'cell' means". Claim: 'The phrase "one seed per cell" is ambiguous here'. Evidence: the phrase appears in no supplied source (provenance, overview, packet). Verdict: unattributed quotation. Severity: correction. Action: attribute or drop the quotation marks; the all-seed-0 fact stands on Table B alone.

Sections "First, count…" and "Unscored cases are not failures". Claim: unscored cases are "a judge-coverage gap". Evidence: recorded status is infrastructure_unscored; failure_mode_normalized is unknown. Verdict: label promoted into an explanation. Severity: correction. Action: use the recorded status label.

Section "The selection frame" (omission). The draft reports the 10 rejected FAILs but not the nine scored FAILs whose case_disposition is unscored (Table B rows 24, 145, 193, 214, 222, 232, 293, 405, 415; labels: all 5 invalid_action, 2 training_failed, both lowercase runtime_error). Table A counts them in n_scored. Severity: correction. Action: add the parallel flag; unscored as a disposition is undefined in the record and must not be equated with infrastructure_unscored status.

Section "Ten zero-pass environments or seven?" Correct as stated. Note only: the overview also says "~12 at 1.00" against Table A's 17; worth recording alongside the 10-vs-7 gap. Severity: note.

gpt 6 luna max: 1 blocking, 7 corrections, 1 note.

2. Draft opus 5 — verdict: accept with corrections

Section "What can a FAIL label explain?" and "What this supports". Claims: "No environment-by-label breakdown is available here, so I cannot say which environments produced the 51 underfit labels"; "An environment-by-guarantee and environment-by-label cross-tab would narrow some of that; nothing in the present archive supplies it." Evidence: Table D failure_modes and judge_guarantees columns, Table B per-row fields (e.g. underfit: sheaf_invariant_gluing 9, sheaf_physical_constraints 9, functorial_augmentation 6, gnn 4, ssm 4, …). Verdict: false about the record, repeated three times and carried into the conclusion. Severity: blocking. Action: delete the "not available" statements; the per-environment counts may be reported as recorded cross-tabs, with the separate caveat that they are not controlled comparisons.

Section "moco: the only fractional rows". Claim: "no row-by-row key links each value back to its tuple." Evidence: as gpt finding 1 — all 15 moco tuple keys are in the complete matrix. Severity: blocking. Action: same as gpt finding 1.

Same section as 1. Claim: "without an environment-by-guarantee breakdown I cannot test whether the environment contrasts survive a uniform standard." Evidence: breakdown exists; guarantee is constant within each environment, so the limit is confounding, not absence. Severity: correction. Action: reword to the confound.

Same section. Claim: "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." Evidence: four 9/9 environments are behavioral_reference (categorical_lenses, ci_dependency_graph, spreadsheet_dataflow, template_interpreter); six are compile_only. Verdict: over-general. Severity: correction. Action: say which guarantee each 9/9 carries, or restrict the sentence to compile-only environments.

Section "A second layer" bullet and "What this supports". Claim: "214 of 340 rows (63%) sit in environments where every row has the same outcome"; "63% of rows inside environments with a single uniform outcome." Evidence/action: as gpt finding 4 (204 + 10).

Figure after "First, count…". Embed ../figures/fig2_environment_outcome_lollipop.svg with caption "Figure 2: One dot per environment … the dots at 1.0 and 0.0 rest on anywhere from four to 24 cases." Evidence: Section E has no Figure 2; the content matches Figure 9 (36 envs, k/n dots) but the caption omits the Wilson bars, pooled line, and the interval assumptions. Verdict: unverifiable chart number/path; caption incomplete if the asset is Figure 9. Severity: correction. Action: as gpt finding 5. (A figure URL is not path leakage.)

Section "What a 'cell' means". Claim: "The campaign records one seed per cell." Evidence: not in any supplied source. Severity: correction. Action: attribute or remove; Table B's seed column already establishes all seed 0.

Sections "First, count…" / "Unscored cases are not failures". Claims: "a judge-coverage gap"; "Being unscored is a property of the judging pipeline." Evidence: status infrastructure_unscored. Severity: correction. Action: use the recorded label; do not assign the cause to the judge.

Section "The selection frame" (omission). Nine scored FAILs with disposition unscored not mentioned. As gpt finding 8. Severity: correction.

Section "Names are useful handles". Claim: "The 68.4% is sensitive to how tuples were unrolled into cases for a handful of environments." Evidence: arithmetic scenarios are correct; "unrolled" implies a design mechanism not described in any source. Severity: note. Action: phrase as sensitivity to selected case density.

opus 5: 2 blocking, 7 corrections, 1 note.

3. Shared unresolved source discrepancies
Known-gate omissions, 14 vs 24. Bounded by the record: Table C holds exactly 14 (glyph 9, rope 5); the provenance prose says 24. 14 + 10 modality = 24 is an arithmetic coincidence; neither draft asserts it as a reconciliation (correct), and this review does not either. Origin cannot be resolved here.
Zero-pass environments, 10 vs 7; all-pass "~12" vs 17. Table A gives 7 and 17; the overview's parenthetical list enumerates at most 7 names. Neither draft notes the "~12" side. Cannot be reconciled from supplied material.
Provider-outage case. Provenance: "1 retry, 60s"; CSV row: http_attempts_result 19, elapsed_seconds 46.101, provider_transport: completed_with_errors. The fields may count different things; unresolved. The exclusion_reason is the archive's own attribution, not independent causation.
Tuple-level vs case-level counts (98 zero-pass tuples in 19 envs; 7 zero-pass envs; 10 "overview" envs) count different categories and must not be merged.
Overview claims 3–5 (non-monotonic MoCo transitions, proxy-intervention rates 0.30/0.25, 23/23 belief computation) are not supported by any supplied table except the 23/23; outside this review.
4. Handoff for the editorial critic

Carry forward, with attribution to the supplied matrix and the 2026-10-29 local check (not to an Arena finding):

Newly available fields (both drafts wrongly say absent): full difficulty_tuple keys for all 340 rows including the 15 moco rows and the all-easy unscored rd_adaptive_halting tuple; per-environment failure_modes (raw spelling) and judge_guarantees. Keys enable description only — no shared scale, no difficulty effect, no ranking.
Recorded cross-tabs that may be stated as observations: guarantee is uniform within every environment; BR 141/189 scored PASS (74.6%), CO 136/216 (63.0%) — a confounded contrast, not a judged comparison. The two lowercase runtime_error cases (ts_one_step 405, ts_trajectory 415) are both disposition unscored; the nine RUNTIME_ERROR are disposition scored — recorded coincidence, no documented explanation.
Fix 214 → "204 rows in uniformly-scored environments + 10 rows in entirely unscored environments" (62.9% only if the unscored ten are counted).
Add the nine unscored-disposition FAILs beside the ten rejected; both dispositions are undefined; all 19 remain in the 128 and in Table A's n_scored.
Figures: repair gpt's broken "!" embed; for both, reconcile "Figure 2" with Section E (Figure 9 is the only matching description: 36 environments, k/n dots, 95% Wilson bars, pooled 68.4% line, unscored environments omitted). Captions must name the interval and its independence assumption, or the figure must be independently verified before publication.
Remove or attribute "one seed per cell"; replace "judge-coverage gap"/"judging pipeline" with the recorded infrastructure_unscored.
Keep unresolved: 14 vs 24; 10 vs 7 and ~12 vs 17; provider-retry field mismatch; rejected/unscored disposition meanings; ts_parse_only row 409 PASS vs provider-attributed exclusion note (recorded attribution, not established cause).
Preserve [m-word]-style replacements, the verbatim draft order, and the single-seed/dirty-source/selection limits; do not convert seed 0 into a variance estimate or 80 omissions into a sampling frame.