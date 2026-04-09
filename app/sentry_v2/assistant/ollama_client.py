from __future__ import annotations

from typing import List

import requests


class OllamaError(RuntimeError):
    pass


class OllamaClient:
    def __init__(self, host: str = "http://localhost:11434", timeout_s: float = 45.0):
        self.host = str(host or "http://localhost:11434").rstrip("/")
        self.timeout_s = max(5.0, float(timeout_s or 45.0))

    def is_available(self) -> bool:
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=min(self.timeout_s, 5.0))
            return response.status_code == 200
        except Exception:
            return False

    def list_models(self) -> List[str]:
        response = requests.get(f"{self.host}/api/tags", timeout=min(self.timeout_s, 10.0))
        if response.status_code != 200:
            raise OllamaError(f"Ollama model list failed with HTTP {response.status_code}")
        payload = response.json()
        models = payload.get("models") or []
        names = [str(item.get("name") or "").strip() for item in models]
        return [name for name in names if name]

    def generate(self, model: str, prompt: str, system: str = "", *, timeout_s: float | None = None, options: dict | None = None) -> str:
        body = {
            "model": str(model or "").strip(),
            "prompt": str(prompt or ""),
            "system": str(system or ""),
            "stream": False,
        }
        cleaned_options = dict(options or {})
        if cleaned_options:
            body["options"] = cleaned_options
        request_timeout_s = self.timeout_s if timeout_s is None else max(3.0, float(timeout_s or self.timeout_s))
        response = requests.post(
            f"{self.host}/api/generate",
            json=body,
            timeout=(3.05, request_timeout_s),
        )
        if response.status_code != 200:
            raise OllamaError(f"Ollama generate failed with HTTP {response.status_code}: {response.text[:300]}")
        payload = response.json()
        text = str(payload.get("response") or "").strip()
        if text:
            return text
        thinking = str(payload.get("thinking") or "").strip()
        if thinking:
            return thinking
        raise OllamaError("Ollama returned no response text")
