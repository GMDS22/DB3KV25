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


@dataclass(frozen=True)
class SoundPersonalityProfile:
    pitch_bias_hz: int
    duration_scale: float
    gap_scale: float
    cooldown_scale: float
    jitter_scale: float
    fire_step_hz: int


SOUND_PERSONALITY_PROFILES: dict[str, SoundPersonalityProfile] = {
    "sentinel": SoundPersonalityProfile(0, 1.00, 1.00, 1.00, 1.00, 55),
    "hunter": SoundPersonalityProfile(140, 0.88, 0.85, 0.74, 1.25, 78),
    "stealth": SoundPersonalityProfile(-120, 1.20, 1.15, 1.18, 0.60, 42),
    "playful": SoundPersonalityProfile(85, 1.04, 0.96, 0.90, 1.45, 64),
}


class SentryV2SoundEngine:
    """Non-blocking procedural tone scheduler for Smart Sentry board-buzzer playback."""

    def __init__(self, send_tone: Callable[[int, int], None]):
        self._send_tone = send_tone
        self._enabled = True
        self._queue: "queue.Queue[ToneRequest]" = queue.Queue()
        self._stop = threading.Event()
        self._lock = threading.Lock()
        self._random = random.Random()
        self._cooldowns: dict[str, float] = {}
        self._personality = "sentinel"
        self._attitude_pct = 60
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

    def set_profile(self, personality: str, attitude_pct: int = 60) -> None:
        profile_key = str(personality or "sentinel").strip().lower()
        if profile_key not in SOUND_PERSONALITY_PROFILES:
            profile_key = "sentinel"
        with self._lock:
            self._personality = profile_key
            self._attitude_pct = int(max(0, min(100, int(attitude_pct))))

    def note_settings_changed(self) -> None:
        if not self._allow("settings", 0.12):
            return
        profile = self._profile()
        base = self._jitter(820 + profile.pitch_bias_hz, int(70 * profile.jitter_scale))
        self._enqueue_phrase(
            (base - 90, 36, 18),
            (base + 35, 52, 18),
            (base + 180, 124, 28),
            accent=0.45,
        )

    def note_detection_acquired(self, area_ratio: Optional[float], *, qualified: bool) -> None:
        if not self._allow("detect", 0.45):
            return
        base = self._pitch_from_distance(area_ratio, near_hz=640, far_hz=1320)
        if qualified:
            variants = self._qualified_detection_variants(base)
            self._enqueue_phrase(*self._random.choice(variants), accent=0.65)
        else:
            self._enqueue_phrase(
                (base - 40, 32, 14),
                (base + 80, 78, 22),
                accent=0.25,
            )

    def note_target_lost(self) -> None:
        if not self._allow("lost", 0.75):
            return
        base = self._jitter(720 + self._profile().pitch_bias_hz, int(45 * self._profile().jitter_scale))
        variants = self._lost_variants(base)
        self._enqueue_phrase(*self._random.choice(variants), accent=0.35)

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
                accent=0.55,
            )
        else:
            self._enqueue_phrase(
                (freq - 35, 26, 10),
                (freq + 55, duration, 18),
                accent=0.30,
            )

    def note_target_lock(self, area_ratio: Optional[float]) -> None:
        if not self._allow("lock", 0.55):
            return
        base = self._pitch_from_distance(area_ratio, near_hz=860, far_hz=1560)
        variants = self._lock_variants(base)
        self._enqueue_phrase(*self._random.choice(variants), accent=0.85)

    def note_fire(self, burst_count: int, area_ratio: Optional[float]) -> None:
        base = self._pitch_from_distance(area_ratio, near_hz=980, far_hz=1750)
        step_hz = self._profile().fire_step_hz
        tones = []
        for index in range(max(1, min(3, int(burst_count)))):
            freq = self._jitter(base + (index * step_hz), int(36 * self._profile().jitter_scale))
            tones.extend([
                self._build_tone_request(freq - 60, 24, 8, accent=0.92),
                self._build_tone_request(freq + 25, 62, 18, accent=1.0),
            ])
        self._enqueue_sequence(*tones)

    def note_guard_tick(self, *, scanning: bool) -> None:
        if scanning:
            if not self._allow("guard_scan", 1.15):
                return
            self._enqueue_phrase(*self._random.choice(self._guard_scan_patterns()), accent=0.40)
        else:
            if not self._allow("guard_idle", 1.75):
                return
            self._enqueue_phrase(*self._random.choice(self._guard_idle_patterns()), accent=0.18)

    def note_rest_position(self, *, closing: bool = False) -> None:
        cooldown_key = "rest_close" if closing else "rest"
        if not self._allow(cooldown_key, 0.65 if closing else 0.35):
            return
        base = self._jitter(560 + self._profile().pitch_bias_hz, int(42 * self._profile().jitter_scale))
        if closing:
            self._enqueue_phrase(
                (base + 130, 34, 12),
                (base + 30, 48, 14),
                (base - 70, 136, 26),
                accent=0.22,
            )
            return
        self._enqueue_phrase(
            (base - 35, 30, 10),
            (base + 85, 40, 12),
            (base - 10, 92, 22),
            accent=0.30,
        )

    def note_home_position(self, *, waking_from_rest: bool = False) -> None:
        cooldown_key = "home_wake" if waking_from_rest else "home"
        if not self._allow(cooldown_key, 0.55 if waking_from_rest else 0.35):
            return
        base = self._jitter(760 + self._profile().pitch_bias_hz, int(40 * self._profile().jitter_scale))
        if waking_from_rest:
            self._enqueue_phrase(
                (base - 120, 44, 16),
                (base - 30, 58, 18),
                (base + 95, 118, 24),
                (base + 210, 150, 28),
                accent=0.42,
            )
            return
        self._enqueue_phrase(
            (base - 70, 28, 10),
            (base + 40, 38, 12),
            (base + 160, 108, 22),
            accent=0.48,
        )

    def note_pir_event(self, sensor_id: int) -> None:
        if not self._allow(f"pir:{int(sensor_id)}", 0.45):
            return
        base = 760 + (int(sensor_id) * 120)
        self._enqueue_phrase(
            (base - 40, 30, 10),
            (base + 80, 38, 12),
            (base + 170, 52, 14),
            (base + 60, 168, 28),
            accent=0.50,
        )

    def note_identity_recognized(self, name: str, *, friendly: bool = True) -> None:
        cleaned = "".join(ch for ch in str(name or "").upper() if ch.isalnum() or ch == " ").strip()
        if not cleaned:
            return
        key = f"identity:{cleaned.lower()}"
        if not self._allow(key, 1.5 if friendly else 2.2):
            return
        intro_base = 820 if friendly else 720
        intro = [
            (intro_base - 80, 26, 10),
            (intro_base + 35, 34, 12),
        ]
        letters = cleaned[:8]
        phrase: list[tuple[int, int, int]] = list(intro)
        for index, char in enumerate(letters):
            code = ord(char)
            if char == " ":
                phrase.append((intro_base - 120, 20, 38))
                continue
            freq = 560 + ((code % 17) * 42) + (index * 18)
            duration = 42 if char in "AEIOU0123456789" else 28
            gap = 14 if index < len(letters) - 1 else 24
            phrase.append((freq, duration, gap))
        tail_base = 1040 if friendly else 900
        phrase.extend([
            (tail_base - 40, 58, 14),
            (tail_base + 110, 92, 20),
        ])
        self._enqueue_phrase(*phrase, accent=0.58 if friendly else 0.32)

    def _enqueue_phrase(self, *tones: tuple[int, int, int], accent: float = 0.0) -> None:
        requests = []
        for freq_hz, duration_ms, gap_ms in tones:
            requests.append(self._build_tone_request(freq_hz, duration_ms, gap_ms, accent=accent))
        self._enqueue_sequence(*requests)

    def _enabled_locked(self) -> bool:
        return bool(self._enabled)

    def _allow(self, key: str, cooldown_s: float) -> bool:
        now = time.monotonic()
        with self._lock:
            if not self._enabled_locked():
                return False
            last = float(self._cooldowns.get(key, 0.0) or 0.0)
            if now - last < self._scaled_cooldown(float(cooldown_s)):
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
            return self._apply_pitch_style(int((int(near_hz) + int(far_hz)) * 0.5), accent=0.25)
        area = max(0.0003, min(0.10, float(area_ratio)))
        t = (area - 0.0003) / (0.10 - 0.0003)
        return self._apply_pitch_style(int(round(float(far_hz) - ((float(far_hz) - float(near_hz)) * t))), accent=0.25)

    def _jitter(self, freq_hz: int, spread_hz: int) -> int:
        return int(max(120, int(freq_hz) + self._random.randint(-int(spread_hz), int(spread_hz))))

    def _profile(self) -> SoundPersonalityProfile:
        return SOUND_PERSONALITY_PROFILES.get(self._personality, SOUND_PERSONALITY_PROFILES["sentinel"])

    def _attitude_mix(self) -> float:
        return max(0.0, min(1.0, float(self._attitude_pct) / 100.0))

    def _scaled_cooldown(self, cooldown_s: float) -> float:
        profile = self._profile()
        attitude = self._attitude_mix()
        return max(0.05, float(cooldown_s) * profile.cooldown_scale * (1.08 - (0.28 * attitude)))

    def _apply_pitch_style(self, freq_hz: int, *, accent: float) -> int:
        profile = self._profile()
        attitude = self._attitude_mix()
        accent_shift = int(round((40.0 * accent) + (55.0 * attitude * accent)))
        return int(max(120, int(freq_hz) + profile.pitch_bias_hz + accent_shift))

    def _build_tone_request(self, freq_hz: int, duration_ms: int, gap_ms: int, *, accent: float = 0.0) -> ToneRequest:
        profile = self._profile()
        attitude = self._attitude_mix()
        styled_freq = self._apply_pitch_style(int(freq_hz), accent=accent)
        spread = max(10, min(120, int(abs(freq_hz) * 0.04 * profile.jitter_scale * (0.70 + (0.70 * attitude)))))
        duration_scale = profile.duration_scale * (1.05 - (0.18 * attitude))
        gap_scale = profile.gap_scale * (1.02 - (0.12 * attitude))
        return ToneRequest(
            self._jitter(styled_freq, spread),
            max(18, int(round(int(duration_ms) * duration_scale))),
            max(6, int(round(int(gap_ms) * gap_scale))),
        )

    def _qualified_detection_variants(self, base: int) -> list[list[tuple[int, int, int]]]:
        personality = self._personality
        if personality == "hunter":
            return [
                [(base - 60, 28, 10), (base + 80, 34, 12), (base + 240, 110, 22)],
                [(base + 20, 24, 10), (base + 140, 30, 10), (base + 280, 118, 20)],
            ]
        if personality == "stealth":
            return [
                [(base - 120, 38, 18), (base - 20, 56, 22), (base + 70, 138, 28)],
                [(base - 90, 34, 16), (base + 10, 44, 18), (base + 90, 128, 26)],
            ]
        if personality == "playful":
            return [
                [(base - 20, 22, 10), (base + 95, 28, 10), (base + 10, 34, 10), (base + 210, 118, 24)],
                [(base + 60, 26, 10), (base - 40, 24, 10), (base + 140, 36, 12), (base + 250, 124, 24)],
            ]
        return [
            [(base - 80, 34, 16), (base + 35, 42, 16), (base + 180, 132, 26)],
            [(base + 70, 40, 18), (base - 25, 34, 14), (base + 150, 52, 16), (base + 250, 118, 28)],
        ]

    def _lost_variants(self, base: int) -> list[list[tuple[int, int, int]]]:
        personality = self._personality
        if personality == "hunter":
            return [[(base + 260, 30, 10), (base + 110, 42, 12), (base - 60, 116, 26)]]
        if personality == "stealth":
            return [[(base + 90, 42, 18), (base + 10, 58, 20), (base - 110, 170, 34)]]
        if personality == "playful":
            return [[(base + 200, 32, 12), (base + 40, 30, 10), (base + 110, 34, 12), (base - 50, 124, 26)]]
        return [[(base + 220, 48, 16), (base + 120, 52, 18), (base - 30, 148, 34)]]

    def _lock_variants(self, base: int) -> list[list[tuple[int, int, int]]]:
        personality = self._personality
        if personality == "hunter":
            return [[(base - 90, 24, 10), (base + 60, 28, 10), (base + 240, 36, 12), (base + 360, 138, 28)]]
        if personality == "stealth":
            return [[(base - 140, 30, 14), (base - 20, 36, 16), (base + 95, 52, 16), (base + 180, 180, 32)]]
        if personality == "playful":
            return [[(base - 40, 24, 10), (base + 110, 26, 10), (base + 20, 28, 10), (base + 260, 148, 28)]]
        return [[(base - 110, 28, 12), (base + 25, 34, 12), (base + 170, 44, 14), (base + 280, 166, 34)]]

    def _guard_scan_patterns(self) -> list[list[tuple[int, int, int]]]:
        personality = self._personality
        if personality == "hunter":
            return [
                [(450, 26, 10), (620, 32, 12), (860, 88, 18)],
                [(520, 22, 8), (710, 24, 10), (910, 98, 20)],
            ]
        if personality == "stealth":
            return [
                [(300, 42, 18), (430, 66, 20), (590, 144, 28)],
                [(340, 34, 16), (480, 54, 18), (640, 132, 28)],
            ]
        if personality == "playful":
            return [
                [(430, 24, 8), (600, 22, 8), (520, 24, 8), (760, 118, 22)],
                [(500, 24, 8), (650, 24, 8), (820, 40, 12), (610, 126, 24)],
            ]
        return [
            [(410, 34, 14), (565, 46, 16), (720, 134, 26)],
            [(360, 28, 12), (520, 28, 12), (690, 44, 14), (520, 152, 30)],
            [(470, 42, 14), (610, 116, 22), (790, 54, 18)],
        ]

    def _guard_idle_patterns(self) -> list[list[tuple[int, int, int]]]:
        personality = self._personality
        if personality == "hunter":
            return [[(360, 22, 8), (520, 78, 16)], [(410, 24, 8), (590, 82, 16)]]
        if personality == "stealth":
            return [[(250, 48, 20), (360, 132, 26)], [(280, 54, 22), (390, 140, 28)]]
        if personality == "playful":
            return [[(350, 22, 8), (500, 28, 10), (410, 98, 18)], [(390, 22, 8), (560, 24, 8), (470, 104, 18)]]
        return [[(330, 34, 14), (460, 118, 24)], [(380, 40, 16), (520, 42, 14), (430, 106, 22)]]