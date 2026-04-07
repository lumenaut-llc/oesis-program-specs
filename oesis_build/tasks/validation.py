"""Validation-task namespace scaffolding."""

from .base import TaskNamespace


VALIDATION_TASK_NAMESPACE = TaskNamespace(
    name="validation",
    description="Future shared validation flows for publication and build checks.",
    planned_consumers=(
        "Makefile",
        "scripts/oesis_smoke_check.sh",
        "scripts/oesis_http_smoke_check.sh",
    ),
)
