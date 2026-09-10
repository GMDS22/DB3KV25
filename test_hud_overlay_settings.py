"""Regression checks for live HUD overlay setting propagation."""

from types import SimpleNamespace

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _CheckBox:
    def __init__(self, checked):
        self.checked = checked

    def isChecked(self):
        return self.checked


class _Overlay:
    def __init__(self):
        self.updated_config = None

    def update_config(self, config):
        self.updated_config = config


class _SpinBox:
    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value


def test_hud_checkbox_changes_update_overlay_refresh_and_persistence():
    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab.config = SimpleNamespace(
        show_overlay=False,
        show_threat_scores=False,
        show_engagement_zone=False,
        show_guard_crosshair=False,
        show_no_fire_masks=False,
    )
    tab._chk_overlay = _CheckBox(True)
    tab._chk_scores = _CheckBox(True)
    tab._chk_zone = _CheckBox(True)
    tab._chk_guard_crosshair = _CheckBox(True)
    tab._chk_show_no_fire_masks = _CheckBox(True)
    tab.overlay = _Overlay()
    tab._force_next_display_refresh = False
    calls = []
    tab._push_config = lambda: calls.append("push")
    tab._note_sound_settings_changed = lambda: calls.append("sound")

    tab._on_overlay_changed()

    assert tab.config.show_overlay is True
    assert tab.config.show_threat_scores is True
    assert tab.config.show_engagement_zone is True
    assert tab.config.show_guard_crosshair is True
    assert tab.config.show_no_fire_masks is True
    assert tab.overlay.updated_config is tab.config
    assert tab._force_next_display_refresh is True
    assert calls == ["push", "sound"]


def test_hud_text_changes_update_all_video_overlay_refresh_and_persistence():
    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab.config = SimpleNamespace(
        overlay_text_size_pct=100,
        overlay_text_opacity_pct=100,
        overlay_text_background_opacity_pct=0,
    )
    tab._spin_overlay_text_size = _SpinBox(125)
    tab._spin_overlay_text_opacity = _SpinBox(55)
    tab._spin_overlay_text_background = _SpinBox(35)
    tab.overlay = _Overlay()
    tab._force_next_display_refresh = False
    calls = []
    tab._push_config = lambda: calls.append("push")
    tab._note_sound_settings_changed = lambda: calls.append("sound")

    tab._on_overlay_text_changed()

    assert tab.config.overlay_text_size_pct == 125
    assert tab.config.overlay_text_opacity_pct == 55
    assert tab.config.overlay_text_background_opacity_pct == 35
    assert tab.overlay.updated_config is tab.config
    assert tab._force_next_display_refresh is True
    assert calls == ["push", "sound"]
