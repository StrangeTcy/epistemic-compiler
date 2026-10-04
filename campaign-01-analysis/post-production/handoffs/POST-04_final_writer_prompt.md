# Final public-post writer — POST-04

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


POST-04 editorial-input note: the editorial-critic artifact is a compiler-assembled bundle of two separately labeled critiques, not a synthesized consensus or ranking. Reconcile their recommendations against the evidence packet; preserve the boundaries and do not reproduce internal critic labels in the public article.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post04_prepare_post:response | source_sha256=5660bc1bcd44eb95f5f7c39ed22b537d288b9f8790330240a56ff8c241249f31 | rendered_sha256=4742cf0dc42718d8625ad9eda2d193ec5a6822d66e34e2e5ff36d591d1e2e2d5 ]]]
# Compiler evidence packet — POST-04

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
# POST-04 — One score, six different ways to fail

**Dek:** In this archive, a zero can mean no patch, invalid source, a runtime crash, a failed behavioral test, a malformed action, or a provider outage. Treating all of them as one model failure hides the engineering story.

**Draft**

A campaign summary usually starts with a pass rate. This archive shows why the next question should be: *what exactly happened in each failed case?*

The raw checkpoint records 131 PASS and 63 FAIL across 194 scored cases. It separately lists 24 omissions: 17 unsupported `rope` cases and 7 cases blocked before provider access by calibration problems. Those omissions are not failures. The campaign report names one provider outage, but two final result files contain the terminal note “provider transient failure after bounded retries.” Removing only the report-listed row gives 131/193 PASS; excluding both final provider-coded rows gives 131/192 PASS and 61 eligible FAIL. All three counts matter because the report counter and the row-level terminal notes do not fully agree. Any implementation details below come from the clean source comparator; the campaign records `repository.dirty=true`, so this is not proof of the exact paid-run code. ⟦POST-04-C01 · F-01/F-02/F-03⟧

The 192-case analysis set is itself mixed: 72 cases are labeled `behavioral_reference`, while 120 are `compile_only`. The campaign report says compile-only verdicts are exploratory and excluded from a validated aggregate. That means 131/192 is bookkeeping across two judge modes—not a uniform accuracy estimate or a standalone model score. ⟦POST-04-C02 · F-04⟧

Among the 61 eligible failed cases, the recorded taxonomy contains 24 `patch_invalid`, 20 `underfit`, 10 `source_invalid`, 3 `runtime_error`, 2 `invalid_action`, and 2 `overfit_visible_tests`. Every `patch_invalid` final note says the patch file is empty. The source-invalid cases are syntax or disallowed-import rejections. The runtime errors are execution failures. These are different points in the pipeline, not six interchangeable ways of being conceptually wrong. ⟦POST-04-C03 · F-09⟧

Even a failure label can conceal the wrong event. Two cases are labeled `overfit_visible_tests`, but their final metrics give a trusted score of 1.0 and their notes say a required companion file is missing. The two provider-coded cases are both raw `invalid_action` rows, although the terminal note blames provider transients. Keeping those in the raw result is faithful to the archive; treating them as ordinary invalid model submissions is not. ⟦POST-04-C04 · F-03/F-09⟧

The track summary has a similar problem. All seven `epistemic_games` rows are assigned to `ml_debugging`, despite the inspected task core implementing Bayesian inference over policy tables. The recorded track total is 37 cases with 16 passes; separating the seven epistemic rows leaves 30 ML-debugging cases with 9 passes and 21 failures, and a distinct 7/7 epistemic result. The analysis preserves the original labels and adds a semantic regrouping instead of silently rewriting the archive. ⟦POST-04-C05 · F-05⟧

Prior work on test-based software-agent benchmarks makes the general warning familiar: a passing test suite is only as strong as the tests that ran. A recent SWE-bench study reported that 7.8% of plausible patches in its studied setting passed the benchmark validation while failing the full developer-written test suite. That rate is not an estimate for this campaign; it is context for why local judge contracts and exact artifacts matter. Here, the more direct evidence is already in the ZIP: 122 raw rows are compile-only, two “overfit” labels describe missing files, and several task/judge contracts differ in the inspected comparator. The archive also records `repository.dirty=true`, so comparator mismatches are not proof of the exact paid-run source. ([Study](https://dl.acm.org/doi/10.1145/3744916.3764576)). ⟦POST-04-C06 · F-01/F-04/F-09/F-15/F-17⟧

Telemetry adds another layer. The archive contains 268 run directories, including earlier and superseded attempts, and its retry counts differ by source: selected run manifests, API logs, checkpoint rows, and campaign progress do not reconcile. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows with a `reasoning_content` field. Those are metadata discrepancies, not evidence about cognition; no reasoning text is reproduced here. No spend field is present, so the archive cannot support a cost estimate. ⟦POST-04-C07 · F-13⟧

A better campaign dashboard would separate at least four layers: (1) whether the provider returned a usable response, (2) whether the agent emitted a valid action and nonempty patch, (3) whether the patch passed source/runtime checks, and (4) whether it satisfied independent behavioral tests. It would also retain raw verdicts, explicit exclusions, scoring mode, judge notes, and per-case artifacts. This is consistent with broader multi-metric evaluation practice, but the exact layers must fit the code-agent pipeline being measured. ([HELM](https://arxiv.org/abs/2211.09110)). ⟦POST-04-C08 · F-04/F-09/F-13/F-17⟧

The central result is not that scalar scores are useless. It is that a scalar should be the last line of a traceable evidence chain, not the first and only one. In this archive, the most informative questions concern empty patches, validator policy, required files, provider termination, and what each judge actually verifies. ⟦POST-04-C09 · F-09/F-13/F-16⟧

**Editor’s note:** Double-bracket tags are evidence keys. The exact per-case source paths and quantitative result are mapped in `claim_traceability.csv`.

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
POST-04 prior-work references from the source draft; context only, not validation of this campaign.

- You Wang, Michael Pradel, and Zhongxin Liu. “Are ‘Solved Issues’ in SWE-bench Really Solved Correctly? An Empirical Study.” The study reports that 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite in its studied SWE-bench Verified setting. This rate is not an estimate for the Atria campaign. https://dl.acm.org/doi/10.1145/3744916.3764576
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: a precedent for broad scenario and metric coverage, not a validation of this campaign. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim.

## Claim-to-finding map
post_id,claim_id,finding_ids
POST-04,POST-04-C01,F-01;F-02;F-03
POST-04,POST-04-C02,F-04
POST-04,POST-04-C03,F-09
POST-04,POST-04-C04,F-03;F-09
POST-04,POST-04-C05,F-05
POST-04,POST-04-C06,F-01;F-04;F-09;F-15;F-17
POST-04,POST-04-C07,F-13
POST-04,POST-04-C08,F-04;F-09;F-13;F-17
POST-04,POST-04-C09,F-09;F-13;F-16

## Relevant finding records
{"claim_ids":["POST-04-C01","POST-04-C02","POST-04-C03","POST-04-C04","POST-04-C05","POST-04-C06","POST-04-C07","POST-04-C08","POST-04-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign report records 194 scored selected cases and 24 separate pre-scoring omissions; the case manifest and result checkpoint contain the same 194 case IDs.","confidence":"HIGH.","id":"F-02","limitations":["The 7 gate-blocked and 17 unsupported cases have no model score and must not be counted as failures or passes.","A complete unfiltered planned-design file is not required to reproduce this report-level union."],"quantitative_result":"194/194 selected results have status scored across 33 environments; 17 rope cases are omitted for unsupported provider input modality and 7 cases are omitted before provider access for known calibration failures; 218 case IDs are recorded as scored or explicitly omitted.","status":"OBSERVED"},{"claim":"Two final selected results, not just the one named in the campaign-level outage counter, explicitly attribute their terminal failure to provider transients after bounded retries.","confidence":"HIGH that both final notes exist; MEDIUM that every terminal provider-coded row should be excluded from model-performance analysis, because the official campaign counter tracks only one episode.","id":"F-03","limitations":["The raw row remains scored and its raw failure label is retained; the 192 denominator is an explicit analysis exclusion, not a rewritten campaign report.","API error events also include transient retries that recovered; only final-result terminal notes define these two exclusions."],"quantitative_result":"Raw checkpoint: 131 PASS / 63 FAIL among 194. Removing only report-listed ts_trajectory gives 131/193 PASS and 62 FAIL. Removing both final-note provider cases gives 131/192 PASS and 61 FAIL.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The archive assigns all seven epistemic_games cases to the recorded ml_debugging track, although the inspected task core implements symbolic Bayesian inference.","confidence":"HIGH for recorded label; HIGH that task semantics are symbolic Bayesian inference in the comparator; MEDIUM for whether the recorded grouping was intentionally multi-purpose.","id":"F-05","limitations":["The analysis_family override is an explicit editorial regrouping; the raw track is preserved unchanged.","A dirty source tree limits claims about the exact executed task code."],"quantitative_result":"Recorded track summary: ml_debugging 37 cases, 16 PASS/21 FAIL. Source-semantic regrouping: 30 ML-debugging cases, 9 PASS/21 FAIL; epistemic_games separate at 7/7 PASS.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"After removing the epistemic_games track-label anomaly, the three selected ML-debugging environments show 9/30 PASS, with highly uneven task outcomes.","confidence":"HIGH for per-environment result counts and notes; MEDIUM for using the three tasks as a coherent ML-debugging construct.","id":"F-12","limitations":["Only three environment families are grouped here; one has compile-only judgments.","One seed and one selected response per case; no general ML-debugging inference."],"quantitative_result":"batchnorm_ema 0/11 (compile_only), glyph 0/8 (behavioral_reference), moco 9/11 (behavioral_reference); the two MoCo/BatchNorm rows labeled overfit_visible_tests have notes about missing required companion files.","status":"OBSERVED"},{"claim":"The archive contains incompatible retry counters and a reasoning-mode metadata discrepancy; usage or retry totals should not be collapsed into a single canonical value.","confidence":"HIGH that the archived counters/fields disagree; LOW about the underlying cause.","id":"F-13","limitations":["No spend/cost field exists in the exported archive.","No reasoning content is copied or interpreted; presence counts are metadata only."],"quantitative_result":"All 268 runs: 4,061 successful responses, 4,023 summed run/turn IDs, 9,447,242 successful-response tokens. `reasoning_enabled=false` coexists with 325,785 reported reasoning tokens and 2,710 rows containing a reasoning_content field. Retry counts range by source/scope from 3,869 selected final-manifest attempts to 6,412 progress-reported attempts.","status":"OBSERVED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-04","schema_version":1,"trace_finding_ids":["F-01","F-02","F-03","F-04","F-05","F-09","F-13","F-15","F-16","F-17"]}

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

## Evidence Case Results Post-04
case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
architecture_naturality,5,5,5,0,1.0,0,0,0,5,5,0
batchnorm_ema,11,11,0,11,0.0,0,0,0,11,0,11
categorical_lenses,5,5,4,1,0.8,5,4,1,0,0,0
ci_dependency_graph,5,5,5,0,1.0,5,5,0,0,0,0
compositional_optimizer,5,5,3,2,0.6,0,0,0,5,3,2
css_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0
equivariant_diagram,5,5,5,0,1.0,0,0,0,5,5,0
functorial_augmentation,5,5,2,3,0.4,0,0,0,5,2,3
glyph,8,8,0,8,0.0,8,0,8,0,0,0
gnn_message_passing,5,5,0,5,0.0,0,0,0,5,0,5
moco,11,11,9,2,0.8181818181818182,11,9,2,0,0,0
monadic_reward,5,5,1,4,0.2,0,0,0,5,1,4
neuro_symbolic_parser,5,5,4,1,0.8,0,0,0,5,4,1
rd_adaptive_halting,11,11,9,2,0.8181818181818182,0,0,0,11,9,2
rd_gradient_credit,11,11,11,0,1.0,0,0,0,11,11,0
rd_state_carry,11,11,11,0,1.0,11,11,0,0,0,0
regex_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
semiring_unification,5,5,5,0,1.0,0,0,0,5,5,0
sheaf_invariant_gluing,5,5,5,0,1.0,0,0,0,5,5,0
sheaf_physical_constraints,5,4,0,4,0.0,0,0,0,4,0,4
sheaf_schema_sync,5,5,1,4,0.2,0,0,0,5,1,4
spreadsheet_dataflow,5,5,5,0,1.0,5,5,0,0,0,0
sql_fixed_point,5,5,4,1,0.8,5,4,1,0,0,0
ssm_parallel_scan,5,5,5,0,1.0,0,0,0,5,5,0
stochastic_monad,5,5,5,0,1.0,0,0,0,5,5,0
template_interpreter,5,5,5,0,1.0,5,5,0,0,0,0
tensor_functor,5,5,2,3,0.4,0,0,0,5,2,3
tokenizer_adjunction,5,5,5,0,1.0,0,0,0,5,5,0
transformer_ssm_lift,5,5,5,0,1.0,0,0,0,5,5,0
ts_one_step,3,3,0,3,0.0,0,0,0,3,0,3
ts_parse_only,3,3,2,1,0.6666666666666666,0,0,0,3,2,1
ts_trajectory,3,2,0,2,0.0,0,0,0,2,0,2

## Selected failure details
environment,condition,judge,score,failure,detail
batchnorm_ema,optimizer_hint=easy_red_herring=medium_visible_tests=easy_data_complexity=easy_symptom_mask=easy,compile_only,0.95,overfit_visible_tests,required companion file missing: train.py; trusted_score=1.0 despite failed terminal label
categorical_lenses,naming=easy_symptom_mask=hard,behavioral_reference,0.0,source_invalid,
compositional_optimizer,naming=medium_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import weakref
css_state_machine,surface_deceptiveness=easy_hidden_depth=easy,behavioral_reference,0.416667,underfit,
css_state_machine,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source validator rejected import re
functorial_augmentation,naming=easy_symptom_mask=easy,compile_only,0.416667,underfit,
functorial_augmentation,naming=hard_symptom_mask=easy,compile_only,0.416667,underfit,
functorial_augmentation,naming=medium_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=hard,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=medium,compile_only,0.416667,underfit,
gnn_message_passing,naming=hard_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=medium_symptom_mask=easy,compile_only,0.416667,underfit,
moco,naming=easy_distractors=easy_queue_math=easy_temperature=easy_visible_tests=medium_symptom_mask=easy,behavioral_reference,0.95,overfit_visible_tests,required companion file missing: moco_model.py temperature_cancelled; trusted_score=1.0 despite failed terminal label
monadic_reward,naming=easy_symptom_mask=hard,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=easy_symptom_mask=medium,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=hard_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=medium_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import ast
neuro_symbolic_parser,naming=hard_symptom_mask=easy,compile_only,0.0,underfit,
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=easy_batching_complexity=easy,compile_only,0.0,source_invalid,source syntax error: unexpected indentation
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=medium_batching_complexity=easy,compile_only,0.0,RUNTIME_ERROR,runtime error: float tensor used as a boolean condition
regex_state_machine,surface_deceptiveness=hard_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 66"
regex_state_machine,surface_deceptiveness=medium_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 34"
sheaf_physical_constraints,naming=easy_symptom_mask=hard,compile_only,0.277778,underfit,
sheaf_physical_constraints,naming=medium_symptom_mask=easy,compile_only,0.277778,underfit,
sql_fixed_point,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source syntax error: unterminated triple-quoted string
tensor_functor,naming=easy_symptom_mask=hard,compile_only,0.0,underfit,
tensor_functor,naming=easy_symptom_mask=medium,compile_only,0.0,underfit,
tensor_functor,naming=medium_symptom_mask=easy,compile_only,0.0,underfit,
ts_one_step,witness_status=broken_representation=flat,compile_only,0.2857142857142857,underfit,
ts_one_step,witness_status=broken_representation=reflective,compile_only,0.0,source_invalid,source syntax error: unterminated triple-quoted string
ts_one_step,witness_status=valid_representation=flat,compile_only,0.7142857142857143,underfit,
ts_parse_only,witness_status=broken_representation=reflective,compile_only,0.5,underfit,
ts_trajectory,witness_status=broken_representation=flat,compile_only,0.0,runtime_error,
ts_trajectory,witness_status=valid_representation=flat,compile_only,0.0,runtime_error,

## Failure taxonomy
failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"
[[[ END INPUT 01 — job:post04_prepare_post:response ]]]

[[[ BEGIN INPUT 02 — job:post04_battle_writer_a:response | source_sha256=4366932de5467426271d19c4ef154cb81b26a3734f81717cfbe3aa09716e8a21 | rendered_sha256=4366932de5467426271d19c4ef154cb81b26a3734f81717cfbe3aa09716e8a21 ]]]
---
title: "Whose Zero Is It?"
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt><dd>Low to moderate. Breaking a pass rate down by pipeline stage is standard practice. What this post adds is one specific attribution exercise on one frozen archive.</dd>
<dt>Synthesis</dt><dd>Moderate. Most of the work is reconciling row labels, terminal notes, judge modes, and telemetry counters that don't fully agree.</dd>
<dt>Prose</dt><dd>A language model wrote this in the Arena pipeline, working from an audited evidence packet and an earlier source draft. Later editorial and model passes are revisions of one analysis. They are not independent replications of it.</dd>
<dt>Certainty</dt><dd>High for the archived counts, labels, and notes quoted here. Low for anything about why a given output was produced.</dd>
<dt>Importance</dt><dd>Moderate as a reporting lesson. Low as a statement about model capability. The data is one campaign with one seed per cell.</dd>
</dl>

Here's a question I couldn't answer about a campaign I thought I understood: of the cases that failed, how many failed because of the model?

That should be easy. The archive is a completed paid run with a result checkpoint, a failure label on every row, and a campaign report on top. But the more carefully I read it, the less the question meant. A FAIL row isn't a statement about the model. It says that *something*, somewhere between the provider's API and the hidden judge, didn't reach the end. Which something it was is recorded, if at all, in a free-text note that no summary table ever reads.

So this post isn't about the pass rate. It's about **attribution**: for each zero, whose zero is it?

## First, who gets a row at all

Before attribution there's admission. The checkpoint holds **194 scored cases: 131 PASS, 63 FAIL.** That's the raw record, and I'm not going to edit it.

There are also **24 cases that never got a row.** Seventeen `rope` cases were dropped because the provider didn't support their input modality. Seven were blocked before any provider call because of known calibration failures. None of these cases were scored. Counting them as failures would charge the model for tasks it never saw. Counting them as passes would be absurd in the other direction. They sit outside every denominator below.

Then there's a disagreement inside the scored set. The campaign-level outage counter names one provider failure, but two final result files carry the terminal note that the failure came from a provider transient after bounded retries. Where should those two rows go?

I don't think the archive settles it, so I keep all three readings:

| View | What's removed | PASS / FAIL |
|---|---|---|
| Raw checkpoint | nothing | 131 / 63 of 194 |
| Report-consistent sensitivity set | the one outage the report counter names | 131 / 62 of 193 |
| Analysis set | both rows with provider-terminal notes | 131 / 61 of 192 |

The 192 set is my explicit exclusion, not a corrected campaign report. The two excluded rows stay scored in the raw archive with their original labels. Everything below uses 192 unless I say otherwise.

One more admission caveat applies to every sentence about task or judge code in this post. The archive records `repository.dirty=true`. All 33 selected config hashes match a clean source comparator, but matching configs aren't proof that the executed task, test, and judge code were the clean code. When I describe what a judge checks, I'm describing the comparator.

## FAIL is a sum type that got cast to a bool

My first plan was to compute a "model-attributable failure rate": take the 61 failures, drop the obviously infrastructural ones, and divide what's left by 192.

That plan was wrong, and the reason it was wrong is the point of this post.

Each failure label really names a variant of a tagged union, something like

$$
\textsf{Outcome} \;=\; \textsf{ProviderDied} + \textsf{NoPatch} + \textsf{RejectedSource} + \textsf{Crashed} + \textsf{JudgeSaidNo}(s) + \textsf{Pass},
$$

and the scoreboard applies $\textsf{isPass} : \textsf{Outcome} \to \{0,1\}$, which throws away the tag. You can't recover the tag from the bool. Worse, the two judge modes in this archive (more on them below) mean $\textsf{JudgeSaidNo}$ isn't one variant but two, with different guarantees. So even after I strip out the infrastructure failures, what's left isn't one homogeneous quantity I can divide by 192.

So let me read the tags instead.

## Walking the gates

In the 192-case set, the 61 failures carry these recorded labels:

| Recorded label | Count | Behavioral-reference | Compile-only | Where it stopped |
|---|---:|---:|---:|---|
| `patch_invalid` | 24 | 9 | 15 | patch file was empty (every final note says so) |
| `underfit` | 20 | 3 | 17 | judge scored the submission below passing |
| `source_invalid` | 10 | 3 | 7 | syntax error or disallowed import, before execution |
| `runtime_error` | 3 | 0 | 3 | executed and crashed |
| `invalid_action` | 2 | 0 | 2 | action rejected as malformed |
| `overfit_visible_tests` | 2 | 1 | 1 | see next section; the label doesn't match the note |

Read the last column top to bottom and you get a pipeline. Something has to come back from the provider. The agent has to emit a well-formed action carrying a non-empty patch. The patch has to parse and pass the source validator's import policy. It has to run. Only then does a judge decide whether it's *right*.

The `source_invalid` notes make the layering concrete. Four `monadic_reward` cases were rejected for importing `ast`. One `compositional_optimizer` case was rejected for `weakref`, and one `css_state_machine` case for `re`. Others died on syntax: an unterminated triple-quoted string (once in `sql_fixed_point`, once in `ts_one_step`) and an unexpected indentation in `rd_adaptive_halting`. The `runtime_error` rows include an `rd_adaptive_halting` case that used a float tensor as a boolean condition, plus two `ts_trajectory` runtime failures.

These events aren't all the same kind. A syntax error is plausibly the model's output being broken. A rejected `import ast` is a collision between the output and a validator policy. Whether that counts as a model error depends on whether the policy was stated to the agent, and this archive doesn't answer that. An empty patch says nothing reached the validator. From the label alone I can't tell whether the agent emitted nothing or something got lost between the agent and the patch file. All of them score 0, but they belong to different owners.

Now the number that changed my mind. **The behavioral-reference slice has 16 failures. Nine are empty patches, three are source rejections, one is the mislabeled "overfit" case, and only three are `underfit`.** Those three are the only rows where an independent behavioral judge ran on a submission and found it wanting. The notes on two of them are specific: `regex_state_machine` outputs of length 66 and 34 where the input had length 32.

So in the slice with the strongest judge guarantee, three of sixteen failures look like what people mean by "the model got the task wrong." The other thirteen stopped earlier. I'm not claiming the model is blameless for those thirteen. An empty patch may well be the agent's doing. But I can't say that from these labels, so the honest move is to leave the attribution open rather than default it to the model.

The `underfit` label is also less uniform than it looks. Seventeen of its twenty rows are compile-only, which means "underfit" there means something different (next section but one). And `failure_mode` is a campaign/judge label, not a validated taxonomy of cognitive mechanisms. It tells you where a row stopped, not why.

## When the tag itself is wrong

Two rows go further. Their labels don't just hide the event; they point at the wrong event.

**The two "overfits."** `overfit_visible_tests` sounds like the most interesting failure in the set: a model fitting the visible tests rather than the problem. Both rows so labeled have `trusted_score=1.0`. Both final notes say a required companion file is missing: `train.py` in one `batchnorm_ema` case, `moco_model.py` in one `moco` case (the latter note also mentions `temperature_cancelled`). Whatever happened there, the notes describe a packaging or contract failure, not overfitting. The label is the only evidence for overfitting, and the label is contradicted by its own row.

**The two provider-terminal rows.** These are the rows I removed to get from 194 to 192. In the raw archive, both are labeled `invalid_action`. Read naively, that's two cases of the model emitting malformed output. Their final notes say the terminal failure was a provider transient after bounded retries. So I hold both facts at once: the raw label is `invalid_action`, and it stays. The terminal note points to the provider, and that's why the rows sit outside the analysis denominator. What I won't do is describe them as ordinary model-format failures. (The *other* two `invalid_action` rows, both compile-only, are inside the 61 and have no such note. They're a separate pair.)

If a single row can carry a label that inverts its own note, then any aggregate built from labels inherits the inversion. That can't be fixed at the top of the stack, only row by row.

## Two judges, two promises

The 192 rows weren't graded under one contract. **72 are `behavioral_reference`: 56 PASS, 16 FAIL. 120 are `compile_only`: 75 PASS, 45 FAIL.** The campaign report itself calls compile-only verdicts exploratory and excludes them from any validated aggregate. (In the raw 194, compile-only is 122 rows at 75/47. Both provider-terminal rows were compile-only.)

So "131/192" isn't an accuracy. It's a sum across two guarantees, and one of them is explicitly not validated behavior. If you want a validated behavioral figure from this archive, it's 56 of 72. Even that is one seed per cell across a handful of environments, not a population estimate.

Why does the guarantee matter so much? Because a test only certifies what it executes. The comparator gives specific reasons to be careful even where judges did run. In the comparator, the compositional-optimizer prompt promises nested associativity across multiple steps, but its judge checks shape and one state-isolation chain. The physical-constraints judge enforces a 5:3 ratio the task never states. The categorical-lens hidden judge checks the laws but doesn't itself assert the coordinate-zero view, though the visible test does. These are comparator observations from a dirty-repo campaign, so they don't prove what the paid run executed, and they don't show that every category task is under-specified. They do show that "the judge said FAIL" and "the task was failed" can come apart in both directions.

Outside this archive, the gap has been measured. A [SWE-bench empirical study](https://dl.acm.org/doi/10.1145/3744916.3764576) found that, in its studied SWE-bench Verified setting, 7.8% of plausible patches counted as correct by benchmark validation failed the full developer-written test suite. That's a fact about that setting, not a rate for this campaign. I cite it only to show the problem isn't hypothetical.

## Tracks are tags too

The same attribution problem shows up one level up. All seven `epistemic_games` rows are recorded under the `ml_debugging` track. In the comparator, that task's core is Bayesian inference over stipulated policy tables. That's a well-defined inference problem, but it isn't ML debugging, and it isn't recursive theory of mind either.

The recorded track total stays as recorded: `ml_debugging` has **37 cases, 16 PASS / 21 FAIL.** As a separate analysis view, not an edit to the archive, I split it:

- the three ML-debugging environments: **9 PASS / 21 FAIL of 30**
- `epistemic_games`: **7 / 7 PASS**

Even the 30 aren't one thing. `moco` is 9/11 under behavioral-reference judging, `glyph` is 0/8 under behavioral-reference, and `batchnorm_ema` is 0/11 under compile-only. The recorded 16/37 blends a perfect inference slice into a debugging slice whose own environments range from 0% to 82% under different judges. The blended number describes none of them.

## Telemetry that won't settle on one number

Below the results sits the run telemetry, and it doesn't reconcile either. The archive has 268 run directories, including superseded attempts. Retry counts depend on where you look: 3,869 attempts in the selected final manifests, 6,412 in campaign progress, with API logs and checkpoint rows disagreeing in between. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a `reasoning_content` field.

I treat all of this as **metadata discrepancy**: counters and flags that disagree across export scopes, cause unknown. It's not evidence about what the model did internally. I reproduce no reasoning text and infer nothing from the field's presence. There's also no spend field anywhere in the export, so the archive can't support a cost estimate, and I won't make one.

## What a row should carry

If the question is "whose zero is it?", then a row needs enough structure to answer it. The minimum for a code-agent pipeline like this one looks like:

```
provider:  usable response?          → else infrastructure
action:    valid action, non-empty patch?  → else agent/harness (needs artifact to split)
source:    parses, passes import policy?   → else output vs. stated policy
runtime:   executes?                  → else output (usually)
judge:     which guarantee, which verdict, which note?
```

Alongside that, the row keeps the raw verdict, any explicit exclusion and its reason, the scoring mode, the judge's note, and the artifact itself. Nothing here is new as a principle. [HELM](https://arxiv.org/abs/2211.09110) made the broad argument for many scenarios and many metrics over a single number. But the specific layers have to match the machine being measured, and for an agent that edits files and submits them to a validator, these are where it can stop.

## What this licenses

The archive supports a **descriptive map**. Results vary sharply by environment, from 2/8 eligible passes in trajectory synthesis to 31/33 in the recurrent-depth family, under judge guarantees that differ case to case. In the 192-case set, the 61 failures span at least six recorded stopping points. In the behavioral-reference slice, only 3 of 16 failures are the `underfit` kind closest to a behavioral miss. Two "overfit" labels describe missing companion files with a trusted score of 1.0. Two `invalid_action` rows have terminal notes blaming the provider. One recorded track bundles an unrelated inference task.

It does **not** support a general capability ranking, a common difficulty scale across environments, or causal claims about any difficulty axis. There's one selected seed per cell and no replication. The repository was dirty. Two grading contracts are stitched into one table, and the compile-only half is exploratory throughout. Validator rejections, runtime crashes, harness contract misses, judge-label mismatches, and provider outages are failures of different parts of the apparatus. I've tried to keep each one apart from the thing people actually want to measure.

A pass rate can still go at the bottom of the page. It just has to be computed last, from rows that still carry their tags. In this archive the tags are where the answer is, and for most of the zeros, the answer to "whose zero is it?" is still open.
[[[ END INPUT 02 — job:post04_battle_writer_a:response ]]]

[[[ BEGIN INPUT 03 — job:post04_battle_writer_b:response | source_sha256=9c5e5fbfcaa2b51d59e27493bc5ab705be6b020df3502d78d7a338ce2bf706e1 | rendered_sha256=9c5e5fbfcaa2b51d59e27493bc5ab705be6b020df3502d78d7a338ce2bf706e1 ]]]
---
title: "A Verdict Needs Provenance"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The article frames the campaign verdicts as provenance-bearing records: their meaning depends on which stage of the evaluation produced them.</dd>
  <dt>Synthesis</dt>
  <dd>Analysis of the supplied campaign archive, with the SWE-bench study and HELM used only as context.</dd>
  <dt>Prose</dt>
  <dd>Produced through the Arena writing process from supplied artifacts; subsequent editorial/model-role passes are review steps, not independent experimental replications.</dd>
  <dt>Certainty</dt>
  <dd>High for recorded counts and terminal notes; limited for claims about exact paid-run code or latent model behavior because the repository was recorded dirty.</dd>
  <dt>Importance</dt>
  <dd>Useful for separating provider, artifact, validator, runtime, and judge outcomes before interpreting an aggregate score.</dd>
</dl>

A PASS in a code-agent campaign is not a property of a model in isolation. It is the recorded endpoint of a path through a provider, an action format, a patch artifact, a validator, a runtime, and a judge. A single verdict compresses that path. A FAIL compresses it too, even when the event was an empty patch, a rejected import, a crash, a missing file, or a provider transient.

That distinction changes how I read the Atria-Dawn-Preview archive. The headline counts are real records, but they do not all answer the same question. The useful result is not a new scalar for general ability; it is a more careful map of what was counted, which checks ran, and where some evaluations stopped.

## The denominator is an audit choice

The raw checkpoint records 194 scored rows: 131 PASS and 63 FAIL. Separately, the campaign records 24 omissions: 17 `rope` cases unsupported by the provider’s input modality, and 7 cases blocked by calibration problems before provider access. Those 24 have no model score. They belong in an account of the campaign, but not in its pass or fail totals.

There is also a discrepancy between the campaign-level outage counter and the final result notes. The report lists one provider outage. Two final selected results, however, end with notes attributing terminal failure to provider transients after bounded retries. Both rows remain in the raw checkpoint and both carry the raw label `invalid_action`. Keeping that label is faithful to the record; treating it as proof of an ordinary model-format failure is not.

These distinctions give us three related views:

| View | Scored rows | PASS | FAIL | What the view represents |
|---|---:|---:|---:|---|
| Raw checkpoint | 194 | 131 | 63 | All selected scored rows, including provider-terminal rows |
| Single-provider-exclusion sensitivity set | 193 | 131 | 62 | Removes the one row named by the campaign-level outage counter |
| Two-provider-exclusion analysis set | 192 | 131 | 61 | Excludes both rows whose final notes attribute termination to provider transients |
| Separate omissions | 24 | — | — | Unscored cases; neither passes nor failures |

The 193- and 192-row sets are sensitivity views, not replacements for the raw checkpoint. The first follows the report’s single-outage count; the second follows both row-level terminal notes. The omitted cases are separate from both. A trustworthy summary should show these choices rather than silently selecting the denominator that makes its headline easiest to read.

## The same numerator crosses two judge modes

Even the 192-row analysis set does not have one uniform scoring contract. It contains 72 cases labeled `behavioral_reference` and 120 labeled `compile_only`. In the behavioral-reference group, 56 passed and 16 failed. In the compile-only group, 75 passed and 45 failed.

Before the two provider exclusions, the raw 194 rows comprise 72 behavioral-reference cases and 122 compile-only cases; their respective results are 56/16 and 75/47. The exclusions leave the behavioral-reference count unchanged and reduce compile-only to 120 cases, with 75 passes and 45 failures. Together, those results yield the 131 PASS and 61 FAIL in the 192-row set.

That arithmetic is correct, but it does not turn 131/192 into a validated behavioral accuracy estimate. The campaign report describes compile-only outcomes as exploratory and excludes them from a validated aggregate. A pass under that mode is not interchangeable with a pass under a behavioral-reference judge. Combining the modes answers a bookkeeping question—how many recorded rows passed under their respective checks—not a common question about how often the agent produced behaviorally correct repairs.

This is why a judge-guarantee label should travel with the score. The count matters; so does the condition under which a pass was granted. And because there is one selected seed per case, these rows do not provide within-cell replication. Editorial or model-role passes over the archive do not add new experimental runs.

## Failure labels mark different boundaries

The 61 failures in the 192-row set divide into six recorded categories. The table keeps the judge modes visible because most of the categories span both, while some appear only under compile-only scoring.

| Recorded failure label | Count | Behavioral-reference / compile-only | What the record supports |
|---|---:|---:|---|
| `patch_invalid` | 24 | 9 / 15 | Every final note says the patch file is empty |
| `underfit` | 20 | 3 / 17 | A recorded score or judge shortfall, not a diagnosis of internal reasoning |
| `source_invalid` | 10 | 3 / 7 | Syntax errors or imports rejected by the source validator |
| `runtime_error` | 3 | 0 / 3 | Execution failures |
| `invalid_action` | 2 | 0 / 2 | Two compile-only failures in this analysis set |
| `overfit_visible_tests` | 2 | 1 / 1 | Labels that conflict with the final notes and metrics |

The table is a ledger of terminal results, not a taxonomy of cognitive mechanisms. An empty patch is an absent artifact. A validator rejection is an interaction with a source policy. A runtime error occurs during execution. An underfit label records a shortfall according to a judge; it does not, by itself, identify why the code fell short. Treating all four as evidence of the same kind of behavioral mistake would make the data less informative.

The `invalid_action` label particularly needs its boundary stated. The two `invalid_action` failures in the table belong to the 192-row taxonomy. Separately, two raw rows also carry that label but are excluded from the 192-row set because their final notes attribute terminal failure to provider transients. Those provider-terminal rows are not the two compile-only entries in the table. The same raw string occurs in different evidentiary situations; it cannot settle which event happened.

The two `overfit_visible_tests` rows show a different kind of mismatch. One is in `batchnorm_ema`, one in `moco`. Their final notes say a required companion file is missing—`train.py` in one case and `moco_model.py` in the other—and the metrics report `trusted_score=1.0`. One row is behavioral-reference and one compile-only. The record does not resolve whether the problem lies in output packaging, the judge’s requirements, or some interaction between them. It does show why the label alone is insufficient: these are not straightforward evidence of overfitting.

## A judge is part of the measured system

The source-comparator audit makes that point concrete. In `compositional_optimizer`, the prompt promises nested associativity and multiple steps, while the inspected judge checks tensor shape and a state-isolation chain. In `sheaf_physical_constraints`, the inspected judge enforces a 5:3 ratio that is not stated in the prompt. These are observations about the clean source comparator, not proof that the paid run used precisely that task and judge code.

The qualification matters. The archive records that its repository was dirty. All 33 selected configuration hashes match the clean comparator, but matching configuration hashes do not establish byte-for-byte identity for every task, visible test, judge, or helper. The comparator can point to contracts worth investigating; it cannot remove uncertainty about the exact paid-run implementation.

This is not a reason to dismiss behavioral tests. It is a reason to specify what they establish. A study of SWE-bench Verified reported that 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite in that studied setting. That figure is not an estimate for this campaign; it is a bounded reminder that passing one validation regime need not imply passing a broader one. 

The same caution applies when scores are grouped by track. All seven `epistemic_games` rows retain their recorded `ml_debugging` track label. That recorded track contains 37 cases, with 16 passes and 21 failures. As a separate analysis view—not a rewrite of the archive—one can distinguish those seven rows from the other 30: the latter have 9 passes and 21 failures, while `epistemic_games` is 7/7.

The inspected task core for `epistemic_games` implements symbolic Bayesian inference over stipulated policies, not recursive theory of mind. That semantic distinction helps explain why an analyst might report the rows separately, but it does not authorize changing their archived labels. Nor does 7/7 establish a general capability: the task group is small, selected once per case, and its exact paid-run source identity remains subject to the dirty-repository caveat.

## Metadata can establish a discrepancy, not a thought

The archive’s telemetry presents another temptation to overinterpret. It contains 268 run directories, including earlier and superseded attempts. Retry counts vary by source and scope, from 3,869 selected final-manifest attempts to 6,412 progress-reported attempts. Those values do not reconcile into one canonical retry count.

The configuration records `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a `reasoning_content` field. This establishes a metadata discrepancy. It does not establish what the model internally did, why it produced a particular patch, or which configuration fuckingly governed every recorded response. No reasoning text is reproduced here. The archive also has no spend field, so it cannot support a cost estimate.

A good evaluation report should preserve such discrepancies as discrepancies. Choosing one telemetry field as definitive without a reconciliation would turn uncertain metadata into a confident story. The same principle applies to verdicts: keep the raw label, the terminal note, and the analysis decision distinct enough that readers can see what each one contributes.

## Put the boundary in the report

I would keep a single score as a summary, but only after the report has made the scoring path inspectable. At minimum, each row should preserve the raw verdict, any exclusion and its reason, the judge-guarantee label, whether an action and nonempty patch were produced, the validator outcome, the runtime or tool outcome, and the judge’s final note. The report should identify missing required artifacts separately from behavioral-test failures.

Then aggregate within documented scoring modes before offering a combined count. Show compile-only outcomes as exploratory, not as validated behavioral results. Keep provider-terminal cases in the raw results while making any provider-exclusion sensitivity set explicit. Retain task and judge provenance, especially when the inspected source is only a comparator. A broad, multi-scenario and multi-metric approach such as HELM offers relevant precedent for resisting a single-metric view; it does not validate this archive or supply a universal score for code agents. 

The payoff is not a more elaborate scoreboard. It is a report in which a reader can tell whether a zero followed an empty artifact, a source-policy rejection, an execution failure, a judge decision, or a provider termination—and can tell when the archive does not resolve the cause.

This campaign licenses a descriptive account of its recorded outcomes under specific configurations and judge modes. It does not establish causal effects for task variations, a common difficulty scale, or a general capability ranking. Its category-track totals are heterogeneous code-repair outcomes, not a theorem or a calibrated scalar. With one selected seed per case and unresolved source-identity questions, the careful conclusion is narrower: these rows show what happened according to the recorded checks, while leaving open what a different run, judge, or implementation would have shown.
[[[ END INPUT 03 — job:post04_battle_writer_b:response ]]]

[[[ BEGIN INPUT 04 — job:post04_editorial_critic:response | source_sha256=2e1005b125d17adb69a47714ea204fa656f867b03a196e0d665bf8da8e5da97e | rendered_sha256=2e1005b125d17adb69a47714ea204fa656f867b03a196e0d665bf8da8e5da97e ]]]
# POST-04 editorial critic response bundle

Compiler-assembled wrapper containing two separately labeled user-supplied critiques. The bodies are preserved verbatim; this file does not claim consensus or select a critic.

## Critic response 1 — grok 4.3

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

## Critic response 2 — sonnet 4.6

# Editorial Blueprint — POST-04

---

## 1. Conceptual Structure and Thesis

**What the real argument is**

Both drafts establish that a scalar FAIL is a lossy encoding of a pipeline event. Writer A frames this as an attribution problem ("whose zero is it?") organized around a tagged-union metaphor. Writer B frames it as a provenance problem ("a verdict needs provenance") organized around audit procedure. Neither framing is wrong, but neither is as sharp as the evidence allows.

The argument the evidence actually supports is more specific: **a scalar verdict is a lossy projection of a pipeline event, and the loss is not symmetric.** Different stopping points — provider termination, absent artifact, validator rejection, runtime crash, behavioral miss — implicate different owners, require different fixes, and cannot be recovered from the bool. The archive doesn't just illustrate this generically; it contains rows where the recorded label actively inverts its own terminal note. That inversion is the sharpest version of the claim.

The thesis should say so directly: not "scalar scores are insufficient" (too familiar) but "the label and the event can point in opposite directions, which means any aggregate built from labels inherits the inversion." The evidence for this is specific and traceable.

**What should move or be cut**

- Writer A's tagged-union equation. It restates in notation what the table and prose already say more clearly. Drop it. If the final writer wants a compact formalization, the pipeline-gate list at A's "What a row should carry" section does more work without the overhead.
- Both drafts' prescriptive "what a row should carry" checklists. These are design-doc register, not argument. The prescription should be one or two sentences integrated into the closing, not a fenced code block or a bullet list.
- The blended "what this licenses / doesn't license" lists at the end of both drafts are solid but too long. They read like a hedge hedge hedge pattern. One tight paragraph is enough; the unlicensed claims don't all need individual enumeration.
- B's "Put the boundary in the report" section title is accurate but dull. Its content is important; its structure as a separate section inflates the post past where the argument runs out.

**Where the structures diverge**

A has a narrative arc with a turning-point moment ("the number that changed my mind"), aggressive section titles, and specific examples throughout. Its telemetry section is well-scoped. B is more systematic: it uses better table column headers and handles the `invalid_action` boundary (provider-terminal vs. compile-only) more precisely. A's argumentative momentum is better; B's evidentiary precision is better. The final article needs both.

---

## 2. Opening

**Comparing the two**

A opens with a question the author couldn't answer — "of the cases that failed, how many failed because of the model?" — then explains why the question dissolved. This is close to the StrangeTcy voice (see "The Next Question Is Part of the Game": opens with a strategic framing, uses the question as a structural device). The problem is that A's opening is still primarily about the author's epistemic journey rather than a concrete event in the archive.

B opens with a thesis: "A PASS in a code-agent campaign is not a property of a model in isolation." This is crisp but abstract. It reads like the opening of a brief, not a post. It states the conclusion before the reader has a reason to care.

Both openings are generic by StrangeTcy standards. The reference posts open with something specific enough to be immediately strange — a unit test vs. a diagram, "most benchmarks hand the agent its context for free," "suppose I want you to make the wrong decision."

**Proposed opening strategy**

Start with the most concrete fact in the archive that makes the general problem vivid and verifiable. The two `overfit_visible_tests` rows are ideal: they carry a label that sounds like the most interesting failure in the set, their `trusted_score` is 1.0, and their terminal notes describe a missing companion file. The label and the event point in opposite directions on the same row.

Open there — not as "here is an anomaly I found" but as a direct statement of what the record shows. Then raise the problem: if a label can invert its own note, every aggregate built from labels inherits the inversion. Then widen to the full pipeline-compression argument.

Do not start with the author's confusion. Do not start with the pass rate. Do not start with "here's a question." Start with the row.

---

## 3. Examples and Technical Depth

**What is exact, source-grounded, and useful**

From the evidence packet, all of the following are directly traceable:

- The four `monadic_reward` cases rejected for importing `ast` — useful because they show a validator-policy collision that is distinct from a behavioral miss; the policy is not stated in the evidence as having been disclosed to the agent, which makes the ownership ambiguous
- The `compositional_optimizer` case rejected for `weakref`, the `css_state_machine` case rejected for `re` — same point, different environments
- The two `regex_state_machine` underfit cases: input length 32, outputs of length 66 and 34 — these are the closest to a behavioral miss in the behavioral-reference slice and should be named, because they show what a real underfit looks like
- The `rd_adaptive_halting` runtime error (float tensor used as boolean condition) — concrete, traceable, shows execution failure as distinct from source rejection
- The `overfit_visible_tests` mislabeling: `batchnorm_ema` missing `train.py`, `moco` missing `moco_model.py` with `trusted_score=1.0` — both cases, both notes, both environments
- The comparator audit examples: `compositional_optimizer` prompt promises nested associativity / multiple steps while judge checks shape and state-isolation chain; `sheaf_physical_constraints` judge enforces a 5:3 ratio not stated in the prompt — both useful, both require the dirty-repo caveat immediately before or after

**What is decorative or unsupported**

- The tagged-union equation in A. Drop it. The same information is in the failure table and the gate-prose. The equation adds a formalism that isn't earned by the rest of the post and is inconsistent with the airy-paragraph style.
- The full environment totals table. Too long, too granular for this post. The per-environment variance that matters is expressible in prose with three numbers: `moco` 9/11, `glyph` 0/8, `batchnorm_ema` 0/11 — and the one-seed caveat must travel with those numbers.
- Per-case condition strings in the failure examples (e.g., `naming=easy_symptom_mask=hard`) — granular enough to be noise at the prose level; they can be dropped or moved to a parenthetical.

**Tables to retain**

Two tables, both present in both drafts in slightly different forms:

The three-view denominator table should use B's column structure ("What the view represents") — it is cleaner. Keep all three rows (194 raw, 193 single-exclusion, 192 two-exclusion) plus the 24-omission row as a clearly separated note.

The failure taxonomy table should use B's "What the record supports" column (more precise than A's "Where it stopped"). Add the behavioral-reference / compile-only split within each row, as both drafts do. Do not add a separate row for the two provider-terminal `invalid_action` rows; note them in prose immediately below the table to avoid the label collision with the two compile-only `invalid_action` rows inside the 192-case set.

---

## 4. Generic AI Prose and Benchmark-Report Tone

**From Writer A — flag and cut**

- "That plan was wrong, and the reason it was wrong is the point of this post" — functional but slightly theatrical. It works if the opening is concrete enough to make the plan memorable.
- "FAIL is a sum type that got cast to a bool" — strong title; the section body justifies it. Keep the concept; the equation underneath it does not earn its notation.
- "the honest move is to leave the attribution open" — fine as a stated policy; becomes stock if used more than once.
- "the most informative questions concern empty patches, validator policy, required files, provider termination, and what each judge fuckingly verifies" — this is from the source draft and appears in A's closing. The expletive is a deliberate voice marker. If it stays it should appear once and at the argument's peak, not in a list.

**From Writer B — flag and cut**

- "That distinction changes how I read the Atria-Dawn-Preview archive" — stock pivot phrase.
- "A trustworthy summary should show these choices rather than silently selecting the denominator" — design-doc register; cut or fold into a shorter observation.
- "This is not a reason to dismiss behavioral tests. It is a reason to specify what they establish" — the "not X, it is Y" deflation structure appears twice in B. Once is rhetorical; twice is a tic.
- "The payoff is not a more elaborate scoreboard" — fine deflation; keep once.
- "with one selected seed per case and unresolved source-identity questions, the careful conclusion is narrower" — accurate but reads like a grant-paper caveat section. Integrate into the main argument, don't segregate at the end.
- Both drafts use "it does not support / it does not establish" in lists at the close. One negative statement is enough. The rest of the space should be used to say what the evidence does support, which is more interesting.

**From the source draft**

- "This is consistent with broader multi-metric evaluation practice" — generic. Cut; the HELM citation does the work.
- "The central result is not that scalar scores are useless. It is that a scalar should be the last line of a traceable evidence chain, not the first and only one" — this is the cleanest version of the thesis in the source draft and neither final writer reproduces it verbatim. It is worth adapting — not copying — for the final article's thesis statement.

---

## 5. Transitions and Caveat Placement

**Dirty-source/comparator caveat**

Must appear *before* the first claim about what a task or judge checks. Both drafts introduce it in the denominator section, which is correct. But both drafts then use comparator examples later (the compositional-optimizer and physical-constraints cases) without a local reminder. The final article should include a brief local reminder at the "judge is part of the measured system" section — one clause is enough: "these are comparator observations; the dirty repository means they describe the clean snapshot, not the paid-run code with certainty."

**Judge-mode/defect caveat**

Must accompany every compile-only pass rate and every reference to the 131/192 aggregate. Both drafts handle this. The final article should make it part of the table introduction, not a separate paragraph — the column label "explore only" or equivalent in the failure table is one way to carry it without repeating the caveat in prose.

**Provider-terminal / exclusion boundary**

B handles this more precisely than A: B explicitly distinguishes the two provider-terminal `invalid_action` rows (excluded from 192-case set) from the two compile-only `invalid_action` rows inside the taxonomy table. This distinction must be in the final article, with a clear sentence: the same raw label appears in two different situations; the terminal note is what distinguishes them.

**One-seed boundary**

Neither draft integrates this caveat at the point where it most matters: the per-environment variance discussion. When citing `moco` 9/11 vs. `glyph` 0/8 as evidence of heterogeneity, the final article must say "each of these numbers is from one seed per case" before or immediately after — not only in the closing. A reader who sees 82% vs. 0% without that caveat may incorrectly treat the contrast as stable.

---

## 6. Unsupported Claims and Claim Traceability

**Remove or cut entirely**

- Any cost or spend estimate. No spend field exists in the archive. Neither draft makes one, but the blueprint should flag this as a hard prohibition.
- Any characterization of the `epistemic_games` task as involving recursive theory of mind. The comparator shows Bayesian inference over stipulated policy tables. That is what the evidence supports.
- "First" or exhaustive-novelty claims. The prior-work check is targeted, not systematic.

**Narrow before using**

- A's "only three of sixteen failures look like what people mean by 'the model got the task wrong'" — the phrase "what people mean" is an unsupported reader-psychology claim. Narrow to: three of the sixteen behavioral-reference failures carry the `underfit` label, the only category where an independent behavioral judge ran on a submitted patch and found it wanting. Everything else in the sixteen stopped before that judgment.
- B's "A PASS in a code-agent campaign is not a property of a model in isolation" — this is a general claim that slightly exceeds the archive. Frame it as an observation from this specific archive, not a universal statement about the category.
- A's "A syntax error is plausibly the model's output being broken" — OK as stated uncertainty; do not strengthen it.
- Both drafts: "the label is contradicted by its own row" (for `overfit_visible_tests`) — this is accurate for the two labeled cases and is directly traceable. Keep it.

**Substantiate or remove**

- The claim that the `underfit` label "means something different" under compile-only vs. behavioral-reference scoring is asserted but not developed. The evidence supports this: compile-only is explicitly exploratory, and 17 of 20 underfit rows are compile-only. The final article should say this plainly: under compile-only scoring, "underfit" records a judge-shortfall in an exploratory mode; under behavioral-reference, it records a finding by the judge with the stronger guarantee. They are not interchangeable even though the label is identical.
- The SWE-bench 7.8% figure — use it exactly as qualified in the source packet: "in its studied SWE-bench Verified setting." Do not generalize it to this campaign. Both drafts handle this correctly; the blueprint confirms it.
- HELM — cite only as precedent for multi-scenario evaluation, not as validation of this campaign or this post's method.

**Do not reproduce or paraphrase**

Reasoning content is absent. No inference about what the model "did internally" is licensed. The `reasoning_enabled=false` / `reasoning_content` field discrepancy establishes a metadata disagreement, and both drafts correctly decline to interpret it. The final article should name the interpretive temptation (a reader might conclude the model reasoned despite the flag) and then decline it explicitly, in one sentence.

---

## 7. Public-Site Fit

**YAML frontmatter**

Both drafts have the correct fields. Final writer should verify: `title`, `date: 2026-10-03`, `layout: post`. Title should be confirmed as argumentative rather than descriptive — both "Whose Zero Is It?" (A) and "A Verdict Needs Provenance" (B) are acceptable in register; the final writer should choose based on which opening strategy they adopt.

**`{% include mathjax.html %}`**

Include it only if the final article retains LaTeX. If the tagged-union equation is dropped (recommended), remove the include. B includes it with no math in the draft — that is an error B introduces. The final article should not include it decoratively.

**Byline**

Both use the exact form `*by <span class="icon-self">StrangeTcy</span>*` — correct. No change needed.

**Epistemic-status fields**

Use A's "Original ideas" language as the model: explicitly saying "breaking a pass rate down by pipeline stage is standard practice; what this post adds is one specific attribution exercise on one frozen archive" is more honest than B's description of the framing. The "Prose" field must accurately describe the Arena pipeline process. A's version ("a language model wrote this in the Arena pipeline, working from an audited evidence packet and an earlier source draft; later editorial and model passes are revisions of one analysis, not independent replications") is correct and should be carried forward in substance. B's is shorter but less transparent.

The "Certainty" field should specify both what is high-confidence (archived counts, labels, terminal notes) and what is not (exact paid-run task/judge code due to dirty repository, latent model behavior). A's "Low for anything about why a given output was produced" is correctly calibrated.

**Section headers**

A's argumentative headers ("When the tag itself is wrong," "Two judges, two promises") fit the StrangeTcy voice better than B's descriptive ones ("The denominator is an audit choice," "The same numerator crosses two judge modes"). The reference posts use headers as turns in an argument, not labels on containers. Final writer should follow A's approach throughout, including the closing section.

**Voice and register**

A is closer to the reference-post voice. Short paragraphs, questions that advance the argument, willingness to say "that plan was wrong." B is more careful evidentiary­ but reads slightly like an audit report. The final article should move at A's pace with B's precision on label boundaries and table columns.

**Word count**

A runs long; B is at the right length. The section sequence proposed below targets 1,800–2,400 words without padding. The prescriptive checklist and the extended "what this licenses" list are the primary sources of overage in both drafts.

---

## Blueprint Summary for the Final Writer

**Proposed thesis (do not copy verbatim; use as direction)**

A scalar verdict is a lossy projection of a pipeline event. The loss is not symmetric: different stopping points implicate different owners. In this archive, two rows carry a label that inverts their own terminal note. Any aggregate built from labels inherits the inversion. That is what makes the row-level anatomy more informative than the pass rate.

**Opening strategy**

Open with the two `overfit_visible_tests` rows — state the label, state the trusted score of 1.0, state the missing-file note. Do not frame this as discovery or surprise. State it as a fact, then ask what follows from it for every aggregate that uses those labels. That question is the article.

**Section-by-section sequence**

1. **Opening** (~180 words): The mislabeled rows, then the general pipeline-compression problem.
2. **Who gets a row and what the denominator means** (~280 words): 194 scored / 24 omissions / three denominator views (table) / dirty-repo caveat. Introduce provider-terminal distinction here.
3. **Six labels, six stages** (~380 words): Failure taxonomy table (B's column structure). Gate-walkthrough prose. Specific examples: `ast` rejections, length mismatches, float-tensor crash. Underfit label split across judge modes. One-seed caveat when citing per-environment numbers.
4. **When the label contradicts the note** (~200 words): `overfit_visible_tests` detail (expand the opening observation with full evidence). Provider-terminal `invalid_action` pair vs. compile-only `invalid_action` pair — distinguish precisely.
5. **Two judges, two guarantees** (~280 words): Behavioral-reference vs. compile-only split. Comparator audit examples with dirty-repo caveat immediately preceding. SWE-bench citation with its studied-setting qualifier.
6. **Track labels are tags too** (~180 words): `epistemic_games` / `ml_debugging` regrouping in prose with inline numbers. One-seed caveat local to the per-environment contrast.
7. **Telemetry as discrepancy** (~130 words): Retry counter range. `reasoning_enabled=false` / reasoning-token disagreement. Name the interpretive temptation; decline it in one sentence. No spend estimate.
8. **What the evidence licenses** (~180 words): Descriptive map of stopping points; one specific note on what is not licensed (capability ranking, common difficulty scale, causal claims). One sentence on what a pass rate can be if it comes last in a traceable chain.

**Example and equation plan**

Retain: three-view denominator table; failure taxonomy table with B's column structure and judge-mode split; `monadic_reward` + `ast` import rejection (×4); `regex_state_machine` length mismatches; `rd_adaptive_halting` float-tensor crash; `overfit_visible_tests` detail for both cases; comparator audit examples with local dirty-repo caveat.

Drop: tagged-union equation; full environment totals table; per-case condition strings in prose.

**A elements worth retaining**

Argumentative section headers; narrative turning-point structure; specific example depth (ast imports, length mismatches, crash); "the honest move is to leave attribution open" as stated policy; gate-walkthrough prose approach; closing that distinguishes the licensed descriptive map from unlicensed capability claims; voice and pacing.

**B elements worth retaining**

Three-view denominator table with "What the view represents" column; failure taxonomy table with "What the record supports" column; precise handling of provider-terminal vs. compile-only `invalid_action` distinction; "A judge is part of the measured system" as a section concept; epistemic-status "Certainty" language; the formulation that a behavioral-reference pass is not interchangeable with a compile-only pass even when both score 1.

**Elements neither draft handles well**

The underfit-label ambiguity across judge modes — neither draft says explicitly that "underfit" under compile-only and "underfit" under behavioral-reference are not the same epistemic object. The final article should say this once, plainly, in the failure-label section.

The one-seed caveat is in the closing of both drafts but absent from the per-environment contrast discussion, where it most needs to be.

The interpretive temptation posed by the reasoning-token discrepancy is named but not articulated. A reader who sees `reasoning_enabled=false` alongside 325,785 reasoning tokens would naturally want to conclude something. The final article should name that inference, then decline it with the reason: field presence is not field semantics, and no reasoning text is available.

---

## Final Quality Checklist

- [ ] YAML frontmatter complete: `title`, `date: 2026-10-03`, `layout: post`
- [ ] `{% include mathjax.html %}` included only if LaTeX is retained in the body; removed if equation is dropped
- [ ] Exact byline: `*by <span class="icon-self">StrangeTcy</span>*`
- [ ] `<dl class="epistemic-status">` present with all five fields in order; "Prose" field accurately describes Arena pipeline process without claiming independent experimental replication
- [ ] "Original ideas" field calibrated honestly (standard practice + one specific archive exercise)
- [ ] Dirty-repo caveat precedes every claim about task or judge behavior drawn from the comparator; a local reminder appears at the comparator-audit section even if the caveat was introduced earlier
- [ ] Compile-only/exploratory caveat accompanies every compile-only pass rate and the 131/192 aggregate
- [ ] One-seed caveat appears inline at the per-environment contrast (moco / glyph / batchnorm_ema numbers), not only in the closing
- [ ] Provider-terminal `invalid_action` pair explicitly distinguished from compile-only `invalid_action` pair inside the 192-case taxonomy
- [ ] `overfit_visible_tests` treatment states: the label, `trusted_score=1.0`, the missing-file note, and that the record does not resolve cause — without calling it overfitting or dismissing it
- [ ] No claim about reasoning content or cognition from the `reasoning_content` field; the interpretive temptation is named and declined
- [ ] No cost or spend estimate (no spend field in archive)
- [ ] SWE-bench 7.8% figure cited with "in its studied SWE-bench Verified setting" qualifier — not generalized to this campaign
- [ ] HELM cited as precedent for multi-scenario evaluation, not as validation
- [ ] `epistemic_games` task described as Bayesian inference over stipulated policy tables — not as recursive theory of mind
- [ ] Section headers are argumentative turns, not descriptive labels
- [ ] No tagged-union equation unless the final writer finds it indispensable (default: drop)
- [ ] No fenced code block or bullet-list design-doc checklist for "what a row should carry"; integrate as one or two sentences
- [ ] Closing states what the evidence licenses in one paragraph; does not list every unlicensed claim individually
- [ ] No internal compiler paths, hashes, claim IDs, or evidence-packet labels in public prose
- [ ] Word count 1,800–2,400; no padding sections
- [ ] Expletive voice marker used at most once, at the argument's peak, not in a list
[[[ END INPUT 04 — job:post04_editorial_critic:response ]]]
