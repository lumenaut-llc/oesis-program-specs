"""Structured publication allowlist defaults."""

from ..model import PublicationPolicy


current_public_preview_policy = PublicationPolicy(
    name="public_preview_2026_04_14",
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
        "release/2026-04-14/",
        "legal/privacy/",
        "architecture/",
        "legal/",
    ),
    excluded_from_public_navigation=(
        "release/2026-04-14/reviewer-packet-index.md",
        "release/2026-04-14/publish-internal-map.md",
        "release/2026-04-14/preview-execution-plan.md",
        "release/2026-04-14/launch-readiness-checklist.md",
        "legal/counsel-questions/",
        "legal/provisional-*",
    ),
    canonical_policy_sources=(
        "release/2026-04-14/site/public-content-allowlist.md",
        "release/2026-04-14/site/README.md",
        "legal/public-preview-scope.md",
    ),
)
