# `post_editor` review — Campaign 01 drafts

**Review status:** all five required drafts are complete and retained. This is an internal editorial pass by the same Arena Agent that conducted the analysis; it is not an independent reviewer or an external model replication.

## Publication decision

**Conditional pass, after verification of the mapped archive members.** Each article is a complete narrative draft, not an outline. There are 43 internal claim IDs across POST-01–POST-05; every ID has a corresponding row in [`claim_traceability.csv`](claim_traceability.csv) that maps the prose claim to a finding, quantitative result, case IDs, raw ZIP members, comparator files, or external reference. The row set currently has 43 entries and no unmapped draft markers.

The final public version should remove the double-bracket editorial tags only after the linked artifacts are checked. Do not remove the DOI/ACL/NeurIPS links or the dirty-source qualifiers.

## Per-post review

### POST-01 — non-monotone capability map / nominal difficulty

- Required thesis retained as a descriptive, sparse map; no general difficulty or latent-capability scale is asserted.
- Denominators are explicit: raw 131/194 PASS, report-listed-only 131/193, and primary provider-terminal exclusion 131/192. The 24 omitted IDs are not described as failures.
- The compile-only caveat remains adjacent to the primary denominator.
- Regex, CSS, SQL, spreadsheet, MoCo, and recurrent-depth examples have task-specific descriptions. Syntax/import failures are not presented as reasoning errors.
- **Guardrail:** preserve “one seed-0 run per selected cell,” and keep class names/hints and task-size confounds in the paragraph if shortening.

### POST-02 — epistemic games

- The result is stated as 7/7 exact selected cases, not a broad model score.
- The Bayesian equation and the source implementation are distinguished from recursive strategic reasoning; the post follows the task core’s explicit statement that v0 does not implement a fully recursive level-k engine.
- The prior-work section treats MindGames, Hi-ToM, and BigToM as distinct precedents, not equivalent tasks or direct score comparisons.
- **Guardrail:** never shorten the headline to “the model passed a recursive ToM test.” Keep “Bayesian inference over specified policies” in the deck or opening section.

### POST-03 — heterogeneous category/compositional results

- The 57/84 eligible total is stratified by the 5 behavioral-reference / 79 compile-only split; the campaign’s exploratory compile-only disclaimer is retained.
- Optimizer, lens, and physical-constraints examples cite task and judge behavior, including the visible-test distinction and unreferenced nominal placeholders.
- Clean-comparator findings are explicitly conditional on the campaign’s dirty repository record. They are not presented as proof of exact executed workspaces.
- **Guardrail:** do not replace the title/deck with “LLMs cannot do category theory” or imply that these software checks measure formal theorem proving.

### POST-04 — failure taxonomy and scalar scores

- Raw counts, both provider-terminal sensitivities, omissions, modes, and failure taxonomy are separated.
- The two `overfit_visible_tests` rows’ trusted scores and missing-file notes are called out; provider-terminal failures are not misattributed to the model.
- Telemetry disagreements are treated as metadata/provenance discrepancies. No reasoning content is reproduced and no cost estimate is inferred.
- The SWE-bench 7.8% statistic is explicitly restricted to that study’s setting and is not projected onto this archive.

### POST-05 — weird machines, surface versus hidden depth

- The regex pattern is stated as a one-run observation; name and hard-hint confounds are made prominent.
- “Hidden depth” is identified as different input-size proxies across environments, not one shared measure.
- The conclusion explicitly rejects both a general weird-machine capability claim and a causal “surface deception beats hidden depth” law.
- One explicitly tagged `SPECULATIVE` hypothesis is included: changed names or the hard-level hint may matter more than tested input length in this one task. It is described as untested and cannot be promoted to the headline.
- **Guardrail:** retain the class-name/hint confound and dirty-source caveat in any shorter version.

## Evidence and citation checks

- The archive SHA-256 and Git blob, selected case counts, omission list, provider-terminal rows, modes, failure labels, and final posterior examples are traceable to the locally archived ZIP and generated evidence tables.
- The campaign’s `repository.dirty=true` flag is retained whenever source-comparator observations are used. The source directory `/tmp/rl_eval_generator_base` has no Git metadata; the clean revision association comes from archived commit/config metadata, not independent Git verification.
- The citation list is targeted, not systematic. HELM, VarBench, MindGames, Hi-ToM, BigToM, and the SWE-bench patch-correctness study were checked against their linked publisher/ACL/NeurIPS pages. No global priority claim is made. The SWE-bench percentage is kept with its proper study-specific scope.
- Council documents remain untouched after saving. Their analyses were sequential role passes by one Arena Agent, not independent replications.

## Outstanding editorial actions before external publication

1. Re-run the traceability check after any sentence, number, denominator, citation, or case-example edit.
2. Confirm each listed raw member exists in `/tmp/atria-campaign-state-62.zip`; the generated case tables are navigation aids, not substitutes for the ZIP.
3. Keep the status as “draft” until a human editor reviews the voice, audience, and citations.
4. If the source comparator is later replaced by the campaign’s dirty tree, update only the separate source audit and claims that depend on it; do not silently rewrite raw results or frozen Mission 01/04 materials.
