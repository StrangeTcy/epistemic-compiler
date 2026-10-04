# POST-05 compact evidence and editorial brief

This is a compiler-authored condensation for battle-mode use; the evidence packet, both candidate articles, and both full critiques remain separately preserved but are not attached here. Treat the facts below as the evidence available for this call. If a point is unclear, omit or qualify it rather than resolving it from memory or from unprovided drafts. This is not a new critic response or a claim of consensus.

## The claim to make

One archived, single-seed sweep shows an eye-catching local regex pattern: the easy-surface cases pass at all three input lengths, while two altered-surface cases fail at length 32. The manipulation is confounded, the other tasks use different notions of size and different judges, and the archive does not identify a cause. The article is about what this pattern does—and does not—show, not a general ability to recognize “weird machines.”

## Evidence card

- The track has six five-case tasks: regex state machine, CSS state machine, SQL fixed point, spreadsheet dataflow, CI dependency graph, and template interpreter. All 30 selected cases are eligible and use behavioral-reference judges; none are compile-only, excluded, or provider-terminal. Twenty-five pass and five fail.
- Per task: CI 5/5, spreadsheet 5/5, template 5/5, SQL 4/5, CSS 3/5, regex 3/5. These are heterogeneous counts, not a common capability or difficulty score.

| Regex surface | Input length | Result | Score | Judge note |
|---|---:|---|---:|---|
| easy | 32 | PASS | 1.0 | — |
| easy | 128 | PASS | 1.0 | — |
| easy | 512 | PASS | 1.0 | — |
| medium | 32 | FAIL | 0.208333 | length mismatch, in=32, out=34 |
| hard | 32 | FAIL | 0.208333 | length mismatch, in=32, out=66 |

- The regex task asks for one Rule 110 update using regex. Its judge checks four specific criteria, including length preservation and exact behavior on 15 seeded strings. Passing this bounded check is not general regex correctness or arbitrary iteration.
- The five failures stop at different layers: two regex underfits (outputs of 34 and 66 characters from length 32); one CSS behavioral underfit (score 0.416667 at 3 bits); one CSS source-invalid result at 4 bits (disallowed top-level `import re`); and one SQL source-invalid result at chain length 12 (unterminated triple-quoted string). The CSS 5-bit case passes; SQL chain lengths 6 and 25 pass. Source-validator rejections are gate failures, not behavioral evidence of semantic inability.
- The CSS surface sweep at 3 bits is fail/pass/pass for easy/medium/hard—the opposite direction from the regex contrast. These local outcomes are non-monotone; they do not establish a shared depth scale.

## Source and design limits

- Each selected cell has one seed-0 run. Three easy-surface regex passes are not a size-invariance estimate; the two altered-surface failures do not establish an effect or cause.
- In the clean-source comparator, surface levels use different class names and the hard prompt adds a performance hint. The campaign archive records `repository.dirty=true`. All 33 selected configuration hashes match the clean comparator, but that does not prove the paid-run prompts, task files, or judges were byte-identical to it. State comparator findings as such.
- The proposed “names or hint mattered more than length” idea is an untested hypothesis; label it speculative if used. Do not diagnose the 34/66 mechanism.
- A separate clean-comparator scan found ten nominal control/variable axes without direct template references across nine category-track environments. This is adjacent benchmark QA, not evidence about the weird-machine regex task; include at most one carefully qualified sentence.
- A better experiment would separate class-name and hint manipulations, use multiple instances and seeds, diff rendered prompts/starters/tests/judges before calls, and report patch creation, source validity, execution, and behavioral correctness separately.

## Editorial guidance from the separately preserved critiques

- Shared direction—not full consensus: use a fresh, concrete opening; keep the five-cell regex table; place the single-seed and confound limits beside the regex claim; separate source-invalid failures from behavioral underfits; invent no mechanism for 34/66; and close in prose with what the evidence does and does not license.
- Sonnet 4.6 emphasizes failure-layer clarity and an airy essay: keep the regex table and, if useful, one compact failure-layer table; move per-environment and CSS/SQL depth counts into prose; keep the broader 192/61 campaign taxonomy out; place comparator and dirty-source caveats where they matter.
- Opus 4.7 favors retaining the regex and failure-layer tables plus per-environment counts, and allows a brief 192/61 scale aside. Its advice on tables and breadth differs from Sonnet’s; this brief resolves that disagreement by keeping only the five-cell regex table plus at most one failure-layer table, and putting counts in prose.
- Both drafts remain distinct: Writer A’s strengths are careful evidential boundaries, failure-layer separation, and a bounded ending; Writer B’s are the regex table, useful failure stratification, and refusal to invent a 34/66 mechanism. Do not stitch or paraphrase either draft; write a new essay.
- Keep citations limited and relevant: [HELM](https://arxiv.org/abs/2211.09110) as context for broad scenario/multi-metric evaluation (42 scenarios); [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) for dynamic variable perturbation and five-seed sampling in its variable-based experiments. These are precedents, not validation of this campaign or grounds for a novelty claim.
- The Opus 4.7 checklist miscounts a profanity in the source drafts (it says Writer A has one and Writer B three; the preserved copies show Writer A zero and Writer B one). Omit it entirely from public copy. No supplied critic’s checklist is authoritative; follow the evidence and requirements here, not an asserted consensus.

## Public article requirements

- Target 2,000–2,300 words, within the workflow’s 1,800–2,500-word target. First-person, curious, technically literate, self-correcting, airy paragraphs, short argumentative `##` headings, no `Introduction` heading. Style reference: actual posts sometimes open with a short declarative claim and then complicate it; borrow the movement, not their wording.
- Use Jekyll frontmatter: quoted, specific `title`; `date: 2026-10-03`; `layout: post`. No MathJax include unless adding a justified formula (none is warranted). Exact byline: `*by <span class="icon-self">StrangeTcy</span>*`.
- If using the site's `<dl class="epistemic-status">`, keep fields in this order: Original ideas, Synthesis, Prose, Certainty, Importance. Describe the actual Arena-assisted writing process accurately; do not imply independent external writers or experiments.
- Keep caveats next to the claims they qualify. Do not infer causality, Turing completeness, arbitrary iteration, general weird-machine recognition, paid-run source identity, or a common difficulty scale. Do not present source-invalid failures as behavioral failures.
- No internal paths, hashes, claim/evidence IDs, draft labels, critic labels, editor notes, placeholders, or invented facts/links. Return only the complete Markdown article.
