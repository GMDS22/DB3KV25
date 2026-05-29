"""
SMART SENTRY V3 — ML Training Logger

Collects engagement and manual targeting data for ML model training.
Tracks both automatic Sentry decisions and manual user targeting.

Features:
  - Log automatic engagement decisions (Sentry fires / ignores)
  - Log manual fire events with detections
  - Log visible detections user ignored (negative examples)
  - Extract features from detections automatically
  - Save/load training data to JSON
  - Train ML model from collected data
"""

from __future__ import annotations

import json
import time
from collections import defaultdict, deque
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .target_filter import DetectedObject


@dataclass
class TrainingExample:
    """Single training example: features + label."""
    timestamp: float
    features: List[float]  # [proximity, size, conf, class_score, speed, persistence, approach]
    label: float  # 0.0 = ignore, 1.0 = fire
    source: str  # "auto_sentry", "manual_fire", "manual_ignore_sample"
    class_name: str = ""
    frame_number: int = 0


class MLTrainingLogger:
    """
    Collects training data from Sentry engagement decisions
    and manual user targeting.
    """

    def __init__(self, data_file: str = "config/ml_training_data.json"):
        self.data_file = Path(data_file)
        # Cap in-memory examples so a long-running session can never exhaust
        # RAM.  deque(maxlen=N) evicts the oldest entry automatically on append
        # once the cap is reached — all consumers (.append, for-in, len,
        # list-comprehension, .clear) are fully compatible with deque.
        self.max_examples: int = 10_000
        self.examples: deque = deque(maxlen=self.max_examples)
        self._load_existing()
        self._last_ignore_sample_time = time.time()
        self._ignore_sample_interval = 2.0  # sample ignore targets every 2 sec

    def _load_existing(self) -> None:
        """Load any previously saved training data."""
        try:
            if self.data_file.exists():
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    for item in data.get("examples", []):
                        ex = TrainingExample(
                            timestamp=item["timestamp"],
                            features=item["features"],
                            label=item["label"],
                            source=item["source"],
                            class_name=item.get("class_name", ""),
                            frame_number=item.get("frame_number", 0),
                        )
                        self.examples.append(ex)
        except Exception:
            pass

    def save(self) -> bool:
        """Save training data to disk."""
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            data = {
                "examples": [asdict(ex) for ex in self.examples],
                "count": len(self.examples),
                "last_saved": time.time(),
            }
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False

    def log_auto_sentry_fire(
        self,
        target: DetectedObject,
        speed: float = 0.0,
        persistence: float = 0.0,
        approach_rate: float = 0.0,
    ) -> None:
        """Log automatic Sentry engagement decision (fire)."""
        features = self._extract_features(
            target, speed, persistence, approach_rate
        )
        ex = TrainingExample(
            timestamp=time.time(),
            features=features,
            label=1.0,
            source="auto_sentry",
            class_name=target.class_name,
        )
        self.examples.append(ex)

    def log_auto_sentry_ignore(
        self,
        target: DetectedObject,
        speed: float = 0.0,
        persistence: float = 0.0,
        approach_rate: float = 0.0,
    ) -> None:
        """Log automatic Sentry ignore decision."""
        features = self._extract_features(
            target, speed, persistence, approach_rate
        )
        ex = TrainingExample(
            timestamp=time.time(),
            features=features,
            label=0.0,
            source="auto_sentry",
            class_name=target.class_name,
        )
        self.examples.append(ex)

    def log_manual_fire(
        self,
        target: DetectedObject,
        speed: float = 0.0,
        persistence: float = 0.0,
        approach_rate: float = 0.0,
    ) -> None:
        """
        Log manual user fire at a target.
        This is ground truth — user explicitly fired at this.
        """
        features = self._extract_features(
            target, speed, persistence, approach_rate
        )
        ex = TrainingExample(
            timestamp=time.time(),
            features=features,
            label=1.0,
            source="manual_fire",
            class_name=target.class_name,
        )
        self.examples.append(ex)

    def log_manual_ignore_sample(
        self,
        target: DetectedObject,
        speed: float = 0.0,
        persistence: float = 0.0,
        approach_rate: float = 0.0,
    ) -> bool:
        """
        Log a visible detection the user is NOT firing at.
        Sampled to avoid too many negative examples.
        Returns True if logged, False if interval not reached.
        """
        now = time.time()
        if now - self._last_ignore_sample_time < self._ignore_sample_interval:
            return False

        self._last_ignore_sample_time = now
        features = self._extract_features(
            target, speed, persistence, approach_rate
        )
        ex = TrainingExample(
            timestamp=now,
            features=features,
            label=0.0,
            source="manual_ignore_sample",
            class_name=target.class_name,
        )
        self.examples.append(ex)
        return True

    def get_training_data(
        self, min_examples: int = 10
    ) -> Tuple[List[List[float]], List[float]]:
        """
        Extract features and labels for ML training.
        Returns (features_list, labels_list) or ([], []) if insufficient data.
        """
        if len(self.examples) < min_examples:
            return [], []

        features_list = [ex.features for ex in self.examples]
        labels = [ex.label for ex in self.examples]
        return features_list, labels

    def get_stats(self) -> Dict:
        """Return training data statistics."""
        total = len(self.examples)
        fires = sum(1 for ex in self.examples if ex.label > 0.5)
        ignores = total - fires

        by_source = defaultdict(int)
        for ex in self.examples:
            by_source[ex.source] += 1

        return {
            "total_examples": total,
            "fire_examples": fires,
            "ignore_examples": ignores,
            "by_source": dict(by_source),
        }

    def summary_stats(self) -> Dict:
        """Compatibility summary used by the UI/engine helpers."""
        stats = self.get_stats()
        total = int(stats.get("total_examples", 0))
        engaged = int(stats.get("fire_examples", 0))
        ignored = int(stats.get("ignore_examples", 0))
        engagement_rate = (float(engaged) / float(total)) if total > 0 else 0.0

        class_distribution = defaultdict(int)
        for ex in self.examples:
            class_name = str(ex.class_name or "unknown").strip() or "unknown"
            class_distribution[class_name] += 1

        return {
            "total_records": total,
            "engaged_count": engaged,
            "ignored_count": ignored,
            "engagement_rate": engagement_rate,
            "class_distribution": dict(class_distribution),
            "by_source": dict(stats.get("by_source", {})),
            "data_file": str(self.data_file),
            "data_file_exists": bool(self.data_file.exists()),
        }

    def clear(self) -> None:
        """Clear all training data."""
        self.examples.clear()

    def _extract_features(
        self,
        det: DetectedObject,
        speed: float,
        persistence: float,
        approach_rate: float,
    ) -> List[float]:
        """Extract the 7-dimensional feature vector."""
        import math

        # Proximity
        dx = det.norm_cx - 0.5
        dy = det.norm_cy - 0.5
        dist = math.sqrt(dx * dx + dy * dy)
        proximity = max(0.0, 1.0 - dist / 0.707)

        # Size
        size = min(1.0, det.area_ratio / 0.15)

        # Confidence
        conf = det.confidence

        # Class priority (default to 1.0 if unknown)
        class_score = 1.0

        # Speed
        speed_score = min(1.0, speed / 2.0)

        # Persistence
        persistence_score = min(1.0, persistence / 10.0)

        # Approach
        approach_score = max(0.0, min(1.0, approach_rate / 1.0 + 0.5))

        return [proximity, size, conf, class_score, speed_score, persistence_score, approach_score]
