"""
SMART TRACKING ENHANCEMENT MODULE
==================================
Provides advanced tracking features to improve target following:
- Detection persistence (maintains target through brief detection gaps)
- Centroid history and smoothing (reduces jitter)
- Velocity prediction (predicts where target should be)
- Detection confidence scoring (improves detection quality)
- Re-detection hysteresis (prevents rapid on/off toggling)

Usage:
    tracker = SmartTracker()
    
    # Each frame, call update with current detections
    smoothed_boxes, confidence = tracker.update_detections(boxes, frame_width, frame_height)
    
    # Or use individual components
    tracker.update_motion_history(centroid_x, centroid_y)
    predicted_x, predicted_y = tracker.predict_position()
"""

import time
import numpy as np
from collections import deque


class SmartTracker:
    """
    Intelligent tracker that maintains detection continuity and smooth following.
    """
    
    def __init__(self, 
                 max_loss_frames=5,           # How many frames to hold target before considering lost
                 history_size=10,             # How many recent centroids to keep for smoothing
                 confidence_threshold=0.6,    # Minimum confidence to accept detection (0-1)
                 prediction_enabled=True,     # Use motion prediction for lost targets
                 smoothing_factor=0.7):       # 0=instant, 1=no movement. Higher = smoother
        """
        Initialize smart tracker.
        
        Args:
            max_loss_frames: Frames to hold position before considering target lost
            history_size: Number of frames to keep in centroid history
            confidence_threshold: Minimum confidence score (0-1) for detection
            prediction_enabled: Whether to predict target motion
            smoothing_factor: Exponential smoothing factor for jitter reduction
        """
        self.max_loss_frames = max_loss_frames
        self.history_size = history_size
        self.confidence_threshold = confidence_threshold
        self.prediction_enabled = prediction_enabled
        self.smoothing_factor = smoothing_factor
        
        # State tracking
        self.last_centroids = deque(maxlen=history_size)  # Recent centroid positions
        self.last_valid_detection = None                  # Last known valid detection
        self.frames_since_detection = 0                   # Frames without detection
        self.last_detection_time = 0                      # Timestamp of last detection
        self.detection_confidence = 0.0                   # Current detection confidence (0-1)
        self.velocity_x = 0.0                             # Estimated X velocity
        self.velocity_y = 0.0                             # Estimated Y velocity
        self.smoothed_centroid = None                     # Smoothed centroid position
        
        # Statistics
        self.total_detections = 0
        self.total_predictions_used = 0
        self.total_losses = 0
        
    def update_detections(self, boxes, frame_width=640, frame_height=480):
        """
        Process detected boxes and return improved/smoothed detections.
        
        Args:
            boxes: List of (x, y, w, h) tuples from detector
            frame_width: Frame width in pixels
            frame_height: Frame height in pixels
            
        Returns:
            Tuple of (improved_boxes, confidence_score)
            - improved_boxes: List of smoothed bounding boxes
            - confidence_score: 0.0-1.0 indicating how confident in detections
        """
        current_time = time.time()
        
        if boxes and len(boxes) > 0:
            # DETECTION RECEIVED
            self.frames_since_detection = 0
            self.last_detection_time = current_time
            self.total_detections += 1
            
            # Select largest box (most likely to be the actual target)
            try:
                largest_box = max(boxes, key=lambda b: b[2] * b[3])
                x, y, w, h = largest_box
            except Exception:
                x, y, w, h = boxes[0]
            
            # Calculate centroid
            cx = x + w // 2
            cy = y + h // 2
            
            # Add to history for smoothing
            self.last_centroids.append((cx, cy))
            
            # Calculate velocity from historical data
            if len(self.last_centroids) >= 2:
                prev_cx, prev_cy = self.last_centroids[-2]
                self.velocity_x = cx - prev_cx
                self.velocity_y = cy - prev_cy
            
            # Calculate detection confidence based on consistency
            self.detection_confidence = self._calculate_confidence()
            
            # Apply smoothing to reduce jitter
            smoothed_cx, smoothed_cy = self._smooth_centroid(cx, cy)
            self.smoothed_centroid = (smoothed_cx, smoothed_cy)
            
            # Create smoothed box
            improved_boxes = [(x - (cx - int(smoothed_cx)), 
                             y - (cy - int(smoothed_cy)), 
                             w, h)]
            
            self.last_valid_detection = (int(smoothed_cx), int(smoothed_cy), w, h)
            
            return improved_boxes, self.detection_confidence
        
        else:
            # NO DETECTION THIS FRAME
            self.frames_since_detection += 1
            
            # Check if we should use prediction or hold last known position
            if self.frames_since_detection <= self.max_loss_frames:
                # Within hold window - use prediction or last position
                if self.prediction_enabled and self.last_valid_detection is not None:
                    # Predict where target should be
                    predicted_boxes = self._predict_position()
                    if predicted_boxes:
                        self.total_predictions_used += 1
                        # Slightly lower confidence for predicted boxes
                        return predicted_boxes, self.detection_confidence * 0.7
                
                elif self.last_valid_detection is not None:
                    # No prediction - just hold last position
                    return [self.last_valid_detection], self.detection_confidence * 0.8
            
            else:
                # Loss exceeded threshold - full detection loss
                if self.detection_confidence > 0.0:  # First time we're reporting loss
                    self.total_losses += 1
                self.detection_confidence = 0.0
                self.last_centroids.clear()
                self.velocity_x = 0.0
                self.velocity_y = 0.0
            
            return [], self.detection_confidence
    
    def _calculate_confidence(self):
        """
        Calculate detection confidence based on centroid stability.
        
        Returns:
            Confidence score from 0.0 to 1.0
        """
        if len(self.last_centroids) < 2:
            return 0.5  # Low confidence with minimal history
        
        # Calculate variance in recent positions
        recent = list(self.last_centroids)[-5:]  # Last 5 points
        if len(recent) < 2:
            return 0.5
        
        positions = np.array(recent)
        distances = np.linalg.norm(np.diff(positions, axis=0), axis=1)
        mean_distance = np.mean(distances) if len(distances) > 0 else 0
        
        # Normalize: small movements = high confidence, large = lower
        # Typical object should move < 30 pixels per frame
        max_expected_movement = 50.0
        normalized_distance = np.clip(mean_distance / max_expected_movement, 0, 1)
        
        # Confidence = 1 - normalized_distance (smooth movement = high confidence)
        base_confidence = 1.0 - normalized_distance
        
        # Boost with historical consistency
        history_boost = min(len(self.last_centroids) / 10.0, 0.2)  # Up to +0.2 bonus
        
        return np.clip(base_confidence + history_boost, 0.0, 1.0)
    
    def _smooth_centroid(self, cx, cy):
        """
        Apply exponential smoothing to reduce jitter.
        
        Args:
            cx, cy: Current centroid position
            
        Returns:
            Tuple of (smoothed_cx, smoothed_cy)
        """
        if self.smoothed_centroid is None:
            return float(cx), float(cy)
        
        prev_cx, prev_cy = self.smoothed_centroid
        
        # Exponential smoothing: smooth_new = α * current + (1 - α) * smooth_old
        # Higher smoothing_factor = smoother (more lag)
        smoothed_cx = (1 - self.smoothing_factor) * cx + self.smoothing_factor * prev_cx
        smoothed_cy = (1 - self.smoothing_factor) * cy + self.smoothing_factor * prev_cy
        
        return smoothed_cx, smoothed_cy
    
    def _predict_position(self):
        """
        Predict where target should be based on velocity.
        
        Returns:
            List with predicted box or empty if can't predict
        """
        if self.last_valid_detection is None:
            return []
        
        cx, cy, w, h = self.last_valid_detection
        
        # Predict next position based on velocity
        predicted_cx = cx + self.velocity_x * 0.8  # 0.8 factor for slight damping
        predicted_cy = cy + self.velocity_y * 0.8
        
        # Create predicted box
        predicted_x = int(predicted_cx - w // 2)
        predicted_y = int(predicted_cy - h // 2)
        
        return [(predicted_x, predicted_y, w, h)]
    
    def update_motion_history(self, cx, cy):
        """
        Manually add a position to motion history.
        Useful for integrating with servo feedback.
        
        Args:
            cx: Centroid X position
            cy: Centroid Y position
        """
        self.last_centroids.append((cx, cy))
        
        if len(self.last_centroids) >= 2:
            prev_cx, prev_cy = self.last_centroids[-2]
            self.velocity_x = cx - prev_cx
            self.velocity_y = cy - prev_cy
    
    def predict_position(self):
        """
        Get predicted target position based on motion history.
        
        Returns:
            Tuple of (predicted_x, predicted_y, confidence)
        """
        if self.last_valid_detection is None:
            return None, None, 0.0
        
        cx, cy, w, h = self.last_valid_detection
        predicted_cx = cx + self.velocity_x
        predicted_cy = cy + self.velocity_y
        
        return predicted_cx, predicted_cy, self.detection_confidence
    
    def reset(self):
        """Reset all tracking state."""
        self.last_centroids.clear()
        self.last_valid_detection = None
        self.frames_since_detection = 0
        self.last_detection_time = 0
        self.detection_confidence = 0.0
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.smoothed_centroid = None
    
    def get_statistics(self):
        """
        Get tracking statistics.
        
        Returns:
            Dict with tracking metrics
        """
        return {
            'total_detections': self.total_detections,
            'total_predictions_used': self.total_predictions_used,
            'total_losses': self.total_losses,
            'current_confidence': self.detection_confidence,
            'frames_since_detection': self.frames_since_detection,
            'velocity': (self.velocity_x, self.velocity_y),
            'history_length': len(self.last_centroids),
        }
    
    def log_statistics(self):
        """Get formatted statistics for logging."""
        stats = self.get_statistics()
        return (f"[TRACKER] detections={stats['total_detections']} "
                f"predictions={stats['total_predictions_used']} "
                f"losses={stats['total_losses']} "
                f"confidence={stats['current_confidence']:.2f} "
                f"velocity=({stats['velocity'][0]:.1f},{stats['velocity'][1]:.1f})")


class DetectionQualityFilter:
    """
    Filters detections to improve quality and reduce false positives.
    """
    
    def __init__(self, 
                 min_area=100,           # Minimum box area (pixels²)
                 max_area=None,          # Maximum box area (None = unlimited)
                 min_aspect_ratio=0.1,   # Minimum width/height ratio
                 max_aspect_ratio=10.0,  # Maximum width/height ratio
                 edge_buffer=20):        # Pixel buffer from frame edges
        """
        Initialize quality filter.
        
        Args:
            min_area: Minimum bounding box area in pixels
            max_area: Maximum bounding box area (None to disable)
            min_aspect_ratio: Minimum width/height ratio
            max_aspect_ratio: Maximum width/height ratio
            edge_buffer: Reject detections too close to frame edges
        """
        self.min_area = min_area
        self.max_area = max_area
        self.min_aspect_ratio = min_aspect_ratio
        self.max_aspect_ratio = max_aspect_ratio
        self.edge_buffer = edge_buffer
    
    def filter_boxes(self, boxes, frame_width=640, frame_height=480):
        """
        Filter out poor quality detections.
        
        Args:
            boxes: List of (x, y, w, h) tuples
            frame_width: Frame width in pixels
            frame_height: Frame height in pixels
            
        Returns:
            Filtered list of boxes
        """
        filtered = []
        
        for box in boxes:
            try:
                x, y, w, h = box
                w, h = max(1, int(w)), max(1, int(h))
                
                # Check minimum area
                area = w * h
                if area < self.min_area:
                    continue
                
                # Check maximum area
                if self.max_area is not None and area > self.max_area:
                    continue
                
                # Check aspect ratio
                aspect_ratio = float(w) / float(h) if h > 0 else 1.0
                if aspect_ratio < self.min_aspect_ratio or aspect_ratio > self.max_aspect_ratio:
                    continue
                
                # Check edge buffer
                if (x < self.edge_buffer or 
                    y < self.edge_buffer or
                    x + w > frame_width - self.edge_buffer or
                    y + h > frame_height - self.edge_buffer):
                    continue  # Too close to edge
                
                filtered.append((x, y, w, h))
            
            except Exception:
                continue
        
        return filtered
