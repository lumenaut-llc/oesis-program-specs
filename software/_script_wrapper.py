#!/usr/bin/env python3

import importlib
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def ensure_repo_root_on_sys_path():
    repo_root = str(REPO_ROOT)
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)


def load_canonical_module(module_name: str):
    ensure_repo_root_on_sys_path()
    return importlib.import_module(module_name)


def export_canonical_module(module_name: str, namespace: dict):
    module = load_canonical_module(module_name)
    public_names = getattr(module, "__all__", None)
    if public_names is None:
        public_names = [name for name in vars(module) if not name.startswith("_")]
    for name in public_names:
        namespace[name] = getattr(module, name)
    namespace["__all__"] = list(public_names)
    namespace["__doc__"] = module.__doc__
    return module


def run_canonical_main(module_name: str) -> int:
    module = load_canonical_module(module_name)
    result = module.main()
    return 0 if result is None else int(result)
