# Independent StrangeTcy research essay — POST-05

Write one complete essay with a new thesis, opening, and argument structure. Use the full draft as an evidence map, not an outline or prose to paraphrase. This is one of two parallel candidates; do not refer to or imitate another answer.

Use only supplied facts and citations. Keep raw scores, exclusions, provider-terminal cases, denominators, judge guarantees, and failure layers distinct. Compile-only outcomes are exploratory, not a validated behavioral aggregate. There is one selected seed per cell; subsequent editorial/model role passes are not independent replications. The repository was recorded dirty: the clean source is only a comparator. These sparse results do not establish causal effects, a common difficulty scale, or a general capability ranking. Keep caveats next to claims. Distinguish validator/runtime/tool/judge failures from behavioral misses.

POST-02 is Bayesian inference over stipulated policies, not recursive ToM; POST-05's Rule 110/code-repair observations do not establish Turing completeness. Category-track outcomes are heterogeneous code-repair results, not a theorem or scalar score.

The packet includes verbatim excerpts from actual StrangeTcy posts: use them only for rhetorical structure, never copy distinctive wording, examples, titles, or author-process claims. Avoid generic AI prose and benchmark-report tone; use technical detail and math/tables/diagrams only when they clarify.

Return only the complete Markdown article, 1,800–2,500 words. Use frontmatter `title`, `date: 2026-10-03`, `layout: post`; the exact StrangeTcy byline; and the site's epistemic-status `<dl>` fields in order: Original ideas, Synthesis, Prose, Certainty, Importance. If using math, place `{% include mathjax.html %}` after frontmatter. Attribute the actual Arena writing process accurately. No preface, editor note, draft label, internal `F-xx`/`POST-xx` ID, path, hash, or response fence.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post05_prepare_post:response | source_sha256=0ec5bd833da23585f48f4141dd1cd4f9cd3d793e922f27f87f2b043cf5d45942 | rendered_sha256=8f301efbae02f0677ef5889034383607b886fd1c23bb75a3f13dbbb6861a1e26 ]]]
# Compiler evidence packet — POST-05

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
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

## Target-site style and Jekyll conventions
Target Jekyll frame: YAML frontmatter with `title`, `date: 2026-10-03`, `layout: post`; when using math, place `{% include mathjax.html %}` immediately after it. Then use the exact byline `*by <span class="icon-self">StrangeTcy</span>*` and the site's `<dl class="epistemic-status">` fields, in order: Original ideas, Synthesis, Prose, Certainty, Importance. Attribute the actual Arena writing process accurately; do not invent outside authors.

Voice: first-person, curious, technically literate, willing to self-correct. Open in prose, not an `Introduction`; use short, specific `##` argumentative turns and airy paragraphs. Questions should move the argument. End by stating what the evidence does and does not license. Links/citations belong where they matter; avoid a generic benchmark-report register. Target 1,800–2,800 words without padding.

## Actual StrangeTcy reference-post excerpts
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

## Relevant prior-work references
POST-05 prior-work references from the source draft; context only, not validation of this campaign.

- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation and repeated sampling for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: broad scenario coverage and multiple metrics, as context for avoiding a single-score interpretation. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim.

## Claim-to-finding map
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

## Relevant finding records
{"claim_ids":["POST-05-C01","POST-05-C02","POST-05-C03","POST-05-C04","POST-05-C05","POST-05-C06","POST-05-C07","POST-05-C08","POST-05-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"Selected nominal-axis outcomes are heterogeneous and sometimes nonmonotone; the archived `easy`/`medium`/`hard` labels do not form a common calibrated scalar difficulty scale.","confidence":"HIGH for these observed case outcomes; LOW for any causal effect of a nominal axis.","id":"F-06","limitations":["One selected case/seed per cell and no cell-level replications.","Many comparisons are one-factor contrasts around a single baseline, not full factorial designs.","Axis names such as hidden_depth map to different quantities in different environments."],"quantitative_result":"Examples: regex at easy surface passes at lengths 32/128/512, while medium/hard surface labels fail at length 32; CSS at easy surface scores 0.416667/0/1.0 over 3/4/5 bits (the middle row is source-invalid); SQL at easy surface passes at graph-chain lengths 6 and 25 but has a source-invalid length-12 case; moco visible-test levels are pass/fail/pass.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"The weird_machine track shows task-specific successes and failures under regex, CSS, SQL, spreadsheet, CI, and template tasks; the controlled surface/depth pattern is especially sharp in regex but confounded and unreplicated.","confidence":"HIGH for the selected case outcomes; LOW for generalized surface/depth causality.","id":"F-10","limitations":["One run per selected cell, no seed-level replication, and only a sparse design.","The regex surface manipulation bundles class name and an extra hard-level hint.","CSS and SQL selected failures include source-validation errors."],"quantitative_result":"25/30 eligible PASS overall. Regex 3/5; CSS 3/5; SQL 4/5; spreadsheet 5/5; CI dependency graph 5/5; template interpreter 5/5. At easy regex surface, all 3 string lengths pass; at easy string length, the other 2 class-name variants fail.","status":"OBSERVED"},{"claim":"The category-track source comparator indicates several advertised axes were not implemented in the environment templates, so nominal coverage can overstate the number of distinct interventions.","confidence":"HIGH for no direct reference in the inspected clean source files; MEDIUM for the claim about executed paid cases because the recorded repository was dirty.","id":"F-14","limitations":["The static scan does not execute generation or compare every rendered task bundle.","Only selected configurations were scanned; unsupported and gate-blocked cases were not model-run."],"quantitative_result":"The static scan finds ten no-reference control/variable axes across nine category environments, including both axes in compositional_optimizer; details are in axis_placeholder_audit.csv and source_implementation_audit.md.","status":"INFERRED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"},{"claim":"In this particular regex task and model run, surface class names or the hard-level performance hint may have influenced the two failures more than the tested input-string length; this is an untested hypothesis, not an inferred causal effect.","confidence":"LOW; deliberately speculative.","id":"F-18","limitations":["Only five selected rows from one model/configuration; no repeated seed per cell.","Surface label bundles class-name changes and an added hard-level hint.","The clean comparator is not proven identical to the dirty paid-run source."],"quantitative_result":"At easy surface, selected lengths 32, 128, and 512 all pass. At string length 32, the medium and hard surface variants fail with output lengths 34 and 66. The hard prompt adds a performance note.","status":"SPECULATIVE"}],"post_id":"POST-05","schema_version":1,"trace_finding_ids":["F-01","F-06","F-09","F-10","F-14","F-16","F-17","F-18"]}

## Archive evidence extract
Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## Evidence limitations
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

## Source-comparator audit
## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## Analysis-family totals
analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
weird_machine,30,30,25,5,0.8333333333333334,30,25,5,0,0,0

## Selected axis results
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

## Evidence Case Results Post-05
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

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
ci_dependency_graph,5,5,5,0,1.0,5,5,0,0,0,0
css_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
regex_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
spreadsheet_dataflow,5,5,5,0,1.0,5,5,0,0,0,0
sql_fixed_point,5,5,4,1,0.8,5,4,1,0,0,0
template_interpreter,5,5,5,0,1.0,5,5,0,0,0,0

## Selected failure details
environment,condition,judge,score,failure,detail
css_state_machine,surface_deceptiveness=easy_hidden_depth=easy,behavioral_reference,0.416667,underfit,
css_state_machine,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source validator rejected import re
regex_state_machine,surface_deceptiveness=hard_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 66"
regex_state_machine,surface_deceptiveness=medium_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 34"
sql_fixed_point,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source syntax error: unterminated triple-quoted string

## Failure taxonomy
failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"
[[[ END INPUT 01 — job:post05_prepare_post:response ]]]
