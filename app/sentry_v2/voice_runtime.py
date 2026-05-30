from __future__ import annotations

import os
import audioop
import base64
import math
import queue
import re
import subprocess
import tempfile
import threading
import time
import wave
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
        self._queue: "queue.Queue[tuple[str, int, str]]" = queue.Queue()
        self._stop = threading.Event()
        self._mci_lock = threading.Lock()
        self._current_mci_alias = ""
        self._current_mci_channel = ""
        self._worker = threading.Thread(target=self._worker_loop, name="sentry-voice-wav", daemon=True)
        self._worker.start()

    @staticmethod
    def _clamp_volume_pct(volume_pct: object) -> int:
        try:
            return int(max(0, min(100, int(volume_pct))))
        except Exception:
            return 100

    @staticmethod
    def _normalize_channel(channel: object) -> str:
        normalized = str(channel or "default").strip().lower()
        return normalized or "default"

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

    def play_file(self, wav_path: str, *, volume_pct: int = 100, channel: str = "default") -> bool:
        path = str(wav_path or "").strip()
        if not path:
            return False
        if not Path(path).is_file():
            return False
        try:
            self._queue.put_nowait((path, self._clamp_volume_pct(volume_pct), self._normalize_channel(channel)))
            return True
        except Exception:
            return False

    def set_live_volume_pct(self, volume_pct: int, *, channel: str = "speech") -> bool:
        if os.name != "nt":
            return False
        target_channel = self._normalize_channel(channel)
        with self._mci_lock:
            alias = str(self._current_mci_alias or "").strip()
            current_channel = self._normalize_channel(self._current_mci_channel)
        if not alias:
            return False
        if target_channel and current_channel != target_channel:
            return False
        return self._set_mci_volume(alias, self._clamp_volume_pct(volume_pct))

    def _set_mci_volume(self, alias: str, volume_pct: int) -> bool:
        if os.name != "nt":
            return False
        try:
            import ctypes

            mci_send_string = ctypes.windll.winmm.mciSendStringW
            target = int(round(self._clamp_volume_pct(volume_pct) * 10.0))
            return mci_send_string(f"setaudio {alias} volume to {target}", None, 0, None) == 0
        except Exception:
            return False

    def _play_via_mci(self, path: str, *, media_type: str, volume_pct: int, channel: str) -> bool:
        if os.name != "nt":
            return False
        try:
            import ctypes

            alias = f"sentry_voice_{int(time.time() * 1000)}"
            mci_send_string = ctypes.windll.winmm.mciSendStringW
            open_rc = mci_send_string(f'open "{path}" type {media_type} alias {alias}', None, 0, None)
            if open_rc != 0:
                return False
            with self._mci_lock:
                self._current_mci_alias = alias
                self._current_mci_channel = self._normalize_channel(channel)
            try:
                self._set_mci_volume(alias, volume_pct)
                play_rc = mci_send_string(f"play {alias} wait", None, 0, None)
                if play_rc == 0:
                    return True
                self._on_log(f"[VOICE] Windows audio playback failed for {path} (play rc={play_rc})")
                return False
            finally:
                mci_send_string(f"close {alias}", None, 0, None)
                with self._mci_lock:
                    if self._current_mci_alias == alias:
                        self._current_mci_alias = ""
                        self._current_mci_channel = ""
        except Exception:
            return False

    @staticmethod
    def _scale_pydub_segment(segment, volume_pct: int):
        if volume_pct <= 0:
            return segment.apply_gain(-120.0)
        if volume_pct >= 100:
            return segment
        return segment.apply_gain(20.0 * math.log10(max(0.001, float(volume_pct) / 100.0)))

    def _write_scaled_wav_copy(self, path: str, *, volume_pct: int) -> str:
        target_volume = self._clamp_volume_pct(volume_pct)
        if target_volume <= 0:
            return ""
        if target_volume >= 100:
            return str(path)
        temp_path = ""
        try:
            with wave.open(path, "rb") as wav_reader:
                params = wav_reader.getparams()
                sample_width = int(wav_reader.getsampwidth() or 2)
                frame_data = wav_reader.readframes(wav_reader.getnframes())
            scaled_frame_data = audioop.mul(frame_data, sample_width, float(target_volume) / 100.0)
            with tempfile.NamedTemporaryFile(prefix="smart_sentry_speech_", suffix=".wav", delete=False) as handle:
                temp_path = str(handle.name)
            with wave.open(temp_path, "wb") as wav_writer:
                wav_writer.setparams(params)
                wav_writer.writeframes(scaled_frame_data)
            return temp_path
        except Exception as exc:
            if temp_path:
                try:
                    Path(temp_path).unlink(missing_ok=True)
                except Exception:
                    pass
            self._on_log(f"[VOICE] Failed to prepare scaled speech audio for {path}: {exc}")
            return ""

    def _play_single(self, path: str, sa, *, volume_pct: int = 100, channel: str = "default") -> None:
        """Play a single audio file (WAV or MP3) using available backend."""
        try:
            ext = Path(path).suffix.lower()
            channel = self._normalize_channel(channel)
            volume_pct = self._clamp_volume_pct(volume_pct)
            if ext == ".mp3":
                if volume_pct <= 0:
                    return
                if os.name == "nt" and self._play_via_mci(path, media_type="mpegvideo", volume_pct=volume_pct, channel=channel):
                    return
                try:
                    from pydub import AudioSegment
                    from pydub.playback import play as pydub_play
                    seg = AudioSegment.from_mp3(path)
                    seg = self._scale_pydub_segment(seg, volume_pct)
                    pydub_play(seg)
                    return
                except Exception:
                    pass
                self._on_log(f"[VOICE] No MP3 playback backend is available for {path}")
                return
            # WAV playback
            if ext == ".wav":
                if volume_pct <= 0:
                    return
                if os.name == "nt" and channel == "speech" and volume_pct == 100:
                    if self._play_via_mci(path, media_type="waveaudio", volume_pct=volume_pct, channel=channel):
                        return
                if sa is not None:
                    if volume_pct == 100:
                        wave_obj = sa.WaveObject.from_wave_file(path)
                    else:
                        import wave

                        with wave.open(path, "rb") as wav_reader:
                            channels = wav_reader.getnchannels()
                            sample_width = wav_reader.getsampwidth()
                            sample_rate = wav_reader.getframerate()
                            frame_data = wav_reader.readframes(wav_reader.getnframes())
                        scaled_frame_data = audioop.mul(frame_data, sample_width, float(volume_pct) / 100.0)
                        wave_obj = sa.WaveObject(scaled_frame_data, channels, sample_width, sample_rate)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                else:
                    play_path = path
                    cleanup_path = ""
                    try:
                        if volume_pct != 100:
                            play_path = self._write_scaled_wav_copy(path, volume_pct=volume_pct)
                            if not play_path:
                                return
                            cleanup_path = play_path if play_path != path else ""
                        import winsound
                        winsound.PlaySound(play_path, winsound.SND_FILENAME)
                    finally:
                        if cleanup_path:
                            try:
                                Path(cleanup_path).unlink(missing_ok=True)
                            except Exception:
                                pass
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
                item = self._queue.get(timeout=0.20)
            except queue.Empty:
                continue
            if not item:
                continue
            if isinstance(item, tuple):
                wav_path, volume_pct, channel = item
            else:
                wav_path = str(item or "")
                volume_pct = 100
                channel = "default"
            if not wav_path:
                continue
            self._play_single(str(wav_path), sa, volume_pct=int(volume_pct), channel=str(channel or "default"))


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
        volume_pct: int = 100,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._model_path = str(model_path or "").strip()
        self._voices_path = str(voices_path or "").strip()
        self._voice_name = str(voice_name or "af_sarah").strip() or "af_sarah"
        self._speed = max(0.5, min(2.0, float(speed or 1.0)))
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)
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
        """Stop any in-progress speech and clear the queue.

        Only drains the pending queue — the worker thread is kept alive so that
        the Kokoro model does not need to be reloaded on every stop/speak cycle.
        Any phrase currently being synthesised will finish playing (Kokoro ONNX
        does not support mid-synthesis interruption), but queued phrases are
        discarded immediately.
        """
        try:
            # Drain the queue so pending phrases are discarded
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
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

    def set_volume_pct(self, volume_pct: int) -> None:
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)

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
                self._wav_player.play_file(wav_path, volume_pct=self._volume_pct, channel="speech")
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
        volume_pct: int = 100,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._speech_key = str(speech_key or "").strip()
        self._speech_region = str(speech_region or "").strip()
        self._voice_name = str(voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
        self._output_dir = Path(output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)
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

    def set_volume_pct(self, volume_pct: int) -> None:
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)

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
                    self._wav_player.play_file(str(wav_path), volume_pct=self._volume_pct, channel="speech")
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
        volume_pct: int = 100,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._wav_player = wav_player
        self._voice_name = str(voice_name or "en-US-JennyNeural").strip() or "en-US-JennyNeural"
        self._output_dir = Path(output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)
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

    def set_volume_pct(self, volume_pct: int) -> None:
        self._volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)

    def _edge_volume_arg(self) -> str:
        delta = int(self._volume_pct) - 100
        return f"{delta:+d}%"

    def _worker_loop(self) -> None:
        if not self._enabled:
            return
        import asyncio
        import edge_tts

        loop = asyncio.new_event_loop()

        async def _synth(phrase: str, out_path: str) -> bool:
            try:
                communicator = edge_tts.Communicate(phrase, self._voice_name, volume=self._edge_volume_arg())
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
                    self._wav_player.play_file(wav_path, volume_pct=self._volume_pct, channel="speech")
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
        self._wake_command_window_s: float = 10.0
        self._command_window_until_s: float = 0.0
        self._partial_wake_ack_hold_s: float = 0.45
        self._suppress_wake_only_until_s: float = 0.0
        self._diag_last_audio_log_s: float = 0.0
        self._diag_last_quiet_log_s: float = 0.0
        self._diag_last_gain_log_s: float = 0.0
        self._diag_audio_log_interval_s: float = 3.0
        self._diag_quiet_log_interval_s: float = 8.0
        self._diag_audio_rms_min: int = 90
        self._diag_gain_log_interval_s: float = 12.0
        self._input_gain_target_rms: int = 1450
        self._input_gain_max: float = 6.5
        self._recent_signature: dict[str, object] = {}
        self._recent_spoken_phrase_suppressions: list[dict[str, object]] = []
        self._recent_output_input_block_until_s: float = 0.0
        self._voice_state: str = "IDLE"
        self._last_status_text: str = ""
        self._last_status_emit_s: float = 0.0
        self._status_emit_throttle_s: float = 0.18
        self._last_hearing_detected_s: float = 0.0
        self._hearing_status_release_s: float = 0.42
        self._listen_window_s: float = 2.4
        self._listen_window_until_s: float = 0.0
        self._listen_window_buffer: list[str] = []
        self._active_speech_started_s: float = 0.0
        self._min_final_words: int = 1
        self._min_final_duration_s: float = 0.2
        self._min_final_confidence: float = 0.45
        self._noise_rms_threshold: int = 95
        self._adaptive_noise_threshold: bool = True
        self._noise_baseline_samples: list[int] = []
        self._baseline_sample_count: int = 0
        self._dynamic_silence_threshold: float = 0.8
        self._last_partial_text: str = ""
        self._last_partial_updated_s: float = 0.0
        self._stale_partial_finalize_s: float = 1.15
        self._last_emitted_command_text: str = ""
        self._last_emitted_command_s: float = 0.0
        # Lock protecting the cross-thread suppression timestamps.
        # Written on the main thread (suppress_recent_output_text / clear_recent_output_suppression),
        # read on the audio-recognition thread (_flush_stale_partial_if_due,
        # _emit_partial_wake_ack, _recent_output_input_block_active, _normalize_command_text).
        self._wake_suppress_lock = threading.Lock()
        # Audio watchdog: timestamp (monotonic) of the last callback frame that carried
        # any audio content (rms > 0).  Written by _audio_callback on the sounddevice
        # callback thread; read by the recognition loop to detect a stalled device.
        # Python float writes are GIL-atomic, so no extra lock is needed here.
        self._last_audio_ts: float = time.monotonic()
        # Monotonic timestamp of the last chunk whose raw RMS was > 0, tracked in the
        # recognition loop.  Used to detect persistent zero-signal (e.g. hardware mute
        # or device reconnect) and force a stream restart before the stall watchdog would
        # normally fire.  Initialized to monotonic time so the grace window starts at boot.
        self._last_nonzero_audio_ts: float = time.monotonic()
        # Recognition-loop-side activity stamp: monotonic time of the last audio chunk
        # that was pulled from the queue AND passed the RMS gate in the recognition loop.
        # Initialized to 0.0 so the 10-second silence warning never fires at startup
        # before any audio has been processed.  GIL-atomic; no lock required.
        self._last_audio_activity_s: float = 0.0
        # Throttle timestamp for the 10-second "no audio activity" warning log.
        self._last_audio_warn_s: float = 0.0
        # Throttle timestamp for the queue-full debug warning in _audio_callback.
        self._last_queue_full_warn_s: float = 0.0
        self._queue_full_drop_count: int = 0
        self._last_input_status_log_s: float = 0.0
        self._input_overflow_count: int = 0
        self._input_overflow_window_s: float = 5.0
        # How many consecutive stream restart attempts have been made.  Reset to 0
        # whenever the stream delivers a healthy, above-gate audio frame.
        self._stream_restart_attempts: int = 0

    def _latest_signature(self) -> dict[str, object]:
        return dict(self._recent_signature)

    def _update_noise_baseline(self, rms: int) -> None:
        """Dynamically update noise baseline for better VAD sensitivity"""
        if not self._adaptive_noise_threshold:
            return
        
        self._noise_baseline_samples.append(rms)
        self._baseline_sample_count += 1
        
        # Keep only recent samples (last 10 seconds worth)
        if len(self._noise_baseline_samples) > 100:
            self._noise_baseline_samples.pop(0)
        
        # Update threshold every 50 samples
        if self._baseline_sample_count % 50 == 0 and len(self._noise_baseline_samples) > 10:
            avg_noise = sum(self._noise_baseline_samples) / len(self._noise_baseline_samples)
            # Set threshold to average + 20% margin
            self._noise_rms_threshold = max(80, int(avg_noise * 1.2))

    def _recognizer_gate_rms(self) -> int:
        threshold = max(55, int(getattr(self, "_noise_rms_threshold", 95) or 95))
        return max(48, min(threshold, int(threshold * 0.72)))

    def _should_process_recognizer_audio(self, rms: int) -> bool:
        try:
            level = max(0, int(rms or 0))
        except Exception:
            return False
        self._update_noise_baseline(level)
        return level >= self._recognizer_gate_rms()

    def _capture_chunk_signature(self, chunk: bytes, rms: int) -> None:
        # Use dynamic threshold for speech detection
        current_threshold = max(120, int(getattr(self, "_noise_rms_threshold", 95)))
        if not chunk or rms < current_threshold:
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

    def _emit_status(
        self,
        status: str,
        *,
        source: str = "stt",
        now: Optional[float] = None,
        force: bool = False,
    ) -> None:
        cleaned = re.sub(r"\s+", " ", str(status or "").strip().lower())
        if not cleaned:
            return
        current_time = float(now if now is not None else time.time())
        last_status = str(getattr(self, "_last_status_text", "") or "").strip().lower()
        last_emit_s = float(getattr(self, "_last_status_emit_s", 0.0) or 0.0)
        throttle_s = float(getattr(self, "_status_emit_throttle_s", 0.18) or 0.18)
        if not force and cleaned == last_status and (current_time - last_emit_s) < throttle_s:
            return
        self._last_status_text = cleaned
        self._last_status_emit_s = current_time
        self._emit_transcript("status", cleaned, source=source)

    def _note_live_hearing_activity(self, *, now: Optional[float] = None, source: str = "stt") -> None:
        current_time = float(now if now is not None else time.time())
        self._last_hearing_detected_s = current_time
        self._emit_status("hearing", source=source, now=current_time)

    def _publish_partial_transcript(self, partial_text: str, *, source: str) -> None:
        cleaned = str(partial_text or "").strip().lower()
        if not cleaned:
            return
        partial_time = time.time()
        if float(getattr(self, "_active_speech_started_s", 0.0) or 0.0) <= 0.0:
            self._active_speech_started_s = partial_time
        if self._recent_output_input_block_active(now=partial_time):
            self._on_log(f"[VOICE-DIAG] self-echo-partial-window-suppressed text='{cleaned}'")
            return
        if self._matches_recent_output_echo(cleaned, partial=True):
            self._on_log(f"[VOICE-DIAG] self-echo-partial-suppressed text='{cleaned}'")
            return
        self._last_partial_text = cleaned
        self._last_partial_updated_s = partial_time
        self._note_live_hearing_activity(now=partial_time, source=source)
        self._emit_transcript("partial", cleaned, source=source)
        if self._partial_contains_wake(cleaned):
            self._emit_partial_wake_ack(cleaned)

    def _release_live_hearing_status_if_due(self, *, now: Optional[float] = None, source: str = "stt") -> None:
        current_time = float(now if now is not None else time.time())
        last_hearing_s = float(getattr(self, "_last_hearing_detected_s", 0.0) or 0.0)
        if last_hearing_s <= 0.0:
            return
        if (current_time - last_hearing_s) < float(getattr(self, "_hearing_status_release_s", 0.42) or 0.42):
            return
        current_status = str(getattr(self, "_last_status_text", "") or "").strip().lower()
        if current_status != "hearing":
            return
        state = str(getattr(self, "_voice_state", "IDLE") or "IDLE").strip().upper() or "IDLE"
        fallback = "processing" if state == "PROCESSING" else ("idle" if state == "IDLE" else "listening")
        self._emit_status(fallback, source=source, now=current_time, force=True)

    def _set_voice_state(self, state: str, *, reason: str = "") -> None:
        next_state = str(state or "IDLE").strip().upper() or "IDLE"
        current = str(getattr(self, "_voice_state", "IDLE") or "IDLE").strip().upper() or "IDLE"
        if next_state == current:
            return
        self._voice_state = next_state
        if next_state == "IDLE":
            self._active_speech_started_s = 0.0
            self._listen_window_until_s = 0.0
            self._listen_window_buffer = []
            self._clear_pending_partial_text()
        reason_text = f" reason='{reason}'" if reason else ""
        self._on_log(f"[VOICE-DIAG] state-transition {current} -> {next_state}{reason_text}")
        self._emit_status(next_state.lower(), source="state", force=True)

    def _begin_listening_window(self, *, now: Optional[float] = None, reason: str = "") -> None:
        current_time = float(now if now is not None else time.time())
        self._listen_window_buffer = []
        self._active_speech_started_s = current_time
        self._listen_window_until_s = current_time + float(getattr(self, "_listen_window_s", 5.0) or 5.0)
        self._open_wake_command_window(now=current_time)
        self._set_voice_state("LISTENING", reason=reason or "wake")

    def _append_listening_text(self, text: str) -> None:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip())
        if cleaned:
            self._listen_window_buffer.append(cleaned)

    def _clear_pending_partial_text(self) -> None:
        self._last_partial_text = ""
        self._last_partial_updated_s = 0.0

    def _finalize_listening_window_text(self) -> str:
        merged = re.sub(r"\s+", " ", " ".join(self._listen_window_buffer)).strip()
        self._listen_window_buffer = []
        return merged

    def _abort_listening_window(self, *, reason: str) -> None:
        self._listen_window_buffer = []
        self._listen_window_until_s = 0.0
        self._set_voice_state("IDLE", reason=reason)

    def _record_emitted_command(self, text: str, *, now: Optional[float] = None) -> None:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        if not normalized:
            return
        self._last_emitted_command_text = normalized
        self._last_emitted_command_s = float(now if now is not None else time.time())

    def _is_recent_duplicate_command(self, text: str, *, now: Optional[float] = None, window_s: float = 2.0) -> bool:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        if not normalized:
            return False
        last_text = re.sub(r"\s+", " ", str(getattr(self, "_last_emitted_command_text", "") or "").strip().lower())
        if not last_text or normalized != last_text:
            return False
        current_time = float(now if now is not None else time.time())
        last_time = float(getattr(self, "_last_emitted_command_s", 0.0) or 0.0)
        return last_time > 0.0 and (current_time - last_time) <= float(max(0.1, window_s))

    def _passes_final_transcript_gate(self, text: str, *, confidence: Optional[float] = None, now: Optional[float] = None) -> bool:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip())
        if not cleaned:
            return False
        words = [token for token in cleaned.split() if token]
        word_ok = len(words) >= int(getattr(self, "_min_final_words", 2) or 2)
        current_time = float(now if now is not None else time.time())
        started_s = float(getattr(self, "_active_speech_started_s", 0.0) or 0.0)
        duration_ok = started_s > 0.0 and (current_time - started_s) >= float(getattr(self, "_min_final_duration_s", 1.2) or 1.2)
        confidence_ok = True
        if confidence is not None:
            try:
                c = float(confidence)
                min_conf = float(getattr(self, "_min_final_confidence", 0.45) or 0.45)
                # Inside an active command window the operator has already confirmed
                # attention via wake word.  Relax the floor so that a follow-up
                # utterance with high background noise can still pass to command
                # matching.  Short noise bursts are still gated by duration_ok
                # because they won't reach the 1.2 s sustained-speech threshold.
                in_window = current_time <= float(getattr(self, "_command_window_until_s", 0.0) or 0.0)
                if in_window:
                    if duration_ok:
                        min_conf = min(min_conf, 0.12)
                    else:
                        min_conf = min(min_conf, 0.20)
                confidence_ok = c >= min_conf
            except Exception:
                confidence_ok = True
        return (word_ok or duration_ok) and confidence_ok

    def _is_allowed_command_or_intent(self, text: str) -> bool:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        if not normalized:
            return False
        known_fragments = set(self._command_grammar_fragments())  # Ensure we have the command grammar fragments
        if normalized in known_fragments:
            return True
        if self._fuzzy_command_fragment_match(normalized):
            return True
        intent_patterns = (
            r"\b(?:connect|disconnect|enable|disable|resume|pause|start|stop|open|close|run|set|change|switch|load|use|increase|decrease|go)\b",
            r"\b(?:who are you|what do you do|what can you do|identify yourself|tell me a joke|make a joke|personality)\b",
            r"\b(?:introduce yourself|describe yourself|tell me about yourself)\b",
            r"\b(?:tell|say)(?: me| us)? who you are\b",
            r"\b(?:can|could|would) you (?:tell|say)(?: me| us)? who you are\b",
            r"\b(?:what(?:s| is) your name|what(?:s| is) your purpose|who (?:created|made) you)\b",
            r"\b(?:can you introduce yourself|what all can you do|what all can you do for us|what can we ask you|what should we say|give us some ideas)\b",
            r"\b(?:what games can we play|do you remember (?:me|us)|do you still remember (?:me|us)|who did you just meet|(?:we are|we're) back)\b",
            r"\b(?:how can i|how do i)\b.*\b(?:aim|aiming|precision|accuracy|jitter|overshoot|drift|playful|fun)\b",
            r"\b(?:give us|give me|start|launch|another|different|next|one more)\b.*\b(?:mission|challenge|game|round)\b",
            r"\b(?:stealth|sneak|ninja|spy|freeze(?: dance)?|statue|countdown|race|timer|ready set go)\b.*\b(?:mission|challenge|game|round)\b",
            r"\b(?:my|the)\s+(?:kids|children|family)\b.*\b(?:meet|meet you|introduce yourself|say hi|say hello|greet)\b",
            r"\b(?:tell|say)(?: me| us)? something funny\b",
            r"\b(?:can|could|would) you (?:tell|say)(?: me| us)? something funny\b",
            r"\b(?:hello|hi|hey)(?: there)?(?: elion)?\b",
            r"\bhow are you(?: doing(?: today)?)?(?: elion)?\b",
            r"^(?:british|american|russian|indian|spanish|french|italian|japanese|hindi|mandarin|chinese|australian|filipino)(?:\s+(?:male|female))?$",
            r"^(?:male|female)$",
            r"^(?:another|another one|one more|try another(?: one)?|different one|next (?:voice|one)|voice options|what are the options|what options|list voices|list the voices)$",
            r"\b(?:what voice are you using|what is your current voice|current voice|what voices do you have)\b",
            r"\b(?:test voice|scan voices|scan all voices|save settings|save configuration|export snapshot|export conversation|open(?: the)? (?:export |snapshot )?folder)\b",
            r"\b(?:open|show)\s+(?:the\s+)?(?:document|docs) browser\b",
            r"\bbrowse (?:the )?documents\b",
            r"\bopen documentation\b",
            r"\b(?:face status|face recognition status|known face status|face library status)\b",
            r"\b(?:list face profiles|list known faces|what faces do you know|who do you know|how many face profiles|how many known faces)\b",
            r"\b(?:detect faces|scan faces|find faces|detect faces in preview|scan faces in preview)\b",
            r"\b(?:load|open|show|use)\b\s+(?:the\s+)?(?:latest|newest)\s+(?:face\s+import|face\s+photo|import\s+photo)(?:\s+(?:in|into)\s+preview)?\b",
            r"\b(?:load|open|show|use)\b\s+(?:the\s+)?(?:preview\s+)?(?:face\s+import\s+inbox|import\s+inbox)(?:\s+photo)?\b",
            r"\b(?:save detected faces|save face candidates|save detected face profiles)\b",
            r"\b(?:test face recognition|run face test|who is in view|who is on camera|recognize faces)\b",
            r"\b(?:what can you see|what do you see|what are you seeing)\b.*\b(?:camera|view|frame|scene)\b",
            r"\b(?:what objects|what classes)\b.*\b(?:see|seeing|detect|detected)\b.*\b(?:camera|view|frame|scene)\b",
            r"\b(?:tell me|describe)\b.*\b(?:what you see|current camera view|camera view|current scene|scene on camera)\b",
            r"\bdescribe to me what you currently see\b",
            r"\btell me what is on camera\b",
            r"\bwhat is in front of you\b",
            r"\bimport\b\s+(?:(?:target|friendly|non[- ]target)\s+)?face(?:\s+photos?|\s+images?)(?:\s+batch)?\s+(?:for|as)\b",
            r"\b(?:register|save|add)\b\s+(?:(?:current|live|known)\s+)?(?:(?:target|friendly|non[- ]target)\s+)?face(?:\s+profile)?\b",
            r"\b(?:remove|delete)\b\s+(?:known\s+)?face(?:\s+profile)?\b",
            r"\b(?:update|refresh)\b\s+(?:known\s+)?face(?:\s+profile)?\b",
            r"\b(?:rename|change)\b\s+(?:known\s+)?face(?:\s+profile)?\b.*\b(?:to|as)\b",
            r"\b(?:mark|set|make)\b\s+(?:known\s+)?face(?:\s+profile)?\b.*\b(?:target|friendly|non[- ]target)\b",
            r"\b(?:current profile|active profile|what profile is active|which profile is active|what preset is active)\b",
            r"\b(?:list profiles|profile list|profile options|what profiles do you have|which profiles do you have|available profiles)\b",
            r"\b(?:current|active|what .* active|which .* active|list|available|what .* do you have|which .* do you have|load|use|apply|switch|set|change)\b.*\b(?:detection(?: mode)?|target filter|filter|threat(?: ai| scoring)?|engagement|engage|servo(?: move time)?|move time|bus servo)\b.*\bpreset(?:s)?\b",
            r"\b(?:status report|system report|check status|run diagnostics|analy(?:ze|sis)|diagnos(?:e|is))\b",
        )
        return any(re.search(pattern, normalized) for pattern in intent_patterns)

    def _flush_listening_window_if_due(self, *, now: Optional[float] = None) -> None:
        current_time = float(now if now is not None else time.time())
        state = str(getattr(self, "_voice_state", "IDLE") or "IDLE").strip().upper()
        window_until = float(getattr(self, "_listen_window_until_s", 0.0) or 0.0)
        if state != "LISTENING" or window_until <= 0.0 or current_time < window_until:
            return
        combined = self._finalize_listening_window_text()
        self._listen_window_until_s = 0.0
        self._set_voice_state("PROCESSING", reason="listen-window-timeout")
        if not combined:
            self._set_voice_state("IDLE", reason="listen-window-empty")
            return
        if not self._passes_final_transcript_gate(combined, now=current_time):
            self._on_log(f"[VOICE-DIAG] listening-window-final-rejected text='{combined}'")
            self._set_voice_state("IDLE", reason="listen-window-gate-reject")
            return
        if not self._is_allowed_command_or_intent(combined):
            self._on_log(f"[VOICE-DIAG] listening-window-unknown-command text='{combined}'")
            self._set_voice_state("IDLE", reason="listen-window-unknown-command")
            return
        try:
            self._on_log(f"[VOICE-DIAG] command-emitted-window='{combined}'")
            self._record_emitted_command(combined, now=current_time)
            self._on_command(combined)
        finally:
            self._set_voice_state("IDLE", reason="listen-window-complete")

    def _flush_stale_partial_if_due(self, *, now: Optional[float] = None) -> None:
        current_time = float(now if now is not None else time.time())
        partial_text = re.sub(r"\s+", " ", str(getattr(self, "_last_partial_text", "") or "").strip())
        updated_s = float(getattr(self, "_last_partial_updated_s", 0.0) or 0.0)
        if not partial_text or updated_s <= 0.0:
            return
        if (current_time - updated_s) < float(getattr(self, "_stale_partial_finalize_s", 1.15) or 1.15):
            return

        self._clear_pending_partial_text()
        wake_candidate = self._partial_contains_wake(partial_text)
        command_window_open = current_time <= float(getattr(self, "_command_window_until_s", 0.0) or 0.0)
        state = str(getattr(self, "_voice_state", "IDLE") or "IDLE").strip().upper()
        if self._wake_word and not (wake_candidate or command_window_open or state == "LISTENING"):
            return

        normalized = self._normalize_command_text(partial_text)
        if not normalized and wake_candidate and self._wake_word:
            with self._wake_suppress_lock:
                suppress_until = float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0)
            if current_time > suppress_until:
                normalized = str(self._wake_word or "").strip().lower()
                if normalized:
                    self._on_log(
                        f"[VOICE-DIAG] stale-partial-wake-dispatched text='{partial_text}' wake='{normalized}'"
                    )
                    self._emit_transcript("final", normalized, source="partial-timeout")
        if not normalized:
            return
        if self._wake_word and normalized == str(self._wake_word or "").strip().lower():
            with self._wake_suppress_lock:
                suppress_until = float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0)
            if current_time <= suppress_until:
                self._on_log(
                    f"[VOICE-DIAG] stale-partial-wake-suppressed text='{partial_text}' suppress_until={suppress_until:.2f}"
                )
                return
        if self._is_recent_duplicate_command(normalized, now=current_time):
            self._on_log(f"[VOICE-DIAG] stale-partial-command-deduped='{normalized}'")
            return
        if self._command_cooldown_s > 0.0 and (current_time - self._last_emit_s) < self._command_cooldown_s:
            self._on_log("[VOICE-DIAG] stale-partial-command-throttled-by-cooldown")
            return
        self._last_emit_s = current_time
        self._on_log(f"[VOICE-DIAG] stale-partial-command-emitted='{normalized}'")
        self._record_emitted_command(normalized, now=current_time)
        self._on_command(normalized)

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
            with self._wake_suppress_lock:
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
        with self._wake_suppress_lock:
            self._recent_output_input_block_until_s = 0.0
            self._suppress_wake_only_until_s = 0.0

    def _recent_output_input_block_active(self, *, now: Optional[float] = None) -> bool:
        current_time = float(now if now is not None else time.time())
        with self._wake_suppress_lock:
            block_until = float(getattr(self, "_recent_output_input_block_until_s", 0.0) or 0.0)
        return current_time <= block_until

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

        def _matches_spoken_window(spoken_tokens: list[str], *, min_ratio: float) -> bool:
            token_count = len(sanitized_tokens)
            if token_count < 2 or len(spoken_tokens) < token_count:
                return False
            for start_index in range(len(spoken_tokens) - token_count + 1):
                window = " ".join(spoken_tokens[start_index : start_index + token_count])
                if not window:
                    continue
                if sanitized == window:
                    return True
                if SequenceMatcher(None, sanitized, window).ratio() >= min_ratio:
                    return True
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
                if sanitized in spoken:
                    return True
                if _matches_spoken_window(spoken_tokens, min_ratio=0.88):
                    return True
                continue
            ratio = SequenceMatcher(None, sanitized, spoken).ratio()
            token_overlap = len(set(sanitized_tokens) & set(spoken_tokens))
            if sanitized == spoken:
                return True
            if sanitized in spoken and len(sanitized_tokens) >= 2:
                return True
            if _matches_spoken_window(spoken_tokens, min_ratio=0.84):
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
            "introduce yourself",
            "describe yourself",
            "tell me about yourself",
            "can you tell us who you are",
            "tell us who you are",
            "what is your name",
            "what is your purpose",
            "who created you",
            "who made you",
            "can you introduce yourself",
            "what all can you do",
            "what all can you do for us",
            "what can we ask you",
            "what games can we play",
            "what should we say",
            "do you remember us",
            "do you still remember me",
            "who did you just meet",
            "we are back",
            "how can i improve the aiming precision",
            "how can i make it more playful",
            "could you make it more fun for the kids",
            "give us a splash mission",
            "give us another challenge",
            "give us one more game",
            "give us a stealth mission",
            "give us a freeze dance challenge",
            "give us a countdown race",
            "start a splash challenge",
            "my kids are here and they want to meet you can you introduce yourself",
            "tell me a joke",
            "tell a joke",
            "make a joke",
            "could you say something funny please",
            "hello there elion",
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
            "restart smart sentry",
            "restart the smart sentry",
            "restart app",
            "restart the app",
            "elion restart the smart sentry app",
            "elion restart smart sentry app",
            "relaunch smart sentry",
            "relaunch the smart sentry",
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
            "change your voice",
            "change your voice to",
            "set voice to",
            "switch voice to",
            "use voice",
            "change your voice to russian dmitry",
            "set voice to russian dmitry",
            "use russian dmitry voice",
            "what voice are you using",
            "what is your current voice",
            "current voice",
            "voice options",
            "list voices",
            "what voices do you have",
            "test voice",
            "scan voices",
            "scan all voices",
            "save settings",
            "save configuration",
            "export snapshot",
            "export conversation",
            "open folder",
            "open export folder",
            "open snapshot folder",
            "open document browser",
            "open docs browser",
            "show document browser",
            "browse documents",
            "face status",
            "face recognition status",
            "known face status",
            "face library status",
            "list face profiles",
            "list known faces",
            "what faces do you know",
            "who do you know",
            "how many face profiles",
            "how many known faces",
            "detect faces",
            "scan faces",
            "find faces",
            "detect faces in preview",
            "scan faces in preview",
            "load latest face import",
            "load latest face import into preview",
            "load latest face photo",
            "open latest face import",
            "open face import inbox",
            "save detected faces",
            "save face candidates",
            "save detected face profiles",
            "test face recognition",
            "run face test",
            "who is in view",
            "who is on camera",
            "recognize faces",
            "what can you see in the current camera view",
            "what objects can you see in the current camera view",
            "what classes can you see in the current camera view",
            "what do you see on camera",
            "describe what you see in the camera view",
            "describe to me what you currently see",
            "tell me what is on camera",
            "import face photos",
            "import target face photos",
            "import friendly face photos",
            "register face",
            "save current face",
            "add known face",
            "register target face",
            "remove face",
            "delete face",
            "remove known face",
            "delete face profile",
            "update face",
            "refresh face",
            "rename face",
            "change face profile",
            "mark face as target",
            "mark face as friendly",
            "set face to target",
            "set face to friendly",
            "make face a target",
            "make face friendly",
            "close the app",
            "close app",
            "quit the app",
            "quit app",
            "exit the app",
            "exit app",
            "open ai tab",
            "open ai assistant tab",
            "open connection tab",
            "open guard tab",
            "open tab",
            "load profile",
            "switch profile",
            "current profile",
            "active profile",
            "what profile is active",
            "which profile is active",
            "what preset is active",
            "list profiles",
            "profile list",
            "profile options",
            "what profiles do you have",
            "which profiles do you have",
            "available profiles",
            "current detection preset",
            "list detection presets",
            "load detection preset",
            "current filter preset",
            "list filter presets",
            "load filter preset",
            "current threat preset",
            "list threat presets",
            "load threat preset",
            "current engagement preset",
            "list engagement presets",
            "load engagement preset",
            "current servo preset",
            "list servo presets",
            "load servo preset",
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

    def _use_constrained_vosk_phrase_grammar(self) -> bool:
        raw = str(os.getenv("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR", "") or "").strip().lower()
        if raw in {"1", "true", "yes", "on"}:
            return True
        if raw in {"0", "false", "no", "off"}:
            return False
        configured_input = str(getattr(self, "_device_name", "") or "").strip()
        # On Windows, a pinned headset mic is usually being used for explicit voice control.
        # Defaulting that path back to command grammar keeps wake-word/command detection
        # stable on this hardware instead of drifting into open-dictation hallucinations.
        if os.name == "nt" and configured_input:
            return True
        return False

    def _windows_speech_grammar_phrases(self) -> list[str]:
        wake_aliases = self._wake_word_aliases(self._wake_word)
        command_fragments = self._command_grammar_fragments()
        # Build the same "alias + fragment" cross-product as _recognizer_grammar_phrases so
        # that Windows SR's phrase grammar can match whole utterances like
        # "Elion run the smart sentry" at high confidence instead of falling back to
        # DictationGrammar which produces garbage confidence for combined phrases.
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
        ]
        return list(dict.fromkeys(str(item).strip().lower() for item in phrases if str(item).strip()))

    def _use_windows_dictation_grammar(self) -> bool:
        raw = str(os.getenv("SMART_SENTRY_WINDOWS_STT_DICTATION", "") or "").strip().lower()
        if raw in {"1", "true", "yes", "on"}:
            return True
        if raw in {"0", "false", "no", "off"}:
            return False
        # Default to phrase grammar only on Windows. DictationGrammar can degrade
        # wake+command accuracy in noisy environments.
        return False

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

        # Do not force the operator to shout before AGC engages. Keep an ultra-low
        # floor so near-silence stays untouched, but allow genuinely quiet speech
        # to be amplified into the recognizer's useful range.
        if raw_rms < 8 or raw_peak < 16 or raw_rms >= self._input_gain_target_rms:
            return chunk, raw_rms, raw_peak, 1.0

        target_gain = max(1.0, float(self._input_gain_target_rms) / max(1.0, float(raw_rms)))
        peak_headroom_gain = max(1.0, 30000.0 / max(1.0, float(raw_peak)))
        gain = min(float(self._input_gain_max), target_gain, peak_headroom_gain)
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
        corrected = self._apply_phrase_alias_corrections(sanitized)
        aliases = self._partial_wake_word_aliases(self._wake_word)
        for candidate in tuple(dict.fromkeys(item for item in (corrected, sanitized) if item)):
            cue_like_candidates = tuple(
                dict.fromkeys(
                    item
                    for item in (
                        candidate,
                        self._strip_leading_conversational_fillers(candidate),
                    )
                    if item
                )
            )
            for cue_like_candidate in cue_like_candidates:
                for alias in aliases:
                    if cue_like_candidate == alias or cue_like_candidate.startswith(f"{alias} "):
                        return True
                cue_token_count = len([tok for tok in re.findall(r"[a-z0-9]+", cue_like_candidate) if tok])
                if 0 < cue_token_count <= 3:
                    for alias in aliases:
                        if SequenceMatcher(None, cue_like_candidate, alias).ratio() >= 0.80:
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

    @staticmethod
    def _repair_domain_token_confusions(text: str) -> str:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        if not normalized:
            return ""

        explicit_aliases = {
            "smarts": "smart",
            "smard": "smart",
            "smert": "smart",
            "smahrt": "smart",
            "centry": "sentry",
            "sentri": "sentry",
            "sentra": "sentry",
            "sentree": "sentry",
            "sentery": "sentry",
            "sentrys": "sentry",
            "conect": "connect",
            "connekt": "connect",
            "cannect": "connect",
            "konnect": "connect",
            "disconect": "disconnect",
            "disconnekt": "disconnect",
            "discconect": "disconnect",
            "inable": "enable",
            "anable": "enable",
            "enabel": "enable",
            "desable": "disable",
            "dissable": "disable",
            "disabel": "disable",
            "bords": "boards",
            "boreds": "boards",
            "boardz": "boards",
            "boareds": "boards",
            "camra": "camera",
            "kamra": "camera",
            "canera": "camera",
            "camerah": "camera",
            "gaurd": "guard",
            "gaurding": "guarding",
            "garding": "guarding",
            "guardin": "guarding",
            "traking": "tracking",
            "trakking": "tracking",
            "trackin": "tracking",
            "rekognition": "recognition",
            "recognision": "recognition",
            "recognizion": "recognition",
            "recognitian": "recognition",
            "recognizition": "recognition",
            "prophile": "profile",
            "profyle": "profile",
            "voyce": "voice",
            "vois": "voice",
            "boice": "voice",
            "seriel": "serial",
            "searial": "serial",
            "brighness": "brightness",
            "brightnes": "brightness",
            "confidance": "confidence",
            "confidense": "confidence",
            "confidents": "confidence",
            "diganostics": "diagnostics",
            "diagnotics": "diagnostics",
            "diognostics": "diagnostics",
            "diagnosticz": "diagnostics",
            "statis": "status",
            "stetus": "status",
        }
        fuzzy_domain_tokens = (
            "smart",
            "sentry",
            "connect",
            "disconnect",
            "board",
            "boards",
            "camera",
            "tracking",
            "guard",
            "guarding",
            "mode",
            "enable",
            "disable",
            "face",
            "recognition",
            "voice",
            "human",
            "assistant",
            "shortcuts",
            "profile",
            "brightness",
            "confidence",
            "status",
            "diagnostics",
            "current",
            "export",
            "snapshot",
            "conversation",
            "folder",
            "serial",
            "com",
            "port",
            "ports",
            "home",
            "rest",
            "resume",
            "start",
            "stop",
            "open",
            "close",
            "theme",
        )

        repaired_parts: list[str] = []
        for part in re.findall(r"[a-z0-9]+|[^a-z0-9]+", normalized):
            if not re.fullmatch(r"[a-z0-9]+", part):
                repaired_parts.append(part)
                continue
            canonical = explicit_aliases.get(part)
            if canonical is None and part not in fuzzy_domain_tokens and len(part) >= 4:
                best_match = ""
                best_ratio = 0.0
                for candidate in fuzzy_domain_tokens:
                    if candidate == part or abs(len(candidate) - len(part)) > 2:
                        continue
                    ratio = SequenceMatcher(None, part, candidate).ratio()
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_match = candidate
                if best_ratio >= 0.86:
                    canonical = best_match
            repaired_parts.append(canonical or part)

        repaired = "".join(repaired_parts)
        repaired = re.sub(r"\bdis\s+connect\b", "disconnect", repaired)
        repaired = re.sub(r"\bdis\s+able\b", "disable", repaired)
        repaired = re.sub(r"\bin\s+able\b", "enable", repaired)
        repaired = re.sub(r"\bcon\s+nect\b", "connect", repaired)
        repaired = re.sub(r"\s+", " ", repaired).strip()
        return repaired

    def _apply_phrase_alias_corrections(self, sanitized: str) -> str:
        corrected = str(sanitized or "").strip().lower()
        if not corrected:
            return ""
        corrected = self._repair_domain_token_confusions(corrected)
        replacements = (
            (r"\be lion\b", "elion"),
            (r"\ba lion\b", "elion"),
            (r"\bon lion\b", "elion"),
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
            (r"\bsmart sent tree\b", "smart sentry"),
            (r"\bsmart sent three\b", "smart sentry"),
            (r"\bsmart entry\b", "smart sentry"),
            (r"\bsmarts? entry\b", "smart sentry"),
            (r"\bsmarts?\s+and\s+(?:tree|three|drink)\b", "smart sentry"),
            (r"\bsmart\s+sentry\s+to\s+(?:rob|run)\b", "run smart sentry"),
            (r"\brun\s+(?:the\s+)?smarts?\s+and\b", "run smart sentry"),
            (r"\brun\s+(?:the\s+)?smart\s+sent\s+(?:tree|three)\b", "run smart sentry"),
            (r"\brun\s+(?:the\s+)?smarts?\s+and\s+(?:tree|three|drink)\b", "run smart sentry"),
            (r"\bgo to the home\b", "go home"),
            (r"\bgo to home\b", "go home"),
            (r"\bgo to the rest\b", "go rest"),
            (r"\bgo to rest\b", "go rest"),
            (r"\brestaart\b", "restart"),
            (r"\bcome ports?\b", "com ports"),
            (r"\bcalm ports?\b", "com ports"),
            (r"\bcome port\b", "com port"),
            (r"\bcalm port\b", "com port"),
            (r"\bc o m\b", "com"),
            (r"\bguard mode\b", "guarding mode"),
            (r"\bguarding mold\b", "guarding mode"),
            (r"\bauto tracking\b", "autotracking"),
            (r"\bvoice styles?\b", "voice style"),
            (r"\bvoicwe\b", "voice"),
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
            (r"\bwho are u\b", "who are you"),
            (r"\bwho r you\b", "who are you"),
            (r"\bcancel that(?:\s+[a-z]+)?$", "cancel that"),
            (r"\byou do it\b", "do it"),
        )
        for pattern, replacement in replacements:
            corrected = re.sub(pattern, replacement, corrected)
        corrected = self._repair_domain_token_confusions(corrected)
        corrected = re.sub(r"\s+", " ", corrected).strip()
        return corrected

    @staticmethod
    def _strip_leading_conversational_fillers(text: str) -> str:
        cleaned = re.sub(r"\s+", " ", str(text or "").strip().lower())
        if not cleaned:
            return ""
        filler_prefix = (
            r"^(?:(?:hey|hi|hello|yo|please|ok(?:ay)?|well|so|um|uh|ah|oh|hmm|huh|there|just)\s+)+"
        )
        previous = None
        while cleaned and cleaned != previous:
            previous = cleaned
            cleaned = re.sub(filler_prefix, "", cleaned).strip()
        return cleaned

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
            (r"\bactivate\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bconnect\b.*\b(app|boards?|smart\s+sentry)\b.*\b(com|port|ports|serial)\b.*\benable\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bconnect\b.*\benable\b.*\bsmart\s+sentry\b", "connect boards and enable smart sentry"),
            (r"\bcancel\b.*\ball\b.*\b(queue|queued|tasks?)\b", "cancel all tasks in queue"),
            (r"\bclear\b.*\bqueue\b", "cancel all tasks in queue"),
            (r"\bcancel\b.*\b(last|latest)\b", "cancel the last"),
            (r"\bconnect\b.*\bapp\b.*\bcom\b.*\bports?\b", "connect the app to com ports"),
            (r"\bdisconnect\b.*\b(app|link|controller|board|boards|smart\s+sentry|com|port|ports|serial)\b", "disconnect smart sentry boards"),
            (r"\benable\b.*\bsmart\s+sentry\b", "enable smart sentry"),
            (r"\bdisable\b.*\bsmart\s+sentry\b", "disable smart sentry"),
            (r"\bactivate\b.*\b(auto\s*tracking|autotracking|auto\s*tracker|autotracker|tracking)\b", "resume guarding mode"),
            (r"\bresume\b.*\b(auto\s*tracking|autotracking|guard(?:ing)?\s*mode|smart\s+sentry)\b", "resume guarding mode"),
            (r"\bconnect\b.*\bsmart\s+sentry\b.*\bboards?\b", "connect smart sentry boards"),
            (r"\bconnect\b.*\b(app|com|port|ports|serial)\b", "connect boards"),
            (r"\bconnect\b.*\bboards?\b", "connect boards"),
            (r"\bopen\b.*\b(camera|video)\b", "open camera"),
            (r"\bclose\b.*\b(camera|video)\b", "close camera"),
            (r"\b(?:close|quit|exit)\b.*\b(?:app|application|smart\s+sentry)\b", "close the app"),
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
            (r"\bopen\b.*\btab\b", "open tab"),
        )
        for pattern, canonical in canonical_rules:
            if re.search(pattern, corrected):
                return canonical
        recovered_core_intent = self._recover_core_intent_phrase(corrected)
        if recovered_core_intent:
            return recovered_core_intent
        wake_word = str(getattr(self, "_wake_word", "") or "").strip().lower()
        if wake_word:
            for alias in self._wake_word_aliases(wake_word):
                normalized_alias = re.sub(r"\s+", " ", str(alias or "").strip().lower())
                if normalized_alias and (corrected == normalized_alias or corrected.startswith(f"{normalized_alias} ")):
                    return corrected
        fuzzy_match = self._fuzzy_command_fragment_match(corrected)
        if fuzzy_match:
            return fuzzy_match
        return corrected

    def _recover_core_intent_phrase(self, text: str) -> str:
        normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
        tokens = [tok for tok in re.findall(r"[a-z0-9]+", normalized) if tok]
        if len(tokens) < 2:
            return ""

        ignored_tokens = {"a", "an", "the", "to", "for", "please", "now", "uh", "um", "ah", "oh"}
        signal_tokens = {tok for tok in tokens if tok not in ignored_tokens}
        compact_text = " ".join(tok for tok in tokens if tok not in ignored_tokens) or normalized

        core_candidates = (
            "who are you",
            "what do you do",
            "what can you do",
            "introduce yourself",
            "tell me a joke",
            "say something funny",
            "personality",
        )

        best_match = ""
        best_ratio = 0.0
        best_overlap = 0
        for candidate in core_candidates:
            candidate_text = re.sub(r"\s+", " ", str(candidate or "").strip().lower())
            candidate_tokens = [tok for tok in re.findall(r"[a-z0-9]+", candidate_text) if tok]
            if len(candidate_tokens) < 1:
                continue
            candidate_signal_tokens = {tok for tok in candidate_tokens if tok not in ignored_tokens}
            overlap = len(signal_tokens & candidate_signal_tokens)
            compact_candidate = " ".join(tok for tok in candidate_tokens if tok not in ignored_tokens) or candidate_text
            ratio = max(
                SequenceMatcher(None, normalized, candidate_text).ratio(),
                SequenceMatcher(None, compact_text, compact_candidate).ratio(),
            )
            if ratio > best_ratio or (abs(ratio - best_ratio) < 1e-9 and overlap > best_overlap):
                best_match = candidate_text
                best_ratio = ratio
                best_overlap = overlap

        if not best_match:
            return ""
        if best_ratio >= 0.63:
            return best_match
        if best_overlap >= 1 and best_ratio >= 0.58:
            return best_match
        return ""

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
        self._listen_window_until_s = max(float(getattr(self, "_listen_window_until_s", 0.0) or 0.0), time.time() + duration)
        self._set_voice_state("LISTENING", reason=reason or "external-open")
        if reason:
            self._on_log(
                f"[VOICE-DIAG] external-command-window-open reason='{reason}' "
                f"window_until={self._command_window_until_s:.2f}"
            )

    def _audio_callback(self, indata, _frames, _time_info, status) -> None:
        if status:
            status_text = str(status).strip()
            if status_text:
                now = time.monotonic()
                is_overflow = "overflow" in status_text.lower()
                if is_overflow:
                    self._input_overflow_count += 1
                    if (now - float(getattr(self, "_last_input_status_log_s", 0.0) or 0.0)) >= float(
                        getattr(self, "_input_overflow_window_s", 5.0) or 5.0
                    ):
                        count = int(getattr(self, "_input_overflow_count", 0) or 0)
                        self._last_input_status_log_s = now
                        self._input_overflow_count = 0
                        self._on_log(
                            f"[VOICE-DIAG] input-overflow count={count} over "
                            f"{float(getattr(self, '_input_overflow_window_s', 5.0) or 5.0):.1f}s"
                        )
                elif (now - float(getattr(self, "_last_input_status_log_s", 0.0) or 0.0)) >= 3.0:
                    self._last_input_status_log_s = now
                    self._on_log(f"Vosk input status: {status_text}")
        if self._stop.is_set():
            return
        chunk = self._coerce_stream_chunk(indata)
        boosted_chunk, rms, peak, gain = self._boost_audio_chunk(chunk)
        # Watchdog heartbeat: any frame with content means the device is alive.
        if rms > 0:
            self._last_audio_ts = time.monotonic()
        self._log_audio_chunk_diagnostics(chunk, rms, peak, gain, queue_depth=self._audio_queue.qsize())
        try:
            self._audio_queue.put_nowait(boosted_chunk)
        except queue.Full:
            # Recognition loop is behind — evict the oldest frame and retry.
            # Log a throttled debug warning so this is visible in diagnostics
            # without flooding the log under sustained overload.
            _qf_now = time.monotonic()
            self._queue_full_drop_count += 1
            if (_qf_now - float(getattr(self, "_last_queue_full_warn_s", 0.0) or 0.0)) > 5.0:
                dropped = int(getattr(self, "_queue_full_drop_count", 0) or 0)
                self._last_queue_full_warn_s = _qf_now
                self._on_log(
                    "[VOICE-DIAG] audio-queue-full — oldest frame dropped "
                    f"{max(1, dropped)} time(s) in last 5s; recognition loop may be falling behind"
                )
                self._queue_full_drop_count = 0
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
        with self._wake_suppress_lock:
            curr_suppress = float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0)
            if now <= curr_suppress:
                self._on_log(
                    f"[VOICE-DIAG] partial-wake-ack-suppressed suppress_until={curr_suppress:.2f}"
                )
                return
            new_suppress = max(
                curr_suppress,
                now + float(getattr(self, "_partial_wake_ack_hold_s", 1.75) or 1.75),
            )
            self._suppress_wake_only_until_s = new_suppress
        window_until = self._open_wake_command_window(now=now)
        self._on_log(
            f"[VOICE-DIAG] partial-wake-ack-emitted wake='{self._wake_word}' "
            f"window_until={window_until:.2f} "
            f"suppress_until={new_suppress:.2f}"
        )
        self._begin_listening_window(now=now, reason="partial-wake")

    def _normalize_command_text(self, text: str, *, confidence: Optional[float] = None) -> str:
        normalized = str(text or "").strip().lower()
        normalized = re.sub(r"\s+", " ", normalized)
        if not normalized:
            return ""
        sanitized = re.sub(r"[^a-z0-9 ]+", " ", normalized)
        sanitized = re.sub(r"\s+", " ", sanitized).strip()

        wake_word = re.sub(r"[^a-z0-9 ]+", " ", str(self._wake_word or "").strip().lower())
        wake_word = re.sub(r"\s+", " ", wake_word).strip()
        wake_aliases = self._wake_word_aliases(wake_word) if wake_word else []
        wake_pattern = r"\b(?:" + "|".join(re.escape(alias) for alias in wake_aliases) + r")\b" if wake_aliases else ""
        wake_barge_in_requested = False
        if wake_aliases:
            wake_barge_in_requested = bool(re.search(wake_pattern, sanitized))
            if not wake_barge_in_requested:
                wake_barge_in_requested = self._fuzzy_contains_wake(sanitized, wake_aliases)

        now = time.time()
        command_window_until = float(getattr(self, "_command_window_until_s", 0.0) or 0.0)
        listen_window_until = float(getattr(self, "_listen_window_until_s", 0.0) or 0.0)
        explicit_listen_window_active = now <= max(command_window_until, listen_window_until)
        if self._recent_output_input_block_active(now=now):
            if not (wake_barge_in_requested or explicit_listen_window_active):
                self._on_log(f"[VOICE-DIAG] self-echo-final-window-suppressed text='{sanitized}'")
                return ""
            if wake_barge_in_requested:
                self._on_log(f"[VOICE-DIAG] self-echo-final-window-barge-in-allowed text='{sanitized}'")
            else:
                self._on_log(f"[VOICE-DIAG] self-echo-final-window-listen-allowed text='{sanitized}'")
        if self._matches_recent_output_echo(sanitized, partial=False):
            if not wake_barge_in_requested:
                self._on_log(f"[VOICE-DIAG] self-echo-final-suppressed text='{sanitized}'")
                return ""
            self._on_log(f"[VOICE-DIAG] self-echo-final-barge-in-allowed text='{sanitized}'")
        corrected = self._canonicalize_command_text(sanitized)
        if not self._wake_word:
            final_text = corrected or sanitized or normalized
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            if not self._passes_final_transcript_gate(final_text, confidence=confidence, now=now):
                self._on_log(f"[VOICE-DIAG] final-transcript-gate-rejected text='{final_text}'")
                return ""
            if not self._is_allowed_command_or_intent(final_text):
                self._on_log(f"[VOICE-DIAG] final-transcript-unknown-command text='{final_text}'")
                return ""
            self._set_voice_state("PROCESSING", reason="final-no-wake")
            self._set_voice_state("IDLE", reason="final-no-wake-complete")
            return final_text
        if not wake_word:
            final_text = corrected or sanitized or normalized
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            return final_text
        strict_high_intent_patterns = (
            r"\bconnect\b.*\benable\b.*\bsmart\s+sentry\b",
            r"\bconnect\b.*\b(board|boards|com|port|serial)\b",
            r"\benable\b.*\bsmart\s+sentry\b",
            r"\b(?:run|start)\b.*\bsmart\s+sentry\b",
        )
        pattern = wake_pattern
        wake_matched = bool(re.search(pattern, corrected))
        if not wake_matched and wake_aliases:
            wake_matched = self._fuzzy_contains_wake(corrected, wake_aliases)
        if wake_matched:
            stripped = re.sub(pattern, " ", corrected).strip()
            stripped = re.sub(r"\s+", " ", stripped)
            stripped = self._strip_leading_conversational_fillers(stripped)
            stripped = self._canonicalize_command_text(stripped)
            stripped = self._strip_leading_conversational_fillers(stripped)
            self._begin_listening_window(now=now, reason="wake-final")
            if stripped and self._should_reject_low_signal_window_text(stripped, confidence=confidence):
                self._on_log(
                    f"[VOICE-DIAG] wake-followup-noise-rejected wake='{wake_word}' text='{stripped}'"
                )
                self._abort_listening_window(reason="wake-followup-noise-reject")
                with self._wake_suppress_lock:
                    _suppress_snap = float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0)
                if now <= _suppress_snap:
                    self._on_log(
                        f"[VOICE-DIAG] wake-word-final-suppressed text='{corrected}' "
                        f"suppress_until={_suppress_snap:.2f}"
                    )
                    return ""
                return ""
            final_text = f"{wake_word} {stripped}".strip() if stripped else wake_word
            self._on_log(
                f"[VOICE-DIAG] wake-word-match wake='{wake_word}' text='{corrected}' window_until={self._command_window_until_s:.2f}"
            )
            self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
            self._emit_transcript("final", final_text, source="final", confidence=confidence)
            if not stripped:
                with self._wake_suppress_lock:
                    _suppress_snap = float(getattr(self, "_suppress_wake_only_until_s", 0.0) or 0.0)
                if now <= _suppress_snap:
                    self._on_log(
                        f"[VOICE-DIAG] wake-word-final-suppressed text='{corrected}' "
                        f"suppress_until={_suppress_snap:.2f}"
                    )
                    self._on_log(
                        f"[VOICE-DIAG] wake-word-final-dropped-after-partial text='{corrected}'"
                    )
                    self._clear_pending_partial_text()
                    return ""
                self._on_log(f"[VOICE-DIAG] wake-word-final-dispatched text='{corrected}'")
                return wake_word
            self._append_listening_text(stripped)
            if not self._passes_final_transcript_gate(stripped, confidence=confidence, now=now):
                if any(re.search(expr, stripped) for expr in strict_high_intent_patterns):
                    self._on_log(
                        f"[VOICE-DIAG] wake-followup-gate-bypassed-high-intent text='{stripped}'"
                    )
                else:
                    self._on_log(f"[VOICE-DIAG] wake-followup-gate-rejected text='{stripped}'")
                    self._abort_listening_window(reason="wake-followup-gate-reject")
                    return ""
            if not self._is_allowed_command_or_intent(stripped):
                self._on_log(f"[VOICE-DIAG] wake-followup-unknown-command text='{stripped}'")
                self._abort_listening_window(reason="wake-followup-unknown-command")
                return ""
            self._set_voice_state("PROCESSING", reason="wake-followup-final")
            self._set_voice_state("IDLE", reason="wake-followup-complete")
            return stripped

        final_text = corrected or sanitized or normalized
        self._on_log(f"[VOICE-DIAG] transcript-final='{final_text}'")
        self._emit_transcript("final", final_text, source="final", confidence=confidence)

        if not self._passes_final_transcript_gate(final_text, confidence=confidence, now=now):
            if any(re.search(expr, final_text) for expr in strict_high_intent_patterns):
                self._on_log(
                    f"[VOICE-DIAG] final-transcript-gate-bypassed-high-intent text='{final_text}'"
                )
            else:
                self._on_log(f"[VOICE-DIAG] final-transcript-gate-rejected text='{final_text}'")
                return ""
        if not self._is_allowed_command_or_intent(final_text):
            self._on_log(f"[VOICE-DIAG] final-transcript-unknown-command text='{final_text}'")
            return ""

        # Fail-open for explicit high-intent command phrases so wake-word OCR drift
        # does not block critical operations like connect/enable.
        explicit_patterns = (
            r"\bwho\s+are\s+you\b",
            r"\bintroduce\s+yourself\b",
            r"\bwhat\s+do\s+you\s+do\b",
            r"\bwhat\s+can\s+you\s+do\b",
            r"\bwhat(?:'s|\s+is)\s+your\s+name\b",
            r"\btell\s+me\s+about\s+yourself\b",
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
            r"\b(?:run|start)\b.*\bsmart\s+sentry\b",
            r"\bstart\b.*\btracking\b",
            r"\bresume\b.*\b(auto\s*tracking|autotracking|guard(ing)?\s*mode)\b",
            r"\b(?:open|close)\b.*\b(camera|video)\b",
            r"\b(?:enable|disable)\b.*\b(face\s+recognition|human\s+voice|assistant\s+auto\s+speak|shortcuts?)\b",
            r"\bvoice\s+style\b",
            r"\b(?:load|switch(?:\s+to)?|use)\b.*\bprofile\b",
            r"\b(?:use|switch(?:\s+to)?|load)\b.*\b(nano|small|medium|large|xlarge|tiny|yolo|object\s+detection|best\s+mode)\b",
            r"\b(?:set|increase|decrease)\b.*\b(brightness|speed|confidence)\b",
            r"\b(?:change|set|switch(?:\s+to)?|use)\b.*\bvoice\b",
            r"\bopen\b.*\btab\b",
            r"\b(?:tell|make)\b.*\bjoke\b",
            r"\bpersonality\b",
            *(pattern for pattern, _canonical in iter_voice_toggle_command_patterns()),
        )
        if any(re.search(expr, final_text) for expr in explicit_patterns):
            self._command_window_until_s = max(
                float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
                now + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
            )
            self._on_log(
                f"[VOICE-DIAG] fail-open-command text='{final_text}' window_until={self._command_window_until_s:.2f}"
            )
            self._set_voice_state("PROCESSING", reason="fail-open-final")
            self._set_voice_state("IDLE", reason="fail-open-complete")
            return final_text

        if now <= float(getattr(self, "_command_window_until_s", 0.0) or 0.0):
            if self._should_reject_low_signal_window_text(final_text, confidence=confidence):
                self._on_log(f"[VOICE-DIAG] command-window-noise-rejected text='{final_text}'")
                return ""
            self._on_log(f"[VOICE-DIAG] command-window-accept text='{final_text}'")
            self._set_voice_state("PROCESSING", reason="window-final")
            self._set_voice_state("IDLE", reason="window-final-complete")
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
            try:
                if self._use_constrained_vosk_phrase_grammar():
                    grammar_phrases = self._recognizer_grammar_phrases()
                    recognizer = KaldiRecognizer(model, 16000, json.dumps(grammar_phrases))
                    self._on_log(
                        f"[VOICE-DIAG] recognizer-grammar-enabled phrases={len(grammar_phrases)} wake='{self._wake_word}'"
                    )
                else:
                    recognizer = KaldiRecognizer(model, 16000)
                    self._on_log(
                        f"[VOICE-DIAG] recognizer-dictation-enabled wake='{self._wake_word}'"
                    )
            except Exception as grammar_exc:
                self._on_log(f"[VOICE-DIAG] recognizer-grammar-fallback reason={grammar_exc}")
                recognizer = KaldiRecognizer(model, 16000)
        except Exception as exc:
            self._on_log(f"Failed to initialize Vosk recognizer: {exc}")
            return

        # Tunable I/O watchdog constants (not configurable at runtime; change here if needed).
        _QUEUE_TIMEOUT_S: float = 2.0   # how long to wait for each audio frame from the queue
        _STALL_TIMEOUT_S: float = 5.0   # seconds of silence from callback before declaring a stall
        _ZERO_SIGNAL_RESTART_S: float = 20.0  # persistent rms=0 seconds before forcing a stream restart
        _MAX_RESTART: int = 3           # max consecutive stream restart attempts before giving up

        self._stream_restart_attempts = 0

        while not self._stop.is_set():
            # Drain any stale frames left from a previous stream instance so the
            # recognizer does not get confused by out-of-order audio on restart.
            while not self._audio_queue.empty():
                try:
                    self._audio_queue.get_nowait()
                except queue.Empty:
                    break
            # Reset the watchdog clocks for the new stream attempt.
            self._last_audio_ts = time.monotonic()
            self._last_nonzero_audio_ts = time.monotonic()

            try:
                device_index = self._resolve_input_device(sd)
                # Callback-based InputStream: _audio_callback fires on the sounddevice
                # thread and enqueues boosted PCM chunks.  The recognition loop below
                # consumes from the queue with a bounded timeout so the thread can never
                # block indefinitely if the device stalls or is unplugged.
                with sd.InputStream(
                    samplerate=16000,
                    blocksize=4000,
                    dtype="float32",
                    channels=1,
                    device=device_index,
                    callback=self._audio_callback,
                ) as _stream:
                    self._emit_status("listening", source="vosk", force=True)
                    if device_index is not None:
                        self._on_log(f"Offline voice command listener started on device index {device_index}")
                    else:
                        self._on_log("Offline voice command listener started")

                    while not self._stop.is_set():
                        loop_now = time.time()
                        self._release_live_hearing_status_if_due(now=loop_now, source="vosk")
                        self._flush_stale_partial_if_due(now=loop_now)
                        self._flush_listening_window_if_due(now=loop_now)
                        if self._enable_wake_word_coordination and self._wake_word_detected_event.is_set():
                            self._wake_word_detected_event.clear()
                            self._command_window_until_s = max(
                                float(getattr(self, "_command_window_until_s", 0.0) or 0.0),
                                time.time() + float(getattr(self, "_wake_command_window_s", 10.0) or 10.0),
                            )

                        # ── Bounded queue read (replaces blocking stream.read) ──────────
                        try:
                            chunk = self._audio_queue.get(timeout=_QUEUE_TIMEOUT_S)
                        except queue.Empty:
                            # No frame arrived within the timeout window.
                            # --- 10-second soft activity warning ---
                            # Fires when the recognition loop has not processed any
                            # above-gate audio for 10 s.  Distinct from the harder
                            # stall-restart below: this fires even if the device
                            # callback is running (e.g. room is very quiet or the
                            # mic level is too low to clear the RMS gate).
                            _now_mono = time.monotonic()
                            if (
                                self._last_audio_activity_s > 0.0
                                and _now_mono - self._last_audio_activity_s > 10.0
                                and (_now_mono - self._last_audio_warn_s) > 10.0
                            ):
                                self._last_audio_warn_s = _now_mono
                                self._on_log(
                                    "Voice pipeline: no audio activity for 10s"
                                    " — check microphone/device selection."
                                )
                            # --- Stall / device-dead restart ---
                            # Escalate only when the callback has stopped firing entirely.
                            if _now_mono - self._last_audio_ts > _STALL_TIMEOUT_S:
                                self._stream_restart_attempts += 1
                                if self._stream_restart_attempts > _MAX_RESTART:
                                    self._on_log(
                                        "[VOICE] Audio stream stalled — max restart attempts reached, "
                                        "disabling voice input"
                                    )
                                    self._emit_transcript("status", "mic_error", source="watchdog")
                                    return
                                self._on_log(
                                    f"[VOICE] Audio stream stalled — attempting restart "
                                    f"({self._stream_restart_attempts}/{_MAX_RESTART})"
                                )
                                break  # exit inner loop; outer loop will reopen the stream
                            continue
                        # ── Audio processing (chunk is already AGC-boosted by callback) ─
                        if not chunk:
                            continue
                        try:
                            rms = int(audioop.rms(chunk, 2))
                        except Exception:
                            rms = 0
                        # ── Zero-signal watchdog ────────────────────────────────────────
                        # The stall watchdog (queue.Empty path above) only fires when the
                        # callback stops delivering frames entirely.  A device that streams
                        # all-zero PCM (hardware mute, device reconnect, driver reset) keeps
                        # the queue full and bypasses that check.  Detect persistent zero-
                        # signal here and force a stream restart so the device is re-opened
                        # on the new default (e.g. a freshly connected microphone).
                        _now_mono = time.monotonic()
                        if rms > 0:
                            self._last_nonzero_audio_ts = _now_mono
                        elif _now_mono - self._last_nonzero_audio_ts > _ZERO_SIGNAL_RESTART_S:
                            self._stream_restart_attempts += 1
                            if self._stream_restart_attempts > _MAX_RESTART:
                                self._on_log(
                                    "[VOICE] Persistent zero-signal — max restart attempts reached, "
                                    "disabling voice input"
                                )
                                self._emit_transcript("status", "mic_error", source="watchdog")
                                return
                            self._on_log(
                                f"[VOICE] Persistent zero-signal detected — restarting audio stream "
                                f"({self._stream_restart_attempts}/{_MAX_RESTART}); "
                                "device may have been muted or disconnected"
                            )
                            self._last_nonzero_audio_ts = _now_mono  # reset so we don't loop-restart
                            break  # exit inner loop; outer loop will reopen the stream
                        if not self._should_process_recognizer_audio(rms):
                            continue
                        # Device is delivering healthy audio — reset the stall counter
                        # and stamp the activity clock so the 10-s silence warning
                        # does not fire while we are actively processing audio.
                        self._stream_restart_attempts = 0
                        self._last_audio_activity_s = time.monotonic()
                        current_time = time.time()
                        self._capture_chunk_signature(chunk, rms)
                        self._note_live_hearing_activity(now=current_time, source="vosk")
                        if recognizer.AcceptWaveform(chunk):
                            self._clear_pending_partial_text()
                            result = json.loads(recognizer.Result() or "{}")
                            normalized = self._normalize_command_text(result.get("text", ""))
                            if not normalized:
                                continue
                            now = time.time()
                            if self._command_cooldown_s > 0.0 and (now - self._last_emit_s) < self._command_cooldown_s:
                                self._on_log("[VOICE-DIAG] command-throttled-by-cooldown")
                                continue
                            if self._is_recent_duplicate_command(normalized, now=now):
                                self._on_log(f"[VOICE-DIAG] command-deduped='{normalized}'")
                                continue
                            self._last_emit_s = now
                            self._on_log(f"[VOICE-DIAG] command-emitted='{normalized}'")
                            self._record_emitted_command(normalized, now=now)
                            self._on_command(normalized)
                        else:
                            try:
                                partial = json.loads(recognizer.PartialResult() or "{}")
                                partial_text = str(partial.get("partial", "") or "").strip().lower()
                                if partial_text:
                                    self._publish_partial_transcript(partial_text, source="vosk")
                            except Exception:
                                pass

            except Exception as exc:
                self._on_log(f"Vosk listen loop error: {exc}")
                if self._stop.is_set():
                    return
                self._stream_restart_attempts += 1
                if self._stream_restart_attempts > _MAX_RESTART:
                    self._on_log(
                        "[VOICE] Audio stream failed — max restart attempts reached, "
                        "disabling voice input"
                    )
                    self._emit_transcript("status", "mic_error", source="watchdog")
                    return
                self._on_log(
                    f"[VOICE] Audio stream error — will retry in 1 s "
                    f"(attempt {self._stream_restart_attempts}/{_MAX_RESTART})"
                )

            # Brief back-off before the next stream open attempt (stall break or error).
            # Skip sleep if we are stopping to avoid a 1-second delay on clean shutdown.
            if not self._stop.is_set():
                time.sleep(1.0)

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
        dictation_enabled = self._use_windows_dictation_grammar()
        dictation_literal = "$true" if dictation_enabled else "$false"
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
$engine.EndSilenceTimeout = [TimeSpan]::FromMilliseconds(1800)
$engine.EndSilenceTimeoutAmbiguous = [TimeSpan]::FromMilliseconds(1700)
$dictationEnabled = {dictation_literal}
if ($dictationEnabled) {{
    $engine.LoadGrammar((New-Object System.Speech.Recognition.DictationGrammar))
}}
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
        _ps_script_path: Optional[str] = None
        try:
            import tempfile
            script = self._powershell_listener_script()
            # Write the script to a temp file and pass via -File to avoid the
            # Windows CreateProcess command-line 32 767-character limit that
            # causes [WinError 206] when the grammar phrase list is large.
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".ps1",
                delete=False,
                encoding="utf-8",
            ) as _tf:
                _tf.write(script)
                _ps_script_path = _tf.name
            self._recognizer_process = subprocess.Popen(
                [
                    "powershell.exe",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    _ps_script_path,
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
            if _ps_script_path:
                try:
                    os.unlink(_ps_script_path)
                except Exception:
                    pass
            super()._listen_loop()
            return

        self._on_log("[VOICE] Runtime STT backend: Windows native speech")
        self._signature_probe.start()
        proc = self._recognizer_process
        try:
            while not self._stop.is_set() and proc is not None:
                loop_now = time.time()
                self._release_live_hearing_status_if_due(now=loop_now, source="windows")
                self._flush_listening_window_if_due(now=loop_now)
                line = proc.stdout.readline() if proc.stdout is not None else ""
                if not line:
                    if proc.poll() is not None:
                        break
                    continue
                message = str(line or "").strip()
                if not message:
                    continue
                if message == "status|listening":
                    self._emit_status("listening", source="windows", force=True)
                    self._on_log("Windows speech command listener started on default input device")
                    continue
                if message.startswith("partial|"):
                    partial_text = str(message.split("|", 1)[1] or "").strip().lower()
                    if partial_text:
                        self._publish_partial_transcript(partial_text, source="windows")
                    continue
                if message.startswith("recognized|"):
                    _prefix, confidence_text, raw_text = (message.split("|", 2) + ["", "", ""])[:3]
                    recognized_text = str(raw_text or "").strip().lower()
                    if recognized_text:
                        self._note_live_hearing_activity(now=time.time(), source="windows")
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
            if _ps_script_path:
                try:
                    os.unlink(_ps_script_path)
                except Exception:
                    pass

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
    if not requested:
        raw = str(os.getenv("SMART_SENTRY_USE_WINDOWS_NATIVE_STT", "") or "").strip().lower()
        if raw not in {"1", "true", "yes", "on"}:
            return False
        default_name = _default_windows_input_device_name().strip()
        return bool(default_name)
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
        speech_volume_pct: int = 100,
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
        self._speech_volume_pct = AsyncWavPlayer._clamp_volume_pct(speech_volume_pct)

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
                    volume_pct=self._speech_volume_pct,
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
                    volume_pct=self._speech_volume_pct,
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
                    volume_pct=self._speech_volume_pct,
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
        return self._wav_player.play_file(str(wav_path), volume_pct=100, channel="event")

    def set_speech_volume_pct(self, volume_pct: int) -> None:
        self._speech_volume_pct = AsyncWavPlayer._clamp_volume_pct(volume_pct)
        for tts_engine in (self._kokoro_tts, self._neural_tts, self._edge_tts):
            if tts_engine is None:
                continue
            try:
                tts_engine.set_volume_pct(self._speech_volume_pct)
            except Exception:
                pass
        try:
            self._wav_player.set_live_volume_pct(self._speech_volume_pct, channel="speech")
        except Exception:
            pass

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

    def register_output_echo_suppression(self, text: str, *, extra_hold_s: float = 3.5) -> None:
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
