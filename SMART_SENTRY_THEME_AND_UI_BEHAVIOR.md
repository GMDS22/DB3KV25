# Smart Sentry v2 — Theme & UI Behavior Reference

> Canonical document describing the global theme system, panel layout contracts,
> and button/widget behaviour rules for the Smart Sentry v2 desktop application.
> All future UI changes **must** consult this file to preserve visual and
> behavioural consistency.

---

## 1. Theme Engine Overview

| Item | Location |
|------|----------|
| Palette bootstrap | `app/theme_manager.py` → `get_dark_palette()` |
| Live stylesheet generator | `sentry_v2_tab.py` → `_apply_theme()` |
| Theme presets dictionary | `THEME_PRESETS` constant near top of `sentry_v2_tab.py` |
| Per-user config | `ThemeConfig` dataclass persisted in `sentry_v2_config.json` |
| Shared docs + AI widget adapters | `document_browser.py` / `ai_dashboard_widgets.py` → `apply_theme_tokens()` |
| Theme profile import/export | Theme tab → `Export Profile` / `Import Profile` JSON actions |
| Saved theme presets | Theme tab → `Saved Theme Presets` snapshot manager |
| Panel zoom shortcut | `Shift + Mouse Wheel` (while settings panel focused) |

### 1.1 Token System

The stylesheet is built from a **token dictionary** produced by `_theme_tokens()`.
Key tokens and their roles:

| Token | Purpose |
|-------|---------|
| `hero_start`, `hero_mid` | Gradient stops for hero / accent panels |
| `surface`, `surface_alt_rgba` | Default and alternate panel backgrounds |
| `accent`, `accent_soft`, `accent_faint` | Primary accent colour at full / soft / faint opacity |
| `hero_text`, `hero_subtle` | Text colours on hero-gradient surfaces |
| `danger`, `danger_soft` | Safety / fire button colours |
| `text`, `text_secondary` | Default text and secondary text |
| `border`, `border_strong` | Default and emphasised borders |

### 1.2 Configurable Sliders

| Config Key | Range | Default | Effect |
|------------|-------|---------|--------|
| `preset` | string key | `"ember"` | Base colour scheme |
| `accent_strength_pct` | 60–140 | 100 | Accent colour saturation multiplier |
| `contrast_pct` | 85–125 | 100 | Surface ↔ text contrast factor |
| `surface_opacity_pct` | 55–100 | 94 | Panel background opacity |
| `video_panel_opacity_pct` | 55–100 | 100 | Video overlay background opacity |
| `window_opacity_pct` | 70–100 | 100 | Entire window transparency |
| `hero_glow_pct` | 70–150 | 100 | Header/hero glow intensity |
| `divider_strength_pct` | 60–145 | 100 | Border and divider emphasis |
| `corner_radius_px` | 8–24 | 14 | Global corner rounding size |
| `font_scale_pct` | 50–280 | 100 | Global text size multiplier |
| `settings_panel_width` | min–860 | 420 | Right settings column width |

Theme profile contract:
- Export writes a self-contained JSON payload (`smart-sentry-theme-profile-v1`) with theme fields plus `settings_panel_width`.
- Import accepts either nested (`{"theme": {...}}`) or flat payloads and clamps all numeric values to live slider ranges.
- Unknown preset keys are ignored and the current preset remains active.

Saved preset contract:
- The `Saved Theme Presets` section stores named snapshots under `app/config/smart_sentry_theme_snapshots.json`.
- Snapshots round-trip the same live theme fields as export/import and can be applied, updated, or deleted from the Theme tab.

---

## 2. Panel Layout Architecture

```
_main_splitter  (Qt.Horizontal)
├── left_panel
│   └── _layout_splitter  (Qt.Vertical)
│       ├── [0] Video Canvas               stretch 5
│       └── [1] _bottom_info_splitter      stretch 1
│           ├── [0] _telemetry_voice_splitter   stretch 1
│           │   ├── System Telemetry   (AITelemetryPanel)
│           │   └── Speech To Text     (QFrame)
│           ├── [1] Serial Output         (QGroupBox)
│           └── [2] Command Status        (QGroupBox)
└── right_panel
    └── Settings Tabs
```

### 2.1 Bottom Info Panels

The `_bottom_info_splitter` holds three independently resizable panes. The left pane is itself a horizontal splitter so the telemetry and speech transcript surfaces can sit side by side by default and still be adjusted independently when needed.

| Panel | Object name | Min size / default behavior |
|-------|-------------|-----------------------------|
| Telemetry / Speech column | `sentryV2TelemetryVoiceSplitter` | Equal-width 1:1 default split |
| System Telemetry | `aiTelemetryPanel` | Left half of the left column |
| Speech To Text | `sentryV2VoiceHearingPanel` | Right half of the left column, expandable |
| Serial Output | (QGroupBox) | 120 px minimum height |
| Command Status | (QGroupBox) | 120 px minimum height |

The left pane video height is adjusted with the vertical `sentryV2LayoutSplitter` handle. The bottom band and the bottom-left telemetry/speech pair are adjusted with horizontal splitter handles (`sentryV2BottomInfoSplitter` and `sentryV2TelemetryVoiceSplitter`). All three handles are intentionally visible in the live stylesheet so operators can discover the resize path quickly.

---

## 3. Button Roles & Styling

Buttons are assigned a **role** via `_set_button_role(button, role)` which sets
a `buttonRole` property. The stylesheet uses `QPushButton[buttonRole="..."]`
selectors for each role.

| Role | Purpose | Typical colour |
|------|---------|---------------|
| `primary` | Main actions (HOME, Sweep, Link) | Accent gradient |
| `utility` | Secondary actions (export, clear, camera) | Surface with border |
| `mode` | Toggle/state buttons (LED, Laser, Sentry) | Accent tint when checked |
| `danger` | Safety-critical buttons (FIRE, Safety) | Red/danger gradient |
| `dpadArrow` | Directional movement arrows | Subtle surface |

---

## 4. Object-Name → Stylesheet Selector Map

| Object Name | Widget | Stylesheet Selector |
|-------------|--------|-------------------|
| `sentryV2Video` | QLabel (video canvas) | `QLabel#sentryV2Video` |
| `sentryV2LayoutSplitter` | QSplitter (video vs bottom area) | `QSplitter#sentryV2LayoutSplitter` |
| `sentryV2TelemetryVoiceSplitter` | QSplitter (telemetry vs speech column) | `QSplitter#sentryV2TelemetryVoiceSplitter` |
| `sentryV2Log` | QTextEdit (serial log) | `QTextEdit#sentryV2Log` |
| `sentryV2VoiceHearingPanel` | QFrame (speech transcript card) | `QFrame#sentryV2VoiceHearingPanel` |
| `sentryV2StatusCard` | QFrame (status card) | `QFrame#sentryV2StatusCard` |
| `sentryV2StatusSubframe` | QFrame (position/bridge) | `QFrame#sentryV2StatusSubframe` |

### 4.1 Dynamic Properties Used in Stylesheets

| Property | Values | Applied to |
|----------|--------|-----------|
| `buttonRole` | `"primary"`, `"utility"`, `"mode"`, `"danger"`, `"dpadArrow"` | All styled buttons |
| `themeRole` | various | Status labels and detail strings |
| `accentColor` | hex colour | Status cards |
| `barRole` | `"pan"`, `"tilt"` | Position progress bars |

Text contract:
- All operator-visible tab text must derive from live theme tokens, either through base widget selectors, `themeRole` selectors, or helper methods such as `_compact_status_style()`.
- Do not use hardcoded hex text colors for labels or checkboxes in tab content, because those break readability on light themes.
- Checkbox text must remain theme-driven in every tab, including the Manual Control sound controls.
- The shared Documentation renderer and the AI dashboard widgets must consume the live Smart Sentry theme tokens through their adapter methods instead of freezing a separate hardcoded palette.

---

## 5. Persistence & Layout Restore

| Config Key | Content |
|------------|---------|
| `layout_splitter_sizes` | list[int] — [video, bottom] |
| `bottom_info_splitter_sizes` | list[int] — [telemetry+speech column, serial, command-status] |
| `telemetry_voice_splitter_sizes` | list[int] — [system telemetry, speech to text] |
| `main_splitter_sizes` | list[int] — [left-pane, settings-panel] |

On app start:
- Layout splitter sizes restored from config, with fallback proportions.
- Bottom info splitter sizes restored, with equal-width fallback across the three bottom panes.
- Telemetry / speech splitter sizes restored, with fallback 1:1 equal widths.

---

## 6. Responsive / Zoom Behaviour

- `Shift + Mouse Wheel` adjusts `font_scale_pct` (50–280%).
- `_apply_theme()` regenerates the entire stylesheet with new `base_font`,
  `status_font`, `button_min_h` derived from the scale.
- `_apply_theme()` is also the canonical pass for text contrast, so label,
  checkbox, and status text colors must follow the current theme tokens for
  both dark and light presets.
- Button minimum heights and grid spacings are computed from the font scale.
- Registered responsive button grids keep multi-column layouts left-to-right,
  but when a grid collapses to a single column its buttons are placed in a
  centered middle track rather than hugging the left edge.
- The layout automatically reflows as font sizes change.

---

*Last updated: 2026-05-14*
