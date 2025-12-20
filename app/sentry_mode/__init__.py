"""
Sentry Ambush Mode - Intelligent Guard Turret System

A standalone tracking module for ambush-style target engagement.
Learns movement patterns, predicts trajectories, and fires predictively.

Usage:
    from sentry_mode import SentryController
    
    controller = SentryController(config_path="config/sentry_defaults.json")
    controller.start()
    
For main app integration:
    from sentry_mode import SentryTabWidget
    
    sentry_tab = SentryTabWidget()
    main_tab_widget.addTab(sentry_tab, "🎯 Sentry")
"""

from .sentry_controller import SentryController
from .track_recorder import TrackRecorder
from .path_analyzer import PathAnalyzer
from .trajectory_predictor import TrajectoryPredictor
from .peripheral_sensor import PeripheralSensor
from .sentry_overlay import SentryOverlay
from .sentry_config import SentryConfig

# Import tab widget for main app integration (optional - requires PyQt5)
try:
    from .sentry_tab_widget import SentryTabWidget
except ImportError:
    SentryTabWidget = None

__all__ = [
    'SentryController',
    'TrackRecorder', 
    'PathAnalyzer',
    'TrajectoryPredictor',
    'PeripheralSensor',
    'SentryOverlay',
    'SentryConfig',
    'SentryTabWidget'
]

__version__ = '1.0.0'
