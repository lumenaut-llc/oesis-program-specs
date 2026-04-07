import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PROGRAM_ROOT = REPO_ROOT / "programs" / "open-environmental-sensing-and-inference-system"
DOCS_ROOT = PROGRAM_ROOT / "docs"
RUNTIME_ROOT = REPO_ROOT / "oesis"
RUNTIME_ASSETS_DIR = RUNTIME_ROOT / "assets"
RUNTIME_EXAMPLES_DIR = RUNTIME_ASSETS_DIR / "examples"
RUNTIME_INFERENCE_CONFIG_DIR = RUNTIME_ASSETS_DIR / "config" / "inference"

_contracts_bundle_dir = os.environ.get("OESIS_CONTRACTS_BUNDLE_DIR")
if _contracts_bundle_dir:
    bundle_examples_dir = Path(_contracts_bundle_dir).expanduser().resolve() / "examples"
    DOCS_EXAMPLES_DIR = bundle_examples_dir if bundle_examples_dir.is_dir() else RUNTIME_EXAMPLES_DIR
else:
    DOCS_EXAMPLES_DIR = RUNTIME_EXAMPLES_DIR

_inference_config_dir = os.environ.get("OESIS_INFERENCE_CONFIG_DIR")
if _inference_config_dir:
    INFERENCE_CONFIG_DIR = Path(_inference_config_dir).expanduser().resolve()
else:
    INFERENCE_CONFIG_DIR = RUNTIME_INFERENCE_CONFIG_DIR
