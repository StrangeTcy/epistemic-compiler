gpt 6 sol max:

---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions"
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

A middle setting fails; the settings on either side pass. Connect the points and it looks as though Mercury-2.5 encountered a pocket of difficulty, then recovered. In the archived run, though, those points are individual outcomes, not estimates of a response curve.

The narrower finding is more useful: the campaign’s *difficulty* settings are not a validated ordinal scale of model performance. Some settings change test coverage, others change task size or surface form. Within a setting, one seed gives us no estimate of how often the result would recur.

## What the campaign counted

The Mercury-2.5 campaign selected 416 cases across 38 environments and scored 405 of them: 277 `PASS`, 128 `FAIL`, and a pass share of 0.684 **among scored cases** (F-004). The other 11 selected cases were unscored, not failures. The packet does not establish whether scoring omissions are independent of environment or difficulty setting, so the scored-only share need not describe every selected case.

The environment × difficulty-tuple matrix contains 340 rows, with case and score counts, failure modes, and judge guarantees. It is a way to locate recorded outcomes, not a collection of replicated difficulty curves: each selected cell used seed-0, with no rerun at that setting. The judge guarantees also differ across the campaign, so pooled `PASS` labels need not certify the same kind of success.

Environment pass rates in the packet span 0.00 to 1.00 (F-006), another reason the pooled 0.684 is a poor stand-in for the probability of passing any particular task. There is a bookkeeping limit here: F-006 calls seven environments zero-scoring but names six—`glyph`, `functorial_augmentation`, `monadic_reward`, `sheaf_invariant`, `ts_one_step`, and `ts_trajectory`—while describing an additional entry as unscored. I do not count an unscored environment as one with a zero pass rate.

!

*Figure 1. Selected environment × difficulty-tuple rows. Cell labels give passes over scored cases; grey denotes unscored cases, not zero passes. The display does not enumerate all eligible three-level sweeps.*

## Three sequences, not three curves

For this essay, the selection rule is simple: report the three contrasts explicitly identified in F-008. The packet gives neither a prespecified search rule nor an exhaustive count of complete, comparable three-level sweeps in the 340-row matrix. These examples therefore cannot tell us how prevalent reversals are.

| Environment | Setting varied | Recorded sequence | What the sequence does **not** establish |
| --- | --- | --- | --- |
| MoCo | Visible-test level | `PASS` → `FAIL` → `PASS` | A change in pass probability, from one outcome at each level. |
| CSS state machine | Bit count, at the easy-surface label: 3 → 4 → 5 bits | Partial score → source-validation failure → `PASS` | A binary pass/fail/pass curve: the first result is partial, and the middle result stops at source validation. |
| SQL fixed points | Graph-chain length: 6 → 12 → 25 | `PASS` → source-validation failure → `PASS` | A behavioral failure at length 12 or a threshold between the sparsely sampled lengths. |

Only the MoCo sequence is an unambiguous binary zigzag in the supplied description. The CSS partial score is not documented as a binary `PASS`; neither source-validation failure tells us how valid code would have performed on the task. The packet also does not reconcile those row-level descriptions with its scored-`FAIL` and unscored totals, so I do not silently assign them to either denominator.

!

*Figure 2. Selected MoCo visible-test comparisons. Lines connect recorded outcomes for legibility; with seed-0 alone in each selected cell, they are not fitted pass-rate curves.*

## How surprising is a zigzag?

As a deliberately crude check, suppose each level independently produced a binary pass with the campaign-wide probability \(p=277/405\), approximately 0.684. A three-level sequence would read `PASS/FAIL/PASS` or `FAIL/PASS/FAIL` with probability \(p(1-p)\), approximately **21.6%**. An oscillation is not, by itself, unlikely under that artificial no-level-effect model.

That is **not** a calibrated null hypothesis for Mercury-2.5. It pools unlike environments and judge guarantees; it applies to binary outcomes, unlike the CSS record; and the packet supplies no denominator of eligible sweeps against which to compare the three selected examples. Even if an environment’s *underlying* chance of success decreased steadily with a task-size setting, one outcome per setting could still zigzag. The MoCo trace neither proves nor rules out such a decrease.

The two intermediate source-validation failures pose a separate problem. They are failures of the end-to-end submission pipeline, but not observations that valid submitted code failed a behavioral check. Truncated or length-limited output is one possible explanation; malformed source or a validator interaction is another. The packet provides no generated files, output lengths, limits, or validator diagnostics with which to choose among them. A pass at the larger CSS bit count or SQL chain length does not settle a response-length hypothesis, because generated source length need not increase with the nominal task-size setting.

## What the labels change

In MoCo, the visible-test setting changes test coverage. In the cited CSS comparison, *bit count* changes while the recorded surface label remains easy; CSS configurations can also alter class names, but that is not the axis swept in the table. SQL varies graph-chain length. Regex state machines provide input-string lengths of 32, 128, and 512 characters; the supplied packet gives no corresponding regex outcome sequence, so none is inferred here.

Bits, graph-chain lengths, and characters have numerical orders. Whether they put *this model* under increasing difficulty is a different, unmeasured proposition. Visible-test coverage does not even specify a direction without knowing how the changed tests affect the information available to the solver and the conditions checked. This cross-environment mismatch explains why a shared “easy to hard” x-axis is unjustified. It does **not** explain why the middle MoCo cell failed.

The executed source is another boundary. The campaign repository was dirty, so a clean checkout alone would not establish that it reproduces the task templates or judges used in the run; the supplied model name likewise does not specify a checkpoint, inference settings, or harness revision. These limits matter when interpreting a change in configuration as a change in the task actually presented.

A useful follow-up would freeze the executed source, including its uncommitted changes, alongside the exact model and harness configuration, rendered tasks, tests, validators, and output limits. It would declare in advance which complete sweeps qualify, hold other settings and judge guarantees fixed or report them separately, and repeat each level across seeds and instances. It would keep source validity, behavioral results, and unscored cases distinct, with an explicit denominator for each analysis. Denser SQL lengths around 12 and the rejected source itself would be better evidence about that case than a line drawn from 6 through 12 to 25.

In this single-seed, dirty-repository Mercury-2.5 archive, the three recorded sequences identify cases worth auditing. They do not locate where a model’s ability breaks. Before a difficulty transition can be measured, *difficulty* has to name a controlled change, and each outcome has to say what was actually judged.

*Evidence base: F-004 (campaign accounting), F-006 (environment-rate summary), F-008 (recorded sequences), and the supplied description of the 340-row environment × difficulty-tuple matrix.*


&&&&&&&&&&&&&&

gpt 6.1 sol max:

---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Claim</dt>
  <dd>The campaign does not validate its difficulty labels as an ordinal scale; the reported outcome sequences do not establish difficulty curves.</dd>
  <dt>Evidence</dt>
  <dd>F-004, F-006, F-008, and the supplied descriptions of the difficulty matrix and its axes.</dd>
  <dt>Certainty</dt>
  <dd>One Mercury-2.5 campaign; one seed-0 run per selected cell; no replication; dirty source repository.</dd>
  <dt>Importance</dt>
  <dd>Separates task parameters, evaluator coverage, source validity, and probability of success—quantities that a single “difficulty” label can obscure.</dd>
</dl>

Pass, fail, pass is an inviting shape. It suggests a model that succeeds on a small problem, breaks somewhere in the middle, then recovers when the problem grows.

The Mercury evidence packet contains that sequence in MoCo, alongside related sequences in CSS state machines and SQL fixed points—but these are selected, single-seed observations, not estimates of a difficulty curve. Some of the recorded failures concern source validation rather than demonstrated failure on the task’s semantic requirements.

The defensible finding is methodological: **the archive does not establish that its difficulty labels form a validated ordinal scale.** Its axes change different task properties, and its one-seed-per-cell design provides no replicated basis for identifying a threshold.

That is narrower than discovering an unexpected valley in model capability. It is also more useful. Before asking where Mercury breaks, we need to know what the horizontal axis measures and what the vertical axis certifies.

## What was actually recorded

The campaign selected **416 cases**, scored **405**, and recorded **277 PASS** and **128 FAIL**, for a scored-case pass rate of **0.684** across **38 environments**. That rate describes scored cases, not every selected case. The **11** selected-but-unscored cases remain outside its denominator. These are campaign totals from F-004, not results specific to the transition examples.

The environment difficulty matrix has **340 rows**, each identified by an environment and a difficulty tuple. Its fields include case counts, scored counts, pass and fail counts, pass rates, failure modes, and judge guarantees. Cases, matrix rows, and matched difficulty sweeps are therefore different units; the row count is not a count of independent opportunities to observe a reversal.

F-008 supplies the following examples. Each inherits the campaign’s single-seed limitation.

| Environment | Reported ordering | Recorded outcomes | Qualification |
|---|---|---|---|
| MoCo | Successive visible-test levels | PASS → FAIL → PASS | The axis changes test coverage; the packet does not identify the middle failure’s stage. |
| CSS state machine | Bit counts **3 → 4 → 5**, at the easy surface setting | Partial score → source-validation failure → PASS | The partial score has no supplied mapping to the campaign’s binary accounting. |
| SQL fixed points | Graph-chain lengths **6 → 12 → 25** | PASS → source-validation failure → PASS | These are separated sampled lengths, not a dense sweep or a located boundary. |

These are not interchangeable observations.

MoCo supplies a reported binary reversal, although its failed stage is unspecified. SQL supplies endpoint successes around a source-validation rejection. CSS supplies a mixed-status sequence: without a documented mapping from its partial score to PASS or FAIL, it cannot simply be entered into a binary reversal count.

The campaign totals contain PASS and FAIL, not a separate partial-score category. Preserving the CSS description does not add another category to those totals; it acknowledges that the packet does not explain how that local score was reconciled with them.

The easy-surface qualifier belongs to the CSS example. No corresponding SQL surface setting is established by the packet, so none is assumed here. Nor do the examples, by themselves, establish that every other component of each difficulty tuple was matched.

## An axis is not a common unit of difficulty

The packet’s axis definitions describe different interventions:

- **MoCo visible-test level changes test coverage.** This changes how a submission is examined; it is not automatically a measure of how difficult the submission was to construct.
- **CSS varies class names and bit counts.** The quoted sequence concerns bit count at a fixed easy surface setting, not an unspecified progression through surface labels.
- **SQL varies graph-chain length.** A longer chain is an ordered structural parameter, but the packet does not calibrate that parameter against a replicated success probability.
- **Regex varies input-string length: 32, 128, and 512 characters.** Those lengths define an axis here; the supplied evidence does not establish an accompanying all-pass sequence.

Calling these settings “difficulty” does not make them measurements of the same quantity. More test coverage, more state bits, a longer graph chain, and a longer input string can each matter, but they matter through different mechanisms.

That heterogeneity does **not** explain the within-environment reversals. Different axes across environments cannot tell us why a particular CSS submission failed validation or why a particular MoCo run failed between two passes. It tells us why pooling their labels into a common difficulty scale would require additional justification.

The distinction also applies within an environment. A parameter can have a clear order without its effect on model performance having been measured. Conversely, an occasional reversal would not disprove a genuinely ordered difficulty manipulation: even monotonically declining success probabilities can produce non-monotonic sequences of individual outcomes.

For MoCo, even proof that test suites were nested would establish an implication only for a **fixed submission**: passing a larger suite would imply passing its subset. It would not require separately generated submissions at successive settings to produce monotonic outcomes.

The archive therefore neither validates a common latent difficulty scale nor disproves every possible one. It leaves that validation undone.

## A reversal is an observation, not a curve

A simple calculation shows why a reversal alone is weak evidence.

Suppose, purely as an illustration, that three binary outcomes were independent and had the same pass probability \(p\) at every level. The probability of either PASS–FAIL–PASS or FAIL–PASS–FAIL would be

\[
p^2(1-p) + p(1-p)^2 = p(1-p).
\]

Using the campaign’s scored-case fraction, \(p = 277/405 \approx 0.684\), gives approximately **21.6%**. That percentage is a hypothetical calculation derived from F-004, **not a measured reversal rate or a calibrated null model for this campaign**.

The assumptions matter. The campaign pools heterogeneous environments; independence is not established; the examples were not supplied through a declared exhaustive selection procedure; and the CSS sequence is not resolved into three binary outcomes. The calculation only demonstrates that a flat success probability can readily produce an apparently interesting shape.

The actual prevalence question cannot be answered from the supplied examples. The packet does not enumerate every eligible matched sweep, state how those sweeps were selected, or provide their complete outcomes. We consequently have neither a defensible sweep denominator nor a basis for claiming that reversals are unusually frequent.

An exhaustive analysis would start with the matrix, fix an environment and all non-varied tuple components, and enumerate every eligible ordering along the chosen axis. It would retain incomplete and unscored groups, identify partial-score mappings, and distinguish failure stages. Only then could a reversal count be compared with an explicitly justified baseline.

That enumeration is not reported here. The observations are examples worth investigating, not evidence of enrichment over chance.

Nor do the SQL lengths locate a transition. Success at **6** and **25**, with a validation failure at **12**, does not establish where performance changes between those settings—or that an underlying success probability changes at all.

## First ask what failed

The CSS middle case and the SQL middle case are explicitly described as **source-validation failures**, not reported semantic-test failures. That distinction limits what can be inferred about task competence.

A source-validation rejection can still be a legitimate benchmark failure when valid source is part of the contract. Separating it from a semantic failure is diagnosis, not forgiveness. But “the submitted source was rejected” is not equivalent to “the model could not solve the underlying state-machine or fixed-point problem.”

The truncation or length hypothesis is unresolved. An incomplete or over-length submission could plausibly fail source validation, but the packet does not supply submitted artifacts, termination reasons, output budgets, or validator diagnostics sufficient to test that explanation.

The SQL success at the longer chain does not rule truncation out: task size need not map directly to emitted-source length, and different runs need not terminate in the same way. Equally, the middle rejection does not establish truncation. The failure label identifies a category, not its cause.

A useful follow-up would inspect the preserved submissions, reproduce their validation results, examine completeness and termination information, and test any budget-related explanation under controlled conditions. Without that work, attributing these cases either to output limits or to reasoning failure would outrun the evidence.

Judge guarantees introduce a related constraint. The matrix records a `judge_guarantees` field, and the campaign has mixed guarantees; a PASS therefore should not be assumed to certify an identical property everywhere. A comparison across levels needs to establish that the relevant acceptance criteria are comparable.

The packet does not show that a guarantee changed along any particular quoted sequence, so changing guarantees are a possible confound to audit—not an established explanation for a reversal.

## The denominator and the provenance matter

The aggregate pass fraction is especially unsuitable as a universal success probability because environment outcomes are heterogeneous.

F-006 describes the environment pattern as bimodal and reports pass rates spanning **0.00 to 1.00**, but its zero-rate tally is internally inconsistent. It names six zero-rate environments—`glyph`, `functorial_augmentation`, `monadic_reward`, `sheaf_invariant`, `ts_one_step`, and `ts_trajectory`—while the further entry `epistemic_silence/type_games` is marked unscored. Its claimed total of seven is therefore not established as seven measured zeros.

The reported range supplies context for heterogeneity; it does not, from this summary alone, validate a precise distributional shape. An unscored entry must not be converted into a zero to make the tally work.

The **11 unscored selected cases**, derived as \(416-405\), require similar care. They are missing scores, not an additional set of recorded failures. Their missingness cannot be assumed random because the packet does not establish why they were unscored. If score availability depends on case properties or failure-producing behavior, the missingness could be outcome-dependent—potentially missing not at random. That mechanism remains unverified.

Accordingly, **0.684 is a conditional result among scored cases**, not an established unconditional success rate for the selected campaign. Missing scores also matter for sweep selection: retaining only complete scored triples could select a different subset from all requested comparisons.

Provenance further limits the interpretation. This is one campaign under the **Mercury-2.5** label, not a demonstrated property of every deployment bearing that name. The supplied packet does not establish a complete model-and-harness manifest covering the exact model build, prompting and generation settings, task-generation configuration, and evaluator versions.

The repository was also dirty. That does not show that the recorded counts are wrong or that an uncommitted change caused an anomaly; it means a clean commit reference alone would not reconstruct the executed source state. Reproduction requires the relevant working-tree changes or an equivalent frozen snapshot.

Finally, one seed-0 run per selected cell provides no replicated seed-level estimate of variability. Without clarity about what the seed controls, it should not be treated as a substitute for documenting either task variation or model-generation variation. No probabilistic threshold is detected here.

## What would make a transition claim credible?

The next experiment should test the ordering rather than merely collect another striking sequence.

- **Define the proposed order.** State which task property changes, which remain fixed, and whether the axis concerns construction difficulty, evaluator coverage, input scale, or another quantity. Do not let a shared label stand in for that definition.
- **Enumerate before selecting examples.** Publish all eligible matched sweeps, their inclusion rules, scoring status, failure modes, and judge guarantees. Resolve the CSS partial-score accounting before using it in a binary analysis.
- **Replicate the cells.** Vary task seeds and, where generation is stochastic, repeat generations while recording those sources of variation separately. Estimate uncertainty before interpreting an isolated middle-level loss as a dip in success probability.
- **Separate failure layers.** Keep contract-level success visible, but distinguish source validity from semantic evaluation. Inspect artifacts and termination information before attributing validation failures to either truncation or task reasoning.
- **Freeze provenance and account for attrition.** Preserve the executed source state, model configuration, prompts, budgets, and judges. Explain unscored cases rather than silently discarding them from matched comparisons.

These are proposed checks, not analyses already completed. Their purpose is to turn a suggestive sequence into a testable claim about performance.

## The finding is about measurement

The archive records MoCo’s pass–fail–pass sequence, CSS’s partial-score–validation-failure–pass sequence, and SQL’s successes around a validation rejection—but under single-seed, incompletely enumerated conditions, none establishes a non-monotonic difficulty curve.

The larger lesson is not that harder problems secretly become easier. It is that **an ordered parameter, an evaluator setting, and an estimated probability of success are different things**.

Mercury’s labels have not been validated as a common ordinal scale, and one seed per cell supplies no replicated basis for locating a threshold. These observations tell us where to audit the measurement. They do not yet tell us where Mercury’s capability breaks.

---

*Evidence scope: campaign counts come from F-004; reported sequences from F-008; environment spread and the unresolved zero-rate tally from F-006. Matrix structure, axis definitions, and run limitations come from the supplied evidence packet. The chance calculation is explicitly derived from F-004 under hypothetical assumptions; no new sweep enumeration, artifact inspection, or replication is claimed.*
