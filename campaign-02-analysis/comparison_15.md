grok 4.5:

```html
---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Treat a difficulty label as a measurement claim to be checked, not an ordering supplied by the label itself.</dd>
  <dt>Synthesis</dt>
  <dd>Analysis of the archived Mercury-2.5 evidence packet. No additional cases were run.</dd>
  <dt>Prose</dt>
  <dd>Written from the evidence dossier and its adversarial review.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded counts and sequences; low for any claim about difficulty effects. Each selected cell has one seed and no replication.</dd>
  <dt>Importance</dt>
  <dd>A configuration sweep cannot locate a capability threshold until its axis, outcomes, and variation are measured.</dd>
</dl>

Pass, fail, pass is an inviting shape. It suggests a model that succeeds on a small problem, breaks somewhere in the middle, then recovers when the problem grows.

The Mercury-2.5 evidence packet contains that sequence in MoCo, alongside related sequences in CSS state machines and SQL fixed points—but these are selected, single-seed observations, not estimates of a difficulty curve. Some of the recorded failures concern source validation rather than demonstrated failure on the task’s semantic requirements.

The deeper finding is methodological: **the archive does not establish that its difficulty labels form a validated ordinal scale.** Its axes change different task properties, and its one-seed-per-cell design provides no replicated basis for identifying a threshold.

That is narrower than discovering an unexpected valley in model capability. It is also more useful. Before asking where Mercury breaks, I need to know what the horizontal axis measures and what the vertical axis certifies.

## What was recorded

The campaign selected **416 cases**, scored **405**, and recorded **277 PASS** and **128 FAIL**, for a scored-case pass rate of **0.684** across **38 environments** (F-004). That rate describes scored cases, not every selected case. The **11** selected-but-unscored cases remain outside its denominator. These are campaign totals, not results specific to the transition examples.

The environment × difficulty-tuple matrix has **340 rows**, each identified by an environment and a difficulty tuple. Its fields include case counts, scored counts, pass and fail counts, pass rates, failure modes, and judge guarantees. Cases, matrix rows, and matched difficulty sweeps are therefore different units; the row count is not a count of independent opportunities to observe a reversal. Each selected cell used seed-0, with no replication.

!

*Figure 1. Selected environment × difficulty-tuple rows. Cell labels give passes over scored cases; grey denotes unscored cases, not zero passes. The display does not enumerate all eligible three-level sweeps.*

For this essay, the selection rule is simple: report the three contrasts explicitly identified in F-008. The packet gives neither a prespecified search rule nor an exhaustive count of complete, comparable three-level sweeps in the 340-row matrix. These examples therefore cannot tell us how prevalent reversals are.

| Environment | Setting varied | Recorded sequence | What the sequence does **not** establish |
| --- | --- | --- | --- |
| MoCo | Visible-test level | PASS → FAIL → PASS | A change in pass probability, from one outcome at each level. |
| CSS state machine | Bit count, at the easy-surface label: 3 → 4 → 5 bits | Partial score → source-validation failure → PASS | A binary pass/fail/pass curve: the first result is partial, and the middle result stops at source validation. |
| SQL fixed points | Graph-chain length: 6 → 12 → 25 | PASS → source-validation failure → PASS | A behavioral failure at length 12 or a threshold between the sparsely sampled lengths. |

These are not interchangeable observations. Only the MoCo sequence is an unambiguous binary zigzag in the supplied description. The CSS partial score is not documented as a binary PASS; neither source-validation failure tells us how valid code would have performed on the task.

!

*Figure 2. Selected sequences across MoCo visible-test levels, CSS bit counts, and SQL graph-chain lengths. Lines connect recorded outcomes for legibility; with seed-0 alone in each selected cell, they are not fitted pass-rate curves.*

## An axis is not a common unit of difficulty

The packet’s axis definitions (unverified beyond the supplied descriptions) describe different interventions:

- **MoCo visible-test level changes test coverage.** This changes how a submission is examined; it is not automatically a measure of how difficult the submission was to construct. Visible-test coverage does not even specify a direction without knowing how the changed tests affect the information available to the solver and the conditions checked.
- **CSS bit count at the easy-surface setting.** The quoted sequence concerns bit count (3 → 4 → 5) while the surface label remains easy.
- **SQL graph-chain length.** A longer chain is an ordered structural parameter, but the packet does not calibrate that parameter against a replicated success probability.
- **Regex input-string lengths of 32, 128, and 512 characters.** Those lengths define an axis in the packet; the supplied evidence gives no corresponding outcome sequence, so none is inferred here.

Calling these settings “difficulty” does not make them measurements of the same quantity. More test coverage, more state bits, a longer graph chain, and a longer input string can each matter, but they matter through different mechanisms. This cross-environment mismatch explains why a shared “easy to hard” x-axis is unjustified. It does **not** explain why the middle MoCo cell failed.

That heterogeneity does **not** explain the within-environment reversals. Different axes across environments cannot tell us why a particular CSS submission failed validation or why a particular MoCo run failed between two passes. It tells us why pooling their labels into a common difficulty scale would require additional justification.

The distinction also applies within an environment. A parameter can have a clear numerical order without its effect on model performance having been measured. Conversely, an occasional reversal would not disprove a genuinely ordered difficulty manipulation: even monotonically declining success probabilities can produce non-monotonic sequences of individual outcomes.

For MoCo, even proof that test suites were nested would establish an implication only for a **fixed submission**: passing a larger suite would imply passing its subset. It would not require separately generated submissions at successive settings to produce monotonic outcomes.

The archive therefore neither validates a common latent difficulty scale nor disproves every possible one. It leaves that validation undone.

## A reversal is an observation, not a curve

A simple calculation shows why a reversal alone is weak evidence.

Suppose, purely as an illustration, that three binary outcomes were independent and had the same pass probability \(p\) at every level. The probability of either PASS–FAIL–PASS or FAIL–PASS–FAIL would be

\[
p(1-p).
\]

Using the campaign’s scored-case fraction, \(p = 277/405 \approx 0.684\), gives approximately **21.6%**. That percentage is a hypothetical calculation derived from F-004 under artificial assumptions, **not a measured reversal rate or a calibrated null model for this campaign**.

The assumptions matter. The campaign pools heterogeneous environments and judge guarantees; independence is not established; the examples were not supplied through a declared exhaustive selection procedure; and the CSS sequence is not resolved into three binary outcomes. The calculation only demonstrates that a flat success probability can readily produce an apparently interesting shape. Even if an environment’s underlying chance of success decreased steadily with a task-size setting, one outcome per setting could still zigzag. The MoCo trace neither proves nor rules out such a decrease.

The actual prevalence question cannot be answered from the supplied examples. The packet does not enumerate every eligible matched sweep, state how those sweeps were selected, or provide their complete outcomes. I consequently have neither a deeper sweep denominator nor a basis for claiming that reversals are unusually frequent.

An exhaustive analysis would start with the matrix, fix an environment and all non-varied tuple components, and enumerate every eligible ordering along the chosen axis. It would retain incomplete and unscored groups, identify partial-score mappings, and distinguish failure stages. Only then could a reversal count be compared with an explicitly justified baseline.

That enumeration is not reported here. The observations are examples worth investigating, not evidence of enrichment over chance.

Nor do the SQL lengths locate a transition. Success at **6** and **25**, with a validation failure at **12**, does not establish where performance changes between those settings—or that an underlying success probability changes at all.

## First ask what failed

The CSS middle case and the SQL middle case are explicitly described as **source-validation failures**, not reported semantic-test failures. That distinction limits what can be inferred about task competence.

A source-validation rejection can still be a legitimate benchmark failure when valid source is part of the contract. Separating it from a semantic failure is diagnosis, not forgiveness. But “the submitted source was rejected” is not equivalent to “the model could not solve the underlying state-machine or fixed-point problem.”

The truncation or length hypothesis is unresolved. An incomplete or over-length submission could plausibly fail source validation, but the packet does not supply submitted artifacts, termination reasons, output budgets, or validator diagnostics sufficient to test that explanation. A pass at the larger CSS bit count or SQL chain length does not settle a response-length hypothesis, because generated source length need not increase with the nominal task-size setting.

Judge guarantees introduce a related constraint and remain an audit item. The matrix records a `judge_guarantees` field, and the campaign has mixed guarantees; a PASS therefore should not be assumed to certify an identical property everywhere. A comparison across levels needs to establish that the relevant acceptance criteria are comparable. The packet does not show that a guarantee changed along any particular quoted sequence, so changing guarantees are a possible confound to audit—not an established explanation for a reversal.

## The denominator and the provenance matter

The aggregate pass fraction is especially unsuitable as a universal success probability because environment outcomes are heterogeneous. F-006 describes pass rates spanning 0.00 to 1.00 and names six zero-rate environments (`glyph`, `functorial_augmentation`, `monadic_reward`, `sheaf_invariant`, `ts_one_step`, `ts_trajectory`) while marking an additional entry unscored; I do not treat the unscored entry as a measured zero.

The **11 unscored selected cases**, derived as \(416-405\), require similar care. They are missing scores, not an additional set of recorded failures. Their missingness cannot be assumed random because the packet does not establish why they were unscored. Accordingly, **0.684 is a conditional result among scored cases**, not an established unconditional success rate for the selected campaign.

Provenance further limits the interpretation. This is one campaign under the **Mercury-2.5** label. The supplied packet does not establish a complete model-and-harness manifest covering the exact model build, prompting and generation settings, task-generation configuration, and evaluator versions. The repository was dirty: a clean commit reference alone would not reconstruct the executed source state. Reproduction requires the relevant working-tree changes or an equivalent frozen snapshot.

Finally, one seed-0 run per selected cell provides no replicated estimate of variability. No probabilistic threshold is detected here.

## What would make a transition claim credible?

The next experiment should test the ordering rather than merely collect another striking sequence.

- **Define the proposed order.** State which task property changes, which remain fixed, and whether the axis concerns construction difficulty, evaluator coverage, input scale, or another quantity. Do not let a shared label stand in for that definition.
- **Enumerate before selecting examples.** Publish all eligible matched sweeps, their inclusion rules, scoring status, failure modes, and judge guarantees.
- **Replicate the cells.** Vary task seeds and, where generation is stochastic, repeat generations while recording those sources of variation separately. Estimate uncertainty before interpreting an isolated middle-level loss as a dip in success probability.
- **Separate failure layers.** Keep contract-level success visible, but distinguish source validity from semantic evaluation. Inspect artifacts and termination information before attributing validation failures to either truncation or task reasoning.
- **Freeze provenance and account for attrition.** Preserve the executed source state (including uncommitted changes), model configuration, prompts, budgets, and judges. Explain unscored cases rather than silently discarding them from matched comparisons. Denser SQL lengths around 12 and the rejected source itself would be better evidence about that case than a line drawn from 6 through 12 to 25.

These are proposed checks, not analyses already completed. Their purpose is to turn a suggestive sequence into a testable claim about performance.

## The finding is about measurement

The archive records MoCo’s pass–fail–pass sequence, CSS’s partial-score–validation-failure–pass sequence, and SQL’s successes around a validation rejection—but under single-seed, incompletely enumerated conditions, none establishes a non-monotonic difficulty curve.

The larger lesson is not that harder problems secretly become easier. It is that **an ordered parameter, an evaluator setting, and an estimated probability of success are different things**.

Mercury’s labels have not been validated as a common ordinal scale, and one seed per cell supplies no replicated basis for locating a threshold. In this single-seed, dirty-repository Mercury-2.5 archive, the three recorded sequences identify cases worth auditing. They do not locate where a model’s ability breaks. Before a difficulty transition can be measured, *difficulty* has to name a controlled change, and each outcome has to say what was judged.

---

*Evidence base: F-004 (campaign accounting), F-006 (environment-rate summary), F-008 (recorded sequences), and the supplied description of the 340-row environment × difficulty-tuple matrix. The chance calculation is explicitly derived from F-004 under hypothetical assumptions; no new sweep enumeration, artifact inspection, or replication is claimed.*
```

&&&&&&&&&&&&&&&&&

gpt 6 luna max:

---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Treat a difficulty label as a measurement claim to be checked, not an ordering supplied by the label itself.</dd>
  <dt>Synthesis</dt>
  <dd>Analysis of the archived Mercury-2.5 evidence packet. No additional cases were run.</dd>
  <dt>Prose</dt>
  <dd>Written from the evidence dossier and its adversarial review.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded counts and sequences; low for any claim about difficulty effects. Each selected cell has one seed and no replication.</dd>
  <dt>Importance</dt>
  <dd>A configuration sweep cannot locate a capability threshold until its axis, outcomes, and variation are measured.</dd>
</dl>

MoCo’s `PASS` → `FAIL` → `PASS` is an inviting shape. It can look as though Mercury succeeds at one visible-test level, fails at the next, then recovers at a later setting. But the archive records individual outcomes, not estimates of a response curve.

F-008 also reports sequences for CSS state machines and SQL fixed points, though their middle outcomes are not all ordinary task-level failures. I read the narrower finding as methodological: **the archive does not establish that its difficulty labels form a validated ordinal scale.** The settings concern different things, and one seed per selected cell gives no estimate of how often an outcome would recur.

That is narrower than discovering an unexpected valley in model capability. It is also more useful. Before asking where Mercury breaks, I need to know what the horizontal axis measures and what the vertical axis certifies.

## What the campaign counted

The Mercury-2.5 campaign selected **416 cases** across **38 environments** and scored **405**: 277 `PASS` and 128 `FAIL`. The pass share was **0.684 among scored cases** (F-004). The remaining 11 selected cases were unscored and outside that denominator. These are campaign totals, not statistics specific to the transition examples.

The supplied environment × difficulty-tuple matrix has **340 rows**. Its fields include case and score counts, pass rates, failure modes, and judge guarantees. I treat it as an index of recorded configurations, not as 340 replicated difficulty curves or a count of matched three-level sweeps. Each selected cell used seed-0; the campaign did not replicate it.

| Layer | Summary |
|---|---|
| Campaign accounting (F-004) | 416 selected across 38 environments; 405 scored: 277 `PASS`, 128 `FAIL`; 0.684 among scored cases; 11 unscored. |
| Difficulty matrix | 340 environment × difficulty-tuple rows, with `n_cases`, `n_scored`, `n_pass`, `n_fail`, `pass_rate`, `failure_modes`, and `judge_guarantees`. |
| Run design | One seed-0 run per selected cell; no replication; dirty repository. |

*Figure 1. Campaign accounting and matrix overview. This is a schematic of the supplied summaries, not a rendering of all 340 rows or an enumeration of eligible sweeps.*

## Three sequences, not three curves

For this essay, my selection rule is simple: I report the three contrasts explicitly identified in F-008. The supplied packet gives neither a prespecified search rule nor an exhaustive count of complete, comparable three-level sweeps in the 340-row matrix. These examples therefore cannot tell me how prevalent reversals are.

| Environment | Setting order as reported | Recorded outcomes |
|---|---|---|
| MoCo | Successive visible-test levels | `PASS` → `FAIL` → `PASS` |
| CSS state machine | Easy-surface cases; bit count 3 → 4 → 5 | Partial score → source-validation failure → `PASS` |
| SQL fixed points | Graph-chain length 6 → 12 → 25 | `PASS` → source-validation failure → `PASS` |

*Figure 2. The three F-008 sequences. Arrows show the reported order only; the outcomes are not all the same kind of result and do not form fitted pass-rate curves.*

Only MoCo is an unambiguous binary pass/fail/pass sequence in the supplied description; the packet does not identify the stage at which its middle case failed. CSS is a mixed-status sequence, and I leave its partial score as reported rather than recoding it as `PASS` or `FAIL`. The middle SQL result is a source-validation failure, not a reported semantic-test failure. The packet also does not establish that every other component of each difficulty tuple was matched.

## An axis is not a common unit of difficulty

The axis descriptions in the packet have not been independently verified as operational definitions. As reported, MoCo varies visible-test level, the CSS comparison varies bit count at the easy-surface setting, and SQL varies graph-chain length. Those are different parameters, not measurements of a shared quantity.

Bit count and graph-chain length have numerical orders. That does not establish that they place this model under increasing difficulty. Visible-test coverage has no direction on its label alone: without knowing what the solver can see and what conditions the evaluator checks, I cannot infer whether a higher level makes the task harder, easier, or simply changes what is measured.

This cross-environment mismatch explains why a shared “easy to hard” axis needs justification. It does **not** explain why the middle MoCo outcome was `FAIL`. Nor does the archive validate a common latent difficulty scale—or disprove every possible one.

The matrix records `judge_guarantees`, so I would audit whether the relevant guarantees and acceptance criteria are comparable before comparing levels. The packet does not establish that a guarantee changed along any of the three reported sequences; I treat this as an audit item, not an explanation for a reversal.

## A reversal is an observation, not a curve

As a deliberately crude illustration, suppose three binary outcomes were independent and had the same pass probability \(p\) at every level. Plugging in the campaign-wide scored-case fraction, \(p = 277/405 \approx 0.684\), gives:

\[
P(\text{PASS–FAIL–PASS}) = p^2(1-p) \approx 14.8\%,
\]

\[
P(\text{either alternating sequence}) =
p^2(1-p) + p(1-p)^2 = p(1-p) \approx 21.6\%.
\]

These percentages are illustrative arithmetic, **not a calibrated null model for Mercury-2.5**. The calculation pools unlike environments and judge guarantees; independence is not established; CSS is not a three-outcome binary sequence; and the packet does not document an exhaustive set of eligible sweeps or how the examples were found. I consequently have neither a [d-word] sweep denominator nor a basis for claiming that reversals are unusually frequent.

Even if an underlying probability of success declined steadily along an ordered task parameter, one outcome at each level could still zigzag. The MoCo sequence neither proves nor rules out such a decline. The three observations do not locate a threshold.

## First ask what failed

The CSS and SQL middle cases are described as **source-validation failures**, not semantic-test failures. That tells me the submitted source was rejected; it does not show that valid source would have failed the underlying task. Source validity can still be part of the benchmark contract. Distinguishing it from semantic performance is diagnosis, not forgiveness.

Truncation or a length limit is one possible explanation. Malformed source or a validator interaction is another. The supplied packet includes no submitted artifacts, output lengths, budgets, termination information, or validator diagnostics with which to choose among them.

A pass at the larger CSS bit count or SQL chain length does not settle a response-length hypothesis: the nominal task parameter does not tell us how long the generated source was, and separate runs need not emit the same amount of source. I would inspect the preserved submissions and validation records before attributing either rejection to truncation or to reasoning failure.

## The denominator and the provenance matter

F-006 labels the environment-rate pattern bimodal and reports rates from 0.00 to 1.00, but its claimed tally of seven zero-rate environments is unresolved: it names six—`glyph`, `functorial_augmentation`, `monadic_reward`, `sheaf_invariant`, `ts_one_step`, and `ts_trajectory`—and lists `epistemic_silence/type_games` as unscored, not as a measured zero.

That reported spread is a reason not to treat the pooled 0.684 as a success probability for any particular task. The 11 selected-but-unscored cases also remain outside the scored denominator. The packet does not say why they were unscored, so I cannot assume the omissions were random or extend the scored-case share to all 416 selected cases.

The repository was dirty. That does not show that the counts are wrong or explain any failure, but reproducing the run requires preserving the executed working-tree state or an equivalent snapshot. One seed-0 run per selected cell supplies no within-cell estimate of variation; the seed label alone also does not tell me which sources of variation it controls.

For a reproduction, I would record the exact source snapshot alongside the model and harness configuration, prompts, generation settings, rendered tasks, validators, output budgets, and submitted artifacts. Those are requirements for a useful follow-up, not details I infer from the campaign label.

## What would make a transition claim credible?

I would design the next experiment to test an ordering, not merely collect another striking sequence:

- **Define the proposed order.** State what task property changes, what remains fixed, and whether the axis concerns task construction, evaluator coverage, input scale, or something else.
- **Enumerate before selecting examples.** Publish the inclusion rule and every eligible matched sweep, including incomplete and unscored groups. Record failure modes and audit `judge_guarantees`; keep partial scores and validation outcomes distinct.
- **Replicate the cells.** Repeat task instances and, where generation is stochastic, model generations. Record those sources of variation separately rather than treating a seed label as a substitute for replication.
- **Separate failure layers.** Preserve the source, validation result, semantic result, and termination information. Test a budget or truncation explanation before attributing a validation failure to it.
- **Freeze provenance and account for attrition.** Preserve the executed source state and the model, prompts, harness, judges, and output limits. Explain unscored cases rather than silently dropping them from comparisons.
- **Sample the SQL axis more densely around 12.** Retain the rejected source and compare additional graph-chain lengths; the existing points do not locate a boundary.

These are proposed checks, not analyses already completed.

*Evidence scope: campaign counts come from F-004; the environment-rate summary and unresolved zero-rate tally from F-006; the reported sequences from F-008. Matrix structure, axis descriptions, and run limitations come from the supplied evidence packet. The percentages above are derived from F-004 under hypothetical assumptions; I report no new sweep enumeration, artifact inspection, or reruns.*

I do not read this archive as showing that harder problems secretly become easier. An ordered parameter, an evaluator setting, and an estimated probability of success are different things.

In this single-seed, dirty-repository Mercury-2.5 archive, the three recorded sequences identify cases worth auditing. They do not locate where a model’s ability breaks. Before a difficulty transition can be measured, *difficulty* has to name a controlled change, and each outcome has to say what was judged.

