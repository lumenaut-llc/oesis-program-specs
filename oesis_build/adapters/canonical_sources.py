"""Canonical source adapter scaffolding."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CanonicalSourceAdapter:
    """Describe a canonical source tree that a build consumer may read from."""

    name: str
    root: str
    description: str
