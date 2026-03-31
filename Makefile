.PHONY: rhi-demo rhi-validate rhi-check rhi-http-check

rhi-demo:
	python3 programs/resilient-home-intelligence/software/parcel-platform/scripts/reference_pipeline.py

rhi-validate:
	python3 programs/resilient-home-intelligence/software/ingest-service/scripts/validate_examples.py

rhi-check:
	./scripts/rhi_smoke_check.sh

rhi-http-check:
	./scripts/rhi_http_smoke_check.sh
