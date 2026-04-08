"""
SMART SENTRY V3 — Threat Scorer

Assigns a 0-1 threat score to each qualified detection using a weighted
formula.  Optionally refines scores with a small ML model (sklearn MLP)
that can be trained from user engagement feedback.

Scoring factors:
  - Proximity to frame center (closer = higher)
  - Object size (larger = higher)
  - YOLO confidence
  - Class priority
  - Movement speed
  - Time-in-frame (persistence)
  - Approach heading (moving toward guard point = higher)
"""

from __future__ import annotations

import math
import importlib
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from .sentry_v2_config import ThreatScoringConfig, TargetFilterConfig
from .target_filter import DetectedObject

def _sklearn_available() -> bool:
    try:
        return importlib.util.find_spec("sklearn") is not None
    except Exception:
        return False


@dataclass
class TrackedTarget:
    """Enriched target with history for scoring."""
    det: DetectedObject
    threat_score: float = 0.0
    speed: float = 0.0          # pixels / second
    heading_x: float = 0.0      # normalised velocity
    heading_y: float = 0.0
    persistence: float = 0.0    # seconds since first seen
    approach_rate: float = 0.0  # closing speed toward center (positive = approaching)

    @property
    def id(self) -> int:
        """Compatibility alias for older call sites that still expect target.id."""
        return int(self.det.track_id)

    @property
    def target_id(self) -> int:
        return int(self.det.track_id)


class ThreatScorer:
    """
    Computes threat scores for detected objects.

    Maintains a lightweight history per track_id to derive speed,
    persistence, and heading.  History is pruned when a track disappears.
    """

    def __init__(
        self,
        scoring_cfg: ThreatScoringConfig,
        filter_cfg: TargetFilterConfig,
        ml_logger: Optional[object] = None,
    ):
        self.scoring = scoring_cfg
        self.filter_cfg = filter_cfg
        self.ml_logger = ml_logger  # Optional training logger

        # Per-track history: track_id → list of (timestamp, norm_cx, norm_cy)
        self._history: Dict[int, List[Tuple[float, float, float]]] = defaultdict(list)
        # First-seen timestamps
        self._first_seen: Dict[int, float] = {}
        # Last-seen (for pruning)
        self._last_seen: Dict[int, float] = {}
        self._warning_keys: Set[str] = set()

        # Optional ML model
        self._ml_model: object = None
        if scoring_cfg.use_ml_model and _sklearn_available():
            self._load_ml_model(scoring_cfg.ml_model_path)
        elif scoring_cfg.use_ml_model and not _sklearn_available():
            self._log_ml_warning(
                "ML scoring requested but scikit-learn is not installed; using weighted scoring only",
                once_key="missing_sklearn",
            )

        self._MAX_HISTORY = 30  # frames kept per track

    def _log_ml_warning(self, message: str, exc: Optional[Exception] = None, *, once_key: str = "") -> None:
        if once_key:
            if once_key in self._warning_keys:
                return
            self._warning_keys.add(once_key)
        suffix = f": {exc}" if exc is not None else ""
        print(f"[SENTRY_V2_THREAT] {message}{suffix}", flush=True)

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def score(
        self, detections: List[DetectedObject], timestamp: Optional[float] = None
    ) -> List[TrackedTarget]:
        """Score and return enriched targets sorted by threat (descending)."""
        now = timestamp or time.time()
        self._update_history(detections, now)
        targets = [self._score_one(d, now) for d in detections]
        targets.sort(key=lambda t: t.threat_score, reverse=True)
        self._prune_stale(now, max_age=5.0)
        return targets

    def update_config(
        self,
        scoring_cfg: ThreatScoringConfig,
        filter_cfg: TargetFilterConfig,
    ) -> None:
        self.scoring = scoring_cfg
        self.filter_cfg = filter_cfg
        
        # Hot-reload ML model if enabled and path changed or toggled on
        if scoring_cfg.use_ml_model and _sklearn_available():
            self._load_ml_model(scoring_cfg.ml_model_path)
        elif scoring_cfg.use_ml_model and not _sklearn_available():
            self._log_ml_warning(
                "ML scoring requested but scikit-learn is not installed; using weighted scoring only",
                once_key="missing_sklearn",
            )
        else:
            self._ml_model = None

    # ------------------------------------------------------------------ #
    # Internal scoring
    # ------------------------------------------------------------------ #

    def _score_one(self, det: DetectedObject, now: float) -> TrackedTarget:
        s = self.scoring
        tid = det.track_id

        # --- Proximity (distance from center, inverted) ---
        dx = det.norm_cx - 0.5
        dy = det.norm_cy - 0.5
        dist = math.sqrt(dx * dx + dy * dy)  # max ~0.707
        proximity = max(0.0, 1.0 - dist / 0.707)

        # --- Size ---
        size = min(1.0, det.area_ratio / 0.15)  # soft cap at 15% of frame

        # --- Confidence ---
        conf = det.confidence

        # --- Class priority ---
        base_prio = self.filter_cfg.class_priority.get(det.class_name, 1.0)
        max_prio = max(self.filter_cfg.class_priority.values()) if self.filter_cfg.class_priority else 1.0
        class_score = base_prio / max(1.0, max_prio)

        # --- Speed & heading (from history) ---
        speed = 0.0
        heading_x, heading_y = 0.0, 0.0
        approach_rate = 0.0
        hist = self._history.get(tid, [])
        if len(hist) >= 2:
            t0, x0, y0 = hist[-2]
            t1, x1, y1 = hist[-1]
            dt = max(0.001, t1 - t0)
            vx = (x1 - x0) / dt
            vy = (y1 - y0) / dt
            speed = math.sqrt(vx * vx + vy * vy)
            heading_x, heading_y = vx, vy
            # Approach rate: positive if getting closer to center
            dist_prev = math.sqrt((x0 - 0.5) ** 2 + (y0 - 0.5) ** 2)
            dist_now = math.sqrt((x1 - 0.5) ** 2 + (y1 - 0.5) ** 2)
            approach_rate = (dist_prev - dist_now) / dt  # positive = approaching

        speed_score = min(1.0, speed / 2.0)  # cap at 2 norm-units/sec
        approach_score = max(0.0, min(1.0, approach_rate / 1.0 + 0.5))

        # --- Persistence ---
        persistence = now - self._first_seen.get(tid, now)
        persistence_score = min(1.0, persistence / 10.0)  # fully maxed at 10s

        # --- Weighted sum ---
        raw = (
            s.w_proximity * proximity
            + s.w_size * size
            + s.w_confidence * conf
            + s.w_class_priority * class_score
            + s.w_speed * speed_score
            + s.w_persistence * persistence_score
            + s.w_approach * approach_score
        )
        total_weight = (
            s.w_proximity + s.w_size + s.w_confidence + s.w_class_priority
            + s.w_speed + s.w_persistence + s.w_approach
        )
        threat = raw / max(0.01, total_weight)

        # --- Optional ML refinement ---
        if self._ml_model is not None:
            features = [proximity, size, conf, class_score, speed_score, persistence_score, approach_score]
            try:
                ml_score = float(self._ml_model.predict([features])[0])  # type: ignore[union-attr]
                threat = 0.6 * threat + 0.4 * max(0.0, min(1.0, ml_score))
            except Exception as exc:
                self._log_ml_warning(
                    "ML threat refinement failed; using weighted scoring fallback",
                    exc,
                    once_key="predict_failed",
                )

        threat = max(0.0, min(1.0, threat))

        return TrackedTarget(
            det=det,
            threat_score=threat,
            speed=speed,
            heading_x=heading_x,
            heading_y=heading_y,
            persistence=persistence,
            approach_rate=approach_rate,
        )

    # ------------------------------------------------------------------ #
    # History management
    # ------------------------------------------------------------------ #

    def _update_history(self, detections: List[DetectedObject], now: float) -> None:
        for d in detections:
            tid = d.track_id
            self._history[tid].append((now, d.norm_cx, d.norm_cy))
            if len(self._history[tid]) > self._MAX_HISTORY:
                self._history[tid] = self._history[tid][-self._MAX_HISTORY:]
            if tid not in self._first_seen:
                self._first_seen[tid] = now
            self._last_seen[tid] = now

    def _prune_stale(self, now: float, max_age: float = 5.0) -> None:
        stale = [k for k, v in self._last_seen.items() if now - v > max_age]
        for k in stale:
            self._history.pop(k, None)
            self._first_seen.pop(k, None)
            self._last_seen.pop(k, None)

    # ------------------------------------------------------------------ #
    # ML model (optional)
    # ------------------------------------------------------------------ #

    def _load_ml_model(self, path: str) -> None:
        if not _sklearn_available():
            return
        try:
            import pickle
            from pathlib import Path as _P

            p = _P(path)
            if p.exists():
                with open(p, "rb") as f:
                    self._ml_model = pickle.load(f)  # noqa: S301
        except Exception as exc:
            self._ml_model = None
            self._log_ml_warning(f"Failed to load ML model from {path}", exc, once_key=f"load:{path}")

    def save_ml_model(self, path: str) -> None:
        if self._ml_model is None or not _sklearn_available():
            return
        import pickle
        from pathlib import Path as _P

        p = _P(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "wb") as f:
            pickle.dump(self._ml_model, f)

    def train_ml_model(
        self, features_list: List[List[float]], labels: List[float]
    ) -> bool:
        """
        Train an MLP from user-labelled engagement data.
        features: [proximity, size, conf, class_score, speed, persistence, approach]
        labels: 0-1 threat score (1 = should engage, 0 = ignore)
        Returns True on success.
        """
        if not _sklearn_available() or len(features_list) < 10:
            return False
        try:
            from sklearn.neural_network import MLPRegressor  # type: ignore

            model = MLPRegressor(
                hidden_layer_sizes=(16, 8),
                max_iter=500,
                random_state=42,
            )
            model.fit(features_list, labels)
            self._ml_model = model
            return True
        except Exception as exc:
            self._log_ml_warning("ML model training failed", exc)
            return False
