from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from .target_filter import DetectedObject


@dataclass
class _TrackState:
    track_id: int
    class_name: str
    bbox: Tuple[int, int, int, int]
    center_x: float
    center_y: float
    last_seen: float


class SimpleBBoxTracker:
    """Greedy bbox/centroid tracker for stable Smart Sentry track IDs."""

    def __init__(self) -> None:
        self._tracks: Dict[int, _TrackState] = {}
        self._next_track_id: int = 1
        self.max_match_distance_px: float = 220.0
        self.max_track_age_s: float = 1.8

    def reset(self) -> None:
        self._tracks.clear()
        self._next_track_id = 1

    def assign_tracks(
        self,
        detections: List[DetectedObject],
        timestamp: float,
    ) -> List[DetectedObject]:
        if not detections:
            self._prune(timestamp)
            return []

        unmatched_track_ids = list(self._tracks.keys())
        unmatched_det_indices = list(range(len(detections)))
        matches: List[Tuple[int, int]] = []

        while unmatched_track_ids and unmatched_det_indices:
            best_pair: Optional[Tuple[int, int]] = None
            best_cost = float("inf")

            for track_id in unmatched_track_ids:
                track = self._tracks[track_id]
                for det_idx in unmatched_det_indices:
                    det = detections[det_idx]
                    if det.class_name != track.class_name:
                        continue
                    dist = math.hypot(det.center_x - track.center_x, det.center_y - track.center_y)
                    if dist > self._match_distance_limit(track, det):
                        continue
                    iou = self._bbox_iou(det.bbox, track.bbox)
                    area_cost = abs(self._bbox_area(det.bbox) - self._bbox_area(track.bbox)) / max(
                        1.0,
                        float(max(self._bbox_area(det.bbox), self._bbox_area(track.bbox))),
                    )
                    cost = dist - (iou * 35.0) + (area_cost * 25.0)
                    if cost < best_cost:
                        best_cost = cost
                        best_pair = (track_id, det_idx)

            if best_pair is None:
                break

            matches.append(best_pair)
            unmatched_track_ids.remove(best_pair[0])
            unmatched_det_indices.remove(best_pair[1])

        for track_id, det_idx in matches:
            det = detections[det_idx]
            det.track_id = track_id
            self._tracks[track_id] = _TrackState(
                track_id=track_id,
                class_name=det.class_name,
                bbox=det.bbox,
                center_x=det.center_x,
                center_y=det.center_y,
                last_seen=timestamp,
            )

        for det_idx in unmatched_det_indices:
            det = detections[det_idx]
            track_id = self._next_track_id
            self._next_track_id += 1
            det.track_id = track_id
            self._tracks[track_id] = _TrackState(
                track_id=track_id,
                class_name=det.class_name,
                bbox=det.bbox,
                center_x=det.center_x,
                center_y=det.center_y,
                last_seen=timestamp,
            )

        self._prune(timestamp)
        return detections

    def _prune(self, timestamp: float) -> None:
        stale_ids = [
            track_id
            for track_id, track in self._tracks.items()
            if (timestamp - track.last_seen) > self.max_track_age_s
        ]
        for track_id in stale_ids:
            self._tracks.pop(track_id, None)

    @staticmethod
    def _bbox_iou(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
        ax1, ay1, aw, ah = a
        bx1, by1, bw, bh = b
        ax2, ay2 = ax1 + aw, ay1 + ah
        bx2, by2 = bx1 + bw, by1 + bh

        ix1 = max(ax1, bx1)
        iy1 = max(ay1, by1)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iw = max(0, ix2 - ix1)
        ih = max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0

        area_a = aw * ah
        area_b = bw * bh
        union = max(1, area_a + area_b - inter)
        return inter / union

    def _match_distance_limit(self, track: _TrackState, det: DetectedObject) -> float:
        track_diag = math.hypot(float(track.bbox[2]), float(track.bbox[3]))
        det_diag = math.hypot(float(det.bbox[2]), float(det.bbox[3]))
        dynamic_limit = 0.60 * max(track_diag, det_diag)
        return max(float(self.max_match_distance_px), dynamic_limit)

    @staticmethod
    def _bbox_area(bbox: Tuple[int, int, int, int]) -> float:
        return float(max(1, bbox[2] * bbox[3]))