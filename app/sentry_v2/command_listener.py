from __future__ import annotations

from typing import Callable, Optional

from .voice_runtime import VoskCommandListener


class CommandListener:
    """Thin compatibility wrapper around the offline Vosk command listener."""

    def __init__(
        self,
        model_path: str = "models/vosk",
        wake_word: str = "sentry",
        command_cooldown_s: float = 0.35,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._model_path = str(model_path)
        self._wake_word = str(wake_word)
        self._command_cooldown_s = float(command_cooldown_s)
        self._on_log = on_log
        self._listener = VoskCommandListener(
            model_path=self._model_path,
            wake_word=self._wake_word,
            command_cooldown_s=self._command_cooldown_s,
            on_command=lambda _text: None,
            on_log=self._on_log,
        )

    def start(self, on_command: Callable[[str], None]) -> None:
        self._listener = VoskCommandListener(
            model_path=self._model_path,
            wake_word=self._wake_word,
            command_cooldown_s=self._command_cooldown_s,
            on_command=on_command,
            on_log=self._on_log,
        )
        self._listener.start()

    def stop(self) -> None:
        self._listener.stop()


def listen_loop(on_command: Callable[[str], None], model_path: str = "models/vosk", wake_word: str = "sentry") -> CommandListener:
    """Compatibility helper similar to a direct listen loop API.

    Returns the listener handle so callers can stop it when needed.
    """
    listener = CommandListener(model_path=model_path, wake_word=wake_word)
    listener.start(on_command)
    return listener
