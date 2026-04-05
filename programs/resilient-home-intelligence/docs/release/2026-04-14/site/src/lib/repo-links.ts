const REPO_BASE = "https://github.com/lumenaut-llc/resilient-home-intelligence";
const DEFAULT_BRANCH = "main";

const repoBlob = (path: string) => `${REPO_BASE}/blob/${DEFAULT_BRANCH}/${path}`;

export const repoLinks = {
  repoHome: REPO_BASE,
  rootLicenses: repoBlob("LICENSES.md"),
  programReadme: repoBlob("programs/resilient-home-intelligence/README.md"),
  releaseReadme: repoBlob("programs/resilient-home-intelligence/docs/release/2026-04-14/README.md"),
  releaseNotice: repoBlob("programs/resilient-home-intelligence/docs/release/2026-04-14/NOTICE.md"),
  nodeObservationSchema: repoBlob(
    "programs/resilient-home-intelligence/docs/data-model/schemas/node-observation.schema.json"
  ),
  parcelStateSchema: repoBlob(
    "programs/resilient-home-intelligence/docs/data-model/schemas/parcel-state.schema.json"
  ),
  parcelStateExample: repoBlob(
    "programs/resilient-home-intelligence/docs/data-model/examples/parcel-state.example.json"
  ),
  dataOwnership: repoBlob("programs/resilient-home-intelligence/docs/privacy-governance/data-ownership.md"),
  privacy: repoBlob("programs/resilient-home-intelligence/docs/privacy-governance/privacy.md"),
  claimsAndLimitations: repoBlob(
    "programs/resilient-home-intelligence/docs/privacy-governance/claims-and-safety-language.md"
  ),
  governance: repoBlob("programs/resilient-home-intelligence/legal/GOVERNANCE.md"),
  ip: repoBlob("programs/resilient-home-intelligence/legal/ip.md"),
  datasetReleasePolicy: repoBlob("programs/resilient-home-intelligence/legal/dataset-release-policy.md"),
  contributionPolicy: repoBlob("programs/resilient-home-intelligence/legal/contribution-policy/README.md"),
  publicReleaseScope: repoBlob("programs/resilient-home-intelligence/legal/public-preview-scope.md"),
  holdbackList: repoBlob("programs/resilient-home-intelligence/legal/holdback-list.md"),
  operatorQuickstart: repoBlob("programs/resilient-home-intelligence/software/operator-quickstart.md")
};
