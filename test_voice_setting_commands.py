#!/usr/bin/env python3
"""Focused regression checks for direct voice setting adjustment commands."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _ValueWidget:
    def __init__(self, value: int, minimum: int, maximum: int) -> None:
        self._value = value
        self._minimum = minimum
        self._maximum = maximum

    def value(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def minimum(self):
        return self._minimum

    def maximum(self):
        return self._maximum


def _make_tab() -> SentryV2TabWidget:
    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab._slider_led_pwm = _ValueWidget(180, 0, 255)
    tab._spin_auto_brightness_threshold = _ValueWidget(140, 0, 255)
    tab._spin_auto_pwm_min = _ValueWidget(60, 0, 255)
    tab._spin_auto_pwm_max = _ValueWidget(255, 0, 255)
    tab._slider_speed = _ValueWidget(50, 10, 100)
    tab._slider_sound_volume = _ValueWidget(40, 0, 100)
    tab._slider_human_voice_rate = _ValueWidget(100, 50, 150)
    tab._slider_human_voice_pitch = _ValueWidget(100, 50, 150)
    tab._slider_human_voice_volume = _ValueWidget(85, 0, 100)
    tab._assistant_setting_runtime_specs = lambda: {
        "lighting.led_pwm_value": {
            "label": "LED brightness",
            "widget": tab._slider_led_pwm,
            "kind": "int",
            "step": 10,
        },
        "lighting.auto_brightness_threshold": {
            "label": "Auto brightness threshold",
            "widget": tab._spin_auto_brightness_threshold,
            "kind": "int",
            "step": 10,
        },
        "lighting.auto_pwm_min": {
            "label": "Auto PWM minimum",
            "widget": tab._spin_auto_pwm_min,
            "kind": "int",
            "step": 10,
        },
        "lighting.auto_pwm_max": {
            "label": "Auto PWM maximum",
            "widget": tab._spin_auto_pwm_max,
            "kind": "int",
            "step": 10,
        },
        "engagement.engagement_speed_pct": {
            "label": "Engagement speed",
            "widget": tab._slider_speed,
            "kind": "int",
            "step": 5,
        },
        "sound.volume_pct": {
            "label": "Sound volume",
            "widget": tab._slider_sound_volume,
            "kind": "int",
            "step": 5,
        },
        "sound.human_voice_rate_pct": {
            "label": "Voice rate",
            "widget": tab._slider_human_voice_rate,
            "kind": "int",
            "step": 5,
        },
        "sound.human_voice_pitch_pct": {
            "label": "Voice pitch",
            "widget": tab._slider_human_voice_pitch,
            "kind": "int",
            "step": 5,
        },
        "sound.human_voice_volume_pct": {
            "label": "Voice volume",
            "widget": tab._slider_human_voice_volume,
            "kind": "int",
            "step": 5,
        },
    }
    return tab


def test_set_auto_brightness_threshold_by_voice() -> None:
    tab = _make_tab()

    result = tab._execute_voice_setting_adjustment_command("set auto brightness threshold to 150")

    assert result is not None
    acknowledge_event, spoken_confirmation, handled_summary, deferred_action = result
    assert acknowledge_event == "acknowledged"
    assert "auto brightness threshold" in str(spoken_confirmation or "").lower()
    assert "150" in str(spoken_confirmation or "")
    assert deferred_action is not None

    deferred_action()

    assert tab._spin_auto_brightness_threshold.value() == 150
    assert "150" in str(handled_summary or "")


def test_increase_voice_volume_uses_default_step_when_amount_missing() -> None:
    tab = _make_tab()

    result = tab._execute_voice_setting_adjustment_command("increase voice volume")

    assert result is not None
    acknowledge_event, spoken_confirmation, handled_summary, deferred_action = result
    assert acknowledge_event == "acknowledged"
    assert "voice volume" in str(spoken_confirmation or "").lower()
    assert "90 percent" in str(spoken_confirmation or "").lower()
    assert deferred_action is not None

    deferred_action()

    assert tab._slider_human_voice_volume.value() == 90
    assert "90 percent" in str(handled_summary or "").lower()


def main() -> None:
    test_set_auto_brightness_threshold_by_voice()
    test_increase_voice_volume_uses_default_step_when_amount_missing()
    print("voice setting command checks passed")


if __name__ == "__main__":
    main()