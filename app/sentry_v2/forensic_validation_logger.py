"""
SMART SENTRY V3 - Forensic Validation Logger

Append-only JSONL logger for runtime detection/filter/planner/engagement
forensics. This logger is diagnostics-only and must never influence
runtime targeting decisions.
"""

from __future__ import annotations

import json
import threading
import time
from pathlib import Path
from typing import Any, Dict, Optional


class ForensicValidationLogger:
    def __init__(self, log_dir: Optional[Path] = None):
        root = Path(__file__).resolve().parents[2]
        base = root / "logs" / "forensic_validation"
        self.log_dir = Path(log_dir) if log_dir is not None else base
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.run_id = time.strftime("%Y%m%d_%H%M%S")
        self.log_path = self.log_dir / f"forensic_validation_{self.run_id}.jsonl"
        self._lock = threading.Lock()
        self._sequence = 0

    def append(self, record: Dict[str, Any]) -> None:
        payload = dict(record or {})
        with self._lock:
            self._sequence += 1
            payload.setdefault("sequence", int(self._sequence))
            payload.setdefault("timestamp", float(time.time()))
            payload.setdefault(
                "timestamp_local",
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(payload["timestamp"])),
            )
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            with self.log_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
