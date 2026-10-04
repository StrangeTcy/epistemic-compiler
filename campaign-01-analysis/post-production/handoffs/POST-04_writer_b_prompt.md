# Independent StrangeTcy research essay — POST-04

Write one complete essay with a new thesis, opening, and argument structure. Use the full draft as an evidence map, not an outline or prose to paraphrase. This is one of two parallel candidates; do not refer to or imitate another answer.

Use only supplied facts and citations. Keep raw scores, exclusions, provider-terminal cases, denominators, judge guarantees, and failure layers distinct. Compile-only outcomes are exploratory, not a validated behavioral aggregate. There is one selected seed per cell; subsequent editorial/model role passes are not independent replications. The repository was recorded dirty: the clean source is only a comparator. These sparse results do not establish causal effects, a common difficulty scale, or a general capability ranking. Keep caveats next to claims. Distinguish validator/runtime/tool/judge failures from behavioral misses.

POST-02 is Bayesian inference over stipulated policies, not recursive ToM; POST-05's Rule 110/code-repair observations do not establish Turing completeness. Category-track outcomes are heterogeneous code-repair results, not a theorem or scalar score.

POST-04-specific evidence boundaries:
- Keep the 194 raw scored rows, 24 separate omissions, the 193-row single-provider-exclusion sensitivity set, and the 192-row two-provider-exclusion analysis set distinct. The 24 omissions are not scored failures.
- In the 192-row set, distinguish 72 behavioral-reference cases from 120 exploratory compile-only cases; scope the 61-failure taxonomy to that set.
- Two raw rows have `invalid_action` labels but final notes attributing terminal failure to provider transients. Preserve the raw labels and the terminal-note interpretation; do not describe those rows as ordinary model-format failures.
- The seven `epistemic_games` rows retain their recorded track label. Any semantic regrouping is an analysis view, not a rewrite of the archive.
- Treat configuration/telemetry inconsistencies as metadata discrepancies, not evidence about internal reasoning. The archive has no spend field, and no reasoning text is reproduced.
- The SWE-bench study's 7.8% result applies only to its studied setting; never present it as a rate for this campaign.
- For literature context, use only the SWE-bench study and HELM entries in the POST-04 reference block. Do not import unrelated cross-post bibliography items from campaign-wide evidence summaries.

The packet includes verbatim excerpts from actual StrangeTcy posts: use them only for rhetorical structure, never copy distinctive wording, examples, titles, or author-process claims. Avoid generic AI prose and benchmark-report tone; use technical detail and math/tables/diagrams only when they clarify.

Return only the complete Markdown article, 1,800–2,500 words. Use frontmatter `title`, `date: 2026-10-03`, `layout: post`; the exact StrangeTcy byline; and the site's epistemic-status `<dl>` fields in order: Original ideas, Synthesis, Prose, Certainty, Importance. If using math, place `{% include mathjax.html %}` after frontmatter. Attribute the actual Arena writing process accurately. No preface, editor note, draft label, internal `F-xx`/`POST-xx` ID, path, hash, or response fence.

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
