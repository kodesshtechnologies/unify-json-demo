# src/utils/utils.py
from pathlib import Path
import json
from typing import Iterable

def ensure_parent(path: Path):
    """Create the parent folder if needed."""
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

def write_ndjson(items: Iterable[dict], path: Path):
    """Write iterable dicts to NDJSON file."""
    ensure_parent(path)
    count = 0
    with open(path, "w", encoding="utf-8") as fp:
        for item in items:
            fp.write(json.dumps(item, default=str) + "\n")
            count += 1
    return count
