# Compiler evidence packet — POST-04

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## BEGIN INPUT ARTIFACT: 01 — source_draft_POST-04
Source snapshot SHA-256: `1ae2208ea2af67f284e042f7522f7340ba6a100611c4369ca908c4d495000b38`
Rendered message SHA-256: `1ae2208ea2af67f284e042f7522f7340ba6a100611c4369ca908c4d495000b38`
Original reference: `mission:source_draft_POST-04`

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

## END INPUT ARTIFACT: 01 — source_draft_POST-04

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
Rendered message SHA-256: `62bde9c3b0532996932e70e1d3c033a858a8b789834ae5854f1fba9bfa021afb`
Original reference: `mission:references`

POST-04 prior-work references from the source draft; context only, not validation of this campaign.

- You Wang, Michael Pradel, and Zhongxin Liu. “Are ‘Solved Issues’ in SWE-bench Really Solved Correctly? An Empirical Study.” The study reports that 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite in its studied SWE-bench Verified setting. This rate is not an estimate for the Atria campaign. https://dl.acm.org/doi/10.1145/3744916.3764576
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: a precedent for broad scenario and metric coverage, not a validation of this campaign. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim.

## END INPUT ARTIFACT: 04 — references

## BEGIN INPUT ARTIFACT: 07 — trace_rows_POST-04
Source snapshot SHA-256: `c64b4bd39323d9ed8d26f176dda07eba0c929ef59bc1822a7c5bc8067ce97362`
Rendered message SHA-256: `36aebf78eb701287c8a5b8e45bf9f7c7bf9fba1c13a9384c81e738c5636d3e32`
Original reference: `mission:trace_rows_POST-04`

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

## END INPUT ARTIFACT: 07 — trace_rows_POST-04

## BEGIN INPUT ARTIFACT: 08 — relevant_findings_POST-04
Source snapshot SHA-256: `dd0c94b3d256a124cfdf5eb45f8c7dc4fa51ebc9a633936b970cb1b7d6f38f12`
Rendered message SHA-256: `6a0a9762dd4d0473232d37e3166968c7d512bc3d9ecdba85cc1f151bb5e741c6`
Original reference: `mission:relevant_findings_POST-04`

{"claim_ids":["POST-04-C01","POST-04-C02","POST-04-C03","POST-04-C04","POST-04-C05","POST-04-C06","POST-04-C07","POST-04-C08","POST-04-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign report records 194 scored selected cases and 24 separate pre-scoring omissions; the case manifest and result checkpoint contain the same 194 case IDs.","confidence":"HIGH.","id":"F-02","limitations":["The 7 gate-blocked and 17 unsupported cases have no model score and must not be counted as failures or passes.","A complete unfiltered planned-design file is not required to reproduce this report-level union."],"quantitative_result":"194/194 selected results have status scored across 33 environments; 17 rope cases are omitted for unsupported provider input modality and 7 cases are omitted before provider access for known calibration failures; 218 case IDs are recorded as scored or explicitly omitted.","status":"OBSERVED"},{"claim":"Two final selected results, not just the one named in the campaign-level outage counter, explicitly attribute their terminal failure to provider transients after bounded retries.","confidence":"HIGH that both final notes exist; MEDIUM that every terminal provider-coded row should be excluded from model-performance analysis, because the official campaign counter tracks only one episode.","id":"F-03","limitations":["The raw row remains scored and its raw failure label is retained; the 192 denominator is an explicit analysis exclusion, not a rewritten campaign report.","API error events also include transient retries that recovered; only final-result terminal notes define these two exclusions."],"quantitative_result":"Raw checkpoint: 131 PASS / 63 FAIL among 194. Removing only report-listed ts_trajectory gives 131/193 PASS and 62 FAIL. Removing both final-note provider cases gives 131/192 PASS and 61 FAIL.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The archive assigns all seven epistemic_games cases to the recorded ml_debugging track, although the inspected task core implements symbolic Bayesian inference.","confidence":"HIGH for recorded label; HIGH that task semantics are symbolic Bayesian inference in the comparator; MEDIUM for whether the recorded grouping was intentionally multi-purpose.","id":"F-05","limitations":["The analysis_family override is an explicit editorial regrouping; the raw track is preserved unchanged.","A dirty source tree limits claims about the exact executed task code."],"quantitative_result":"Recorded track summary: ml_debugging 37 cases, 16 PASS/21 FAIL. Source-semantic regrouping: 30 ML-debugging cases, 9 PASS/21 FAIL; epistemic_games separate at 7/7 PASS.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"After removing the epistemic_games track-label anomaly, the three selected ML-debugging environments show 9/30 PASS, with highly uneven task outcomes.","confidence":"HIGH for per-environment result counts and notes; MEDIUM for using the three tasks as a coherent ML-debugging construct.","id":"F-12","limitations":["Only three environment families are grouped here; one has compile-only judgments.","One seed and one selected response per case; no general ML-debugging inference."],"quantitative_result":"batchnorm_ema 0/11 (compile_only), glyph 0/8 (behavioral_reference), moco 9/11 (behavioral_reference); the two MoCo/BatchNorm rows labeled overfit_visible_tests have notes about missing required companion files.","status":"OBSERVED"},{"claim":"The archive contains incompatible retry counters and a reasoning-mode metadata discrepancy; usage or retry totals should not be collapsed into a single canonical value.","confidence":"HIGH that the archived counters/fields disagree; LOW about the underlying cause.","id":"F-13","limitations":["No spend/cost field exists in the exported archive.","No reasoning content is copied or interpreted; presence counts are metadata only."],"quantitative_result":"All 268 runs: 4,061 successful responses, 4,023 summed run/turn IDs, 9,447,242 successful-response tokens. `reasoning_enabled=false` coexists with 325,785 reported reasoning tokens and 2,710 rows containing a reasoning_content field. Retry counts range by source/scope from 3,869 selected final-manifest attempts to 6,412 progress-reported attempts.","status":"OBSERVED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-04","schema_version":1,"trace_finding_ids":["F-01","F-02","F-03","F-04","F-05","F-09","F-13","F-15","F-16","F-17"]}

## END INPUT ARTIFACT: 08 — relevant_findings_POST-04

## BEGIN INPUT ARTIFACT: 09 — evidence_extract_POST-04
Source snapshot SHA-256: `d6a8a332ff5173f4b42371b0e06ae4668d31d7733003cf8ec2a2517269565203`
Rendered message SHA-256: `b1f18fc5b56446429645f80a557acdc0724885c08f5f486b399794c8db01b92c`
Original reference: `mission:evidence_extract_POST-04`

Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## END INPUT ARTIFACT: 09 — evidence_extract_POST-04

## BEGIN INPUT ARTIFACT: 10 — limitations_POST-04
Source snapshot SHA-256: `e83695e956d4dcb47177cde0ec505b963650898e34ed5d20e47f148f734f629e`
Rendered message SHA-256: `b5e81d5692a6bfbf41a9eb3cf48bf4d2e3882616db8f3356b3775d41325e5586`
Original reference: `mission:limitations_POST-04`

- One selected seed per case; no cell-level replications. Keep 194 raw results, 24 separate omissions, two provider-terminal cases, and the 192-case sensitivity set distinct.
- The eligible set mixes 72 behavioral-reference and 120 compile-only cases; compile-only results are exploratory, not a validated behavioral aggregate.
- The repository was recorded dirty; matching config hashes do not establish exact task/judge identity. Axes are task-specific and sparse; names/hints are bundled, and validator/runtime/judge failures are not behavioral misses.

## END INPUT ARTIFACT: 10 — limitations_POST-04

## BEGIN INPUT ARTIFACT: 11 — source_audit_POST-04
Source snapshot SHA-256: `2c17ea0fb622c866b5d11582080817041bc7abb59b098333b2c78c465d878b72`
Rendered message SHA-256: `a3b7c00b7463d5d3936a61b0d9c6f768f6085d52580baec5b29227b90e8cd8e8`
Original reference: `mission:source_audit_POST-04`

## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## END INPUT ARTIFACT: 11 — source_audit_POST-04

## BEGIN INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-04
Source snapshot SHA-256: `adf76efc0842ab0fc123a5ac021c56227588d65938f3bfc15ae5a203a2c7f4b4`
Rendered message SHA-256: `dcf1bdd8d2636f1bc4c65703e7e2511ff9a5032bc2a564b109ed7cfa150970cd`
Original reference: `mission:evidence_analysis_family_summary_POST-04`

analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails

## END INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-04

## BEGIN INPUT ARTIFACT: 15 — evidence_case_results_POST-04
Source snapshot SHA-256: `6fac93cfe36d331f85bf454908d40989f5337e68546354023267f9742a986e09`
Rendered message SHA-256: `f42e55d003ecef9313b2c70a8957f406234b05568c55c3fd559d3c597bf5c21a`
Original reference: `mission:evidence_case_results_POST-04`

case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason

## END INPUT ARTIFACT: 15 — evidence_case_results_POST-04

## BEGIN INPUT ARTIFACT: 16 — evidence_environment_summary_POST-04
Source snapshot SHA-256: `3de3177a6dbdd61e74b3532f14157efc865b517aa3f4f9c6023e721d22e6d806`
Rendered message SHA-256: `ff02a48e76491da94ac988842239c6657ec5fa875867e3a3320b15406c3aa9d9`
Original reference: `mission:evidence_environment_summary_POST-04`

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

## END INPUT ARTIFACT: 16 — evidence_environment_summary_POST-04

## BEGIN INPUT ARTIFACT: 17 — evidence_failure_details_POST-04
Source snapshot SHA-256: `ddfbf8f204f2f1935b4166d4fee88ec7e5988fdabd191c09c9fc0c7f2268ba84`
Rendered message SHA-256: `a5d63501d8fdf6bf86eedcbfd53ce4c879838cd3831236dc439243444002d0fc`
Original reference: `mission:evidence_failure_details_POST-04`

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

## END INPUT ARTIFACT: 17 — evidence_failure_details_POST-04

## BEGIN INPUT ARTIFACT: 18 — evidence_failure_taxonomy_POST-04
Source snapshot SHA-256: `49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4`
Rendered message SHA-256: `379b2b331fd20d910a3cbf6277cf82680f95fd19c160fc8042c8b3fd5f9d12b5`
Original reference: `mission:evidence_failure_taxonomy_POST-04`

failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"

## END INPUT ARTIFACT: 18 — evidence_failure_taxonomy_POST-04

## Compiler-only validator metadata (never copy into public copy)
<!-- POST_PRODUCTION_VALIDATOR_METADATA
{"allowed_numbers": ["0", "0.0", "0.03278688524590164", "0.04918032786885246", "0.16393442622950818", "0.2", "0.208333", "0.277778", "0.2857142857142857", "0.32786885245901637", "0.39344262295081966", "0.4", "0.416667", "0.5", "0.6", "0.6666666666666666", "0.7142857142857143", "0.8", "0.8181818181818182", "0.95", "1", "1.0", "10", "11", "120", "122", "131", "15", "16", "17", "192", "193", "194", "2", "20", "21", "218", "24", "256", "268", "2710", "2968", "3", "30", "31", "32", "325785", "33", "34", "37", "3869", "4", "4023", "4061", "42", "45", "47", "5", "56", "61", "62", "63", "6412", "66", "7", "7.8", "7.8%", "72", "75", "8", "9", "9447242"], "evidence_input_sha256": {"mission:campaign_provenance": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "mission:evidence_analysis_family_summary_POST-04": "adf76efc0842ab0fc123a5ac021c56227588d65938f3bfc15ae5a203a2c7f4b4", "mission:evidence_campaign_exclusions_POST-04": "3300ad90064458a38b1166bd9f5b3c840fa690604c2219cbc3129a3207b92542", "mission:evidence_campaign_scope_POST-04": "acacd9f7891af79958df9f66838bdafa4a237021826784d195a3b1eae5c9208e", "mission:evidence_case_results_POST-04": "6fac93cfe36d331f85bf454908d40989f5337e68546354023267f9742a986e09", "mission:evidence_environment_summary_POST-04": "3de3177a6dbdd61e74b3532f14157efc865b517aa3f4f9c6023e721d22e6d806", "mission:evidence_extract_POST-04": "d6a8a332ff5173f4b42371b0e06ae4668d31d7733003cf8ec2a2517269565203", "mission:evidence_failure_details_POST-04": "ddfbf8f204f2f1935b4166d4fee88ec7e5988fdabd191c09c9fc0c7f2268ba84", "mission:evidence_failure_taxonomy_POST-04": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "mission:house_style": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "mission:limitations_POST-04": "e83695e956d4dcb47177cde0ec505b963650898e34ed5d20e47f148f734f629e", "mission:references": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "mission:relevant_findings_POST-04": "dd0c94b3d256a124cfdf5eb45f8c7dc4fa51ebc9a633936b970cb1b7d6f38f12", "mission:source_audit_POST-04": "2c17ea0fb622c866b5d11582080817041bc7abb59b098333b2c78c465d878b72", "mission:source_draft_POST-04": "1ae2208ea2af67f284e042f7522f7340ba6a100611c4369ca908c4d495000b38", "mission:style_reference_material": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "mission:trace_rows_POST-04": "c64b4bd39323d9ed8d26f176dda07eba0c929ef59bc1822a7c5bc8067ce97362", "mission:workflow_input_manifest": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158"}, "finding_ids": ["F-01", "F-02", "F-03", "F-04", "F-05", "F-09", "F-12", "F-13", "F-15", "F-16", "F-17"], "post_id": "POST-04", "publication_date": "2026-10-03", "source_input_records": [{"attachment_index": 0, "reference": "mission:source_draft_POST-04", "sha256": "1ae2208ea2af67f284e042f7522f7340ba6a100611c4369ca908c4d495000b38", "size_bytes": 5765, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/source_draft.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/source_draft.md"}, {"attachment_index": 1, "reference": "mission:house_style", "sha256": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "size_bytes": 12397, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/house_style.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/house_style.md"}, {"attachment_index": 2, "reference": "mission:style_reference_material", "sha256": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "size_bytes": 19939, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md"}, {"attachment_index": 3, "reference": "mission:references", "sha256": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "size_bytes": 3532, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/references.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/references.md"}, {"attachment_index": 4, "reference": "mission:campaign_provenance", "sha256": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "size_bytes": 13690, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md"}, {"attachment_index": 5, "reference": "mission:workflow_input_manifest", "sha256": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158", "size_bytes": 28349, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json"}, {"attachment_index": 6, "reference": "mission:trace_rows_POST-04", "sha256": "c64b4bd39323d9ed8d26f176dda07eba0c929ef59bc1822a7c5bc8067ce97362", "size_bytes": 9307, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/trace_rows.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/trace_rows.csv"}, {"attachment_index": 7, "reference": "mission:relevant_findings_POST-04", "sha256": "dd0c94b3d256a124cfdf5eb45f8c7dc4fa51ebc9a633936b970cb1b7d6f38f12", "size_bytes": 45774, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/relevant_findings.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/relevant_findings.json"}, {"attachment_index": 8, "reference": "mission:evidence_extract_POST-04", "sha256": "d6a8a332ff5173f4b42371b0e06ae4668d31d7733003cf8ec2a2517269565203", "size_bytes": 1853, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence_extract.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence_extract.md"}, {"attachment_index": 9, "reference": "mission:limitations_POST-04", "sha256": "e83695e956d4dcb47177cde0ec505b963650898e34ed5d20e47f148f734f629e", "size_bytes": 1347, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/limitations.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/limitations.md"}, {"attachment_index": 10, "reference": "mission:source_audit_POST-04", "sha256": "2c17ea0fb622c866b5d11582080817041bc7abb59b098333b2c78c465d878b72", "size_bytes": 5888, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/source_audit_excerpt.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/source_audit_excerpt.md"}, {"attachment_index": 11, "reference": "mission:evidence_analysis_family_summary_POST-04", "sha256": "adf76efc0842ab0fc123a5ac021c56227588d65938f3bfc15ae5a203a2c7f4b4", "size_bytes": 341, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/analysis_family_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/analysis_family_summary.csv"}, {"attachment_index": 12, "reference": "mission:evidence_campaign_exclusions_POST-04", "sha256": "3300ad90064458a38b1166bd9f5b3c840fa690604c2219cbc3129a3207b92542", "size_bytes": 8047, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/campaign_exclusions.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/campaign_exclusions.csv"}, {"attachment_index": 13, "reference": "mission:evidence_campaign_scope_POST-04", "sha256": "acacd9f7891af79958df9f66838bdafa4a237021826784d195a3b1eae5c9208e", "size_bytes": 6058, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/campaign_scope.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/campaign_scope.json"}, {"attachment_index": 14, "reference": "mission:evidence_case_results_POST-04", "sha256": "6fac93cfe36d331f85bf454908d40989f5337e68546354023267f9742a986e09", "size_bytes": 207, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/selected_case_results.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/selected_case_results.csv"}, {"attachment_index": 15, "reference": "mission:evidence_environment_summary_POST-04", "sha256": "3de3177a6dbdd61e74b3532f14157efc865b517aa3f4f9c6023e721d22e6d806", "size_bytes": 1998, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/environment_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/environment_summary.csv"}, {"attachment_index": 16, "reference": "mission:evidence_failure_details_POST-04", "sha256": "ddfbf8f204f2f1935b4166d4fee88ec7e5988fdabd191c09c9fc0c7f2268ba84", "size_bytes": 20228, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/failure_details.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/failure_details.csv"}, {"attachment_index": 17, "reference": "mission:evidence_failure_taxonomy_POST-04", "sha256": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "size_bytes": 6231, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/failure_taxonomy.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-04/evidence/failure_taxonomy.csv"}], "trace_row_ids": ["POST-04-C01", "POST-04-C02", "POST-04-C03", "POST-04-C04", "POST-04-C05", "POST-04-C06", "POST-04-C07", "POST-04-C08", "POST-04-C09"]}
-->
