# R-POST-02 pipeline — dispatch order, isolation rules, promotion

Series: *Reasoning-Atria* (campaign 03). Slot: **R-POST-02 — "Hard" does not reliably make tasks harder.**
Snapshot of record: `atria-campaign-state-62.zip` (completed campaign, 194/194 scored).

## Slot ownership

Slot IDs follow the **dispatch order** on `arena/4a683b34-epistemic-compiler`, not the order articles were written. R-POST-02 is the difficulty-dial slot as dispatched; the article that already exists for this subject is `comparison_41.md` ("Does Hard Make Tasks Harder?"), which is a source draft, not a publishable one — it undercounts the pairs, pools the guarantee buckets, and carries stale state-56 numbers (packet §9).

The floor-of-the-distribution subject went to R-POST-03 (`R-POST-03_*`), which had no distinct subject of its own.

| Slot | Subject | Existing artefact |
|---|---|---|
| R-POST-01 | Environment dominates difficulty | `comparison_40.md` (candidates) / `comparison_44.md` |
| **R-POST-02** | **"Hard" does not reliably make tasks harder** | **`comparison_41.md` → this pipeline** |
| R-POST-03 | The floor: six families that passed nothing | `R-POST-03_*` |
| R-POST-04 | The ceiling: fourteen families passed everything | `comparison_42.md` |
| R-POST-05 | FAIL carries partial credit | `comparison_43.md` |

Boundary rules: 01 claims environment family is the better coarse sorter; 02 claims the *direction* of a difficulty flip is inconsistent within families and unresolvable at this n; 04 claims some families are uniformly solved. No article may borrow another's thesis, and 02 in particular may not drift into 01's "environment dominates" framing.

## Files

| File | Stage | Role |
|---|---|---|
| `R-POST-02_packet.md` | — | authoritative evidence base; single source of truth |
| `R-POST-02_writer_A_prompt.md` | A | first independent draft |
| `R-POST-02_writer_B_prompt.md` | B | second draft, funnel structure, mandatory self-argument |
| `R-POST-02_reviewer_C_prompt.md` | C | adjudication: claims ledger, pair spot checks, spine recommendation |
| `R-POST-02_reconciler_D_prompt.md` | D | publishable article + reconciliation log |
| `R-POST-02_pipeline.md` | — | this file |

Drafts land in `campaign-03-analysis/post-production/drafts/` as `R-POST-02_A.md`, `_B.md`, `_C_review.md`, `_D_final.md`.

## Dispatch

Packet first, prompt second:

```
cat R-POST-02_packet.md R-POST-02_writer_A_prompt.md   # → Writer A session
cat R-POST-02_packet.md R-POST-02_writer_B_prompt.md   # → Writer B session, separate context
```

Run A and B in parallel and, where possible, on different model families; Stage C is only worth running if the drafts differ.

## Isolation rules

1. A and B never see each other's output, prompts, or existence beyond "a second candidate exists".
2. **Never paste a draft into the other writer's prompt.** The R-POST-01 Writer B prompt on `arena/4a683b34` quotes Writer A's entire article inside the prompt; that produced a derivative, not a second opinion.
3. Do not paste `comparison_41.md` into either writer's prompt either. It covers this slot, it is wrong in six specific ways, and a writer who reads it will inherit them.
4. C sees both drafts and the packet, with no preference and no author or model names.
5. D sees everything plus the review and may not invent evidence to break a tie.
6. Suspected contamination (a draft echoing the other's phrasing) → discard and re-dispatch rather than review.

## Dispatch log (kept outside the article)

`slot · stage · model · prompt sha256 · packet sha256 · dispatched_at · output path · output sha256`

Record the model. The series review note (`comparison_30.md`) is interpretable only because its drafts were labelled by model.

## Stage gates

| Gate | Pass condition | On failure |
|---|---|---|
| A → C | complete article, frontmatter present, pair arithmetic checkable | re-dispatch A quoting the failed constraint |
| B → C | same, plus the mandatory self-argument paragraph | re-dispatch B |
| C → D | spine named, ≥3 quoted transplants, full pair spot-check table | send C back; an adjudication without a spine cannot be reconciled |
| D → publish | D's 13-line self-check all actual values correct | return to D with the failing line only |

## Promotion to the site

Target repo `StrangeTcy/strangetcy.github.io`, path `_posts/2026-10-21-<slug>.md`.

1. Frontmatter limited to `title`, `date`, `layout: post`.
2. Byline and five epistemic fields render in order.
3. `<figure>` + `<figcaption>` present, caption carries the four outcome counts and 73; no `assets/` reference and no `<img>`.
4. Links resolve and point at public artefacts only.
5. Grep clean: `fuck`, `🫣`, `TODO`, `R-POST`, `Reasoning-Atria`, `Writer`, `runs/atria_campaign`, `seed-0`, `state-62`, `coverage.json`.
6. Add the entry to `index.md`, grouped with the campaign-03 posts, in slot order.
7. Revisions keep the date stable; the site's convention is to update the file, not re-date it.

## Standing corrections across the series

- pooled pass rates across the two judge guarantees → forbidden; report per bucket (72 → 56/16, 0.778; 122 → 75/47, 0.615);
- "five uniformly unsolvable families" → six (`gnn_message_passing` omitted);
- "the remaining 14 environments" → 13 mixed;
- "the campaign is paused at provider_error" / "193 scored" → completed, 194 scored;
- `comparison_41.md`'s "five counterintuitive, four intuitive pairs" → **11 and 7**, across **5 and 6** families;
- the `moco` 0.95 FAIL read as "essentially solved" → `trusted_score` 1.0 with a missing `moco_model.py`: a record conflict, not a near-miss;
- leftover draft debris: `some model:` header in `comparison_44.md`, `fuckingly` and `🫣` in the published Oct-3 posts.
