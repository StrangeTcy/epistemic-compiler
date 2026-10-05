# Mission workbench

The workbench is a small front end over the existing resumable DAG engine. It reads `mission-*/workbench.yaml`, discovers recorded Council samples from their configured paths, and stages one authorized role as a `manual_arena` job. The job writes an immutable handoff, snapshots the exact prompt and inputs, records DAG transitions, and waits for a person. **It does not call Arena, use an API, need an API key, approve gates, or start a paid experiment.**

## Windows / PowerShell quick start

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r runtime/requirements.txt

python scripts/mission_workbench.py list
python scripts/mission_workbench.py status mission-02
python scripts/mission_workbench.py validate mission-02
python scripts/mission_workbench.py next mission-02
```

`list` discovers configured missions. `status` reads the actual role response files and shows recorded hashes, gates, holds, and local DAG runs. `validate mission-02` checks the manifest, configured prompt/input paths, and recorded response text without changing state or clearing any blocker. `next mission-02` stages the first missing Council role; in the current state that is Skeptic (P03-S). It uses the complete prompt at `mission-02/council/prompts/03_skeptic_prompt.md` without editing it. The staged handoff prints a path to the run-local prompt snapshot and its SHA-256.

Open that exact snapshot, copy all of it into a **fresh, manually opened Arena session**, and add nothing. The workbench has not submitted it. Save the visible model response to a UTF-8 text file without adding a provenance header or rewriting the response. Put provenance in a separate JSON file, for example:

```json
{
  "arena_mode": "Direct",
  "model_label": "the exact label displayed by Arena",
  "session_time": "the time you actually observed; include timezone if known",
  "tools": {"browsing": false, "code_execution": false}
}
```

Then ingest the saved file:

```powershell
python scripts/mission_workbench.py ingest `
  runtime/runs/mission-02/<run-id> skeptic_single `
  C:\path\to\skeptic-response.txt `
  --metadata-file C:\path\to\arena-metadata.json
```

Use the actual run directory printed by `next`; `skeptic_single` is the default single-response job id. If Arena presents two independent side-by-side answers, do not discard one: stage both response slots together before using the UI:

```powershell
python scripts/mission_workbench.py next mission-02 --role skeptic --samples a,b
```

Ingest each answer verbatim into `skeptic_a` and `skeptic_b`, with its own actual run metadata. Required metadata not supplied is recorded in the intake record as missing; it is never guessed. A default single response is retained as `mission-02/council/skeptic.md`; paired samples are retained as `skeptic.a.md` / `skeptic.b.md`. Each has a matching `.intake.json` sidecar, and the response plus provenance are also retained inside the ignored local DAG run. Those canonical files are immutable: identical recovery is idempotent; different bytes are rejected.

To inspect or resume an existing run:

```powershell
python scripts/mission_workbench.py status mission-02
python scripts/mission_workbench.py resume mission-02
# or: python scripts/mission_workbench.py resume runtime/runs/mission-02/<run-id>
```

A response handoff remains waiting until the human ingests the response; `resume` only re-displays the same hash-checked prompt and never resubmits it. If the local process was interrupted before the handoff was written, `resume` delegates recovery to the existing engine. Completed DAG jobs are not repeated.

## Configuration and gates

Each mission declares lifecycle, human hold, gate status, stage authorization, role prompt source/template, input paths, expected sample files, and metadata requirements in its own `workbench.yaml`. Prompt templates use literal `{{name}}` substitutions only—no executable template language. Optional blindness rules reject forbidden source paths or literals before a prompt is materialized. Per-role runs are ordinary engine DAGs, not a second scheduler.

`mission-01` is closed and cannot be reopened by the CLI. `mission-04` is explicitly on HOLD; Gate 1 is not approved and Gate 2 is unauthorized. No workbench override exists. Mission 02 Council completion does not decide Gate 1. Mission 03 Stage 0 is marked blocked, so `next mission-03` refuses to create a prompt or run until its listed human/specification blockers are resolved. The Stage 0-only instruction does not authorize Stage 1/2 or solver spend.

Local run state, prompt/input snapshots, raw ingested responses, event logs, and provenance remain under `runtime/runs/` and generated run specs under `runtime/workbench_specs/`; both are gitignored because they may contain local operational metadata. The configured mission response and intake sidecar are written once into the mission folder after ingestion. The workbench never commits them automatically.

## Tests and boundary

Run deterministic tests with:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -q tests/test_mission_workbench.py tests/test_runtime_engine.py
```

Tests use temporary files and fake/model-free runtime boundaries. They do not contact Arena or Google, verify a live login, or establish any research result. A passing test is not human authorization for a research gate or experiment.
