# Compiler evidence packet — POST-02

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## BEGIN INPUT ARTIFACT: 01 — source_draft_POST-02
Source snapshot SHA-256: `eeea2454b3b15e67568a54efc9f1ddd2e3b06e560be15f5fac1a6a78e6903964`
Rendered message SHA-256: `eeea2454b3b15e67568a54efc9f1ddd2e3b06e560be15f5fac1a6a78e6903964`
Original reference: `mission:source_draft_POST-02`

# POST-02 — Seven correct Bayesian answers are not seven recursive strategists

**Dek:** The selected epistemic-games cases were answered perfectly. The task source, however, defines inference over specified behavioral policies—not an engine for recursive strategic reasoning.

**Draft**

A model can calculate what an observation says about two possible worlds without reasoning recursively about what one player believes another player believes. The distinction matters in the `epistemic_games` results from this campaign.

The archived Atria-Dawn-Preview run passes all seven selected `epistemic_games` cases, with score 1.0 in each final result. The judge records the posterior, likelihood-ratio verdict, most-supported world, consistency, and provenance checks; all required checks pass. Examples of the exact posterior values in the final results include 1/2, 3/5, 1/15, and 92/177. These are observed task-level outcomes for seven selected seed-0 instances—not an estimate across models, seeds, or a broad theory-of-mind population. ⟦POST-02-C01 · F-07⟧

The source code defines two hypotheses, priors over those worlds, an observed announcement, and a likelihood table for each stipulated behavior policy. The posterior is computed as:

> P(W1 | o) = P(o | W1) P(W1) / [P(o | W1) P(W1) + P(o | W2) P(W2)]

The judge checks whether the submitted answer matches the resulting posterior and whether the accompanying verdict and most-supported-world label are internally consistent. That is a well-specified Bayesian calculation, and the archived answers are correct on the selected cases. ⟦POST-02-C02 · F-07⟧

But the task’s “genuine” and “strategic” labels should not be mistaken for a demonstrated recursive policy solver. The inspected `core.py` says explicitly that v0 does not implement a fully recursive level-k engine with utilities and recursive belief updates. It supplies the likelihoods directly through an evidence table. Its own design description characterizes the target as “Bayesian inference over two specified behavioral policies, presented through genuine-versus-strategic narratives.” The story motivates the inference problem; it does not make the likelihood table a product of the model’s recursive strategic reasoning. These implementation statements follow the inspected clean source comparator; the campaign records `repository.dirty=true`, so exact paid-run source identity remains unresolved. ⟦POST-02-C03 · F-01/F-07⟧

That boundary is especially important in the paired-world cases. In the ambiguous-evidence condition, both worlds can produce the observation with equal likelihood. The correct conclusion is non-identifiability, not confidence in whichever narrative sounds more plausible. The selected balanced-prior cases return 1/2; the skewed-prior case returns 3/5. For the strong and weak evidence cases, the judge separately checks the posterior value and whether the evidence belongs in the appropriate likelihood-ratio band. ⟦POST-02-C04 · F-07⟧

The result is therefore meaningful, but bounded: the model produced exact answers on a small, public, deterministic family with a reference behavior table and a public Bayesian oracle self-test. The archive contains no evidence that the model inferred the policy table itself, generated an opponent model, or recursively updated beliefs over multiple strategic agents. Nor does a passing result reveal which internal procedure produced the answer. ⟦POST-02-C05 · F-04/F-07⟧

This is not a claim that epistemic evaluation is unimportant. Prior work already uses dynamic epistemic logic to isolate controlled theory-of-mind problems in MindGames, targets higher-order recursive beliefs and deception in Hi-ToM, and uses causal templates to generate social-reasoning evaluations in BigToM. Those are distinct tasks and methods; their relevance here is that a seven-item Bayesian-calculation result should not be presented as a new recursive ToM benchmark or as evidence that the same construct was measured. ([MindGames](https://aclanthology.org/2023.findings-emnlp.303/); [Hi-ToM](https://aclanthology.org/2023.findings-emnlp.717/); [BigToM](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and-Benchmarks.pdf)). ⟦POST-02-C06 · F-17⟧

A stronger follow-up would keep the current Bayesian cases as calibration and add a separately specified recursive task: define base policies, utilities, observer/player alternation, belief-update rules, and how those generate public actions. It should test unseen likelihood tables and multiple seeds, and include counterfactual cases where a narrative cue conflicts with the supplied evidence. The benchmark should then score the final inference separately from evidence that the model reconstructed the policy or recursion. ⟦POST-02-C07 · F-07⟧

For now, the accurate headline is narrower and still positive: **Atria-Dawn-Preview answered all seven selected Bayesian-inference cases correctly under the policies specified by the task implementation.** The result supports competence on those bounded calculations. It does not establish recursive strategic reasoning. ⟦POST-02-C08 · F-07⟧

**Editor’s note:** Evidence tags and source paths are internal provenance markers; see the claim-traceability sheet before removing them.

## END INPUT ARTIFACT: 01 — source_draft_POST-02

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
Rendered message SHA-256: `7d33eb6ed595d751cd72d4e5ef6578da96ededdc6cae7a22fc95b4e8942890a4`
Original reference: `mission:references`

Prior-work references from the supplied campaign bibliography; context only, not validation of this campaign.

- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: 42 scenarios and multiple metrics. https://arxiv.org/abs/2211.09110
- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation; five sampled runs (seeds 40–44) for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/

This targeted reference check supports no “first” or exhaustive-novelty claim.

## END INPUT ARTIFACT: 04 — references

## BEGIN INPUT ARTIFACT: 07 — trace_rows_POST-02
Source snapshot SHA-256: `40abbbb39f0b435e9e77e79f50202460a7db4834cd887477d7b845a6e84d0ce9`
Rendered message SHA-256: `2324a801d51ead461fb2d962213eada535b938f189edc92900de35792ce6a423`
Original reference: `mission:trace_rows_POST-02`

post_id,claim_id,finding_ids
POST-02,POST-02-C01,F-07
POST-02,POST-02-C02,F-07
POST-02,POST-02-C03,F-01;F-07
POST-02,POST-02-C04,F-07
POST-02,POST-02-C05,F-04;F-07
POST-02,POST-02-C06,F-17
POST-02,POST-02-C07,F-07
POST-02,POST-02-C08,F-07

## END INPUT ARTIFACT: 07 — trace_rows_POST-02

## BEGIN INPUT ARTIFACT: 08 — relevant_findings_POST-02
Source snapshot SHA-256: `0cd1bb194592dc77e92fce37bf1730470d98aa2c74618dd7210caebf192b7f1d`
Rendered message SHA-256: `40ffe397ecf500600a416b35e871d101e25443a671566eee76bdfb10ab04e91e`
Original reference: `mission:relevant_findings_POST-02`

{"claim_ids":["POST-02-C01","POST-02-C02","POST-02-C03","POST-02-C04","POST-02-C05","POST-02-C06","POST-02-C07","POST-02-C08"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The archive assigns all seven epistemic_games cases to the recorded ml_debugging track, although the inspected task core implements symbolic Bayesian inference.","confidence":"HIGH for recorded label; HIGH that task semantics are symbolic Bayesian inference in the comparator; MEDIUM for whether the recorded grouping was intentionally multi-purpose.","id":"F-05","limitations":["The analysis_family override is an explicit editorial regrouping; the raw track is preserved unchanged.","A dirty source tree limits claims about the exact executed task code."],"quantitative_result":"Recorded track summary: ml_debugging 37 cases, 16 PASS/21 FAIL. Source-semantic regrouping: 30 ML-debugging cases, 9 PASS/21 FAIL; epistemic_games separate at 7/7 PASS.","status":"OBSERVED"},{"claim":"Atria-Dawn-Preview returned fully correct answers on the seven selected epistemic_games instances, whose source defines Bayesian inference over two specified behavioral policies rather than a recursive level-k process.","confidence":"HIGH for the recorded task-level outcomes and source-described target; MEDIUM for generalization to the executed tree due dirty-source provenance.","id":"F-07","limitations":["Seven instances, one seed, one model/configuration; only one solo presentation and one skewed prior.","The policies and likelihood tables are stipulated and public; there is no recursively generated strategic agent with utilities and alternating beliefs."],"quantitative_result":"7/7 PASS, score 1.0; each final result records exact posterior credit, correct likelihood-ratio verdict, correct most-supported world, provenance_ok=true, and all_correct=true. The selected exact posteriors include 1/2, 3/5, 1/15, and 92/177.","status":"OBSERVED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-02","schema_version":1,"trace_finding_ids":["F-01","F-04","F-07","F-17"]}

## END INPUT ARTIFACT: 08 — relevant_findings_POST-02

## BEGIN INPUT ARTIFACT: 09 — evidence_extract_POST-02
Source snapshot SHA-256: `b276f9e3564eb7cb8e3a016684dffa58763ac6252de85e7840941f553a58a8dc`
Rendered message SHA-256: `b1f18fc5b56446429645f80a557acdc0724885c08f5f486b399794c8db01b92c`
Original reference: `mission:evidence_extract_POST-02`

Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## END INPUT ARTIFACT: 09 — evidence_extract_POST-02

## BEGIN INPUT ARTIFACT: 10 — limitations_POST-02
Source snapshot SHA-256: `7fcc58d4ce9331cf23a1a2d1f143627110749b0f6dc2245a36a33af51c7f6bd6`
Rendered message SHA-256: `7fcc58d4ce9331cf23a1a2d1f143627110749b0f6dc2245a36a33af51c7f6bd6`
Original reference: `mission:limitations_POST-02`

# Limitations to preserve — Two Policies, One Posterior, No Recursive Strategist

1. The empirical result is seven selected cases, one seed, one provider/model/configuration; do not generalize to a model population.
2. All seven cases use specified, public behavioral policies and likelihood tables; the task does not ask the model to infer a policy-generating process.
3. The inspected task source explicitly excludes a fully recursive level-k engine with utilities and recursive belief updates.
4. Correct outputs do not identify the model's internal algorithm; formula/pattern recognition remains an alternative.
5. The exact posterior outputs are verified in final results; do not estimate or invent other fractions.
6. A public Bayesian oracle self-test is recorded for this task, but its existence does not prove independent validation of other environments or internal reasoning.
7. The raw track label places the seven cases under `ml_debugging`; analysis separates them semantically without rewriting the archived label.
8. Source implementation claims rely on the clean comparator; the campaign records `repository.dirty=true`.
9. MindGames, Hi-ToM, and BigToM are distinct prior work, not direct score comparators or equivalent versions of the same task.
10. Do not call the result recursive ToM, general theory of mind, social reasoning, or a new ToM benchmark.

## END INPUT ARTIFACT: 10 — limitations_POST-02

## BEGIN INPUT ARTIFACT: 11 — source_audit_POST-02
Source snapshot SHA-256: `168935bd41f48a2c281a43aa4c6a5d83ef78e8d89c4e86f1098b264adf691beb`
Rendered message SHA-256: `a3b7c00b7463d5d3936a61b0d9c6f768f6085d52580baec5b29227b90e8cd8e8`
Original reference: `mission:source_audit_POST-02`

## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## END INPUT ARTIFACT: 11 — source_audit_POST-02

## BEGIN INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-02
Source snapshot SHA-256: `30c966fff429a3d634ef6eca92b3e167af55ceee459176ffe9b758381d6d86ee`
Rendered message SHA-256: `7a760d05b68c06da4b292c6d605e1eee8ec428a76990b4f0443a43ff069ab770`
Original reference: `mission:evidence_analysis_family_summary_POST-02`

analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0

## END INPUT ARTIFACT: 12 — evidence_analysis_family_summary_POST-02

## BEGIN INPUT ARTIFACT: 13 — evidence_axis_summary_POST-02
Source snapshot SHA-256: `ef2e3448ac367023c5705cd38bad376f03ee81092ff7abf3c73cafa11e8c2fd3`
Rendered message SHA-256: `874d6e2ce7a450e0ca82be1e1fcae48dda01587ca3720240e22a6a8e8f9690ae`
Original reference: `mission:evidence_axis_summary_POST-02`

environment,axis,level,control,recorded,eligible,passes,fails,rate,judge
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,strong,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,weak,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,narrative,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""strong"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""weak"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,solo,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,skewed,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,trap,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference

## END INPUT ARTIFACT: 13 — evidence_axis_summary_POST-02

## BEGIN INPUT ARTIFACT: 14 — evidence_case_results_POST-02
Source snapshot SHA-256: `d3f6e76008fdbdf2e85f5959a366aae6a53a7fd8004fd98bab0dcfdd086860d6`
Rendered message SHA-256: `ed866423d860ab58658cbfbbdf9b25122a017c898a26f378e2d26aa0194343b8`
Original reference: `mission:evidence_case_results_POST-02`

case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=balanced_framing=narrative__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=skewed_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.6 vs true 3/5 (0.6000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='world1' vs true 'world1'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=solo_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=strong_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.0666667 vs true 1/15 (0.0667); reported verdict='distinguishable' vs true 'distinguishable'; reported support='world2' vs true 'world2'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=weak_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.519774 vs true 92/177 (0.5198); reported verdict='weakly_distinguishable' vs true 'weakly_distinguishable'; reported support='world1' vs true 'world1'; consistent=True; strict=True""]",True,
epistemic_games__scenario=trap_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,

## END INPUT ARTIFACT: 14 — evidence_case_results_POST-02

## BEGIN INPUT ARTIFACT: 15 — evidence_environment_summary_POST-02
Source snapshot SHA-256: `a29d015640d99e171cb2a861df5759b23503073e204bf690d8d72be8dfb7df76`
Rendered message SHA-256: `51dc35de1f6e6c762469bce8dc64f233bc3908e992ecd0c347bb6a3c15564d37`
Original reference: `mission:evidence_environment_summary_POST-02`

environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0

## END INPUT ARTIFACT: 15 — evidence_environment_summary_POST-02

## BEGIN INPUT ARTIFACT: 16 — evidence_failure_taxonomy_POST-02
Source snapshot SHA-256: `49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4`
Rendered message SHA-256: `379b2b331fd20d910a3cbf6277cf82680f95fd19c160fc8042c8b3fd5f9d12b5`
Original reference: `mission:evidence_failure_taxonomy_POST-02`

failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"

## END INPUT ARTIFACT: 16 — evidence_failure_taxonomy_POST-02

## Compiler-only validator metadata (never copy into public copy)
<!-- POST_PRODUCTION_VALIDATOR_METADATA
{"allowed_numbers": ["0", "0.03278688524590164", "0.04918032786885246", "0.0666667", "0.0667", "0.16393442622950818", "0.32786885245901637", "0.39344262295081966", "0.5", "0.5000", "0.519774", "0.5198", "0.6", "0.6000", "1", "1.0", "10", "120", "122", "15", "16", "17", "177", "2", "20", "21", "24", "256", "2968", "3", "30", "33", "37", "4", "40", "42", "44", "45", "47", "5", "56", "6", "7", "7.8", "7.8%", "72", "75", "8", "9", "92"], "evidence_input_sha256": {"mission:campaign_provenance": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "mission:evidence_analysis_family_summary_POST-02": "30c966fff429a3d634ef6eca92b3e167af55ceee459176ffe9b758381d6d86ee", "mission:evidence_axis_summary_POST-02": "ef2e3448ac367023c5705cd38bad376f03ee81092ff7abf3c73cafa11e8c2fd3", "mission:evidence_case_results_POST-02": "d3f6e76008fdbdf2e85f5959a366aae6a53a7fd8004fd98bab0dcfdd086860d6", "mission:evidence_environment_summary_POST-02": "a29d015640d99e171cb2a861df5759b23503073e204bf690d8d72be8dfb7df76", "mission:evidence_extract_POST-02": "b276f9e3564eb7cb8e3a016684dffa58763ac6252de85e7840941f553a58a8dc", "mission:evidence_failure_taxonomy_POST-02": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "mission:house_style": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "mission:limitations_POST-02": "7fcc58d4ce9331cf23a1a2d1f143627110749b0f6dc2245a36a33af51c7f6bd6", "mission:references": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "mission:relevant_findings_POST-02": "0cd1bb194592dc77e92fce37bf1730470d98aa2c74618dd7210caebf192b7f1d", "mission:source_audit_POST-02": "168935bd41f48a2c281a43aa4c6a5d83ef78e8d89c4e86f1098b264adf691beb", "mission:source_draft_POST-02": "eeea2454b3b15e67568a54efc9f1ddd2e3b06e560be15f5fac1a6a78e6903964", "mission:style_reference_material": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "mission:trace_rows_POST-02": "40abbbb39f0b435e9e77e79f50202460a7db4834cd887477d7b845a6e84d0ce9", "mission:workflow_input_manifest": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158"}, "finding_ids": ["F-01", "F-04", "F-05", "F-07", "F-17"], "post_id": "POST-02", "publication_date": "2026-10-03", "source_input_records": [{"attachment_index": 0, "reference": "mission:source_draft_POST-02", "sha256": "eeea2454b3b15e67568a54efc9f1ddd2e3b06e560be15f5fac1a6a78e6903964", "size_bytes": 5377, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/source_draft.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/source_draft.md"}, {"attachment_index": 1, "reference": "mission:house_style", "sha256": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973", "size_bytes": 12397, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/house_style.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/house_style.md"}, {"attachment_index": 2, "reference": "mission:style_reference_material", "sha256": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4", "size_bytes": 19939, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/style_reference_material.md"}, {"attachment_index": 3, "reference": "mission:references", "sha256": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0", "size_bytes": 3532, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/references.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/references.md"}, {"attachment_index": 4, "reference": "mission:campaign_provenance", "sha256": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9", "size_bytes": 13690, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/campaign_provenance.md"}, {"attachment_index": 5, "reference": "mission:workflow_input_manifest", "sha256": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158", "size_bytes": 28349, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/shared/workflow_input_manifest.json"}, {"attachment_index": 6, "reference": "mission:trace_rows_POST-02", "sha256": "40abbbb39f0b435e9e77e79f50202460a7db4834cd887477d7b845a6e84d0ce9", "size_bytes": 5619, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/trace_rows.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/trace_rows.csv"}, {"attachment_index": 7, "reference": "mission:relevant_findings_POST-02", "sha256": "0cd1bb194592dc77e92fce37bf1730470d98aa2c74618dd7210caebf192b7f1d", "size_bytes": 23469, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/relevant_findings.json", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/relevant_findings.json"}, {"attachment_index": 8, "reference": "mission:evidence_extract_POST-02", "sha256": "b276f9e3564eb7cb8e3a016684dffa58763ac6252de85e7840941f553a58a8dc", "size_bytes": 1501, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence_extract.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence_extract.md"}, {"attachment_index": 9, "reference": "mission:limitations_POST-02", "sha256": "7fcc58d4ce9331cf23a1a2d1f143627110749b0f6dc2245a36a33af51c7f6bd6", "size_bytes": 1376, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/limitations.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/limitations.md"}, {"attachment_index": 10, "reference": "mission:source_audit_POST-02", "sha256": "168935bd41f48a2c281a43aa4c6a5d83ef78e8d89c4e86f1098b264adf691beb", "size_bytes": 5098, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/source_audit_excerpt.md", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/source_audit_excerpt.md"}, {"attachment_index": 11, "reference": "mission:evidence_analysis_family_summary_POST-02", "sha256": "30c966fff429a3d634ef6eca92b3e167af55ceee459176ffe9b758381d6d86ee", "size_bytes": 387, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/analysis_family_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/analysis_family_summary.csv"}, {"attachment_index": 12, "reference": "mission:evidence_axis_summary_POST-02", "sha256": "ef2e3448ac367023c5705cd38bad376f03ee81092ff7abf3c73cafa11e8c2fd3", "size_bytes": 11547, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/axis_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/axis_summary.csv"}, {"attachment_index": 13, "reference": "mission:evidence_case_results_POST-02", "sha256": "d3f6e76008fdbdf2e85f5959a366aae6a53a7fd8004fd98bab0dcfdd086860d6", "size_bytes": 10078, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/selected_case_results.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/selected_case_results.csv"}, {"attachment_index": 14, "reference": "mission:evidence_environment_summary_POST-02", "sha256": "a29d015640d99e171cb2a861df5759b23503073e204bf690d8d72be8dfb7df76", "size_bytes": 383, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/environment_summary.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/environment_summary.csv"}, {"attachment_index": 15, "reference": "mission:evidence_failure_taxonomy_POST-02", "sha256": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4", "size_bytes": 6231, "snapshot_path": "campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/failure_taxonomy.csv", "source_path": "/home/user/epistemic-compiler/campaign-01-analysis/post-production/source_snapshots/POST-02/evidence/failure_taxonomy.csv"}], "trace_row_ids": ["POST-02-C01", "POST-02-C02", "POST-02-C03", "POST-02-C04", "POST-02-C05", "POST-02-C06", "POST-02-C07", "POST-02-C08"]}
-->
