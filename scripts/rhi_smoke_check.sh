#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[rhi-check] validating example payloads"
python3 programs/resilient-home-intelligence/software/ingest-service/scripts/validate_examples.py >/tmp/rhi-validate.out

echo "[rhi-check] running reference pipeline"
python3 programs/resilient-home-intelligence/software/parcel-platform/scripts/reference_pipeline.py >/tmp/rhi-demo.out

echo "[rhi-check] checking pipeline output shape"
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path("/tmp/rhi-demo.out").read_text(encoding="utf-8"))

required_top = {"node_packet", "normalized_observation", "parcel_state", "parcel_view"}
missing = required_top - payload.keys()
if missing:
    raise SystemExit(f"missing top-level keys: {sorted(missing)}")

parcel_state = payload["parcel_state"]
parcel_view = payload["parcel_view"]

for key in ("shelter_status", "reentry_status", "egress_status", "asset_risk_status"):
    if key not in parcel_state:
        raise SystemExit(f"parcel_state missing {key}")

for key in ("statuses", "summary", "confidence", "evidence_mode"):
    if key not in parcel_view:
        raise SystemExit(f"parcel_view missing {key}")

statuses = parcel_view["statuses"]
for key in ("shelter", "reentry", "egress", "asset_risk"):
    if key not in statuses:
        raise SystemExit(f"parcel_view.statuses missing {key}")

print("PASS rhi-check")
PY
