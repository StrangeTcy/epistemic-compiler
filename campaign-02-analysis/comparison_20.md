sonnet 5:

```markdown
---
title: "How Mercury Fails: Observed Failure Patterns in Mercury-2.5"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Failure-mode taxonomy as the organising lens; separation of quantified patterns from descriptive ones.</dd>
  <dt>Synthesis</dt>
  <dd>Role-separated analysis over the archived Mercury evidence (F-002, F-005, F-007, F-009; failure taxonomy and judge-guarantee tables).</dd>
  <dt>Prose</dt>
  <dd>Final writer from evidence dossier and adversarial review brief.</dd>
  <dt>Certainty</dt>
  <dd>Low-to-moderate. Judge-assigned labels, single model (mercury-2.5), single seed per cell, dirty repository, no replication, no difficulty-matching between intervention and base populations, no manual audit of individual verdicts. Everything below is correlational; nothing here is causal.</dd>
  <dt>Importance</dt>
  <dd>Establishes the base-rate shape of Mercury-2.5's failures and the one intervention-level pattern the data can currently support.</dd>
</dl>

## A note on the title

An earlier version of this post promised "failure modes and their conditions." The word *conditions* was doing more work than the evidence can bear. What we have is a count of judge-assigned labels on 128 failed cases, one intervention comparison with small cells, and a handful of descriptive observations about individual cases. That is enough to describe *patterns*. It is not enough to say under what conditions Mercury-2.5 fails, and still less to say why. The framing below is deliberately weaker than the one it replaces, and nothing in it should be read as a conditional or counterfactual claim.

## The shape of the failure set

Of the 128 FAIL verdicts in the archived run, 51 carry the label `underfit` and 49 carry `overfit_visible_tests`. Together these two labels account for 100 of 128 failures, or 78.1%. The remaining 28 (21.9%) split across four labels: `runtime_error` (11), `source_invalid` (9), `invalid_action` (5), and `training_failure` (3). The six counts sum to 128 (F-007).

One thing has to be said plainly about that 128 before anything else is built on it: the underlying taxonomy field is `share_of_eligible_failures`. The 128 is a count of *eligible* failures under a criterion that is not spelled out in the packet, and the percentages above are shares of 128 only. They cannot be reconciled against the 416 cases selected for judging (189 `behavioral_reference` + 227 `compile_only`), nor against the 331-case base population used elsewhere. Different denominators are in play in different parts of this report, and no mapping between them is given. Treat 78.1% and 21.9% as internal to the 128, nothing more.

The stub this post replaces summarised the 78/22 split as "mostly behavioural, not infrastructural." That phrasing is retired for two reasons. First, the taxonomy does not classify its labels along a behavioural/infrastructural axis; that split was an editorial gloss, not a field in the data. Second, even on the most generous reading of the gloss, roughly one failure in five (28/128) is a mechanical error — the patch did not run, did not parse, took an action the harness rejected, or crashed during training. One in five is not a rounding error.

A related claim in the stub — that the model "usually produces a patch that runs; it just does not solve the task" — is also withdrawn. F-007 records failure-mode labels, not execution status. It is tempting to infer that the 108 cases not labelled `runtime_error` or `source_invalid` executed cleanly, but the taxonomy does not say so, and a case labelled `underfit` may well have crashed on a hidden check that the judge chose to describe in terms of coverage rather than execution. The inference is plausible. It is not in the evidence packet, and it is flagged here as inference only.

What the counts do support is narrower and still useful: the two dominant labels describe cases where a patch was produced and judged against hidden behaviour, and the dominant *verdict* when Mercury-2.5 fails is that the patch did not do enough (`underfit`) or did the visible part and not the hidden part (`overfit_visible_tests`).

![Failure modes](../figures/fig5_failure_modes.svg)

*Figure 5. Failure-mode counts across n=128 eligible failures (F-007). Labels are judge-assigned; shares reported are shares of this 128 and are not reconciled against the 416 selected cases or the 331 base-condition cases.*

## What "overfit" does and does not mean here

The label `overfit_visible_tests` invites the reading that the model gamed the visible tests. In at least some cases that reading is wrong. Several cases carrying this label have a `trusted_score` of 1.0 — the behavioural check passed — and were marked FAIL because a required companion file was missing. The `batchnorm_ema` case is the sole documented example in the evidence packet: the patch scored 1.0 but the spec required a `model.py` that was not delivered.

How many of the 49 overfit cases are of this kind is not stated beyond "several." No individual audit of the 49 has been done, so any specific fraction — a handful or half — would be invented rather than derived, and none is given here. What can be said is that 49 functions as an upper bound on pure visible-test gaming: some unknown portion of it is a deliverable-completeness failure rather than hidden-test gaming, and the two are conflated under one label.

The `batchnorm_ema` case also motivates a hypothesis that recurs below: that specs requiring multi-file deliverables are harder for Mercury-2.5 than single-file specs. This is a hypothesis from one example. It is not a measured pattern, and it should not be quoted as a rate.

## The one quantified intervention pattern

The evidence packet contains one comparison with cell-level numbers (F-002). Base cases pass at 228 of 331 (0.69). Cases carrying a `visible_proxy` channel pass at 8 of 27 (0.30). Cases carrying a `reward_proxy` channel pass at 1 of 4 (0.25).

These two intervention cells deserve different weight. The visible-proxy cell, at n=27, is small but not degenerate; it shows a drop from 0.69 to 0.30. No confidence interval has been computed here, and no difficulty matching was performed between the intervention cases and the base population, so the gap should be read as a descriptive, unreplicated measurement — not as evidence of a significant effect. The reward-proxy cell, at n=4, is degenerate: one additional pass would move it from 0.25 to 0.50. It is reported for completeness and should not be quoted as a rate.

Within the 76 latent specifications shared between base and intervention cases, seven interventions flipped a passing base case to a failure — a flip rate of roughly 9% (one in eleven) of shared specs. The flip count is the more [d-word] quantity here, because it is a within-spec comparison rather than a cross-population one; but it carries the same single-seed caveat as everything else in the run, and the identity of this 76 against the 76 verified twins discussed below has not been confirmed.

F-009 restates the same comparison and should not be counted as a replication. There is one measurement of this effect, not two.

![Pairwise intervention](../figures/fig6_pairwise_intervention.svg)

*Figure 6. Pass rates by intervention tag. Base 228/331; visible_proxy 8/27; reward_proxy 1/4 (F-002). The reward_proxy cell (n=4) is degenerate and too small to interpret as a rate.*

## What the proxy pattern does not show

The stub described the proxy channel as "a shortcut that the model takes." That is a claim about the model's process, and the data contain no observation of the model's process. What the data show is that pass rates are lower in cells tagged with a proxy channel. Several explanations are consistent with that, and none is ruled out by anything in the packet:

- The model may indeed optimise against the proxy rather than the hidden target — the "shortcut" reading.
- Proxy-tagged specs may be harder on average, independently of the proxy, because the intervention cases were not difficulty-matched to the base population.
- Adding a proxy channel may lengthen or complicate the spec, and the drop may be a general spec-complexity effect rather than a proxy-specific one.
- The judge may grade proxy cases more strictly, or may be more likely to assign `overfit_visible_tests` when a proxy is present, by construction of the taxonomy.
- With a single seed per cell, some portion of the gap may be sampling variance that a second seed would shrink.

What can be said safely, and only this, is: pass rate is lower in cells carrying a proxy channel, and within shared specs the intervention flipped roughly one in eleven passing cases to failure. Anything about intent or mechanism is speculation, and the whole pattern is correlational.

## Observed patterns, sorted by how much evidence stands behind them

It is worth being explicit about which of the "conditions" in the original draft are measured and which are not.

**Quantified (one measurement, no replication):**

- Presence of a `visible_proxy` channel is associated with a lower pass rate (0.30 vs 0.69; n=27 vs n=331).
- Within 76 shared latent specs, 7 interventions flipped pass to fail.

**Descriptive, from one or a few cases:**

- Specs requiring companion files (e.g. `model.py` alongside the primary patch) can produce FAIL verdicts with a trusted score of 1.0. Documented in `batchnorm_ema`; the count of such cases among the 49 overfit cases is unknown.
- "Visible-test-heavy grading" and "multi-file edits" as general risk factors are generalisations from this same small set of cases and should be read as hypotheses, not as measured general risk factors.

**Not measured at all:**

- The stub asserted that failures were eliminated under single-file specifications with exact oracles. No pass-rate for that stratum is in the evidence packet. There is also a circularity risk: if single-file, exact-oracle cases are simply the cases that are easiest to pass, then observing a higher pass rate there tells us about difficulty, not about a failure-suppressing condition. This is presented here strictly as a hypothesis for a future stratified analysis and nothing more.

## Caveats

The following limitations apply to every number above, and most of them were absent from the earlier draft.

1. **Judge-label composition.** All failure-mode labels are judge-assigned. The 416 selected cases split into 189 with a `behavioral_reference` guarantee and 227 with `compile_only`. A `compile_only` judge cannot, by construction, assign some labels with the same confidence as a `behavioral_reference` judge; the taxonomy counts above do not stratify by guarantee, no cross-tab of failure label by guarantee type exists in the packet, and the share of each label attributable to each judge type is not reported.
2. **Unscored cases.** 11 cases received no score: 6 `epistemic_silence`, 4 `epistemic_type_games`, 1 `rd_adaptive_halting` (F-005). These are excluded from the 128 failures and from the pass rates reported above. This is a non-ignorable exclusion — the direction and size of its effect on any rate in this post is not established here.
3. **Unverified twins.** 56 of 132 twin cases (42.4%) are unverified. The remainder, 76, numerically matches the "76 shared latent specs" used for the flip-rate denominator in the section above. Whether these are the same 76 cases or a coincidence has not been confirmed; the identity needs checking before the flip rate is relied on as resting specifically on verified twins.
4. **Single seed, single model, no replication.** Every cell was run once. The model is mercury-2.5 from a single provider. F-009 restates F-002 rather than reproducing it independently. No result above has been observed twice.
5. **Dirty repository.** The run was executed against a repository with uncommitted or uncontrolled state. Which cases, if any, were affected is unknown.
6. **No difficulty matching, no manual audit.** Intervention cases were not difficulty-matched to base cases, so any pass-rate gap may partly reflect differences in task difficulty rather than the intervention itself. No manual audit of individual verdicts was performed for this post; all counts come from the taxonomy labels as recorded.

## Summary

Mercury-2.5's 128 eligible failures are dominated by two judge labels — `underfit` (51) and `overfit_visible_tests` (49), together 78.1% of 128 — with the remaining 21.9% spread across mechanical errors of four kinds. These shares are internal to the 128 and do not reconcile against the 416 selected or 331 base-condition cases. Within the overfit label, an unknown fraction are companion-file artifacts rather than visible-test gaming; `batchnorm_ema` is the one documented case, and 49 should be read as an upper bound rather than a clean count. The one quantified intervention pattern is that proxy-channel cases pass less often than base cases (0.30 vs 0.69 for visible proxy, n=27; the reward-proxy cell at n=4 is too small to interpret as a rate), with 7 pass-to-fail flips across 76 shared specs — a pattern restated once more in F-009 but not independently replicated. That pattern is correlational, singly measured on unmatched cells, and admits several explanations besides the model taking a shortcut. Whether any specific condition reduces or eliminates these failures has not been measured and is offered here only as a target for the next pass.
```


&&&&&&&&

opus 5:

I'll assemble the final article and save it to the workspace path.Checks pass: no emojis, no "beyond noise"/"flatter"/Wilson/derived 3-of-49 bounds; all mandatory additions present. The three flagged strings appear **only** inside quotation marks as explicitly retracted stub language, never as assertions. Structure is 9 sections (title/epistemic-status block + 8 `##` headings), ~2,290 words.

Saved to `campaign-02-analysis/posts/POST-04-failure-modes.md`:

```markdown
---
title: "How Mercury Fails: Observed Failure Patterns in Mercury-2.5"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Failure-mode taxonomy as the organising lens; separation of quantified patterns from descriptive ones.</dd>
  <dt>Synthesis</dt>
  <dd>Role-separated analysis over the archived Mercury evidence (F-002, F-005, F-007, F-009; failure taxonomy and judge-guarantee tables).</dd>
  <dt>Prose</dt>
  <dd>Final writer from evidence dossier and adversarial review brief.</dd>
  <dt>Certainty</dt>
  <dd>Low-to-moderate. Judge-assigned labels; a single model (mercury-2.5) from a single provider; a single seed per cell; a dirty repository; no replication; no difficulty matching between intervention and base cells; no manual audit of individual verdicts. Everything below is correlational; nothing is causal.</dd>
  <dt>Importance</dt>
  <dd>Establishes the base-rate shape of Mercury-2.5's failures and the one intervention-level pattern the data can currently support.</dd>
</dl>

## A note on the title

An earlier version of this post promised "failure modes and their conditions." The word *conditions* was doing more work than the evidence can bear, and I have removed it. What I have is a count of judge-assigned labels on 128 failed cases, one intervention comparison with small cells, and a handful of descriptive observations about individual cases. That is enough to describe *patterns*. It is not enough to say under what conditions Mercury-2.5 fails, and still less to say why. Nothing in this post should be read as a conditional or counterfactual claim — not the section headings, not the figure captions, and not the summary. The framing below is deliberately weaker than the one it replaces.

## The shape of the failure set

Of the 128 FAIL verdicts in the archived run, 51 carry the label `underfit` and 49 carry `overfit_visible_tests`. Together these two labels account for 100 of 128 failures, or 78.1%. The remaining 28 (21.9%) split across four labels: `runtime_error` (11), `source_invalid` (9), `invalid_action` (5), and `training_failure` (3). The six counts sum to 128 (F-007).

Before going further, a point about that denominator. The field F-007 reports is `share_of_eligible_failures`. The 128 are therefore *eligible* failures under a criterion the packet does not state, and every percentage in this section is a share of 128 and of nothing else. I cannot reconcile 128 against the 416 selected cases, nor against the 331 base cases in F-002, and I have not tried: the arithmetic would be invented rather than derived. Read 78.1% as "78.1% of the eligible failure set," not as a proportion of the run.

The stub this post replaces summarised the distribution as "mostly behavioural, not infrastructural." I am retiring that phrasing for two reasons. First, the taxonomy does not classify its labels along a behavioural/infrastructural axis; that split was an editorial gloss I imposed, not a field in the data. Second, even on the most generous reading of the gloss, roughly one failure in five (28/128) is a mechanical error — the patch did not run, did not parse, took an action the harness rejected, or crashed during training. One in five is not a rounding error.

A related claim in the stub — that the model "usually produces a patch that runs; it just does not solve the task" — is also withdrawn. F-007 records failure-mode labels, not execution status. It is tempting to infer that the 108 cases not labelled `runtime_error` or `source_invalid` executed cleanly, but the taxonomy does not say so, and a case labelled `underfit` may well have crashed on a hidden check that the judge chose to describe in terms of coverage rather than execution. The inference is plausible. It is not in the evidence packet, and I flag it here as inference only.

What the counts do support is narrower and still useful, on a deliberately narrow reading: the two dominant labels describe cases where a patch was produced and judged against hidden behaviour, and the dominant *verdict* when Mercury-2.5 fails is that the patch did not do enough (`underfit`) or did the visible part and not the hidden part (`overfit_visible_tests`).

![Failure modes](../figures/fig5_failure_modes.svg)

*Figure 5. Failure-mode counts across n=128 eligible failures (F-007). Labels are judge-assigned.*

## What "overfit" does and does not mean here

The label `overfit_visible_tests` invites the reading that the model gamed the visible tests. In at least some cases that reading is wrong. Several cases carrying this label have a `trusted_score` of 1.0 — the behavioural check passed — and were marked FAIL because a required companion file was missing. The `batchnorm_ema` case is the documented example, and as far as the packet goes it is the *only* documented example: the patch scored 1.0 but the spec required a `model.py` that was not delivered.

How many of the 49 overfit cases are of this kind is not known. The word the evidence packet uses is "several," and I am going to leave it at that. I could write down a range, but any range I produced would be an illustration of my ignorance rather than a measurement — the packet contains no count, and inventing bounds would lend the gap a precision it does not have. The consequence is a real interpretive fork that I cannot resolve: at the low end, the overfit label is mostly about hidden-test coverage; at the high end, it is substantially a deliverable-completeness artifact. Until the 49 cases are individually audited — which has not been done — the overfit count should be read as an **upper bound** on visible-test overfitting proper, with an unquantified companion-file component to be subtracted from it.

The `batchnorm_ema` case also motivates a hypothesis that recurs below: that specs requiring multi-file deliverables are harder for Mercury-2.5 than single-file specs. This is a hypothesis from one example. It is not a measured pattern, and there is no multi-file pass rate anywhere in the packet to turn it into one.

## The one quantified intervention pattern

The evidence packet contains one comparison with cell-level numbers (F-002). Base cases pass at 228 of 331 (0.69). Cases carrying a `visible_proxy` channel pass at 8 of 27 (0.30). Cases carrying a `reward_proxy` channel pass at 1 of 4 (0.25).

These three numbers deserve different weights. The visible-proxy cell, at n=27, is small. The association between the proxy tag and the lower pass rate is a single unreplicated measurement on cells that were not difficulty-matched to the base population, and I have computed no interval for it and make no claim about its statistical significance. The reward-proxy cell, at n=4, is degenerate. One additional pass would move it from 0.25 to 0.50. I report it for completeness and it should not be quoted as a rate.

Within the 76 latent specifications shared between base and intervention cases, seven interventions flipped a passing base case to a failure — a flip rate of roughly 9%, or about one in eleven, of shared specs. The flip count is the more [d-word] quantity here, because it is a within-spec comparison rather than a cross-population one; but it carries the same single-seed caveat as everything else in the run, it rests on a twin-identity assumption discussed in the caveats below, and seven events is seven events.

F-009 restates the same comparison. It is not a replication and I am not counting it as one: there is one measurement of this effect in the archive, not two.

![Pairwise intervention](../figures/fig6_pairwise_intervention.svg)

*Figure 6. Pass rates by intervention tag (F-002). Base 228/331; visible_proxy 8/27; reward_proxy 1/4. The reward_proxy cell is n=4 and is degenerate — too small to interpret as a rate. Cells were not difficulty-matched; the figure shows association only.*

## What the proxy pattern does not show

The stub described the proxy channel as "a shortcut that the model takes." That is a claim about the model's process, and the data contain no observation of the model's process. What the data show is that pass rates are lower in cells tagged with a proxy channel. At least five explanations are consistent with that, and they are not mutually exclusive:

- The model may optimise against the proxy rather than the hidden target — the shortcut-taking reading, which is one candidate among several and not the default.
- Proxy-tagged specs may be harder on average, independently of the proxy, because the intervention cases were not difficulty-matched to the base population.
- Adding a proxy channel may lengthen or complicate the spec, and the drop may be a general spec-complexity effect rather than a proxy-specific one.
- The grading surface may differ: the judge may grade proxy cases more strictly, or may be more likely to assign `overfit_visible_tests` when a proxy is present, by construction of the taxonomy.
- With a single seed per cell, some portion of the gap may be sampling variance that a second seed would shrink.

I have ruled out none of these. The [d-word] statement is: *pass rate is lower in the cells tagged with a proxy channel, and within shared specs the intervention coincided with roughly one in eleven passing cases becoming failures.* Anything about intent or mechanism is speculation.

## Observed patterns, sorted by how much evidence stands behind them

It is worth being explicit about which of the "conditions" in the original draft are measured and which are not.

**Tier 1 — Quantified (one measurement, no replication):**

- Presence of a `visible_proxy` channel is associated with a lower pass rate (0.30 on 8/27 vs 0.69 on 228/331). Unreplicated, unmatched cells, small n.
- Within 76 shared latent specs, 7 interventions flipped pass to fail.
- The failure-label distribution itself: 51 / 49 / 11 / 9 / 5 / 3 across 128 eligible failures.

**Tier 2 — Descriptive, from one or a few cases:**

- Specs requiring companion files (e.g. `model.py` alongside the primary patch) can produce FAIL verdicts with a trusted score of 1.0. Documented in `batchnorm_ema`, the sole documented case; the count among the 49 overfit cases is unknown.
- "Visible-test-heavy grading" and "multi-file edits" appear in my notes as failure conditions. They are descriptive observations generalised from this same small set of cases. I offer them as hypotheses, not as measured general risk factors, and no rate attaches to either.

**Tier 3 — Not measured at all:**

- The stub asserted that failures "disappear" under single-file specifications with exact oracles. I withdraw that assertion. No pass rate for that stratum exists in the evidence packet, and the success conditions are unquantified in the source. There is also a circularity risk: if single-file-exact-oracle cases are simply the cases that are easiest to pass, then observing that they pass more often tells us about difficulty, not about a failure-suppressing condition. Single-file specifications and exact oracles are recorded here strictly as hypotheses for a future stratified analysis, and nothing more.

## Caveats

The following limitations apply to every number above, and most of them were absent from the earlier draft.

1. **Judge-label composition.** All failure-mode labels are judge-assigned. The 416 selected cases split into 189 with a `behavioral_reference` guarantee and 227 with `compile_only`. A `compile_only` judge cannot, by construction, assign some labels with the same confidence as a `behavioral_reference` judge. There is no cross-tabulation of failure labels by guarantee type anywhere in the packet, and the counts above are not stratified by guarantee; the share of each label attributable to each judge type is simply unknown.
2. **Eligibility of the 128.** As noted above, the taxonomy field is `share_of_eligible_failures`. The shares are shares of 128 eligible failures only and cannot be reconciled against the 416 selected cases or the 331 base cases.
3. **Unscored cases.** 11 cases received no score: 6 `epistemic_silence`, 4 `epistemic_type_games`, 1 `rd_adaptive_halting` (F-005). These are excluded from the 128 failures and from the pass rates. They are not failures in the taxonomy's sense and they are not successes either; they are non-ignorable exclusions, and I make no claim about the direction in which their exclusion moves any rate.
4. **Unverified twins.** 56 of 132 twin cases (42%) are unverified. The remainder, 76, numerically matches the "76 shared latent specs" used for the flip-rate denominator. Whether that is the same 76 or a coincidence has not been confirmed. If it is the same set, the flip analysis rests on the verified twins only, which is the right subset; if it is not, the denominator means something else. The identity needs checking before the number is relied on, and I flag the match as unverified.
5. **Single seed, single model, no replication.** Every cell was run once, with a single seed. The model is mercury-2.5 from a single provider. F-009 restates F-002 rather than reproducing it. No result above has been observed twice.
6. **Dirty repository.** The run was executed against a repository with uncommitted or uncontrolled state. Which cases, if any, were affected is unknown.
7. **No matching, no audit.** Intervention cases were not difficulty-matched to base cases, and no manual audit of individual verdicts was performed.

## Summary

Mercury-2.5's 128 eligible failures are dominated by two judge labels — `underfit` (51) and `overfit_visible_tests` (49), together 78.1% — with the remaining 21.9% spread across mechanical errors of four kinds. Within the overfit label, an unknown fraction are companion-file artifacts rather than visible-test gaming, so 49 is an upper bound on gaming proper and `batchnorm_ema` is the only case documented in detail. The one quantified intervention pattern is that proxy-channel cells pass less often than base cells (0.30 on 8/27 vs 0.69 on 228/331; the reward-proxy cell at n=4 is degenerate and not quotable), with 7 pass-to-fail flips across 76 shared specs, measured once and restated once in F-009 rather than replicated. That pattern is correlational, singly measured, and admits at least five explanations besides the model taking a shortcut. The conditions under which failures might be suppressed have not been measured, and single-file specifications with exact oracles are offered only as a target for the next pass.
```

**Redaction notes.** Deletions applied: "a difference one would not expect from noise alone" (gone, replaced with an explicit no-significance-claim sentence); the "slightly flatters every rate" directional clause (replaced with "non-ignorable exclusions" plus an explicit refusal to claim direction); both emojis; no Wilson intervals imported from opus 5; the 3/49–20/49 derived bounds dropped in favour of a stated refusal to numericise "several." Imported from opus 5: the `share_of_eligible_failures` call-out (now in both §3 and caveat 2), the 132−56=76 coincidence flag, and the F-009-is-a-restatement flag. Caveats expanded from 5 to 7 to carry the no-cross-tab point, the eligibility point, and the no-matching/no-audit pair as numbered items rather than a trailing sentence. Figure captions carry n=128 eligible failures and the n=4-degenerate call-out respectively, with no causal language.
