#!/usr/bin/env python3
"""Run the campaign's human-gated post-production DAG on the existing runtime.

Typical sequence:
  python scripts/post_workflow.py start
  python scripts/post_workflow.py show
  python scripts/post_workflow.py ingest-pair RUN_ID WRITER_A_JOB WRITER_B_JOB --stdin
  python scripts/post_workflow.py ingest RUN_ID CRITIC_JOB --stdin

Every model call is a manual Battle handoff. Responses are saved as immutable
job artifacts and the existing runtime engine resumes only dependency-ready jobs.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import hashlib
import io
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime import engine  # noqa: E402

ANALYSIS = ROOT / "campaign-01-analysis"
POSTS = ANALYSIS / "posts"
BATTLE = ANALYSIS / "battle"
GENERATED = ANALYSIS / "evidence" / "generated"
WORKFLOW_ROOT = ANALYSIS / "post-production"
SNAPSHOT_ROOT = WORKFLOW_ROOT / "source_snapshots"
MISSION_ID = "campaign-01-post-production"
MISSION_PATH = WORKFLOW_ROOT / "mission.yaml"
PUBLICATION_DATE = "2026-10-03"
POST_IDS = tuple(f"POST-{index:02d}" for index in range(1, 6))
SOURCE_DRAFTS = {
    "POST-01": "POST-01-non-monotone-capability-map.md",
    "POST-02": "POST-02-epistemic-games-bayesian-not-recursive.md",
    "POST-03": "POST-03-category-track-implementation-audit.md",
    "POST-04": "POST-04-what-scalar-scores-conceal.md",
    "POST-05": "POST-05-weird-machines-surface-and-depth.md",
}

WEIRD_MACHINE_ENVIRONMENTS = {
    "ci_dependency_graph",
    "css_state_machine",
    "regex_state_machine",
    "spreadsheet_dataflow",
    "sql_fixed_point",
    "template_interpreter",
}

PROMPT_TEMPLATES: dict[str, str] = {
    "local_prepare_post.md": """Local compiler stage: construct one immutable content packet from every attached input artifact, preserving the source draft, relevant findings, evidence tables, comparator/source audit, limitations, target house style, and verbatim public style-reference excerpts. Do not call a model, change evidence, or modify campaign records. Record the input hashes and trace-row IDs in the compiler-only validator metadata at the end of the packet. The packet is internal and must never be copied into a public post.""",
    "writer.md": """# Independent StrangeTcy research-essay draft — {{POST_ID}}

Write a complete, independently structured public research essay for the requested post. The attached evidence packet contains the selected internal source draft, the relevant finding and claim-trace rows, primary evidence extracts/tables, source-implementation audit, limitations, public reference list, the target house-style note, and **verbatim content from actual StrangeTcy posts**. Read all of it.

The internal draft is an evidence map, not a required outline and not prose to paraphrase. Choose a clear thesis, a distinct opening, a new argument sequence, and examples/notation that make the reasoning easier to inspect. Do not track the draft paragraph by paragraph. Treat the two side-by-side writer responses as independent candidates; do not refer to or imitate another writer.

Evidence rules:
- Do not invent results, sources, citations, replications, causal effects, or implementation details. Keep raw counts, performance-eligible counts, exclusions, judge guarantees, and task/source limitations distinct.
- The campaign records one selected seed per cell. It is one paid Atria-Dawn-Preview campaign; subsequent editorial/model role passes are not independent replications. Do not upgrade a case-level result into a general capability ranking.
- The campaign repository was recorded dirty. The inspected clean source revision is a comparator, not proof of the exact paid-run working tree. Keep that limitation adjacent to source-level claims.
- Distinguish behavioral-reference/exact-instance judgments from compile-only judgments; compile-only results are exploratory and are not a validated behavioral aggregate. Mention the actual judge defects or task/judge mismatches where relevant, and distinguish them from model failures.
- Keep terminal provider failures, pre-scoring omissions, invalid/source-rejected patches, tool-action failures, and judged behavioral failures separate. Do not turn an exclusion into a pass or fail.
- POST-02 is a seven-item Bayesian inference task over stipulated policies, not recursive theory of mind. POST-05's Rule 110 / code-repair examples are bounded task observations, not a claim of Turing completeness or general computation. Category-track outcomes are heterogeneous code-repair results, not a single theorem/capability score.
- Use numerical claims only when the attached evidence supports them; keep denominator and judge mode next to the number. Keep research caveats in the public prose, not only in a footnote.

Style/construction:
- Produce a StrangeTcy essay with an opening that earns the reader's attention, concrete technical detail, varied transitions, and a clear argument. Useful equations, small tables, or a diagram description are welcome only when they clarify the claim.
- Use actual reference-post content for rhythm and structural judgment, but do not copy distinctive sentences, examples, titles, or author-process claims. Do not write generic AI filler, a benchmark report, or a paraphrase of the draft.
- Aim for 1,800–2,500 words. Do not include a preface, critique, notes to an editor, or a code fence around the article.
- Return only the full article as Markdown. It will be edited later by a critic and final writer.
""",
    "critic.md": """# Editorial critic and blueprint — {{POST_ID}}

You receive the evidence packet, Writer A, and Writer B. Do not choose a winner and do not simply merge the two drafts. Build an actionable editorial blueprint for an original final article. Check each dimension explicitly:

1. Conceptual structure and thesis: what is the real argument, what should be moved/cut, and where do the posts' structures diverge?
2. Opening: compare specificity, tension, and how quickly the opening states its limit; propose a fresh opening strategy, not copied prose.
3. Examples and technical depth: are task examples exact, source-grounded, and useful? Are mathematics/tables/diagrams useful or decorative? Specify equations or a compact diagram only when they sharpen the argument.
4. Generic AI prose and benchmark-report tone: identify stock transitions, empty emphasis, overlong setup, unsupported superlatives, or score-led reporting.
5. Transitions and caveat placement: keep each limitation beside the claim it qualifies; retain dirty-source/comparator, judge-mode/defect, provider/exclusion, and one-seed boundaries relevant to this post.
6. Unsupported claims and claim traceability: list exact statements to remove, narrow, or substantiate from the packet. Do not invent evidence or citations.
7. Public-site fit: check StrangeTcy voice against the actual excerpt content, Jekyll frontmatter/date/title, `{% include mathjax.html %}`, the author signature convention, epistemic-status framing, link/Markdown details, and likely layout mismatches.

The final writer must receive a usable blueprint: proposed thesis, opening strategy, section-by-section sequence, example/equation/table plan, A/B elements worth retaining (with reasons), elements neither draft handles well, exact evidence boundaries, and a final quality checklist. Do not draft the complete article. Do not copy author-process claims from reference posts.
""",
    "final_writer.md": """# Final public-post writer — {{POST_ID}}

Synthesize a real, publication-ready StrangeTcy article from the attached evidence dossier, the exact internal source draft, both independently produced drafts, the critic's blueprint, and verbatim content from actual StrangeTcy reference posts. The blueprint is guidance, not a substitute for checking the evidence. You must reconcile it with the sources.

Return only the complete article in Markdown, with no wrapper or commentary. Use the target Jekyll convention:

---
title: "A specific public title"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

Use the site's epistemic-status HTML pattern when useful, but make every authorship/process statement strictly accurate. Do not copy reference-post authorship claims. Do not call internal work a public result.

Requirements:
- Aim for 1,800–2,500 words; lead with an argument, not a campaign summary. Make a StrangeTcy research essay, not a stitched paraphrase or benchmark report.
- Keep exact factual claims, denominators, judge guarantees, exclusions, and evidence status traceable to the dossier. Include the source-comparator/dirty-working-tree limitation, one-seed scope, and judge defects/compile-only caveat where relevant. No invented numbers, results, links, or citations.
- Do not imply independent replication or independent model execution. The campaign is one selected run/seed per cell; role-separated passes do not become replications.
- For POST-02, explicitly say the epistemic-games task is Bayesian inference over stipulated policies and is not recursive ToM. For POST-05, do not imply that a Rule 110 example or bounded code-repair task establishes Turing completeness/general computation. For POST-03, do not present the heterogeneous category track as one validated category-theory score. For POST-01 and POST-04, do not flatten mixed judge modes, terminal provider notes, or failures at different pipeline stages into one capability scalar.
- Keep all research caveats near the claims they qualify. Explain equations and axes in prose; use mathematics, tables, or diagrams only when they add information.
- Use the **actual reference excerpts** to calibrate voice, pacing, and structure. Do not reproduce distinctive phrases/examples. Do not copy any internal trace ID, `F-xx` reference, source path, archive member, internal filename, editor note, or POST/draft label into public copy.
- Use syntactically valid Markdown, links, Jekyll frontmatter/includes, and a specific title that produces a clean slug. Do not add unresolved TODOs/placeholders.
""",
    "post_validator.md": """Local compiler validator: check frontmatter/date/title/slug, the target Jekyll layout/include/signature, Markdown fences and external-link syntax, HTML balance, internal-provenance leakage, article length, all numerical literals against the source/evidence packet, source trace rows and input hashes, independent-replication claims, POST-02 recursive-ToM overclaims, POST-05 Turing-completeness overclaims, and required evidence/judge/source caveats. Return a machine-readable report. A failed report opens one targeted human revision gate; a stylistically different article is not rejected merely for departing from the draft.""",
    "validation_revision.md": """# Targeted validator repair — {{POST_ID}}

The attached local-validator report identifies specific public-copy defects. Repair only those defects while keeping the evidence boundaries intact. The source draft/evidence packet and exact current article are attached. Do not broaden claims, invent facts, change the article merely to imitate the draft, or expose internal trace IDs. Return only the complete corrected Jekyll Markdown article with its frontmatter, include, and site signature. If a reported check appears to be a false positive, make the smallest public-copy adjustment that resolves it without weakening the caveat; the revised response is validated again locally.
""",
    "cross_post_prepare.md": """Local compiler stage: combine the five individually validated public articles, the five relevant finding/evidence dossiers, house-style rules, and actual style-reference excerpts once. Preserve all input snapshots and hashes. Do not revise posts or publish files.""",
    "cross_post_editor.md": """# Cross-post series review

Review the five individually validated public articles together with their finding/evidence records, actual StrangeTcy style excerpts, and house-style conventions. Do not rewrite any article and do not invent a series-level result. Assess:

- duplicate or repetitive arguments and openings; structural similarity that makes the five posts feel like one template;
- conflicting numbers, denominators, benchmark/task descriptions, judge guarantees, or evidence status across posts;
- conceptual-role overlap: preserve each post's distinct job in the series (non-monotone capability map; Bayesian epistemic game, not recursive ToM; category-track implementation audit; what scalar scores conceal; surface/depth weird machines);
- one-seed scope, dirty-source/comparator uncertainty, judge defects, exclusions, provider failures, and unsupported causal/generalization claims;
- notation, equation/term reuse, public Jekyll conventions, transitions, tone, and StrangeTcy voice calibrated from the actual reference content.

Only request a revision where a concrete issue exists. Do not force structural variety by changing a strong opening, rewrite all five, or reject stylistic experimentation solely because it differs from the source draft. Return exactly one strict JSON object (no prose/fences) in this schema:
{"revisions":[{"post_id":"POST-01","needed":false,"issues":[],"change_request":""},{"post_id":"POST-02","needed":false,"issues":[],"change_request":""},{"post_id":"POST-03","needed":false,"issues":[],"change_request":""},{"post_id":"POST-04","needed":false,"issues":[],"change_request":""},{"post_id":"POST-05","needed":false,"issues":[],"change_request":""}]}
Set `needed` true only for a specific cross-post correction. `change_request` must say what to change and what to preserve; do not write replacement prose.
""",
    "cross_post_revision.md": """# Targeted cross-post revision — {{POST_ID}}

The series reviewer requested the attached, limited correction. The full validated five-post series, source/evidence packet for this post, and current article are attached. Revise only the target article enough to resolve the stated cross-post conflict/repetition; retain its distinct conceptual role, strong material, Jekyll conventions, citations, and all evidence limits. Do not rewrite other posts, add unsupported results, or leak internal IDs. Return only the complete target article as valid Jekyll Markdown. It will be run through the local validator again.
""",
    "cross_post_router.md": """Local compiler stage: parse the cross-post editor's strict JSON, normalize all five post decisions, reject unknown/duplicate post IDs or malformed requests, and produce a deterministic revision plan. Do not reinterpret or silently discard issues.""",
    "final_post_set_assembler.md": """Local compiler stage: require five final validator reports marked valid; create an internal export manifest with each public article's title/date/slug, immutable runtime artifact path and hash, source trace-row IDs, and validation report path. Do not copy into a Jekyll repository, commit, or push.""",
}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _ensure_immutable(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(
                f"workflow source snapshot already exists with different bytes: {path}; "
                "do not replace inputs for an existing mission/run"
            )
        return
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        if path.read_bytes() == data:
            return
        raise RuntimeError(f"source snapshot was concurrently changed: {path}")
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def _csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def _render_csv(headers: list[str], rows: Iterable[dict[str, Any]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=headers, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def _selected_case_fields(source: Path, predicate: Any) -> bytes:
    headers, rows = _csv_rows(source)
    columns = [
        "case_id", "environment", "track", "analysis_family", "seed",
        "difficulty_levels", "judge_guarantee", "status", "verdict", "score",
        "failure_mode_raw", "failure_mode_normalized", "final_notes", "final_metrics",
        "performance_eligible", "exclusion_reason",
    ]
    selected = [row for row in rows if predicate(row)]
    return _render_csv([name for name in columns if name in headers], selected)


def _selected_axis_fields(source: Path, environments: set[str]) -> bytes:
    headers, rows = _csv_rows(source)
    selected = [row for row in rows if row.get("environment") in environments]
    return _render_csv(headers, selected)


def _selected_failure_fields(source: Path, predicate: Any) -> bytes:
    headers, rows = _csv_rows(source)
    columns = [
        "case_id", "environment", "analysis_family", "recorded_track",
        "judge_guarantee", "performance_eligible", "exclusion_reason", "score",
        "failure_mode_raw", "final_notes", "final_metrics",
    ]
    selected = [row for row in rows if predicate(row)]
    return _render_csv([name for name in columns if name in headers], selected)


def _source_audit_excerpt(post_id: str) -> bytes:
    source_path = ANALYSIS / "evidence" / "source_implementation_audit.md"
    text = source_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    # Keep the source-identity/scope context, then only the post-relevant audited
    # implementation sections. These excerpts are source material, not new claims.
    keep_sections = {
        "POST-01": ("### Weird-machine tasks", "### Recurrent depth"),
        "POST-02": ("### Epistemic games",),
        "POST-03": ("### Category-theoretic/compositional track", "### Nominal axes"),
        "POST-04": ("## Family summary", "## Post and claim links"),
        "POST-05": ("### Weird-machine tasks",),
    }[post_id]
    heading_positions = [i for i, line in enumerate(lines) if line.startswith("#")]
    sections: list[tuple[int, int, str]] = []
    for offset, start in enumerate(heading_positions):
        end = heading_positions[offset + 1] if offset + 1 < len(heading_positions) else len(lines)
        sections.append((start, end, lines[start]))
    selected: list[str] = []
    for start, end, heading in sections:
        if heading in {"## Scope and source identity", "## What the campaign actually sampled"}:
            selected.extend(lines[start:end])
        elif any(heading.startswith(prefix) for prefix in keep_sections):
            selected.extend(lines[start:end])
    if not selected:
        raise RuntimeError(f"could not build source-audit excerpt for {post_id}")
    return ("# Source implementation audit excerpt\n\n" + "\n".join(selected).strip() + "\n").encode("utf-8")


def _campaign_scope_json(audit: dict[str, Any], *, include_usage: bool) -> bytes:
    campaign = audit.get("campaign", {})
    archive = audit.get("archive", {})
    selected_campaign_keys = (
        "campaign_progress_episodes_completed", "campaign_progress_episodes_total",
        "campaign_status_report", "compile_only_cases", "exact_instance_oracle_cases",
        "explicit_omission_count_known_gate_blocked", "explicit_omission_count_unsupported_modality",
        "explicit_omission_total", "known_gate_blocked_disposition", "max_steps",
        "max_tokens_per_call", "mode_summary", "omitted_unsupported_case_count",
        "performance_eligible_case_count", "performance_eligible_pass_rate_descriptive_mixed_modes",
        "performance_eligible_verdict_counts", "provider_failure_case_count_from_final_result_notes",
        "provider_failure_case_ids_from_final_result_notes", "raw_verdict_counts",
        "reasoning_enabled_config", "recorded_results_plus_reported_omissions",
        "recorded_track_label_mismatch_case_ids", "registry_environment_count",
        "repository_dirty_at_run", "selected_case_count_manifest", "selected_case_count_results",
        "selected_environment_count", "temperature", "top_p",
    )
    result: dict[str, Any] = {
        "archive": {key: archive.get(key) for key in ("archive_ref", "archive_sha256", "member_count")},
        "campaign": {key: campaign.get(key) for key in selected_campaign_keys if key in campaign},
        "failure_taxonomy_all_recorded_failures": audit.get("failure_taxonomy_all_recorded_failures", {}),
        "failure_taxonomy_performance_eligible": audit.get("failure_taxonomy_performance_eligible", {}),
    }
    if include_usage:
        result["execution_and_usage"] = audit.get("execution_and_usage", {})
        result["api_cost_or_spend"] = audit.get("execution_and_usage", {}).get("api_cost_or_spend")
    return (json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _snapshot_sources() -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
    """Freeze only requested drafts and relevant audited source materials."""
    if set(SOURCE_DRAFTS) != set(POST_IDS):
        raise RuntimeError("source draft map must list all five requested posts")
    inputs: dict[str, str] = {}
    ledger: dict[str, dict[str, Any]] = {}

    def snapshot(key: str, relative_path: Path, data: bytes, source: Path | None = None) -> None:
        destination = SNAPSHOT_ROOT / relative_path
        _ensure_immutable(destination, data)
        inputs[key] = destination.relative_to(WORKFLOW_ROOT).as_posix()
        ledger[key] = {
            "snapshot": destination.relative_to(WORKFLOW_ROOT).as_posix(),
            "snapshot_sha256": _sha256(data),
            "snapshot_bytes": len(data),
            "source_path": str(source.relative_to(ROOT)) if source and source.is_relative_to(ROOT) else str(source or "generated"),
            "source_sha256": _sha256(source.read_bytes()) if source and source.is_file() else None,
        }

    shared_sources = {
        "house_style": POSTS / "HOUSE_STYLE.md",
        "style_reference_material": WORKFLOW_ROOT / "style_reference_material.md",
        "references": ANALYSIS / "sources" / "references.md",
        "campaign_provenance": ANALYSIS / "evidence" / "PROVENANCE.md",
    }
    for key, source in shared_sources.items():
        if not source.is_file():
            raise FileNotFoundError(f"required shared workflow input is missing: {source}")
        snapshot(key, Path("shared") / f"{key}.md", source.read_bytes(), source)

    _, trace_rows = _csv_rows(POSTS / "claim_traceability.csv")
    finding_registry = json.loads((ANALYSIS / "findings" / "findings.json").read_text(encoding="utf-8"))
    finding_by_id = {row.get("id"): row for row in finding_registry.get("findings", [])}
    audit_path = GENERATED / "audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    case_source = GENERATED / "case_results.csv"
    axis_source = GENERATED / "axis_summary.csv"
    failure_source = GENERATED / "failure_details.csv"
    placeholder_source = GENERATED / "axis_placeholder_audit.csv"
    environment_source = GENERATED / "environment_summary.csv"
    family_source = GENERATED / "analysis_family_summary.csv"
    taxonomy_source = GENERATED / "failure_taxonomy.csv"
    exclusions_source = GENERATED / "campaign_exclusions.csv"
    track_source = GENERATED / "track_summary.csv"

    for post_id, draft_filename in SOURCE_DRAFTS.items():
        post_dir = Path(post_id)
        draft_source = POSTS / draft_filename
        battle_dir = BATTLE / post_id
        required = [draft_source, battle_dir / "relevant_findings.json", battle_dir / "evidence_extract.md", battle_dir / "LIMITATIONS.md", battle_dir / "evidence" / "source_implementation_audit.md"]
        for required_path in required:
            if not required_path.is_file():
                raise FileNotFoundError(f"required {post_id} workflow input is missing: {required_path}")
        snapshot(f"source_draft_{post_id}", post_dir / "source_draft.md", draft_source.read_bytes(), draft_source)
        relevant_json = json.loads((battle_dir / "relevant_findings.json").read_text(encoding="utf-8"))
        post_claims = [row for row in trace_rows if row.get("post_id") == post_id]
        claim_ids = {row.get("claim_id") for row in post_claims}
        finding_ids = {finding_id for row in post_claims for finding_id in row.get("finding_ids", "").split(";") if finding_id}
        # Prefer the existing post dossier when it is present; also freeze the exact
        # claim-trace rows independently so validation is not tied to its prose.
        trace_columns = [
            "post_id", "claim_id", "claim_summary", "finding_ids",
            "finding_quantitative_results", "generated_evidence_artifacts",
            "source_comparator_paths", "source_identity_qualifier", "external_references",
        ]
        trace_bytes = _render_csv(trace_columns, post_claims)
        snapshot(f"trace_rows_{post_id}", post_dir / "trace_rows.csv", trace_bytes)
        dossier_finding_ids = {row.get("id") for row in relevant_json.get("findings", []) if row.get("id")}
        all_finding_ids = sorted(finding_ids | dossier_finding_ids)
        missing_registry_ids = sorted(set(all_finding_ids) - set(finding_by_id))
        if missing_registry_ids:
            raise RuntimeError(f"finding registry is missing IDs for {post_id}: {missing_registry_ids}")
        findings_packet = {
            "schema_version": 1,
            "post_id": post_id,
            "claim_ids": sorted(claim_ids),
            "trace_finding_ids": sorted(finding_ids),
            "battle_dossier_finding_ids": sorted(dossier_finding_ids),
            "finding_id_reconciliation": {
                "trace_rows_not_in_battle_dossier": sorted(finding_ids - dossier_finding_ids),
                "battle_dossier_not_in_trace_rows": sorted(dossier_finding_ids - finding_ids),
            },
            "findings": [finding_by_id[fid] for fid in all_finding_ids],
            "existing_battle_dossier": relevant_json,
        }
        findings_bytes = (json.dumps(findings_packet, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
        snapshot(f"relevant_findings_{post_id}", post_dir / "relevant_findings.json", findings_bytes, battle_dir / "relevant_findings.json")
        for key, source, filename in (
            (f"evidence_extract_{post_id}", battle_dir / "evidence_extract.md", "evidence_extract.md"),
            (f"limitations_{post_id}", battle_dir / "LIMITATIONS.md", "limitations.md"),
        ):
            snapshot(key, post_dir / filename, source.read_bytes(), source)
        audit_bytes = _source_audit_excerpt(post_id)
        snapshot(f"source_audit_{post_id}", post_dir / "source_audit_excerpt.md", audit_bytes, ANALYSIS / "evidence" / "source_implementation_audit.md")

        if post_id == "POST-01":
            keep_envs = WEIRD_MACHINE_ENVIRONMENTS | {"moco", "rd_adaptive_halting", "rd_gradient_credit", "rd_state_carry"}
            case_predicate = lambda row, envs=keep_envs: row.get("environment") in envs
            selected_axis_envs = keep_envs
        elif post_id == "POST-02":
            keep_envs = {"epistemic_games"}
            case_predicate = lambda row: row.get("analysis_family") == "epistemic_games"
            selected_axis_envs = keep_envs
        elif post_id == "POST-03":
            keep_envs = {"categorical_lenses", "compositional_optimizer", "sheaf_physical_constraints"}
            case_predicate = lambda row, envs=keep_envs: row.get("environment") in envs
            selected_axis_envs = {row.get("environment", "") for row in _csv_rows(axis_source)[1] if row.get("track") == "category_theoretic_compositional"}
        elif post_id == "POST-04":
            keep_envs = set()
            case_predicate = lambda row: False
            selected_axis_envs = set()
        else:
            keep_envs = WEIRD_MACHINE_ENVIRONMENTS
            case_predicate = lambda row: row.get("analysis_family") == "weird_machine"
            selected_axis_envs = keep_envs

        case_bytes = _selected_case_fields(case_source, case_predicate)
        snapshot(f"evidence_case_results_{post_id}", post_dir / "evidence" / "selected_case_results.csv", case_bytes, case_source)
        env_rows = _csv_rows(environment_source)[1]
        family_rows = _csv_rows(family_source)[1]
        if post_id == "POST-02":
            env_rows = [row for row in env_rows if row.get("environment") == "epistemic_games"]
            family_rows = [row for row in family_rows if row.get("analysis_family") == "epistemic_games"]
        elif post_id == "POST-03":
            env_rows = [row for row in env_rows if row.get("environment") in {"categorical_lenses", "compositional_optimizer", "sheaf_physical_constraints"}]
            family_rows = [row for row in family_rows if row.get("analysis_family") == "category_theoretic_compositional"]
        elif post_id == "POST-05":
            env_rows = [row for row in env_rows if row.get("environment") in WEIRD_MACHINE_ENVIRONMENTS]
            family_rows = [row for row in family_rows if row.get("analysis_family") == "weird_machine"]
        elif post_id == "POST-01":
            family_rows = [row for row in family_rows if row.get("analysis_family") in {"weird_machine", "ml_debugging", "recurrent_depth_behavioral"}]
        elif post_id == "POST-04":
            family_rows = []
        snapshot(f"evidence_environment_summary_{post_id}", post_dir / "evidence" / "environment_summary.csv", _render_csv(_csv_rows(environment_source)[0], env_rows), environment_source)
        snapshot(f"evidence_analysis_family_summary_{post_id}", post_dir / "evidence" / "analysis_family_summary.csv", _render_csv(_csv_rows(family_source)[0], family_rows), family_source)
        snapshot(f"evidence_failure_taxonomy_{post_id}", post_dir / "evidence" / "failure_taxonomy.csv", taxonomy_source.read_bytes(), taxonomy_source)

        if selected_axis_envs:
            snapshot(f"evidence_axis_summary_{post_id}", post_dir / "evidence" / "axis_summary.csv", _selected_axis_fields(axis_source, selected_axis_envs), axis_source)
        if post_id in {"POST-01", "POST-04"}:
            snapshot(f"evidence_campaign_exclusions_{post_id}", post_dir / "evidence" / "campaign_exclusions.csv", exclusions_source.read_bytes(), exclusions_source)
        if post_id == "POST-03":
            headers, rows = _csv_rows(placeholder_source)
            selected = [row for row in rows if "/cat_theo/" in row.get("config_path", "")]
            snapshot(f"evidence_axis_placeholder_audit_{post_id}", post_dir / "evidence" / "axis_placeholder_audit.csv", _render_csv(headers, selected), placeholder_source)
            headers, rows = _csv_rows(track_source)
            rows = [row for row in rows if row.get("track") == "category_theoretic_compositional"]
            snapshot(f"evidence_track_summary_{post_id}", post_dir / "evidence" / "track_summary.csv", _render_csv(headers, rows), track_source)
        if post_id in {"POST-01", "POST-04", "POST-05"}:
            predicate = lambda row, envs=keep_envs: row.get("environment") in envs
            if post_id == "POST-04":
                predicate = lambda row: True
            elif post_id == "POST-05":
                predicate = lambda row: row.get("analysis_family") == "weird_machine"
            snapshot(f"evidence_failure_details_{post_id}", post_dir / "evidence" / "failure_details.csv", _selected_failure_fields(failure_source, predicate), failure_source)
        if post_id in {"POST-01", "POST-04", "POST-05"}:
            if post_id == "POST-01":
                scoped = _campaign_scope_json(audit, include_usage=False)
            elif post_id == "POST-04":
                scoped = _campaign_scope_json(audit, include_usage=True)
            else:
                scoped = _campaign_scope_json(audit, include_usage=False)
            snapshot(f"evidence_campaign_scope_{post_id}", post_dir / "evidence" / "campaign_scope.json", scoped, audit_path)

    manifest = {
        "schema_version": 1,
        "workflow_id": MISSION_ID,
        "publication_date": PUBLICATION_DATE,
        "requested_source_drafts": SOURCE_DRAFTS,
        "reference_material": {
            "file": "style_reference_material.md",
            "source_commit": "bcc89c392920b3be172a27eec10ad205b58d4fa3",
            "sha256": _sha256((WORKFLOW_ROOT / "style_reference_material.md").read_bytes()),
        },
        "snapshots": ledger,
        "constraints": [
            "No Atria campaign rerun or evidence rewrite",
            "No Mission 01/04 edits",
            "No public export until all five validators and cross-post review pass",
            "No automatic push",
        ],
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    snapshot("workflow_input_manifest", Path("shared") / "workflow_input_manifest.json", manifest_bytes)
    return inputs, ledger


def _prompt_files() -> None:
    for name, content in PROMPT_TEMPLATES.items():
        _ensure_immutable(WORKFLOW_ROOT / "prompts" / name, (content.rstrip() + "\n").encode("utf-8"))


def _job(job_id: str, role: str, site: str, prompt: str, inputs: list[str], dependencies: list[str]) -> dict[str, Any]:
    return {
        "id": job_id,
        "role": role,
        "site": site,
        "prompt_artifact": f"prompts/{prompt}",
        "input_artifacts": inputs,
        "dependencies": dependencies,
        "output_artifact": f"artifacts/jobs/{job_id}/response.md",
        "timeout_seconds": 300,
    }


def _build_mission(inputs: dict[str, str]) -> dict[str, Any]:
    jobs: list[dict[str, Any]] = []
    last_validator_job: str | None = None
    post_job_ids: dict[str, dict[str, str]] = {}
    for post_id in POST_IDS:
        short = post_id.replace("-", "").lower()
        prepare = f"{short}_prepare_post"
        writer_a = f"{short}_battle_writer_a"
        writer_b = f"{short}_battle_writer_b"
        critic = f"{short}_editorial_critic"
        final_writer = f"{short}_final_writer"
        validator = f"{short}_post_validator"
        validation_revision = f"{short}_validation_revision"
        revision_validator = f"{short}_validation_revision_validator"
        prepare_inputs = [
            f"mission:source_draft_{post_id}",
            "mission:house_style",
            "mission:style_reference_material",
            "mission:references",
            "mission:campaign_provenance",
            "mission:workflow_input_manifest",
            f"mission:trace_rows_{post_id}",
            f"mission:relevant_findings_{post_id}",
            f"mission:evidence_extract_{post_id}",
            f"mission:limitations_{post_id}",
            f"mission:source_audit_{post_id}",
        ]
        evidence_keys = sorted(key for key in inputs if key.startswith("evidence_") and key.endswith(post_id))
        prepare_inputs.extend(
            f"mission:{key}" for key in evidence_keys
            if f"mission:{key}" not in prepare_inputs
        )
        prepare_deps = [last_validator_job] if last_validator_job else []
        jobs.append(_job(prepare, "prepare_post", "local", "local_prepare_post.md", prepare_inputs, prepare_deps))
        jobs.append(_job(writer_a, "battle_writer_a", "manual", "writer.md", [f"job:{prepare}:response"], [prepare]))
        jobs.append(_job(writer_b, "battle_writer_b", "manual", "writer.md", [f"job:{prepare}:response"], [prepare]))
        jobs.append(_job(critic, "editorial_critic", "manual", "critic.md", [f"job:{prepare}:response", f"job:{writer_a}:response", f"job:{writer_b}:response"], [prepare, writer_a, writer_b]))
        jobs.append(_job(final_writer, "final_writer", "manual", "final_writer.md", [f"job:{prepare}:response", f"job:{writer_a}:response", f"job:{writer_b}:response", f"job:{critic}:response"], [prepare, writer_a, writer_b, critic]))
        jobs.append(_job(validator, "post_validator", "local", "post_validator.md", [f"job:{final_writer}:response", f"job:{prepare}:response"], [final_writer, prepare]))
        jobs.append(_job(validation_revision, "validation_revision", "manual", "validation_revision.md", [f"job:{validator}:response", f"job:{final_writer}:response", f"job:{prepare}:response"], [validator, final_writer, prepare]))
        jobs.append(_job(revision_validator, "validation_revision_validator", "local", "post_validator.md", [f"job:{validation_revision}:response", f"job:{prepare}:response"], [validation_revision, prepare]))
        post_job_ids[post_id] = {
            "prepare": prepare,
            "writer_a": writer_a,
            "writer_b": writer_b,
            "critic": critic,
            "final_writer": final_writer,
            "validator": validator,
            "validation_revision": validation_revision,
            "revision_validator": revision_validator,
        }
        last_validator_job = revision_validator

    cross_prepare = "cross_post_prepare"
    cross_inputs = ["mission:style_reference_material", "mission:house_style"]
    for post_id in POST_IDS:
        cross_inputs.extend([
            f"job:{post_job_ids[post_id]['validation_revision']}:response",
            f"mission:relevant_findings_{post_id}",
            f"mission:evidence_extract_{post_id}",
            f"mission:limitations_{post_id}",
        ])
    cross_dependencies = [
        job_id
        for post_id in POST_IDS
        for job_id in (post_job_ids[post_id]["revision_validator"], post_job_ids[post_id]["validation_revision"])
    ]
    jobs.append(_job(cross_prepare, "prepare_cross_post", "local", "cross_post_prepare.md", cross_inputs, cross_dependencies))
    cross_editor = "cross_post_editor"
    jobs.append(_job(cross_editor, "cross_post_editor", "manual", "cross_post_editor.md", [f"job:{cross_prepare}:response"], [cross_prepare]))
    router = "cross_post_review_router"
    jobs.append(_job(router, "cross_post_review_router", "local", "cross_post_router.md", [f"job:{cross_editor}:response"], [cross_editor]))

    cross_revision_validators: list[str] = []
    cross_revision_jobs: list[str] = []
    for post_id in POST_IDS:
        short = post_id.replace("-", "").lower()
        revision = f"{short}_cross_post_revision"
        validator = f"{short}_cross_post_revision_validator"
        prior_article = f"job:{post_job_ids[post_id]['validation_revision']}:response"
        jobs.append(_job(revision, "cross_post_revision", "manual", "cross_post_revision.md", [f"job:{router}:response", prior_article, f"job:{post_job_ids[post_id]['prepare']}:response", f"job:{cross_prepare}:response"], [router, post_job_ids[post_id]["revision_validator"], post_job_ids[post_id]["validation_revision"], post_job_ids[post_id]["prepare"], cross_prepare]))
        jobs.append(_job(validator, "cross_post_revision_validator", "local", "post_validator.md", [f"job:{revision}:response", f"job:{post_job_ids[post_id]['prepare']}:response"], [revision, post_job_ids[post_id]["prepare"]]))
        cross_revision_validators.append(validator)
        cross_revision_jobs.append(revision)

    assemble_inputs: list[str] = []
    for post_id in POST_IDS:
        short = post_id.replace("-", "").lower()
        assemble_inputs.extend([f"job:{short}_cross_post_revision:response", f"job:{short}_cross_post_revision_validator:response"])
    jobs.append(_job("final_post_set_assembler", "final_post_set_assembler", "local", "final_post_set_assembler.md", assemble_inputs, [*cross_revision_validators, *cross_revision_jobs]))
    return {
        "mission_id": MISSION_ID,
        "type": "campaign-post-production",
        "inputs": inputs,
        "defaults": {"site": "local", "timeout_seconds": 300},
        "jobs": jobs,
    }


def _yaml_bytes(value: dict[str, Any]) -> bytes:
    return yaml_safe_dump(value).encode("utf-8")


def yaml_safe_dump(value: dict[str, Any]) -> str:
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - engine already depends on PyYAML
        raise RuntimeError("PyYAML is required to build the post-production mission") from exc
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def ensure_workflow() -> Path:
    if not WORKFLOW_ROOT.is_dir():
        raise FileNotFoundError(f"post-production directory not found: {WORKFLOW_ROOT}")
    _prompt_files()
    if MISSION_PATH.is_file():
        # Once the mission and source snapshots exist, they are the immutable
        # inputs for every run. Do not re-read mutable campaign working files or
        # attempt to rebuild an existing mission during start/resume.
        engine.load_mission(MISSION_PATH)
        return MISSION_PATH
    inputs, _ = _snapshot_sources()
    mission_bytes = _yaml_bytes(_build_mission(inputs))
    _ensure_immutable(MISSION_PATH, mission_bytes)
    # Parse before a run is created so malformed references cannot produce a
    # partial mission state.
    engine.load_mission(MISSION_PATH)
    return MISSION_PATH


def _run_dir_for(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if path.is_dir() and (path / engine.STATE_FILE).is_file():
        return path.resolve()
    candidates = sorted((engine.RUN_ROOT / MISSION_ID).glob(f"{value}*"), key=lambda item: item.stat().st_mtime, reverse=True)
    candidates = [candidate for candidate in candidates if (candidate / engine.STATE_FILE).is_file()]
    if not candidates:
        raise FileNotFoundError(f"no saved post-production run matches {value!r}")
    if len(candidates) > 1 and candidates[0].name == value:
        return candidates[0]
    if len(candidates) > 1 and value not in {candidate.name for candidate in candidates}:
        raise ValueError(f"run selector {value!r} is ambiguous; pass a full run ID or directory")
    return candidates[0]


def _latest_run() -> Path | None:
    parent = engine.RUN_ROOT / MISSION_ID
    if not parent.is_dir():
        return None
    candidates = [path for path in parent.iterdir() if path.is_dir() and (path / engine.STATE_FILE).is_file()]
    return max(candidates, key=lambda path: path.stat().st_mtime) if candidates else None


def _load_state(run_dir: Path) -> dict[str, Any]:
    return json.loads((run_dir / engine.STATE_FILE).read_text(encoding="utf-8"))


def _pending_handoffs(run_dir: Path, state: dict[str, Any]) -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    result: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for job_id, job_state in state.get("jobs", {}).items():
        if job_state.get("status") != "waiting_for_human":
            continue
        interaction = job_state.get("interaction", {})
        handoff_path = run_dir / interaction.get("handoff_json", "")
        if not handoff_path.is_file():
            continue
        try:
            handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        result.append((job_id, job_state, handoff))
    return result


def _print_status(run_dir: Path, state: dict[str, Any], *, include_prompts: bool = False, job_filter: str | None = None) -> None:
    print(f"Run: {run_dir.name}")
    print(f"Status: {state.get('run_status', 'unknown')}")
    print("Jobs:")
    for job_id, job_state in state["jobs"].items():
        if job_filter and job_filter not in job_id:
            continue
        print(f"  {job_id}: {job_state['status']}")
    handoffs = _pending_handoffs(run_dir, state)
    if job_filter:
        handoffs = [item for item in handoffs if job_filter in item[0]]
    if not handoffs:
        return
    print("\nPending Battle handoffs (not auto-submitted):")
    for job_id, _job_state, handoff in handoffs:
        print(f"\n  {handoff.get('post_id') or 'CROSS-POST'} / {handoff.get('role')} ({job_id})")
        print(f"    Next stage: {handoff.get('next_stage')}")
        print(f"    Exact prompt: {run_dir / handoff['prompt_to_paste']}")
        print(f"    Prompt SHA-256: {handoff.get('prompt_sha256')}")
        print(f"    Expected response artifact: {run_dir / handoff['expected_response_artifact']}")
        print(f"    Ingest: python scripts/post_workflow.py ingest {run_dir.name} {job_id} --stdin")
        if include_prompts:
            prompt = (run_dir / handoff["prompt_to_paste"]).read_text(encoding="utf-8")
            print("\n----- EXACT PROMPT TO PASTE INTO BATTLE -----\n")
            print(prompt, end="" if prompt.endswith("\n") else "\n")
            print("\n----- END EXACT PROMPT -----")

    # Side-by-side Writer A/B are two distinct waiting jobs with identical prompt
    # and attachment hashes. Give the no-renaming pair-ingest shortcut.
    waiting_by_post: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for job_id, _state, handoff in handoffs:
        if handoff.get("role") in {"battle_writer_a", "battle_writer_b"}:
            waiting_by_post.setdefault(str(handoff.get("post_id")), []).append((job_id, handoff))
    for post_id, pair in waiting_by_post.items():
        if len(pair) == 2 and pair[0][1].get("prompt_sha256") == pair[1][1].get("prompt_sha256") and [item.get("sha256") for item in pair[0][1].get("inputs", [])] == [item.get("sha256") for item in pair[1][1].get("inputs", [])]:
            writer_a = next(job_id for job_id, item in pair if item.get("role") == "battle_writer_a")
            writer_b = next(job_id for job_id, item in pair if item.get("role") == "battle_writer_b")
            print(f"\n  Side-by-side shortcut for {post_id}: paste either identical writer prompt once; save both Arena answers with:")
            print(f"    python scripts/post_workflow.py ingest-pair {run_dir.name} {writer_a} {writer_b} --stdin")


def _read_stdin_pair() -> tuple[str, str]:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("--stdin for ingest-pair expects a JSON object with 'left' and 'right' response strings") from exc
    if not isinstance(payload, dict):
        raise ValueError("pair response must be a JSON object")
    left = payload.get("left", payload.get("writer_a"))
    right = payload.get("right", payload.get("writer_b"))
    if not isinstance(left, str) or not isinstance(right, str) or not left.strip() or not right.strip():
        raise ValueError("pair JSON must contain non-empty string values 'left' and 'right'")
    return left, right


def _ingest_one(run_dir: Path, job_id: str, response_bytes: bytes, model_label: str | None) -> dict[str, Any]:
    return engine.ingest_human_response(run_dir, job_id, response_bytes, model_label=model_label)


def _resume_after_ingest(run_dir: Path) -> tuple[Path, dict[str, Any]]:
    state = _load_state(run_dir)
    mission_path = Path(state.get("mission_path", MISSION_PATH)).resolve()
    return asyncio.run(
        engine.run_mission(
            mission_path,
            resume_dir=run_dir,
            resume_waiting_for_human=False,
            max_parallel=2,
        )
    )


def _source_job_response(run_dir: Path, state: dict[str, Any], job_id: str) -> Path:
    job_state = state.get("jobs", {}).get(job_id)
    if not job_state or job_state.get("status") != "completed":
        raise ValueError(f"final export is unavailable: {job_id} is not completed")
    artifact = job_state.get("output_artifact")
    if not artifact:
        raise ValueError(f"completed job {job_id} has no response artifact")
    path = (run_dir / artifact).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def _export_preview(run_dir: Path) -> Path:
    """Create isolated _posts exports after all five final validators pass."""
    state = _load_state(run_dir)
    manifest_path = _source_job_response(run_dir, state, "final_post_set_assembler")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "validated_internal_export_manifest":
        raise ValueError("assembler output is not a validated export manifest")
    export_root = WORKFLOW_ROOT / "exports" / run_dir.name
    posts_dir = export_root / "_posts"
    for post in manifest.get("posts", []):
        source_artifact = post.get("article_source_artifact", "")
        match = source_artifact.removeprefix("job:").removesuffix(":response")
        source = _source_job_response(run_dir, state, match)
        article = source.read_bytes()
        if _sha256(article) != post.get("article_sha256"):
            raise ValueError(f"final artifact hash changed for {post.get('post_id')}")
        report_path = _source_job_response(run_dir, state, post.get("validation_report_artifact", "").removeprefix("job:").removesuffix(":response"))
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if report.get("valid") is not True:
            raise ValueError(f"{post.get('post_id')} failed final validation")
        target = posts_dir / post["suggested_jekyll_filename"]
        _ensure_immutable(target, article)
    export_manifest = {
        "schema_version": 1,
        "workflow_id": MISSION_ID,
        "run_id": run_dir.name,
        "source_final_manifest": str(manifest_path.relative_to(run_dir)),
        "source_final_manifest_sha256": _sha256(manifest_path.read_bytes()),
        "export_directory": str(export_root),
        "posts": manifest["posts"],
        "commit_performed": False,
        "push_performed": False,
    }
    export_manifest_path = export_root / "export_manifest.json"
    _ensure_immutable(export_manifest_path, (json.dumps(export_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    return export_root


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True, timeout=120)
    return result.stdout.strip()


def _show_exact_prompt(run_dir: Path, job_id: str) -> int:
    state = _load_state(run_dir)
    handoffs = {job: handoff for job, _, handoff in _pending_handoffs(run_dir, state)}
    if job_id not in handoffs:
        raise ValueError(f"job {job_id} has no pending model-response handoff")
    handoff = handoffs[job_id]
    prompt_path = run_dir / handoff["prompt_to_paste"]
    prompt_bytes = prompt_path.read_bytes()
    if _sha256(prompt_bytes) != handoff.get("prompt_sha256"):
        raise ValueError("saved prompt checksum does not match handoff record")
    print(prompt_bytes.decode("utf-8"), end="" if prompt_bytes.endswith(b"\n") else "\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="snapshot the five requested drafts and start/resume the DAG")
    start_parser.add_argument("campaign", nargs="?", default="campaign-01-analysis", help="campaign folder (currently campaign-01-analysis)")

    status_parser = subparsers.add_parser("status", help="show saved DAG status and pending Battle handoffs")
    status_parser.add_argument("run", nargs="?", help="run ID or directory; defaults to latest post-production run")
    status_parser.add_argument("--show-prompts", action="store_true", help="print full exact prompts for all waiting jobs")

    show_parser = subparsers.add_parser("show", help="print the exact saved prompt for one waiting job")
    show_parser.add_argument("run", help="run ID or directory")
    show_parser.add_argument("job_id", help="waiting job ID")

    ingest_parser = subparsers.add_parser("ingest", help="save one Battle response immutably and resume ready jobs")
    ingest_parser.add_argument("run", help="run ID or directory")
    ingest_parser.add_argument("job_id", help="waiting handoff job ID")
    response_group = ingest_parser.add_mutually_exclusive_group(required=True)
    response_group.add_argument("response_file", nargs="?", help="UTF-8 response file; no renaming is required")
    response_group.add_argument("--stdin", action="store_true", help="read response text from stdin until EOF")
    ingest_parser.add_argument("--model-label", help="optional label shown by Battle; provenance only")

    pair_parser = subparsers.add_parser("ingest-pair", help="ingest both side-by-side writer answers in one operation")
    pair_parser.add_argument("run", help="run ID or directory")
    pair_parser.add_argument("writer_a_job", help="Writer A waiting job ID")
    pair_parser.add_argument("writer_b_job", help="Writer B waiting job ID")
    pair_parser.add_argument("--stdin", action="store_true", help="read JSON {\"left\": \"...\", \"right\": \"...\"} from stdin")
    pair_parser.add_argument("--left-file", help="file containing the first side-by-side response")
    pair_parser.add_argument("--right-file", help="file containing the second side-by-side response")
    pair_parser.add_argument("--model-label", help="optional shared Arena label for provenance")

    export_parser = subparsers.add_parser("export-preview", help="export validated articles into an isolated _posts preview; never changes a Jekyll repo")
    export_parser.add_argument("run", help="completed run ID or directory")

    prompt_parser = subparsers.add_parser("print-prompt", help="print the exact stored prompt for a waiting job")
    prompt_parser.add_argument("run", help="run ID or directory")
    prompt_parser.add_argument("job_id", help="waiting job ID")

    args = parser.parse_args(argv)
    try:
        if args.command == "start":
            if args.campaign not in {"campaign-01-analysis", str(ANALYSIS), str(ANALYSIS.resolve())}:
                raise ValueError("this workflow is bound to campaign-01-analysis and the five named source drafts")
            mission_path = ensure_workflow()
            current = _latest_run()
            if current is None:
                run_dir, state = asyncio.run(engine.run_mission(mission_path, max_parallel=2))
            else:
                state = _load_state(current)
                if state.get("run_status") == "completed":
                    run_dir = current
                else:
                    run_dir, state = asyncio.run(engine.run_mission(mission_path, resume_dir=current, resume_waiting_for_human=False, max_parallel=2))
            print(f"Mission: {MISSION_PATH}")
            _print_status(run_dir, state, include_prompts=False)
            if state.get("run_status") == "waiting_for_human":
                print("\nNo browser/UI submission was attempted. Use 'show' to print a prompt and 'ingest'/'ingest-pair' to save the response.")
            return 0 if state.get("run_status") in {"completed", "waiting_for_human", "in_progress"} else 1

        if args.command in {"status", "show", "print-prompt", "ingest", "ingest-pair", "export-preview"}:
            run_dir = _run_dir_for(args.run if hasattr(args, "run") and args.run else _latest_run().name if _latest_run() else "")
            if args.command == "status":
                _print_status(run_dir, _load_state(run_dir), include_prompts=args.show_prompts)
                return 0
            if args.command in {"show", "print-prompt"}:
                return _show_exact_prompt(run_dir, args.job_id)
            if args.command == "ingest":
                if args.stdin:
                    response_bytes = sys.stdin.buffer.read()
                else:
                    response_bytes = Path(args.response_file).expanduser().read_bytes()
                result = _ingest_one(run_dir, args.job_id, response_bytes, args.model_label)
                run_dir, state = _resume_after_ingest(run_dir)
                print(f"Ingested {args.job_id}: sha256={result['response_sha256']}")
                _print_status(run_dir, state)
                return 0 if state.get("run_status") in {"completed", "waiting_for_human", "in_progress"} else 1
            if args.command == "ingest-pair":
                if args.stdin:
                    if args.left_file or args.right_file:
                        raise ValueError("choose either --stdin or --left-file/--right-file")
                    left, right = _read_stdin_pair()
                else:
                    if not args.left_file or not args.right_file:
                        raise ValueError("provide both --left-file and --right-file, or use --stdin")
                    left = Path(args.left_file).expanduser().read_text(encoding="utf-8")
                    right = Path(args.right_file).expanduser().read_text(encoding="utf-8")
                state = _load_state(run_dir)
                job_a = state.get("jobs", {}).get(args.writer_a_job, {})
                job_b = state.get("jobs", {}).get(args.writer_b_job, {})
                if job_a.get("status") != "waiting_for_human" or job_b.get("status") != "waiting_for_human":
                    raise ValueError("both Writer A/B jobs must be waiting_for_human before pair ingestion")
                interaction_a = job_a.get("interaction", {})
                interaction_b = job_b.get("interaction", {})
                if interaction_a.get("post_id") != interaction_b.get("post_id"):
                    raise ValueError("Writer A/B handoffs must belong to the same post")
                handoff_a = json.loads((run_dir / interaction_a["handoff_json"]).read_text(encoding="utf-8"))
                handoff_b = json.loads((run_dir / interaction_b["handoff_json"]).read_text(encoding="utf-8"))
                if handoff_a.get("role") != "battle_writer_a" or handoff_b.get("role") != "battle_writer_b":
                    raise ValueError("pair ingestion requires the distinct Writer A and Writer B jobs in that order")
                if handoff_a.get("prompt_sha256") != handoff_b.get("prompt_sha256") or [row.get("sha256") for row in handoff_a.get("inputs", [])] != [row.get("sha256") for row in handoff_b.get("inputs", [])]:
                    raise ValueError("A/B prompts or evidence inputs differ; ingest responses separately")
                first = _ingest_one(run_dir, args.writer_a_job, left.encode("utf-8"), args.model_label)
                second = _ingest_one(run_dir, args.writer_b_job, right.encode("utf-8"), args.model_label)
                run_dir, state = _resume_after_ingest(run_dir)
                print(f"Ingested Writer A sha256={first['response_sha256']}")
                print(f"Ingested Writer B sha256={second['response_sha256']}")
                _print_status(run_dir, state)
                return 0 if state.get("run_status") in {"completed", "waiting_for_human", "in_progress"} else 1
            if args.command == "export-preview":
                export_root = _export_preview(run_dir)
                print(f"Validated Jekyll export preview: {export_root}")
                print("Files are isolated from any target site; no target repository was modified, committed, or pushed.")
                for path in sorted((export_root / "_posts").glob("*.md")):
                    print(f"  {path.relative_to(export_root)}  sha256={_sha256(path.read_bytes())}")
                return 0
    except (ValueError, RuntimeError, FileNotFoundError, engine.MissionValidationError, engine.ArtifactReferenceError) as exc:
        print(f"Post-production workflow error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted. The engine preserves every completed artifact and human handoff.", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
