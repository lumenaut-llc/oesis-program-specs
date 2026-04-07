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
        "docs/release/2026-04-14/",
        "docs/privacy-governance/",
        "technical-architecture/",
        "docs/system-overview/",
        "legal/",
    ),
    excluded_from_public_navigation=(
        "docs/release/2026-04-14/reviewer-packet-index.md",
        "docs/release/2026-04-14/publish-internal-map.md",
        "docs/release/2026-04-14/preview-execution-plan.md",
        "docs/release/2026-04-14/launch-readiness-checklist.md",
        "legal/counsel-questions/",
        "legal/provisional-*",
    ),
    canonical_policy_sources=(
        "docs/release/2026-04-14/site/public-content-allowlist.md",
        "docs/release/2026-04-14/site/README.md",
        "legal/public-preview-scope.md",
    ),
)
