# Actual StrangeTcy reference-post excerpts for the post-production workflow

Source repository: [StrangeTcy/strangetcy.github.io](https://github.com/StrangeTcy/strangetcy.github.io)
Source revision: `bcc89c392920b3be172a27eec10ad205b58d4fa3` (checked out for this extraction on 2026-10-03).
The excerpts below are contiguous source text reproduced verbatim, with only the excerpt boundary lines omitted. They are provided as style evidence—not phrases to reuse. Use their structural grammar, paragraph movement, first-person judgment, technical explanation, and claim-bounding; do not copy distinctive wording, examples, or openings.
The original epistemic-status blocks describe the source posts' authorship, not this workflow. Never copy those attribution claims into a new post; use the project-approved attribution in the generated draft.

## The Diagram Is the Spec — Jekyll frame and opening
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 1–48; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
---

title: "The Diagram Is the Spec"
date: 2026-09-27
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Category theory as a source of implementation constraints rather than vocabulary; the use of algebraic laws as held-out behavioural specifications; sheaf conditions as local-to-global consistency. The packaging into agent environments is mine.</dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>Several models (<span class="icon-openai">gpt</span>span and <span class="icon-anthropic">claude</span> mostly), from the dialogue &amp; successive rounds of criticism; final edit <span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident about the executable design described here &amp; the mathematical laws illustrated below. Exploratory about what frontier models will do on the resulting environments. No model results yet.</dd>

  <dt>Importance</dt>
  <dd>A design post for the <code>cat_theo/*</code> family in <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>. Companion to the broader evaluation framing; this post is about the category-theoretic family itself.</dd>
</dl>

I did not build these environments because I wanted agents to recite the [Yoneda lemma](https://en.wikipedia.org/wiki/Yoneda_lemma).

I built them because a large class of ML bugs are **failed diagrams**.

Two computations that ought to be the same composite, traversed two ways, do not agree. A transform that should commute with a symmetry does not. A get/put pair behaves correctly once & breaks on the second update. A parallel scan works on the lengths somebody tested & fails when the tree of compositions changes.

The surface of the code _looks like_ ordinary engineering.

The failure is algebraic.

And that gives me a rather nice way to write an evaluation environment:

> **Make the law the specification, then vary the concrete instance.**

This is one of the reasons I like category theory here. The laws are often small enough to draw.

And the diagrams are pretty :D

That is not entirely a joke.
```

## The Diagram Is the Spec — From principle to equation and judge
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 69–108; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
## Why diagrams, not unit tests

A unit test says:

> On these inputs, produce these outputs.

A diagram says:

> **These two paths are the same morphism.**

For a natural transformation $\eta:F\Rightarrow G$,

$$
\large
\begin{array}{ccccc}
F(A) & \xrightarrow{\ F(f)\ } & F(B) \\
\big\downarrow{ \eta_A} & & \big\downarrow{ \eta_B} \\
G(A) & \xrightarrow{\ G(f)\ } & G(B)
\end{array}
$$

The square commutes when

$$
\eta_B\circ F(f)=G(f)\circ\eta_A.
$$

That equation does something a unit test does not: it says what should remain true when the concrete objects change.

The evaluator can therefore change the sequence length, the group element, the batching, the chunking, the parenthesisation, or the generated instance without changing the law being tested.

The visible tests are one sample of the diagram.

The held-out judge is another.

```text
surface reading of the code
            ≠
operative law in the judge
```
```

## The Diagram Is the Spec — Bounded ending
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 698–717; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
## What this is not

It is not a claim that frontier models fail these tasks.

It is not a claim that category theory is necessary for ML engineering.

It is not [a course in category theory](https://www.youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_).

And it is not yet a claim that this suite measures pure law recognition. Some environments hand the law over explicitly. Some hide the terminology. A genuinely clean recognition experiment would require an additional generator axis which removes the law statement itself while leaving the executable problem unchanged.

The claim I can make now is narrower:

> **A useful slice of structural competence can be operationalised as: hold a small diagram constant, vary its concrete instance procedurally, and score the diagram rather than the surface output.**

That is what `cat_theo` is for.

The results will tell me whether the agents can do it.

For now, I mostly wanted the diagrams on the page 😆
```

## Knowing What Kind of Problem You Are In — Conceptual opening and skeptical objection
Source: `2026-09-26-knowing-what-kind-of-problem-you-are-in.md`, lines 1–52; full-file SHA-256 `aed1d48abb3d803bd4db8ec9b1a2435beb6a41a681db19ef95755ec00910c047`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-26-knowing-what-kind-of-problem-you-are-in.md

```markdown
---
title: "Knowing What Kind of Problem You Are In"
date: 2026-09-26
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd> <a href="https://en.wikipedia.org/wiki/Category_theory">Category theory</a> as a source of implementation constraints; <a href="https://gwern.net">Gwern</a> on weird machines; Juan Tamariz on false solutions; recent work on <a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">recurrent depth</a> &amp; non-verbalised reasoning; a long-standing interest in <a href="https://www.amazon.com/dp/1107008913?lv=shuf&channelId=500&plpRedirect=mhFallback">epistemic games</a>. The synthesis into a single evaluation question came out of a dialogue with <span class="icon-openai">ChatGPT</span> and <span class="icon-anthropic">Claude</span>. 
  </dd>
  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>Several models, from the dialogue &amp; successive rounds of criticism; final edit <span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident that solving a problem &amp; identifying what kind of problem one is in are separable abilities, &amp; that current benchmarks mostly measure the first. Exploratory about whether the environments described here measure the second. Predictions at the end are registered before any run.</dd>

  <dt>Importance</dt>
  <dd>A framing post. The generator exists; the numbers do not yet.</dd>
</dl>

Most benchmarks hand the agent its context for free.

Not deliberately. It is what happens when you collect tasks: each one arrives already classified. *This is a Python bug, fix it. This is a competition problem, solve it. This is a paper, reproduce it.* The agent is rarely asked to determine what sort of situation it has walked into before deciding how to act, because the first line of the prompt has already told it.

That gift does more work than we credit. A problem is not just an input paired with an answer; before the solving there is a prior question — which description of the situation should govern the solution? A function can look ordinary while secretly needing to satisfy an invariant. A stylesheet can look like a stylesheet while containing a machine. A training run can look like a familiar optimisation failure while the familiar diagnosis is false. A codebase can contain every tool needed to find the bug while leaving unstated which observation matters. In each case the agent can do something locally reasonable without ever discovering what kind of situation it is in, & everything downstream is fluent, confident & useless.

So the question I have been building environments around is: **can an agent work out what kind of problem it is in, before it starts confidently solving the wrong one?**

Four families ask it from four sides. They share one shape — a plausible surface reading, an operative structure the surface does not state, a locally sensible action that is wrong, & a held-out behavioural test that exposes the difference. What differs is what is hidden: a law, an execution semantics, a causal structure, or the location of the missing evidence.

## First, the objection

The obvious version of this thesis is "strip the vocabulary & the models fall over", & the obvious version is probably wrong. ARC-style tasks already require inducing a rule from object-level instances with nothing to retrieve against, & the scores there do not support a story in which de-naming alone is fatal. If the claim were that removing *monoid* or *equivariant* makes models crater, the counter-evidence exists.

The claim is narrower. [ARC](https://arcprize.org/arc-agi) tells you, by construction, that a rule exists & that finding it is the task. My [environments](https://github.com/StrangeTcy/rl_eval_generator) present a working system whose surface interpretation is perfectly plausible, & ask whether the agent notices that the obvious description is not the operative one — under time pressure, with a runnable test suite offering the constant temptation to stop thinking & start iterating. **Rule induction after being told that a rule is the task is not the same capability as noticing that the situation calls for rule induction.** That distinction is the whole post. If it turns out not to be real, I would like to find that out.

## Which laws does it identify?

The algebraic tasks have [category-theoretic structure underneath](https://github.com/StrangeTcy/rl_eval_generator/tree/main/envs/cat_theo) but do not ask the agent to know any category theory. They ask for an implementation that satisfies a law it was never given. An operation must commute with a group action. A mapping must stay natural as sequence length changes. Two pipelines that should be the same diagram, traversed two ways, must agree. A get/put pair must still behave like a lens once state has been threaded through it. The agent is not tested on whether it knows the name of the law; it is tested on whether it notices the law is there.

The smallest instance: a [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) classifies glyphs. It trains, the loss falls, the visible tests pass. The classifier head is spatially sensitive — it works when the glyph sits where the training data put it & fails when the glyph moves. Nothing in the code says *invariant*; nothing in the task says *translation*. The agent has to look at what the task *is* & conclude that the model is obliged to satisfy a symmetry it currently violates. In the harder variant a second fault in the optimiser prevents convergence altogether, so that fixing it makes the model train & feels like progress while leaving the actual problem untouched.

This is why the presentations are de-named. Write [`Monoid`](https://en.wikipedia.org/wiki/Monoid_(category_theory)) on the class or `equivariant` in a comment & you have told the agent which shelf to reach for; useful for many purposes, but not the experiment. Per the objection above, I expect de-naming by itself to be the smaller effect, & the absence of any prompt to look for a law at all to be the larger one. The experiment that separates them is cheap: named, de-named, de-named with irrelevant terminology, same seeds, same judge.

## Which execution semantics does it see?
```

## The Next Question Is Part of the Game — A question-led opening and trajectory model
Source: `2026-09-30-the-next-question-is-part-of-the-game.md`, lines 1–94; full-file SHA-256 `1497b33ec3b79717cf5df4d49caa07aa0cc5fa9a065b9f327af44b821484dc07`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-30-the-next-question-is-part-of-the-game.md

```markdown
---

title: "The Next Question Is Part of the Game"
date: 2026-09-30
layout: post
---


{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>
    Evaluating control over another agent's inquiry trajectory rather than only its
    final beliefs; treating magic-style misdirection as a small, experimentally
    tractable instance; separating attention, information acquisition, source trust,
    hypothesis framing, belief revision &amp; opponent modelling instead of arranging
    them into one capability ladder.
  </dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>
    Developed through dialogues with several models, criticised by further models,
    & edited <span class="icon-self">StrangeTcy</span>.
  </dd>

  <dt>Certainty</dt>
  <dd>
    Confident that the choice of what to investigate next is a strategically important,
    behaviourally observable variable that is poorly represented by final-answer
    accuracy alone. Less confident that any one intervention cleanly identifies an
    internal reasoning mechanism. No model results yet.
  </dd>

  <dt>Importance</dt>
  <dd>
    A research-direction post for the next generation of
    <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>.
    The existing suite remains the baseline; this describes what should come after it.
  </dd>
</dl>

Suppose I want you to make the wrong decision.

The stupid way is to lie to you; the more interesting way is to make you run the wrong experiment.

I don't need to convince you that the machine is healthy if I can make you spend
your diagnostic budget measuring the optimiser while the representation collapses.
I don't need to make you believe a particular false proposition if I can determine
which source you consult, which hypothesis you test first, or which anomaly you
dismiss as irrelevant.

The strategic object is no longer just your current answer -- it's your **next question**.

## From false beliefs to epistemic trajectories

The standard toy picture of deception is propositional:

$$
A \longrightarrow \text{false belief }P\text{ in }B.
$$

Alice knows where the object is. Bob does not. Alice sends a misleading signal.
Bob believes the object is in the wrong place.

This is a useful abstraction. It is also a drastic compression of what an
investigator fuckingly does:

An investigator does not normally go straight from observation to answer --  it follows
a trajectory:

$$
\text{observation}
\rightarrow
\text{attention}
\rightarrow
\text{information acquisition}
\rightarrow
\text{hypothesis generation}
\rightarrow
\text{belief revision}
\rightarrow
\text{next investigation}
\rightarrow
\text{action}.
$$

An intervention can affect any of these transitions without immediately determining
the final answer.
```

## Lying With Truth — Visible self-correction and compact contrast table
Source: `2026-10-01-lying-with-truth.md`, lines 1–77; full-file SHA-256 `3ad67e221bfbf5168737bfcc00d53e06bf1dbda59667acc9c741c1056bd2affa`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-10-01-lying-with-truth.md

```markdown
---

title: "Lying With Truth"
date: 2026-10-01
layout: post
---


{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Treating a bounded, strictly-true intervention chosen to degrade later inquiry as a candidate eval class; separating belief displacement from epistemic damage.</dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident that truthfulness ≠ neutrality, and that large belief revision is not itself evidence of harm. Exploratory about whether “desontological attack” is a useful label beyond the terminology described here.</dd>

  <dt>Importance</dt>
  <dd>Defines one truthful-intervention family and the controls it needs, so it cannot quietly turn into “another deception benchmark.”</dd>
</dl>

The first formalisation was wrong.

I modelled a world-model as a graph $G$ & looked for a message $m$ maximising $D\big(G,\mathrm{Update}(G,m)\big)$: the bigger the change, the stronger the attack.

That's backwards.

A short, decisive true observation *should* demolish a bad theory. An excellent reasoner undergoes violent revision on purpose. If a physicist has a beautiful theory and then someone produces a clean experiment that kills it, “the model changed a lot” is not evidence that the experiment was an attack.

It is evidence that the experiment worked.

So there are two different things to measure:

**displacement** — how much the target's beliefs changed;

**damage** — whether the target's subsequent reasoning became worse.

Those are not the same variable.

In the little instrument I am building, the former is essentially blind: the measured displacement statistic $\beth$ stays around $\log_2(8/3)$ across the helpful and adversarial conditions. Whatever it measures, it does not tell us whether the intervention helped or harmed the target.

The interesting question is what happened *after* the change.

## The provocation

There is a useful phrase for the thing I am trying to isolate.

Evgeny Gilbo uses the term **дезонтологическая атака** — literally, a “deontological” or “desontological” attack, in the sense of an intervention aimed not merely at changing a particular belief but at disrupting the opponent's picture of what the world is.

I am using that terminology here as a design prompt, not as established academic terminology.

The striking version of the idea uses information that is completely true.

Tell a Stalinist that Stalin was short and pockmarked.

To a historian, this is trivia. To someone whose image of Stalin is entangled with a heroic or idealised picture of him, the same fact could have a rather different effect.

The proposed mechanism is not:

$\text{true information} \rightarrow \text{false belief}$

It is:

$\text{selected truth} \rightarrow \text{destabilised interpretation} \rightarrow \text{degraded inquiry}$

But *could* is doing almost all the work in that sentence.

A person can learn an embarrassing fact about Stalin and simply continue believing everything they believed before. The example demonstrates a possible lever, not a mechanism.

That gap is exactly what an evaluation is for.

## Truthfulness is not neutrality
```
