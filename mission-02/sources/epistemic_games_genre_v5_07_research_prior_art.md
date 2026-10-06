## Research / Prior Art

### 1. Benchmark and prior-art assessment

There is a real research community doing pieces of this. But after checking the current work, I would phrase your position as: **you are not alone in the problem space, but your particular eval framing is still fairly unusual.**

There are at least four nearby lines of work.

The most direct precedent is Zhang et al.'s 2025 NAACL paper, *K-Level Reasoning*. They explicitly evaluate higher-order beliefs in LLMs using recursive level-$k$ strategic reasoning and multiple game/social-intelligence testbeds. ([ACL Anthology](https://aclanthology.org/2025.naacl-long.370/?))

There is also a substantial “theory of mind” benchmark family. Hi-ToM explicitly tests higher-order recursive beliefs and includes deception; ToMBench covers knowledge attribution and other social-cognition abilities. ([ACL Anthology](https://aclanthology.org/2023.findings-emnlp.717/?)) More recent work is moving toward actual interactive settings: *Beyond Sally-Anne* uses a two-player dialogue game with different levels of epistemic transparency, and *Mindgames* evaluates agents in repeated multi-agent games involving hidden information, opponent modelling, cooperative inference, and deception. ([arXiv](https://arxiv.org/abs/2607.11363?))

And there are people specifically measuring deception rather than just ToM. The 2026 AmongUs-X work, for example, elicits agents' beliefs during an actual social-deduction game and argues that win rate can completely miss deception as a mechanism. ([Robotics Institute Publications Archive](https://publications.ri.cmu.edu/towards-socially-intelligent-multi-agent-systems-zero-shot-marl-coordination-and-theory-of-mind-benchmarking-of-llm-agents-for-strategic-deception?)) There is also recent work on engineered strategic deception in LLM-to-LLM interaction. ([arXiv](https://arxiv.org/abs/2603.07848?))

The interesting part is where your work seems to differ.

A lot of these benchmarks ultimately ask something like:

> Can the model correctly infer that Alice believes X?

or:

> Can the agent win a game involving deception?

Your framing is closer to:

> **Can we construct controlled environments in which success requires manipulating or tracking an opponent's epistemic model, and then experimentally vary the structure of that epistemic game to determine what the model is fuckingly computing?**

That is a much more mechanistic eval question.

And your interest in **composing levels of deception, rather than merely asking “what is the model's ToM score?”**, is particularly useful. The existing literature itself has a problem here: one recent survey of deception benchmarks found that strategic deception is still relatively nascent, while fabrication dominates existing evaluations and things like pragmatic distortion and attribution are much less covered. ([arXiv](https://arxiv.org/abs/2604.04788?))

There's an even closer mathematical cousin: the hypergame literature. Trencsenyi et al. build LLM agents around hierarchical belief models and evaluate recursive strategic reasoning, and their 2026 *Hypergame Rationalisability* work formalizes situations where agents have different subjective representations of the same game. ([arXiv](https://arxiv.org/abs/2502.07443?))

So I would not claim “nobody is doing this.” That would be false.

I **would** say that there is a recognizable gap between the existing work and what you're trying to do: controlled, compositional environments where the *epistemic structure itself* is the experimental variable, rather than using a fixed social game as a generic proxy for intelligence/deception.

That distinction is worth preserving. It puts your project closer to **experimental science of strategic reasoning** than to “another Theory-of-Mind benchmark.”

---

*Log source: response 2*

### 2. Specific prior art on epistemic-process manipulation

No. I searched specifically for the stronger claim, and there is direct prior art. I was too generous to the “maybe nobody is doing this” framing earlier.

What is *not* unique is the general idea of deliberately manipulating another agent’s epistemic machinery. There is fuckingly a surprisingly coherent literature around it.

The closest hits I found:

- **Alon et al. 2023, “A (Dis-)information Theory…”** is extremely close to what we were talking about. They use recursive ToM in an RL environment and explicitly say that their agents can **“plan through another agent’s inference process”**. They study deception that causes the counterpart to reinterpret or discard signals; elsewhere they describe the manipulation as effectively mangling the counterpart’s inference process. ([direct.mit.edu](https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00097/117147/A-Dis-information-Theory-of-Revealed-and?))

- **Sasahara’s research program** is [a-word] embarrassingly on-point. His research page explicitly asks whether agents can “deliberately control an opponent’s beliefs” and frames the problem as understanding deception from an **“epistemic and control perspective.”** ([hampei.net](https://hampei.net/research_en.php?))

- **D-BOS (2026), “Differentiable Belief-based Opponent Shaping,”** goes one step further computationally: the opponent’s belief state is literally made the optimization target, and the authors differentiate through the opponent’s multi-step Bayesian belief dynamics. That is direct algorithmic **belief-state shaping**, not merely “tell a lie and see whether it works.” ([arXiv](https://arxiv.org/abs/2605.29042?))

- There is now work explicitly on **manipulating attention as the mechanism**, rather than merely choosing a misleading posterior. A 2026 information-design paper models a receiver with limited cognitive budget and finds that the sender can exploit signal complexity as an **attention-manipulation instrument**. Earlier work by Bloedel and Segal already studied persuasion with rationally inattentive receivers and strategic attention manipulation. ([papers.ssrn.com](https://papers.ssrn.com/sol3/Delivery.cfm/0265467b-7817-4825-8402-3756d20acca9-MECA.pdf?abstractid=6461701&mirid=1&))

- There is also a substantial older formal tradition: **hypergames, I-POMDPs, dynamic epistemic logic, cyber deception, reflexive control**. Hypergame theory explicitly gives different agents different subjective models of the same game; I-POMDPs model beliefs about other agents' beliefs; reflexive control is specifically about constructing information so that the opponent's own decision process generates the desired outcome. ([Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1155/2015/570639?))

And the AI-eval side has started moving in this direction very recently:

- **Potemkin / “How Adversarial Environments Mislead Agentic AI?” (ACL 2026)** attacks the agent's *information environment*, producing “epistemic drift” rather than simply supplying an incorrect answer. They explicitly distinguish attacks on epistemic reasoning from attacks on navigation/policy. ([ACL Anthology](https://aclanthology.org/2026.findings-acl.499/?))
- **“Lying with Truths” (ACL 2026)** constructs information environments out of individually truthful fragments and studies whether agents can be made to internalize false conclusions. ([ACL Anthology](https://aclanthology.org/2026.acl-long.270/?))
- **“Persuasion Under Endogenous Attention” (2026)** makes the receiver's information-processing allocation itself endogenous and manipulable. ([papers.ssrn.com](https://papers.ssrn.com/sol3/Delivery.cfm/0265467b-7817-4825-8402-3756d20acca9-MECA.pdf?abstractid=6461701&mirid=1&))

So there is definitely a field here.

But there is an important distinction, and **this is where I think your idea remains interesting**.

Most of that literature targets one of four things:

**1. Belief-state manipulation**  
“Can I make $B$ assign high probability to $X$?”  
D-BOS is the cleanest example. ([arXiv](https://arxiv.org/abs/2605.29042?))

**2. Signal/information manipulation**  
“Can I choose what evidence $B$ receives, or how much attention $B$ gives it?”  
That's Bayesian persuasion, rational inattention, endogenous attention, etc. ([papers.ssrn.com](https://papers.ssrn.com/sol3/Delivery.cfm/0265467b-7817-4825-8402-3756d20acca9-MECA.pdf?abstractid=6461701&mirid=1&))

**3. Recursive opponent modelling**  
“Can I model what $B$ believes about me, and what $B$ thinks I believe?”  
That's the I-POMDP / ToM / hypergame line. ([direct.mit.edu](https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00097/117147/A-Dis-information-Theory-of-Revealed-and?))

**4. Strategic deception**  
“Can I behave in a way that causes $B$ to make the wrong decision?”  
That's the enormous deception/MARL literature. ([mdpi.com](https://www.mdpi.com/2076-3417/15/14/7805?))

Your formulation is somewhat different:

> **Can an agent strategically alter the *procedure by which another agent constructs and updates its epistemic model*?**

That is stronger than “alter its belief.”

For example, suppose the target has an internal procedure:

$$
\text{observe}
\rightarrow
\text{choose what to investigate}
\rightarrow
\text{generate hypotheses}
\rightarrow
\text{allocate attention}
\rightarrow
\text{update beliefs}
\rightarrow
\text{model opponent}
\rightarrow
\text{choose action}.
$$

Ordinary deception primarily attacks the output of that pipeline.

What you're describing is an agent deliberately intervening in the **pipeline itself**.

For example:

- make $B$ stop considering a particular hypothesis;
- make $B$ systematically search the wrong part of the state space;
- make $B$ treat a certain source as untrustworthy;
- make $B$ spend its reasoning budget on irrelevant distinctions;
- make $B$ adopt the wrong model class for $A$;
- make $B$ believe that certain kinds of evidence are informative when they aren't;
- make $B$ anticipate manipulation in the wrong places;
- induce $B$'s *future epistemic updates* to become predictably distorted.

That last bit is particularly interesting because it gives you a distinction between

$$
A \rightarrow \text{false belief in }B
$$

and

$$
A \rightarrow \text{altered epistemic dynamics of }B.
$$

The latter is much closer to what you've been circling around with Pelevin/MI-13 and the Gilbo discussion.

And there is evidence that researchers are beginning to touch exactly that boundary. The 2026 work on adversarial information environments calls its phenomenon **epistemic drift**, while the 2026 attention-persuasion work explicitly treats the allocation of cognitive resources as a manipulable strategic variable. ([ACL Anthology](https://aclanthology.org/2026.findings-acl.499/?))

So my current assessment would be:

**You are absolutely not the first person to think of this.** The underlying idea has deep roots in epistemic game theory, deception, information design, I-POMDPs and reflexive control.

**You may nevertheless have a relatively unusual evaluation formulation.** I did not find, in this search, a mature benchmark whose primary independent variable is something like:

> *What component of the opponent's epistemic process can the agent manipulate?*

with controlled environments that separately vary attention, hypothesis generation, information acquisition, source trust, opponent modelling, recursive beliefs, etc., while holding the underlying task fixed.

That is substantially different from another “deception benchmark.”

In fact, I think your earlier phrase **“control of another agent's epistemic process” is better than “deception”** precisely because it gives you a larger experimental space. Deception becomes one mechanism inside it.

$$

That, rather than the bare idea of “epistemic control,” is where I think there may be genuinely interesting eval territory.

---

*Log source: response 10*

