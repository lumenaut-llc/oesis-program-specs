import { repoLink } from "./releaseContent";

export const publicDiagrams = [
  {
    title: "System context",
    description:
      "Shows how parcel nodes, public context, parcel context, inference, homeowner views, and policy-gated shared outputs fit together.",
    takeaway: "The parcel view is primary; shared outputs are downstream and policy-gated.",
    audience: "Public overview",
    versionRelevance: "1.0 through later networked versions",
    purpose: "Explain the full system shape without exposing implementation detail.",
    relatedSpecs: [
      { label: "Technical architecture v0.1", href: repoLink("technical-architecture/v0.1/README.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") },
      { label: "Parcel platform overview", href: repoLink("software/parcel-platform/README.md") }
    ],
    code: `flowchart LR
    A["Purpose-built parcel nodes"] --> B["Ingest and normalization"]
    P["Public context"] --> B
    C["Parcel context and node registry"] --> D["Parcel inference"]
    B --> D
    D --> E["Homeowner parcel view"]
    D --> F["Policy-gated shared map"]
    D --> G["Exports, rights, and governance flows"]`
  },
  {
    title: "Recommended first integrated prototype",
    description:
      "Explains the current public-safe recommended parcel prototype and how modular nodes converge into one parcel experience.",
    takeaway: "The first useful release already behaves like one coherent parcel product, not a collection of disconnected devices.",
    audience: "Current release framing",
    versionRelevance: "1.0 and 1.5",
    purpose: "Show what the first integrated release looks like in practice.",
    relatedSpecs: [
      { label: "Integrated parcel kit BOM", href: repoLink("docs/build-guides/integrated-parcel-kit-bom.md") },
      { label: "Bench air node", href: repoLink("hardware/bench-air-node/README.md") },
      { label: "Mast-lite", href: repoLink("hardware/mast-lite/README.md") }
    ],
    code: `flowchart TB
    subgraph oneParcel["One parcel"]
        A["Bench-Air Node\\nindoor reference"]
        B["Mast-Lite\\nsheltered outdoor reference"]
        C["Flood Node\\noptional low-point module"]
    end

    R["Parcel identity\\nnode registry\\nsharing settings"] --> I["Single ingest path"]
    A --> I
    B --> I
    C --> I
    P["Public weather and smoke context"] --> E["Single inference engine"]
    I --> E
    R --> E
    E --> V["Single homeowner parcel view"]
    E --> S["Optional shared-map aggregation"]`
  },
  {
    title: "Data-rights and visibility boundary",
    description:
      "Shows how private parcel data, user-selected sharing, and public context remain distinct lanes in the system.",
    takeaway: "Open release does not erase privacy boundaries or turn real parcel-linked data into open data.",
    audience: "Governance and privacy",
    versionRelevance: "All versions",
    purpose: "Explain ownership and visibility rules visually.",
    relatedSpecs: [
      { label: "Governance and privacy", href: "/governance-and-privacy" },
      { label: "Shared neighborhood signal schema", href: repoLink("docs/data-model/shared-neighborhood-signal-schema.md") }
    ],
    code: `flowchart TB
    A["Private parcel data"] --> B["Parcel platform"]
    C["User-selected shared contributions"] --> D["Shared neighborhood signals"]
    E["Public external data"] --> F["Public context lane"]

    B --> G["Homeowner controls\\nconsent\\nrights requests"]
    D --> H["Coarse shared-map outputs"]
    F --> B
    D --> B

    X["No public parcel-resolution map\\nfor real contributed data"]`
  },
  {
    title: "Homeowner product surface",
    description:
      "Anchors the public product shape around the parcel experience rather than around separate device dashboards.",
    takeaway: "The homeowner-facing unit is the parcel, not the device dashboard.",
    audience: "Product overview",
    versionRelevance: "1.0 and beyond",
    purpose: "Show how the product stays centered on the parcel experience.",
    relatedSpecs: [
      { label: "Parcel platform overview", href: repoLink("software/parcel-platform/README.md") },
      { label: "Feature matrix", href: repoLink("docs/system-overview/feature-matrix-by-use-case.md") }
    ],
    code: `flowchart TB
    A["Parcel home screen"] --> B["Readiness cards"]
    A --> C["Event timeline"]
    A --> D["Evidence view"]
    A --> E["Node health and freshness"]
    A --> F["Sharing and rights controls"]

    B --> B1["shelter"]
    B --> B2["air quality"]
    B --> B3["heat"]
    B --> B4["flood"]
    B --> B5["power"]
    B --> B6["route"]`
  }
];
