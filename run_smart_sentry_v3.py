#!/usr/bin/env python3
"""Compatibility launcher that forwards to the canonical run.py entrypoint."""

from __future__ import annotations

from app.run_smart_sentry_v2_3_2 import SmartSentryV2_3_2StandaloneWindow, SmartSentryV3StandaloneWindow
from run import main


if __name__ == "__main__":
    raise SystemExit(main())