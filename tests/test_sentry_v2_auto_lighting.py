import unittest
from types import MethodType, SimpleNamespace

import numpy as np

from app.sentry_v2.sentry_v2_config import LightingConfig
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _ButtonStub:
    def __init__(self) -> None:
        self.text = ""

    def setText(self, text: str) -> None:
        self.text = text


class _AutoLightingHarness:
    def __init__(self, *, auto_enabled: bool, led_on: bool, manual_pwm: int = 255) -> None:
        self.config = SimpleNamespace(
            lighting=LightingConfig(
                auto_lighting_enabled=auto_enabled,
                led_pwm_value=manual_pwm,
                auto_brightness_threshold=70,
                auto_pwm_min=100,
                auto_pwm_max=255,
                auto_sample_interval_frames=8,
            )
        )
        self._led_on = led_on
        self._auto_led_pwm = 0
        self._scene_luma = 128.0
        self._queued: list[tuple[str, tuple[object, ...], dict[str, object]]] = []
        self.engine = SimpleNamespace(current_pan=10.0, current_tilt=20.0)
        self._btn_led = _ButtonStub()
        self._last_raw_frame = None

        self._update_auto_lighting = MethodType(SentryV2TabWidget._update_auto_lighting, self)
        self._apply_auto_lighting_from_cached_frame = MethodType(SentryV2TabWidget._apply_auto_lighting_from_cached_frame, self)
        self._sync_auto_lighting_toggle_widgets = MethodType(SentryV2TabWidget._sync_auto_lighting_toggle_widgets, self)

    def _host_controls_hardware(self) -> bool:
        return False

    def _queue_comm_task(self, name: str, *args: object, **kwargs: object) -> None:
        self._queued.append((name, args, kwargs))

    def _save_config_quietly(self) -> None:
        pass


class AutoLightingBehaviorTests(unittest.TestCase):
    def test_led_toggle_with_auto_enabled_dispatches_bright_scene_zero_pwm(self) -> None:
        harness = _AutoLightingHarness(auto_enabled=True, led_on=False)
        harness._last_raw_frame = np.full((12, 12, 3), 255, dtype=np.uint8)

        SentryV2TabWidget._on_led_toggled(harness, True)

        self.assertEqual(harness._btn_led.text, "LED: ON")
        self.assertEqual(harness._auto_led_pwm, 0)
        self.assertEqual(harness._queued, [("set_led_pwm", (0, 10.0, 20.0), {})])

    def test_auto_toggle_on_with_led_already_on_applies_cached_frame_immediately(self) -> None:
        harness = _AutoLightingHarness(auto_enabled=False, led_on=True, manual_pwm=180)
        harness._last_raw_frame = np.full((12, 12, 3), 255, dtype=np.uint8)

        SentryV2TabWidget._on_auto_lighting_toggled(harness, True)

        self.assertTrue(harness.config.lighting.auto_lighting_enabled)
        self.assertEqual(harness._auto_led_pwm, 0)
        self.assertEqual(harness._queued, [("set_led_pwm", (0, 10.0, 20.0), {})])


if __name__ == "__main__":
    unittest.main()
