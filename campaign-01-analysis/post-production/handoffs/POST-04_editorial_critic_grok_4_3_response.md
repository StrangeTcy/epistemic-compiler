**Editorial blueprint for the final POST-04 article**

**Proposed thesis**  
A single scalar (131/192 or similar) is the compressed endpoint of a pipeline whose stages—provider response, valid nonempty action/patch, source validation, runtime execution, judge guarantee, and terminal note—can each produce a zero for independent reasons. The archive’s value is the legible map of those stopping points and their mismatches, not a cleaned capability number. The central claim is therefore diagnostic and methodological: keep every tag, note, exclusion reason, and judge mode attached to its row so that attribution questions remain answerable.

**Opening strategy**  
Open with one concrete, anomalous row rather than a campaign summary. Lead with the `batchnorm_ema` or `moco` case whose `overfit_visible_tests` label is contradicted by `trusted_score=1.0` and a missing-companion-file note. State the tension immediately: the label points one way, the terminal record another. Ask what the zero actually records. This creates specificity and stakes faster than either draft’s general “what happened in each failed case?” setup while remaining fully grounded in the packet (F-09). Follow with the minimal context needed to make the row legible, then move to the broader denominator and pipeline questions.

**Section-by-section sequence**  
1. **Denominators and admissions** (raw 194, 24 omissions, report vs row-level provider transients → three explicit views: 194, 193, 192). Retain the sensitivity-table format from both drafts; make the 192-row analysis set an explicit editorial choice, not a corrected campaign figure.  
2. **Pipeline stages and the failure taxonomy** (walk the 61 failures through provider → action/patch → source → runtime → judge). Use the six-label table with behavioral-reference / compile-only split and the “where it stopped” column. Surface the 24 empty-patch cases and the three source-invalid syntax/import examples with concrete validator rejections.  
3. **When the label itself is wrong** (the two overfit rows and the two provider-terminal `invalid_action` rows). Keep the contradiction explicit; do not fold them into the 61.  
4. **Two judges, two guarantees** (72 behavioral_reference vs 120 compile-only; 56/16 vs 75/45 in the 192 set; report disclaimer on compile-only). Add the comparator examples of prompt/judge mismatch (compositional_optimizer, sheaf_physical_constraints) as concrete illustrations of what a behavioral guarantee actually checks.  
5. **Tracks as another tagging layer** (epistemic_games 7/7 under ml_debugging; the 30-case ML-debugging regrouping). Preserve the recorded track total while showing the semantic separation.  
6. **Telemetry discrepancies** (retry counters, reasoning_enabled flag vs usage logs). Treat strictly as metadata; no inference about internal reasoning.  
7. **What a row should carry / what the archive licenses** (minimum provenance fields; descriptive map only). End by stating the exact boundaries (one seed, dirty repo, mixed judge modes, no replication, no cost data).

**Example / equation / table plan**  
- One compact pipeline diagram (text or simple ASCII/Mermaid) showing the four-to-five gates with arrows labeled “else infrastructure / else agent-harness / else output vs policy / else execution / judge verdict.” Use only when it sharpens the sum-type point; keep it small.  
- No new equations beyond the minimal Outcome = ProviderDied + NoPatch + … + Pass (already in Writer A) if it clarifies the bool-casting problem.  
- Tables: (a) three-view denominator table, (b) six-label failure table with judge-mode split and “where stopped” column, (c) environment-family variation summary (range 0 %–100 % under documented guarantees) only if it illustrates heterogeneity without implying a ranking. All tables must carry the dirty-repo and one-seed caveats in their captions or immediately below.

**A/B elements worth retaining (with reasons)**  
- Writer A: “Whose zero is it?” framing and the explicit “sum type cast to bool” language—sharpens the attribution question and avoids generic “failures are different” prose.  
- Writer A: Concrete validator-rejection examples (import ast, weakref, re; syntax errors) and the behavioral-reference slice breakdown (only 3 of 16 failures are underfit)—grounds the pipeline claim.  
- Writer B: “Verdict needs provenance” and the repeated insistence that raw label + terminal note + analysis decision must remain distinct—excellent for caveat placement.  
- Writer B: Clean three-view table and the explicit “sensitivity set, not replacement” language—improves traceability.  
- Both: The epistemic-status block and the exact byline; the SWE-bench 7.8 % and HELM citations used only as bounded context, never as validation of this campaign.

**Elements neither draft handles well**  
- A compact, non-decorative pipeline diagram that makes the staged stopping points visually immediate.  
- Explicit side-by-side comparison of the two “overfit” rows (environment, judge mode, trusted_score, exact note) in a micro-table so the label/note mismatch is unmistakable at a glance.  
- A short paragraph on the three ML-debugging environments’ internal spread (moco 9/11 behavioral, glyph 0/8 behavioral, batchnorm_ema 0/11 compile-only) to show that even the regrouped 30 cases are not homogeneous.  
- Stronger visual separation between “recorded track total” and “analysis regrouping” so readers never mistake the latter for an edit to the archive.

**Exact evidence boundaries (do not exceed)**  
- Use only the supplied counts, labels, terminal notes, and F-01–F-17 findings.  
- Dirty-repo caveat on every claim about task/judge behavior.  
- One selected seed per case; no replication or population inference.  
- 24 omissions are never failures or passes.  
- Two provider-terminal rows stay outside the 192 analysis set; their raw `invalid_action` labels remain visible.  
- Compile-only results are exploratory per the campaign report.  
- No cost, no internal reasoning content, no causal claims about difficulty axes.  
- SWE-bench and HELM references remain narrow precedent only.

**Public-site fit checklist**  
- Frontmatter: `title`, `date: 2026-10-03`, `layout: post`, `{% include mathjax.html %}` immediately after if any math is used.  
- Byline exactly `*by <span class="icon-self">StrangeTcy</span>*`.  
- Epistemic-status `<dl>` in the prescribed order with the supplied phrasing adapted only for accuracy.  
- First-person curious/self-correcting voice; short argumentative `##` turns; questions that advance the argument.  
- No generic benchmark-report register, no stock superlatives, no overlong setup.  
- Links and citations placed where they do work (SWE-bench and HELM only as context).  
- Target 1,800–2,800 words; airy paragraphs; end by stating precisely what the evidence does and does not license.  
- No author-process meta-claims beyond the epistemic-status block.

**Final quality checklist for the writer**  
- Every limitation sits beside the claim it qualifies.  
- No row is re-labeled; raw labels and notes remain visible.  
- Denominators are always shown with their explicit exclusions.  
- Tables and examples are source-grounded and never decorative.  
- The article ends on the descriptive-map claim, not a stronger capability statement.  
- Voice matches the reference excerpts: precise, willing to self-correct, technically literate, first-person.
