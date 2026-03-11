"""
YOLO Trainer Window - Main App Interface
========================================
This module provides the YoloTrainerWindow class for the main turret application.
It imports the actual implementation from the yolo_trainer subfolder.
"""

# Import the actual trainer window from the subfolder
import sys
import os
from pathlib import Path

# Add the yolo_trainer directory to the path
current_dir = Path(__file__).parent.parent  # Go up to the main directory
yolo_trainer_dir = current_dir / "yolo_trainer"
if str(yolo_trainer_dir) not in sys.path:
    sys.path.insert(0, str(yolo_trainer_dir))

# Import the trainer window
from yolo_trainer.trainer_window import YoloTrainerWindow