"""Repository link adapters for downstream build consumers."""

import os
from dataclasses import dataclass, field

from ..paths import BuildRoots


@dataclass(frozen=True)
class RepoLinkAdapter:
    """Translate repo-relative paths into browser-friendly repository links."""

    roots: BuildRoots
    repo_blob_base: str = field(
        default_factory=lambda: os.environ.get(
            "OESIS_REPO_BLOB_BASE",
            "https://github.com/lumenaut-llc/resilient-home-intelligence/blob/main/",
        )
    )

    def repo_link(self, relative_path: str) -> str:
        """Build a repository blob URL from a repo-relative path."""

        return f"{self.repo_blob_base}{relative_path}"

    def release_doc_link(self, relative_path: str) -> str:
        """Build a blob URL for the current public release packet."""

        release_root = self.roots.repo_relative(self.roots.current_public_release_root)
        return self.repo_link(f"{release_root}/{relative_path}")

    def privacy_doc_link(self, relative_path: str) -> str:
        """Build a blob URL for privacy-governance documents."""

        privacy_root = self.roots.repo_relative(self.roots.privacy_governance_root)
        return self.repo_link(f"{privacy_root}/{relative_path}")

    def legal_doc_link(self, relative_path: str) -> str:
        """Build a blob URL for legal/governance documents."""

        legal_root = self.roots.repo_relative(self.roots.legal_root)
        return self.repo_link(f"{legal_root}/{relative_path}")
