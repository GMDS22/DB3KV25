#!/usr/bin/env python3
"""Compatibility launcher kept for older v3-named import paths."""

from __future__ import annotations

from run_smart_sentry_v2_3_2 import SmartSentryV2_3_2StandaloneWindow, SmartSentryV3StandaloneWindow, main


if __name__ == "__main__":
    raise SystemExit(main())