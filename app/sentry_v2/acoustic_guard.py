from __future__ import annotations

import math
import threading
import time
from typing import Callable, List, Optional

import numpy as np


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
    ) -> None:
        self._on_anomaly = on_anomaly
        self.sample_rate_hz = int(max(8000, sample_rate_hz))
        self.block_size = int(max(128, block_size))
        self.warmup_seconds = float(max(0.5, warmup_seconds))
        self.baseline_adapt_rate = float(min(0.25, max(0.001, baseline_adapt_rate)))
        self.anomaly_threshold_db = float(max(1.0, anomaly_threshold_db))
        self.anomaly_zscore_threshold = float(max(0.5, anomaly_zscore_threshold))
        self.cooldown_s = float(max(0.5, cooldown_s))
        self.device_name = str(device_name or "").strip()

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
    ) -> None:
        self.sample_rate_hz = int(max(8000, sample_rate_hz))
        self.block_size = int(max(128, block_size))
        self.warmup_seconds = float(max(0.5, warmup_seconds))
        self.baseline_adapt_rate = float(min(0.25, max(0.001, baseline_adapt_rate)))
        self.anomaly_threshold_db = float(max(1.0, anomaly_threshold_db))
        self.anomaly_zscore_threshold = float(max(0.5, anomaly_zscore_threshold))
        self.cooldown_s = float(max(0.5, cooldown_s))
        self.device_name = str(device_name or "").strip()

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
                    continue

                alpha = self.baseline_adapt_rate
                delta = level_db - baseline_mean

                # Warmup learns ambient profile before firing anomalies.
                if (now - warmup_started) < self.warmup_seconds:
                    baseline_mean = (1.0 - alpha) * baseline_mean + (alpha * level_db)
                    baseline_var = (1.0 - alpha) * baseline_var + (alpha * (delta * delta))
                    continue

                sigma = max(0.25, math.sqrt(max(1e-6, baseline_var)))
                z_score = delta / sigma

                if delta >= self.anomaly_threshold_db and z_score >= self.anomaly_zscore_threshold:
                    if (now - last_event_time) >= self.cooldown_s:
                        last_event_time = now
                        try:
                            self._on_anomaly(level_db, baseline_mean)
                        except Exception:
                            pass

                # Keep adapting baseline to environment so normal changes are absorbed.
                baseline_mean = (1.0 - alpha) * baseline_mean + (alpha * level_db)
                baseline_var = (1.0 - alpha) * baseline_var + (alpha * (delta * delta))
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
