.PHONY: rhi-demo rhi-validate rhi-check rhi-http-check

rhi-demo:
	python3 -m rhi.parcel_platform.reference_pipeline

rhi-validate:
	python3 -m rhi.ingest.validate_examples

rhi-check:
	./scripts/rhi_smoke_check.sh

rhi-http-check:
	./scripts/rhi_http_smoke_check.sh
