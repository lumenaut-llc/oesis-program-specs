"""Validation-task namespace scaffolding."""

from .base import TaskNamespace


VALIDATION_TASK_NAMESPACE = TaskNamespace(
    name="validation",
    description="Future shared validation flows for publication and build checks.",
    planned_consumers=(
        "Makefile (oesis-runtime)",
        "oesis-runtime: scripts/oesis_smoke_check.sh",
        "oesis-runtime: scripts/oesis_http_smoke_check.sh",
    ),
)
