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
    ),
    excluded_from_public_navigation=(
        "release/v1.0/reviewer-packet-index.md",
        "release/v1.0/publish-internal-map.md",
        "release/v1.0/preview-execution-plan.md",
        "release/v1.0/launch-readiness-checklist.md",
        "release/v1.0/NOTICE.md",
        "release/v1.0/asset-class-license-and-publication-matrix.md",
        "release/v1.0/contributor-and-review-guide.md",
        "release/v1.0/open-source-v1-summary.md",
        "release/v1.0/v1.0-acceptance-spec.md",
        "release/v1.0/v1.0-gap-register.md",
        "release/v1.0/v1.0-launch-checklist.md",
        "release/v1.0/v1.0-pilot-minimum-subset.md",
        "release/v1.0/v1.0-scope-matrix.md",
        "release/v1.0/v1.0-scope.md",
    ),
    canonical_policy_sources=(
        "artifacts/public-content-bundle/public-content-bundle.json",
    ),
)
