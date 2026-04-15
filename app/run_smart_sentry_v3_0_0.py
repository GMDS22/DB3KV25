#!/usr/bin/env python3
"""Compatibility launcher for the Smart Sentry v3.0.0 release token."""

from __future__ import annotations

from app.run_smart_sentry_v3 import SmartSentryV2_3_2StandaloneWindow, SmartSentryV3StandaloneWindow, main


if __name__ == "__main__":
    raise SystemExit(main())
