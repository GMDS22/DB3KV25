from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from runtime_paths import runtime_root_path
except ImportError:
    from app.runtime_paths import runtime_root_path

DEFAULT_VERSION = "2.3.2"
DEFAULT_TITLE_PREFIX = "SMART SENTRY"


def _read_text_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _repo_root() -> Path:
    return runtime_root_path()


def get_version(default: str = DEFAULT_VERSION) -> str:
    version_files = [
        _repo_root() / "SMART_SENTRY_V2_3_2_VERSION.txt",
        _repo_root() / "SMART_SENTRY_V2_3_1_VERSION.txt",
        _repo_root() / "SMART_SENTRY_V2_3_VERSION.txt",
        _repo_root() / "SMART_SENTRY_V3_0_VERSION.txt",
        _repo_root() / "SMART_SENTRY_V2_0_VERSION.txt",
        _repo_root() / "DB3K_VERSION.txt",
    ]
    for version_path in version_files:
        try:
            raw = _read_text_utf8(version_path).strip()
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
        data = json.loads(_read_text_utf8(path))
        items = data.get("items", [])
        file_max = int(data.get("max_items", max_items) or max_items)
        return _normalize_items(items, min(max_items, file_max))
    except Exception:
        return []


def append_recent_update(date: str, title: str, max_items: int = 10) -> None:
    """Optional helper for maintainers/scripts: appends an update and trims to max_items."""
    path = _repo_root() / "RECENT_UPDATES.json"
    try:
        data = json.loads(_read_text_utf8(path))
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
