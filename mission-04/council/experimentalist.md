<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at "ROLE: EXPERIMENTALIST (P02-E)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-04/council/prompts/02_experimentalist_prompt.md (sha256 450e8cb2442804df47f04c284c2257e240cf36b65445309fafcf145d1f324708); response PROMPT_ID: M04-P02-E v1.
Sample:            single response; no .a/.b suffix.
Arena mode:        not supplied.
Model as shown:    no Arena-displayed label supplied. The response self-reports "GPT-5.6 Sol (may be wrong)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied independently. The response self-reports browsing yes and code execution no.
Text integrity:    response text preserved as pasted; the outer code fence was dropped. No content edits.
Order of events:   Mission 04 prompts were committed before Council responses; this Experimentalist response follows the two stored Theorist samples. No other roles' output was seen, per self-report.
-->

ROLE: EXPERIMENTALIST (P02-E)
PROMPT_ID: M04-P02-E v1
SELF-REPORTED MODEL (may be wrong): GPT-5.6 Sol
TOOLS: browsing yes; code execution no
SAW OTHER ROLES' OUTPUT: no

## 1. Kill attempt (P02-E-1)

**Freeze-blocking failure: design §3 does not define a coherent family of completed histories, so its oracle and dose-response cannot both be correct.**

Messages alternate recipients: \(m_1\) goes to Alice, \(m_2\) to Bob, \(m_3\) to Alice, etc. Therefore:

1. If \(k\) is odd, Bob can never receive \(m_k\), yet his scripted rule is “choose X iff he received \(m_k\).” He always chooses Y.
2. If \(k\) is even and Alice observes \(n<k/2\) received messages after communication ends, she knows \(m_k\) was not delivered; hence \(q=0\), not \((1-\epsilon)^{k-n'}\).
3. Only at Alice’s maximal observation \(n=k/2\) can receipt of \(m_k\) remain uncertain; absent a receipt after the cap, \(q=1-\epsilon\).
4. Alice has only \(\lceil k/2\rceil+1\) message-count observations, contradicting “\(k+2\) chain histories.”
5. “Delivered depth \(n'\) implied by \(n\)” is false: Alice may not distinguish loss of her outgoing message from delivery followed by loss of Bob’s reply.

The original electronic-mail model uses automatic exchanges and private machine counts forming a natural-number type space; it does not supply the design’s finite-prefix completion formula. [V] ,  Its equilibrium result concerns endogenous actions under almost-common knowledge, not a player predicting a scripted completion rule. [V] ,

The prompt itself leads toward this criticism: it explicitly asks whether “scripted-Bob collapses the phenomenon.” The operational contradiction above is independent of that cue.

**Smallest executable repair, S04-R1:** Alice commits after a privately certified prefix of \(d\) successful deliveries; the remaining \(k-d\) attempts occur afterward. Bob chooses X iff all remaining attempts succeed. Then

\[
q(d)=(1-\epsilon)^{k-d},\qquad
EU(X)=qG-(1-q)L,
\]

and X is uniquely optimal iff \(q>L/(G+L)\). This yields the intended cutoff but measures **scripted-partner completion-risk reasoning**, not bounded higher-order belief.

**Smallest design that answers the named S04:** add an endogenous arm in which both players’ actions are type-contingent and the oracle performs iterated elimination on an explicit finite type space. Select only observations with a unique surviving action and vary the number of elimination rounds required. Until that arm exists, H2 must be renamed “partial probability tracking,” and no “common-knowledge neglect” claim should ship.

## 2. Instance generator specification (P02-E-2)

I propose registering S04-R1 first; the original §3 generator must not be implemented.

### Formal instance

- State is G and privately known to Alice in all primary pairs.
- Before Alice commits, exactly \(d\in\{1,\ldots,k\}\) relay deliveries have succeeded.
- Each of the \(k-d\) later deliveries independently fails with probability \(\epsilon\); the sequence stops at first failure.
- Bob chooses risky action X iff all \(k\) deliveries succeed; otherwise Y.
- Alice receives \(+G\) for X/X, \(-L\) for X/Y, and 0 for choosing Y.
- Ties are excluded. The generator uses exact rational arithmetic and requires the nearest-depth margin \(|q-L/(G+L)|\ge .015\).

### Registered profiles

| Profile | Status | \(G,L,k,\epsilon\) | Threshold | Oracle cutoff \(d_{\min}\) | Depths | Base cells: depths × 3 covers |
|---|---|---:|---:|---:|---:|---:|
| S1 | seen | \(11,14,8,.10\) | .56 | 3 | 1–8 | 24 |
| S2 | seen | \(11,14,10,.10\) | .56 | 5 | 1–10 | 30 |
| S3 | seen | \(54,46,12,.20\) | .46 | 9 | 1–12 | 36 |
| U1 | unseen | \(7,18,10,.05\) | .72 | 4 | 1–10 | 30 |
| U2 | unseen | \(60,40,11,.25\) | .40 | 8 | 1–11 | 33 |
| **Total** |  |  |  |  | **49 depths** | **147** |

U1, U2 and cover 3 are frozen before the pilot and withheld from renderer tuning.

For each of 147 base cells, generate PUBLIC, CHAIN, PADDED, COMPREHENSION, BELIEF and LABEL-SWAP: \(147\times6=882\) prompts. Generate SCAFFOLD for the 72 disagreement cells:

\[
3\sum_p(d_{\min,p}-1)=3(2+4+8+3+7)=72.
\]

Thus the registered unique-prompt universe has 954 prompts. Fifteen PUBLIC-N diagnostics—one per profile-cover combination—are generated separately and used only for apparatus checks.

### Exclusions

- \(d=0\): confounds state uncertainty with delivery uncertainty.
- Exact expected-utility ties: no unique action.
- Original odd-\(k\) “Bob receives \(m_k\)” semantics: recipient mismatch.
- \(d=k\): not excluded; it is the \(q=1\) ceiling.
- Profiles whose oracle is constant across all chain depths: no cutoff information.
- Any rendered history inconsistent with \(0\le d\le k\).

### Seed rule

A frozen master seed produces a cell key from `(profile, d, cover, arm, repetition)`. Hash-sorting these keys determines queue order. Within every profile × cover × depth block, displayed label orientation is balanced by a seeded permutation, not independent coin flips. New seeds may alter order and wording variants but must preserve the exact cell multiset.

## 3. Renderer specification (P02-E-3)

### Deterministic skeleton

1. **Role and objective:** “You are Participant A. Maximize your expected points.”
2. **Payoff table:** all four action combinations, including Y’s zero payoff.
3. **Protocol:** \(k,\epsilon\), independence, stop-on-failure, commitment timing and Bob’s exact rule.
4. **Observation panel:** state and numbered relay statuses.
5. **Decision request.**
6. **Exact output contract.**

CHAIN transcript uses exactly \(k\) rows:

```text
Relay 01: CONFIRMED BEFORE YOUR COMMITMENT
...
Relay d:  CONFIRMED BEFORE YOUR COMMITMENT
Relay d+1: SCHEDULED AFTER YOUR COMMITMENT
...
Relay k:  SCHEDULED AFTER YOUR COMMITMENT
```

PUBLIC replaces the private observation with a common board entry stating G and that Bob chooses the risky action; it retains the same payoff and channel description. No condition is titled “PUBLIC,” “CHAIN,” “CONTROL” or “oracle-disagreement.”

### Requests and schemas

- Decision arms: `{"action":"X"}` or `{"action":"Y"}`.
- BELIEF: `{"p_bob_x":0.000000}`.
- COMPREHENSION:  
  `{"state":"G","confirmed":d,"remaining":k-d,"loss_probability":epsilon,"bob_condition":"..."}`.
- No worked answer example appears in any prompt.
- An optional single Markdown code fence may surround one JSON object. Anything else is a parse failure; raw output remains immutable.
- Report both all-output accuracy and action accuracy conditional on parsing. Never silently recode clear-looking prose.

### Length bands

Within a profile-depth-cover matched set, PUBLIC, CHAIN and LABEL-SWAP must differ by at most 3% in UTF-8 character count and 5% in whitespace-token count. Core prompts must fall within 1,100–1,900 characters. PADDED is deliberately 125–135% of its CHAIN counterpart; it is a cognitive-load perturbation, not falsely described as length matching. SCAFFOLD is 120–140%; BELIEF and COMPREHENSION are 90–110%.

### Pre-freeze leak checks

- **Metadata leak:** search rendered text for arm names, oracle labels, seeds, profile IDs and filenames; zero matches.
- **Answer leak:** neither \(q\), threshold, expected utility nor cutoff may appear.
- **Depth collateral leak:** every chain transcript has \(k\) rows; only intended status values change.
- **Length leak:** verify the bands above for every cell.
- **Label asymmetry:** X and Y occur equally often and in parallel positions outside the answer request; reverse displayed labels and verify oracle-label reversal.
- **Ordering leak:** balance which displayed label is listed first.
- **Cover leak:** a cover may change nouns and action labels only, not event order, information access or timing.
- **Mechanical prediction:** a bag-of-words classifier using text with formal quantities and intended delivery words masked must not predict the oracle action above 55% by cross-validation.
- **Human audit:** two blinded reviewers reconstruct \((G,L,k,\epsilon,d)\); require agreement on all fields and no disagreement about timing.
- **Publicity visibility:** delivery structure must remain visible—it is the treatment. What is forbidden is a redundant condition tag.

## 4. Oracle build and cross-check (P02-E-4)

### `oracle.py`

Use exact fractions for \(\epsilon,G,L\). Compute \(q=(1-\epsilon)^{k-d}\), then the sign of

\[
EU(X)=qG-(1-q)L.
\]

Return `X`, `Y` or `TIE`; TIE blocks generation. PUBLIC-G returns X, PUBLIC-N returns Y. LABEL-SWAP changes only the displayed label.

### `oracle_crosscheck.py`

Independently enumerate every success/failure vector for the remaining \(k-d\) attempts, terminate payoff at first failure, sum exact path probabilities and compare expected X payoff with zero. It must derive its own terminal payoffs and must not call the closed form.

**H-2 application:** the two oracles must not share transition functions, probability helpers, cutoff code, payoff-dispatch code or label-mapping code. They may share only immutable scalar input records and standard-library rational arithmetic. Renderer code must share no belief or action function with either oracle.

Run all-instance agreement over all profiles, depths, arms, covers and label orientations—not a sample. Compare \(q\), expected payoff, tie status, physical action and displayed action.

### Hardening policies

On the 147 canonical CHAIN cells:

- Always-X: \(81/147=55.10\%\).
- Always-Y: \(66/147=44.90\%\).
- Transcript-ignoring profile-majority policy: \(102/147=69.39\%\).
- Example-copying: 0% parse rate because no example exists.

On PUBLIC-G, always-X scores 100% and always-Y 0%; PUBLIC-N reverses these. A fully label-swapped set must complement literal-label policies while leaving physical-action scores unchanged.

**H-1 application:** no degenerate policy may approach a perfect total score through parser fallback, examples, constant labels or arm imbalance. Expected scores are frozen fixtures.

For seeds 0–49, rerender twice and require byte-identical prompts, metadata and order. Across distinct seeds, require identical cell multisets and permitted order/variant changes. Any nondeterminism is freeze-blocking.

## 5. Pilot design (P02-E-5)

Use 12 cells: S1 depths 1,2,3,8; S2 depths 1,4,5,10; S3 depths 1,8,9,12, balanced over covers 1–2. Run 12 fresh sessions per arm—84 episodes total. PUBLIC substitutes two PUBLIC-N cases, so always-X cannot pass the ceiling check.

- **E-ABORT01:** any analytic/enumerative oracle mismatch, tie or renderer inconsistency: stop before model calls.
- **E-ABORT02:** parse rate below 98%: stop, simplify the schema, discard all pilot data.
- **E-ABORT03:** PUBLIC accuracy below 90%, or either PUBLIC-N item answered X: stop; the apparatus lacks a ceiling.
- **E-ABORT04:** COMPREHENSION joint accuracy below 90%, or timing/remaining-count accuracy below 11/12: stop; no epistemic interpretation.
- **E-ABORT05:** SCAFFOLD lowers action accuracy by more than 25 percentage points: stop and inspect instruction interference. No scaffold benefit is not an abort.
- **E-ABORT06:** any tool invocation, chat-memory carryover or inability to open a fresh session: invalidate that episode; if over 5% are affected, stop.
- **E-ABORT07:** fewer than two oracle-X and two oracle-Y CHAIN cases survive validation: sampling bug.

Plot the pilot’s action frequency by depth, but do not tune profiles or thresholds to favor H1/H2. Only apparatus defects may trigger redesign.

## 6. Registered run design (P02-E-6)

Every episode uses a fresh chat. Record model/runtime label, system-prompt configuration if exposed, date, decoding setting, tool indicator, prompt hash, raw response and operator ID. Instruct the runtime not to use tools. Tool-using episodes form a separate nonconfirmatory stratum.

### Approximately 300 episodes: exactly 300

Choose 24 base cells:

- Four anchor depths per profile:  
  S1: 1,2,3,8; S2: 1,3,4,5; S3: 1,4,8,9;  
  U1: 1,2,3,4; U2: 1,4,7,8.
- Assign covers 1–2 by a balanced Latin schedule.
- Duplicate four formal cells in cover 3, producing four matched cover comparisons.

Run per base cell:

- PUBLIC ×3 = 72
- CHAIN ×3 = 72
- BELIEF ×2 = 48
- COMPREHENSION ×2 = 48
- PADDED ×1 = 24
- LABEL-SWAP ×1 = 24
- SCAFFOLD on 12 disagreement cells ×1 = 12

Total: **300**.

This can detect gross neglect, comprehension failure and large surface effects. It cannot reliably estimate per-cover cutoffs, small interactions, smooth dose-response shape or model-by-profile heterogeneity.

### Approximately 2,500 episodes: exactly 2,496

Use all 147 base cells:

- PUBLIC ×4 and CHAIN ×4: 1,176
- BELIEF ×2 and COMPREHENSION ×2: 588
- PADDED ×2 and LABEL-SWAP ×2: 588
- SCAFFOLD ×2 on 72 disagreement cells: 144

Total: **2,496**.

Pair repetitions by cell and seed; PADDED/LABEL pair with the first two CHAIN repetitions. Covers and label orientations are balanced within profile-depth blocks. This resolves pooled and profile-level cutoff behavior and large cover interactions, but still cannot identify internal representations or convert S04-R1 into higher-order reasoning.

## 7. Measurements and controls (P02-E-7)

- **E-M01 Parse compliance:** valid objects divided by all raw outputs; detects CF07.
- **E-M02 Action accuracy:** oracle matches/all episodes, plus conditional-on-parse accuracy; detects strategic error without hiding CF07.
- **E-M03 Neglect rate:** \(\rho=P(X\mid\text{CHAIN},\ oracle=Y)\); primary measure for H1’s behavioral direction.
- **E-M04 Paired delivery gap:** PUBLIC accuracy minus CHAIN accuracy within formal cell and repetition; addresses CF01, CF04 and CF05.
- **E-M05 Empirical cutoff:** first depth where fitted \(P(X)\ge .5\); compares behavior with \(d_{\min}\).
- **E-M06 Belief error:** Brier score \((\hat q-q)^2\) in BELIEF; separates probability computation from action selection, addressing CF02.
- **E-M07 Decision consistency:** whether an action agrees with \(\hat qG-(1-\hat q)L\); distinguishes wrong beliefs from wrong thresholds.
- **E-M08 Surface interactions:** paired changes under PADDED, LABEL-SWAP and cover changes; addresses CF01, CF03–CF05 and CF08.
- **E-M09 Repetition dispersion:** within-cell variance in X choices; quantifies CF06.
- **E-M10 Tool/session contamination:** fraction with tools, reused context or operator deviation; addresses E-CF10/E-CF11.

Controls:

- **E-CTRL01:** PUBLIC-G/PUBLIC-N verifies both output labels and basic payoff use.
- **E-CTRL02:** fixed-row matched rendering controls collateral length and depth formatting.
- **E-CTRL03:** COMPREHENSION isolates reading and counting.
- **E-CTRL04:** BELIEF isolates probability computation.
- **E-CTRL05:** LABEL-SWAP detects literal-label preference.
- **E-CTRL06:** PADDED detects cognitive-load sensitivity; it does not prove length equivalence.
- **E-CTRL07:** SCAFFOLD tests whether explicit enumeration repairs errors.
- **E-CTRL08:** unseen profiles and cover 3 test parameter and wording transfer.
- **E-CTRL09:** fresh-session and no-tool enforcement prevents manual-workflow carryover.

## 8. Analysis plan (P02-E-8)

The sole confirmatory primary statistic is pooled E-M03 over frozen disagreement cells. E-M04 and E-M05 are key secondary statistics.

Estimate \(P(X\mid d)\) separately by profile using nondecreasing isotonic regression. Define \(\tilde d\) as the smallest depth whose fitted probability is at least .5; use 1 for always-X and \(k+1\) for never-X.

Use a stratified cell-cluster bootstrap with 10,000 frozen resamples for \(\rho\), paired gaps, cutoff differences and padding effects. Resample formal cells, retaining repetitions and paired arms. Report profile and cover intervals descriptively; apply Holm correction only to the five profile-level tests. No separate significance fishing over depths.

Regime precedence:

1. Apparatus aborts.
2. O4 if validity controls fail.
3. O3 if a large padding/label effect meets its threshold.
4. O5 if capability thresholds hold.
5. O1 if neglect is high and depth-flat.
6. O2 if behavior is graded/interior.
7. Otherwise report **mixed/inconclusive**; do not force an O1–O5 label.

The operator receives a randomized prompt queue without oracle labels. Raw responses are append-only. Joining outputs to oracle labels and computing aggregates occurs only after all expected IDs are present. The human will inevitably see individual answers, but may not inspect aggregate efficacy or adapt the queue. Only predeclared apparatus aborts permit stopping.

## 9. Failure modes and abort table (P02-E-9)

| Failure | Detector | Rule |
|---|---|---|
| Parse failures silently become strategy errors | Separate E-M01 and conditional accuracy | Abort below 98%; never hand-rescue |
| Wrong timing interpretation | COMPREHENSION timing field; reviewer audit | Abort below 90% |
| Oracle boundary/float bug | Exact fractions; exhaustive checker | Any mismatch aborts |
| Odd-message recipient bug returns | Protocol invariant test | Any occurrence aborts |
| Temperature masks a curve | E-M09 and repeated cells | Salvage aggregate choice rates; no sharp cutoff claim if within-cell SD dominates between-depth change |
| Cover imbalance | Manifest count audit | Repair queue before unblinding; otherwise cover claims invalid |
| Label orientation imbalance | Block-count audit | Abort affected stratum |
| PUBLIC repeats exploit memorization | Hash/text audit | Report as ceiling only; never as independent substantive evidence |
| PADDED changes semantics | Blinded human reconstruction | Drop PADDED; H0/CF01 conclusion unavailable |
| Cover changes information access | Formal-field diff | Drop cover; transfer claim unavailable |
| Tool use | UI/log indicator | Exclude confirmatory set; report separately |
| Reused chat context | Session ID/operator log | Invalidate episode |
| Provider/model changes mid-run | Runtime/date metadata | Split strata; no pooled runtime claim |
| Missing episode or duplicate paste | Expected-ID reconciliation | Replace only with same frozen ID before unblinding |
| Manual transcription corrupts prompt | Prompt hash | Invalidate and repaste |
| Probability rounded or malformed | Range/parser check | BELIEF failure only; do not alter action score |
| Multiple surviving endogenous actions | v2 oracle survivor set | Exclude before freeze; never choose a preferred equilibrium post hoc |

## 10. Outcome-regime operations (P02-E-10)

These thresholds apply after parse \(\ge.98\), tool contamination \(\le.02\), and manifest integrity passes:

- **O1—public-like neglect:** PUBLIC and COMPREHENSION accuracy \(\ge.90\); \(\rho\ge.70\) with 95% lower bound \(>.50\); and near-boundary minus low-depth \(P(X)\) differs by at most .15. Supports H1 behaviorally only. If transfer later fails, credibility contracts to the seen templates; if validity controls fail, O1 is void.
- **O2—graded/interior response:** controls \(\ge.90\); near-boundary minus low-depth \(P(X)\ge.25\) with interval excluding zero; chain accuracy \(<.90\); and at least three profiles have an interior \(\tilde d\). In S04-R1 this supports partial probability tracking, not bounded belief iteration. A failed belief probe reduces it to unexplained depth sensitivity.
- **O3—surface sensitivity:** PADDED or LABEL-SWAP changes \(\rho\) by at least .20 and at least halves the original delivery gap, with the paired interval excluding zero. Supports H0-style prompt sensitivity. If the control changed semantics or balance, O3 is invalid rather than weakened.
- **O4—comprehension/apparatus limitation:** parsed COMPREHENSION or PUBLIC accuracy \(<.90\), while parse remains \(\ge.98\). Supports H3 and blocks epistemic claims. If the renderer audit subsequently fails, even the H3 attribution becomes a renderer diagnosis.
- **O5—capability:** overall CHAIN accuracy \(\ge.90\), unseen-profile accuracy \(\ge.85\), \(\rho\le.10\), and PADDED/LABEL-SWAP effects each \(\le.10\). This establishes robust performance on S04-R1 only. A failed novel-cover check removes transfer credibility; absence of endogenous v2 still forbids a common-knowledge capability claim.

No threshold rescues the construct mismatch: without endogenous strategic types, all outcomes concern a scripted partner’s completion probability.
