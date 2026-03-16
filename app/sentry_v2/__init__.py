"""
Smart Sentry v2 — Package init

Drop-in replacement / companion for the original sentry_mode.
Import SentryV2TabWidget and add it as a tab in the main app.
"""

from .sentry_v2_config import SentryV2Config
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .sentry_v2_comm import SentryV2Comm
from .sentry_v2_detector import SentryV2Detector
from .target_filter import TargetFilter, DetectedObject
from .threat_scorer import ThreatScorer, TrackedTarget
from .engagement_planner import EngagementPlanner, EngagementOrder
from .sentry_v2_overlay import SentryV2Overlay
from .sentry_v2_tab import SentryV2TabWidget

__version__ = "2.0.0"
