from __future__ import annotations

import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "sources.yaml"
BRAIN_PATH = ROOT / "data" / "brain.json"
LEARNINGS_PATH = ROOT / "brain" / "LEARNINGS.md"


def load_sources() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def get_env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        if default is not None:
            return default
        raise ValueError(f"Missing required environment variable: {name}")
    return value
