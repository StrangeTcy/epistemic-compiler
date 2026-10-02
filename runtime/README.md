# Local mission runner

This is a narrow, optional execution utility for the existing compiler. It runs an explicit YAML job DAG through a local persistent Playwright browser profile. It does not define research questions, score evidence, approve gates, revise the protocol, or replace the protocol's human decisions. It has no provider/API adapter; the first site adapter is Arena Direct.

## Browser channel and profile

The default browser channel is `chrome`. Playwright launches the installed stable Google Chrome through its branded-browser support (`channel="chrome"`); the default workflow does **not** require Playwright's downloaded Chromium. The `EPISTEMIC_BROWSER_CHANNEL` environment variable configures the channel for both the login helper and mission runner. Set it to `chromium` to retain/use Playwright's bundled Chromium instead; that option requires `python -m playwright install chromium`. Other Playwright channel names are passed through unchanged.

Each channel/profile pair gets a separate persistent automation profile. With the default channel and profile id `arena`, the directory is `runtime/browser_profiles/chrome-arena/`. It is gitignored because it contains local authenticated site state, including cookies. **This is not your normal Chrome profile.** Do not point the runner at Chrome's regular `User Data` directory, sync this automation profile, or commit/copy it. `browser_login.py arena` and a mission whose site/profile defaults to `arena` resolve to the same directory, so a manually authenticated session can persist between those commands.

## Windows setup and smoke workflow

1. Verify that the Google Chrome desktop application (stable channel) is installed. The runner asks Playwright for channel `chrome`; it does not need a downloaded Playwright Chromium executable.
2. From the repository root, create and activate a virtual environment, then install the runtime packages in PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r runtime/requirements.txt
   ```

3. Open the dedicated, headed Chrome automation profile:

   ```powershell
   python scripts/browser_login.py arena
   ```

   Complete Google/Arena sign-in or any verification **manually** in that browser window. No Google login is automated. Press Enter in the terminal when finished; the browser closes and saves the session in the separate `runtime/browser_profiles/chrome-arena/` profile. The user's normal Chrome profile is not opened or modified.

4. Create a harmless throwaway smoke mission and its prompt file in a temporary directory. The runner requires a `role` and a `prompt_artifact`; prompts are files rather than an inline `prompt` field:

   ```powershell
   $smokeDir = Join-Path $env:TEMP 'arena-smoke-test'
   New-Item -ItemType Directory -Force $smokeDir | Out-Null

   @'
   mission_id: arena-smoke-test
   jobs:
     - id: smoke
       role: smoke
       site: arena
       model: Max
       prompt_artifact: arena-smoke-prompt.md
   '@ | Set-Content -Encoding ascii (Join-Path $smokeDir 'mission.yaml')

   'Reply with exactly: RUNTIME_OK' | Set-Content -Encoding ascii (Join-Path $smokeDir 'arena-smoke-prompt.md')
   ```

5. From the repository root, run the mission. **`scripts/run_mission.py` is the browser-backed mission runner; `browser_login.py` only bootstraps the manual login profile.**

   ```powershell
   python scripts/run_mission.py (Join-Path $smokeDir 'mission.yaml')
   ```

   The runner prints the run directory. Paste that path when prompted to inspect it:

   ```powershell
   $runPath = Read-Host 'Paste the run directory printed by run_mission.py'
   python scripts/inspect_run.py $runPath
   ```

The mission runner reuses the same `chrome-arena` profile by default. If you set `EPISTEMIC_BROWSER_CHANNEL` or pass a different profile id to `browser_login.py`, use the same channel/profile for the mission. If Google/Arena shows a CAPTCHA, security warning, or other login ambiguity, stop for manual handling; do not automate or bypass the login.

For example, to explicitly use Playwright's bundled Chromium instead of installed Chrome, set the channel **before both login and run** and install its browser binary:

```powershell
$env:EPISTEMIC_BROWSER_CHANNEL = 'chromium'
python -m playwright install chromium
```

This selects a separate `chromium-arena` automation profile. Return to installed Chrome with `$env:EPISTEMIC_BROWSER_CHANNEL = 'chrome'` (or clear the variable, since `chrome` is the default). No `executable_path` override is used.

## One-shot execution, unattended worker, and authentication

These are three separate operations:

1. **One-time interactive authentication:** `python scripts/browser_login.py arena` opens the headed, dedicated Chrome profile. The user signs in manually; the script does not automate Google or Arena authentication.
2. **One-shot execution:** `python scripts/run_mission.py path/to/mission.yaml` executes/resumes that explicit mission once and exits. It is the direct command for testing a single run.
3. **Unattended local worker:** `python scripts/worker.py` continuously polls the local inbox and delegates all DAG scheduling/execution to the existing engine. It reuses the same persistent browser profile and sleeps when the inbox has no runnable work.

The worker watches only `.yaml`/`.yml` files placed directly in the gitignored `runtime/queue/` directory; it does not scan or execute `examples/`, including the inert campaign example. Put only explicitly approved mission YAML and its referenced prompt/input files there. A new file is noticed on the next poll. Existing run state is matched by mission id and YAML content hash; completed jobs are not repeated after worker restart. The queue file stays in place and an unchanged completed mission is idempotently skipped; use a fresh mission id for a deliberately new run. For example:

```powershell
# One deterministic scan: process currently runnable work, then exit.
python scripts/worker.py --once

# Keep polling; Ctrl+C records active jobs for safe inspection/resume and stops.
python scripts/worker.py --poll-interval 30 --max-parallel 2 --max-retries 2 --site arena
```

Useful options include `--queue-dir`, `--once`, `--poll-interval`, `--max-parallel`, `--max-retries`, and `--site` (`--provider` is an alias; Arena is the only currently supported site). `--once` also applies the bounded retry policy before exiting. The default policy allows two additional attempts (three attempts total) for failures explicitly marked safe to retry—currently, Playwright navigation timeouts before any prompt interaction—with exponential backoff capped at 60 seconds. Ambiguous UI, CAPTCHA/login, and response-completion uncertainty remain `waiting_for_human` and are never retried automatically. The existing engine continues independent DAG jobs when another job is waiting for a person.

A worker leaves `waiting_for_human` unchanged so it remains externally recoverable. After manually resolving the condition, use the one-shot runner to explicitly resume that run. It will process the saved DAG state; on its next poll the worker reconciles that state and never duplicates completed jobs:

```powershell
python scripts/run_mission.py path/to/mission.yaml --resume runtime/runs/mission-name/exact-run-id
```

Replace both paths with the mission YAML and run directory shown by `inspect_run.py`.

The worker uses `runtime/queue/.worker.lock` to prevent duplicate local workers. On an unclean termination, inspect the recorded PID before removing a stale lock. This is a single-machine queue process, not a distributed daemon, cloud service, or agent swarm; it does not create/approve missions or make research decisions. **Unattended Arena execution has not been live-verified.**

## General setup and manual login

On macOS/Linux, the equivalent setup is:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r runtime/requirements.txt
```

The default channel is still installed `chrome`; no `playwright install chromium` step is needed unless `EPISTEMIC_BROWSER_CHANNEL=chromium` is selected. Open the Arena profile and authenticate manually with:

```bash
python scripts/browser_login.py arena
```

The helper is headed and uses the persistent profile described above. It never reads or prints passwords, cookies, or tokens. If the browser needs login or CAPTCHA verification during a job, the job becomes `waiting_for_human`; use `inspect_run.py` to find the saved URL, reopen it with `python scripts/browser_login.py arena --url 'https://arena.ai/…'`, complete verification manually, close the window with Enter, then resume. The URL option rejects non-HTTPS or non-Arena hosts and embedded credentials. For an ambiguous submit control, inspect the saved prompt/input snapshot and only manually submit if that is explicitly intended; the persisted ambiguous-submission marker prevents a second automatic send.

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

Deterministic tests cover mission execution, worker queue/retry/resume behavior, and browser channel/profile configuration through fake Playwright objects; they do not contact Arena or Google. Run them with:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests/test_browser_config.py tests/test_worker.py tests/test_runtime_engine.py tests/test_arena_adapter.py
```

A green test suite does not verify that Chrome is installed/discovered on a particular Windows host, that Google/Arena permits interactive login in the new profile, that unattended worker operation succeeds, or that Arena's live DOM/accessibility tree matches the adapter.

### Latest smoke attempt (2026-10-02; before Chrome channel support)

A temporary, harmless `arena-smoke-test` mission (`Reply with exactly: RUNTIME_OK`, no file inputs) exercised the real runner entry point. At that time, the default was Playwright's bundled Chromium; the job reached `queued -> running` and failed in `BrowserController.start` because the Chromium executable was absent (`chromium-1243/.../chrome`). The earlier `playwright install chromium` attempt failed with TLS `ECONNRESET` from `cdn.playwright.dev`. The browser never opened, no request reached Arena, no prompt was submitted, and no response artifact was produced. The installed-Chrome channel and local worker are covered only by deterministic mocked configuration/engine tests so far: **no live Google login, Chrome launch, unattended worker session, Arena request, or selector has been verified.**
