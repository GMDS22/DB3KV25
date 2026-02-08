import json
import os
import sys
import time

from PyQt5.QtWidgets import QApplication

ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT, "app")
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from MAIN_FILE_SINGLE_CAM import TrackingApp


def _print_result(label, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    msg = f"[{status}] {label}"
    if detail:
        msg += f" :: {detail}"
    print(msg)
    return ok


def main():
    qapp = QApplication.instance() or QApplication(sys.argv)

    # Prepare settings file with controlled idle zone values
    settings_path = os.path.join(ROOT, "settings.json")
    if not settings_path:
        print("[FAIL] SETTINGS_FILE path not found")
        return 1

    backup = None
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            backup = f.read()
        try:
            settings = json.loads(backup) if backup else {}
        except Exception:
            settings = {}
    else:
        settings = {}

    # Override only idle-zone-related keys
    settings.update(
        {
            "idle_zone_return_enabled": True,
            "idle_zone_pan_divisions": 4,
            "idle_zone_tilt_divisions": 2,
            "idle_zone_selected_pan": 2,
            "idle_zone_selected_tilt": 1,
            "idle_mode_enabled": True,
            "idle_behavior": "Rest",
        }
    )

    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)

    try:
        with open(settings_path, "r") as f:
            written_raw = json.load(f)
        print(
            "[INFO] written settings.json idle_zone_*:",
            {
                k: written_raw.get(k)
                for k in (
                    "idle_zone_return_enabled",
                    "idle_zone_pan_divisions",
                    "idle_zone_tilt_divisions",
                    "idle_zone_selected_pan",
                    "idle_zone_selected_tilt",
                )
            },
        )
    except Exception as e:
        print(f"[WARN] Could not read written settings.json: {e}")

    app = TrackingApp()
    try:
        for _ in range(3):
            qapp.processEvents()
            time.sleep(0.05)
    except Exception:
        pass

    print(f"[INFO] SETTINGS_FILE={getattr(app, 'SETTINGS_FILE', None)}")
    try:
        with open(settings_path, "r") as f:
            loaded_raw = json.load(f)
        print(
            "[INFO] settings.json idle_zone_*:",
            {
                k: loaded_raw.get(k)
                for k in (
                    "idle_zone_return_enabled",
                    "idle_zone_pan_divisions",
                    "idle_zone_tilt_divisions",
                    "idle_zone_selected_pan",
                    "idle_zone_selected_tilt",
                )
            },
        )
    except Exception as e:
        print(f"[WARN] Could not read settings.json: {e}")

    # Validate UI initialization for Idle Zones
    ok_tab = app.idle_zones_tab is not None and getattr(app, "idle_zones_widget", None) is not None
    _print_result("Idle Zones tab created", ok_tab)

    ok_enable = bool(getattr(app, "idle_zone_enable_checkbox", None) and app.idle_zone_enable_checkbox.isChecked())
    _print_result("Idle zone enable checkbox loaded", ok_enable)

    ok_divs = (
        str(getattr(app, "idle_zone_pan_divisions_combo", None).currentText()) == "4"
        and str(getattr(app, "idle_zone_tilt_divisions_combo", None).currentText()) == "2"
    )
    try:
        pan_combo = getattr(app, "idle_zone_pan_divisions_combo", None)
        tilt_combo = getattr(app, "idle_zone_tilt_divisions_combo", None)
        pan_items = [pan_combo.itemText(i) for i in range(pan_combo.count())]
        tilt_items = [tilt_combo.itemText(i) for i in range(tilt_combo.count())]
    except Exception:
        pan_items = []
        tilt_items = []
    print(
        "[INFO] combo divisions:",
        getattr(app, "idle_zone_pan_divisions_combo", None).currentText(),
        getattr(app, "idle_zone_tilt_divisions_combo", None).currentText(),
        "| items:",
        pan_items,
        tilt_items,
    )
    _print_result("Idle zone divisions loaded", ok_divs)

    ok_sel = (
        int(getattr(app, "idle_zone_selected_pan", -1)) == 2
        and int(getattr(app, "idle_zone_selected_tilt", -1)) == 1
    )
    _print_result("Idle zone selection loaded", ok_sel)
    try:
        app.idle_zones_widget.set_selected_zones([(0, 0), (1, 1)], emit=True)
        ok_multi = getattr(app, "idle_zone_selected_list", []) == [(0, 0), (1, 1)]
    except Exception:
        ok_multi = False
    _print_result("Multi-zone selection updates list", ok_multi)
    print(
        "[INFO] idle_zone_divisions (attr):",
        getattr(app, "idle_zone_pan_divisions", None),
        getattr(app, "idle_zone_tilt_divisions", None),
    )

    # Validate live limits binding (change limits and verify center)
    try:
        app.pan_min_input.setValue(10)
        app.pan_max_input.setValue(210)
        app.tilt_min_input.setValue(20)
        app.tilt_max_input.setValue(100)
        app.apply_new_limits()
        center = app._idle_zone_get_center()
        first_zone = (0, 0)
        expected_pan = 10 + (210 - 10) / 4 * (first_zone[0] + 0.5)
        expected_tilt = 20 + (100 - 20) / 2 * (first_zone[1] + 0.5)
        ok_center = center is not None and abs(center[0] - expected_pan) < 0.01 and abs(center[1] - expected_tilt) < 0.01
    except Exception:
        ok_center = False
    _print_result("Idle zone center reflects live limits", ok_center)

    # Validate user interaction: selecting a zone updates state + saves settings
    try:
        app.idle_zones_widget.set_selected_zone(0, 0, emit=True)
        ok_interaction = app.idle_zone_selected_pan == 0 and app.idle_zone_selected_tilt == 0
    except Exception:
        ok_interaction = False
    _print_result("Zone selection updates internal state", ok_interaction)

    # Validate return-to-zone gating (idle mode enabled + rest)
    try:
        app.idle_zone_return_enabled = True
        app.idle_behavior = "rest"
        app.idle_mode_toggle_btn.setChecked(True)
        ok_gate = app._idle_zone_should_apply(app.idle_behavior) is True
    except Exception:
        ok_gate = False
    _print_result("Idle zone return gating (idle+rest)", ok_gate)

    # Save settings after interaction
    try:
        app.save_settings()
        ok_saved = True
    except Exception:
        ok_saved = False
    _print_result("Settings saved after interaction", ok_saved)

    # Reload app to verify persistence
    app.close()
    del app

    app2 = TrackingApp()
    ok_reload = (
        int(getattr(app2, "idle_zone_selected_pan", -1)) == 0
        and int(getattr(app2, "idle_zone_selected_tilt", -1)) == 0
        and bool(getattr(app2, "idle_zone_enable_checkbox", None) and app2.idle_zone_enable_checkbox.isChecked())
    )
    _print_result("Persistence on reload", ok_reload)

    app2.close()

    # Restore settings file
    if backup is not None:
        with open(settings_path, "w") as f:
            f.write(backup)

    # Exit cleanly
    qapp.quit()

    all_ok = all([ok_tab, ok_enable, ok_divs, ok_sel, ok_center, ok_interaction, ok_gate, ok_saved, ok_reload])
    return 0 if all_ok else 2


if __name__ == "__main__":
    sys.exit(main())
