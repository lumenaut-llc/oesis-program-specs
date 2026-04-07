"""Shared repository and release path primitives."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildRoots:
    """Canonical path roots used by build-facing code."""

    repo_root: Path
    program_root: Path
    docs_root: Path
    legal_root: Path
    sites_root: Path
    public_preview_site_root: Path
    privacy_governance_root: Path
    system_overview_root: Path
    technical_architecture_root: Path
    current_public_release_tag: str
    current_public_release_root: Path

    def repo_relative(self, path: Path) -> str:
        """Return a repository-relative POSIX path string."""

        return path.relative_to(self.repo_root).as_posix()


def build_roots(*, release_tag: str = "2026-04-14") -> BuildRoots:
    """Discover the current repository and program roots."""

    repo_root = Path(__file__).resolve().parents[1]
    program_root = repo_root / "programs" / "open-environmental-sensing-and-inference-system"
    docs_root = program_root / "docs"
    legal_root = program_root / "legal"
    sites_root = repo_root / "sites"
    public_preview_site_root = sites_root / "public-preview"
    privacy_governance_root = docs_root / "privacy-governance"
    system_overview_root = docs_root / "system-overview"
    technical_architecture_root = program_root / "technical-architecture"
    current_public_release_root = docs_root / "release" / release_tag

    return BuildRoots(
        repo_root=repo_root,
        program_root=program_root,
        docs_root=docs_root,
        legal_root=legal_root,
        sites_root=sites_root,
        public_preview_site_root=public_preview_site_root,
        privacy_governance_root=privacy_governance_root,
        system_overview_root=system_overview_root,
        technical_architecture_root=technical_architecture_root,
        current_public_release_tag=release_tag,
        current_public_release_root=current_public_release_root,
    )
