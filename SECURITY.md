# Security Policy

## Reporting a vulnerability

If you believe you have found a security vulnerability, use
**GitHub > Security > Report a vulnerability** on this repository. Do not file
a public issue.

For issues that span program specifications, runtime code, and the public site,
report on the most relevant repository first and coordinate with maintainers as
needed.

## What to include

- Description of the vulnerability and its potential impact
- Steps to reproduce, if applicable
- Affected files, endpoints, or contract objects
- Suggested fix, if you have one

## Response timeline

- **Acknowledgment:** within 48 hours of report
- **Triage and assessment:** within 7 days
- **Fix for critical issues:** target within 14 days of confirmed triage
- **Fix for non-critical issues:** target within 30 days

These timelines are best-effort targets for a small open-source project. We
will communicate delays if they occur.

## Supported scope

Security reports are accepted for:

- **oesis-program-specs** — contract schemas, governance rules, publication
  controls, build scripts
- **oesis-runtime** — Python reference services, inference logic, data handling
- **oesis-public-site** — Next.js site, content rendering, publication boundary

## Disclosure

We follow coordinated disclosure. We will work with reporters to agree on a
disclosure timeline before any public announcement. Credit will be given to
reporters unless they prefer to remain anonymous.

## Not in scope

- Vulnerabilities in third-party dependencies that have already been publicly
  disclosed (please check upstream first)
- Issues in development tooling that do not affect the deployed system
- Theoretical attacks that require physical access to hardware nodes (report
  these as regular issues for the hardware threat model)
