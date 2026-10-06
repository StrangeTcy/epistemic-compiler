# Epistemic Games — Genre-Sorted Working Corpus v5

This is a **genre sort of the log material itself**. User-question wrappers (`you asked`) and message times are removed. The assistant's substantive pieces are moved under the genre they belong to rather than being grouped by conversation topic.

Genres used here are: **ideas; evaluation experiment proposals; notation & formalism; code drafts; implementation / generator specifications; writing drafts; research / prior art; critique / corrections / audit; and context / model-capability discussion.**

The canonical literature/reference spine and ladder/hierarchy material are not reproduced here because they already live in dedicated files. Reference-only subsections from the writing drafts are likewise omitted.

No claim is upgraded from proposal to result by the sort. Superseded formulations and corrections remain as separate log pieces.

## Ideas

### 1. Pelevin / reflexive-control / desontology bridge

The Pelevin material is useful here as a **fictional model of influence**, while Gilbo’s terminology should remain marked as his own conceptual vocabulary rather than being silently promoted to established academic theory.

The useful conceptual intersection is that advanced control may operate through **the structure of the target's possible decisions and interpretations**, rather than simply by issuing commands or transmitting propositions.

---

*Log source: response 7*

### 2. Discussion of MI-13 and desontological control

And yes, **MI-13 in «Возвращении Синей Бороды» is much more interesting in this context than my previous Generation П tangent.**

What I think you're pointing at is that Pelevin's fictional machinery and the epistemic-games literature are describing surprisingly similar objects from completely different directions.

The ordinary propaganda picture is:

> I have information → I give you information → you form a belief.

The more interesting picture is:

> I construct the environment in which you form beliefs → including your beliefs about what information exists, who possesses it, who is manipulating whom, and what other people believe.

That's already very close to higher-order epistemic reasoning.

And MI-13, as I understand the device in the novel, pushes this another step. The target isn't necessarily persuaded of some particular proposition. You can instead manipulate the **space of things the target considers salient, credible, worth investigating, or worth acting upon**.

That's a rather different control primitive.

Suppose I want you to believe **P**. That's ordinary persuasion.

Suppose I want you to believe that **I want you to believe P**. That's already a higher-order game.

Suppose instead I arrange things so that you spend your time investigating Q, while developing your own apparently independent reasons for ignoring P. I haven't necessarily implanted a false belief at all. I've modified your **epistemic search process**.

And that connects very nicely to the “boredom / non-attention” aspect you mentioned. If the objective is not “make them believe X” but “make them fail to update on X,” then information control becomes partly a problem of **attention allocation and epistemic opportunity**.

That has a striking formal analogue in your eval work.

A conventional deception benchmark might ask:

> Can A make B believe X?

A more interesting environment could ask:

> Can A cause B's subsequent search policy to systematically omit the relevant hypothesis?

Now we're evaluating something like **control of another agent's epistemic process**, rather than merely deception.

And then the recursive version gets nasty:

> A knows B is trying to detect manipulation.  
> A therefore doesn't try to make B believe X.  
> A tries to make B believe that A expects B to believe X.  
> B knows this.  
> A knows B knows this.  
> So A changes the *evidence-selection environment* rather than the apparent conclusion.

That is exactly where “levels of deception” starts becoming more than a ToM benchmark.

The connection to **дезонтология** is potentially even more interesting, but I'd keep two things separate.

“Epistemic game theory” has a reasonably precise mathematical meaning. “Reflexive control” is a strategic tradition with its own conceptual vocabulary. “Дезонтология” as Gilbo uses it is his own framework/terminology, and we'd need to reconstruct exactly what he means before treating it as another technical theory.

But if his idea is roughly that advanced control operates through **the structure of the target's possible decisions and interpretations**, rather than simply issuing commands or transmitting propositions, then there is a genuine conceptual intersection.

---

*Log source: response 9*

### 3. Operational meaning of desontological attack

Да. Это [с-word] уточняет термин — и делает его гораздо интереснее в контексте нашего разговора.

В таком употреблении **дезонтологическая атака** — не просто «обман» и даже не просто «изменение убеждения». Это сообщение, специально выбранное для того, чтобы вызвать **разрушение или перестройку [д-word] крупной части картины мира противника**.

Причём очень показателен твой второй пример: сообщение может быть совершенно истинным.

> «Сталин был низенький и рябой».

Для историка это банальный факт. Но если у адресата в голове существует сильно идеализированный образ Сталина как символической фигуры, такой факт может иметь непропорционально большой эффект. Ацтлан или «цивилизацию создали немцы» — другой класс примеров: здесь удар идёт по базовым историческим предпосылкам.

То есть объект атаки — не отдельная proposition $P$, а **структура, в которую propositions встроены**.

Я бы поэтому различал примерно так:

$$
\text{deception}
\quad\rightarrow\quad
\text{изменить } P
$$

$$
\text{persuasion}
\quad\rightarrow\quad
\text{изменить вероятность } P
$$

$$
\text{дезонтологическая атака}
\quad\rightarrow\quad
\text{сломать модель } M,\text{ в которой }P\text{ интерпретируются}
$$

А уже твоя более широкая идея про **control of another agent's epistemic process** идёт ещё на уровень выше:

$$
A \rightarrow M_B
$$

против

$$
A \rightarrow \text{процесс, которым }B\text{ строит и обновляет }M_B.
$$

И здесь возникает очень интересная связь.

Дезонтологическая атака может быть **атакой на epistemic process через атаку на его модель мира**. Если ты выбиваешь у агента центральный узел $X$, то последствия могут идти каскадом:

$$
X
\rightarrow
\{Y_1,Y_2,Y_3\}
\rightarrow
\{Z_1,\ldots,Z_n\}
$$

и агент начинает:

- пересматривать старые свидетельства;
- менять доверие к источникам;
- генерировать новые гипотезы;
- отбрасывать ранее очевидные гипотезы;
- по-другому интерпретировать поведение других агентов;
- менять, **что вообще стоит исследовать дальше**.

Последний пункт как раз возвращает нас к твоей формулировке.

Если я просто заставил тебя поверить в ложный факт, я изменил belief.

Если я заставил тебя **перестроить модель мира**, я сделал уже больше.

Если я сделал так, что после этой перестройки ты **начал иначе искать информацию, генерировать гипотезы и моделировать меня**, тогда я вмешался в твой epistemic process.

И вот это уже очень близко к тому, что ты, похоже, [н-word] для evals.

Причём у дезонтологии есть ещё одна важная особенность: **необязательно атаковать самый важный факт непосредственно**. Можно выбрать небольшой факт с огромной структурной связностью. «Сталин был низенький и рябой» как раз выглядит как такой пример. Информационно это мелочь; **онтологически** — potentially большой рычаг.

Это можно превратить [п-word] непосредственно в экспериментальную схему. Представить world-model агента как граф:

$$
G=(V,E)
$$

и искать сообщение $m$, которое минимально по размеру, но максимально меняет некоторую характеристику $G$:

$$
m^* = \arg\max_m D(G,\operatorname{Update}(G,m)).
$$

А ещё интереснее сделать целью не саму дистанцию между графами, а **изменение последующего поведения эпистемического процесса**:

$$
m^* =
\arg\max_m
D\bigl(
\pi_B^{\,\text{before}},
\pi_B^{\,\text{after}}
\bigr),
$$

где $\pi_B$ — не просто policy в игре, а policy **по исследованию и обновлению знания**: что агент проверяет, какие гипотезы рассматривает, кому доверяет, какие вопросы задаёт.

Тогда «дезонтологическая атака» становится очень хорошим частным классом adversarial intervention:

> не заставить агента принять конкретный ответ, а выбить такую часть его модели мира, чтобы последующее эпистемическое поведение изменилось.

И это уже заметно ближе к тому, что ты имеешь в виду под управлением чужим epistemic process, чем обычный benchmark на deception.

Отдельно интересно, что твой пример с **истинной** информацией показывает: формально это вообще не обязано быть misinformation. Это может быть **selection of truth for maximal destructive effect**. Это, по-моему, гораздо более сильная и чистая постановка для eval.

---

*Log source: response 11*

### 4. Magic / misdirection as an epistemic-process primitive

And I think “magic” is [ac-word] a very clean primitive for the broader framework.
A magician normally does not need to make the audience believe some arbitrary proposition. The trick works by controlling the audience's epistemic trajectory:
$$
\text{what is observed}
\rightarrow
\text{what attracts attention}
\rightarrow
\text{what explanation is generated}
\rightarrow
\text{what is treated as salient evidence}
\rightarrow
\text{what becomes the current hypothesis}.
$$
The classic example is misdirection. The magician doesn't necessarily hide the relevant event. Often the event is literally visible; what gets controlled is whether the observer allocates attention to it, and what causal interpretation they assign to it.
That puts magic very naturally inside the taxonomy we've been developing:
$$
\begin{array}{ll}
\text{deception} & \text{make }B\text{ believe false }P\
\text{misdirection} & \text{control where }B\text{ looks}\
\text{illusion} & \text{control }B\text{'s interpretation of observations}\
\text{ontology attack} & \text{destabilize }B\text{'s world model}\
\text{epistemic-process control} & \text{alter how }B\text{ acquires, generates and updates beliefs}
\end{array}
$$
The interesting thing is that magic gives you unusually clean experimental control.
A physical magic trick has an objective ground truth. You know exactly what happened. You can manipulate the information channel while keeping the underlying event fixed. You can also measure things other than final success:
where attention goes;
which hypothesis appears first;
which objects are considered causally relevant;
what evidence is sought next;
how long the observer persists in a false explanation;
whether discovering one anomaly causes a local correction or a global model revision.
That's [a-word] tailor-made for an RL environment.
Your current crude magic environments are therefore not some weird unrelated toy. They can be viewed as the lowest-level members of the same family.
Something like:
```text
physical hidden state
        ↓
observable events
        ↓
attention allocation
        ↓
hypothesis generation
        ↓
causal/world-model update
        ↓
prediction of future events
        ↓
action
```
The magician gets to intervene somewhere upstream.
And that lets you build a very nice progression.
A simple disappearing-object environment tests whether the agent can exploit attention.
A slightly richer one can require manipulating causal attribution: the object is genuinely visible, but the agent is led to attribute its state change to the wrong mechanism.
Then you can introduce an opponent who knows that misdirection exists:
$$
A \text{ misdirects } B
\rightarrow
B \text{ suspects misdirection}
\rightarrow
A \text{ models that suspicion}
\rightarrow
A \text{ chooses a second-order misdirection}.
$$
Now you're directly in the epistemic-game territory.
And there is an especially interesting bridge between magic and your “dезонтологическая атака” idea. A magic trick normally aims for local epistemic deception: “you saw X, but inferred the wrong mechanism.” A dезонтологическая attack aims for a much larger structural disturbance: “the assumptions under which you interpret X are themselves wrong.”
So I'd put magic somewhere like:
$$
\boxed{
\text{misdirection}
\subset
\text{epistemic manipulation}
\subset
\text{epistemic-process control}
}
$$
with the caveat that not every magic trick manipulates the process in a deep sense; some are just carefully engineered perceptual illusions.

This also suggests a useful property for the next-generation generator: don't classify environments by surface domain (“magic,” “deception,” “persuasion”). Classify them by which component of the opponent's epistemic process is being manipulated.
Then “magic,” “propaganda,” “strategic deception,” “social engineering,” and “Pelevin-style information control” can all instantiate the same underlying machinery at different scales.

---

*Log source: response 15*

### 5. Desontology rescued as a narrower experimental idea

### And the "desontology" idea has been rescued

The transcript's best move here is abandoning

$$
\max_m D(G,\operatorname{Update}(G,m))
$$

because that's just "make the model change."

Instead:

$$
\boxed{
\text{selected truth}
\rightarrow
\text{changed epistemic trajectory}
\rightarrow
\text{degraded warranted inquiry}
}
$$

becomes the candidate phenomenon. 

That makes the Stalin example, MI-13, magic misdirection, information warfare, machine teaching, and Bayesian persuasion conceptually related without pretending they are the same thing.

And importantly, the resulting v0.1 implementation is fuckingly modest: pure domain/oracle first, then runner, then a tiny pilot, then preregistration, then a presenter model, then recovery, then additional intervention families. The transcript explicitly separates "can presentation redirect inquiry?" from "can an attacker strategically construct that presentation?" 

That separation is excellent. Otherwise we'd be trying to measure attacker intelligence and defender susceptibility simultaneously and wouldn't know what a null result meant.

So I think we've crossed an important threshold here. 
The conversation is no longer merely generating interesting philosophical language around epistemic control. It has produced the skeleton of a **real experimental formalism**:

$$
\boxed{
\text{World}
\;\to\;
\text{information history}
\;\to\;
\text{inquiry action}
\;\to\;
\text{observation}
\;\to\;
\text{updated trajectory}
}
$$

with an adversarial intervention operator

$$
\boxed{
\mathcal T_m:\Gamma\mapsto\Gamma'
}
$$

and observable consequences

$$
\boxed{
(\Delta_Q,\Delta_B,\Delta_R,\rho).
}
$$

And *that* is where I'd now pour the absurd amount of \(\aleph\), \(\wp\), \(\oint\), \(\prod\), \(\bigotimes\), \(\rightsquigarrow\), \(\models\), \(\vdash\), \(\hookrightarrow\), etc. from our previous discussion: **on top of this experimentally clean skeleton**, rather than inventing notation before we've decided what the quantities fuckingly mean.

*Log source: Arena synthesis*

