#!/usr/bin/env python3

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from rhi.common.repo_paths import REPO_ROOT

from .format_evidence_summary import build_evidence_summary
from .format_parcel_view import ParcelViewError, build_parcel_view, validate_sharing_settings
from .reference_store import append_access_event
from .reference_store import append_intervention_event
from .reference_store import append_rights_request
from .reference_store import append_verification_outcome
from .reference_store import build_reference_state_summary
from .reference_store import build_rights_request
from .reference_store import clone_default_sharing
from .reference_store import ensure_path_within_allowed_roots
from .reference_store import export_bundle_for_parcel
from .reference_store import find_rights_request
from .reference_store import list_intervention_events
from .reference_store import list_verification_outcomes
from .reference_store import load_control_compatibility
from .reference_store import load_house_capability
from .reference_store import load_house_state
from .reference_store import list_rights_requests
from .reference_store import load_access_log
from .reference_store import load_rights_store
from .reference_store import load_sharing_store
from .reference_store import now_iso
from .reference_store import parcel_ref_for_id
from .reference_store import process_delete_request
from .reference_store import process_export_request
from .reference_store import remove_parcel_from_sharing_store
from .reference_store import resolve_allowed_input_path
from .reference_store import resolve_export_output_path
from .reference_store import rights_request_id
from .reference_store import save_rights_store
from .reference_store import save_sharing_store
from .reference_store import sharing_from_store
from .reference_store import upsert_control_compatibility
from .reference_store import upsert_house_capability
from .reference_store import upsert_house_state
from .reference_store import update_rights_request_status
from .reference_store import update_sharing_store
from .run_retention_cleanup import run_cleanup
from .support_objects import SupportObjectError
from .support_objects import prepare_intervention_event
from .support_objects import prepare_verification_outcome
from .support_objects import validate_control_compatibility
from .support_objects import validate_house_capability
from .support_objects import validate_house_state
from .support_objects import validate_intervention_event
from .support_objects import validate_verification_outcome

__all__ = [
    "ParcelPlatformRequestHandler",
    "ParcelViewError",
    "append_access_event",
    "append_intervention_event",
    "append_rights_request",
    "append_verification_outcome",
    "build_evidence_summary",
    "build_parcel_view",
    "build_reference_state_summary",
    "build_rights_request",
    "clone_default_sharing",
    "ensure_path_within_allowed_roots",
    "export_bundle_for_parcel",
    "find_rights_request",
    "list_intervention_events",
    "list_verification_outcomes",
    "load_control_compatibility",
    "load_house_capability",
    "load_house_state",
    "list_rights_requests",
    "load_access_log",
    "load_rights_store",
    "load_sharing_store",
    "main",
    "now_iso",
    "parcel_ref_for_id",
    "parse_args",
    "process_delete_request",
    "process_export_request",
    "remove_parcel_from_sharing_store",
    "resolve_allowed_input_path",
    "resolve_export_output_path",
    "rights_request_id",
    "save_rights_store",
    "save_sharing_store",
    "sharing_from_store",
    "upsert_control_compatibility",
    "upsert_house_capability",
    "upsert_house_state",
    "update_rights_request_status",
    "update_sharing_store",
    "validate_sharing_settings",
]


class ParcelPlatformRequestHandler(BaseHTTPRequestHandler):
    server_version = "RHIParcelPlatform/0.1"
    sharing_store_path = None
    rights_store_path = None
    access_log_path = None
    export_dir_path = None
    house_state_store_path = None
    house_capability_store_path = None
    control_compatibility_store_path = None
    intervention_event_store_path = None
    verification_outcome_store_path = None
    allowed_input_roots = []

    def _send_json(self, status: int, payload: dict):
        body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(content_length)
        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise ParcelViewError(f"request body: invalid JSON: {exc}") from exc

    def _path_parts(self):
        return [part for part in self.path.split("/") if part]

    def _sharing_for_parcel(self, parcel_id: str) -> dict:
        return sharing_from_store(self.sharing_store_path, parcel_id)

    def _support_object_response(self, *, parcel_id: str, response_key: str, payload, action: str):
        append_access_event(
            self.access_log_path,
            actor="parcel-platform-api",
            action=action,
            parcel_id=parcel_id,
            data_classes=["private_parcel_data"],
            justification=f"{response_key}_request",
        )
        self._send_json(
            HTTPStatus.OK,
            {
                "ok": True,
                response_key: payload,
            },
        )

    def do_GET(self):
        if self.path == "/v1/parcel-platform/health":
            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "service": "parcel-platform",
                },
            )
            return

        if self.path == "/v1/admin/reference-state/summary":
            try:
                summary = build_reference_state_summary(
                    self.sharing_store_path,
                    self.rights_store_path,
                    self.access_log_path,
                )
            except (OSError, json.JSONDecodeError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    {
                        "ok": False,
                        "error": "reference_state_unavailable",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "summary": summary,
                },
            )
            return

        parts = self._path_parts()
        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "sharing":
            parcel_id = parts[2]
            append_access_event(
                self.access_log_path,
                actor="parcel-platform-api",
                action="view_sharing_settings",
                parcel_id=parcel_id,
                data_classes=["administrative_record"],
                justification="sharing_settings_request",
            )
            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "sharing": self._sharing_for_parcel(parcel_id),
                },
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "rights":
            parcel_id = parts[2]
            append_access_event(
                self.access_log_path,
                actor="parcel-platform-api",
                action="list_rights_requests",
                parcel_id=parcel_id,
                data_classes=["administrative_record"],
                justification="rights_request_status_view",
            )
            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "rights_requests": list_rights_requests(self.rights_store_path, parcel_id),
                },
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "house-state":
            parcel_id = parts[2]
            self._support_object_response(
                parcel_id=parcel_id,
                response_key="house_state",
                payload=load_house_state(self.house_state_store_path, parcel_id),
                action="view_house_state",
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "capabilities":
            parcel_id = parts[2]
            self._support_object_response(
                parcel_id=parcel_id,
                response_key="house_capability",
                payload=load_house_capability(self.house_capability_store_path, parcel_id),
                action="view_house_capability",
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "controls":
            parcel_id = parts[2]
            self._support_object_response(
                parcel_id=parcel_id,
                response_key="control_compatibility",
                payload=load_control_compatibility(self.control_compatibility_store_path, parcel_id),
                action="view_control_compatibility",
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "interventions":
            parcel_id = parts[2]
            self._support_object_response(
                parcel_id=parcel_id,
                response_key="interventions",
                payload=list_intervention_events(self.intervention_event_store_path, parcel_id),
                action="list_intervention_events",
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "verification":
            parcel_id = parts[2]
            self._support_object_response(
                parcel_id=parcel_id,
                response_key="verification_outcomes",
                payload=list_verification_outcomes(self.verification_outcome_store_path, parcel_id),
                action="list_verification_outcomes",
            )
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self):
        if self.path == "/v1/parcels/state/view":
            try:
                payload = self._read_json()
                parcel_id = payload["parcel_id"]
                sharing_settings = self._sharing_for_parcel(parcel_id)
                parcel_view = build_parcel_view(payload, sharing_settings)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="view_parcel_state",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data", "derived_parcel_state"],
                    justification="parcel_view_request",
                )
            except (ParcelViewError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_parcel_state",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "parcel_view": parcel_view,
                },
            )
            return

        if self.path == "/v1/parcels/state/evidence-summary":
            try:
                payload = self._read_json()
                parcel_id = payload["parcel_id"]
                evidence_summary = build_evidence_summary(payload)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="view_evidence_summary",
                    parcel_id=parcel_id,
                    data_classes=["derived_parcel_state"],
                    justification="evidence_summary_request",
                )
            except (ParcelViewError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_parcel_state",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "evidence_summary": evidence_summary,
                },
            )
            return

        parts = self._path_parts()
        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "sharing":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                payload["parcel_id"] = parcel_id
                payload["updated_at"] = now_iso()
                validate_sharing_settings(payload)
                update_sharing_store(self.sharing_store_path, parcel_id, payload)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="update_sharing_settings",
                    parcel_id=parcel_id,
                    data_classes=["administrative_record"],
                    justification="sharing_settings_update",
                )
            except (ParcelViewError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_sharing_settings",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "sharing": self._sharing_for_parcel(parcel_id),
                },
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "house-state":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                payload["parcel_id"] = parcel_id
                payload["updated_at"] = now_iso()
                payload.setdefault("observed_at", payload["updated_at"])
                validate_house_state(payload)
                upsert_house_state(self.house_state_store_path, payload)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="update_house_state",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data"],
                    justification="house_state_update",
                )
            except (SupportObjectError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_house_state",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(HTTPStatus.OK, {"ok": True, "house_state": load_house_state(self.house_state_store_path, parcel_id)})
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "capabilities":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                payload["parcel_id"] = parcel_id
                payload["updated_at"] = now_iso()
                validate_house_capability(payload)
                upsert_house_capability(self.house_capability_store_path, payload)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="update_house_capability",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data"],
                    justification="house_capability_update",
                )
            except (SupportObjectError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_house_capability",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {"ok": True, "house_capability": load_house_capability(self.house_capability_store_path, parcel_id)},
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "controls":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                payload["parcel_id"] = parcel_id
                payload["updated_at"] = now_iso()
                validate_control_compatibility(payload)
                upsert_control_compatibility(self.control_compatibility_store_path, payload)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="update_control_compatibility",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data"],
                    justification="control_compatibility_update",
                )
            except (SupportObjectError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_control_compatibility",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "control_compatibility": load_control_compatibility(self.control_compatibility_store_path, parcel_id),
                },
            )
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "interventions":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                prepared = prepare_intervention_event(payload, parcel_id=parcel_id, now_iso=now_iso())
                validate_intervention_event(prepared)
                stored = append_intervention_event(self.intervention_event_store_path, prepared)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="record_intervention_event",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data"],
                    justification="intervention_event_append",
                )
            except (SupportObjectError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_intervention_event",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(HTTPStatus.CREATED, {"ok": True, "intervention_event": stored})
            return

        if len(parts) == 4 and parts[:2] == ["v1", "parcels"] and parts[3] == "verification":
            parcel_id = parts[2]
            try:
                payload = self._read_json()
                prepared = prepare_verification_outcome(payload, parcel_id=parcel_id, now_iso=now_iso())
                validate_verification_outcome(prepared)
                stored = append_verification_outcome(self.verification_outcome_store_path, prepared)
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="record_verification_outcome",
                    parcel_id=parcel_id,
                    data_classes=["private_parcel_data"],
                    justification="verification_outcome_append",
                )
            except (SupportObjectError, KeyError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_verification_outcome",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(HTTPStatus.CREATED, {"ok": True, "verification_outcome": stored})
            return

        if len(parts) == 5 and parts[:2] == ["v1", "parcels"] and parts[3] == "rights" and parts[4] in {"export", "delete"}:
            parcel_id = parts[2]
            request_type = parts[4]
            rights_request = build_rights_request(parcel_id, request_type)
            append_rights_request(self.rights_store_path, rights_request)
            append_access_event(
                self.access_log_path,
                actor="parcel-platform-api",
                action=f"create_{request_type}_request",
                parcel_id=parcel_id,
                data_classes=["administrative_record"],
                justification="rights_request_submission",
            )
            self._send_json(
                HTTPStatus.ACCEPTED,
                {
                    "ok": True,
                    "rights_request": rights_request,
                },
            )
            return

        if self.path == "/v1/admin/rights/process-delete":
            try:
                payload = self._read_json()
                request_id = payload["request_id"]
                result = process_delete_request(
                    self.rights_store_path,
                    self.sharing_store_path,
                    request_id,
                    house_state_store_path=self.house_state_store_path,
                    house_capability_store_path=self.house_capability_store_path,
                    control_compatibility_store_path=self.control_compatibility_store_path,
                    intervention_event_store_path=self.intervention_event_store_path,
                    verification_outcome_store_path=self.verification_outcome_store_path,
                )
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="process_delete_request",
                    parcel_id=result["parcel_id"],
                    data_classes=["administrative_record"],
                    justification="delete_request_execution",
                )
            except (ParcelViewError, KeyError, OSError, json.JSONDecodeError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_delete_request",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "rights_request": result,
                },
            )
            return

        if self.path == "/v1/admin/rights/process-export":
            try:
                payload = self._read_json()
                request_id = payload["request_id"]
                output_name = payload.get("output_name", f"{request_id}.json")
                output_path = resolve_export_output_path(self.export_dir_path, output_name)
                parcel_state_path = None
                if payload.get("parcel_state_path"):
                    allowed_roots = [*self.allowed_input_roots, self.export_dir_path]
                    parcel_state_path = resolve_allowed_input_path(
                        payload["parcel_state_path"],
                        allowed_roots=allowed_roots,
                        label="parcel_state_path",
                    )
                result = process_export_request(
                    self.rights_store_path,
                    self.sharing_store_path,
                    self.access_log_path,
                    request_id,
                    output_path,
                    parcel_state_path=parcel_state_path,
                    house_state_store_path=self.house_state_store_path,
                    house_capability_store_path=self.house_capability_store_path,
                    control_compatibility_store_path=self.control_compatibility_store_path,
                    intervention_event_store_path=self.intervention_event_store_path,
                    verification_outcome_store_path=self.verification_outcome_store_path,
                )
                append_access_event(
                    self.access_log_path,
                    actor="parcel-platform-api",
                    action="process_export_request",
                    parcel_id=result["parcel_id"],
                    data_classes=["administrative_record"],
                    justification="export_request_execution",
                )
            except (ParcelViewError, KeyError, OSError, json.JSONDecodeError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_export_request",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "rights_request": result,
                    "output_path": str(output_path),
                },
            )
            return

        if self.path == "/v1/admin/retention/cleanup":
            try:
                payload = self._read_json()
                retention_days = int(payload.get("retention_days", 30))
                report = run_cleanup(
                    rights_store_path=self.rights_store_path,
                    access_log_path=self.access_log_path,
                    retention_days=retention_days,
                )
            except (ParcelViewError, KeyError, OSError, ValueError, json.JSONDecodeError) as exc:
                self._send_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "ok": False,
                        "error": "invalid_retention_cleanup_request",
                        "detail": str(exc),
                    },
                )
                return

            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "cleanup_report": report,
                },
            )
            return
        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def log_message(self, format, *args):
        return


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a tiny local parcel-platform API for parcel-state formatting.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind.")
    parser.add_argument("--port", type=int, default=8789, help="Port to listen on.")
    parser.add_argument(
        "--sharing-store",
        default="/tmp/rhi-sharing-store.json",
        help="Path to a JSON sharing store file used across reference services.",
    )
    parser.add_argument(
        "--rights-store",
        default="/tmp/rhi-rights-request-store.json",
        help="Path to a JSON rights-request store file.",
    )
    parser.add_argument(
        "--access-log",
        default="/tmp/rhi-operator-access-log.json",
        help="Path to a JSON operator access log file.",
    )
    parser.add_argument(
        "--export-dir",
        default="/tmp/rhi-parcel-exports",
        help="Directory for reference export bundles written by admin export processing endpoints.",
    )
    parser.add_argument("--house-state-store", default="/tmp/rhi-house-state-store.json", help="Path to the JSON house-state store file.")
    parser.add_argument(
        "--house-capability-store",
        default="/tmp/rhi-house-capability-store.json",
        help="Path to the JSON house-capability store file.",
    )
    parser.add_argument(
        "--control-compatibility-store",
        default="/tmp/rhi-control-compatibility-store.json",
        help="Path to the JSON control-compatibility store file.",
    )
    parser.add_argument(
        "--intervention-event-store",
        default="/tmp/rhi-intervention-event-store.json",
        help="Path to the JSON intervention-event store file.",
    )
    parser.add_argument(
        "--verification-outcome-store",
        default="/tmp/rhi-verification-outcome-store.json",
        help="Path to the JSON verification-outcome store file.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    ParcelPlatformRequestHandler.sharing_store_path = Path(args.sharing_store).resolve()
    ParcelPlatformRequestHandler.rights_store_path = Path(args.rights_store).resolve()
    ParcelPlatformRequestHandler.access_log_path = Path(args.access_log).resolve()
    ParcelPlatformRequestHandler.export_dir_path = Path(args.export_dir).resolve()
    ParcelPlatformRequestHandler.house_state_store_path = Path(args.house_state_store).resolve()
    ParcelPlatformRequestHandler.house_capability_store_path = Path(args.house_capability_store).resolve()
    ParcelPlatformRequestHandler.control_compatibility_store_path = Path(args.control_compatibility_store).resolve()
    ParcelPlatformRequestHandler.intervention_event_store_path = Path(args.intervention_event_store).resolve()
    ParcelPlatformRequestHandler.verification_outcome_store_path = Path(args.verification_outcome_store).resolve()
    ParcelPlatformRequestHandler.allowed_input_roots = [REPO_ROOT.resolve()]
    ParcelPlatformRequestHandler.export_dir_path.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((args.host, args.port), ParcelPlatformRequestHandler)
    print(f"Listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
