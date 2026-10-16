#!/usr/bin/env python3
"""Build and validate the Campaign 01 post-to-evidence index.

Reads only the generated reconstruction tables and editorial draft markers;
never opens, alters, or executes the campaign archive.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "posts"
GENERATED = ROOT / "evidence" / "generated"
FINDINGS = ROOT / "findings" / "findings.json"
OUTPUT = POSTS / "claim_traceability.csv"
SOURCE_ROOT = Path("/tmp/rl_eval_generator_base")
COMPARATOR_REV = "d7357092493f311f649a0742889b301d796911b5"

# Fields: post, claim tag, summary, findings, raw archive roots, selector,
# generated evidence, source-comparator paths, external references.
SPECS = [
    ("POST-01", "POST-01-C01", "Campaign scope, raw totals, omissions, and provider-terminal sensitivity", ["F-02", "F-03"], ["campaign_report.json", "suite_checkpoint.json"], "provider-terminal", ["campaign-01-analysis/evidence/generated/audit.json", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/campaign_exclusions.csv"], [], []),
    ("POST-01", "POST-01-C02", "Primary eligible set is mixed across behavioral_reference and compile_only modes", ["F-01", "F-04"], ["campaign_report.json", "instance_oracles.json", "oracle_preflight.json", "suite_checkpoint.json", "pilot_manifest.json"], "all", ["campaign-01-analysis/evidence/generated/audit.json", "campaign-01-analysis/evidence/generated/case_results.csv"], [], []),
    ("POST-01", "POST-01-C03", "Regex Rule 110 outcomes across easy length and changed surface labels", ["F-01", "F-06", "F-10"], ["pilot_manifest.json"], "env:regex_state_machine", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/regex_state_machine/config.yaml", "envs/weird_machine/regex_state_machine/files/prompt.md", "envs/weird_machine/regex_state_machine/files/judge.py"], []),
    ("POST-01", "POST-01-C04", "CSS and SQL outcome patterns and validator failure causes", ["F-06", "F-09", "F-10"], [], "envset:[\"css_state_machine\",\"sql_fixed_point\"]", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/css_state_machine/config.yaml", "envs/weird_machine/css_state_machine/files/judge.py", "envs/weird_machine/sql_fixed_point/config.yaml", "envs/weird_machine/sql_fixed_point/files/judge.py"], []),
    ("POST-01", "POST-01-C05", "Spreadsheet, weird-machine total, MoCo visible-test, and adaptive recurrence outcomes", ["F-06", "F-09", "F-10", "F-11", "F-12"], [], "union:[\"family:weird_machine\",\"env:moco\",\"env:rd_adaptive_halting\"]", ["campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/spreadsheet_dataflow/config.yaml", "envs/weird_machine/spreadsheet_dataflow/files/judge.py", "envs/moco/config.yaml", "envs/recurrent_depth/adaptive_halting/config.yaml"], []),
    ("POST-01", "POST-01-C06", "A map should show task, judge mode, and failure layer rather than scalar color", ["F-04", "F-09", "F-16"], ["campaign_report.json", "instance_oracles.json", "oracle_preflight.json"], "", ["campaign-01-analysis/evidence/generated/failure_taxonomy.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv"], [], []),
    ("POST-01", "POST-01-C07", "Recurrent-depth versus trajectory/synthesis family descriptive counts only", ["F-04", "F-11", "F-16"], ["suite_checkpoint.json"], "family:recurrent_depth_behavioral", ["campaign-01-analysis/evidence/generated/analysis_family_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv"], [], []),
    ("POST-01", "POST-01-C08", "Prior-work context for multi-metric evaluation and variable perturbation", ["F-17"], [], "", ["campaign-01-analysis/sources/references.md"], [], ["HELM: https://arxiv.org/abs/2211.09110", "VarBench: https://aclanthology.org/2024.findings-emnlp.946/"]),
    ("POST-01", "POST-01-C09", "Claim ceiling and proposed replicated axis audit", ["F-06", "F-14", "F-16"], [], "", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/axis_placeholder_audit.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], [], []),

    ("POST-02", "POST-02-C01", "Seven exact selected epistemic-game results and posterior examples", ["F-07"], ["suite_checkpoint.json", "oracle_preflight.json"], "env:epistemic_games", ["campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/trace_index.csv"], [], []),
    ("POST-02", "POST-02-C02", "Bayesian posterior rule and judge-scored outputs", ["F-07"], [], "env:epistemic_games", ["campaign-01-analysis/evidence/generated/case_results.csv"], ["envs/epistemic_games/files/core.py", "envs/epistemic_games/files/judge.py"], []),
    ("POST-02", "POST-02-C03", "Source explicitly limits v0 to specified policy likelihoods, not recursive level-k", ["F-01", "F-07"], ["pilot_manifest.json"], "", ["campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/epistemic_games/files/core.py"], []),
    ("POST-02", "POST-02-C04", "Ambiguous evidence, balanced/skewed priors, and likelihood-ratio bands", ["F-07"], [], "env:epistemic_games", ["campaign-01-analysis/evidence/generated/case_results.csv"], ["envs/epistemic_games/files/core.py", "envs/epistemic_games/files/renderer.py"], []),
    ("POST-02", "POST-02-C05", "Self-test, sample size, and mechanism/generalization limits", ["F-04", "F-07"], ["instance_oracles.json", "oracle_preflight.json"], "env:epistemic_games", ["campaign-01-analysis/evidence/generated/trace_index.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/epistemic_games/files/core.py", "envs/epistemic_games/files/renderer.py", "envs/epistemic_games/files/judge.py", "envs/epistemic_games/config.yaml"], []),
    ("POST-02", "POST-02-C06", "Prior work on epistemic logic, recursive ToM, deception, and causal-template generation", ["F-17"], [], "", ["campaign-01-analysis/sources/references.md"], [], ["MindGames: https://aclanthology.org/2023.findings-emnlp.303/", "Hi-ToM: https://aclanthology.org/2023.findings-emnlp.717/", "BigToM: https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and_Benchmarks.pdf"]),
    ("POST-02", "POST-02-C07", "Follow-up design for a separately specified recursive task", ["F-07"], [], "", ["campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/epistemic_games/files/core.py", "envs/epistemic_games/files/renderer.py", "envs/epistemic_games/files/judge.py"], []),
    ("POST-02", "POST-02-C08", "Narrow positive headline: seven selected policy-Bayes cases pass", ["F-07"], ["suite_checkpoint.json"], "env:epistemic_games", ["campaign-01-analysis/evidence/generated/case_results.csv"], [], []),

    ("POST-03", "POST-03-C01", "Category/compositional selected and eligible result counts and mode split", ["F-01", "F-03", "F-04", "F-08"], ["campaign_report.json", "instance_oracles.json", "oracle_preflight.json", "suite_checkpoint.json", "pilot_manifest.json"], "family:category_theoretic_compositional", ["campaign-01-analysis/evidence/generated/analysis_family_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv"], [], []),
    ("POST-03", "POST-03-C02", "Optimizer prompt versus judge/visible-test scope in source comparator", ["F-15"], [], "", ["campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/cat_theo/compositional_optimizer/files/prompt.md", "envs/cat_theo/compositional_optimizer/files/judge.py", "envs/cat_theo/compositional_optimizer/files/visible_tests.py"], []),
    ("POST-03", "POST-03-C03", "Optimizer placeholders absent from comparator templates; outcomes are not an axis curve", ["F-01", "F-14"], ["pilot_manifest.json", "suite_checkpoint.json"], "env:compositional_optimizer", ["campaign-01-analysis/evidence/generated/axis_placeholder_audit.csv", "campaign-01-analysis/evidence/generated/config_hash_audit.csv"], ["envs/cat_theo/compositional_optimizer/config.yaml", "envs/cat_theo/compositional_optimizer/files/prompt.md", "envs/cat_theo/compositional_optimizer/files/judge.py", "envs/cat_theo/compositional_optimizer/files/visible_tests.py"], []),
    ("POST-03", "POST-03-C04", "Categorical-lens prompt/judge/visible-test and STRICT_LAWS behavior", ["F-08", "F-14", "F-15"], ["suite_checkpoint.json"], "env:categorical_lenses", ["campaign-01-analysis/evidence/generated/axis_placeholder_audit.csv", "campaign-01-analysis/evidence/generated/case_results.csv"], ["envs/cat_theo/categorical_lenses/config.yaml", "envs/cat_theo/categorical_lenses/files/prompt.md", "envs/cat_theo/categorical_lenses/files/judge.py", "envs/cat_theo/categorical_lenses/files/visible_tests.py"], []),
    ("POST-03", "POST-03-C05", "Physical-constraints prompt/judge ratio mismatch", ["F-15"], ["suite_checkpoint.json"], "env:sheaf_physical_constraints", ["campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/cat_theo/sheaf/sheaf_physical_constraints/files/prompt.md", "envs/cat_theo/sheaf/sheaf_physical_constraints/files/judge.py", "envs/cat_theo/sheaf/sheaf_physical_constraints/files/visible_tests.py"], []),
    ("POST-03", "POST-03-C06", "Family heterogeneity, outcome range, empty patches, and source-invalid failures", ["F-08", "F-09", "F-15"], ["suite_checkpoint.json"], "family:category_theoretic_compositional", ["campaign-01-analysis/evidence/generated/analysis_family_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/generated/failure_details.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], [], []),
    ("POST-03", "POST-03-C07", "Implementation-contract and axis-linter recommendations", ["F-08", "F-14", "F-15"], [], "", ["campaign-01-analysis/evidence/audit_config_axes.py", "campaign-01-analysis/evidence/source_implementation_audit.md"], [], []),
    ("POST-03", "POST-03-C08", "Bounded category-track conclusion", ["F-08", "F-16"], ["suite_checkpoint.json"], "family:category_theoretic_compositional", ["campaign-01-analysis/evidence/generated/analysis_family_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv"], [], []),

    ("POST-04", "POST-04-C01", "Raw scores, 24 omissions, provider-coded terminal cases, and denominator sensitivities", ["F-01", "F-02", "F-03"], ["campaign_report.json", "suite_checkpoint.json", "pilot_manifest.json"], "provider-terminal", ["campaign-01-analysis/evidence/generated/audit.json", "campaign-01-analysis/evidence/generated/campaign_exclusions.csv"], [], []),
    ("POST-04", "POST-04-C02", "Primary denominator mixes judge modes; compile-only is exploratory", ["F-04"], ["campaign_report.json", "instance_oracles.json", "oracle_preflight.json", "suite_checkpoint.json"], "all", ["campaign-01-analysis/evidence/generated/audit.json", "campaign-01-analysis/evidence/generated/case_results.csv"], [], []),
    ("POST-04", "POST-04-C03", "Eligible failure taxonomy and distinct patch/source/runtime outcomes", ["F-09"], ["suite_checkpoint.json"], "eligible-failures", ["campaign-01-analysis/evidence/generated/failure_taxonomy.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], [], []),
    ("POST-04", "POST-04-C04", "Overfit labels have trusted score 1 and missing-file notes; provider rows are invalid_action", ["F-03", "F-09"], [], "exact:[\"batchnorm_ema__optimizer_hint=easy_red_herring=medium_visible_tests=easy_data_complexity=easy_symptom_mask=easy__seed-0\",\"moco__naming=easy_distractors=easy_queue_math=easy_temperature=easy_visible_tests=medium_symptom_mask=easy__seed-0\",\"sheaf_physical_constraints__naming=easy_symptom_mask=easy__seed-0\",\"ts_trajectory__witness_status=broken_representation=reflective__seed-0\"]", ["campaign-01-analysis/evidence/generated/failure_details.csv"], [], []),
    ("POST-04", "POST-04-C05", "Recorded ML-debugging track includes seven epistemic cases; semantic regrouping counts", ["F-05"], ["suite_checkpoint.json"], "union:[\"family:ml_debugging\",\"env:epistemic_games\"]", ["campaign-01-analysis/evidence/generated/track_summary.csv", "campaign-01-analysis/evidence/generated/analysis_family_summary.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/epistemic_games/files/core.py"], []),
    ("POST-04", "POST-04-C06", "Prior SWE-bench result bounds test-validation claims; it is not a campaign rate", ["F-01", "F-04", "F-09", "F-15", "F-17"], ["campaign_report.json", "instance_oracles.json", "suite_checkpoint.json", "pilot_manifest.json"], "family:category_theoretic_compositional", ["campaign-01-analysis/evidence/generated/failure_details.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/cat_theo/compositional_optimizer/files/prompt.md", "envs/cat_theo/compositional_optimizer/files/judge.py", "envs/cat_theo/sheaf/sheaf_physical_constraints/files/prompt.md", "envs/cat_theo/sheaf/sheaf_physical_constraints/files/judge.py"], ["SWE-bench empirical study: https://dl.acm.org/doi/10.1145/3744916.3764576"]),
    ("POST-04", "POST-04-C07", "Run-directory, retry-counter, reasoning metadata, and absent-cost observations", ["F-13"], ["coverage.json", "campaign_progress.json", "pilot_manifest.json", "campaign_telemetry.json", "runtime.json"], "", ["campaign-01-analysis/evidence/generated/audit.json", "campaign-01-analysis/evidence/generated/run_attempts.csv", "campaign-01-analysis/evidence/generated/trace_index.csv"], [], []),
    ("POST-04", "POST-04-C08", "Multi-layer dashboard recommendation and multi-metric precedent", ["F-04", "F-09", "F-13", "F-17"], ["campaign_report.json", "suite_checkpoint.json"], "", ["campaign-01-analysis/evidence/generated/failure_taxonomy.csv", "campaign-01-analysis/evidence/generated/audit.json"], [], ["HELM: https://arxiv.org/abs/2211.09110"]),
    ("POST-04", "POST-04-C09", "Scalar is a summary, not a substitute for traceable terminal artifacts", ["F-09", "F-13", "F-16"], ["suite_checkpoint.json"], "eligible-failures", ["campaign-01-analysis/evidence/generated/failure_taxonomy.csv", "campaign-01-analysis/evidence/generated/failure_details.csv", "campaign-01-analysis/evidence/generated/run_attempts.csv"], [], []),

    ("POST-05", "POST-05-C01", "Six weird-machine environments and eligible case total", ["F-10"], ["suite_checkpoint.json"], "family:weird_machine", ["campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/generated/analysis_family_summary.csv"], [], []),
    ("POST-05", "POST-05-C02", "Regex surface/depth outcome pattern and output lengths", ["F-06", "F-10"], [], "env:regex_state_machine", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/regex_state_machine/config.yaml", "envs/weird_machine/regex_state_machine/files/prompt.md", "envs/weird_machine/regex_state_machine/files/judge.py"], []),
    ("POST-05", "POST-05-C03", "Regex name/hint confound, single seed, and dirty-source boundary", ["F-01", "F-10"], ["pilot_manifest.json", "suite_checkpoint.json"], "env:regex_state_machine", ["campaign-01-analysis/evidence/generated/config_hash_audit.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/weird_machine/regex_state_machine/config.yaml", "envs/weird_machine/regex_state_machine/files/prompt.md", "envs/weird_machine/regex_state_machine/files/judge.py"], []),
    ("POST-05", "POST-05-C04", "CSS, SQL, and spreadsheet cells, input-size proxies, and validation failures", ["F-06", "F-09", "F-10"], [], "envset:[\"css_state_machine\",\"sql_fixed_point\",\"spreadsheet_dataflow\"]", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/css_state_machine/config.yaml", "envs/weird_machine/css_state_machine/files/judge.py", "envs/weird_machine/sql_fixed_point/config.yaml", "envs/weird_machine/sql_fixed_point/files/judge.py", "envs/weird_machine/spreadsheet_dataflow/config.yaml", "envs/weird_machine/spreadsheet_dataflow/files/judge.py"], []),
    ("POST-05", "POST-05-C05", "Task-specific checks and non-equivalent hidden-depth proxies", ["F-10"], ["suite_checkpoint.json"], "family:weird_machine", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/source_implementation_audit.md"], ["envs/weird_machine/regex_state_machine/config.yaml", "envs/weird_machine/regex_state_machine/files/judge.py", "envs/weird_machine/css_state_machine/config.yaml", "envs/weird_machine/css_state_machine/files/judge.py", "envs/weird_machine/sql_fixed_point/config.yaml", "envs/weird_machine/sql_fixed_point/files/judge.py", "envs/weird_machine/spreadsheet_dataflow/config.yaml", "envs/weird_machine/spreadsheet_dataflow/files/judge.py", "envs/weird_machine/ci_dependency_graph/config.yaml", "envs/weird_machine/template_interpreter/config.yaml"], []),
    ("POST-05", "POST-05-C06", "Prior perturbation work and category-axis comparator finding; no run-source identity proof", ["F-01", "F-10", "F-14", "F-17"], ["pilot_manifest.json"], "", ["campaign-01-analysis/evidence/generated/axis_placeholder_audit.csv", "campaign-01-analysis/evidence/source_implementation_audit.md", "campaign-01-analysis/sources/references.md"], [], ["VarBench: https://aclanthology.org/2024.findings-emnlp.946/", "HELM: https://arxiv.org/abs/2211.09110"]),
    ("POST-05", "POST-05-C07", "Future matched, randomized, repeated, rendered-diff experiment", ["F-06", "F-10", "F-14"], [], "", ["campaign-01-analysis/evidence/audit_config_axes.py", "campaign-01-analysis/evidence/source_implementation_audit.md"], [], []),
    ("POST-05", "POST-05-C08", "Narrow weird-machine conclusion and rejection of a general causal law", ["F-06", "F-10", "F-16"], ["suite_checkpoint.json"], "env:regex_state_machine", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/environment_summary.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], [], []),
    ("POST-05", "POST-05-C09", "Speculative hypothesis: surface names or hard hint may matter more than tested length in this specific regex pilot", ["F-18"], [], "env:regex_state_machine", ["campaign-01-analysis/evidence/generated/axis_summary.csv", "campaign-01-analysis/evidence/generated/case_results.csv", "campaign-01-analysis/evidence/generated/failure_details.csv"], ["envs/weird_machine/regex_state_machine/config.yaml", "envs/weird_machine/regex_state_machine/files/prompt.md"], []),
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def select_cases(selector: str, cases: list[dict[str, str]]) -> list[dict[str, str]]:
    if not selector:
        return []
    if selector == "all":
        return cases
    if selector == "provider-terminal":
        return [row for row in cases if row["performance_eligible"] == "false" and "provider" in row["exclusion_reason"].lower()]
    if selector == "eligible-failures":
        return [row for row in cases if row["verdict"] == "FAIL" and row["performance_eligible"] == "true"]
    if selector.startswith("env:"):
        env = selector[4:]
        return [row for row in cases if row["environment"] == env]
    if selector.startswith("envset:"):
        envs = json.loads(selector[7:])
        return [row for row in cases if row["environment"] in envs]
    if selector.startswith("family:"):
        family = selector[7:]
        return [row for row in cases if row["analysis_family"] == family]
    if selector.startswith("track:"):
        track = selector[6:]
        return [row for row in cases if row["track"] == track]
    if selector.startswith("exact:"):
        ids = set(json.loads(selector[6:]))
        return [row for row in cases if row["case_id"] in ids]
    if selector.startswith("union:"):
        result: dict[str, dict[str, str]] = {}
        for child in json.loads(selector[6:]):
            for row in select_cases(child, cases):
                result[row["case_id"]] = row
        return list(result.values())
    raise ValueError(f"Unknown selector: {selector}")


def member_paths(rows: list[dict[str, str]], traces: dict[str, dict[str, str]], roots: list[str]) -> list[str]:
    result = [f"archive root: {root}" for root in roots]
    if not rows:
        return result
    # For broad groups, the checkpoint is the immutable row-level source; case_ids
    # in the adjacent column keep the subset explicit without copying hundreds of paths.
    if len(rows) > 15:
        result.append("archive root: suite_checkpoint.json#/results")
        return result
    for row in rows:
        for key in ("result_member", "final_member"):
            value = row.get(key, "")
            if value and value not in result:
                result.append(value)
        trace = traces.get(row["case_id"], {})
        for key in ("submission_patch_member", "trace_member", "api_errors_member"):
            value = trace.get(key, "")
            if value and value not in result:
                result.append(value)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        default=SOURCE_ROOT,
        help="optional local clean source comparator at the recorded commit; when absent, paths remain documented but are not locally checked",
    )
    args = parser.parse_args()
    source_root = args.source_root
    source_available = source_root.is_dir()

    cases = load_csv(GENERATED / "case_results.csv")
    traces = {row["case_id"]: row for row in load_csv(GENERATED / "trace_index.csv")}
    with FINDINGS.open(encoding="utf-8") as handle:
        finding_doc = json.load(handle)
    finding_index = {item["id"]: item for item in finding_doc["findings"]}
    draft_text = "\n".join(path.read_text(encoding="utf-8") for path in sorted(POSTS.glob("POST-*.md")))
    tags: dict[str, list[str]] = {}
    for claim_id, finding_text in re.findall(r"⟦(POST-\d\d-C\d\d) · ([^⟧]+)⟧", draft_text):
        tags[claim_id] = [part.strip() for part in finding_text.split("/")]

    spec_index = {spec[1]: spec for spec in SPECS}
    if set(tags) != set(spec_index):
        missing = sorted(set(tags) - set(spec_index))
        unused = sorted(set(spec_index) - set(tags))
        raise ValueError(f"Draft/spec tag mismatch; unmapped={missing}, unused={unused}")

    output_rows = []
    for claim_id, finding_ids in tags.items():
        spec = spec_index[claim_id]
        post, _, summary, declared_findings, raw_roots, selector, generated, source_paths, references = spec
        if set(finding_ids) != set(declared_findings):
            raise ValueError(f"Finding tag mismatch for {claim_id}: {finding_ids} != {declared_findings}")
        selected = select_cases(selector, cases)
        quantitative = {fid: finding_index[fid]["quantitative_result"] for fid in finding_ids}
        source_paths = [s for s in source_paths if not s.startswith("campaign-01-analysis/")]
        if source_available:
            for source in source_paths:
                if not (source_root / source).is_file():
                    raise FileNotFoundError(f"Comparator path not found: {source_root / source}")
        for item in generated:
            if not Path(item).is_file():
                raise FileNotFoundError(f"Evidence artifact not found: {item}")
        output_rows.append({
            "post_id": post,
            "claim_id": claim_id,
            "claim_summary": summary,
            "finding_ids": ";".join(finding_ids),
            "finding_quantitative_results": json.dumps(quantitative, ensure_ascii=False),
            "case_ids": json.dumps(sorted(row["case_id"] for row in selected), ensure_ascii=False),
            "raw_archive_members": json.dumps(member_paths(selected, traces, raw_roots), ensure_ascii=False),
            "generated_evidence_artifacts": "; ".join(generated),
            "source_comparator_paths": "; ".join(source_paths),
            "source_identity_qualifier": (f"Comparator at {COMPARATOR_REV}; archive records repository.dirty=true, so executed-source identity is not established." if source_paths else ""),
            "external_references": "; ".join(references),
        })

    fieldnames = list(output_rows[0])
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} claim links to {OUTPUT.relative_to(ROOT.parent)}")
    verification = "verified" if source_available else "not locally checked; comparator paths retained as references"
    print(f"Draft markers mapped: {len(tags)}; source comparator paths: {verification}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
