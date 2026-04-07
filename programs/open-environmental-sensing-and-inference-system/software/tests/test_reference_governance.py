import importlib.util
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path


PROGRAM_ROOT = Path(__file__).resolve().parents[2]
DOC_EXAMPLES = PROGRAM_ROOT / "docs" / "data-model" / "examples"
INGEST_SCRIPT_DIR = PROGRAM_ROOT / "software" / "ingest-service" / "scripts"
INFERENCE_SCRIPT_DIR = PROGRAM_ROOT / "software" / "inference-engine" / "scripts"
PARCEL_SCRIPT_DIR = PROGRAM_ROOT / "software" / "parcel-platform" / "scripts"
SHARED_SCRIPT_DIR = PROGRAM_ROOT / "software" / "shared-map" / "scripts"
WEATHER_PM_MAST_FIRMWARE = (
    PROGRAM_ROOT
    / "hardware"
    / "weather-pm-mast"
    / "firmware"
    / "weather_pm_mast_serial_json"
    / "weather_pm_mast_serial_json.ino"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, str(INGEST_SCRIPT_DIR))
sys.path.insert(0, str(INFERENCE_SCRIPT_DIR))
sys.path.insert(0, str(PARCEL_SCRIPT_DIR))
sys.path.insert(0, str(SHARED_SCRIPT_DIR))

normalize_packet = load_module("normalize_packet", INGEST_SCRIPT_DIR / "normalize_packet.py")
infer_parcel_state = load_module("infer_parcel_state", INFERENCE_SCRIPT_DIR / "infer_parcel_state.py")
format_parcel_view = load_module("format_parcel_view", PARCEL_SCRIPT_DIR / "format_parcel_view.py")
format_evidence_summary = load_module("format_evidence_summary", PARCEL_SCRIPT_DIR / "format_evidence_summary.py")
serve_parcel_api = load_module("serve_parcel_api", PARCEL_SCRIPT_DIR / "serve_parcel_api.py")
summarize_reference_state = load_module("summarize_reference_state", PARCEL_SCRIPT_DIR / "summarize_reference_state.py")
aggregate_shared_map = load_module("aggregate_shared_map", SHARED_SCRIPT_DIR / "aggregate_shared_map.py")
serve_shared_map_api = load_module("serve_shared_map_api", SHARED_SCRIPT_DIR / "serve_shared_map_api.py")
run_retention_cleanup = load_module("run_retention_cleanup", PARCEL_SCRIPT_DIR / "run_retention_cleanup.py")


class ReferenceGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.parcel_state = json.loads((DOC_EXAMPLES / "parcel-state.example.json").read_text(encoding="utf-8"))
        self.sharing_settings = json.loads((DOC_EXAMPLES / "sharing-settings.example.json").read_text(encoding="utf-8"))
        self.shared_signal = json.loads((DOC_EXAMPLES / "shared-neighborhood-signal.example.json").read_text(encoding="utf-8"))
        self.sharing_store_seed = json.loads((DOC_EXAMPLES / "sharing-store.example.json").read_text(encoding="utf-8"))
        self.rights_store_seed = json.loads((DOC_EXAMPLES / "rights-request-store.example.json").read_text(encoding="utf-8"))

    def test_parcel_view_includes_sharing_summary_and_data_classes(self):
        view = format_parcel_view.build_parcel_view(self.parcel_state, self.sharing_settings)
        self.assertIn("sharing_summary", view)
        self.assertTrue(view["sharing_summary"]["private_only"])
        self.assertEqual(view["data_classes_visible"], ["private_parcel_data", "derived_parcel_state"])

    def test_evidence_summary_groups_contributions_by_source_class(self):
        summary = format_evidence_summary.build_evidence_summary(self.parcel_state)
        self.assertEqual(summary["parcel_id"], "parcel_123")
        self.assertEqual(summary["confidence_band"], "low")
        self.assertIn("grouped_contributions", summary)
        self.assertIn("local", summary["grouped_contributions"])
        self.assertEqual(summary["grouped_contributions"]["local"][0]["contribution_id"], "local_siting_limit")

    def test_shared_map_uses_store_eligibility(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            store_path = Path(tmpdir) / "sharing-store.json"
            store_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")

            initial = aggregate_shared_map.aggregate_shared_map(
                self.shared_signal,
                sharing_store=aggregate_shared_map.load_sharing_store(store_path),
            )
            self.assertEqual(initial["cells"][0]["shared_signal_status"], "suppressed")

            updated = serve_parcel_api.clone_default_sharing("parcel_002")
            updated["private_only"] = False
            updated["neighborhood_aggregate"] = True
            serve_parcel_api.update_sharing_store(store_path, "parcel_002", updated)

            visible_payload = dict(self.shared_signal)
            visible_payload["min_participants"] = 2
            visible = aggregate_shared_map.aggregate_shared_map(
                visible_payload,
                sharing_store=aggregate_shared_map.load_sharing_store(store_path),
            )
            self.assertEqual(visible["cells"][0]["shared_signal_status"], "visible")
            self.assertEqual(visible["cells"][0]["shared_participant_count"], 2)

    def test_shared_map_inspection_summarizes_visible_and_suppressed_cells(self):
        inspection = serve_shared_map_api.build_shared_map_inspection(
            self.shared_signal,
            sharing_store=self.sharing_store_seed,
        )
        self.assertIn("shared_map", inspection)
        self.assertIn("inspection", inspection)
        self.assertEqual(inspection["inspection"]["cell_count"], 1)
        self.assertEqual(inspection["inspection"]["suppressed_cell_count"], 1)
        self.assertEqual(inspection["inspection"]["visible_cell_count"], 0)
        self.assertEqual(inspection["inspection"]["eligible_shared_ref_count"], 1)

    def test_shared_map_handler_loads_configured_sharing_store(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            serve_shared_map_api.SharedMapRequestHandler.sharing_store_path = sharing_path
            handler = serve_shared_map_api.SharedMapRequestHandler.__new__(serve_shared_map_api.SharedMapRequestHandler)
            configured = handler._configured_sharing_store()
            self.assertEqual(configured["parcels"][0]["parcel_id"], "parcel_001")

    def test_shared_map_inspection_exposes_eligible_refs_and_policy_notice(self):
        inspection = serve_shared_map_api.build_shared_map_inspection(
            self.shared_signal,
            sharing_store=self.sharing_store_seed,
        )
        self.assertEqual(inspection["inspection"]["eligible_shared_refs"], ["parcel_ref_parcel_001"])
        self.assertEqual(
            inspection["inspection"]["coverage_notice"],
            "Neighborhood conditions are delayed and aggregated. Participation is partial.",
        )
        self.assertFalse(inspection["inspection"]["public_map_supported"])

    def test_rights_requests_and_access_events_are_persisted_and_summarized(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            rights_path = Path(tmpdir) / "rights-store.json"
            access_path = Path(tmpdir) / "access-log.json"

            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            rights_path.write_text(json.dumps(self.rights_store_seed), encoding="utf-8")
            access_path.write_text("[]", encoding="utf-8")

            request = serve_parcel_api.build_rights_request("parcel_001", "delete")
            serve_parcel_api.append_rights_request(rights_path, request)
            serve_parcel_api.append_access_event(
                access_path,
                actor="parcel-platform-api",
                action="view_parcel_state",
                parcel_id="parcel_001",
                data_classes=["private_parcel_data", "derived_parcel_state"],
                justification="parcel_view_request",
            )

            summary = summarize_reference_state.summarize(
                json.loads(sharing_path.read_text(encoding="utf-8")),
                json.loads(rights_path.read_text(encoding="utf-8")),
                json.loads(access_path.read_text(encoding="utf-8")),
            )

            parcel_summary = summary["parcels"]["parcel_001"]
            self.assertEqual(len(parcel_summary["rights_requests"]), 2)
            self.assertEqual(len(parcel_summary["recent_access_events"]), 1)
            self.assertEqual(parcel_summary["recent_access_events"][0]["action"], "view_parcel_state")

    def test_reference_state_summary_helper_reads_file_backed_stores(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            rights_path = Path(tmpdir) / "rights-store.json"
            access_path = Path(tmpdir) / "access-log.json"

            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            rights_path.write_text(json.dumps(self.rights_store_seed), encoding="utf-8")
            access_path.write_text(
                json.dumps(
                    [
                        {
                            "event_id": "access_view_parcel_001_1",
                            "occurred_at": "2026-03-30T20:30:00Z",
                            "actor": "parcel-platform-api",
                            "action": "view_parcel_state",
                            "parcel_id": "parcel_001",
                            "data_classes": ["private_parcel_data"],
                            "justification": "parcel_view_request",
                        }
                    ]
                ),
                encoding="utf-8",
            )

            summary = serve_parcel_api.build_reference_state_summary(
                sharing_path,
                rights_path,
                access_path,
            )

            self.assertEqual(summary["parcel_count"], 3)
            self.assertIn("parcel_001", summary["parcels"])
            self.assertEqual(summary["parcels"]["parcel_001"]["recent_access_events"][0]["action"], "view_parcel_state")

    def test_delete_request_processing_completes_request_and_removes_sharing_state(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            rights_path = Path(tmpdir) / "rights-store.json"

            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            rights_store = {
                "updated_at": "2026-03-30T20:40:00Z",
                "requests": [
                    {
                        "request_id": "rights_delete_parcel_002",
                        "parcel_id": "parcel_002",
                        "account_id": "acct_123",
                        "request_type": "delete",
                        "status": "submitted",
                        "created_at": "2026-03-30T20:20:00Z",
                        "scope": ["private_parcel_data", "derived_parcel_state"],
                        "requested_from_surface": "parcel_settings_ui",
                    }
                ],
            }
            rights_path.write_text(json.dumps(rights_store), encoding="utf-8")

            result = serve_parcel_api.process_delete_request(
                rights_path,
                sharing_path,
                "rights_delete_parcel_002",
            )

            self.assertEqual(result["status"], "completed")
            updated_rights = json.loads(rights_path.read_text(encoding="utf-8"))
            self.assertEqual(updated_rights["requests"][0]["status"], "completed")

            updated_sharing = json.loads(sharing_path.read_text(encoding="utf-8"))
            remaining_ids = [entry["parcel_id"] for entry in updated_sharing["parcels"]]
            self.assertNotIn("parcel_002", remaining_ids)

    def test_export_request_processing_writes_bundle_and_completes_request(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            rights_path = Path(tmpdir) / "rights-store.json"
            access_path = Path(tmpdir) / "access-log.json"
            export_path = Path(tmpdir) / "parcel-export.json"
            parcel_state_path = Path(tmpdir) / "parcel-state.json"

            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            access_path.write_text(json.dumps([json.loads((DOC_EXAMPLES / "operator-access-event.example.json").read_text(encoding="utf-8"))]), encoding="utf-8")
            parcel_state = dict(self.parcel_state)
            parcel_state["parcel_id"] = "parcel_001"
            parcel_state_path.write_text(json.dumps(parcel_state), encoding="utf-8")
            rights_store = {
                "updated_at": "2026-03-30T20:40:00Z",
                "requests": [
                    {
                        "request_id": "rights_export_parcel_001",
                        "parcel_id": "parcel_001",
                        "account_id": "acct_123",
                        "request_type": "export",
                        "status": "submitted",
                        "created_at": "2026-03-30T20:20:00Z",
                        "scope": ["private_parcel_data", "derived_parcel_state"],
                        "requested_from_surface": "parcel_settings_ui",
                    }
                ],
            }
            rights_path.write_text(json.dumps(rights_store), encoding="utf-8")

            result = serve_parcel_api.process_export_request(
                rights_path,
                sharing_path,
                access_path,
                "rights_export_parcel_001",
                export_path,
                parcel_state_path=parcel_state_path,
            )

            self.assertEqual(result["status"], "completed")
            bundle = json.loads(export_path.read_text(encoding="utf-8"))
            self.assertEqual(bundle["parcel_id"], "parcel_001")
            self.assertIsNotNone(bundle["sharing"])
            self.assertEqual(bundle["parcel_state"]["parcel_id"], "parcel_001")
            updated_rights = json.loads(rights_path.read_text(encoding="utf-8"))
            self.assertEqual(updated_rights["requests"][0]["status"], "completed")

    def test_export_request_processing_uses_completed_status_inside_bundle(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sharing_path = Path(tmpdir) / "sharing-store.json"
            rights_path = Path(tmpdir) / "rights-store.json"
            access_path = Path(tmpdir) / "access-log.json"
            export_path = Path(tmpdir) / "parcel-export.json"

            sharing_path.write_text(json.dumps(self.sharing_store_seed), encoding="utf-8")
            access_path.write_text("[]", encoding="utf-8")
            rights_store = {
                "updated_at": "2026-03-30T20:40:00Z",
                "requests": [
                    {
                        "request_id": "rights_export_parcel_001",
                        "parcel_id": "parcel_001",
                        "account_id": "acct_123",
                        "request_type": "export",
                        "status": "submitted",
                        "created_at": "2026-03-30T20:20:00Z",
                        "scope": ["private_parcel_data", "derived_parcel_state"],
                        "requested_from_surface": "parcel_settings_ui",
                    }
                ],
            }
            rights_path.write_text(json.dumps(rights_store), encoding="utf-8")

            serve_parcel_api.process_export_request(
                rights_path,
                sharing_path,
                access_path,
                "rights_export_parcel_001",
                export_path,
            )

            bundle = json.loads(export_path.read_text(encoding="utf-8"))
            self.assertEqual(bundle["rights_requests"][0]["status"], "completed")

    def test_retention_cleanup_prunes_old_access_and_completed_export_requests(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            rights_path = Path(tmpdir) / "rights-store.json"
            access_path = Path(tmpdir) / "access-log.json"

            rights_store = {
                "updated_at": "2026-03-30T20:40:00Z",
                "requests": [
                    {
                        "request_id": "rights_export_old",
                        "parcel_id": "parcel_001",
                        "account_id": "acct_123",
                        "request_type": "export",
                        "status": "completed",
                        "created_at": "2026-01-01T00:00:00Z",
                        "scope": ["private_parcel_data"],
                        "requested_from_surface": "parcel_settings_ui",
                    },
                    {
                        "request_id": "rights_delete_old",
                        "parcel_id": "parcel_001",
                        "account_id": "acct_123",
                        "request_type": "delete",
                        "status": "completed",
                        "created_at": "2026-01-01T00:00:00Z",
                        "scope": ["private_parcel_data"],
                        "requested_from_surface": "parcel_settings_ui",
                    },
                ],
            }
            access_log = [
                {
                    "event_id": "access_old",
                    "occurred_at": "2026-01-01T00:00:00Z",
                    "actor": "parcel-platform-api",
                    "action": "view_parcel_state",
                    "parcel_id": "parcel_001",
                    "data_classes": ["private_parcel_data"],
                    "justification": "parcel_view_request",
                }
            ]
            rights_path.write_text(json.dumps(rights_store), encoding="utf-8")
            access_path.write_text(json.dumps(access_log), encoding="utf-8")

            report = run_retention_cleanup.run_cleanup(
                rights_store_path=rights_path,
                access_log_path=access_path,
                retention_days=30,
            )

            self.assertEqual(report["access_events_removed"], 1)
            self.assertEqual(report["rights_requests_removed"], 1)

            updated_rights = json.loads(rights_path.read_text(encoding="utf-8"))
            remaining_ids = [item["request_id"] for item in updated_rights["requests"]]
            self.assertNotIn("rights_export_old", remaining_ids)
            self.assertIn("rights_delete_old", remaining_ids)

            updated_access = json.loads(access_path.read_text(encoding="utf-8"))
            self.assertEqual(updated_access, [])

    def test_access_log_appends_are_safe_under_concurrency(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            access_path = Path(tmpdir) / "access-log.json"
            access_path.write_text("[]", encoding="utf-8")
            barrier = threading.Barrier(12)
            errors = []

            def worker(index: int):
                try:
                    barrier.wait(timeout=5)
                    serve_parcel_api.append_access_event(
                        access_path,
                        actor="parcel-platform-api",
                        action="view_parcel_state",
                        parcel_id=f"parcel_{index}",
                        data_classes=["private_parcel_data"],
                        justification="parcel_view_request",
                    )
                except Exception as exc:  # pragma: no cover - assertion below captures failures
                    errors.append(exc)

            threads = [threading.Thread(target=worker, args=(index,)) for index in range(12)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

            self.assertEqual(errors, [])
            access_events = json.loads(access_path.read_text(encoding="utf-8"))
            self.assertEqual(len(access_events), 12)
            self.assertEqual(
                {event["parcel_id"] for event in access_events},
                {f"parcel_{index}" for index in range(12)},
            )

    def test_export_paths_are_confined_to_allowed_roots(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            export_dir = Path(tmpdir) / "exports"
            allowed_input_root = Path(tmpdir) / "allowed-inputs"
            export_dir.mkdir()
            allowed_input_root.mkdir()
            parcel_state_path = allowed_input_root / "parcel-state.json"
            parcel_state_path.write_text("{}", encoding="utf-8")

            safe_output = serve_parcel_api.resolve_export_output_path(export_dir, "nested/bundle.json")
            self.assertEqual(safe_output, (export_dir / "nested" / "bundle.json").resolve())

            safe_input = serve_parcel_api.resolve_allowed_input_path(
                str(parcel_state_path),
                allowed_roots=[allowed_input_root],
                label="parcel_state_path",
            )
            self.assertEqual(safe_input, parcel_state_path.resolve())

            with self.assertRaises(serve_parcel_api.ParcelViewError):
                serve_parcel_api.resolve_export_output_path(export_dir, "../escaped.json")

            with self.assertRaises(serve_parcel_api.ParcelViewError):
                serve_parcel_api.resolve_allowed_input_path(
                    str(Path(tmpdir) / "outside.json"),
                    allowed_roots=[allowed_input_root],
                    label="parcel_state_path",
                )

    def test_normalize_packet_ignores_missing_sensor_derived_defaults(self):
        payload = {
            "schema_version": "oesis.bench-air.v1",
            "node_id": "bench-air-01",
            "observed_at": "2026-03-30T19:45:00Z",
            "firmware_version": "0.1.0",
            "location_mode": "indoor",
            "sensors": {
                "sht45": {
                    "present": False,
                    "temperature_c": 0.0,
                    "relative_humidity_pct": 0.0,
                },
                "bme680": {
                    "present": False,
                    "temperature_c": 0.0,
                    "relative_humidity_pct": 0.0,
                    "pressure_hpa": 0.0,
                    "gas_resistance_ohm": 1.0,
                },
            },
            "derived": {
                "temperature_c_primary": 0.0,
                "relative_humidity_pct_primary": 0.0,
                "pressure_hpa": 0.0,
                "voc_trend_source": "gas_resistance_ohm",
            },
            "health": {
                "uptime_s": 1,
                "wifi_connected": True,
                "free_heap_bytes": 1,
                "read_failures_total": 2,
                "last_error": "sensor_missing",
            },
        }

        normalized = normalize_packet.normalize_packet(payload, parcel_id="parcel_demo_001")
        self.assertEqual(normalized["values"], {})

    def test_combine_public_contexts_rejects_mixed_parcels(self):
        weather_context = json.loads((DOC_EXAMPLES / "public-context.example.json").read_text(encoding="utf-8"))
        smoke_context = json.loads((DOC_EXAMPLES / "public-context.example.json").read_text(encoding="utf-8"))
        smoke_context["context_id"] = "pubctx_other"
        smoke_context["parcel_id"] = "parcel_other"
        smoke_context["source_name"] = "demo_other_source"

        with self.assertRaises(infer_parcel_state.InferenceError):
            infer_parcel_state.combine_public_contexts([weather_context, smoke_context])

    def test_weather_pm_mast_does_not_claim_live_pm_values_without_sensor_reads(self):
        firmware_source = WEATHER_PM_MAST_FIRMWARE.read_text(encoding="utf-8")
        self.assertIn('\\"sps30\\":{\\"present\\":false}', firmware_source)
        self.assertNotIn("pm1_ugm3", firmware_source)


if __name__ == "__main__":
    unittest.main()
