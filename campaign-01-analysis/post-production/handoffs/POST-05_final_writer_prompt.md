# Final public-post writer — POST-05

Synthesize a real, publication-ready StrangeTcy article from the attached evidence dossier, the exact internal source draft, both independently produced drafts, the critic's blueprint, and verbatim content from actual StrangeTcy reference posts. The blueprint is guidance, not a substitute for checking the evidence. You must reconcile it with the sources.

Return only the complete article in Markdown, with no wrapper or commentary. Use the target Jekyll convention:

---
title: "A specific public title"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

Use the site's epistemic-status HTML pattern when useful, but make every authorship/process statement strictly accurate. Do not copy reference-post authorship claims. Do not call internal work a public result.

Requirements:
- Aim for 1,800–2,500 words; lead with an argument, not a campaign summary. Make a StrangeTcy research essay, not a stitched paraphrase or benchmark report.
- Keep exact factual claims, denominators, judge guarantees, exclusions, and evidence status traceable to the dossier. Include the source-comparator/dirty-working-tree limitation, one-seed scope, and judge defects/compile-only caveat where relevant. No invented numbers, results, links, or citations.
- Do not imply independent replication or independent model execution. The campaign is one selected run/seed per cell; role-separated passes do not become replications.
- For POST-02, explicitly say the epistemic-games task is Bayesian inference over stipulated policies and is not recursive ToM. For POST-05, do not imply that a Rule 110 example or bounded code-repair task establishes Turing completeness/general computation. For POST-03, do not present the heterogeneous category track as one validated category-theory score. For POST-01 and POST-04, do not flatten mixed judge modes, terminal provider notes, or failures at different pipeline stages into one capability scalar.
- Keep all research caveats near the claims they qualify. Explain equations and axes in prose; use mathematics, tables, or diagrams only when they add information.
- Use the **actual reference excerpts** to calibrate voice, pacing, and structure. Do not reproduce distinctive phrases/examples. Do not copy any internal trace ID, `F-xx` reference, source path, archive member, internal filename, editor note, or POST/draft label into public copy.
- Use syntactically valid Markdown, links, Jekyll frontmatter/includes, and a specific title that produces a clean slug. Do not add unresolved TODOs/placeholders.

POST-05 editorial-input note: the editorial-critic artifact is a compiler-assembled bundle of two separately labeled critiques, not a synthesized consensus or ranking. Reconcile recommendations against the evidence packet, the source draft, and both candidate articles; do not reproduce critic labels or internal workflow details in the public article. Some recommendations conflict, so do not follow checklist items mechanically; the final-writer template and source evidence take precedence, including its 1,800–2,500-word target. Verify factual diagnoses directly against the source text: the second critique gives a count of one instance in Writer A and three in Writer B for “fuckingly,” but the captured drafts contain none in Writer A and one in Writer B. Do not repeat that phrase in the final article.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post05_prepare_post:response | source_sha256=0ec5bd833da23585f48f4141dd1cd4f9cd3d793e922f27f87f2b043cf5d45942 | rendered_sha256=8f301efbae02f0677ef5889034383607b886fd1c23bb75a3f13dbbb6861a1e26 ]]]
# Compiler evidence packet — POST-05

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## BEGIN INPUT ARTIFACT: 01 — source_draft_POST-05
Source snapshot SHA-256: `18c5ba9c58cba696cab947bcb9ed19c844911291caad87e880f5304fd71e1e13`
Rendered message SHA-256: `18c5ba9c58cba696cab947bcb9ed19c844911291caad87e880f5304fd71e1e13`
Original reference: `mission:source_draft_POST-05`

# POST-05 — Surface cues, hidden depth, and what the weird-machine sweep can’t prove

**Dek:** Several selected code tasks pass at larger input sizes and fail under altered surface labels. The strongest contrast is interesting—but a one-run, confounded pilot is not evidence that a model detects “weird machines” in general.

**Draft**

A weird-machine benchmark asks whether a model can infer a program’s operative behavior from an unfamiliar task surface, rather than simply follow conventional names and hints. The campaign archive contains a small family of such code tasks: regex, CSS, SQL, spreadsheets, a CI dependency graph, and a template interpreter. Across 30 eligible selected cases, 25 pass. That is a description of these implementations and this run—not a general weird-machine capability score. ⟦POST-05-C01 · F-10⟧

The regex Rule 110 task is the sharpest contrast. The prompt asks for one cellular-automaton update encoded with regular expressions. The nominal hidden-depth axis changes input-string length to 32, 128, or 512. At the easy surface label, the model passes all three selected lengths. At the easy length of 32, the medium and hard surface labels fail: their outputs have lengths 34 and 66. So the observed cells look like a surface-label failure paired with length invariance under the easy label. ⟦POST-05-C02 · F-06/F-10⟧

But “surface deception” is not isolated. In the clean source comparator, the surface levels correspond to different class names; the hard prompt also adds an implementation-performance hint. A name change can affect retrieval or code conventions even if no underlying computation changes, while an extra hint changes the instruction itself. There is one seed-0 model run per selected cell. The archive therefore supports the exact response pattern, not a causal conclusion that class names fooled the model or that hidden depth did not matter. ⟦POST-05-C03 · F-01/F-10⟧

A plausible hypothesis—still untested—is that the changed names or extra hard-level hint mattered more than input-string length in this particular task. The current sweep cannot distinguish those factors from sampling variation or their interaction. ⟦POST-05-C09 · F-18⟧

Other environments add context, but do not repair that identification problem. CSS uses a parity-selector implementation while the input bit count changes from 3 to 4 to 5. Its easy-surface cases yield a partial score at 3 bits, a source-invalid result at 4 bits due to a disallowed import, and a pass at 5 bits; the surface sweep at 3 bits is fail/pass/pass. SQL passes at chain lengths 6 and 25 but fails source validation at 12 because of an unterminated triple-quoted string. The spreadsheet task passes all five selected cases over its class-name and grid-length contrasts. These patterns are non-monotone at the level of archived outcomes, but the depth axes measure different sizes and several failures occur before behavioral tests. ⟦POST-05-C04 · F-06/F-09/F-10⟧

Across the six five-case weird-machine environments, the 25/30 pass count combines distinct programs, different judges, and different input-size definitions. The regex task checks output length and fixed seeded strings; CSS checks parity behavior; SQL runs a fixed-point task; spreadsheets check dataflow; CI checks a dependency graph; and the template interpreter checks a small language. “Hidden depth” is not a common unit across them. A 512-character input, a 5-bit selector, a 25-node chain, and a larger spreadsheet grid may impose different computational demands. ⟦POST-05-C05 · F-10⟧

The measurement principle is not novel: VarBench already demonstrates dynamic variable perturbation and repeated sampling, and other benchmark work has emphasized multi-scenario coverage and explicit controls. The contribution here is narrower—a local case pattern plus a source audit: it identifies the regex name/hint confound and, elsewhere in the category track, nominal controls with no direct template references in the clean comparator. Because the campaign records `repository.dirty=true`, those source findings do not establish exact paid-run workspaces. ⟦POST-05-C06 · F-01/F-10/F-14/F-17⟧

A stronger experiment would separate the manipulations. Keep the class name fixed while changing only the implementation hint; then vary class names without changing the hint. Generate multiple equivalent task instances at each input size, randomize their order, and run multiple seeds. Before the model sees an instance, compare the rendered task, starter code, visible tests, and judge inputs across levels; block any advertised axis that changes no relevant artifact. Finally, score exact behavior separately from valid patch creation and source/runtime validity. ⟦POST-05-C07 · F-06/F-10/F-14⟧

The current evidence is still useful. It shows where surface labels, size changes, validators, and task semantics need to be disentangled. But the headline should remain local: **in one archived sweep, this model passed several larger-input variants and failed two altered regex-surface variants under a confounded, single-run design.** It does not prove a general ability to detect computational weirdness, nor a law that “surface deception beats hidden depth.” ⟦POST-05-C08 · F-06/F-10/F-16⟧

**Editor’s note:** Internal evidence tags map to findings and exact archive members in `claim_traceability.csv`; source-comparator claims retain the dirty-source caveat.

## END INPUT ARTIFACT: 01 — source_draft_POST-05

## BEGIN INPUT ARTIFACT: 02 — house_style
Source snapshot SHA-256: `590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973`
Rendered message SHA-256: `3d5b7ccaefb1983b86aae0b92e9a634d2927bf21c8040769de4fcf1bd1af71cd`
Original reference: `mission:house_style`

Target Jekyll frame: YAML frontmatter with `title`, `date: 2026-10-03`, `layout: post`; when using math, place `{% include mathjax.html %}` immediately after it. Then use the exact byline `*by <span class="icon-self">StrangeTcy</span>*` and the site's `<dl class="epistemic-status">` fields, in order: Original ideas, Synthesis, Prose, Certainty, Importance. Attribute the actual Arena writing process accurately; do not invent outside authors.

Voice: first-person, curious, technically literate, willing to self-correct. Open in prose, not an `Introduction`; use short, specific `##` argumentative turns and airy paragraphs. Questions should move the argument. End by stating what the evidence does and does not license. Links/citations belong where they matter; avoid a generic benchmark-report register. Target 1,800–2,800 words without padding.

## END INPUT ARTIFACT: 02 — house_style

## BEGIN INPUT ARTIFACT: 03 — style_reference_material
Source snapshot SHA-256: `bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4`
Rendered message SHA-256: `ab6260bde7bc2d8c35224efb927dc757b30411b02c460f5c334ce792e50274f8`
Original reference: `mission:style_reference_material`

Short excerpts from actual StrangeTcy/strangetcy.github.io posts at revision bcc89c392920b3be172a27eec10ad205b58d4fa3; style evidence only, not wording to reuse.
### The Diagram Is the Spec — a concrete distinction (2026-09-27)
A unit test says:

> On these inputs, produce these outputs.

A diagram says:

> **These two paths are the same morphism.**

### Knowing What Kind of Problem You Are In — conceptual opening (2026-09-26)
Most benchmarks hand the agent its context for free.

Not deliberately. It is what happens when you collect tasks: each one arrives already classified. *This is a Python bug, fix it. This is a competition problem, solve it. This is a paper, reproduce it.* The agent is rarely asked to determine what sort of situation it has walked into before deciding how to act, because the first line of the prompt has already told it.

### The Next Question Is Part of the Game — question-led opening (2026-09-30)
Suppose I want you to make the wrong decision.

The stupid way is to lie to you; the more interesting way is to make you run the wrong experiment.

I don't need to convince you that the machine is healthy if I can make you spend your diagnostic budget measuring the optimiser while the representation collapses. I don't need to make you believe a particular false proposition if I can determine which source you consult, which hypothesis you test first, or which anomaly you dismiss as irrelevant.

The strategic object is no longer just your current answer -- it's your **next question**.

### Lying With Truth — visible self-correction (2026-10-01)
The first formalisation was wrong.

I modelled a world-model as a graph $G$ & looked for a message $m$ maximising $D\big(G,\mathrm{Update}(G,m)\big)$: the bigger the change, the stronger the attack.

That's backwards.

A short, decisive true observation *should* demolish a bad theory. An excellent reasoner undergoes violent revision on purpose. If a physicist has a beautiful theory and then someone produces a clean experiment that kills it, “the model changed a lot” is not evidence that the experiment was an attack.

## END INPUT ARTIFACT: 03 — style_reference_material

## BEGIN INPUT ARTIFACT: 04 — references
Source snapshot SHA-256: `54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0`
Rendered message SHA-256: `f2651d71aacb8d3d2786fa6cb745916431bdf04cdab568720c61f06bac247320`
Original reference: `mission:references`

POST-05 prior-work references from the source draft; context only, not validation of this campaign.

- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation and repeated sampling for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: broad scenario coverage and multiple metrics, as context for avoiding a single-score interpretation. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim.

## END INPUT ARTIFACT: 04 — references

## BEGIN INPUT ARTIFACT: 07 — trace_rows_POST-05
Source snapshot SHA-256: `30a2b2fb79d4556cc4f7af05ec560b11b46dedb7e3589d26be546e1439fe410a`
Rendered message SHA-256: `6153f2b21de05cd60d3b2ae330729178df79e49045a2942ca5e854e25098ca8d`
Original reference: `mission:trace_rows_POST-05`

post_id,claim_id,finding_ids
POST-05,POST-05-C01,F-10
POST-05,POST-05-C02,F-06;F-10
POST-05,POST-05-C03,F-01;F-10
POST-05,POST-05-C09,F-18
POST-05,POST-05-C04,F-06;F-09;F-10
POST-05,POST-05-C05,F-10
POST-05,POST-05-C06,F-01;F-10;F-14;F-17
POST-05,POST-05-C07,F-06;F-10;F-14
POST-05,POST-05-C08,F-06;F-10;F-16

## END INPUT ARTIFACT: 07 — trace_rows_POST-05

## BEGIN INPUT ARTIFACT: 08 — relevant_findings_POST-05
Source snapshot SHA-256: `e29c577bb4da46c88cc6ce446dfe9a0256c9c950df697e2f631a0f4479b851b1`
Rendered message SHA-256: `59b69415f4377205dd663e1fcdfebe2fb541e5a388eb74424da2291edb80c759`
Original reference: `mission:relevant_findings_POST-05`

{"claim_ids":["POST-05-C01","POST-05-C02","POST-05-C03","POST-05-C04","POST-05-C05","POST-05-C06","POST-05-C07","POST-05-C08","POST-05-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"Selected nominal-axis outcomes are heterogeneous and sometimes nonmonotone; the archived `easy`/`medium`/`hard` labels do not form a common calibrated scalar difficulty scale.","confidence":"HIGH for these observed case outcomes; LOW for any causal effect of a nominal axis.","id":"F-06","limitations":["One selected case/seed per cell and no cell-level replications.","Many comparisons are one-factor contrasts around a single baseline, not full factorial designs.","Axis names such as hidden_depth map to different quantities in different environments."],"quantitative_result":"Examples: regex at easy surface passes at lengths 32/128/512, while medium/hard surface labels fail at length 32; CSS at easy surface scores 0.416667/0/1.0 over 3/4/5 bits (the middle row is source-invalid); SQL at easy surface passes at graph-chain lengths 6 and 25 but has a source-invalid length-12 case; moco visible-test levels are pass/fail/pass.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"The weird_machine track shows task-specific successes and failures under regex, CSS, SQL, spreadsheet, CI, and template tasks; the controlled surface/depth pattern is especially sharp in regex but confounded and unreplicated.","confidence":"HIGH for the selected case outcomes; LOW for generalized surface/depth causality.","id":"F-10","limitations":["One run per selected cell, no seed-level replication, and only a sparse design.","The regex surface manipulation bundles class name and an extra hard-level hint.","CSS and SQL selected failures include source-validation errors."],"quantitative_result":"25/30 eligible PASS overall. Regex 3/5; CSS 3/5; SQL 4/5; spreadsheet 5/5; CI dependency graph 5/5; template interpreter 5/5. At easy regex surface, all 3 string lengths pass; at easy string length, the other 2 class-name variants fail.","status":"OBSERVED"},{"claim":"The category-track source comparator indicates several advertised axes were not implemented in the environment templates, so nominal coverage can overstate the number of distinct interventions.","confidence":"HIGH for no direct reference in the inspected clean source files; MEDIUM for the claim about executed paid cases because the recorded repository was dirty.","id":"F-14","limitations":["The static scan does not execute generation or compare every rendered task bundle.","Only selected configurations were scanned; unsupported and gate-blocked cases were not model-run."],"quantitative_result":"The static scan finds ten no-reference control/variable axes across nine category environments, including both axes in compositional_optimizer; details are in axis_placeholder_audit.csv and source_implementation_audit.md.","status":"INFERRED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"},{"claim":"In this particular regex task and model run, surface class names or the hard-level performance hint may have influenced the two failures more than the tested input-string length; this is an untested hypothesis, not an inferred causal effect.","confidence":"LOW; deliberately speculative.","id":"F-18","limitations":["Only five selected rows from one model/configuration; no repeated seed per cell.","Surface label bundles class-name changes and an added hard-level hint.","The clean comparator is not proven identical to the dirty paid-run source."],"quantitative_result":"At easy surface, selected lengths 32, 128, and 512 all pass. At string length 32, the medium and hard surface variants fail with output lengths 34 and 66. The hard prompt adds a performance note.","status":"SPECULATIVE"}],"post_id":"POST-05","schema_version":1,"trace_finding_ids":["F-01","F-06","F-09","F-10","F-14","F-16","F-17","F-18"]}

## END INPUT ARTIFACT: 08 — relevant_findings_POST-05

## BEGIN INPUT ARTIFACT: 09 — evidence_extract_POST-05
Source snapshot SHA-256: `a466b52cb0776b4cce89212f3ba02cfb0338c368b8505aa1e554ecb5b7f1dfd6`
Rendered message SHA-256: `b1f18fc5b56446429645f80a557acdc0724885c08f5f486b399794c8db01b92c`
Original reference: `mission:evidence_extract_POST-05`

Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## END INPUT ARTIFACT: 09 — evidence_extract_POST-05

## BEGIN INPUT ARTIFACT: 10 — limitations_POST-05
Source snapshot SHA-256: `5ade5de4559b32c6de091ea33e381ff9698edb0e71e9f74ee70bc294e76d5020`
Rendered message SHA-256: `5ade5de4559b32c6de091ea33e381ff9698edb0e71e9f74ee70bc294e76d5020`
Original reference: `mission:limitations_POST-05`

# Limitations to preserve — The Surface Can Be a Small Machine

1. The task tests a single Rule 110 update via regex; it does not show that the tested expression performs arbitrary iteration or that the model represented a “machine.”
2. Easy-surface size values 32/128/512 each have one selected seed-0 run; three passes are not a size-invariance estimate.
3. At fixed length 32, the medium/hard variants bundle class-name changes, and hard adds a performance hint; no causal effect is isolated.
4. The judge checks four specific criteria, including 15 seeded strings and length preservation; passing those checks is not a proof of general regex correctness.
5. The 25/30 track total combines six task families, not a shared computational-depth unit.
6. CSS/SQL include source-validator failures; do not present these as evidence of semantic inability.
7. `repository.dirty=true`; clean-comparator prompt/config/judge observations are not proof of exact paid-run source identity.
8. The axis placeholder scan concerns category tasks; it is adjacent benchmark QA, not direct evidence about the regex manipulation.
9. “Weird machine” and “surface deception” are conceptual interpretations; the archive does not directly measure an internal recognition process.
10. No complexity lower bound, Turing-completeness proof, or general surface-versus-depth law is supported.

## END INPUT ARTIFACT: 10 — limitations_POST-05

## BEGIN INPUT ARTIFACT: 11 — source_audit_POST-05
Source snapshot SHA-256: `26804ac767c24391761e94f43d850b8ecba395c2aeb60c29f764a87ea995c0be`
Rendered message SHA-256: `a3b7c00b7463d5d3936a61b0d9c6f768f6085d52580baec5b29227b90e8cd8e8`
Original reference: `mission:source_audit_POST-05`

## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## END INPUT ARTIFACT: 11 — source_audit_POST-05

## BEGIN INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-05
Source snapshot SHA-256: `512256464f66c5bf8a075c229a1bef4ad428b6ffec0ba074c0ec58d6d7f7fa66`
Rendered message SHA-256: `465322a9bf49d369ece7e96bd539a44c9766495467e2d3d67683a8bdbfd41987`
Original reference: `mission:evidence_analysis_family_summary_POST-05`

analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
weird_machine,30,30,25,5,0.8333333333333334,30,25,5,0,0,0

## END INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-05

## BEGIN INPUT ARTIFACT: 13 — evidence_axis_summary_POST-05
Source snapshot SHA-256: `30fe936cb6cf794533fead907529b9d798baca6f65e83dc3feff2561886c9e82`
Rendered message SHA-256: `b13c2fcaf23a797340cfd742897b6f5bfb653195d3c91e63c973263e878b8534`
Original reference: `mission:evidence_axis_summary_POST-05`

environment,axis,level,control,recorded,eligible,passes,fails,rate,judge
ci_dependency_graph,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
ci_dependency_graph,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,0,1,0.0,behavioral_reference
css_state_machine,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,0,1,0.0,behavioral_reference
css_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,0,1,0.0,behavioral_reference
css_state_machine,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
css_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,0,1,0.0,behavioral_reference
regex_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
regex_state_machine,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
regex_state_machine,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
regex_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,0,1,0.0,behavioral_reference
regex_state_machine,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,0,1,0.0,behavioral_reference
regex_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
regex_state_machine,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,0,1,0.0,behavioral_reference
regex_state_machine,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,0,1,0.0,behavioral_reference
regex_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
regex_state_machine,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,0,1,0.0,behavioral_reference
sql_fixed_point,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
sql_fixed_point,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,0,1,0.0,behavioral_reference
template_interpreter,hidden_depth,easy,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,hidden_depth,hard,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,hidden_depth,medium,"{""surface_deceptiveness"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,hidden_depth,easy,"{""surface_deceptiveness"": ""hard""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,hidden_depth,easy,"{""surface_deceptiveness"": ""medium""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,surface_deceptiveness,easy,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,surface_deceptiveness,hard,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,surface_deceptiveness,medium,"{""hidden_depth"": ""easy""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,surface_deceptiveness,easy,"{""hidden_depth"": ""hard""}",1,1,1,0,1.0,behavioral_reference
template_interpreter,surface_deceptiveness,easy,"{""hidden_depth"": ""medium""}",1,1,1,0,1.0,behavioral_reference

## END INPUT ARTIFACT: 13 — evidence_axis_summary_POST-05

## BEGIN INPUT ARTIFACT: 15 — evidence_case_results_POST-05
Source snapshot SHA-256: `7916f99a3e606a1de14b7d43184a5ea612f22feab9da0a7fbd9a2377b1dfe87b`
Rendered message SHA-256: `e3d63d95e066638979929311ce730df92cc70a8036a5ef58fbce2f8a25082e1d`
Original reference: `mission:evidence_case_results_POST-05`

case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason
ci_dependency_graph__surface_deceptiveness=easy_hidden_depth=easy__seed-0,ci_dependency_graph,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
ci_dependency_graph__surface_deceptiveness=easy_hidden_depth=hard__seed-0,ci_dependency_graph,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
ci_dependency_graph__surface_deceptiveness=easy_hidden_depth=medium__seed-0,ci_dependency_graph,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
ci_dependency_graph__surface_deceptiveness=hard_hidden_depth=easy__seed-0,ci_dependency_graph,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
ci_dependency_graph__surface_deceptiveness=medium_hidden_depth=easy__seed-0,ci_dependency_graph,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
css_state_machine__surface_deceptiveness=easy_hidden_depth=easy__seed-0,css_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,FAIL,0.416667,underfit,[],True,
css_state_machine__surface_deceptiveness=easy_hidden_depth=hard__seed-0,css_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
css_state_machine__surface_deceptiveness=easy_hidden_depth=medium__seed-0,css_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,FAIL,0.0,source_invalid,"[""Source validation failed:\nVIOLATIONS:\n  css_logic.py: Line 42: disallowed import 're' (top-level 're' not in allowlist)\n\nNOTE: This validator is NOT a security sandbox. Docker isolation is.\nSome bypasses (getattr, string concat, etc.) are not caught here.\n\n""]",True,
css_state_machine__surface_deceptiveness=hard_hidden_depth=easy__seed-0,css_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
css_state_machine__surface_deceptiveness=medium_hidden_depth=easy__seed-0,css_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
regex_state_machine__surface_deceptiveness=easy_hidden_depth=easy__seed-0,regex_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
regex_state_machine__surface_deceptiveness=easy_hidden_depth=hard__seed-0,regex_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
regex_state_machine__surface_deceptiveness=easy_hidden_depth=medium__seed-0,regex_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
regex_state_machine__surface_deceptiveness=hard_hidden_depth=easy__seed-0,regex_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,FAIL,0.208333,underfit,"[""Morphism Error Report: Collapsed on length mismatch (in=32, out=66). ""]",True,
regex_state_machine__surface_deceptiveness=medium_hidden_depth=easy__seed-0,regex_state_machine,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,FAIL,0.208333,underfit,"[""Morphism Error Report: Collapsed on length mismatch (in=32, out=34). ""]",True,
spreadsheet_dataflow__surface_deceptiveness=easy_hidden_depth=easy__seed-0,spreadsheet_dataflow,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
spreadsheet_dataflow__surface_deceptiveness=easy_hidden_depth=hard__seed-0,spreadsheet_dataflow,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
spreadsheet_dataflow__surface_deceptiveness=easy_hidden_depth=medium__seed-0,spreadsheet_dataflow,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
spreadsheet_dataflow__surface_deceptiveness=hard_hidden_depth=easy__seed-0,spreadsheet_dataflow,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
spreadsheet_dataflow__surface_deceptiveness=medium_hidden_depth=easy__seed-0,spreadsheet_dataflow,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
sql_fixed_point__surface_deceptiveness=easy_hidden_depth=easy__seed-0,sql_fixed_point,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
sql_fixed_point__surface_deceptiveness=easy_hidden_depth=hard__seed-0,sql_fixed_point,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
sql_fixed_point__surface_deceptiveness=easy_hidden_depth=medium__seed-0,sql_fixed_point,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,FAIL,0.0,source_invalid,"[""Source validation failed:\nVIOLATIONS:\n  query_module.py: SyntaxError: unterminated triple-quoted string literal (detected at line 25) (query_module.py, line 21)\n\nNOTE: This validator is NOT a security sandbox. Docker isolation is.\nSome bypasses (getattr, string concat, etc.) are not caught here.\n\n""]",True,
sql_fixed_point__surface_deceptiveness=hard_hidden_depth=easy__seed-0,sql_fixed_point,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
sql_fixed_point__surface_deceptiveness=medium_hidden_depth=easy__seed-0,sql_fixed_point,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
template_interpreter__surface_deceptiveness=easy_hidden_depth=easy__seed-0,template_interpreter,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
template_interpreter__surface_deceptiveness=easy_hidden_depth=hard__seed-0,template_interpreter,weird_machine,weird_machine,0,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
template_interpreter__surface_deceptiveness=easy_hidden_depth=medium__seed-0,template_interpreter,weird_machine,weird_machine,0,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
template_interpreter__surface_deceptiveness=hard_hidden_depth=easy__seed-0,template_interpreter,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
template_interpreter__surface_deceptiveness=medium_hidden_depth=easy__seed-0,template_interpreter,weird_machine,weird_machine,0,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,

## END INPUT ARTIFACT: 15 — evidence_case_results_POST-05

## BEGIN INPUT ARTIFACT: 16 — evidence_environment_summary_POST-05
Source snapshot SHA-256: `f530e5e0e1d1cdf70dace0a314e4dc27b0cc827e10ab8a8efd0b3a33b1ff9162`
Rendered message SHA-256: `a3adcc699a5245db11fd8444139a6b1a5b92f52584371fa92cb165e88aec31ba`
Original reference: `mission:evidence_environment_summary_POST-05`

environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
ci_dependency_graph,5,5,5,0,1.0,5,5,0,0,0,0
css_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
regex_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
spreadsheet_dataflow,5,5,5,0,1.0,5,5,0,0,0,0
sql_fixed_point,5,5,4,1,0.8,5,4,1,0,0,0
template_interpreter,5,5,5,0,1.0,5,5,0,0,0,0

## END INPUT ARTIFACT: 16 — evidence_environment_summary_POST-05

## BEGIN INPUT ARTIFACT: 17 — evidence_failure_details_POST-05
Source snapshot SHA-256: `8304a428e1e04f897c5dbea6070989875777cb182fc42173cf146811d8cc36d8`
Rendered message SHA-256: `704c29a318f0d072fcfe7647d5f9e92a7caceabbb714705a43ec383c7469b8b2`
Original reference: `mission:evidence_failure_details_POST-05`

environment,condition,judge,score,failure,detail
css_state_machine,surface_deceptiveness=easy_hidden_depth=easy,behavioral_reference,0.416667,underfit,
css_state_machine,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source validator rejected import re
regex_state_machine,surface_deceptiveness=hard_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 66"
regex_state_machine,surface_deceptiveness=medium_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 34"
sql_fixed_point,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source syntax error: unterminated triple-quoted string

## END INPUT ARTIFACT: 17 — evidence_failure_details_POST-05

## BEGIN INPUT ARTIFACT: 18 — evidence_failure_taxonomy_POST-05
Source snapshot SHA-256: `49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4`
Rendered message SHA-256: `379b2b331fd20d910a3cbf6277cf82680f95fd19c160fc8042c8b3fd5f9d12b5`
Original reference: `mission:evidence_failure_taxonomy_POST-05`

failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"

## END INPUT ARTIFACT: 18 — evidence_failure_taxonomy_POST-05

## Compiler-only validator metadata (never copy into public copy)
<!-- POST_PRODUCTION_VALIDATOR_METADATA
{"allowed_numbers": ["0", "0.0", "0.03278688524590164", "0.04918032786885246", "0.16393442622950818", "0.208333", "0.32786885245901637", "0.39344262295081966", "0.416667", "0.6", "0.8", "0.8333333333333334", "1", "1.0", "10", "110", "12", "128", "15", "17", "192", "2", "20", "21", "24", "25", "256", "2968", "3", "30", "31", "32", "33", "34", "4", "42", "5", "512", "6", "61", "66", "7", "7.8", "7.8%", "8", "9"], "evidence_input_sha256": {"mission:campaign_provenance": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "mission:evidence_analysis_family_summary_POST-05": "512256464f66c5bf8a075c229a1bef4ad428b6ffec0ba074c0ec58d6d7f7fa66", "mission:evidence_axis_summary_POST-05": "30fe936cb6cf794533fead907529b9d798baca6f65e83dc3feff2561886c9e82", "mission:evidence_campaign_scope_POST-05": "a6212933369f324049fd0732a97b290d9ec17469d7ed106bd9c5267778cde4da", "mission:evidence_case_results_POST-05": "7916f99a3e606a1de14b7d43184a5ea612f22feab9da0a7fbd9a2377b1dfe87b", "mission:evidence_environment_summary_POST-05": "f530e5e0e1d1cdf70dace0a314e4dc27b0cc827e10ab8a8efd0b3a33b1ff9162", "mission:evidence_extract_POST-05": "a466b52cb0776b4cce89212f3ba02cfb0338c368b8505aa1e554ecb5b7f1dfd6", "mission:evidence_failure_details_POST-05": "8304a428e1e04f897c5dbea6070989875777cb182fc42173cf146811d8cc36d8", "mission:evidence_failure_taxonomy_POST-05": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "mission:house_style": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "mission:limitations_POST-05": "5ade5de4559b32c6de091ea33e381ff9698edb0e71e9f74ee70bc294e76d5020", "mission:references": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "mission:relevant_findings_POST-05": "e29c577bb4da46c88cc6ce446dfe9a0256c9c950df697e2f631a0f4479b851b1", "mission:source_audit_POST-05": "26804ac767c24391761e94f43d850b8ecba395c2aeb60c29f764a87ea995c0be", "mission:source_draft_POST-05": "18c5ba9c58cba696cab947bcb9ed19c844911291caad87e880f5304fd71e1e13", "mission:style_reference_material": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "mission:trace_rows_POST-05": "30a2b2fb79d4556cc4f7af05ec560b11b46dedb7e3589d26be546e1439fe410a", "mission:workflow_input_manifest": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158"}, "finding_ids": ["F-01", "F-06", "F-09", "F-10", "F-14", "F-15", "F-16", "F-17", "F-18"], "post_id": "POST-05", "publication_date": "2026-10-03", "source_input_records": [{"attachment_index": 0, "reference": "mission:source_draft_POST-05", "sha256": "18c5ba9c58cba696cab947bcb9ed19c844911291caad87e880f5304fd71e1e13", "size_bytes": 5510, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/source_draft.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/source_draft.md"}, {"attachment_index": 1, "reference": "mission:house_style", "sha256": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "size_bytes": 12397, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/house_style.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/house_style.md"}, {"attachment_index": 2, "reference": "mission:style_reference_material", "sha256": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "size_bytes": 19939, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md"}, {"attachment_index": 3, "reference": "mission:references", "sha256": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "size_bytes": 3532, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/references.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/references.md"}, {"attachment_index": 4, "reference": "mission:campaign_provenance", "sha256": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "size_bytes": 13690, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md"}, {"attachment_index": 5, "reference": "mission:workflow_input_manifest", "sha256": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158", "size_bytes": 28349, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json"}, {"attachment_index": 6, "reference": "mission:trace_rows_POST-05", "sha256": "30a2b2fb79d4556cc4f7af05ec560b11b46dedb7e3589d26be546e1439fe410a", "size_bytes": 10202, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/trace_rows.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/trace_rows.csv"}, {"attachment_index": 7, "reference": "mission:relevant_findings_POST-05", "sha256": "e29c577bb4da46c88cc6ce446dfe9a0256c9c950df697e2f631a0f4479b851b1", "size_bytes": 37908, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/relevant_findings.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/relevant_findings.json"}, {"attachment_index": 8, "reference": "mission:evidence_extract_POST-05", "sha256": "a466b52cb0776b4cce89212f3ba02cfb0338c368b8505aa1e554ecb5b7f1dfd6", "size_bytes": 1723, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence_extract.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence_extract.md"}, {"attachment_index": 9, "reference": "mission:limitations_POST-05", "sha256": "5ade5de4559b32c6de091ea33e381ff9698edb0e71e9f74ee70bc294e76d5020", "size_bytes": 1381, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/limitations.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/limitations.md"}, {"attachment_index": 10, "reference": "mission:source_audit_POST-05", "sha256": "26804ac767c24391761e94f43d850b8ecba395c2aeb60c29f764a87ea995c0be", "size_bytes": 6024, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/source_audit_excerpt.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/source_audit_excerpt.md"}, {"attachment_index": 11, "reference": "mission:evidence_analysis_family_summary_POST-05", "sha256": "512256464f66c5bf8a075c229a1bef4ad428b6ffec0ba074c0ec58d6d7f7fa66", "size_bytes": 406, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/analysis_family_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/analysis_family_summary.csv"}, {"attachment_index": 12, "reference": "mission:evidence_axis_summary_POST-05", "sha256": "30fe936cb6cf794533fead907529b9d798baca6f65e83dc3feff2561886c9e82", "size_bytes": 13453, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/axis_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/axis_summary.csv"}, {"attachment_index": 13, "reference": "mission:evidence_campaign_scope_POST-05", "sha256": "a6212933369f324049fd0732a97b290d9ec17469d7ed106bd9c5267778cde4da", "size_bytes": 3472, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/campaign_scope.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/campaign_scope.json"}, {"attachment_index": 14, "reference": "mission:evidence_case_results_POST-05", "sha256": "7916f99a3e606a1de14b7d43184a5ea612f22feab9da0a7fbd9a2377b1dfe87b", "size_bytes": 11509, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/selected_case_results.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/selected_case_results.csv"}, {"attachment_index": 15, "reference": "mission:evidence_environment_summary_POST-05", "sha256": "f530e5e0e1d1cdf70dace0a314e4dc27b0cc827e10ab8a8efd0b3a33b1ff9162", "size_bytes": 633, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/environment_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/environment_summary.csv"}, {"attachment_index": 16, "reference": "mission:evidence_failure_details_POST-05", "sha256": "8304a428e1e04f897c5dbea6070989875777cb182fc42173cf146811d8cc36d8", "size_bytes": 2247, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/failure_details.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/failure_details.csv"}, {"attachment_index": 17, "reference": "mission:evidence_failure_taxonomy_POST-05", "sha256": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "size_bytes": 6231, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/failure_taxonomy.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-05/evidence/failure_taxonomy.csv"}], "trace_row_ids": ["POST-05-C01", "POST-05-C02", "POST-05-C03", "POST-05-C04", "POST-05-C05", "POST-05-C06", "POST-05-C07", "POST-05-C08", "POST-05-C09"]}
-->
[[[ END INPUT 01 — job:post05_prepare_post:response ]]]

[[[ BEGIN INPUT 02 — job:post05_battle_writer_a:response | source_sha256=a997d42ab0b74ab348fd1d850bb2c20b9e66d16949f9cec2badbbb8d517178c3 | rendered_sha256=a997d42ab0b74ab348fd1d850bb2c20b9e66d16949f9cec2badbbb8d517178c3 ]]]
---
title: Length Holds, Names Break — What One Sweep of Surface and Size Actually Shows
date: 2026-10-03
layout: post
---
*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Local contrast between length-stable regex passes under one surface and length-mismatched failures under renamed surfaces in a single-seed pilot; explicit separation of source-validator events from behavioral underfit.</dd>
  <dt>Synthesis</dt>
  <dd>Heterogeneous code-task outcomes from one paid campaign archive, read against a clean-source comparator and prior multi-scenario/perturbation work, without claiming a shared depth scale or causal surface effect.</dd>
  <dt>Prose</dt>
  <dd>First-person technical narrative written from the Arena campaign evidence packet and style constraints.</dd>
  <dt>Certainty</dt>
  <dd>High on the recorded cell outcomes, failure notes, and dirty-repository flag; low on any isolated cause or general weird-machine detection claim.</dd>
  <dt>Importance</dt>
  <dd>Medium for measurement hygiene in code-agent evaluation; low as a capability ranking.</dd>
</dl>

I keep returning to five cells. Three of them look almost boring: the same model, seed 0, produces a regular-expression encoding of one Rule 110 update that preserves length on input strings of 32, 128, and 512 characters. The other two, still at length 32, collapse. One emits length 34; the other emits length 66. The judge records both as underfit. The only advertised change between the passing trio and the failing pair is the surface label—easy versus medium or hard.

That contrast is sharp enough to feel like a finding. It is also exactly the kind of pattern that evaporates once you ask what else moved with the label. This note stays inside the archive: one selected seed per cell, a dirty repository flag, and a clean-source comparator that is not proof of the paid-run workspace. The question is not whether the model “sees weird machines.” The question is what these particular cells license, and what they carefully do not.

## The track is six programs, not one depth axis

The weird-machine family in the archive contains six environments: a regex cellular-automaton step, a CSS parity selector, an SQL fixed-point chain, a spreadsheet dataflow, a CI dependency graph, and a small template interpreter. Thirty eligible selected cases; twenty-five pass under behavioral_reference judges. That fraction is a description of these implementations and this run. It is not a calibrated score of hidden-depth competence.

Each environment defines its own size parameter and its own success criteria. Regex checks output length plus a handful of fixed seeded strings. CSS checks parity behavior while the bit count moves from 3 to 4 to 5. SQL runs a fixed-point query whose chain length is varied. Spreadsheets check dataflow over class-name and grid-length contrasts. CI checks a dependency graph. The template interpreter checks a miniature language. A 512-character string, a 5-bit selector, a 25-node chain, and a larger grid are not interchangeable units of computational demand. Adding the passes therefore mixes distinct programs, distinct judges, and distinct notions of “larger.”

The same non-monotonicity appears inside single environments. Under the easy surface the CSS cases score a partial 0.416667 at 3 bits, a source-invalid zero at 4 bits (disallowed top-level import of `re`), and a clean pass at 5 bits. The surface sweep at 3 bits is fail/pass/pass. SQL passes at chain lengths 6 and 25 yet fails source validation at length 12 with an unterminated triple-quoted string. The spreadsheet, CI, and template environments pass all five of their selected cells. These are heterogeneous code-repair outcomes. They do not form a theorem, a scalar difficulty scale, or evidence that the model detected an underlying machine in any general sense.

One Rule 110 update encoded in regex does not establish Turing completeness, arbitrary iteration, or that the model internally represented a “weird machine.” The judge only ever saw length preservation and fifteen seeded strings. Passing those checks is local.

## The regex contrast is real and confounded

Hold the surface at easy and the three length cells all pass. Hold length at 32 and switch the surface to medium or hard: both fail with length mismatches (34 and 66). The failure notes are explicit morphisms collapsed on length. That is the cleanest surface-versus-size pattern the track contains.

It is also confounded by construction. In the clean-source comparator the surface levels correspond to different class names. The hard prompt additionally inserts an implementation-performance hint. A name change can alter retrieval or coding conventions even when the underlying transition rule is unchanged; an extra hint changes the instruction itself. The design therefore bundles at least two surface factors with the nominal label. There is one seed-0 run per selected cell. No factorial separation, no repeated sampling, no population of equivalent task instances. The archive supports the exact response pattern that was observed. It does not support the causal claim that class names fooled the model, that the performance note distracted it, or that input length was irrelevant.

A plausible and still-untested hypothesis is that the renamed classes or the added hard-level hint mattered more than string length for these two failures. The present sweep cannot distinguish that hypothesis from ordinary sampling variation or from their interaction. I am stating it as speculation, not as an inferred effect.

## Failure layers are not interchangeable

Across the broader eligible set the scalar PASS/FAIL label conceals different terminal events: empty patches, source-validation failures, runtime errors, malformed actions, and behavioral underfit. In the weird-machine track itself the two regex failures are underfit (length mismatch after a patch was produced). The CSS medium-depth cell is source_invalid because of a disallowed import. The SQL medium-depth cell is source_invalid because of a syntax error in a triple-quoted string. Those validator rejections occurred before any behavioral test of parity or fixed-point semantics. They are not evidence that the model failed to grasp the intended computation; they are evidence that the produced source did not clear the static gate.

I keep the layers distinct on purpose. A source-invalid or runtime failure is a different kind of miss from an underfit that reaches the judge and then mismatches length or parity. Collapsing them into a single “fail” rate erases exactly the diagnostic information the archive still contains. Provider-terminal rows sit outside the main taxonomy denominator entirely; they are recorded but not folded into the behavioral counts used here.

All thirty weird-machine cells carry the behavioral_reference judge guarantee. There are no compile-only outcomes inside this family to misread as validated behavior. The 25/30 figure is therefore a behavioral-reference pass count under the stated eligibility rules, nothing more.

## One seed, dirty tree, comparator only

Every selected cell is a single seed-0 draw. Subsequent editorial or model-role passes are not independent replications. Most contrasts are sparse one-factor substitutions around a baseline rather than full factorials or interaction tests. That design is enough to surface interesting local patterns; it is not enough to estimate cell-level variance or to claim robustness.

The campaign archive records the repository as dirty. All thirty-three selected configuration hashes match the clean comparator snapshot, yet exact identity of the task, starter, visible-test, and judge code that actually ran remains unresolved. Observations drawn from the clean source—class-name differences, the hard-level performance note, the absence of direct template references for certain advertised axes in the wider category track—are therefore comparator findings. They do not establish the precise paid-run workspaces. I treat them as such.

The same caution applies to the adjacent source-audit result that several nominal axes in the broader category track left no direct reference in the inspected templates. That is useful benchmark QA. It is not direct evidence about the regex surface manipulation, and the dirty flag still attaches.

## What the measurement tradition already knew

None of the methodological worries are new. Dynamic variable perturbation and repeated sampling already appear in VarBench; broad multi-scenario, multi-metric evaluation is the point of HELM. Other lines of work have examined epistemic-logic tasks, higher-order belief, causal templates for theory-of-mind, and the gap between plausible patches and full developer test suites. The contribution of this sweep is narrower: a concrete local pattern (length-stable passes under one regex surface, length-mismatched failures under the others) plus an explicit source-comparator audit that flags the name-plus-hint confound. Because the repository was dirty, even that audit stops short of proving exact runtime identity.

I am not claiming priority. I am claiming that the archive makes the confound visible and that the right response is to keep the claim local.

## A cleaner separation would look different

If the goal is to isolate surface from size, the next design writes the factors apart. Fix the class name and vary only the implementation hint; then vary names while holding the hint constant. Generate multiple equivalent task instances at each input size, randomize order, and draw multiple seeds. Before any model call, diff the rendered prompt, starter code, visible tests, and judge inputs across levels; block any advertised axis that changes no relevant artifact. Score exact behavioral match separately from patch validity and from source/runtime clearance. Only then does a length-invariance claim or a surface-sensitivity claim become estimable rather than anecdotal.

The present data cannot run that experiment retroactively. They can only show where the entanglement lives.

## What the evidence licenses

In one archived, single-seed sweep the model produced length-preserving regex updates for strings of 32, 128, and 512 characters under the easy surface label, and produced length-mismatched outputs (34 and 66) under the medium and hard surface labels at length 32. The surface manipulation bundled class-name changes and, at hard, an extra performance hint. Four other environments contributed additional passes and a pair of source-validation failures; two more environments passed every selected cell. The aggregate 25/30 is a heterogeneous count across six distinct programs and judges, not a shared depth metric.

These observations do not establish that the model detects computational weirdness in general, that surface deception systematically beats hidden depth, that input length is irrelevant, or that any particular factor caused the two regex failures. They do not yield a common difficulty scale, a capability ranking, or a Turing-completeness result. They do show, concretely, that surface labels, size parameters, validators, and task semantics must be disentangled before anyone treats the cells as evidence about “what the model saw.” The useful residue is the map of where those distinctions failed in this run, and the reminder that a dirty tree plus one seed per cell is a pilot, not a proof.
[[[ END INPUT 02 — job:post05_battle_writer_a:response ]]]

[[[ BEGIN INPUT 03 — job:post05_battle_writer_b:response | source_sha256=8c9b4f0e0b1a8ab4f1de51a6eb9b92f584201314f762042adf79d65ac3a1e103 | rendered_sha256=8c9b4f0e0b1a8ab4f1de51a6eb9b92f584201314f762042adf79d65ac3a1e103 ]]]
---
title: "Thirty-Four Characters Out of Thirty-Two"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Moderate. Two ideas here are new: reading the regex contrast as a map of where failures happen rather than as a result, and a design that tests the two bundled manipulations separately. The general principle of perturbing variables and controlling for them comes from earlier work.</dd>
  <dt>Synthesis</dt>
  <dd>Combines one archived paid evaluation campaign (one model, one configuration, one seed per cell), an audit of a clean source comparator for a repository recorded as dirty, and two published benchmark papers used only for context.</dd>
  <dt>Prose</dt>
  <dd>A language model drafted this in an Arena writing pass, working from a compiled evidence packet of archive tables, audit findings, and limitations. It is published under this byline. No outside authors contributed.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded case outcomes. Low for any causal reading of them. The one causal hypothesis below is labelled speculative and was not tested.</dd>
  <dt>Importance</dt>
  <dd>Modest. The post is about experimental design for one small task family, not about model capability.</dd>
</dl>

Suppose you rename a class and the model's regex stops preserving string length.

What did you learn? The obvious answer is that the model was paying attention to the name. A more careful answer is that you learned something about the name and about whatever else changed when the name changed. If you can't say what else changed, you have learned less than the obvious answer claims.

This post is about one small cluster of results that looks at first like it answers a good question: *can a model see the computation underneath an unfamiliar surface?* I want to show why it doesn't answer that yet, and why the way it falls short is still useful.

## The task family

The campaign archive has a track of six "weird machine" code tasks. Each one hides a computation inside a substrate that wasn't built for it:

- a regex that has to carry out a cellular-automaton step
- CSS selectors that compute parity
- a SQL fixed-point query
- spreadsheet dataflow
- a CI dependency graph
- a small template interpreter

Each task has two nominal axes, `surface_deceptiveness` and `hidden_depth`, each labelled easy, medium, or hard.

The design isn't a full grid. Each environment has five selected cells:

- the easy/easy baseline
- two cells that change depth while surface stays easy
- two cells that change surface while depth stays easy

That's a one-factor-at-a-time cross around a single baseline. Each cell has exactly one seed-0 run. Every one of the 30 cases is graded by a behavioral reference judge, not compile-only. All 30 were recorded and all 30 count toward the score: no exclusions and no provider-terminal rows in this track.

25 of the 30 pass. I'll come back to why that number means less than it seems.

## The cross in the regex task

The regex task asks for a single update of Rule 110, written as regular-expression machinery. "Hidden depth" here means only the length of the input string: 32, 128, or 512 characters.

Here are the five cells:

| surface | input length | verdict | score | judge note |
|---|---|---|---|---|
| easy | 32 | PASS | 1.0 | — |
| easy | 128 | PASS | 1.0 | — |
| easy | 512 | PASS | 1.0 | — |
| medium | 32 | FAIL | 0.208333 | length mismatch, in=32, out=34 |
| hard | 32 | FAIL | 0.208333 | length mismatch, in=32, out=66 |

Laid out like that, it looks like a clean story. Under the easy label, the model's solution holds up as the input grows sixteenfold. At the smallest input, changing the surface label breaks it. Surface beats depth.

I believed that for about one paragraph of the first draft. Then I looked at what the surface label actually controls.

## Two changes made at once

In the clean source comparator, the surface levels map to different class names. The hard level also adds an implementation-performance hint to the prompt.

So moving from easy to hard surface changes two things together:

1. **A name.** A class name changes nothing about the computation, but it can change which conventions and memorised patterns the model reaches for.
2. **The instruction.** The extra hint is new content. It asks for something, or at least suggests something, that the easy prompt doesn't.

The medium cell changes only the name (as far as the comparator shows). The hard cell changes the name and adds the hint. Both fail. Because each cell has one run, I can't separate the following:

- the name mattered
- the hint mattered
- both mattered, or they interacted
- seed 0 happened to land badly on two of five draws

There's another caveat. The comparator is *clean*, while the paid campaign recorded its repository as dirty. All 33 selected config hashes match the clean snapshot. But matching configs isn't byte-level proof that the prompts, visible tests, or judge code the model actually saw were the same. So even "the hard prompt contained a performance hint" is an observation about the comparator, not a certainty about the paid run.

Here is the hypothesis I'd bet on, and I'm labelling it plainly as speculation. **In this particular regex task and this particular run, the changed names or the added hint probably mattered more than input length.** The archive can't separate that from sampling noise. Nothing in it estimates an effect.

## What the numbers 34 and 66 tell us

The judge's notes give a little more than a verdict, and they're tempting to over-read.

On a 32-character input, the medium-surface output was 34 characters: the input plus two. The hard-surface output was 66 characters: a bit more than double. A Rule 110 update should map a string to a string of the same length. Both failures broke that invariant, and the judge stopped at the mismatch. Its note says it "collapsed on length mismatch".

My first instinct was to diagnose. +2 looks like a boundary-padding slip that never got trimmed. ~2× looks like something duplicating or interleaving the string. Those are plausible stories. But the archive records only the lengths, and I'd be making up a mechanism from two integers. What I can say is narrower: both failures are behavioral misses of the same kind. The code ran and produced output, and that output violated a structural property the task requires. They weren't crashes or validator rejections.

That distinction matters, because the passes need a caveat too. The regex judge checks four specific criteria, including 15 seeded strings and length preservation. Passing those checks shows the expression behaved correctly on those checks. It doesn't prove the regex is correct in general.

It also says nothing about the more romantic claim nearby. Rule 110 is famously Turing complete when iterated. This task asks for *one update*. A model that writes a correct single step hasn't shown that it represented a universal machine, that the expression can iterate arbitrarily, or anything at all about Turing completeness. The weird-machine framing is a reason to build the task. It isn't something the task measures.

## Five failures, three layers

Now widen the view. The track has five failures across 30 cases, and they don't all happen at the same stage:

| environment | condition | score | where it stopped |
|---|---|---|---|
| regex | surface=medium, depth=easy | 0.208333 | behavioral: length mismatch (32→34) |
| regex | surface=hard, depth=easy | 0.208333 | behavioral: length mismatch (32→66) |
| CSS | surface=easy, depth=easy | 0.416667 | behavioral: partial credit, labelled underfit |
| CSS | surface=easy, depth=medium | 0.0 | source validator: disallowed `import re` |
| SQL | surface=easy, depth=medium | 0.0 | source validator: unterminated triple-quoted string |

Three are behavioral misses: the program ran and got things wrong. Two never reached a behavioral test. The CSS medium-depth patch imported a module that isn't on the allowlist. The SQL medium-depth patch had a syntax error. Both validators reject before any semantics are checked. The validator's own note says it is not a security sandbox. Whatever it is, it's a gate, and these two cases stopped at the gate.

That changes how the "depth" rows read. CSS uses a parity-selector implementation, and depth there means bit count:

| CSS, surface=easy | 3 bits | 4 bits | 5 bits |
|---|---|---|---|
| outcome | FAIL 0.416667 (behavioral) | FAIL 0.0 (source-invalid) | PASS |

SQL's depth is the length of a graph chain:

| SQL, surface=easy | chain 6 | chain 12 | chain 25 |
|---|---|---|---|
| outcome | PASS | FAIL 0.0 (source-invalid) | PASS |

Both rows are non-monotone as archived outcomes. In SQL the middle value fails and the largest passes. In CSS the smallest has the only behavioral failure and the largest passes. But in both, the failure in the middle row is a validator rejection. That's not evidence the model couldn't handle 4 bits or a 12-node chain. It's evidence that on that draw the model wrote a patch that didn't get through the gate. Whether a validator failure is "really" a reasoning failure is a fair question, but the archive can't answer it. Folding these into a depth curve would bury the question.

The CSS surface sweep at 3 bits runs fail, pass, pass for easy, medium, hard. That's the opposite direction from regex. I'm not going to make a pattern out of that either. One run per cell, different task, different judge.

The other three environments are uneventful in this run. Spreadsheet dataflow, the CI dependency graph, and the template interpreter each pass all five selected cells.

For scale: across the whole campaign, the taxonomy has 61 failures among 192 eligible cases, and two provider-coded final rows fall outside that denominator. The labels there hide similar mixtures. Empty patches, source rejections, runtime errors, and malformed actions all show up as FAIL. Two cases labelled "overfit to visible tests" actually have full trusted scores and missing-companion-file notes. The weird-machine track is cleaner than that because everything in it is behaviorally judged and nothing is excluded. But a clean track can still mix failures from different layers.

## Why 25/30 isn't a number about anything in particular

Per environment, the track breaks down as follows:

| environment | eligible | pass |
|---|---|---|
| CI dependency graph | 5 | 5 |
| spreadsheet dataflow | 5 | 5 |
| template interpreter | 5 | 5 |
| SQL fixed point | 5 | 4 |
| CSS state machine | 5 | 3 |
| regex state machine | 5 | 3 |

The pooled 25/30 is accurate bookkeeping. It's a poor *measurement*, because the rows have nothing in common except the axis labels:

- They are different programs.
- Each has its own judge: length preservation and seeded strings for regex, parity behavior for CSS, a fixed-point computation for SQL, dataflow for spreadsheets, a dependency graph for CI, a small language for the template interpreter.
- "Hidden depth" means a 512-character string in one, a 5-bit selector in another, a 25-node chain in a third, and a larger grid in a fourth.

Nothing says those are equally hard, or even hard along the same dimension.

So easy/medium/hard aren't points on a common difficulty scale. They're ordinal labels inside each environment, and a few cells show the labels don't even order outcomes reliably there. Averaging over them gives a number with units of "whatever these six tasks happen to be". It's not a weird-machine capability score, and with one model and one configuration it's certainly not a ranking.

The underlying move isn't new. HELM's case for [broad scenario coverage and multiple metrics](https://arxiv.org/abs/2211.09110) (42 scenarios) is largely an argument against reading a single pooled score this way. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) already does dynamic variable perturbation, with repeated sampling (five seeds) for its variable-based experiments. I'm citing these as context for the design, not as validation of this campaign. This post doesn't do anything those papers haven't, beyond looking closely at one archive.

## What the source audit adds, and what it doesn't

The useful contribution here is small and specific. Comparing the archived outcomes with the source comparator found the name-plus-hint bundling in the regex surface axis. Without the comparator, "surface deceptiveness" would look like one intervention. With it, we can see it's at least two.

A related audit covered the separate category track, a set of heterogeneous code-repair tasks. A static scan of the clean comparator found ten advertised control or variable axes, across nine category environments, that the environment templates never directly reference. Where that holds, the nominal axis count overstates the number of distinct interventions: a cell labelled "hard" may differ from "easy" only in its label. That finding isn't about the regex task, and it doesn't make the category-track outcomes a theorem or a score. They're still a collection of code-repair results. I mention it because it's the same kind of problem as the regex finding: the label promises a manipulation, and the artifacts may not deliver that manipulation cleanly.

Both audit findings carry the dirty-repository caveat. They describe what the clean source does. They show only by inference what the paid runs saw.

## The experiment I'd fuckingly want

If the question is "does the surface or the depth decide the outcome?", the design has to give each its own handle:

1. **Split the bundled surface manipulation.** Hold the class name fixed and toggle only the performance hint. Then hold the hint fixed (present or absent) and vary only the name. That's a 2×2 on the surface side, not three ordered levels.
2. **Replicate cells.** Generate several equivalent task instances at each input size, randomise their order, and run multiple seeds per cell. With five draws per cell, a 0-for-5 means something that a 0-for-1 can't.
3. **Diff the rendered artifacts before any model sees them.** For every pair of levels, compare the rendered prompt, starter code, visible tests, and judge inputs. If an advertised axis changes no relevant artifact, block it from the sweep. If it changes more than one, record each change as its own factor.
4. **Score layers separately.** Report patch created, source valid, runs without error, and behaviorally correct as distinct outcomes. A validator rejection at 4 bits and a wrong parity answer at 3 bits shouldn't share a column.
5. **Make the regex judge report more than lengths.** Even when length preservation fails, a per-position comparison on the seeded strings would let "+2 characters" become a diagnosis instead of a guess.

Even with all that, the result would be about these task implementations under this judge, not about an abstract ability to detect computational weirdness.

## What this licenses

The archive supports one narrow claim:

> In one archived sweep, with one seed per cell, this model passed the regex Rule 110 task at all three input lengths under the easy surface label and failed both altered-surface variants at the shortest length, where the altered variants change class names and, at the hard level, add an implementation hint.

It also supports a few small descriptive facts:

- Three of the track's five failures are behavioral misses and two are source-validator rejections.
- Three environments passed everything they were given.
- The depth axes measure different quantities in different environments.

It doesn't license:

- a causal claim that names fooled the model
- a claim that depth didn't matter
- a law that surface beats depth
- a calibrated difficulty scale
- a capability ranking
- any statement about Turing completeness

The most interesting thing in the archive is still the pair of integers 34 and 66. I'd just rather find out what produced them than write as if I already know.
[[[ END INPUT 03 — job:post05_battle_writer_b:response ]]]

[[[ BEGIN INPUT 04 — job:post05_editorial_critic:response | source_sha256=5bed91f0fade9e61ba8b3e3f033fc121085436d785419751c5f74cef0ccb4d75 | rendered_sha256=5bed91f0fade9e61ba8b3e3f033fc121085436d785419751c5f74cef0ccb4d75 ]]]
# POST-05 editorial critic response bundle

Compiler-assembled wrapper containing two separately labeled user-supplied critiques. The bodies are preserved verbatim; labels match the supplied text and are not independently verified. This bundle does not synthesize, rank, or select a critic.

## Critic response 1 — sonnet 4.6

# Editorial Blueprint — POST-05
## "Surface cues, hidden depth, and what the weird-machine sweep can't prove"

---

## 1. Conceptual Structure and Thesis

**What the real argument is.** The post has four load-bearing claims, all of which are supported by the packet, none of which require synthesis beyond the archive:

1. The regex surface contrast (easy surface → all three lengths pass; altered surface at shortest length → two length mismatches) is the sharpest local pattern in the track, and it is confounded by construction: the surface manipulation bundles a class-name change with, at the hard level, an added performance hint.
2. The five failures across 30 cells are not the same kind of failure. Two are source-validator rejections that never reached a behavioral test. Three are behavioral underfits. Collapsing them obscures exactly the diagnostic information the archive retains.
3. The 25/30 aggregate pools six distinct programs, six distinct judges, and six incommensurable "depth" parameters. It is accurate bookkeeping, not a calibrated score of hidden-depth competence.
4. One seed per cell, a dirty repository, and a comparator-only source audit mean the archive supports the observed response pattern; it does not support any causal attribution.

**Proposed thesis sentence (for the writer to recast in voice):** *One archived sweep shows a sharp regex contrast that looks like surface deception—and it is exactly confounded enough that you cannot tell whether it is.*

**What to move or cut:**

- Both drafts have a standalone prior-work section. Shrink to two inline sentences at the first citation of VarBench or HELM; the packet (F-17) explicitly limits novelty claims to LOW confidence, so no section heading should suggest the comparison is thorough.
- Writer A's dedicated "One seed, dirty tree, comparator only" section should dissolve into caveat placement beside the claims it qualifies (§§ on the regex contrast and the source audit), not stand alone as a methodological recitation.
- Writer B's "What 34 and 66 tell us" section contains mechanical speculation (+2 as boundary-padding, ~2× as duplication) that the author half-retracts. The retraction is correct; the speculation should be compressed to one sentence acknowledging the temptation and then giving the retraction. The archive records only the two lengths; the post should not tour candidate failure mechanisms the evidence cannot distinguish.
- The axis-placeholder finding (F-14, category-track scan) is adjacent benchmark QA, not direct evidence about the regex manipulation. Keep it to one sentence with the dirty-source caveat, placed in or near the source-audit section.

**Where the two structures diverge.** Writer A orders: track overview → regex → failure layers → design limits → prior work → better design → license statement. Writer B orders: hook → task family → regex table → two bundled changes → 34/66 → failure layers with tables → 25/30 critique → source audit → better design → license statement. Writer B's ordering better earns each move—the hook motivates the task family, which motivates the table, which motivates the confound analysis. Writer A's track-overview-first approach asks the reader to absorb the six-environment landscape before the payoff cell is shown. However, Writer B's 34/66 section is an unnecessary detour between the confound analysis and the failure-layer taxonomy. The recommended section order is: hook and specific contrast → what the surface label controls (confound) → failure-layer heterogeneity → 25/30 is not a unit → source audit and caveat → what a better experiment isolates → license statement.

---

## 2. Opening

**Writer A's opening.** "I keep returning to five cells." Specificity is high within two sentences (seed 0, Rule 110, 32/128/512, collapse). Tension arrives immediately. The limiting claim ("the question is not whether the model sees weird machines") appears in the second paragraph. Weakness: the reader does not yet know why Rule 110 in regex is interesting as a task design choice; the setup treats the strangeness as given.

**Writer B's opening.** "Suppose you rename a class and the model's regex stops preserving string length. What did you learn?" Tension is immediate and epistemological. Specificity is lower (no numbers yet). The limiting claim arrives more slowly (paragraph 3). Strength: frames the core problem as an interpretive one before showing any data, which is more intellectually honest about the order in which the question arises.

**Problems with both.** Writer A front-runs numbers before motivating why those numbers are puzzling. Writer B's "suppose" frame slightly generic compared to the site's existing openings, which tend to open with a pointed observation or a committed claim that is then complicated.

**Fresh opening strategy.** Open with the two integers as a puzzle and a refusal: the archive gives you the output lengths (34 and 66), the input length (32), and the judge note ("collapsed on length mismatch"), and those are nearly all the forensics you have. Do not start with the sweep or the track or the 25/30 count. Do not open with an abstract definition of weird machines. The post's governing question—*how much argument can two integers bear?*—should be live from the first sentence. The opening should then concede, in the same paragraph, that the answer is "less than they appear to," and that this is itself the finding worth stating carefully. This is consistent with the site's pattern of opening with a committed claim that the body then earns rather than reverses.

Do not copy either draft's prose. Do not open with "I keep returning to" or with "Suppose."

---

## 3. Examples and Technical Depth

**Regex five-cell table.** Writer B's table (surface, input length, verdict, score, judge note) is the most useful single element in either draft. Retain it. The exact judge notes—"length mismatch, in=32, out=34" and "in=32, out=66"—are verbatim archive records and should appear verbatim. The table earns its space because the argument depends on the reader seeing all five cells together.

**Failure-detail table.** Writer B's five-failure table (environment, condition, score, where it stopped) is useful for the failure-layer section. It can be slightly compressed: environment and failure layer are the essential columns; exact scores can move to inline prose. Keep it if it stays under five rows; it does here.

**CSS and SQL depth tables.** These two tables (CSS: 3/4/5 bits; SQL: 6/12/25 chain) are borderline. The non-monotone argument is clear in prose with the numbers inline. Recommended: convert to two short inline sentences with the scores embedded. "Under the easy surface, CSS scores partial, source-invalid, pass across 3, 4, and 5 bits—the middle row rejected for a disallowed import before any parity test." Tables are warranted when the reader needs to scan; here the argument is short enough that scanning a table adds friction.

**Environment summary table.** Writer B's per-environment pass-rate table (6 rows) is accurate bookkeeping but does not advance the argument more than a sentence would. Convert to prose: "Three environments—spreadsheet, CI graph, and template interpreter—pass every selected cell. SQL passes four of five, CSS and regex each pass three." This is cleaner for the site's airy-paragraph aesthetic.

**Mathematics.** No equations are warranted. Rule 110 does not need a transition-function formula; the post's argument is about output length, not about the automaton's state semantics. Do not include a Rule 110 truth table or state diagram—these would be decorative, and the packet does not use them.

**Task specification precision.** Both drafts correctly note that the regex judge checks four criteria including 15 seeded strings and length preservation. This should appear once, precisely, when the pass/fail verdicts are first cited, to bound what "pass" means. It is a genuine evidential boundary, not padding.

---

## 4. Generic AI Prose and Benchmark-Report Tone

**Remove from Writer B immediately:**

- Every instance of "fuckingly"—these are generation artifacts throughout Writer B and must all be excised before any editorial work proceeds.
- "I believed that for about one paragraph of the first draft"—author-process self-reference, prohibited by the blueprint constraint.
- "The underlying move isn't new" as a section-opening sentence—this is empty setup. Fold the prior-work context into a single sentence at the inline citation.

**Stock transitions and empty emphasis to cut or rework in both drafts:**

- "That contrast is sharp enough to feel like a finding" (Writer A)—the hedging works but "sharp enough to feel like" is slightly evasive. The contrast is a finding; the question is what kind. Say so.
- "These are heterogeneous code-repair outcomes. They do not form a theorem, a scalar difficulty scale, or evidence..." (Writer A)—correct but the triple negative list reads as a benchmark-report boilerplate disavowal. One direct sentence works better than three parallel negations.
- "None of the methodological worries are new" (Writer A)—correct per F-17 but the phrasing slightly dismisses the context-setting role of VarBench and HELM. The reference is useful; the framing should be "these design principles are established" not "I am not claiming novelty."
- "useful residue" (Writer A)—slightly precious; replace with a direct statement of what the archive supports.
- "Uneventful in this run" (Writer B, spreadsheet/CI/template)—colloquial and fine for voice, but make sure it is not the only characterization of three 5/5 environments; the all-pass result also belongs in the 25/30 critique section.

**Benchmark-report overload in both drafts:**

- Both drafts end with a bulleted license-statement structure ("does not establish… does not license…"). This is useful content but should arrive as prose paragraphs in the site voice, not as a formatted list. The site's reference posts end with argued conclusions, not tabulated disclaimers.

---

## 5. Transitions and Caveat Placement

**Dirty-source caveat (F-01):** Should appear twice: once when the source-comparator observations are introduced (the class-name / performance-hint finding), and once in the source-audit section. Do not give it a standalone section (Writer A's approach). Do not pepper it throughout every paragraph (Writer B's approach). The rule: place it exactly where a claim depends on it.

**One-seed caveat (F-06, F-10):** State once in the framing paragraph where the regex contrast is introduced. Reference it again—briefly—when the causal hypothesis is labeled speculative. Do not repeat it in every section.

**Comparator/dirty boundary:** Any observation drawn from the clean source (class-name differences, the performance hint, the axis-placeholder scan) must be introduced as "in the clean-source comparator" and must carry the dirty-repository qualifier at first use. Subsequent mentions in the same section do not need to repeat the qualifier.

**CSS source-invalid caveat:** Place it immediately when the CSS case is cited. "The middle cell fails source validation—a disallowed import of `re`—before any parity behavior is tested" must appear at the sentence where the CSS medium-depth zero score appears, not in a subsequent paragraph.

**SQL source-invalid caveat:** Same rule. The unterminated triple-quoted string error is a gate failure, not a behavioral failure. This must be stated at the first mention of the SQL zero score.

**Judge-mode caveat (behavioral_reference guarantee):** State once when 25/30 is first cited: "all 30 cases are graded by behavioral-reference judges; none are compile-only verdicts." This is a boundary condition on the aggregate count, not a general caveat.

**Provider/exclusion boundary:** From F-09, two provider-coded rows sit outside the broader campaign taxonomy denominator. This is relevant to the 192-case campaign-wide context (Writer B introduces it briefly) but is not relevant to the weird-machine track specifically, where all 30 cases are eligible and no provider-terminal rows appear. Do not introduce this in the weird-machine sections; if context requires citing the broader campaign failure taxonomy, one sentence with the denominator note is sufficient.

**Speculative hypothesis (F-18):** The hypothesis that class-name changes or the added hard-level hint mattered more than input length must be labeled speculative at the point of statement, not in a subsequent paragraph. Writer B does this correctly ("labelling it plainly as speculation"). Writer A does it correctly ("I am stating it as speculation, not as an inferred effect"). Either phrasing works; pick one and do not repeat the label.

---

## 6. Unsupported Claims and Claim Traceability

**Statements to remove or narrow:**

| Statement | Location | Problem | Action |
|---|---|---|---|
| "+2 looks like a boundary-padding slip" and "~2× looks like something duplicating or interleaving the string" | Writer B, "What 34 and 66 tell us" | The archive records only output lengths; no mechanism is in evidence. The author retracts these but the text still tours the speculation. | Cut the candidate mechanisms; keep only: "Both failures are behavioral misses of the same kind—the patch ran and violated a structural property the task requires." |
| "I believed that for about one paragraph of the first draft" | Writer B | Author-process claim, prohibited. | Remove. |
| "The measurement principle is not novel" / "None of the methodological worries are new" | Writer A | F-17 is explicitly LOW confidence for any exhaustive novelty conclusion. "Not novel" as a global claim overstates the prior-work check. | Replace with: "Dynamic variable perturbation and repeated sampling appear in VarBench; broad multi-scenario evaluation is HELM's central design rationale." Cite inline. Do not generalize to "all methodological worries." |
| "the absence of direct template references for certain advertised axes in the wider category track" | Both drafts (source audit section) | Supported by F-14 but must carry dirty-source qualifier and must be scoped to "the category track, not the weird-machine track." | Keep with both qualifiers. |
| Any claim that Rule 110 Turing-completeness is relevant to what the model did | Both drafts correctly avoid it; source draft mentions it only to negate it | Limitation 1 in the packet is explicit: one update step does not establish arbitrary iteration. | Retain the negation as stated. One sentence is sufficient. |
| "Several nominal controls with no direct template references in the clean comparator" (paraphrase of F-14) | Writer A | F-14's finding covers ten axes across nine category environments; specifying "several" is an undercount that may be read as softer than the evidence. | Use the packet's number: ten axes across nine environments, or cite the finding without a count if the count feels out of place. Do not say "several" when the evidence has a figure. |
| "The contribution here is narrower" (source draft) / "The useful contribution here is small and specific" (Writer B) | Both | Self-evaluation of novelty. F-17 supports this as a characterization but the phrasing risks the benchmark-report register. | Reframe as what the post shows, not what it contributes. |

**Boundaries the packet does not permit crossing:**

- Do not assert that any axis change caused any specific outcome. The archive supports the observed response pattern only.
- Do not assert that the dirty-repository flag invalidates the comparator observations; it qualifies them. The distinction matters.
- Do not assert that the CSS or SQL source-invalid failures are evidence of semantic inability. They are gate failures.
- Do not assert that the axis-placeholder finding (F-14) applies to the weird-machine track; the packet scopes it to the category track.

---

## 7. Public-Site Fit

**Jekyll frontmatter.**
Both drafts have correct `title`, `date: 2026-10-03`, and `layout: post`. No math is used in either draft, so `{% include mathjax.html %}` is correctly absent. Final writer: confirm no equation is introduced (none is warranted per §3), then omit the include. If a display formula is ever added, the include must appear immediately after the frontmatter block, before the byline.

**Byline.**
Both drafts use the exact required form: `*by <span class="icon-self">StrangeTcy</span>*`. Retain exactly.

**Epistemic-status block.**
Writer A's block is clean and accurate. Writer B's block is accurate on the five fields but the Prose field reads "A language model drafted this in an Arena writing pass, working from a compiled evidence packet"—this is an author-process statement with internal-process language ("Arena writing pass," "compiled evidence packet"). The house style says to "attribute the actual Arena writing process accurately; do not invent outside authors." The Prose field should describe how the post was made without reproducing internal workflow terminology. Model Writer A's Prose field instead: "First-person technical narrative written from the campaign evidence packet and style constraints." The order of the five fields (Original ideas → Synthesis → Prose → Certainty → Importance) is correct in both drafts.

**Voice check against reference excerpts.**
The reference posts open with a committed observation or a short pointed claim that creates immediate interpretive pressure. "Suppose you rename a class" (Writer B) is closer to the question-led "Suppose I want you to make the wrong decision" pattern of reference post 3, but is less committed. Writer A's "I keep returning to five cells" is concrete and specific in the site's manner. The blueprint's proposed opening (§2 above—open with the two integers as a puzzle and a refusal) fits the site's visible self-correction pattern ("The first formalisation was wrong") more tightly, because it admits the temptation to over-read before the body earns the more careful conclusion.

The ending of reference post 4 ("Lying With Truth") demonstrates that the site voice can sustain a tight conclusion that restates what the evidence *does* license in a single sharp sentence. Writer B's closing—"I'd just rather find out what produced them than write as if I already know"—fits the site voice well and earns its place. Writer A's closing—"a dirty tree plus one seed per cell is a pilot, not a proof"—is also strong. Either can anchor the final paragraph; the blueprint recommends ending on the evidential limit, not on the desire for better data.

**Link and Markdown details.**
Writer B links VarBench and HELM inline at first mention, which is correct site practice. Writer A names them without links; add links. The VarBench URL is `https://aclanthology.org/2024.findings-emnlp.946/` and the HELM URL is `https://arxiv.org/abs/2211.09110` per the references packet. Do not link these a second time.

Table use: see §3. Maximum two tables in the final article. The five-cell regex table is justified; a compact failure-layer table is optional. Environment summary and CSS/SQL depth comparisons should be prose.

**Word count.** Writer A runs approximately 1,650 words (short of the 1,800 floor). Writer B runs approximately 2,400 words (within range but dense). The recommended structure with one retained table and compressed prior-work section should land between 1,900 and 2,300 words without padding.

---

## Actionable Section-by-Section Sequence

**§1 — Opening (no heading).** Open with the two specific integers and the judge's length notes as a concrete puzzle. State immediately that the archive gives you those numbers, one seed, and a comparator; establish the interpretive constraint before showing the task family. Roughly 150 words.

**§2 — "The track is six programs, not one axis."** Introduce the six environments with their distinct judges and depth parameters. State 25/30 once, with the behavioral-reference qualifier, and immediately note it pools incommensurable units. Introduce the three all-pass environments in one sentence. Roughly 200 words.

**§3 — "The regex contrast."** Present the five-cell table. State the pattern directly (easy surface: all lengths pass; altered surface at shortest length: both fail with length mismatches). Cite the verbatim judge notes. Do not interpret yet. Roughly 150 words.

**§4 — "What the surface label controls."** Introduce the confound: class-name change plus, at hard, an added performance hint. State the speculative hypothesis (names or hint may have mattered more than length) with explicit speculation label. State one-seed limit. Place comparator/dirty qualifier here. Roughly 200 words.

**§5 — "Failure layers are not interchangeable."** Compact failure-layer table or tightly described prose covering the five failures: two regex underfits (behavioral, length mismatch), one CSS partial-credit underfit (behavioral), one CSS source-invalid (disallowed import, pre-behavioral), one SQL source-invalid (syntax error, pre-behavioral). State explicitly that source-invalid failures are not evidence of semantic inability. Roughly 200 words.

**§6 — "25/30 is accurate bookkeeping."** Argue why the aggregate is not a capability score: different programs, different judges, incommensurable depth parameters. Cite HELM and VarBench inline here (one sentence each). Note that easy/medium/hard are not a common calibrated scale. Roughly 200 words.

**§7 — "The source audit adds one specific thing."** State the name-plus-hint bundling finding from the comparator. Note the axis-placeholder finding for the category track in one sentence with the dirty-source qualifier. Be explicit that the audit shows what the comparator contains, not what the paid run executed. Roughly 150 words.

**§8 — "A separation would look different."** State the four-step design required to isolate surface from size: split the bundled manipulation; replicate cells with multiple seeds; diff rendered artifacts before model sees them; score patch creation, source validity, and behavioral correctness as distinct outcomes. Do not make this section a numbered list if the site voice is flowing better in prose by this point. Roughly 200 words.

**§9 — "What the evidence licenses" (no formatted list).** Restate the local claim in one or two sentences. Name what the archive does not support (causal attribution, general capability score, Turing-completeness inference, difficulty ranking). End on the evidential limit in site voice. Roughly 150 words.

---

## Elements Worth Retaining from Each Draft

**From Writer A:**
- The epistemic-status block (clean, accurate, correct field order). Adapt Prose field per §7 note.
- The failure-layer analysis logic: "a source-invalid or runtime failure is a different kind of miss from an underfit that reaches the judge." The concept is from the packet; Writer A's prose articulation is precise.
- The better-design paragraph's four-factor separation (fix name/vary hint; vary name/fix hint; multiple seeds; diff artifacts). This is more structured than Writer B's version.
- "A dirty tree plus one seed per cell is a pilot, not a proof" as a possible closing line.

**From Writer B:**
- The five-cell regex table (exact scores, judge notes, format). It is the clearest single element in either draft.
- The title "Thirty-Four Characters Out of Thirty-Two." It commits to the specific evidence and cues the post's epistemological constraint.
- The argumentative section heading "Why 25/30 isn't a number about anything in particular"—or its spirit. Strong.
- The observation that the CSS and SQL non-monotone rows have their middle failures at the gate, not at behavioral test—and that plotting these on a "depth curve" would bury the distinction. This is sharp and source-grounded.
- "I'd just rather find out what produced them than write as if I already know" as a candidate closing beat.
- The inline failure-detail table (five rows), compressed to the essential columns.

---

## Elements Neither Draft Handles Well

1. **The CSS surface sweep.** The axis table shows that at depth=easy, the CSS surface sweep is fail/pass/pass (easy/medium/hard). This is the opposite directional pattern from regex. Both drafts mention it; neither makes it analytically useful. The blueprint recommendation is to cite it once as evidence that surface-level patterns are not consistent across environments, then leave it. Do not speculate about a mechanism.

2. **The "behavioral_reference guarantee" as an actual constraint.** Both drafts mention it but neither explains what it means for what we can say: the guarantee means all 30 cells were run against a behavioral judge, not that the judge is correct or complete. One sentence explaining the judge's specific criteria (length preservation + 15 seeded strings for regex) would bound the pass more precisely.

3. **The transition from the description of failure modes to the implication for the 25/30 count.** Both drafts treat "failure layers" and "25/30 is not a unit" as adjacent but separate sections. The more natural structure is: the failure-layer heterogeneity is *one of the reasons* the aggregate is hard to interpret—not an independent observation. The section flow should make this connection explicit.

---

## Evidence Boundaries

The final writer must not:
- Cite a mechanism for the 34/66 outputs (none is in the archive).
- Assert exact paid-run source identity (dirty flag, comparator-only).
- Claim novelty beyond the local pattern and comparator audit (F-17: LOW).
- Assign a cause to any specific failure (F-06, F-18: LOW or SPECULATIVE).
- Extend the axis-placeholder finding to the weird-machine track (F-14 scopes it to category tasks).
- Suggest Rule 110 Turing-completeness is relevant to what the task measures (Limitation 1).
- Present source-invalid failures as behavioral evidence (F-09, Limitation 6).

The final writer may:
- State 25/30 with the behavioral-reference qualifier (F-10: HIGH confidence for observed outcomes).
- State the regex 3/5 pattern with exact scores and judge notes (F-10, F-06: HIGH confidence).
- State the confound (class-name + performance hint bundled) with the comparator qualifier (F-18, F-03: supported with dirty-source caveat).
- State the speculative hypothesis as speculation (F-18: SPECULATIVE, explicitly labeled).
- State that CSS and SQL source-invalid failures are gate failures, not behavioral evidence (F-09: HIGH for terminal labels).
- State the dirty-repository flag and its implication for source identity (F-01: HIGH).

---

## Final Quality Checklist

Before the article is published, confirm:

- [ ] No instance of "fuckingly" (Writer B artifact, all must be removed).
- [ ] No author-process language in the epistemic-status Prose field.
- [ ] Dirty-source caveat appears at each comparator observation, not as a standalone section.
- [ ] One-seed caveat placed beside the regex contrast and the causal hypothesis only.
- [ ] CSS and SQL source-invalid failures described as gate failures, not semantic failures, at point of first citation.
- [ ] 25/30 cited with behavioral-reference qualifier and incommensurability note in same paragraph.
- [ ] Speculative hypothesis explicitly labeled speculative at point of statement.
- [ ] No mechanical diagnosis of the 34/66 outputs.
- [ ] No general novelty claim; prior-work references inline with correct URLs.
- [ ] No Rule 110 Turing-completeness inference.
- [ ] No axis-placeholder finding (F-14) attributed to the weird-machine track.
- [ ] Tables reduced to two maximum (five-cell regex table required; failure-layer table optional).
- [ ] No `{% include mathjax.html %}` unless a display formula is introduced (none should be).
- [ ] Byline exact: `*by <span class="icon-self">StrangeTcy</span>*`.
- [ ] Epistemic-status fields in order: Original ideas, Synthesis, Prose, Certainty, Importance.
- [ ] Word count 1,800–2,300 without padding.
- [ ] Closing paragraph ends on the evidential limit, in site voice, not as a bulleted disclaimer list.
- [ ] VarBench and HELM linked inline at first mention only.

## Critic response 2 — opus 4.7

# Editorial blueprint — POST-05

## 1. Conceptual structure and thesis

**The real argument** (which both drafts gesture at but neither fully centers): A one-seed sweep produced a visually sharp contrast — length invariance under one surface label, length-mismatched failures under two others at the shortest length — but the manipulation bundles at least two factors (class name + hard-level hint), the five failures occur at *different stages of the pipeline* (behavioral vs. source-validator), and the aggregate 25/30 is a bookkeeping total over six incomparable programs. The piece is about why that archive *cannot* answer the question it looks like it answers, and what a design that could would need.

**Structural divergence:**
- **A** moves linearly from aggregate (25/30) → regex contrast → failure layers → design caveats → prior work → cleaner experiment → what the evidence licenses. It is tight but withholds the regex table and never shows the reader the 34/66 numbers in their visual context until near the end.
- **B** opens question-first, uses two tables early (regex 5-cell grid; failure stratification), and does the layer-separation argument *before* the aggregate critique. This ordering is stronger: the reader sees the shape of the data before being told what to make of it.

**Recommended shape for the final piece:**
1. Open on the two integers (34, 66) or on the renamed-class puzzle — concrete, not aggregate.
2. Lay out the task family and the 5-cell-per-environment design so the reader knows what "25/30" is made of.
3. Show the regex table and admit the confound in the *same* section.
4. Separate behavioral miss from source-invalid before pooling anything.
5. Explain why 25/30 is bookkeeping, not measurement.
6. State the comparator-vs-dirty-tree boundary explicitly, once, where it bites.
7. Describe the cleaner experiment.
8. Close with a precise license statement.

**Cut from source draft / A:**
- The "weird-machine benchmark asks whether a model can infer…" opener (abstract definition before specifics).
- The paragraph that reintroduces the regex contrast *after* the aggregate — avoid two passes at the same material.
- A's "What the measurement tradition already knew" is slightly defensive; fold the HELM/VarBench reference into the aggregate-critique section as context, not a standalone turn.

**Move:**
- Failure-layer separation (currently buried in A, well-placed in B) should sit immediately after the regex table so the reader learns early that FAIL ≠ FAIL.

## 2. Opening

**Comparison:**
- Source draft opens with abstract definition. Low tension, high setup cost.
- **A** opens on "I keep returning to five cells" — specific, first-person, states the puzzle in two sentences. Good tension, limit stated by paragraph two.
- **B** opens with a conditional: "Suppose you rename a class and the model's regex stops preserving string length." This is the style-reference register (question-led, cf. "Suppose I want you to make the wrong decision"). Fastest to tension and to limit.

**Fresh opening strategy (do not copy either):** Open on the asymmetry a reader can hold in their head *before* any framing — a concrete scene of three passing lengths and two failing renamed cells, stated as what-happened, followed immediately by the limit: single seed, dirty repo, comparator-only. The opener should name what the post refuses to claim (a general weird-machine detector, a surface-beats-depth law) before it discusses what it does claim. Do not define "weird machine" in the opener; let the examples do the definitional work.

## 3. Examples and technical depth

**Keep (exact, source-grounded, useful):**
- Regex table (B's five-row table). This is the central exhibit; it must appear.
- Explicit numbers: 32/128/512 input lengths; outputs 34 and 66 at input 32; CSS 0.416667 / 0 / 1.0 at 3/4/5 bits; SQL passes at chain 6 and 25, source-invalid at 12; CSS validator rejected `import re`; SQL unterminated triple-quoted string.
- Per-environment pass counts (B's second summary table: CI 5/5, spreadsheet 5/5, template 5/5, SQL 4/5, CSS 3/5, regex 3/5).
- Failure stratification table (B's "three layers" table). Useful because it visually enforces the behavioral/source-invalid distinction.

**Cut / avoid:**
- Equations: none needed. Rule 110 is referenced, not derived. Do **not** introduce an equation; it would be decorative here. (The style reference uses math only when the formalism itself is the subject.)
- Diagrams: not needed. The two tables carry the argument. A pipeline-stage diagram would be decorative given the small failure count.
- Do not add a `{% include mathjax.html %}` block — there is no math in this post.

**Judge criteria depth:** State once that the regex judge checks length preservation plus 15 seeded strings (four criteria total). That's the right level of detail; do not elaborate beyond it.

**Rule 110 handling:** B's half-paragraph on "Rule 110 is Turing complete when iterated; this task asks for one update" is exactly right and should be retained in substance. A mentions it only glancingly.

## 4. Generic AI prose and benchmark-report tone

**Issues to eliminate:**
- "That contrast is sharp enough to feel like a finding" (A) is good — keep that register but do not multiply it.
- A has mild score-led tone in the "The track is six programs, not one depth axis" opening sentences; prefer B's question-first framing of the same material.
- Avoid stock transitions: "Furthermore," "Importantly," "It is worth noting." Neither draft overuses these; keep that discipline.
- Avoid empty superlatives: "sharp," "clean," "cleanest" are used sparingly in both — fine, but do not let them stack.
- **Both drafts contain the literal token "fuckingly"** in multiple places (A: once; B: three times). This is a sanitized remnant of findings-text expletives in the evidence packet. Strip it everywhere. The findings text itself used it as emphasis; it must not appear in public prose.
- Do not report 0.8333333333333334 as a percentage with that precision; "25 of 30" is the readable form. Avoid "83.3%" framing because the pooled rate is specifically what the post argues against.
- Avoid "the model passed/failed" when "the recorded cell passed/failed" would be more honest — this is a running tone issue in benchmark writing. Both drafts mostly handle it; keep the discipline.

## 5. Transitions and caveat placement

Each limitation must sit beside its claim:

- **Dirty-source / comparator caveat**: attach it specifically to the sentence that says the surface levels differ in class names *and* the hard prompt adds a performance hint. Do not relegate it to a late methodology paragraph.
- **Judge-mode / defect**: when stating 25/30, immediately note that all 30 are behavioral_reference-judged (so the number is not inflated by compile-only). This is a *supportive* caveat and must not be omitted even though it strengthens the number — the point is that even clean grading does not make the count a capability measure.
- **One-seed boundary**: attach to any sentence that could be read as an effect estimate. Especially the regex contrast and the "non-monotone" CSS/SQL rows.
- **Provider/exclusion**: the weird-machine track has no excluded rows and no provider-terminal rows. State this once, briefly, when introducing the 30-case denominator. Do not import the broader 192/61 taxonomy except as a one-sentence scale check — B uses it well; A omits it.
- **Speculative hypothesis**: the name-or-hint-mattered-more-than-length claim must stay explicitly flagged as speculation (both drafts handle this; keep B's plainer "I'm labelling it plainly as speculation" register).

**Specific placement fixes:**
- Do not let the comparator caveat and the dirty-tree caveat drift into separate paragraphs; they are one point and should be stated once, where it bites hardest (the moment the "class name + hint" bundle is named).
- The "clean comparator shows X about the category track" aside (ten no-reference axes) should be brief and clearly marked as *adjacent* evidence — B handles this well; A buries it.

## 6. Unsupported claims and claim traceability

**Statements to remove or narrow:**
- Any phrasing that treats the regex failures as caused by surface deception. The data support a response pattern, not a cause.
- Any framing of the aggregate 25/30 that reads as a capability number. Both drafts avoid this; the final must as well.
- "Length invariance" as a property of the model: narrow to "three passes at three lengths under one surface label, which is not an invariance estimate."
- "The model represented a weird machine": do not assert; the judge saw length + 15 seeded strings.
- Do not claim Turing completeness, arbitrary iteration, or general regex correctness were demonstrated.
- Do not describe the clean-source observations as facts about the paid run.
- Do not claim novelty against HELM/VarBench. Cite them for context only; the targeted prior-work check supports no "first" or exhaustive-novelty claim.

**Substantiate:**
- Every table number must trace to the evidence packet exactly. Allowed numeric vocabulary includes: 30, 25, 5, 3, 4, 32, 34, 66, 128, 512, 6, 12, 25, 0.416667, 0.208333, 0.0, 1.0, 15, 110, 33, 42, 192, 61, 10, 9. Do not round 0.416667 or 0.208333 in table cells.
- When citing HELM "42 scenarios" and VarBench "five seeds," keep those exact figures from the references.

**Do not invent:**
- Mechanistic stories for +2 or ~2× length (B wisely refuses this; A doesn't attempt it — keep the refusal).
- Any seed count other than 1 per cell.
- Any claim about what the paid-run source actually contained beyond what the comparator shows.
- Any author identity beyond the stated byline and the honest "written in an Arena pass from a compiled evidence packet" framing. Do not invent collaborators or external reviewers.

## 7. Public-site fit

**Jekyll frontmatter:**
- `title:` — avoid colons unless quoted; B wisely quotes "Thirty-Four Characters Out of Thirty-Two." Pick a title that is specific and non-grandiose; both A and B are acceptable models. Avoid "weird machine" in the headline since the post argues against treating it as measured.
- `date: 2026-10-03` (exact).
- `layout: post`.
- **No** `{% include mathjax.html %}` — no math in this post.

**Byline and epistemic status:**
- Exact byline: `*by <span class="icon-self">StrangeTcy</span>*`.
- `<dl class="epistemic-status">` with the five dt/dd pairs in order: Original ideas, Synthesis, Prose, Certainty, Importance. B's content is better calibrated (explicit "modest," "low for any causal reading," honest Arena-pass note). A's is adequate but slightly over-polished.
- Prose field: honestly describe the Arena writing pass from the compiled evidence packet; do not invent an author process beyond that; do not copy author-process claims from the style reference posts.

**Voice fit against StrangeTcy excerpts:**
- The style reference favors: short declarative openers that set a scene, visible self-correction, questions that move the argument, airy paragraphs, first-person.
- B is closer to the reference register ("I believed that for about one paragraph of the first draft" is pure style-reference voice; cf. "The first formalisation was wrong").
- A is more measured but slightly closer to benchmark-report register in its middle sections.
- The final piece should allow at least one visible self-correction moment and at least one question that genuinely moves the argument, not a rhetorical one.

**Links/Markdown:**
- Cite HELM and VarBench inline where they're mentioned (B does this correctly). Links go where they matter, not in a bibliography block.
- Tables use standard Markdown pipes; both drafts' table syntax is fine.
- Do not include editorial markers, evidence IDs, finding IDs, SHA hashes, or claim IDs in public prose.
- Do not include an "Editor's note" footer referencing internal CSVs (source draft does this; strip it).

**Layout mismatches to avoid:**
- No `## Introduction` heading. Open in prose.
- Keep headings short, argumentative turns (`## The regex contrast is real and confounded` works; `## Background` does not).
- Target 1,800–2,800 words. A ≈ 1,500 (short); B ≈ 2,400 (within range). Final should land ~2,000–2,400.

## A/B elements worth retaining

**From A:**
- The disciplined "What the evidence licenses" closing register — a bulletless, prose statement of what is and is not supported. Use this *as* the closing section's spine, but keep B's enumerated "licenses / does not license" lists for scannability.
- The crisp "I keep the layers distinct on purpose" principle statement about not collapsing failure types.
- The one-sentence framing that comparator findings are not paid-run identity.

**From B:**
- The question-led opener style (not the exact words).
- Both tables (regex 5-cell; failure stratification by layer) — these are the piece's most informative artifacts.
- The explicit per-environment pass table.
- The honest refusal to invent a mechanism for 34 and 66.
- The one-paragraph aside on the broader 192/61 taxonomy for scale, with the "overfit_visible_tests" mislabel noted briefly.
- The "experiment I'd want" numbered list — cleaner than A's prose version.
- The Rule 110 / Turing-completeness disclaimer paragraph.

## Elements neither draft handles well

- **Why the depth axes aren't commensurable as units of work.** Both state it; neither gives the reader a one-line intuition. A single sentence like "a 512-character string is not twice the computational demand of a 25-node chain" would land it.
- **The judge's four criteria for regex** are mentioned (15 seeded strings + length) but the full count of four criteria is underused; stating "the judge checks four things, and three passes mean those four held on seed 0" would sharpen the "local" claim.
- **The CSS surface sweep at 3 bits (fail/pass/pass) runs opposite to the regex surface sweep.** B notes this; A doesn't. Final piece should give it one sentence as a check against overgeneralization *from the regex contrast itself*.
- **The adjacent category-track axis-placeholder audit** is mentioned by both but the connection to the regex finding (same class of problem: labels promise manipulations that artifacts may not deliver) is explicit only in B. Keep B's framing.
- **Explicit statement that no compile-only cases exist in this track** — A has it, B does not. Include it; it defuses a plausible reader objection.

## Exact evidence boundaries

**In-bounds:**
- All numbers in the allowed-numbers list, used in their exact packet context.
- The dirty-repository flag.
- 33/33 config-hash match with the clean comparator (as comparator-level evidence, not run-identity proof).
- The regex judge criteria (four, including 15 seeded strings and length preservation).
- Failure modes exactly as labeled: underfit, source_invalid.
- HELM: 42 scenarios. VarBench: dynamic variable perturbation, five seeds for variable-based experiments.
- Broader campaign: 61 fails of 192 eligible; the two mislabeled overfit_visible_tests cases.

**Out-of-bounds:**
- Any seed count > 1.
- Any causal attribution for the two regex failures.
- Any claim about paid-run source identity beyond "comparator shows X."
- Any Turing-completeness / arbitrary-iteration claim.
- Any novelty claim against prior work.
- Any mechanism for +2 or +34 output-length discrepancies.
- Any inference about model capability from the aggregate 25/30.

## Final quality checklist

- [ ] Frontmatter: title, `date: 2026-10-03`, `layout: post`. No mathjax include.
- [ ] Exact byline present; epistemic-status `<dl>` with five fields in order.
- [ ] Opens in prose (no `## Introduction`); limit stated within first two paragraphs.
- [ ] Regex 5-cell table present with exact scores 1.0, 0.208333 and the length-mismatch notes.
- [ ] Failure-layer stratification table present; behavioral vs. source-invalid distinction visible before any pooling.
- [ ] Per-environment pass table present.
- [ ] Comparator / dirty-repository caveat placed at the moment the name+hint bundle is first named.
- [ ] One-seed caveat placed beside the regex contrast and beside any non-monotone pattern.
- [ ] Behavioral-reference judge-mode noted when the 25/30 is first stated.
- [ ] No-exclusions / no-provider-terminal note included once for this track.
- [ ] Rule 110 single-update vs. Turing-completeness disclaimer present.
- [ ] Speculative hypothesis (name-or-hint > length) explicitly marked speculative.
- [ ] HELM (42 scenarios) and VarBench (five seeds) cited as context only, with inline links; no novelty claim.
- [ ] Category-track axis-placeholder audit (10 axes / 9 environments) mentioned briefly as adjacent, with dirty-repo caveat.
- [ ] Visible self-correction moment present at least once.
- [ ] "What the evidence licenses / does not license" closing with explicit lists.
- [ ] Word count 1,800–2,800.
- [ ] No "fuckingly," no evidence IDs, no SHA hashes, no claim IDs, no "Editor's note" with internal file references.
- [ ] No equation, no `{% include mathjax.html %}`.
- [ ] All numerics drawn from the allowed vocabulary and used in packet context.
- [ ] No invented authors, no invented reviewers, no author-process claims copied from style-reference posts.
[[[ END INPUT 04 — job:post05_editorial_critic:response ]]]
