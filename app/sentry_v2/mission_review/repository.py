from __future__ import annotations

import json
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


ARCHIVE_SCHEMA_VERSION = 1


def default_archive_root() -> Path:
    here = Path(__file__).resolve()
    workspace_candidate = here.parents[4] / "logs" / "mission_archive"
    if workspace_candidate.parent.exists():
        return workspace_candidate
    return here.parents[3] / "logs" / "mission_archive"


def event_category(event_type: str) -> str:
    et = str(event_type or "").strip().lower()
    if "fire" in et:
        return "fire"
    if "detection" in et:
        return "detection"
    if "tracking" in et or "motion" in et:
        return "tracking"
    if "planner" in et:
        return "planner"
    if "engagement" in et:
        return "engagement"
    if "config" in et:
        return "configuration"
    if "state" in et or "mission_" in et:
        return "system"
    return "system"


@dataclass
class MissionEvent:
    mission_id: str
    sequence: int
    event_id: str
    occurred_at: float
    written_at: float
    event_type: str
    category: str
    source: str
    severity: str
    frame_number: int = -1
    tracker_id: int = -1
    object_class: str = ""
    confidence: float = 0.0
    threat_score: float = 0.0
    decision: str = ""
    planner_state: str = ""
    motion_policy_state: str = ""
    safety_state: str = ""
    media_refs: List[str] = field(default_factory=list)
    data: Dict[str, Any] = field(default_factory=dict)
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MissionSummary:
    mission_name: str
    mission_id: str
    start_time: float
    end_time: float
    duration_s: float
    active_profile: str
    detection_model: str
    events_count: int
    detections_count: int
    engagements_count: int
    shots_fired: int
    mission_size_bytes: int
    has_notes: bool
    bookmarked: bool
    notes_count: int
    path: str


class MissionRepository:
    def __init__(self, archive_root: Optional[Path] = None):
        self.archive_root = Path(archive_root) if archive_root is not None else default_archive_root()

    def list_mission_dirs(self) -> List[Path]:
        if not self.archive_root.exists():
            return []
        return sorted(
            [p for p in self.archive_root.iterdir() if p.is_dir() and p.name.startswith("mission_")],
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )

    def load_missions(self) -> List[MissionSummary]:
        items: List[MissionSummary] = []
        for mission_dir in self.list_mission_dirs():
            summary = self._build_summary(mission_dir)
            if summary is not None:
                items.append(summary)
        return items

    def load_mission_events(self, mission_id: str) -> List[MissionEvent]:
        mission_dir = self.archive_root / str(mission_id)
        events_path = mission_dir / "events.jsonl"
        if not events_path.exists():
            return []

        out: List[MissionEvent] = []
        for line in events_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except Exception:
                continue
            out.append(self._to_event(payload))
        out.sort(key=lambda e: e.sequence)
        return out

    def load_manifest(self, mission_id: str) -> Dict[str, Any]:
        path = self.archive_root / str(mission_id) / "mission_manifest.json"
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def load_annotations(self, mission_id: str) -> Dict[str, Any]:
        path = self.archive_root / str(mission_id) / "annotations.json"
        if not path.exists():
            return {"version": 1, "bookmarked": False, "notes": [], "event_annotations": {}}
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            payload = {}
        if not isinstance(payload, dict):
            payload = {}
        payload.setdefault("version", 1)
        payload.setdefault("bookmarked", False)
        payload.setdefault("notes", [])
        payload.setdefault("event_annotations", {})
        return payload

    def save_annotations(self, mission_id: str, payload: Dict[str, Any]) -> None:
        mission_dir = self.archive_root / str(mission_id)
        mission_dir.mkdir(parents=True, exist_ok=True)
        path = mission_dir / "annotations.json"
        path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

    def rename_mission(self, mission_id: str, mission_name: str) -> None:
        mission_id = str(mission_id)
        manifest = self.load_manifest(mission_id)
        manifest["mission_name"] = str(mission_name or mission_id).strip() or mission_id
        path = self.archive_root / mission_id / "mission_manifest.json"
        path.write_text(json.dumps(manifest, ensure_ascii=True, indent=2), encoding="utf-8")

    def delete_mission(self, mission_id: str) -> None:
        target = self.archive_root / str(mission_id)
        if target.exists() and target.is_dir():
            shutil.rmtree(target)

    def duplicate_mission(self, mission_id: str) -> str:
        source = self.archive_root / str(mission_id)
        if not source.exists():
            raise FileNotFoundError(f"Mission not found: {mission_id}")
        suffix = time.strftime("%Y%m%d_%H%M%S")
        new_id = f"{mission_id}_copy_{suffix}"
        target = self.archive_root / new_id
        shutil.copytree(source, target)
        return new_id

    def mission_size_bytes(self, mission_id: str) -> int:
        mission_dir = self.archive_root / str(mission_id)
        if not mission_dir.exists():
            return 0
        total = 0
        for path in mission_dir.rglob("*"):
            if path.is_file():
                try:
                    total += int(path.stat().st_size)
                except Exception:
                    pass
        return total

    def search_events(self, events: Iterable[MissionEvent], keyword: str) -> List[MissionEvent]:
        query = str(keyword or "").strip().lower()
        if not query:
            return list(events)
        out: List[MissionEvent] = []
        for event in events:
            blob = " ".join(
                [
                    str(event.event_type),
                    str(event.category),
                    str(event.source),
                    str(event.object_class),
                    str(event.decision),
                    str(event.planner_state),
                    str(event.motion_policy_state),
                    str(event.safety_state),
                    json.dumps(event.data, ensure_ascii=True),
                ]
            ).lower()
            if query in blob:
                out.append(event)
        return out

    def _build_summary(self, mission_dir: Path) -> Optional[MissionSummary]:
        mission_id = mission_dir.name
        manifest_path = mission_dir / "mission_manifest.json"
        events_path = mission_dir / "events.jsonl"
        if not manifest_path.exists() or not events_path.exists():
            return None

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            return None

        annotations = self.load_annotations(mission_id)
        stats = dict(manifest.get("stats") or {})
        start_time = float(manifest.get("started_at", 0.0) or 0.0)
        end_time = float(manifest.get("ended_at", 0.0) or 0.0)
        duration_s = float(manifest.get("duration_s", max(0.0, end_time - start_time)) or 0.0)

        active_profile = ""
        detection_model = ""
        cfg = dict(manifest.get("initial_config_snapshot") or {})
        runtime_cfg = dict(cfg.get("runtime") or {})
        active_profile = str(runtime_cfg.get("active_master_profile", "") or "")
        detection_mode = dict(cfg.get("detection_mode") or {})
        detection_model = str(detection_mode.get("yolo_model_name", "") or runtime_cfg.get("yolo_model_name", ""))

        name = str(manifest.get("mission_name") or mission_id)
        size_bytes = int(manifest.get("mission_size_bytes", self.mission_size_bytes(mission_id)) or 0)
        notes = list(annotations.get("notes") or [])
        bookmarked = bool(annotations.get("bookmarked", False))

        return MissionSummary(
            mission_name=name,
            mission_id=mission_id,
            start_time=start_time,
            end_time=end_time,
            duration_s=duration_s,
            active_profile=active_profile,
            detection_model=detection_model,
            events_count=int(stats.get("event_count", 0) or 0),
            detections_count=int(stats.get("detection_count", 0) or 0),
            engagements_count=int(stats.get("engagement_count", 0) or 0),
            shots_fired=int(stats.get("shot_count", 0) or 0),
            mission_size_bytes=size_bytes,
            has_notes=bool(notes),
            bookmarked=bookmarked,
            notes_count=len(notes),
            path=str(mission_dir),
        )

    def _to_event(self, payload: Dict[str, Any]) -> MissionEvent:
        data = dict(payload.get("data") or {})
        planner = data.get("planner_state")
        if isinstance(planner, dict):
            planner_state = str(planner.get("engage_phase", "") or "")
        else:
            planner_state = str(planner or "")

        safety = data.get("safety_state")
        if isinstance(safety, dict):
            safety_state = str(safety.get("fire_veto_reason", "") or "")
        else:
            safety_state = str(safety or "")

        decision = str(data.get("firing_rejected_reason", "") or "")
        if not decision and bool(data.get("firing_approved", False)):
            decision = "approved"

        frame_number = int(payload.get("frame_number", data.get("frame_number", -1)) or -1)
        tracker_id = int(payload.get("tracker_id", data.get("tracker_id", -1)) or -1)
        confidence = float(payload.get("yolo_confidence", data.get("yolo_confidence", 0.0)) or 0.0)
        threat_score = float(payload.get("threat_score", data.get("threat_score", 0.0)) or 0.0)
        object_class = str(payload.get("yolo_class", data.get("yolo_class", "")) or "")

        et = str(payload.get("event_type", "") or "")
        motion_policy_state = str(payload.get("motion_policy_state", data.get("motion_policy_state", "")) or "")

        return MissionEvent(
            mission_id=str(payload.get("mission_id", "") or ""),
            sequence=int(payload.get("sequence", 0) or 0),
            event_id=str(payload.get("event_id", "") or ""),
            occurred_at=float(payload.get("occurred_at", 0.0) or 0.0),
            written_at=float(payload.get("written_at", 0.0) or 0.0),
            event_type=et,
            category=event_category(et),
            source=str(payload.get("source", "") or ""),
            severity=str(payload.get("severity", "info") or "info"),
            frame_number=frame_number,
            tracker_id=tracker_id,
            object_class=object_class,
            confidence=confidence,
            threat_score=threat_score,
            decision=decision,
            planner_state=planner_state,
            motion_policy_state=motion_policy_state,
            safety_state=safety_state,
            media_refs=list(payload.get("media_refs") or []),
            data=data,
            raw=dict(payload),
        )
