.PHONY: rhi-demo rhi-validate

rhi-demo:
	python3 programs/resilient-home-intelligence/software/parcel-platform/scripts/reference_pipeline.py

rhi-validate:
	python3 programs/resilient-home-intelligence/software/ingest-service/scripts/validate_examples.py
