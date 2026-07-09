from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

MISSION_ARCHIVE_SCHEMA_VERSION = 1
MISSION_EVENT_SCHEMA_VERSION = 1


@dataclass
class MissionArchiveSession:
    mission_id: str
    started_at: float
    mission_path: str
    events_path: str
    snapshots_path: str
    status: str = "active"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MissionMediaRef:
    media_id: str
    kind: str
    rel_path: str
    frame_key: str
    created_at: float
    width: int = 0
    height: int = 0
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MissionEventDraft:
    event_type: str
    source: str
    severity: str = "info"
    occurred_at: Optional[float] = None
    data: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    media_refs: List[str] = field(default_factory=list)
    config_snapshot: Optional[Dict[str, Any]] = None


@dataclass
class MissionEventRecord:
    mission_id: str
    sequence: int
    event_id: str
    event_schema_version: int
    archive_schema_version: int
    occurred_at: float
    written_at: float
    event_type: str
    source: str
    severity: str
    data: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    media_refs: List[str] = field(default_factory=list)
    config_snapshot: Optional[Dict[str, Any]] = None
    prev_event_id: str = ""
