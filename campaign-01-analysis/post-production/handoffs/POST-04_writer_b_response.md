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
