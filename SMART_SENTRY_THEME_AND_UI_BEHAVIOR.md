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
| `corner_radius_px` | 8–24 | 14 | Global corner rounding size |
| `font_scale_pct` | 50–280 | 100 | Global text size multiplier |

---

## 2. Panel Layout Architecture

```
_main_splitter  (Qt.Horizontal)
├── left_panel
│   └── _layout_splitter  (Qt.Vertical)
│       ├── [0] Video Canvas               stretch 5
│       └── [1] _bottom_info_splitter      stretch 1
│           ├── Serial Output   (QGroupBox)   stretch 2
│           └── Command Status  (QGroupBox)   stretch 3
└── right_panel
    └── Settings Tabs
```

### 2.1 Bottom Info Panels

The `_bottom_info_splitter` holds two `QGroupBox` widgets:

| Panel | Object name | Min height |
|-------|-------------|------------|
| Serial Output | (QGroupBox) | 120 px |
| Command Status | (QGroupBox) | 120 px |

Both are independently resizable via the splitter handle.

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
| `sentryV2Log` | QTextEdit (serial log) | `QTextEdit#sentryV2Log` |
| `sentryV2StatusCard` | QFrame (status card) | `QFrame#sentryV2StatusCard` |
| `sentryV2StatusSubframe` | QFrame (position/bridge) | `QFrame#sentryV2StatusSubframe` |

### 4.1 Dynamic Properties Used in Stylesheets

| Property | Values | Applied to |
|----------|--------|-----------|
| `buttonRole` | `"primary"`, `"utility"`, `"mode"`, `"danger"`, `"dpadArrow"` | All styled buttons |
| `themeRole` | various | Status labels and detail strings |
| `accentColor` | hex colour | Status cards |
| `barRole` | `"pan"`, `"tilt"` | Position progress bars |

---

## 5. Persistence & Layout Restore

| Config Key | Content |
|------------|---------|
| `layout_splitter_sizes` | list[int] — [video, bottom] |
| `bottom_info_splitter_sizes` | list[int] — [serial, command-status] |
| `main_splitter_sizes` | list[int] — [left-pane, settings-panel] |

On app start:
- Layout splitter sizes restored from config, with fallback proportions.
- Bottom info splitter sizes restored, with fallback 2:3 ratio.

---

## 6. Responsive / Zoom Behaviour

- `Shift + Mouse Wheel` adjusts `font_scale_pct` (50–280%).
- `_apply_theme()` regenerates the entire stylesheet with new `base_font`,
  `status_font`, `button_min_h` derived from the scale.
- Button minimum heights and grid spacings are computed from the font scale.
- The layout automatically reflows as font sizes change.

---

*Last updated: 2026-04-09*
