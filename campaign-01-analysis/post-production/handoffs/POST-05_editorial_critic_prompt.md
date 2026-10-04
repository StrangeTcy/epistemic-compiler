# Editorial critic and blueprint — POST-05

You receive the evidence packet, Writer A, and Writer B. Do not choose a winner and do not simply merge the two drafts. Build an actionable editorial blueprint for an original final article. Check each dimension explicitly:

1. Conceptual structure and thesis: what is the real argument, what should be moved/cut, and where do the posts' structures diverge?
2. Opening: compare specificity, tension, and how quickly the opening states its limit; propose a fresh opening strategy, not copied prose.
3. Examples and technical depth: are task examples exact, source-grounded, and useful? Are mathematics/tables/diagrams useful or decorative? Specify equations or a compact diagram only when they sharpen the argument.
4. Generic AI prose and benchmark-report tone: identify stock transitions, empty emphasis, overlong setup, unsupported superlatives, or score-led reporting.
5. Transitions and caveat placement: keep each limitation beside the claim it qualifies; retain dirty-source/comparator, judge-mode/defect, provider/exclusion, and one-seed boundaries relevant to this post.
6. Unsupported claims and claim traceability: list exact statements to remove, narrow, or substantiate from the packet. Do not invent evidence or citations.
7. Public-site fit: check StrangeTcy voice against the actual excerpt content, Jekyll frontmatter/date/title, `{% include mathjax.html %}`, the author signature convention, epistemic-status framing, link/Markdown details, and likely layout mismatches.

The final writer must receive a usable blueprint: proposed thesis, opening strategy, section-by-section sequence, example/equation/table plan, A/B elements worth retaining (with reasons), elements neither draft handles well, exact evidence boundaries, and a final quality checklist. Do not draft the complete article. Do not copy author-process claims from reference posts.

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
