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
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/",
        "programs/open-environmental-sensing-and-inference-system/docs/privacy-governance/",
        "programs/open-environmental-sensing-and-inference-system/technical-architecture/",
        "programs/open-environmental-sensing-and-inference-system/docs/system-overview/",
        "programs/open-environmental-sensing-and-inference-system/legal/",
    ),
    excluded_from_public_navigation=(
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/reviewer-packet-index.md",
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/publish-internal-map.md",
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/preview-execution-plan.md",
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/launch-readiness-checklist.md",
        "programs/open-environmental-sensing-and-inference-system/legal/counsel-questions/",
        "programs/open-environmental-sensing-and-inference-system/legal/provisional-*",
    ),
    canonical_policy_sources=(
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/site/public-content-allowlist.md",
        "programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/site/README.md",
        "programs/open-environmental-sensing-and-inference-system/legal/public-preview-scope.md",
    ),
)
