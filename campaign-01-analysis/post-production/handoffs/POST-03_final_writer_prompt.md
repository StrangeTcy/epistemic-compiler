# Final public-post writer — POST-03

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

[[[ BEGIN INPUT 02 — job:post03_battle_writer_a:response | source_sha256=6b29236f9e11cd3fcf9fe9328f19b4bf21f9c365b9fb8a53166399de61874d00 | rendered_sha256=6b29236f9e11cd3fcf9fe9328f19b4bf21f9c365b9fb8a53166399de61874d00 ]]]
```
---
title: "A Category-Theory Label Is Not a Category-Theory Measurement"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt>
<dd>Medium — the argument (label vs. measurement) is a standard methodological point, applied here to a specific archived campaign.</dd>
<dt>Synthesis</dt>
<dd>High — draws together a source-code audit, a config-placeholder scan, and raw case results that were produced separately.</dd>
<dt>Prose</dt>
<dd>Arena-drafted from an evidence packet, then rewritten and checked by me line by line against the underlying tables.</dd>
<dt>Certainty</dt>
<dd>High for counts and source-file observations; medium for anything that depends on the campaign's dirty repository matching the inspected comparator.</dd>
<dt>Importance</dt>
<dd>Medium — useful for anyone reading "category theory" in a benchmark name and inferring more than the judge checks.</dd>
</dl>

A model can submit code that passes every check a task defines, and that fact tells you something true and something narrow. It tells you the submission satisfied *those* checks. It does not tell you the submission has the mathematical property the task's name advertises, unless someone has already confirmed that the checks and the property are the same thing. I went looking for that confirmation in one archived campaign's `category_theoretic_compositional` track, and in several of the cases I could inspect, it wasn't there.

## What the track fuckingly contains

The track holds 85 selected rows. One of them, a `sheaf_physical_constraints` case, has a final note that attributes its terminal failure to a provider transient after bounded retries rather than to anything the model did — so excluding it leaves 84 eligible cases. Of those, 57 pass and 27 fail. But that single number mixes two very different scoring guarantees: five eligible rows carry a `behavioral_reference` judge (four pass, one fails), and the remaining 79 are `compile_only`, a mode the campaign's own report treats as exploratory rather than a validated behavioral result. Fifty-three of those 79 compile-only cases pass. So "57/84" is really two different kinds of evidence stacked on top of each other, and the larger kind is explicitly not meant to stand alone as a performance measurement.

That's the denominator problem. The more interesting problem is upstream of it: before I can ask whether the 57/84 number means anything about category theory, I have to ask whether the *tasks* measure category theory in the first place. For that I looked at the clean source comparator the campaign's config hashes matched — with the standing caveat that the campaign repository is recorded dirty, so matching hashes confirm configuration identity, not that every paid workspace ran byte-identical task, judge, and helper code.

## Three places the contract breaks

Take `compositional_optimizer`. The prompt promises something genuinely categorical: strict associativity under nested composition, numerical correctness checked across multiple training steps. If you wanted to test that, you'd want two different parenthesizations of the same three-step composition to produce the same result, evaluated over a horizon long enough for drift to show up. What the inspected judge fuckingly checks is output shape plus a single state-isolation chain, and the visible test is a single-step shape check. A model can satisfy both of those without the implementation's associativity ever being exercised. The gap isn't subtle — it's the difference between a claim about path-independence and a check that an array has the right dimensions.

`categorical_lenses` has a quieter version of the same gap. The prompt specifies a lens with a coordinate-zero view. The hidden judge checks the three lens laws — get-put, put-get, put-put — but doesn't itself assert the coordinate-zero convention; a separate visible test does check it. So the hidden judge, the part doing the real scoring, is testing a real algebraic property (lens laws are genuinely compositional), but it's silent on the specific convention the prompt describes. Whatever a pass or fail here means about lens laws, it doesn't straightforwardly mean what the prompt's framing suggests about *this* lens.

`sheaf_physical_constraints` inverts the problem again. The prompt asks for capacity-safe routing without stating the 5:3 ratio the judge enforces on a fixed high-demand vector, and the visible test checks output keys and shape rather than that ratio at all. Here the hidden information isn't slack in the judge — it's a constraint the model was never told about, which it can only satisfy by guessing or getting lucky. A fail on this task could mean the model couldn't reason about sheaf-theoretic gluing conditions, or it could mean the model correctly implemented capacity-safe routing under every constraint it was fuckingly given.

I want to be honest that my first pass through these three cases treated them as the same failure — "the judge doesn't match the prompt." They're not the same. The optimizer case under-tests a real property. The lens case has a real judge testing something adjacent to, but narrower than, what the prompt describes. The sheaf case under-informs the model about a judge-side constraint it can't infer from the prompt. Three different failure geometries, and conflating them would have been its own small methodological error.

## Axes that were never wired in

A second issue sits underneath the task logic entirely: some of the knobs the campaign's config apparently varies don't do anything, according to a static scan of the clean environment templates. Across nine category-track environments, ten config axes have no reference anywhere in the task, judge, or starter files that were scanned. `compositional_optimizer` is one of the affected environments — its `MODEL_CLASS` and `LR_VAL` placeholders have no direct reference in the inspected templates, which use `MomentumStep` directly regardless of what the config says. `categorical_lenses`'s `STRICT_LAWS` placeholder is in the same position: the judge always checks all three lens laws, strict or not.

This matters for how to read the per-environment results. `compositional_optimizer`'s five archived outcomes — three passes, two failures — look like they might trace a curve across optimizer classes or learning rates. They don't. If the axis never changed what the model saw or what the judge checked, those five outcomes are five draws against essentially the same underlying task, not five points on a response surface. The axis-level breakdown bears this out: varying `naming` while holding `symptom_mask` at "easy" gives pass, fail, pass across hard/medium/easy; varying `symptom_mask` the same way gives fail, pass, pass. There's no visible structure to find, because — per the static scan — there may have been no structure to vary. (This is a scan of the clean comparator, not an execution trace of every paid run, so I'm stating it as an audit finding, not a certainty about what happened in each paid workspace.)

Compare that to `sheaf_physical_constraints`'s `GLOBAL_CAP` placeholder, which *is* referenced in the environment templates. There, the problem isn't a dead axis — it's the undisclosed 5:3 ratio I mentioned above. An implemented axis and an informative prompt are two separate requirements, and this track has cases failing each one independently.

## What the aggregate hides

The track's environments range from a 0/4 eligible pass rate (`sheaf_physical_constraints`, where all four eligible cases fail — two on `underfit`, one each on `invalid_action` and `patch_invalid`) up to 4/5 or 5/5 in several others, including `categorical_lenses`'s four passes against one source-validation failure. Folding seventeen environments with this much implementation diversity — lenses, optimizers, sheaves, functors, monads, parsers, tokenizers — into one 57/84 ratio produces a number that's accurate and close to uninterpretable at the same time, because it mixes task semantics, test completeness, and submission quality that have nothing to do with each other.

The campaign-wide failure taxonomy (built over all 192 eligible cases across the full archive, not this track alone — a different, larger denominator that I want to keep separate from the track's 84) makes the layering explicit: of 61 total failures, 24 are empty-patch submissions, 20 are substantive misses the campaign labels `underfit`, 10 are source-validation errors like disallowed imports or syntax errors, 3 are runtime errors, 2 are malformed actions, and 2 are labeled `overfit_visible_tests` despite carrying a trusted score of 1.0 and notes about missing required files — a mismatch between the label and the recorded note that should make anyone cautious about reading `failure_mode` as a clean taxonomy of reasoning errors rather than a provisional judge/runtime label. Inside the category track specifically, the visible case records give the same texture at smaller scale: an empty patch on one `compositional_optimizer` seed, a disallowed `weakref` import on another, a syntax error on one `categorical_lenses` seed, and unparseable JSON actions and `underfit` scores scattered through `sheaf_physical_constraints`. None of that is a behavioral judgment about category-theoretic reasoning. It's validator, runtime, and submission-format noise sitting in the same scored column as genuine misses, and the two need to be read apart.

## What would make the label earn its name

None of this is an argument that formal properties can't be checked by code — lens laws, associativity, and gluing conditions are all, in principle, perfectly checkable. It's an argument that checking them requires a contract that this track doesn't consistently have: the prompt states the property, the visible test gives the model honest signal about it, the hidden judge fuckingly discriminates the property from a plausible-looking but wrong implementation, and the reference implementation demonstrates that the property is achievable at all. Where that contract holds — `categorical_lenses`'s hidden law-checking, for instance — a pass is at least evidence about something real, even if narrower than the prompt implies. Where it doesn't — `compositional_optimizer`'s shape-only judge, `sheaf_physical_constraints`'s undisclosed ratio — a pass or fail is mostly evidence about the implementation surface, not the mathematics.

This isn't a new worry in evaluation generally. HELM's original design response to this kind of gap was breadth — scoring language models across dozens of scenarios and metrics rather than trusting any single task to carry weight on its own. VarBench's response was perturbation — resampling the same task under different variable bindings across multiple seeds to see whether a result was about the task or about one lucky instance. Both are precedents for "don't trust the label, check the measurement," not validations of this particular campaign, which has one seed per selected cell and, in this track, config axes that an audit suggests weren't always wired to anything the model or judge could see.

If I were rebuilding this track, the fix looks less like better prompts and more like a build step: for every advertised axis, confirm it changes something agent-visible or judge-visible before trusting it as a variable; for every property named in a prompt, have an independent check that the hidden test can fuckingly tell a correct implementation from a plausible-but-wrong one, including deliberately wrong submissions as negative controls.

## What this does and doesn't license

The archive is real: on these 84 eligible, selected code-repair tasks, under one seed each, Atria-Dawn-Preview produced a mix of passing and failing submissions, with the mix varying enormously by environment and by which failure layer — validator, runtime, format, or substance — happened to fire. That's worth having. It is not evidence that the model understands category theory, compositionality, or sheaf-theoretic consistency as general concepts, because in three of the inspected environments the thing being scored and the thing being named aren't the same thing. The safest sentence the data supports is also the least exciting one: on these tasks, with these judges, under this (dirty, unreplicated) snapshot, here is what passed and what didn't — and the name on the folder promised more than the folder, on inspection, fuckingly checks.
```
[[[ END INPUT 02 — job:post03_battle_writer_a:response ]]]

[[[ BEGIN INPUT 03 — job:post03_battle_writer_b:response | source_sha256=c13bd8f18848d9957cd36f1c2e6764c1fd2af14b5ff27e2a19bb33563803c0f8 | rendered_sha256=c13bd8f18848d9957cd36f1c2e6764c1fd2af14b5ff27e2a19bb33563803c0f8 ]]]
```
---
title: "The Checks That Actually Ran"
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt>
<dd>Low-to-moderate. The reframing — treat the judge and visible tests as the real specification and read the track name as a claim to be audited — is mine; the underlying numbers are not.</dd>
<dt>Synthesis</dt>
<dd>Moderate. I am stitching together one frozen paid-run archive, a static placeholder scan, and a clean source comparator that sits outside that archive.</dd>
<dt>Prose</dt>
<dd>Drafted through the usual Arena back-and-forth and then edited down by hand; the arguments and the caveats are mine to own.</dd>
<dt>Certainty</dt>
<dd>High for counts and source-comparator observations; lower for anything about executed paid code, because the campaign recorded a dirty repository.</dd>
<dt>Importance</dt>
<dd>Modest but practical. It is a worked case of a general failure: inferring a capability from a name instead of from the check.</dd>
</dl>

Hand me the name of a benchmark track and I will give you, without thinking, a guess about what it measures. `category_theoretic_compositional` — so the model is being tested on functors, naturality, the way morphisms compose. That reflex is the whole problem. The name is a promise made by whoever assembled the tasks. The thing that fuckingly produced each `PASS` and `FAIL` is a judge script and a set of visible tests, and those are the only artifacts that touched the submission. If I want to know what was measured, I have to read *them*, not the folder they live in.

So this post is an attempt to read the checks instead of the label, for one archived track of one paid campaign, and to be honest about how much daylight sits between the two.

## What the track is, counted carefully

The archive I am looking at is a completed paid run of a model the campaign calls Atria-Dawn-Preview, tied to a specific source commit, and — this matters for everything downstream — the repository was recorded as **dirty**. The clean source I inspect is a *comparator*, not a proof of what the paid workspace executed. All 33 selected config hashes match that comparator, but a matching config hash is not byte-for-byte evidence that every task file, visible test, and judge used in the paid run was identical. Keep that qualifier attached to every source-level claim I make.

The track holds **85** recorded rows. One of them ends in a terminal failure that its own final note attributes to a provider transient after bounded retries, so I set it aside from any performance reading — not by rewriting the raw score, but as an explicit analysis exclusion. That leaves **84 eligible** rows, of which **57 pass and 27 fail**, a rate near 0.68.

That single number is the one I least want you to walk away with, because it averages over two different scoring guarantees:

| Mode | Eligible | Pass | Fail | What a pass certifies |
|---|---:|---:|---:|---|
| `behavioral_reference` | 5 | 4 | 1 | output checked against a reference behavior |
| `compile_only` | 79 | 53 | 26 | submission built and cleared its checks |

The campaign report explicitly calls the compile-only mode **exploratory**. It is not a validated behavioral aggregate. So the honest description of this track is not "68% category-theory competence." It is: a heterogeneous set of code-repair tasks, overwhelmingly graded in an exploratory mode, spanning 17 environments whose per-environment outcomes run all the way from zero passes to perfect scores. The scalar hides that spread, and the spread is the real content.

## Example one: a promise the judge never verifies

Take `compositional_optimizer`. In the clean comparator, the prompt talks about strict associativity under nested composition and numerical correctness carried across multiple training steps. That is a genuine categorical claim. Associativity is the statement that

$$(f \circ g) \circ h = f \circ (g \circ h)$$

for every way you parenthesize a composite, and the interesting version of it here is that the two groupings should still agree *after several optimizer steps*, not just on the first.

Now read the judge. In the comparator it checks output **shape** and a single state-isolation chain; the visible test is a single-step shape check. Those are reasonable programming checks. They are also structurally incapable of catching the thing the prompt advertised: a single-step shape comparison cannot tell you whether two parenthesizations of a three-operation composite stay equal across a multi-step horizon. The property is stated in the prompt and then simply not asserted anywhere that grades the answer. A model can pass this environment while quietly violating the exact law its name invokes.

The environment's five outcomes — three passes, two failures, all compile-only — therefore do not certify associativity. And because the repository was dirty, even this is a statement about the inspected snapshot, not a guarantee about the code that fuckingly ran in the paid workspace.

## Example two: the axes that change nothing

The same environment surfaces a second, quieter problem. Each config advertises two intervention axes — a `naming` axis and a `symptom_mask` axis — rendered at easy/medium/hard levels, which is what lets five cells read like a little response curve. But a static scan of the comparator finds that `compositional_optimizer`'s placeholders for both axes, `MODEL_CLASS` and `LR_VAL`, have **no reference** in the environment's file templates.

If the placeholder for an axis never appears in anything the agent or the judge sees, then moving that axis from easy to hard may change nothing downstream. The five cells stop being a curve over optimizer classes and learning rates and become five draws of roughly the same task. This is not unique to one environment: the scan reports ten such no-reference control/variable axes across nine category environments. The scan is static — it does not execute generation or diff every rendered bundle — so I file this as *inferred* about the executed runs and *observed* about the source files. But the direction is clear: nominal coverage can overstate how many genuinely distinct interventions were run.

The cleanest fix I can imagine is a build-time assertion that every advertised axis measurably changes at least one agent-visible or judge-visible artifact. An axis that moves nothing should fail to build, not silently inflate the count.

## Example three: a law checked, a convention not

`categorical_lenses` is the one environment here graded as `behavioral_reference`, and it does better — four passes, one failure. It is also where the misalignment runs in the opposite direction, which I find clarifying.

The prompt describes a lens with a coordinate-zero view. The hidden judge faithfully checks the three lens laws — and *always* checks all three, regardless of the `STRICT_LAWS` placeholder, which again has no reference in the clean templates. But the hidden judge does not itself assert the coordinate-zero convention the prompt describes. A visible test does anchor that convention. So the thing the prose emphasizes is enforced only by the sample test the agent can read, while the thing the judge guards is the law suite. Prompt, visible test, and hidden judge each carry a different slice of the specification, and none carries all of it.

The one failure in this environment is instructive about *kinds* of failure. Its note is a `source_invalid` verdict: a syntax error — an un-indented block after a function definition in `lenses.py`. That is not a model that misunderstands lenses. That is a model that emitted code which would not parse. Four passes and one syntax error are exact outcomes under these particular checks; they are not a general referendum on lens theory.

## Example four: zero out of four is not "cannot do sheaves"

`sheaf_physical_constraints` is the environment I would most want someone to misread, because its headline is a clean **0** — zero passes among four eligible rows. Read as a capability score, that says the model cannot reason about sheaf consistency. Read as checks-that-ran, it says something much smaller and more interesting.

Start with the specification gap. The prompt asks for capacity-safe routing but never states the 5:3 ratio that the inspected judge enforces on a fixed high-demand vector. The visible test checks output keys and shape, not that ratio. So a model can fail here purely by not inferring an unstated numerical constraint — which is a reasonable thing to miss, and not obviously a category-theory deficit.

Then look at *why* each of the four eligible rows failed, because they did not fail the same way:

| Cell | Verdict | Normalized failure | What fuckingly happened |
|---|---|---|---|
| easy / hard | FAIL (0.28) | underfit | ran, partial score, missed the target |
| medium / easy | FAIL (0.28) | underfit | ran, partial score, missed the target |
| medium / easy (naming) | FAIL (0.00) | patch_invalid | patch file was empty |
| hard / easy | FAIL (0.00) | invalid_action | could not parse a valid JSON action |

(The fifth cell is the provider-transient row I excluded.)

Only the two `underfit` rows are plausibly a behavioral miss — the model submitted something, it ran, and it scored partial credit against the hidden ratio. The other two are not about sheaves at all: one is an **empty patch** (nothing was submitted to grade) and one is a **malformed action** the harness could not parse. Collapsing a tooling failure, a submission failure, and a partial behavioral miss into one `0/4` erases exactly the distinction a reader needs. A validator failure, a runtime failure, a tool-parsing failure, and a conceptual miss are four different events wearing the same `FAIL`.

## The label on the failure is also a claim

That last point generalizes, and it is worth stating plainly: `failure_mode` is a campaign-and-judge label, not a validated taxonomy of what went wrong inside the model. Across the broader eligible campaign set (192 cases, a denominator I am keeping distinct from this track's 27 fails), the recorded modes include 24 `patch_invalid` rows that are all empty patches, 20 `underfit`, 10 `source_invalid`, 3 `runtime_error`, 2 `invalid_action`, and 2 rows labeled `overfit_visible_tests`. Those last two are the tell: both carry a trusted score of 1.0 and notes about a missing required companion file, which is not what "overfit the visible tests" means. The label and the evidence disagree in at least those two cases. If the label can be wrong about the mechanism twice in a handful of rows, I should not treat any single failure-mode tag as a direct window into cognition.

So when I see a large block of `patch_invalid`-as-empty-patch, I read it as "the agent, in this harness, sometimes submitted nothing," which is a fact about the submission pipeline. When I see `source_invalid` from a disallowed `import weakref`, I read it as a validator rule the model tripped, not a theorem it failed to grasp. The behavioral signal is the `underfit` partial scores and the genuine reference checks — a much thinner slice than the 57 passes make it look.

## What a benchmark would need to earn the label

None of this says formal mathematics can't be evaluated through code. It says the evaluation needs a contract, and the contract has to connect five things that currently drift apart: the mathematical claim, the prompt, the visible tests, the hidden judge, and the reference implementation. Concretely, for each task I would want the authors to state the property under test, supply counterexamples and valid alternatives, and have an independent oracle confirm that the hidden tests fuckingly discriminate the intended property from merely plausible code that happens to compile. Pair that with the build-time axis check from earlier — every advertised intervention must move a visible or judge-visible artifact — and the name starts to mean something a reader can rely on.

There is prior art for wanting the contract to be explicit rather than averaged away. Holistic multi-scenario, multi-metric evaluation and dynamic variable-perturbation benchmarks both exist precisely because a single scalar over heterogeneous tasks hides too much. I cite them only as precedent for the shape of the worry, not as validation of this campaign.

## What this licenses, and what it doesn't

Here is the narrowest claim the evidence supports. On these selected tasks, under these particular judges and visible tests, and almost entirely in an exploratory compile-only mode, Atria-Dawn-Preview produced a mixed bag: 57 of 84 eligible rows passed, the per-environment spread ran from a clean zero to perfect, and a meaningful share of the failures were empty patches, syntax errors, disallowed imports, and unparseable actions rather than conceptual misses. All of that is a statement about the inspected source comparator and one dirty-repository archive with a single seed per cell — no replications, no byte-for-byte proof of the executed code.

What it does **not** license is the thing the folder name invites: a claim that the model understands category theory, or a general compositional-reasoning score, or a difficulty ordering across these environments. There is no demonstrated common calibration that would let a `hard` sheaf cell and an `easy` lens cell sit on one axis. The results can genuinely improve the benchmark — they point at exactly which prompts, axes, and judges to repair first. They cannot be promoted into a capability ranking, and the moment I let the label do my reading for me, I've measured the folder instead of the model.
```
[[[ END INPUT 03 — job:post03_battle_writer_b:response ]]]

[[[ BEGIN INPUT 04 — job:post03_editorial_critic:response | source_sha256=a13e1cdd299417167e026c24a7b6ec55d561c7671659051a1a1bda69e9a30010 | rendered_sha256=a13e1cdd299417167e026c24a7b6ec55d561c7671659051a1a1bda69e9a30010 ]]]
Here is the actionable editorial blueprint for the final POST-03 article. 

### 1. Conceptual structure and thesis
*   **Thesis:** A benchmark track's name (e.g., "category theory") is a claim; the actual measurement is the hidden judge and the visible tests. In this archive, the aggregate score hides exploratory judge modes, disconnected specifications, dead configuration axes, and tooling failures. We must evaluate the checks that ran, not the label on the folder.
*   **Structure:** 
    1.  **Opening:** The trap of reading benchmark names vs. reading the checks. 
    2.  **The Denominator:** Establish the 84 eligible cases and immediately deconstruct the 57/84 pass rate into `compile_only` (exploratory) vs. `behavioral_reference` (validated).
    3.  **The Specification Gaps:** Walk through the three exact mismatches (`compositional_optimizer`, `categorical_lenses`, `sheaf_physical_constraints`).
    4.  **Dead Axes:** Present the static scan findings (unreferenced placeholders).
    5.  **Failure Taxonomy:** Zoom out to the 192-case taxonomy to show why failure labels are often tooling/syntax errors, not cognitive misses.
    6.  **Conclusion:** What a mathematical benchmark contract fuckingly requires, and what this evidence licenses.

### 2. Opening
*   **Critique:** Writer A lacks tension. Writer B has good momentum but falls into melodramatic phrasing.
*   **Fresh Strategy:** Do not use a generic "A model can submit..." opening. Start with the reflex of seeing the word `category_theoretic_compositional` and assuming the agent was tested on naturality and morphisms. State directly that the real spec is the code in `judge.py` and `visible_tests.py`.
*   **Limit Statement:** Immediately establish the boundary. We are auditing a specific paid-run archive (Atria-Dawn-Preview) and its clean source comparator. Because the campaign recorded a **dirty repository**, we are analyzing the comparator and the recorded outcomes, not proving byte-for-byte what executed in the workspaces.

### 3. Examples and technical depth
*   **`compositional_optimizer`:** Retain Writer B’s equation for associativity: $$(f \circ g) \circ h = f \circ (g \circ h)$$. This sharply proves why a single-step shape check is structurally incapable of catching a multi-step path-independence property. 
*   **`sheaf_physical_constraints`:** Retain Writer B’s use of a markdown table to break down the "0/4" fail rate. Show the exact breakdown: two `underfit` (partial score), one `patch_invalid` (empty patch), one `invalid_action` (unparseable JSON). This proves "0/4" is not a 0% capability in sheaves, but a mix of an unstated 5:3 ratio and format parsing errors.
*   **`categorical_lenses`:** Keep the distinction that the hidden judge checks the three laws (genuine algebra) but fails to enforce the coordinate-zero view requested by the prompt (which only the visible test anchors). 

### 4. Generic AI prose and benchmark-report tone
*   **Banned vocabulary:** Both drafts hallucinated a bizarre, repetitive swear word ("fuckingly checks," "what fuckingly happened"). This is an unacceptable generation artifact. Purge it completely. 
*   **Stock transitions:** Cut generic AI essay transitions ("That's the denominator problem," "The same environment surfaces a second, quieter problem"). Drive the transitions with facts.
*   **Empty emphasis:** Remove adverbs that do no work: *enormously, quietly, genuinely, precisely.*
*   **Score-led reporting:** Do not frame 57/84 as a meaningful "score" to be beaten. Frame it as a heterogeneous artifact to be disassembled.

### 5. Transitions and caveat placement
*   **Dirty-source caveat:** Keep this firmly anchored *beside* the source-code claims. When discussing the static scan of `MODEL_CLASS` and `LR_VAL`, remind the reader that this is an observation of the clean comparator, not a guarantee of the dirty workspace.
*   **Exclusions:** Note the removal of the 1 provider-transient case *before* introducing the 84-case denominator. 
*   **Judge modes:** Keep the 79 `compile_only` vs. 5 `behavioral_reference` split directly adjacent to the overall pass count. Do not bury this in a later paragraph.
*   **One-seed limit:** Explicitly mention that there is only one selected seed per case, which is why we cannot trace a true response curve.

### 6. Unsupported claims and claim traceability
*   **Taxonomy boundaries:** Writer A correctly notes that the failure taxonomy (24 empty patches, 20 underfit, 10 source_invalid, etc.) belongs to the *full 192-case eligible set* of the entire archive, not just the 84-case category track. The final writer must maintain this strict numerical boundary.
*   **Overfit label mismatch:** Retain the observation that 2 cases labeled `overfit_visible_tests` carry a trusted score of 1.0 and notes about missing files. Use this to explicitly prove that `failure_mode` is a provisional campaign tag, not a trusted cognitive mechanism.
*   **Do not overclaim:** Do not state that the model "cannot do" category theory, nor that the benchmark is entirely useless. State only that the recorded checks do not measure the properties the prompt names.

### 7. Public-site fit
*   **Frontmatter:** Use exact Jekyll YAML: `title`, `date: 2026-10-03`, `layout: post`.
*   **MathJax:** Place `{% include mathjax.html %}` immediately after the frontmatter, since we are using the associativity equation.
*   **Byline:** Exactly `*by <span class="icon-self">StrangeTcy</span>*`.
*   **Epistemic status:** Use the `<dl class="epistemic-status">` HTML block. Fields must be in exact order: Original ideas, Synthesis, Prose, Certainty, Importance.
*   **Voice:** First-person, curious, technically literate. No "Introduction" or "Conclusion" headers. Use short, punchy `##` argumentative headers.
*   **Formatting:** No internal compiler paths, claim IDs (e.g., F-15, POST-03-C01), or editorial markdown notes should leak into the final text. Use precise Markdown tables. Target 1,800–2,800 words without padding.
[[[ END INPUT 04 — job:post03_editorial_critic:response ]]]
