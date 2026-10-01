"""Integrity check for the Mission 02 freeze (mission-02/freeze/game_cards.freeze.yaml).

This is a change-detector on purpose. The freeze records the exact text of the game-family cards
and vocabulary features as authored before any Council response existed, so a silent edit would
undermine the claim that the cards were written without sight of the Council's design.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "mission-02" / "freeze" / "game_cards.freeze.yaml"
VOCABULARY = ROOT / "research_protocol" / "structural_features.yaml"

ADVICE = (
    "A frozen Mission 02 input changed. Bump the card's version, add a new freeze entry that records "
    "what changed and why, and mark it post_council if any Council response was already stored."
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def test_frozen_mission_02_cards_and_features_are_unchanged() -> None:
    freeze = yaml.safe_load(FREEZE.read_text(encoding="utf-8"))
    assert freeze["cards"] and freeze["features"], "the freeze lists nothing"

    for card in freeze["cards"]:
        path = ROOT / card["file"]
        assert path.is_file(), f"frozen card {card['file']} is missing. {ADVICE}"
        assert _sha256(path.read_bytes()) == card["sha256"], f"{card['file']} changed. {ADVICE}"
        assert yaml.safe_load(path.read_text(encoding="utf-8"))["version"] == card["version"]

    features = {f["id"]: f for f in yaml.safe_load(VOCABULARY.read_text(encoding="utf-8"))["features"]}
    for feature_id, digest in freeze["features"].items():
        assert feature_id in features, f"frozen feature {feature_id} was removed from the vocabulary. {ADVICE}"
        canonical = json.dumps(features[feature_id], sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        assert _sha256(canonical.encode("utf-8")) == digest, f"feature {feature_id} changed. {ADVICE}"
