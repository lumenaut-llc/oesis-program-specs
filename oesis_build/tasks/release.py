"""Release-task namespace scaffolding."""

from .base import TaskNamespace


RELEASE_TASK_NAMESPACE = TaskNamespace(
    name="release",
    description="Future release-packet assembly and manifest workflows.",
    planned_consumers=(
        "release/",
        "release-owned publication controls",
    ),
)
