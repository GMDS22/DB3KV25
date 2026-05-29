from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


@dataclass(frozen=True)
class KnowledgeSource:
    title: str
    relative_path: str
    keywords: Sequence[str]
    category: str = "doc"
    max_chars: int = 1400


class AppKnowledgeBase:
    def __init__(self, root: Path | None = None):
        self.root = Path(root) if root is not None else Path(__file__).resolve().parents[3]

    def context_for_query(self, query: str, snapshot: Dict[str, Any], *, task_kind: str, max_chars: int = 6400) -> str:
        normalized_query = str(query or "").strip()
        tokens = self._query_tokens(normalized_query)
        sections: List[str] = [self._app_map_summary()]

        config_excerpt = self._config_excerpt(snapshot.get("config") or {}, tokens)
        if config_excerpt:
            sections.append("Relevant current config:\n" + config_excerpt)

        sources = self._select_sources(tokens, task_kind=task_kind)
        source_sections: List[str] = []
        remaining = max(1200, int(max_chars))
        for source in sources:
            excerpt = self._source_excerpt(source, tokens=tokens, max_chars=min(source.max_chars, remaining))
            if not excerpt:
                continue
            block = f"[{source.title}] ({source.relative_path})\n{excerpt}"
            block_len = len(block)
            if block_len > remaining and source_sections:
                break
            source_sections.append(block[:remaining])
            remaining -= min(block_len, remaining)
            if remaining <= 600:
                break
        if source_sections:
            sections.append("Relevant intended-behavior context:\n\n" + "\n\n".join(source_sections))

        return "\n\n".join(section for section in sections if section).strip()

    def _app_map_summary(self) -> str:
        return (
            "App structure overview:\n"
            "- app/sentry_v2/sentry_v2_tab.py: primary Smart Sentry UI, runtime controls, buttons, AI panel, config binding, camera/link actions.\n"
            "- app/sentry_v2/sentry_v2_engine.py: targeting, engagement state machine, target-loss recovery, guard return, search protocols, handoff logic.\n"
            "- app/sentry_v2/sentry_v2_config.py: authoritative dataclasses and default settings for detection, engagement, guard, connection, PIR, AI assistant, and UI behavior.\n"
            "- app/sentry_v2/sentry_v2_detector.py: detection pipeline and YOLO integration.\n"
            "- app/sentry_v2/sentry_v2_comm.py: controller bridge, transport state, servo telemetry, IO runtime.\n"
            "- app/sentry_v2/prompted_targets.py: prompted-target library and matcher.\n"
            "- app/sentry_v2/face_identity.py: lightweight face recognition pipeline.\n"
            "- SMART_SENTRY_MANUAL.md and validation docs: intended operator-visible behavior, contracts, troubleshooting, and recent verified feature changes."
        )

    def _select_sources(self, tokens: Sequence[str], *, task_kind: str) -> List[KnowledgeSource]:
        scored: List[tuple[int, KnowledgeSource]] = []
        for source in _KNOWLEDGE_SOURCES:
            score = self._source_score(source, tokens=tokens, task_kind=task_kind)
            if score > 0:
                scored.append((score, source))
        scored.sort(key=lambda item: (-item[0], item[1].relative_path))

        selected: List[KnowledgeSource] = []
        seen: set[str] = set()
        for _, source in scored:
            if source.relative_path in seen:
                continue
            seen.add(source.relative_path)
            selected.append(source)
            if len(selected) >= 6:
                break
        if not selected:
            return list(_DEFAULT_SOURCES)
        return selected

    def _source_score(self, source: KnowledgeSource, *, tokens: Sequence[str], task_kind: str) -> int:
        score = 1 if source in _DEFAULT_SOURCES else 0
        token_set = set(tokens)
        for keyword in source.keywords:
            keyword_tokens = set(self._query_tokens(keyword))
            if keyword_tokens and keyword_tokens.issubset(token_set):
                score += 5
            elif keyword_tokens and keyword_tokens & token_set:
                score += 2
        if task_kind in ("analysis", "recommendations") and source.category == "doc":
            score += 1
        if task_kind == "prompt" and source.category == "code":
            score += 1
        return score

    def _source_excerpt(self, source: KnowledgeSource, *, tokens: Sequence[str], max_chars: int) -> str:
        path = self.root / source.relative_path
        if not path.exists():
            return ""
        try:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
        except Exception:
            return ""
        if source.category == "code":
            return self._code_excerpt(text, tokens=tokens, max_chars=max_chars)
        return self._document_excerpt(text, tokens=tokens, max_chars=max_chars)

    def _document_excerpt(self, text: str, *, tokens: Sequence[str], max_chars: int) -> str:
        line_excerpt = self._document_line_excerpt(text, tokens=tokens, max_chars=max_chars)
        if line_excerpt:
            return line_excerpt
        chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
        scored: List[tuple[int, str]] = []
        for chunk in chunks:
            score = self._chunk_score(chunk, tokens)
            if score > 0:
                scored.append((score, chunk))
        if not scored:
            return text[:max_chars].strip()
        scored.sort(key=lambda item: -item[0])
        selected: List[str] = []
        used = 0
        for _, chunk in scored[:4]:
            snippet = chunk[: min(len(chunk), 900)]
            if used and used + len(snippet) > max_chars:
                break
            selected.append(snippet)
            used += len(snippet) + 2
            if used >= max_chars:
                break
        return "\n\n".join(selected)[:max_chars].strip()

    def _document_line_excerpt(self, text: str, *, tokens: Sequence[str], max_chars: int) -> str:
        if not tokens:
            return ""
        lines = text.splitlines()
        matched_indexes = [index for index, line in enumerate(lines) if self._chunk_score(line, tokens) > 0]
        if not matched_indexes:
            return ""
        windows: List[str] = []
        consumed = 0
        seen_ranges: set[tuple[int, int]] = set()
        for index in matched_indexes[:6]:
            start = max(0, index - 1)
            end = min(len(lines), index + 3)
            marker = (start, end)
            if marker in seen_ranges:
                continue
            seen_ranges.add(marker)
            window = "\n".join(line.rstrip() for line in lines[start:end] if line.strip()).strip()
            if not window:
                continue
            if consumed and consumed + len(window) > max_chars:
                break
            windows.append(window)
            consumed += len(window) + 2
            if consumed >= max_chars:
                break
        return "\n\n".join(windows)[:max_chars].strip()

    def _code_excerpt(self, text: str, *, tokens: Sequence[str], max_chars: int) -> str:
        blocks = self._split_code_blocks(text)
        scored: List[tuple[int, str]] = []
        for block in blocks:
            score = self._chunk_score(block, tokens)
            if score > 0:
                scored.append((score, block))
        if not scored:
            return ""
        scored.sort(key=lambda item: -item[0])
        selected: List[str] = []
        used = 0
        for _, block in scored[:3]:
            snippet = block[: min(len(block), 1200)]
            if used and used + len(snippet) > max_chars:
                break
            selected.append(snippet)
            used += len(snippet) + 2
            if used >= max_chars:
                break
        return "\n\n".join(selected)[:max_chars].strip()

    def _split_code_blocks(self, text: str) -> List[str]:
        lines = text.splitlines()
        blocks: List[str] = []
        current: List[str] = []
        current_indent = 0
        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            is_header = stripped.startswith("def ") or stripped.startswith("class ")
            if is_header and current:
                blocks.append("\n".join(current).strip())
                current = []
            if is_header:
                current_indent = indent
            if current or is_header:
                if stripped and indent < current_indent and not is_header:
                    blocks.append("\n".join(current).strip())
                    current = []
                current.append(line)
        if current:
            blocks.append("\n".join(current).strip())
        return [block for block in blocks if block]

    def _config_excerpt(self, config: Dict[str, Any], tokens: Sequence[str]) -> str:
        if not isinstance(config, dict):
            return ""
        focus_keys = ["detection_mode", "target_filter", "engagement", "guard", "connection", "pir_guard", "face_recognition", "sound", "ai_assistant"]
        token_set = set(tokens)
        if token_set & {"loss", "target", "search", "reacquire", "handoff", "persistent", "recovery"}:
            focus_keys = ["engagement", "guard", "detection_mode", "target_filter", "pir_guard"]
        elif token_set & {"camera", "link", "connection", "bridge", "udp", "wifi", "serial"}:
            focus_keys = ["connection", "guard", "engagement"]
        elif token_set & {"face", "identity", "voice", "speech", "assistant"}:
            focus_keys = ["face_recognition", "sound", "ai_assistant", "connection"]
        elif token_set & {"button", "control", "ui", "toggle", "save", "rest", "home"}:
            focus_keys = ["guard", "connection", "sound", "ai_assistant"]
        slim = {key: config.get(key) for key in focus_keys if key in config}
        return json.dumps(slim, indent=2)[:2600]

    def _chunk_score(self, chunk: str, tokens: Sequence[str]) -> int:
        lowered = chunk.lower()
        score = 0
        for token in tokens:
            if token in lowered:
                score += 2
        if any(token in lowered for token in ("loss", "reacquire", "search", "handoff", "button", "guard", "camera", "link")):
            score += 1
        return score

    def _query_tokens(self, query: str) -> List[str]:
        words = re.findall(r"[a-z0-9_]+", str(query or "").lower())
        filtered = [word for word in words if len(word) >= 3 or word in {"ui", "io"}]
        return filtered[:32]


_KNOWLEDGE_SOURCES: List[KnowledgeSource] = [
    KnowledgeSource("AI Blueprint", "SMART SENTRY AI BLUEPRINT.md", ("assistant", "conversation", "diagnostic", "diagnostics", "face detection", "runtime analysis", "wake word"), "doc", 1600),
    KnowledgeSource("Documentation Hub", "SMART_SENTRY_DOCUMENTATION_HUB.md", ("documentation", "docs", "documents", "where to start", "doc map", "document hub"), "doc", 1200),
    KnowledgeSource("Documentation Style Standard", "SMART_SENTRY_DOCUMENTATION_STYLE_STANDARD.md", ("documentation style", "formatting", "doc standard", "metadata", "docs formatting"), "doc", 1200),
    KnowledgeSource("Smart Sentry Manual", "SMART_SENTRY_MANUAL.md", ("manual", "operator", "feature", "button", "target loss", "reacquire", "guard", "settings"), "doc", 1800),
    KnowledgeSource("Face Import Voice Guide", "SMART_SENTRY_FACE_IMPORT_VOICE_GUIDE.md", ("face", "photo", "import", "preview inbox", "batch", "profile batches"), "doc", 1400),
    KnowledgeSource("Document Browser Guide", "SMART_SENTRY_DOCUMENT_BROWSER_GUIDE.md", ("document browser", "docs browser", "browse documents", "search docs"), "doc", 1200),
    KnowledgeSource("Issue Log", "SMART_SENTRY_ISSUE_LOG.md", ("issue", "fix", "target loss", "recovery", "preview", "performance", "reacquire"), "doc", 1400),
    KnowledgeSource("App Change Impact", "SMART_SENTRY_APP_CHANGE_IMPACT.md", ("contract", "impact", "target loss", "recovery", "return to guard"), "doc", 1400),
    KnowledgeSource("Live Validation Checklist", "SMART_SENTRY_V2_3_2_LIVE_VALIDATION_CHECKLIST.md", ("validation", "checklist", "target loss", "recovery", "handoff"), "doc", 1400),
    KnowledgeSource("Runtime Export Guide", "SMART_SENTRY_RUNTIME_DATA_EXPORT.md", ("runtime", "snapshot", "export", "analysis"), "doc", 1200),
    KnowledgeSource("PIR At A Glance", "PIR_AT_A_GLANCE.md", ("pir", "sensor id", "cue hold", "search rounds", "current contract", "nano"), "doc", 1200),
    KnowledgeSource("PIR Quick Start", "PIR_GUARD_QUICK_START.md", ("pir", "search style", "fast reacquire", "hunting"), "doc", 1200),
    KnowledgeSource("PIR Implementation", "PIR_GUARD_IMPLEMENTATION_COMPLETE.md", ("pir", "search style", "cue hold", "target loss"), "doc", 1200),
    KnowledgeSource("Main UI Tab", "app/sentry_v2/sentry_v2_tab.py", ("button", "ui", "toggle", "camera", "connection", "home", "rest", "analyze"), "code", 1600),
    KnowledgeSource("Engine", "app/sentry_v2/sentry_v2_engine.py", ("engine", "loss recovery", "reacquire", "handoff", "persistent", "search", "guard"), "code", 1800),
    KnowledgeSource("Config", "app/sentry_v2/sentry_v2_config.py", ("config", "engagement", "guard", "connection", "pir", "face", "assistant"), "code", 1500),
    KnowledgeSource("Detector", "app/sentry_v2/sentry_v2_detector.py", ("detector", "yolo", "motion", "color", "tracking"), "code", 1200),
    KnowledgeSource("Comms", "app/sentry_v2/sentry_v2_comm.py", ("connection", "bridge", "udp", "wifi", "serial", "servo telemetry"), "code", 1200),
    KnowledgeSource("Prompted Targets", "app/sentry_v2/prompted_targets.py", ("prompted", "target", "matcher", "search"), "code", 1200),
    KnowledgeSource("Face Identity", "app/sentry_v2/face_identity.py", ("face", "identity", "recognition", "friendly"), "code", 1000),
]

_DEFAULT_SOURCE_TITLES: Sequence[str] = (
    "AI Blueprint",
    "Smart Sentry Manual",
    "PIR At A Glance",
    "PIR Quick Start",
)

_DEFAULT_SOURCES: Sequence[KnowledgeSource] = tuple(
    next(source for source in _KNOWLEDGE_SOURCES if source.title == title)
    for title in _DEFAULT_SOURCE_TITLES
)