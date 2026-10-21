# R-POST-03 pipeline — dispatch order, isolation rules, promotion

Series: *Reasoning-Atria* (campaign 03). Slot: **R-POST-03 — a zero-pass-rate family is not a capability verdict**.
Snapshot of record: `atria-campaign-state-62.zip` (completed campaign, 194/194 scored).

## Why this slot exists

Slot IDs follow the dispatch order on `arena/4a683b34-epistemic-compiler`, not the order the articles were written.

- **R-POST-02** is the difficulty-dial slot, as dispatched ("Hard" does not reliably make tasks harder), with its own pipeline in `R-POST-02_*`. Its source draft is `comparison_41.md`.
- **R-POST-03** had no distinct subject of its own: its prompts duplicated R-POST-02's dispatch and were deleted as "redundant" while its article stayed. It is therefore re-slotted onto the campaign's floor — the six families that passed nothing — which is the mirror of R-POST-04's ceiling.

The series now reads:

| Slot | Subject | Article |
|---|---|---|
| R-POST-01 | Environment dominates difficulty | `comparison_40.md` (candidates) / `comparison_44.md` |
| R-POST-02 | The difficulty dial does not turn one way | `comparison_41.md` → `R-POST-02_*` pipeline |
| **R-POST-03** | **The floor: six families that passed nothing** | **this pipeline** |
| R-POST-04 | The ceiling: fourteen families passed everything | `comparison_42.md` |
| R-POST-05 | FAIL carries partial credit | `comparison_43.md` |

R-POST-03 and R-POST-04 are deliberately mirrors: 35 cases at the floor, 84 at the ceiling, each with its guarantee composition stated. Neither may borrow the other's claim. R-POST-02 and R-POST-01 must not swap their theses either: 01 is about environment family predicting outcomes, 02 is about the direction of a difficulty flip staying inconsistent within families.

## Files

| File | Stage | Role |
|---|---|---|
| `R-POST-03_packet.md` | — | authoritative evidence base; single source of truth |
| `R-POST-03_writer_A_prompt.md` | A | first independent draft |
| `R-POST-03_writer_B_prompt.md` | B | second independent draft, different structural mandate |
| `R-POST-03_reviewer_C_prompt.md` | C | adjudication: claims ledger, spot checks, spine recommendation |
| `R-POST-03_reconciler_D_prompt.md` | D | publishable article + reconciliation log |
| `R-POST-03_pipeline.md` | — | this file |

Drafts land in `campaign-03-analysis/post-production/drafts/` as `R-POST-03_A.md`, `R-POST-03_B.md`, `R-POST-03_C_review.md`, `R-POST-03_D_final.md`.

## Dispatch

Each stage is dispatched as **packet + prompt**, in that order:

```
cat R-POST-03_packet.md R-POST-03_writer_A_prompt.md   # → Writer A session
cat R-POST-03_packet.md R-POST-03_writer_B_prompt.md   # → Writer B session, separate context
```

Use different model families for A and B where possible; the value of Stage C depends on the drafts differing. Stages A and B may run in parallel.

## Isolation rules

1. Writer A and Writer B never see each other's output, prompts, or existence beyond "a second candidate exists".
2. **Never paste a draft into the other writer's prompt.** The R-POST-01 Writer B prompt on `arena/4a683b34` quoted Writer A's entire article inside the prompt; that instrument produced a derivative, not a second opinion.
3. The reviewer sees both drafts and the packet, and nothing else — no preference, no author names, no model names.
4. The reconciler sees everything plus the review, and may not invent evidence to break a tie.
5. If contamination is suspected (a draft echoing the other's phrasing), discard and re-dispatch rather than review.

## Dispatch log (one row per stage, kept outside the article)

`slot · stage · model · prompt sha256 · packet sha256 · dispatched_at · output path · output sha256`

Record the model. The series' review note (`comparison_30.md`) shows why: a review of "grok 4.5" and "gemini 3.1 pro grounding" drafts was only interpretable because the drafts were labelled.

## Stage gates

| Gate | Pass condition | On failure |
|---|---|---|
| A → C | article complete, frontmatter present, self-contained | re-dispatch A with the failed constraint quoted |
| B → C | same, plus the mandatory self-argument paragraph | re-dispatch B |
| C → D | review contains a spine, ≥3 quoted transplants, and a full spot-check table | send C back; an adjudication without transplants cannot be reconciled |
| D → publish | D's 12-line self-check all `actual value` entries correct | return to D with the failing line |

## Promotion to the site

Target repo `StrangeTcy/strangetcy.github.io`, path `_posts/2026-10-21-<slug>.md`.

Checklist:

1. Frontmatter only `title`, `date`, `layout: post`.
2. Byline and five epistemic fields render, in order.
3. `<figure>` + `<figcaption>` present; caption states counts and total; no `assets/` reference and no `<img>`.
4. Links resolve and point at public artefacts only.
5. Grep clean: `fuck`, `🫣`, `TODO`, `R-POST`, `Reasoning-Atria`, `Writer`, `runs/atria_campaign`, `seed-0`, `state-62`, `coverage.json`.
6. Add the entry to `index.md`, grouped with the other campaign-03 posts, in slot order.
7. If the post is later revised, keep its date stable; the site's convention is to update the file, not to re-date it.

## Standing corrections for the whole series

These are inherited from the prior drafts and must not reappear in any campaign-03 post:

- "five uniformly unsolvable families" → **six** (`gnn_message_passing` was omitted);
- "the remaining 14 environments" → **13** mixed;
- "near-zero scores" → the range inside the zero families is 0.0000–0.9500;
- "the campaign is paused at provider_error" / "193 scored" → state-62 completed with 194;
- the pooled 0.726-vs-0.650 easy/hard comparison → cross-bucket; per bucket it is 0.808/0.761 and 0.681/0.573, and it belongs to R-POST-03;
- the `moco` 0.95 row read as "essentially solved" → the record shows `trusted_score` 1.0 with a missing `moco_model.py`, which is a conflict, not a near-miss;
- leftover draft debris (`some model:` header in `comparison_44.md`, `fuckingly` and `🫣` in the published posts).
