"""Scene Memory — passive class-prior accumulator.

Tracks per-class detection statistics across a sentry session so the
engagement planner can give a mild preference to classes that have been
reliably observed before.

Usage:
    memory = SceneMemory()
    memory.record(det, now)                      # once per detection per frame
    weight = memory.get_class_weight(cls, now)   # 0.0–1.0 recency-weighted
    ordered = memory.order_candidates_by_prior(targets, now)
"""
from __future__ import annotations

from typing import Dict, List, Optional, Tuple


class SceneMemory:
    """Passive, bounded session-scoped class-prior collector.

    Accumulates per-class hit counts and average positions from live
    detections.  All entries expire after *ttl_s* seconds without a new
    observation (default 90 s) to prevent stale-session bias across
    very different target environments.
    """

    _MAX_SAMPLE_COUNT: int = 200  # cap per class to avoid overflow in long sessions

    def __init__(self, ttl_s: float = 90.0) -> None:
        self._ttl_s: float = max(10.0, float(ttl_s))
        # Keyed by lower-cased class_name string.
        self._class_stats: Dict[str, Dict] = {}

    # ------------------------------------------------------------------ #
    # Recording
    # ------------------------------------------------------------------ #

    def record(self, det: object, now: float) -> None:
        """Record a single detection observation.

        Accepts any DetectedObject-compatible object with ``class_name``,
        ``norm_cx``, ``norm_cy``, and ``confidence`` attributes.
        """
        class_name = str(getattr(det, "class_name", "") or "").strip().lower()
        if not class_name:
            return
        if class_name not in self._class_stats:
            self._class_stats[class_name] = {
                "hit_count": 0,
                "last_seen": 0.0,
                "norm_cx_sum": 0.0,
                "norm_cy_sum": 0.0,
                "confidence_sum": 0.0,
                "sample_count": 0,
            }
        entry = self._class_stats[class_name]
        entry["hit_count"] = int(entry["hit_count"]) + 1
        entry["last_seen"] = float(now)
        n = int(entry["sample_count"])
        if n < self._MAX_SAMPLE_COUNT:
            entry["norm_cx_sum"] = (
                float(entry["norm_cx_sum"]) + float(getattr(det, "norm_cx", 0.5) or 0.5)
            )
            entry["norm_cy_sum"] = (
                float(entry["norm_cy_sum"]) + float(getattr(det, "norm_cy", 0.5) or 0.5)
            )
            entry["confidence_sum"] = (
                float(entry["confidence_sum"]) + float(getattr(det, "confidence", 0.5) or 0.5)
            )
            entry["sample_count"] = n + 1

    # ------------------------------------------------------------------ #
    # Query
    # ------------------------------------------------------------------ #

    def get_class_weight(self, class_name: str, now: float) -> float:
        """Return a bias weight [0.0–1.0] for a class based on prior observations.

        0.0 — class never observed or entry fully expired.
        1.0 — class was seen very recently and many times.

        The weight combines a linear recency decay (reaches 0 at ttl_s) with a
        count saturation factor that approaches 1.0 asymptotically, reaching
        ~0.83 after 10 hits.  Small weights ensure the bias never overrides a
        meaningful threat-score difference between targets.
        """
        entry = self._class_stats.get(str(class_name or "").strip().lower())
        if entry is None:
            return 0.0
        age_s = max(0.0, float(now) - float(entry["last_seen"]))
        if age_s > self._ttl_s:
            return 0.0
        recency = max(0.0, 1.0 - (age_s / self._ttl_s))
        count = min(1.0, float(int(entry["hit_count"])) / 12.0)
        return float(recency * count)

    def get_avg_position(self, class_name: str) -> Optional[Tuple[float, float]]:
        """Return average normalised (cx, cy) for a class, or None if unknown."""
        entry = self._class_stats.get(str(class_name or "").strip().lower())
        if entry is None or int(entry["sample_count"]) == 0:
            return None
        n = float(int(entry["sample_count"]))
        return (
            float(entry["norm_cx_sum"]) / n,
            float(entry["norm_cy_sum"]) / n,
        )

    def snapshot(self) -> Dict[str, Dict]:
        """Return a shallow copy of all current class stats (for diagnostics)."""
        return {k: dict(v) for k, v in self._class_stats.items()}

    # ------------------------------------------------------------------ #
    # Ordering helpers
    # ------------------------------------------------------------------ #

    def order_candidates_by_prior(
        self,
        candidates: list,
        now: float,
        *,
        bias_strength: float = 0.20,
    ) -> list:
        """Re-order *candidates* so scene-prior-favoured classes sort first.

        The bias is intentionally small (default 20 % threat-score multiplier)
        so it only breaks near-ties among similar-threat targets and never
        overrides a meaningful threat-score differential.

        Works with ``TrackedTarget`` objects (``t.threat_score``, ``t.det.class_name``)
        and any compatible structure.
        """
        if len(candidates) <= 1:
            return list(candidates)

        def _key(t: object) -> float:
            # Support both TrackedTarget (t.threat_score) and flat structures.
            threat = float(
                getattr(t, "threat_score", None)
                or 0.0
            )
            det = getattr(t, "det", t)
            class_name = str(getattr(det, "class_name", "") or "")
            w = self.get_class_weight(class_name, now)
            return threat * (1.0 + float(bias_strength) * w)

        return sorted(candidates, key=_key, reverse=True)

    # ------------------------------------------------------------------ #
    # Maintenance
    # ------------------------------------------------------------------ #

    def prune_stale(self, now: float) -> None:
        """Remove entries whose TTL has been exceeded twice over."""
        cutoff = float(now) - self._ttl_s * 2.0
        expired = [k for k, v in self._class_stats.items() if float(v["last_seen"]) < cutoff]
        for k in expired:
            del self._class_stats[k]

    def clear(self) -> None:
        """Discard all accumulated state (e.g. on explicit operator reset)."""
        self._class_stats.clear()
