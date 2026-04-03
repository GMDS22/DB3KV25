from __future__ import annotations

import queue
import random
import threading
import time
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass(frozen=True)
class ToneRequest:
    freq_hz: int
    duration_ms: int
    gap_ms: int = 25


class SentryV2SoundEngine:
    """Non-blocking procedural tone scheduler for ESP32 buzzer playback."""

    def __init__(self, send_tone: Callable[[int, int], None]):
        self._send_tone = send_tone
        self._enabled = True
        self._queue: "queue.Queue[ToneRequest]" = queue.Queue()
        self._stop = threading.Event()
        self._lock = threading.Lock()
        self._random = random.Random()
        self._cooldowns: dict[str, float] = {}
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-v2-sound", daemon=True)
        self._worker.start()

    def close(self) -> None:
        self._stop.set()
        self._clear_queue()

    def set_enabled(self, enabled: bool) -> None:
        with self._lock:
            self._enabled = bool(enabled)
        if not enabled:
            self._clear_queue()

    def note_settings_changed(self) -> None:
        if not self._allow("settings", 0.12):
            return
        base = self._jitter(820, 70)
        self._enqueue_phrase(
            (base - 90, 36, 18),
            (base + 35, 52, 18),
            (base + 180, 124, 28),
        )

    def note_detection_acquired(self, area_ratio: Optional[float], *, qualified: bool) -> None:
        if not self._allow("detect", 0.45):
            return
        base = self._pitch_from_distance(area_ratio, near_hz=640, far_hz=1320)
        if qualified:
            variants = [
                [
                    (base - 80, 34, 16),
                    (base + 35, 42, 16),
                    (base + 180, 132, 26),
                ],
                [
                    (base + 70, 40, 18),
                    (base - 25, 34, 14),
                    (base + 150, 52, 16),
                    (base + 250, 118, 28),
                ],
            ]
            self._enqueue_phrase(*self._random.choice(variants))
        else:
            self._enqueue_phrase(
                (base - 40, 32, 14),
                (base + 80, 78, 22),
            )

    def note_target_lost(self) -> None:
        if not self._allow("lost", 0.75):
            return
        base = self._jitter(720, 45)
        self._enqueue_phrase(
            (base + 220, 48, 16),
            (base + 120, 52, 18),
            (base - 30, 148, 34),
        )

    def note_tracking_move(self, move_delta: float, area_ratio: Optional[float]) -> None:
        if float(move_delta) < 0.35 or not self._allow("move", 0.16):
            return
        base = self._pitch_from_distance(area_ratio, near_hz=470, far_hz=980)
        freq = int(base + min(180.0, max(0.0, float(move_delta)) * 32.0))
        duration = int(min(118, max(32, 28 + (float(move_delta) * 10.0))))
        if float(move_delta) >= 2.2:
            self._enqueue_phrase(
                (freq - 70, 34, 12),
                (freq + 65, 40, 12),
                (freq + 10, duration, 22),
            )
        else:
            self._enqueue_phrase(
                (freq - 35, 26, 10),
                (freq + 55, duration, 18),
            )

    def note_target_lock(self, area_ratio: Optional[float]) -> None:
        if not self._allow("lock", 0.55):
            return
        base = self._pitch_from_distance(area_ratio, near_hz=860, far_hz=1560)
        self._enqueue_phrase(
            (base - 110, 28, 12),
            (base + 25, 34, 12),
            (base + 170, 44, 14),
            (base + 280, 166, 34),
        )

    def note_fire(self, burst_count: int, area_ratio: Optional[float]) -> None:
        base = self._pitch_from_distance(area_ratio, near_hz=980, far_hz=1750)
        tones = []
        for index in range(max(1, min(3, int(burst_count)))):
            freq = self._jitter(base + (index * 55), 36)
            tones.extend([
                ToneRequest(freq - 60, 24, 8),
                ToneRequest(freq + 25, 62, 18),
            ])
        self._enqueue_sequence(*tones)

    def note_guard_tick(self, *, scanning: bool) -> None:
        if scanning:
            if not self._allow("guard_scan", 1.15):
                return
            patterns = [
                [
                    (410, 34, 14),
                    (565, 46, 16),
                    (720, 134, 26),
                ],
                [
                    (360, 28, 12),
                    (520, 28, 12),
                    (690, 44, 14),
                    (520, 152, 30),
                ],
                [
                    (470, 42, 14),
                    (610, 116, 22),
                    (790, 54, 18),
                ],
            ]
            self._enqueue_phrase(*self._random.choice(patterns))
        else:
            if not self._allow("guard_idle", 1.75):
                return
            patterns = [
                [(330, 34, 14), (460, 118, 24)],
                [(380, 40, 16), (520, 42, 14), (430, 106, 22)],
            ]
            self._enqueue_phrase(*self._random.choice(patterns))

    def note_pir_event(self, sensor_id: int) -> None:
        if not self._allow(f"pir:{int(sensor_id)}", 0.45):
            return
        base = 760 + (int(sensor_id) * 120)
        self._enqueue_phrase(
            (base - 40, 30, 10),
            (base + 80, 38, 12),
            (base + 170, 52, 14),
            (base + 60, 168, 28),
        )

    def _enqueue_phrase(self, *tones: tuple[int, int, int]) -> None:
        requests = []
        for freq_hz, duration_ms, gap_ms in tones:
            requests.append(
                ToneRequest(
                    self._jitter(int(freq_hz), max(12, min(90, int(abs(freq_hz) * 0.04)))),
                    int(duration_ms),
                    int(gap_ms),
                )
            )
        self._enqueue_sequence(*requests)

    def _enabled_locked(self) -> bool:
        return bool(self._enabled)

    def _allow(self, key: str, cooldown_s: float) -> bool:
        now = time.monotonic()
        with self._lock:
            if not self._enabled_locked():
                return False
            last = float(self._cooldowns.get(key, 0.0) or 0.0)
            if now - last < float(cooldown_s):
                return False
            self._cooldowns[key] = now
            return True

    def _enqueue_sequence(self, *tones: ToneRequest) -> None:
        with self._lock:
            if not self._enabled_locked():
                return
        for tone in tones:
            if int(tone.freq_hz) <= 0 or int(tone.duration_ms) <= 0:
                continue
            self._queue.put(tone)

    def _clear_queue(self) -> None:
        while True:
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

    def _worker_loop(self) -> None:
        while not self._stop.is_set():
            try:
                tone = self._queue.get(timeout=0.10)
            except queue.Empty:
                continue
            with self._lock:
                enabled = self._enabled_locked()
            if not enabled:
                continue
            try:
                self._send_tone(int(tone.freq_hz), int(tone.duration_ms))
            except Exception:
                pass
            total_sleep = max(0.0, (int(tone.duration_ms) + int(tone.gap_ms)) / 1000.0)
            if total_sleep > 0.0:
                self._stop.wait(total_sleep)

    def _pitch_from_distance(self, area_ratio: Optional[float], *, near_hz: int, far_hz: int) -> int:
        if area_ratio is None:
            return int((int(near_hz) + int(far_hz)) * 0.5)
        area = max(0.0003, min(0.10, float(area_ratio)))
        t = (area - 0.0003) / (0.10 - 0.0003)
        return int(round(float(far_hz) - ((float(far_hz) - float(near_hz)) * t)))

    def _jitter(self, freq_hz: int, spread_hz: int) -> int:
        return int(max(120, int(freq_hz) + self._random.randint(-int(spread_hz), int(spread_hz))))