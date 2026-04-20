#!/usr/bin/env python3
"""Compatibility launcher that forwards to the canonical run.py entrypoint."""

from __future__ import annotations

from run import main


if __name__ == "__main__":
    raise SystemExit(main())