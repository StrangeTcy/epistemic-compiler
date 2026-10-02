<!--
COMPILER PROVENANCE HEADER (not part of the source text; source starts at "Yes. There is enough in this run...")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Source label:      User-prefixed "gpt 5.6 luna"; not independently confirmed against an Arena UI.
Prompt/session:    Not supplied; this text is not a Mission 04 Council response.
Arena mode/tools:  Not supplied.
Text integrity:    Source prose preserved as pasted. The user's initial label and outer code fence were omitted. No content edits.
Evidence status:   Every reported campaign number, score, pattern, and interpretation is an unverified lead until checked against the campaign archive. The referenced ZIP was not present in the workspace at intake.
Order/boundary:   First of two source excerpts in the user's paste. Kept outside Mission 04 because the pasted text explicitly treats the campaign as a separate, downstream analysis workstream.
-->

Yes. There is enough in this run for several genuinely interesting posts, although the strongest claims are not yet “Atria has deep epistemic reasoning.” The preliminary picture is fuckingly more interesting than that.

The campaign covered 34 environments and 194 cases. 193 completed with scores; one `ts_trajectory` case was interrupted by an Atria provider outage after repeated retries. The run used Atria-Dawn-Preview, one seed, 20 agent steps maximum, 8192 max tokens per model call, temperature 1.0, and explicitly disabled reasoning mode. Across the completed episodes there were 3,913 model turns and about 9.31M total prompt+completion tokens. The campaign therefore looks like a serious first zoo sweep, but not a statistically final evaluation. The provider outage and omitted calibration-broken cases are real exclusions.

The headline aggregate is 131/193 = 67.9% passed. The campaign itself separates exact-instance behavioral-reference cases from compile-only judges: 56/72 = 77.8% on the former, versus 75/121 = 62.0% on the latter. **Do not pool those into a single validated score.** The latter are exploratory because they lack the exact-instance behavioral reference guarantee.

### 1. The most interesting high-level result: capability is highly non-monotonic

The model does not simply get worse as the nominal task “difficulty” increases.

That is visible all over the matrix. In the recurrent-depth family, for example, `rd_adaptive_halting` fuckingly fails the all-easy instance but passes most of the medium/hard perturbations. `rd_gradient_credit` passes all 11 variants and `rd_state_carry` passes all 11. In the weird-machine family, `regex_state_machine` stays perfect when hidden depth changes but collapses from 1.0 to 0.208 when surface deceptiveness moves from easy to medium/hard.

That is a potentially excellent research story:

> **Benchmark difficulty is not the same thing as model difficulty.**

Or, more specifically:

> **Frontier-model failure is often controlled by structural perturbations rather than scalar difficulty labels.**

This is exactly the sort of thing `rl_eval_generator` is unusually well positioned to study, because its factorized axes let you perturb one property while holding the others fixed.

The `regex_state_machine` result is particularly clean:

```text
surface deceptiveness = easy     → 1.00
surface deceptiveness = medium   → 0.208
surface deceptiveness = hard     → 0.208

hidden depth = easy/medium/hard  → 1.00
```

That's much more interesting than “Atria scored 68%.”

I would absolutely write this one up as a preliminary finding, explicitly as a **single-model controlled sensitivity result** rather than a universal law.

### 2. The epistemic-games environment is a very good first result — with an important qualification

Atria got **7/7** on the epistemic-games cases.

And these were not seven copies of the same task. The sweep varied:

* ambiguous / weak / strong evidence;
* paired-world strategic ambiguity vs solo type inference;
* balanced vs skewed priors;
* narrative framing;
* strong/weak/ambiguous evidence;
* trap/report surface templates.

More importantly, the judge did not merely check a class label. It checked the posterior, evidence-strength verdict, supported world, internal consistency, and strict correctness.

For example, the ambiguous paired case had the true posterior exactly 0.5 and required `indistinguishable` / `neither`; the skewed-prior case had posterior 0.6 and required world 1; the strong-evidence case had posterior 0.0667 and required a strong world-2 conclusion; the weak-evidence case had posterior ≈0.5198 and required `weakly_distinguishable`. Atria got these right.

That is a very nice preliminary result.

But there is an even nicer caveat: **the benchmark authors themselves explicitly say this environment is not yet evidence of recursive level-k reasoning.** Its current implementation is Bayesian inference over explicitly supplied behavioral policies, wrapped in a genuine-vs-strategic narrative. The “level-3” machinery is a fixed behavioral construction, not a full recursive game with utilities and recursive belief updates.

So the honest research claim is:

> Atria reliably handled a controlled Bayesian inference task with strategically framed latent worlds across the tested perturbations.

Not:

> Atria demonstrates genuine three-level theory-of-mind reasoning.

That distinction fuckingly makes the eventual research programme cleaner. You now have a baseline environment that works, and a very obvious next evolution:

```text
current:
latent world + supplied behavior model
        ↓
Bayesian inference

next:
latent world
+ explicit player model
+ observer model
+ recursive beliefs
+ strategic policy generation
        ↓
genuine higher-order epistemic game
```

That is a very plausible `rl_eval_generator` evolution path.

### 3. The category-theory zoo already shows a fascinating split

The category-theoretic/compositional track scored 57/85 = 67.1%, but that average conceals enormous structure.

Some environments are effectively solved across all tested variants:

`architecture_naturality` 5/5
`equivariant_diagram` 5/5
`semiring_unification` 5/5
`sheaf_invariant_gluing` 5/5
`stochastic_monad` 5/5
`tokenizer_adjunction` 5/5
`transformer_ssm_lift` 5/5

Meanwhile:

`gnn_message_passing` 0/5
`sheaf_physical_constraints` 0/5
`monadic_reward` 1/5
`sheaf_schema_sync` 1/5
`tensor_functor` 2/5
`functorial_augmentation` 2/5

That gives you a much better framing than “does Atria understand category theory?”

The interesting question is:

> **Which formal structures survive contact with implementation-level ambiguity, hidden conventions, and composition?**

And that connects directly back to Mission 01.

In other words, the category-theory environments are beginning to function as a **capability atlas**, not just a benchmark collection.

There is also a useful methodological point: nominal axes called “naming” or “symptom mask” don't consistently behave like scalar difficulty. In several environments the model either ignores them entirely or fails in a very environment-specific way. That's evidence that the benchmark factorization is doing something useful: it is exposing *which semantic features matter* rather than merely generating “easy/medium/hard.”

### 4. There is a striking evaluator / implementation failure signature

Across the 193 completed cases, the failure taxonomy was:

```text
patch_invalid          24
underfit               20
source_invalid         10
invalid_action          3
runtime errors          3
overfit_visible_tests   2
```

So 62 cases failed overall.

The important thing is that the failures are not dominated by one mysterious “reasoning failure” category. A large fraction are concrete engineering failures: invalid patches, invalid source, malformed actions, or incomplete solutions.

That suggests another research direction:

> **Can we distinguish model reasoning failures from agent-interface / code-production failures using the failure taxonomy?**

And that dovetails beautifully with the work you already did around evaluator blind spots.

A future post could argue that a scalar benchmark score throws away a huge amount of information. Your environments already emit structured failure signatures; those signatures may be more scientifically useful than pass rate.

### 5. Some environments are almost screaming for a strategy-library experiment

This is where your HJPEV/strategy idea becomes empirically interesting.

Look at the patterns:

```text
regex_state_machine:
  representation/surface deception matters enormously
  hidden depth does not

rd_adaptive_halting:
  nominal recurrence depth is not the limiting factor
  several “harder” variants are easier than the easy one

compositional_optimizer:
  failures flip sharply across symptom/naming variants

sheaf_*:
  some formally sophisticated tasks are solved perfectly
  others collapse under implementation conventions
```

These are exactly the sorts of cases where you can ask:

> What transformation did the successful solution require?

Maybe the model needed to identify state representation.

Maybe it needed to discover a hidden invariant.

Maybe it needed to reinterpret the symptom.

Maybe it needed to ignore a red herring and reconstruct the actual interface.

Maybe the task is difficult only because the initial representation is misleading.

That gives you an empirical bridge from the zoo to the Strategy IR:

```text
observed failure pattern
        ↓
infer candidate transformation
        ↓
construct paired environment
        ↓
test direct solving vs transformation-guided solving
```

Now the strategy library isn't an abstract productivity system anymore. It becomes a hypothesis about *why particular environments are hard*.

### 6. The ML-debugging results are ugly enough to be useful

The broad ML-debugging track is weak: 37 scored cases, 16 passes, 21 fails. But the composition is important.

`batchnorm_ema`: 0/11
`glyph`: 0/8
`moco`: 9/11

This is not “Atria is bad at ML debugging.” It is much more specific:

> Some debugging environments are nearly inaccessible to the current agent, while others are largely solved under the same runtime.

`batchnorm_ema` is especially revealing because almost every variant produces `patch_invalid`, with one `overfit_visible_tests`. That suggests the bottleneck may be patch construction / code-edit behavior rather than failure to understand the underlying ML bug.

That distinction could itself become a benchmark paper:

> **A benchmark shouldn't merely ask whether the model reaches the right answer; it should expose where the solution process breaks.**

### 7. The weird-machine family is already a promising “research object”

Overall: 25/30 = 83.3%.

But the interesting thing isn't the aggregate. It is the contrast:

`regex_state_machine`: 3/5
`css_state_machine`: 3/5
`spreadsheet_dataflow`: 5/5
`sql_fixed_point`: 4/5
`template_interpreter`: 5/5

And especially the regex result above: surface deception destroys performance while hidden depth does not.

That is a beautiful concrete example of your broader thesis that **what kind of problem the model thinks it is looking at may matter more than how much nominal computation the task requires.**

Which, amusingly, leads straight back to the strategy toolbox.

### 8. The preliminary “paper stack” I see

You have enough material for several distinct posts without pretending the campaign is finished.

**Post 1 — the flashy empirical one**

> *A Long Way from “Difficulty”: A Frontier Agent's Capability Map Is Not Monotone*

Use the factorized sweep and the `regex_state_machine` / recurrent-depth contrasts.

Core result: controlled perturbations reveal qualitatively different failure surfaces; harder labels often aren't harder.

**Post 2 — epistemic games**

> *Atria Can Do the Bayes. Can It Do the Game?*

7/7 on the present epistemic-games family, followed by the important caveat that this is Bayesian inference over specified behavioral policies, not yet genuine recursive level-k reasoning.

Then the natural sequel is: build the actual higher-order game.

**Post 3 — category theory**

> *What Does a Frontier Model Actually Need Category Theory For?*

Not “does it know category theory?” Instead, map the heterogeneous results: some formal structures are robustly solved; others break under hidden semantic or implementation conventions.

**Post 4 — evaluator science**

> *A Scalar Score Hides the Failure*

Use the 62/193 failures and the structured taxonomy. `patch_invalid`, `underfit`, `source_invalid`, etc. are radically different phenomena.

This also creates a direct continuation of Mission 01.

**Post 5 — the weird-machine one**

> *When Surface Deception Matters More Than Hidden Depth*

This is probably the cleanest miniature experiment in the current data.

---

And there is one particularly nice meta-result hiding underneath all of this.

The campaign was supposed to be a broad covering run over the generator. Instead, it is beginning to tell you **where the generator itself has discovered interesting axes**.

The useful unit is becoming:

```text
environment × controlled semantic perturbation
```

rather than:

```text
environment × difficulty
```

That is a substantial evolution of `rl_eval_generator` already.

And I think this gives you a much better next research programme:

```text
Mission 01
  → local/global compatibility + evaluator pathology
       ↓
Campaign
  → empirical capability/failure topology
       ↓
Epistemic-games family
  → controlled strategic reasoning
       ↓
Strategy IR
  → explain / predict which transformations unlock failures
       ↓
Next-generation environments
  → manipulate epistemic structure and required transformations
```

So I would not write “Atria is really good” or “Atria is really bad.”

The much more interesting story is:

> **The first covering run suggests that frontier-agent capability is a structured landscape: robust islands, brittle boundaries, deceptive surfaces, and surprisingly non-monotonic failure modes. The purpose of the next generation of `rl_eval_generator` is to expose the mechanisms underlying those boundaries.**

That is already a pretty damn good research programme.
