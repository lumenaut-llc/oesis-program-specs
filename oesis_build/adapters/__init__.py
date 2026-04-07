"""Adapter scaffolding for build-facing consumers."""

from .canonical_sources import CanonicalSourceAdapter
from .repo_links import RepoLinkAdapter

__all__ = [
    "CanonicalSourceAdapter",
    "RepoLinkAdapter",
]
