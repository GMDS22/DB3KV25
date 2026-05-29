from __future__ import annotations

import math
import threading
import wave
from array import array
from pathlib import Path
from typing import Callable, Dict, Iterable


EVENT_SOUND_NAMES = (
    "target_detected",
    "tracking_engaged",
    "returning_to_standby",
    "acknowledged",
    "command_not_recognized",
)

EVENT_SOUND_STYLE_OPTIONS = [
    ("classic", "Classic"),
    ("droid", "Droid Chirp"),
    ("scanner", "Scanner Sweep"),
]
EVENT_SOUND_STYLE_LABELS = {key: label for key, label in EVENT_SOUND_STYLE_OPTIONS}


_SAMPLE_RATE_HZ = 22050
_PACK_LOCK = threading.Lock()
_READY_PACKS: set[tuple[str, str]] = set()


def normalize_event_sound_style(style_key: str) -> str:
    key = str(style_key or "classic").strip().lower()
    return key if key in EVENT_SOUND_STYLE_LABELS else "classic"


def resolve_event_sound_key(sound_root: str | Path, style_key: str, event_name: str) -> str:
    root = Path(sound_root)
    normalized_event = str(event_name or "").strip().lower()
    if not normalized_event:
        return ""
    style = normalize_event_sound_style(style_key)
    if style == "classic":
        return normalized_event
    pack_dir = ensure_event_sound_pack(root, style)
    try:
        relative_dir = pack_dir.relative_to(root)
    except ValueError:
        return normalized_event
    return (relative_dir / normalized_event).as_posix()


def ensure_event_sound_pack(sound_root: str | Path, style_key: str) -> Path:
    root = Path(sound_root)
    style = normalize_event_sound_style(style_key)
    if style == "classic":
        return root
    pack_dir = root / "_generated_event_packs" / style
    cache_key = (str(root), style)
    with _PACK_LOCK:
        if cache_key in _READY_PACKS and all((pack_dir / f"{event_name}.wav").is_file() for event_name in EVENT_SOUND_NAMES):
            return pack_dir
        pack_dir.mkdir(parents=True, exist_ok=True)
        builder = _STYLE_BUILDERS.get(style, _build_droid_pack)
        builder(pack_dir)
        _READY_PACKS.add(cache_key)
        return pack_dir


def _write_wave(path: Path, samples: array) -> None:
    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(_SAMPLE_RATE_HZ)
        wav_file.writeframes(samples.tobytes())


def _concat_segments(*segments: Iterable[int]) -> array:
    merged = array("h")
    for segment in segments:
        merged.extend(segment)
    return merged


def _silence(duration_s: float) -> array:
    frame_count = max(1, int(round(float(duration_s) * _SAMPLE_RATE_HZ)))
    return array("h", [0]) * frame_count


def _chirp(
    duration_s: float,
    start_hz: float,
    end_hz: float,
    *,
    amplitude: float = 0.5,
    vibrato_hz: float = 0.0,
    vibrato_depth_hz: float = 0.0,
    harmonic_mix: float = 0.24,
    brightness: float = 0.10,
) -> array:
    frame_count = max(1, int(round(float(duration_s) * _SAMPLE_RATE_HZ)))
    phase = 0.0
    samples = array("h")
    for index in range(frame_count):
        t = index / float(_SAMPLE_RATE_HZ)
        progress = index / float(max(1, frame_count - 1))
        freq_hz = float(start_hz) + ((float(end_hz) - float(start_hz)) * progress)
        if vibrato_hz > 0.0 and vibrato_depth_hz > 0.0:
            freq_hz += math.sin(2.0 * math.pi * float(vibrato_hz) * t) * float(vibrato_depth_hz)
        phase += (2.0 * math.pi * freq_hz) / float(_SAMPLE_RATE_HZ)
        env = math.sin(math.pi * progress) ** 0.82
        carrier = (
            math.sin(phase)
            + (float(harmonic_mix) * math.sin((phase * 2.0) + 0.18))
            + (float(brightness) * math.sin((phase * 3.0) + 0.32))
        )
        sample = max(-1.0, min(1.0, carrier * 0.72 * float(amplitude) * env))
        samples.append(int(round(sample * 32767.0)))
    return samples


def _tone(
    duration_s: float,
    freq_hz: float,
    *,
    amplitude: float = 0.46,
    vibrato_hz: float = 0.0,
    vibrato_depth_hz: float = 0.0,
    harmonic_mix: float = 0.14,
) -> array:
    return _chirp(
        duration_s,
        freq_hz,
        freq_hz,
        amplitude=amplitude,
        vibrato_hz=vibrato_hz,
        vibrato_depth_hz=vibrato_depth_hz,
        harmonic_mix=harmonic_mix,
        brightness=0.04,
    )


def _build_pack(pack_dir: Path, renderers: Dict[str, Callable[[], array]]) -> None:
    for event_name in EVENT_SOUND_NAMES:
        renderer = renderers.get(event_name, renderers["acknowledged"])
        _write_wave(pack_dir / f"{event_name}.wav", renderer())


def _build_droid_pack(pack_dir: Path) -> None:
    _build_pack(
        pack_dir,
        {
            "target_detected": lambda: _concat_segments(
                _chirp(0.060, 980, 1580, amplitude=0.56, vibrato_hz=7.0, vibrato_depth_hz=32.0),
                _silence(0.018),
                _chirp(0.072, 1620, 1160, amplitude=0.48, vibrato_hz=10.5, vibrato_depth_hz=46.0),
                _silence(0.016),
                _chirp(0.116, 1040, 1920, amplitude=0.58, vibrato_hz=14.0, vibrato_depth_hz=72.0),
            ),
            "tracking_engaged": lambda: _concat_segments(
                _chirp(0.050, 820, 1340, amplitude=0.46, vibrato_hz=8.5, vibrato_depth_hz=26.0),
                _silence(0.016),
                _chirp(0.062, 1360, 940, amplitude=0.45, vibrato_hz=12.0, vibrato_depth_hz=38.0),
                _silence(0.018),
                _chirp(0.138, 980, 1760, amplitude=0.54, vibrato_hz=16.0, vibrato_depth_hz=84.0),
            ),
            "returning_to_standby": lambda: _concat_segments(
                _chirp(0.080, 1420, 900, amplitude=0.46, vibrato_hz=6.0, vibrato_depth_hz=22.0),
                _silence(0.024),
                _chirp(0.122, 1180, 640, amplitude=0.40, vibrato_hz=9.0, vibrato_depth_hz=28.0),
            ),
            "acknowledged": lambda: _concat_segments(
                _chirp(0.046, 940, 1320, amplitude=0.42, vibrato_hz=8.0, vibrato_depth_hz=20.0),
                _silence(0.014),
                _chirp(0.070, 1180, 1680, amplitude=0.48, vibrato_hz=12.0, vibrato_depth_hz=36.0),
            ),
            "command_not_recognized": lambda: _concat_segments(
                _chirp(0.052, 1240, 920, amplitude=0.42, vibrato_hz=5.5, vibrato_depth_hz=20.0),
                _silence(0.016),
                _chirp(0.060, 980, 1520, amplitude=0.46, vibrato_hz=11.0, vibrato_depth_hz=40.0),
                _silence(0.020),
                _chirp(0.124, 1340, 700, amplitude=0.42, vibrato_hz=7.0, vibrato_depth_hz=32.0),
            ),
        },
    )


def _build_scanner_pack(pack_dir: Path) -> None:
    _build_pack(
        pack_dir,
        {
            "target_detected": lambda: _concat_segments(
                _tone(0.040, 920, amplitude=0.38),
                _silence(0.014),
                _tone(0.048, 1180, amplitude=0.42),
                _silence(0.016),
                _chirp(0.090, 1280, 1740, amplitude=0.50),
            ),
            "tracking_engaged": lambda: _concat_segments(
                _tone(0.034, 760, amplitude=0.34),
                _silence(0.012),
                _tone(0.040, 980, amplitude=0.38),
                _silence(0.012),
                _chirp(0.112, 1020, 1580, amplitude=0.46),
            ),
            "returning_to_standby": lambda: _concat_segments(
                _chirp(0.078, 1360, 980, amplitude=0.38),
                _silence(0.020),
                _chirp(0.116, 1040, 680, amplitude=0.34),
            ),
            "acknowledged": lambda: _concat_segments(
                _tone(0.034, 980, amplitude=0.34),
                _silence(0.012),
                _tone(0.060, 1420, amplitude=0.42),
            ),
            "command_not_recognized": lambda: _concat_segments(
                _tone(0.032, 1260, amplitude=0.34),
                _silence(0.014),
                _tone(0.036, 920, amplitude=0.32),
                _silence(0.016),
                _chirp(0.116, 1080, 740, amplitude=0.36),
            ),
        },
    )


_STYLE_BUILDERS = {
    "droid": _build_droid_pack,
    "scanner": _build_scanner_pack,
}