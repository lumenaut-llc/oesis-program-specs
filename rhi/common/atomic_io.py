import json
import os
import tempfile
from pathlib import Path


def atomic_write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(
        dir=str(path.parent),
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def atomic_write_json(path: Path, payload):
    atomic_write_text(path, json.dumps(payload, indent=2, sort_keys=True))


def read_optional_text(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def restore_previous_text(path: Path, previous_content: str | None):
    if previous_content is None:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        return
    atomic_write_text(path, previous_content)
