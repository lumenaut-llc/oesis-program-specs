"""Site-task namespace scaffolding."""

from .base import TaskNamespace


SITE_TASK_NAMESPACE = TaskNamespace(
    name="site",
    description="Future shared site-build adapters and publication-safe surfaces.",
    planned_consumers=(
        "../oesis-public-site",
        "site-side publication policy consumers",
    ),
)
