# Editorial critic and blueprint — POST-01

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

[[[ BEGIN INPUT 01 — job:post01_prepare_post:response | source_sha256=df336be278a34547e17b7fd8094bc981ade9154f0262bc681743eaec2fb3746f | rendered_sha256=20a780738098344a92c5eb77e641085c622464247904e521656f323c313b295f ]]]
# Compiler evidence packet — POST-01

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
# POST-01 — The benchmark’s “hard” is not one difficulty scale

**Dek:** A single campaign sweep produced a jagged pattern across task families. That is useful evidence about these cases, but not a universal ranking of reasoning ability.

**Draft**

“Easy, medium, hard” sounds like a staircase. In this campaign archive, it is closer to a set of labels attached to different stairs—and sometimes to a different building entirely.

The raw checkpoint contains 194 selected results: 131 PASS and 63 FAIL. The archive separately lists 24 cases that never became scored model results. Two of the 194 final results carry provider-transient failure notes. For the primary performance analysis, I exclude both while keeping the raw counts visible: 131 PASS and 61 FAIL among 192 eligible cases. This is a descriptive result from one Atria-Dawn-Preview campaign, not a common score for general reasoning. ⟦POST-01-C01 · F-02/F-03⟧

Even that 192-case set combines two different judge guarantees: 72 behavioral-reference cases and 120 compile-only cases after provider exclusions. The campaign report explicitly calls compile-only verdicts exploratory. Any capability map should therefore show task and judge mode—not just color each environment green or red. All source-implementation descriptions below use the clean comparator at the recorded commit; the archive’s `repository.dirty=true` flag means exact paid-run source identity is unresolved. ⟦POST-01-C02 · F-01/F-04⟧

## What changes when “difficulty” changes?

In the regex Rule 110 environment, “hidden depth” means input-string length: 32, 128, or 512 characters. With the surface label held at easy, the selected model run passes all three lengths. At length 32, however, the medium and hard surface labels fail: the output grows to 34 and 66 characters, respectively, instead of preserving length. The archived cases show a sharp contrast, but they do not isolate a general surface effect: in the clean source comparator, those labels also change class names, and the hard prompt includes an extra performance hint. Because the campaign records `repository.dirty=true`, those comparator details do not prove the exact paid-run files. There is one seed-0 run per selected cell. ⟦POST-01-C03 · F-01/F-06/F-10⟧

CSS and SQL make the word “difficulty” even less portable. In the CSS state-machine task, the easy-surface cases over 3, 4, and 5 bits yield a partial score, a source-validation failure caused by a disallowed import, and a pass. At the fixed three-bit input, the surface-label sweep yields a failure followed by two passes. For SQL, the easy-surface cases pass at graph-chain lengths 6 and 25, while the 12-node case fails source validation because of an unterminated string. The 4/5 SQL and 3/5 CSS environment totals hide those different failure layers. ⟦POST-01-C04 · F-06/F-09/F-10⟧

Other task families produce different profiles again. The five selected spreadsheet cases pass at their tested class-name and grid-length levels; the six weird-machine environments together have 25 passes out of 30 eligible cases. In the MoCo debugging task, the visible-test levels produce pass, fail, pass; the middle case has a trusted test score of 1.0 but is marked failed because a required companion file is missing. In adaptive recurrence halting, the easy-depth case is a syntax error, while the medium- and hard-depth cases pass. None of those patterns is a clean measure of one shared latent “difficulty.” ⟦POST-01-C05 · F-06/F-09/F-10/F-11/F-12⟧

## A map, not a leaderboard

A useful map here has at least four layers: what input changed, what the judge actually checked, whether the judge had an instance-specific behavioral reference, and how the submission terminated. It should display the empty-patch, validator, runtime, and behavioral-test outcomes separately. A red cell for an empty file is not the same observation as a wrong algorithm that runs and fails a hidden behavioral test. ⟦POST-01-C06 · F-04/F-09/F-16⟧

The archive’s family totals reinforce that caution. Recurrent-depth has 31 passes in 33 eligible cases, while trajectory/synthesis has 2 in 8. That contrast is a description of these selected tasks, model, prompts, and judges—not evidence that recurrence is intrinsically easier than synthesis. The family labels cover different code tasks, sizes, tests, and score modes, and they are not calibrated to a common construct. ⟦POST-01-C07 · F-04/F-11/F-16⟧

This is not a new evaluation principle. HELM is an established example of broad scenario coverage with multiple metrics, while VarBench dynamically perturbs task variables and repeats variable-based experiments across sampled values. The relevant lesson is modest: a benchmark should expose what each score means and where a manipulation changed the actual task. This campaign’s single-seed contrasts fall short of estimating general intervention effects. ([HELM](https://arxiv.org/abs/2211.09110); [VarBench](https://aclanthology.org/2024.findings-emnlp.946/)). ⟦POST-01-C08 · F-17⟧

So what can the “capability map” say? It can show that, in this archived run, outcomes are heterogeneous and some nominal contrasts are non-monotone. It cannot rank general capabilities, make “hard” comparable across environments, or establish that surface form caused the differences. A repaired follow-up would first verify each rendered axis, then hold names and hints constant, run multiple seeds, and report results by judge guarantee and failure layer. Until then, the map is most useful as a guide to which cases and implementations need inspection—not as a model leaderboard. ⟦POST-01-C09 · F-06/F-14/F-16⟧

**Editor’s note:** Evidence tags and links in double brackets are internal provenance markers; they can be removed from a public-facing copy after the traceability sheet is reviewed.

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
POST-01 prior-work citations from the source draft; precedent only, not validation of this campaign.

- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: 42 scenarios and multiple metrics. https://arxiv.org/abs/2211.09110
- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation; five sampled runs (seeds 40–44) for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/

This targeted reference check supports no “first” or exhaustive-novelty claim.

## Claim-to-finding map
post_id,claim_id,finding_ids
POST-01,POST-01-C01,F-02;F-03
POST-01,POST-01-C02,F-01;F-04
POST-01,POST-01-C03,F-01;F-06;F-10
POST-01,POST-01-C04,F-06;F-09;F-10
POST-01,POST-01-C05,F-06;F-09;F-10;F-11;F-12
POST-01,POST-01-C06,F-04;F-09;F-16
POST-01,POST-01-C07,F-04;F-11;F-16
POST-01,POST-01-C08,F-17
POST-01,POST-01-C09,F-06;F-14;F-16

## Relevant finding records
{"claim_ids":["POST-01-C01","POST-01-C02","POST-01-C03","POST-01-C04","POST-01-C05","POST-01-C06","POST-01-C07","POST-01-C08","POST-01-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign report records 194 scored selected cases and 24 separate pre-scoring omissions; the case manifest and result checkpoint contain the same 194 case IDs.","confidence":"HIGH.","id":"F-02","limitations":["The 7 gate-blocked and 17 unsupported cases have no model score and must not be counted as failures or passes.","A complete unfiltered planned-design file is not required to reproduce this report-level union."],"quantitative_result":"194/194 selected results have status scored across 33 environments; 17 rope cases are omitted for unsupported provider input modality and 7 cases are omitted before provider access for known calibration failures; 218 case IDs are recorded as scored or explicitly omitted.","status":"OBSERVED"},{"claim":"Two final selected results, not just the one named in the campaign-level outage counter, explicitly attribute their terminal failure to provider transients after bounded retries.","confidence":"HIGH that both final notes exist; MEDIUM that every terminal provider-coded row should be excluded from model-performance analysis, because the official campaign counter tracks only one episode.","id":"F-03","limitations":["The raw row remains scored and its raw failure label is retained; the 192 denominator is an explicit analysis exclusion, not a rewritten campaign report.","API error events also include transient retries that recovered; only final-result terminal notes define these two exclusions."],"quantitative_result":"Raw checkpoint: 131 PASS / 63 FAIL among 194. Removing only report-listed ts_trajectory gives 131/193 PASS and 62 FAIL. Removing both final-note provider cases gives 131/192 PASS and 61 FAIL.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"Selected nominal-axis outcomes are heterogeneous and sometimes nonmonotone; the archived `easy`/`medium`/`hard` labels do not form a common calibrated scalar difficulty scale.","confidence":"HIGH for these observed case outcomes; LOW for any causal effect of a nominal axis.","id":"F-06","limitations":["One selected case/seed per cell and no cell-level replications.","Many comparisons are one-factor contrasts around a single baseline, not full factorial designs.","Axis names such as hidden_depth map to different quantities in different environments."],"quantitative_result":"Examples: regex at easy surface passes at lengths 32/128/512, while medium/hard surface labels fail at length 32; CSS at easy surface scores 0.416667/0/1.0 over 3/4/5 bits (the middle row is source-invalid); SQL at easy surface passes at graph-chain lengths 6 and 25 but has a source-invalid length-12 case; moco visible-test levels are pass/fail/pass.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"The weird_machine track shows task-specific successes and failures under regex, CSS, SQL, spreadsheet, CI, and template tasks; the controlled surface/depth pattern is especially sharp in regex but confounded and unreplicated.","confidence":"HIGH for the selected case outcomes; LOW for generalized surface/depth causality.","id":"F-10","limitations":["One run per selected cell, no seed-level replication, and only a sparse design.","The regex surface manipulation bundles class name and an extra hard-level hint.","CSS and SQL selected failures include source-validation errors."],"quantitative_result":"25/30 eligible PASS overall. Regex 3/5; CSS 3/5; SQL 4/5; spreadsheet 5/5; CI dependency graph 5/5; template interpreter 5/5. At easy regex surface, all 3 string lengths pass; at easy string length, the other 2 class-name variants fail.","status":"OBSERVED"},{"claim":"The recurrent-depth family has high recorded pass counts, but the environment and judge-mode mixture does not establish a general recurrence-depth scaling law.","confidence":"HIGH for recorded counts and terminal notes; LOW for a depth-related mechanism.","id":"F-11","limitations":["Mixed behavioral-reference/compile-only guarantees and one seed per selected case.","The depth manipulation changes several numerical capacities and is not replicated."],"quantitative_result":"31/33 PASS; rd_state_carry 11/11 behavioral_reference, rd_gradient_credit 11/11 compile_only, rd_adaptive_halting 9/11 compile_only. The adaptive easy-depth failure is an unexpected-indentation source error; another failure is a float-mask runtime error.","status":"OBSERVED"},{"claim":"After removing the epistemic_games track-label anomaly, the three selected ML-debugging environments show 9/30 PASS, with highly uneven task outcomes.","confidence":"HIGH for per-environment result counts and notes; MEDIUM for using the three tasks as a coherent ML-debugging construct.","id":"F-12","limitations":["Only three environment families are grouped here; one has compile-only judgments.","One seed and one selected response per case; no general ML-debugging inference."],"quantitative_result":"batchnorm_ema 0/11 (compile_only), glyph 0/8 (behavioral_reference), moco 9/11 (behavioral_reference); the two MoCo/BatchNorm rows labeled overfit_visible_tests have notes about missing required companion files.","status":"OBSERVED"},{"claim":"The category-track source comparator indicates several advertised axes were not implemented in the environment templates, so nominal coverage can overstate the number of distinct interventions.","confidence":"HIGH for no direct reference in the inspected clean source files; MEDIUM for the claim about executed paid cases because the recorded repository was dirty.","id":"F-14","limitations":["The static scan does not execute generation or compare every rendered task bundle.","Only selected configurations were scanned; unsupported and gate-blocked cases were not model-run."],"quantitative_result":"The static scan finds ten no-reference control/variable axes across nine category environments, including both axes in compositional_optimizer; details are in axis_placeholder_audit.csv and source_implementation_audit.md.","status":"INFERRED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-01","schema_version":1,"trace_finding_ids":["F-01","F-02","F-03","F-04","F-06","F-09","F-10","F-11","F-12","F-14","F-16","F-17"]}

## Archive evidence extract
Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## Evidence limitations
- One selected seed per case; no cell-level replications. Keep 194 raw results, 24 separate omissions, two provider-terminal cases, and the 192-case sensitivity set distinct.
- The eligible set mixes 72 behavioral-reference and 120 compile-only cases; compile-only results are exploratory, not a validated behavioral aggregate.
- The repository was recorded dirty; matching config hashes do not establish exact task/judge identity. Axes are task-specific and sparse; names/hints are bundled, and validator/runtime/judge failures are not behavioral misses.

## Source-comparator audit
## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## Analysis-family totals
analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
ml_debugging,30,30,9,21,0.3,19,9,10,11,0,11
recurrent_depth_behavioral,33,33,31,2,0.9393939393939394,11,11,0,22,20,2
weird_machine,30,30,25,5,0.8333333333333334,30,25,5,0,0,0

## Selected axis results
environment,axis,level,control,recorded,eligible,passes,fails,rate,judge
css_state_machine,hidden_depth,easy,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
css_state_machine,hidden_depth,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
css_state_machine,hidden_depth,medium,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
css_state_machine,surface_deceptiveness,easy,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
css_state_machine,surface_deceptiveness,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
css_state_machine,surface_deceptiveness,medium,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
moco,visible_tests,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
moco,visible_tests,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
moco,visible_tests,medium,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
rd_adaptive_halting,recurrence_depth,easy,all_other_axes_easy,1,1,0,1,0.0,compile_only
rd_adaptive_halting,recurrence_depth,hard,all_other_axes_easy,1,1,1,0,1.0,compile_only
rd_adaptive_halting,recurrence_depth,medium,all_other_axes_easy,1,1,1,0,1.0,compile_only
regex_state_machine,hidden_depth,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
regex_state_machine,hidden_depth,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
regex_state_machine,hidden_depth,medium,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
regex_state_machine,surface_deceptiveness,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
regex_state_machine,surface_deceptiveness,hard,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
regex_state_machine,surface_deceptiveness,medium,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,hidden_depth,medium,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
spreadsheet_dataflow,surface_deceptiveness,medium,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,easy,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,hard,all_other_axes_easy,1,1,1,0,1.0,behavioral_reference
sql_fixed_point,hidden_depth,medium,all_other_axes_easy,1,1,0,1,0.0,behavioral_reference

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
batchnorm_ema,11,11,0,11,0.0,0,0,0,11,0,11
ci_dependency_graph,5,5,5,0,1.0,5,5,0,0,0,0
css_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
glyph,8,8,0,8,0.0,8,0,8,0,0,0
moco,11,11,9,2,0.8181818181818182,11,9,2,0,0,0
rd_adaptive_halting,11,11,9,2,0.8181818181818182,0,0,0,11,9,2
rd_gradient_credit,11,11,11,0,1.0,0,0,0,11,11,0
rd_state_carry,11,11,11,0,1.0,11,11,0,0,0,0
regex_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
spreadsheet_dataflow,5,5,5,0,1.0,5,5,0,0,0,0
sql_fixed_point,5,5,4,1,0.8,5,4,1,0,0,0
template_interpreter,5,5,5,0,1.0,5,5,0,0,0,0

## Selected failure details
environment,condition,judge,score,failure,detail
css_state_machine,surface_deceptiveness=easy_hidden_depth=easy,behavioral_reference,0.416667,underfit,
css_state_machine,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source validator rejected import re
moco,naming=easy_distractors=easy_queue_math=easy_temperature=easy_visible_tests=medium_symptom_mask=easy,behavioral_reference,0.95,overfit_visible_tests,required companion file missing: moco_model.py temperature_cancelled; trusted_score=1.0 despite failed terminal label
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=easy_batching_complexity=easy,compile_only,0.0,source_invalid,source syntax error: unexpected indentation
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=medium_batching_complexity=easy,compile_only,0.0,RUNTIME_ERROR,runtime error: float tensor used as a boolean condition
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
[[[ END INPUT 01 — job:post01_prepare_post:response ]]]

[[[ BEGIN INPUT 02 — job:post01_battle_writer_a:response | source_sha256=1487cb4192f795635fe3e8013be006e10095d0fffcc87dfd7da180399283821d | rendered_sha256=1487cb4192f795635fe3e8013be006e10095d0fffcc87dfd7da180399283821d ]]]
---
title: "Same Numerator, Three Denominators"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The framing of a campaign archive as a stack of stopping layers, and the claim that a pass rate is only legible once you say which layer it was taken from. The underlying evidence is one archived campaign; nothing here is a new evaluation principle.</dd>
  <dt>Synthesis</dt><dd>Written from an audited evidence packet prepared for this post in the Arena pipeline: a frozen archive of one paid Atria-Dawn-Preview campaign, finding records with stated confidence, a source-comparator audit, and a targeted (not systematic) prior-work check. I did not re-run any cases.</dd>
  <dt>Prose</dt><dd>Drafted in one pass from the packet; the argument structure is mine, the numbers are the packet's.</dd>
  <dt>Certainty</dt><dd>High for recorded counts and terminal notes; low for any causal reading of the difficulty axes, and low for the identity between the inspected source and what fuckingly ran, because the repository was recorded dirty.</dd>
  <dt>Importance</dt><dd>Moderate as a reading guide for this archive; modest as a general point, since the general point is old.</dd>
</dl>

I was handed the number 131 three times before I noticed it was the same number.

The first time it was 131 out of 194. The second time, 131 out of 193. The third, 131 out of 192. The passes never moved. Only the thing they were being divided by moved, and each division was quietly a different claim about what the campaign had measured.

That is the whole essay, really. A benchmark archive is not a scoreboard with some footnotes attached. It is a stack of places where a case can stop, and the number you report depends on which of those places you decided to stop counting at. Once I started reading the archive that way, most of the apparently interesting "difficulty" patterns in it turned into something else — not less interesting, but differently interesting, and much less flattering to the word *hard*.

## Where a case can stop

Let me lay out the stack as the archive records it, from the outside in.

Before any model was called, 24 cases were already out. Seventeen were omitted because the provider did not support the input modality those cases needed; seven were omitted before provider access because their calibration was already known to fail. Together with the 194 that were scored, that makes 218 case IDs the campaign accounts for. Those 24 have no model score. They are not failures, and they are not passes; they are cases the campaign never asked the question of.

Of the 194 that were scored, 131 passed and 63 failed. That is the raw checkpoint and it stays the raw checkpoint; I am not rewriting it.

Two of the 63 failures carry final-result notes attributing the terminal outcome to provider transients after bounded retries. Here the archive disagrees with itself in a small way: the campaign-level outage counter names only one episode, but two final rows carry the note. If you remove the one the report names, you get 131/193. If you remove both, you get 131/192. I use 192 below, and I want to be honest that it is an analysis choice layered on top of the report, not the report itself. My first instinct was to put 192 in a headline. It is the better denominator for asking about the model, but it is already an editorial act, and the point of this piece is that such acts should be visible.

Now the 61 remaining failures. The archive labels each with a failure mode, and the labels are worth reading literally rather than psychologically:

| Terminal label | Count | What the notes fuckingly say |
|---|---:|---|
| patch_invalid | 24 | every one an empty patch |
| underfit | 20 | ran, was judged, scored below threshold |
| source_invalid | 10 | rejected by the source validator before execution |
| runtime_error | 3 | crashed during execution |
| invalid_action | 2 | malformed action |
| overfit_visible_tests | 2 | trusted score of 1.0; a required companion file was missing |

Those last two rows are the ones that made me stop. The label says the submission overfit the visible tests. The note says the trusted test score was perfect and a required file was absent. Whatever happened there, "overfit" is not what the recorded evidence describes. I take this as a reminder that `failure_mode` is a campaign label, applied by a judge pipeline, and not a validated taxonomy of what the model was doing. It is a stopping layer with a name attached.

So of 61 failures, 24 never produced anything, 10 never got past a syntax or import check, 3 crashed, 2 were malformed, and 2 are mislabelled by their own notes. That leaves 20 cases where a program ran, was judged, and was judged wrong. Twenty is the number of behavioural misses in the plain sense of the phrase. The other 41 are something, but they are not that.

## Two judges wearing one colour

There is a second seam in the stack that the raw pass rate hides entirely. The 192 eligible cases were judged under two different guarantees. Seventy-two had an instance-specific behavioural reference — the judge knew what this particular task's correct behaviour was. One hundred and twenty were compile-only, and the campaign report itself calls those verdicts exploratory and keeps them out of any validated aggregate.

The split in outcomes: behavioural-reference cases went 56 pass, 16 fail. Compile-only cases went 75 pass, 45 fail (47 before removing the two provider-terminal rows).

Why does this matter beyond bookkeeping? Because the families the archive groups into "tracks" mix the two guarantees unevenly. The weird-machine track is entirely behavioural-reference: all 30 of its eligible cases. The recurrent-depth family is 11 behavioural-reference and 22 compile-only. The three ML-debugging environments split 19 and 11. A green cell in one track and a green cell in another are not the same observation. One says *the judge checked this instance's behaviour and it was right*. The other says *it compiled and cleared an exploratory check*. Colouring them the same shade is not a lie, exactly, but it is a design decision that makes the map harder to read than the data underneath it.

Within the compile-only families the point sharpens. The gradient-credit environment went 11 for 11 and the BatchNorm EMA environment went 0 for 11, both compile-only. I genuinely do not know how to compare those two numbers to the MoCo environment's 9 of 11 under behavioural reference, and I think the correct response to not knowing is to not pretend.

## What the difficulty knobs fuckingly turn

With the layers in view, I can look at the part of the archive that invites the most tempting story: the easy/medium/hard axes.

The regex state-machine environment is where the pattern looks cleanest, so start there. Its "hidden depth" axis is input-string length: 32, 128, or 512 characters. With the surface label held at easy, the selected run passes all three lengths. Hold length at 32 instead and sweep the surface label, and medium and hard both fail — underfit, same partial score, with the notes recording that the output came back 34 and 66 characters long against a 32-character input. Length preservation is the whole game in a Rule-110-style task, so those are real behavioural misses, judged against a behavioural reference.

That looks like a surface effect. Is it? The clean source comparator says the surface levels also change class names, and the hard prompt carries an extra performance hint the easy prompt does not. So the manipulation is a bundle: label, name, hint. There is one seed-0 run per cell. And the archive records the repository as dirty at the time of the run, which means the comparator I just described is a comparator, not a transcript of what ran. The contrast is sharp and it is real for these cases. It does not isolate a cause.

CSS is where the layers really earn their keep. Sweep hidden depth at easy surface and you get, over 3, 4, and 5 bits: a partial score of about 0.42, a zero, and a pass. Read as a difficulty curve it is non-monotone and strange. Read by layer it dissolves: the zero at 4 bits is a source-validator rejection because the submission imported `re`, which was disallowed. That is not the model failing to solve a four-bit state machine. It is the model never being allowed to try. The 3-bit case *is* a judged behavioural miss; the 4-bit case is a validator stop; the 5-bit case passed. Three different layers, one row of a table.

SQL repeats the shape. At easy surface, chain lengths 6 and 25 pass; length 12 fails. The length-12 failure is an unterminated triple-quoted string caught by the source validator. Whatever one wants to say about a model that produces an unterminated string literal, "the medium-depth SQL task was harder" is not supported by this row.

The recurrent-depth adaptive-halting environment does the same thing from the other side. The easy-depth case fails and medium and hard pass — exactly backwards from the staircase story — but the easy-depth failure is an unexpected-indentation syntax error. Another failure in that environment is a runtime error from using a float tensor as a boolean condition. Those are failures. They are not depth-related failures in any sense the axis name promises.

And MoCo's visible-test axis goes pass, fail, pass, where the middle fail is the case I described above: trusted score 1.0, required companion file missing, labelled overfit.

So when I sort the selected axis sweeps by what fuckingly stopped each failing case, I get this:

- Regex surface sweep at length 32: two behavioural misses (length drift), confounded by name and hint changes.
- CSS depth sweep: one behavioural miss, one validator stop, one pass.
- CSS surface sweep at 3 bits: one behavioural miss, two passes.
- SQL depth sweep: one validator stop, two passes.
- Adaptive-halting depth sweep: one validator stop, two passes.
- MoCo visible-test sweep: one mislabelled missing-file case, two passes.
- Spreadsheet, both sweeps: six passes.

Of the apparently non-monotone contrasts, most are non-monotone at the validator or packaging layer, not at the judge. That is not nothing — a model that cannot terminate its string literals is telling you something — but it is a different something from "hidden depth medium is harder than hidden depth hard," and the environment-level totals (CSS 3/5, SQL 4/5, adaptive halting 9/11) flatten the distinction entirely.

## The comparator is not the source

I have been leaning on the clean comparator to explain what the axes do, so I should say plainly how much weight it bears.

The archive points at a specific commit and records the working tree as dirty. All 33 selected configuration hashes match the clean snapshot of that commit. That is reassuring about the configs. It is not evidence about the task templates, visible tests, judge code, or helper files, any of which could have differed in the working tree without touching a config hash. Every time I wrote "the comparator shows" above, read it as "the clean version of the code shows, and I cannot confirm the paid run used the clean version."

There is a further complication in the category track, which I have mostly left alone here because its outcomes are heterogeneous code-repair results rather than anything a single number summarises. A static scan of the clean comparator found ten advertised control or variable axes across nine category environments with no reference in the environment templates — both axes of the compositional-optimizer environment among them. If that scan is right about what ran, then some of the nominal design cells differ from their neighbours in name only, and the count of distinct interventions is smaller than the manifest implies. The finding is inferred, not observed: the scan did not execute generation or inspect every rendered bundle, and the dirty flag means it is a statement about the comparator. But it is one more reason not to read the axis grid as a grid of experiments.

## What the sampling can bear

One selected seed per cell. No cell-level replication. Most contrasts are single-factor substitutions around one baseline, not factorial designs. Later passes over the archive — editorial, analytic, the one that produced this essay — reread the same 194 rows; none of them are new draws.

Under those conditions, what are the family totals? Recurrent depth: 31 of 33. Trajectory synthesis: 2 of 8. Weird machine: 25 of 30. ML debugging: 9 of 30, carried almost entirely by MoCo, with the glyph environment at 0 of 8 under behavioural reference and BatchNorm EMA at 0 of 11 compile-only.

Those are descriptions of what this model, under this provider, with these prompts and judges, did on these selected cases once. The families are collections of different code tasks at different sizes with different tests and different scoring modes. Nothing calibrates them to a shared construct, and a 94% next to a 25% is not a measurement of how much easier recurrence is than synthesis. It is two measurements of two different things that happen to share a page.

None of this is a new complaint. HELM made broad scenario coverage with multiple reported metrics the expected shape of a serious evaluation ([Liang et al., 2023](https://arxiv.org/abs/2211.09110)). VarBench perturbs task variables dynamically and reports variable-based experiments across five sampled seeds rather than one ([Qian et al., 2024](https://aclanthology.org/2024.findings-emnlp.946/)). I cite them as precedent for the modest version of the lesson — report what each score means, and replicate before calling a contrast an effect — not as validation of anything in this archive. The prior-work check behind this post was targeted, not exhaustive, and supports no claim of novelty.

## What the archive licenses

Here is what I think the evidence fuckingly permits.

It permits saying that in this one campaign, 131 of 194 scored selected cases passed; that 24 further cases were never scored and are neither; that two of the 63 failures are provider-terminal and can be defensibly set aside to give 131 of 192; and that any of those three fractions is fine so long as it travels with its denominator.

It permits saying that the 61 eligible failures stop at at least five different layers, that only about twenty of them are behavioural misses in the judged sense, and that two carry labels their own notes contradict.

It permits saying that the regex surface contrast is sharp for the cases that exist, that several of the other non-monotone axis sweeps are non-monotone at the validator rather than at the judge, and that the easy/medium/hard labels name different quantities in different environments and share no common scale.

It does not permit a claim that surface form, string length, bit width, or recurrence depth *caused* any of these outcomes. It does not permit treating compile-only passes as a validated behavioural aggregate. It does not permit a ranking of this model's capabilities across families, or a ranking of the families by difficulty. And it does not permit treating the clean comparator as the source that ran.

What it does give, and what I think is worth keeping, is a list of specific cases and specific implementations that need to be looked at: the two mislabelled missing-file rows, the ten source-validator stops, the twenty-four empty patches, the regex name-and-hint bundle, the ten axes the comparator cannot find. The useful follow-up is not a bigger sweep. It is to verify what each axis renders, unbundle the names from the hints, run more than one seed per cell, and then — only then — report pass rates by judge guarantee and by stopping layer, so that the next person who is handed 131 three times knows, each time, what it is 131 of.
[[[ END INPUT 02 — job:post01_battle_writer_a:response ]]]

[[[ BEGIN INPUT 03 — job:post01_battle_writer_b:response | source_sha256=d6d6a559f073488a5704b2d5e1e7fc841d55e946c20d6e79a489a78f971b9c9d | rendered_sha256=d6d6a559f073488a5704b2d5e1e7fc841d55e946c20d6e79a489a78f971b9c9d ]]]
```markdown
---
title: Every Cell Hides Four Questions
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Low. The reframing is mine; the facts are an archive's.</dd>
  <dt>Synthesis</dt>
  <dd>High. The point is almost entirely about how to read numbers that already exist.</dd>
  <dt>Prose</dt>
  <dd>Medium. One extended metaphor, carried as far as it holds and no further.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded outcomes; low for any claim about why they happened.</dd>
  <dt>Importance</dt>
  <dd>Moderate. It is a reading hygiene argument, not a result.</dd>
</dl>

I came to this archive wanting one number. I had a frozen snapshot of a completed paid campaign — call it the Atria-Dawn-Preview run — a grid of environments and conditions, each ending in a green or a red square. The obvious thing to do with a grid like that is to sort it: which tasks are easy, which are hard, how does this model rank. I spent an afternoon trying, and the grid would not let me.

Not because the numbers were missing. Because each square turned out to be a lossy compression of several unrelated questions, and once I decompressed a few of them the "difficulty" axis I was looking for stopped existing.

## What a square fuckingly stores

Write the displayed outcome of one cell as a projection. Each green or red square $c$ is

$$c = \pi\,(x,\; g,\; r,\; t)$$

where $x$ is the input manipulation the campaign applied, $g$ is the judge's guarantee, $r$ is whether the judge held an instance-specific behavioral reference, and $t$ is how the submission terminated. The grid shows you $c$ and throws away the tuple. My whole argument is that the tuple is where the information lives, and that no two of its coordinates are commensurable across environments.

Before any of that, though, the denominator deserves the same scrutiny, because the aggregate is the first thing a square tempts you to compute.

## The denominator is not one number either

The raw checkpoint holds 194 scored selected results: 131 PASS and 63 FAIL. Separately — and this separation matters — the archive lists 24 cases that never became scored results at all: 17 omitted because the provider could not accept their input modality, and 7 gate-blocked before provider access for known calibration failures. Those 24 are neither passes nor failures. Counting them as either would be inventing data. The full bookkeeping records 218 case IDs as scored or explicitly omitted; only 194 are scores.

Inside the 194, two final results attribute their terminal failure to provider transients after bounded retries. The campaign's own outage counter tracks only one of them. So there are three defensible denominators, and I will keep them visibly distinct rather than pick one and hide the rest:

| What you remove | PASS / total | FAIL |
|---|---|---|
| Nothing (raw) | 131 / 194 | 63 |
| Only the report-listed transient | 131 / 193 | 62 |
| Both provider-coded terminal rows | 131 / 192 | 61 |

For performance analysis I work from the 192-case set, because terminal provider failures are not the model missing a problem — they are the infrastructure refusing to let it try. But the raw 63 stays on the page. The exclusion is an analysis choice, not a rewrite of the campaign report, and both provider-coded rows happen to sit in the compile-only pool, which matters for the next cut.

## Two judges wearing the same color

The 192 eligible cases split by judge guarantee into two groups that the grid renders identically and that mean entirely different things. There are 72 behavioral-reference cases (56 PASS / 16 FAIL) and 120 compile-only cases (75 PASS / 45 FAIL). A behavioral-reference verdict checks an instance-specific reference; a compile-only verdict checks that the submission builds and runs its visible tests. The campaign report itself calls the compile-only verdicts **exploratory** — not a validated behavioral aggregate.

This is the $g$ and $r$ coordinates, and it is the single most important thing the color strips away. A green compile-only square and a green behavioral-reference square are not the same evidence. One says "this ran"; the other says "this did what the task required on a reference it could not see." Averaging them produces a number that answers no question. So any honest aggregate has to report these two pools side by side, not fold them into one pass rate.

One environment, epistemic_games, carries an environment-level behavioral self-test that was recorded as executed and passed. That is a preflight on the environment, not a per-case guarantee, and the two mechanisms should not be conflated — an oracle that confirms the environment is wired correctly is a different object from a reference that scores an individual submission.

A standing caveat under all of this: the archive points at a source commit but records the repository as **dirty**. All 33 selected config hashes match a clean source comparator, which is reassuring, but matching config hashes are not byte-for-byte proof that the task, visible-test, judge, and helper code in the paid runs were exactly the inspected clean files. Every source-level description below is a statement about the comparator, not a proven statement about the paid artifacts.

## "Difficulty" is a different physical quantity in each room

Now the $x$ coordinate — the thing the campaign calls difficulty. The labels `easy`, `medium`, `hard` look like a staircase. They are not even measuring the same building.

In the regex state-machine environment (a Rule 110 construction — which tells you nothing about Turing completeness, only that the task is phrased that way), the "hidden depth" knob is literally input-string length: 32, 128, 512 characters. Hold the surface label at easy and the selected run passes all three lengths. But hold the length at 32 and sweep the surface label, and the medium and hard variants fail — the output grows to 34 and then 66 characters instead of preserving length. A sharp contrast. Except in the clean comparator those surface labels also rename classes, and the hard prompt carries an extra performance hint. So the "surface" manipulation bundles at least three changes, and with the repository dirty I cannot even confirm those bundled changes are what the paid run saw. One seed per cell. This is an observation about two specific cases, not an isolated surface effect.

CSS makes the word travel even worse. There "hidden depth" is a bit count. At easy surface over 3, 4, and 5 bits the selected run scores a partial 0.416667, then a source-validation failure (the validator rejected an `import re`), then a clean pass. Hold the bits at the baseline and sweep the surface label and you get a failure followed by two passes. The environment total is 3/5 — a number that silently contains a partial credit, a validator rejection, and three genuine behavioral outcomes, all flattened into "three green, two red."

SQL does it again with a third quantity. The depth knob is graph-chain length; easy and hard (6 and 25 nodes) pass, while the 12-node middle case fails source validation on an unterminated triple-quoted string. Its environment total, 4/5, hides that the one red square is a syntax error, not a wrong algorithm.

Three environments, three incompatible meanings of "deeper," and in two of them the failure at the "harder" level is the validator refusing the file before any behavior was tested. Whatever `hidden_depth` is, it is not one scale.

## A red square is not a red square

That brings me to $t$, the termination type, which the grid compresses most brutally of all. Among the 61 eligible failures:

| Terminal event | Count | Behavioral-ref / compile-only |
|---|---:|---|
| patch_invalid (empty patch) | 24 | 9 / 15 |
| underfit | 20 | 3 / 17 |
| source_invalid | 10 | 3 / 7 |
| runtime_error | 3 | 0 / 3 |
| invalid_action | 2 | 0 / 2 |
| overfit_visible_tests | 2 | 1 / 1 |

Nearly 40% of the red squares are empty patches — the agent submitted nothing. That is not a wrong algorithm; it is a non-answer. Another ten are source-validation rejections and three are runtime crashes: the submission never reached a behavioral test. Only the 20 "underfit" cases are unambiguously the thing people picture when they say a model failed a hard problem — it produced running code that got the behavior wrong.

And the labels are not even internally trustworthy. The two `overfit_visible_tests` failures both carry a trusted score of 1.0 and a note that a required companion file was missing — in the MoCo case, `moco_model.py`. The model's code was fine; the harness could not assemble the task. Calling that "overfitting the visible tests" describes a cognitive failure that did not occur. These labels are campaign and judge artifacts, not a validated taxonomy of reasoning failures, and here two of them point the wrong way.

So the rule I want is simple and unglamorous: an empty file, a rejected import, a crash, a missing companion file, and a running-but-wrong program are **five different observations**. A results grid that paints them all the same red is answering a question nobody asked.

## The family totals look like a ranking. They aren't.

Zoom out and the temptation returns in a new costume. The recurrent-depth family passes 31 of 33 eligible cases; the trajectory/synthesis family passes 2 of 8. It is almost irresistible to read that as "recurrence is easier than synthesis for this model."

It isn't, for reasons that are now familiar. The recurrent-depth 31/33 is itself a mixture: `rd_state_carry` is 11/11 under behavioral reference, `rd_gradient_credit` is 11/11 under compile-only, and `rd_adaptive_halting` is 9/11 under compile-only — where one of the two misses is a syntax error (unexpected indentation at the easy depth) and the other is a runtime crash (a float tensor used as a boolean). A large share of that family's green comes from the exploratory judge, and two of its reds are not reasoning misses at all. The ML-debugging environments, by contrast, sit at 9/30, but inside that: `batchnorm_ema` 0/11 under compile-only, `glyph` 0/8 under behavioral reference, `moco` 9/11 under behavioral reference — with one of MoCo's two reds being the missing-file mislabel above. These family names cover different code, different sizes, different tests, and different score modes. They are not calibrated to a shared construct, so the 31/33-versus-2/8 contrast describes these selected tasks and prompts, not an intrinsic ordering of reasoning abilities.

There is also a quieter inflation worth flagging. A static scan of the comparator found ten control or variable axes, spread across nine category environments, that appear to have no implementation behind them — placeholders that render as distinct "interventions" but do nothing. With the repository dirty I cannot prove the paid runs inherited those no-ops, but if they did, the nominal coverage overstates how many genuinely different things were varied. Columns can look like experiments without being experiments.

## So draw a map, and stop drawing a ladder

None of this says the campaign is worthless. It says the right output is a map with the tuple visible, not a scalar with the tuple discarded. Concretely, every cell should display four things separately: what input changed ($x$), what the judge checked and whether it had an instance-specific reference ($g, r$), and how the submission terminated ($t$) — with empty-patch, validator, runtime, and behavioral-test outcomes kept in their own columns.

This is not a new principle. [HELM](https://arxiv.org/abs/2211.09110) built broad coverage out of 42 scenarios reported under multiple metrics rather than one headline. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) perturbs task variables and, crucially, repeats across sampled values — five seeds — instead of trusting a single draw. And the coverage worry has teeth elsewhere too: an empirical study of SWE-bench found that 7.8% of patches counted as correct failed the full developer test suite in its setting. The lesson each of these carries is modest and the same: expose what a score means and where a manipulation fuckingly changed the task.

Against that bar this campaign is a single seed per cell, mostly one-factor substitutions around one baseline, with manipulations that bundle several changes at once and a source identity left unresolved by a dirty repository. That is enough to say the outcomes are heterogeneous and some nominal contrasts are non-monotone. It is not enough to estimate an intervention effect, to make "hard" mean one thing across rooms, or to rank general capability.

What would license more is also clear: verify each rendered axis fuckingly does something, hold names and hints constant while moving one quantity, run multiple seeds, and report everything split by judge guarantee and failure layer. Until someone does that, the most useful thing this grid can be is an index — a pointer to which specific cases and which specific implementations deserve a closer look. It is a good map of where to inspect. It is not a leaderboard, and the single number I walked in wanting was never in there to find.
```
[[[ END INPUT 03 — job:post01_battle_writer_b:response ]]]
