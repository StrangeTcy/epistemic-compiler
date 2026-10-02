# Source note: the 2026-10-02 Arena instruction revision (GPT-5.6 Luna)

**Status.** The compiler agent's note on a single Arena output the user pasted on 2026-10-02. The
response itself is stored verbatim, unedited, at `raw/2026-10-02_instruction_revision.gpt_5.6_luna.md`,
under a provenance header marked as not part of the response. This note is the compiler's reading; it is
not part of the record and decides nothing.

## 1. What the material is

A revised Arena kickoff instruction. The respondent (shown as "gpt 5.6 luna"; the same label appears in
the 2026-09-29 round note's model list) retracts an earlier position of its own — that the
epistemic-games direction was too broad to study — and instead argues that epistemic games / strategic
reasoning should be a **core research domain**, with the mindcluster in `knowledge/` used as a generator
of candidate benchmark mechanisms. The embedded instruction asks an agent to search the mindcluster,
formulate candidate phenomena, select one, and design a benchmark with controls, an oracle, Strategy-IR
connection, falsification variants, and artifacts at `mission-02/seed.yaml`, `mission-02/design.md` and
`mission-01/harvest.md`.

The prompt it answers was not supplied; from its first line it responds to a critique of the
respondent's own earlier instruction draft. It is not a response to any of the four Mission 02 Council
prompts (P01–P04) and is not shown to the Council.

## 2. Where it collides with the current repository state

- It directs creation of `mission-02/seed.yaml` and `mission-02/design.md`. Both exist: `mission-02/`
  on this branch is a paused proposal with a seed, a freeze record (`freeze/game_cards.freeze.yaml`,
  M02-FREEZE-1) and three of four Council responses stored. `tests/test_mission_02_freeze.py` protects
  the freeze. The response predates that state.
- It directs `mission-01/harvest.md`. Mission 01 is frozen here as elsewhere; nothing in the
  instruction conflicts with that, but the harvest file does not exist yet.
- It treats `rl_eval_generator` as a working repository. In this workspace `rl_eval_generator/` is an
  empty placeholder; the runtime repository is not present in the snapshot.

Executing it literally is therefore impossible; executing it at all would mean adapting it to a new
mission directory (mission-04, since mission-02 and mission-03 exist), which is a human decision the
compiler does not make. Nothing in the response has been executed, checked, or adopted.

## 3. What was checked (2026-10-02)

Only text integrity: the stored file reproduces the paste exactly, nested code fences included, with the
user's label line dropped. No claim in the response was verified against `knowledge/` or any other file.
