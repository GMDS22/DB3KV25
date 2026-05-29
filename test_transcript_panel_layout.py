#!/usr/bin/env python3
"""Structural regression check for the transcript panel layout."""

from pathlib import Path


def test_transcript_panel_is_not_stacked_under_telemetry() -> None:
    source_path = Path(__file__).parent / "app" / "sentry_v2" / "sentry_v2_tab.py"
    source = source_path.read_text(encoding="utf-8")

    assert 'self._telemetry_voice_splitter = QSplitter(Qt.Horizontal)' in source
    assert 'QSplitter#sentryV2TelemetryVoiceSplitter::handle:horizontal' in source
    assert 'self._telemetry_voice_splitter.addWidget(self._build_voice_hearing_panel())' in source


def main() -> None:
    test_transcript_panel_is_not_stacked_under_telemetry()
    print("transcript panel layout check passed")


if __name__ == "__main__":
    main()