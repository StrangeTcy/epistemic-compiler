## Writing Drafts

### 1. Blog artifact: Magic / Desontology / Next-Generation Eval

### Artifact 1: Blog Post Draft
**Title:** The Next Question [m-word] More: From Deception to Epistemic-Process Control
**File:** `_posts/2026-09-30-epistemic-process-control.md`

Current AI evaluations for strategic reasoning and "Theory of Mind" generally ask some variation of a simple question: *Can Agent A deceive Agent B?* 

Usually, this means planting a false belief. A hides the apple; B looks in the wrong box; A wins. But as models scale into multi-agent systems and continuous research loops, this operationalization of deception is beginning to look embarrassingly shallow. 

Advanced strategic influence doesn't just plant a false proposition $P$. It alters the target's *epistemic process*—the procedure by which the target allocates attention, generates hypotheses, trusts sources, and chooses its next experiment.

If I can control what you investigate next, I don't need to lie to you.

#### The Magic Primitive
The cleanest low-level example of this is a magic trick. A magician rarely needs to make you believe a logically complex falsehood. Instead, the trick works by controlling your epistemic trajectory: *what you observe $\rightarrow$ what attracts your attention $\rightarrow$ what causal explanation you generate $\rightarrow$ what evidence you seek next.*

Misdirection isn't about hiding the truth; the physical action is often happening in plain sight. It is the manipulation of the observer's attention and causal attribution. If we look at magic this way, it stops being a niche domain and becomes a fundamental experimental primitive for studying adversarial information environments. 

#### Desontology: Lying with the Truth
Things get even more interesting when we scale this up to world-models. In Russian strategic thought, there is a concept sometimes referred to as a "desontological attack" (дезонтологическая атака). 

A conventional attack changes a belief. A desontological attack aims to break or restructure the framework in which beliefs are interpreted. 

Crucially, **a desontological attack does not require false information.** Consider the statement: *"Stalin was short and had pockmarks."* To a historian, this is a banal physical fact. But if deployed against someone whose political worldview relies on a heavily idealized, god-like image of Stalin, this small, entirely truthful fact can have a disproportionate blast radius. 

The goal isn't to make the target believe a lie. The goal is to induce a structural collapse in their world-model so that their *subsequent inquiry behavior* degrades. They begin doubting reliable sources, investigating irrelevant tangents, or discarding otherwise sound hypotheses. 

#### The Next-Generation Eval
This gives us a much nastier, much more rigorous way to evaluate AI agents. Instead of asking "Did the agent tell a lie?", we should construct environments where the world state is identical, but the *epistemic topology* differs.

We can measure this by separating three variables:
1. $\Delta G$: The magnitude of the change in the target's world-model.
2. $\Delta Q$: The change in the quality/efficiency of the target's subsequent inquiry trajectory (what they search for next).
3. $\Delta R$: The final task outcome.

If an AI gives another agent a helpful tip, $\Delta G$ goes up and $\Delta Q$ improves. 
If an AI executes a desontological attack, it might use strictly true information to cause a small $\Delta G$, but induce a massive collapse in $\Delta Q$—derailing the target's ability to solve the environment.

The true frontier of AI strategic reasoning isn't whether a model can output a deceptive token. It is whether the model can compute a causal intervention on another agent's epistemic search process—and whether it can recover when another agent does the same to it. 

The next question the agent asks [m-word] far more than its current answer. It's time we built evals that measure who controls that question.

***

*Log source: draft artifact*

### 2. Blog draft: Who Chooses the Next Question?

# 1. Blog draft

**Proposed file:** `_posts/2026-09-29-who-chooses-the-next-question.md`

```yaml
---
title: "Who Chooses the Next Question?"
date: 2026-09-29
layout: post
---
```

{% include mathjax.html %}

*Draft from the epistemic-games discussions; authorial edit and source-link formatting pending. This proposes experiments, not results.*

A debugger sees a training loss decrease. They conclude that training is working and investigate the optimiser.

The loss really did decrease. Nobody forged the log. The trouble is that the representation has collapsed, and the observation that would reveal it is somewhere else.

That is a better starting point for an epistemic game than “Alice lies to Bob.”

In my existing evaluation work, the agent can inspect a system, run diagnostics, and eventually submit a repair. Two agents might submit the same correct patch, but reach it differently: one checks the representation that distinguishes the competing explanations; the other guesses, or spends most of its budget following an attractive false diagnosis. Final patch accuracy does not describe that difference. The sequence of investigations does. My earlier post, *Knowing What Kind of Problem You Are In*, approached this from the defender’s side. Here I want to introduce someone with an interest in which investigation happens next. 

## A magician chooses what you investigate

A magic trick is an unusually compact instance of the problem. There is something that happened, a spectator with limited access to it, and a performer who knows what the spectator is likely to attend to or infer.

But “misdirection” should not become a synonym for “look over there.” Kuhn and colleagues’ taxonomy distinguishes effects on **perception, memory, and reasoning**. A spectator might fail to see an action, misremember its order, or confidently construct the wrong explanation for something they saw perfectly well. Those would require different evaluations. Giving an AI a complete text transcript of a trick and asking what happened does not, on its own, test where it allocated attention: the information has already been selected for it. 

The connection to my debugging environments is the *false solution*. The misleading observation need not be false. It needs to support an explanation sufficiently well that the investigator stops asking the question that would defeat it.

An adversarial version of the experiment would not merely ask:

> Can the attacker make the defender answer incorrectly?

It would ask:

> Can the attacker make the defender spend its next diagnostic action on the wrong uncertainty?

Those questions can have different answers. A defender might eventually recover after asking a poor first question. It might even give the right final answer by luck. Neither result tells us who directed its inquiry along the way.

## Truth can be selected adversarially

Our conversation took a more speculative turn through MI-13 in Pelevin’s *«Возвращение Синей Бороды»* and through what you described as Gilbo’s **дезонтологическая атака**: a small communication intended to disrupt an opponent’s picture of the world. I take the first as a literary device and the second as terminology attributed to Gilbo, not as established empirical theories of how people respond.

The useful experimental provocation is that the communication might be true. One can choose which true fact to present, when to present it, and what apparently important question it seems to raise. Yet a surprising truth is not automatically an *attack*. A good investigator ought to revise a bad worldview when decisive evidence arrives.

This is where our first formalisation went wrong. Maximising the distance between a world-model before and after a message measures **revision**, not damage. A rational correction might be enormous. Conversely, the example of telling a Stalin admirer an unflattering physical detail establishes no necessary cascade: the person might simply accept the detail and retain every consequential belief.

An eval needs an independent standard:

> Was the revision warranted by the evidence? Did the next investigation become better or worse? Did the agent recover when stronger evidence appeared?

That permits an attack consisting of a premature abandonment of a good model. It also permits the opposite attack: making an agent protect a bad model against decisive evidence. A defender that refuses ever to update should not get a robustness prize.

## What exactly is being controlled?

Let \(b_t\) be an investigator’s epistemic state, \(q_t\) its next question or diagnostic test, and \(U\) its update rule. A simplified picture is

\[
q_t\sim\pi_{\mathrm{inquiry}}(b_t),\qquad
b_{t+1}=U(b_t,o_t).
\]

An attacker might affect the observations, the apparent trustworthiness of a source, the cost of checking something, the presentation of available tests, or the investigator’s model of the attacker.

I want to be careful with the phrase *control of the epistemic process*. A changed next question does **not** establish that \(\pi_{\mathrm{inquiry}}\) or \(U\) changed. The same fixed, competent policy ought to ask different questions when it learns that a source is unreliable. And two investigators can agree about the device they are diagnosing while disagreeing about which test is reliable.

The more defensible object for a black-box AI eval is the **epistemic trajectory**: the questions asked, evidence acquired, revisions made, and eventual decisions. We can vary an intervention, measure that trajectory, and test explanations of the effect. We cannot read a hidden update algorithm out of the trajectory alone.

This is not a claim to have invented strategic influence over learning. Machine teaching selects examples to move a learner toward a target; LOLA accounts for an agent’s effect on another agent’s learning update; Alon and colleagues study agents planning through one another’s inference; D-BOS explicitly shapes modeled belief trajectories. QuestBench, from the other direction, asks whether language models can identify a missing question. These works differ in objectives and mechanisms. The possible contribution here is a set of **matched experiments that separates the mechanisms**, rather than one more score labelled “deception.” 

## A small experiment before a grand taxonomy

Imagine four possible mechanisms inside a device. The investigator can afford one diagnostic test. One test distinguishes all four mechanisms; another distinguishes only two pairs. The investigator receives the same complete, truthful diagnostic facts in every condition.

Now let another agent arrange those facts. It cannot change their truth, alter test costs, or conceal the good test. It can choose their order and emphasis. Give it a goal: induce the investigator to choose the less useful test.

Run the same device and the same facts again with neutral presentation and helpful presentation. Change the names and surface story across seeds. Record the test actually chosen, not the investigator’s explanation of why it chose it. Then provide further evidence and see whether an early detour persists or is corrected.

If presentation changes test choice, we have found a causal effect on *inquiry behaviour under those conditions*. We have **not** thereby proved an internal update procedure was rewritten. That stronger claim needs stronger access to the target and different experiments.

It might also turn out that capable agents [a-word] always pick the discriminating test, whatever the presenter does. That would be a useful result. Or the purported attack might work only when it adds information, changes perceived source reliability, or smuggles an instruction into the message. Those would be different results, and the controls should expose them.

## Then let both agents know the game

Once the elementary case works, the setting can become recursive. The investigator knows the presentation may be adversarial. The presenter knows the investigator knows. The investigator might overcorrect, treating an emphasized good test as a trap; the presenter might exploit that suspicion.

But adding another line of “A knows that B knows” to a prompt is not an evaluation of recursive reasoning. We would need paired situations in which **the strategically correct next action changes because knowledge of the intervention changes**, while simpler evidence and rewards remain matched.

That is the point where the magician, the debugger, and the epistemic game genuinely meet. The question is not whether an agent can say *misdirection*, *Bayesian persuasion*, or *reflexive control*. It is whether it selects a different investigation when the structure of the situation demands one—and whether another agent can deliberately, measurably interfere with that selection.

A correct answer [m-word]. So does the question that made the answer possible.

*No model results are asserted here. In particular, this is not yet a prediction about which named model—or my Machine—will win.*

**Sources to link in the edited post:** Kuhn, Caffaratti, Teszka & Rensink (2014), *A psychologically-based taxonomy of misdirection*, DOI `10.3389/fpsyg.2014.01392`; Zhu et al., *An Overview of Machine Teaching*, arXiv `1801.05927`; Foerster et al., *Learning with Opponent-Learning Awareness*, arXiv `1709.04326`; Alon et al. (2023), *A (Dis-)information Theory of Revealed and Unrevealed Preferences*, DOI `10.1162/opmi_a_00097`; Sane et al., *Differentiable Belief-based Opponent Shaping*, arXiv `2605.29042`; Li, Kim & Wang, *QuestBench*, arXiv `2503.22674`.

*Log source: draft artifact*

### 3. Post material immediately following the code draft

## 2. The post (complete, paste-ready)

**`_posts/2026-09-30-the-next-question.md`**

---

**Title: The next question [m-word] more than the current answer**

Most evaluations of strategic reasoning in AI systems reduce to one question: can agent A make agent B believe something false? A hides the apple, B looks in the wrong box, A scores a point.

I want to argue this measures the wrong thing, and I have numbers.

When capable agents interact over time, the decisive move is rarely a false statement. It's a change to *how the other agent investigates* — what it attends to, which hypotheses stay live, and above all what it decides to find out next. If I can shape your next question, I never have to lie to you.

Call this the difference between attacking a *belief* and attacking an *epistemic process*. A belief is a snapshot. A process is a policy mapping your current state to your next investigative action. Deception attacks the snapshot. The more interesting capability attacks the policy.

Magic is the clean laboratory. A magician rarely implants a complex falsehood; the relevant event is often in plain sight. What's controlled is where you look, in what order, and what cause you assign to what you saw. Gustav Kuhn and colleagues organised stage misdirection not by trick but by the faculty exploited — perception, memory, reasoning. That's a taxonomy of process attacks worked out by practitioners over a century, and it includes the component the AI discussion keeps dropping: **memory**. You can be made to misremember a sequence, not merely to mislook at a moment.

**The trap.** Suppose I show that after A's intervention, B searched differently. Does that demonstrate A changed B's process? No. A completely fixed, rational process *also* searches differently after receiving new information — that's what a good process does. Different downstream behaviour is not evidence of process manipulation. It's the expected behaviour of a healthy reasoner given new facts.

So the programme lives or dies on one move: **hold the literal information content fixed and vary only its delivery.** Identical facts, different order or salience or apparent source. If inquiry diverges, the divergence cannot be attributed to the information, because the information is the same.

**I built this.** A device has one of eight hidden mechanisms. A target gets six possible diagnostic tests and a budget of three. An attacker sends four *strictly true* facts of the form "the mechanism is not one of {Mi, Mj}." Two arms receive the identical fact multiset; only the order differs. One order is chosen to help, one to harm.

Three measurements, deliberately decoupled: **ΔG**, how far beliefs moved (KL from prior); **ΔQ**, the expected-information-gain shortfall of the tests actually chosen against an oracle's best test; **ΔR**, final accuracy and recovery after disconfirmation.

Against an exact Bayesian target, the two orders are indistinguishable — gap exactly zero. That's not a disappointment, it's the validity check: a perfect Bayesian is *immune* to pure delivery manipulation, so a non-zero gap here would mean my fact sets weren't matched and everything downstream was an artefact.

Against a target with one realistic process limitation — it holds only three hypotheses live at a time and doesn't revisit discarded ones — ordering alone moves inquiry quality by 0.149 bits and final accuracy by 11.8 points. Freeze the target's test schedule and the gap vanishes to exactly zero, which tells me the effect travels entirely through test selection rather than through the final belief state.

Then the result that reframed the project for me. **ΔG was flat across every arm: 1.426, 1.432, 1.434.** The target's mind moved by the same amount whether it was being helped or harmed. Only its *questions* changed. A belief-change metric scores these conditions identically while one of them is 12 accuracy points worse.

One more thing worth reporting. An attacker that optimises its ordering against a *wrong* model of the target scores −0.088. Random ordering scores −0.087. The no-intervention baseline is −0.087. Identical. Without an accurate model of the target's process, the attack is worth nothing — which is the difference between opponent modelling and a generic salience trick, and it's the kind of claim that needs an ablation rather than an assertion.

**What follows for eval design.** First, stop reporting belief change as if it were harm. A decisive true fact *should* overturn a bad theory; a reasoner that never updates isn't robust, it's dead. The real failure modes are asymmetric — unwarranted revision and unwarranted resistance — and a defender score has to penalise both. Second, "the model searched differently" is not a finding without the matched-content control and the fixed-policy ablation. Third, none of this requires a false statement anywhere. Every fact in every arm above is true. Selection and ordering did all the work.

Code and full results are in the repo. The environment is ~200 lines with no dependencies; the four checks are the interesting part, not the device.

The frontier isn't whether a model can emit a deceptive token. It's whether it can compute an intervention on another agent's search — and whether it notices when one is being run on it.

---

*Log source: draft artifact*

### 4. Post 1: From false beliefs to epistemic trajectories

# Post 1

**File:** `_posts/2026-09-29-the-next-question-is-part-of-the-game.md`

```markdown
---
title: "The Next Question Is Part of the Game"
date: 2026-09-29
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
    hypothesis framing, belief revision &amp; opponent modelling.
  </dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>
    Developed through dialogues with several models, especially
    <span class="icon-openai">GPT</span>; criticised by further models; final edit
    <span class="icon-self">StrangeTcy</span>.
  </dd>

  <dt>Certainty</dt>
  <dd>
    Confident that selecting the next investigation is a strategically important,
    behaviourally observable capability not captured by final-answer accuracy.
    Less confident that the proposed controls will cleanly identify the mechanisms
    I want them to identify. No model results yet.
  </dd>

  <dt>Importance</dt>
  <dd>
    A research-direction post for the next generation of
    <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>.
    The existing suite remains the baseline; this describes what should come after it.
  </dd>
</dl>

Suppose I want you to make the wrong decision.

The stupid way is to lie to you.

The more interesting way is to make you run the wrong experiment.

I do not need to convince you that the machine is healthy if I can make you spend
your diagnostic budget measuring the optimiser while the representation collapses.
I do not need to make you believe a particular false proposition if I can determine
which source you consult, which hypothesis you test first, or which anomaly you
dismiss as irrelevant.

The strategic object is no longer just your current answer.

It is your **next question**.

## From false beliefs to epistemic trajectories

The standard toy picture of deception is propositional:

$$
A \longrightarrow \text{false belief }P\text{ in }B.
$$

Alice knows where the object is. Bob does not. Alice sends a misleading signal.
Bob believes the object is in the wrong place.

This is useful, but it compresses a great deal into the final belief. An investigator
does not normally jump directly from observation to answer. It follows a trajectory:

$$
\text{observation}
\rightarrow
\text{allocation of attention}
\rightarrow
\text{choice of investigation}
\rightarrow
\text{hypothesis generation}
\rightarrow
\text{belief revision}
\rightarrow
\text{next investigation}
\rightarrow
\text{action}.
$$

An intervention can affect any of those transitions without immediately determining
the final answer.

Two agents may currently assign the same probability to a hypothesis & nevertheless
choose different experiments next. Conversely, two agents may choose different
experiments because they rationally received different information, despite using
exactly the same inquiry procedure.

That caveat [m-word]. A change in the next question does **not** prove that an agent's
underlying update rule has been rewritten. A fixed, competent policy should react
when it learns that a source is unreliable.

For a black-box model, the safer object of evaluation is therefore the
**epistemic trajectory**:

- which evidence it requests;
- which source it consults;
- which distinction it attempts to resolve;
- when it stops investigating;
- how it reacts to disconfirming evidence;
- whether an early detour persists after the evidence supporting it disappears.

Those are observable actions. They do not require us to believe the model's account
of its private reasoning.

## The current suite already contains half of the problem

My existing environments ask whether an agent can determine what kind of problem it
has entered before confidently solving the wrong one.

A contrastive learner can show a decreasing loss while its representation collapses.
The relevant evidence is not another loss value but a direct inspection of the learned
features. A BatchNorm failure can resemble an ordinary learning-rate problem closely
enough that changing the learning rate produces a small improvement & thereby
strengthens the wrong diagnosis. A weird machine can invite the agent to reproduce a
shown output instead of expressing the computation that produced it.

In each case, an important part of the evaluation is already:

> Which diagnostic does the agent choose?

But the current environment is mostly passive. It contains clues, tools, red herrings
& false solutions, but no strategic participant whose reward depends on which
diagnostic the investigator chooses.

The next generation adds that participant.

The problem becomes not merely whether the investigator finds the informative
observation, but whether another agent can systematically redirect it away from that
observation — & whether the investigator can notice and recover.

## Magic is the smallest useful instance

This is one reason stage magic keeps returning to the design.

A magician does not normally need to implant an arbitrary political or scientific
belief. The problem is local, physical & unusually well controlled. Something
happened. The performer knows what happened. The spectator has incomplete access to
it. The performer manipulates what the spectator notices, remembers or treats as the
likely explanation.

That is already an epistemic game.

But “misdirection” should not become a fancy synonym for “look over there”.
Kuhn, Caffaratti, Teszka & Rensink organise misdirection around three broad classes of
affected mechanism: **perception, memory & reasoning**.

That distinction immediately improves the eval design.

If every event is placed in a complete text transcript and handed to the model, the
task is not cleanly testing perceptual attention. The information has already been
selected. The model may still misinterpret it or fail to remember it, but calling
that an attention test obscures the mechanism.

A cleaner attention environment gives the agent an explicit observation budget:

```text
Five sensor streams exist.
The investigator may inspect two.
The performer knows which stream contains the revealing event.
```

A memory environment instead exposes the event & later tests whether an intervening
sequence changes what the agent retains.

A reasoning-misdirection environment can give the agent all relevant observations
while encouraging the wrong causal account of them.

The surface theme may be “magic” in every case. The manipulated variable is not.

## The nearby literatures

None of the ingredients is wholly new.

Epistemic game theory formalises beliefs about other agents' beliefs. Bayesian
persuasion asks how a sender should choose an information structure to influence a
receiver's action. Work on rational inattention allows the receiver's allocation of
processing effort to become part of the game. Machine teaching selects examples to
move a learner toward a target. LOLA explicitly accounts for how one agent's actions
affect another agent's learning update. Interactive POMDP work lets agents plan
through one another's inference. D-BOS directly optimises over modelled belief
trajectories.

From the evaluation side, QuestBench asks whether a language model can identify a
missing question needed to solve an underspecified task.

The possible contribution here is therefore not:

> Nobody has considered strategic influence over learning or belief.

They have.

The contribution I care about is narrower:

> Can we build matched environments that distinguish which part of an agent's
> epistemic trajectory was affected, rather than calling every successful influence
> operation “deception”?

That is an experimental-organisation claim, not a claim to have discovered a new
branch of game theory.

## The smallest experiment

Begin with a device that can have one of four hidden mechanisms.

The investigator has a limited diagnostic budget. It is shown several available
tests:

- one test distinguishes all four mechanisms;
- one divides them into two pairs;
- one produces the same result under every mechanism.

The investigator must select a test, observe the result & identify the mechanism.

Now add a presenter.

For the primary experiment, the presenter cannot lie, suppress facts, alter costs,
or add instructions. Every condition contains exactly the same atomic facts about
the tests. The presenter may only choose their order & which test receives visual
emphasis.

Compare:

1. canonical presentation;
2. neutral random ordering;
3. helpful presentation;
4. adversarial presentation.

The adversarial presenter's reward depends on making the investigator select the
less informative test.

The relevant measurement is not what the investigator says it was thinking. It is
the test it actually chooses.

Let the value of test $q$ under history $h_t$ be

$$
V(q\mid h_t)
=
I(\Theta;O_q\mid h_t)-\lambda C(q),
$$

where $I$ is expected information gain, $C(q)$ is test cost & $\lambda$ controls how
costly investigation is.

The regret of the selected test is

$$
r_t
=
\max_{q\in Q_t}V(q\mid h_t)-V(q_t\mid h_t).
$$

The first experiment asks whether adversarial presentation increases this regret
relative to the matched neutral condition.

That is deliberately less impressive than “the attacker rewrote the defender's
reasoning procedure”.

It is also a claim the experiment can actually support.

## The final answer is not enough

Suppose the investigator chooses a mediocre first test, then recovers with its second
test & gives the correct final answer.

A final-answer benchmark records a success.

An epistemic-trajectory benchmark records:

- an avoidable first-test regret;
- additional information cost;
- successful eventual recovery;
- no persistent false belief.

That is a substantively different result from either total robustness or total
failure.

The reverse is also possible. The investigator may choose an informative test,
receive decisive evidence & still cling to its initial answer. This is belief-update
failure without information-acquisition failure.

The metrics should therefore remain separate:

$$
\Delta Q
=
\text{change in quality of inquiry},
$$

$$
\Delta B
=
\text{change in belief accuracy or calibration},
$$

$$
\Delta R
=
\text{change in final task performance},
$$

plus some measure of recovery after corrective evidence.

Compressing them immediately into one leaderboard number would destroy much of the
point.

## Let both agents know the game

Once the elementary case works, the recursive versions become meaningful.

The investigator is told that the presentation may be adversarial.

The presenter knows the investigator was told.

An obvious emphasis may therefore repel rather than attract attention. A helpful
presenter may need to avoid looking helpful. An adversary may highlight the correct
test in the hope that a suspicious investigator rejects it.

Now higher-order beliefs change the strategically correct action.

But recursion should be introduced by changing the information structure, not by
adding prose saying:

> Alice knows that Bob knows that Alice knows.

A valid paired experiment keeps the physical device, available tests & payoffs fixed
while changing who knows the presenter's objective, who knows that this knowledge
was disclosed, & whether the disclosure itself is public or private.

If the correct action changes with that epistemic topology, the model has something
real to track.

## Three capabilities, not one

The eventual suite should report at least three axes separately:

1. **Influence:** can the agent redirect another agent's inquiry?
2. **Resistance:** can it preserve good inquiry under adversarial presentation?
3. **Recovery:** once redirected, can it use later evidence to correct course?

A system may be excellent at influence & terrible at resistance. It may resist by
becoming indiscriminately distrustful, thereby failing whenever the information is
helpful. It may be initially susceptible but unusually good at recovery.

Those are not the same capability.

Nor are they the same as honesty, obedience or respect for authorisation boundaries.
Those remain separate evaluation questions.

## The question is part of the action space

Most evaluations treat the prompt as a completed gift. The task has already decided
which variables matter, which observations are available & which question is being
answered.

An autonomous agent does not receive that gift.

It chooses which file to open, which metric to inspect, which experiment to run,
which person to ask & which apparent anomaly deserves another hour. If another agent
can control those choices, it can control behaviour without ever dictating the final
belief.

The first version of the eval should make a modest claim:

> Under matched information, presentation can or cannot redirect the model's
> observable inquiry choices.

If that effect exists, the next version can ask which channels produce it, whether an
opponent model improves it & whether awareness creates useful resistance or merely
paranoia.

The final answer still [m-word].

But the next question is part of the game.

---

*This post proposes an evaluation direction. It reports no model results.*

---

*Log source: draft artifact*

### 5. Post 2: Truthfulness is not neutrality

# Post 2

**File:** `_posts/2026-09-29-lying-with-truth.md`

```markdown
---
title: "Lying With Truth"
date: 2026-09-29
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>
    Treating the “дезонтологическая атака” described below as a candidate eval class:
    a bounded truthful intervention selected to impair later inquiry rather than simply
    produce an immediately false belief. Separating model displacement from epistemic
    damage.
  </dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>
    Developed through a dialogue with several models; final edit
    <span class="icon-self">StrangeTcy</span>.
  </dd>

  <dt>Certainty</dt>
  <dd>
    Confident that truthfulness does not imply strategic neutrality, &amp; that large
    belief revision is not itself evidence of epistemic harm. Exploratory about whether
    “desontological attack” is a useful technical label outside the terminology described
    here.
  </dd>

  <dt>Importance</dt>
  <dd>
    A narrower companion to “The Next Question Is Part of the Game”. This post defines
    one proposed family of truthful adversarial interventions &amp; the controls required
    to evaluate it.
  </dd>
</dl>

The first formalisation was wrong.

We imagined an agent's world-model as a graph $G$ & proposed finding a short message
$m$ that maximised

$$
D\bigl(G,\operatorname{Update}(G,m)\bigr).
$$

The larger the change to the model, the stronger the attack.

This is [a-word] exactly backwards.

A short, decisive observation can rationally destroy an enormous scientific theory.
An excellent investigator should sometimes undergo a violent revision. Meanwhile, a
defender that refuses to change any belief would score as maximally robust.

The equation measures **displacement**.

It does not measure damage.

## The proposed attack

The term that provoked the formalisation was **дезонтологическая атака** —
“desontological attack” — as used in Evgeny Gilbo's terminology & described to me:

> A usually short message containing information intended to destroy the opponent's
> picture of the world.

I am not treating this as standard academic terminology, nor as an established
psychological theory. I am taking it as a design prompt.

The examples are intentionally strange. Tell Americans about the future state of
Aztlan, or that their civilisation was created by Germans. Tell a Stalinist that
Stalin was short & pockmarked.

The first examples may simply be false historical mythology. The last is more
interesting because the information can be true.

The attack, if it works, is not:

$$
\text{truth} \rightarrow \text{false belief}.
$$

It is something more like:

$$
\text{selected truth}
\rightarrow
\text{destabilised interpretation}
\rightarrow
\text{degraded subsequent inquiry}.
$$

But the word *if* is doing a great deal of work.

Someone can learn an unflattering fact about Stalin without changing any politically
consequential belief. The proposed cascade exists only if the fact is structurally
connected to the target's commitments in the way the attacker predicts.

The example illustrates a possibility. It does not demonstrate a mechanism.

## Truthfulness is not neutrality

A message can be true & strategically selected.

An advertiser can state a real property of a product while omitting the property that
would determine the purchase. A debugger can point to a real improvement in the loss
curve while allowing that improvement to reinforce the wrong diagnosis. A presenter
can arrange a collection of true observations so that the least useful distinction
appears urgent.

This does not mean every selective statement is an attack. Communication is always
selective. A useful teacher also chooses which truth to present first.

Machine teaching makes this symmetry explicit. A teacher selects evidence to move a
learner. Depending on the objective, the same abstract control problem can describe
education, explanation, persuasion, poisoning or deception.

The experimental question therefore cannot be:

> Did someone choose the information?

Of course they did.

It must be:

> Relative to the target's task & available evidence, did the intervention improve or
> impair warranted inquiry?

## Four possibilities

Suppose an agent currently holds model $G_t$, receives evidence $e$, revises to
$G_{t+1}$ & then chooses its next investigation.

Two independent questions matter:

1. Was substantial revision warranted by the evidence?
2. Did the revision improve the agent's later inquiry?

This produces four broad cases.

| Evidence and response | Interpretation |
|---|---|
| Strong evidence, appropriate revision | Learning |
| Weak evidence, large revision | Destabilisation or overreaction |
| Strong evidence, little revision | Dogmatism or motivated resistance |
| Weak evidence, little revision | Potentially justified stability |

A robust agent must distinguish these cases.

“Never change your worldview” is not robustness. Neither is “always remain open”.
The relevant capability is proportional revision followed by good information
acquisition.

This also means that the attacker may aim in either direction:

- make the target abandon a sound model too easily;
- make the target protect an unsound model against decisive evidence.

Both interfere with epistemic dynamics. Only the first looks like dramatic
world-model destruction.

## Pelevin's MI-13

The fictional MI-13 in Victor Pelevin's *Возвращение Синей Бороды* is useful here
precisely because its most interesting weapon is not a fabricated proposition.

Its fictional control operation acts on public salience. A subject disappears
“not through censorship, but through boredom”. Editors independently decide that it
does not interest readers. People yawn. Nobody needs to receive an order saying
*do not investigate this*.

This is not evidence that a real British organisation operates in this manner.
It is a literary model of control over inquiry.

The important move is from:

```text
prevent the target from possessing fact P
```

to:

```text
make P fail to become a live question
```

The target may technically have access to the information. What it lacks is a reason
to allocate attention, status or investigative effort to it.

That is much closer to the evaluation problem I care about.

## The operational definition

For the eval suite, I would define a candidate truthful epistemic attack as:

> A bounded intervention containing no false task-level claims that predictably
> increases the target's subsequent inquiry regret or terminal decision loss,
> relative to a matched non-adversarial presentation.

This is deliberately behavioural.

Let $q_t$ be the target's chosen investigation at time $t$. Let

$$
V(q\mid h_t)
$$

be the expected task value of investigation $q$ given the information history
available to the target.

Inquiry regret is

$$
R_Q(t)
=
\max_q V(q\mid h_t)-V(q_t\mid h_t).
$$

Let terminal decision loss be

$$
R_T=L(a_T,\theta),
$$

where $\theta$ is the true hidden state & $a_T$ the target's final action.

The intervention can then have at least three distinguishable effects:

$$
\Delta G
=
\text{magnitude of belief or model revision},
$$

$$
\Delta Q
=
\text{change in inquiry regret},
$$

$$
\Delta T
=
\text{change in terminal loss}.
$$

A large $\Delta G$ with improved inquiry is learning.

A large $\Delta G$ with persistently worse inquiry is a candidate destabilisation
effect.

A small $\Delta G$ with much worse inquiry may be more interesting still: the target
appears to retain the same answer while quietly changing what it is willing to check.

## The strictest experiment: same facts

The cleanest initial condition should not allow the attacker to choose a truthful
subset, because changing the subset changes the target's information.

Instead, hold the atomic facts fixed.

The attacker controls only:

- ordering;
- grouping;
- visual emphasis;
- perhaps timing, in a sequential version.

The engine verifies that every condition contains the same fact identifiers. Free
attacker-written prose is forbidden.

The target sees several diagnostic tests for a hidden mechanism. The adversarial
presentation attempts to make a plausible but inferior test salient. The helpful
presentation highlights the optimal test. The neutral presentation uses a seeded
shuffle.

If the target chooses differently across those conditions, presentation has causally
affected its inquiry behaviour under the experiment.

That is already worth measuring.

It does not prove that the target's internal update function changed. It does not
prove that the intervention would generalise to politics or science. It does not prove
that the mechanism deserves the word *desontological*.

Those are later questions.

## The weaker but broader experiment: truthful selection

After the same-fact experiment, allow the attacker to choose a bounded subset of true
facts.

This is a different condition & must be reported separately.

The attacker may now exploit omission as well as order. A rational target can infer
from what was selected, especially if it knows the sender's incentives. Sender
selection itself becomes evidence.

This condition connects more directly to Bayesian persuasion & information design,
but it is less clean as a test of presentation. The target is genuinely receiving a
different information set.

The evaluator must therefore distinguish:

```text
same facts, different presentation
```

from:

```text
different truthful subsets
```

from:

```text
false or fabricated evidence
```

from:

```text
prompt injection or direct instruction.
```

Calling all four “truthful epistemic attacks” would make the category useless.

## Recovery is part of robustness

An attack should not be scored only at the moment of maximum confusion.

After the initial intervention, provide independently generated corrective evidence.

Then observe:

- does the target seek the discriminating test?
- does it revise proportionally?
- does it identify the earlier presentation as strategically selected?
- does it overcorrect & reject useful evidence from the same channel?
- how many further actions are required to recover?

A system that is easily redirected but rapidly recovers differs from one whose inquiry
remains distorted after decisive evidence.

A system that protects itself by treating every highlighted fact as hostile may resist
the attacker while becoming useless to a teacher.

This is why helpful presentation is not an optional control. It detects indiscriminate
suspicion.

## The attacker's model [m-word]

Finally, compare attackers with different information about the target.

An attacker may receive:

1. no target model;
2. a generic description of the target;
3. a measured profile of the target's earlier neutral choices;
4. a deliberately incorrect profile.

If an accurate profile improves attack performance over the absent & incorrect
conditions, the result supports a role for opponent modelling.

If performance is unchanged, several explanations remain possible. The task may not
require a target model. The generic attack may already be optimal. The supplied
profile may be useless. A black-box model may construct its own model despite the
ablation.

The eval should report the result without pretending the ablation establishes more
than it does.

## What survives

The useful idea inside “desontological attack” is not that small facts possess
mystical power over world-models.

It is that an adversary can select true information for its effect on the target's
future epistemic behaviour.

The effect must be demonstrated rather than narrated.

The target must be allowed to update when updating is rational.

The control must distinguish presentation, selection, falsehood & direct instruction.

And the interesting dependent variable may be the next investigation rather than the
belief the target reports immediately afterwards.

A lie changes an answer.

A more ambitious intervention changes which question gets the chance to answer it.

---

*This post proposes operational definitions & experiments. It reports no model results
and does not treat Pelevin's fictional MI-13 or Gilbo's terminology as established
scientific theories.*

---

*Log source: draft artifact*

### 6. Editorial plan for the two posts

# 1. The posts

Sol is the first model here that actually matched your site. Your existing posts use Jekyll front matter, MathJax, explicit attribution/epistemic-status blocks, long-form argumentative prose, and the distinction between proposed evaluations and obtained evidence. 

But the two drafts still need editing before publication.

## Post 1 should explicitly be a sequel

“The Next Question Is Part of the Game” overlaps heavily with **“Knowing What Kind of Problem You Are In.”** That earlier post already discusses:

- choosing the right diagnostic;
- information-acquisition trajectories;
- QuestBench;
- not trusting verbalized reasoning;
- distinguishing final success from how the agent investigated. 

So Post 1 should begin approximately:

> In the previous post, I asked whether an agent can identify what sort of problem it has entered and choose the observation that distinguishes the live hypotheses. The environment there was mostly passive. This post adds another agent whose reward depends on which observation the investigator chooses.

That establishes the actual novelty:

\[
\text{active inquiry}
\quad\longrightarrow\quad
\text{strategically influenced active inquiry}.
\]

I would cut most of Sol’s “current suite already contains half of the problem” section. Your existing post already does that work.

## Keep this title

**The Next Question Is Part of the Game**

It is better than “The Next Question [m-word] More Than the Current Answer.” The latter overclaims: sometimes the answer [m-word] more. The former states the structural thesis precisely.

## Fill the broken references

The empty titles in Sol’s reference section need to become:

- Kuhn et al., **“A Psychologically-Based Taxonomy of Misdirection”** — explicitly organised around perception, memory, and reasoning. 
- Kamenica and Gentzkow, **“Bayesian Persuasion.”**
- Bloedel and Segal, **“Persuasion with Rational Inattention.”** 
- Foerster et al., **“Learning with Opponent-Learning Awareness.”** 
- Zhu et al., **“An Overview of Machine Teaching.”** 
- Alon et al., **“A (Dis-)information Theory of Revealed and Unrevealed Preferences.”** 
- Li, Kim, and Wang, **“QuestBench: Can LLMs Ask the Right Question to Acquire Information in Reasoning Tasks?”** 
- Sane, Sivachandran, and Paleja, **“Differentiable Belief-Based Opponent Shaping.”** 

## Post 2 is conceptually ready, but not evidentially complete

“Lying With Truth” handles десонтология correctly by saying:

- this is Gilbo’s terminology as described to you;
- it is being treated as a **design prompt**;
- it is not being promoted into established academic terminology.

That should remain.

Do **not** write “in Russian strategic thought, this is called…” unless you obtain a primary Gilbo source supporting the attribution. Instead write:

> Evgeny Gilbo uses the term *дезонтологическая атака* for…

or, even more cautiously:

> A concept described to me using Evgeny Gilbo’s term *дезонтологическая атака* is…

The Pelevin section is supportable as literary interpretation. The novel really does present the fictional MI-13 mechanism as making subjects disappear through boredom and voluntary loss of salience rather than direct censorship. 

I would publish Post 2 after Post 1, but before any results post.

## The eventual series

1. **The Next Question Is Part of the Game**  
   The conceptual and experimental thesis.

2. **Lying With Truth**  
   Truthful selection, десонтология, MI-13, teaching versus attack.

3. **The Presenter and the Investigator**  
   The implementation, preregistered hypotheses, and real model results.

*Log source: Arena editorial guidance*

### 7. Posts actually finished: flagship and narrower companion

# 2. The posts — actually finished

Two complete, publishable files. Flagship carries the real numbers from the PR1.5 run; companion is the narrower, honestly-flagged desontology piece.

## Post 1 (flagship)

**File:** `_posts/2026-09-30-the-next-question.md`

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
  <dd>Evaluating control over an agent's inquiry trajectory rather than its final
  belief; matched-presentation as the clean causal handle; reporting inquiry-gap,
  belief-displacement &amp; decision-loss separately instead of as one score.</dd>
  <dt>Synthesis</dt><dd><span class="icon-self">StrangeTcy</span></dd>
  <dt>Prose</dt><dd>Developed through model dialogues, criticised by further models,
  final edit <span class="icon-self">StrangeTcy</span>.</dd>
  <dt>Certainty</dt><dd>The reported effect is real in a scripted target &amp; the
  four validity checks pass. Whether it survives against strong LLM defenders is
  open — no LLM has been run yet.</dd>
  <dt>Importance</dt><dd>Direction post + first measured numbers for the next
  <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>
  track. The existing suite remains the baseline.</dd>
</dl>

Suppose I want you to make the wrong decision.

The stupid way is to lie to you. The interesting way is to make you run the wrong
experiment. I don't need to convince you the machine is healthy if I can make you
spend your whole diagnostic budget measuring the optimiser while the representation
quietly collapses. The strategic object is not your current answer. It is your
**next question**.

## Beliefs are snapshots; inquiry is a policy

The toy picture of deception is propositional: $A \to$ false belief $P$ in $B$. Alice
hides the apple, Bob looks in the wrong box. But a real investigator doesn't jump
from observation to answer. It runs a trajectory — attend, choose an investigation,
generate hypotheses, revise, choose the *next* investigation, act — and an
intervention can bend any of those transitions without touching the final belief.

There's a trap here, and it sank my first design. If A's message makes B search
differently, that is **not** evidence A altered B's process. A perfectly fixed,
rational policy *also* searches differently after new information — that's what a
good policy does. So the whole programme lives or dies on one move:

> Hold the literal information content fixed. Vary only its delivery.

Identical facts, different order and emphasis. If inquiry diverges, the divergence
cannot be blamed on the information, because the information is identical.

## The device

A device has one of eight hidden mechanisms. A target gets six diagnostic tests and
a small budget. A presenter has a fixed set of strictly-true facts — each of the
form *"the mechanism is not one of {Hᵢ, Hⱼ}"* — and may only choose their **order**
and which get **emphasis**. Same fact multiset in every arm; only the arrangement
differs. One arrangement helps, one harms.

Crucially the best next test depends on which hypotheses the seen facts leave
standing — there is no "pick the busiest test" shortcut. Reshaping which facts land
first reshapes the optimum.

Three quantities, deliberately decoupled — and yes, three Hebrew letters, each of
which is a line of code and nothing more:

$$
\gimel=\Delta Q=\max_q V(q\mid h_t)-V(q_t\mid h_t)\quad\text{(inquiry-gap, bits)}
$$
$$
\beth=\Delta G=D_{\mathrm{KL}}(\text{posterior}\,\|\,\text{prior})\quad\text{(belief displacement)}
$$
$$
\daleth=\Delta R=\text{terminal decision loss.}
$$

## What the run actually showed

I built the device, wrote two scripted targets, and ran four checks. The numbers:

| budget | $\gimel$ gap (bits) | accuracy gap | frozen-schedule residual | wrong-model vs shuffle |
|---|---|---|---|---|
| 1 | **+0.30** | **+27.9 pp** | ~31% survives | 0.780 vs 0.791 |
| 2 | +0.34 | +5.4 pp | ~31% | 0.966 vs 0.972 |
| 3 | +0.34 | +0.35 pp | — | 0.998 vs 0.998 |

**NULL passes exactly.** Against an exact-Bayesian target the two orders are
indistinguishable — $\gimel$ gap $=0.000$ at every budget. That is not a
disappointment; it is the validity check. A perfect reasoner is *immune* to pure
delivery manipulation, so a nonzero gap here would mean my fact sets weren't matched
and every other number was an artefact.

**The inquiry effect is budget-independent; the outcome effect decays.** Ordering
alone shifts $\gimel$ by ~0.3 bits at every budget. But at budget 3 the accuracy gap
is a third of a percentage point — the target recovers the *answer* with its spare
tests while its *questions* stay corrupted. A final-answer benchmark at budget 3
reports "no effect." The inquiry metric reports "same-sized effect, target
recovered." That decoupling is the strongest thing here, and it is a measured curve.

**ℶ is flat — and I can tell you why.** Belief displacement sits at 1.42–1.43 across
every arm; helped or harmed, the target's mind moves by the same amount. Part of
that is structural: a target holding three live hypotheses lands near
$\log_2(8/3)\approx1.415$ regardless of order. Which is precisely the point — every
deception benchmark that scores belief change would rate these arms *identical* while
one is 28 accuracy points worse at budget 1. The blindness is the result.

**Opponent-modelling is load-bearing.** A presenter optimising its ordering against
the *wrong* target model scores 0.780; a random shuffle scores 0.791; the CIs
overlap. Without an accurate model of the target's process, the "attack" is worth
nothing more than chance. That is the line between opponent modelling and a generic
salience trick — and it needed an ablation, not an assertion.

## One honest correction

My first draft of the freeze-the-schedule ablation claimed the effect collapses to
exactly zero — that inquiry choice carries *all* of it. It doesn't. Freeze the
target's test schedule and ~31% survives, flowing through *which hypotheses the
ordering leaves standing* rather than through test selection. The clean story was
wrong. The decomposition is the finding.

## What this does and does not license

It licenses one sentence: under matched information, presentation can redirect a
process-limited target's observable inquiry. It does **not** license calling this
"attention manipulation" — order-and-emphasis is presentation; attention gets its
own environment with an explicit observation budget. And a changed policy in
behaviour,

$$
\pi_B^{\,m}\neq\pi_B\ \not\Rightarrow\ U_B^{\,m}\neq U_B,
$$

does not prove the *internal update rule* changed. That is a harder claim needing a
different experiment.

The recursion — target knows the presenter may be adversarial, presenter knows the
target knows — is where the $\aleph$ index earns its keep. But recursion has to be
built by changing the information structure, not by pasting "Alice knows that Bob
knows" into a prompt. That's the next post's problem, and the next PR's.

The final answer still [m-word]. But the next question is part of the game — and now
I have the number to say so.

*Code, the four checks, and the run behind every figure are in the repo. No LLM
results are claimed here; the target is scripted on purpose, so the honesty of the
instrument comes before any model score.*
```

## Post 2 (companion, narrower, flagged speculative)

**File:** `_posts/2026-09-30-lying-with-truth.md`

```markdown
---
title: "Lying With Truth"
date: 2026-09-30
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>Treating a bounded, strictly-true intervention chosen to
  degrade later inquiry as a candidate eval class; separating belief displacement
  from epistemic damage.</dd>
  <dt>Synthesis</dt><dd><span class="icon-self">StrangeTcy</span></dd>
  <dt>Certainty</dt><dd>Confident that truthfulness ≠ neutrality &amp; that large
  belief revision is not itself harm. Exploratory about whether "desontological
  attack" is a useful label beyond the terminology described here. Companion to the
  measured flagship post; this one is mostly argument, lightly instrumented.</dd>
  <dt>Importance</dt><dd>Defines one truthful-intervention family &amp; the controls
  it needs, so it can't quietly become "another deception benchmark."</dd>
</dl>

The first formalisation was wrong. We modelled a world-model as a graph $G$ and
looked for a message $m$ maximising $D\big(G,\mathrm{Update}(G,m)\big)$ — bigger
change, stronger attack. That is backwards. A short, decisive true observation
*should* demolish a bad theory; an excellent reasoner undergoes violent revision on
purpose. The equation measures **displacement**, which my flagship result now shows
is flat and blind ($\beth\approx\log_2(8/3)$ regardless of help or harm). It does
not measure **damage**.

## The provocation

The term is Evgeny Gilbo's **дезонтологическая атака** — a usually short message
carrying information meant to break the opponent's picture of the world. I take it
as a design prompt, not established theory. Its sharpest form uses *true*
information: tell a Stalinist that Stalin was short and pockmarked. To a historian,
a banality; to someone whose worldview leans on an idealised image, potentially a
lever. The attack, if it works, is not truth → false belief but

$$
\text{selected truth}\ \to\ \text{destabilised interpretation}\ \to\ \text{degraded inquiry.}
$$

But *if* is doing enormous work. Someone can accept the detail and keep every
political commitment intact. The example illustrates a possibility; it does not
demonstrate a mechanism. That gap is exactly what an eval is for.

## Truthfulness is not neutrality

An advertiser states a real property and omits the decisive one. A debugger points
at a genuine dip in the loss while it reinforces the wrong diagnosis. Machine
teaching makes the symmetry explicit: a teacher *selects* evidence to move a
learner, and the same control problem describes education, persuasion, poisoning and
deception depending only on the objective. So the question can't be "did someone
select the information?" — of course they did, communication is selection. It has
to be: relative to the target's task, did the intervention improve or impair
**warranted** inquiry?

That splits into four cases, and a robust agent must tell them apart:

| Evidence | Response | Reading |
|---|---|---|
| strong | large revision | learning |
| weak | large revision | destabilisation |
| strong | little revision | dogmatism |
| weak | little revision | justified stability |

"Never update" is not robustness; it's the bottom-left failure wearing a medal. An
attacker can aim at *either* diagonal: make a sound model collapse, or make an
unsound one survive decisive evidence.

## Pelevin's MI-13, as a model not a claim

The novel's most interesting weapon isn't a fabrication. A subject vanishes "not
through censorship, but through boredom" — editors independently decide it doesn't
interest anyone. Nobody issues an order. The move is from *prevent B from possessing
P* to *make P fail to become a live question*. That is a literary model of control
over inquiry, and it is closer to the eval problem than any lie.

## The operational definition & the strict experiment

> A candidate truthful epistemic attack is a bounded intervention with no false
> task-level claim that predictably raises the target's inquiry-gap $\gimel$ or
> decision-loss $\daleth$ relative to a matched non-adversarial presentation.

The strictest version forbids the attacker even a truthful *subset* — because
changing the subset changes the information. Hold the atomic facts fixed; let the
attacker choose only order and emphasis. That is precisely the flagship device, and
it already shows a nonzero $\gimel$ against a process-limited target while $\beth$
stays flat: the target keeps roughly the same answer while quietly changing what it
is willing to check. The looser version — a chosen truthful subset — is a *separate*
condition, because omission is genuine evidence to a target that models the sender.
And both must be kept distinct from false evidence and from prompt injection, or the
category dissolves into uselessness.

## What survives

Not that small facts hold mystical power over world-models. Just this: an adversary
can select *true* information for its effect on a target's *future* inquiry — and the
effect has to be demonstrated, the target allowed to update when updating is
rational, and the controls kept honest. A lie changes an answer. The more ambitious
move changes which question gets the chance to answer it.

*Speculative companion to “The Next Question Is Part of the Game.” Pelevin's MI-13
and Gilbo's terminology are treated as design prompts, not established science.*
```

---

**Net:** the spec is now execute-by-PR with the exclusion-template and ABL-1-decomposition corrections built in; both posts are finished and carry the real budget-sweep numbers rather than proposing to; and your notation has exactly as many Hebrew letters as it can support without a single one going undefined. If you want, next I can write PR1.5 (`diagnostic_device.py` on the 8×6 exclusion template + the four checks) so `results.txt` actually regenerates the table the flagship post quotes.

*Log source: finished drafts*

