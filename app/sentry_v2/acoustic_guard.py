from __future__ import annotations

import json
import math
import threading
import time
from pathlib import Path
from typing import Callable, List, Optional

import logging

import numpy as np

_log = logging.getLogger(__name__)


class USBMicrophoneAnomalyDetector:
    """Adaptive USB microphone anomaly detector.

    Uses a rolling baseline (EWMA mean/variance) so the detector adapts to
    the surrounding environment and only raises events for unusual spikes.
    """

    def __init__(
        self,
        on_anomaly: Callable[[float, float], None],
        *,
        sample_rate_hz: int = 16000,
        block_size: int = 1024,
        warmup_seconds: float = 3.0,
        baseline_adapt_rate: float = 0.035,
        anomaly_threshold_db: float = 8.0,
        anomaly_zscore_threshold: float = 2.8,
        cooldown_s: float = 8.0,
        device_name: str = "",
        on_wake_word: Optional[Callable[[str], None]] = None,
        wake_word: str = "",
        vosk_model_path: str = "",
    ) -> None:
        self._on_anomaly = on_anomaly
        self._on_wake_word = on_wake_word or (lambda _word: None)
        self.sample_rate_hz = int(max(8000, sample_rate_hz))
        self.block_size = int(max(128, block_size))
        self.warmup_seconds = float(max(0.5, warmup_seconds))
        self.baseline_adapt_rate = float(min(0.25, max(0.001, baseline_adapt_rate)))
        self.anomaly_threshold_db = float(max(1.0, anomaly_threshold_db))
        self.anomaly_zscore_threshold = float(max(0.5, anomaly_zscore_threshold))
        self.cooldown_s = float(max(0.5, cooldown_s))
        self.device_name = str(device_name or "").strip()
        self.wake_word = str(wake_word or "").strip().lower()
        self.vosk_model_path = str(vosk_model_path or "").strip()
        self._minimum_anomaly_duration_s = 0.18
        self._wake_word_buffer: bytes = b""
        self._last_wake_word_check = 0.0
        # Vosk recognizer is created once and reused (not per-call) to avoid heap thrash.
        self._wake_recognizer = None
        self._wake_recognizer_ready = False

        self._thread: Optional[threading.Thread] = None
        self._stop = threading.Event()
        self._last_error: str = ""
        self._running: bool = False

    @property
    def running(self) -> bool:
        return bool(self._running)

    @property
    def last_error(self) -> str:
        return str(self._last_error or "")

    def update_settings(
        self,
        *,
        sample_rate_hz: int,
        block_size: int,
        warmup_seconds: float,
        baseline_adapt_rate: float,
        anomaly_threshold_db: float,
        anomaly_zscore_threshold: float,
        cooldown_s: float,
        device_name: str,
        wake_word: str = "",
        vosk_model_path: str = "",
    ) -> None:
        self.sample_rate_hz = int(max(8000, sample_rate_hz))
        self.block_size = int(max(128, block_size))
        self.warmup_seconds = float(max(0.5, warmup_seconds))
        self.baseline_adapt_rate = float(min(0.25, max(0.001, baseline_adapt_rate)))
        self.anomaly_threshold_db = float(max(1.0, anomaly_threshold_db))
        self.anomaly_zscore_threshold = float(max(0.5, anomaly_zscore_threshold))
        self.cooldown_s = float(max(0.5, cooldown_s))
        self.device_name = str(device_name or "").strip()
        self.wake_word = str(wake_word or "").strip().lower()
        if vosk_model_path:
            new_path = str(vosk_model_path).strip()
            if new_path != self.vosk_model_path:
                self.vosk_model_path = new_path
                # Invalidate cached recognizer so it rebuilds on next check.
                self._wake_recognizer = None
                self._wake_recognizer_ready = False

    def start(self) -> None:
        if self._thread is not None and self._thread.is_alive():
            return
        self._stop.clear()
        self._last_error = ""
        self._thread = threading.Thread(target=self._run, name="sentry-v2-acoustic-guard", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        thread = self._thread
        self._thread = None
        if thread is not None and thread.is_alive():
            thread.join(timeout=1.0)
        self._running = False

    def _required_anomaly_blocks(self) -> int:
        block_duration_s = float(self.block_size) / float(max(1, self.sample_rate_hz))
        return max(2, int(math.ceil(self._minimum_anomaly_duration_s / max(1e-3, block_duration_s))))

    def _resolve_input_device(self, sd_module) -> Optional[int]:
        target = self.device_name.lower().strip()
        if not target:
            return None
        try:
            devices = sd_module.query_devices()
        except Exception:
            return None
        for index, info in enumerate(devices):
            try:
                channels = int(info.get("max_input_channels", 0) or 0)
                name = str(info.get("name", "") or "").lower()
            except Exception:
                continue
            if channels <= 0:
                continue
            if target in name:
                return int(index)
        return None

    @staticmethod
    def list_input_devices() -> List[str]:
        """Return available microphone device names from the local machine."""
        try:
            import sounddevice as sd  # type: ignore
            devices = sd.query_devices()
        except Exception:
            return []

        names: List[str] = []
        for info in devices:
            try:
                channels = int(info.get("max_input_channels", 0) or 0)
                name = str(info.get("name", "") or "").strip()
            except Exception:
                continue
            if channels <= 0 or not name:
                continue
            names.append(name)
        return names

    def _run(self) -> None:
        try:
            import sounddevice as sd  # type: ignore
        except Exception as exc:
            self._last_error = f"sounddevice unavailable: {exc}"
            self._running = False
            return

        baseline_mean: Optional[float] = None
        baseline_var: float = 0.0
        warmup_started = time.time()
        last_event_time = 0.0
        consecutive_anomaly_blocks = 0
        anomaly_peak_level_db = float("-inf")
        anomaly_peak_baseline_db = 0.0
        self._running = True

        stream = None
        try:
            device_index = self._resolve_input_device(sd)
            stream = sd.InputStream(
                samplerate=self.sample_rate_hz,
                channels=1,
                dtype="float32",
                blocksize=self.block_size,
                device=device_index,
            )
            stream.start()

            while not self._stop.is_set():
                frames, _overflowed = stream.read(self.block_size)
                samples = np.asarray(frames, dtype=np.float32).reshape(-1)
                if samples.size == 0:
                    continue

                rms = float(np.sqrt(np.mean(np.square(samples))) + 1e-9)
                level_db = float(20.0 * math.log10(max(rms, 1e-9)))
                now = time.time()

                if baseline_mean is None:
                    baseline_mean = level_db
                    baseline_var = 1.0
                    consecutive_anomaly_blocks = 0
                    anomaly_peak_level_db = float("-inf")
                    anomaly_peak_baseline_db = 0.0
                    continue

                alpha = self.baseline_adapt_rate
                delta = level_db - baseline_mean

                # Warmup learns ambient profile before firing anomalies.
                if (now - warmup_started) < self.warmup_seconds:
                    baseline_mean = (1.0 - alpha) * baseline_mean + (alpha * level_db)
                    baseline_var = (1.0 - alpha) * baseline_var + (alpha * (delta * delta))
                    consecutive_anomaly_blocks = 0
                    anomaly_peak_level_db = float("-inf")
                    anomaly_peak_baseline_db = 0.0
                    continue

                sigma = max(0.25, math.sqrt(max(1e-6, baseline_var)))
                z_score = delta / sigma

                is_anomaly = delta >= self.anomaly_threshold_db and z_score >= self.anomaly_zscore_threshold
                if is_anomaly:
                    consecutive_anomaly_blocks += 1
                    if level_db >= anomaly_peak_level_db:
                        anomaly_peak_level_db = level_db
                        anomaly_peak_baseline_db = baseline_mean
                    if consecutive_anomaly_blocks >= self._required_anomaly_blocks():
                        if (now - last_event_time) >= self.cooldown_s:
                            last_event_time = now
                            try:
                                self._on_anomaly(
                                    anomaly_peak_level_db if math.isfinite(anomaly_peak_level_db) else level_db,
                                    anomaly_peak_baseline_db,
                                )
                            except Exception:
                                pass
                        consecutive_anomaly_blocks = 0
                        anomaly_peak_level_db = float("-inf")
                        anomaly_peak_baseline_db = 0.0
                else:
                    consecutive_anomaly_blocks = 0
                    anomaly_peak_level_db = float("-inf")
                    anomaly_peak_baseline_db = 0.0

                # Keep adapting baseline to environment so normal changes are absorbed.
                baseline_mean = (1.0 - alpha) * baseline_mean + (alpha * level_db)
                baseline_var = (1.0 - alpha) * baseline_var + (alpha * (delta * delta))
                
                # Optional: check for wake word in audio buffer if enabled
                if self.wake_word:
                    self._check_wake_word_in_stream(samples)
        except Exception as exc:
            self._last_error = str(exc)
        finally:
            try:
                if stream is not None:
                    stream.stop()
                    stream.close()
            except Exception:
                pass
            self._running = False

    def _ensure_wake_recognizer(self) -> bool:
        """Lazily initialise the Vosk recognizer once and reuse it.

        Returns True if the recognizer is ready to use, False otherwise.
        The recognizer is intentionally created only once per detector
        instance to avoid the native heap corruption (0xc0000374) that
        results from constructing and immediately destroying a Vosk Model
        inside a hot audio callback.
        """
        if self._wake_recognizer_ready:
            return True
        if not self.wake_word:
            return False
        try:
            from vosk import KaldiRecognizer, Model  # type: ignore
        except ImportError:
            return False

        # Resolve model directory: prefer the explicitly configured path,
        # then fall back to the path used by voice_runtime.py.
        model_dir: Optional[Path] = None
        if self.vosk_model_path:
            candidate = Path(self.vosk_model_path)
            if candidate.is_dir():
                model_dir = candidate
        if model_dir is None:
            # Walk up from this file to find models/vosk
            for base in (Path(__file__).parent, Path(__file__).parent.parent,
                         Path(__file__).parent.parent.parent):
                candidate = base / "models" / "vosk"
                if candidate.is_dir():
                    model_dir = candidate
                    break
        if model_dir is None:
            _log.warning("[ACOUSTIC-GUARD] Vosk model directory not found — wake-word detection disabled")
            return False

        try:
            model = Model(str(model_dir))
            self._wake_recognizer = KaldiRecognizer(model, self.sample_rate_hz)
            self._wake_recognizer_ready = True
            _log.info("[ACOUSTIC-GUARD] Vosk recognizer initialised from %s", model_dir)
            return True
        except Exception as exc:
            _log.warning("[ACOUSTIC-GUARD] Failed to init Vosk recognizer: %s", exc)
            return False

    def _check_wake_word_in_stream(self, samples: np.ndarray) -> None:
        """Check if wake word appears in audio samples (optional feature).

        Uses a single long-lived KaldiRecognizer instance rather than
        creating a new Model on every call.
        """
        if not self.wake_word or not samples.size:
            return

        now = time.time()
        if (now - self._last_wake_word_check) < 0.5:
            return
        self._last_wake_word_check = now

        if not self._ensure_wake_recognizer():
            return

        try:
            import json
            audio_bytes = (samples * 32767).clip(-32768, 32767).astype(np.int16).tobytes()
            # Maintain a rolling 4-second PCM buffer.
            if len(self._wake_word_buffer) > self.sample_rate_hz * 4 * 2:
                self._wake_word_buffer = self._wake_word_buffer[-(self.sample_rate_hz * 4 * 2):]
            self._wake_word_buffer += audio_bytes

            rec = self._wake_recognizer
            # Feed the most recent ~0.5 s of audio to the recognizer.
            chunk = self._wake_word_buffer[-(self.sample_rate_hz * 2):]
            if rec.AcceptWaveform(chunk):
                result = json.loads(rec.Result() or "{}")
                text = str(result.get("text", "")).lower()
                if self.wake_word in text:
                    _log.info("[ACOUSTIC-GUARD] Wake word '%s' detected in stream: '%s'",
                              self.wake_word, text)
                    self._on_wake_word(self.wake_word)
            else:
                partial = json.loads(rec.PartialResult() or "{}")
                text = str(partial.get("partial", "")).lower()
                if self.wake_word in text:
                    _log.info("[ACOUSTIC-GUARD] Wake word '%s' in partial: '%s'",
                              self.wake_word, text)
                    self._on_wake_word(self.wake_word)
        except Exception as exc:  # noqa: BLE001
            _log.debug("[ACOUSTIC-GUARD] _check_wake_word_in_stream error: %s", exc)
