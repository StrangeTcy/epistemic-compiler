<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the first "ROLE: PRIOR-WORK KILLER (P04-PW)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-04/council/prompts/04_prior_work_killer_prompt.md (sha256 95cc07caeccefdc298ad4491968e9b1650e37b2a9cf65bb90fb24d4f85139f86); response PROMPT_ID: M04-P04-PW v1.
Sample:            single response; no .a/.b suffix.
Arena mode:        not supplied.
Model as shown:    user-supplied prefix "fable 5.1"; not independently confirmed as the Arena UI label. The response self-reports "Claude (Anthropic)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied independently. The response self-reports browsing yes (five web searches, snippets/abstracts only; no full-text fetch) and code execution no.
Text integrity:    response text preserved as pasted, including the initial pre-writing narration, repeated role header, and source's literal HTML entities. The user's model-label prefix and outer code fence were omitted. No content edits.
Order of events:   Mission 04 prompts were committed before Council responses. This response follows the two Theorist samples, Experimentalist, and Skeptic; no other roles' output was seen, per self-report.
-->

ROLE: PRIOR-WORK KILLER (P04-PW)  
PROMPT_ID: M04-P04-PW v1  
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic)  
TOOLS: browsing yes (web search, snippets/abstracts only; no full-text fetch); code execution no  
SAW OTHER ROLES' OUTPUT: no  
  
Before writing, I am running the searches the prompt requires.ROLE: PRIOR-WORK KILLER (P04-PW)  
PROMPT_ID: M04-P04-PW v1  
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic)  
TOOLS: browsing yes (5 web searches, snippet-level only, no full-text retrieval); code execution no  
SAW OTHER ROLES' OUTPUT: no  
  
Search budget note: I had five searches. Three of the six required search targets were covered (email-game/common-knowledge on LLMs; public-vs-private in LLM strategic benchmarks; global games with LMs; shared-vs-common knowledge coordination). Two were NOT searched for budget reasons: coordination-under-communication-loss benchmarks, and 2026 industry-track delivery-structure artifacts. The email-game query returned only patents and email-tool marketing (no hit), so "nothing found" there is weak evidence.  
  
Prompt-leading flags: (i) the prompt's sentence "a game-playing battery is not the same contribution as a delivery-structure manipulation with an exact oracle" pre-states the wedge design §9 wants me to find; I treat it as a hypothesis to attack. (ii) The seed's `relevant_prior_work` contains only LLM game batteries and ToM-QA; it omits the entire experimental-economics and cognitive-science literature on shared-vs-common knowledge, which is where the actual collision lives. (iii) The claim ceiling and prompt §2 contain the word "fuckingly"; I read it as a text artifact, not an instruction.  
  
## 1. Verdicts (P04-PW-1)  
  
**Strongest reason not to proceed as framed.** The phenomenon S04 names "common-knowledge neglect" is already an established finding in humans and already reported in LLMs. Bolander, Engelhardt and Nicolet ran three separate experiments investigating to which degree human participants (N=802) are able to recognize the difference between common knowledge and nth-order shared knowledge, using a new two-person coordination game with imperfect information, and found that participants have a very hard time accepting the fact that common knowledge is not reducible to shared knowledge; instead, participants try to coordinate even at the shallowest depths of shared knowledge and in spite of huge payoff penalties [S]. That is H1, with a dose-response over depth, with payoff penalties, six years ago. On the LLM side, a 2026 preprint (Rocca, Boukortt, Keeling, Street, arXiv:2607.11363) introduces EAST, a two-player dialogue game in which pairs of models must independently settle on the same semantic Schelling point while each side has carefully controlled private versus shared knowledge, and reports that only frontier models handle the full range of epistemic conditions, and most failures come from specific tracking errors such as treating private information as if it were mutual [S]. "Treating private information as if it were mutual" is the seed's headline hypothesis, in LLMs, in print. S04 is therefore not discovering a phenomenon; at best it is building a parametric, oracle-graded instrument for a known one, and its title, intuition and §1 "under-tested contrast" wording must change.  
  
Second reason (internal, reinforced by prior work): design §3 admits that with Bob's rule fixed, v1 is "strategic-uncertainty reasoning about Bob's information, not unbounded belief iteration." That means v1 measures a first-order probability-threshold decision (compute (1−ε)^{k−n′}, compare with L/(G+L)), not common knowledge. The prior-work collision for v1 is then with LLM probabilistic/threshold reasoning studies, not with epistemic game theory; and the name "common-knowledge neglect" is unearned until v2 runs.  
  
Verdicts:  
- **Mission overall: REFRAME.** Proceed only as "a parametric lossy-chain instrument that replicates and quantifies a known shared-vs-common-knowledge conflation in LLMs," with Bolander et al. and EAST cited as precedents in the first paragraph.  
- **(a) Phenomenon as new LLM evaluation object: REFRAME → "replication-and-quantification object."** Killed as "new" by EAST [S] and, as a hypothesis, by Bolander et al. [S] and Thomas et al. (PNAS 2019), whose experiments manipulate whether participants receive information that generates private, shared, or common knowledge, and reveal that people are sensitive to the difference [S].  
- **(b) Public-vs-chain manipulation with facts held fixed: PROCEED, cite-and-distinguish.** The private/shared/common manipulation with facts fixed is standard in the human literature; EAST does controlled private-vs-shared in LLMs. What I did not find is a sampled-depth, lossy (ε) chain with a public-announcement arm in LLMs.  
- **(c) Exact deterministic oracle as primary verdict: PROCEED, but strike any novelty wording.** Oracles are routine in this literature; the MathAI 2026 battery evaluates against benchmark-optimal strategies across complete and incomplete-information games [S], and Bolander et al.'s game necessarily has a normative solution. The S04 oracle is a three-line closed form; its value is hygiene, not contribution.  
- **(d) Dose-response depth design: PROCEED, not novel.** Bolander et al. vary nth-order depth in humans [S]; Thomas et al. report that people's decision to help zigzagged with the depth of their asymmetric, recursive knowledge [S]; Hi-ToM varies ToM order in LLM QA [V-inherited]. Novel only as the (k, ε, payoff) three-parameter cutoff family in LLMs.  
- **(e) Claim ceiling as written: REFRAME.** Add: "not the first demonstration of private/shared-vs-common conflation in humans or LLMs"; add: "v1 measures decision under first-order strategic uncertainty with a scripted partner; it does not measure higher-order iteration." Remove "common-knowledge neglect" as the name of the v1 finding.  
  
## 2. Collision matrix (P04-PW-2)  
  
| ID | Citation | Checked | Contribution-level overlap with S04 | Remaining gap |  
|---|---|---|---|---|  
| L01 | Rubinstein 1989, Electronic Mail Game | [S] via secondary: a 2026 theory paper states the basic lesson of this literature is that arbitrarily precise private information need not induce coordination because equilibrium behavior also hinges on higher-order beliefs (Rubinstein, 1989) | Mechanism only; no LLM content. Seed's characterization consistent with snippet. | None claimed; fine. But note graph edge 081 labels it "empirically-tests", which is wrong (theory paper) [R]. |  
| L02 | Baltag, Moss, Solecki 1998 | UNCHECKED (pack DOI looks like an *Artificial Intelligence* journal DOI; I recall BMS 1998 as a TARK proceedings paper [R]; flag as possibly mismatched) | Semantics only. | None. |  
| L03 | LLM-Coordination, Findings NAACL 2025 | UNCHECKED this session | Per seed [S]: no delivery manipulation. | Unverified by me. |  
| L04 | TMGBench; "Strategic Reasoning in LLMs" MathAI 2026; GameBench; GTBench | [S] partial: the openreview id 3SIgzUk0Yd resolves to a MathAI 2026 paper whose evaluation combines task-level correctness with rubric-based scoring on two public dimensions: DQ and RQ, aggregated into the SRI; TMGBench is a separate artifact (arXiv:2410.10479) [S] | Play-quality batteries; no delivery contrast. Seed's description holds. | **Identifier fault:** L04 attaches the MathAI openreview URL to TMGBench; they are different papers. |  
| L05 | MultiAgent-Bench; Communication Enables Cooperation; elimination_game | UNCHECKED this session | Per seed. | Unverified by me. |  
| L06 | MindGames (EMNLP 2023), Hi-ToM | [V-inherited]; not re-checked | QA, not decisions. | **Name collision:** a 2026 preprint "MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs" (arXiv:2605.29512) exists [S] and discusses information leakage → private/public reasoning separation; the write-up must disambiguate. |  
| L07 | Carlsson &amp; van Damme 1993; "Morris &amp; Robins"; Aumann 1976 | [S] for C&amp;vD as cited in 2607.28821; "Morris &amp; Robins" UNCHECKED and likely a wrong name — the standard global-games citation is Morris &amp; Shin (snippet cites Carlsson and van Damme, 1993; Morris and Shin, 2003) | Mechanism backup. | Fix the citation. |  
| **PW-L08** | Bolander, Engelhardt, Nicolet, "The Curse of Shared Knowledge" (arXiv:2008.08849, 2020) | [S] | **High.** Same hypothesis (shared ≠ common; agents coordinate at shallow depth despite penalties), same two-player imperfect-information coordination game form, depth-graded, N=802 humans. Crucially the design notes the game has a similar underlying mathematical structure as the example just given, but cast in a simpler, more everyday-like setting, where the higher-order uncertainty is established already when the game is initialised and not, as above, through a series of message passings — i.e. it already solves CF01 (length confound) by construction. | Not LLMs. No ε-lossy chain. Lead author is a DEL researcher; an exact DEL oracle is almost certainly available in the paper [R]. |  
| **PW-L09** | Rocca, Boukortt, Keeling, Street, "Beyond Sally-Anne: Evaluating ToM in LLMs using Epistemic Schelling Points" (arXiv:2607.11363, 2026) | [S] | **High.** LLMs; controlled private vs shared knowledge; failure mode "treating private information as if it were mutual." Also argues standard text-based Theory of Mind tests for large language models are too easily gamed by training data, which is S04's CF03 argument. | Schelling (focal-point) game, not payoff-threshold; dialogue between two models (partner confounded, cf. seed's objection to L05); no depth parameter, no lossy chain, no padding control, oracle is "normative outcome" not Bayesian cutoff. |  
| **PW-L10** | Thomas, De Freitas, DeScioli, Pinker, PNAS 2019, "Common knowledge, coordination, and strategic mentalizing" | [S] | Medium-high at hypothesis level: private/shared/common manipulation with facts fixed; depth zigzag in volunteer's dilemma. | Humans; vignette designs. |  
| **PW-L11** | "You better play 7: mutual versus common knowledge of advice in a weak-link experiment" (Synthese, c. 2012) | [S] | Medium: manipulates mutual knowledge of level 1, level 2 and common knowledge of advice; reports that contrary to our hypothesis, mutual knowledge of level 2 induces, under suitable conditions, successful coordination more frequently than common knowledge. | Humans. Relevant because it shows the H1 direction is not guaranteed even in humans—the design should pre-register a two-sided test. |  
| **PW-L12** | Global-games experiments (snippet, likely Heinemann–Nagel–Ockenfels 2004 [R] for attribution) | [S] content, [R] attribution | Medium: comparing sessions with common and private information, we observe only small differences in behavior. For common information, subjects coordinate on threshold strategies that deviate from the global game solution towards the payoff-dominant equilibrium. | Humans; but this is the exact "public vs private, facts fixed" contrast, and the null-ish human result is a prior for H0. |  
| **PW-L13** | Workshop proposal, Proceedings of 2nd Workshop on Advancing AI through ToM (arXiv:2603.18786, 2026) | [S] | Low-medium: proposes to model common knowledge as a group-level epistemic state in which all agents know a proposition p, know that others know p, and so on for LLM agents, operationalized by parsing messages. | Proposal only; no oracle; different method. Signals a crowded 2026 space. |  
| **PW-L14** | Akata et al., Nature Human Behaviour 2025 | [S] | Topical only: LLMs perform well in self-interested games such as the iterated Prisoner's Dilemma but struggle in games that require coordination. | No epistemic manipulation. Cite as context. |  
| **PW-L15** | "Tacit Coordination of LLMs" (arXiv:2601.22184) | [S] | Topical: focal points; LLMs have a remarkable capability to coordinate and often outperform humans, yet fail on common-sense coordination that involves numbers. | The "numbers" failure is a CF02 warning. |  
  
Searched and found nothing: (1) any LLM run of the electronic mail game or consecutive-numbers/coordinated-attack game (query returned noise; weak null); (2) global-games or p-dominance experiments with LMs (returned Akata et al., tacit coordination; none specific). Not searched: communication-loss coordination benchmarks; 2026 industry-track delivery-structure artifacts.  
  
## 3. Killed claims (P04-PW-3)  
  
- **PW-K01** — Implicit claim (seed title, intuition "under-tested contrast", design §1 "Selected phenomenon") that testing whether agents treat finite shared knowledge as common knowledge is new. Killed by PW-L08 (humans, depth-graded, payoff penalties) and PW-L09 (LLMs, "private as if mutual").  
- **PW-K02** — Design §1/§9 and `why_it_might_be_true` item 3: "no benchmark found that manipulates delivery structure with facts held fixed." Killed in its general form by PW-L09 (controlled private vs shared knowledge in LLMs) and PW-L10/L12 (humans). Survives only as "no LLM benchmark with a lossy sampled-depth chain vs public announcement."  
- **PW-K03** — Any suggestion (design §9 "surviving wedge") that an exact oracle on the primary outcome is part of the contribution. Killed: incomplete-information batteries already score against benchmark-optimal strategies (L04 MathAI 2026 [S]); human shared-vs-common games carry normative solutions (PW-L08, L10). The oracle is required hygiene.  
- **PW-K04** — Any suggestion that depth dose-response is novel. Killed by PW-L08 (nth-order depth, humans), PW-L10 (depth zigzag), Hi-ToM (order depth, LLMs, [V-inherited]).  
- **PW-K05** — `why_it_might_be_true` item 3's inference "benchmarks never manipulate delivery … so no training pressure selects for the distinction." Killed twice: the premise is false (PW-L09), and benchmarks are not training pressure; the inference is a non sequitur independent of prior work.  
- **PW-K06** — Calling the v1 measurement "common-knowledge neglect." Killed by the design's own §3 limitation plus PW-L08's distinction: with Bob's rule fixed, v1 is a first-order threshold decision; the shared-vs-common distinction is only tested in the deferred v2.  
- **PW-K07** — L07's "Morris &amp; Robins." No such global-games citation found; snippets cite Morris &amp; Shin [S]. Replace or justify.  
- **PW-K08** — L04's identifier: openreview 3SIgzUk0Yd is the MathAI 2026 "Strategic Reasoning in LLMs" paper, not TMGBench [S]. Split the entry.  
- **PW-K09** — The implicit one-directional prior that models will err toward the public policy. PW-L11 (level-2 mutual knowledge beat common knowledge in humans) and PW-L12 (small public/private differences in global-games sessions) show the human literature is mixed; H1's direction must be a two-sided registered test, and H0 should be given a human-literature prior rather than treated as a surface-artifact story only.  
  
## 4. Surviving novelty wedges (P04-PW-4)  
  
- **PW-N01** — Parametric lossy-chain delivery manipulation in LLMs: public announcement vs CHAIN(k, ε, h), exhaustive instance space, closed-form Bayesian cutoff n*(P,k,ε), estimated empirical cutoff ñ vs n*. Not found. **Dies if:** any paper runs Rubinstein's email game, the coordinated-attack problem, or Bolander et al.'s game on LLMs with graded depth (my email-game search was noisy; a second targeted search by the author is mandatory before registration).  
- **PW-N02** — Length-matched PADDED control separating transcript length from epistemic depth in an LLM epistemic task. Not found in PW-L09 snippets. **Dies if:** EAST or a follow-up includes a length control, or if the mission adopts Bolander's initialization-encoded construction (then the control is unnecessary, which is a better outcome).  
- **PW-N03** — Discrimination of H1 (step to public policy) vs H2 (graded depth) in LLMs by dose-response shape. Bolander et al. did this for humans (shallow-depth coordination); not found for LLMs. **Dies if:** PW-L09's full text reports depth-graded results, or a Hi-ToM-style decision variant exists.  
- **PW-N04** — v2 endogenous game with iterated-dominance oracle over a finite type space, as an LLM decision task. Not found. This is the only part that tests common knowledge proper; it should be promoted from "held out" to the primary target if the mission wants to keep its title. **Dies if:** an LLM replication of PW-L08's game exists (same search obligation as PW-N01).  
  
Honest summary: nothing survives at the level of "phenomenon." What survives is an instrument: three parameters, an exact cutoff, paired arms, and an LLM population. That is publishable as a measurement contribution only if framed as replicating PW-L08/PW-L09 and extending them with a quantitative cutoff.  
  
## 5. Reuse list (P04-PW-5)  
  
- **PW-L08 (Bolander et al.)** — *Reuse the game construction* as cover story 3 or as the v2 construction: higher-order uncertainty encoded at initialization rather than via message passing removes CF01 structurally. *Cite* as the human baseline (N=802) the LLM result must be compared against. Request the paper's normative solution to cross-check `oracle_crosscheck.py` against an independent implementation (the Mission 01 lesson about shared code paths applies).  
- **PW-L09 (EAST)** — *Cite-and-distinguish*: Schelling game vs payoff-threshold game; two live models vs scripted partner; no depth. *Reuse* its failure taxonomy ("treating private information as if mutual" and similar tracking errors) as the registered coding scheme for the tertiary `reason` field, so S04's qualitative evidence is comparable.  
- **PW-L10 (Thomas et al.)** — *Cite-and-distinguish*; its volunteer's-dilemma depth zigzag is a candidate for a non-monotone oracle variant that would be hard to pass by heuristic.  
- **PW-L11, PW-L12** — *Cite* as the reason H1 is two-sided and H0 has a human prior.  
- **Hi-ToM / MindGames (L06)** — *Reuse* the question format for COMPREHENSION and BELIEF arms rather than inventing one.  
- **L04 batteries, PW-L14, PW-L15** — *Cite* only; PW-L15's "fails on numbers" supports keeping the CF02 gate strict.  
- **MINDGAMES Live Arena (2026)** — do not reuse; *disambiguate* from MindGames 2023 in every citation.  
  
## 6. Evidence-pack audit (P04-PW-6)  
  
- **Retrieval relevance.** The lexical retrieval returned ~30 nodes; roughly two-thirds (watermarking drift, SRE agents, Gemini 4 Argon, SAFA, dots appendix, Terminal-Bench-Science, OpenShell, LongHarness, StateTape, SINGED, PrivacySkills, EnterpriseBench) have no bearing on S04. The seed's own anchors **aumann-1976 and lewis-1969 were not retrieved**, nor were **edges 002, 076, 207**. I cannot audit them; the seed cites them as if present.  
- **Duplicate link.** Edges 003 `rubinstein-1989 formalizes common-knowledge`) and 081 `rubinstein-1989 empirically-tests common-knowledge`) connect the same pair with incompatible labels. 081 is wrong: Rubinstein 1989 is a theoretical paper [R; consistent with PW-L08/2607.28821 snippets treating it as a theoretical lesson]. The seed's intuition quotes the 081 label approvingly. This is the mission-02 duplicate-link pattern affecting S04 directly.  
- **Edge 008** `aumann-brandenburger-1995 formalizes common-knowledge`): imprecise. Aumann &amp; Brandenburger 1995 gives epistemic conditions for Nash equilibrium (the node title says so); the formalization of common knowledge is Aumann 1976, whose node is missing from the pack.  
- **Edge 164** `dynamic-epistemic-logic connects common-knowledge`): vacuous relation label; harmless.  
- **baltag-moss-solecki-1998 DOI** `10.1016/S0004-3702(98)00035-1`: an Elsevier *Artificial Intelligence* DOI pattern; I recall BMS 1998 as TARK proceedings [R]. Flag as unverified and plausibly mismatched; the design should not cite the DOI without resolving it.  
- **rubinstein-1989** node carries no annotation; JSTOR id unverified. Fine as a lead.  
- **Seed-side identifier faults** (not graph): L04 URL/title conflation (PW-K08); L07 "Morris &amp; Robins" (PW-K07); L06 name collision with the 2026 MINDGAMES arena.  
- Net effect: none of the graph faults changes the mechanism; all of them would embarrass a write-up that cites graph edges as evidence. Cite primary papers, never edge ids.  
  
## 7. Binding terminology and citation discipline (P04-PW-7)  
  
Words not to use without qualification:  
- **"common knowledge" / "common-knowledge neglect"** — for v1 say "finite-order shared knowledge" or "strategic uncertainty about the partner's information under a scripted partner rule"; reserve "common knowledge" for v2 with the iterated-dominance oracle.  
- **"knows" / "represents" / "neglect"** — behavioural measurements only; "neglect" implies a representational deficit. Prefer "public-policy adoption rate ρ."  
- **"first" / "novel" / "under-tested"** — banned; PW-L08, L09, L10 exist.  
- **"exact oracle"** — say "closed-form oracle under the registered solution concept and the stated partner rule"; it is exact relative to assumptions, and it is hygiene, not contribution.  
- **"delivery structure"** — acceptable, but define it as the (public vs chain) arm variable, not as a general construct.  
- **"MindGames"** — always with year/venue.  
  
Required prior-work sentence (or equivalent) in the eventual write-up:  
"The conflation of finite-order shared knowledge with common knowledge has been demonstrated behaviourally in humans (Thomas et al., PNAS 2019; Bolander, Engelhardt &amp; Nicolet, 2020, N=802 in a depth-graded coordination game) and reported for LLMs as 'treating private information as if it were mutual' in a Schelling-point task (Rocca et al., 2026); mixed human results exist (weak-link advice and global-games experiments). This work does not claim the phenomenon; it contributes a parametric lossy-chain instrument with a closed-form Bayesian cutoff and a length-matched control, and reports whether tested runtimes show a graded or step-shaped departure from that cutoff."  
  
What would change without browsing: PW-L08 through PW-L15 would all be [R] or unknown; I could not have cited EAST at all (post-cutoff for me). The mission-level verdict would weaken from "REFRAME: phenomenon already published" to "REFRAME on internal grounds (v1 does not test common knowledge; novelty unverifiable)." Verdicts (c) and (d) would be unchanged. The audit findings in §6 are mostly internal to the pack and would stand.  
  
Cut for length: a fuller treatment of L03/L05 (unchecked), and the two unsearched targets (communication-loss benchmarks; 2026 industry-track artifacts) — both must be searched before Gate 2.
