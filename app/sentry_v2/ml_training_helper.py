"""
Smart Sentry v2 — ML Training Helper

Manages engagement logging and model training.
Collects data from user engagement decisions and trains the ML scorer.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional, Dict, Any
import time


@dataclass
class EngagementRecord:
    """Single engagement decision logged for training."""
    timestamp: float
    proximity: float          # 0-1, distance from center
    size: float               # 0-1, object size
    confidence: float         # 0-1, YOLO confidence
    class_score: float        # 0-1, class priority normalized
    speed: float              # 0-1, movement speed
    persistence: float        # 0-1, time in frame
    approach_rate: float      # 0-1, approaching center
    was_engaged: bool         # True = fired at this target, False = ignored
    class_name: str           # e.g., "person", "car"
    track_id: int             # for grouping consecutive decisions
    
    def to_feature_vector(self) -> List[float]:
        """Return as feature vector for ML training."""
        return [
            self.proximity,
            self.size,
            self.confidence,
            self.class_score,
            self.speed,
            self.persistence,
            self.approach_rate,
        ]


class MLTrainingLogger:
    """
    Logs engagement decisions for later ML model training.
    
    Usage:
        logger = MLTrainingLogger()
        # ... during engagement ...
        logger.log_engagement(features..., was_engaged=True)
        # ... later ...
        records = logger.get_all_records()
        train_ml_model(records)
    """
    
    def __init__(self, max_records: int = 10000):
        self.max_records = max_records
        self.records: List[EngagementRecord] = []
    
    def log_engagement(
        self,
        proximity: float,
        size: float,
        confidence: float,
        class_score: float,
        speed: float,
        persistence: float,
        approach_rate: float,
        was_engaged: bool,
        class_name: str = "unknown",
        track_id: int = 0,
    ) -> None:
        """Log a single engagement decision."""
        record = EngagementRecord(
            timestamp=time.time(),
            proximity=proximity,
            size=size,
            confidence=confidence,
            class_score=class_score,
            speed=speed,
            persistence=persistence,
            approach_rate=approach_rate,
            was_engaged=was_engaged,
            class_name=class_name,
            track_id=track_id,
        )
        self.records.append(record)
        
        # Keep buffer size under control
        if len(self.records) > self.max_records:
            self.records = self.records[-self.max_records:]
    
    def get_all_records(self) -> List[EngagementRecord]:
        """Return all logged records."""
        return list(self.records)
    
    def get_training_data(self) -> tuple[List[List[float]], List[float]]:
        """
        Convert records into training format.
        
        Returns:
            (features_list, labels) where:
            - features_list: list of feature vectors
            - labels: list of 0-1 labels (1 = engaged, 0 = ignored)
        """
        features_list = []
        labels = []
        
        for record in self.records:
            features_list.append(record.to_feature_vector())
            labels.append(1.0 if record.was_engaged else 0.0)
        
        return features_list, labels
    
    def clear(self) -> None:
        """Clear all logged records."""
        self.records.clear()
    
    def save_to_json(self, path: str | Path) -> bool:
        """Save logged records to a JSON file for later review."""
        try:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            
            data_list = [asdict(r) for r in self.records]
            with open(p, "w") as f:
                json.dump(data_list, f, indent=2)
            return True
        except Exception:
            return False
    
    def load_from_json(self, path: str | Path) -> bool:
        """Load previously saved records from JSON."""
        try:
            p = Path(path)
            if not p.exists():
                return False
            
            with open(p, "r") as f:
                data_list = json.load(f)
            
            self.records.clear()
            for data in data_list:
                record = EngagementRecord(**data)
                self.records.append(record)
            return True
        except Exception:
            return False
    
    def summary_stats(self) -> Dict[str, Any]:
        """Return summary statistics about logged data."""
        if not self.records:
            return {"total_records": 0}
        
        engaged = sum(1 for r in self.records if r.was_engaged)
        ignored = len(self.records) - engaged
        
        return {
            "total_records": len(self.records),
            "engaged_count": engaged,
            "ignored_count": ignored,
            "engagement_rate": engaged / len(self.records) if self.records else 0.0,
            "class_distribution": self._class_distribution(),
        }
    
    def _class_distribution(self) -> Dict[str, int]:
        """Count classes in the logged data."""
        dist = {}
        for record in self.records:
            dist[record.class_name] = dist.get(record.class_name, 0) + 1
        return dist
