# Mission 02: running the Council round

**Status (2026-10-05): all four Council roles are stored. Skeptic (P03-S) has two separate samples: `skeptic.a.md` (source-bundle label `opus 5`) and `skeptic.b.md` (label `gpt 6 luna max`); the source bundle remains at `skeptic_prompt_responses`. Each sample has an `.intake.json` sidecar. The compiler-prepared, non-decisional cross-critique is at `cross_critique.md`; it uses the current Council round only, and does not independently verify cited literature. The human chose to keep the earlier Arena dialogue in `../sources/2026-09-29_arena_round_note.md` separate from round 1. Since then, the user manually collected advisory Gate 1 review bundles at `gate01_responses_v1` and `gate01_responses_v2`; these are not Council votes or a human gate disposition. No further model opinions are requested for now. A non-decisional portfolio of multiple sharp candidate questions is prepared at `../gates/question_portfolio_draft.md`. The assistant made no Arena call. Gate 1 remains pending; Gate 2 is not reached, and no experiment is authorized.** A research-director pass the same day recommends running `../../mission-03/` first (`mission-03/DESIGN.md`, section 9).

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
3. Save each response body without rewriting it or adding a provenance header. Canonical paired files use names such as `experimentalist.a.md` / `.b.md`, `skeptic.a.md` / `.b.md`, and `prior_work_killer.a.md` / `.b.md`; a single response uses the configured unsuffixed path. Workbench intake stores provenance in a separate `.intake.json` sidecar.
4. Record only metadata actually visible or otherwise known from the Arena session. Keep a model's self-reported model name distinct from the Arena-displayed label; if tool availability is only self-reported in the answer, record that source and do not present it as independently observed. Leave absent details missing rather than guessing. See `../../runtime/WORKBENCH.md`.
5. If a session errors out or truncates, rerun it in a fresh session and keep both outputs.

## Order of events (so the record shows what was known when)

1. The seed, the retrieval view, the evidence digest and these prompts are committed first.
2. The `game`-family candidate cards were authored from the graph leads and the primary literature, and frozen (card versions and content hashes in `mission-02/freeze/`) in a later commit, **before any Council response was stored in this repository**. The Council does not see the cards in this round, so the instance-family design cannot be tuned to them.
3. Responses are stored unedited. The human kept the separate Arena dialogue (`../sources/2026-09-29_arena_round_note.md`) outside round 1; the compiler-prepared cross-critique is in `cross_critique.md`. That analysis is not Gate 1 approval; Gate 1 remains an explicit human decision.

## Material received after these prompts were written

On 2026-10-02 the user supplied an earlier dialogue and Arena round on the same topic. The compiler had not seen it when it wrote the seed, these prompts or the five `game` cards, and the prompts do not contain it. It proposes a different instance family from the one in the seed. Whether and how to bring it into the Council round is an open decision, recorded with a verification table in `../sources/2026-09-29_arena_round_note.md`.

## What this round can and cannot tell us

It collects the opinions of a few anonymous models, each told to attack the framing first. The prompts were written to avoid the leading framing that Mission 01's review found, and every role is asked to flag wording that still leads, but nothing here proves they do not. A Council response is a proposal or a critique, not evidence. Where a role cites literature without having read it, it is asked to say so, and the Prior-Work Killer is asked to verify the seed's leads and audit the evidence pack.
