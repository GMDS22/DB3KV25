"""
ByteTrack Object Tracker - Bundled implementation for Sentry Mode.

This is a simplified implementation of ByteTrack algorithm for multi-object tracking.
Based on the original ByteTrack paper: https://arxiv.org/abs/2110.06864

ByteTrack achieves robust tracking by associating both high and low confidence
detections, which helps maintain tracks through occlusion and detection failures.
"""

import numpy as np
from typing import List, Tuple, Optional
from dataclasses import dataclass, field
from collections import deque


@dataclass
class TrackState:
    """State for a tracked object."""
    TENTATIVE = 1    # New track, not yet confirmed
    CONFIRMED = 2    # Confirmed track
    DELETED = 3      # Track marked for deletion


@dataclass
class STrack:
    """Single object track (Simple Track)."""
    track_id: int
    bbox: np.ndarray              # [x, y, w, h]
    score: float
    state: int = TrackState.TENTATIVE
    frame_id: int = 0
    start_frame: int = 0
    tracklet_len: int = 0
    is_activated: bool = False
    
    # Kalman filter state
    mean: Optional[np.ndarray] = None   # [x, y, a, h, vx, vy, va, vh]
    covariance: Optional[np.ndarray] = None
    
    # History
    history: deque = field(default_factory=lambda: deque(maxlen=30))
    
    def __post_init__(self):
        if self.history is None:
            self.history = deque(maxlen=30)
    
    @property
    def tlwh(self) -> np.ndarray:
        """Get current bounding box in top-left-width-height format."""
        if self.mean is not None:
            x, y, a, h = self.mean[:4]
            w = a * h
            return np.array([x - w/2, y - h/2, w, h])
        return self.bbox.copy()
    
    @property
    def tlbr(self) -> np.ndarray:
        """Get current bounding box in top-left-bottom-right format."""
        tlwh = self.tlwh
        return np.array([tlwh[0], tlwh[1], tlwh[0] + tlwh[2], tlwh[1] + tlwh[3]])
    
    @property
    def xywh(self) -> np.ndarray:
        """Get current bounding box in center-width-height format."""
        tlwh = self.tlwh
        return np.array([tlwh[0] + tlwh[2]/2, tlwh[1] + tlwh[3]/2, tlwh[2], tlwh[3]])
    
    def activate(self, frame_id: int, track_id: int) -> None:
        """Activate a new track."""
        self.track_id = track_id
        self.frame_id = frame_id
        self.start_frame = frame_id
        self.tracklet_len = 0
        self.is_activated = True
        self.state = TrackState.CONFIRMED
    
    def re_activate(self, new_track: 'STrack', frame_id: int) -> None:
        """Re-activate a lost track with new detection."""
        self.bbox = new_track.bbox.copy()
        self.score = new_track.score
        self.frame_id = frame_id
        self.tracklet_len = 0
        self.is_activated = True
        self.state = TrackState.CONFIRMED
    
    def update(self, new_track: 'STrack', frame_id: int) -> None:
        """Update track with new detection."""
        self.bbox = new_track.bbox.copy()
        self.score = new_track.score
        self.frame_id = frame_id
        self.tracklet_len += 1
        self.is_activated = True
        
        # Save to history
        self.history.append(self.tlwh.copy())
    
    def mark_lost(self) -> None:
        """Mark track as lost."""
        self.state = TrackState.TENTATIVE
    
    def mark_removed(self) -> None:
        """Mark track for removal."""
        self.state = TrackState.DELETED


class ByteTracker:
    """
    ByteTrack multi-object tracker.
    
    Key features:
    - Uses both high and low confidence detections
    - Two-stage association: first high-conf, then low-conf with remaining tracks
    - Simple and efficient IoU-based matching
    
    Usage:
        tracker = ByteTracker()
        
        for frame in video:
            detections = detector.detect(frame)  # [(x, y, w, h, score), ...]
            tracks = tracker.update(detections)  # [(track_id, x, y, w, h), ...]
    """
    
    def __init__(self,
                 track_thresh: float = 0.5,
                 track_buffer: int = 30,
                 match_thresh: float = 0.8,
                 min_box_area: int = 100):
        """
        Initialize ByteTracker.
        
        Args:
            track_thresh: Confidence threshold for "high confidence" detections
            track_buffer: Number of frames to keep lost tracks
            match_thresh: IoU threshold for matching
            min_box_area: Minimum detection box area to consider
        """
        self.track_thresh = track_thresh
        self.track_buffer = track_buffer
        self.match_thresh = match_thresh
        self.min_box_area = min_box_area
        
        # Track storage
        self.tracked_stracks: List[STrack] = []  # Confirmed tracks
        self.lost_stracks: List[STrack] = []     # Lost but not removed
        self.removed_stracks: List[STrack] = []  # Removed tracks
        
        # Frame counter
        self.frame_id: int = 0
        
        # Track ID counter
        self._next_id: int = 1
    
    def update(self, detections: List[Tuple[int, int, int, int, float]]) -> List[Tuple[int, int, int, int, int]]:
        """
        Update tracker with new detections.
        
        Args:
            detections: List of (x, y, w, h, score) detections
            
        Returns:
            List of (track_id, x, y, w, h) for active tracks
        """
        self.frame_id += 1
        
        # Convert detections to STracks
        if len(detections) == 0:
            det_stracks = []
        else:
            det_stracks = []
            for det in detections:
                x, y, w, h = det[:4]
                score = det[4] if len(det) > 4 else 1.0
                
                # Filter by minimum area
                if w * h < self.min_box_area:
                    continue
                
                strack = STrack(
                    track_id=-1,
                    bbox=np.array([x, y, w, h], dtype=float),
                    score=score
                )
                det_stracks.append(strack)
        
        # Separate detections by confidence
        high_conf = [t for t in det_stracks if t.score >= self.track_thresh]
        low_conf = [t for t in det_stracks if t.score < self.track_thresh]
        
        # Get existing tracks
        unconfirmed = [t for t in self.tracked_stracks if not t.is_activated]
        tracked = [t for t in self.tracked_stracks if t.is_activated]
        
        # Combine tracked and lost tracks for matching
        strack_pool = tracked + self.lost_stracks
        
        # First association: high confidence detections with tracked stracks
        if len(strack_pool) > 0 and len(high_conf) > 0:
            costs = self._iou_distance(strack_pool, high_conf)
            matches, u_track, u_detection = self._linear_assignment(
                costs, thresh=self.match_thresh
            )
            
            for itracked, idet in matches:
                track = strack_pool[itracked]
                det = high_conf[idet]
                
                if track.state == TrackState.CONFIRMED:
                    track.update(det, self.frame_id)
                else:
                    track.re_activate(det, self.frame_id)
            
            # Update unmatched track indices for second stage
            remaining_tracks = [strack_pool[i] for i in u_track]
            remaining_dets_high = [high_conf[i] for i in u_detection]
        else:
            remaining_tracks = strack_pool
            remaining_dets_high = high_conf
        
        # Second association: low confidence detections with remaining tracks
        remaining_tracked = [t for t in remaining_tracks if t in tracked]
        
        if len(remaining_tracked) > 0 and len(low_conf) > 0:
            costs = self._iou_distance(remaining_tracked, low_conf)
            matches, u_track2, _ = self._linear_assignment(
                costs, thresh=0.5  # Lower threshold for low-conf
            )
            
            for itracked, idet in matches:
                track = remaining_tracked[itracked]
                det = low_conf[idet]
                track.update(det, self.frame_id)
                remaining_tracks.remove(track)
        
        # Mark remaining tracks as lost
        for track in remaining_tracks:
            if track.state != TrackState.DELETED:
                track.mark_lost()
        
        # Third association: unconfirmed tracks with remaining high-conf detections
        if len(unconfirmed) > 0 and len(remaining_dets_high) > 0:
            costs = self._iou_distance(unconfirmed, remaining_dets_high)
            matches, u_unconf, u_det3 = self._linear_assignment(
                costs, thresh=0.7
            )
            
            for itracked, idet in matches:
                track = unconfirmed[itracked]
                det = remaining_dets_high[idet]
                track.update(det, self.frame_id)
            
            for i in u_unconf:
                track = unconfirmed[i]
                track.mark_removed()
            
            # New detections that didn't match
            remaining_dets_high = [remaining_dets_high[i] for i in u_det3]
        
        # Create new tracks from unmatched high-conf detections
        for det in remaining_dets_high:
            if det.score >= self.track_thresh:
                det.activate(self.frame_id, self._next_id)
                self._next_id += 1
                self.tracked_stracks.append(det)
        
        # Remove dead tracks
        self.tracked_stracks = [t for t in self.tracked_stracks 
                                if t.state != TrackState.DELETED]
        
        # Update lost tracks
        self.lost_stracks = [t for t in self.tracked_stracks 
                            if t.frame_id < self.frame_id - 1]
        self.tracked_stracks = [t for t in self.tracked_stracks 
                               if t.frame_id >= self.frame_id - 1]
        
        # Remove tracks lost for too long
        self.lost_stracks = [t for t in self.lost_stracks
                            if self.frame_id - t.frame_id <= self.track_buffer]
        
        # Output active tracks
        output = []
        for track in self.tracked_stracks:
            if track.is_activated:
                bbox = track.tlwh
                output.append((
                    track.track_id,
                    int(bbox[0]),
                    int(bbox[1]),
                    int(bbox[2]),
                    int(bbox[3])
                ))
        
        return output
    
    def _iou_distance(self, tracks: List[STrack], 
                      detections: List[STrack]) -> np.ndarray:
        """
        Calculate IoU distance matrix between tracks and detections.
        
        Returns:
            Cost matrix where lower = better match
        """
        n_tracks = len(tracks)
        n_dets = len(detections)
        
        if n_tracks == 0 or n_dets == 0:
            return np.zeros((n_tracks, n_dets))
        
        # Get bounding boxes
        track_boxes = np.array([t.tlbr for t in tracks])
        det_boxes = np.array([d.tlbr for d in detections])
        
        # Calculate IoU
        ious = self._box_iou(track_boxes, det_boxes)
        
        # Convert to cost (1 - IoU)
        return 1.0 - ious
    
    def _box_iou(self, boxes1: np.ndarray, boxes2: np.ndarray) -> np.ndarray:
        """Calculate IoU between two sets of boxes."""
        n1 = boxes1.shape[0]
        n2 = boxes2.shape[0]
        
        ious = np.zeros((n1, n2))
        
        for i in range(n1):
            for j in range(n2):
                box1 = boxes1[i]
                box2 = boxes2[j]
                
                # Intersection
                x1 = max(box1[0], box2[0])
                y1 = max(box1[1], box2[1])
                x2 = min(box1[2], box2[2])
                y2 = min(box1[3], box2[3])
                
                w = max(0, x2 - x1)
                h = max(0, y2 - y1)
                inter = w * h
                
                # Union
                area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
                area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
                union = area1 + area2 - inter
                
                if union > 0:
                    ious[i, j] = inter / union
        
        return ious
    
    def _linear_assignment(self, cost_matrix: np.ndarray, 
                           thresh: float) -> Tuple[List[Tuple[int, int]], 
                                                   List[int], List[int]]:
        """
        Solve linear assignment problem using greedy algorithm.
        
        For optimal results, use scipy.optimize.linear_sum_assignment,
        but this greedy version is faster and works well for tracking.
        
        Returns:
            matches: List of (track_idx, det_idx) pairs
            unmatched_tracks: List of unmatched track indices
            unmatched_dets: List of unmatched detection indices
        """
        if cost_matrix.size == 0:
            return [], list(range(cost_matrix.shape[0])), list(range(cost_matrix.shape[1]))
        
        n_rows, n_cols = cost_matrix.shape
        matches = []
        unmatched_rows = set(range(n_rows))
        unmatched_cols = set(range(n_cols))
        
        # Greedy matching: always pick the best available match
        costs_flat = cost_matrix.flatten()
        indices = np.argsort(costs_flat)
        
        for idx in indices:
            i = idx // n_cols
            j = idx % n_cols
            
            if i in unmatched_rows and j in unmatched_cols:
                if cost_matrix[i, j] < thresh:
                    matches.append((i, j))
                    unmatched_rows.discard(i)
                    unmatched_cols.discard(j)
        
        return matches, list(unmatched_rows), list(unmatched_cols)
    
    def reset(self) -> None:
        """Reset tracker state."""
        self.tracked_stracks.clear()
        self.lost_stracks.clear()
        self.removed_stracks.clear()
        self.frame_id = 0
        self._next_id = 1


# Factory function for creating tracker
def create_tracker(track_thresh: float = 0.5,
                   track_buffer: int = 30,
                   match_thresh: float = 0.8) -> ByteTracker:
    """
    Create a ByteTracker instance.
    
    Args:
        track_thresh: Confidence threshold for high-confidence detections
        track_buffer: Frames to keep lost tracks
        match_thresh: IoU threshold for matching
        
    Returns:
        Configured ByteTracker instance
    """
    return ByteTracker(
        track_thresh=track_thresh,
        track_buffer=track_buffer,
        match_thresh=match_thresh
    )
