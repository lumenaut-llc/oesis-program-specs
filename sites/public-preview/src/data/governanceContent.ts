import { legalDocLink, privacyDocLink } from "../lib/releaseAdapters";

export const governanceSourceLinks = [
  { label: "Data ownership", href: privacyDocLink("data-ownership.md") },
  { label: "Privacy", href: privacyDocLink("privacy.md") },
  {
    label: "Claims and safety language",
    href: privacyDocLink("claims-and-safety-language.md")
  },
  { label: "Governance", href: legalDocLink("GOVERNANCE.md") },
  { label: "IP position", href: legalDocLink("ip.md") }
];
