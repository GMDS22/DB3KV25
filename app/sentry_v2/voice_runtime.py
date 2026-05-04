from __future__ import annotations

import os
import queue
import re
import threading
import time
from pathlib import Path
from typing import Callable, Optional


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
                # Fallback: convert mp3 bytes via wave if possible
                try:
                    import subprocess
                    import tempfile
                    wav_tmp = path.replace(".mp3", "_tmp.wav")
                    subprocess.run(
                        ["ffmpeg", "-y", "-i", path, wav_tmp],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
                    )
                    path = wav_tmp
                    ext = ".wav"
                except Exception:
                    pass
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


class VoskCommandListener:
    """Offline Vosk recognizer loop with wake-word and callback dispatch."""

    def __init__(
        self,
        *,
        model_path: str,
        wake_word: str,
        command_cooldown_s: float,
        on_command: Callable[[str], None],
        on_log: Optional[Callable[[str], None]] = None,
        device_name: str = "",
    ) -> None:
        self._model_path = str(model_path or "").strip()
        self._wake_word = str(wake_word or "sentry").strip().lower()
        self._command_cooldown_s = max(0.0, float(command_cooldown_s or 0.0))
        self._on_command = on_command
        self._on_log = on_log or (lambda _msg: None)
        self._stop = threading.Event()
        self._audio_queue: "queue.Queue[bytes]" = queue.Queue(maxsize=24)
        self._worker: Optional[threading.Thread] = None
        self._last_emit_s: float = 0.0
        self._device_name = str(device_name or "").strip()

    def start(self) -> bool:
        if self._worker is not None and self._worker.is_alive():
            return True
        self._stop.clear()
        self._worker = threading.Thread(target=self._listen_loop, name="sentry-voice-vosk", daemon=True)
        self._worker.start()
        return True

    def stop(self) -> None:
        self._stop.set()

    def _audio_callback(self, indata, _frames, _time_info, status) -> None:
        if status:
            self._on_log(f"Vosk input status: {status}")
        if self._stop.is_set():
            return
        try:
            self._audio_queue.put_nowait(bytes(indata))
        except queue.Full:
            try:
                self._audio_queue.get_nowait()
            except queue.Empty:
                pass
            try:
                self._audio_queue.put_nowait(bytes(indata))
            except Exception:
                pass

    def _normalize_command_text(self, text: str) -> str:
        normalized = str(text or "").strip().lower()
        normalized = re.sub(r"\s+", " ", normalized)
        if not normalized:
            return ""
        if not self._wake_word:
            return normalized
        wake_word = re.sub(r"[^a-z0-9 ]+", " ", str(self._wake_word or "").strip().lower())
        wake_word = re.sub(r"\s+", " ", wake_word).strip()
        if not wake_word:
            return normalized
        sanitized = re.sub(r"[^a-z0-9 ]+", " ", normalized)
        sanitized = re.sub(r"\s+", " ", sanitized).strip()
        pattern = r"\b" + re.escape(wake_word) + r"\b"
        if not re.search(pattern, sanitized):
            return ""
        stripped = re.sub(pattern, " ", sanitized, count=1).strip()
        stripped = re.sub(r"\s+", " ", stripped)
        if not stripped:
            return wake_word
        return stripped

    def _listen_loop(self) -> None:
        try:
            import json
            import sounddevice as sd
            from vosk import KaldiRecognizer, Model
        except Exception as exc:
            self._on_log(f"Vosk listener dependencies unavailable: {exc}")
            return

        model_dir = Path(self._model_path)
        if not model_dir.is_dir():
            self._on_log(f"Vosk model path not found: {model_dir}")
            return

        try:
            model = Model(str(model_dir))
            recognizer = KaldiRecognizer(model, 16000)
        except Exception as exc:
            self._on_log(f"Failed to initialize Vosk recognizer: {exc}")
            return

        try:
            device_index = self._resolve_input_device(sd)
            with sd.RawInputStream(
                samplerate=16000,
                blocksize=8000,
                dtype="int16",
                channels=1,
                callback=self._audio_callback,
                device=device_index,
            ):
                if device_index is not None:
                    self._on_log(f"Offline voice command listener started on device index {device_index}")
                else:
                    self._on_log("Offline voice command listener started")
                while not self._stop.is_set():
                    try:
                        data = self._audio_queue.get(timeout=0.25)
                    except queue.Empty:
                        continue
                    if recognizer.AcceptWaveform(data):
                        result = json.loads(recognizer.Result() or "{}")
                        normalized = self._normalize_command_text(result.get("text", ""))
                        if not normalized:
                            continue
                        now = time.time()
                        if self._command_cooldown_s > 0.0 and (now - self._last_emit_s) < self._command_cooldown_s:
                            continue
                        self._last_emit_s = now
                        self._on_command(normalized)
        except Exception as exc:
            self._on_log(f"Vosk listen loop terminated: {exc}")

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
        on_log: Optional[Callable[[str], None]] = None,
        neural_tts_enabled: bool = False,
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
    ) -> None:
        self._on_log = on_log or (lambda _msg: None)
        self._sounds_dir = Path(sounds_dir)
        self._sounds_dir.mkdir(parents=True, exist_ok=True)
        self._commands_enabled = bool(commands_enabled)
        self._wav_player = AsyncWavPlayer(on_log=self._on_log)
        self._listener = VoskCommandListener(
            model_path=model_path,
            wake_word=wake_word,
            command_cooldown_s=command_cooldown_s,
            on_command=on_command,
            on_log=self._on_log,
            device_name=device_name,
        )

        self._kokoro_tts: Optional[KokoroTTS] = None
        self._neural_tts: Optional[AzureNeuralTTS] = None
        self._edge_tts: Optional[EdgeNeuralTTS] = None

        _kokoro_model = str(kokoro_model_path or "").strip()
        _kokoro_voices = str(kokoro_voices_path or "").strip()
        if _kokoro_model and Path(_kokoro_model).is_file() and _kokoro_voices and Path(_kokoro_voices).is_file():
            self._kokoro_tts = KokoroTTS(
                self._wav_player,
                model_path=_kokoro_model,
                voices_path=_kokoro_voices,
                voice_name=kokoro_voice_name,
                speed=kokoro_speed,
                on_log=self._on_log,
            )
            self._on_log(f"[VOICE] Runtime speech backend: Kokoro offline (voice: {kokoro_voice_name})")
        elif neural_tts_enabled:
            self._on_log("[VOICE] Kokoro runtime speech unavailable: missing model or voices file")

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
        if self._neural_tts is not None:
            self._neural_tts.close()
        if self._kokoro_tts is not None:
            self._kokoro_tts.close()
        if self._edge_tts is not None:
            self._edge_tts.close()
        self._wav_player.close()

    def play_event(self, event_name: str) -> bool:
        key = str(event_name or "").strip().lower()
        if not key:
            return False
        wav_path = self._sounds_dir / f"{key}.wav"
        return self._wav_player.play_file(str(wav_path))

    def speak_dynamic(self, text: str) -> bool:
        # Runtime app speech is intentionally Kokoro-first and Kokoro-only unless
        # an explicit fallback backend is wired by the caller.
        if self._kokoro_tts is not None and self._kokoro_tts.enabled:
            return self._kokoro_tts.speak_async(text)
        if self._neural_tts is not None and self._neural_tts.enabled:
            return self._neural_tts.speak_async(text)
        if self._edge_tts is not None and self._edge_tts.enabled:
            return self._edge_tts.speak_async(text)
        return False
