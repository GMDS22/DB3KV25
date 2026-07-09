from __future__ import annotations

import json
import threading
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


class EngagementTelemetryLogger:
    """Append-only JSONL telemetry sink for engagement decision evidence."""

    def __init__(self, runtime_root: Path | None = None) -> None:
        self._lock = threading.Lock()
        self._run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._sequence = 0
        self._runtime_root = Path(runtime_root) if runtime_root is not None else Path(__file__).resolve().parents[2]
        self._log_dir = self._runtime_root / "logs" / "engagement_telemetry"
        self._log_path = self._log_dir / f"engagement_telemetry_{self._run_id}.jsonl"

    @property
    def run_id(self) -> str:
        return self._run_id

    @property
    def log_path(self) -> Path:
        return self._log_path

    def append(self, record: Dict[str, Any]) -> None:
        payload = dict(record)
        with self._lock:
            self._sequence += 1
            payload.setdefault("run_id", self._run_id)
            payload.setdefault("sequence", self._sequence)
            self._log_dir.mkdir(parents=True, exist_ok=True)
            with self._log_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False))
                handle.write("\n")
