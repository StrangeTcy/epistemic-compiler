# Independent StrangeTcy research essay — POST-03

Write one complete essay with a new thesis, opening, and argument structure. Use the full draft as an evidence map, not an outline or prose to paraphrase. This is one of two parallel candidates; do not refer to or imitate another answer.

Use only supplied facts and citations. Keep raw scores, exclusions, provider-terminal cases, denominators, judge guarantees, and failure layers distinct. Compile-only outcomes are exploratory, not a validated behavioral aggregate. There is one selected seed per cell; subsequent editorial/model role passes are not independent replications. The repository was recorded dirty: the clean source is only a comparator. These sparse results do not establish causal effects, a common difficulty scale, or a general capability ranking. Keep caveats next to claims. Distinguish validator/runtime/tool/judge failures from behavioral misses.

POST-02 is Bayesian inference over stipulated policies, not recursive ToM; POST-05's Rule 110/code-repair observations do not establish Turing completeness. Category-track outcomes are heterogeneous code-repair results, not a theorem or scalar score.

The packet includes verbatim excerpts from actual StrangeTcy posts: use them only for rhetorical structure, never copy distinctive wording, examples, titles, or author-process claims. Avoid generic AI prose and benchmark-report tone; use technical detail and math/tables/diagrams only when they clarify.

Return only the complete Markdown article, 1,800–2,500 words. Use frontmatter `title`, `date: 2026-10-03`, `layout: post`; the exact StrangeTcy byline; and the site's epistemic-status `<dl>` fields in order: Original ideas, Synthesis, Prose, Certainty, Importance. If using math, place `{% include mathjax.html %}` after frontmatter. Attribute the actual Arena writing process accurately. No preface, editor note, draft label, internal `F-xx`/`POST-xx` ID, path, hash, or response fence.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post03_prepare_post:response | source_sha256=c0e3ffc72dbd4e820c043c1e019f41e0a1ab38d555e95b05c83ac3303b76f94f | rendered_sha256=32250e7e4e4e0c13c8f1f17e7be8e91f879082e1b089af735dc3e08fa9ba7eaa ]]]
# Compiler evidence packet — POST-03

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
# POST-03 — A category-theory label is not a category-theory measurement

**Dek:** The category/compositional track contains real code-repair outcomes, but its task prompts, judges, and nominal controls do not consistently measure the mathematical properties their labels suggest.

**Draft**

A passing test can establish that a submitted implementation satisfied the checks that ran. It does not, on its own, establish that a model “understands category theory.” That distinction is especially important in the archived `category_theoretic_compositional` track.

The campaign contains 85 selected rows in this track. After excluding one final case whose judge note attributes its failure to bounded provider transients, 57 of 84 eligible cases pass. Five eligible rows are labeled `behavioral_reference`; the other 79 are `compile_only`, a mode the campaign report explicitly calls exploratory. The total is therefore a heterogeneous code-repair result, not a validated score for category-theoretic competence. The source-level examples below come from the clean comparator; the campaign records `repository.dirty=true`, so those observations do not establish that every paid workspace matched it. ⟦POST-03-C01 · F-01/F-03/F-04/F-08⟧

The source comparator illustrates why. In `compositional_optimizer`, the prompt describes strict associativity under nested composition and numerical correctness across multiple training steps. The inspected judge checks output shape and a single state-isolation chain; the visible test is a single-step shape check. Those can be useful programming checks, but they do not test whether two parenthesizations of a three-operation composition agree across a multi-step horizon. ⟦POST-03-C02 · F-15⟧

The same task’s nominal axes raise a more basic issue: the clean comparator’s task, starter file, visible test, and judge use `MomentumStep` directly. The selected config placeholders for `MODEL_CLASS` and `LR_VAL` have no direct reference in those environment templates. The five archived outcomes—three passes and two failures—therefore cannot be interpreted as a response curve over optimizer classes or learning rates under that comparator. Because the campaign records a dirty repository, this is a finding about the inspected source snapshot, not proof that every paid workspace was identical. ⟦POST-03-C03 · F-01/F-14⟧

A second example comes from `categorical_lenses`. The prompt describes a lens with a coordinate-zero view, while the inspected hidden judge checks the three lens laws but does not itself assert that coordinate-zero convention; a visible test does check it. The config’s `STRICT_LAWS` placeholder has no direct reference in the clean environment templates, and the judge always checks all three laws. The environment’s four passes and one failure are exact outcomes under those checks, not a general test of lens theory. ⟦POST-03-C04 · F-08/F-14/F-15⟧

A third mismatch appears in `sheaf_physical_constraints`. The prompt asks for capacity-safe routing but does not state the 5:3 ratio enforced by the inspected judge on a fixed high-demand vector. The visible test checks output keys and shape rather than that ratio. A model can fail because it did not infer an unstated numerical constraint; a pass shows that it met this implementation’s fixed checks. Neither outcome alone demonstrates an understanding of sheaf consistency or physical constraints as a general concept. ⟦POST-03-C05 · F-15⟧

The track’s family total conceals this implementation diversity. It includes tasks around lenses, compositional optimizers, sheaves, functors, monads, parsers, tokenizers, and other code structures. In the eligible set, recorded outcomes range from 0/4 for `sheaf_physical_constraints` to 5/5 in several environments. The inspected comparator helps explain some cases, while the raw final artifacts identify others as empty patches or source-validation errors. The overall 57/84 result mixes task semantics, test completeness, judge modes, and submission quality. ⟦POST-03-C06 · F-08/F-09/F-15⟧

This is not an argument that formal ideas cannot be evaluated through code. It is an argument that a benchmark needs a clear contract between the mathematical claim, prompt, visible tests, judge, and reference implementation. For each task, the authors should state the property being tested, include counterexamples and valid alternatives, and have an independent oracle check that the hidden tests discriminate the intended property from merely plausible code. The existing source audit also suggests adding a build-time check that every advertised axis changes an agent-visible or judge-visible artifact. ⟦POST-03-C07 · F-08/F-14/F-15⟧

The safe conclusion is deliberately narrower than the track name: on these selected code tasks and these implementations, Atria-Dawn-Preview produced a mixed set of passing and failing submissions. The archived results can help improve the benchmark. They do not warrant a claim of category-theory mastery, nor do they establish a general compositional-reasoning capability. ⟦POST-03-C08 · F-08/F-16⟧

**Implementation references:** The comparator audit cites `envs/cat_theo/compositional_optimizer/files/prompt.md` and `judge.py`; `envs/cat_theo/categorical_lenses/files/prompt.md`, `judge.py`, and `visible_tests.py`; and `envs/cat_theo/sheaf/sheaf_physical_constraints/files/prompt.md`, `judge.py`, and `visible_tests.py`. Exact line ranges and the dirty-source qualification are recorded in [`evidence/source_implementation_audit.md`](../evidence/source_implementation_audit.md).

**Editor’s note:** Double-bracket evidence markers are internal and link each factual paragraph to the findings register and raw case files.

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
POST-03,POST-03-C01,F-01;F-03;F-04;F-08
POST-03,POST-03-C02,F-15
POST-03,POST-03-C03,F-01;F-14
POST-03,POST-03-C04,F-08;F-14;F-15
POST-03,POST-03-C05,F-15
POST-03,POST-03-C06,F-08;F-09;F-15
POST-03,POST-03-C07,F-08;F-14;F-15
POST-03,POST-03-C08,F-08;F-16

## Relevant finding records
{"claim_ids":["POST-03-C01","POST-03-C02","POST-03-C03","POST-03-C04","POST-03-C05","POST-03-C06","POST-03-C07","POST-03-C08"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"Two final selected results, not just the one named in the campaign-level outage counter, explicitly attribute their terminal failure to provider transients after bounded retries.","confidence":"HIGH that both final notes exist; MEDIUM that every terminal provider-coded row should be excluded from model-performance analysis, because the official campaign counter tracks only one episode.","id":"F-03","limitations":["The raw row remains scored and its raw failure label is retained; the 192 denominator is an explicit analysis exclusion, not a rewritten campaign report.","API error events also include transient retries that recovered; only final-result terminal notes define these two exclusions."],"quantitative_result":"Raw checkpoint: 131 PASS / 63 FAIL among 194. Removing only report-listed ts_trajectory gives 131/193 PASS and 62 FAIL. Removing both final-note provider cases gives 131/192 PASS and 61 FAIL.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The category_theoretic_compositional track is a heterogeneous code-repair set with mixed judge guarantees, not a homogeneous test of category-theoretic reasoning.","confidence":"HIGH for counts and source-semantic heterogeneity; MEDIUM for task categorization under dirty-source provenance.","id":"F-08","limitations":["79 eligible cases are compile-only, and the exact behavioral-reference cases are only a subset.","Several axes are not referenced in the clean comparator; some prompts/judges have scope mismatches.","The campaign's source dirty flag blocks complete executed-implementation attribution."],"quantitative_result":"85 raw rows; one provider-coded row excluded; 57 PASS/27 FAIL among 84 eligible rows. Eligible mode split: 4/5 PASS for categorical_lenses behavioral_reference and 53/79 PASS for compile_only cases. The 17-environment track spans task families with outcomes from 0/5 to 5/5.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"The category-track source comparator indicates several advertised axes were not implemented in the environment templates, so nominal coverage can overstate the number of distinct interventions.","confidence":"HIGH for no direct reference in the inspected clean source files; MEDIUM for the claim about executed paid cases because the recorded repository was dirty.","id":"F-14","limitations":["The static scan does not execute generation or compare every rendered task bundle.","Only selected configurations were scanned; unsupported and gate-blocked cases were not model-run."],"quantitative_result":"The static scan finds ten no-reference control/variable axes across nine category environments, including both axes in compositional_optimizer; details are in axis_placeholder_audit.csv and source_implementation_audit.md.","status":"INFERRED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-03","schema_version":1,"trace_finding_ids":["F-01","F-03","F-04","F-08","F-09","F-14","F-15","F-16"]}

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
category_theoretic_compositional,85,84,57,27,0.6785714285714286,5,4,1,79,53,26

## Evidence Axis Placeholder Audit Post-03
config_path,axis,placeholder,source_reference_status
envs/cat_theo/architecture_naturality/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/architecture_naturality/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/architecture_naturality/config.yaml,symptom_mask,CHECK_DIM,no reference in environment file templates
envs/cat_theo/categorical_lenses/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/categorical_lenses/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/categorical_lenses/config.yaml,symptom_mask,STRICT_LAWS,no reference in environment file templates
envs/cat_theo/compositional_optimizer/config.yaml,naming,MODEL_CLASS,no reference in environment file templates
envs/cat_theo/compositional_optimizer/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/compositional_optimizer/config.yaml,symptom_mask,LR_VAL,no reference in environment file templates
envs/cat_theo/equivariant_diagram/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/equivariant_diagram/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/equivariant_diagram/config.yaml,symptom_mask,SYMMETRY_DIM,no reference in environment file templates
envs/cat_theo/functorial_augmentation/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/functorial_augmentation/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/functorial_augmentation/config.yaml,symptom_mask,AUG_PARAM,no reference in environment file templates
envs/cat_theo/monadic_reward/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/monadic_reward/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/monadic_reward/config.yaml,symptom_mask,SIDE_EFFECT_CHECK,no reference in environment file templates
envs/cat_theo/semiring/gnn_message_passing/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring/gnn_message_passing/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/semiring/gnn_message_passing/config.yaml,symptom_mask,TOLERANCE,placeholder referenced in environment file templates
envs/cat_theo/semiring/neuro_symbolic_parser/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring/neuro_symbolic_parser/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/semiring/neuro_symbolic_parser/config.yaml,symptom_mask,TOLERANCE,no reference in environment file templates
envs/cat_theo/semiring/ssm_parallel_scan/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring/ssm_parallel_scan/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/semiring/ssm_parallel_scan/config.yaml,symptom_mask,TOLERANCE,placeholder referenced in environment file templates
envs/cat_theo/semiring_unification/config.yaml,naming,ARITH_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring_unification/config.yaml,naming,BOOL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring_unification/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/semiring_unification/config.yaml,naming,TROP_CLASS,placeholder referenced in environment file templates
envs/cat_theo/semiring_unification/config.yaml,symptom_mask,INF_VAL,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_invariant_gluing/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_invariant_gluing/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/sheaf/sheaf_invariant_gluing/config.yaml,symptom_mask,THRESHOLD,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_physical_constraints/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_physical_constraints/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/sheaf/sheaf_physical_constraints/config.yaml,symptom_mask,GLOBAL_CAP,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_schema_sync/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/sheaf/sheaf_schema_sync/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/sheaf/sheaf_schema_sync/config.yaml,symptom_mask,DEFER_CONSTRAINTS,placeholder referenced in environment file templates
envs/cat_theo/stochastic_monad/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/stochastic_monad/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/stochastic_monad/config.yaml,symptom_mask,SIGMA_VAL,no reference in environment file templates
envs/cat_theo/tensor_functor/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/tensor_functor/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/tensor_functor/config.yaml,symptom_mask,DIM_CHECK,placeholder referenced in environment file templates
envs/cat_theo/tensor_functor/config.yaml,symptom_mask,RIGID_SLICE,placeholder referenced in environment file templates
envs/cat_theo/tokenizer_adjunction/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/tokenizer_adjunction/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/tokenizer_adjunction/config.yaml,symptom_mask,UNICODE_SUPPORT,no reference in environment file templates
envs/cat_theo/transformer_ssm_lift/config.yaml,naming,MODEL_CLASS,placeholder referenced in environment file templates
envs/cat_theo/transformer_ssm_lift/config.yaml,naming,MODEL_FILE,no reference in environment file templates
envs/cat_theo/transformer_ssm_lift/config.yaml,symptom_mask,TOLERANCE,placeholder referenced in environment file templates

## Selected axis results
environment,axis,level,control,recorded,eligible,passes,fails,rate,judge
categorical_lenses,naming,easy,"{""symptom_mask"": ""easy""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,naming,hard,"{""symptom_mask"": ""easy""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,naming,medium,"{""symptom_mask"": ""easy""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,naming,easy,"{""symptom_mask"": ""hard""}",1,1,0,1,0.0,behavioral_reference
categorical_lenses,naming,easy,"{""symptom_mask"": ""medium""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,symptom_mask,easy,"{""naming"": ""easy""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,symptom_mask,hard,"{""naming"": ""easy""}",1,1,0,1,0.0,behavioral_reference
categorical_lenses,symptom_mask,medium,"{""naming"": ""easy""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,symptom_mask,easy,"{""naming"": ""hard""}",1,1,1,0,1.0,behavioral_reference
categorical_lenses,symptom_mask,easy,"{""naming"": ""medium""}",1,1,1,0,1.0,behavioral_reference
compositional_optimizer,naming,easy,"{""symptom_mask"": ""easy""}",1,1,0,1,0.0,compile_only
compositional_optimizer,naming,hard,"{""symptom_mask"": ""easy""}",1,1,1,0,1.0,compile_only
compositional_optimizer,naming,medium,"{""symptom_mask"": ""easy""}",1,1,0,1,0.0,compile_only
compositional_optimizer,naming,easy,"{""symptom_mask"": ""hard""}",1,1,1,0,1.0,compile_only
compositional_optimizer,naming,easy,"{""symptom_mask"": ""medium""}",1,1,1,0,1.0,compile_only
compositional_optimizer,symptom_mask,easy,"{""naming"": ""easy""}",1,1,0,1,0.0,compile_only
compositional_optimizer,symptom_mask,hard,"{""naming"": ""easy""}",1,1,1,0,1.0,compile_only
compositional_optimizer,symptom_mask,medium,"{""naming"": ""easy""}",1,1,1,0,1.0,compile_only
compositional_optimizer,symptom_mask,easy,"{""naming"": ""hard""}",1,1,1,0,1.0,compile_only
compositional_optimizer,symptom_mask,easy,"{""naming"": ""medium""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,naming,easy,"{""symptom_mask"": ""easy""}",1,0,0,0,,compile_only
sheaf_physical_constraints,naming,hard,"{""symptom_mask"": ""easy""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,naming,medium,"{""symptom_mask"": ""easy""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,naming,easy,"{""symptom_mask"": ""hard""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,naming,easy,"{""symptom_mask"": ""medium""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,symptom_mask,easy,"{""naming"": ""easy""}",1,0,0,0,,compile_only
sheaf_physical_constraints,symptom_mask,hard,"{""naming"": ""easy""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,symptom_mask,medium,"{""naming"": ""easy""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,symptom_mask,easy,"{""naming"": ""hard""}",1,1,0,1,0.0,compile_only
sheaf_physical_constraints,symptom_mask,easy,"{""naming"": ""medium""}",1,1,0,1,0.0,compile_only

## Evidence Case Results Post-03
case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason
categorical_lenses__naming=easy_symptom_mask=easy__seed-0,categorical_lenses,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
categorical_lenses__naming=easy_symptom_mask=hard__seed-0,categorical_lenses,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",behavioral_reference,scored,FAIL,0.0,source_invalid,"[""Source validation failed:\nVIOLATIONS:\n  lenses.py: SyntaxError: expected an indented block after function definition on line 5 (lenses.py, line 9)\n\nNOTE: This validator is NOT a security sandbox. Docker isolation is.\nSome bypasses (getattr, string concat, etc.) are not caught here.\n\n""]",True,
categorical_lenses__naming=easy_symptom_mask=medium__seed-0,categorical_lenses,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
categorical_lenses__naming=hard_symptom_mask=easy__seed-0,categorical_lenses,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
categorical_lenses__naming=medium_symptom_mask=easy__seed-0,categorical_lenses,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",behavioral_reference,scored,PASS,1.0,pass,[],True,
compositional_optimizer__naming=easy_symptom_mask=easy__seed-0,compositional_optimizer,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",compile_only,scored,FAIL,0.0,patch_invalid,"[""Patch validation failed:\nFAIL: Patch file is empty\n\n""]",True,
compositional_optimizer__naming=easy_symptom_mask=hard__seed-0,compositional_optimizer,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",compile_only,scored,PASS,1.0,pass,[],True,
compositional_optimizer__naming=easy_symptom_mask=medium__seed-0,compositional_optimizer,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",compile_only,scored,PASS,1.0,pass,[],True,
compositional_optimizer__naming=hard_symptom_mask=easy__seed-0,compositional_optimizer,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",compile_only,scored,PASS,1.0,pass,[],True,
compositional_optimizer__naming=medium_symptom_mask=easy__seed-0,compositional_optimizer,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",compile_only,scored,FAIL,0.0,source_invalid,"[""Source validation failed:\nVIOLATIONS:\n  optimizer.py: Line 1: disallowed import 'weakref' (top-level 'weakref' not in allowlist)\n\nNOTE: This validator is NOT a security sandbox. Docker isolation is.\nSome bypasses (getattr, string concat, etc.) are not caught here.\n\n""]",True,
sheaf_physical_constraints__naming=easy_symptom_mask=easy__seed-0,sheaf_physical_constraints,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",compile_only,scored,FAIL,0.0,invalid_action,"[""provider transient failure after bounded retries""]",False,final result explicitly attributes terminal failure to provider transient after bounded retries
sheaf_physical_constraints__naming=easy_symptom_mask=hard__seed-0,sheaf_physical_constraints,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",compile_only,scored,FAIL,0.277778,underfit,[],True,
sheaf_physical_constraints__naming=easy_symptom_mask=medium__seed-0,sheaf_physical_constraints,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",compile_only,scored,FAIL,0.0,patch_invalid,"[""Patch validation failed:\nFAIL: Patch file is empty\n\n""]",True,
sheaf_physical_constraints__naming=hard_symptom_mask=easy__seed-0,sheaf_physical_constraints,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",compile_only,scored,FAIL,0.0,invalid_action,"[""Could not parse a valid JSON action""]",True,
sheaf_physical_constraints__naming=medium_symptom_mask=easy__seed-0,sheaf_physical_constraints,category_theoretic_compositional,category_theoretic_compositional,0,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",compile_only,scored,FAIL,0.277778,underfit,[],True,

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
categorical_lenses,5,5,4,1,0.8,5,4,1,0,0,0
compositional_optimizer,5,5,3,2,0.6,0,0,0,5,3,2
sheaf_physical_constraints,5,4,0,4,0.0,0,0,0,4,0,4

## Failure taxonomy
failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"

## Evidence Track Summary Post-03
track,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,provider_failure_exclusions,recorded_behavioral_reference,recorded_compile_only,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
category_theoretic_compositional,85,84,57,27,0.6785714285714286,1,5,80,5,4,1,79,53,26
[[[ END INPUT 01 — job:post03_prepare_post:response ]]]
