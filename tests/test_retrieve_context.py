from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.retrieve_context import compile_context, retrieve


def _write_yaml(path: Path, doc: dict) -> None:
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def _mini_graph(tmp_path: Path) -> tuple[Path, Path, Path]:
    seed_path = tmp_path / "seed.yaml"
    _write_yaml(seed_path, {"title": "boundary contracts and local global composition", "research_question": "Do explicit interface contracts reduce composition failures?"})
    knowledge = tmp_path / "knowledge"
    knowledge.mkdir()
    _write_yaml(knowledge / "index.yaml", {"knowledge_base_id": "test", "nodes_file": "nodes.yaml", "edges_file": "edges.yaml", "sources_file": "sources.yaml"})
    _write_yaml(knowledge / "nodes.yaml", {"nodes": [
        {"id": "L-A", "type": "formal_literature", "title": "Compositional interface contracts", "concepts": ["boundary semantics", "local global composition"], "source_refs": ["SRC-A"], "candidate_source_refs": ["SRC-B"], "epistemic_status": "reported_by_source", "claims": [{"id": "A1", "statement": "Explicit boundary assumptions support modular verification.", "epistemic_status": "reported_by_source", "source_refs": ["SRC-A"]}], "candidate_formalism": True},
        {"id": "L-B", "type": "empirical_literature", "title": "Integration failures in agent teams", "concepts": ["multi-agent coordination"], "limitations": ["This study does not isolate contract structure from shared context."], "evidence_stance": "mixed", "epistemic_status": "reported_by_source", "source_refs": ["SRC-B"]},
        {"id": "C-C", "type": "concept", "title": "Distributed systems", "concepts": ["systems"], "epistemic_status": "interpretive"},
    ]})
    _write_yaml(knowledge / "edges.yaml", {"edges": [
        {"id": "E-AB", "source": "L-A", "target": "L-B", "relation": "competes_with", "epistemic_status": "interpretive", "source_refs": []},
        {"id": "E-BC", "source": "L-B", "target": "C-C", "relation": "related_to", "epistemic_status": "interpretive", "source_refs": []},
    ]})
    _write_yaml(knowledge / "sources.yaml", {"sources": [
        {"id": "SRC-A", "title": "Primary source A", "url": "https://example.invalid/a", "primary": True, "verification_status": "verified"},
        {"id": "SRC-B", "title": "Source B", "url": "https://example.invalid/b", "primary": False, "verification_status": "unverified"},
    ]})
    return seed_path, knowledge, tmp_path / "out"


def test_retrieval_expands_graph_and_preserves_relation_status(tmp_path: Path) -> None:
    seed, knowledge, out = _mini_graph(tmp_path)
    manifest = compile_context(seed, knowledge, out, hops=2, roles=["theorist", "skeptic", "prior_work_killer"])
    assert set(manifest["selected_node_ids"]) == {"L-A", "L-B", "C-C"}
    assert manifest["selected_edge_ids"] == ["E-AB", "E-BC"]
    assert manifest["retrieval_id"]
    skeptic = (out / "skeptic.md").read_text(encoding="utf-8")
    assert "CONTRADICTORY EVIDENCE" in skeptic
    assert "This study does not isolate contract structure" in skeptic
    assert "epistemic status: `interpretive`" in skeptic
    shared = (out / "shared.md").read_text(encoding="utf-8")
    assert "https://example.invalid/a" in shared
    assert "Candidate verification target (not checked)" in shared
    assert "https://example.invalid/b" in shared
    disk_manifest = json.loads((out / "retrieval_manifest.json").read_text(encoding="utf-8"))
    assert disk_manifest["knowledge_node_count"] == 3


def test_empty_knowledge_base_is_explicit_not_fabricated(tmp_path: Path) -> None:
    seed = tmp_path / "seed.yaml"
    _write_yaml(seed, {"title": "local validity and composition"})
    knowledge = tmp_path / "knowledge"
    knowledge.mkdir()
    _write_yaml(knowledge / "index.yaml", {"knowledge_base_id": "empty-test"})
    _write_yaml(knowledge / "nodes.yaml", {"nodes": []})
    _write_yaml(knowledge / "edges.yaml", {"edges": []})
    _write_yaml(knowledge / "sources.yaml", {"sources": []})
    out = tmp_path / "out"
    manifest = compile_context(seed, knowledge, out)
    assert manifest["selected_node_ids"] == []
    shared = (out / "shared.md").read_text(encoding="utf-8")
    assert "No prior-work evidence was retrieved" in shared
    assert "absence of nodes is not evidence of absence" in shared


def test_duplicate_node_ids_are_rejected() -> None:
    with pytest.raises(ValueError, match="unique"):
        retrieve({"title": "boundary"}, [{"id": "x"}, {"id": "x"}], [], [])


def test_unknown_role_is_rejected(tmp_path: Path) -> None:
    seed, knowledge, out = _mini_graph(tmp_path)
    with pytest.raises(ValueError, match="Unknown role"):
        compile_context(seed, knowledge, out, roles=["synthesizer"])
