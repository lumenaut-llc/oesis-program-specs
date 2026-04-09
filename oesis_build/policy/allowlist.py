"""Structured publication allowlist defaults."""

from ..model import PublicationPolicy


current_public_preview_policy = PublicationPolicy(
    name="public_preview_v1_0",
    approved_anchors=(
        "/#snapshot",
        "/#roadmap",
        "/#how-it-works",
        "/#hardware-specs",
        "/#software-specs",
        "/#governance",
        "/#diagrams",
    ),
    approved_source_roots=(
        "release/v1.0/",
        "legal/privacy/",
        "architecture/",
        "legal/",
    ),
    excluded_from_public_navigation=(
        "release/v1.0/reviewer-packet-index.md",
        "release/v1.0/publish-internal-map.md",
        "release/v1.0/preview-execution-plan.md",
        "release/v1.0/launch-readiness-checklist.md",
        "legal/counsel-questions/",
        "legal/provisional-*",
    ),
    canonical_policy_sources=(
        "artifacts/public-content-bundle/public-content-bundle.json",
        "legal/public-preview-scope.md",
    ),
)
