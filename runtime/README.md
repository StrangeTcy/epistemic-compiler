# Local mission runner

This is a narrow, optional execution utility for the existing compiler. It runs an explicit YAML job DAG through a local persistent Playwright browser profile. It does not define research questions, score evidence, approve gates, revise the protocol, or replace the protocol's human decisions. It has no provider/API adapter; the first site adapter is Arena Direct.

## Setup

```bash
python -m venv .venv
. .venv/bin/activate                 # Windows: .venv\Scripts\activate
python -m pip install -r runtime/requirements.txt
python -m playwright install chromium
```

Open the Arena profile and authenticate or complete verification manually:

```bash
python scripts/browser_login.py arena
```

The persistent profile is stored outside the repository under `${XDG_DATA_HOME:-~/.local/share}/epistemic-compiler/browser_profiles/epistemic-compiler/<profile-id>/` and remains on the local machine between runs. It contains the browser's site session data, so do not copy or share it. The runner never reads or prints passwords, cookies, or tokens. If the browser needs login or CAPTCHA verification during a job, the job becomes `waiting_for_human`; use `inspect_run.py` to find the saved URL, reopen it with `python scripts/browser_login.py arena --url 'https://arena.ai/…'`, complete verification manually, close the window with Enter, then resume. The URL option rejects non-HTTPS or non-Arena hosts and embedded credentials. For an ambiguous submit control, inspect the saved prompt/input snapshot and only manually submit if that is explicitly intended; the persisted ambiguous-submission marker prevents a second automatic send.

For a headless local run after manual login, set `EPISTEMIC_BROWSER_HEADLESS=1`. Visible mode is the default and is preferable while checking the UI.

## Mission YAML

See `schema.yaml` and `../examples/campaign-analysis.yaml`. A mission lists prompt artifacts, file inputs, dependencies, an Arena model label, and output paths. Input references are:

- `mission:<input_id>` — a file declared in top-level `inputs`.
- `job:<job_id>:response` — a completed dependency's response artifact.
- A path — relative to the mission YAML file (or an absolute local path).

The runner rejects unknown dependencies, dependency cycles, unsafe output paths, missing prompt/input files, and model/UI ambiguity before submission. Runtime state and provenance are stored under `runtime/runs/<mission_id>/<run_id>/` and ignored by Git. A run contains `run_state.json`, append-only `events.jsonl`, immutable prompt/input snapshots, each response artifact, per-job `provenance.json`, and screenshots saved when the adapter pauses or fails.

## Run, resume, inspect

For a mission that has been explicitly approved for execution:

```bash
python scripts/run_mission.py path/to/mission.yaml
python scripts/inspect_run.py runtime/runs/<mission_id>/<run_id>
python scripts/run_mission.py path/to/mission.yaml \
  --resume runtime/runs/<mission_id>/<run_id>
```

`--max-parallel N` runs independent ready jobs in separate tabs (1–16; default 1). Use `--retry-failed` only when intentionally retrying failed/blocked jobs. Completed jobs are never re-run during resume. A per-run `.runner.lock` prevents two processes from resuming one run simultaneously. If the process is killed, inspect the recorded PID before removing a stale lock; never delete it while a runner is active. Ambiguous or in-flight submissions are inspected before anything can be submitted again; if the saved conversation does not prove whether a click succeeded, the job waits for a human rather than risking a duplicate.

Job states are `queued`, `running`, `completed`, `failed`, `blocked`, and `waiting_for_human`. A failed dependency blocks its descendants; independent siblings may still finish. Each response artifact is the exact visible text isolated from the assistant's message region, with its SHA-256 and UI model label recorded in provenance. The Arena adapter does not rewrite assistant content or strip model-generated code fences. Arena UI labels are outside the extracted assistant message; if a label or transcript wrapper is supplied separately, record it in the intake/provenance rather than treating it as response prose.

## Arena behavior and limits

Reconnaissance identified the public Direct route as `https://arena.ai/text/direct`, currently resolving to `?model_a=max` and displaying the label “Max”. Arena's official help says the model selector is used in Direct mode. Public page fetching did **not** expose the live accessibility tree, so this adapter's textbox, selector, upload, submit, and message-region matching are deliberately not claimed to be verified. It resolves semantic accessible roles and exact visible names at run time. If one unique control/message boundary is not available, it records a screenshot and waits for a person; it does not guess a CSS selector, bypass CAPTCHA, scrape private APIs, or infer that a response is complete from a short pause alone.

The Direct adapter currently expects one unique chat textbox, a uniquely identifiable configured model, a native file input (when attachments are declared), and distinct ARIA `article` regions for the submitted prompt and following response. Completion is a conservative local UI heuristic: the response article must remain unchanged across four polls, the composer must be enabled, and no visible stop/cancel control may be present. This is not a server-confirmed completion state; if those UI signals are absent or inconsistent, the job waits for human inspection. If Arena changes its accessibility structure, it will stop at the uncertain stage for manual inspection. This first slice runs one Direct conversation per job; it does not automate Side-by-Side, so capture of two paired answers is not yet supported by this adapter. The observed public route and model label are reconnaissance facts, not a guarantee that every account, model, upload format, or current UI behaves the same way.

## Inert campaign example

`../examples/campaign-analysis.yaml` demonstrates one ingest job followed by four independent Council-role jobs. The prompts are explicit placeholders that prohibit campaign analysis. The referenced `atria-campaign-state-56.zip` is not staged in this checkout. This example was not executed; do not run it or upload any Atria material until campaign analysis is explicitly authorized and its input has been reviewed/staged. The example is kept separate from Mission 04, which remains on HOLD with Gate 1 unapproved.

## Verification

Deterministic tests use a fake executor/browser boundary and do not contact Arena. Run them with:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests/test_runtime_engine.py tests/test_arena_adapter.py
```

A green test suite does not verify Arena's live DOM/accessibility tree or guarantee UI behavior for your account.

### Latest smoke attempt (2026-10-02)

A temporary, harmless `arena-smoke-test` mission (`Reply with exactly: RUNTIME_OK`, no file inputs) exercised the real runner entry point. It reached `queued -> running` and failed in `BrowserController.start` because the Playwright Chromium executable was absent (`chromium-1243/.../chrome`). The earlier `playwright install chromium` attempt failed with TLS `ECONNRESET` from `cdn.playwright.dev`. The browser never opened, no request reached Arena, no prompt was submitted, and no response artifact was produced. **There is still zero live evidence for Arena selectors or response extraction.** The real adapter should be exercised cautiously in a signed-in local browser once Chromium is available; stop and report if CAPTCHA, login, unexpected model, upload restrictions, or ambiguous UI appears.
