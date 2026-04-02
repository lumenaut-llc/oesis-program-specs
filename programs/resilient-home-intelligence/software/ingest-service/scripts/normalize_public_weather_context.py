#!/usr/bin/env python3

import sys as _sys
from pathlib import Path as _Path

_SOFTWARE_ROOT = _Path(__file__).resolve().parents[2]
if str(_SOFTWARE_ROOT) not in _sys.path:
    _sys.path.insert(0, str(_SOFTWARE_ROOT))

from _script_wrapper import export_canonical_module as _export_canonical_module
from _script_wrapper import run_canonical_main as _run_canonical_main

_CANONICAL_MODULE = "rhi.ingest.normalize_public_weather_context"
_export_canonical_module(_CANONICAL_MODULE, globals())

if __name__ == "__main__":
    raise SystemExit(_run_canonical_main(_CANONICAL_MODULE))
