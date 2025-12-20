from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable, Optional, Tuple

from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtWidgets import QMessageBox, QProgressDialog


@dataclass
class RangeCheckResult:
    ok: bool
    cancelled: bool
    issues: Tuple[str, ...]
    details: Tuple[str, ...]


class PanTiltRangeCheck(QObject):
    """Non-blocking pan/tilt sweep intended for quick hardware validation.

    Design goals:
    - Never blocks the Qt UI thread.
    - Temporarily pauses tracking/detection to avoid fights.
    - Restores the prior runtime state when done/cancelled.
    - Best-effort tilt movement confirmation via encoder feedback when available.
    """

    def __init__(self, app: Any, on_finished: Optional[Callable[[RangeCheckResult], None]] = None):
        super().__init__(app)
        self._app = app
        self._on_finished = on_finished
        self._timer: Optional[QTimer] = None
        self._progress: Optional[QProgressDialog] = None

        self._saved_state: dict[str, Any] = {}

        # encoder-based movement confirmation
        self._encoder_supported = False
        self._encoder_samples: list[Tuple[float, float]] = []  # (t, tilt)
        self._last_encoder_poll = 0.0

        # sweep state
        self._phase = "idle"
        self._phase_start = 0.0
        self._cancelled = False

        self._pan_min = 0
        self._pan_max = 180
        self._tilt_min = 0
        self._tilt_max = 90
        self._pan_mid = 90
        self._tilt_mid = 45

        self._step_deg = 1
        self._interval_ms = 80

        # For encoder-based confirmation, avoid the known clamp region (<18°)
        self._tilt_confirm_min = 20
        self._tilt_confirm_max = 70

    def start(self) -> None:
        self._capture_state()
        self._prepare_for_test()

        self._compute_ranges()
        self._phase = "pan_forward"
        self._phase_start = time.time()

        self._progress = QProgressDialog(
            "Running slow pan/tilt range check...",
            "Cancel",
            0,
            100,
            self._app,
        )
        try:
            self._progress.setWindowTitle("Hardware Test")
            self._progress.setMinimumDuration(0)
            self._progress.setAutoClose(False)
            self._progress.setAutoReset(False)
        except Exception:
            pass
        self._progress.canceled.connect(self.cancel)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(self._interval_ms)

        self._log("[HWTEST] Pan/Tilt range check started")

    def cancel(self) -> None:
        self._cancelled = True

    def _compute_ranges(self) -> None:
        app = self._app
        self._pan_min = int(getattr(app, "PAN_MIN", 0))
        self._pan_max = int(getattr(app, "PAN_MAX", 220))
        self._tilt_min = int(getattr(app, "TILT_MIN", 0))
        self._tilt_max = int(getattr(app, "TILT_MAX", 70))

        # Midpoints used to isolate each axis during the other axis sweep.
        self._pan_mid = int(round((self._pan_min + self._pan_max) / 2.0))
        self._tilt_mid = int(round((self._tilt_min + self._tilt_max) / 2.0))

        self._tilt_confirm_min = max(self._tilt_min, 20)
        self._tilt_confirm_max = min(self._tilt_max, 70)

    def _capture_state(self) -> None:
        a = self._app
        self._saved_state = {
            "tracking_active": bool(getattr(a, "tracking_active", False)),
            "aiming_active": bool(getattr(a, "aiming_active", False)),
            "detection_enabled": bool(getattr(a, "detection_enabled", False)),
            "serial_tx_paused": bool(getattr(a, "serial_tx_paused", False)),
            "target_pan": float(getattr(a, "target_pan", getattr(a, "HOME_PAN", 90))),
            "target_tilt": float(getattr(a, "target_tilt", getattr(a, "HOME_TILT", 40))),
        }

    def _prepare_for_test(self) -> None:
        a = self._app

        # Cancel/stop any active tracking loop so it doesn't fight the test.
        try:
            if getattr(a, "tracking_active", False):
                a.stop_tracking()
        except Exception:
            try:
                a.tracking_active = False
            except Exception:
                pass

        # Disable detection flag as a courtesy (some modes still run regardless).
        try:
            a.detection_enabled = False
        except Exception:
            pass

        # Ensure servos are enabled for the sweep.
        try:
            if hasattr(a, "toggle_aiming"):
                a.toggle_aiming(True)
            else:
                a.aiming_active = True
        except Exception:
            try:
                a.aiming_active = True
            except Exception:
                pass

        # Determine whether encoder feedback is available for confirmation.
        self._encoder_supported = bool(
            getattr(a, "tilt_encoder_enabled", False)
            and getattr(a, "tilt_pid_enabled", False)
        )

        if self._saved_state.get("serial_tx_paused"):
            self._log("[HWTEST] WARNING: TX Pause is enabled; movement cannot be verified")

    def _restore_state(self) -> None:
        a = self._app
        st = self._saved_state

        try:
            a.detection_enabled = bool(st.get("detection_enabled", False))
        except Exception:
            pass

        # Restore aim/tracking in a safe order.
        try:
            if bool(st.get("tracking_active", False)):
                a.start_tracking()
            else:
                # restore aiming state if tracking was not active
                if hasattr(a, "toggle_aiming"):
                    a.toggle_aiming(bool(st.get("aiming_active", False)))
                else:
                    a.aiming_active = bool(st.get("aiming_active", False))
        except Exception:
            pass

        # Restore original target values (best-effort)
        try:
            a.target_pan = float(st.get("target_pan", a.target_pan))
            a.target_tilt = float(st.get("target_tilt", a.target_tilt))
        except Exception:
            pass

    def _set_targets(self, pan: int, tilt: int) -> None:
        a = self._app
        try:
            a.target_pan = float(pan)
            a.target_tilt = float(tilt)
        except Exception:
            return

        try:
            a.send_serial_command()
        except Exception:
            pass

    def _poll_encoder(self) -> None:
        a = self._app
        now = time.time()
        if not self._encoder_supported:
            return
        if now - self._last_encoder_poll < 0.10:
            return
        self._last_encoder_poll = now

        try:
            # Request an update; parse happens asynchronously when serial reads occur.
            if hasattr(a, "request_encoder_feedback"):
                a.request_encoder_feedback()
        except Exception:
            pass

        try:
            tilt_pos = float(getattr(a, "tilt_encoder_position", 0.0))
            self._encoder_samples.append((now, tilt_pos))
        except Exception:
            pass

    def _tick(self) -> None:
        if self._cancelled:
            self._finish(cancelled=True)
            return

        a = self._app

        # Basic progress: treat phases as 4 equal chunks.
        try:
            if self._progress is not None:
                phase_index = {
                    "pan_forward": 0,
                    "pan_back": 1,
                    "tilt_down": 2,
                    "tilt_up": 3,
                }.get(self._phase, 0)
                elapsed = max(0.0, time.time() - self._phase_start)
                # assume ~20s per phase worst-case
                pct = int(min(99, phase_index * 25 + min(25, (elapsed / 20.0) * 25)))
                self._progress.setValue(pct)
        except Exception:
            pass

        pan = int(round(float(getattr(a, "target_pan", self._pan_mid))))
        tilt = int(round(float(getattr(a, "target_tilt", self._tilt_mid))))

        if self._phase == "pan_forward":
            if tilt != self._tilt_mid:
                tilt = self._tilt_mid
            pan = min(self._pan_max, pan + self._step_deg)
            self._set_targets(pan, tilt)
            if pan >= self._pan_max:
                self._phase = "pan_back"
                self._phase_start = time.time()

        elif self._phase == "pan_back":
            if tilt != self._tilt_mid:
                tilt = self._tilt_mid
            pan = max(self._pan_min, pan - self._step_deg)
            self._set_targets(pan, tilt)
            if pan <= self._pan_min:
                self._phase = "tilt_down"
                self._phase_start = time.time()
                # park at pan mid for tilt test
                self._set_targets(self._pan_mid, tilt)

        elif self._phase == "tilt_down":
            if pan != self._pan_mid:
                pan = self._pan_mid
            # move within the full safe range
            tilt = max(self._tilt_min, tilt - self._step_deg)
            self._set_targets(pan, tilt)
            self._poll_encoder()
            if tilt <= self._tilt_min:
                self._phase = "tilt_up"
                self._phase_start = time.time()

        elif self._phase == "tilt_up":
            if pan != self._pan_mid:
                pan = self._pan_mid
            tilt = min(self._tilt_max, tilt + self._step_deg)
            self._set_targets(pan, tilt)
            self._poll_encoder()
            if tilt >= self._tilt_max:
                self._finish(cancelled=False)

        else:
            self._finish(cancelled=False)

    def _finish(self, cancelled: bool) -> None:
        # stop timer first
        try:
            if self._timer is not None:
                self._timer.stop()
        except Exception:
            pass

        try:
            if self._progress is not None:
                self._progress.setValue(100)
                self._progress.close()
        except Exception:
            pass

        result = self._analyze(cancelled=cancelled)
        self._restore_state()
        self._show_result(result)

        if callable(self._on_finished):
            try:
                self._on_finished(result)
            except Exception:
                pass

    def _analyze(self, cancelled: bool) -> RangeCheckResult:
        issues: list[str] = []
        details: list[str] = []

        a = self._app
        try:
            ser_open = bool(getattr(a, "ser", None) is not None and getattr(a.ser, "is_open", False))
        except Exception:
            ser_open = False

        if not ser_open:
            issues.append("Serial not connected (cannot verify movement)")

        if bool(getattr(a, "serial_tx_paused", False)):
            issues.append("TX Pause is enabled (commands suppressed)")

        details.append(f"Pan sweep: {self._pan_min}° → {self._pan_max}° → {self._pan_min}°")
        details.append(f"Tilt sweep: {self._tilt_min}° → {self._tilt_max}°")

        # Best-effort tilt movement confirmation.
        if self._encoder_supported and self._encoder_samples:
            tilts = [v for (_, v) in self._encoder_samples]
            tmin = min(tilts)
            tmax = max(tilts)
            moved = (tmax - tmin) >= 2.0
            details.append(f"Encoder tilt observed: min={tmin:.1f}° max={tmax:.1f}°")
            if not moved:
                issues.append(
                    "No tilt movement detected via encoder (check tilt servo wiring/power, encoder, or firmware pin mapping)"
                )
        else:
            details.append(
                "Encoder confirmation unavailable (tilt encoder/PID not enabled); cannot automatically confirm physical tilt motion."
            )

        if cancelled:
            return RangeCheckResult(ok=False, cancelled=True, issues=tuple(issues or ["Cancelled"]), details=tuple(details))

        ok = len(issues) == 0
        return RangeCheckResult(ok=ok, cancelled=False, issues=tuple(issues), details=tuple(details))

    def _show_result(self, result: RangeCheckResult) -> None:
        title = "Pan/Tilt Range Check"
        if result.cancelled:
            icon = QMessageBox.Warning
            headline = "Cancelled"
        elif result.ok:
            icon = QMessageBox.Information
            headline = "Completed successfully"
        else:
            icon = QMessageBox.Critical
            headline = "Issues detected"

        lines = [headline]
        if result.issues:
            lines.append("")
            lines.append("Issues:")
            lines.extend([f"- {i}" for i in result.issues])
        if result.details:
            lines.append("")
            lines.append("Details:")
            lines.extend([f"- {d}" for d in result.details])

        msg = "\n".join(lines)

        try:
            QMessageBox(icon, title, msg, QMessageBox.Ok, self._app).exec_()
        except Exception:
            # best-effort fallback
            self._log(f"[HWTEST] {title}: {msg}")

        self._log("[HWTEST] Pan/Tilt range check finished")

    def _log(self, text: str) -> None:
        a = self._app
        try:
            if hasattr(a, "enhancer") and a.enhancer is not None:
                a.enhancer.log_serial_output(text, fire=False)
            else:
                print(text)
        except Exception:
            try:
                print(text)
            except Exception:
                pass
