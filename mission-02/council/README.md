# Mission 02: running the Council round

**Status (2026-10-02): prompts are ready; nothing has been run. No Council response exists yet.**

Mission 02 asks two linked questions (see `../seed.yaml`): Q-A, what a higher-order epistemic-game instance family needs so that its ground truth is independently checkable; and Q-B, whether trigger-matched strategy packs improve solving, with the comparison's design constraints registered in the seed. Mission 01 is frozen and is not reopened.

## What to paste

Each file in `prompts/` is the complete prompt for one role. Open it, select all, paste into a **fresh arena session**. Add nothing and remove nothing. Each is about 46 KB.

| Role | File | Bytes | SHA-256 (first 16) |
| --- | --- | ---: | --- |
| Theorist (P01-T) | `prompts/01_theorist_prompt.md` | 47,532 | `f668ecf81a355a52` |
| Experimentalist (P02-E) | `prompts/02_experimentalist_prompt.md` | 47,451 | `469513786cd8a664` |
| Skeptic (P03-S) | `prompts/03_skeptic_prompt.md` | 46,112 | `7b89da36787d1c10` |
| Prior-Work Killer (P04-PW) | `prompts/04_prior_work_killer_prompt.md` | 46,712 | `7eb7a445d9a51f92` |

Full hashes (so a saved response can be tied to the exact text it answered):

```text
f668ecf81a355a52c73daae656e88605fb9f5777d3ec1292b31e0c9ebcccc6f0  prompts/01_theorist_prompt.md
469513786cd8a664163b1b98a924ecaffbc2ea6314fc9c976812618fe575dd0e  prompts/02_experimentalist_prompt.md
7b89da36787d1c10dc8c082921d44cbf10d4b7f2c236233dfc43c98cf0bb1a90  prompts/03_skeptic_prompt.md
7eb7a445d9a51f929fbe3532bbebb84c29eaaa2fbdc736a64a58f3340d98805b  prompts/04_prior_work_killer_prompt.md
```

## Rules for the round

1. One fresh session per role. Never show one role's answer to another role's session, and paste nothing else into a session.
2. If the arena shows two answers side by side, **save both**. They are two independent samples of the Council, which is useful; the vote is not a result. Note which models they turned out to be.
3. Save each answer unedited as `mission-02/council/<role>.md` (`theorist`, `experimentalist`, `skeptic`, `prior_work_killer`; with `.a` / `.b` before `.md` if there are two), or paste them into the chat and the compiler agent will store them verbatim.
4. At the top of each saved answer, add a few lines of your own: arena mode (battle or direct), the model name as the arena displays it, date and time, and whether the session had browsing or code execution. The model's self-reported name in its header is not reliable.
5. If a session errors out or truncates, rerun it in a fresh session and keep both outputs.

## Order of events (so the record shows what was known when)

1. The seed, the retrieval view, the evidence digest and these prompts are committed first.
2. The `game`-family candidate cards are authored from the graph leads and the primary literature, and frozen (card versions and content hashes in `mission-02/freeze/`) in a later commit, **before any Council response is stored in this repository**. The Council does not see the cards in this round, so the instance-family design cannot be tuned to them.
3. Responses are then stored unedited, and the cross-critique and Gate 1 follow.

## Material received after these prompts were written

On 2026-10-02 the user supplied an earlier dialogue and Arena round on the same topic. The compiler had not seen it when it wrote the seed, these prompts or the five `game` cards, and the prompts do not contain it. It proposes a different instance family from the one in the seed. Whether and how to bring it into the Council round is an open decision, recorded with a verification table in `../sources/2026-09-29_arena_round_note.md`.

## What this round can and cannot tell us

It collects the opinions of a few anonymous models, each told to attack the framing first. The prompts were written to avoid the leading framing that Mission 01's review found, and every role is asked to flag wording that still leads, but nothing here proves they do not. A Council response is a proposal or a critique, not evidence. Where a role cites literature without having read it, it is asked to say so, and the Prior-Work Killer is asked to verify the seed's leads and audit the evidence pack.
