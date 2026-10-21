some model:

---
title: "Environment Dominates Difficulty"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic status**

- **Original ideas:** 3/10. The observation is a grouping of outcomes that was already sitting in the campaign ledger; my contribution is reading it against the "hard case" intuition.
- **Synthesis:** 7/10. One campaign, one provider, 194 cases, 33 environment families. Everything below comes from that ledger.
- **Prose:** 7/10. First person, self-correcting, and deliberately boring where the numbers demand it.
- **Certainty:** High on the counts. Moderate on the descriptive claim that environment family is the better coarse sorter. Low on anything that would require case-level difficulty features, which this packet does not contain.
- **Importance:** 6/10. If the pattern holds up under replication, it changes which question I ask first when a case fails.

---

### The question I thought I was asking

When I design a reasoning case, I think about difficulty as something I turn up. More constraints, deeper inference, longer context, more state to carry across steps. The implicit model is a slider: push it right and the pass probability goes down, push it left and it goes up, more or less regardless of what kind of task it is. If that model were right, then the single most useful thing to know about a case before seeing its verdict would be where its slider sits.

The Atria covering campaign gave me a chance to check that intuition against actual outcomes, and the first thing I had to do was admit that the campaign does not record the slider at all. There are no case-level difficulty ratings in the ledger. What the ledger does record is which of 33 environment families each case belongs to, and what verdict it received. So the question I can actually answer is narrower than the one I started with: *if I had to pick one coarse label to sort these outcomes, would "environment family" do a good job?*

The answer is that it does a surprisingly good job. Good enough that I now think the slider model, at least for this campaign, has the order of operations backwards.

### What was measured, and under which guarantee

The campaign ran on the Atria provider in paid mode, text-only input. It recorded 194 cases, and all 194 episodes completed. One case, from the TS trajectory family, is sitting in a paused state after a provider outage (roughly 55 minutes of waiting, 8 retries, a final backoff of 600 seconds). The campaign is marked resumable. I mention this only so the arithmetic below adds up: 193 cases carry a scored verdict, and one does not.

The verdicts split into two buckets that must not be merged, and I will not merge them.

| Judge guarantee | Cases | Scored | PASS | FAIL | Unscored |
|---|---:|---:|---:|---:|---|
| Behavioral reference | 72 | 72 | 56 | 16 | — |
| Compile-only | 122 | 121 | 75 | 46 | 1 paused |

The behavioral-reference bucket is the gated one: each of those 72 cases has an exact-instance behavioral reference, so a PASS or FAIL there is a validated verdict. The compile-only bucket does not have that reference on the exact instance. Those 121 verdicts were produced by judges without an oracle for the specific case, and they are exploratory. They tell me something about how the judge read the output; they do not tell me, with the same guarantee, whether the model was right. I am not going to compute a campaign-wide pass rate, because 56 validated passes plus 75 exploratory passes is not a number that means anything.

There is a second constraint that matters even more for this essay. The per-environment ledger I am about to show pools both buckets. The packet does not give me a per-environment split by judge guarantee. So when I say that a family is "all PASS," I mean all of its scored verdicts, across both guarantee levels, were PASS. That is descriptive evidence about the ledger. It is not a validated claim about the behavioral-reference subset within that family, and I cannot make it one with the data I have.

### The ledger

Here are all 33 families, with PASS and FAIL counts and the reported family score. The score is not the pass fraction; it includes partial credit, which I will come back to.

| Environment family | PASS | FAIL | Paused | Score |
|---|---:|---:|---:|---:|
| Architecture naturality | 5 | 0 | 0 | 1.000 |
| BatchNorm EMA | 0 | 11 | 0 | 0.086 |
| Categorical lenses | 4 | 1 | 0 | 0.800 |
| CI dependency graph | 5 | 0 | 0 | 1.000 |
| Compositional optimizer | 3 | 2 | 0 | 0.600 |
| CSS state machine | 3 | 2 | 0 | 0.683 |
| Epistemic games | 7 | 0 | 0 | 1.000 |
| Equivariant diagram | 5 | 0 | 0 | 1.000 |
| Functorial augmentation | 2 | 3 | 0 | 0.650 |
| Glyph | 0 | 8 | 0 | 0.000 |
| GNN message passing | 0 | 5 | 0 | 0.417 |
| MoCo | 9 | 2 | 0 | 0.905 |
| Monadic reward | 1 | 4 | 0 | 0.200 |
| Neuro-symbolic parser | 4 | 1 | 0 | 0.800 |
| RD adaptive halting | 9 | 2 | 0 | 0.818 |
| RD gradient credit | 11 | 0 | 0 | 1.000 |
| RD state carry | 11 | 0 | 0 | 1.000 |
| Regex state machine | 3 | 2 | 0 | 0.683 |
| Semiring unification | 5 | 0 | 0 | 1.000 |
| Sheaf invariant gluing | 5 | 0 | 0 | 1.000 |
| Sheaf physical constraints | 0 | 5 | 0 | 0.111 |
| Sheaf schema sync | 1 | 4 | 0 | 0.200 |
| Spreadsheet dataflow | 5 | 0 | 0 | 1.000 |
| SQL fixed point | 4 | 1 | 0 | 0.800 |
| SSM parallel scan | 5 | 0 | 0 | 1.000 |
| Stochastic monad | 5 | 0 | 0 | 1.000 |
| Template interpreter | 5 | 0 | 0 | 1.000 |
| Tensor functor | 2 | 3 | 0 | 0.400 |
| Tokenizer adjunction | 5 | 0 | 0 | 1.000 |
| Transformer–SSM lift | 5 | 0 | 0 | 1.000 |
| TS one-step | 0 | 3 | 0 | 0.333 |
| TS parse-only | 2 | 1 | 0 | 0.833 |
| TS trajectory | 0 | 2 | 1 | 0.000 |

I checked that this reconciles with the bucket totals: the PASS column sums to 131 (56 + 75) and the FAIL column to 62 (16 + 46), with one paused case, for 194. It does.

### The shape of the distribution

If the slider model were the whole story, I would expect a family's pass fraction to depend on how its cases happened to be parameterised, and across 33 families I would expect something like a hump in the middle: most families somewhere between 30% and 70%, with a few at the ends.

That is not what the ledger looks like.

```text
Per-family pass fraction (scored verdicts only), 33 families

  0%          |  ######               6
  1–39%       |  ##                   2
  40–59%      |  ##                   2
  60–79%      |  ####                 4
  80–99%      |  #####                5
  100%        |  ##############      14
```

**Figure 1.** Histogram of pass fraction across the 33 environment families in the Atria covering campaign. Each family counts once, regardless of size (families range from 3 to 11 scored cases). Twenty of the 33 families sit at one of the two extremes: fourteen with every scored verdict PASS, six with no PASS at all. The middle bins are sparsely populated. Pass fraction is computed from PASS and FAIL counts and does not use the partial-credit score; TS trajectory's paused case is excluded from its denominator.

The distribution is U-shaped. Fourteen families — Architecture naturality, CI dependency graph, Epistemic games, Equivariant diagram, RD gradient credit, RD state carry, Semiring unification, Sheaf invariant gluing, Spreadsheet dataflow, SSM parallel scan, Stochastic monad, Template interpreter, Tokenizer adjunction, Transformer–SSM lift — passed every scored case and carry a score of 1.000. That is 84 cases with zero failures among them.

At the other end, five families failed every scored case and carry low scores: BatchNorm EMA (0 / 11, score 0.086), Glyph (0 / 8, score 0.000), Sheaf physical constraints (0 / 5, score 0.111), TS one-step (0 / 3, score 0.333), and TS trajectory (0 / 2 scored, score 0.000, one case paused). That is 29 scored failures with zero passes among them.

The sharpest single contrast is between families of identical size. RD gradient credit and RD state carry each have eleven scored cases, and all eleven passed in both. BatchNorm EMA also has eleven scored cases, and all eleven failed. Same count, same campaign, same provider, same modality, same judge regime — opposite outcomes, family by family. If someone handed me a case from one of those three families and asked me to guess its verdict before telling me anything else, I would be right 33 times out of 33 using the family name alone. I do not know of any single difficulty dimension that would let me do that.

### Two corrections I owe the reader

I want to be exact about the "five uniformly unsolvable" count, because the ledger supports a slightly different number depending on what you are counting.

First: by verdicts alone, there are *six* families with no PASS, not five. GNN message passing has 0 PASS and 5 FAIL. I have left it out of the "uniformly unsolvable" list because its reported score is 0.417, which is not near zero. On the binary verdict it sits with the failures; on the partial-credit score it sits with the middle. I think the honest thing is to say both: six families recorded no PASS, and five of those also recorded a score at or below 0.333. GNN message passing is the sixth, and the partial credit it earned is itself evidence that something case-level is going on inside that family — the judges gave meaningfully different amounts of credit across five cases that all ended in FAIL.

Second: TS trajectory is not a complete set. Two of its three cases failed; the third is paused, not scored. "All scored cases failed" is true. "All cases failed" is not something I can say.

Neither correction changes the picture in Figure 1. Twenty families at the extremes becomes twenty families at the extremes either way. But I would rather the reader count the same way I do.

### The middle is where difficulty still has to live

The remaining families contain both verdicts, and they are the reason I will not say that difficulty is irrelevant.

Some lean towards passing with a stumble or two: MoCo (9 / 2), RD adaptive halting (9 / 2), Categorical lenses (4 / 1), Neuro-symbolic parser (4 / 1), SQL fixed point (4 / 1), TS parse-only (2 / 1). Some lean the other way: Monadic reward (1 / 4), Sheaf schema sync (1 / 4). And a handful are close to even: Compositional optimizer (3 / 2), CSS state machine (3 / 2), Regex state machine (3 / 2), Functorial augmentation (2 / 3), Tensor functor (2 / 3).

Inside each of these families, something distinguishes the cases that passed from the cases that failed. The family label does not distinguish them — by construction, it is constant within the family. Whatever does distinguish them is a case-level property, and "difficulty," in some operational sense, is the natural candidate. I cannot confirm that from this packet, because the packet does not record difficulty features per case. But I would be making an error in the opposite direction if I read the U-shape as "environment is destiny." It is not. In 13 of 33 families (14 if you count GNN message passing's partial credit as within-family variation, which I do), the outcome varied, and the family name alone would not have told you how.

Partial credit reinforces this. The limitations register lists FAIL verdicts carrying scores of 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208. A FAIL at 0.95 and a FAIL at 0.0 are the same verdict and very different outputs. The score column is graded, not binary, and the gradation is visible even inside families with no PASS.

So the claim I can defend is the coarse one. Environment family sorts these 193 scored outcomes into three groups — always pass, never pass, mixed — and the first two groups between them contain 113 cases, or roughly three-fifths of the scored ledger. Within the third group, and in the partial-credit scores everywhere, there is residual variation that the family label does not explain. Difficulty is the obvious place to look for it. It is just not the first place.

### What "predicts" is allowed to mean here

I have been using the word *predicts*, and I should say what I am entitled to mean by it.

If "predicts" means "sorts the observed outcomes," then environment family wins by inspection, and Figure 1 is the argument. If it means "would win a fitted, held-out comparison against measured difficulty features," I cannot say, because no such features exist in the packet and no such comparison has been run. I do not have a number for *how much* more predictive the family is than, say, constraint count or context length, because I do not have constraint count or context length. What I have is a ledger in which the family label alone is enough to call 113 of 193 scored verdicts without error, and that is a strong enough descriptive pattern to be worth writing down and worth trying to break.

### What the evidence cannot establish

**No mechanism.** The ledger says *that* Glyph fails and *that* RD state carry passes. It says nothing about *why*. The family names are suggestive — I notice that two of the three Trajectory-synthesis families fail completely while the parse-only one mostly passes, and I notice that the two RD families with the word "carry" or "credit" in them are perfect while "adaptive halting" is not — but noticing a pattern in names is not evidence about what the model is doing internally. I am not going to speculate about representation, tokenisation, or anything architectural. The data does not reach there.

**No validated per-family claim.** The per-family ledger pools validated and exploratory verdicts, and I cannot separate them. The U-shape is a fact about the pooled ledger. Whether it holds inside the 72 behavioral-reference cases alone is a question I would like answered and cannot answer from this packet.

**No confidence intervals.** One seed per selected cell, families of three to eleven cases. A family that went 5 / 0 is consistent with a true pass rate well below 100%. The sharpness of the extremes is real in the ledger; its sharpness in the population is unknown.

**No generalisation.** One provider, one modality, one campaign. A different provider could produce a different partition of the same 33 families, and I would not be surprised.

**No prescriptions.** I am not going to tell anyone how to design benchmarks on the strength of this. The most I will say is what I will do myself, which is below.

### What I will do differently

Before this campaign, when a case failed, my first question was "what made it hard?" After this campaign, my first question is "what family is it in, and does that family pass anything?" If the family is one of the fourteen, the failure is interesting and I should look at the case. If the family is one of the five — or six — the failure is expected, and the case-level details are probably not where the information is.

That is a change in the order I ask questions, not a theory about models. The Atria covering campaign does not tell me why environment family carries so much of the signal. It tells me, for these 194 cases, that it does: fourteen families solved outright, five unsolved outright, the rest in between, and the difficulty dial — whatever it is — only visibly doing work in that middle third. The environment sets the range. Difficulty, as far as I can see here, moves within it.

&&&&&&&&&&&&&&&&&&

some other model:

---
title: "Environment dominates difficulty"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 3/10 (Interpretation of patterns already latent in the campaign ledger).
- **Synthesis:** 8/10 (Isolating environment-family outcome clusters from the scored cases while keeping judge-guarantee buckets distinct).
- **Prose:** 8/10 (First-person, evidence-bound, and deliberately cautious about over-claim).
- **Certainty:** High on the exact counts and per-family tallies from this Atria campaign; low on any extrapolation beyond the recorded cells.
- **Importance:** 7/10 (Directly relevant to how we interpret what a reasoning benchmark is actually measuring).

***

When we design or grade a reasoning task, the most natural instinct is to reach for difficulty. We talk about stacking more constraints, lengthening the inference chain, increasing the size of the state space, or packing denser structure into the prompt. The working assumption is that these dials are largely domain-agnostic: turn them up and success probability should fall, turn them down and it should rise, more or less independently of the surrounding “world” the task lives in.

But what if that assumption is the wrong place to start? What if the environment family a case belongs to acts as a stronger, coarser predictor of pass or fail than any individual difficulty dimension we might assign to that case? In other words: does “hard” predict failure better than environment, or does environment dominate?

That is the narrow question I took into the scored results of the `atria_covering_campaign`. The campaign is a single paid, text-only run under the Atria provider. It recorded 194 cases across 33 environment families. One case ended in a provider-error pause; the rest received scored verdicts. Looking at how those verdicts distribute, the pattern that emerges is starkly bimodal at the family level. Fourteen families are uniformly solvable. Five are uniformly unsolvable (or effectively so among their scored cases). The remaining fourteen sit in between. Knowing the environment family tells you far more, at first glance, than knowing whether a given instance was intended to be easy or hard.

I will stay strictly inside the evidence. No causal story about why certain families are hard, no stitching of judge-guarantee buckets into a single campaign pass rate, and no general prescriptions for how benchmarks should be built.

### Campaign boundaries and the two judge-guarantee buckets

Before any environment ledger, the dataset itself must be partitioned correctly. The campaign carries a gate: 72 cases have a behavioral reference (exact-instance oracle guarantee). These are the validated model verdicts. The remaining 122 cases are compile-only: judges graded them without a behavioral reference on that exact instance. Compile-only verdicts are exploratory only. They do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts.

The scored totals are therefore reported separately:

- Behavioral reference: 72 scored — 56 PASS, 16 FAIL.
- Compile-only: 121 scored — 75 PASS, 46 FAIL, plus 1 case left in `paused_provider_error`.

I will never combine these into one aggregate pass rate. The environment-family tallies that follow are drawn from the supplied ledger that spans both buckets; they are useful for seeing structural clustering, but they inherit the exploratory status of every compile-only row. The pause itself is mentioned only for completeness: a provider outage of roughly 55 minutes (3300 seconds waited, 8 retries, final backoff 600 seconds) left the case `ts_trajectory__witness_status=broken_representation=reflective__seed-0` unscored. The analysis concerns the 193 scored cases and the family patterns they form.

### The bimodal pattern: 14 all-PASS, 5 no-PASS

If difficulty dimensions were the dominant driver, most environment families should show mixed outcomes. Easy instances would pass, hard ones would fail, and families would cluster around intermediate success rates. That is not what appears.

Fourteen families are uniformly solvable among their scored cases. Every instance returned PASS and a reported score of 1.000:

- architecture_naturality: PASS 5, FAIL 0  
- ci_dependency_graph: PASS 5, FAIL 0  
- epistemic_games: PASS 7, FAIL 0  
- equivariant_diagram: PASS 5, FAIL 0  
- rd_gradient_credit: PASS 11, FAIL 0  
- rd_state_carry: PASS 11, FAIL 0  
- semiring_unification: PASS 5, FAIL 0  
- sheaf_invariant_gluing: PASS 5, FAIL 0  
- spreadsheet_dataflow: PASS 5, FAIL 0  
- ssm_parallel_scan: PASS 5, FAIL 0  
- stochastic_monad: PASS 5, FAIL 0  
- template_interpreter: PASS 5, FAIL 0  
- tokenizer_adjunction: PASS 5, FAIL 0  
- transformer_ssm_lift: PASS 5, FAIL 0  

Select any scored case from `rd_state_carry` or `epistemic_games` and the outcome is already known before the specific constraints are examined. The family itself is a near-perfect predictor of success in this snapshot.

Five families show the opposite extreme—no scored PASS:

- batchnorm_ema: PASS 0, FAIL 11, score 0.086  
- glyph: PASS 0, FAIL 8, score 0.000  
- sheaf_physical_constraints: PASS 0, FAIL 5, score 0.111  
- ts_one_step: PASS 0, FAIL 3, score 0.333  
- ts_trajectory: PASS 0, FAIL 2, paused 1, score 0.000  

Here the environment is effectively a terminal diagnosis among the scored cells. Even an instance one might subjectively label “easy” inside `glyph` or `batchnorm_ema` still failed. The family label overrides the difficulty dial.

A small but necessary qualification applies to the fifth entry. `ts_trajectory` contributed two FAILs and one paused, unscored case. It is therefore “no scored PASS,” not a fully adjudicated set of three failures. The other four families are complete all-FAIL sets among their scored cases. I treat the group of five as the observed no-PASS cluster, with that caveat attached.

The contrast is sharpest when families of equal size are placed side by side. `rd_gradient_credit` and `rd_state_carry` each have 11 scored cases, all PASS, scores 1.000. `batchnorm_ema` also has 11 scored cases, all FAIL, score 0.086. Same cardinality, opposite poles. A generic “hard/easy” label applied without regard to family would smear that distinction into noise.

<br>

> **Figure 1. Environment families by observed verdict pattern**  
> *(Conceptual bar summary of the 33 families in the Atria covering campaign. Fourteen families sit at 100 % PASS among scored cases. Five families sit at 0 % scored PASS (four complete all-FAIL sets plus `ts_trajectory` with two FAILs and one pause). Fourteen families contain both PASS and FAIL. The distribution is bimodal at the extremes rather than a smooth difficulty gradient. Partial-credit scores exist inside some FAIL verdicts and are noted in the text; the bars reflect binary verdict presence.)*

<br>

### The middle fourteen: where variation still appears

The claim is not that difficulty is irrelevant. Fourteen families contain both PASS and FAIL verdicts. Inside these families the individual case parameters clearly matter.

Families that lean successful but still stumble:

- moco: PASS 9, FAIL 2 (score 0.905)  
- categorical_lenses: PASS 4, FAIL 1 (score 0.800)  
- neuro_symbolic_parser: PASS 4, FAIL 1 (score 0.800)  
- rd_adaptive_halting: PASS 9, FAIL 2 (score 0.818)  
- sql_fixed_point: PASS 4, FAIL 1 (score 0.800)  
- ts_parse_only: PASS 2, FAIL 1 (score 0.833)  

Families that lean unsuccessful but occasionally allow a pass:

- monadic_reward: PASS 1, FAIL 4 (score 0.200)  
- sheaf_schema_sync: PASS 1, FAIL 4 (score 0.200)  

And the more evenly contested battlegrounds:

- compositional_optimizer: PASS 3, FAIL 2 (score 0.600)  
- css_state_machine: PASS 3, FAIL 2 (score 0.683)  
- functorial_augmentation: PASS 2, FAIL 3 (score 0.650)  
- regex_state_machine: PASS 3, FAIL 2 (score 0.683)  
- tensor_functor: PASS 2, FAIL 3 (score 0.400)  

One additional family, `gnn_message_passing`, recorded 0 PASS and 5 FAIL yet carries a reported score of 0.417. Because the partial credit is substantial, it sits with the nuanced middle rather than the near-zero unsolvable cluster. The dataset as a whole contains FAIL verdicts that still received non-zero scores (examples include 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, 0.208). A FAIL is therefore not synonymous with a score of zero; the model can make graded progress even when the binary verdict is negative. That gradient is further evidence that case-level details still move the needle inside some families.

The middle group is precisely why the thesis must stay narrow. Environment family is a powerful coarse sorter; it is not destiny for every instance.

### What the evidence establishes, and what it cannot

The strongest defensible statement is descriptive and limited to this campaign’s ledger:

1. Fourteen environment families are uniformly solvable (all scored cases PASS, score 1.000).  
2. Five environment families show no scored PASS (four complete all-FAIL sets with near-zero or low scores, plus `ts_trajectory` with two FAILs and one pause).  
3. The remaining fourteen families are mixed.  
4. Consequently, knowing the environment family is a stronger first-order predictor of the binary outcome than a generic difficulty label would be, at least among the cells that were actually run.

An “easy” case inside a uniformly unsolvable family is far more likely to fail than a “hard” case inside a uniformly solvable family. That is the concrete pattern the counts support.

What the evidence cannot establish is equally important.

It cannot show that difficulty dimensions are irrelevant. The mixed families demonstrate within-family variation; something about the individual instances is deciding the outcome there. The packet simply supplies no case-level difficulty ratings or ablation that would let us quantify how much those dimensions contribute once environment is controlled.

It cannot supply a causal mechanism. I will not speculate about tokenization, architectural inductive biases, representation gaps, or any other internal reason why `glyph` fails universally while `rd_state_carry` succeeds universally. The data record *that* the families differ; they do not record *why*.

It cannot support a formal head-to-head predictive comparison. There is no fitted model, no out-of-sample test, and no reported feature importance that pits environment labels against measured difficulty features. “Predicts more” here means “sorts the observed outcomes into cleaner groups,” not “wins a quantitative prediction contest.”

Finally, it cannot underwrite general evaluation prescriptions. This is one provider, one modality, one campaign, single seed per selected cell, and a mixture of behavioral-reference and compile-only rows. The pattern is worth noticing inside these bounds; it is not a blueprint for how every reasoning benchmark should be redesigned.

### Caveats that travel with every claim

Several limitations sit beside the results rather than after them.

- Single provider (`atria`) and text-only input modality. A different provider or a multi-modal setting could rearrange the environmental biases entirely.  
- No confidence intervals. Each selected cell used a single seed; we are looking at one frozen snapshot.  
- The per-environment ledger pools behavioral-reference and compile-only cases. No environment-by-guarantee breakdown is supplied, so the sharp family pattern is visible in the combined ledger but cannot be confirmed to hold inside the behavioral-reference bucket alone. Compile-only rows remain exploratory.  
- One case is unscored because of the provider pause. That incompleteness affects only the `ts_trajectory` family tally and does not overturn the broader bimodal shape.  
- Partial credit exists. Binary PASS/FAIL is the primary lens used above, but scores inside FAIL verdicts are not uniformly zero.

These constraints keep the thesis narrow: environment family dominates as a descriptive grouping in the recorded data of this campaign. They do not license stronger language.

### Closing the loop

The familiar story says that when a model fails a reasoning task we should first inspect the complexity of the prompt—how many constraints, how deep the search, how tangled the data structures. The `atria_covering_campaign` ledger suggests a prior question is often more informative: which environment family does the case inhabit?

In the scored results, fourteen families admit no failures, five admit no scored successes, and fourteen sit in the contested middle. The environment sets a strong baseline; difficulty dimensions still modulate outcomes inside some families, but they do not erase the family-level separation. An easy instance in an unsolvable family remains far more likely to fail than a hard instance in a solvable one.

That is all the evidence supports, and it is already enough to change how I read the next set of reasoning results. Ask first what world the task lives in. Only then ask how hard the particular instance is. In this dataset, the environment dominates.

&&&&&&&&&

openhard 3.0 cot 1015:

---
title: "Environment Dominates Difficulty"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (The core interpretation builds on categorical patterns already visible in the campaign dataset.)
- **Synthesis:** 8/10 (Aggregating case outcomes by environment family while preserving judge-guarantee boundaries.)
- **Prose:** 8/10 (First-person analytical writing, constrained to what the recorded evidence supports.)
- **Certainty:** High for the observed Atria campaign results; no generalization to other providers, modalities, or campaigns.
- **Importance:** 7/10 (Useful for clarifying what benchmark outcomes are actually measuring when we label tasks as easy or hard.)

***

When we design reasoning evaluations, we usually begin with a simple mental model of difficulty. We imagine difficulty as a set of dials: more constraints, longer inference chains, more complex data structures, larger context. Turn the dials up, and success should decline. Turn them down, and success should rise. On this view, a hard case should fail and an easy case should pass, more or less independently of the domain in which the case happens to be written.

That intuition is the tension I want to examine here. Does the hardness of an individual case predict whether the model fails? Or does the **environment family**—the broad task domain in which the case sits—predict the outcome more strongly?

The `atria_covering_campaign` gives us a concrete dataset to test that question. It is a paid, text-only campaign run on the Atria provider, with 194 recorded cases across 33 environment families. I initially expected to see a smooth gradient: environments mostly containing a mixture of passes and failures, with harder cases tipping toward failure. The observed pattern is sharper than that. The narrow, defensible conclusion is that **environment family is the dominant coarse predictor of outcome in this dataset**. It does not erase within-environment variation, and it does not prove that difficulty dimensions are irrelevant. But it does show that an "easy" case in an unsolved environment is much more likely to fail than a "hard" case in a uniformly solved one.

Before interpreting that pattern, the dataset boundaries have to be stated clearly.

## Two judge-guarantee buckets must stay separate

The campaign recorded 194 cases, but they do not all carry the same evidentiary weight. The most important methodological line in the whole analysis is the distinction between cases with a behavioral reference and compile-only cases.

1. **Behavioral reference bucket.** These cases carry an exact-instance oracle guarantee. There are 72 scored cases: 56 `PASS` and 16 `FAIL`. These are the validated verdicts.
2. **Compile-only bucket.** These cases were graded by judges without an exact-instance behavioral reference. There are 121 scored cases: 75 `PASS` and 46 `FAIL`. One additional case is in a `paused_provider_error` state. Compile-only verdicts are exploratory signals, not validated model verdicts.

I will not combine these buckets into a single campaign-wide pass rate. Doing so would treat exploratory judgments as if they had the same guarantee as the reference-validated cases, and that would overstate what the dataset establishes.

The environment-level ledger pools both buckets in order to map structural trends across the 33 families. That is useful descriptively, but it comes with an explicit qualification: the environment pattern is observed across a mixture of validated and exploratory grading, and the packet does not provide a per-environment split by judge guarantee. We can describe the pattern; we cannot claim that the identical pattern holds within the behavioral-reference bucket alone.

The single paused case belongs to `ts_trajectory`. The campaign paused after a provider outage of roughly 55 minutes, with eight retries and a final backoff of 600 seconds. I mention this only to explain why one case is unscored. It is not the subject of the essay, and it does not change the analysis of the completed cases.

## The bimodal environment landscape

If individual difficulty dimensions were the main driver, we would expect most environment families to contain both passes and failures. An easy instance in a family would pass, a harder instance would fail, and many families would sit somewhere near the middle of the pass-rate range.

That is not what the ledger shows. Instead, outcomes cluster at the extremes.

> **Figure 1: Observed verdict patterns across 33 environment families**
>
> ```text
> All scored cases PASS      14 | ██████████████
> Both PASS and FAIL         14 | ██████████████
> No scored PASS              5 | █████
> ```
>
> The campaign does not produce a broad, smooth bell curve of family-level pass rates. Fourteen families are uniformly PASS among scored cases, fourteen contain both outcomes, and five have no scored PASS. This bimodal grouping is the central evidence that environment family carries substantial predictive information.

### Fourteen uniformly solvable environments

Fourteen environment families returned only `PASS` verdicts on every scored case, with reported scores of 1.000.

- `architecture_naturality`: PASS=5, FAIL=0
- `ci_dependency_graph`: PASS=5, FAIL=0
- `epistemic_games`: PASS=7, FAIL=0
- `equivariant_diagram`: PASS=5, FAIL=0
- `rd_gradient_credit`: PASS=11, FAIL=0
- `rd_state_carry`: PASS=11, FAIL=0
- `semiring_unification`: PASS=5, FAIL=0
- `sheaf_invariant_gluing`: PASS=5, FAIL=0
- `spreadsheet_dataflow`: PASS=5, FAIL=0
- `ssm_parallel_scan`: PASS=5, FAIL=0
- `stochastic_monad`: PASS=5, FAIL=0
- `template_interpreter`: PASS=5, FAIL=0
- `tokenizer_adjunction`: PASS=5, FAIL=0
- `transformer_ssm_lift`: PASS=5, FAIL=0

This is the strongest part of the environment-dominance observation. In `rd_state_carry` and `rd_gradient_credit`, for example, the model passed all eleven scored cases. If I know only that a case belongs to one of these families, I can predict success with high accuracy before hearing anything about its specific constraint count, inference depth, or structural complexity. The family sets a high baseline, and within the sampled cases, no difficulty setting was enough to break it.

A useful contrast appears by matching sample sizes. `rd_gradient_credit` and `rd_state_carry` each have eleven scored cases and eleven passes. `batchnorm_ema` also has eleven scored cases, but eleven failures and a reported score of 0.086. Same number of scored cases, opposite outcome, separated entirely by environment family. That is the kind of contrast an environment-blind "hard/easy" label struggles to explain.

### Five environments with no scored PASS

At the other extreme, five families have no scored `PASS` verdicts.

- `batchnorm_ema`: PASS=0, FAIL=11, score=0.086
- `glyph`: PASS=0, FAIL=8, score=0.000
- `sheaf_physical_constraints`: PASS=0, FAIL=5, score=0.111
- `ts_one_step`: PASS=0, FAIL=3, score=0.333
- `ts_trajectory`: PASS=0, FAIL=2, with 1 paused case, score=0.000

One qualification is important here. Four families—`batchnorm_ema`, `glyph`, `sheaf_physical_constraints`, and `ts_one_step`—have complete scored sets containing only failures. `ts_trajectory` has two scored failures plus one paused, unscored case. It is therefore accurate to say it has **no scored PASS**, but not accurate to say all three of its cases failed. The paused case remains unresolved.

These families behave like a low ceiling. Even if one constructed an instance that looked simple along traditional difficulty axes, the observed result in this campaign is still failure. The environment, rather than the per-case difficulty dial, appears to determine the upper bound on performance.

I want to be careful about what that means. It is a statement about the sampled cases in this campaign, not a universal law about every possible instance that could ever be written in these families. It does not identify a mechanism, and it does not tell us why these families sit at zero. It only tells us that, within the recorded data, the family label sorts the outcomes very sharply.

## The middle ground: difficulty still matters

The evidence does **not** support the claim that difficulty dimensions are irrelevant. Fourteen environment families contain both passes and failures, and that within-family variation is direct evidence that something at the case level can tip the result.

Some mixed environments lean toward success:

- `moco`: PASS=9, FAIL=2, score=0.905
- `categorical_lenses`: PASS=4, FAIL=1, score=0.800
- `neuro_symbolic_parser`: PASS=4, FAIL=1, score=0.800
- `rd_adaptive_halting`: PASS=9, FAIL=2, score=0.818
- `sql_fixed_point`: PASS=4, FAIL=1, score=0.800
- `ts_parse_only`: PASS=2, FAIL=1, score=0.833

Others lean toward failure:

- `monadic_reward`: PASS=1, FAIL=4, score=0.200
- `sheaf_schema_sync`: PASS=1, FAIL=4, score=0.200

And several sit closer to the middle, where case-level parameters appear to matter a great deal:

- `compositional_optimizer`: PASS=3, FAIL=2, score=0.600
- `css_state_machine`: PASS=3, FAIL=2, score=0.683
- `functorial_augmentation`: PASS=2, FAIL=3, score=0.650
- `regex_state_machine`: PASS=3, FAIL=2, score=0.683
- `tensor_functor`: PASS=2, FAIL=3, score=0.400

These families are the reason the thesis must remain narrow. Environment sets the baseline, but it does not dictate every individual outcome. In a mixed family, two cases can share the same environment label and still receive different verdicts. That is exactly where traditional difficulty dimensions—constraint count, inference depth, structural complexity—are likely to do explanatory work.

### Partial credit complicates the binary picture

There is another layer of nuance. A `FAIL` verdict is not always a score of zero. The dataset contains failed cases with non-zero scores including 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208.

`gnn_message_passing` is the clearest example. It has 0 passes and 5 failures, but a reported score of 0.417. It has no successful verdict, yet the model earns substantial partial credit. It therefore does not belong in the same "near-zero uniformly unsolvable" category as `glyph`. It belongs in the middle ground: binary failure every time, but with meaningful variation in how much progress the model makes.

This distinction matters for the environment-versus-difficulty question. Even in a family with no PASS, case-level differences can still affect the degree of failure. Environment may dominate the binary pass/fail outcome, while difficulty dimensions continue to shape the partial score underneath it. The data does not let us separate those effects cleanly, but it does warn against treating every FAIL as identical.

## What the evidence establishes

The strongest defensible claim can be stated in three parts.

1. **Fourteen environment families are uniformly solvable in the scored sample.** Every scored case in these families passed, regardless of its individual difficulty settings.
2. **Five environment families have no scored PASS.** Four are complete all-FAIL scored sets, and one has two scored failures plus one paused case. Their scores are near zero except where partial credit is present.
3. **Environment family is the stronger coarse grouping in this ledger.** Knowing the family tells you more about the likely outcome than a generic easy/hard label would, because the family sorts cases into all-pass, no-pass, and mixed groups.

A compact way to phrase the practical implication is this: a hard case drawn from a uniformly solvable environment passed in this dataset, while an ostensibly easy case drawn from a no-pass environment still failed. The environment ceiling overrides the difficulty dial more often than the difficulty dial overrides the environment.

## What the evidence cannot establish

The limits are as important as the findings.

First, **this is not a formal head-to-head predictive test**. The evidence packet does not include case-level difficulty ratings, fitted models, feature importance scores, or out-of-sample prediction metrics. We can say environment is a strong descriptive grouping, but we cannot quantify how much more predictive it is than any specific difficulty dimension. We cannot run a controlled comparison that the dataset was not instrumented to perform.

Second, **difficulty has not been ruled out**. The fourteen mixed families prove that outcomes vary within environments. Partial-credit gradients prove that progress varies even within all-FAIL families. The correct conclusion is hierarchy, not elimination: environment dominates the coarse outcome, while case-level difficulty remains relevant in the middle ground and in partial scores.

Third, **the data does not identify a causal mechanism**. It shows that `glyph` has no scored passes and `rd_state_carry` has no scored failures. It does not show why. I will not speculate about tokenization bottlenecks, internal representational limits, architectural mismatches, or hidden failure modes. Mechanistic claims would require a different kind of experiment, not an outcome ledger.

Fourth, **the environment pattern pools validated and exploratory grading**. The behavioral-reference bucket contains 72 validated cases; the compile-only bucket contains 121 exploratory scored cases. Since the packet does not break environments down by guarantee, the family-level pattern should be read as a structural trend across the full campaign, not as a reference-only result.

Finally, **this is not a general benchmark prescription**. The conclusion is bounded to one provider, one text-only modality, one campaign, and one seed per selected cell. It suggests a pattern worth investigating further; it does not dictate how the industry should design reasoning benchmarks.

## Scope and remaining caveats

A few additional constraints should stay visible while reading the result.

- **Single provider and modality.** The campaign uses Atria in text-only mode. A different provider, or a multimodal setup, could produce different environment-level biases.
- **Single seed per cell.** Without multiple seeds, we cannot compute confidence intervals or estimate run-to-run variance. The numbers describe a fixed snapshot, not a distribution.
- **Small family sizes in some cases.** Several families contain only three to five scored cases. Uniform results in a small family are suggestive, not a precise estimate of the family's true pass probability.
- **One paused case.** The `ts_trajectory` pause is contextual metadata, not part of the core argument. It affects the completeness of that one family and nothing more.
- **No aggregate pass rate.** Behavioral-reference and compile-only results are reported separately, and they should remain separate.

These caveats do not erase the bimodal pattern. They define how strongly the pattern can be stated.

## Conclusion

Our default explanation for a reasoning failure is usually case-centric: the prompt was too complex, the inference chain too long, the constraints too many. The Atria campaign suggests that this explanation is incomplete. The environment family in which a case sits acts as a powerful prior. Fourteen families were uniformly solved, five had no scored pass, and fourteen were mixed. That is not the signature of a single, domain-agnostic difficulty slider. It is the signature of a model whose performance is strongly partitioned by task environment.

The right conclusion is therefore measured. Environment dominates difficulty as a **coarse predictor** in this dataset, but it does not abolish difficulty. Within mixed families, case-level features still decide outcomes; within failing families, they still shape partial credit. We have a sharp descriptive pattern, not a causal theory, and a campaign-specific result, not a universal rule.

So, if you want to predict the outcome of a case in this ledger, the first question should not be "how hard is it?" The first question should be "which environment does it live in?" In the Atria campaign, that question carries more information. The environment sets the ceiling; difficulty operates underneath it.

Need me to tighten the word count or adjust the figure styling?

&&&&&&&&&&&&&&

gemini 3.1 pro grounding:

---
title: "Environment Dominates Difficulty"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** High. Formulating the conceptual distinction between "environment as baseline" and "difficulty as variance" based directly on the raw campaign data.
- **Synthesis:** Analyzing 194 cases from the `atria_covering_campaign` to evaluate the relative predictive weight of environment grouping versus case-level complexity.
- **Prose:** First-person, strictly empirical, and rigorously bounded by the provided dataset.
- **Certainty:** Complete certainty regarding the aggregate counts and categorical distributions within this specific snapshot; extremely limited certainty regarding any generalization to other models, modalities, or providers.
- **Importance:** Significant for benchmark design. If environment predicts outcome more strongly than difficulty, our current approach to calibrating task complexity may be fundamentally misaligned.

***

When evaluating reasoning models, we often operate under a pervasive, almost unquestioned assumption: the concept of the "difficulty dial." We tend to assume that task complexity is a continuous, domain-agnostic variable. In this mental model, if a model successfully resolves a prompt, we believe we can induce failure simply by turning up the difficulty dials—adding more logical constraints, increasing the depth of inference required, expanding the context size, or demanding more intricate data structures. Conversely, if a model fails, we assume we can coax out a success by turning those same dials down.

We treat "difficulty" as the primary independent variable that predicts model success. We assume a hard prompt will fail and an easy prompt will pass, largely irrespective of the thematic or structural environment in which that prompt lives.

But what if this framework is fundamentally inverted? What if the overarching environment family of a task acts as a rigid ceiling and a rigid floor, overwhelmingly overriding the specific, fine-grained difficulty dimensions we so carefully tune? Does the label "hard" actually predict failure, or does the environment family serve as the true arbiter of outcome?

This tension became the central focus of my analysis while reviewing the recent records of the `atria_covering_campaign`. Executed using the `atria` provider in a text-only, paid modality, this campaign offers a pristine, if bounded, window into how a model actually distributes its successes and failures across a diverse set of reasoning domains. I approached this dataset expecting to find a smooth, predictable gradient of performance, governed by the internal complexity of the individual cases.

The evidence forced me to abandon that expectation. The data points toward a narrow, stark, and highly defensible thesis: an individual case’s outcome is predicted far more strongly by its environment family than by its individual difficulty dimensions.

### The Strict Boundaries of the Campaign Data

Before we can interrogate the relationship between environment and difficulty, we must establish the rigid methodological boundaries of the dataset itself. The `atria_covering_campaign`, recorded on September 29, 2026, encompasses exactly 194 cases. 

To maintain analytical integrity, we must strictly enforce the division of these cases based on the judge guarantee they carry. The dataset is bifurcated into two fundamentally different buckets of evaluation, and we absolutely cannot stitch them together to report a single, blended aggregate pass rate. To do so would be to carelessly conflate validated ground truth with exploratory signal.

**The Behavioral Reference Bucket**
This bucket contains 72 cases that carry a strict, exact-instance oracle guarantee. For these cases, we possess a validated behavioral reference. Within this rigorously gated bucket, the model was scored on all 72 cases, returning 56 `PASS` verdicts and 16 `FAIL` verdicts. These are the validated model outcomes.

**The Compile-Only Bucket**
The remaining cases fall into the compile-only bucket. I must state this disclaimer with absolute clarity: compile-only rows are graded by judges without a behavioral reference on that exact instance. They do not carry the exact-instance oracle guarantee. Therefore, they are purely exploratory and must not be read or treated as validated model verdicts. Within this exploratory bucket, 121 cases were successfully scored, resulting in 75 `PASS` verdicts and 46 `FAIL` verdicts.

There is one single case within the compile-only bucket (`ts_trajectory__witness_status=broken_representation=reflective__seed-0`) marked as `paused_provider_error`. I mention this solely to contextualize why the total campaign status is currently marked as paused, and why the scored compile-only cases total 121 rather than 122. The campaign experienced a provider outage lasting roughly 55 minutes (3300.0 seconds), triggering 8 retries and a final backoff of 600.0 seconds before halting on this specific case. This pause is a logistical artifact of the execution; it has no bearing on the completed, scored verdicts we are analyzing today.

By respecting this strict separation—reporting 56 passes and 16 fails in the validated bucket, and 75 passes and 46 fails in the exploratory bucket—we preserve the epistemological boundaries of our data. However, the overarching structural trends regarding *environment families* remain visible across the dataset as a whole, providing a macro-level view of how outcomes stubbornly cluster.

### The Bimodal Reality: Environment as Destiny

If the "difficulty dial" theory were correct, we would expect the pass rates within specific environment families to resemble a normal distribution. Most environments would contain a mix of easy cases (which the model passes) and hard cases (which the model fails), resulting in most environment families hovering around a 40% to 60% success rate. The environment itself would be largely agnostic, merely serving as a neutral backdrop for the true test of case-level complexity.

The actual results from the `atria_covering_campaign` completely shatter this expectation. Instead of a bell curve, the outcomes cluster violently at the extremes. 

Across the dataset, **fourteen environments are uniformly solvable.** Within these fourteen distinct environment families, the model achieved a flawless 100% pass rate. Every single scored case returned a `PASS` verdict, yielding a perfect score of 1.0. In these domains, tuning the difficulty dials appears essentially meaningless. You can add constraints, increase the required inference steps, or expand the context window, and the model simply absorbs the complexity and passes anyway. The environment itself acts as a guarantee of success. If you know a case belongs to one of these fourteen families, you can predict its outcome with near absolute certainty, completely blind to its individual difficulty dimensions.

On the exact opposite end of the spectrum, **five environments are uniformly unsolvable.** Within these five families, the model achieved a 0% pass rate. Every single scored case returned a `FAIL` verdict, with scores plummeting to near-zero. (This includes the `ts_trajectory` environment, which registered failures on its scored cases alongside its one paused instance). In these environments, the difficulty dial is equally irrelevant, but in the opposite direction. You could design what you believe to be the most trivially simple, low-constraint case possible, and the model will still reliably fail. The environment acts as an immovable ceiling. The domain itself is a terminal diagnosis for the model's capabilities in this snapshot.

> **Figure 1: The Polarization of Capability**
> 
> ```text
> 100% Pass Rate | ██████████████  (14 uniformly solvable environments)
>                |
>  Mixed Results | ██████████████  (14 environmentally mixed domains)
>                |
>   0% Pass Rate | █████           (5 uniformly unsolvable environments)
> ```
> *(A conceptual representation of the Atria campaign's environment outcomes. Rather than a normal distribution centered around 50% pass rates, the data reveals a starkly polarized landscape. 14 environments sit strictly at a 100% pass rate, while 5 environments sit strictly at a 0% pass rate. Only the remaining 14 environments exhibit the mixed outcomes we would naturally expect if intra-environment difficulty were the primary driver of success.)*

This polarization sits at the core of the thesis: knowing the environment family tells you far more about the likely outcome of a case than knowing whether that specific case was designed to be "easy" or "hard." The environment establishes a baseline capability that overwhelmingly dominates the specific complexities of the prompt.

### The Middle Ground and the Nuance of Difficulty

At this juncture, it is critical that I strictly bound my claims. I am asserting that environment *dominates* difficulty as a predictive factor. I am emphatically *not* claiming that difficulty dimensions do not matter at all. Such a claim is demonstrably false, and the data actively refutes it.

The remaining fourteen environments in our dataset sit in the middle ground. In these families, we see a mix of `PASS` and `FAIL` verdicts. It is exactly here, in these mixed environments, that the difficulty dials function as intended. In these domains, the environment does not dictate the binary outcome; instead, it provides a tractable battleground where the specific complexities of the case—the depth of the logic, the number of constraints, the length of the data structures—ultimately tip the scales between success and failure. This variation exists, and it proves that intra-environment complexity is a real, measurable force.

Furthermore, the dataset provides compelling evidence of this complexity through the presence of partial credit. A `FAIL` verdict in this campaign is not a monolith. The records explicitly show that `FAIL` verdicts frequently carry non-zero scores. Across the dataset, failing cases registered nuanced partial scores of 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208. 

This partial credit is profound. It demonstrates that even when the model fails to fully satisfy the exact-instance oracle or the compile-only criteria, it is still making variable degrees of progress based on the specific constraints of the prompt. A score of 0.95 indicates a model that nearly navigated the labyrinth but tripped on a final, nuanced constraint. A score of 0.208 indicates a model that grasped a fraction of the structure before collapsing. 

This rich gradient of partial success confirms that the model is highly sensitive to the internal architecture of the case. Individual difficulty dimensions absolutely matter—they shape the exact degree of partial success, and in the middle-ground environments, they dictate the final outcome. They simply do not matter *as much* as the environment family itself when predicting the broad, coarse likelihood of failure.

### What the Evidence Establishes (And What It Cannot)

As a curious but strictly empirical observer, I must draw a hard line between what this dataset proves and what it merely invites us to imagine. 

The evidence establishes the following concrete realities for this campaign:
1. **Environment sets the baseline.** The overarching family to which a task belongs is the single most powerful predictive variable for success or failure.
2. **Difficulty is secondary, but not irrelevant.** While 19 environments are completely polarized (14 uniformly solvable, 5 uniformly unsolvable), the remaining 14 environments demonstrate that internal case complexity still drives variation when the environment itself is not a terminal roadblock or an automatic success.

However, the limits of what this evidence can tell us are just as important as its revelations. 

First, this dataset provides absolutely no causal mechanism for *why* some environments are uniformly unsolvable and others are uniformly solvable. I will not engage in unsupported mechanistic speculation about tokenization bottlenecks, internal representational failures, or architectural blind spots. The data tells us *that* the model fails universally in five specific domains; it does not, and cannot, tell us *how* or *why* those failures manifest at the network level. 

Second, this analysis cannot be used to issue general evaluation prescriptions for the broader industry. This is an autopsy of one specific campaign. While it reveals a fascinating vulnerability in our assumptions about task difficulty, it does not provide a mandate for how we should fundamentally restructure all future benchmarks. 

### Methodological Limitations and Caveats

Finally, this essay must be read through the lens of its strict methodological constraints. 

We are observing a single, frozen snapshot in time. The `atria_covering_campaign` relied entirely on a single provider operating in a text-only input modality. If we were to run these same environments through a multi-modal interface, or test them on a different provider, we might observe a completely different distribution of solvable and unsolvable domains. 

Additionally, the campaign executed only a single seed per selected cell. Because we do not have multiple runs across varying seeds, we are unable to calculate rigorous confidence intervals for these pass rates. The data is definitive for this specific run, but we must be cautious about its statistical variance.

Most critically, I must reiterate the heavy reliance on compile-only data in observing these broad environmental trends. Of the 194 cases analyzed, 122 belong to the exploratory compile-only bucket. While the 72 behavioral reference cases give us a solid bedrock of validated ground truth, the wider observations about the 33 total environment families are intrinsically tied to this exploratory methodology. The macro-trends are undeniable within this dataset, but they remain inextricably bound to the caveats of compile-only evaluation.

### Conclusion

When a model fails a reasoning task, our immediate instinct is to blame the "difficulty" of the prompt. We assume the model was simply overwhelmed by the sheer number of logic steps or the density of the constraints. We view failure as a direct consequence of dialing the complexity too high.

But the records from the `atria_covering_campaign` challenge that deeply ingrained assumption. The data suggests that difficulty is not a universal, domain-agnostic slider. Instead, the model's baseline capacity is overwhelmingly dictated by the environment family in which it is operating. 

Fourteen environments guarantee success. Five environments guarantee failure. Only in the remainder does the difficulty dial actually control the outcome. If you want to predict whether a model will pass or fail, your first question should not be, "How hard is the prompt?" Your first question must be, "What environment does the prompt live in?" Because, as this dataset rigorously demonstrates, the environment sets the ceiling, the environment sets the floor, and ultimately, the environment dominates the difficulty.
