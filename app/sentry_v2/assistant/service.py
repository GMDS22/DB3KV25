from __future__ import annotations

import json
import re
from typing import Any, Dict, Iterable, List

from .app_knowledge import AppKnowledgeBase
from .models import AssistantAction, AssistantReply
from .ollama_client import OllamaClient
from .runtime_analyzer import RuntimeAnalyzer


class LocalAssistantService:
    def __init__(self, client: OllamaClient | None = None, analyzer: RuntimeAnalyzer | None = None, knowledge_base: AppKnowledgeBase | None = None):
        self._client = client or OllamaClient()
        self._analyzer = analyzer or RuntimeAnalyzer()
        self._knowledge = knowledge_base or AppKnowledgeBase()

    def is_available(self) -> bool:
        return self._client.is_available()

    def list_models(self) -> List[str]:
        return self._client.list_models()

    def analyze_runtime(self, snapshot: Dict[str, Any], *, model: str, include_logs: bool = True) -> AssistantReply:
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
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
                timeout_s=min(float(self._client.timeout_s), 28.0),
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
                error=str(exc),
            )

    def recommend_settings(self, snapshot: Dict[str, Any], *, model: str, include_logs: bool = False) -> AssistantReply:
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
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
                timeout_s=min(float(self._client.timeout_s), 34.0),
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
                error=str(exc),
            )

    def answer_operator_prompt(self, prompt_text: str, snapshot: Dict[str, Any], *, model: str, include_logs: bool = True) -> AssistantReply:
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
        actions = self._parse_actions(prompt_text)
        excerpt = self._snapshot_excerpt(snapshot, query_text=prompt_text, include_logs=include_logs, max_log_lines=6, max_chars=3600)
        knowledge = self._knowledge.context_for_query(prompt_text, snapshot, task_kind="prompt", max_chars=4200)
        prompt = self._operator_prompt(prompt_text, summary, findings, recommendations, actions, excerpt, knowledge)
        try:
            reply_text = self._client.generate(
                model=model,
                prompt=prompt,
                system=self._system_prompt(),
                timeout_s=min(float(self._client.timeout_s), 30.0),
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
                error=str(exc),
            )

    def _parse_actions(self, prompt_text: str) -> List[AssistantAction]:
        lower_prompt = str(prompt_text or "").lower()
        if not self._is_explicit_action_request(lower_prompt):
            return []
        actions: List[AssistantAction] = []
        seen: set[str] = set()

        def _append(action: AssistantAction) -> None:
            if action.action_type not in seen:
                seen.add(action.action_type)
                actions.append(action)

        if self._matches_action_request(lower_prompt, ("wake", "return", "go", "move"), ("home", "guard home", "home position")):
            _append(AssistantAction("go_home", "Move to guard home position", requires_permission=False))
        if self._matches_action_request(lower_prompt, ("rest", "go", "move", "return"), ("rest", "rest position")):
            _append(AssistantAction("go_rest", "Move to rest position", requires_permission=False))
        position_action = self._extract_position_action(prompt_text)
        if position_action is not None:
            _append(position_action)
        if self._matches_action_request(lower_prompt, ("switch", "set", "change", "use"), ("color detection", "color mode", "color tracking")):
            _append(AssistantAction("set_detection_mode", "Switch to Color Detection mode", {"mode_index": 6}, True))
        if self._matches_action_request(lower_prompt, ("switch", "set", "change", "use"), ("yolo", "yolo mode", "object detection")):
            _append(AssistantAction("set_detection_mode", "Switch to YOLO Object Detection mode", {"mode_index": 2}, True))
        if self._matches_action_request(lower_prompt, ("switch", "set", "change", "use"), ("motion mode", "frame difference mode", "motion detection")):
            _append(AssistantAction("set_detection_mode", "Switch to Motion mode", {"mode_index": 0}, True))
        if self._matches_action_request(lower_prompt, ("switch", "set", "change", "use"), ("filtered target", "motion-locked", "motion locked")):
            _append(AssistantAction("set_detection_mode", "Switch to Motion-Locked Filtered Target mode", {"mode_index": 10}, True))
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
        if self._matches_action_request(lower_prompt, ("disconnect", "close"), ("link", "controller link", "connection")):
            _append(AssistantAction("disconnect_link", "Disconnect controller link", {}, False))
        elif self._matches_action_request(lower_prompt, ("connect", "open"), ("link", "controller link", "connection")):
            _append(AssistantAction("connect_link", "Connect controller link", {}, False))
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
        return (
            "You are Smart Sentry's local offline assistant. "
            "Use the supplied app structure, docs, and code excerpts as the intended-behavior source of truth. "
            "Be concise, safety-first, and specific to the runtime snapshot. "
            "Do not invent hardware state. "
            "If actions are suggested, clearly separate observations from recommended operator actions. "
            "When you detect a mismatch between intended app behavior and current runtime/settings, say so explicitly."
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
        return (
            "Analyze the Smart Sentry runtime against the intended app behavior and answer in four short sections: Current State, Intended Contract, Mismatch Check, Next Steps.\n\n"
            f"Deterministic summary:\n{summary}\n\n"
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
        return (
            "Answer the operator request using the runtime context. "
            "If explicit supported actions were detected, mention them clearly as pending/available actions rather than pretending they already happened. "
            "Use the app knowledge context to compare intended behavior versus the current runtime/settings when relevant. Stay concise.\n\n"
            f"Operator request:\n{operator_prompt}\n\n"
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
        engagement_cfg = config.get("engagement") or {}
        summary_parts = [
            f"state={engine.get('state', 'UNKNOWN')}",
            f"camera_open={bool(camera.get('capture_open'))}",
            f"yolo_loaded={bool(yolo.get('detector_loaded'))}",
            f"mode={detection_cfg.get('detection_mode', 'n/a')}",
        ]
        if engagement_cfg:
            summary_parts.append(
                f"loss_protocols={engagement_cfg.get('loss_recovery_protocol_new_target', 'n/a')}/{engagement_cfg.get('loss_recovery_protocol_no_detection', 'n/a')}"
            )
        head = findings[0].detail if findings else "Runtime looks stable from the deterministic checks that are available."
        next_step = recommendations[0] if recommendations else "No immediate corrective action is recommended."
        return f"Local runtime analysis fallback: {head} Runtime facts: {' | '.join(summary_parts)}. Next step: {next_step}"

    def _fallback_recommendation_text(self, recommendations: List[str]) -> str:
        if recommendations:
            return "Local recommendation fallback:\n" + "\n".join(f"{idx + 1}. {item}" for idx, item in enumerate(recommendations[:5]))
        return "Local recommendation fallback: no immediate settings changes are recommended."

    def _fallback_chat_text(self, prompt_text: str, snapshot: Dict[str, Any], findings: List[Any], recommendations: List[str], actions: List[AssistantAction]) -> str:
        if actions:
            action_text = "; ".join(action.label for action in actions)
            return f"I recognized supported local actions related to your request: {action_text}. The local model was unavailable, so I am returning the deterministic action parse and local execution path instead."
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
