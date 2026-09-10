import unittest

from app.sentry_v2.sentry_v2_config import SentryV2Config, TargetFilterConfig
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget
from app.sentry_v2.target_filter import DetectedObject, TargetFilter
from app.sentry_v2.voice_runtime import VoskCommandListener


class TargetFilterShapeProfileTests(unittest.TestCase):
    def test_rat_profile_accepts_realistic_rat_like_bbox(self) -> None:
        cfg = TargetFilterConfig(
            allowed_classes=["rat"],
            min_confidence=0.46,
            min_size_ratio=0.0001,
            max_size_ratio=0.08,
            shape_filter_enabled=True,
            shape_profile_name="rat",
            semantic_min_confirm_frames=1,  # Disable semantic confirmation for base gate test
        )
        det = DetectedObject(
            track_id=1,
            class_name="rat",
            confidence=0.90,
            bbox=(0, 120, 90, 100),
            center_x=45.0,
            center_y=170.0,
            frame_width=1280,
            frame_height=720,
        )

        # The shape-profile regression should validate the base gate only. Semantic
        # confirmation is intentionally multi-frame and should not be required in a
        # single-detection geometry test.
        passed, reason, detail = TargetFilter(cfg)._passes_base(det)

        self.assertTrue(passed, f"expected rat bbox to pass base shape gate, got {reason}: {detail}")

    def test_rat_profile_accepts_tall_rat_like_bbox(self) -> None:
        cfg = TargetFilterConfig(
            allowed_classes=["rat"],
            min_confidence=0.46,
            min_size_ratio=0.0001,
            max_size_ratio=0.08,
            shape_filter_enabled=True,
            shape_profile_name="rat",
            semantic_min_confirm_frames=1,  # Disable semantic confirmation for base gate test
        )
        det = DetectedObject(
            track_id=2,
            class_name="rat",
            confidence=0.90,
            bbox=(228, 150, 58, 116),
            center_x=257.0,
            center_y=208.0,
            frame_width=1280,
            frame_height=720,
        )

        passed, reason, detail = TargetFilter(cfg)._passes_base(det)

        self.assertTrue(passed, f"expected tall rat bbox to pass base shape gate, got {reason}: {detail}")


class HUDOverlayTextSettingsTests(unittest.TestCase):
    def test_overlay_text_defaults_exist(self) -> None:
        cfg = SentryV2Config()
        self.assertEqual(cfg.overlay_text_opacity_pct, 100)
        self.assertEqual(cfg.overlay_text_background_opacity_pct, 0)
        self.assertEqual(cfg.overlay_text_size_pct, 100)

    def test_hud_overlay_settings_resolve_to_guard_tab(self) -> None:
        widget = SentryV2TabWidget.__new__(SentryV2TabWidget)
        widget._settings_tab_titles = [
            "Connection",
            "Master Profiles",
            "Detection Mode",
            "Target Library",
            "Target Filter",
            "Guard",
        ]
        self.assertEqual(widget._resolve_settings_tab_index_from_query("show me the hud settings"), 5)
        self.assertEqual(widget._resolve_settings_tab_index_from_query("show me the hud overlay"), 5)
        self.assertEqual(widget._resolve_settings_tab_index_from_query("show me the overlay text settings"), 5)


class VoiceCommandNormalizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.listener = VoskCommandListener(
            model_path="test-model",
            wake_word="elion",
            command_cooldown_s=0.0,
            on_command=lambda command: None,
            on_log=lambda message: None,
        )
        self.listener._settings_tab_titles = [
            "Connection",
            "Master Profiles",
            "Detection Mode",
            "Target Library",
            "Target Filter",
        ]

    def test_presets_tab_variants_canonicalize_to_master_profiles(self) -> None:
        self.assertEqual(
            self.listener._canonicalize_command_text("can you show me the presets tab"),
            "open master profiles tab",
        )
        self.assertEqual(
            self.listener._canonicalize_command_text("open the presets tab"),
            "open master profiles tab",
        )

    def test_presets_tab_variants_resolve_to_master_profiles_tab(self) -> None:
        widget = SentryV2TabWidget.__new__(SentryV2TabWidget)
        widget._settings_tab_titles = [
            "Connection",
            "Master Profiles",
            "Detection Mode",
            "Target Library",
            "Target Filter",
        ]
        widget._settings_tabs = type("TabsStub", (), {"count": lambda self: len(widget._settings_tab_titles), "isTabEnabled": lambda self, idx: True, "setCurrentIndex": lambda self, idx: None, "tabToolTip": lambda self, idx: widget._settings_tab_titles[idx]})()

        self.assertEqual(widget._resolve_settings_tab_index_from_query("open the presets tab"), 1)
        self.assertEqual(widget._resolve_settings_tab_index_from_query("can you show me the presets tab"), 1)
        self.assertEqual(widget._resolve_settings_tab_index_from_query("show presets"), 1)


if __name__ == "__main__":
    unittest.main()
