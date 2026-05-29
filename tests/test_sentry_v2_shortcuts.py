import unittest
from types import MethodType, SimpleNamespace

from PyQt5.QtCore import Qt

from app.sentry_v2.sentry_v2_config import SentryV2Config, ShortcutConfig
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget, SHORTCUT_ACTION_SPECS_BY_ID


class _ShortcutHarness:
    def __init__(self, *, bindings=None, enabled=True, manual_controls_enabled=True) -> None:
        self.config = SimpleNamespace(
            shortcuts=ShortcutConfig(
                enabled=enabled,
                manual_controls_enabled=manual_controls_enabled,
                bindings=dict(bindings or {}),
            )
        )
        self._normalize_shortcut_sequences = MethodType(SentryV2TabWidget._normalize_shortcut_sequences, self)
        self._shortcut_sequences_for_action = MethodType(SentryV2TabWidget._shortcut_sequences_for_action, self)
        self._effective_shortcut_bindings = MethodType(SentryV2TabWidget._effective_shortcut_bindings, self)
        self._manual_shortcut_match_map = MethodType(SentryV2TabWidget._manual_shortcut_match_map, self)
        self._shortcut_conflict_owner_label = MethodType(SentryV2TabWidget._shortcut_conflict_owner_label, self)
        self._shortcut_default_sequences = MethodType(SentryV2TabWidget._shortcut_default_sequences, self)
        self._manual_keyboard_shortcuts_enabled = MethodType(SentryV2TabWidget._manual_keyboard_shortcuts_enabled, self)


class _ShortcutMutationHarness(_ShortcutHarness):
    def __init__(self, *, bindings=None, enabled=True, manual_controls_enabled=True) -> None:
        super().__init__(bindings=bindings, enabled=enabled, manual_controls_enabled=manual_controls_enabled)
        self._shortcut_action_spec = MethodType(SentryV2TabWidget._shortcut_action_spec, self)
        self._set_shortcut_bindings = MethodType(SentryV2TabWidget._set_shortcut_bindings, self)
        self._install_calls = 0
        self._refresh_calls = 0
        self._saved = False

    def _portable_path_string(self, path) -> str:
        return str(path)

    def _install_global_shortcuts(self) -> None:
        self._install_calls += 1

    def _refresh_shortcut_editor_rows(self, _text: str = "", *, selected_action_id: str = "") -> None:
        _ = (_text, selected_action_id)
        self._refresh_calls += 1

    def _save_config_quietly(self) -> None:
        self._saved = True


class ShortcutConfigBehaviorTests(unittest.TestCase):
    def test_sanitize_shortcut_config_preserves_explicit_empty_binding(self) -> None:
        shortcut_cfg = SentryV2Config._sanitize_shortcut_config(
            ShortcutConfig(bindings={"go_home": [], "manual_fire": ["Space", " Space "]})
        )

        self.assertEqual(shortcut_cfg.bindings, {"go_home": [], "manual_fire": ["Space"]})

    def test_command_shortcuts_without_modifiers_fall_back_to_default(self) -> None:
        harness = _ShortcutHarness(bindings={"go_home": ["F6"]})

        sequences = harness._shortcut_sequences_for_action(SHORTCUT_ACTION_SPECS_BY_ID["go_home"])

        self.assertEqual(sequences, ["Ctrl+Alt+W"])

    def test_explicit_empty_binding_keeps_command_unassigned(self) -> None:
        harness = _ShortcutHarness(bindings={"go_home": []})

        sequences = harness._shortcut_sequences_for_action(SHORTCUT_ACTION_SPECS_BY_ID["go_home"])

        self.assertEqual(sequences, [])

    def test_manual_shortcuts_allow_bare_keys_and_populate_match_map(self) -> None:
        harness = _ShortcutHarness(bindings={"manual_pan_left": ["Left", "A"], "manual_fire": ["Ctrl+Shift+F"]})

        match_map = harness._manual_shortcut_match_map()

        self.assertEqual(match_map[(int(Qt.Key_Left), 0)], "manual_pan_left")
        self.assertEqual(match_map[(int(Qt.Key_A), 0)], "manual_pan_left")
        self.assertEqual(match_map[(int(Qt.Key_F), int(Qt.CTRL) | int(Qt.SHIFT))], "manual_fire")

    def test_conflict_owner_lookup_reports_existing_command(self) -> None:
        harness = _ShortcutHarness(bindings={"go_home": ["Ctrl+Shift+H"]})

        owner = harness._shortcut_conflict_owner_label("Ctrl+Shift+H", exclude_action_id="toggle_sentry")

        self.assertEqual(owner, "Go home")

    def test_setting_default_binding_removes_override_and_empty_binding_persists(self) -> None:
        harness = _ShortcutMutationHarness(bindings={"go_home": ["Ctrl+Shift+H"]})

        harness._set_shortcut_bindings("go_home", ["Ctrl+Alt+W"])
        self.assertNotIn("go_home", harness.config.shortcuts.bindings)
        self.assertEqual(harness._install_calls, 1)
        self.assertEqual(harness._refresh_calls, 1)
        self.assertTrue(harness._saved)

        harness._saved = False
        harness._set_shortcut_bindings("go_home", [])
        self.assertEqual(harness.config.shortcuts.bindings["go_home"], [])
        self.assertTrue(harness._saved)


if __name__ == "__main__":
    unittest.main()