# Atria source resolution

Checked 2026-10-28. This memo records a source identity error in the existing writer handoffs. No campaign was run, and no existing post or handoff was changed.

## Finding

The six writer handoffs covering the newer four-post series call their dataset **Reasoning-Atria**, but every handoff names `atria_covering_campaign` and manifest `c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d`. Their 194-recorded / 131-PASS / 62-FAIL / one-paused accounting matches **`atria-campaign-state-56.zip`**, an earlier snapshot of the ordinary Atria covering campaign.

This is not merely a disagreement between old and new post plans. Two different campaigns have been mixed, and the ordinary-Atria snapshot used in the handoffs was itself superseded by a completed snapshot already in the repository.

## The three distinct records

| Field | Ordinary Atria: snapshot 56 | Ordinary Atria: snapshot 62 | Reasoning Atria pairwise |
|---|---|---|---|
| Archive | `atria-campaign-state-56.zip` | `atria-campaign-state-62.zip` | `reasoning-atria-pairwise-state-39028365163.zip` |
| Event | `atria_covering_campaign` | `atria_covering_campaign` | `reasoning_atria_pairwise_campaign` |
| Requested/resolved model | `Atria-Dawn-Preview` | `Atria-Dawn-Preview` | `Atria-Dawn-Preview` |
| Reasoning configuration | Same covering-campaign identity; the later snapshot's compatibility record says `provider_default_uncontrolled` | `compatibility.json`: `reasoning_mode = provider_default_uncontrolled`; episode `request_extra = {}` | `campaign_intent.json` and episode manifest: `wire_api = responses`, `reasoning_effort = high` |
| Case manifest SHA-256 | `c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d` | `c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d` | `67a19386845861e8971ea57efc663be5e88e853631da0dd702f8aba969670e3f` |
| Status | `paused`, `provider_error`, resumable | `completed`, no pause reason, not resumable | `paused`, `max_tokens_total`, not resumable |
| Recorded | 194 | 194 | 415 of 416 manifest cases |
| Reported PASS / FAIL / paused | 131 / 62 / 1 | 131 / 63 / 0 | 290 / 125 / 0 recorded paused rows; one manifest case absent |
| Behavioral-reference report | 72 scored: 56 PASS / 16 FAIL | 72 scored: 56 PASS / 16 FAIL | 189 scored: 131 PASS / 58 FAIL |
| Compile-only report | 121 scored: 75 PASS / 46 FAIL; one paused | 122 scored: 75 PASS / 47 FAIL | 226 scored: 159 PASS / 67 FAIL |
| Progress timestamp | `2026-10-02T04:55:06.143150Z` | `2026-10-02T14:44:58.180645Z` | `2026-10-17T15:54:27.368118Z` |

The shared model name does not make these the same evaluation. Their manifest hashes, campaign events, source commits, case selections, reasoning settings, and dates differ. `provider_default_uncontrolled` does not prove that the ordinary campaign used no internal reasoning; it establishes that this archive did not record the controlled high-effort setting of the separate reasoning campaign.

The ordinary campaign's last case was `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. Snapshot 56 retains a provider-error pause. Snapshot 62 records `last_case_status = scored` and adds one compile-only FAIL, with all 194 cases scored. The separate reasoning campaign lacks `ts_trajectory__witness_status=valid_representation=reflective__seed-0`.

## Pinned provenance

- Newer writer branch: `origin/arena/4a683b34-epistemic-compiler`, resolved to `e370581946557a1a0d752a859de86bf8b61b6b7f`.
- Its six affected paths are under `campaign-03-analysis/post-production/handoffs/`: `R-POST-01_writer_A_prompt.md`, `R-POST-01_writer_B_prompt.md`, `R-POST-02_writer_A_prompt.md`, `R-POST-02_writer_B_prompt.md`, `R-POST-03_writer_A_prompt.md`, and `R-POST-04_writer_A_prompt.md`.
- Every affected handoff explicitly contains the covering-campaign event, the `c08e...` manifest, and 194 recorded cases. Five give the full 131/62/one-paused total; the remaining handoff gives the corresponding judge-level accounting.
- Ordinary snapshot 56 Git blob: `3743dedf05cc2f4fc7768128ae76f1dd1c54cd24`; local ZIP SHA-256: `3cb8162a754223264ab37238d12eb8ed97020893dde0c913218a90166a2818aa`.
- Ordinary snapshot 62 Git blob: `c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3`; local ZIP SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`.
- Ordinary archive source/campaign ref: `d7357092493f311f649a0742889b301d796911b5`; the inspected episode manifest records `repository_dirty = true`.
- Reasoning evidence branch: `origin/arena/7471eb0f-epistemic-compiler`, resolved to `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed`.
- Reasoning ZIP Git blob: `cb682350a0f8c8f0ce44910b4bb8a9b734126005`; SHA-256 recorded in the pinned provenance file: `2daf0e24cf2a38702f3e1182153627aa28b51b71f67744c50febd3741cea231f`.
- Reasoning archive source/campaign ref: `9ec2d919726ba39aded2e1d011a8274f938fb7ba`; the inspected episode manifest records `repository_dirty = true`.
- Directly inspected ZIP members: `campaign_intent.json`, `campaign_report.json`, `campaign_progress.json`; ordinary `compatibility.json`; one episode `manifest.json` in each campaign. The reasoning ZIP was read from the pinned Git blob in memory.
- Reasoning supporting records: `campaign-03-analysis/evidence/PROVENANCE.md`, `evidence/generated/headline_counts.csv`, and `posts/POST_PLAN.md` at `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed`.

## Consequence for the pipeline

For posts intended to describe **Reasoning-Atria**, use the separate reasoning-pairwise archive and its generated evidence tables. The newer four-topic outline can remain editorial input, but its article candidates and handoff counts cannot be promoted as results from that campaign. Rebuild their evidence packets and send the corrected packets through evidence review before advancing those candidates.

For a post deliberately describing the earlier ordinary-Atria paused snapshot, retain the snapshot-56 counts only with that historical scope stated explicitly. A current account of the ordinary covering campaign should use snapshot 62, including the final FAIL and completed status. Do not silently transfer either ordinary snapshot's results into Reasoning-Atria.

The reasoning report itself has documented limitations: 18 FAIL rows carry `case_disposition = unscored`, 62 FAIL rows carry `rejected`, one FAIL is performance-ineligible, and the source tree was dirty. Its report totals must remain identified as reported totals with these discrepancies disclosed. None of this changes Mercury POST-02's evidence or requires interruption of its current battle.
