<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the line "ROLE: PRIOR-WORK KILLER (P04-PW)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-02/council/prompts/04_prior_work_killer_prompt.md (sha256 7eb7a445d9a51f929fbe3532bbebb84c29eaaa2fbdc736a64a58f3340d98805b); the response's own PROMPT_ID is M02-P04-PW v1.
Sample:            "b" of two answers to the same prompt that were pasted together; "a" is prior_work_killer.a.md.
Arena mode:        not stated; two answers from two named models suggest battle mode.
Model as shown:    "gpt 6 luna max" (the label the user put on the paste). The response self-reports "ChatGPT (specific deployment model not exposed)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied. The response self-reports browsing yes, code execution no.
Text integrity:    preserved exactly as pasted. The user's label line and the separator between the two answers are not part of the response and are dropped. Several paragraphs end with a trailing space where the arena's citation markers appear to have been stripped; kept as received.
Order of events:   the five game-family cards were frozen in commit 426d693, before this response was stored.
-->

ROLE: PRIOR-WORK KILLER (P04-PW)
PROMPT_ID: M02-P04-PW v1
SELF-REPORTED MODEL (may be wrong): ChatGPT (specific deployment model not exposed)
TOOLS: browsing yes; code execution no
SAW OTHER ROLES' OUTPUT: no

0. Response header (above).

1. Verdicts (P04-PW-1)

**Strongest reason not to proceed as framed:** Q-A’s broad “generate higher-order epistemic problems from explicit semantics” contribution already has close predecessors. *MindGames* generates natural-language problems from dynamic epistemic logic and uses SMCDEL to check entailment; *Hi-ToM* generates questions through fourth-order theory of mind; and the 2026 evolving-scenarios benchmark covers sequential DEL puzzles. A new general-purpose generator would be duplicative unless its **strategic behavior-policy semantics** add something these puzzle benchmarks do not. 

- **Q-A: REFRAME.** Reuse MindGames/SMCDEL and existing DEL-puzzle data. Proceed only with a sharply specified gap—e.g., behavior generated from explicit strategic policies, with ground truth checked independently of the text-generation path. “Higher-order,” “procedural,” or “explicit semantics” alone is not a novelty claim.
- **Q-B: REFRAME.** Broad retrieval of reasoning methods or templates is already well represented, and a 2026 method’s cards have the fields `Trigger / Do / Avoid / Check / Risk`. The plausible wedge is narrower: whether explicit, operational obligations reduce misapplication when a retrieved move is invalid. The proposed arms do not isolate the causal effect of obligations: add a same-card **with/without-obligations** comparison. Also, R4 does not specify a distinct generic explicit-modelling arm, so H3 is not cleanly tested as written. 
- **Prompt-bias note:** “PRIOR-WORK KILLER,” “strongest collision,” and the required “Killed claims” section prime a negative verdict. The seed’s “new mission” and its frozen-card procedure could prime the opposite. I treat neither as evidence of novelty or non-novelty.

2. Collision matrix

### (a) LLM evaluation of epistemic, ToM, or DEL reasoning

- **L01 — VERIFIED [V].** Damien Sileo and Antoine Lernould, “MindGames: Targeting Theory of Mind in Large Language Models with Dynamic Epistemic **Modal** Logic,” Findings of EMNLP 2023, pp. 4570–4577. The seed citation omits “Modal.” The paper generates controlled DEL problems and natural-language premises/hypotheses, uses SMCDEL for entailment, and reports public code and data. Its described generation uses \(K=2\); this is not the same as Hi-ToM’s fourth-order benchmark. **Overlap:** contribution-level for DEL-generated ToM problems; still open for strategic behavior policies and a separately audited text-to-model mapping. Code is Apache-2.0; dataset licence unknown. URL: `https://aclanthology.org/2023.findings-emnlp.303/`; code: `https://github.com/sileod/llm-theory-of-mind`. 
- **L02 — VERIFIED [S] (abstract and accessible article sections, not full text).** Zhaoqun Li, Jieting Luo, and Beishui Liao, “Logical reasoning in evolving scenarios: Evaluating LLMs with dynamic epistemic logic puzzles,” *Knowledge-Based Systems* 342 (2026), 115885, DOI 10.1016/j.knosys.2026.115885. The article describes 2,784 samples based on Muddy Children and Cheryl’s birthday, with answer-prediction and role-playing tasks, and reports lower accuracy on harder cases. This is a close Q-A collision on sequential knowledge updates; strategic policies and independently released artifacts remain unchecked. URL: `https://www.sciencedirect.com/science/article/pii/S0950705126006118`; artifacts/licence: unknown from the material checked. 
- **L03 — VERIFIED [V].** Yufan Wu, Yinghui He, Yilin Jia, Rada Mihalcea, Yulong Chen, and Naihao Deng, “Hi-ToM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models,” Findings of EMNLP 2023, pp. 10691–10706. It generates Sally–Anne-like stories and questions from zeroth through fourth order; the authors say they manually reviewed story/question/answer consistency. This kills “higher-order ToM benchmark” as a novelty claim, but is not a game-theoretic policy generator or demonstrated independent formal verifier. Paper says code and data are released; licence not checked. URL: `https://aclanthology.org/2023.findings-emnlp.717/`. 
- **L04 — VERIFIED [V].** Jinhao Duan et al., “GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations,” NeurIPS 2024; arXiv:2402.12348. It evaluates LLMs in ten games and compares reasoning prompts, reporting that CoT/ToT do not uniformly help. It collides with broad game-theoretic evaluation and intervention claims, not with a formally labeled DEL puzzle family. The public repository lists an MIT licence. URLs: `https://arxiv.org/abs/2402.12348`; `https://github.com/jinhaoduan/GTBench`. 

### (b) Procedural benchmarks and verifiable ground truth

L01, L02, and L03 above already establish substantial prior work on generated epistemic/ToM tasks. Their important difference is that a formal checker, a simulated puzzle, or manual review does not by itself establish that the **natural-language instance** faithfully expresses the formal object.

- **PW-L09 — VERIFIED [V].** Daniel Miedema and Malvin Gattinger, “Exploiting Asymmetry in Logic Puzzles: Using ZDDs for Symbolic Model Checking Dynamic Epistemic Logic,” arXiv:2307.05067 (2023). It uses the existing SMCDEL model checker on formalizations of Muddy Children, Sum and Product, and Dining Cryptographers puzzles. SMCDEL’s repository describes a symbolic DEL checker; its command-line interface covers S5 with public announcements, while its Haskell library supports broader models. This is a strong verifier to reuse for appropriate DEL subfamilies, not an off-the-shelf verifier for every Bayesian/game-theoretic semantics or for validating a prose-to-model translation. SMCDEL is GPL-2.0. URLs: `https://arxiv.org/abs/2307.05067`; `https://github.com/jrclogic/SMCDEL`. 

### (c) Retrieval or composition of reasoning strategies, templates, or skills

- **L05 — VERIFIED [V].** Pei Zhou et al., “Self-Discover: Large Language Models Self-Compose Reasoning Structures,” NeurIPS 2024. The method selects, adapts, and implements reasoning modules into task-specific structures. It is a direct collision with “selecting/composing methods improves solving,” though selection is by the model rather than a fixed trigger matcher and the paper does not establish the proposed invalid-move obligation test. URL: `https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf`. 
- **L06 — VERIFIED [V].** Ling Yang et al., “Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models,” arXiv:2406.04271 (2024). It distills high-level thought templates, retrieves one for a problem, and adapts it. This is a contribution-level collision with retrieval of reusable methods, but not with explicit validity obligations or the proposed S1/S2 test. URL: `https://arxiv.org/abs/2406.04271`. 
- **PW-L10 — VERIFIED [S].** Yanjian Zhang, Guillaume Wisniewski, Nadi Tomeh, and Thierry Charnois, “Reasoning Strategies in Large Language Models: Can They Follow, Prefer, and Optimize?” arXiv:2507.11423 (2025). It studies strategy prompting for logical problem-solving and reports that no single strategy consistently improves accuracy. This directly weakens a general “method hint helps” claim; the precise trigger-matching and obligation design remains open. URL: `https://arxiv.org/abs/2507.11423`. 
- **PW-L11 — VERIFIED [V].** Guangxiang Zhao et al., “Thinking with Reasoning Skills: Fewer Tokens, More Accuracy,” ACL 2026 Industry Track, pp. 2295–2308. It retrieves compact skill cards using retrieval triggers and structures them as `Trigger / Do / Avoid / Check / Risk`; it evaluates math and coding tasks. This is the strongest Q-B collision: the *card format and trigger-based retrieval* are not novel. The proposed S2 test could still differ if it prospectively tests whether checkable obligations prevent invalid application. URL: `https://aclanthology.org/2026.acl-industry.154/`; code: `https://github.com/stallone0000/Reasoning-Skill`; licence not verified. 
- **PW-L12 — VERIFIED [S].** Di Wu, Devendra Singh Sachan, Wen-tau Yih, and Mingda Chen, “Procedural Knowledge at Scale Improves Reasoning,” arXiv:2604.01348 (2026). It retrieves procedural subroutines from a large datastore for reasoning tasks. This further kills generic “retrieved procedural knowledge improves reasoning” novelty; it does not establish trigger-validity obligations in epistemic games. The official repository states a FAIR Noncommercial Research License. URLs: `https://arxiv.org/abs/2604.01348`; `https://github.com/facebookresearch/reasoning-memory`. 

### (d) Controlled prompt-intervention comparisons

The comparisons are not identical to R4, but the broad idea of testing reasoning prompts and ablations is established: GTBench tests reasoning-method variants; Self-Discover ablates its composition stages; TRS reports prompt-strategy and other ablations. I did **not** find in these works the registered combination of length-matched prose, random cards, absent-trigger items, and planted invalid moves. That combination is a possible design contribution, not evidence that the underlying intervention is new. 

### (e) Epistemic-logic model checkers and puzzle solvers

PW-L09 and L01 are the directly useful precedents. SMCDEL provides a formal checker; MindGames reports using it to determine entailment. Reuse is preferable to building another DEL checker. But do not call two executions of one model checker “independent verification,” or mistake a checker’s validation of a formal model for validation that the generated text encodes that model. 

### (f) Evaluation-awareness and strategic-deception benchmarks

- **L07 — VERIFIED [S] (bibliographic/abstract-level only).** “Strategic behavior of large language models and the role of game structure versus contextual framing,” *Scientific Reports* 14 (2024), article 18490. The lead concerns game structure and contextual framing, so it is relevant to CF09, but I did not read the publisher full text or verify the author list here. It is not a formal DEL ground-truth generator. URL: `https://www.nature.com/articles/s41598-024-69032-z`. 
- **PW-L13 — VERIFIED [S].** Xiaojian Li et al., “AwarenessBench: Assessing Cognitive Capabilities of Language Models,” ACL 2026. Its abstract describes metacognition, self-awareness, social awareness, and situational awareness. It is relevant context, but does not make “evaluation awareness” equivalent to recursive epistemic-game reasoning. URL: `https://aclanthology.org/2026.acl-long.124/`. 
- **PW-L14 — VERIFIED [S].** “SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence,” arXiv:2606.02380 (2026; author list not verified in this session). This is a nearby strategic-deception evaluation, but its plan/action-divergence target is not the proposed exact-answer epistemic puzzle task. URL: `https://arxiv.org/abs/2606.02380`. 

**Lead-status summary:** L01 VERIFIED [V]; L02 VERIFIED [S]; L03 VERIFIED [V]; L04 VERIFIED [V]; L05 VERIFIED [V]; L06 VERIFIED [V]; L07 VERIFIED [S]; **L08 UNCHECKED** as a bundle of classic sources. No lead was refuted.

3. Killed claims (PW-K01, ...)

- **PW-K01:** Do not claim “no published benchmark generates higher-order epistemic/ToM instances.” MindGames, Hi-ToM, and the 2026 DEL-puzzle benchmark directly contradict that. 
- **PW-K02:** Do not claim “trigger-matched retrieval of reusable reasoning strategies is new.” Self-Discover, Buffer of Thoughts, TRS, and Reasoning Memory are direct counterexamples at different levels of overlap. 
- **PW-K03:** Do not infer that explicit formal semantics alone guarantee independent ground truth. A checker can verify a formal object while leaving the text-to-object mapping or shared modeling assumptions unvalidated.
- **PW-K04:** Do not claim this design establishes that obligations prevent misapplication unless an obligation-ablation arm is included. Comparing a full pack against prose/random/no-pack controls cannot isolate the obligations’ effect.
- **PW-K05:** Do not claim H3 is resolved by R4 unless L is explicitly the generic “list states, update on events” control. “Length-matched generic prose” alone is not that control.
- **PW-K06:** Do not call benchmark accuracy proof of recursive reasoning, ToM, or a model’s internal strategy. State only performance on the named generated instances.

4. Surviving novelty wedges (PW-N01, ...)

- **PW-N01 — Strategic behavior generated from explicit policies.** A candidate contribution is a family whose public behavior is generated from specified types, beliefs, information, utilities, and policies—not directly supplied as a behavior table—and whose correct answers are checked by a separate implementation. **Dies if** instances reduce to ordinary public-announcement puzzles, or if policies/actions are hand-entered answer tables like v0.
- **PW-N02 — Obligation efficacy, not card novelty.** Test whether explicit, machine-checkable or behaviorally observable obligations reduce wrong applications on trigger-present/invalid instances, against the *same card without obligations* and a generic explicit-modeling control. **Dies if** obligations are merely prose fields, are not checked as a separate intervention, or show no incremental effect over generic modeling.
- **PW-N03 — End-to-end verification boundary.** Demonstrate separate verification of both the formal semantics and the text encoding, with disagreements handled by a prewritten rule. **Dies if** “independent” means only running the same generator/judge twice, or if no independent check of the text-to-model mapping is performed.

5. Reuse list (P04-PW-2)

- **MindGames:** Reuse its generator/data as the direct DEL baseline; paper reports public code/data and the repository shows Apache-2.0 code. Dataset licence: unknown. 
- **SMCDEL:** Reuse as the DEL verifier where the semantics fit; GPL-2.0. Do not assume it checks arbitrary strategic-game solution concepts. 
- **Hi-ToM:** Reuse its generated higher-order ToM benchmark/code as a comparator; paper says data and code are released. Licence: unknown from the sources checked. 
- **L02 benchmark:** Reuse or compare against it before generating more Muddy Children/Cheryl-style examples. Dataset, code, and licence: unknown from the material checked. 
- **GTBench:** Reuse its game-evaluation framework as a strategic-game comparator, not as a DEL truth oracle; repository lists MIT. 
- **TRS / Buffer of Thoughts / Reasoning Memory:** Use as retrieval baselines or prior-method comparators. TRS code is public but licence was not verified; BoT’s project is identified in its paper, licence unknown; Reasoning Memory’s repository specifies a FAIR Noncommercial Research License. 

6. Evidence-pack audit (P04-PW-3)

**Five concept-node scope checks against primary benchmark sources—not verification of the classic bibliographic nodes:**

- `dynamic-epistemic-logic`: MindGames formalizes knowledge updates and public announcements and uses a model checker. This supports DEL’s relevance to generated epistemic tasks, not the graph’s classic-paper edges. [V] 
- `strategic-reasoning`: GTBench evaluates LLMs in strategic games. The overlap is real, but its game-playing evaluation is not the same contribution as a formally generated, answer-labeled epistemic puzzle family. [V] 
- `opponent-modelling`: GTBench evaluates play against conventional and model opponents; that does not, by itself, establish explicit higher-order belief modeling. [V] 
- `evaluation-awareness`: AwarenessBench’s abstract includes situational-awareness evaluation, but that is not automatically evaluation-gaming measurement. [S] 
- `strategic-deception`: SPADE-Bench is a nearby strategic-deception benchmark, but its described target is plan/action divergence rather than DEL puzzle truth conditions. [S] 

**Discrepancy found:** the L01 seed citation shortens the published title by omitting “Modal.” I did not verify a metadata error in the classic graph nodes. The digest itself identifies `baltag-moss-solecki-1998`, `aumann-1976`, `aumann-brandenburger-1995`, `bernheim-1984`, `pearce-1984`, `harsanyi-1967`, `crawford-sobel-1982`, `kamenica-gentzkow-2011`, and several other classic entries as bare bibliography or near-bare entries; I did **not** source-check their original texts in this session. The same JSTOR URL appears on both the Bernheim and Pearce nodes in the supplied pack: flag that for bibliographic review, but I cannot confirm from the sources accessed whether it is an error.

7. Binding terminology and citation discipline (P04-PW-4)

- Avoid **“first,” “novel,” “independently verified,” “validated strategy,”** and unqualified **“higher-order reasoning benchmark”** until the exact scope has been compared against the cited work. Distinguish a DEL puzzle benchmark from a strategic game with policy-generated behavior.
- Say **“separately implemented checker”** only when that is true. Separately report whether the formal semantics, generator, text renderer, and verifier share code or assumptions.
- Cite the primary paper and artifact for every prior-work claim; mark abstract-only checks [S], and leave release/licence status “unknown” when it was not checked.
- Suggested prior-work wording: *“We reuse and extend existing DEL-generated ToM benchmarks and model-checking tools; our targeted difference is [specific policy-generated semantics or obligation test]. We make no claim to introduce DEL-based higher-order evaluation or retrieval of reasoning methods.”*
