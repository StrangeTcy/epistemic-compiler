# Council round 1: intake log

The compiler's running notes on each response as it is stored: how it conforms to the required output format, which of its checkable claims were checked and how, and what it asks of the seed. This is the compiler's reading. It is not part of the Council record, and it decides nothing. The cross-critique and Gate 1 wait until all four responses are in. Responses are stored unedited as `<role>.md`, with a provenance header that is marked as not part of the response.

| Role | Stored | File | Format | Checked claims |
| :--- | :--- | :--- | :--- | :--- |
| Theorist (P01-T) | 2026-10-02 | `theorist.md` | sections 1 to 9 of 10; section 10 absent and not declared cut; 4,261 words against a 3,500 guide | the 3 claims that could be checked all hold |
| Experimentalist (P02-E) | not yet | | | |
| Skeptic (P03-S) | not yet | | | |
| Prior-Work Killer (P04-PW) | not yet | | | |

Missing for every stored response so far: the arena mode, the model name as the arena displayed it, the session time, and whether tools were present. The response's own header is self-reported and unreliable.

## Theorist (P01-T)

**Conformance.** Header lines present. Evidence tags: 19 x [R], no [V] or [S]; it says it had tools available but used none, so every external claim is recalled. Role-prefixed ids T-A01 to T-A10 and T-H0 to T-H8 minted as instructed. **Section 10 (qualitative outcome table, P01-T-10) is absent and was not listed under "cut for length"**, which names only the action-model definitions and a power estimate. About 22% over the length guide.

**Checked on 2026-10-02.**
1. The ten relations it calls dubious all exist in `knowledge/edges.yaml` (edges 004, 005, 038, 138, 166, 009, 081, 085, 086, 080). None was invented. Whether each is wrong is a literature judgment, tagged [R] and not checked.
2. A real data error: `bernheim-1984` and `pearce-1984` carry the same title ("Rationalizable Strategic Behavior") and the same JSTOR link in the graph. The importer reproduces the user's HTML export faithfully, so the fault is in the source graph and the fix belongs there, followed by a re-import. Pearce's own paper has a different title [R].
3. Its recalled claim about L01 is confirmed by the paper (read two of four chunks of the PDF, Findings of EMNLP 2023): labels come from the SMCDEL model checker (an S5 announcement logic); code and data are public; 2 to 4 agents, belief order up to 2, announcements restricted to first-order beliefs; a small trained classifier flags examples with shortcut cues, which is precedent for the Theorist's shortcut certificate.

**Not checked.** L02 (neither it nor the compiler has read it); the Hi-ToM order claim; every other [R] literature claim; the construction of SCH-1 to SCH-4 (no generator or verifier exists), including its prediction that the semi-public variant of SCH-1 typically gives "never".

**What it asks of the seed** (for Gate 1; none applied):
1. **Strata.** Define S2 from validity conditions declared independently of the cards (publicness, truthfulness, protocol, prior, incentive alignment, commitment, dominance type), then map cards onto them at Gate 2. Leave the leaking validity features undeclared in problem states, because declaring them makes S2 empty by construction.
2. **Q-A reframed.** One finite probabilistic epistemic model; level-k and rationalizability as generators of behaviour tables, not as semantics; reject belief revision and equilibrium-selection questions; keep v0 as the control subfamily.
3. **Certificates.** A depth certificate (a (k-1)-bisimilar witness model with a different answer) and a shortcut-failure certificate against a registered set of naive programs (B1 to B6).
4. **Reuse.** Use L01's generator and SMCDEL as source and verifier for the public-announcement subfamilies; build only the rest (T-H8).
5. **Controls and hypotheses.** A generic-enumeration arm (T-H3); a validity-clause warning with no method (T-H7); a scored parse of the formal spec; load crossed with depth (T-H6).
6. **Verdict.** "Do not proceed as framed", with the reframed Q-A and strata that do not depend on the cards. Its strongest argument is that H3 is close to true by construction: on a finite explicit semantics, full enumeration is always valid, so a card can only help by being a valid shortcut.

**Compiler observations** (from the five frozen cards, which the Theorist did not see and which were written independently of it):
- **Card A as written has the problem the Theorist describes.** Its trigger feature `public_events_change_what_agents_know` already says events are "available to all agents", and its exclusion is the negation. A semi-public instance fires the exclusion or fails the trigger. It does not sit as "trigger present, move invalid".
- **Convergence.** Six of the Theorist's nine declared validity conditions have a matching obligation in a frozen card: publicness, truthfulness and protocol (card A, OB3, OB4, XC1), knowledge versus belief (B, OB1), policy status (C OB1, E OB1), dominance type (D, OB3, OB4). The three with no card are the common prior, incentive alignment and commitment, which are exactly the agreement, signalling and persuasion cards the library lacks.
- One voice, not corroboration: the Theorist's doubts about Q-B's design are consistent with the case in `mission-03/DESIGN.md` for testing the Strategy IR's central claim on existing tasks first.

**Open.** The other three responses; the arena metadata; the Pearce/Bernheim correction in the source graph.
