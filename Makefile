RUNTIME_REPO ?= ../oesis-runtime
CONTRACTS_REPO ?= ../oesis-contracts
PUBLIC_SITE_REPO ?= ../oesis-public-site

.PHONY: cross-repo-sync cross-repo-sync-fix cross-repo-sync-dry-run oesis-demo oesis-validate oesis-accept oesis-check oesis-http-check contracts-validate public-site-install public-site-dev public-site-build public-site-preview repo-split-sync-runtime-assets repo-split-build-contracts-bundle repo-split-build-runtime-evidence-bundle repo-split-build-public-content-bundle repo-split-extract-site repo-split-extract-runtime repo-split-stage print-bundle print-bundle-full print-bundle-pdf

# Read-only concat of v0.1 technical markdown → build/print/ (gitignored)
print-bundle:
	python3 meta/print/bundle_v01_technical.py

print-bundle-full:
	python3 meta/print/bundle_v01_technical.py --extras --bench-air

print-bundle-pdf:
	python3 meta/print/bundle_v01_technical.py --extras --bench-air --pdf

cross-repo-sync:
	python3 scripts/cross_repo_sync_check.py

# Apply contracts->downstream propagation to all local sibling checkouts.
# Use this locally when you've edited oesis-contracts and want the other
# repos updated before opening PRs.
cross-repo-sync-fix:
	python3 scripts/repo_split.py all

# Show what cross-repo-sync-fix would change without writing anything.
cross-repo-sync-dry-run:
	python3 scripts/repo_split.py --dry-run all

contracts-validate:
	@find "$(CONTRACTS_REPO)" -name "*.example.json" -exec python3 -m json.tool {} \; >/dev/null && echo "PASS oesis-contracts JSON syntax"

oesis-demo:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-demo

oesis-validate:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-validate

oesis-accept:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-accept

oesis-check:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-check

oesis-http-check:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-http-check

public-site-install:
	npm --prefix "$(PUBLIC_SITE_REPO)" install

public-site-dev:
	npm --prefix "$(PUBLIC_SITE_REPO)" run dev

public-site-build:
	npm --prefix "$(PUBLIC_SITE_REPO)" run build

public-site-preview:
	npm --prefix "$(PUBLIC_SITE_REPO)" run preview

repo-split-sync-runtime-assets:
	python3 scripts/repo_split.py sync-runtime-assets

repo-split-build-contracts-bundle:
	python3 scripts/repo_split.py build-contracts-bundle

repo-split-build-runtime-evidence-bundle:
	python3 scripts/repo_split.py build-runtime-evidence-bundle

repo-split-build-public-content-bundle:
	python3 scripts/repo_split.py build-public-content-bundle

repo-split-extract-site:
	python3 scripts/repo_split.py extract-site-repo

repo-split-extract-runtime:
	python3 scripts/repo_split.py extract-runtime-repo

repo-split-stage: repo-split-sync-runtime-assets repo-split-build-contracts-bundle repo-split-build-public-content-bundle
