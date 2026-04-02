from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PROGRAM_ROOT = REPO_ROOT / "programs" / "resilient-home-intelligence"
DOCS_ROOT = PROGRAM_ROOT / "docs"
DOCS_EXAMPLES_DIR = DOCS_ROOT / "data-model" / "examples"
INFERENCE_CONFIG_DIR = PROGRAM_ROOT / "software" / "inference-engine" / "config"
