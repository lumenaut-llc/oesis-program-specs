RUNTIME_REPO ?= ../oesis-runtime
PUBLIC_SITE_REPO ?= ../oesis-public-site

.PHONY: oesis-demo oesis-validate oesis-check oesis-http-check rhi-demo rhi-validate rhi-check rhi-http-check public-site-install public-site-dev public-site-build public-site-preview repo-split-sync-runtime-assets repo-split-build-contracts-bundle repo-split-build-runtime-evidence-bundle repo-split-build-public-content-bundle repo-split-extract-site repo-split-extract-runtime repo-split-stage

oesis-demo:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-demo

oesis-validate:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-validate

oesis-check:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-check

oesis-http-check:
	$(MAKE) -C "$(RUNTIME_REPO)" oesis-http-check

rhi-demo: oesis-demo

rhi-validate: oesis-validate

rhi-check: oesis-check

rhi-http-check: oesis-http-check

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
