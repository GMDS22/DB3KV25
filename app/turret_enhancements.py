# turret_enhancements.py
# Minimal, clean TurretEnhancements used by Movement_Detect_Yolo_me.py
import os
import re
from typing import Any

from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QTextCursor
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QStatusBar, QWidget

# Optional winsound fallback on Windows
winsound: Any = None
HAVE_WINSOUND = False
try:
    import winsound as _winsound

    winsound = _winsound
    HAVE_WINSOUND = True
except Exception:
    HAVE_WINSOUND = False


class TurretEnhancements:
    """Small helper: top-bar, status bar, and safe sound playback helpers."""

    def __init__(self, main_window):
        if (
            hasattr(main_window, "enhancer_initialized")
            and main_window.enhancer_initialized
        ):
            return
        main_window.enhancer_initialized = True

        self.main = main_window
        self.serial_widget = None
        self.target_locked = False

        self.sound_paths = {
            "fire": ("sounds/laser-312360.wav", "sounds/laser-312360.mp3"),
            "detect": ("sounds/target-detected.wav", "sounds/target detected.mp3"),
            "startup": ("sounds/Start.wav", "sounds/Start.mp3"),
            "armed": ("sounds/armed.wav", "sounds/armed.mp3"),
            "disarmed": ("sounds/disarmed.wav", "sounds/disarmed.mp3"),
            "connect": ("sounds/success_02-68338.wav", "sounds/success_02-68338.mp3"),
            "stop": ("sounds/StopAutotracking_1.wav", "sounds/StopAutotracking.mp3"),
        }

        self.fire_sound = self._create_sound(self.sound_paths["fire"][0], 0.7)
        self.detect_sound = self._create_sound(self.sound_paths["detect"][0], 0.5)
        self.startup_sound = self._create_sound(self.sound_paths["startup"][0], 0.8)

        # Optional sound effects
        self.connect_sound = self._create_sound(self.sound_paths["connect"][0], 0.7)
        self.armed_sound = self._create_sound(self.sound_paths["armed"][0], 0.8)
        self.stop_autotrack_sound = self._create_sound(self.sound_paths["stop"][0], 0.6)

        try:
            self.top_bar = self._create_top_bar()
        except Exception:
            self.top_bar = None

        try:
            self.status_bar = self._create_status_bar()
        except Exception:
            self.status_bar = None

    # ------------------------------------
    # SOUND HANDLING
    # ------------------------------------
    def _try_sound_file(self, path):
        try:
            if path and os.path.isfile(path):
                return path
            if path.endswith(".wav"):
                alt = path[:-4] + ".mp3"
            elif path.endswith(".mp3"):
                alt = path[:-4] + ".wav"
            else:
                alt = None
            if alt and os.path.isfile(alt):
                return alt
        except Exception:
            pass
        return None

    def _create_sound(self, path, volume):
        """Create a QSoundEffect object with volume, handling fallbacks."""
        try:
            sound_path = self._try_sound_file(path)
            if sound_path:
                sound = QSoundEffect()
                sound.setSource(QUrl.fromLocalFile(sound_path))
                sound.setVolume(volume)
                return sound
        except Exception:
            pass
        return None

    def play_sound(self, sound_obj, volume=None):
        """Play a sound safely with winsound fallback.
        
        Args:
            sound_obj: QSoundEffect object to play
            volume: Optional volume level (0-100). If None, uses slider value from main window.
        """
        try:
            if not sound_obj or not getattr(self.main, "sound_enabled", True):
                return
            
            # Get volume from parameter or from slider in main window
            if volume is None:
                # Try to get volume from sound_volume_slider
                if hasattr(self.main, "sound_volume_slider"):
                    volume = self.main.sound_volume_slider.value()
                else:
                    volume = 80  # Default to 80%
            
            # Clamp volume to 0-100 range
            volume = max(0, min(100, volume))
            
            # Convert percentage to QSoundEffect volume (0.0 to 1.0)
            qse_volume = volume / 100.0
            
            try:
                # Set volume on QSoundEffect if available
                if hasattr(sound_obj, "setVolume"):
                    sound_obj.setVolume(qse_volume)
                
                sound_obj.play()
                return
            except Exception:
                pass

            if HAVE_WINSOUND:
                try:
                    src = sound_obj.source()
                    if src and hasattr(src, "toLocalFile"):
                        p = src.toLocalFile()
                        if os.path.isfile(p):
                            # winsound doesn't support volume, so just play at system volume
                            winsound.PlaySound(
                                p, winsound.SND_FILENAME | winsound.SND_ASYNC
                            )
                except Exception:
                    pass
        except Exception:
            pass

    def play_startup(self):
        self.play_sound(self.startup_sound)

    def play_fire(self):
        self.play_sound(self.fire_sound)

    def play_detect(self):
        self.play_sound(self.detect_sound)

    # ------------------------------------
    # TOP BAR (ARM / SAFE)
    # ------------------------------------
    def _create_top_bar(self):
        w = QWidget()
        layout = QHBoxLayout(w)
        layout.setContentsMargins(8, 4, 8, 4)

        self.arm_toggle_btn = QPushButton("ARM SYSTEM")
        self.arm_toggle_btn.setCheckable(True)
        self.arm_toggle_btn.toggled.connect(self._on_arm_toggled)
        # Fire indicator: small circular widget that pulses when host requests a fire
        self.fire_indicator = QLabel()
        try:
            self.fire_indicator.setFixedSize(12, 12)
            self.fire_indicator.setToolTip(
                "Indicates a requested fire event from the host. Pulses when a fire is requested and remains extended when the MCU confirms the action."
            )
            self.fire_indicator.setStyleSheet(
                "background: lightgray; border: 1px solid #222; border-radius: 6px;"
            )
        except Exception:
            pass

        self.status_label = QLabel("SYSTEM: SAFE")
        # Use explicit horizontal+vertical centering
        self.status_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # Place arm button and indicator together so the indicator is always visible
        layout.addWidget(self.arm_toggle_btn)
        try:
            layout.addWidget(self.fire_indicator)
        except Exception:
            pass
        layout.addStretch()
        layout.addWidget(self.status_label)
        return w

    def pulse_fire_indicator(self, pulse_ms: int = 400, confirmed: bool = False):
        """Pulse the small fire indicator in the top bar. This method
        respects the host's `safety_state` if available (only pulses when
        `safety_state == 0` which means ARMED).
        """
        try:
            # Respect Safety state on the main window if available
            try:
                if getattr(self.main, "safety_state", 1) != 0:
                    return
            except Exception:
                pass
            if getattr(self, "fire_indicator", None) is None:
                return
            dur = int(pulse_ms if not confirmed else max(pulse_ms, 1000))
            try:
                self.fire_indicator.setStyleSheet(
                    "background: red; border: 1px solid #400; border-radius: 6px;"
                )
            except Exception:
                pass

            def _restore():
                try:
                    if getattr(self, "fire_indicator", None) is not None:
                        self.fire_indicator.setStyleSheet(
                            "background: lightgray; border: 1px solid #222; border-radius: 6px;"
                        )
                except Exception:
                    pass

            try:
                QTimer.singleShot(dur, _restore)
            except Exception:
                pass
        except Exception:
            pass

    def _on_arm_toggled(self, checked):
        try:
            self.status_label.setText("SYSTEM: ARMED" if checked else "SYSTEM: SAFE")
            if checked:
                self.play_sound(self.armed_sound)
            else:
                disarm_path = self.sound_paths.get("disarmed", (None, None))[0]
                if disarm_path:
                    tmp = self._create_sound(disarm_path, 0.8)
                    if tmp:
                        self.play_sound(tmp)
        except Exception:
            pass

    # ------------------------------------
    # STATUS BAR
    # ------------------------------------
    def _create_status_bar(self):

        sb = QStatusBar()
        self.fps_label = QLabel("FPS: --")
        self.mode_label = QLabel("Mode: --")
        self.serial_status = QLabel("Link: --")
        sb.addWidget(self.fps_label)
        sb.addWidget(self.mode_label)
        sb.addWidget(self.serial_status)
        return sb

    def update_fps(self, fps):
        try:
            self.fps_label.setText(f"FPS: {fps:.1f}")
        except Exception:
            pass

    def update_mode(self, mode_text):
        try:
            self.mode_label.setText(f"Mode: {mode_text}")
        except Exception:
            pass

    def update_serial_status(self, text):
        try:
            self.serial_status.setText(f"Link: {text}")
        except Exception:
            pass

    # ------------------------------------
    # SERIAL CONSOLE
    # ------------------------------------
    def attach_serial_console(self, text_edit):
        try:
            self.serial_widget = text_edit
            if text_edit:
                text_edit.setStyleSheet(
                    """
                    QTextEdit {
                        background-color: #151515;
                        color: #00ff88;
                        font-family: Consolas;
                        font-size: 10pt;
                        border: 1px solid #666;
                        border-radius: 8px;
                    }
                """
                )
        except Exception:
            pass

    def _format_serial_text(self, text):
        """Convert raw serial/command lines into a human-friendly summary for UI display.

        This is display-only: it does not change any serial transmissions. It
        attempts to recognize the "P..T..F.." command string emitted by
        `send_serial_command()` and produce a readable status line. If the
        message doesn't match a known pattern, it is returned unchanged.
        """
        try:
            if text is None:
                return text
            s = str(text).strip()

            # Try to parse the standard packed command: P{pan}T{tilt}F{fire}L{led}R{laser}G{acc3}S{safety}M{mode}
            m = re.search(r"P(-?\d+).*?T(-?\d+).*?F(\d).*?L(\d).*?R(\d).*?G(\d).*?S(\d).*?M(\d)", s)
            if m:
                try:
                    pan = int(m.group(1))
                    tilt = int(m.group(2))
                    fire_tok = int(m.group(3))
                    led_tok = int(m.group(4))
                    laser_tok = int(m.group(5))
                    acc3_tok = int(m.group(6))
                    safety_tok = int(m.group(7))
                    mode_tok = int(m.group(8))
                except Exception:
                    return s

                fire_str = "YES" if fire_tok else "no"
                led_str = "on" if led_tok else "off"
                laser_str = "on" if laser_tok else "off"
                safety_str = "ARMED" if safety_tok == 0 else "SAFE"
                mode_str = "BB" if mode_tok == 1 else "TRACK"

                friendly = (
                    f"TO MCU -> Pan={pan}°, Tilt={tilt}° | Fire={fire_str} | "
                    f"LED={led_str} | Laser={laser_str} | Safety={safety_str} | Mode={mode_str}"
                )

                # Motion/delta hints using last_sent values when available.
                try:
                    last_pan = getattr(self.main, "last_sent_pan", None)
                    last_tilt = getattr(self.main, "last_sent_tilt", None)
                    if last_pan is not None and last_tilt is not None:
                        dp = pan - int(last_pan)
                        dt = tilt - int(last_tilt)
                        dp_abs = abs(dp)
                        dt_abs = abs(dt)
                        sudden = getattr(self.main, "sudden_move_threshold", 8)
                        jitter = getattr(self.main, "jitter_threshold", 2)
                        motion_desc = None
                        if dp_abs >= sudden or dt_abs >= sudden:
                            motion_desc = f"[MOTION] Large move: Pan {dp:+d}°, Tilt {dt:+d}°"
                        elif dp_abs >= jitter or dt_abs >= jitter:
                            motion_desc = f"[MOTION] Adjustment: Pan {dp:+d}°, Tilt {dt:+d}°"
                        elif dp_abs > 0 or dt_abs > 0:
                            motion_desc = f"[MOTION] Small correction: Pan {dp:+d}°, Tilt {dt:+d}°"
                        if motion_desc:
                            friendly = friendly + "   " + motion_desc
                except Exception:
                    pass

                # Preserve the original raw command for reference
                return friendly + f"   (raw: {s})"

            # Return other messages unmodified
            return s
        except Exception:
            return text

    def log_serial_output(self, text, fire=True):
        """Write a line to the serial/log console in a safe, human-friendly form.

        - Converts packed commands (P..T..F..) into readable status lines for the UI
          while preserving the raw command in parentheses.
        - Buffers messages when the main window has `serial_log_paused` set.
        - Marshals UI writes onto the Qt main thread using QTimer.singleShot.
        - Plays the fire sound if the message or flags indicate a fire event.
        """
        try:
            display_text = self._format_serial_text(text)
        except Exception:
            display_text = text

        # Respect a main-window-level "paused" flag and buffer when paused.
        try:
            if getattr(self.main, "serial_log_paused", False):
                try:
                    buf = getattr(self.main, "_serial_log_buffer", None)
                    if buf is None:
                        self.main._serial_log_buffer = [display_text]
                    else:
                        buf.append(display_text)
                        # cap buffer size to avoid runaway memory usage
                        try:
                            max_lines = getattr(self.main, "serial_buffer_max_lines", 2000)
                            if len(buf) > max_lines:
                                # drop oldest
                                del buf[0 : len(buf) - max_lines]
                        except Exception:
                            pass
                except Exception:
                    # If buffering fails, silently drop so we don't block
                    pass
                return
        except Exception:
            # if any error checking main state, fall through and try to write
            pass

        # BULLETPROOF FIX: Try serial_widget first, then fall back to main.serial_output
        serial_widget = self.serial_widget
        if not serial_widget and hasattr(self.main, "serial_output"):
            serial_widget = self.main.serial_output
        
        if not serial_widget:
            return

        # Prefer emitting to main window if it exposes a serial_text_signal
        try:
            sig = getattr(self.main, "serial_text_signal", None)
            if sig is not None:
                try:
                    sig.emit(str(display_text))
                    try:
                        if fire or (isinstance(display_text, str) and "FIRE" in display_text.upper()):
                            self.play_fire()
                    except Exception:
                        pass
                    return
                except Exception:
                    # fall through to direct write if emit fails
                    pass
        except Exception:
            pass

        # FIX (DEC 15): Avoid Qt signal marshaling issues with captured variables
        # Write directly instead of using QTimer to avoid TypeError with QTextCursor
        try:
            try:
                serial_widget.moveCursor(QTextCursor.End)
                # keep the display compact (append adds its own newline)
                serial_widget.insertPlainText(str(display_text).rstrip() + "\n")
                serial_widget.moveCursor(QTextCursor.End)
            except Exception:
                pass
            # play fire sound if flagged or if the text contains FIRE
            try:
                if fire or (isinstance(display_text, str) and "FIRE" in display_text.upper()):
                    self.play_fire()
            except Exception:
                pass
        except Exception:
            # Silent failure - don't block the app
            pass

    # ------------------------------------
    # BUTTON STYLE HELPER
    # ------------------------------------
    def style_toggle_button(self, btn):
        try:
            if not isinstance(btn, QPushButton):
                return
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #333;
                    color: #f0f0f0;
                    border: 1px solid #bdbdbd;
                    border-radius: 8px;
                    padding: 4px 8px;
                }
                QPushButton:hover {
                    background-color: #3a3a3a;
                }
                QPushButton:checked {
                    background-color: #ff3333;
                    border: 1px solid #ff5555;
                    color: white;
                }
            """
            )
        except Exception:
            pass
