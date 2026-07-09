from __future__ import annotations

from typing import Iterable

from .model import MissionEventDraft

_ALLOWED_SEVERITY = {"debug", "info", "warning", "error", "critical"}


def coerce_event_draft(draft: MissionEventDraft) -> MissionEventDraft:
    event_type = str(draft.event_type or "unknown_event").strip() or "unknown_event"
    source = str(draft.source or "unknown_source").strip() or "unknown_source"
    severity = str(draft.severity or "info").strip().lower()
    if severity not in _ALLOWED_SEVERITY:
        severity = "info"

    tags = _unique_nonempty(str(tag).strip() for tag in list(draft.tags or []))
    media_refs = _unique_nonempty(str(ref).strip() for ref in list(draft.media_refs or []))

    draft.event_type = event_type
    draft.source = source
    draft.severity = severity
    draft.tags = tags
    draft.media_refs = media_refs
    draft.data = dict(draft.data or {})
    if draft.config_snapshot is not None:
        draft.config_snapshot = dict(draft.config_snapshot)
    return draft


def _unique_nonempty(values: Iterable[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out
