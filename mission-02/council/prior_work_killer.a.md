<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the first line "ROLE: PRIOR-WORK KILLER (P04-PW)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-02/council/prompts/04_prior_work_killer_prompt.md (sha256 7eb7a445d9a51f929fbe3532bbebb84c29eaaa2fbdc736a64a58f3340d98805b); the response's own PROMPT_ID is M02-P04-PW v1.
Sample:            "a" of two answers to the same prompt that were pasted together; "b" is prior_work_killer.b.md.
Arena mode:        not stated; two answers from two named models suggest battle mode.
Model as shown:    "fable 5" (the label the user put on the paste). The response self-reports "Claude (Anthropic)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied. The response self-reports browsing yes (web search, snippet-level only), code execution no.
Text integrity:    preserved exactly as pasted. The user's label line and the separator between the two answers are not part of the response and are dropped. The response contains a first, short header block followed by two lines of search narration, then a second, full header block glued to the end of the narration ("...surfaced above.ROLE: PRIOR-WORK KILLER (P04-PW)"); kept as received.
Order of events:   the five game-family cards were frozen in commit 426d693, before this response was stored.
-->

ROLE: PRIOR-WORK KILLER (P04-PW)
PROMPT_ID: M02-P04-PW v1
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic)
TOOLS: browsing yes (web search only, snippet-level; no full-text fetch, no code execution)
SAW OTHER ROLES' OUTPUT: no

Before writing I will run verification searches on the seed's leads and on the obvious missing areas (symbolic DEL model checkers as independent verifiers; procedurally generated ToM benchmarks; retrieval-of-strategy work; distractor/length controls).Running a second batch to check the remaining seed leads (L02, L04, L05, L07) and the DEL-ToM collision surfaced above.ROLE: PRIOR-WORK KILLER (P04-PW)
PROMPT_ID: M02-P04-PW v1
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic)
TOOLS: browsing yes (web search, snippet-level only — tagged [S]; where a snippet was substantial and consistent across multiple independent sources I still tag [S], not [V], because I did not read full texts); code execution no
SAW OTHER ROLES' OUTPUT: no

Search-budget disclosure: I ran 5 searches (MindGames, Hi-ToM, SMCDEL, ExploreToM, Buffer of Thoughts) before the budget was exhausted. L02, L04, L05, L07 and all L08 primary sources remain UNCHECKED this session; claims about them are [R] or restate the seed. Prompt-leading flag (ground rule 2): this role prompt presupposes that "the published work that already does what this mission proposes" exists; I treated that as a hypothesis to test, and for Q-B's specific contribution I did not find it.

---

## 1. Verdicts (P04-PW-1)

**Attack first — the strongest argument against proceeding as framed.** Q-A asks for a "minimal specification" of a generated epistemic family with inspectable semantics and an independently auditable judge. Nearly every ingredient of that already ships, with code: MindGames leverages dynamic epistemic logic to generate controlled problems and introduces verbalization techniques to express them in English [S], and its code and datasets are publicly available [S]. The independent verifier Q-A treats as the hard part is a mature, maintained artifact: SMCDEL, a symbolic model checker for Dynamic Epistemic Logic [S], distributed under GNU General Public License v2.0 or later [S], whose example library already contains the seed's own named headroom-check puzzles — SMCDEL.Examples.Cheryl ... SMCDEL.Examples.DrinkLogic [S] and a worked muddy-children encoding [S]. And the seed's "instances on which the obvious reading is systematically wrong" is precisely the published contribution of ExploreToM, which leverages an A* search over a custom domain-specific language to produce complex story structures and novel, diverse, yet plausible scenarios to stress test the limits of LLMs [S], with accuracies as low as 0% and 9% on ExploreToM-generated data [S]. Building a new v1 DEL/ToM generator would reproduce 2023–2025 work with fewer tests and no community validation. That is the kill case; what survives it is narrower than the seed's framing.

**Q-A: REFRAME.** Strongest collision: L01 (MindGames) + SMCDEL jointly. Do not build a DEL-puzzle generator or verbalizer; reuse. The defensible residue of Q-A is the part the v0 docstring itself names and no lead I found covers: a family whose *public behaviour table is generated from utilities, a base policy and a solution concept* (signalling/level-k/persuasion semantics), plus the S2 "valid-looking but invalid" construction. Q-A should be re-scoped from "minimal specification of a higher-order epistemic family" (already exists) to "minimal game-theoretic extension not expressible as a plain DEL puzzle, verified against an existing checker where the two overlap."

**Q-B: PROCEED, with the claim narrowed.** Strongest collision: L06 (Buffer of Thoughts), which already does similarity-based retrieval of procedural templates: a meta-buffer stores high-level thought-templates distilled from problem-solving across tasks; for each problem a relevant thought-template is retrieved and adaptively instantiated [S]; ReasonFlux extends this with a structured template library [S]. So "retrieval of strategies helps LLM reasoning" is claimed prior art. What I did **not** find in this session, and do not recall existing [R]: a *pre-registered, controlled* test of trigger-matched strategy retrieval against length-matched prose and random-card controls, with a planted trigger-present-but-move-invalid stratum testing whether stated validity obligations prevent misapplication. That evaluation design — not strategy retrieval — is Q-B's only novelty. If the Council proceeds, the contribution must be stated as "a controlled negative-capable test of retrieval-augmented strategy hints," never as a new method.

---

## 2. Collision matrix

Seed leads first, then new items (PW-L09+).

### (a) LLM evaluation of epistemic / ToM / DEL reasoning

**L01 — VERIFIED (as a collision; some seed unknowns resolved).** Sileo & Lernould, *MindGames*, Findings of EMNLP 2023, pp. 4570–4577, https://aclanthology.org/2023.findings-emnlp.303/ [S]. Generates DEL problems and verbalizes them; the dataset encompasses numerous variations of the Muddy Children and Drinking Logicians problems [S]. Seed's open questions answered: code and dataset are public (GitHub sileod/llm-theory-of-mind; HF sileod/mindgames) [S]; on depth, a 2025 survey states the published MindGames dataset is currently limited to testing second-order beliefs, though it has the potential to assess higher-order reasoning [S]. A secondary table describes its ground truth as model-checker-derived [S]. Overlap with Q-A: **contribution-level** for "DEL-grounded generation + verbalization + exact ground truth"; **topical** for higher-order depth and for game-generated behaviour (absent there). Note also: a related task was incorporated into BIG-Bench as the epistemic-reasoning task [S].

**L02 — UNCHECKED.** The 2026 ScienceDirect DEL-puzzle benchmark; search budget exhausted. If it exists as described, it deepens the L01 collision (muddy children + Cheryl's birthday at scale) and bears directly on the headroom unknown (H5). Must be verified before Gate 2.

**L03 — VERIFIED.** *Hi-ToM*, Findings of EMNLP 2023, pp. 10691–10706, arXiv:2310.16755 [S]. Explores higher-order ToM involving recursive reasoning on others' beliefs; evaluation of various LLMs indicates a decline in performance on higher-order tasks [S]; questions range from Order 0 up to Order 4 [S]; it also incorporates agent communications, including deceptive public and private claims [S]. Author-order discrepancy: the seed says "Wu et al."; the ACL PDF byline leads with Yinghui He (He and Wu appear as co-first authors; OpenReview lists Wu first) [S] — cite carefully. Overlap: **contribution-level** against any claim that "higher-order" is new; **topical** only vs. the game-theoretic semantics and the strategy-pack gate.

**PW-L09 — DEL-ToM** (EMNLP 2025): "Del-tom: Inference-time scaling for theory-of-mind reasoning via dynamic epistemic logic," EMNLP 2025, pp. 11383–11397 [S]. A DEL-structured inference-time method. Direct threat to Q-B's premise that a DEL-style method hint is an untested intervention: a DEL-based reasoning scaffold has already been published as a *method*. Q-B's control structure remains unduplicated, but any Q-B write-up must cite this. Overlap: contribution-level with "DEL method hints help"; topical with the retrieval/obligation apparatus.

**PW-L10 — AutoToM** (arXiv:2502.15676) [S]: automated model-based mental inference; on Hi-ToM, while GPT-4o declines sharply as ToM order increases, AutoToM maintains a smaller drop and substantially higher accuracy on higher-order questions [S]. This is published evidence for the seed's intuition 3 (explicit modelling beats narrative reading) — which means that intuition is *not* a novel hypothesis, it is a replication target, and it strengthens H3 (generic explicit modelling explains gains) as the default expectation.

**PW-L11 — prompting-method line for ToM**: RECTOM compared against CoT, SimToM and TimeToM on Hi-ToM [S]; EnigmaToM (Findings ACL 2025) [S]. A whole literature already tests ToM-specific prompting interventions against CoT baselines. None, to my knowledge [R], uses length-matched or random-hint controls — that absence is Q-B's wedge and should be stated with citations to these as the contrast class.

**PW-L12 — FANToM** [S]: tests models in multi-party conversational settings where characters possess unequal access to ground-truth information. Topical overlap with "information is public/private and sequential."

### (b) Procedural generation with verifiable ground truth; adversarial instances

**PW-L13 — ExploreToM**, Sclar et al., ICLR 2025 [S]. Program-guided adversarial generation: A* over a DSL; models driven to near-floor [S] (note an internal discrepancy across pages: the Meta abstract page says accuracies as low as 5% while the ICLR version says 0% and 9% [S] — version difference, verify before citing numbers); stories generated to challenge one model remained difficult for other models [S]. **Contribution-level collision** with Q-A's "obvious reading systematically wrong by construction," and it bears on H5: generated (non-canonical) instances have ample headroom, while canonical puzzles are the contaminated stratum — this partially answers two of the seed's known_unknowns.

**PW-L14 — MMToM-QA** [S]: procedural generation where the agent is formulated as a POMDP and belief is represented as a probability over object locations, with ground-truth beliefs recorded. Shows "explicit semantics → computed ground truth" is established practice even outside logic puzzles.

**PW-L15 — OSCToM** (arXiv 2605.20423, 2026) [S]: RL-guided adversarial generation for high-order ToM; its related-work framing confirms ExploreToM's position and notes its scaling limits beyond 3rd-order depth [S]. UNCHECKED beyond snippet.

### (c) Retrieval / composition of reasoning strategies

**L06 — VERIFIED.** Buffer of Thoughts (NeurIPS 2024; arXiv:2406.04271), Yang et al. [S]. Retrieval is embedding-similarity over distilled problems [S]; templates carry no validity obligations and selection is not a deterministic feature-trigger match. Overlap: **contribution-level** against "retrieving procedural knowledge improves LLM problem solving"; **topical** against the IR's obligations, declared-feature matching, and registered controls.

**PW-L16 — ReasonFlux** (arXiv:2502.06772) [S]: constructs a structured thought template library enabling more precise, targeted retrieval [S]. Closes some of the gap between BoT's embedding retrieval and the IR's structured matching — the "structured retrieval of templates" wedge is thinner than the seed assumes.

**L05 — UNCHECKED** this session. From memory [R]: Self-Discover (Zhou et al., 2024) has the model select and compose reasoning modules per task; no external trigger matcher, no obligations, no misapplication stratum. Treat as the "model-selects" alternative arm in any discussion, but verify before citing specifics.

### (d) Controlled ablations of prompt interventions

Nothing found this session with the exact P/L/R/N + S1/S2/S3 design. From memory [R]: Shi et al. 2023 ("LLMs can be easily distracted by irrelevant context") shows added non-informative text *hurts*, which makes CF01 a live, documented confound and makes the length-matched arm L mandatory rather than optional; GTBench (L04, UNCHECKED, [R]) reportedly found CoT-style methods do not uniformly help in game-theoretic tasks. I could not verify either this session. **This cell of the matrix is where Q-B's novelty lives, and it is also the cell I could least verify — flagging that honestly.**

### (e) Independent verifiers

**PW-L17 — SMCDEL — VERIFIED as artifact** [S]. Haskell, GPL-2+, maintained (v1.3.0, 2024 Zenodo DOI) [S]; web demo [S]; caveat: the executables only provide model checking for S5 with public announcements; for K and more complex models and updates it must be used as a Haskell library [S]. So R1's independent verifier exists off the shelf for the S5/public-announcement subfamilies; private/strategic information needs the library or another tool.

**PW-L18 — other checkers** [S]: finite-state model checkers for various epistemic logics are available, e.g., MCMAS, DEMO, SMCDEL, and MCK. Two genuinely independent implementations for cross-checking exist; H4 is close to trivially satisfiable for DEL subfamilies — which *weakens* H4 as a contribution claim.

**PW-L19 — ToM-LM** (arXiv:2404.15515) [S]: delegates ToM reasoning to the SMCDEL model checker, to perform the ToM reasoning in a transparent and verifiable way [S]. This instantiates the seed's known_alternative "give solvers code execution / an external solver, and the method hint becomes moot" — it is published, so the Q-B write-up must position the pack against tool-delegation, not only against prompting controls.

### (f) Evaluation-awareness / strategic deception

Not searched this session (budget). Evidence-pack items (`lying-with-truths-2026`, `dbos-2026`, `evaluation-awareness`) UNCHECKED; topical only relative to Q-A/Q-B as framed.

**L04, L07, L08 — UNCHECKED** this session. L08's primary texts (Aumann 1976, Crawford-Sobel 1982, Kamenica-Gentzkow 2011, etc.) are foundational theory, not collisions with the *contribution*; they are inputs to card authoring. See §6 for bibliographic problems in the pack's records of them.

---

## 3. Killed claims

- **PW-K01.** "We introduce DEL-grounded procedural generation of epistemic problems with exact ground truth and natural-language verbalization." Dead: MindGames, 2023, with public code and data [S].
- **PW-K02.** "First/novel higher-order epistemic benchmark," or "higher-order" as a headline differentiator. Dead: Hi-ToM (orders 0–4, with deception) [S]; ExploreToM and successors [S].
- **PW-K03.** "Independent verification of epistemic-puzzle ground truth is a new capability we must build." Dead as a build-claim: SMCDEL, DEMO, MCMAS, MCK exist [S]; ToM-LM already used SMCDEL as the verifying component [S]. H4 may be *run*, but it is an engineering check, not a contribution.
- **PW-K04.** "Constructing instances where the obvious/narrative reading is systematically wrong" as a novel idea. Dead: ExploreToM does adversarial search for exactly such instances and drives frontier models to near-floor [S].
- **PW-K05.** "Retrieving stored procedural strategies improves LLM reasoning" as a hypothesis this mission could be first to confirm. Dead as a first-claim: BoT and ReasonFlux claim it with benchmark gains [S]. The mission can only test it *properly* (controls, registration), not discover it.
- **PW-K06.** "Explicit state-tracking/model-building helps on epistemic tasks" as a finding. Dead: AutoToM's higher-order results [S], DEL-ToM [S], the SimToM/TimeToM line [S]. This must be the mission's *baseline expectation* (it is H3), not its result.
- **PW-K07.** Any claim that canonical puzzles (muddy children, Cheryl's birthday) can serve as uncontaminated test items. Not strictly killed, but prior work treats classic ToM sets as leaked and trivially perturbable [S] (trivial alterations of the ToMi dataset cause model performance to drop [S]); the registered set must be generated-only.
- **PW-K08.** Any mechanism claim ("models perform level-k reasoning / possess ToM"). Already barred by the seed's claim ceiling; prior work shows even the field's own mechanism claims are contested [S]. Keep barred.

---

## 4. Surviving novelty wedges

- **PW-N01 — Game-generated behaviour tables.** A family where the observed public behaviour is *derived* from explicitly specified utilities, a base policy, and a solution concept (level-k with explicit level-0; signalling equilibrium; persuasion), rather than hand-specified (v0) or purely announcement-logical (MindGames/SMCDEL). This is the v0 docstring's own stated gap and no checked lead fills it. **Dies if:** a published benchmark already derives verifiable public behaviour from explicit solution concepts — GTBench (L04, unchecked) and any "LLM signalling-game benchmark" are the live threats; verify both before Gate 2.
- **PW-N02 — The S2 misapplication stratum with obligations.** Mechanically planting trigger-present-but-move-invalid instances and testing whether a card's *stated validity obligations* prevent misapplication. I found nothing like it. **Dies if:** any skill-/template-library work (BoT ablations, Voyager-style skill preconditions [R], Self-Discover variants) already ran a planted-invalid-applicability test with outcome measurement.
- **PW-N03 — The controlled, registered retrieval test itself.** P/L/R/N arms, length-matched and random-card controls, characterization frozen pre-output, paired analysis, stop rule. BoT/ReasonFlux report gains without such controls [S as to what their abstracts claim; absence of controls is [R] and must be confirmed against their full texts]. **Dies if:** a controlled ablation of retrieved-template prompting with length-matched controls exists; a targeted search for "irrelevant/random hint controls for prompting interventions" is mandatory before Gate 2.
- **PW-N04 — Cross-implementation agreement as a reported metric.** Measuring and publishing generator-vs-SMCDEL (or DEMO) agreement rates per subfamily, with a pre-written exclusion rule (R1). Modest, real, cheap. **Dies if:** MindGames or L02 already report exactly this (plausible for MindGames, since its ground truth appears model-checker-derived [S]) — in which case reuse their number and drop the claim.
- **Withdrawn wedge:** "inference from silence" (seed's why_it_might_be_true #2) is *not* a wedge — muddy children, the canonical generated puzzle in both MindGames and SMCDEL, is precisely inference from non-announcement [R].

---

## 5. Reuse list (P04-PW-2)

| Artifact | Use | Availability / licence |
|---|---|---|
| SMCDEL (github.com/jrclogic/SMCDEL) | Independent verifier for S5/public-announcement subfamilies; its Examples (Muddy, Cheryl, DrinkLogic, SumAndProduct) [S] as headroom pilots | GPL-2.0-or-later [S]; Haskell; web demo |
| MindGames dataset + code (HF sileod/mindgames; github sileod/llm-theory-of-mind) | Instance source; verbalization templates; baseline numbers | Public [S]; licence unknown — check |
| Hi-ToM | Higher-order + deception stratum; avoids building a story generator | arXiv/ACL; data availability and licence unknown |
| ExploreToM (Meta/ICLR 2025) | Adversarial generation pattern; evidence of headroom on generated instances | Code status and licence unknown — check |
| DEMO / MCMAS / MCK [S] | Second independent checker for cross-verification (strengthens R1 beyond one external tool) | Academic tools; licences unknown |
| DEL-ToM, SimToM, TimeToM, AutoToM | Published method baselines to position arm P against | Papers [S]; code unknown |
| BoT / ReasonFlux | The retrieval-method contrast class for Q-B's related-work section | arXiv [S]; code unknown |

**Not reusable from prior work (hence buildable):** the game-generated behaviour-table subfamily (PW-N01) and the S2 planting machinery (PW-N02).

---

## 6. Evidence-pack audit (P04-PW-3)

All checks below are from memory **[R]** except where tagged; I had no search budget left for bibliographic verification. These are *suspected* discrepancies to verify, not findings.

1. **`aumann-1976`** — DOI given is `10.1214/aop/1176996109`, an *Annals of Probability* prefix; "Agreeing to Disagree" appeared in the *Annals of Statistics* (4(6), 1976) [R]. Likely wrong DOI. Bare bibliography otherwise.
2. **`pearce-1984`** — the pack gives the *same* JSTOR URL (`stable/1911391`) for both `bernheim-1984` and `pearce-1984`. Both papers are titled "Rationalizable Strategic Behavior" (Econometrica 52(4), 1984) but they are distinct articles; one of the two links must be wrong [R]. Classic copy-paste error; whoever authors the `game` cards from these nodes will propagate it.
3. **`plaza-2007`** — Plaza's "Logics of Public Communications" was originally 1989 (ISMIS proceedings); 2007 is the Synthese reprint [R]. Dating it 2007 misorders it relative to `baltag-moss-solecki-1998`, which the graph has BMS *extending* Plaza — temporally incoherent under the pack's own dates.
4. **`baltag-moss-solecki-1998`** — the DOI given (`10.1016/S0004-3702(98)00035-1`) is an *Artificial Intelligence* journal identifier; BMS 1998 is a TARK proceedings paper [R]. Suspect link.
5. **`camerer-ho-chong-2004`** — "A Cognitive Hierarchy Model of Games" is QJE 119(3) 2004; the DOI given (`10.1162/003465304323023249`) looks like a *Review of Economics and Statistics* identifier [R]. Suspect.
6. **`rubinstein-1989`** — "The Electronic Mail Game" is *American Economic Review* 79(3); the JSTOR id given (`1911054`) is in an Econometrica-looking range [R]. Suspect. Also, the graph's relation `rubinstein-1989 --empirically-tests--> common-knowledge` is wrong in kind: it is a theoretical paper, not an empirical test [R].
7. **Bare-bibliography count:** of the nodes I examined, the following carry no description text at all and therefore contribute nothing beyond a (sometimes wrong) citation: `aumann-1976`, `pearce-1984`, `lewis-1969`, `spence-1973`, `level-k`, `rubinstein-1989`, `plaza-2007`, `carlsson-vandamme-1993`, `signalling`, `harsanyi-1967`, `kamenica-gentzkow-2011`, `crawford-sobel-1982`, `aumann-brandenburger-1995`, `bernheim-1984`, plus most concept nodes. The pack is a reading list with unreliable metadata, and card provenance (R3) must cite verified primary sources, never these nodes.
8. **Post-cutoff nodes** (`gemini4-argon-2026`, `enterprisebench-2026`, `dbos-2026`, `lying-with-truths-2026`, `nguyen-attention-2026`): UNCHECKED; I could not verify existence. `gemini4-argon-2026` is irrelevant to both Q-A and Q-B and its inclusion by the retriever is itself evidence that the retrieval is lexical, not topical — consistent with the pack's own warning.

Bibliographic hygiene verdict: the graph's error rate on the handful of nodes I could assess from memory is high enough (≥4 suspected bad identifiers out of ~10 checked) that **no identifier from the pack should be copied into a card or the spec without independent verification**.

---

## 7. Binding terminology and citation discipline (P04-PW-4)

**Banned words/phrases in the spec and claim set:**
- "first", "novel benchmark", "new paradigm" — in any form, for anything touching DEL generation, higher-order evaluation, verifiable ground truth, or strategy retrieval (PW-K01–K05).
- "theory of mind", "recursive reasoning ability", "level-k reasoning" as descriptions of *solver behaviour* (mechanism claims; barred by the claim ceiling and by Hi-ToM-era disputes [S]). Permitted only as names of task semantics ("level-k-generated behaviour table").
- "independent verification" without qualifying *which* implementations are independent and where they share semantics (the v0 lesson; also SMCDEL-S5-executable scope limits [S]).
- "strategies improve reasoning" — replace with "the trigger-matched pack did/did not exceed controls on stratum Sx under registration <id>".

**Claims requiring a citation at point of claim:** any statement about headroom or contamination (cite ExploreToM/Ullman-line [S]); any statement that explicit modelling helps (cite AutoToM, DEL-ToM, SimToM/TimeToM, as the expectation being controlled for); any statement about retrieval-augmented reasoning (cite BoT + ReasonFlux); any use of a classic result (Aumann, Crawford-Sobel, etc.) — cite the verified primary source, not the graph node.

**Mandatory wording for the prior-work section:** "DEL-grounded generation with exact ground truth (MindGames), higher-order evaluation (Hi-ToM), adversarial program-guided generation (ExploreToM), external model-checker verification (SMCDEL; ToM-LM), and similarity-retrieved thought templates (BoT, ReasonFlux) all pre-exist this work. This mission contributes only: (i) a subfamily whose public behaviour is derived from explicit utilities and solution concepts [if PW-N01 survives verification of L04/L02], and (ii) a registered, controlled test of trigger-matched strategy packs with planted-invalid strata [if PW-N02/N03 survive a targeted search of the prompting-ablation literature]." Both conditionals must be resolved, with searches logged, before Gate 2.

**Cut for length:** detailed per-node audit of remaining pack items; discussion of (f) beyond the UNCHECKED flag; verification plan details for L02/L04/L05/L07 (one line: all four must be fetched and read before Gate 2, and PW-N01 dies or survives on L04's contents).
