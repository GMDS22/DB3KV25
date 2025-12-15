"""
Keyboard shortcuts mapping and help text for the Auto Turret app.

This module only contains a compact mapping and a function that produces
human-friendly markdown describing the configured shortcuts. MAIN_FILE.py
imports it to show the help in the user manual and to keep the mapping in one place.
"""
from PyQt5.QtCore import Qt

# Map action keys (human-friendly name) -> list of Qt.Key values
KEYMAP = {
    "move_up": [Qt.Key_W, Qt.Key_Up],
    "move_down": [Qt.Key_S, Qt.Key_Down],
    "move_left": [Qt.Key_A, Qt.Key_Left],
    "move_right": [Qt.Key_D, Qt.Key_Right],
    "center": [Qt.Key_C],
    "go_home": [Qt.Key_H],
    "fire_momentary": [Qt.Key_Space],
    "toggle_safety": [Qt.Key_K],
    "toggle_trigger_mode": [Qt.Key_T],
    "toggle_rapid_fire": [Qt.Key_R],
    "export_rapid_preset": [Qt.Key_E],
    "save_layout": [Qt.Key_L],
    # Additional manual shortcuts
    "mosfet_hold": [Qt.Key_M],
    "toggle_relay1": [Qt.Key_1],
    "toggle_relay2": [Qt.Key_2],
    "step_dec": [Qt.Key_BracketLeft],
    "step_inc": [Qt.Key_BracketRight],
    "manual_speed_dec": [Qt.Key_Minus, Qt.Key_Underscore],
    "manual_speed_inc": [Qt.Key_Plus, Qt.Key_Equal],
}

# Human friendly labels for actions
LABELS = {
    "move_up": "Move Up (tilt +)",
    "move_down": "Move Down (tilt -)",
    "move_left": "Move Left (pan -)",
    "move_right": "Move Right (pan +)",
    "center": "Center (zero pan/tilt)",
    "go_home": "Go Home (move to HOME position)",
    "fire_momentary": "Manual Fire (momentary)",
    "toggle_safety": "Toggle Safety Lock/Arm",
    "toggle_trigger_mode": "Toggle Trigger Mode (MOSFET / BB)",
    "toggle_rapid_fire": "Toggle Rapid-Fire (MOSFET)",
    "export_rapid_preset": "Export Rapid-Fire Preset to file",
    "save_layout": "Save current dock layout",
    "mosfet_hold": "MOSFET Hold (latched)",
    "toggle_relay1": "Toggle Relay 1 (LED)",
    "toggle_relay2": "Toggle Relay 2 (Laser)",
    "step_dec": "Decrease Step Size",
    "step_inc": "Increase Step Size",
    "manual_speed_dec": "Decrease Manual Speed",
    "manual_speed_inc": "Increase Manual Speed",
}

# Map Qt keys to action names (reverse mapping) for quick lookup
REVERSE_KEYMAP = {}
for action, keys in KEYMAP.items():
    for k in keys:
        REVERSE_KEYMAP.setdefault(k, []).append(action)


def help_markdown():
    """Return a markdown string documenting the keyboard shortcuts."""
    lines = ["## Keyboard Shortcuts\n", "The app supports the following keyboard shortcuts:", ""]
    for action in LABELS:
        key_names = []
        for k in KEYMAP.get(action, []):
            # Try to present a friendly name for Qt keys
            name = None
            try:
                # Qt has enumerations but not a direct name mapping; craft common names
                if k == Qt.Key_W:
                    name = "W"
                elif k == Qt.Key_A:
                    name = "A"
                elif k == Qt.Key_S:
                    name = "S"
                elif k == Qt.Key_D:
                    name = "D"
                elif k == Qt.Key_Up:
                    name = "Up Arrow"
                elif k == Qt.Key_Down:
                    name = "Down Arrow"
                elif k == Qt.Key_Left:
                    name = "Left Arrow"
                elif k == Qt.Key_Right:
                    name = "Right Arrow"
                elif k == Qt.Key_Space:
                    name = "Space"
                elif k == Qt.Key_C:
                    name = "C"
                elif k == Qt.Key_H:
                    name = "H"
                elif k == Qt.Key_K:
                    name = "K"
                elif k == Qt.Key_T:
                    name = "T"
                elif k == Qt.Key_R:
                    name = "R"
                elif k == Qt.Key_E:
                    name = "E"
                elif k == Qt.Key_L:
                    name = "L"
                elif k == Qt.Key_M:
                    name = "M"
                elif k == Qt.Key_1:
                    name = "1"
                elif k == Qt.Key_2:
                    name = "2"
                elif k == Qt.Key_BracketLeft:
                    name = "["
                elif k == Qt.Key_BracketRight:
                    name = "]"
                elif k == Qt.Key_Plus or k == Qt.Key_Equal:
                    name = "+"
                elif k == Qt.Key_Minus or k == Qt.Key_Underscore:
                    name = "-"
                else:
                    name = str(k)
            except Exception:
                name = str(k)
            key_names.append(name)
        lines.append(f"- **{LABELS.get(action, action)}** — {', '.join(key_names)}")
    lines.append("")
    lines.append("Notes: Press-and-hold works where supported (movement keys). The Fire key is momentary: press to fire, release to stop.")
    return "\n".join(lines)


if __name__ == "__main__":
    print(help_markdown())
