#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

INGEST_PID=""
INFERENCE_PID=""
PARCEL_PID=""

cleanup() {
  for pid in "$PARCEL_PID" "$INFERENCE_PID" "$INGEST_PID"; do
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
      wait "$pid" 2>/dev/null || true
    fi
  done
}
trap cleanup EXIT

echo "[oesis-http-check] starting ingest api"
python3 -m oesis.ingest.serve_ingest_api --host 127.0.0.1 --port 8787 >/tmp/oesis-ingest.log 2>&1 &
INGEST_PID=$!

echo "[oesis-http-check] starting inference api"
python3 -m oesis.inference.serve_inference_api --host 127.0.0.1 --port 8788 >/tmp/oesis-inference.log 2>&1 &
INFERENCE_PID=$!

echo "[oesis-http-check] starting parcel-platform api"
python3 -m oesis.parcel_platform.serve_parcel_api --host 127.0.0.1 --port 8789 >/tmp/oesis-parcel.log 2>&1 &
PARCEL_PID=$!

sleep 1

echo "[oesis-http-check] checking health endpoints"
curl -s http://127.0.0.1:8787/v1/ingest/health >/tmp/oesis-ingest-health.json
curl -s http://127.0.0.1:8788/v1/inference/health >/tmp/oesis-inference-health.json
curl -s http://127.0.0.1:8789/v1/parcel-platform/health >/tmp/oesis-parcel-health.json

NODE_PACKET_EXAMPLE="$(python3 - <<'PY'
from oesis.common.repo_paths import DOCS_EXAMPLES_DIR

print((DOCS_EXAMPLES_DIR / "node-observation.example.json").resolve())
PY
)"

echo "[oesis-http-check] posting node packet to ingest api"
curl -s -X POST http://127.0.0.1:8787/v1/ingest/node-packets \
  -H 'Content-Type: application/json' \
  -H 'X-OESIS-Parcel-Id: parcel_demo_http' \
  --data-binary @"$NODE_PACKET_EXAMPLE" \
  >/tmp/oesis-ingest-response.json

echo "[oesis-http-check] posting normalized observation to inference api"
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path("/tmp/oesis-ingest-response.json").read_text(encoding="utf-8"))
Path("/tmp/oesis-normalized-from-http.json").write_text(
    json.dumps(payload["normalized_observation"]),
    encoding="utf-8",
)
PY

curl -s -X POST http://127.0.0.1:8788/v1/inference/parcel-state \
  -H 'Content-Type: application/json' \
  -H 'X-OESIS-Computed-At: 2026-03-30T19:46:00Z' \
  --data-binary @/tmp/oesis-normalized-from-http.json \
  >/tmp/oesis-inference-response.json

echo "[oesis-http-check] posting parcel state to parcel-platform api"
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path("/tmp/oesis-inference-response.json").read_text(encoding="utf-8"))
Path("/tmp/oesis-parcel-state-from-http.json").write_text(
    json.dumps(payload["parcel_state"]),
    encoding="utf-8",
)
PY

curl -s -X POST http://127.0.0.1:8789/v1/parcels/state/view \
  -H 'Content-Type: application/json' \
  --data-binary @/tmp/oesis-parcel-state-from-http.json \
  >/tmp/oesis-parcel-response.json

echo "[oesis-http-check] checking response shapes"
python3 - <<'PY'
import json
from pathlib import Path

def load(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))

ingest_health = load("/tmp/oesis-ingest-health.json")
inference_health = load("/tmp/oesis-inference-health.json")
parcel_health = load("/tmp/oesis-parcel-health.json")
ingest_payload = load("/tmp/oesis-ingest-response.json")
inference_payload = load("/tmp/oesis-inference-response.json")
parcel_payload = load("/tmp/oesis-parcel-response.json")

assert ingest_health["ok"] is True
assert inference_health["ok"] is True
assert parcel_health["ok"] is True

normalized = ingest_payload["normalized_observation"]
parcel_state = inference_payload["parcel_state"]
parcel_view = parcel_payload["parcel_view"]

for key in ("node_id", "parcel_id", "values", "provenance"):
    if key not in normalized:
        raise SystemExit(f"normalized observation missing {key}")

for key in ("shelter_status", "reentry_status", "egress_status", "asset_risk_status"):
    if key not in parcel_state:
        raise SystemExit(f"parcel_state missing {key}")

for key in ("statuses", "summary", "confidence", "evidence_mode"):
    if key not in parcel_view:
        raise SystemExit(f"parcel_view missing {key}")

print("PASS oesis-http-check")
PY
