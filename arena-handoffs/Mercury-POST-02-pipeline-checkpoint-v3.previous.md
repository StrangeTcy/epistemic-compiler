# Mercury POST-02 pipeline checkpoint — 2026-10-29

Current stage: **final-writer package prepared; in-app browser recovery required before dispatch**.

## Completed stages

1. Evidence review: https://arena.ai/c/01a187dd-b0eb-7501-b2e8-5dce27b56175
   - Raw names: grok-4.5-search, claude-fable-5.1-search. Vote: Both are bad; findings preserved and reconciled against rows.
   - Full rendered text: `Mercury-POST-02-redo-evidence-check-v3.retry-1.responses.md`; exact DOM HTML/text: `.rendered.json`. Copy controls returned empty clipboard, so original Markdown fidelity is not claimed.
2. Editorial blueprints: https://arena.ai/c/01a187f3-a83f-7da0-ac6e-b689dd235cdb
   - Raw names: claude-fable-5.1-search, grok-4.5-search. Vote: Both are bad; material blueprint defects carried into claim check.
   - Pair: `Mercury-POST-02-editorial-critic-v3.responses.md`; exact code-block text for A, complete rendered text for B, original DOM HTML in sidecar.
3. Claim check: https://arena.ai/c/01a18816-4a23-7355-97e5-6ee5c1fac266
   - Raw names: claude-opus-5-search, gpt-6-luna-search-max. Vote: Both are bad; B introduced a nine-versus-four parse-only typo; A has narrow agreement/key-count wording qualifications.
   - Pair: `Mercury-POST-02-claim-check-v3.responses.md`; both reports captured as exact full Markdown from their outer twelve-tilde code blocks.

No prose winner was chosen. All original outputs are preserved, with source-based reconciliations kept separately. Supporting local work is not described as an Arena verdict.

## Ready final-writer handoff

- Full prompt: `Mercury-POST-02-final-writer-v3.prompt.md` (554699 characters).
- SHA-256: `ce71f393e8d5e52fc6a5db3f5c736ffbe8da14c934e03b34974cc49de731c2bc`.
- Twelve transport files: `Mercury-POST-02-final-writer-v3.part-1.txt` through `part-12.txt`.
- Exact input manifest: `Mercury-POST-02-final-writer-v3.input-manifest.json`. All ten original source-file hashes were recomputed and matched. It supplies the prior Web Search UI observations and artifact paths/hashes missing from the claim-check prompt.
- Record: `Mercury-POST-02-final-writer-v3.record.json`.
- No part of the final-writer request has been submitted.

The final prompt contains both original candidates, the complete pinned evidence packet and matrix, provenance, current internal article, house style and reference excerpts, both complete current evidence reviews, both blueprints, both claim reports, supporting source/figure checks, all reconciliations, and verified orchestration metadata. Its final part requests one twelve-tilde Markdown fence for lossless capture, preserving the exact article frontmatter inside.

## Current browser blocker

Browser binding: `arenaBrowser` (in-app browser ID 2 / iab). New-tab creation failed twice with webview attachment timeouts. Completed editorial tab 5 was then reused for https://arena.ai/search, but its DOM is empty/only an alert and screenshot width is zero even after reconnect and reload. Reconnected handle: `recoveredFinalTab`. The completed claim-check tab 6 (`claimTab`) now intermittently times out. The app open-page tool also returned a message-port error. No Edge browser was used and no working tab was closed.

Restoring the in-app browser is required. Do not repeat earlier stages. Resume by opening/using a healthy in-app https://arena.ai/search page, observe Web Search mode, submit all twelve final-writer parts sequentially and record both receipts after parts 1–11, then capture and rate both final articles. Keep the working tab open.

## Required continuation

1. Capture both final-writer articles, revealed names, and the both-good/both-bad vote. Preserve exact output; do not select a prose winner.
2. Save separate candidates in the existing `Mercury-POST-02-pipeline-resources/campaign-02-analysis/posts/` folder with unique names so all four `../figures/` links resolve, without replacing the current internal article.
3. Validate each candidate against source rows, the exact site contract, figure source checks, author wording exclusions, complete input provenance, and all necessary evidence qualifications. Produce a machine-readable report.
4. A failed local report opens the pipeline’s targeted human revision gate; no local final-article report exists yet.

Supporting corrections include 204 uniform-scored-outcome rows plus ten wholly unscored rows; four BR + five CO among nine 9/9 environments; all four omission environments; no inferred cell/planning unit; only scored singleton rows have binary rates; parse-only is FOUR PASSes (4/4), one performance-ineligible. Unresolved 14/24, seven/ten, approximately-12/17, provider-note, disposition, and source-state conflicts remain explicit.

**Not completed:** final writer, local final-article validation, human review, publication.
