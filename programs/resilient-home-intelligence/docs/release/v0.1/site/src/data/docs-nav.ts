export interface NavItem {
  label: string;
  href: string;
}

export interface NavSection {
  title: string;
  slug: string;
  items: NavItem[];
}

export const docsNav: NavSection[] = [
  {
    title: "Getting Started",
    slug: "getting-started",
    items: [
      { label: "Overview", href: "/docs/getting-started/overview.html" }
    ]
  },
  {
    title: "Data Model",
    slug: "data-model",
    items: [
      { label: "Overview", href: "/docs/data-model/overview.html" },
      { label: "Parcel State", href: "/docs/data-model/parcel-state-schema.html" },
      { label: "Node Observation", href: "/docs/data-model/node-observation-schema.html" },
      { label: "Node Registry", href: "/docs/data-model/node-registry-schema.html" },
      { label: "Parcel Context", href: "/docs/data-model/parcel-context-schema.html" },
      { label: "Public Context", href: "/docs/data-model/public-context-schema.html" },
      { label: "House State", href: "/docs/data-model/house-state-schema.html" },
      { label: "House Capability", href: "/docs/data-model/house-capability-schema.html" },
      { label: "Control Compatibility", href: "/docs/data-model/control-compatibility-schema.html" },
      { label: "Intervention Event", href: "/docs/data-model/intervention-event-schema.html" },
      { label: "Verification Outcome", href: "/docs/data-model/verification-outcome-schema.html" },
      { label: "Explanation Payload", href: "/docs/data-model/explanation-payload-schema.html" },
      { label: "Evidence Summary", href: "/docs/data-model/evidence-summary-schema.html" },
      { label: "Evidence Mode", href: "/docs/data-model/evidence-mode-and-observability.html" }
    ]
  },
  {
    title: "Privacy & Governance",
    slug: "privacy",
    items: [
      { label: "Sharing Settings", href: "/docs/data-model/sharing-settings-schema.html" },
      { label: "Consent Record", href: "/docs/data-model/consent-record-schema.html" },
      { label: "Rights Request", href: "/docs/data-model/rights-request-schema.html" },
      { label: "Neighborhood Signal", href: "/docs/data-model/shared-neighborhood-signal-schema.html" },
      { label: "Operator Access", href: "/docs/data-model/operator-access-event-schema.html" },
      { label: "Export Bundle", href: "/docs/data-model/export-bundle-schema.html" },
      { label: "Retention Report", href: "/docs/data-model/retention-cleanup-report-schema.html" },
      { label: "Sharing Store", href: "/docs/data-model/sharing-store-schema.html" }
    ]
  },
  {
    title: "Hardware",
    slug: "hardware",
    items: []
  },
  {
    title: "System Overview",
    slug: "system",
    items: []
  },
  {
    title: "Build Guides",
    slug: "build-guides",
    items: []
  },
  {
    title: "Pilot Playbooks",
    slug: "pilot-playbooks",
    items: []
  },
  {
    title: "Legal",
    slug: "legal",
    items: []
  }
];
