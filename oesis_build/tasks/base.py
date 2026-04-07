"""Base task-namespace models for scaffolded build workflows."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class TaskNamespace:
    """Describe a future build-task namespace without implementing it yet."""

    name: str
    description: str
    planned_consumers: tuple[str, ...] = field(default_factory=tuple)
    behavior_status: str = "scaffold_only"
