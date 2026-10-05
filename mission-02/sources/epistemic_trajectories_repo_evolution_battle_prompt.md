# Arena Battle prompt — Epistemic Trajectories and `rl_eval_generator` evolution

You are an independent research-and-engineering auditor. Analyze the full raw epistemic-games dialogue, compare its ideas and implementation claims with the repository as it exists now, and propose a prioritized, actionable evolution for future generations of `rl_eval_generator`.

This is an **analysis and roadmap request only**. Do not call another model, run an experiment, make paid API calls, change files, edit a seed, or infer authorization to pass any gate.

## Materials and scope

Primary source:

- Repository-root file `epistemic games_copyable.md` (the full long-form dialogue and embedded proposals/specs). Read the whole file, not only its opening summary or final sections. It is about 6,389 lines; if you cannot access the whole file, state exactly what you could and could not read.
- Public branch URL: `https://github.com/StrangeTcy/epistemic-compiler/blob/arena/01a107c8-epistemic-compiler/epistemic%20games_copyable.md`

Compare against the current `StrangeTcy/epistemic-compiler` checkout/branch, especially these artifacts where present:

- `mission-02/sources/2026-09-29_arena_round_note.md`
- `mission-02/seed.yaml`, `mission-02/workbench.yaml`, `mission-02/gates/question_portfolio_draft.md`, and the E-question cards
- `mission-02/council/` and `mission-02/sources/` records, while keeping the earlier dialogue separate from Council round 1
- `mission-03/DESIGN.md`, `mission-03/seed.yaml`, `strategies/`, and any relevant runtime/validation code
- `mission-04/seed.yaml`, `mission-04/design.md`, `mission-04/gates/gate1_question.md`, and `mission-04/workbench.yaml`
- repository `README.md`, tests, and all relevant implementation files discoverable by searching for names such as `epistemic.py`, `diagnostic_device.py`, `run_experiment.py`, `epistemic_trajectories`, and `epistemic_process_control`

`rl_eval_generator` is a **separate repository** from `epistemic-compiler`. Inspect its current source/branches only if you actually have access. If it is absent or inaccessible, say so and identify which implementation claims cannot be verified. Never treat a Markdown specification, a model's assertion that a PR shipped, or a results table embedded in the dialogue as proof that code or results exist.

## Critical interpretation correction

An earlier assistant summarized the core as “adversarially steering an agent’s next inquiry.” The researcher explicitly rejected that summary. **Do not use it as your premise or repeat it as the central thesis.** Reconstruct the intended object from the full dialogue: explain what the primary construct is, how inquiry choice relates to it, and what the earlier summary leaves out or gets wrong. If the dialogue supports several distinct constructs rather than one core, say so and keep them distinct.

The raw file is an evolving dialogue, not a final specification. Separate, and attribute where possible:

- the researcher’s own ideas, corrections, and decisions;
- suggestions from individual model voices;
- ideas accepted, rejected, superseded, or left speculative;
- implementation specifications versus verified implementation;
- reported experiment results versus reproducible, independently auditable results.

Do not smooth contradictions into a single coherent history. Identify them and state which evidence would resolve them.

## Required distinctions and safeguards

Use the dialogue and repository as evidence; do not assume the following distinctions are interchangeable:

- changing an observed answer or belief versus changing a process, policy, or information environment;
- changed behaviour under a fixed policy versus evidence that the policy/update procedure itself changed;
- belief displacement versus warranted/unwarranted revision, inquiry quality, decision loss, and recovery;
- same atomic facts reordered/re-emphasized versus selecting a truthful subset, adding false information, or prompt injection;
- presentation effects versus an actual attention manipulation with a defined observation/action budget;
- a scripted presenter/target versus a model presenter/defender, and presenter capability versus target susceptibility;
- truthful persuasion/teaching versus adversarial intent and harmful impact;
- dimensions such as attention, source trust, hypothesis search, memory, opponent modelling, recursion, and inquiry policy. Do not force them into one capability ladder unless the source evidence justifies it.

The transcript uses the term `дезонтологическая атака` / “desontological attack,” attributed to Gilbo. Do not silently convert this into ethical “deontology,” present it as an established scientific construct, or treat it as synonymous with deception, propaganda, information warfare, or prompt injection. Report how the dialogue operationalizes it, what remains speculative, and what evidence/source verification is missing.

Treat claims about the pilot, numeric results, PR status, external papers, and runtime files as **unverified until checked against actual artifacts**. The log contains corrections and cautions about earlier claims; locate and honor them. If a result cannot be regenerated from code, seeds/manifests, traces, and analysis, label it “reported in the dialogue,” not “verified.”

## Analysis tasks

### 1. Reconstruct the intended research object

Give a concise, evidence-backed account of the central research program as the researcher describes it—not as a prior assistant slogan. State:

- what capability or failure is to be studied;
- what an intervention acts on;
- what is observed, what remains latent, and what cannot be claimed from behaviour alone;
- how the truthful-information / “desontological” thread relates to, but differs from, the implemented or proposed process-control work;
- which parts are separable research dimensions rather than stages of a single ladder.

Quote or cite exact sections/line ranges from the raw file and repository. If your interpretation is uncertain, present competing readings rather than forcing a resolution.

### 2. Audit the repository and implementation status

Build a crosswalk with one row per substantial idea or deliverable. At minimum include:

| Idea/deliverable | Provenance in raw log | Current repository artifact/code | Status | Evidence actually checked | Gap/contradiction |
|---|---|---|---|---|---|

Use explicit status labels: **verified implemented**, **partially implemented**, **specification only**, **reported but unverified**, **proposed**, **rejected/superseded**, or **not found**. For “implemented,” require a concrete path/commit plus relevant tests or executable artifacts. Keep `epistemic-compiler` and `rl_eval_generator` distinct. Identify duplicate, stale, or conflicting versions of the spec and any divergence between the repository and the dialogue.

### 3. Identify the strongest ideas and the dangerous conflations

Rank the ideas by research value and actionability. For each high-priority idea, state:

- the minimum observable claim it could support;
- a falsifier or null result that would be informative;
- the control/ablation needed to distinguish it from the nearest alternative;
- what would be overclaiming.

Pay particular attention to the dialogue’s insistence that belief movement alone is not harm, that truthful content need not be neutral, and that a behavioural change does not by itself prove a changed internal update rule.

### 4. Propose a versioned, PR-sized evolution for `rl_eval_generator`

Recommend a small number of staged improvements—not a new framework or a kitchen-sink taxonomy. Reuse the actual architecture and artifact conventions you verified. If the runtime source is unavailable, phrase file-level items conditionally and mark the architecture gap.

For every proposed generation/PR, provide:

1. **Purpose and claim ceiling** — what the stage establishes and explicitly does not establish.
2. **Minimal construct and unit** — what changes, what stays fixed, what the target/presenter can observe or do.
3. **Metrics and controls** — keep distinct outcome measures distinct; name the null, positive control, and key ablation.
4. **Implementation surface** — concrete modules, schemas, config, artifacts, or CLI changes, mapped to verified existing interfaces where possible.
5. **Independent validity checks** — oracle/verifier independence, same-information invariants, renderer/text fidelity, and deterministic replay as applicable.
6. **Tests and acceptance criteria** — deterministic unit/property tests, failure cases, interruption/recovery where relevant, and clear stop conditions.
7. **Dependencies and risk** — what must be true before the next stage; cost/complexity risks; what to defer.

Assess (but do not assume) the sequence described in the dialogue: pure domain/oracle; scripted-target and presentation checks; runner/artifact layer; any live infrastructure pilot; model presenter; recovery; and later independent channels such as explicit attention, source trust, hypothesis search, memory, or recursive presentation. Recommend changes only where repository evidence or the dialogue’s corrections warrant them. Do not silently move a future phase into the current implementation claim.

### 5. Preserve project and authorization boundaries

- Do not merge this thread into E1 or Mission 04 S04 merely because they share epistemic vocabulary. Explain the relationship and differences.
- Mission 02 Gate 1 is pending; Mission 04 is on HOLD; Gate 2 and experiments are unauthorized. Do not change or imply any of these statuses.
- Keep the 15-question portfolio intact unless the researcher explicitly changes it.
- Do not write blog posts, publicity copy, or results claims. Blog work is stopped.
- Do not recommend a live Arena/model call or paid run as an immediate action. This Battle response is advice only; any later call or experiment requires explicit human authorization.

## Required output

1. **Bottom line** (no more than 10 bullets): the best-supported description of the research object and the single most valuable next engineering step.
2. **Idea genealogy and construct map** with provenance and distinctions.
3. **Repository/implementation crosswalk** using the status labels above.
4. **Contradictions and unverified claims** that must not be repeated as fact.
5. **Prioritized roadmap** of at most 4 stages/PRs, each meeting the seven requirements in Task 4.
6. **Human decisions still required** (at most 5, phrased neutrally; do not infer the answer).
7. **Evidence index** with repository paths and section/line references; external citations only when you actually checked the primary source.

Be candid, specific, and economical. Prefer one falsifiable, testable increment over grand claims or ornate notation. Do not produce code or claim that anything was implemented unless you can point to the artifact and verify it.