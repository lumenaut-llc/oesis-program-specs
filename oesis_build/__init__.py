"""Shared build-foundation scaffolding for the repository."""

from .adapters import CanonicalSourceAdapter, RepoLinkAdapter
from .model import ArtifactRef, PublicationPolicy, ReleaseManifest
from .paths import BuildRoots, build_roots
from .policy import current_public_preview_policy
from .tasks import TASK_NAMESPACES, TaskNamespace

__all__ = [
    "ArtifactRef",
    "BuildRoots",
    "CanonicalSourceAdapter",
    "PublicationPolicy",
    "ReleaseManifest",
    "RepoLinkAdapter",
    "TASK_NAMESPACES",
    "TaskNamespace",
    "build_roots",
    "current_public_preview_policy",
]
