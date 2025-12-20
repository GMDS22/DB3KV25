"""
Object Trackers for Sentry Mode.

This package provides multi-object tracking algorithms.
ByteTrack is the default and recommended tracker.
"""

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .byte_tracker import ByteTracker, STrack, create_tracker
except ImportError:
    from byte_tracker import ByteTracker, STrack, create_tracker

__all__ = ['ByteTracker', 'STrack', 'create_tracker']
