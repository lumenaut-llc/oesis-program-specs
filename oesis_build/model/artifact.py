"""Artifact reference models for shared build code."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ArtifactRef:
    """Describe a canonical or derived build artifact."""

    path: str
    label: str
    category: str
    description: str = ""
    release_tag: str | None = None
    public: bool = False
    metadata: dict[str, str] = field(default_factory=dict)
