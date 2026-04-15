# Contributing

Thank you for helping with OESIS program specifications, contracts, and release
materials. This guide covers what you need to know before opening a pull request.

## Code of conduct

All participants are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
Be respectful, constructive, and focused on what is best for the project.

## Security vulnerabilities

If you find a security vulnerability, **do not open a public issue**. Use
GitHub's private vulnerability reporting instead. See [SECURITY.md](SECURITY.md)
for response timelines and scope.

## Getting started

### Repository layout

| Directory | Contents | License |
| --- | --- | --- |
| Root, `architecture/`, `contracts/`, `program/`, `release/`, `legal/`, `operations/` | Documentation and specifications | CC BY-SA 4.0 ([`LICENSE`](LICENSE)) |
| `software/` | Reference code and tests | GNU AGPL v3 ([`software/LICENSE`](software/LICENSE)) |
| `hardware/` | Design files, wiring, build guides | CERN-OHL-S-2.0 ([`hardware/LICENSE`](hardware/LICENSE)) |
| `hardware/**/firmware/` | Firmware source | GNU AGPL v3 (per [`LICENSES.md`](LICENSES.md)) |

If a file has a more specific notice or license statement, that statement
controls (see [`NOTICE.md`](NOTICE.md)).

### Sibling repositories

The runnable Python reference implementation lives in
**[oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime)**. The public
preview site lives in
**[oesis-public-site](https://github.com/lumenaut-llc/oesis-public-site)**.

Changes that span repos (e.g., a new hardware contract that needs a normalizer)
should reference the companion PR in the other repo. You can open them in
parallel or sequence; just link them so reviewers see the full picture.

### Local validation

Clone the repo and siblings into the same parent directory, then:

```bash
# Validate JSON examples and schemas
make oesis-validate

# Run reference-path checks
make oesis-check

# Run HTTP smoke tests (starts and stops local servers)
make oesis-http-check
```

The Makefile expects `oesis-runtime` and `oesis-public-site` as sibling
directories. See the root [README](README.md) for full setup.

## Opening a pull request

### Before you start

1. Read [`NOTICE.md`](NOTICE.md) and [`LICENSES.md`](LICENSES.md).
2. For nontrivial changes, open an issue first to discuss the approach.
3. Follow the reviewer-oriented guide at
   [`release/v1.0/contributor-and-review-guide.md`](release/v1.0/contributor-and-review-guide.md).

### PR checklist

The [pull request template](.github/PULL_REQUEST_TEMPLATE.md) asks you to
confirm:

- Which **asset class** (license) applies to your changes
- That you have read CONTRIBUTING.md and NOTICE.md
- That your changes contain **no real participant data or credentials**
- That changes are consistent with sibling repos where applicable
- That you have updated relevant documentation

### Commit messages

Use short, descriptive commit messages. Prefix with the area when helpful:

```
docs: add v0.1 minimum subset callout to parcel-state schema
hardware: complete circuit-monitor wiring guide
fix: correct stale path in implementation-posture
```

### Version lanes

OESIS uses a lane overlay system (`v0.1` baseline, `v1.0` overlay, etc.). When
your change affects a specific lane:

- Place baseline contracts and examples under `contracts/v0.1/`
- Place overlay additions under `contracts/v1.0/` or later
- Set `OESIS_RUNTIME_LANE=v1.0` (or appropriate lane) when testing overlay
  features

See [`program/operating-packet/00-version-labels-and-lanes.md`](program/operating-packet/00-version-labels-and-lanes.md)
for the full glossary of program phases, capability stages, and runtime lanes.

## Governance and privacy

Privacy, data ownership, and publication boundaries are documented under
[`legal/`](legal/). Key rules:

- Do not include secrets, non-cleared third-party data, or real participant
  parcel-linked data unless explicitly part of an approved public release
- The `.gitignore` excludes firmware secrets files (`secrets.h`, `config.h`) —
  use `config.example.h` templates instead
- Review [`legal/privacy/permissions-matrix.md`](legal/privacy/permissions-matrix.md)
  before touching sharing, consent, or data export surfaces

## Questions?

Open a [discussion](https://github.com/lumenaut-llc/oesis-program-specs/discussions)
or an issue. We are happy to help orient new contributors.
