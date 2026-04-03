from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

DEFAULT_VERSION = "2.0.0"
DEFAULT_TITLE_PREFIX = "Smart Sentry"


def _repo_root() -> Path:
    # app/db3k_meta.py -> repo root is one level up from /app
    return Path(__file__).resolve().parent.parent


def get_version(default: str = DEFAULT_VERSION) -> str:
    version_files = [
        _repo_root() / "SMART_SENTRY_V2_0_VERSION.txt",
        _repo_root() / "DB3K_VERSION.txt",
    ]
    for version_path in version_files:
        try:
            raw = version_path.read_text(encoding="utf-8").strip()
            raw = raw.lstrip("vV").strip()
            if raw:
                return raw
        except Exception:
            continue
    return default


def get_commit_prefix() -> str:
    return f"db3kv{get_version()}"


def get_app_title(prefix: str = DEFAULT_TITLE_PREFIX) -> str:
    return f"{prefix} V{get_version()}"


@dataclass(frozen=True)
class RecentUpdate:
    date: str
    title: str


def _normalize_items(items: Iterable[dict[str, Any]], max_items: int) -> list[RecentUpdate]:
    normalized: list[RecentUpdate] = []
    for item in items:
        date = str(item.get("date", "")).strip()
        title = str(item.get("title", "")).strip()
        if not title:
            continue
        normalized.append(RecentUpdate(date=date, title=title))

    # Keep newest-first, cap
    return normalized[: max(0, int(max_items))]


def load_recent_updates(max_items: int = 10) -> list[RecentUpdate]:
    path = _repo_root() / "RECENT_UPDATES.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        items = data.get("items", [])
        file_max = int(data.get("max_items", max_items) or max_items)
        return _normalize_items(items, min(max_items, file_max))
    except Exception:
        return []


def append_recent_update(date: str, title: str, max_items: int = 10) -> None:
    """Optional helper for maintainers/scripts: appends an update and trims to max_items."""
    path = _repo_root() / "RECENT_UPDATES.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        data = {"schema": 1, "max_items": max_items, "items": []}

    items = list(data.get("items", []) or [])
    items.insert(0, {"date": str(date).strip(), "title": str(title).strip()})

    trimmed = []
    for it in items:
        t = str(it.get("title", "")).strip()
        if not t:
            continue
        trimmed.append({"date": str(it.get("date", "")).strip(), "title": t})
        if len(trimmed) >= max_items:
            break

    data["max_items"] = max_items
    data["items"] = trimmed
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
