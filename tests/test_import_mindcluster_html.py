from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.import_mindcluster_html import build_documents, extract_graph, write_import


def _graph() -> dict:
    return {
        "nodes": [
            {
                "id": "paper-a",
                "type": "paper",
                "title": "An unverified paper record",
                "author": "Author A",
                "date": "2026",
                "url": "https://example.invalid/paper-a",
                "desc": "The export annotation is preserved but not independently verified.",
            },
            {
                "id": "concept-a",
                "type": "concept",
                "title": "Research concept",
                "author": "Research concept",
                "date": "",
                "url": "",
                "desc": "Synthesis node from the export.",
            },
        ],
        "edges": [
            {"source": "paper-a", "type": "loosely-parallels", "target": "concept-a", "uncertain": True}
        ],
        "meta": {"last_verified": "2026-10-01", "notes": ["Export metadata only"]},
    }


def _html(graph: dict) -> str:
    return f'<html><title>Test Export</title><script>const G={json.dumps(graph)};const x=1;</script></html>'


def _source_meta() -> dict[str, str]:
    return {
        "title": "Test Export",
        "url": "https://github.com/example/repo/blob/main/graph.html",
        "raw_url": "https://raw.githubusercontent.com/example/repo/main/graph.html",
        "local_path": "graph.html",
        "repository_commit": "deadbeefcommit",
        "git_blob_sha": "deadbeef0123456789",
        "sha256": "0123456789abcdef",
        "retrieved_at": "2026-10-01T12:00:00+03:00",
    }


def test_extracts_json_literal_without_executing_html() -> None:
    html = _html(_graph()) + '<script>throw new Error("must not execute");</script>'
    parsed = extract_graph(html)
    assert parsed["nodes"][0]["id"] == "paper-a"
    assert parsed["edges"][0]["uncertain"] is True


def test_build_documents_preserves_provenance_and_uncertain_relation() -> None:
    index, nodes, edges, sources = build_documents(_graph(), source_meta=_source_meta())
    source_id = "src-mindcluster-html-export-deadbeef"
    paper = nodes["nodes"][0]
    assert paper["source_refs"] == [source_id]
    assert paper["candidate_source_refs"] == ["src-paper-a"]
    assert paper["claims"][1]["epistemic_status"] == "unverified"
    assert edges["edges"][0]["relation"] == "loosely-parallels"
    assert edges["edges"][0]["epistemic_status"] == "unverified"
    assert edges["edges"][0]["source_refs"] == [source_id]
    assert index["import"]["uncertain_edge_count"] == 1
    assert sources["sources"][1]["verification_status"] == "link_not_independently_verified"
    assert "linked page was not retrieved" in sources["sources"][1]["limitations"][1]


def test_import_writes_yaml_and_hash_manifest(tmp_path: Path) -> None:
    source = tmp_path / "graph.html"
    source.write_text(_html(_graph()), encoding="utf-8")
    out = tmp_path / "knowledge"
    html_bytes = source.read_bytes()
    git_blob_sha = hashlib.sha1(b"blob " + str(len(html_bytes)).encode() + b"\0" + html_bytes).hexdigest()
    manifest = write_import(
        source,
        out,
        source_url=_source_meta()["url"],
        raw_url=_source_meta()["raw_url"],
        repository_commit=_source_meta()["repository_commit"],
        git_blob_sha=git_blob_sha,
        retrieved_at=_source_meta()["retrieved_at"],
    )
    assert manifest["counts"]["nodes"] == 2
    assert manifest["counts"]["edges"] == 1
    assert manifest["validation"]["html_or_javascript_executed"] is False
    assert yaml.safe_load((out / "nodes.yaml").read_text())["nodes"][0]["id"] == "paper-a"
    assert json.loads((out / "import_manifest.json").read_text())["input"]["sha256"] == manifest["input"]["sha256"]


def test_invalid_edge_endpoint_is_rejected() -> None:
    graph = _graph()
    graph["edges"][0]["target"] = "missing-node"
    html = _html(graph)
    with pytest.raises(ValueError, match="endpoint"):
        extract_graph(html)


def test_write_import_rejects_wrong_git_blob_sha(tmp_path: Path) -> None:
    source = tmp_path / "graph.html"
    source.write_text(_html(_graph()), encoding="utf-8")
    meta = _source_meta()
    with pytest.raises(ValueError, match="Git blob SHA mismatch"):
        write_import(
            source,
            tmp_path / "knowledge",
            source_url=meta["url"],
            raw_url=meta["raw_url"],
            repository_commit=meta["repository_commit"],
            git_blob_sha="0" * 40,
            retrieved_at=meta["retrieved_at"],
        )
