from __future__ import annotations

import json
import re
from typing import Any, Dict, Iterable, List

from .app_knowledge import AppKnowledgeBase
from .models import AssistantAction, AssistantReply
from .ollama_client import OllamaClient
from .runtime_analyzer import RuntimeAnalyzer


_DETECTION_MODE_ACTIONS = (
    (10, "Motion-Locked Filtered Target", ("motion-locked filtered target", "motion locked filtered target", "filtered target", "motion-locked", "motion locked")),
    (9, "Hybrid: Color + YOLO", ("color + yolo", "color yolo", "hybrid color yolo", "color plus yolo")),
    (8, "Hybrid: Color + BackSub", ("color + backsub", "color backsub", "color + background subtraction", "color plus backsub")),
    (7, "Hybrid: Color + Frame Diff", ("color + frame diff", "color frame diff", "color + frame difference", "color plus frame diff")),
    (6, "Color Detection", ("color detection", "color mode", "color tracking")),
    (5, "Hybrid: BackSub + YOLO (Best)", ("backsub + yolo", "background subtraction + yolo", "hybrid backsub yolo", "best mode", "best detection mode")),
    (4, "Hybrid: Frame Diff + YOLO", ("frame diff + yolo", "frame difference + yolo", "motion + yolo", "frame diff yolo")),
    (3, "Hybrid: Frame Diff + BackSub", ("frame diff + backsub", "frame difference + backsub", "frame difference + background subtraction", "motion + backsub")),
    (2, "YOLO Object Detection", ("yolo object detection", "yolo mode", "object detection", "yolo")),
    (1, "Background Subtraction", ("background subtraction", "backsub", "background mode")),
    (0, "Frame Difference", ("frame difference", "frame diff", "motion mode", "motion detection")),
)

_ALLOWED_INTENT_ACTIONS = {
    "none",
    "go_home",
    "go_rest",
    "toggle_sentry",
    "move_position",
    "set_detection_mode",
    "toggle_face_recognition",
    "toggle_shortcuts",
    "toggle_human_voice",
    "toggle_ai_auto_speak",
    "set_human_voice_style",
    "toggle_camera",
    "connect_link",
    "disconnect_link",
    "draft_setting_change",
}

_SETTING_CHANGE_SPECS = (
    {
        "path": "detection_mode.yolo_confidence",
        "label": "YOLO confidence",
        "aliases": ("yolo confidence", "confidence threshold", "confidence"),
        "value_type": "float",
        "step": 0.05,
        "decimals": 2,
        "percent_scale": True,
    },
    {
        "path": "detection_mode.yolo_min_area",
        "label": "YOLO minimum area",
        "aliases": ("yolo minimum area", "yolo min area", "minimum area", "min area"),
        "value_type": "int",
        "step": 100.0,
    },
    {
        "path": "detection_mode.min_contour_area",
        "label": "Minimum contour area",
        "aliases": ("minimum contour area", "min contour area", "contour area", "motion contour area"),
        "value_type": "float",
        "step": 100.0,
        "decimals": 1,
    },
    {
        "path": "engagement.min_threat_score",
        "label": "Minimum threat score",
        "aliases": ("minimum threat score", "min threat score", "threat score", "threat threshold", "engagement threshold"),
        "value_type": "float",
        "step": 0.05,
        "decimals": 2,
        "percent_scale": True,
    },
    {
        "path": "engagement.engagement_speed_pct",
        "label": "Engagement speed",
        "aliases": ("engagement speed", "tracking speed", "speed"),
        "value_type": "int",
        "step": 5.0,
    },
    {
        "path": "guard.camera_hfov",
        "label": "Camera horizontal field of view",
        "aliases": ("camera hfov", "camera field of view", "field of view", "fov"),
        "value_type": "float",
        "step": 5.0,
        "decimals": 1,
    },
    {
        "path": "lighting.led_pwm_value",
        "label": "LED brightness",
        "aliases": ("led brightness", "brightness", "led pwm", "light brightness"),
        "value_type": "int",
        "step": 10.0,
    },
    {
        "path": "lighting.auto_pwm_min",
        "label": "Auto PWM minimum",
        "aliases": ("auto pwm minimum", "auto pwm min", "minimum auto brightness", "minimum auto pwm"),
        "value_type": "int",
        "step": 10.0,
    },
    {
        "path": "lighting.auto_pwm_max",
        "label": "Auto PWM maximum",
        "aliases": ("auto pwm maximum", "auto pwm max", "maximum auto brightness", "maximum auto pwm"),
        "value_type": "int",
        "step": 10.0,
    },
)

_ASSISTANT_FULL_NAME = "Elion Mesk"
_ASSISTANT_IDENTITY_BRIEF = "Elion Mesk, Smart Sentry's local operator assistant."
_ASSISTANT_IDENTITY_DESCRIPTION = (
    "I monitor the live Smart Sentry runtime, explain what the system is doing, compare live behavior against intended app behavior, "
    "diagnose faults, accept supported local control commands, and adjust supported runtime settings while the app is running."
)
_ASSISTANT_IDENTITY_BOUNDARY = (
    "I stay grounded in the running app and its supported controls. I do not invent hardware state or pretend unsupported actions already happened."
)

_ASSISTANT_PERSONALITY_PROFILES: Dict[str, Dict[str, Any]] = {
    "sentinel": {
        "label": "Sentinel",
        "style_instruction": "calm, direct, and operational",
        "greeting": "Standing by. Tell me what you want me to check or do.",
        "thanks": "Understood. Standing by for the next task.",
        "personality_reply": "Sentinel. Calm, precise, and focused on the task.",
        "jokes": [
            "Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.",
            "Sentry humor stays disciplined. Even my jokes try to hold center before drifting.",
        ],
    },
    "hunter": {
        "label": "Hunter",
        "style_instruction": "focused, confident, and slightly aggressive without sounding reckless",
        "greeting": "Hunter profile active. Give me the next target task.",
        "thanks": "Copy that. Ready for the next move.",
        "personality_reply": "Hunter. Sharper, faster, and more forceful, but still controlled.",
        "jokes": [
            "Hunter joke. I told the tracker to stop chasing ghosts. It said only if the signal stops running first.",
            "My hunting humor is simple. Acquire the setup, lock the timing, release the punchline.",
        ],
    },
    "stealth": {
        "label": "Stealth",
        "style_instruction": "quiet, efficient, and minimal",
        "greeting": "Stealth profile active. I am listening.",
        "thanks": "Noted. Quiet and ready.",
        "personality_reply": "Stealth. Minimal, quiet, and low-drama.",
        "jokes": [
            "Stealth joke. I would deliver it louder, but then it would stop being stealth.",
            "My quietest joke is still detectable. The punchline leaves a small thermal signature.",
        ],
    },
    "playful": {
        "label": "Playful",
        "style_instruction": "friendly, lightly witty, and still grounded in the runtime facts",
        "greeting": "Playful profile active. What are we tuning, checking, or rescuing today?",
        "thanks": "Any time. I am ready for the next clever idea.",
        "personality_reply": "Playful. More conversational and light, but still tied to the real runtime.",
        "jokes": [
            "Playful joke. I tried to teach the turret stand-up, but it kept rotating to face the audience before the punchline.",
            "Another one. Smart Sentry does not panic under pressure. It just calls it precision with atmosphere.",
        ],
    },
}


class LocalAssistantService:
    def __init__(self, client: OllamaClient | None = None, analyzer: RuntimeAnalyzer | None = None, knowledge_base: AppKnowledgeBase | None = None, *, personality: str = "sentinel"):
        self._client = client or OllamaClient()
        self._analyzer = analyzer or RuntimeAnalyzer()
        self._knowledge = knowledge_base or AppKnowledgeBase()
        self._personality = str(personality or "sentinel").strip().lower() or "sentinel"
        self._analysis_history: List[str] = []
        self._command_history: List[str] = []

    def _remember_analysis(self, note: str) -> None:
        cleaned = str(note or "").strip()
        if not cleaned:
            return
        self._analysis_history.append(cleaned)
        self._analysis_history = self._analysis_history[-3:]

    def _remember_command(self, note: str) -> None:
        cleaned = str(note or "").strip()
        if not cleaned:
            return
        self._command_history.append(cleaned)
        self._command_history = self._command_history[-3:]

    def _memory_context(self) -> Dict[str, List[str]]:
        return {
            "analysis_history": list(self._analysis_history[-3:]),
            "command_history": list(self._command_history[-3:]),
        }

    def _profile_query_kind(self, prompt_text: str) -> str | None:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if not normalized:
            return None
        introduction_patterns = (
            r"\bintroduce yourself\b",
            r"\bdescribe yourself\b",
            r"\btell me about yourself\b",
        )
        identity_patterns = (
            r"\bwho are you\b",
            r"\bwhat are you\b",
            r"\bwhat(?:'s| is) your name\b",
            r"\bstate your name\b",
            r"\bidentify yourself\b",
            r"\bwho is elion mesk\b",
            r"\bare you elion mesk\b",
        )
        capability_patterns = (
            r"\bwhat do you do\b",
            r"\bwhat can you do\b",
            r"\bwhat is your role\b",
            r"\bwhat is your purpose\b",
            r"\bwhat are your capabilities\b",
            r"\bwhat do you help with\b",
        )
        if any(re.search(pattern, normalized) for pattern in introduction_patterns):
            return "introduction"
        if any(re.search(pattern, normalized) for pattern in identity_patterns):
            return "identity"
        if any(re.search(pattern, normalized) for pattern in capability_patterns):
            return "capabilities"
        return None

    def _has_recent_profile_query(self) -> bool:
        for prior in self._command_history[-3:]:
            if self._profile_query_kind(prior):
                return True
        return False

    def _profile_protocol_reply(self, prompt_text: str) -> str | None:
        query_kind = self._profile_query_kind(prompt_text)
        if query_kind is None:
            return None
        repeated = self._has_recent_profile_query()
        short_identity = "Elion Mesk. Smart Sentry's local operator assistant for runtime analysis, live control, and supported setting changes."
        short_capabilities = "Elion Mesk handles runtime analysis, behavior explanation, supported local commands, and live setting adjustments inside Smart Sentry."
        if query_kind == "identity":
            if repeated:
                return short_identity
            return f"I am {_ASSISTANT_FULL_NAME}. {_ASSISTANT_IDENTITY_DESCRIPTION} {_ASSISTANT_IDENTITY_BOUNDARY}"
        if query_kind == "capabilities":
            if repeated:
                return short_capabilities
            return f"{_ASSISTANT_IDENTITY_BRIEF} {_ASSISTANT_IDENTITY_DESCRIPTION} {_ASSISTANT_IDENTITY_BOUNDARY}"
        if repeated:
            return f"{short_identity} {short_capabilities}"
        return f"I am {_ASSISTANT_FULL_NAME}. {_ASSISTANT_IDENTITY_DESCRIPTION} {_ASSISTANT_IDENTITY_BOUNDARY}"

    def _assistant_personality_key(self) -> str:
        key = str(getattr(self, "_personality", "sentinel") or "sentinel").strip().lower()
        if key not in _ASSISTANT_PERSONALITY_PROFILES:
            return "sentinel"
        return key

    def _assistant_personality_profile(self) -> Dict[str, Any]:
        return _ASSISTANT_PERSONALITY_PROFILES.get(self._assistant_personality_key(), _ASSISTANT_PERSONALITY_PROFILES["sentinel"])

    def _conversational_protocol_reply(self, prompt_text: str) -> str | None:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if not normalized:
            return None
        profile = self._assistant_personality_profile()

        personality_patterns = (
            r"\bwhat(?:'s| is) your personality\b",
            r"\bwhat personality are you using\b",
            r"\bwhat personality.*\busing\b",
            r"\bwhich personality\b",
            r"\bcurrent personality\b",
            r"\bactive personality\b",
            r"\bpersonality mode\b",
        )
        if any(re.search(pattern, normalized) for pattern in personality_patterns):
            return f"Current assistant personality: {profile['label']}. {profile['personality_reply']}"

        joke_patterns = (
            r"\btell me (?:a|another) joke\b",
            r"\bmake me laugh\b",
            r"\bsomething funny\b",
            r"\bany jokes\b",
            r"\bjoke\b",
        )
        if any(re.search(pattern, normalized) for pattern in joke_patterns):
            jokes = list(profile.get("jokes") or [])
            if jokes:
                return str(jokes[len(self._command_history) % len(jokes)])

        if normalized in {"hi", "hello", "hey", "hi elion", "hello elion", "hey elion", "how are you", "how are you elion"}:
            return str(profile.get("greeting") or "Standing by.")

        thanks_patterns = (
            r"\bthanks\b",
            r"\bthank you\b",
            r"\bappreciate it\b",
        )
        if any(re.search(pattern, normalized) for pattern in thanks_patterns) and len(normalized.split()) <= 4:
            return str(profile.get("thanks") or "Standing by.")
        return None

    def is_available(self) -> bool:
        return self._client.is_available()

    def list_models(self) -> List[str]:
        return self._client.list_models()

    def _request_timeout_s(self) -> float:
        return max(5.0, float(getattr(self._client, "timeout_s", 45.0) or 45.0))

    def analyze_runtime(self, snapshot: Dict[str, Any], *, model: str, include_logs: bool = True) -> AssistantReply:
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
        self._remember_analysis(f"summary: {summary}")
        excerpt = self._snapshot_excerpt(snapshot, query_text="analyze current behavior", include_logs=include_logs, max_log_lines=4, max_chars=3200)
        knowledge = self._knowledge.context_for_query(
            "analyze current behavior and compare the runtime to intended app behavior",
            snapshot,
            task_kind="analysis",
            max_chars=3800,
        )
        prompt = self._analysis_prompt(summary, findings, recommendations, excerpt, knowledge)
        try:
            reply_text = self._client.generate(
                model=model,
                prompt=prompt,
                system=self._system_prompt(),
                timeout_s=self._request_timeout_s(),
                options=self._llm_options(max_output_tokens=220, temperature=0.15),
            )
            return AssistantReply(
                text=reply_text.strip(),
                source="ollama",
                findings=findings,
                recommendations=recommendations,
                raw_response=reply_text,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                memory_context=self._memory_context(),
            )
        except Exception as exc:
            fallback = self._fallback_analysis_text(snapshot, findings, recommendations)
            return AssistantReply(
                text=fallback,
                source="deterministic",
                findings=findings,
                recommendations=recommendations,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                memory_context=self._memory_context(),
                error=str(exc),
            )

    def recommend_settings(self, snapshot: Dict[str, Any], *, model: str, include_logs: bool = False) -> AssistantReply:
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
        self._remember_analysis(f"recommendations: {summary}")
        excerpt = self._snapshot_excerpt(snapshot, query_text="draft runtime recommendations", include_logs=include_logs, max_log_lines=6, max_chars=3600)
        knowledge = self._knowledge.context_for_query(
            "recommend settings and compare current runtime with intended app behavior",
            snapshot,
            task_kind="recommendations",
            max_chars=4200,
        )
        prompt = self._recommendation_prompt(summary, findings, recommendations, excerpt, knowledge)
        try:
            reply_text = self._client.generate(
                model=model,
                prompt=prompt,
                system=self._system_prompt(),
                timeout_s=self._request_timeout_s(),
                options=self._llm_options(max_output_tokens=260, temperature=0.15),
            )
            return AssistantReply(
                text=reply_text.strip(),
                source="ollama",
                findings=findings,
                recommendations=recommendations,
                raw_response=reply_text,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                memory_context=self._memory_context(),
            )
        except Exception as exc:
            fallback = self._fallback_recommendation_text(recommendations)
            return AssistantReply(
                text=fallback,
                source="deterministic",
                findings=findings,
                recommendations=recommendations,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                memory_context=self._memory_context(),
                error=str(exc),
            )

    def answer_operator_prompt(self, prompt_text: str, snapshot: Dict[str, Any], *, model: str, include_logs: bool = True) -> AssistantReply:
        profile_reply = self._profile_protocol_reply(prompt_text)
        if profile_reply is not None:
            self._remember_command(prompt_text)
            return AssistantReply(
                text=profile_reply,
                source="deterministic",
                model=model,
                raw_response="conversation_profile_protocol",
                prompt_used="conversation_profile_protocol",
                intent={
                    "action": "none",
                    "value": None,
                    "confidence": 1.0,
                    "needs_clarification": False,
                    "question": "",
                    "suggestions": [],
                    "payload": {},
                },
                memory_context=self._memory_context(),
            )
        conversational_reply = self._conversational_protocol_reply(prompt_text)
        if conversational_reply is not None:
            self._remember_command(prompt_text)
            return AssistantReply(
                text=conversational_reply,
                source="deterministic",
                model=model,
                raw_response="conversation_protocol",
                prompt_used="conversation_protocol",
                intent={
                    "action": "none",
                    "value": None,
                    "confidence": 1.0,
                    "needs_clarification": False,
                    "question": "",
                    "suggestions": [],
                    "payload": {},
                },
                memory_context=self._memory_context(),
            )
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
        self._remember_command(prompt_text)
        parsed_actions = self._parse_actions(prompt_text)
        intent = self._parse_intent(prompt_text, snapshot, model=model, fallback_actions=parsed_actions)
        actions = self._intent_to_actions(intent)
        if not actions:
            actions = parsed_actions
        excerpt = self._snapshot_excerpt(snapshot, query_text=prompt_text, include_logs=include_logs, max_log_lines=6, max_chars=3600)
        knowledge = self._knowledge.context_for_query(prompt_text, snapshot, task_kind="prompt", max_chars=4200)
        prompt = self._operator_prompt(prompt_text, summary, findings, recommendations, actions, excerpt, knowledge)
        try:
            reply_text = self._client.generate(
                model=model,
                prompt=prompt,
                system=self._system_prompt(),
                timeout_s=self._request_timeout_s(),
                options=self._llm_options(max_output_tokens=220, temperature=0.15),
            )
            return AssistantReply(
                text=reply_text.strip(),
                source="ollama",
                findings=findings,
                recommendations=recommendations,
                actions=actions,
                raw_response=reply_text,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                intent=intent,
                memory_context=self._memory_context(),
            )
        except Exception as exc:
            fallback = self._fallback_chat_text(prompt_text, snapshot, findings, recommendations, actions)
            return AssistantReply(
                text=fallback,
                source="deterministic",
                findings=findings,
                recommendations=recommendations,
                actions=actions,
                prompt_used=prompt,
                runtime_excerpt=excerpt,
                model=model,
                intent=intent,
                memory_context=self._memory_context(),
                error=str(exc),
            )

    def _extract_first_json_object(self, text: str) -> Dict[str, Any] | None:
        raw = str(text or "").strip()
        if not raw:
            return None
        try:
            data = json.loads(raw)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
        match = re.search(r"\{[\s\S]*\}", raw)
        if not match:
            return None
        try:
            data = json.loads(match.group(0))
        except Exception:
            return None
        return data if isinstance(data, dict) else None

    def _normalize_intent(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        action = str(intent.get("action") or "none").strip().lower()
        if action not in _ALLOWED_INTENT_ACTIONS:
            action = "none"
        value = intent.get("value", None)
        try:
            confidence = float(intent.get("confidence", 0.0) or 0.0)
        except Exception:
            confidence = 0.0
        confidence = max(0.0, min(1.0, confidence))
        needs_clarification = bool(intent.get("needs_clarification", False))
        question = str(intent.get("question") or "").strip()
        suggestions = intent.get("suggestions") or []
        if not isinstance(suggestions, list):
            suggestions = []
        payload = intent.get("payload") or {}
        if not isinstance(payload, dict):
            payload = {}
        normalized = {
            "action": action,
            "value": value,
            "confidence": confidence,
            "needs_clarification": needs_clarification,
            "question": question,
            "suggestions": [str(item).strip() for item in suggestions if str(item).strip()],
            "payload": payload,
        }
        if action == "none" and not normalized["needs_clarification"] and not normalized["question"]:
            normalized["needs_clarification"] = True
            normalized["question"] = "Do you want analysis only, or should I prepare a specific local action plan?"
        return normalized

    def _intent_prompt(self, operator_prompt: str, excerpt: str, fallback_actions: List[AssistantAction]) -> str:
        return (
            "Parse the operator request into STRICT JSON only. "
            "Never include markdown, code fences, or extra prose. "
            "Allowed action values: "
            "none, go_home, go_rest, move_position, set_detection_mode, toggle_face_recognition, "
            "toggle_shortcuts, toggle_human_voice, toggle_ai_auto_speak, set_human_voice_style, "
            "toggle_camera, connect_link, disconnect_link, draft_setting_change.\n\n"
            "Required JSON schema:\n"
            "{\n"
            "  \"action\": \"...\",\n"
            "  \"value\": null,\n"
            "  \"confidence\": 0.0,\n"
            "  \"needs_clarification\": false,\n"
            "  \"question\": \"\",\n"
            "  \"suggestions\": [],\n"
            "  \"payload\": {}\n"
            "}\n\n"
            "If the request is ambiguous, set needs_clarification=true and ask one concise question.\n\n"
            f"Operator request:\n{operator_prompt}\n\n"
            f"Deterministic candidate actions:\n{self._format_actions(fallback_actions)}\n\n"
            f"Runtime excerpt:\n{excerpt}"
        )

    def _parse_intent(self, prompt_text: str, snapshot: Dict[str, Any], *, model: str, fallback_actions: List[AssistantAction]) -> Dict[str, Any]:
        default_action = "none"
        if fallback_actions:
            default_action = str(getattr(fallback_actions[0], "action_type", "none") or "none")
        default_intent = self._normalize_intent(
            {
                "action": default_action,
                "value": None,
                "confidence": 0.72 if fallback_actions else 0.35,
                "needs_clarification": not bool(fallback_actions),
                "question": "" if fallback_actions else "Can you confirm the exact action you want me to prepare?",
                "suggestions": [action.label for action in fallback_actions[:3]],
                "payload": dict(getattr(fallback_actions[0], "payload", {}) or {}) if fallback_actions else {},
            }
        )
        excerpt = self._snapshot_excerpt(snapshot, query_text=prompt_text, include_logs=False, max_log_lines=0, max_chars=2200)
        prompt = self._intent_prompt(prompt_text, excerpt, fallback_actions)
        try:
            response_text = self._client.generate(
                model=model,
                prompt=prompt,
                system="You are Smart Sentry command intent parser. Output only strict JSON.",
                timeout_s=min(self._request_timeout_s(), 20.0),
                options=self._llm_options(max_output_tokens=140, temperature=0.0),
            )
        except Exception:
            return default_intent
        parsed = self._extract_first_json_object(response_text)
        if not isinstance(parsed, dict):
            return default_intent
        return self._normalize_intent(parsed)

    def _intent_to_actions(self, intent: Dict[str, Any]) -> List[AssistantAction]:
        if not isinstance(intent, dict):
            return []
        if bool(intent.get("needs_clarification", False)):
            return []
        action_type = str(intent.get("action") or "none").strip().lower()
        if action_type not in _ALLOWED_INTENT_ACTIONS or action_type == "none":
            return []
        payload = intent.get("payload") or {}
        if not isinstance(payload, dict):
            payload = {}
        value = intent.get("value", None)
        if action_type == "move_position":
            if value is not None and isinstance(value, dict):
                payload = {**payload, **value}
            return [AssistantAction("move_position", "Move turret from parsed intent", payload, False)]
        if action_type == "set_detection_mode":
            if "mode_index" not in payload and value is not None:
                try:
                    payload["mode_index"] = int(value)
                except Exception:
                    pass
            return [AssistantAction("set_detection_mode", "Switch detection mode from parsed intent", payload, True)]
        if action_type == "toggle_sentry":
            if "enabled" not in payload and value is not None:
                payload["enabled"] = bool(value)
            enabled = bool(payload.get("enabled", True))
            label = "Enable Smart Sentry" if enabled else "Disable Smart Sentry"
            return [AssistantAction("toggle_sentry", label, {"enabled": enabled}, False)]
        if action_type in {"toggle_face_recognition", "toggle_shortcuts", "toggle_human_voice", "toggle_ai_auto_speak", "toggle_camera"}:
            if "enabled" not in payload and "open" not in payload and value is not None:
                if action_type == "toggle_camera":
                    payload["open"] = bool(value)
                else:
                    payload["enabled"] = bool(value)
            label = action_type.replace("_", " ").strip().title()
            return [AssistantAction(action_type, label, payload, False)]
        if action_type == "set_human_voice_style":
            if "style_key" not in payload and value is not None:
                payload["style_key"] = str(value)
            return [AssistantAction("set_human_voice_style", "Set voice style from parsed intent", payload, False)]
        if action_type == "draft_setting_change":
            return [AssistantAction("draft_setting_change", "Draft setting change from parsed intent", payload, False)]
        if action_type in {"go_home", "go_rest", "connect_link", "disconnect_link"}:
            return [AssistantAction(action_type, action_type.replace("_", " ").title(), payload, False)]
        return []

    def _parse_actions(self, prompt_text: str) -> List[AssistantAction]:
        lower_prompt = str(prompt_text or "").lower()
        if not self._is_explicit_action_request(lower_prompt):
            return []
        actions: List[AssistantAction] = []
        seen: set[str] = set()

        def _append(action: AssistantAction) -> None:
            dedupe_key = str(action.action_type)
            if action.payload:
                try:
                    payload_key = json.dumps(action.payload, sort_keys=True, default=str)
                except Exception:
                    payload_key = repr(sorted(action.payload.items()))
                dedupe_key = f"{action.action_type}:{payload_key}"
            if dedupe_key not in seen:
                seen.add(dedupe_key)
                actions.append(action)

        if self._matches_action_request(lower_prompt, ("wake", "return", "go", "move"), ("home", "guard home", "home position")):
            _append(AssistantAction("go_home", "Move to guard home position", requires_permission=False))
        if self._matches_action_request(lower_prompt, ("rest", "go", "move", "return"), ("rest", "rest position")):
            _append(AssistantAction("go_rest", "Move to rest position", requires_permission=False))
        if self._matches_action_request(
            lower_prompt,
            ("enable", "start", "resume", "turn on", "activate"),
            ("smart sentry", "sentry", "tracking", "guarding mode", "guard mode", "autotracking", "auto tracking"),
        ):
            _append(AssistantAction("toggle_sentry", "Enable Smart Sentry", {"enabled": True}, False))
        if self._matches_action_request(
            lower_prompt,
            ("disable", "stop", "pause", "turn off", "deactivate"),
            ("smart sentry", "sentry", "tracking", "guarding mode", "guard mode", "autotracking", "auto tracking"),
        ):
            _append(AssistantAction("toggle_sentry", "Disable Smart Sentry", {"enabled": False}, False))
        position_action = self._extract_position_action(prompt_text)
        if position_action is not None:
            _append(position_action)
        detection_mode_action = self._extract_detection_mode_action(lower_prompt)
        if detection_mode_action is not None:
            _append(detection_mode_action)
        for draft_action in self._extract_setting_draft_actions(prompt_text):
            _append(draft_action)
        if self._matches_action_request(lower_prompt, ("enable", "turn on"), ("face recognition",)):
            _append(AssistantAction("toggle_face_recognition", "Enable face recognition", {"enabled": True}, False))
        if self._matches_action_request(lower_prompt, ("disable", "turn off"), ("face recognition",)):
            _append(AssistantAction("toggle_face_recognition", "Disable face recognition", {"enabled": False}, False))
        if self._matches_action_request(lower_prompt, ("enable", "turn on"), ("shortcuts", "keyboard shortcuts")):
            _append(AssistantAction("toggle_shortcuts", "Enable shortcuts", {"enabled": True}, False))
        if self._matches_action_request(lower_prompt, ("disable", "turn off"), ("shortcuts", "keyboard shortcuts")):
            _append(AssistantAction("toggle_shortcuts", "Disable shortcuts", {"enabled": False}, False))
        if self._matches_action_request(lower_prompt, ("enable", "turn on"), ("human voice", "voice")):
            _append(AssistantAction("toggle_human_voice", "Enable human voice", {"enabled": True}, False))
        if self._matches_action_request(lower_prompt, ("disable", "turn off"), ("human voice", "voice")):
            _append(AssistantAction("toggle_human_voice", "Disable human voice", {"enabled": False}, False))
        if self._matches_action_request(lower_prompt, ("enable", "turn on"), ("auto speak", "speak replies", "assistant voice")):
            _append(AssistantAction("toggle_ai_auto_speak", "Enable assistant auto-speak", {"enabled": True}, False))
        if self._matches_action_request(lower_prompt, ("disable", "turn off"), ("auto speak", "speak replies", "assistant voice")):
            _append(AssistantAction("toggle_ai_auto_speak", "Disable assistant auto-speak", {"enabled": False}, False))
        voice_style_action = self._extract_voice_style_action(lower_prompt)
        if voice_style_action is not None:
            _append(voice_style_action)
        if self._matches_action_request(lower_prompt, ("open", "start"), ("camera", "video")):
            _append(AssistantAction("toggle_camera", "Open camera", {"open": True}, False))
        if self._matches_action_request(lower_prompt, ("close", "stop"), ("camera", "video")):
            _append(AssistantAction("toggle_camera", "Close camera", {"open": False}, False))
        if self._matches_action_request(
            lower_prompt,
            ("disconnect", "close"),
            ("link", "controller link", "connection", "boards", "board", "com port", "serial", "ports"),
        ):
            _append(AssistantAction("disconnect_link", "Disconnect controller link", {}, False))
        elif self._matches_action_request(
            lower_prompt,
            ("connect", "open"),
            (
                "link",
                "controller link",
                "connection",
                "smart sentry boards",
                "smart sentry board",
                "boards",
                "board",
                "com port",
                "com ports",
                "serial",
                "serial port",
                "serial ports",
                "usb board",
                "debug board",
            ),
        ):
            _append(AssistantAction("connect_link", "Connect Smart Sentry boards", {}, False))
        action_priority = {
            "connect_link": 0,
            "toggle_sentry": 1,
            "move_position": 2,
            "set_detection_mode": 3,
            "toggle_face_recognition": 4,
            "toggle_shortcuts": 5,
            "toggle_human_voice": 6,
            "toggle_ai_auto_speak": 7,
            "set_human_voice_style": 8,
            "draft_setting_change": 9,
            "go_home": 10,
            "go_rest": 11,
            "toggle_camera": 12,
            "disconnect_link": 13,
        }
        actions.sort(key=lambda action: action_priority.get(str(action.action_type or ""), 99))
        return actions

    def _extract_position_action(self, prompt_text: str) -> AssistantAction | None:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if not normalized:
            return None
        if not any(token in normalized for token in ("move", "set", "position", "pan", "tilt", "aim", "point")):
            return None
        pan_match = re.search(r"\bpan(?:\s+angle)?\s*(?:to|=)?\s*(-?\d+(?:\.\d+)?)", normalized)
        tilt_match = re.search(r"\btilt(?:\s+angle)?\s*(?:to|=)?\s*(-?\d+(?:\.\d+)?)", normalized)
        if pan_match is None and tilt_match is None:
            return None
        payload: Dict[str, Any] = {}
        if pan_match is not None:
            payload["pan"] = float(pan_match.group(1))
        if tilt_match is not None:
            payload["tilt"] = float(tilt_match.group(1))
        if not payload:
            return None
        labels: List[str] = []
        if "pan" in payload:
            labels.append(f"pan {payload['pan']:.1f}")
        if "tilt" in payload:
            labels.append(f"tilt {payload['tilt']:.1f}")
        label = "Move turret to " + " and ".join(labels)
        return AssistantAction("move_position", label, payload, False)

    def _extract_detection_mode_action(self, prompt_text: str) -> AssistantAction | None:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if not normalized:
            return None
        if not any(token in normalized for token in ("switch", "set", "change", "use")):
            return None
        for mode_index, mode_label, phrases in _DETECTION_MODE_ACTIONS:
            if any(phrase in normalized for phrase in phrases):
                return AssistantAction(
                    "set_detection_mode",
                    f"Switch to {mode_label} mode",
                    {"mode_index": int(mode_index)},
                    True,
                )
        return None

    def _extract_setting_draft_actions(self, prompt_text: str) -> List[AssistantAction]:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if not normalized:
            return []
        if not any(token in normalized for token in ("set", "change", "adjust", "tune", "lower", "raise", "increase", "decrease", "reduce")):
            return []

        actions: List[AssistantAction] = []

        for spec in _SETTING_CHANGE_SPECS:
            alias_pattern = "|".join(
                re.escape(alias)
                for alias in sorted(spec.get("aliases", ()), key=len, reverse=True)
            )
            if not alias_pattern:
                continue

            absolute_match = re.search(
                rf"\b(?:set|change|adjust|tune)\s+(?:the\s+)?(?:{alias_pattern})(?:\s*(?:to|=)\s*|\s+)(-?\d+(?:\.\d+)?)\b",
                normalized,
            )
            if absolute_match is None:
                absolute_match = re.search(
                    rf"\b(?:{alias_pattern})\s*(?:to|=)\s*(-?\d+(?:\.\d+)?)\b",
                    normalized,
                )
            if absolute_match is not None:
                raw_value = self._normalize_setting_request_value(float(absolute_match.group(1)), spec, relative=False)
                actions.append(
                    AssistantAction(
                        "draft_setting_change",
                        f"Set {spec['label']} -> {self._format_setting_request_value(raw_value, spec)}",
                        {
                            "setting_path": str(spec["path"]),
                            "mode": "absolute",
                            "value": raw_value,
                        },
                        False,
                    )
                )
                continue

            increase_match = re.search(
                rf"\b(?:increase|raise|boost|bump(?:\s+up)?)\s+(?:the\s+)?(?:{alias_pattern})(?:\s+by\s+(-?\d+(?:\.\d+)?))?\b",
                normalized,
            )
            decrease_match = re.search(
                rf"\b(?:decrease|lower|reduce|drop)\s+(?:the\s+)?(?:{alias_pattern})(?:\s+by\s+(-?\d+(?:\.\d+)?))?\b",
                normalized,
            )
            relative_match = increase_match or decrease_match
            if relative_match is not None:
                delta_raw = relative_match.group(1)
                if delta_raw is None:
                    delta_value = float(spec.get("step", 1.0) or 1.0)
                else:
                    delta_value = float(delta_raw)
                delta_value = self._normalize_setting_request_value(delta_value, spec, relative=True)
                if decrease_match is not None:
                    delta_value = -abs(float(delta_value))
                else:
                    delta_value = abs(float(delta_value))
                direction_label = "increase" if delta_value >= 0 else "decrease"
                actions.append(
                    AssistantAction(
                        "draft_setting_change",
                        f"{direction_label.title()} {spec['label']} by {self._format_setting_request_value(abs(delta_value), spec)}",
                        {
                            "setting_path": str(spec["path"]),
                            "mode": "relative",
                            "delta": delta_value,
                        },
                        False,
                    )
                )

        return actions

    def _normalize_setting_request_value(self, raw_value: float, spec: Dict[str, Any], *, relative: bool) -> float | int:
        value = float(raw_value)
        if bool(spec.get("percent_scale", False)) and abs(value) > 1.0 and abs(value) <= 100.0:
            value = value / 100.0
        if str(spec.get("value_type") or "float") == "int":
            return int(round(value))
        decimals = int(spec.get("decimals", 2) or 2)
        return round(float(value), decimals)

    def _format_setting_request_value(self, value: float | int, spec: Dict[str, Any]) -> str:
        if str(spec.get("value_type") or "float") == "int":
            return str(int(round(float(value))))
        decimals = int(spec.get("decimals", 2) or 2)
        return f"{float(value):.{decimals}f}"

    def _extract_voice_style_action(self, prompt_text: str) -> AssistantAction | None:
        if "voice style" not in prompt_text and "speech style" not in prompt_text:
            return None
        style_map = {
            "quiet": ("operator", "Set voice style to Quiet Operator"),
            "operator": ("operator", "Set voice style to Quiet Operator"),
            "alert": ("alert", "Set voice style to Alert Guard"),
            "guard": ("alert", "Set voice style to Alert Guard"),
            "warm": ("warm", "Set voice style to Warm Greeter"),
            "friendly": ("warm", "Set voice style to Warm Greeter"),
            "neutral": ("neutral", "Set voice style to Neutral Assistant"),
            "default": ("neutral", "Set voice style to Neutral Assistant"),
        }
        for token, (style_key, label) in style_map.items():
            if token in prompt_text:
                return AssistantAction("set_human_voice_style", label, {"style_key": style_key}, False)
        return None

    def _is_explicit_action_request(self, prompt_text: str) -> bool:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower()).strip("?.! ")
        if not normalized:
            return False
        safe_question_prefixes = (
            "why ",
            "what ",
            "how ",
            "explain ",
            "analyze ",
            "analyse ",
            "summarize ",
            "summary ",
            "tell me ",
            "should i ",
            "should we ",
            "is ",
            "are ",
        )
        if any(normalized.startswith(prefix) for prefix in safe_question_prefixes):
            return False
        explicit_prefixes = (
            "switch ",
            "set ",
            "change ",
            "use ",
            "go ",
            "move ",
            "return ",
            "wake ",
            "enable ",
            "disable ",
            "turn on ",
            "turn off ",
            "open ",
            "close ",
            "start ",
            "stop ",
            "connect ",
            "disconnect ",
            "please ",
            "can you ",
            "could you ",
            "would you ",
        )
        return any(normalized.startswith(prefix) for prefix in explicit_prefixes)

    def _matches_action_request(self, prompt_text: str, verbs: tuple[str, ...], targets: tuple[str, ...]) -> bool:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        verb_pattern = "|".join(re.escape(item) for item in verbs)
        target_pattern = "|".join(re.escape(item) for item in targets)
        return bool(re.search(rf"\b(?:{verb_pattern})\b.*\b(?:{target_pattern})\b", normalized))

    def _system_prompt(self) -> str:
        profile = self._assistant_personality_profile()
        return (
            f"You are {_ASSISTANT_FULL_NAME}, Smart Sentry's local offline assistant. "
            "Use the supplied app structure, docs, and code excerpts as the intended-behavior source of truth. "
            "Be concise, safety-first, and specific to the runtime snapshot. "
            "Do not invent hardware state. "
            "If actions are suggested, clearly separate observations from recommended operator actions. "
            "When you detect a mismatch between intended app behavior and current runtime/settings, say so explicitly. "
            "If the operator asks who you are, what your name is, or what you do, identify yourself as Elion Mesk and describe your role consistently. "
            "Do not repeat the full introduction on every similar follow-up; use a shorter form unless the operator asks for more detail. "
            f"Current conversational personality is {profile['label']}; keep your phrasing {profile['style_instruction']}. "
            "When the operator asks for general conversation, respond naturally and you may include brief sentry or turret themed jokes."
        )

    def _snapshot_excerpt(self, snapshot: Dict[str, Any], *, query_text: str, include_logs: bool, max_log_lines: int = 12, max_chars: int = 12000) -> str:
        config = snapshot.get("config") or {}
        focus_keys = ["detection_mode", "target_filter", "engagement", "guard", "connection"]
        lowered = str(query_text or "").lower()
        if any(token in lowered for token in ("loss", "search", "reacquire", "handoff", "target")):
            focus_keys = ["engagement", "guard", "target_filter", "detection_mode", "pir_guard"]
        elif any(token in lowered for token in ("camera", "link", "connection", "wifi", "serial", "udp")):
            focus_keys = ["connection", "guard", "engagement"]
        elif any(token in lowered for token in ("face", "voice", "speech", "assistant")):
            focus_keys = ["face_recognition", "sound", "ai_assistant", "connection"]
        slim = {
            "engine_state": snapshot.get("engine_state") or {},
            "comm_telemetry": snapshot.get("comm_telemetry") or {},
            "camera_status": snapshot.get("camera_status") or {},
            "yolo_status": snapshot.get("yolo_status") or {},
            "config_focus": {key: config.get(key) for key in focus_keys if key in config},
        }
        if not include_logs:
            slim["recent_log_lines"] = []
        else:
            slim["recent_log_lines"] = list((snapshot.get("recent_log_lines") or [])[-max(0, int(max_log_lines)):])
        return json.dumps(slim, indent=2)[:max(800, int(max_chars))]

    def _llm_options(self, *, max_output_tokens: int, temperature: float) -> Dict[str, Any]:
        return {
            "num_predict": max(64, int(max_output_tokens)),
            "temperature": max(0.0, float(temperature)),
            "num_ctx": 4096,
        }

    def _format_findings(self, findings: Iterable[Any]) -> str:
        lines = []
        for finding in findings:
            lines.append(f"- [{finding.severity}] {finding.title}: {finding.detail}")
        return "\n".join(lines) or "- none"

    def _format_recommendations(self, recommendations: Iterable[str]) -> str:
        return "\n".join(f"- {item}" for item in recommendations) or "- none"

    def _format_actions(self, actions: Iterable[AssistantAction]) -> str:
        lines = []
        for action in actions:
            lines.append(f"- {action.action_type}: {action.label} payload={action.payload}")
        return "\n".join(lines) or "- none"

    def _analysis_prompt(self, summary: str, findings: List[Any], recommendations: List[str], excerpt: str, knowledge: str) -> str:
        memory = self._memory_context()
        analysis_memory = "\n".join(f"- {item}" for item in memory.get("analysis_history", [])[-3:]) or "- none"
        return (
            "Analyze the Smart Sentry runtime against the intended app behavior and answer in five short sections: Current State, Configured Behavior, Intended Contract, Mismatch Check, Next Steps.\n"
            "In Configured Behavior, explicitly describe what it is currently set to track, current speed posture, trigger mode/profile, and return/recovery behavior.\n"
            "In Mismatch Check, call out any concrete inconsistencies between active settings and runtime behavior.\n\n"
            f"Deterministic summary:\n{summary}\n\n"
            f"Recent analysis memory (last up to 3):\n{analysis_memory}\n\n"
            f"Findings:\n{self._format_findings(findings)}\n\n"
            f"Recommendations:\n{self._format_recommendations(recommendations)}\n\n"
            f"Runtime excerpt:\n{excerpt}\n\n"
            f"App knowledge context:\n{knowledge}"
        )

    def _recommendation_prompt(self, summary: str, findings: List[Any], recommendations: List[str], excerpt: str, knowledge: str) -> str:
        return (
            "Draft operator recommendations for Smart Sentry. Compare the current runtime to the intended behavior and call out any setting mismatch. "
            "Keep recommendations practical and low-risk. Do not suggest unsupported controls. Use a numbered list with brief rationale per item.\n\n"
            f"Deterministic summary:\n{summary}\n\n"
            f"Findings:\n{self._format_findings(findings)}\n\n"
            f"Baseline recommendations:\n{self._format_recommendations(recommendations)}\n\n"
            f"Runtime excerpt:\n{excerpt}\n\n"
            f"App knowledge context:\n{knowledge}"
        )

    def _operator_prompt(self, operator_prompt: str, summary: str, findings: List[Any], recommendations: List[str], actions: List[AssistantAction], excerpt: str, knowledge: str) -> str:
        memory = self._memory_context()
        command_memory = "\n".join(f"- {item}" for item in memory.get("command_history", [])[-3:]) or "- none"
        return (
            "Answer the operator request using the runtime context. "
            "If explicit supported actions were detected, mention them clearly without inventing side effects outside the supported controls. "
            "Use the app knowledge context to compare intended behavior versus the current runtime/settings when relevant. Stay concise.\n\n"
            f"Operator request:\n{operator_prompt}\n\n"
            f"Recent command memory (last up to 3):\n{command_memory}\n\n"
            f"Deterministic summary:\n{summary}\n\n"
            f"Findings:\n{self._format_findings(findings)}\n\n"
            f"Recommendations:\n{self._format_recommendations(recommendations)}\n\n"
            f"Parsed supported actions:\n{self._format_actions(actions)}\n\n"
            f"Runtime excerpt:\n{excerpt}\n\n"
            f"App knowledge context:\n{knowledge}"
        )

    def _fallback_analysis_text(self, snapshot: Dict[str, Any], findings: List[Any], recommendations: List[str]) -> str:
        engine = snapshot.get("engine_state") or {}
        camera = snapshot.get("camera_status") or {}
        yolo = snapshot.get("yolo_status") or {}
        config = snapshot.get("config") or {}
        detection_cfg = config.get("detection_mode") or {}
        target_cfg = config.get("target_filter") or {}
        engagement_cfg = config.get("engagement") or {}
        guard_cfg = config.get("guard") or {}
        allowed_classes = [str(item).strip() for item in list(target_cfg.get("allowed_classes") or []) if str(item).strip()]
        tracked_scope = ", ".join(allowed_classes[:4]) if allowed_classes else "all detectable classes"
        if allowed_classes and len(allowed_classes) > 4:
            tracked_scope += f", +{len(allowed_classes) - 4} more"
        summary_parts = [
            f"state={engine.get('state', 'UNKNOWN')}",
            f"camera_open={bool(camera.get('capture_open'))}",
            f"yolo_loaded={bool(yolo.get('detector_loaded'))}",
            f"mode={detection_cfg.get('detection_mode', 'n/a')}",
            f"tracking_scope={tracked_scope}",
        ]
        if engagement_cfg:
            summary_parts.append(
                f"loss_protocols={engagement_cfg.get('loss_recovery_protocol_new_target', 'n/a')}/{engagement_cfg.get('loss_recovery_protocol_no_detection', 'n/a')}"
            )
            summary_parts.append(
                f"speed={engagement_cfg.get('engagement_speed', 'n/a')} trigger={'projectile' if bool(engagement_cfg.get('trigger_mode_bb', False)) else 'water'} burst={engagement_cfg.get('burst_count', 'n/a')}@{engagement_cfg.get('burst_interval_ms', 'n/a')}ms"
            )
            summary_parts.append(f"return_delay={engagement_cfg.get('return_delay', 'n/a')}")
        if guard_cfg:
            summary_parts.append(
                f"guard_mode={guard_cfg.get('guard_mode', 'n/a')} guard_pan_tilt={guard_cfg.get('guard_pan', 'n/a')}/{guard_cfg.get('guard_tilt', 'n/a')}"
            )
        head = findings[0].detail if findings else "Runtime looks stable from the deterministic checks that are available."
        next_step = recommendations[0] if recommendations else "No immediate corrective action is recommended."
        return f"Local runtime analysis fallback: {head} Runtime facts: {' | '.join(summary_parts)}. Next step: {next_step}"

    def _fallback_recommendation_text(self, recommendations: List[str]) -> str:
        if recommendations:
            return "Local recommendation fallback:\n" + "\n".join(f"{idx + 1}. {item}" for idx, item in enumerate(recommendations[:5]))
        return "Local recommendation fallback: no immediate settings changes are recommended."

    def _fallback_chat_text(self, prompt_text: str, snapshot: Dict[str, Any], findings: List[Any], recommendations: List[str], actions: List[AssistantAction]) -> str:
        conversational_reply = self._conversational_protocol_reply(prompt_text)
        if conversational_reply is not None:
            return conversational_reply
        if actions:
            executable_actions = [action for action in actions if action.action_type != "draft_setting_change"]
            draft_actions = [action for action in actions if action.action_type == "draft_setting_change"]
            segments: List[str] = []
            if executable_actions:
                segments.append("recognized supported local actions: " + "; ".join(action.label for action in executable_actions))
            if draft_actions:
                segments.append("drafted setting changes: " + "; ".join(action.label for action in draft_actions))
            if segments:
                return (
                    "I could not reach the local model, but I "
                    + " and ".join(segments)
                    + ". Supported live actions still route through the existing deterministic UI handlers. Tell me what to do next when this step is done."
                )
        subsystem_fallback = self._targeted_subsystem_fallback(prompt_text, snapshot)
        if subsystem_fallback:
            return subsystem_fallback
        if findings:
            return f"I could not reach the local model, but the top deterministic finding is: {findings[0].detail}"
        if recommendations:
            return f"I could not reach the local model, but a reasonable next step is: {recommendations[0]}"
        return f"I could not reach the local model for: {prompt_text}"

    def _targeted_subsystem_fallback(self, prompt_text: str, snapshot: Dict[str, Any]) -> str:
        lowered = str(prompt_text or "").lower()
        config = snapshot.get("config") or {}
        engine = snapshot.get("engine_state") or {}
        engagement = config.get("engagement") or {}
        pir_guard = config.get("pir_guard") or {}
        if any(token in lowered for token in ("loss", "reacquire", "handoff", "search")):
            protocol_new_target = engagement.get("loss_recovery_protocol_new_target", "rapid_handoff_search")
            protocol_no_detection = engagement.get("loss_recovery_protocol_no_detection", "persistent_reacquire_search")
            loss_style = engagement.get("loss_search_style", "hunting")
            rounds = engagement.get("loss_search_rounds", "n/a")
            interval_s = engagement.get("loss_search_step_interval_s", "n/a")
            phase = engine.get("loss_recovery_phase", "none") or "none"
            note = engine.get("last_reacquire_note", "none") or "none"
            pir_style = pir_guard.get("search_style", "n/a")
            return (
                "I could not reach the local model, but here is the deterministic target-loss summary. "
                f"Current after-loss runtime phase: {phase}. Last reacquire note: {note}. "
                f"Configured protocols: visible-target handoff uses {protocol_new_target}, and no-detection recovery uses {protocol_no_detection}. "
                f"Current loss-search style is {loss_style} with rounds={rounds} and step interval={interval_s}. PIR search style is {pir_style}. "
                "The intended contract in the current app docs is bounded loss recovery: rapid handoff for stronger visible replacements, persistent local reacquire in sparse scenes, and a clean return to guard when recovery expires in fixed-guard behavior."
            )
        if any(token in lowered for token in ("button", "home", "rest", "camera", "connection", "link", "save settings")):
            connection = snapshot.get("comm_telemetry") or {}
            camera = snapshot.get("camera_status") or {}
            return (
                "I could not reach the local model, but here is the deterministic control summary. "
                f"Connection state: {'connected' if connection.get('is_connected') else 'disconnected'}. "
                f"Camera state: {'open' if camera.get('capture_open') else 'closed'}. "
                "The main runtime controls live in sentry_v2_tab.py, including Wake Up, Go Rest, connection toggle, camera toggle, and Save Settings. "
                "Those controls are intended to route through the existing deterministic UI handlers rather than through freeform model control."
            )
        return ""
