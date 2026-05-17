#!/usr/bin/env python3
"""Structural regression checks for the home hero and theme tab."""

from pathlib import Path


def test_home_screen_uses_orb_logo_watermark() -> None:
    source_path = Path(__file__).parent / "app" / "sentry_v2" / "sentry_v2_tab.py"
    source = source_path.read_text(encoding="utf-8")

    assert 'self._ai_orb_home = AICoreWidget()' in source
    assert 'self._ai_orb_home.set_logo_opacity(0.70)' in source
    assert 'orb.set_static_logo(source, enabled=not source.isNull())' in source
    assert 'self._lbl_home_logo = QLabel()' not in source
    assert '("_ai_orb_hero", "_ai_orb_video", "_ai_orb_home")' in source


def test_theme_tab_restores_controls_and_visibility() -> None:
    source_path = Path(__file__).parent / "app" / "sentry_v2" / "sentry_v2_tab.py"
    source = source_path.read_text(encoding="utf-8")

    assert 'self._slider_theme_hero_glow' in source
    assert 'self._slider_theme_divider_strength' in source
    assert 'theme_cfg.hero_glow_pct' in source
    assert 'theme_cfg.divider_strength_pct' in source
    assert 'self._collapsible(preset_grp, collapsed=False)' in source
    assert 'self._collapsible(tune_grp, collapsed=False)' in source
    assert 'self._collapsible(interface_grp, collapsed=False)' in source


def test_settings_nav_restores_title_and_context_help() -> None:
    source_path = Path(__file__).parent / "app" / "sentry_v2" / "sentry_v2_tab.py"
    source = source_path.read_text(encoding="utf-8")

    assert 'tabs_nav_title = QLabel("SETTINGS")' in source
    assert 'tabs_nav_title.setVisible(True)' in source
    assert 'self._btn_settings_tab_help = QPushButton("?")' in source
    assert 'self._btn_settings_tab_help.clicked.connect(self._open_active_settings_help)' in source
    assert 'SETTINGS_TAB_HELP_QUERIES = {' in source
    assert 'browser.set_search_query(search_query, focus_search=focus_search)' in source


def main() -> None:
    test_home_screen_uses_orb_logo_watermark()
    test_theme_tab_restores_controls_and_visibility()
    test_settings_nav_restores_title_and_context_help()
    print("home hero and theme regression checks passed")


if __name__ == "__main__":
    main()