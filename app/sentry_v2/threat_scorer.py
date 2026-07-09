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
    history_samples: int = 0
    heading_stability: float = 0.0


@dataclass
class MotionHistorySnapshot:
    """Recent motion metrics derived from the scorer's track history."""
    track_id: int
    window_s: float
    sample_count: int
    recent_motion_distance_px: float
    average_velocity_px_s: float
    motion_confidence: float
    stationary_duration_s: float
    last_motion_seen_s: float
    first_seen_s: float
    recent_motion_detected: bool

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

    def get_motion_history_snapshot(
        self,
        det: DetectedObject,
        timestamp: Optional[float] = None,
        *,
        window_s: float = 1.25,
    ) -> MotionHistorySnapshot:
        """Return recent motion metrics for a detection using scorer history."""
        now = timestamp or time.time()
        tid = int(det.track_id)
        history = list(self._history.get(tid, []) or [])
        first_seen = float(self._first_seen.get(tid, now))
        if not history:
            return MotionHistorySnapshot(
                track_id=tid,
                window_s=float(window_s),
                sample_count=0,
                recent_motion_distance_px=0.0,
                average_velocity_px_s=0.0,
                motion_confidence=0.0,
                stationary_duration_s=max(0.0, now - first_seen),
                last_motion_seen_s=first_seen,
                first_seen_s=first_seen,
                recent_motion_detected=False,
            )

        window = self._recent_motion_window(history, max_span_s=max(0.10, float(window_s)))
        frame_w = max(1.0, float(getattr(det, "frame_width", 640) or 640))
        frame_h = max(1.0, float(getattr(det, "frame_height", 480) or 480))
        segment_distances_px: List[float] = []
        segment_speeds_px_s: List[float] = []
        last_motion_seen = first_seen
        motion_threshold_px_s = max(1.5, min(frame_w, frame_h) * 0.01)

        for (t0, x0, y0), (t1, x1, y1) in zip(window, window[1:]):
            dt = max(0.001, float(t1 - t0))
            dx_px = (float(x1) - float(x0)) * frame_w
            dy_px = (float(y1) - float(y0)) * frame_h
            distance_px = math.hypot(dx_px, dy_px)
            speed_px_s = distance_px / dt
            segment_distances_px.append(distance_px)
            segment_speeds_px_s.append(speed_px_s)
            if speed_px_s >= motion_threshold_px_s:
                last_motion_seen = float(t1)

        recent_motion_distance_px = float(sum(segment_distances_px))
        window_dt = max(0.001, float(window[-1][0] - window[0][0]))
        average_velocity_px_s = recent_motion_distance_px / window_dt

        bbox_diag_px = math.hypot(float(det.bbox[2]), float(det.bbox[3]))
        distance_scale = max(10.0, bbox_diag_px * 0.22)
        velocity_scale = max(6.0, bbox_diag_px * 0.10)
        distance_score = max(0.0, min(1.0, recent_motion_distance_px / distance_scale))
        velocity_score = max(0.0, min(1.0, average_velocity_px_s / velocity_scale))
        sample_score = max(0.0, min(1.0, max(0, len(window) - 1) / 4.0))
        motion_confidence = max(0.0, min(1.0, (0.45 * distance_score) + (0.40 * velocity_score) + (0.15 * sample_score)))
        stationary_duration_s = max(0.0, now - float(last_motion_seen))

        return MotionHistorySnapshot(
            track_id=tid,
            window_s=float(window_s),
            sample_count=int(max(0, len(window) - 1)),
            recent_motion_distance_px=recent_motion_distance_px,
            average_velocity_px_s=average_velocity_px_s,
            motion_confidence=motion_confidence,
            stationary_duration_s=stationary_duration_s,
            last_motion_seen_s=float(last_motion_seen),
            first_seen_s=float(first_seen),
            recent_motion_detected=bool(
                recent_motion_distance_px >= distance_scale * 0.35
                or average_velocity_px_s >= velocity_scale * 0.35
                or motion_confidence >= 0.45
            ),
        )

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
        history_samples = len(hist)
        heading_stability = 0.0
        if len(hist) >= 2:
            recent_hist = self._recent_motion_window(hist)
            segments: List[Tuple[float, float]] = []
            norm_segments: List[Tuple[float, float]] = []
            for (t0, x0, y0), (t1, x1, y1) in zip(recent_hist, recent_hist[1:]):
                dt = max(0.001, t1 - t0)
                vx = (x1 - x0) / dt
                vy = (y1 - y0) / dt
                segments.append((vx, vy))
                seg_speed = math.sqrt(vx * vx + vy * vy)
                if seg_speed >= 0.02:
                    norm_segments.append((vx / seg_speed, vy / seg_speed))

            if segments:
                heading_x = sum(vx for vx, _ in segments) / float(len(segments))
                heading_y = sum(vy for _, vy in segments) / float(len(segments))
                speed = math.sqrt(heading_x * heading_x + heading_y * heading_y)

                start_t, start_x, start_y = recent_hist[0]
                end_t, end_x, end_y = recent_hist[-1]
                window_dt = max(0.001, end_t - start_t)
                dist_prev = math.sqrt((start_x - 0.5) ** 2 + (start_y - 0.5) ** 2)
                dist_now = math.sqrt((end_x - 0.5) ** 2 + (end_y - 0.5) ** 2)
                approach_rate = (dist_prev - dist_now) / window_dt

            if norm_segments:
                mean_nx = sum(vx for vx, _ in norm_segments) / float(len(norm_segments))
                mean_ny = sum(vy for _, vy in norm_segments) / float(len(norm_segments))
                heading_stability = max(0.0, min(1.0, math.sqrt((mean_nx * mean_nx) + (mean_ny * mean_ny))))

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
                pred_result = self._ml_model.predict([features])  # type: ignore[union-attr]
                if len(pred_result) == 0:
                    raise ValueError("ML model returned empty prediction array")
                ml_score = float(pred_result[0])
                if math.isnan(ml_score) or math.isinf(ml_score):
                    raise ValueError(f"ML score invalid: {ml_score}")
                ml_score = max(0.0, min(1.0, ml_score))
                threat = 0.6 * threat + 0.4 * ml_score
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
            history_samples=history_samples,
            heading_stability=heading_stability,
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

    def _recent_motion_window(
        self,
        history: List[Tuple[float, float, float]],
        *,
        max_points: int = 5,
        max_span_s: float = 0.45,
    ) -> List[Tuple[float, float, float]]:
        if len(history) <= 2:
            return list(history)
        window = list(history[-max_points:])
        while len(window) > 2 and (window[-1][0] - window[0][0]) > max_span_s:
            window.pop(0)
        return window

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
