from __future__ import annotations

import json
import queue
import threading
import time
import uuid
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Optional

from .model import (
    MISSION_ARCHIVE_SCHEMA_VERSION,
    MISSION_EVENT_SCHEMA_VERSION,
    MissionArchiveSession,
    MissionEventDraft,
    MissionEventRecord,
)
from .schema import coerce_event_draft


def _default_archive_root() -> Path:
    here = Path(__file__).resolve()
    workspace_candidate = here.parents[4] / "logs" / "mission_archive"
    if workspace_candidate.parent.exists():
        return workspace_candidate
    return here.parents[3] / "logs" / "mission_archive"


class MissionArchiveWriter:
    """Background writer for immutable mission event archives."""

    def __init__(self, base_dir: Optional[Path] = None, queue_size: int = 0):
        self.base_dir = Path(base_dir) if base_dir is not None else _default_archive_root()
        maxsize = max(0, int(queue_size))
        self._queue: queue.Queue[dict[str, Any]] = queue.Queue(maxsize=maxsize)
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._state_lock = threading.Lock()
        self._active: Optional[MissionArchiveSession] = None
        self._active_events_fp = None
        self._active_mission_dir: Optional[Path] = None
        self._active_manifest_path: Optional[Path] = None
        self._active_started_at: float = 0.0
        self._active_stats: Dict[str, int] = {}
        self._active_sequence = 0
        self._last_event_id = ""
        self._dropped_events = 0
        self._failed_writes = 0
        self._pending_mission_id = ""
        self._last_error = ""

    def start(self) -> None:
        if self._thread is not None and self._thread.is_alive():
            return
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, name="mission-archive-writer", daemon=True)
        self._thread.start()

    def stop(self, timeout_s: float = 2.0) -> None:
        self._stop_event.set()
        self._put_nowait({"kind": "stop"})
        if self._thread is not None:
            self._thread.join(timeout=max(0.1, float(timeout_s)))
            self._thread = None

    def active_mission_id(self) -> str:
        with self._state_lock:
            if self._active is None:
                return str(self._pending_mission_id or "")
            return str(self._active.mission_id)

    def dropped_event_count(self) -> int:
        with self._state_lock:
            return int(self._dropped_events)

    def health_snapshot(self) -> Dict[str, Any]:
        with self._state_lock:
            return {
                "active_mission_id": str(self._active.mission_id) if self._active is not None else "",
                "pending_mission_id": str(self._pending_mission_id or ""),
                "dropped_events": int(self._dropped_events),
                "failed_writes": int(self._failed_writes),
                "queue_size": int(self._queue.qsize()),
                "last_error": str(self._last_error or ""),
            }

    def start_mission(
        self,
        *,
        metadata: Optional[Dict[str, Any]] = None,
        config_snapshot: Optional[Dict[str, Any]] = None,
        start_reason: str = "manual",
    ) -> str:
        current = self.active_mission_id()
        if current:
            return current
        mission_id = f"mission_{time.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        with self._state_lock:
            self._pending_mission_id = mission_id
        cmd = {
            "kind": "start_mission",
            "mission_id": mission_id,
            "started_at": float(time.time()),
            "metadata": dict(metadata or {}),
            "config_snapshot": dict(config_snapshot or {}),
            "start_reason": str(start_reason or "manual"),
        }
        self._put_nowait(cmd)
        return mission_id

    def end_mission(
        self,
        *,
        reason: str = "stopped",
        config_snapshot: Optional[Dict[str, Any]] = None,
    ) -> None:
        self._put_nowait(
            {
                "kind": "end_mission",
                "ended_at": float(time.time()),
                "reason": str(reason or "stopped"),
                "config_snapshot": dict(config_snapshot or {}),
            }
        )

    def publish_event(
        self,
        *,
        event_type: str,
        source: str,
        data: Optional[Dict[str, Any]] = None,
        severity: str = "info",
        tags: Optional[list[str]] = None,
        media_refs: Optional[list[str]] = None,
        config_snapshot: Optional[Dict[str, Any]] = None,
        occurred_at: Optional[float] = None,
        ensure_mission: bool = True,
    ) -> None:
        if ensure_mission and not self.active_mission_id():
            self.start_mission(start_reason="implicit_event")
        draft = MissionEventDraft(
            event_type=str(event_type or "unknown_event"),
            source=str(source or "unknown_source"),
            severity=str(severity or "info"),
            occurred_at=occurred_at,
            data=dict(data or {}),
            tags=list(tags or []),
            media_refs=list(media_refs or []),
            config_snapshot=dict(config_snapshot) if config_snapshot is not None else None,
        )
        self._put_nowait({"kind": "event", "draft": draft, "ensure_mission": bool(ensure_mission)})

    def _put_nowait(self, item: Dict[str, Any]) -> None:
        try:
            self._queue.put_nowait(item)
        except queue.Full:
            try:
                self._queue.put(item, timeout=0.05)
            except queue.Full:
                with self._state_lock:
                    self._dropped_events += 1

    def _run(self) -> None:
        while not self._stop_event.is_set():
            try:
                cmd = self._queue.get(timeout=0.2)
            except queue.Empty:
                continue

            kind = str(cmd.get("kind") or "")
            try:
                if kind == "start_mission":
                    self._handle_start_mission(cmd)
                elif kind == "event":
                    self._handle_event(cmd)
                elif kind == "end_mission":
                    self._handle_end_mission(cmd)
                elif kind == "stop":
                    break
            except Exception as exc:
                with self._state_lock:
                    self._last_error = str(exc)
                print(f"[MISSION_ARCHIVE] writer command failed ({kind}): {exc}", flush=True)

        try:
            self._close_active_stream()
        except Exception:
            pass

    def _handle_start_mission(self, cmd: Dict[str, Any]) -> None:
        if self._active is not None:
            return

        mission_id = str(cmd.get("mission_id") or "")
        started_at = float(cmd.get("started_at") or time.time())
        mission_dir = self.base_dir / mission_id
        snapshots_dir = mission_dir / "snapshots"
        events_path = mission_dir / "events.jsonl"
        manifest_path = mission_dir / "mission_manifest.json"

        snapshots_dir.mkdir(parents=True, exist_ok=True)
        mission_dir.mkdir(parents=True, exist_ok=True)

        manifest = {
            "archive_schema_version": int(MISSION_ARCHIVE_SCHEMA_VERSION),
            "event_schema_version": int(MISSION_EVENT_SCHEMA_VERSION),
            "mission_id": mission_id,
            "started_at": float(started_at),
            "start_reason": str(cmd.get("start_reason") or "manual"),
            "status": "active",
            "metadata": dict(cmd.get("metadata") or {}),
            "initial_config_snapshot": dict(cmd.get("config_snapshot") or {}),
        }
        with manifest_path.open("w", encoding="utf-8") as fp:
            json.dump(manifest, fp, ensure_ascii=True, indent=2)

        self._active_events_fp = events_path.open("a", encoding="utf-8")
        self._active = MissionArchiveSession(
            mission_id=mission_id,
            started_at=started_at,
            mission_path=str(mission_dir),
            events_path=str(events_path),
            snapshots_path=str(snapshots_dir),
            metadata=dict(cmd.get("metadata") or {}),
        )
        self._active_mission_dir = mission_dir
        self._active_manifest_path = manifest_path
        self._active_started_at = float(started_at)
        self._active_stats = {
            "event_count": 0,
            "detection_count": 0,
            "engagement_count": 0,
            "shot_count": 0,
        }
        self._active_sequence = 0
        self._last_event_id = ""
        with self._state_lock:
            self._pending_mission_id = ""

        self._write_event(
            MissionEventDraft(
                event_type="mission_started",
                source="archive_writer",
                severity="info",
                occurred_at=started_at,
                data={
                    "start_reason": str(cmd.get("start_reason") or "manual"),
                },
                config_snapshot=dict(cmd.get("config_snapshot") or {}),
            )
        )

    def _handle_event(self, cmd: Dict[str, Any]) -> None:
        if self._active is None:
            if bool(cmd.get("ensure_mission", False)):
                self._handle_start_mission(
                    {
                        "kind": "start_mission",
                        "mission_id": f"mission_{time.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}",
                        "started_at": float(time.time()),
                        "metadata": {"started_by": "writer_auto"},
                        "config_snapshot": {},
                        "start_reason": "auto_from_event",
                    }
                )
            else:
                return

        draft = cmd.get("draft")
        if not isinstance(draft, MissionEventDraft):
            return
        self._write_event(draft)

    def _handle_end_mission(self, cmd: Dict[str, Any]) -> None:
        if self._active is None:
            return
        ended_at = float(cmd.get("ended_at") or time.time())
        reason = str(cmd.get("reason") or "stopped")
        self._write_event(
            MissionEventDraft(
                event_type="mission_ended",
                source="archive_writer",
                severity="info",
                occurred_at=ended_at,
                data={"reason": reason},
                config_snapshot=dict(cmd.get("config_snapshot") or {}),
            )
        )
        self._finalize_manifest(ended_at=ended_at, reason=reason)
        self._close_active_stream()

    def _write_event(self, draft: MissionEventDraft) -> None:
        if self._active is None or self._active_events_fp is None:
            return
        draft = coerce_event_draft(draft)
        occurred_at = float(draft.occurred_at or time.time())
        written_at = float(time.time())
        self._active_sequence += 1
        event_id = uuid.uuid4().hex
        record = MissionEventRecord(
            mission_id=str(self._active.mission_id),
            sequence=int(self._active_sequence),
            event_id=event_id,
            event_schema_version=int(MISSION_EVENT_SCHEMA_VERSION),
            archive_schema_version=int(MISSION_ARCHIVE_SCHEMA_VERSION),
            occurred_at=occurred_at,
            written_at=written_at,
            event_type=str(draft.event_type),
            source=str(draft.source),
            severity=str(draft.severity),
            data=dict(draft.data or {}),
            tags=list(draft.tags or []),
            media_refs=list(draft.media_refs or []),
            config_snapshot=dict(draft.config_snapshot) if draft.config_snapshot is not None else None,
            prev_event_id=str(self._last_event_id),
        )
        self._last_event_id = event_id
        payload = asdict(record)
        line = json.dumps(payload, ensure_ascii=True) + "\n"
        try:
            self._active_events_fp.write(line)
            self._active_events_fp.flush()
            self._update_active_stats(record)
            return
        except Exception as exc:
            self._record_write_failure(exc)

        # Recovery path: reopen the stream and retry once.
        reopened = self._reopen_active_stream()
        if not reopened or self._active_events_fp is None:
            return
        try:
            self._active_events_fp.write(line)
            self._active_events_fp.flush()
            self._update_active_stats(record)
        except Exception as exc:
            self._record_write_failure(exc)

    def _reopen_active_stream(self) -> bool:
        active = self._active
        if active is None:
            return False
        path = Path(str(active.events_path or ""))
        if not path:
            return False
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            self._active_events_fp = path.open("a", encoding="utf-8")
            return True
        except Exception as exc:
            self._record_write_failure(exc)
            self._active_events_fp = None
            return False

    def _record_write_failure(self, exc: Exception) -> None:
        with self._state_lock:
            self._failed_writes += 1
            self._last_error = str(exc)

    def _update_active_stats(self, record: MissionEventRecord) -> None:
        stats = self._active_stats
        if not stats:
            return
        stats["event_count"] = int(stats.get("event_count", 0)) + 1
        event_type = str(record.event_type or "")
        if "detection" in event_type:
            stats["detection_count"] = int(stats.get("detection_count", 0)) + 1
        if "engagement" in event_type:
            stats["engagement_count"] = int(stats.get("engagement_count", 0)) + 1

        data = dict(record.data or {})
        if event_type == "engagement_telemetry" and bool(data.get("firing_approved", False)):
            burst = int(data.get("burst_count", 1) or 1)
            stats["shot_count"] = int(stats.get("shot_count", 0)) + max(1, burst)

    def _finalize_manifest(self, *, ended_at: float, reason: str) -> None:
        manifest_path = self._active_manifest_path
        mission_dir = self._active_mission_dir
        if manifest_path is None or mission_dir is None:
            return

        payload: Dict[str, Any] = {}
        try:
            if manifest_path.exists():
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            payload = {}

        started_at = float(payload.get("started_at", self._active_started_at) or self._active_started_at)
        duration_s = max(0.0, float(ended_at) - float(started_at))
        size_bytes = 0
        try:
            for path in mission_dir.rglob("*"):
                if path.is_file():
                    size_bytes += int(path.stat().st_size)
        except Exception:
            size_bytes = 0

        payload.update(
            {
                "archive_schema_version": int(MISSION_ARCHIVE_SCHEMA_VERSION),
                "event_schema_version": int(MISSION_EVENT_SCHEMA_VERSION),
                "status": "ended",
                "ended_at": float(ended_at),
                "end_reason": str(reason or "stopped"),
                "duration_s": float(duration_s),
                "stats": {
                    "event_count": int(self._active_stats.get("event_count", 0)),
                    "detection_count": int(self._active_stats.get("detection_count", 0)),
                    "engagement_count": int(self._active_stats.get("engagement_count", 0)),
                    "shot_count": int(self._active_stats.get("shot_count", 0)),
                },
                "mission_size_bytes": int(size_bytes),
            }
        )
        try:
            manifest_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
        except Exception as exc:
            self._record_write_failure(exc)

    def _close_active_stream(self) -> None:
        with self._state_lock:
            events_fp = self._active_events_fp
            self._active_events_fp = None
            self._active = None
            self._active_mission_dir = None
            self._active_manifest_path = None
            self._active_started_at = 0.0
            self._active_stats = {}
            self._active_sequence = 0
            self._last_event_id = ""
            self._pending_mission_id = ""
        if events_fp is not None:
            try:
                events_fp.close()
            except Exception:
                pass
