"""Typed records shared by the small local mission runner.

The runtime stores execution facts, not scientific judgments. Mission design and
claim approval remain governed by research_protocol/protocol.md.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

JOB_STATUSES = (
    "queued",
    "running",
    "completed",
    "failed",
    "blocked",
    "waiting_for_human",
)


@dataclass(frozen=True)
class JobSpec:
    job_id: str
    mission_id: str
    role: str
    prompt_artifact: str
    input_artifacts: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    site: str = "arena"
    model: str | None = None
    profile: str | None = None
    output_artifact: str = ""
    timeout_seconds: int = 300


@dataclass(frozen=True)
class MissionSpec:
    mission_id: str
    mission_type: str
    path: Path
    inputs: dict[str, str]
    jobs: tuple[JobSpec, ...]
    sha256: str

    @property
    def job_map(self) -> dict[str, JobSpec]:
        return {job.job_id: job for job in self.jobs}


@dataclass
class ExecutionResult:
    response_text: str
    model_name: str | None = None
    conversation_id: str | None = None
    current_url: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class WaitingForHuman(Exception):
    """A UI or workflow condition needs a person; do not guess or retry blindly."""

    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.details = details or {}


@dataclass
class JobContext:
    mission: MissionSpec
    job: JobSpec
    run_dir: Path
    job_dir: Path
    prompt_text: str
    prompt_snapshot: Path
    prompt_sha256: str
    input_paths: tuple[Path, ...]
    input_records: tuple[dict[str, Any], ...]
    job_state: dict[str, Any]
    update_progress: Callable[[dict[str, Any]], None]
    browser: Any | None = None


class JobExecutor(Protocol):
    async def execute(self, context: JobContext) -> ExecutionResult:
        """Execute one job through its configured site adapter."""

    async def close(self) -> None:
        """Release browsers and other process-local resources."""
