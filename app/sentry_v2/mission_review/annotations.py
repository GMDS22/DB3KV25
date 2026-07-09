from __future__ import annotations

import time
from typing import Any, Dict, List


def normalize_annotations(payload: Dict[str, Any]) -> Dict[str, Any]:
    data = dict(payload or {})
    data.setdefault("version", 1)
    data.setdefault("bookmarked", False)
    data.setdefault("notes", [])
    data.setdefault("event_annotations", {})
    if not isinstance(data["notes"], list):
        data["notes"] = []
    if not isinstance(data["event_annotations"], dict):
        data["event_annotations"] = {}
    return data


def set_event_annotation(
    payload: Dict[str, Any],
    event_id: str,
    *,
    note: str,
    bookmarked: bool,
    labels: List[str],
    tags: List[str],
    flags: List[str],
) -> Dict[str, Any]:
    out = normalize_annotations(payload)
    event_annotations = dict(out.get("event_annotations") or {})
    event_annotations[str(event_id)] = {
        "note": str(note or "").strip(),
        "bookmarked": bool(bookmarked),
        "labels": [str(v).strip() for v in list(labels or []) if str(v).strip()],
        "tags": [str(v).strip() for v in list(tags or []) if str(v).strip()],
        "flags": [str(v).strip() for v in list(flags or []) if str(v).strip()],
        "updated_at": float(time.time()),
    }
    out["event_annotations"] = event_annotations
    return out


def event_annotation(payload: Dict[str, Any], event_id: str) -> Dict[str, Any]:
    data = normalize_annotations(payload)
    return dict((data.get("event_annotations") or {}).get(str(event_id), {}) or {})
