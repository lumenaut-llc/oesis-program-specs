"""Scaffolded task namespaces for future build workflows."""

from .base import TaskNamespace
from .release import RELEASE_TASK_NAMESPACE
from .site import SITE_TASK_NAMESPACE
from .validation import VALIDATION_TASK_NAMESPACE

TASK_NAMESPACES = (
    RELEASE_TASK_NAMESPACE,
    SITE_TASK_NAMESPACE,
    VALIDATION_TASK_NAMESPACE,
)

__all__ = [
    "TASK_NAMESPACES",
    "TaskNamespace",
]
