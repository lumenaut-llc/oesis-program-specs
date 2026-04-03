.PHONY: rhi-demo rhi-validate rhi-check rhi-http-check rhi-test rhi-compile rhi-lint rhi-ci

PYTHON ?= python3
RUFF ?= $(PYTHON) -m ruff
CHECK_PATHS = rhi programs/resilient-home-intelligence/software/tests

rhi-demo:
	$(PYTHON) -m rhi.parcel_platform.reference_pipeline

rhi-validate:
	$(PYTHON) -m rhi.ingest.validate_examples

rhi-check:
	./scripts/rhi_smoke_check.sh

rhi-http-check:
	./scripts/rhi_http_smoke_check.sh

rhi-test:
	$(PYTHON) -m unittest discover -s programs/resilient-home-intelligence/software/tests -q

rhi-compile:
	$(PYTHON) -m compileall rhi

rhi-lint:
	$(RUFF) check $(CHECK_PATHS)

rhi-ci: rhi-lint rhi-test rhi-compile rhi-check rhi-http-check
