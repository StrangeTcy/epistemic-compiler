#!/usr/bin/env python3
"""Reconstruct campaign results directly from the archived ZIP.

This script uses only the Python standard library. It keeps every recorded
result visible, while marking final rows whose archived judge notes explicitly
attribute failure to bounded provider retries as ineligible for model-performance
summaries. It writes hashes and source-member paths so generated tables can be
traced back to immutable ZIP members.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any

ARCHIVE_REF = "origin/main:atria-campaign-state-62.zip"
ARCHIVE_GIT_BLOB = "c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3"
CAMPAIGN_REF_MEMBER = "campaign_ref.txt"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(zf: zipfile.ZipFile, member: str) -> Any:
    return json.loads(zf.read(member).decode("utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: json.dumps(value, sort_keys=True, ensure_ascii=False)
                    if isinstance(value, (dict, list, tuple))
                    else value
                    for key, value in row.items()
                }
            )


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(fraction * len(ordered)) - 1))
    return ordered[index]


def iso_seconds(start: str | None, end: str | None) -> float | None:
    if not start or not end:
        return None
    return (
        datetime.fromisoformat(end.replace("Z", "+00:00"))
        - datetime.fromisoformat(start.replace("Z", "+00:00"))
    ).total_seconds()


def run_member_path(run_dir: str) -> str:
    prefix = "runs/atria_campaign/"
    if not run_dir.startswith(prefix):
        raise ValueError(f"unexpected suite run_dir: {run_dir}")
    return run_dir[len(prefix) :]


def response_stats(zf: zipfile.ZipFile, member: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    try:
        text = zf.read(member).decode("utf-8")
    except KeyError:
        text = ""
    for line in text.splitlines():
        if line.strip():
            rows.append(json.loads(line))
    tokens = Counter()
    for row in rows:
        usage = row.get("usage") or {}
        for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
            tokens[key] += int(usage.get(key) or 0)
    logical_turns = {
        (row.get("turn"), row.get("parse_attempt", 0)) for row in rows
    }
    distinct_turns = {row.get("turn") for row in rows}
    return {
        "response_rows": len(rows),
        "unique_turn_ids": len(distinct_turns),
        "logical_turn_parse_pairs": len(logical_turns),
        "prompt_tokens": tokens["prompt_tokens"],
        "completion_tokens": tokens["completion_tokens"],
        "total_tokens": tokens["total_tokens"],
        "reasoning_tokens": sum(
            int(
                ((row.get("usage") or {}).get("completion_tokens_details") or {}).get(
                    "reasoning_tokens"
                )
                or 0
            )
            for row in rows
        ),
        "response_rows_with_reasoning_content": sum(
            bool(
                (((row.get("raw_response") or {}).get("choices") or [{}])[0]
                .get("message") or {}).get("reasoning_content")
            )
            for row in rows
        ),
        "attempt_log_rows": sum(len(row.get("attempt_logs") or []) for row in rows),
    }


def error_types(zf: zipfile.ZipFile, member: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    try:
        lines = zf.read(member).decode("utf-8").splitlines()
    except KeyError:
        return counts
    for line in lines:
        if line.strip():
            counts[str(json.loads(line).get("error_type", "unknown"))] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True, help="path to the campaign ZIP")
    parser.add_argument("--out", type=Path, required=True, help="directory for generated evidence tables")
    parser.add_argument("--archive-ref", default=ARCHIVE_REF)
    parser.add_argument("--git-blob", default=ARCHIVE_GIT_BLOB)
    parser.add_argument(
        "--generator-source",
        type=Path,
        help="optional clean checkout/archive of rl_eval_generator at the recorded commit; used only to compare config hashes",
    )
    args = parser.parse_args()
    archive = args.archive.expanduser().resolve()
    out = args.out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    archive_hash = hashlib.sha256()
    with archive.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            archive_hash.update(block)

    with zipfile.ZipFile(archive) as zf:
        infos = zf.infolist()
        member_names = {info.filename for info in infos}
        report = read_json(zf, "campaign_report.json")
        progress = read_json(zf, "campaign_progress.json")
        suite = read_json(zf, "suite_checkpoint.json")
        pilot = read_json(zf, "pilot_manifest.json")
        instance_oracles = read_json(zf, "instance_oracles.json")
        oracle_preflight = read_json(zf, "oracle_preflight.json")
        modality = read_json(zf, "modality_inventory.json")
        intent = read_json(zf, "campaign_intent.json")
        telemetry = read_json(zf, "campaign_telemetry.json")
        campaign_ref = zf.read(CAMPAIGN_REF_MEMBER).decode("utf-8").strip()

        case_specs = {row["case_id"]: row for row in pilot["cases"]}
        results = {row["case_id"]: row for row in suite["results"]}
        provider_case = (report.get("provider_outage") or {}).get("last_case_id")
        if not provider_case:
            raise ValueError("campaign_report.json has no provider-outage case id")
        final_runs = {
            case_id: run_member_path(row["run_dir"]) for case_id, row in results.items()
        }
        # The report names the long outage case, but inspect every final verdict:
        # a second case has the same explicit provider-transient terminal note.
        provider_failure_notes: dict[str, list[str]] = {}
        for case_id, relative_run in final_runs.items():
            final_member = relative_run + "/final.json"
            final_json = read_json(zf, final_member) if final_member in member_names else {}
            notes = [str(note) for note in (final_json.get("notes") or [])]
            if case_id == provider_case or any(
                "provider transient failure after bounded retries" in note.casefold()
                for note in notes
            ):
                provider_failure_notes[case_id] = notes
        provider_failure_cases = set(provider_failure_notes)

        # The report records two distinct omission classes outside the scored
        # manifest: unsupported-modality cases and pre-provider gate exclusions.
        campaign_omissions = report.get("campaign_omissions") or {}
        gate_omissions = report.get("known_gate_blocked_omissions") or {}
        gate_case_detail = {
            str(row.get("case_id")): row for row in (gate_omissions.get("cases") or [])
        }
        exclusion_rows: list[dict[str, Any]] = []
        for case_id in campaign_omissions.get("omitted_case_ids") or []:
            exclusion_rows.append(
                {
                    "case_id": case_id,
                    "environment": str(case_id).split("__", 1)[0],
                    "exclusion_class": "unsupported_provider_input_modality",
                    "reason": campaign_omissions.get("reason"),
                    "disposition": "omitted_before_scoring",
                    "calibration_class": "",
                    "provider_calls_before_omission": "",
                    "source_member": "campaign_report.json#/campaign_omissions",
                }
            )
        for case_id in gate_omissions.get("omitted_case_ids") or []:
            detail = gate_case_detail.get(case_id, {})
            exclusion_rows.append(
                {
                    "case_id": case_id,
                    "environment": str(case_id).split("__", 1)[0],
                    "exclusion_class": "known_gate_calibration_failure",
                    "reason": gate_omissions.get("reason"),
                    "disposition": gate_omissions.get("disposition"),
                    "calibration_class": detail.get("calibration_class"),
                    "provider_calls_before_omission": gate_omissions.get("provider_calls_before_omission"),
                    "source_member": "campaign_report.json#/known_gate_blocked_omissions",
                }
            )
        if len({row["case_id"] for row in exclusion_rows}) != len(exclusion_rows):
            raise ValueError("campaign omission lists contain duplicate case ids")
        if set(row["case_id"] for row in exclusion_rows) & set(results):
            raise ValueError("an explicitly omitted case also appears in scored results")
        write_csv(out / "campaign_exclusions.csv", exclusion_rows)

        # Full immutable member inventory; file names are never used as counts.
        inventory_rows: list[dict[str, Any]] = []
        for info in infos:
            digest = hashlib.sha256()
            with zf.open(info, "r") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
            parts = PurePosixPath(info.filename).parts
            inventory_rows.append(
                {
                    "member_path": info.filename,
                    "uncompressed_bytes": info.file_size,
                    "compressed_bytes": info.compress_size,
                    "sha256": digest.hexdigest(),
                    "top_level": parts[0] if parts else "",
                    "kind": (
                        "run_artifact:" + PurePosixPath(info.filename).name
                        if len(parts) >= 4 and parts[0] == "episodes"
                        else "instance_oracle"
                        if "_instance_oracles" in parts
                        else "root_metadata"
                    ),
                }
            )
        write_csv(out / "archive_inventory.csv", inventory_rows)
        inventory_by_path = {row["member_path"]: row for row in inventory_rows}

        # Enumerate every archived run directory, including superseded attempts.
        run_members: dict[tuple[str, str], set[str]] = defaultdict(set)
        for name in member_names:
            parts = PurePosixPath(name).parts
            if len(parts) >= 4 and parts[0] == "episodes" and parts[2] != "_instance_oracles":
                run_members[(parts[1], parts[2])].add(name)
        run_rows: list[dict[str, Any]] = []
        run_lookup: dict[tuple[str, str], dict[str, Any]] = {}
        all_usage = Counter()
        final_usage = Counter()
        all_attempt_log_rows = 0
        all_response_rows = 0
        all_unique_turns = 0
        all_reasoning_content_rows = 0
        total_api_log_rows = Counter()
        final_run_spans: list[float] = []
        all_run_spans: list[float] = []
        final_result_mismatches: list[str] = []

        for (case_id, run_id), names in sorted(run_members.items()):
            manifest_member = f"episodes/{case_id}/{run_id}/manifest.json"
            final_member = f"episodes/{case_id}/{run_id}/final.json"
            if manifest_member not in member_names:
                continue
            manifest = read_json(zf, manifest_member)
            final = read_json(zf, final_member) if final_member in member_names else {}
            response_member = f"episodes/{case_id}/{run_id}/model_responses.jsonl"
            error_member = f"episodes/{case_id}/{run_id}/api_errors.jsonl"
            usage = response_stats(zf, response_member)
            errors = error_types(zf, error_member)
            span = iso_seconds(manifest.get("started_at"), manifest.get("finished_at"))
            selected_final = final_runs.get(case_id) == f"episodes/{case_id}/{run_id}"
            run_lookup[(case_id, run_id)] = {
                "manifest": manifest,
                "final": final,
                "usage": usage,
                "span": span,
                "selected_final": selected_final,
                "response_member": response_member,
                "final_member": final_member,
            }
            for key in ("prompt_tokens", "completion_tokens", "total_tokens", "reasoning_tokens"):
                all_usage[key] += usage[key]
                if selected_final:
                    final_usage[key] += usage[key]
            all_attempt_log_rows += usage["attempt_log_rows"]
            all_response_rows += usage["response_rows"]
            all_unique_turns += usage["unique_turn_ids"]
            all_reasoning_content_rows += usage["response_rows_with_reasoning_content"]
            total_api_log_rows.update(errors)
            if span is not None:
                all_run_spans.append(span)
                if selected_final:
                    final_run_spans.append(span)
            result = results.get(case_id)
            if selected_final and result:
                if any(
                    result.get(field) != final.get(field)
                    for field in ("verdict", "score", "failure_mode")
                ):
                    final_result_mismatches.append(case_id)
            run_rows.append(
                {
                    "case_id": case_id,
                    "run_id": run_id,
                    "run_member_prefix": f"episodes/{case_id}/{run_id}/",
                    "selected_as_suite_result": selected_final,
                    "started_at": manifest.get("started_at"),
                    "finished_at": manifest.get("finished_at"),
                    "elapsed_seconds_manifest": span,
                    "requested_model": manifest.get("requested_model"),
                    "resolved_model": manifest.get("resolved_model"),
                    "repository_commit": manifest.get("repository_commit"),
                    "repository_dirty": manifest.get("repository_dirty"),
                    "max_steps": manifest.get("max_steps"),
                    "max_tokens": manifest.get("max_tokens"),
                    "temperature": manifest.get("temperature"),
                    "top_p": manifest.get("top_p"),
                    "http_attempts_used_manifest": manifest.get("http_attempts_used"),
                    "verdict_final_json": final.get("verdict"),
                    "score_final_json": final.get("score"),
                    "failure_mode_final_json": final.get("failure_mode"),
                    "response_member": response_member,
                    "response_rows": usage["response_rows"],
                    "unique_turn_ids": usage["unique_turn_ids"],
                    "prompt_tokens": usage["prompt_tokens"],
                    "completion_tokens": usage["completion_tokens"],
                    "total_tokens": usage["total_tokens"],
                    "api_log_rows": sum(errors.values()),
                    "api_log_error_types": dict(errors),
                }
            )
        write_csv(out / "run_attempts.csv", run_rows)

        case_rows: list[dict[str, Any]] = []
        # The archive labels epistemic_games as ml_debugging. Retain that raw
        # label in `track`, but give analyses a source-semantic family field.
        analysis_family_overrides = {"epistemic_games": "epistemic_games"}
        for case_id, result in sorted(results.items()):
            spec = case_specs.get(case_id, {})
            relative_run = final_runs[case_id]
            parts = PurePosixPath(relative_run).parts
            run_id = parts[-1]
            run = run_lookup[(case_id, run_id)]
            perf_eligible = case_id not in provider_failure_cases
            case_rows.append(
                {
                    "case_id": case_id,
                    "environment": result.get("environment"),
                    "track": result.get("track"),
                    "analysis_family": analysis_family_overrides.get(
                        str(result.get("environment")), result.get("track")
                    ),
                    "track_label_overridden_for_analysis": str(result.get("environment"))
                    in analysis_family_overrides,
                    "seed": result.get("seed"),
                    "difficulty_levels": spec.get("difficulty_levels", {}),
                    "config_path": spec.get("config_path"),
                    "config_sha256": spec.get("config_sha256"),
                    "judge_guarantee": result.get("judge_guarantee"),
                    "status": result.get("status"),
                    "verdict": result.get("verdict"),
                    "score": result.get("score"),
                    "failure_mode_raw": result.get("failure_mode"),
                    "failure_mode_normalized": str(result.get("failure_mode") or "unknown").casefold(),
                    "final_notes": run["final"].get("notes") or [],
                    "final_metrics": run["final"].get("metrics") or {},
                    "returncode": result.get("returncode"),
                    "elapsed_seconds": result.get("elapsed_seconds"),
                    "http_attempts_result": result.get("http_attempts"),
                    "http_attempt_ceiling_result": result.get("http_attempt_ceiling"),
                    "reasoning_enabled": result.get("reasoning_enabled"),
                    "performance_eligible": perf_eligible,
                    "exclusion_reason": (
                        "campaign report provider-outage case; " if case_id == provider_case else ""
                    ) + (
                        "final result explicitly attributes terminal failure to provider transient after bounded retries"
                        if case_id in provider_failure_cases else ""
                    ),
                    "run_id": run_id,
                    "run_member_prefix": relative_run + "/",
                    "result_member": "suite_checkpoint.json#/results/" + case_id,
                    "final_member": run["final_member"],
                    "manifest_member": f"episodes/{case_id}/{run_id}/manifest.json",
                    "response_member": run["response_member"],
                    "prompt_tokens_final_run": run["usage"]["prompt_tokens"],
                    "completion_tokens_final_run": run["usage"]["completion_tokens"],
                    "total_tokens_final_run": run["usage"]["total_tokens"],
                }
            )
        write_csv(out / "case_results.csv", case_rows)

        oracle_records = {
            str(row.get("case_id")): row for row in (instance_oracles.get("cases") or [])
        }
        preflight_by_environment = {
            str(row.get("environment")): row for row in (oracle_preflight.get("results") or [])
        }
        trace_index_rows: list[dict[str, Any]] = []
        failure_detail_rows: list[dict[str, Any]] = []
        for row in case_rows:
            case_id = str(row["case_id"])
            prefix = str(row["run_member_prefix"])
            run_id = str(row["run_id"])
            run = run_lookup[(case_id, run_id)]
            trace_member = prefix + "trace.jsonl"
            trace_text = zf.read(trace_member).decode("utf-8") if trace_member in member_names else ""
            trace_rows = sum(bool(line.strip()) for line in trace_text.splitlines())
            response_member = str(row["response_member"])
            api_error_member = prefix + "api_errors.jsonl"
            env_event_member = prefix + "environment-events.jsonl"
            oracle = oracle_records.get(case_id, {})
            oracle_member = (
                f"episodes/{case_id}/_instance_oracles/{oracle['instance_sha256']}.json"
                if oracle.get("instance_sha256") else ""
            )
            preflight = preflight_by_environment.get(str(row["environment"]), {})

            def artifact_field(member: str, field: str) -> Any:
                return inventory_by_path.get(member, {}).get(field, "")

            api_counts = error_types(zf, api_error_member)
            env_events_text = zf.read(env_event_member).decode("utf-8") if env_event_member in member_names else ""
            trace_index_rows.append(
                {
                    "case_id": case_id,
                    "analysis_family": row["analysis_family"],
                    "recorded_track": row["track"],
                    "performance_eligible": row["performance_eligible"],
                    "judge_guarantee": row["judge_guarantee"],
                    "final_run_id": run_id,
                    "trace_member": trace_member,
                    "trace_sha256": artifact_field(trace_member, "sha256"),
                    "trace_bytes": artifact_field(trace_member, "uncompressed_bytes"),
                    "trace_jsonl_rows": trace_rows,
                    "model_responses_member": response_member,
                    "model_responses_sha256": artifact_field(response_member, "sha256"),
                    "model_responses_bytes": artifact_field(response_member, "uncompressed_bytes"),
                    "successful_response_rows": run["usage"]["response_rows"],
                    "unique_turn_ids": run["usage"]["unique_turn_ids"],
                    "prompt_tokens": run["usage"]["prompt_tokens"],
                    "completion_tokens": run["usage"]["completion_tokens"],
                    "reasoning_tokens_reported": run["usage"]["reasoning_tokens"],
                    "response_rows_with_reasoning_content": run["usage"]["response_rows_with_reasoning_content"],
                    "api_errors_member": api_error_member,
                    "api_errors_sha256": artifact_field(api_error_member, "sha256"),
                    "api_error_type_counts": dict(api_counts),
                    "environment_events_member": env_event_member,
                    "environment_events_sha256": artifact_field(env_event_member, "sha256"),
                    "environment_events_jsonl_rows": sum(bool(line.strip()) for line in env_events_text.splitlines()),
                    "submission_patch_member": prefix + "submission.patch",
                    "submission_patch_sha256": artifact_field(prefix + "submission.patch", "sha256"),
                    "workspace_diff_member": prefix + "workspace.diff",
                    "workspace_diff_sha256": artifact_field(prefix + "workspace.diff", "sha256"),
                    "judge_stdout_member": prefix + "judge.stdout",
                    "judge_stderr_member": prefix + "judge.stderr",
                    "final_result_member": row["final_member"],
                    "final_result_sha256": artifact_field(str(row["final_member"]), "sha256"),
                    "instance_oracle_member": oracle_member if oracle_member in member_names else "",
                    "instance_oracle_status": oracle.get("status", "compile_only_or_no_record"),
                    "instance_oracle_sha256": oracle.get("instance_sha256", ""),
                    "environment_oracle_preflight": preflight.get("reference_behavior", ""),
                    "environment_oracle_self_test": preflight.get("reference_self_test", ""),
                    "environment_oracle_behavioral_reference_executed": preflight.get("behavioral_reference_executed", ""),
                }
            )
            if row["verdict"] == "FAIL":
                failure_detail_rows.append(
                    {
                        "case_id": case_id,
                        "environment": row["environment"],
                        "analysis_family": row["analysis_family"],
                        "recorded_track": row["track"],
                        "judge_guarantee": row["judge_guarantee"],
                        "performance_eligible": row["performance_eligible"],
                        "exclusion_reason": row["exclusion_reason"],
                        "score": row["score"],
                        "failure_mode_raw": row["failure_mode_raw"],
                        "final_notes": row["final_notes"],
                        "final_metrics": row["final_metrics"],
                        "result_member": row["result_member"],
                        "final_member": row["final_member"],
                        "trace_member": trace_member,
                        "submission_patch_member": prefix + "submission.patch",
                        "workspace_diff_member": prefix + "workspace.diff",
                    }
                )
        write_csv(out / "trace_index.csv", trace_index_rows)
        write_csv(out / "failure_details.csv", failure_detail_rows)

        def summarize(rows: list[dict[str, Any]], dimension: str) -> list[dict[str, Any]]:
            groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for row in rows:
                groups[str(row.get(dimension, ""))].append(row)
            summaries = []
            for label, group in sorted(groups.items()):
                eligible = [row for row in group if row["performance_eligible"]]
                passes = sum(row["verdict"] == "PASS" for row in eligible)
                fails = sum(row["verdict"] == "FAIL" for row in eligible)
                raw_modes = Counter(row["judge_guarantee"] for row in group)
                summary: dict[str, Any] = {
                    dimension: label,
                    "recorded_cases": len(group),
                    "performance_eligible_cases": len(eligible),
                    "passes_performance_set": passes,
                    "fails_performance_set": fails,
                    "pass_rate_performance_set": passes / len(eligible) if eligible else None,
                    "provider_failure_exclusions": len(group) - len(eligible),
                    "recorded_behavioral_reference": raw_modes["behavioral_reference"],
                    "recorded_compile_only": raw_modes["compile_only"],
                }
                for mode in ("behavioral_reference", "compile_only"):
                    subset = [row for row in eligible if row["judge_guarantee"] == mode]
                    summary[f"{mode}_n"] = len(subset)
                    summary[f"{mode}_passes"] = sum(row["verdict"] == "PASS" for row in subset)
                    summary[f"{mode}_fails"] = sum(row["verdict"] == "FAIL" for row in subset)
                summaries.append(summary)
            return summaries

        write_csv(out / "environment_summary.csv", summarize(case_rows, "environment"))
        write_csv(out / "track_summary.csv", summarize(case_rows, "track"))
        write_csv(out / "analysis_family_summary.csv", summarize(case_rows, "analysis_family"))

        # Axis tables keep controls explicit. They do not impose an ordinal score
        # on names such as easy/medium/hard; each row is a fixed-other-axes group.
        axis_groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in case_rows:
            axes = row.get("difficulty_levels") or {}
            for axis, level in axes.items():
                controls = {key: value for key, value in axes.items() if key != axis}
                key = (
                    str(row["environment"]),
                    str(row["track"]),
                    str(axis),
                    json.dumps(controls, sort_keys=True),
                )
                axis_groups[key + (str(level),)].append(row)
        axis_rows: list[dict[str, Any]] = []
        for (environment, track, axis, controls, level), group in sorted(axis_groups.items()):
            eligible = [row for row in group if row["performance_eligible"]]
            passes = sum(row["verdict"] == "PASS" for row in eligible)
            axis_rows.append(
                {
                    "environment": environment,
                    "track": track,
                    "axis": axis,
                    "other_axis_controls": json.loads(controls),
                    "level": level,
                    "recorded_cases": len(group),
                    "performance_eligible_cases": len(eligible),
                    "passes": passes,
                    "fails": sum(row["verdict"] == "FAIL" for row in eligible),
                    "pass_rate": passes / len(eligible) if eligible else None,
                    "scores": [row["score"] for row in eligible],
                    "case_ids": [row["case_id"] for row in group],
                    "judge_guarantees": sorted({row["judge_guarantee"] for row in group}),
                }
            )
        write_csv(out / "axis_summary.csv", axis_rows)

        fail_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in case_rows:
            if row["performance_eligible"] and row["verdict"] == "FAIL":
                raw = str(row["failure_mode_raw"] or "unknown")
                fail_groups[raw.casefold()].append(row)
        failure_rows = []
        for normalized, group in sorted(fail_groups.items()):
            raw_values = sorted({str(row["failure_mode_raw"]) for row in group})
            failure_rows.append(
                {
                    "failure_mode_normalized": normalized,
                    "failure_mode_raw_values": raw_values,
                    "count": len(group),
                    "share_of_eligible_failures": len(group)
                    / max(1, sum(len(rows) for rows in fail_groups.values())),
                    "case_ids": [row["case_id"] for row in group],
                    "judge_guarantees": dict(Counter(row["judge_guarantee"] for row in group)),
                }
            )
        write_csv(out / "failure_taxonomy.csv", failure_rows)

        config_rows: list[dict[str, Any]] = []
        for config_path in sorted({str(row.get("config_path")) for row in case_specs.values()}):
            manifest_hash = next(
                row["config_sha256"]
                for row in case_specs.values()
                if row.get("config_path") == config_path
            )
            source_file = args.generator_source / config_path if args.generator_source else None
            source_hash = sha256_bytes(source_file.read_bytes()) if source_file and source_file.is_file() else None
            config_rows.append(
                {
                    "config_path": config_path,
                    "campaign_config_sha256": manifest_hash,
                    "source_commit_config_sha256": source_hash,
                    "hash_matches": source_hash == manifest_hash if source_hash else None,
                    "source_path_checked": str(source_file) if source_file else "",
                }
            )
        write_csv(out / "config_hash_audit.csv", config_rows)

        valid_rows = [row for row in case_rows if row["performance_eligible"]]
        raw_verdicts = Counter(row["verdict"] for row in case_rows)
        valid_verdicts = Counter(row["verdict"] for row in valid_rows)
        raw_failures = Counter(
            str(row["failure_mode_raw"]).casefold()
            for row in case_rows if row["verdict"] == "FAIL"
        )
        valid_failures = Counter(
            str(row["failure_mode_raw"]).casefold()
            for row in valid_rows if row["verdict"] == "FAIL"
        )
        mode_summary: dict[str, Any] = {}
        for mode in ("behavioral_reference", "compile_only"):
            all_mode = [row for row in case_rows if row["judge_guarantee"] == mode]
            valid_mode = [row for row in valid_rows if row["judge_guarantee"] == mode]
            mode_summary[mode] = {
                "recorded_rows": len(all_mode),
                "recorded_passes": sum(row["verdict"] == "PASS" for row in all_mode),
                "recorded_fails": sum(row["verdict"] == "FAIL" for row in all_mode),
                "performance_eligible_rows": len(valid_mode),
                "performance_eligible_passes": sum(row["verdict"] == "PASS" for row in valid_mode),
                "performance_eligible_fails": sum(row["verdict"] == "FAIL" for row in valid_mode),
            }

        run_histogram = Counter()
        for case_id in results:
            run_histogram[sum(case == case_id for case, _ in run_members)] += 1
        # Run directories by each selected case; use an explicit map rather than
        # relying on filename order or the case directory's apparent contents.
        run_count_by_case = Counter(case for case, _ in run_members)
        run_histogram = Counter(run_count_by_case[case_id] for case_id in results)
        elapsed = [float(row["elapsed_seconds"]) for row in case_rows if row.get("elapsed_seconds") is not None]
        config_match_count = sum(row["hash_matches"] is True for row in config_rows)
        config_checked_count = sum(row["hash_matches"] is not None for row in config_rows)
        progress_attempts = progress.get("http_attempts")
        checkpoint_observed = suite.get("http_attempts_total")
        checkpoint_unknown = suite.get("http_attempts_unknown_upper_bound_total")

        audit = {
            "archive": {
                "archive_ref": args.archive_ref,
                "git_blob_sha1": args.git_blob,
                "archive_sha256": archive_hash.hexdigest(),
                "archive_bytes": archive.stat().st_size,
                "member_count": len(infos),
                "campaign_ref_member": campaign_ref,
                "campaign_ref_is_campaign_repository_commit": campaign_ref == pilot["repository"]["commit"],
                "root_member_count": sum("/" not in info.filename for info in infos),
                "member_inventory_csv": "archive_inventory.csv",
            },
            "campaign": {
                "intent_provider": intent.get("provider"),
                "execution_mode": intent.get("execution_mode"),
                "recorded_at": intent.get("recorded_at"),
                "telemetry_run_id": telemetry.get("wandb_run_id"),
                "campaign_status_report": report.get("status"),
                "started_at": suite.get("started_at"),
                "finished_at": suite.get("updated_at"),
                "wall_elapsed_seconds": iso_seconds(suite.get("started_at"), suite.get("updated_at")),
                "model": suite.get("run", {}).get("model"),
                "provider": suite.get("run", {}).get("provider"),
                "max_steps": suite.get("run", {}).get("max_steps"),
                "max_tokens_per_call": suite.get("run", {}).get("max_tokens"),
                "temperature": suite.get("run", {}).get("temperature"),
                "top_p": suite.get("run", {}).get("top_p"),
                "reasoning_enabled_config": suite.get("run", {}).get("reasoning_enabled"),
                "all_run_repository_commit": pilot.get("repository", {}).get("commit"),
                "repository_dirty_at_run": pilot.get("repository", {}).get("dirty"),
                "registry_environment_count": pilot.get("environment_count"),
                "selected_environment_count": len({row.get("environment") for row in case_rows}),
                "selected_case_count_manifest": pilot.get("case_count"),
                "selected_case_count_results": len(case_rows),
                "case_id_set_matches_manifest": set(case_specs) == set(results),
                "result_status_counts": dict(Counter(row["status"] for row in case_rows)),
                "raw_verdict_counts": dict(raw_verdicts),
                "analysis_family_label_overrides": analysis_family_overrides,
                "recorded_track_label_mismatch_case_ids": [
                    row["case_id"] for row in case_rows if row["track_label_overridden_for_analysis"]
                ],
                "explicit_omission_count_unsupported_modality": len(campaign_omissions.get("omitted_case_ids") or []),
                "explicit_omission_case_ids_unsupported_modality": campaign_omissions.get("omitted_case_ids") or [],
                "explicit_omission_count_known_gate_blocked": len(gate_omissions.get("omitted_case_ids") or []),
                "explicit_omission_case_ids_known_gate_blocked": gate_omissions.get("omitted_case_ids") or [],
                "known_gate_blocked_calibration_classes": {
                    case_id: detail.get("calibration_class") for case_id, detail in gate_case_detail.items()
                },
                "explicit_omission_total": len(exclusion_rows),
                "recorded_results_plus_reported_omissions": len(case_rows) + len(exclusion_rows),
                "performance_eligible_case_count": len(valid_rows),
                "performance_eligible_verdict_counts": dict(valid_verdicts),
                "performance_eligible_pass_rate_descriptive_mixed_modes": valid_verdicts.get("PASS", 0) / len(valid_rows),
                "provider_outage_case_id_named_by_campaign_report": provider_case,
                "provider_failure_case_count_from_final_result_notes": len(provider_failure_cases),
                "provider_failure_case_ids_from_final_result_notes": sorted(provider_failure_cases),
                "provider_failure_case_notes": provider_failure_notes,
                "campaign_report_provider_outage_counter": report.get("provider_outage"),
                "omitted_unsupported_case_count": len((report.get("campaign_omissions") or {}).get("omitted_case_ids", [])),
                "omitted_unsupported_environments": (report.get("campaign_omissions") or {}).get("omitted_environments", []),
                "known_gate_blocked_case_count": len((report.get("known_gate_blocked_omissions") or {}).get("omitted_case_ids", [])),
                "known_gate_blocked_disposition": (report.get("known_gate_blocked_omissions") or {}).get("disposition"),
                "provider_calls_before_gate_omissions": (report.get("known_gate_blocked_omissions") or {}).get("provider_calls_before_omission"),
                "mode_summary": mode_summary,
                "campaign_report_aggregate_note": report.get("aggregate_note"),
                "campaign_report_compile_only_disclaimer": report.get("compile_only_disclaimer"),
                "oracle_preflight_status_counts": dict(
                    Counter(str(row.get("reference_self_test")) for row in (oracle_preflight.get("results") or []))
                ),
                "oracle_preflight_behavioral_reference_details": {
                    str(row.get("environment")): {
                        "reference_behavior": row.get("reference_behavior"),
                        "reference_self_test": row.get("reference_self_test"),
                        "behavioral_reference_executed": row.get("behavioral_reference_executed"),
                    }
                    for row in (oracle_preflight.get("results") or [])
                    if row.get("behavioral_reference_executed")
                },
                "exact_instance_oracle_cases": len(instance_oracles.get("cases", [])),
                "instance_oracle_case_status_counts": dict(
                    Counter(str(row.get("status")) for row in (instance_oracles.get("cases") or []))
                ),
                "compile_only_cases": len(instance_oracles.get("compile_only_cases", [])),
                "oracle_preflight_behavioral_reference_environments": [
                    row.get("environment") for row in oracle_preflight.get("results", [])
                    if row.get("behavioral_reference_executed")
                ],
                "text_only_selected_case_count": modality.get("selected_case_count"),
                "text_only_unsupported_selected_case_count": len(modality.get("unsupported_case_ids", [])),
                "campaign_progress_episodes_total": progress.get("episodes_total"),
                "campaign_progress_episodes_completed": progress.get("episodes_completed"),
            },
            "execution_and_usage": {
                "archived_run_directory_count": len(run_rows),
                "runs_per_selected_case_histogram": {str(k): v for k, v in sorted(run_histogram.items())},
                "additional_run_directories_over_one_per_case": len(run_rows) - len(results),
                "run_directories_for_campaign_report_provider_case": run_count_by_case[provider_case],
                "run_directories_for_all_provider_failure_cases": sum(run_count_by_case[case_id] for case_id in provider_failure_cases),
                "final_result_vs_final_json_mismatches": final_result_mismatches,
                "all_run_successful_response_rows": all_response_rows,
                "all_run_unique_turn_ids_summed_by_run": all_unique_turns,
                "all_run_prompt_tokens_from_successful_responses": all_usage["prompt_tokens"],
                "all_run_completion_tokens_from_successful_responses": all_usage["completion_tokens"],
                "all_run_total_tokens_from_successful_responses": all_usage["total_tokens"],
                "all_run_reasoning_tokens_reported_in_usage": all_usage["reasoning_tokens"],
                "all_run_response_rows_with_reasoning_content": all_reasoning_content_rows,
                "all_run_embedded_attempt_log_rows": all_attempt_log_rows,
                "final_run_successful_response_rows": sum(run_lookup[(case, PurePosixPath(path).parts[-1])]["usage"]["response_rows"] for case, path in final_runs.items()),
                "final_run_unique_turn_ids_summed_by_case": sum(run_lookup[(case, PurePosixPath(path).parts[-1])]["usage"]["unique_turn_ids"] for case, path in final_runs.items()),
                "final_run_prompt_tokens_from_successful_responses": final_usage["prompt_tokens"],
                "final_run_completion_tokens_from_successful_responses": final_usage["completion_tokens"],
                "final_run_total_tokens_from_successful_responses": final_usage["total_tokens"],
                "api_errors_jsonl_error_type_counts_all_runs": dict(total_api_log_rows),
                "api_errors_jsonl_record_count_all_runs": sum(total_api_log_rows.values()),
                "sum_run_manifest_http_attempts_used": sum(int(row.get("http_attempts_used_manifest") or 0) for row in run_rows),
                "sum_selected_suite_result_http_attempts": sum(int(row.get("http_attempts_result") or 0) for row in case_rows),
                "sum_selected_final_manifest_http_attempts_used": sum(
                    int(run_lookup[(case, PurePosixPath(path).parts[-1])]["manifest"].get("http_attempts_used") or 0)
                    for case, path in final_runs.items()
                ),
                "suite_checkpoint_http_attempts_total": checkpoint_observed,
                "suite_checkpoint_http_attempts_unknown_upper_bound_total": checkpoint_unknown,
                "suite_checkpoint_reported_attempts_plus_unknown": (checkpoint_observed or 0) + (checkpoint_unknown or 0),
                "campaign_progress_http_attempts": progress_attempts,
                "attempt_counter_reconciliation": "Counters have different scopes and do not reconcile from archived per-run manifests/JSONL; report each source separately.",
                "suite_result_elapsed_seconds_sum": sum(elapsed),
                "suite_result_elapsed_seconds_min": min(elapsed) if elapsed else None,
                "suite_result_elapsed_seconds_median": statistics.median(elapsed) if elapsed else None,
                "suite_result_elapsed_seconds_mean": statistics.mean(elapsed) if elapsed else None,
                "suite_result_elapsed_seconds_p95_nearest_rank": percentile(elapsed, 0.95),
                "suite_result_elapsed_seconds_max": max(elapsed) if elapsed else None,
                "archived_run_manifest_elapsed_seconds_sum_all_attempt_runs": sum(all_run_spans),
                "archived_run_manifest_elapsed_seconds_sum_selected_runs": sum(final_run_spans),
                "api_cost_or_spend": "not present in the exported archive",
            },
            "failure_taxonomy_all_recorded_failures": dict(raw_failures),
            "failure_taxonomy_performance_eligible": dict(valid_failures),
            "config_hash_audit": {
                "generator_source_path_argument": str(args.generator_source) if args.generator_source else None,
                "selected_unique_config_paths": len(config_rows),
                "config_paths_checked": config_checked_count,
                "config_hash_matches": config_match_count,
                "config_hash_mismatches": [row["config_path"] for row in config_rows if row["hash_matches"] is False],
            },
            "generated_tables": [
                "archive_inventory.csv", "campaign_exclusions.csv", "case_results.csv",
                "run_attempts.csv", "trace_index.csv", "failure_details.csv",
                "environment_summary.csv", "track_summary.csv", "analysis_family_summary.csv",
                "axis_summary.csv", "failure_taxonomy.csv", "config_hash_audit.csv",
            ],
        }
        (out / "audit.json").write_text(
            json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
