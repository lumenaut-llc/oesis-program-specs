"""Release manifest models for build-facing consumers."""

from dataclasses import dataclass, field

from .artifact import ArtifactRef


@dataclass(frozen=True)
class ReleaseManifest:
    """Represent a versioned release packet and its artifacts."""

    release_tag: str
    title: str
    summary: str
    artifacts: tuple[ArtifactRef, ...] = field(default_factory=tuple)
