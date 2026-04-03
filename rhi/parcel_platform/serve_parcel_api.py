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
from .reference_store import append_rights_request
from .reference_store import build_reference_state_summary
from .reference_store import build_rights_request
from .reference_store import clone_default_sharing
from .reference_store import ensure_path_within_allowed_roots
from .reference_store import export_bundle_for_parcel
from .reference_store import find_rights_request
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
from .reference_store import update_rights_request_status
from .reference_store import update_sharing_store
from .run_retention_cleanup import run_cleanup

__all__ = [
    "ParcelPlatformRequestHandler",
    "ParcelViewError",
    "append_access_event",
    "append_rights_request",
    "build_evidence_summary",
    "build_parcel_view",
    "build_reference_state_summary",
    "build_rights_request",
    "clone_default_sharing",
    "ensure_path_within_allowed_roots",
    "export_bundle_for_parcel",
    "find_rights_request",
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
    return parser.parse_args()


def main():
    args = parse_args()
    ParcelPlatformRequestHandler.sharing_store_path = Path(args.sharing_store).resolve()
    ParcelPlatformRequestHandler.rights_store_path = Path(args.rights_store).resolve()
    ParcelPlatformRequestHandler.access_log_path = Path(args.access_log).resolve()
    ParcelPlatformRequestHandler.export_dir_path = Path(args.export_dir).resolve()
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
