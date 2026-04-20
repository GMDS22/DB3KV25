import unittest

from app.sentry_v2.sentry_v2_config import EngagementConfig, normalize_auto_trigger_engagement


class AutoTriggerEngagementNormalizationTests(unittest.TestCase):
    def test_legacy_auto_trigger_values_are_raised_to_safe_floors(self) -> None:
        engagement = EngagementConfig(
            auto_trigger_enabled=True,
            aim_lock_pan_tolerance=0.65,
            aim_lock_tilt_tolerance=0.55,
            fire_trigger_enter_pan_tolerance=0.08,
            fire_trigger_enter_tilt_tolerance=0.06,
            fire_trigger_exit_pan_tolerance=0.12,
            fire_trigger_exit_tilt_tolerance=0.09,
            fire_recenter_pan_tolerance=0.13,
            fire_recenter_tilt_tolerance=0.10,
        )

        self.assertGreaterEqual(engagement.aim_lock_pan_tolerance, 2.0)
        self.assertGreaterEqual(engagement.aim_lock_tilt_tolerance, 2.0)
        self.assertGreaterEqual(engagement.fire_trigger_enter_pan_tolerance, 2.0)
        self.assertGreaterEqual(engagement.fire_trigger_enter_tilt_tolerance, 2.0)
        self.assertGreaterEqual(
            engagement.fire_trigger_exit_pan_tolerance,
            engagement.fire_trigger_enter_pan_tolerance,
        )
        self.assertGreaterEqual(
            engagement.fire_trigger_exit_tilt_tolerance,
            engagement.fire_trigger_enter_tilt_tolerance,
        )
        self.assertGreaterEqual(
            engagement.fire_recenter_pan_tolerance,
            engagement.fire_trigger_exit_pan_tolerance,
        )
        self.assertGreaterEqual(
            engagement.fire_recenter_tilt_tolerance,
            engagement.fire_trigger_exit_tilt_tolerance,
        )

    def test_valid_auto_trigger_values_are_preserved(self) -> None:
        engagement = EngagementConfig(
            auto_trigger_enabled=True,
            aim_lock_pan_tolerance=3.0,
            aim_lock_tilt_tolerance=2.5,
            fire_trigger_enter_pan_tolerance=2.5,
            fire_trigger_enter_tilt_tolerance=2.0,
            fire_trigger_exit_pan_tolerance=3.5,
            fire_trigger_exit_tilt_tolerance=3.0,
            fire_recenter_pan_tolerance=3.8,
            fire_recenter_tilt_tolerance=3.2,
        )
        adjustments = normalize_auto_trigger_engagement(engagement)

        self.assertEqual(adjustments, [])
        self.assertEqual(engagement.aim_lock_pan_tolerance, 3.0)
        self.assertEqual(engagement.aim_lock_tilt_tolerance, 2.5)
        self.assertEqual(engagement.fire_trigger_enter_pan_tolerance, 2.5)
        self.assertEqual(engagement.fire_trigger_enter_tilt_tolerance, 2.0)


if __name__ == "__main__":
    unittest.main()