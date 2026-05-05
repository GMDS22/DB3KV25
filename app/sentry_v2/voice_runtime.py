from __future__ import annotations

import os
import audioop
import base64
import queue
import re
import subprocess
import threading
import time
from difflib import SequenceMatcher
from pathlib import Path
from typing import Callable, Optional

from .voice_toggle_registry import (
    iter_voice_toggle_command_patterns,
    iter_voice_toggle_grammar_fragments,
)


class AsyncWavPlayer:
    """Background WAV playback so camera/tracking loops never block."""

    def __init__(self, on_log: Optional[Callable[[str], None]] = None) -> None:
        self._on_log = on_log or (lambda _msg: None)
        self._queue: "queue.Queue[str]" = queue.Queue()
        self._stop = threading.Event()
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-wav", daemon=True)
        self._worker.start()

    def close(self) -> None:
        self._stop.set()
        try:
            self._queue.put_nowait("")
        except Exception:
            pass

    def stop(self) -> None:
        """Stop any in-progress playback and clear the queue."""
        self._stop.set()
        try:
            # Clear the queue by draining it
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
            # Reset the stop event for future use
            self._stop.clear()
            # Restart the worker if it was stopped
            if self._worker is not None and not self._worker.is_alive():
                self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-wav", daemon=True)
                self._worker.start()
        except Exception as exc:
            self._on_log(f"[VOICE] WAV player stop error: {exc}")

    def play_file(self, wav_path: str) -> bool:
        path = str(wav_path or "").strip()
        if not path:
            return False
        if not Path(path).is_file():
            return False
        try:
            self._queue.put_nowait(path)
            return True
        except Exception:
            return False

    def _play_single(self, path: str, sa) -> None:
        """Play a single audio file (WAV or MP3) using available backend."""
        try:
            ext = Path(path).suffix.lower()
            if ext == ".mp3":
                try:
                    from pydub import AudioSegment
                    from pydub.playback import play as pydub_play
                    seg = AudioSegment.from_mp3(path)
                    pydub_play(seg)
                    return
                except Exception:
                    pass
                if os.name == "nt":
                    try:
                        import ctypes

                        alias = f"sentry_voice_{int(time.time() * 1000)}"
                        mci_send_string = ctypes.windll.winmm.mciSendStringW
                        open_rc = mci_send_string(f'open "{path}" type mpegvideo alias {alias}', None, 0, None)
                        if open_rc == 0:
                            try:
                                play_rc = mci_send_string(f"play {alias} wait", None, 0, None)
                                if play_rc == 0:
                                    return
                                self._on_log(f"[VOICE] Windows MP3 playback failed for {path} (play rc={play_rc})")
                            finally:
                                mci_send_string(f"close {alias}", None, 0, None)
                        return False
                    except Exception:
                        pass
                self._on_log(f"[VOICE] No MP3 playback backend is available for {path}")
                return
            # WAV playback
            if ext == ".wav":
                if sa is not None:
                    wave_obj = sa.WaveObject.from_wave_file(path)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                else:
                    import winsound
                    winsound.PlaySound(path, winsound.SND_FILENAME)
        except Exception as exc:
            self._on_log(f"Audio playback failed for {path}: {exc}")

    def _worker_loop(self) -> None:
        use_simpleaudio = os.name != "nt" or str(os.environ.get("SMART_SENTRY_FORCE_SIMPLEAUDIO", "")).strip().lower() in {"1", "true", "yes", "on"}
        sa = None
        if use_simpleaudio:
            try:
                import simpleaudio as _sa

                sa = _sa
            except Exception as exc:
                self._on_log(f"simpleaudio unavailable: {exc}")
                if os.name != "nt":
                    return
        else:
            try:
                import winsound  # noqa: F401
            except Exception as exc:
                self._on_log(f"winsound unavailable: {exc}")
                return

        while not self._stop.is_set():
            try:
                wav_path = self._queue.get(timeout=0.20)
            except queue.Empty:
                continue
            if not wav_path:
                continue
            self._play_single(wav_path, sa)


class KokoroTTS:
    """Primary offline neural TTS using Kokoro ONNX — no internet, no API key, near-human quality."""

    # Presets include US/UK and female/male options.
    VOICE_PROFILES = {
        "female_us": "af_sarah",
        "male_us": "am_michael",
        "female_uk": "bf_emma",
        "male_uk": "bm_george",
    }
    RECOMMENDED_VOICES = ["af_sarah", "am_michael", "bf_emma", "bm_george", "af_bella", "bf_isabella"]

    def __init__(
        self,
        wav_player: AsyncWavPlayer,
        *,
        model_path: str,
        voices_path: str,
        voice_name: str = "af_sarah",
        speed: float = 1.0,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._model_path = str(model_path or "").strip()
        self._voices_path = str(voices_path or "").strip()
        self._voice_name = str(voice_name or "af_sarah").strip() or "af_sarah"
        self._speed = max(0.5, min(2.0, float(speed or 1.0)))
        self._on_log = on_log or (lambda _msg: None)
        self._queue: "queue.Queue[str]" = queue.Queue()
        self._stop = threading.Event()
        self._enabled = False
        self._kokoro = None
        # Validate model files exist before starting worker
        if not self._model_path or not Path(self._model_path).is_file():
            self._on_log(f"[VOICE] Kokoro model not found: {self._model_path}")
        elif not self._voices_path or not Path(self._voices_path).is_file():
            self._on_log(f"[VOICE] Kokoro voices not found: {self._voices_path}")
        else:
            self._enabled = True
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-kokoro", daemon=True)
        self._worker.start()

    @property
    def enabled(self) -> bool:
        return bool(self._enabled)

    def close(self) -> None:
        self._stop.set()
        try:
            self._queue.put_nowait("")
        except Exception:
            pass

    def stop(self) -> None:
        try:
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
        except Exception:
            pass
        try:
            self._wav_player.stop()
        except Exception:
            pass

    def stop(self) -> None:
        try:
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
        except Exception:
            pass
        try:
            self._wav_player.stop()
        except Exception:
            pass

    def stop(self) -> None:
        """Stop any in-progress speech and clear the queue."""
        self._stop.set()
        try:
            # Clear the queue by draining it
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
            # Reset the stop event for future use
            self._stop.clear()
            # Restart the worker if it was stopped
            if self._worker is not None and not self._worker.is_alive():
                self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-kokoro", daemon=True)
                self._worker.start()
        except Exception as exc:
            self._on_log(f"[VOICE] Kokoro stop error: {exc}")

    def speak_async(self, text: str) -> bool:
        if not self._enabled:
            return False
        cleaned = str(text or "").strip()
        if not cleaned:
            return False
        try:
            self._queue.put_nowait(cleaned)
            return True
        except Exception:
            return False

    def _worker_loop(self) -> None:
        if not self._enabled:
            return
        try:
            from kokoro_onnx import Kokoro
            import soundfile as sf
        except Exception as exc:
            self._on_log(f"[VOICE] Kokoro import failed: {exc}")
            self._enabled = False
            return
        try:
            self._kokoro = Kokoro(self._model_path, self._voices_path)
            voices = self._kokoro.get_voices()
            if self._voice_name not in voices:
                fallback = self.RECOMMENDED_VOICES[0]
                self._on_log(f"[VOICE] Kokoro voice '{self._voice_name}' not found; using '{fallback}'")
                self._voice_name = fallback
            self._on_log(f"[VOICE] Kokoro TTS ready — voice: {self._voice_name}, speed: {self._speed}x")
        except Exception as exc:
            self._on_log(f"[VOICE] Kokoro model load failed: {exc}")
            self._enabled = False
            return

        tts_output_dir = Path(self._model_path).parent / "_generated_tts"
        tts_output_dir.mkdir(parents=True, exist_ok=True)

        while not self._stop.is_set():
            try:
                phrase = self._queue.get(timeout=0.20)
            except queue.Empty:
                continue
            if not phrase:
                continue
            try:
                ts = int(time.time() * 1000)
                wav_path = str(tts_output_dir / f"kokoro_{ts}.wav")
                samples, rate = self._kokoro.create(
                    phrase,
                    voice=self._voice_name,
                    speed=self._speed,
                    lang="en-us",
                )
                sf.write(wav_path, samples, rate)
                self._wav_player.play_file(wav_path)
            except Exception as exc:
                self._on_log(f"[VOICE] Kokoro synthesis error: {exc}")


class AzureNeuralTTS:
    """Optional neural TTS worker that synthesizes to WAV and plays asynchronously."""

    def __init__(
        self,
        wav_player: AsyncWavPlayer,
        *,
        speech_key: str,
        speech_region: str,
        voice_name: str,
        output_dir: str,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._speech_key = str(speech_key or "").strip()
        self._speech_region = str(speech_region or "").strip()
        self._voice_name = str(voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
        self._output_dir = Path(output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._on_log = on_log or (lambda _msg: None)
        self._queue: "queue.Queue[str]" = queue.Queue()
        self._stop = threading.Event()
        self._enabled = bool(self._speech_key and self._speech_region)
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-azure-tts", daemon=True)
        self._worker.start()

    @property
    def enabled(self) -> bool:
        return bool(self._enabled)

    def close(self) -> None:
        self._stop.set()
        try:
            self._queue.put_nowait("")
        except Exception:
            pass

    def stop(self) -> None:
        try:
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
        except Exception:
            pass
        try:
            self._wav_player.stop()
        except Exception:
            pass

    def speak_async(self, text: str) -> bool:
        if not self._enabled:
            return False
        cleaned = str(text or "").strip()
        if not cleaned:
            return False
        try:
            self._queue.put_nowait(cleaned)
            return True
        except Exception:
            return False

    def _worker_loop(self) -> None:
        if not self._enabled:
            return
        try:
            import azure.cognitiveservices.speech as speechsdk
        except Exception as exc:
            self._on_log(f"Azure speech SDK unavailable: {exc}")
            self._enabled = False
            return

        while not self._stop.is_set():
            try:
                phrase = self._queue.get(timeout=0.20)
            except queue.Empty:
                continue
            if not phrase:
                continue
            try:
                ts = int(time.time() * 1000)
                wav_path = self._output_dir / f"azure_tts_{ts}.wav"
                speech_config = speechsdk.SpeechConfig(subscription=self._speech_key, region=self._speech_region)
                speech_config.speech_synthesis_voice_name = self._voice_name
                audio_config = speechsdk.audio.AudioOutputConfig(filename=str(wav_path))
                synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
                result = synthesizer.speak_text_async(phrase).get()
                if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    self._wav_player.play_file(str(wav_path))
                else:
                    self._on_log(f"Azure TTS synthesis failed: {result.reason}")
            except Exception as exc:
                self._on_log(f"Azure TTS worker error: {exc}")


class EdgeNeuralTTS:
    """Key-free neural TTS using Microsoft Edge voices via edge-tts (internet required, no subscription)."""

    def __init__(
        self,
        wav_player: AsyncWavPlayer,
        *,
        voice_name: str,
        output_dir: str,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._voice_name = str(voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
        self._output_dir = Path(output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._on_log = on_log or (lambda _msg: None)
        self._queue: "queue.Queue[str]" = queue.Queue()
        self._stop = threading.Event()
        self._enabled = False
        try:
            import edge_tts  # noqa: F401
            self._enabled = True
        except Exception as exc:
            self._on_log(f"[VOICE] edge-tts unavailable: {exc}")
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-edge-tts", daemon=True)
        self._worker.start()

    @property
    def enabled(self) -> bool:
        return bool(self._enabled)

    def close(self) -> None:
        self._stop.set()
        try:
            self._queue.put_nowait("")
        except Exception:
            pass

    def stop(self) -> None:
        try:
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
        except Exception:
            pass
        try:
            self._wav_player.stop()
        except Exception:
            pass

    def speak_async(self, text: str) -> bool:
        if not self._enabled:
            return False
        cleaned = str(text or "").strip()
        if not cleaned:
            return False
        try:
            self._queue.put_nowait(cleaned)
            return True
        except Exception:
            return False

    def _worker_loop(self) -> None:
        if not self._enabled:
            return
        import asyncio
        import edge_tts

        loop = asyncio.new_event_loop()

        async def _synth(phrase: str, out_path: str) -> bool:
            try:
                communicator = edge_tts.Communicate(phrase, self._voice_name)
                await communicator.save(out_path)
                return True
            except Exception as exc:
                self._on_log(f"[VOICE] edge-tts synthesis failed: {exc}")
                return False

        while not self._stop.is_set():
            try:
                phrase = self._queue.get(timeout=0.20)
            except queue.Empty:
                continue
            if not phrase:
                continue
            try:
                ts = int(time.time() * 1000)
                wav_path = str(self._output_dir / f"edge_tts_{ts}.mp3")
                ok = loop.run_until_complete(_synth(phrase, wav_path))
                if ok:
                    self._wav_player.play_file(wav_path)
            except Exception as exc:
                self._on_log(f"[VOICE] edge-tts worker error: {exc}")

        loop.close()


class MicrophoneSignatureProbe:
    """Lightweight audio monitor that estimates a coarse speaking frequency band."""

    def __init__(self, *, device_name: str = "", on_log: Optional[Callable[[str], None]] = None) -> None:
        self._device_name = str(device_name or "").strip()
        self._on_log = on_log or (lambda _msg: None)
        self._stop = threading.Event()
        self._worker: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        self._last_signature: dict[str, object] = {}

    def start(self) -> bool:
        if self._worker is not None and self._worker.is_alive():
            return True
        self._stop.clear()
        self._worker = threading.Thread(target=self._listen_loop, name="sentry-voice-signature", daemon=True)
        self._worker.start()
        return True

    def stop(self) -> None:
        self._stop.set()

    def latest_signature(self) -> dict[str, object]:
        with self._lock:
            return dict(self._last_signature)

    def _resolve_input_device(self, sd_module) -> Optional[int]:
        target = self._device_name.lower().strip()
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
            if channels > 0 and target in name:
                return int(index)
        return None

    @staticmethod
    def _coerce_stream_chunk(indata) -> bytes:
        try:
            samples = indata.reshape(-1) if hasattr(indata, "reshape") else indata
            pcm = (samples * 32767.0).clip(-32768, 32767).astype("int16", copy=False)
            return pcm.tobytes()
        except Exception:
            try:
                return bytes(indata)
            except Exception:
                return b""

    def _update_signature(self, chunk: bytes) -> None:
        if not chunk:
            return
        try:
            rms = int(audioop.rms(chunk, 2))
            if rms < 120:
                return
            zero_crossings = int(audioop.cross(chunk, 2))
            sample_count = max(1, len(chunk) // 2)
            freq_hz = float(zero_crossings) * 16000.0 / (2.0 * float(sample_count))
            if freq_hz < 60.0 or freq_hz > 420.0:
                return
            now = time.time()
            with self._lock:
                prev_freq = float(self._last_signature.get("frequency_hz", 0.0) or 0.0)
                prev_at = float(self._last_signature.get("updated_at", 0.0) or 0.0)
                if prev_freq > 0.0 and (now - prev_at) < 1.4:
                    freq_hz = (prev_freq * 0.65) + (freq_hz * 0.35)
                self._last_signature = {
                    "frequency_hz": round(freq_hz, 1),
                    "rms": int(rms),
                    "updated_at": now,
                }
        except Exception:
            return

    def _listen_loop(self) -> None:
        try:
            import sounddevice as sd
        except Exception as exc:
            self._on_log(f"[VOICE] operator signature probe unavailable: {exc}")
            return
        try:
            device_index = self._resolve_input_device(sd)
            with sd.InputStream(
                samplerate=16000,
                blocksize=2048,
                dtype="float32",
                channels=1,
                device=device_index,
            ) as stream:
                while not self._stop.is_set():
                    try:
                        frames, _overflowed = stream.read(2048)
                    except Exception:
                        continue
                    self._update_signature(self._coerce_stream_chunk(frames))
        except Exception as exc:
            self._on_log(f"[VOICE] operator signature probe unavailable: {exc}")


class VoskCommandListener:
    """Offline Vosk recognizer loop with wake-word and callback dispatch."""

    def __init__(
        self,
        *,
        model_path: str,
        wake_word: str,
        command_cooldown_s: float,
        on_command: Callable[[str], None],
        on_transcript: Optional[Callable[[dict[str, object]], None]] = None,
        on_log: Optional[Callable[[str], None]] = None,
        device_name: str = "",
        enable_wake_word_coordination: bool = False,
    ) -> None:
        self._model_path = str(model_path or "").strip()
        self._wake_word = str(wake_word or "sentry").strip().lower()
        self._command_cooldown_s = max(0.0, float(command_cooldown_s or 0.0))
        self._on_command = on_command
        self._on_transcript = on_transcript or (lambda _payload: None)
        self._on_log = on_log or (lambda _msg: None)
        self._stop = threading.Event()
        self._audio_queue: "queue.Queue[bytes]" = queue.Queue(maxsize=24)
        self._worker: Optional[threading.Thread] = None
        self._last_emit_s: float = 0.0
        self._device_name = str(device_name or "").strip()
        self._enable_wake_word_coordination = bool(enable_wake_word_coordination)
        self._wake_word_detected_event = threading.Event()
        self._wake_command_window_s: float = 14.0
        self._command_window_until_s: float = 0.0
        self._partial_wake_ack_hold_s: float = 1.75
        self._suppress_wake_only_until_s: float = 0.0
        self._diag_last_audio_log_s: float = 0.0
        self._diag_last_quiet_log_s: float = 0.0
        self._diag_last_gain_log_s: float = 0.0
        self._diag_audio_log_interval_s: float = 2.0
        self._diag_quiet_log_interval_s: float = 8.0
        self._diag_audio_rms_min: int = 90
        self._diag_gain_log_interval_s: float = 8.0
        self._input_gain_target_rms: int = 1200
        self._input_gain_max: float = 6.0
        self._recent_signature: dict[str, object] = {}
        self._recent_spoken_phrase_suppressions: list[dict[str, object]] = []
        self._recent_output_input_block_until_s: float = 0.0

    def _latest_signature(self) -> dict[str, object]:
        return dict(self._recent_signature)

    def _capture_chunk_signature(self, chunk: bytes, rms: int) -> None:
        if not chunk or rms < 120:
            return
        try:
            zero_crossings = int(audioop.cross(chunk, 2))
            sample_count = max(1, len(chunk) // 2)
            freq_hz = float(zero_crossings) * 16000.0 / (2.0 * float(sample_count))
            if freq_hz < 60.0 or freq_hz > 420.0:
                return
            now = time.time()
            prev_freq = float(self._recent_signature.get("frequency_hz", 0.0) or 0.0)
            prev_at = float(self._recent_signature.get("updated_at", 0.0) or 0.0)
            if prev_freq > 0.0 and (now - prev_at) < 1.4:
                freq_hz = (prev_freq * 0.65) + (freq_hz * 0.35)
            self._recent_signature = {
                "frequency_hz": round(freq_hz, 1),
                "rms": int(rms),
                "updated_at": now,
            }
        except Exception:
            return

    def _emit_transcript(
        self,
        kind: str,
        text: str,
        *,
        confidence: Optional[float] = None,
        source: str = "stt",
    ) -> None:
        payload: dict[str, object] = {
            "kind": str(kind or "").strip().lower(),
            "text": str(text or "").strip(),
            "timestamp": time.time(),
            "source": str(source or "stt").strip().lower() or "stt",
        }
        if confidence is not None:
            payload["confidence"] = float(confidence)
        signature = self._latest_signature()
        if signature:
            payload.update(signature)
        try:
            self._on_transcript(payload)
        except Exception as exc:
            self._on_log(f"[VOICE-DIAG] transcript-callback failed: {exc}")

    @staticmethod
    def _sanitize_speech_text(text: str) -> str:
        normalized = re.sub(r"[^a-z0-9 ]+", " ", str(text or "").strip().lower())
        return re.sub(r"\s+", " ", normalized).strip()

    def suppress_recent_output_text(self, text: str, *, hold_s: float, block_s: Optional[float] = None) -> None:
        sanitized = self._sanitize_speech_text(text)
        if not sanitized:
            return
        now = time.time()
        hold_duration_s = max(0.8, float(hold_s or 0.0))
        expires_at = now + hold_duration_s
        self._recent_spoken_phrase_suppressions.append({
            "text": sanitized,
            "expires_at": expires_at,
        })
        block_duration_s = float(block_s) if block_s is not None else max(0.8, min(4.5, hold_duration_s - 0.65))
        if block_duration_s > 0.0:
            suppress_until = now + block_duration_s
            self._recent_output_input_block_until_s = max(
                float(getattr(self, "_recent_output_input_block_until_s", 0.0) or 0.0),
                suppress_until,
            )
            self._suppress_wake_only_until_s = max(
                float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0),
                suppress_until,
            )
        self._prune_recent_output_suppressions(now=time.time())

    def clear_recent_output_suppression(self) -> None:
        self._recent_spoken_phrase_suppressions = []
        self._recent_output_input_block_until_s = 0.0

    def _recent_output_input_block_active(self, *, now: Optional[float] = None) -> bool:
        current_time = float(now if now is not None else time.time())
        return current_time <= float(getattr(self, "_recent_output_input_block_until_s", 0.0) or 0.0)

    def _prune_recent_output_suppressions(self, *, now: Optional[float] = None) -> None:
        current_time = float(now if now is not None else time.time())
        self._recent_spoken_phrase_suppressions = [
            item
            for item in list(getattr(self, "_recent_spoken_phrase_suppressions", []) or [])
            if current_time < float(item.get("expires_at", 0.0) or 0.0)
        ]

    def _matches_recent_output_echo(self, text: str, *, partial: bool) -> bool:
        sanitized = self._sanitize_speech_text(text)
        if not sanitized:
            return False
        now = time.time()
        self._prune_recent_output_suppressions(now=now)
        candidates = list(getattr(self, "_recent_spoken_phrase_suppressions", []) or [])
        if not candidates:
            return False
        sanitized_tokens = [token for token in sanitized.split(" ") if token]
        if not sanitized_tokens:
            return False
        for item in candidates:
            spoken = self._sanitize_speech_text(str(item.get("text", "") or ""))
            if not spoken:
                continue
            spoken_tokens = [token for token in spoken.split(" ") if token]
            if not spoken_tokens:
                continue
            if partial:
                if len(sanitized_tokens) < 2:
                    continue
                window = " ".join(spoken_tokens[: len(sanitized_tokens)])
                if sanitized == window:
                    return True
                ratio = SequenceMatcher(None, sanitized, window).ratio()
                if ratio >= 0.90:
                    return True
                continue
            ratio = SequenceMatcher(None, sanitized, spoken).ratio()
            token_overlap = len(set(sanitized_tokens) & set(spoken_tokens))
            if sanitized == spoken:
                return True
            if ratio >= 0.88 and token_overlap >= max(2, min(len(sanitized_tokens), len(spoken_tokens)) - 1):
                return True
            if sanitized in spoken and len(sanitized_tokens) >= 2:
                return True
        return False

    def _command_grammar_fragments(self) -> list[str]:
        return list(
            dict.fromkeys(
                fragment
                for fragment in [
            "who are you",
            "what do you do",
            "what can you do",
            "identify yourself",
            "tell me a joke",
            "tell a joke",
            "make a joke",
            "personality",
            "change personality",
            "set personality sentinel",
            "set personality hunter",
            "set personality stealth",
            "set personality playful",
            "run the smart sentry",
            "run smart sentry",
            "run it",
            "connect boards and enable smart sentry",
            "connect the boards and enable smart sentry",
            "connect smart sentry boards and enable smart sentry",
            "connect the app to com ports",
            "connect app to com ports",
            "connect controller link",
            "connect the controller link",
            "connect board",
            "connect boards",
            "connect the board",
            "connect the boards",
            "connect smart sentry",
            "connect the smart sentry",
            "connect smart sentry board",
            "connect smart sentry boards",
            "connect the smart sentry board",
            "connect the smart sentry boards",
            "connect to the com port",
            "connect to com port",
            "connect com port",
            "connect serial",
            "disconnect controller link",
            "disconnect the controller link",
            "disconnect smart sentry boards",
            "disconnect the smart sentry boards",
            "disconnect board",
            "disconnect boards",
            "disconnect the board",
            "disconnect the boards",
            "disconnect from com port",
            "disconnect com port",
            "disconnect serial",
            "yes",
            "no",
            "go ahead",
            "do it",
            "confirm",
            "cancel",
            "cancel current task",
            "abort current task",
            "stop that",
            "cancel that",
            "never mind",
            "say it again",
            "say that again",
            "repeat that",
            "repeat it",
            "cancel the last",
            "cancel last",
            "cancel the last task",
            "cancel all tasks in queue",
            "cancel all queued tasks",
            "clear the queue",
            "resume last task",
            "status update",
            "current request",
            "last request",
            "do it again",
            "same but faster",
            "priority",
            "override",
            "priority connect boards",
            "override connect boards",
            "queue status",
            "what are you doing",
            "what are you working on",
            "what are you checking",
            "what is in queue",
            "whats in queue",
            "current task",
            "status of last command",
            "increase sensitivity",
            "decrease sensitivity",
            "be more strict on commands",
            "be less strict on commands",
            "increase response delay",
            "decrease response delay",
            "increase silence threshold",
            "decrease silence threshold",
            "increase tracking priority",
            "decrease tracking priority",
            "talk less",
            "stay paused",
            "keep paused",
            "hold position",
            "wait there",
            "other task",
            "another task",
            "another question",
            "another command",
            "ask another question",
            "give another command",
            "continue conversation",
            "keep listening",
            "i have a question",
            "question for you",
            "can i ask a question",
            "let me ask a question",
            "i want to ask a question",
            "i need help",
            "i need your help",
            "start tracking",
            "stop tracking",
            "enable smart sentry",
            "enable the smart sentry",
            "disable smart sentry",
            "disable the smart sentry",
            "resume guarding mode",
            "pause smart sentry",
            "go home",
            "go rest",
            "standby",
            "enable face recognition",
            "disable face recognition",
            "enable human voice",
            "disable human voice",
            "enable shortcuts",
            "disable shortcuts",
            "enable assistant auto speak",
            "disable assistant auto speak",
            "open camera",
            "close camera",
            "voice style quiet",
            "voice style operator",
            "voice style alert",
            "voice style guard",
            "voice style warm",
            "voice style friendly",
            "voice style neutral",
            "voice style default",
            "load profile",
            "switch profile",
            "use nano model",
            "use small model",
            "use medium model",
            "use large model",
            "use xlarge model",
            "use tiny model",
            "use yolo model",
            "use object detection",
            "use best mode",
            "use motion mode",
            "use color mode",
            "increase brightness",
            "decrease brightness",
            "set brightness",
            "increase speed",
            "decrease speed",
            "set speed",
            "increase confidence",
            "decrease confidence",
            "set confidence",
            "change the theme",
            "change theme",
            "change the theme to anything else",
            "change theme to anything else",
            "analyze current app behavior",
            "analyze the current app behavior",
            "analyze current app behaviour",
            "analyze the current app behaviour",
            "diagnose",
            "what's wrong",
            "whats wrong",
            "what's wrong with face detection",
            "whats wrong with face detection",
            "why is face detection not loading",
            "why is face detection not working",
            "why is face recognition not loading",
            "why is face recognition not working",
            "analyze why face detection is not loading",
            "analyze why face recognition is not loading",
            "tell me why face detection is not loading",
            "tell me why face recognition is not loading",
            "status report",
            "system report",
            "check status",
            "run diagnostics",
            "connect",
            "disconnect",
            *iter_voice_toggle_grammar_fragments(),
                ]
                if str(fragment or "").strip()
            )
        )

    def _recognizer_grammar_phrases(self) -> list[str]:
        wake_aliases = self._wake_word_aliases(self._wake_word)
        command_fragments = self._command_grammar_fragments()
        prefixed_phrases = [
            f"{alias} {fragment}".strip()
            for alias in wake_aliases
            for fragment in command_fragments
            if alias and fragment
        ]
        phrases = [
            *wake_aliases,
            self._wake_word,
            *command_fragments,
            *prefixed_phrases,
            "[unk]",
        ]
        return list(dict.fromkeys(str(item).strip().lower() for item in phrases if str(item).strip()))

    def _windows_speech_grammar_phrases(self) -> list[str]:
        wake_aliases = self._wake_word_aliases(self._wake_word)
        command_fragments = self._command_grammar_fragments()
        phrases = [
            *wake_aliases,
            self._wake_word,
            *command_fragments,
        ]
        return list(dict.fromkeys(str(item).strip().lower() for item in phrases if str(item).strip()))

    def _fuzzy_command_fragment_match(self, text: str) -> str:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        tokens = [tok for tok in re.findall(r"[a-z0-9]+", normalized) if tok]
        if len(tokens) < 3:
            return ""
        ignored_tokens = {"a", "an", "the", "to", "for", "please", "now"}
        signal_tokens = {tok for tok in tokens if tok not in ignored_tokens}
        if len(signal_tokens) < 2:
            return ""

        compact_text = " ".join(tok for tok in tokens if tok not in ignored_tokens)
        best_match = ""
        best_ratio = 0.0
        for candidate in self._command_grammar_fragments():
            candidate_text = re.sub(r"\s+", " ", str(candidate or "").strip().lower())
            candidate_tokens = [tok for tok in re.findall(r"[a-z0-9]+", candidate_text) if tok]
            if len(candidate_tokens) < 2:
                continue
            candidate_signal_tokens = {tok for tok in candidate_tokens if tok not in ignored_tokens}
            overlap = signal_tokens & candidate_signal_tokens
            if len(overlap) < 2:
                continue
            compact_candidate = " ".join(tok for tok in candidate_tokens if tok not in ignored_tokens)
            ratio = max(
                SequenceMatcher(None, normalized, candidate_text).ratio(),
                SequenceMatcher(None, compact_text, compact_candidate).ratio(),
            )
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = candidate_text
        if best_ratio >= 0.88:
            return best_match
        return ""

    def _looks_meaningful_followup_text(self, sanitized: str) -> bool:
        normalized = re.sub(r"\s+", " ", str(sanitized or "").strip().lower())
        if not normalized:
            return False
        known_fragments = set(self._command_grammar_fragments())
        if normalized in known_fragments:
            return True
        if self._fuzzy_command_fragment_match(normalized):
            return True

        tokens = [tok for tok in re.findall(r"[a-z0-9]+", normalized) if tok]
        token_count = len(tokens)
        if token_count < 2:
            return False

        generic_question_prefixes = (
            "why ",
            "how ",
            "what ",
            "when ",
            "where ",
            "which ",
            "who ",
        )
        if normalized.startswith(generic_question_prefixes) and token_count >= 4:
            return True

        directed_prefixes = (
            "tell me ",
            "explain ",
            "look at ",
            "check ",
            "analyze ",
            "analyse ",
            "diagnose ",
            "can you analyze ",
            "can you explain ",
            "can you check ",
            "can you tell me ",
            "could you analyze ",
            "could you explain ",
            "could you check ",
            "could you tell me ",
            "would you analyze ",
            "would you explain ",
            "would you check ",
            "would you tell me ",
        )
        if normalized.startswith(directed_prefixes) and token_count >= 3:
            return True

        runtime_tokens = (
            "current app",
            "current system",
            "runtime",
            "face detection",
            "face recognition",
            "not loading",
            "not working",
            "what happened",
            "problem",
            "issue",
            "tracking",
            "camera",
        )
        if token_count >= 3 and any(token in normalized for token in runtime_tokens):
            return True

        intent_patterns = (
            r"\b(?:connect|disconnect|enable|disable|resume|pause|start|stop|open|close|run|check|set|change|switch|load|use|increase|decrease|go)\b.*\b(?:smart\s+sentry|boards?|com|port|serial|camera|tracking|guard(?:ing)?\s*mode|face|recognition|human\s+voice|assistant\s+auto\s+speak|shortcuts?|voice\s+style|profile|model|brightness|speed|confidence|theme|home|rest)\b",
            r"\b(?:analy(?:ze|sis)|analyse|diagnos(?:e|is|tic)|explain|look at|check)\b.*\b(?:app|runtime|system|face|recognition|tracking|camera|behavior|behaviour|issue|problem|status)\b",
            r"\b(?:tell me|show me)\b.*\b(?:status|runtime|current\s+app|current\s+system|face\s+detection|face\s+recognition)\b",
        )
        return any(re.search(pattern, normalized) for pattern in intent_patterns)

    def _boost_audio_chunk(self, chunk: bytes) -> tuple[bytes, int, int, float]:
        if not chunk:
            return chunk, 0, 0, 1.0
        try:
            raw_rms = int(audioop.rms(chunk, 2))
            raw_peak = int(audioop.max(chunk, 2))
        except Exception:
            return chunk, 0, 0, 1.0
        if raw_rms < 35 or raw_rms >= self._input_gain_target_rms:
            return chunk, raw_rms, raw_peak, 1.0
        gain = min(float(self._input_gain_max), max(1.0, float(self._input_gain_target_rms) / max(1.0, float(raw_rms))))
        if gain <= 1.15:
            return chunk, raw_rms, raw_peak, 1.0
        try:
            boosted = audioop.mul(chunk, 2, gain)
            boosted_rms = int(audioop.rms(boosted, 2))
            boosted_peak = int(audioop.max(boosted, 2))
            return boosted, boosted_rms, boosted_peak, float(gain)
        except Exception:
            return chunk, raw_rms, raw_peak, 1.0

    @staticmethod
    def _coerce_stream_chunk(indata) -> bytes:
        if isinstance(indata, (bytes, bytearray, memoryview)):
            return bytes(indata)
        try:
            samples = indata.reshape(-1) if hasattr(indata, "reshape") else indata
            pcm = (samples * 32767.0).clip(-32768, 32767).astype("int16", copy=False)
            return pcm.tobytes()
        except Exception:
            try:
                return bytes(indata)
            except Exception:
                return b""

    def _log_audio_chunk_diagnostics(self, chunk: bytes, rms: int, peak: int, gain: float, *, queue_depth: int = 0) -> None:
        now = time.time()
        if (now - self._diag_last_audio_log_s) < self._diag_audio_log_interval_s:
            return
        self._diag_last_audio_log_s = now
        try:
            self._on_log(
                f"[VOICE-DIAG] mic-chunk bytes={len(chunk)} rms={rms} peak={peak} gain={gain:.2f} queue={queue_depth}"
            )
            if rms < self._diag_audio_rms_min and (now - self._diag_last_quiet_log_s) >= self._diag_quiet_log_interval_s:
                self._diag_last_quiet_log_s = now
                self._on_log(
                    "[VOICE-DIAG] microphone level appears low; if wake-word is not detected, check input gain/device selection"
                )
            if gain > 1.15 and (now - self._diag_last_gain_log_s) >= self._diag_gain_log_interval_s:
                self._diag_last_gain_log_s = now
                self._on_log(f"[VOICE-DIAG] input-gain-boost applied gain={gain:.2f} rms={rms} peak={peak}")
        except Exception:
            pass

    @staticmethod
    def _wake_word_aliases(wake_word: str) -> list[str]:
        base = re.sub(r"[^a-z0-9 ]+", " ", str(wake_word or "").strip().lower())
        base = re.sub(r"\s+", " ", base).strip()
        aliases: list[str] = [base] if base else []
        if base == "elion":
            aliases.extend([
                "hey elion",
                "hi elion",
                "leon",
                "hey leon",
                "e lion",
                "a lion",
                "alien",
                "aileen",
                "eileen",
                "elyon",
                "ellion",
                "elian",
                "alion",
                "elliot",
            ])
        return list(dict.fromkeys(alias for alias in aliases if alias))

    @staticmethod
    def _partial_wake_word_aliases(wake_word: str) -> list[str]:
        aliases = VoskCommandListener._wake_word_aliases(wake_word)
        base = re.sub(r"[^a-z0-9 ]+", " ", str(wake_word or "").strip().lower())
        base = re.sub(r"\s+", " ", base).strip()
        if base == "elion":
            conservative = [
                "elion",
                "e lion",
                "ellion",
                "elyon",
                "elian",
                "alion",
            ]
            return [alias for alias in conservative if alias in aliases]
        return aliases[:1] if aliases else []

    def _partial_contains_wake(self, partial_text: str) -> bool:
        sanitized = re.sub(r"[^a-z0-9 ]+", " ", str(partial_text or "").strip().lower())
        sanitized = re.sub(r"\s+", " ", sanitized).strip()
        if not sanitized or not self._wake_word:
            return False
        aliases = self._partial_wake_word_aliases(self._wake_word)
        for alias in aliases:
            if re.search(r"\b" + re.escape(alias) + r"\b", sanitized):
                return True
        return False

    @staticmethod
    def _fuzzy_contains_wake(sanitized_text: str, aliases: list[str]) -> bool:
        tokens = [tok for tok in re.findall(r"[a-z0-9]+", sanitized_text) if tok]
        if not tokens:
            return False
        for alias in aliases:
            alias_tokens = [tok for tok in alias.split() if tok]
            if not alias_tokens:
                continue
            width = len(alias_tokens)
            if width <= 0 or len(tokens) < width:
                continue
            for idx in range(0, len(tokens) - width + 1):
                window = " ".join(tokens[idx : idx + width])
                if window == alias:
                    return True
                if SequenceMatcher(None, window, alias).ratio() >= 0.80:
                    return True
        return False

    def _apply_phrase_alias_corrections(self, sanitized: str) -> str:
        corrected = str(sanitized or "").strip().lower()
        if not corrected:
            return ""
        replacements = (
            (r"\be lion\b", "elion"),
            (r"\ba lion\b", "elion"),
            (r"\belyan\b", "elion"),
            (r"\belyon\b", "elion"),
            (r"\bellion\b", "elion"),
            (r"\belian\b", "elion"),
            (r"\belliot\b", "elion"),
            (r"\bsports? and\b", "smart sentry"),
            (r"\bsport sentry\b", "smart sentry"),
            (r"\bsmart centry\b", "smart sentry"),
            (r"\bsmart century\b", "smart sentry"),
            (r"\bsmart country\b", "smart sentry"),
            (r"\bsmart entry\b", "smart sentry"),
            (r"\bsmarts? entry\b", "smart sentry"),
            (r"\bgo to the home\b", "go home"),
            (r"\bgo to home\b", "go home"),
            (r"\bgo to the rest\b", "go rest"),
            (r"\bgo to rest\b", "go rest"),
            (r"\bcome ports?\b", "com ports"),
            (r"\bcalm ports?\b", "com ports"),
            (r"\bcome port\b", "com port"),
            (r"\bcalm port\b", "com port"),
            (r"\bc o m\b", "com"),
            (r"\bguard mode\b", "guarding mode"),
            (r"\bguarding mold\b", "guarding mode"),
            (r"\bauto tracking\b", "autotracking"),
            (r"\bvoice styles?\b", "voice style"),
            (r"\bhuman boys\b", "human voice"),
            (r"\bauto speed\b", "auto speak"),
            (r"\benabled\b", "enable"),
            (r"\bdisabled\b", "disable"),
            (r"\banalyse\b", "analyze"),
            (r"\bbehaviour\b", "behavior"),
            (r"\brun the offense\b", "run diagnostics"),
            (r"\bi(?:'| a)?ve got a question\b", "i have a question"),
            (r"\bi got a question\b", "i have a question"),
            (r"\bquestion for ya\b", "question for you"),
            (r"\bi need some help\b", "i need help"),
            (r"\bcancel that(?:\s+[a-z]+)?$", "cancel that"),
            (r"\byou do it\b", "do it"),
        )
        for pattern, replacement in replacements:
            corrected = re.sub(pattern, replacement, corrected)
        corrected = re.sub(r"\s+", " ", corrected).strip()
        return corrected

    def _canonicalize_command_text(self, sanitized: str) -> str:
        corrected = self._apply_phrase_alias_corrections(sanitized)
        if not corrected:
            return ""
        corrected = re.sub(r"\b(?:over|done|that is all|that's all)\s*$", "", corrected).strip()
        corrected = re.sub(r"\s+", " ", corrected).strip()
        if not corrected:
            return ""
        short_form_map = {
            "what do": "what do you do",
            "what can you do": "what do you do",
            "who are ya": "who are you",
            "who are you elion": "who are you",
        }
        if corrected in short_form_map:
            return short_form_map[corrected]

        profile_match = re.search(r"\b(?:load|switch(?:\s+to)?|use)\b\s+(.+?)\s+profile\b", corrected)
        if profile_match:
            profile_name = re.sub(r"\s+", " ", str(profile_match.group(1) or "").strip())
            if profile_name:
                return f"load profile {profile_name}"

        model_match = re.search(
            r"\b(?:use|switch(?:\s+to)?|load)\b(?:\s+yolo)?\s+(nano|small|medium|large|xlarge|tiny|n|s|m|l|x)\b(?:\s+model)?\b",
            corrected,
        )
        if model_match:
            size_token = str(model_match.group(1) or "").strip().lower()
            size_map = {"n": "nano", "s": "small", "m": "medium", "l": "large", "x": "xlarge"}
            return f"use {size_map.get(size_token, size_token)} model"

        if "voice style" in corrected or "speech style" in corrected:
            style_map = {
                "quiet": "voice style quiet",
                "operator": "voice style operator",
                "alert": "voice style alert",
                "guard": "voice style alert",
                "warm": "voice style warm",
                "friendly": "voice style warm",
                "neutral": "voice style neutral",
                "default": "voice style neutral",
            }
            for token, canonical in style_map.items():
                if token in corrected:
                    return canonical
        canonical_rules = (
            (r"\b(?:priority|override)\b.*\bconnect\b.*\b(board|boards|com|port|ports|serial)\b", "priority connect boards"),
            (r"^resume last(?:\b| .*)", "resume last task"),
            (r"\bresume\b.*\blast\b.*\btask\b", "resume last task"),
            (r"\bdo\b.*\bagain\b", "do it again"),
            (r"\bsame\b.*\bfaster\b", "same but faster"),
            (r"\b(?:cancel|abort|stop)\b.*\bcurrent\b.*\btask\b", "cancel current task"),
            (r"^cancel last(?:\b| .*)", "cancel the last"),
            (r"\bstop\b.*\bthat\b", "stop that"),
            (r"\bincrease\b.*\bsensitivity\b", "increase sensitivity"),
            (r"\bdecrease\b.*\bsensitivity\b", "decrease sensitivity"),
            (r"\b(?:be\s+)?more\s+strict\b.*\bcommands\b", "be more strict on commands"),
            (r"\b(?:be\s+)?less\s+strict\b.*\bcommands\b", "be less strict on commands"),
            (r"\bincrease\b.*\bresponse\b.*\bdelay\b", "increase response delay"),
            (r"\bdecrease\b.*\bresponse\b.*\bdelay\b", "decrease response delay"),
            (r"\bincrease\b.*\bsilence\b.*\bthreshold\b", "increase silence threshold"),
            (r"\bdecrease\b.*\bsilence\b.*\bthreshold\b", "decrease silence threshold"),
            (r"\bincrease\b.*\btracking\b.*\bpriority\b", "increase tracking priority"),
            (r"\bdecrease\b.*\btracking\b.*\bpriority\b", "decrease tracking priority"),
            (r"\btalk\b.*\bless\b", "talk less"),
            (r"\brun\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bconnect\b.*\b(app|boards?|smart\s+sentry)\b.*\b(com|port|ports|serial)\b.*\benable\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bconnect\b.*\benable\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bcancel\b.*\ball\b.*\b(queue|queued|tasks?)\b", "cancel all tasks in queue"),
            (r"\bclear\b.*\bqueue\b", "cancel all tasks in queue"),
            (r"\bcancel\b.*\b(last|latest)\b", "cancel the last"),
            (r"\bconnect\b.*\bapp\b.*\bcom\b.*\bports?\b", "connect the app to com ports"),
            (r"\bdisconnect\b.*\b(app|link|controller|board|boards|smart\s+sentry|com|port|ports|serial)\b", "disconnect smart sentry boards"),
            (r"\benable\b.*\bsmart\s+sentry\b", "enable smart sentry"),
            (r"\bdisable\b.*\bsmart\s+sentry\b", "disable smart sentry"),
            (r"\bresume\b.*\b(auto\s*tracking|autotracking|guard(?:ing)?\s*mode|smart\s+sentry)\b", "resume guarding mode"),
            (r"\bconnect\b.*\bsmart\s+sentry\b.*\bboards?\b", "connect smart sentry boards"),
            (r"\bconnect\b.*\b(app|com|port|ports|serial)\b", "connect boards"),
            (r"\bconnect\b.*\bboards?\b", "connect boards"),
            (r"\bopen\b.*\b(camera|video)\b", "open camera"),
            (r"\bclose\b.*\b(camera|video)\b", "close camera"),
            *iter_voice_toggle_command_patterns(),
            (r"\bchange\b.*\btheme\b.*\b(anything|something|another|different)\b", "change the theme to anything else"),
            (r"\bchange\b.*\btheme\b", "change theme"),
            (r"\brun\b.*\bdiagnostic(?:s)?\b", "run diagnostics"),
            (r"\bcheck\b.*\bstatus\b", "check status"),
            (r"\bstatus\b.*\breport\b", "status report"),
            (r"\banaly(?:ze|sis)?\b.*\bcurrent app\b.*\bbehavior\b", "analyze current app behavior"),
            (r"\bstart\b.*\btracking\b", "start tracking"),
            (r"\bstop\b.*\btracking\b", "stop tracking"),
            (r"\bgo\b.*\bhome\b", "go home"),
            (r"\bgo\b.*\brest\b", "go rest"),
        )
        for pattern, canonical in canonical_rules:
            if re.search(pattern, corrected):
                return canonical
        fuzzy_match = self._fuzzy_command_fragment_match(corrected)
        if fuzzy_match:
            return fuzzy_match
        return corrected

    def _should_reject_low_signal_window_text(self, sanitized: str, *, confidence: Optional[float] = None) -> bool:
        tokens = [tok for tok in re.findall(r"[a-z0-9]+", str(sanitized or "").lower()) if tok]
        if not tokens:
            return True
        filler_words = {"up", "to", "keep", "he", "has", "uh", "um", "ah", "oh"}
        if all(token in filler_words for token in tokens):
            return True
        if len(tokens) >= 2 and len(set(tokens)) == 1 and tokens[0] in filler_words:
            return True
        if not self._looks_meaningful_followup_text(str(sanitized or "")):
            return True
        if confidence is None:
            return False
        try:
            conf = float(confidence)
        except Exception:
            return False
        known_fragments = set(self._command_grammar_fragments())
        if conf < 0.35 and len(tokens) <= 2 and str(sanitized or "") not in known_fragments:
            return True
        return False

    def start(self) -> bool:
        if self._worker is not None and self._worker.is_alive():
            return True
        self._stop.clear()
        self._worker = threading.Thread(target=self._listen_loop, name="sentry-voice-vosk", daemon=True)
        self._worker.start()
        return True

    def stop(self) -> None:
        self._stop.set()

    def signal_wake_word_detected(self, wake_word: str) -> None:
        """Called by acoustic guard or external coordinator when wake word is detected.
        
        This allows coordination between audio systems sharing a microphone.
        """
        if self._enable_wake_word_coordination and str(wake_word or "").strip().lower() == self._wake_word:
            self._wake_word_detected_event.set()
            self._command_window_until_s = max(
                float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
                time.time() + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
            )

    def open_command_window(self, *, duration_s: Optional[float] = None, reason: str = "") -> None:
        """Allow follow-up speech without requiring the wake word again.

        This is used by higher-level UI flows that explicitly prompt the
        operator for an immediate answer, such as yes/no confirmation or the
        post-command "what next" prompt.
        """
        duration = float(duration_s if duration_s is not None else self._wake_command_window_s)
        duration = max(0.5, duration)
        self._command_window_until_s = max(
            float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
            time.time() + duration,
        )
        if reason:
            self._on_log(
                f"[VOICE-DIAG] external-command-window-open reason='{reason}' "
                f"window_until={self._command_window_until_s:.2f}"
            )

    def _audio_callback(self, indata, _frames, _time_info, status) -> None:
        if status:
            self._on_log(f"Vosk input status: {status}")
        if self._stop.is_set():
            return
        chunk = self._coerce_stream_chunk(indata)
        boosted_chunk, rms, peak, gain = self._boost_audio_chunk(chunk)
        self._log_audio_chunk_diagnostics(chunk, rms, peak, gain, queue_depth=self._audio_queue.qsize())
        try:
            self._audio_queue.put_nowait(boosted_chunk)
        except queue.Full:
            try:
                self._audio_queue.get_nowait()
            except queue.Empty:
                pass
            try:
                self._audio_queue.put_nowait(boosted_chunk)
            except Exception:
                pass

    def _open_wake_command_window(self, *, now: Optional[float] = None) -> float:
        current_time = float(now if now is not None else time.time())
        self._command_window_until_s = max(
            float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
            current_time + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
        )
        return self._command_window_until_s

    def _emit_partial_wake_ack(self, partial_text: str) -> None:
        if not self._wake_word:
            return
        now = time.time()
        self._emit_transcript("wake_partial", partial_text, source="wake")
        self._on_log(f"[VOICE-DIAG] wake-word-partial text='{partial_text}'")
        if now <= float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0):
            self._on_log(
                f"[VOICE-DIAG] partial-wake-ack-suppressed suppress_until={self._suppress_wake_only_until_s:.2f}"
            )
            return
        self._suppress_wake_only_until_s = max(
            float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0),
            now + float(getattr(self, "_partial_wake_ack_hold_s", 1.75) or 1.75),
        )
        window_until = self._open_wake_command_window(now=now)
        self._on_log(
            f"[VOICE-DIAG] partial-wake-ack-emitted wake='{self._wake_word}' "
            f"window_until={window_until:.2f} "
            f"suppress_until={self._suppress_wake_only_until_s:.2f}"
        )
        try:
            self._on_command(self._wake_word)
        except Exception as exc:
            self._on_log(f"[VOICE-DIAG] partial-wake-ack failed: {exc}")

    def _normalize_command_text(self, text: str, *, confidence: Optional[float] = None) -> str:
        normalized = str(text or "").strip().lower()
        normalized = re.sub(r"\s+", " ", normalized)
        if not normalized:
            return ""
        sanitized = re.sub(r"[^a-z0-9 ]+", " ", normalized)
        sanitized = re.sub(r"\s+", " ", sanitized).strip()
        now = time.time()
        if self._recent_output_input_block_active(now=now):
            self._on_log(f"[VOICE-DIAG] self-echo-final-window-suppressed text='{sanitized}'")
            return ""
        if self._matches_recent_output_echo(sanitized, partial=False):
            self._on_log(f"[VOICE-DIAG] self-echo-final-suppressed text='{sanitized}'")
            return ""
        corrected = self._canonicalize_command_text(sanitized)
        if not self._wake_word:
            final_text = corrected or sanitized or normalized
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            return final_text
        wake_word = re.sub(r"[^a-z0-9 ]+", " ", str(self._wake_word or "").strip().lower())
        wake_word = re.sub(r"\s+", " ", wake_word).strip()
        if not wake_word:
            final_text = corrected or sanitized or normalized
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            return final_text
        wake_aliases = self._wake_word_aliases(wake_word)
        pattern = r"\b(?:" + "|".join(re.escape(alias) for alias in wake_aliases) + r")\b"
        wake_matched = bool(re.search(pattern, corrected))
        if not wake_matched and wake_aliases:
            wake_matched = self._fuzzy_contains_wake(corrected, wake_aliases)
        if wake_matched:
            stripped = re.sub(pattern, " ", corrected).strip()
            stripped = re.sub(r"\s+", " ", stripped)
            stripped = self._canonicalize_command_text(stripped)
            self._open_wake_command_window(now=now)
            if stripped and self._should_reject_low_signal_window_text(stripped, confidence=confidence):
                self._on_log(
                    f"[VOICE-DIAG] wake-followup-noise-rejected wake='{wake_word}' text='{stripped}'"
                )
                if now <= float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0):
                    self._on_log(
                        f"[VOICE-DIAG] wake-word-final-suppressed text='{corrected}' "
                        f"suppress_until={self._suppress_wake_only_until_s:.2f}"
                    )
                    return ""
                return wake_word
            final_text = f"{wake_word} {stripped}".strip() if stripped else wake_word
            self._on_log(
                f"[VOICE-DIAG] wake-word-match wake='{wake_word}' text='{corrected}' window_until={self._command_window_until_s:.2f}"
            )
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            if not stripped:
                if now <= float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0):
                    self._on_log(
                        f"[VOICE-DIAG] wake-word-final-suppressed text='{corrected}' "
                        f"suppress_until={self._suppress_wake_only_until_s:.2f}"
                    )
                    return ""
                return wake_word
            return final_text

        final_text = corrected or sanitized or normalized
        self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
        self._emit_transcript("final", final_text, source="final", confidence=confidence)

        # Fail-open for explicit high-intent command phrases so wake-word OCR drift
        # does not block critical operations like connect/enable.
        explicit_patterns = (
            r"\b(?:priority|override)\b",
            r"\bresume\b.*\blast\b.*\btask\b",
            r"\bdo\b.*\bagain\b",
            r"\bsame\b.*\bfaster\b",
            r"\b(?:cancel|abort|stop)\b.*\b(current\s+task|that)\b",
            r"\bincrease\b.*\b(sensitivity|response\s+delay|silence\s+threshold|tracking\s+priority)\b",
            r"\bdecrease\b.*\b(sensitivity|response\s+delay|silence\s+threshold|tracking\s+priority)\b",
            r"\b(?:be\s+)?(?:more|less)\s+strict\b.*\bcommands\b",
            r"\btalk\b.*\bless\b",
            r"\bcancel\b.*\b(last|queue|queued|tasks?)\b",
            r"\bconnect\b.*\benable\b.*\bsmart\s+sentry\b",
            r"\bconnect\b.*\b(board|boards|com|port|serial)\b",
            r"\bdisconnect\b.*\b(board|boards|smart\s+sentry|link|controller|com|port|ports|serial)\b",
            r"\benable\b.*\bsmart\s+sentry\b",
            r"\bdisable\b.*\bsmart\s+sentry\b",
            r"\bstart\b.*\btracking\b",
            r"\bresume\b.*\b(auto\s*tracking|autotracking|guard(ing)?\s*mode)\b",
            r"\b(?:open|close)\b.*\b(camera|video)\b",
            r"\b(?:enable|disable)\b.*\b(face\s+recognition|human\s+voice|assistant\s+auto\s+speak|shortcuts?)\b",
            r"\bvoice\s+style\b",
            r"\b(?:load|switch(?:\s+to)?|use)\b.*\bprofile\b",
            r"\b(?:use|switch(?:\s+to)?|load)\b.*\b(nano|small|medium|large|xlarge|tiny|yolo|object\s+detection|best\s+mode)\b",
            r"\b(?:set|increase|decrease)\b.*\b(brightness|speed|confidence)\b",
            r"\b(?:tell|make)\b.*\bjoke\b",
            r"\bpersonality\b",
        )
        if any(re.search(expr, final_text) for expr in explicit_patterns):
            self._command_window_until_s = max(
                float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
                now + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
            )
            self._on_log(
                f"[VOICE-DIAG] fail-open-command text='{final_text}' window_until={self._command_window_until_s:.2f}"
            )
            return final_text

        if now <= float(getattr(self, "_command_window_until_s", 0.0) or 0.0):
            if self._should_reject_low_signal_window_text(final_text, confidence=confidence):
                self._on_log(f"[VOICE-DIAG] command-window-noise-rejected text='{final_text}'")
                return ""
            self._on_log(f"[VOICE-DIAG] command-window-accept text='{final_text}'")
            return final_text
        self._on_log(f"[VOICE-DIAG] command-rejected-no-wake text='{final_text}'")
        return ""

    def _listen_loop(self) -> None:
        try:
            import json
            import sounddevice as sd
            from vosk import KaldiRecognizer, Model
        except Exception as exc:
            self._on_log(f"Vosk listener dependencies unavailable: {exc}")
            return

        model_dir = self._resolve_model_directory()
        if not model_dir.is_dir():
            self._on_log(f"Vosk model path not found: {model_dir}")
            return

        try:
            model = Model(str(model_dir))
            grammar_phrases = self._recognizer_grammar_phrases()
            try:
                recognizer = KaldiRecognizer(model, 16000, json.dumps(grammar_phrases))
                self._on_log(
                    f"[VOICE-DIAG] recognizer-grammar-enabled phrases={len(grammar_phrases)} wake='{self._wake_word}'"
                )
            except Exception as grammar_exc:
                self._on_log(f"[VOICE-DIAG] recognizer-grammar-fallback reason={grammar_exc}")
                recognizer = KaldiRecognizer(model, 16000)
        except Exception as exc:
            self._on_log(f"Failed to initialize Vosk recognizer: {exc}")
            return

        try:
            device_index = self._resolve_input_device(sd)
            with sd.InputStream(
                samplerate=16000,
                blocksize=4000,
                dtype="float32",
                channels=1,
                device=device_index,
            ) as stream:
                self._emit_transcript("status", "listening", source="vosk")
                if device_index is not None:
                    self._on_log(f"Offline voice command listener started on device index {device_index}")
                else:
                    self._on_log("Offline voice command listener started")
                while not self._stop.is_set():
                    if self._enable_wake_word_coordination and self._wake_word_detected_event.is_set():
                        self._wake_word_detected_event.clear()
                        self._command_window_until_s = max(
                            float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
                            time.time() + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
                        )
                    try:
                        frames, overflowed = stream.read(4000)
                    except Exception as read_exc:
                        self._on_log(f"Vosk input read failed: {read_exc}")
                        continue
                    if overflowed:
                        self._on_log("Vosk input status: input overflow")
                    chunk = self._coerce_stream_chunk(frames)
                    if not chunk:
                        continue
                    data, rms, peak, gain = self._boost_audio_chunk(chunk)
                    self._capture_chunk_signature(data, rms)
                    self._log_audio_chunk_diagnostics(chunk, rms, peak, gain)
                    if recognizer.AcceptWaveform(data):
                        result = json.loads(recognizer.Result() or "{}")
                        normalized = self._normalize_command_text(result.get("text", ""))
                        if not normalized:
                            continue
                        now = time.time()
                        if self._command_cooldown_s > 0.0 and (now - self._last_emit_s) < self._command_cooldown_s:
                            self._on_log("[VOICE-DIAG] command-throttled-by-cooldown")
                            continue
                        self._last_emit_s = now
                        self._on_log(f"[VOICE-DIAG] command-emitted='{normalized}'")
                        self._on_command(normalized)
                    else:
                        try:
                            partial = json.loads(recognizer.PartialResult() or "{}")
                            partial_text = str(partial.get("partial", "") or "").strip().lower()
                            if partial_text:
                                if self._recent_output_input_block_active(now=time.time()):
                                    self._on_log(f"[VOICE-DIAG] self-echo-partial-window-suppressed text='{partial_text}'")
                                    continue
                                if self._matches_recent_output_echo(partial_text, partial=True):
                                    self._on_log(f"[VOICE-DIAG] self-echo-partial-suppressed text='{partial_text}'")
                                    continue
                                self._emit_transcript("partial", partial_text, source="vosk")
                                if self._partial_contains_wake(partial_text):
                                    self._emit_partial_wake_ack(partial_text)
                        except Exception:
                            pass
        except Exception as exc:
            self._on_log(f"Vosk listen loop terminated: {exc}")

    @staticmethod
    def _looks_like_vosk_model_dir(candidate: Path) -> bool:
        if not candidate.is_dir():
            return False
        required_parts = ("am", "conf", "graph", "ivector")
        return all((candidate / part).exists() for part in required_parts)

    def _resolve_model_directory(self) -> Path:
        candidate = Path(self._model_path)
        if self._looks_like_vosk_model_dir(candidate):
            return candidate
        try:
            subdirs = [path for path in candidate.iterdir() if self._looks_like_vosk_model_dir(path)]
        except Exception:
            return candidate
        if not subdirs:
            return candidate

        def _rank(path: Path) -> tuple[int, int]:
            name = path.name.lower()
            score = 0
            if "large" in name or "lgraph" in name:
                score += 40
            elif "medium" in name:
                score += 25
            elif "base" in name:
                score += 15
            elif "small" in name:
                score -= 15
            if any(token in name for token in ("en-us", "en_us", "english", ".en")):
                score += 5
            return score, -len(name)

        resolved = max(subdirs, key=_rank)
        self._on_log(f"[VOICE] Resolved Vosk model directory: {resolved}")
        return resolved

    def _resolve_input_device(self, sd_module) -> Optional[int]:
        target = self._device_name.lower().strip()
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


class WindowsSpeechCommandListener(VoskCommandListener):
    """Windows-native speech recognizer with Vosk fallback for systems where live Vosk decoding is unreliable."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._recognizer_process: Optional[subprocess.Popen] = None
        self._signature_probe = MicrophoneSignatureProbe(device_name=self._device_name, on_log=self._on_log)

    def _latest_signature(self) -> dict[str, object]:
        return self._signature_probe.latest_signature()

    def stop(self) -> None:
        super().stop()
        self._signature_probe.stop()
        self._terminate_recognizer_process()

    def _terminate_recognizer_process(self) -> None:
        proc = self._recognizer_process
        self._recognizer_process = None
        if proc is None:
            return
        try:
            if proc.poll() is None:
                proc.terminate()
        except Exception:
            pass
        try:
            if proc.poll() is None:
                proc.kill()
        except Exception:
            pass

    def _powershell_listener_script(self) -> str:
        phrases = self._windows_speech_grammar_phrases()
        phrase_literals = ", ".join(
            "'" + phrase.replace("'", "''") + "'"
            for phrase in phrases
            if phrase and phrase != "[unk]"
        )
        return f"""
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$culture = [System.Globalization.CultureInfo]::GetCultureInfo('en-US')
$engine = New-Object System.Speech.Recognition.SpeechRecognitionEngine($culture)
$engine.SetInputToDefaultAudioDevice()
$engine.InitialSilenceTimeout = [TimeSpan]::FromSeconds(4)
$engine.BabbleTimeout = [TimeSpan]::FromSeconds(0)
$engine.EndSilenceTimeout = [TimeSpan]::FromMilliseconds(500)
$engine.EndSilenceTimeoutAmbiguous = [TimeSpan]::FromMilliseconds(350)
$engine.LoadGrammar((New-Object System.Speech.Recognition.DictationGrammar))
$choices = New-Object System.Speech.Recognition.Choices
foreach ($phrase in @({phrase_literals})) {{
    if (-not [string]::IsNullOrWhiteSpace($phrase)) {{
        [void]$choices.Add($phrase)
    }}
}}
$grammarBuilder = New-Object System.Speech.Recognition.GrammarBuilder
$grammarBuilder.Culture = $culture
$grammarBuilder.Append($choices)
$engine.LoadGrammar((New-Object System.Speech.Recognition.Grammar($grammarBuilder)))
Register-ObjectEvent -InputObject $engine -EventName SpeechHypothesized -SourceIdentifier 'SentrySpeechHypothesized' -Action {{
    $result = $Event.SourceEventArgs.Result
    if ($null -ne $result -and -not [string]::IsNullOrWhiteSpace($result.Text)) {{
        [Console]::Out.WriteLine('partial|' + $result.Text)
    }}
}} | Out-Null
Register-ObjectEvent -InputObject $engine -EventName SpeechRecognized -SourceIdentifier 'SentrySpeechRecognized' -Action {{
    $result = $Event.SourceEventArgs.Result
    if ($null -ne $result -and -not [string]::IsNullOrWhiteSpace($result.Text)) {{
        [Console]::Out.WriteLine('recognized|' + $result.Confidence.ToString('0.00') + '|' + $result.Text)
    }}
}} | Out-Null
$engine.RecognizeAsync([System.Speech.Recognition.RecognizeMode]::Multiple)
[Console]::Out.WriteLine('status|listening')
try {{
    while ($true) {{
        Wait-Event -Timeout 1 | Out-Null
    }}
}} finally {{
    try {{ $engine.RecognizeAsyncCancel() }} catch {{}}
    try {{ $engine.RecognizeAsyncStop() }} catch {{}}
    try {{ Unregister-Event -SourceIdentifier 'SentrySpeechHypothesized' -ErrorAction SilentlyContinue }} catch {{}}
    try {{ Unregister-Event -SourceIdentifier 'SentrySpeechRecognized' -ErrorAction SilentlyContinue }} catch {{}}
}}
""".strip()

    def _listen_loop(self) -> None:
        if os.name != "nt":
            super()._listen_loop()
            return
        try:
            script = self._powershell_listener_script()
            encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
            self._recognizer_process = subprocess.Popen(
                [
                    "powershell.exe",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-EncodedCommand",
                    encoded,
                ],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
            )
        except Exception as exc:
            self._on_log(f"[VOICE] Windows speech listener unavailable; falling back to Vosk: {exc}")
            super()._listen_loop()
            return

        self._on_log("[VOICE] Runtime STT backend: Windows native speech")
        self._signature_probe.start()
        proc = self._recognizer_process
        try:
            while not self._stop.is_set() and proc is not None:
                line = proc.stdout.readline() if proc.stdout is not None else ""
                if not line:
                    if proc.poll() is not None:
                        break
                    continue
                message = str(line or "").strip()
                if not message:
                    continue
                if message == "status|listening":
                    self._emit_transcript("status", "listening", source="windows")
                    self._on_log("Windows speech command listener started on default input device")
                    continue
                if message.startswith("partial|"):
                    partial_text = str(message.split("|", 1)[1] or "").strip().lower()
                    if partial_text:
                        if self._recent_output_input_block_active(now=time.time()):
                            self._on_log(f"[VOICE-DIAG] self-echo-partial-window-suppressed text='{partial_text}'")
                            continue
                        if self._matches_recent_output_echo(partial_text, partial=True):
                            self._on_log(f"[VOICE-DIAG] self-echo-partial-suppressed text='{partial_text}'")
                            continue
                        self._emit_transcript("partial", partial_text, source="windows")
                        if self._partial_contains_wake(partial_text):
                            self._emit_partial_wake_ack(partial_text)
                    continue
                if message.startswith("recognized|"):
                    _prefix, confidence_text, raw_text = (message.split("|", 2) + ["", "", ""])[:3]
                    recognized_text = str(raw_text or "").strip().lower()
                    if recognized_text:
                        self._on_log(
                            f"[VOICE-DIAG] windows-speech-recognized confidence={confidence_text} text='{recognized_text}'"
                        )
                    normalized = self._normalize_command_text(recognized_text, confidence=float(confidence_text or 0.0))
                    if not normalized:
                        continue
                    now = time.time()
                    if self._command_cooldown_s > 0.0 and (now - self._last_emit_s) < self._command_cooldown_s:
                        self._on_log("[VOICE-DIAG] command-throttled-by-cooldown")
                        continue
                    self._last_emit_s = now
                    self._on_log(f"[VOICE-DIAG] command-emitted='{normalized}'")
                    self._on_command(normalized)
                    continue
                self._on_log(f"[VOICE-DIAG] windows-speech-log {message}")
        except Exception as exc:
            self._on_log(f"[VOICE] Windows speech listener failed; falling back to Vosk: {exc}")
        finally:
            self._terminate_recognizer_process()
            self._signature_probe.stop()

        if not self._stop.is_set():
            self._on_log("[VOICE] Windows speech listener exited; falling back to Vosk")
            super()._listen_loop()


def _default_windows_input_device_name() -> str:
    if os.name != "nt":
        return ""
    try:
        import sounddevice as sd

        devices = sd.query_devices()
        pair = sd.default.device
        input_index = pair[0] if hasattr(pair, "__getitem__") else None
        if input_index is None or int(input_index) < 0:
            return ""
        return str(devices[int(input_index)].get("name", "") or "").strip()
    except Exception:
        return ""


def _normalized_audio_device_signature(name: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", str(name or "").strip().lower())
    normalized = re.sub(r"\s+", " ", normalized).strip()
    if not normalized:
        return ""
    generic_tokens = {"microphone", "input", "audio", "device", "default"}
    tokens = [token for token in normalized.split(" ") if token and token not in generic_tokens]
    if not tokens:
        tokens = [token for token in normalized.split(" ") if token]
    return " ".join(tokens)


def _can_use_windows_speech_backend(device_name: str) -> bool:
    if os.name != "nt":
        return False
    requested = str(device_name or "").strip()
    default_name = _default_windows_input_device_name().strip()
    if not default_name:
        return False
    if not requested:
        return True
    # Windows native speech can only bind to the current default input device.
    # When the operator explicitly selects a microphone, keep STT on Vosk so the
    # configured device is actually honored.
    return False


class SharedAudioInputManager:
    """Optional unified audio input handler for systems needing to share a microphone.
    
    When both acoustic guard and voice listener need the same device,
    this manager opens a single stream and feeds both systems.
    """
    
    def __init__(self, device_name: str = "", on_log: Optional[Callable[[str], None]] = None) -> None:
        self._device_name = str(device_name or "").strip()
        self._on_log = on_log or (lambda _msg: None)
        self._stream = None
        self._consumers: list[Callable[[bytes], None]] = []
        self._lock = threading.Lock()
    
    def add_consumer(self, callback: Callable[[bytes], None]) -> None:
        """Register a consumer to receive audio chunks."""
        with self._lock:
            if callback not in self._consumers:
                self._consumers.append(callback)
    
    def remove_consumer(self, callback: Callable[[bytes], None]) -> None:
        """Unregister a consumer."""
        with self._lock:
            if callback in self._consumers:
                self._consumers.remove(callback)
    
    def _broadcast_audio(self, chunk: bytes) -> None:
        """Send audio chunk to all registered consumers."""
        with self._lock:
            for consumer in self._consumers:
                try:
                    consumer(chunk)
                except Exception:
                    pass
    
    def close(self) -> None:
        """Stop the shared stream and clear consumers."""
        try:
            if self._stream is not None:
                self._stream.stop()
                self._stream.close()
        except Exception:
            pass
        with self._lock:
            self._consumers.clear()


class VoiceRuntimeController:
    """Standalone voice runtime suitable for UI and headless execution."""

    def __init__(
        self,
        *,
        model_path: str,
        sounds_dir: str,
        wake_word: str,
        command_cooldown_s: float,
        on_command: Callable[[str], None],
        on_transcript: Optional[Callable[[dict[str, object]], None]] = None,
        on_log: Optional[Callable[[str], None]] = None,
        neural_tts_enabled: bool = False,
        preferred_tts_backend: str = "auto",
        preferred_voice_name: str = "",
        # Kokoro offline TTS (primary — no internet/key required)
        kokoro_model_path: str = "",
        kokoro_voices_path: str = "",
        kokoro_voice_name: str = "af_sarah",
        kokoro_speed: float = 1.0,
        device_name: str = "",
        # Azure TTS (optional upgrade — highest quality if credentials available)
        azure_speech_key: str = "",
        azure_speech_region: str = "",
        azure_voice_name: str = "en-US-JennyNeural",
        commands_enabled: bool = True,
        enable_wake_word_coordination: bool = False,
    ) -> None:
        self._on_log = on_log or (lambda _msg: None)
        self._sounds_dir = Path(sounds_dir)
        self._sounds_dir.mkdir(parents=True, exist_ok=True)
        self._commands_enabled = bool(commands_enabled)
        self._wav_player = AsyncWavPlayer(on_log=self._on_log)
        listener_kwargs = dict(
            model_path=model_path,
            wake_word=wake_word,
            command_cooldown_s=command_cooldown_s,
            on_command=on_command,
            on_transcript=on_transcript,
            on_log=self._on_log,
            device_name=device_name,
            enable_wake_word_coordination=enable_wake_word_coordination,
        )
        if _can_use_windows_speech_backend(device_name):
            default_input_name = _default_windows_input_device_name() or "default input device"
            self._on_log(f"[VOICE] Runtime STT preference: Windows native speech ({default_input_name})")
            self._listener = WindowsSpeechCommandListener(**listener_kwargs)
        else:
            configured_input_name = str(device_name or "").strip()
            if os.name == "nt" and configured_input_name:
                self._on_log(f"[VOICE] Runtime STT preference: Vosk offline (configured input: {configured_input_name})")
            else:
                self._on_log("[VOICE] Runtime STT preference: Vosk offline")
            self._listener = VoskCommandListener(**listener_kwargs)

        self._kokoro_tts: Optional[KokoroTTS] = None
        self._neural_tts: Optional[AzureNeuralTTS] = None
        self._edge_tts: Optional[EdgeNeuralTTS] = None
        self._active_speech_backend: str = "unavailable"
        self._active_voice_name: str = ""

        _kokoro_model = str(kokoro_model_path or "").strip()
        _kokoro_voices = str(kokoro_voices_path or "").strip()
        kokoro_available = bool(_kokoro_model and Path(_kokoro_model).is_file() and _kokoro_voices and Path(_kokoro_voices).is_file())
        preferred_backend = str(preferred_tts_backend or "auto").strip().lower()
        if preferred_backend not in {"auto", "kokoro", "azure", "edge"}:
            preferred_backend = "auto"
        preferred_voice = str(preferred_voice_name or "").strip()

        backend_order = ["kokoro", "azure", "edge"]
        if preferred_backend != "auto":
            backend_order.insert(0, preferred_backend)

        for backend_name in dict.fromkeys(backend_order):
            if backend_name == "kokoro":
                if not kokoro_available:
                    continue
                self._kokoro_tts = KokoroTTS(
                    self._wav_player,
                    model_path=_kokoro_model,
                    voices_path=_kokoro_voices,
                    voice_name=kokoro_voice_name,
                    speed=kokoro_speed,
                    on_log=self._on_log,
                )
                if self._kokoro_tts.enabled:
                    self._active_speech_backend = "kokoro"
                    self._active_voice_name = str(kokoro_voice_name or "").strip()
                    self._on_log(f"[VOICE] Runtime speech backend: Kokoro offline (voice: {kokoro_voice_name})")
                    break
            elif backend_name == "azure":
                if not neural_tts_enabled:
                    continue
                if not (str(azure_speech_key or "").strip() and str(azure_speech_region or "").strip()):
                    continue
                azure_voice = str(preferred_voice or azure_voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
                self._neural_tts = AzureNeuralTTS(
                    self._wav_player,
                    speech_key=azure_speech_key,
                    speech_region=azure_speech_region,
                    voice_name=azure_voice,
                    output_dir=str(self._sounds_dir / "_generated_tts"),
                    on_log=self._on_log,
                )
                if self._neural_tts.enabled:
                    self._active_speech_backend = "azure"
                    self._active_voice_name = azure_voice
                    self._on_log(f"[VOICE] Runtime speech backend: Azure neural (voice: {azure_voice})")
                    break
            elif backend_name == "edge":
                if not neural_tts_enabled:
                    continue
                edge_voice = str(preferred_voice or azure_voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
                self._edge_tts = EdgeNeuralTTS(
                    self._wav_player,
                    voice_name=edge_voice,
                    output_dir=str(self._sounds_dir / "_generated_tts"),
                    on_log=self._on_log,
                )
                if self._edge_tts.enabled:
                    self._active_speech_backend = "edge"
                    self._active_voice_name = edge_voice
                    self._on_log(f"[VOICE] Runtime speech backend: Edge neural (voice: {edge_voice})")
                    break

        if self._active_speech_backend == "unavailable" and neural_tts_enabled and not kokoro_available:
            self._on_log("[VOICE] Kokoro runtime speech unavailable: missing model or voices file")
        if preferred_backend != "auto" and self._active_speech_backend != preferred_backend:
            if self._active_speech_backend == "unavailable":
                self._on_log(f"[VOICE] Requested speech backend '{preferred_backend}' is unavailable")
            else:
                self._on_log(
                    f"[VOICE] Requested speech backend '{preferred_backend}' unavailable; using '{self._active_speech_backend}' instead"
                )

    def start(self) -> None:
        if self._commands_enabled:
            self._listener.start()
        else:
            self._on_log("Offline voice command listener disabled; voice playback runtime remains active")

    @property
    def neural_tts_ready(self) -> bool:
        if self._kokoro_tts is not None and self._kokoro_tts.enabled:
            return True
        if self._neural_tts is not None and self._neural_tts.enabled:
            return True
        if self._edge_tts is not None and self._edge_tts.enabled:
            return True
        return False

    def stop(self) -> None:
        if self._commands_enabled:
            self._listener.stop()
        self.stop_speaking()
        if self._neural_tts is not None:
            self._neural_tts.close()
        if self._kokoro_tts is not None:
            self._kokoro_tts.close()
        if self._edge_tts is not None:
            self._edge_tts.close()
        self._wav_player.close()

    def stop_speaking(self) -> None:
        try:
            self._listener.clear_recent_output_suppression()
        except Exception:
            pass
        if self._neural_tts is not None:
            self._neural_tts.stop()
        if self._kokoro_tts is not None:
            self._kokoro_tts.stop()
        if self._edge_tts is not None:
            self._edge_tts.stop()
        self._wav_player.stop()

    @staticmethod
    def _estimated_speech_duration_s(text: str) -> float:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip())
        if not cleaned:
            return 0.0
        return max(1.2, min(12.0, (len(cleaned) / 18.0) + 0.9))

    def play_event(self, event_name: str) -> bool:
        key = str(event_name or "").strip().lower()
        if not key:
            return False
        wav_path = self._sounds_dir / f"{key}.wav"
        return self._wav_player.play_file(str(wav_path))

    def speak_dynamic(self, text: str) -> bool:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip())
        if not cleaned:
            return False
        self.register_output_echo_suppression(cleaned)
        if self._kokoro_tts is not None and self._kokoro_tts.enabled:
            return self._kokoro_tts.speak_async(cleaned)
        if self._neural_tts is not None and self._neural_tts.enabled:
            return self._neural_tts.speak_async(cleaned)
        if self._edge_tts is not None and self._edge_tts.enabled:
            return self._edge_tts.speak_async(cleaned)
        return False

    def register_output_echo_suppression(self, text: str, *, extra_hold_s: float = 1.0) -> None:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip())
        if not cleaned:
            return
        try:
            speech_duration_s = self._estimated_speech_duration_s(cleaned)
            self._listener.suppress_recent_output_text(
                cleaned,
                hold_s=speech_duration_s + max(0.0, float(extra_hold_s or 0.0)),
                block_s=speech_duration_s + 0.35,
            )
        except Exception:
            pass

    def signal_wake_word_detected(self, wake_word: str) -> None:
        """Forward external wake-word detection into the command listener window."""
        try:
            self._listener.signal_wake_word_detected(wake_word)
        except Exception as exc:
            self._on_log(f"[VOICE] wake coordination signal failed: {exc}")

    def open_command_window(self, *, duration_s: Optional[float] = None, reason: str = "") -> None:
        """Prime the listener for a follow-up command without requiring wake word repetition."""
        try:
            self._listener.open_command_window(duration_s=duration_s, reason=reason)
        except Exception as exc:
            self._on_log(f"[VOICE] command-window coordination failed: {exc}")
