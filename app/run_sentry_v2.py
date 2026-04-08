#!/usr/bin/env python3
"""Compatibility launcher for older SMART SENTRY entrypoint names."""

from __future__ import annotations

from run_smart_sentry_v2_3_2 import main


if __name__ == "__main__":
    raise SystemExit(main())