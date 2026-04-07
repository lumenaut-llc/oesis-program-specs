"""Release-task namespace scaffolding."""

from .base import TaskNamespace


RELEASE_TASK_NAMESPACE = TaskNamespace(
    name="release",
    description="Future release-packet assembly and manifest workflows.",
    planned_consumers=(
        "programs/open-environmental-sensing-and-inference-system/docs/release/",
        "release-owned publication controls",
    ),
)
