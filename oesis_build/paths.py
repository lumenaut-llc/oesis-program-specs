"""Shared repository and release path primitives."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildRoots:
    """Canonical path roots used by build-facing code."""

    repo_root: Path
    program_root: Path
    legal_root: Path
    sites_root: Path
    public_preview_site_root: Path
    privacy_root: Path
    architecture_root: Path
    current_public_release_tag: str
    current_public_release_root: Path

    def repo_relative(self, path: Path) -> str:
        """Return a repository-relative POSIX path string."""

        return path.relative_to(self.repo_root).as_posix()


def build_roots(*, release_tag: str = "v1.0") -> BuildRoots:
    """Discover the current repository and program roots."""

    repo_root = Path(__file__).resolve().parents[1]
    program_root = repo_root
    legal_root = repo_root / "legal"
    sites_root = repo_root / "sites"
    public_preview_site_root = sites_root / "public-preview"
    privacy_root = legal_root / "privacy"
    architecture_root = repo_root / "architecture"
    current_public_release_root = repo_root / "release" / release_tag

    return BuildRoots(
        repo_root=repo_root,
        program_root=program_root,
        legal_root=legal_root,
        sites_root=sites_root,
        public_preview_site_root=public_preview_site_root,
        privacy_root=privacy_root,
        architecture_root=architecture_root,
        current_public_release_tag=release_tag,
        current_public_release_root=current_public_release_root,
    )
