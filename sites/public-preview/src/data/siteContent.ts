import { repoLink } from "./releaseContent";

export const principles = [
  {
    title: "Parcel first",
    body: "Focus on parcel-level conditions instead of only coarse regional signals."
  },
  {
    title: "Private by default",
    body: "Raw homeowner-contributed data stays homeowner-controlled."
  },
  {
    title: "Shared by choice",
    body: "Broader sharing is opt-in, bounded, and policy-gated."
  }
];

export const currentRelease = {
  label: "1.0",
  title: "Single-home utility",
  scope: "Useful parcel awareness for one home.",
  productUnit: "Parcel",
  hazards: ["Smoke", "Flooding / runoff", "Heat"],
  boundary: "Non-enabling public preview",
  nextUnlock: "Integrated parcel kit"
};

export const v1InformationOverview = {
  title: "Why version 1 matters",
  body:
    "Version 1 is the first public release that establishes a trustworthy parcel information contract: what is directly observed, what is inferred from evidence, how uncertainty is explained, and what remains advisory rather than authoritative.",
  pillars: [
    {
      label: "Observed",
      title: "Direct parcel and public-context inputs",
      body: "Local nodes, parcel context, and relevant public feeds establish the first evidence base instead of asking the homeowner to trust a black box."
    },
    {
      label: "Inferred",
      title: "Parcel-state estimates from evidence",
      body: "The product turns those inputs into parcel-state estimates that stay parcel-first and do not pretend to be certainty or official alerts."
    },
    {
      label: "Explained",
      title: "Confidence, reasons, and evidence framing",
      body: "The homeowner view is meant to distinguish observed conditions from inferred conditions and show why the system is leaning in a given direction."
    },
    {
      label: "Bounded",
      title: "Advisory outputs inside a clear public boundary",
      body: "Version 1 defines what the system may say publicly, what remains private, and what the product does not claim to know or control."
    }
  ]
};

export const publicBoundary = {
  publicNow: [
    {
      title: "Mission and architecture",
      detail: "The parcel-first system model and high-level architecture are public."
    },
    {
      title: "Ownership and sharing",
      detail: "Ownership, privacy, and opt-in sharing rules are public."
    },
    {
      title: "Claims and limits",
      detail: "Claims, limitations, and public-safe diagrams are part of this release."
    }
  ],
  notPublicNow: [
    {
      title: "Implementation detail",
      detail: "Implementation-enabling technical detail remains out of scope."
    },
    {
      title: "Real contributed data",
      detail: "Real homeowner-contributed parcel-linked data is not blanket-open."
    },
    {
      title: "Safety authority claims",
      detail: "The project does not claim emergency authority or guaranteed safety."
    }
  ]
};

export const versionPath = [
  {
    label: "1.0",
    title: "Single-home utility",
    body: "First useful parcel awareness for one home.",
    adds: "Establishes the homeowner parcel view, ownership controls, and the first truthful public release boundary.",
    releaseWindow: "Current preview",
    status: "current"
  },
  {
    label: "1.5",
    title: "Integrated parcel kit",
    body: "One coherent parcel kit instead of separate nodes.",
    adds: "Unifies ingest, strengthens parcel evidence, and turns the first release into a more complete homeowner product surface.",
    releaseWindow: "Next build target",
    status: "next"
  },
  {
    label: "2.0",
    title: "Block intelligence",
    body: "First sparse shared intelligence across nearby parcels.",
    adds: "Introduces block-scale derived intelligence without abandoning parcel ownership rules or the parcel-first operating model.",
    releaseWindow: "Future direction",
    status: "future"
  },
  {
    label: "3.0",
    title: "Neighborhood network",
    body: "Neighborhood coordination becomes a first-class product layer.",
    adds: "Extends from block-scale inference to broader neighborhood coordination, richer shared signals, and clearer network behavior.",
    releaseWindow: "Future direction",
    status: "future"
  },
  {
    label: "4.0",
    title: "City federation",
    body: "Federated local systems connect at city scale.",
    adds: "Connects larger areas without collapsing local control, parcel ownership, or neighborhood-level governance.",
    releaseWindow: "Long-range direction",
    status: "future"
  }
];

export const phaseModel = [
  {
    bridge: "Between 1.0 and 1.5",
    title: "From instrumented parcel to integrated parcel kit",
    outcome:
      "The house stops looking like a few evidence points and starts behaving like one coherent parcel system.",
    phases: [
      {
        label: "1.1",
        title: "Evidence quality and confidence layer",
        body: "Observed vs inferred parcel state becomes clearer, with stronger confidence framing and reason codes for the homeowner view."
      },
      {
        label: "1.2",
        title: "Hazard-specific parcel workflows",
        body: "Smoke, flood / runoff, and heat move from one generic status model toward clearer parcel workflows and more truthful readiness framing."
      },
      {
        label: "1.6",
        title: "Interior response awareness",
        body: "The product begins relating outdoor forcing to indoor response and critical-room conditions instead of treating the parcel as exterior-only."
      },
      {
        label: "1.7",
        title: "Bounded action and verification loop",
        body: "Manual guidance and limited soft integrations are judged by did-it-help verification rather than assumed success."
      }
    ]
  },
  {
    bridge: "Between 1.5 and 2.0",
    title: "From one parcel kit to sparse local intelligence",
    outcome:
      "Shared awareness begins, but it still grows from parcel-first evidence rather than replacing it.",
    phases: [
      {
        label: "2.1",
        title: "Sparse shared inference",
        body: "A partially instrumented local area can support shared signals without requiring every house to look identical or participate at the same depth."
      },
      {
        label: "2.x",
        title: "Route, drainage, and edge dependency modeling",
        body: "Parcels are understood in relation to route vulnerability, low points, drainage edges, and other block-level dependencies."
      }
    ]
  },
  {
    bridge: "Between 2.0 and 3.0",
    title: "From block signals to neighborhood coordination",
    outcome:
      "The system matures from local inference into a broader shared layer that can support neighborhood-scale coordination.",
    phases: [
      {
        label: "2.5",
        title: "Shared neighborhood priors",
        body: "Block-scale evidence starts informing parcel priors, neighborhood context, and broader situational framing even where adoption is uneven."
      },
      {
        label: "2.8",
        title: "Operational neighborhood layer",
        body: "Neighborhood coordination becomes a distinct product concern instead of a loose extension of block intelligence."
      }
    ]
  },
  {
    bridge: "Between 3.0 and 4.0",
    title: "From neighborhood network to city federation",
    outcome:
      "The network scales outward by federation and interoperability rather than by collapsing local control into one central system.",
    phases: [
      {
        label: "3.5",
        title: "Federated interoperability and governance",
        body: "Independent local systems learn how to exchange signals, policies, and coarse status layers while preserving local ownership and governance boundaries."
      }
    ]
  }
];

export const informationInfrastructure = [
  {
    label: "Layer 1",
    title: "Observation layer",
    body: "Outdoor nodes, indoor monitors, parcel / site context, and public feeds provide the raw evidence that starts the parcel picture."
  },
  {
    label: "Layer 2",
    title: "Inference layer",
    body: "Observed signals are interpreted into parcel-state estimates, hazard framing, and later shared intelligence without collapsing the parcel-first model."
  },
  {
    label: "Layer 3",
    title: "Confidence and evidence layer",
    body: "The system needs to show why it thinks what it thinks: observed vs inferred framing, evidence quality, uncertainty, and confidence-bearing context."
  },
  {
    label: "Layer 4",
    title: "Decision surface",
    body: "The homeowner sees parcel status, reasons, recommended actions, and verification cues rather than hidden scores or unexplained outputs."
  },
  {
    label: "Layer 5",
    title: "Rights and sharing layer",
    body: "Private parcel-linked data stays homeowner-controlled, while any broader sharing remains opt-in, bounded, and policy-gated."
  }
];

export const hardwareSpecSections = [
  {
    id: "bench-air-node",
    name: "Bench Air Node",
    status: "released",
    whatItDoes: "Indoor or sheltered microclimate evidence node for the first end-to-end parcel stack.",
    whyItMatters: "It is the fastest hardware path from concept to real parcel evidence and exercises the full ingest-to-parcel-view flow.",
    diagramRelevance: ["System context", "Recommended first integrated prototype"],
    links: [
      { label: "Overview", href: repoLink("hardware/bench-air-node/README.md") },
      { label: "Build guide", href: repoLink("hardware/bench-air-node/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/bench-air-node/firmware/README.md") }
    ]
  },
  {
    id: "mast-lite",
    name: "Mast-Lite Outdoor Node",
    status: "released",
    whatItDoes: "Sheltered outdoor reference node that adds parcel-edge weather and air context.",
    whyItMatters: "It is the simplest outdoor step that turns a single-home slice into a more complete parcel kit.",
    diagramRelevance: ["Recommended first integrated prototype", "Homeowner product surface"],
    links: [
      { label: "Overview", href: repoLink("hardware/mast-lite/README.md") },
      { label: "Build guide", href: repoLink("hardware/mast-lite/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/mast-lite/firmware/README.md") }
    ]
  },
  {
    id: "flood-node",
    name: "Flood Node",
    status: "released",
    whatItDoes: "Low-point runoff evidence node focused on depth and rise-rate at meaningful parcel drainage points.",
    whyItMatters: "It adds flood-specific evidence without pretending a single sensor point is a parcel-wide flood truth engine.",
    diagramRelevance: ["Recommended first integrated prototype", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("hardware/flood-node/README.md") },
      { label: "Build guide", href: repoLink("hardware/flood-node/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/flood-node/firmware/README.md") }
    ]
  },
  {
    id: "thermal-pod",
    name: "Thermal Pod",
    status: "released",
    whatItDoes: "Scene-level thermal sensing pod that emits derived thermal metrics instead of raw frames.",
    whyItMatters: "It opens a privacy-safe path to area-based sensing while staying separate from the default parcel kit.",
    diagramRelevance: ["Homeowner product surface", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("hardware/thermal-pod/README.md") },
      { label: "Build guide", href: repoLink("hardware/thermal-pod/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/thermal-pod/firmware/README.md") }
    ]
  }
];

export const softwareSpecSections = [
  {
    id: "parcel-platform",
    name: "Parcel Platform",
    status: "released",
    whatItDoes: "Homeowner-facing parcel application and API surface for parcel-state outputs, evidence summaries, and freshness data.",
    whyItMatters: "It is the main product surface where parcel awareness becomes usable rather than hidden inside pipeline internals.",
    diagramRelevance: ["System context", "Homeowner product surface"],
    links: [
      { label: "Overview", href: repoLink("software/parcel-platform/README.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") },
      { label: "Feature matrix", href: repoLink("docs/system-overview/feature-matrix-by-use-case.md") }
    ]
  },
  {
    id: "ingest-service",
    name: "Ingest Service",
    status: "released",
    whatItDoes: "Accepts node packets and external feeds, validates them, and normalizes them into canonical observations.",
    whyItMatters: "It is the evidence boundary that turns raw packets into the parcel-first information model.",
    diagramRelevance: ["System context", "Recommended first integrated prototype"],
    links: [
      { label: "Overview", href: repoLink("software/ingest-service/README.md") },
      { label: "Data model", href: repoLink("docs/data-model/README.md") },
      { label: "Node observation schema", href: repoLink("docs/data-model/node-observation-schema.md") }
    ]
  },
  {
    id: "inference-engine",
    name: "Inference Engine",
    status: "released",
    whatItDoes: "Turns normalized observations, parcel context, and public context into parcel-state outputs with explicit uncertainty.",
    whyItMatters: "It is where parcel evidence becomes parcel-state guidance without pretending sparse evidence is certainty.",
    diagramRelevance: ["System context", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("software/inference-engine/README.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") },
      { label: "Evidence mode and observability", href: repoLink("docs/data-model/evidence-mode-and-observability.md") }
    ]
  },
  {
    id: "shared-map",
    name: "Shared Map",
    status: "released",
    whatItDoes: "Creates the coarse neighborhood condition layer and shared-map outputs from policy-gated shared signals.",
    whyItMatters: "It is the public-facing neighborhood layer that must stay downstream of parcel ownership and sharing controls.",
    diagramRelevance: ["System context", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("software/shared-map/README.md") },
      { label: "Shared map posture", href: repoLink("docs/system-overview/shared-map-product-posture.md") },
      { label: "Shared neighborhood signal schema", href: repoLink("docs/data-model/shared-neighborhood-signal-schema.md") }
    ]
  }
];

export const releasedSpecCollections = [
  {
    label: "Technical architecture",
    title: "Versioned architecture and operating model",
    body: "Current technical architecture guidance that explains how hardware, software, parcel identity, governance, and future architecture debate fit together.",
    links: [
      { label: "Technical architecture index", href: repoLink("technical-architecture/README.md") },
      { label: "Technical architecture v0.1", href: repoLink("technical-architecture/v0.1/README.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") },
      { label: "Phase roadmap", href: repoLink("docs/system-overview/phase-roadmap.md") }
    ]
  },
  {
    label: "Data model",
    title: "Schemas and canonical contracts",
    body: "Canonical parcel, node, observation, and sharing definitions for the released system surface.",
    links: [
      { label: "Data model index", href: repoLink("docs/data-model/README.md") },
      { label: "Parcel-state schema", href: repoLink("docs/data-model/parcel-state-schema.md") },
      { label: "Node registry schema", href: repoLink("docs/data-model/node-registry-schema.md") }
    ]
  },
  {
    label: "Build guides",
    title: "Hardware assembly and deployment guidance",
    body: "Cross-subsystem references for building, procuring, and installing the parcel kit.",
    links: [
      { label: "Build guides index", href: repoLink("docs/build-guides/README.md") },
      { label: "Integrated parcel kit BOM", href: repoLink("docs/build-guides/integrated-parcel-kit-bom.md") },
      { label: "Parcel installation checklist", href: repoLink("docs/build-guides/parcel-installation-checklist.md") }
    ]
  }
];
