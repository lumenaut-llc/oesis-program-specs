import json
import threading
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from rhi.common.atomic_io import atomic_write_json as _atomic_write_json
from rhi.common.atomic_io import atomic_write_text as _atomic_write_text
from rhi.common.repo_paths import DOCS_EXAMPLES_DIR

from .format_parcel_view import ParcelViewError
from .summarize_reference_state import load_optional_json as load_optional_reference_json
from .summarize_reference_state import summarize as summarize_reference_state

EXAMPLES_DIR = DOCS_EXAMPLES_DIR
DEFAULT_SHARING = json.loads((EXAMPLES_DIR / "sharing-settings.example.json").read_text(encoding="utf-8"))
DEFAULT_RIGHTS_REQUEST = json.loads((EXAMPLES_DIR / "rights-request.example.json").read_text(encoding="utf-8"))
DEFAULT_SHARING_STORE = json.loads((EXAMPLES_DIR / "sharing-store.example.json").read_text(encoding="utf-8"))
DEFAULT_RIGHTS_REQUEST_STORE = json.loads((EXAMPLES_DIR / "rights-request-store.example.json").read_text(encoding="utf-8"))
DEFAULT_EXPORT_BUNDLE = json.loads((EXAMPLES_DIR / "export-bundle.example.json").read_text(encoding="utf-8"))

_STORE_LOCKS: dict[Path, threading.RLock] = {}
_STORE_LOCKS_GUARD = threading.Lock()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _store_lock(path: Path) -> threading.RLock:
    resolved = path.resolve()
    with _STORE_LOCKS_GUARD:
        lock = _STORE_LOCKS.get(resolved)
        if lock is None:
            lock = threading.RLock()
            _STORE_LOCKS[resolved] = lock
        return lock


def _read_json_unlocked(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json_store_unlocked(path: Path, default_payload):
    if path.exists():
        return _read_json_unlocked(path)
    payload = deepcopy(default_payload)
    _atomic_write_json(path, payload)
    return payload


def _save_json_store_unlocked(path: Path, payload, *, touch_updated_at: bool):
    stored = deepcopy(payload)
    if touch_updated_at:
        stored["updated_at"] = now_iso()
    _atomic_write_json(path, stored)
    return stored


def _load_access_log_unlocked(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return _read_json_unlocked(path)


def _save_access_log_unlocked(path: Path, payload: list[dict]):
    _atomic_write_json(path, payload)


def ensure_path_within_allowed_roots(path: Path, *, allowed_roots: list[Path], label: str) -> Path:
    resolved = path.resolve()
    for root in allowed_roots:
        try:
            resolved.relative_to(root.resolve())
            return resolved
        except ValueError:
            continue
    allowed = ", ".join(str(root.resolve()) for root in allowed_roots)
    raise ParcelViewError(f"{label} must stay within one of: {allowed}")


def resolve_export_output_path(export_dir: Path, output_name: str) -> Path:
    export_root = export_dir.resolve()
    return ensure_path_within_allowed_roots(
        export_root / output_name,
        allowed_roots=[export_root],
        label="output_name",
    )


def resolve_allowed_input_path(raw_path: str, *, allowed_roots: list[Path], label: str) -> Path:
    return ensure_path_within_allowed_roots(
        Path(raw_path),
        allowed_roots=allowed_roots,
        label=label,
    )


def clone_default_sharing(parcel_id: str) -> dict:
    payload = deepcopy(DEFAULT_SHARING)
    payload["parcel_id"] = parcel_id
    payload["updated_at"] = now_iso()
    return payload


def parcel_ref_for_id(parcel_id: str) -> str:
    return f"parcel_ref_{parcel_id}"


def rights_request_id(parcel_id: str, request_type: str) -> str:
    return f"rights_{request_type}_{parcel_id}_{uuid4().hex[:12]}"


def build_rights_request(parcel_id: str, request_type: str) -> dict:
    payload = deepcopy(DEFAULT_RIGHTS_REQUEST)
    payload["request_id"] = rights_request_id(parcel_id, request_type)
    payload["parcel_id"] = parcel_id
    payload["request_type"] = request_type
    payload["created_at"] = now_iso()
    payload["status"] = "submitted"
    return payload


def load_access_log(path: Path) -> list[dict]:
    resolved = path.resolve()
    with _store_lock(resolved):
        return deepcopy(_load_access_log_unlocked(resolved))


def load_sharing_store(path: Path) -> dict:
    resolved = path.resolve()
    with _store_lock(resolved):
        return deepcopy(_load_json_store_unlocked(resolved, DEFAULT_SHARING_STORE))


def save_sharing_store(path: Path, payload: dict):
    resolved = path.resolve()
    with _store_lock(resolved):
        _save_json_store_unlocked(resolved, payload, touch_updated_at=True)


def load_rights_store(path: Path) -> dict:
    resolved = path.resolve()
    with _store_lock(resolved):
        return deepcopy(_load_json_store_unlocked(resolved, DEFAULT_RIGHTS_REQUEST_STORE))


def save_rights_store(path: Path, payload: dict):
    resolved = path.resolve()
    with _store_lock(resolved):
        _save_json_store_unlocked(resolved, payload, touch_updated_at=True)


def append_rights_request(path: Path, request: dict):
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_RIGHTS_REQUEST_STORE)
        for existing in store["requests"]:
            if existing["request_id"] == request["request_id"]:
                raise KeyError(f"rights request already exists: {request['request_id']}")
        store["requests"].append(deepcopy(request))
        _save_json_store_unlocked(resolved, store, touch_updated_at=True)


def list_rights_requests(path: Path, parcel_id: str) -> list[dict]:
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_RIGHTS_REQUEST_STORE)
        return [deepcopy(item) for item in store["requests"] if item["parcel_id"] == parcel_id]


def find_rights_request(store: dict, request_id: str, *, request_type: str | None = None) -> dict:
    for request in store["requests"]:
        if request["request_id"] != request_id:
            continue
        if request_type is not None and request["request_type"] != request_type:
            raise KeyError(f"rights request is not a {request_type} request: {request_id}")
        return request
    raise KeyError(f"rights request not found: {request_id}")


def update_rights_request_status(path: Path, request_id: str, status: str) -> dict:
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_RIGHTS_REQUEST_STORE)
        request = find_rights_request(store, request_id)
        request["status"] = status
        _save_json_store_unlocked(resolved, store, touch_updated_at=True)
        return deepcopy(request)


def remove_parcel_from_sharing_store(path: Path, parcel_id: str):
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_SHARING_STORE)
        store["parcels"] = [entry for entry in store["parcels"] if entry["parcel_id"] != parcel_id]
        _save_json_store_unlocked(resolved, store, touch_updated_at=True)


def process_delete_request(rights_store_path: Path, sharing_store_path: Path, request_id: str) -> dict:
    rights_path = rights_store_path.resolve()
    sharing_path = sharing_store_path.resolve()
    with _store_lock(rights_path):
        store = _load_json_store_unlocked(rights_path, DEFAULT_RIGHTS_REQUEST_STORE)
        request = find_rights_request(store, request_id, request_type="delete")
        updated_store = deepcopy(store)
        updated_request = find_rights_request(updated_store, request_id)
        updated_request["status"] = "completed"

        with _store_lock(sharing_path):
            sharing_store = _load_json_store_unlocked(sharing_path, DEFAULT_SHARING_STORE)
            updated_sharing_store = deepcopy(sharing_store)
            updated_sharing_store["parcels"] = [
                entry for entry in updated_sharing_store["parcels"] if entry["parcel_id"] != request["parcel_id"]
            ]
            _save_json_store_unlocked(sharing_path, updated_sharing_store, touch_updated_at=True)
            try:
                _save_json_store_unlocked(rights_path, updated_store, touch_updated_at=True)
            except Exception:
                _atomic_write_json(sharing_path, sharing_store)
                raise
        return deepcopy(updated_request)


def export_bundle_for_parcel(
    parcel_id: str,
    sharing_store_path: Path,
    rights_store_path: Path,
    access_log_path: Path,
    parcel_state_path: Path | None = None,
    *,
    sharing_store: dict | None = None,
    rights_store: dict | None = None,
    access_log: list[dict] | None = None,
) -> dict:
    sharing = None
    sharing_store = deepcopy(sharing_store) if sharing_store is not None else load_sharing_store(sharing_store_path)
    for entry in sharing_store["parcels"]:
        if entry["parcel_id"] == parcel_id:
            sharing = deepcopy(entry["sharing"])
            break

    if rights_store is None:
        rights_requests = list_rights_requests(rights_store_path, parcel_id)
    else:
        rights_requests = [deepcopy(item) for item in rights_store["requests"] if item["parcel_id"] == parcel_id]

    if access_log is None:
        access_events = [deepcopy(event) for event in load_access_log(access_log_path) if event["parcel_id"] == parcel_id]
    else:
        access_events = [deepcopy(event) for event in access_log if event["parcel_id"] == parcel_id]

    parcel_state = None
    if parcel_state_path and parcel_state_path.exists():
        payload = json.loads(parcel_state_path.read_text(encoding="utf-8"))
        if payload.get("parcel_id") == parcel_id:
            parcel_state = payload
    if parcel_state is None:
        payload = deepcopy(DEFAULT_EXPORT_BUNDLE["parcel_state"])
        if payload.get("parcel_id") == parcel_id:
            parcel_state = payload

    return {
        "generated_at": now_iso(),
        "parcel_id": parcel_id,
        "sharing": sharing,
        "rights_requests": rights_requests,
        "access_events": access_events,
        "parcel_state": parcel_state,
    }


def process_export_request(
    rights_store_path: Path,
    sharing_store_path: Path,
    access_log_path: Path,
    request_id: str,
    output_path: Path,
    parcel_state_path: Path | None = None,
) -> dict:
    rights_path = rights_store_path.resolve()
    with _store_lock(rights_path):
        store = _load_json_store_unlocked(rights_path, DEFAULT_RIGHTS_REQUEST_STORE)
        request = find_rights_request(store, request_id, request_type="export")
        updated_store = deepcopy(store)
        updated_request = find_rights_request(updated_store, request_id)
        updated_request["status"] = "completed"

        bundle = export_bundle_for_parcel(
            request["parcel_id"],
            sharing_store_path,
            rights_store_path,
            access_log_path,
            parcel_state_path=parcel_state_path,
            rights_store=updated_store,
        )
        output_path = output_path.resolve()
        previous_output = output_path.read_text(encoding="utf-8") if output_path.exists() else None
        _atomic_write_json(output_path, bundle)
        try:
            _save_json_store_unlocked(rights_path, updated_store, touch_updated_at=True)
        except Exception:
            if previous_output is None:
                try:
                    output_path.unlink()
                except FileNotFoundError:
                    pass
            else:
                _atomic_write_text(output_path, previous_output)
            raise
        return deepcopy(updated_request)


def build_reference_state_summary(sharing_store_path: Path, rights_store_path: Path, access_log_path: Path) -> dict:
    sharing_store = load_optional_reference_json(sharing_store_path, {"updated_at": None, "parcels": []})
    rights_store = load_optional_reference_json(rights_store_path, {"updated_at": None, "requests": []})
    access_log = load_optional_reference_json(access_log_path, [])
    return summarize_reference_state(sharing_store, rights_store, access_log)


def append_access_event(path: Path, *, actor: str, action: str, parcel_id: str, data_classes: list[str], justification: str):
    resolved = path.resolve()
    with _store_lock(resolved):
        payload = _load_access_log_unlocked(resolved)
        payload.append(
            {
                "event_id": f"access_{action}_{parcel_id}_{len(payload)+1}",
                "occurred_at": now_iso(),
                "actor": actor,
                "action": action,
                "parcel_id": parcel_id,
                "data_classes": data_classes,
                "justification": justification,
            }
        )
        _save_access_log_unlocked(resolved, payload)


def sharing_from_store(path: Path, parcel_id: str) -> dict:
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_SHARING_STORE)
        for entry in store["parcels"]:
            if entry["parcel_id"] == parcel_id:
                return deepcopy(entry["sharing"])
        return clone_default_sharing(parcel_id)


def update_sharing_store(path: Path, parcel_id: str, sharing: dict):
    resolved = path.resolve()
    with _store_lock(resolved):
        store = _load_json_store_unlocked(resolved, DEFAULT_SHARING_STORE)
        for entry in store["parcels"]:
            if entry["parcel_id"] == parcel_id:
                entry["sharing"] = deepcopy(sharing)
                entry["parcel_ref"] = entry.get("parcel_ref") or parcel_ref_for_id(parcel_id)
                _save_json_store_unlocked(resolved, store, touch_updated_at=True)
                return
        store["parcels"].append(
            {
                "parcel_id": parcel_id,
                "parcel_ref": parcel_ref_for_id(parcel_id),
                "sharing": deepcopy(sharing),
            }
        )
        _save_json_store_unlocked(resolved, store, touch_updated_at=True)


__all__ = [
    "append_access_event",
    "append_rights_request",
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
    "now_iso",
    "parcel_ref_for_id",
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
]
