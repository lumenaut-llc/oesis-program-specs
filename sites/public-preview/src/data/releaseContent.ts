import {
  legalDocLink,
  privacyDocLink,
  releaseDocLink,
  repoLink
} from "../lib/releaseAdapters";

export { repoLink };

export const activePublicRelease = {
  id: "2026-04-14",
  title: "April 14, 2026 public preview",
  summary:
    "Current release-scoped public packet and publication boundary for the Astro preview site."
};

export const canonicalReleaseLinks = [
  { label: "Open source v1 summary", href: releaseDocLink("open-source-v1-summary.md") },
  {
    label: "Asset-class licensing matrix",
    href: releaseDocLink("asset-class-license-and-publication-matrix.md")
  },
  {
    label: "Contributor and review guide",
    href: releaseDocLink("contributor-and-review-guide.md")
  },
  { label: "Data ownership", href: privacyDocLink("data-ownership.md") },
  { label: "Privacy", href: privacyDocLink("privacy.md") },
  {
    label: "Claims and safety language",
    href: privacyDocLink("claims-and-safety-language.md")
  },
  { label: "Governance", href: legalDocLink("GOVERNANCE.md") },
  { label: "IP position", href: legalDocLink("ip.md") }
];
