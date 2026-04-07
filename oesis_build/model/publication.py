"""Publication-boundary models for build-facing consumers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicationPolicy:
    """Structured publication-boundary primitives."""

    name: str
    approved_anchors: tuple[str, ...]
    approved_source_roots: tuple[str, ...]
    excluded_from_public_navigation: tuple[str, ...]
    canonical_policy_sources: tuple[str, ...]
