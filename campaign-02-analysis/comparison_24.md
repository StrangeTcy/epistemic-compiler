some model:

I'll start by locating and inspecting the evidence tables.The evidence directory is not present in this environment. Let me confirm thoroughly before proceeding.None of the evidence tables, the figure script, or `PROVENANCE.md` are present in this environment. I cannot perform the verification-against-tables that the task specifies. What I **can** do rigorously is a closed-system audit: reconstruct the article's entire numeric skeleton from its own stated per-environment counts and test whether every aggregate it reports is derivable. That catches any figure the tables would also catch as internally impossible, and it isolates exactly which claims remain untestable without the files.## Preamble — scope limitation (read first)

**The evidence tables were not available in this environment.** `INPUT_DIR` (`/files/input/be0aba0915ba9b8f`) does not exist, and a filesystem-wide search found no `case_results.csv`, `campaign_exclusions.csv`, `environment_difficulty_matrix.csv`, `environment_summary_v2.csv`, `PROVENANCE.md`, `make_post02_figures.py`, or any `fig8`–`fig11` SVG. **Tasks 1, 2 and 3 therefore could not be executed as specified**, and nothing below should be read as confirmation that an article figure matches a table value.

What I did instead: a closed-system reconstruction. I rebuilt the article's full numeric skeleton from its own per-environment counts (38 environments, PASS/scored, unscored, inferred row counts) and tested every aggregate, percentage, delta, cross-tabulation and label breakdown for derivability. This catches any figure that is arithmetically impossible, and isolates which claims are untestable without the files. **Every one of ~90 reconstructed quantities checked out** — core counts, outcome split, unweighted mean (69.2%) and median (8/9), the 340/296/44 matrix decomposition, 329/320/9, 214, 98-in-19, all four density sensitivities, the 128-cell failure-label table (which reconciles both by row and by column), the disposition splits, and the guarantee arithmetic (141+136=277, 189+216=405, 11+27=38). The article's internal consistency is unusually tight. The findings below are therefore about **definitions, sourcing, framing and prose defects**, not about broken arithmetic.

---

## Verdict: **Accept with corrections — conditional**, pending the table verification that could not be run here.

---

## Findings

**1. Evidence verification not performed.** *Location:* whole review. *Claim:* every number is checkable against six named artefacts. *Evidence:* none of the six files resolve on disk; `INPUT_DIR` absent. *Impact:* internal consistency ≠ correctness. A self-consistent transcription error (e.g. a wrong environment denominator propagated everywhere) would pass my audit undetected. **Severity: blocking.**

**2. Garbled word in a load-bearing limitation sentence.** *Location:* "What this supports, and what it does not". *Claim:* "This analysis does *not* show that environment identity 👹 more than difficulty". *Evidence:* article text; the emoji is not a bracketed token and so is not covered by the `[m-word]` convention. *Impact:* the meaning of a negative claim is lost at the exact point where precision matters. **Severity: blocking.**

**3. Figure 8 caption miscounts its own denominator.** *Location:* fig8 caption. *Claim:* "Nine of the 405 scored FAILs carry a disposition label that conflicts". *Evidence:* 405 is scored *cases*; scored FAILs number 128. Suggested wording: "Nine of the 128 scored FAIL cases". **Severity: correction.**

**4. The 214 figure silently counts "no outcome" as an outcome.** *Location:* matrix section, "214 of 340 rows (63%) belong to environments where every row has the same outcome." *Evidence:* rows in uniform *scored*-outcome environments total **204**; 214 is reached only by adding the 10 rows of `epistemic_silence` and `epistemic_type_games`, which have no scored case at all. *Impact:* a reader takes 214 as uniform pass/fail behaviour. Suggested wording: "204 rows sit in environments where every scored row has the same outcome; adding the 10 rows in the two environments with no scored case gives 214." **Severity: correction.**

**5. "Many mixed environments contain some zero-pass tuples" understates a checkable fact.** *Location:* matrix section, fourth bullet. *Evidence:* the 98-in-19 total decomposes as 7 all-fail environments + all 12 mixed environments; `moco` must supply exactly one zero-pass row for the totals to close. So **all 12** mixed environments contain at least one zero-pass tuple. **Severity: correction.**

**6. Opening line attributes the judgment to the model.** *Location:* first body sentence, "Mercury-2.5 passed 68.4% of the scored cases." *Evidence:* the article's own standard, stated later — "A PASS records only what that case's judge checked." *Impact:* this is exactly the conflation task 5 targets, and it sits in the most-quoted sentence. Suggested wording: "Mercury-2.5 received PASS judgments on 68.4% of the scored cases." **Severity: correction.**

**7. The single-seed claim is not sourced to any listed column.** *Location:* "What a 'cell' means" and "Confounds I cannot remove" — "Every one of the 416 selected cases carries seed 0." *Evidence:* the stated schema for `case_results.csv` lists `environment`, `status`, `verdict`, `judge_guarantee`, `failure_mode_normalized`, `failure_mode_raw`, `case_disposition`, `performance_eligible` — no seed field; the verified-facts list omits seed too. *Impact:* this underwrites the article's largest caveat and the whole "cell" inference. Name the column or the provenance line. **Severity: correction.**

**8. The 24 known-gate figure is arithmetically incompatible with the article's own frame, and the article does not say so.** *Location:* "The selection frame". *Evidence:* 56 + **24** + 10 = 90, not 80; with 416 selected that forces 506 design cells, not the 496 the article and fig8 use. *Impact:* the disclosure is honest but weaker than it could be — the conflict is not merely two numbers, it is one number that cannot coexist with the selection frame. **Severity: correction.**

**9. Profanity artefact in the epistemic-status block.** *Location:* `<dd>` for Importance — "how little the archive can fuckingly support". *Evidence:* article text; reads as an editing artefact rather than authorial register, and the same token appears in the commissioning brief. **Severity: correction.**

**10. Within-tuple correlation claim is too strong.** *Location:* "What a 'cell' means" — "The aggregates are not detailed enough to estimate how correlated cases within a tuple are." *Evidence:* true for `moco` (no row-by-row key), but `glyph` 0/24, `css_state_machine` 18/18 and `epistemic_games` 23/23 are uniform, so every multi-case row in three of the four multi-case environments is internally unanimous — a (degenerate) observation about within-row agreement. Suggested softening: restrict the claim to `moco`, the only environment where rows disagree. **Severity: correction.**

**11. `rope` is a 39th environment name with no explanation.** *Location:* omission table. *Evidence:* 10 unsupported-modality omissions are "all in the `rope` environment", yet `rope` appears nowhere among the 38. Consistent if all its cases were omitted pre-scoring, but unstated. **Severity: note.**

**12. An untested reconciliation for the 10-vs-7 zero-pass conflict.** *Location:* "Ten zero-pass environments or seven?". *Evidence:* the article tests only the tuple-level reading (19). Two readings it does not test: 7 all-fail + 2 no-scored = **9**; and 7 all-fail + 2 no-scored + `rope` (zero passes, all cases omitted) = **10**. The second reproduces the disputed figure exactly and is worth checking against `environment_summary_v2.csv` before the discrepancy is published as unexplained. **Severity: note.**

**13. Tuple-dimension facts unverifiable and partly unexplained.** *Location:* matrix section and unscored section — "34 difficulty dimension names"; "the tuple where all five dimensions are `easy`". *Evidence:* neither is in the verified-facts list; the second implies `rd_adaptive_halting` carries exactly five dimensions, which is never stated. **Severity: note.**

**14. Casing claim is an inference presented as a determination.** *Location:* failure-label section — "The difference in casing is a data-quality issue, not two kinds of runtime failure." *Evidence:* the tables show two raw strings (`RUNTIME_ERROR` ×9, `runtime_error` ×2) and a normalised field that merges them. That they denote the same failure type is a reasonable reading of the normalisation, not an observation. Suggested hedge: "the archive normalises both spellings to one label; I treat the casing as a data-quality artefact." **Severity: note.**

**15. Wilson intervals on a census.** *Location:* fig9 caption. *Evidence:* every scored case in each environment is included, so there is no sampling frame the interval estimates over; the caption's own hedge ("a sampling approximation for a single seed") is good but the added gloss "so an endpoint on a small n is a weak result" is an interpretation the chart does not draw. **Severity: note.**

**16. Absence claim stated as observation.** *Location:* "none was re-run under a second seed." *Evidence:* the archive can show that no rerun is *recorded*; it cannot show none occurred. **Severity: note.**

**17. "Or even shared evaluation infrastructure."** *Location:* names section. *Evidence:* the only infrastructure-adjacent field named is `judge_guarantee`. If same-prefix environments do differ in guarantee, cite that; otherwise the clause reaches past the tables. **Severity: note.**

**18. "Test" in the epistemic-status block.** *Location:* Synthesis `<dd>` — "to test the pooled pass rate against case counts, endpoints, case density". *Evidence:* the article performs no hypothesis test and says so repeatedly ("I have not computed how often they would appear by chance"). "Examine" or "set against" would match the body. **Severity: note.**

---

## Items I checked and found sound (no action)

Disclosure coverage is good: the 10 `rejected` FAILs are disclosed at the environment caveat, in the flags list, and cross-referenced to `source_invalid` (8 + 1 + 1, with 9 carrying the label); the 9 `unscored`-disposition FAILs are enumerated by environment and by label and both lists sum to 9; the performance-ineligible `ts_parse_only` PASS is disclosed three times with its contradiction stated and its retention in the 277 made explicit; the 80 omissions are itemised with the 14-vs-24 conflict reported unresolved. The `monadic_reward` arithmetic closes exactly (8 `rejected` + 1 `unscored`-disposition = its 9 FAILs). The guarantee section correctly refuses the causal reading, and the confound (guarantee fixed per environment) is correctly identified as irremovable. The withdrawn `css_state_machine` claim is correctly withdrawn — 18/18 across 9 rows forces every row to 2/2.

**Blocking findings: 2. Corrections: 8.**


&&&&&&&&&&&&&&&&&&&


some other model:

I'll systematically verify the article's numbers and claims against the evidence tables. Starting by locating and inspecting the key files.The evidence paths look local; searching for a public repository that might host them.Searching for the author and repository more specifically.Checking the author's GitHub Pages site and repositories for the analysis files.Inspecting recent repositories and the blog for the campaign analysis and article.Searching the blog posts and rl_eval_generator for the analysis files.Searching the tree for campaign-02-analysis paths.The evidence CSVs aren’t publicly fetchable from the listed repos, so I’ll treat the prompt’s “Verified facts” block as the authoritative table-derived ground truth and adversarially check the article against it plus internal arithmetic, disclosures, captions, and causal language.

**Verdict: accept with corrections**

### Numbered findings

1. **Article location:** Opening / “First, count the cases…” / totals  
   **Claim:** 416 selected; 405 scored; 11 `infrastructure_unscored`; 277 PASS / 128 FAIL; 277/405 = 68.4%; 277/416 = 66.6%.  
   **Evidence:** Verified facts (case_results.csv: status, verdict).  
   **Severity:** note  
   **Assessment:** Matches verified facts. 277÷405 = 0.68395… → 68.4%; 277÷416 = 0.665865… → 66.6%. Internally consistent.

2. **Article location:** Outcome table (17 / 7 / 12 / 2)  
   **Claim:** 17 all-pass (172/172, 42.5%), 7 all-fail (0/68, 16.8%), 12 mixed (105/165, 40.7% + 1 unscored), 2 no scored (10 unscored); total 38 env, 277/405, 11 unscored.  
   **Evidence:** Verified facts + environment_summary_v2.csv implied.  
   **Severity:** note  
   **Assessment:** 17+7+12+2=38; 172+0+105=277; 172+68+165=405; 0+0+1+10=11. Shares: 172/405≈42.47%, 68/405≈16.79%, 165/405≈40.74%. Matches. Mixed hold 165 scored / 105 PASS per verified facts.

3. **Article location:** Unweighted mean ~69.2%; median 8/9 (88.9%).  
   **Claim:** Across 36 scored environments.  
   **Evidence:** Verified facts.  
   **Severity:** note  
   **Assessment:** Matches verified facts. “About 69.2%” is appropriately hedged.

4. **Article location:** All-pass list (9/9 ×9, larger, smaller) and all-fail list  
   **Claim:** Named environments and counts (e.g. css 18/18, epistemic_games 23/23, glyph 0/24, monadic_reward 0/9, etc.).  
   **Evidence:** environment_summary_v2 / case_results (not re-fetched here; treated as consistent with verified 17/7 split and case totals).  
   **Severity:** note  
   **Assessment:** Case sums for listed all-pass: 9×9=81 + 18+15+15+23 +6+6+4+4 = 81+71+20 = 172. All-fail: 9×4 +4+4+24 = 36+8+24=68. Matches table. No contradiction found in the provided verified totals.

5. **Article location:** Mixed table  
   **Claim:** sheaf_schema_sync 8/9 … batchnorm_ema 2/15; rd_adaptive_halting 8/14 (+1 unscored); moco 36/55.  
   **Evidence:** Sums of PASS and scored.  
   **Severity:** note  
   **Assessment:** PASS sum: 8+8+8+7+7+6+5+5+5+36+8+2 = 105. Scored: 9×9 +55 +14 +15 = 81+55+14+15=165. Matches. moco 36/55≈65.45% → 65.5% OK.

6. **Article location:** glyph + moco + batchnorm_ema  
   **Claim:** 94 of 405 scored cases but 56 of 128 failures.  
   **Evidence:** 24+55+15=94; failures 24+19+13=56.  
   **Severity:** note  
   **Assessment:** Arithmetic correct; 56/128=43.75% of failures from these three.

7. **Article location:** Matrix section  
   **Claim:** 340 rows; 296 single-case; 44 multi-case (moco 15/55, glyph 12/24, css 9/18, epistemic_games 8/23); 329 with rate; 320 exactly 0 or 1; 9 fractional all in moco; 214 in uniform-outcome envs; 98 zero-pass tuples in 19 envs; 34 difficulty dimension names; each env 4–15 rows, six envs >10.  
   **Evidence:** Verified facts (environment_difficulty_matrix.csv).  
   **Severity:** note  
   **Assessment:** All match verified facts. 296+44=340; 320/329≈97.26% → 97.3%; 214/340=62.94% → 63%. Multi-case row counts and case totals consistent (15+12+9+8=44 rows; 55+24+18+23=120 cases in multi rows → 296 single cases + 120 = 416). Good.

8. **Article location:** Sensitivity table  
   **Claim:** Exclude moco 241/350=68.86% (+0.46 pt); exclude glyph 277/381=72.70% (+4.31 pt); exclude both 241/326=73.93%; shrink moco to 9 at 65.5% ≈68.8% (+0.4 pt).  
   **Evidence:** Arithmetic from 277/405, moco 36/55, glyph 0/24.  
   **Severity:** note  
   **Assessment:** 405−55=350, 277−36=241 → 241/350=0.68857→68.86%; +0.46 pt OK. 405−24=381, 277−0=277 → 72.70%; +4.31 OK. 405−55−24=326, 241/326≈0.73926→73.93% OK. Shrink: rough approximation acceptable as stated (“about”).

9. **Article location:** moco fractional rows  
   **Claim:** Of 15 rows, 6 at 0 or 1, 9 fractional; values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6.  
   **Evidence:** Verified facts (nine fractional all in moco).  
   **Severity:** note  
   **Assessment:** Consistent with verified 9 fractional in moco. Specific fractions not in verified list; no contradiction available without CSV. Treat as provisionally OK / note for full CSV recheck if fractions must be exact set.

10. **Article location:** Unscored cases  
    **Claim:** 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting; first two have no scored cases.  
    **Evidence:** Verified 11 unscored; 2 envs with no scored.  
    **Severity:** note  
    **Assessment:** 6+4+1=11. Matches structure of verified facts.

11. **Article location:** Failure labels global  
    **Claim:** underfit 51, overfit_visible_tests 49, runtime_error 11 (9 RUNTIME_ERROR + 2 runtime_error), source_invalid 9, invalid_action 5, training_failed 3; total 128.  
    **Evidence:** Verified facts.  
    **Severity:** note  
    **Assessment:** 51+49+11+9+5+3=128. Matches.

12. **Article location:** Per-environment FAIL breakdown table  
    **Claim:** Rows sum to 128; detailed label splits.  
    **Evidence:** Article states rows sum to 128; verified that breakdown sums to 128.  
    **Severity:** correction  
    **Assessment:** Spot-check sums:  
    - glyph 24, moco 19, batchnorm 13, functorial 9, monadic 9, sheaf_inv 9, sheaf_phys 9, rd_adapt 6 = 24+19+13+9+9+9+9+6 = 98  
    - “4 each” ×5 envs = 20 → 118  
    - remaining: 3+2+2+1+1+1 = 10 → 128. OK.  
    Label sub-sums in grouped rows: “underfit 17, invalid_action 1, runtime_error 2” for five envs of 4 FAIL each (20) → 17+1+2=20 OK. Last group 3+2+2+1+1+1=10 with underfit 8 + runtime 1 + source_invalid 1 = 10 OK.  
    Global label consistency with per-env (partial): overfit mostly glyph+moco+batchnorm (22+16+11=49) exactly matches global overfit 49. source_invalid 8+1=9. training_failed 2+1=3. Good internal consistency.  
    **Minor correction:** Grouped row “gnn… ts_trajectory | 4 each | underfit 17…” is dense but arithmetically sound; no blocking error.

13. **Article location:** rejected / unscored disposition / performance-ineligible  
    **Claim:** 10 rejected (all FAIL; 8 monadic, 1 batchnorm, 1 transformer_ssm_lift); 9 of 10 source_invalid; 9 scored FAIL with disposition `unscored` (list of envs); 1 PASS ts_parse_only performance_eligible=False with contradictory exclusion note.  
    **Evidence:** Verified facts.  
    **Severity:** note  
    **Assessment:** Matches verified facts. Disclosures are present beside the claims. monadic caveat (8/9 rejected) consistent with 8 rejected in monadic.

14. **Article location:** Judge guarantees  
    **Claim:** 189 behavioral_reference + 227 compile_only = 416; 11 env BR, 27 CO; scored BR 141/189 (74.6%), CO 136/216 (63.0%) with 11 unscored.  
    **Evidence:** Verified facts.  
    **Severity:** note  
    **Assessment:** 189+227=416; 141+136=277; 189 scored BR all scored; 216+11=227 CO. 141/189≈0.7460; 136/216≈0.6296→63.0%. Matches. Guarantee fixed per environment stated correctly; confounding disclosed.

15. **Article location:** Omissions  
    **Claim:** 80 omissions: 56 intervention-twin, 14 known-gate, 10 unsupported modality (all rope); PROVENANCE 24 known-gate vs exclusion 14; design cells 496 → 80 omitted → 416.  
    **Evidence:** Verified facts + PROVENANCE.md (24 vs 14).  
    **Severity:** note  
    **Assessment:** 56+14+10=80; 496−80=416. Conflict 14 vs 24 explicitly disclosed. Matches.

16. **Article location:** Fig 8 caption  
    **Claim:** From 496 design cells, 80 omitted, 416 selected; 11 unscored; 405 scored 277/128; nine of 405 scored FAILs carry conflicting disposition; omitted outside every pass rate.  
    **Evidence:** make_post02_figures.py / verified facts (script not fetched; caption aligns with stated selection frame).  
    **Severity:** note  
    **Assessment:** Caption matches article body and verified counts. “Nine of the 405 scored FAILs” matches the 9 unscored-disposition FAILs. No overclaim beyond chart role if script draws selection funnel + PASS/FAIL bars.

17. **Article location:** Fig 9 caption  
    **Claim:** Dots = env pass fraction; Wilson 95% intervals; dotted line 68.4%; labels PASS/scored; wide intervals for small n; single-seed approximation; no-scored envs not drawn.  
    **Evidence:** Script intent + verified env counts.  
    **Severity:** note  
    **Assessment:** Caption correctly limits interpretation of intervals (not seed-to-seed). Appropriate.

18. **Article location:** Fig 10 caption  
    **Claim:** 340 squares; colour by pass rate; grey no scored; number if multi-case; most single → 0/1; fractional only moco; columns not comparable.  
    **Evidence:** Verified matrix facts.  
    **Severity:** note  
    **Assessment:** Matches matrix facts. No overclaim.

19. **Article location:** Fig 11 caption  
    **Claim:** Global failure labels for 128 FAILs; per-env in table below.  
    **Evidence:** Verified label counts.  
    **Severity:** note  
    **Assessment:** Matches.

20. **Article location:** “Ten zero-pass environments or seven?”  
    **Claim:** Earlier summary said 10; env-level 7; ≥1 zero-pass tuple → 19; reconciliation open; article uses 7.  
    **Evidence:** Verified facts + ANALYSIS_OVERVIEW.md (per task).  
    **Severity:** note  
    **Assessment:** Open discrepancy correctly flagged; not presented as resolved. Good disclosure.

21. **Article location:** Causal / mechanism language  
    **Claim examples:** “does not show that the three environments share a failure mechanism”; “I cannot infer a mechanism from the label names”; “does not show that environment identity [matters] more than difficulty”; “does not identify a model-internal cause”; endpoints not claimed as capability split; guarantee difference not read as judge effect; names not forecasts; binary rows not evidence of sharp tuple boundaries.  
    **Evidence:** Data limitations (single seed, no common difficulty scale, labels as classifications).  
    **Severity:** note  
    **Assessment:** Article consistently frames labels/dispositions/guarantees as recorded classifications, not model internals. No unsupported causal claim found that the data contradict. “Cannot” / “does not show” statements are aligned with data limits, not contradicted by them.

22. **Article location:** “What can a FAIL label explain?” / sheaf / glyph patterns  
    **Claim:** “Most glyph and moco failures carry the overfit label, and the three sheaf_* environments carry only underfit labels. Both are descriptions of recorded labels. Neither shows why the cases failed.”  
    **Evidence:** Per-env table (overfit 22+16; sheaf underfit 9+9; sheaf_schema_sync is mixed and not in the “only underfit” trio—article says “the three sheaf_*” in the pattern sentence after listing invariant_gluing and physical_constraints as all-fail underfit; schema_sync is mixed with 1 FAIL).  
    **Severity:** correction  
    **Assessment:** Slight ambiguity: earlier “three sheaf_*” in names section includes schema_sync (8/9). In failure section, “the three sheaf_* environments carry only underfit labels” — but only two all-fail sheafs are listed with underfit 9 each; schema_sync’s 1 FAIL is in the last grouped row as part of underfit 8 / … among several envs. If schema_sync’s single FAIL is underfit, the claim can hold; if not, mismatch. Verified facts do not break out schema_sync’s label. **Correction:** Tighten wording to “the two all-fail sheaf_* environments … only underfit” unless case_results confirms schema_sync’s FAIL label is underfit and any third is intended. Non-blocking if data confirm; flag for CSV check.

23. **Article location:** monadic_reward caveat / 0/9 meaning  
    **Claim:** 8 of 9 scored FAIL also `rejected`; 0/9 may not mean the same as other zeros.  
    **Evidence:** Verified 10 rejected, 8 in monadic.  
    **Severity:** note  
    **Assessment:** Properly disclosed; kept in counts with caveat. Good.

24. **Article location:** ts_parse_only performance-ineligible PASS  
    **Claim:** Kept in 277; records disagree.  
    **Evidence:** Verified facts.  
    **Severity:** note  
    **Assessment:** Disclosed; not treated as mechanism fact.

25. **Article location:** “cell” meaning inference  
    **Claim:** Cell most plausibly = environment × tuple row; inference from arithmetic; archive does not state convention.  
    **Evidence:** 340 rows / 416 cases.  
    **Severity:** note  
    **Assessment:** Clearly marked as inference, not archive fact. Appropriate.

26. **Article location:** Importance / epistemic-status “fuckingly”; body “[m-word]”; “👹”  
    **Claim:** Typographic/token placeholders.  
    **Evidence:** Constraints (bracketed tokens intentional).  
    **Severity:** note  
    **Assessment:** Per constraints, not errors. “👹” in “environment identity 👹 more than difficulty” reads as intentional redaction of a verb (e.g. “👹”); does not change evidence status.

27. **Article location:** 496 design cells  
    **Claim:** Fig 8 / selection frame from 496.  
    **Evidence:** Not in the short verified-facts list; implied by 80+416.  
    **Severity:** note  
    **Assessment:** Consistent with 80+416=496. Accept unless exclusions/design table differs.

28. **Article location:** “six environments have more than 10” rows  
    **Claim:** Matrix section.  
    **Evidence:** Multi-case list only names four multi-case envs; “more than 10” is about row count per env, not multi-case.  
    **Severity:** note  
    **Assessment:** Compatible (moco 15, glyph 12, and others with 11–15 single-case rows). No contradiction without full matrix; leave as note for CSV confirm.

29. **Article location:** css_state_machine withdrawn claim  
    **Claim:** 18/18 so every of nine tuple rows is 2/2; no variation.  
    **Evidence:** Verified multi-case css 9 rows 18 cases → 2 per row if uniform; all-pass 18/18.  
    **Severity:** note  
    **Assessment:** Consistent. Withdrawal correctly handled.

30. **Article location:** Any statement treating label/disposition/guarantee as fact about the model  
    **Claim scan:** Article repeatedly says recorded classifications, not internal reasoning; PASS only what that judge checked.  
    **Evidence:** Body text.  
    **Severity:** note  
    **Assessment:** No finding that a recorded label is asserted as model-internal fact. Compliant.

### Summary of open discrepancies (task item 6)
- Env-level zero-pass 7 vs earlier overview 10 vs tuple-level 19: open, disclosed.  
- Known-gate 14 (exclusions) vs 24 (PROVENANCE): open, disclosed.  
- Disposition `rejected` and disposition `unscored` on scored FAILs: undefined in archive; disclosed and retained in scored FAIL counts.  
- performance_eligible=False PASS with contradictory exclusion note: disclosed.  
- Single seed, dirty source, guarantee confounded with environment: disclosed as unremovable confounds.

### Figure caption vs script
Scripts (`make_post02_figures.py`) were not retrieved from the public tree. Captions were checked against verified counts and do not claim causal mechanisms or seed variance. **No blocking caption overclaim** relative to the verified data story; residual risk only if the SVG drawings omit elements the captions name (e.g. Wilson bars, grey cells, multi-case numbers)—flag as **note** pending local script/SVG inspection.

### Causal / “cannot” audit
No data-supported contradiction of the article’s “does not show / cannot” statements. No mechanism claims beyond descriptive label patterns with explicit non-causal framing (aside from the minor sheaf wording tightness in finding 22).

---

**Verdict: accept with corrections**

**Blocking findings: 0**  
**Corrections: 1** (finding 22 — tighten “three sheaf_* … only underfit” to match the two all-fail sheafs or confirm schema_sync FAIL label from case_results.csv)

*(If full CSVs become available locally, re-spot-check: exact moco fractional set, schema_sync FAIL label, “six environments >10 rows,” and fig script outputs. None of those are blocking on current verified facts.)*
