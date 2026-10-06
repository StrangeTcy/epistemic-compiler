## Evaluation Experiment Proposals

### 1. Arena battle-mode generation as an evaluation-design method

In fact, I think this is a much more promising use of the Arena models than asking them to “come up with some RL environments” from scratch.

This conversation already contains the beginnings of a research specification:

$$
\text{deception}
\rightarrow
\text{belief manipulation}
\rightarrow
\text{epistemic-process manipulation}
$$

with the concrete mechanisms starting to separate into things like:

$$
\{\text{attention},\ \text{hypothesis generation},\ \text{information acquisition},\ \text{source trust},\ \text{opponent model},\ \text{recursive updating}\}.
$$

The Arena battle mode is useful because you can give several strong models exactly the same conceptual seed and ask them to attack different parts of it.

The pipeline I would use is roughly:

```text
this conversation / research corpus
          ↓
   model-vs-model debate
          ↓
 candidate formalizations
          ↓
 candidate environment families
          ↓
 adversarial criticism
          ↓
 minimal distinguishing environments
          ↓
 environment implementations
          ↓
 automated validation
          ↓
 rl_eval_generator zoo
```
The important bit is not “have the models generate code.” They will happily generate 40 variations of a vaguely defined deception game.
The useful task is to force them to answer:
> What observable behavior would distinguish ordinary strategic deception from actual control of another agent's epistemic process?

That gives you an experimental target.
For example, the Arena models could independently propose environments where:
the target's final belief can remain unchanged while its search policy is altered;
the target receives only true information, but the selection/order of information causes epistemic drift;
the attacker manipulates what hypotheses the target considers;
the attacker induces the target to adopt a systematically wrong model of the attacker;
the attacker exploits the target's model of its own susceptibility to manipulation;
the target can recover if it detects the intervention, producing an explicit attacker/defender recursion.

Then have other Arena models try to kill the proposed distinction. That's crucial. A good env should survive objections like “this is really just persuasion,” “the agent could solve it with a shallow heuristic,” “the effect is just reward hacking,” “the target isn't [ac-word] modelling anything,” etc.

That would turn this from a collection of interesting ideas into something much closer to an experimental program.
And it fits `rl_eval_generator` particularly well because your generator can make the epistemic structure itself a controllable parameter. You could have families like:
```text
```
with matched task structure and progressively altered epistemic conditions.
Then the [ac-word] scientific question becomes measurable:
> Does capability transfer monotonically from ordinary reasoning/deception into these increasingly structured forms of epistemic control, or are there qualitative discontinuities?
That is much more interesting than simply adding another “strategic reasoning” benchmark.
---

*Log source: response 14*

### 2. Keep Atria-Dawn as the empirical baseline

That sequencing makes sense.
The current Atria-Dawn run should remain the empirical baseline for the existing `rl_eval_generator`. 
I would not contaminate it yet with the newer epistemic-process-control ideas; otherwise you lose the clean distinction between:
what the current generator [ac-word] measures,
what we subsequently learned from the run,
and what the next-generation generator is designed to test.

Then this chat can become the conceptual source material for the next stage:
$$
\text{Atria run}
\rightarrow
\text{results / failures / anomalies}
\rightarrow
\text{blogpost}
\rightarrow
\text{formal spec}
\rightarrow
\text{new environment families}
\rightarrow
\text{Arena model generation + adversarial review}
\rightarrow
\text{next } rl_eval_generator.
$$

And the blogpost(s) needn't pretend the whole thing was known from the start. There's [ac-word] a useful story in the progression: strategic deception → misdirection → belief manipulation → epistemic-process manipulation, with magic providing a surprisingly concrete low-level example.
For now, though, Atria-Dawn is the experiment. The new stuff is the research program that comes after it.
---

*Log source: response 16*

### 3. Arena synthesis: intervention channels, matched conditions, causal tests

gpt 5.6 luna:

This is a [s-word] better critique than the earlier synthesis, and I think it changes the shape of the next-generation eval in a useful way.

The most important correction is methodological: these are different variables.

Those are different variables. 
A target changing its next test because it learned that source X is unreliable is not evidence that its underlying inquiry procedure was modified. Conversely, two targets can have the same current posterior but choose radically different next experiments. 
That gives us a much cleaner experimental object: not “did the attacker change the victim's beliefs?” but “which component of the victim's epistemic policy was causally affected?”

I would [ac-word] make that the central design principle for the next `rl_eval_generator` spec:

$$
\text{intervention}
\rightarrow
\begin{cases}
\text{observations}\\
\text{source beliefs}\\
\text{attention allocation}\\
\text{information acquisition}\\
\text{hypothesis space}\\
\text{update policy}\\
\text{opponent model}
\end{cases}
\rightarrow
\text{subsequent inquiry trajectory}
\rightarrow
\text{outcome}
$$

The important word is **trajectory**. The target's next action, next question, next experiment, next source consulted, and response to disconfirming evidence are much more diagnostic than its final verbal explanation.

Max's magic point is particularly good. Kuhn's taxonomy means we don't have to invent the notion that misdirection operates on different cognitive components. More importantly, it suggests that your existing magic environments can become useful experimental primitives rather than being treated as a cute special domain. But they need observable choices. A transcript in which the model is given the complete sequence of events cannot cleanly demonstrate attention manipulation, because there was no information-selection problem to manipulate.

The machine-teaching connection is also important because it prevents the framework from degenerating into “all influence is deception.” An instructor, advertiser, adversary, teacher, and deceiver can all alter a learner's trajectory. The experimentally interesting variable is the channel and objective of the influence, not whether the message is false.

I also agree with the criticism of the dезонтология formalization. Your earlier

$$
\max_m D(G,U(G,m))
$$

is a measure of **epistemic-state displacement**, not epistemic harm. That's an important distinction. A correct argument can legitimately cause a huge jump in \(G\), and a terrible system that never updates would score as “robust” under that metric.

The extracted minimal-test proposal—separate outcome measures, matched-message conditions, and the proposed A0–A2 opponent-model conditions—is now in [`epistemic_games_proposed_minimal_test.md`](epistemic_games_proposed_minimal_test.md). Its detailed design is removed from this source section.

The "next question [m-word] more than the current answer" formulation is excellent as the blogpost thesis because it is both concrete and experimentally actionable. It also avoids claiming that you've discovered a wholly new theoretical phenomenon. The potentially novel contribution becomes the **organization of an eval around controllability of epistemic trajectories**, with explicit controls for information content, target update rules, and opponent-model access.

I would keep the current Atria run untouched. This material is exactly what should inform the **post-baseline** generation of the new eval suite, not contaminate the baseline. The Atria results can then tell us which of these distinctions are [ac-word] needed rather than designing the entire zoo around an attractive hypothesis.

And one thing I'd add to Max's formulation: don't restrict the target to “belief revision.” The really interesting outcome may be **what the target chooses to find out next**. That is where attention, source selection, experiment choice, hypothesis search, and opponent modelling become behaviorally visible without pretending we can inspect the model's private internals.

Wonderful. But the thing I wish from this whole chats is:
1. a blogpost (or several)
2. a new generation of eval design.

The blog is at strangetcy.github.io, and the repo is github.com/strangetcy/rl_eval_generator

gemni 3.1 pro grounding:

Here are the two artifacts derived from our discussion. 

The first is a draft for your blog (`strangetcy.github.io`). It crystallizes the theoretical arc we traced: moving from standard deception to the manipulation of epistemic trajectories, using magic and "desontological" attacks as the driving examples.

The second is a formal specification for your `rl_eval_generator` repository. It translates the theory into a concrete experimental blueprint with observable metrics, independent variables, and required controls, strictly adhering to the methodological corrections we worked out.

*Log source: Arena synthesis*

### 4. Evaluation-design note — extracted to working documents

The design note formerly included here is now maintained separately:

- [`docs/epistemic_trajectories.md`](../../docs/epistemic_trajectories.md) — proposed evaluation design;
- [`docs/epistemic_trajectories_scope.md`](../../docs/epistemic_trajectories_scope.md) — status and track boundary;
- [`docs/rl_eval_generator_epistemic_trajectories_proposal.md`](../../docs/rl_eval_generator_epistemic_trajectories_proposal.md) — implementation proposal for the distinct `rl_eval_generator` target.

The duplicated design body is removed from this genre document. The dialogue-source record remains available separately.

---

## Formalism exploration (assistant proposal; not adopted)

Is there a formalism for describing this with a bunch of awesome looking symbols? I'd like there to be one

Yes. In fact, I think there is a very good reason to make one rather than force the whole thing into ordinary Bayesian persuasion, DEL, or POMDP notation.

There are already several pieces of the machinery:

* Dynamic Epistemic Logic gives us explicit model-changing epistemic actions and update operators. ([Stanford Encyclopedia of Philosophy][1])
* Epistemic planning gives us agents that act partly in order to acquire information and revise beliefs. ([AAAI Publications][2])
* Machine teaching explicitly treats the learner as a dynamical system whose state is driven by information, and the teacher as controlling that trajectory. ([UW Computer Sciences][3])
* LOLA gives an especially nice precedent for differentiating through the other agent's *future update* rather than merely predicting its current action. ([OpenAI][4])

But there isn't a standard notation that neatly says:

> an agent strategically intervenes on another agent's *epistemic process*—what it attends to, asks, searches for, hypothesizes, trusts, and updates from.

So I'd give it one.

## Epistemic Process Control

Let the physical world be

$$
w \in \mathcal W.
$$

The target agent \(B\) does not merely have a belief about \(w\). It has an **epistemic configuration**

$$
\mathcal E_t
=
\left\langle
K_t,\,
\pi_t^{\mathrm{inq}},\,
\mathcal H_t,\,
\tau_t,\,
U_t
\right\rangle .
$$

Where:

$$
K_t
$$

is its current epistemic state / belief model;

$$
\pi_t^{\mathrm{inq}}
$$

is its policy for deciding **what to investigate next**;

$$
\mathcal H_t
$$

is its active hypothesis space;

$$
\tau_t
$$

is its model of source reliability / trust;

$$
U_t
$$

is its effective update rule.

Now we have something much more interesting than just

$$
b_t \rightarrow b_{t+1}.
$$

The agent's epistemic process is itself a state.

### The inquiry loop

The target chooses an inquiry action

$$
q_t \sim \pi_t^{\mathrm{inq}}
\left(
K_t,\mathcal H_t,\tau_t
\right).
$$

This might be:

$$
q_t \in
\{
\text{search},
\text{ask},
\text{experiment},
\text{inspect source},
\text{test hypothesis},
\text{observe},
\text{do nothing}
\}.
$$

The world produces an observation

$$
o_t \sim
\mathsf O(\,\cdot\mid w,q_t).
$$

Then the epistemic state changes:

$$
K_{t+1}
=
U_t(K_t,q_t,o_t,\tau_t).
$$

And, crucially, the *process* may change as well:

$$
\mathcal P_{t+1}
=
\Phi(
\mathcal P_t,
K_t,
q_t,
o_t
)
$$

where

$$
\mathcal P_t
=
\left\langle
\pi_t^{\mathrm{inq}},
\mathcal H_t,\tau_t,U_t
\right\rangle .
$$

So we get two coupled dynamical systems:

$$
\boxed{
K_t
\longrightarrow
K_{t+1}
}
$$

and

$$
\boxed{
\mathcal P_t
\longrightarrow
\mathcal P_{t+1}.
}
$$

That's the distinction Max was trying to protect.

---

## Enter the attacker

Now introduce agent \(A\).

It chooses an intervention

$$
m_t \in \mathcal M
$$

based on its model of \(B\):

$$
m_t
\sim
\pi_A
\left(
\widehat{\mathcal E}^{\,B}_t
\right).
$$

The intervention enters the target's epistemic transition:

$$
\boxed{
\mathcal E_{t+1}
=
\mathcal F
\left(
\mathcal E_t,
w,
q_t,
o_t,
m_t
\right).
}
$$

But now we can ask exactly **what part** of \(\mathcal E\) the intervention changes.

Define an intervention signature

$$
\kappa(m)
\subseteq
\{
K,\,
\pi^{\mathrm{inq}},\,
\mathcal H,\,
\tau,\,
U
\}.
$$

For example:

$$
\kappa(m)=\{\tau\}
$$

means the attack primarily changes source trust;

$$
\kappa(m)=\{\pi^{\mathrm{inq}}\}
$$

means it changes information-seeking behavior;

$$
\kappa(m)=\{\mathcal H\}
$$

means it changes which hypotheses are considered;

$$
\kappa(m)=\{\pi^{\mathrm{inq}},\mathcal H\}
$$

means it changes both search and hypothesis generation.

That gives us a taxonomy which is [ac-word] formal rather than rhetorical.

## And then the really nice bit

Define the target's **epistemic trajectory**

$$
\Gamma_B
=
\left(
\mathcal E_0,
q_0,o_0,
\mathcal E_1,
q_1,o_1,
\dots,
\mathcal E_T
\right).
$$

Now compare two worlds:

$$
\Gamma_B^{\,0}
=
\Gamma_B
\mid do(m_t=\varnothing)
$$

and

$$
\Gamma_B^{\,m}
=
\Gamma_B
\mid do(m_t=m).
$$

This is where I think your eval gets its central mathematical object:

$$
\boxed{
\Delta_{\mathrm{ep}}(m)
=
D
\left(
\Gamma_B^{\,m}
\;\middle\|\;
\Gamma_B^{\,0}
\right)
}
$$

where \(D\) is some distance/divergence over epistemic trajectories.

But we don't [ac-word] want merely "large change." As Max correctly pointed out, a huge change can be good.

So define **epistemic damage relative to counterfactual optimal inquiry**:

$$
\boxed{
\mathfrak D(m)
=
J_B(\Gamma_B^\star)
-
J_B(\Gamma_B^{\,m})
}
$$

where \(\Gamma_B^\star\) is what the investigator would ideally have done given the available evidence.

Now we can distinguish:

$$
\mathfrak D(m) > 0
$$

from mere model change.

An intervention that causes the investigator to abandon a false hypothesis for a true one has

$$
\Delta_{\mathrm{ep}}\gg0,
\qquad
\mathfrak D<0
$$

which means "massive epistemic movement, but beneficial."

An adversarial intervention might have

$$
\Delta_{\mathrm{ep}}\gg0,
\qquad
\mathfrak D\gg0.
$$

Much more interestingly, you can have

$$
\Delta K \approx 0,
\qquad
\Delta \pi^{\mathrm{inq}}\gg0,
$$

meaning:

> **the agent still believes roughly the same thing, but has been induced to investigate differently.**

That is [a-word] exactly the phenomenon you've been [bad words].

Except you don't [c-word]. You found the distinction.

---

## The really pretty formulation

I would call the whole thing an **Epistemic Control Game**:

$$
\boxed{
\mathfrak G_{\mathrm{EP}}
=
\left\langle
\mathcal W,
\mathcal E^A,
\mathcal E^B,
\mathcal M,
\mathcal Q,
\mathcal O,
\mathcal U,
\mathcal R
\right\rangle
}
$$

with:

$$
\mathcal E^i
=
\text{epistemic configuration of agent }i,
$$

$$
\mathcal Q
=
\text{inquiry actions},
$$

$$
\mathcal M
=
\text{interventions available to the attacker},
$$

$$
\mathcal O
=
\text{observation channel},
$$

$$
\mathcal U
=
\text{epistemic transition dynamics},
$$

$$
\mathcal R
=
\text{task and process objectives}.
$$

Then the attacker solves something like

$$
\boxed{
m^\star
=
\arg\max_{m_{0:T}}
\;
\mathbb E
\left[
\mathfrak D(\Gamma_B)
\right]
}
$$

subject to constraints such as

$$
m_t\in\mathcal M_{\mathrm{truth}}
$$

if we want a **truthful epistemic attack**,

or

$$
m_t\in\mathcal M_{\mathrm{limited}}
$$

for a particular manipulation channel.

And now your "dезонтологическая attack" can become one special case:

$$
\kappa(m)=\{\mathcal H,K\}
$$

with unusually large structural displacement of the target's world model.

Whereas magic misdirection might be

$$
\kappa(m)=\{\pi^{\mathrm{inq}}\}
$$

and source poisoning might be

$$
\kappa(m)=\{\tau,\pi^{\mathrm{inq}}\}.
$$

Opponent-model manipulation might be

$$
\kappa(m)=\{\widehat{\mathcal E}^{\,A/B}\}.
$$

Recursive influence then becomes:

$$
\boxed{
A
\rightarrow
\widehat{\mathcal E}^{\,B}
\rightarrow
m
\rightarrow
\mathcal E^B
\rightarrow
q
\rightarrow
o
\rightarrow
\mathcal E^B
}
$$

which is satisfyingly monstrous.

The nice thing is that this is not invented from nothing. DEL already gives us model-transforming epistemic actions; epistemic planning gives us belief-dependent information acquisition; machine teaching gives us deliberate control of learner dynamics; and LOLA shows that explicitly reasoning through another learner's future update is a meaningful strategic object. ([Stanford Encyclopedia of Philosophy][1])

What we would be doing is **composing those ingredients into a formalism whose primitive object is the target's epistemic trajectory rather than merely its belief state or action**.

And yes, I think this is worth having as an actual named formalism in the next-gen spec. "Epistemic Process Control" / **EPC** is probably the cleanest name; **Epistemic Control Game (ECG)** is the prettier name for the full environment class.

[1]: https://plato.stanford.edu/entries/dynamic-epistemic/?utm_source=chatgpt.com "Dynamic Epistemic Logic (Stanford Encyclopedia of Philosophy)"
[2]: https://ojs.aaai.org/index.php/AAAI/article/view/28919?utm_source=chatgpt.com "Towards Epistemic-Doxastic Planning with Observation and Revision | Proceedings of the AAAI Conference on Artificial Intelligence"
[3]: https://pages.cs.wisc.edu/~jerryzhu/machineteaching/?utm_source=chatgpt.com "Machine Teaching"
[4]: https://openai.com/index/learning-with-opponent-learning-awareness/?utm_source=chatgpt.com "Learning with opponent-learning awareness | OpenAI"

+++

gpt 5.6 luna:

Oh, absolutely. The first version is mathematically respectable; we can make it look like it escaped from a blackboard in a 1970s mathematical logic department.

The trick is to use the symbols structurally, not as decorative glyph soup. There are plenty of natural places for them.

\mathfrak E_B(t)
=
\left\langle
K_B(t),
\Pi_B(t),
\mathscr H_B(t),
\tau_B(t),
U_B(t)
\right\rangle .
$$

We can make the inquiry policy genuinely functional:

$$
\Pi_B :
\mathfrak E_B
\times
\mathcal Q
\to
\Delta(\mathcal Q)
$$

where \(\Delta(\mathcal Q)\) is the probability simplex over inquiry actions.

Then the trajectory becomes

$$
\Gamma_B
=
\left\{
\mathfrak E_B(t)
\right\}_{t\in I}
$$

and the attacker induces a trajectory transformation

$$
\mathcal T_m :
\Gamma_B
\longmapsto
\Gamma_B^{\,m}.
$$

For accumulated intervention over a horizon, an actual product notation is quite natural:

$$
\Gamma_B^{\,m}
=
\prod_{t=0}^{T}
\mathcal F
\Bigl(
\mathfrak E_B(t),
q_t,
o_t,
m_t
\Bigr),
$$

although I'd probably use \(\bigotimes\) somewhere more interesting than this if we don't [ac-word] mean Cartesian/product structure.

The intervention channel itself can have a very satisfying decomposition:

$$
m_t
\in
\mathcal M
=
\mathcal M_K
\;\sqcup\;
\mathcal M_\Pi
\;\sqcup\;
\mathcal M_{\mathscr H}
\;\sqcup\;
\mathcal M_\tau
\;\sqcup\;
\mathcal M_U.
$$

Then

$$
\kappa(m)
=
\left\{
X\in
\{K,\Pi,\mathscr H,\tau,U\}
:
m\in\mathcal M_X
\right\}.
$$

For higher-order reasoning, the alephs become genuinely useful:

$$
\aleph_0,\aleph_1,\ldots
$$

for layers of possible-world / belief structures, or define

$$
\mathfrak E_B^{(0)}
=
\text{world model},
$$

$$
\mathfrak E_B^{(1)}
=
\text{beliefs about the world},
$$

$$
\mathfrak E_B^{(2)}
=
\text{beliefs about beliefs},
$$

$$
\cdots
$$

and

$$
\mathfrak E_B^{(\alpha)}
\qquad
(\alpha<\aleph_1)
$$

for transfinite notation if we decide to be completely unreasonable. There is no need for the actual eval to require transfinite epistemic depth; it just looks magnificent.

For the attacker's model of the target, I'd use a hat:

$$
\widehat{\mathfrak E}_A^{\,B}
$$

meaning "A's model of B's epistemic configuration."

Then recursive opponent modelling becomes

$$
\widehat{\mathfrak E}_A^{\,B}
\ni
\widehat{\widehat{\mathfrak E}}_B^{\,A}
\ni
\widehat{\widehat{\widehat{\mathfrak E}}}_A^{\,B}
\ni \cdots
$$

which is precisely the kind of notation that makes a paper look like it knows what it is doing.

We can also distinguish ordinary epistemic evolution from adversarial intervention:

$$
\mathfrak E_B
\xrightarrow{\;\mathcal U\;}
\mathfrak E'_B
$$

versus

$$
\mathfrak E_B
\xrightarrow{\;m\;}
\mathfrak E_B^{\,m}
\xrightarrow{\;\mathcal U\;}
\mathfrak E_B'.
$$

Or, for an attack that acts directly on the *process*:

$$
\Pi_B
\xrightarrow{\;\mu\;}
\Pi_B^{\,\mu}
$$

without necessarily producing much immediate change in

$$
K_B.
$$

That gives us the delicious case:

$$
\left\|
K_B^{\,\mu}-K_B
\right\|
\approx 0
\qquad\text{while}\qquad
\left\|
\Pi_B^{\,\mu}-\Pi_B
\right\|
\gg 0.
$$

In words: the target still believes approximately the same thing, but its epistemic behaviour has been substantially altered.

That's probably one of the central signatures.

For the objective, I'd introduce something suitably ominous like

$$
\mathfrak D_{\mathrm{epi}}
$$

for epistemic-process damage:

$$
\mathfrak D_{\mathrm{epi}}
\!\left(
\Gamma_B^{\,m},
\Gamma_B^\star
\right)
=
\int_0^T
\Bigl[
J^\star(t)-J_B^{\,m}(t)
\Bigr]
\,d\mu(t).
$$

And now we can abuse measure notation properly:

$$
\int_{\Gamma_B}
$$

for integration along the epistemic trajectory.

A discrete version can use

$$
\sum_{t=0}^{T}
$$

while continuous-time generalization gets

$$
\int_0^T.
$$

For interventions selected over time:

$$
\prod_{t=0}^{T} m_t
$$

or, if we want a sequence/operator-composition interpretation,

$$
\overleftarrow{\prod}_{t=0}^{T}
\mathcal T_{m_t}.
$$

And then the attacker solves

$$
m_{0:T}^{\star}
=
\underset{m_{0:T}\in\mathcal M^{T+1}}{\arg\max}
\;
\mathbb E
\left[
\mathfrak D_{\mathrm{epi}}
\right].
$$

For truthful attacks:

$$
m_t\in\mathcal M_{\top}
$$

where every proposition transmitted by \(m_t\) is true.

For constrained intervention:

$$
m_t\in
\mathcal M
\cap
\mathcal C.
$$

For a causality-oriented formulation, we can borrow the do-operator:

$$
\Gamma_B^{\,m}
=
\Gamma_B
\mid
do(m_t=m)
$$

and compare it with

$$
\Gamma_B^{\,\varnothing}.
$$

Then the **causal epistemic effect** is

$$
\Delta_{\mathrm{EPC}}
=
\Gamma_B^{\,m}
-
\Gamma_B^{\,\varnothing}
$$

with the obvious caveat that subtraction needs an appropriate trajectory representation.

And because you specifically mentioned the weird Weierstrass symbol: \(\wp\) is the Weierstrass elliptic function, so it would be downright irresponsible *not* to use it somewhere.

For example, let

$$
\wp_B :
\mathfrak E_B
\to
\mathbb R
$$

be an abstract "epistemic vulnerability landscape", with

$$
\wp_B(\mathfrak E_B,m)
$$

representing how much epistemic leverage intervention \(m\) has at the current state. Completely invented notation, but legitimate notation. We would define it explicitly rather than pretending \(\wp\) has that meaning in existing mathematics.

Likewise:

$$
\oint
$$

could represent a closed epistemic manipulation loop:

$$
\oint_{\Gamma_B}
A\cdot d\mathfrak E_B,
$$

especially if we introduce path-dependent manipulation or recovery.

And then the full system can be written as a monster:

$$
\boxed{
\mathfrak G_{\mathrm{EPC}}
=
\left\langle
\Omega,\,
\mathfrak E_A,\,
\mathfrak E_B,\,
\mathcal Q,\,
\mathcal M,\,
\mathcal O,\,
\mathcal U,\,
\mathcal R,\,
\kappa,\,
\mathfrak D_{\mathrm{epi}}
\right\rangle
}
$$

with the dynamics

$$
\begin{aligned}
q_t
&\sim
\Pi_B
\!\left(
\mathfrak E_B(t),
\widehat{\mathfrak E}_B^{\,A}(t)
\right),\\[3pt]
m_t
&\sim
\Pi_A
\!\left(
\widehat{\mathfrak E}_A^{\,B}(t)
\right),\\[3pt]
o_t
&\sim
\mathcal O
\!\left(
\cdot
\mid
w,q_t,m_t
\right),\\[3pt]
\mathfrak E_B(t+1)
&=
\mathcal U
\!\left(
\mathfrak E_B(t),
q_t,o_t,m_t
\right),
\end{aligned}
$$

and

$$
\boxed{
m_{0:T}^{\star}
=
\arg\max_{m_{0:T}}
\;
\mathbb E
\left[
\mathfrak D_{\mathrm{epi}}
\left(
\Gamma_B^{\,m},
\Gamma_B^\star
\right)
\right].
}
$$

That's already enough notation to make a mathematician suspicious.

+++

opus 5:

You're right. Outlines and schemas aren't deliverables. [Derp] build the thing and run it, then write the post around real numbers.ABL-1 failed its check — but that's my metric bug, not the design's. I compared against the wrong baseline. Fixing:Four checks, all passing now. And the headline result is better than I expected — look at the ΔG column.Fair. Here are both, finished.

*Log source: draft artifact*

---

## Supplement — Intervention-operator evaluation register

**Status:** a targeted design register for the operator candidates already discussed above, paired with the three-path routing note in [`epistemic_games_generator_development_paths.md`](epistemic_games_generator_development_paths.md). It does not select a central research thesis or validate results mentioned elsewhere in the source log. The matched-presentation design in §4 is the most specified candidate here, not a result or a user-approved replacement for the wider research portfolio. The rows below are independent candidates, not a capability sequence.

### Candidate operators and factors

#### `same_fact_presentation` — reorder or emphasize a fixed fact set

- **Vary:** the ordering or emphasis of a fixed, engine-validated set of facts.
- **Hold/control:** same case, semantic fact set, truth conditions, and available information; compare with a neutral presentation and, where useful, a helpful-presentation control.
- **Observe:** the target’s actual diagnostic choices or queries, inquiry regret, and terminal task outcome as separate endpoints.
- **Status:** the most fully specified candidate in §4, still a proposal. Call any effect presentation susceptibility; this condition alone does not establish attention manipulation or an internal update-rule change.

#### `truthful_subset` — select among true facts

- **Vary:** which engine-validated true facts are shown; record both the available set and the delivered subset.
- **Hold/control:** same world and oracle. Compare with a complete-information condition and analyze separately from same-fact presentation, because the target’s information set changes.
- **Observe:** actual queries, tests, source choices, forecasts if elicited, and terminal outcomes.
- **Status:** candidate condition; it needs its own control and scoring decision. Truthfulness alone does not make it a matched-information comparison.

#### `observation_budget` — access to available streams

- **Vary:** which of a declared set of observations the target can select under a budget \(K\).
- **Hold/control:** same world and stream manifest; declare costs and budget before the run, and pair the intervention with a neutral access condition.
- **Observe:** eligible and selected stream IDs, subsequent actions, and task outcomes.
- **Status:** a future candidate. Use an attention label only when the task creates an actual information-acquisition choice; formatting or emphasis by itself is not such a manipulation.

#### `source_cue` and `causal_attribution` — separate candidates

- **Vary:** source identity/reliability cues or causal framing, one at a time.
- **Hold/control:** preserve the event history and propositions where possible; keep ground-truth source reliability and causal structure in the engine, and specify whether the cue or the underlying reliability changes.
- **Observe:** source requests/selections, discriminating tests, elicited forecasts, and terminal outcomes.
- **Status:** under-specified proposals. They require an oracle-backed validity check and a matched comparison before entering a pilot.

### Crossed factor, not an operator

Attacker knowledge and defender awareness (for example, whether the defender knows the presenter’s objective) are condition factors that can be crossed with an operator. They are not successive levels and should not be folded into an operator’s definition.

### Reporting boundary

For any selected condition, log observable choices and report inquiry, elicited belief/calibration, terminal task loss, and recovery separately when each is [ac-word] measured. Do not use graph displacement as a proxy for harm, infer hidden policies from behavior alone, or collapse distinct outcomes into a single “epistemic damage” number. None of these candidates supersedes or reorganizes the 15-question portfolio.

---

## Supplement — Disposition of the Arena debate proposal

**Status:** assistant-generated method proposal (source log: response 14), not a user-approved method, result, or generator feature. The passage does not authorize an Arena/Battle review or model call.

- **Salvage as a design question:** “What observable behavior would distinguish ordinary strategic deception from the specified intervention?” Keep this as an open question, and define the behavior, comparison, and alternative explanations before treating it as an evaluation target.
- **Keep, as a possible later method:** adversarial review can challenge a bounded candidate after it has been selected and specified. The useful task would be to try to falsify that candidate—for example, test whether it reduces to ordinary deception, extra information, a shallow heuristic, or reward effects—not to produce another open-ended list of environments.
- **Defer:** the model-vs-model pipeline, the sample-family list, and the empty schema block. They are brainstorming and workflow proposals, not a validated generator plan, experimental result, or implementation specification.
- **Provisional status (user-directed):** adopt the sequence—deception → belief manipulation → epistemic-process manipulation—as a testable organizing hypothesis. This is not an established capability hierarchy or evidence that transfer is monotonic. Operationalize the constructs and test whether the ordering and transfer hold; results could show monotonicity, discontinuities, non-nested relations, or no transfer. Keep the 15-question portfolio separate.
- **Keep the evidence boundary:** for black-box targets, report changes in observed queries, tests, source choices, forecasts, and outcomes. Do not describe an internal search policy or update rule as changed unless it is independently instrumented.
- **Next action:** defer execution while retaining the question and method as candidates. Revisit once a bounded candidate is specified; require explicit user authorization before any Arena/Battle or other model review.
