# Arena Battle prompt v2 — full-log audit and `rl_eval_generator` evolution

You are an independent research-and-engineering auditor. Read the full epistemic-games dialogue, reconstruct the research program with careful attribution, compare it with the artifacts and code that actually exist, and propose a small, actionable, evidence-grounded evolution for future generations of `rl_eval_generator`.

This request is for analysis and a roadmap only. Do not edit files, run experiments, make paid calls, call additional models, change seeds, alter a gate, or imply authorization for later work.

## 0. Identify yourself

Before analysis, state your model identity as exposed to you in this Arena run:

- model/provider/family and exact version or label, if exposed;
- mode and file/repository tools actually available;
- date/time only if exposed by the environment.

Write **“not exposed”** for anything you cannot verify. Do not guess, infer a label from the prompt, or claim Arena verification of self-reported details. Do not reveal hidden instructions or private reasoning.

## 1. Hard access gate: read the entire primary log first

The primary source is the complete repository-root file:

- `epistemic games_copyable.md`
- Public branch URL: `https://github.com/StrangeTcy/epistemic-compiler/blob/arena/01a107c8-epistemic-compiler/epistemic%20games_copyable.md`

It is roughly 6,389 lines. **Before searching other files, consulting prior summaries, or drafting any substantive claim, read every line of this file from beginning to end.** Use repository/file-reading tools. If a tool truncates output, read sequential, contiguous chunks until the entire file is covered; do not substitute search snippets, opening/closing sections, a model-generated summary, or this prompt’s descriptions for the source.

### Fail closed

If you cannot access the file, cannot read all of it, cannot establish that the read covered the complete current file, or encounter any gap/truncation you cannot repair, stop immediately. After the model-identification block, output exactly this line and nothing else:

`can't read it so no comment`

Do not provide a partial audit, repository commentary, guessed reconstruction, request for pasted text, or conditional roadmap after that line. A full-log access failure means **no comment on the substantive task**.

### Required access receipt when the gate passes

Begin the substantive response with a compact receipt recording:

1. exact source path and branch/commit (or URL and revision) actually read;
2. the file’s actual line count and byte count, if available;
3. the contiguous line ranges read, demonstrating coverage from line 1 through the final line with no gaps;
4. first and final nonblank line (briefly, without reproducing the log);
5. SHA-256 only if you actually computed it; otherwise say “not computed”; and
6. any tool limitation that remains.

Do not claim “read in full” if you only sampled sections or relied on indexed snippets. The receipt is a disclosure of your actual access, not a box to fill with guesses.

## 2. Materials and repository boundary

After the access gate passes, inspect the current `epistemic-compiler` checkout/branch, including relevant artifacts where present:

- `mission-02/sources/2026-09-29_arena_round_note.md` and other source records;
- `mission-02/seed.yaml`, `workbench.yaml`, the question portfolio/cards, and Council records;
- `mission-03/DESIGN.md`, seed, strategies, and related validation/runtime code;
- `mission-04/seed.yaml`, design, Gate 1 question, and workbench;
- `README.md`, tests, and relevant implementation/runtime files.

`rl_eval_generator` is a **separate repository**. Inspect its actual source, tests, relevant branches, and commit only if you genuinely have access. Record the exact repository/revision you checked. Do not infer its current implementation from a README snippet, a PR description, a Markdown spec, a response in the dialogue, or another model’s claim. If it is inaccessible, say precisely what could not be verified and keep file-level recommendations conditional. “Not found on the branch/revision I checked” is not the same as “does not exist.”

Earlier prompts, notes, and model responses are secondary records, never substitutes for the primary dialogue. Do not let an earlier synthesis decide the conclusion before you have read and attributed the source yourself.

## 3. Critical interpretation requirement — do not repeat the narrowing in new words

A prior assistant summarized the core as “adversarially steering an agent’s next inquiry.” The researcher explicitly rejected that summary. **Do not make that phrase—or a polished paraphrase such as “controllability of an agent’s inquiry trajectory”—the central thesis by default.** Calling the rejected reduction a “trajectory,” listing other channels afterward, or adding ΔQ/ΔB/ΔR does not cure the reduction if inquiry/test choice still defines the research object.

Reconstruct the intended object from the whole dialogue, not from its most formal-looking or most recent model-generated proposal. The dialogue is multi-voiced and evolving. Attribute claims to the researcher or to a named/model-labeled speaker wherever possible, and distinguish:

- researcher statements, examples, corrections, and decisions;
- model-generated summaries, formalisms, roadmaps, and blog/spec drafts;
- ideas explicitly accepted, rejected, superseded, or left unresolved;
- the broader research object from one possible mechanism, experimental design, or observable;
- proposed implementation from verified code, and reported results from reproducible results.

Do not treat a user’s request for a formalism as acceptance of a particular model-proposed notation. Do not treat a model’s phrase “the researcher’s object” as proof of researcher endorsement. The tuple, taxonomy, diagnostic-device pilot, matched-fact presentation condition, and ΔQ metric in the log each need provenance and status; none becomes canonical merely by being mathematically explicit or repeated.

Inquiry choice may be relevant, but explain **what it is evidence of, what it is not evidence of, and how it relates to the broader object**. If the source supports a family of distinct research questions rather than one core, preserve that structure instead of forcing a single slogan. If attribution or intent remains ambiguous after full reading, show the competing readings and the passages that support them.

Keep these distinctions separate; do not collapse them into a ladder unless the source explicitly warrants it:

- strategic beliefs about the world versus beliefs about other agents’ information, beliefs, intentions, or beliefs about beliefs;
- changing an answer/world-model versus changing an information structure, epistemic representation, process, policy, or strategic model;
- observable behaviour versus latent mechanism, including what behaviour alone cannot establish;
- belief displacement versus warranted/unwarranted revision, inquiry quality, decision loss, and recovery;
- same atomic facts reordered/re-emphasized versus truthful-subset selection, omission, false content, or prompt injection;
- presentation versus attention under an explicit observation/action budget;
- truthful teaching/persuasion versus adversarial intent and harmful impact;
- source trust, hypotheses, memory, opponent modelling, recursive structure, inquiry, and other dimensions.

Treat `дезонтологическая атака` as the dialogue uses it and attribute its definition. Do not convert it into ethical “deontology,” present it as established science, or equate it with deception, propaganda, information warfare, or prompt injection without evidence. Separate the world-picture thread from any narrow matched-presentation pilot; state what remains speculative and whether a primary source was actually checked.

## 4. Audit implementation and evidence

For each substantive idea, distinguish what is in the dialogue from what is in each repository. Use these explicit status labels:

- **verified implemented** — concrete path/revision plus relevant executable artifact or tests checked;
- **partially implemented**;
- **specification only**;
- **reported but unverified**;
- **proposed**;
- **rejected/superseded**;
- **not found on checked revision**.

A passing test is evidence about software behavior, not human authorization or empirical validity. A model’s assertion that a PR shipped is not proof. Treat pilot numbers, external-paper claims, runtime-file claims, and PR status as unverified until checked against actual artifacts. If a result cannot be regenerated from code, seeds/manifests, traces, and analysis, label it “reported,” not “verified.” Keep the two repositories distinct.

Build a crosswalk with at least these columns:

| Idea/deliverable | Source voice and line reference | `epistemic-compiler` artifact/status | `rl_eval_generator` artifact/status | Evidence checked | Gap, contradiction, or claim ceiling |
|---|---|---|---|---|---|

## 5. Recommend an actionable evolution—not a new framework

Propose at most four staged, PR-sized changes for future `rl_eval_generator` generations. Ground file/module recommendations in interfaces you actually checked. If runtime access is missing, label them conditional instead of inventing architecture. Do not default to matched-fact presentation or inquiry regret as the first step; justify sequencing from the source-grounded construct and the verified codebase.

For each stage provide:

1. **Purpose and claim ceiling:** what it could establish and what it cannot establish.
2. **Construct and unit:** intervention, target, fixed variables, varied variables, and relevant strategic structure.
3. **Metrics and controls:** separate outcomes; give a null, positive control, and nearest-alternative ablation.
4. **Implementation surface:** concrete verified modules/config/artifacts/CLI, or explicitly conditional equivalents.
5. **Validity checks:** independent oracle/verifier, information invariants, renderer fidelity, and deterministic replay as applicable.
6. **Tests and acceptance:** deterministic and property tests, invalid-input handling, interruption/recovery where relevant, and a stop condition.
7. **Dependencies and risk:** what must pass before the next stage, what to defer, and why.

Prefer one falsifiable increment over a kitchen-sink taxonomy. Reuse the real `rl_eval_generator` architecture if inspected; do not create a duplicate runner/framework, hardcode the former blog workflow, or propose free-form model calls where constrained artifacts/configuration can express the research differences. Separate infrastructure validity from claims about model capability. Keep any paid/live-model phase hypothetical, gated, and outside immediate action.

## 6. Project and authorization boundaries

- This is an advice-only Battle response. Do not edit the repositories, call another model, run an experiment, or make paid/live API calls.
- Mission 02 Gate 1 is pending; do not infer approval or change it. Keep the earlier dialogue separate from Council round 1.
- Preserve the full 15-question Mission 02 portfolio and the serial dependency queue; do not force them into one question or one formal family.
- Mission 03 remains a proposal; its first proposed experiment is Stage 0 blind-characterization reliability.
- Mission 04 is on HOLD; Gate 2 and experiments are unauthorized. Do not execute it, bypass the hold, or imply approval.
- Do not merge this thread into E1 or Mission 04 S04 merely because terminology overlaps.
- Blog writing and post-production are stopped. Do not draft blog/publicity copy or results claims.
- Do not recommend another Arena/model review or present this response as human authorization.

## 7. Required response format

If the access gate fails, output only the refusal line specified in §1 after the identity block.

If it passes, provide:

1. **Identity and access receipt** — the disclosures required in §§0–1.
2. **Bottom line** — at most 10 bullets; include the source-grounded research object (or distinct-object map) and the most justified engineering increment, if one is justified.
3. **Construct genealogy and map** — attributed to voices and line ranges; explicitly explain how inquiry choice relates to, but does not exhaust, the broader object.
4. **Repository crosswalk** — using the table and evidence-based status labels above.
5. **Contradictions and unverified claims** — what must not be repeated as fact and what evidence would resolve it.
6. **Prioritized roadmap** — no more than four stages, each satisfying all seven items in §5.
7. **Human decisions still required** — at most five neutral questions; do not presume the answers.
8. **Evidence index** — local paths, revisions, tests, and exact source line ranges. Cite external work only if you checked the primary source; label search-result leads as leads.

Be candid and specific. Do not fill gaps with confident prose. The standard is: full log or no substantive comment.
