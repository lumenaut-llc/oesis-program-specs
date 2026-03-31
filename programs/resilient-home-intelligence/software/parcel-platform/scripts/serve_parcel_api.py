#!/usr/bin/env python3

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from format_parcel_view import ParcelViewError, build_parcel_view


class ParcelPlatformRequestHandler(BaseHTTPRequestHandler):
    server_version = "RHIParcelPlatform/0.1"

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

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self):
        if self.path != "/v1/parcels/state/view":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
            return

        try:
            payload = self._read_json()
            parcel_view = build_parcel_view(payload)
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

    def log_message(self, format, *args):
        return


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a tiny local parcel-platform API for parcel-state formatting.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind.")
    parser.add_argument("--port", type=int, default=8789, help="Port to listen on.")
    return parser.parse_args()


def main():
    args = parse_args()
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
