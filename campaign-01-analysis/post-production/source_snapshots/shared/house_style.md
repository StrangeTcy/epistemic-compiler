# StrangeTcy house style: operational guide for these five research posts

## Source inspected

The source of truth is the public Jekyll site, [`StrangeTcy/strangetcy.github.io`](https://github.com/StrangeTcy/strangetcy.github.io), inspected at commit `bcc89c392920b3be172a27eec10ad205b58d4fa3` on 2026-10-03. This guide is based on the requested post, [“The Diagram Is the Spec”](https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md), and cross-checks against “Knowing What Kind of Problem You Are In” (2026-09-26), “The Next Question Is Part of the Game” (2026-09-30), “Lying With Truth” (2026-10-01), “A Long Trajectory Is Not Necessarily Deep Reasoning” (2026-09-11), and “Controlling Scheming AIs Giving Strategic Advice” (2026-08-31). These examples were inspected before this guide was written. The last two are useful counterexamples to any claim that there is a single fixed post length or one rigid template.

This is an editorial grammar, not a phrase bank. The new articles should inherit the site's movement between intuition, technical structure, self-correction, and bounded claims; they should not reuse distinctive sentences, metaphors, or openings from the source posts.

## 1. Jekyll frontmatter and includes

The Jekyll site uses the `pages-themes/hacker@v0.2.0` remote theme in `_config.yml`; the recent posts themselves use `layout: post`. They use deliberately spare YAML frontmatter:

```yaml
---
title: "A Sentence-Case or Title-Case Article Title"
date: 2026-10-03
layout: post
---
```

`title`, `date`, and `layout: post` are the recurring fields. The inspected technical posts do not add tags, categories, summaries, or author metadata to frontmatter. Do not invent additional Jekyll fields for these files.

When an article contains inline or display mathematics, put `{% include mathjax.html %}` immediately after the frontmatter and before the byline. This is the include used by the inspected technical posts; `_includes/mathjax.html` is the site's MathJax loader. No other include is needed for the five essays.

The common byline is:

```html
*by <span class="icon-self">StrangeTcy</span>*
```

Recent posts then use an HTML definition list, not a Markdown callout, for epistemic status:

```html
<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>...</dd>
  <dt>Synthesis</dt>
  <dd>...</dd>
  <dt>Prose</dt>
  <dd>...</dd>
  <dt>Certainty</dt>
  <dd>...</dd>
  <dt>Importance</dt>
  <dd>...</dd>
</dl>
```

Preserve the five fields and their order. The HTML block is a compact disclosure about intellectual sources, synthesis/prose, confidence, and why the post matters. In these new drafts, its prose attribution must describe the actual role-separated Arena writing process accurately; it must not imply that two external models or independent human writers participated. Do not turn the disclosure into an internal audit log.

Other inline HTML in the sample includes `<span class="icon-self">`, source/model icon spans, and occasional `<em>`, `<code>`, or `<sup>` elements. Use HTML only where the site's existing styling needs it. There are no custom figure, table, or callout components in the surveyed 2026 research posts.

## 2. Headings and section numbering

- The main body begins without an `Introduction` heading. It opens in prose, often with a short declarative sentence or a compact scene/problem.
- `##` headings mark substantial argumentative turns. They are usually short, specific, and phrased as questions, claims, or objects (“The moving hole”; “What should count as harm?”), not generic report labels.
- Numbered sections are optional, not a house-wide requirement. “The Diagram Is the Spec” uses `## 1 — ...` for a sequence of mathematical examples, but the adjacent posts use unnumbered headings. Use numbering only when the sections really are a sequence of parallel mechanisms; do not number every stage of an essay to make it look systematic.
- `###` is used for subordinate topics or experiment variants. Avoid heading depth beyond that unless the article genuinely needs it.
- The ending usually returns to the central question and states what the idea does and does not license. A “Conclusion” heading is not necessary.

## 3. Length, paragraph density, and pacing

The recent conceptual/research posts are not a fixed word-count format: the inspected set ranges from about 1,800 words (“Lying With Truth”) through roughly 2,800–3,300 words (“The Diagram Is the Spec,” “Knowing What Kind of Problem You Are In,” “The Next Question Is Part of the Game,” and “Controlling Scheming AIs Giving Strategic Advice”) to an intentionally expansive 7,700-word treatment of recurrent depth. The requested target post is about 2,800 words. For these five linked campaign essays, a complete 1,800–2,800-word article fits the observed recent range; longer treatment is warranted where the mechanism needs it. The target's open paragraphing and argumentative development matter more than a threshold. Do not inflate a post to hit a quota.

Paragraphs are visually airy. Most carry one to four sentences; a sentence can stand alone when it marks a conceptual turn. Lists, short equation displays, and occasional one-line contrasts make technical material readable. The rhythm is not “paragraph, citation, paragraph, citation” but a paced alternation between explanation and consequence. A finished piece can be information-dense without reading as a memo.

## 4. Voice and rhetorical moves

The voice is first-person, curious, technically literate, and willing to show its own revision. It is confident about what was inspected and cautious about what the evidence can support. The author can say that an initial idea was wrong, explain why it seemed attractive, and keep the useful part after narrowing the claim. This self-correction is more characteristic than a neutral, impersonal “we evaluate” register.

Rhetorical questions are frequent but purposeful. They open a problem, isolate an ambiguity, or expose a hidden assumption; the next few paragraphs should answer them. Questions such as “what exactly does this measure?” create forward motion. Do not use question marks as a substitute for an argument.

Short contrasts are a recurring device: two variables that sound alike are separated (“rollout length” versus “necessary computation”; “belief displacement” versus “inquiry damage”), then the distinction is given an operational consequence. Use this structure when it clarifies the five topics, not as a repeated formula in every section. Bold is used to mark a thesis or a crucial contrast; italics add local stress rather than substituting for a definition. The author sometimes uses an ampersand in running prose, and occasionally a smiley or emoji as a dry aside. These are recognizable tendencies, not mandatory tokens; use them lightly and do not reproduce a source post's exact line.

Dry humour, self-deprecation, and occasional parenthetical asides are present, but they are intermittent. A small aside can release pressure after a dense point; it should not turn the post into a performance of quirkiness. Profanity exists in some recent writing, including technical prose, but it is an emphatic exception rather than mandatory seasoning. Do not borrow a memorable joke or a distinctive turn of phrase from the source posts.

## 5. Quotations, citations, and links

- Inline Markdown links are the default for papers, named concepts, prior work, and source repositories: `[VarBench](https://...)`.
- Citations are integrated at the point where the source matters. A short “References” section is used when a post has several sources; otherwise a compact inline citation or footnote can suffice. The site does not require a formal author–year style or a numbered bibliography in every post.
- Use blockquotes sparingly for a thesis, a source's consequential formulation, or an experiment's exact claim. The post often quotes a sentence, then interprets it; it does not paste source material as a substitute for analysis.
- Quote only text verified in the linked source. Keep quoted material short and distinguish quotations from paraphrase. Do not cite the blog itself as evidence for campaign results.
- Link to external prior work for conceptual lineage, not as a prestige list. State what each cited item contributes and where it is not a direct comparator.

## 6. Equations, diagrams, and tables

The technical posts use MathJax. Inline expressions use `$...$`; standalone equations use `$$...$$`. The target post frequently expresses commutative diagrams with `\begin{array}` inside display math, then spells out the engineering interpretation in ordinary prose. Other posts use a few equations to make a definition inspectable, not to decorate an assertion.

A diagram must be mathematically and operationally well-typed. State what each symbol means; explain what a failure of the law would look like in code or in the judge. If a full commutative square would overstate the implementation, use a simple equation, a two-column text diagram, or no diagram. The source post's standard is exactness, not ornament.

Tables are occasional and compact. They are useful when they preserve distinctions that a paragraph would blur (e.g., evidence strength by target response, or task claim by actual judge check). They are not the default way to display every result. A table must have explicit row/column meaning and cannot imply a common scale where the campaign did not establish one.

Plain fenced `text` diagrams appear in longer posts for flows or alternative mechanisms. Mermaid, embedded images, and elaborate HTML graphics were not present in the surveyed 2026 research posts; do not add new rendering dependencies.

## 7. Caveats and evidence in the narrative

Caveats appear at the point where an attractive interpretation would otherwise outrun the evidence. The usual move is: state the interesting observation, name the alternative explanation or judge limit immediately, and retain the narrower conclusion. Do not push every limitation into an apologetic final paragraph, and do not interrupt every sentence with a disclaimer.

For this campaign, keep the major constraints close to the evidence they qualify: one selected seed-0 run per cell; mixed `behavioral_reference` and `compile_only` judging; the explicitly exploratory status of compile-only results; two provider-transient terminal rows and the denominator sensitivity; `repository.dirty=true` for all source-comparator claims; implementation/judge defects and static-axis placeholders where relevant; and sequential Council role passes by one Arena model, not independent replications. Do not promote epistemic games to recursive theory of mind, compile checks to behavioral validation, one observed pattern to a causal law, or a task-family count to a general capability score.

The old evidence-marker system remains in its separate traceability files. Public prose must not contain its markers, claim IDs, internal post IDs, editorial notes, or data-extraction instructions.

## 8. A finished post versus an internal memo

An internal memo leads with denominators, evidence tags, source paths, and a list of guardrails. A finished StrangeTcy post begins with an idea a reader can hold in their head, uses a concrete mechanism or example to earn the abstraction, and lets the evidence alter the argument. It still gives exact numbers where they matter, but each number answers a question the essay has already made meaningful. It introduces prior work in relation to the claim rather than stacking references. It uses first-person judgement and self-correction without inventing personal experiences. It ends with a bounded research consequence: what one should test next, what a result would mean, or what the current evidence cannot decide.

For this series the desired progression is: **an intelligible puzzle → the mechanism or mathematical object → a concrete case → what the audited evidence actually says → the strongest counterargument/limitation → the next experiment or research consequence**. Each essay may choose its own order and narrative device. None should read like a benchmark table with prose inserted between rows.
