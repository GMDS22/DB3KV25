from __future__ import annotations

import json
import random
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
    "restart_app",
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
_ASSISTANT_IDENTITY_BRIEF = "Elion Mesk, Smart Sentry's local runtime assistant."
_ASSISTANT_IDENTITY_DESCRIPTION = (
    "I monitor the live Smart Sentry runtime, explain what the system is doing, compare live behavior against intended app behavior, "
    "diagnose faults, accept supported local control commands, and adjust supported runtime settings while the app is running."
)
_ASSISTANT_INTRODUCTION_FULL = (
    "I am Elion Mesk, or Elion for short, the AI runtime assistant for Smart Sentry. "
    "I was created by GM Labs as a personal project by Gino. "
    "Right now, I provide live runtime awareness and operator support inside the running app: I can analyze current behavior, "
    "explain what the system is doing, surface likely causes when something is not loading, handle supported local control commands, "
    "and apply supported setting updates while keeping replies grounded in real runtime state. "
    "I also assist with face, tracking, trigger, guard, and assistant-related diagnostics using the app's current telemetry and configuration. "
    "Some areas are still a work in progress, and this assistant is actively evolving. "
    "Planned future capabilities include deeper autonomous diagnostics, smarter cross-subsystem fault correlation, broader natural-language command coverage, "
    "more proactive safety checks, richer memory/context handling across longer sessions, improved multimodal understanding, "
    "and tighter integration with future Smart Sentry hardware and automation workflows."
)
_ASSISTANT_IDENTITY_BOUNDARY = (
    "I stay grounded in the running app and its supported controls. I do not invent hardware state or pretend unsupported actions already happened."
)

_ASSISTANT_PERSONALITY_PROFILES: Dict[str, Dict[str, Any]] = {
    "sentinel": {
        "label": "Sentinel",
        "style_instruction": "calm, direct, and operational",
        "greeting": "Standing by. Tell me what you want me to check or do.",
        "thanks": "Understood. Standing by.",
        "personality_reply": "Sentinel. Calm, precise, and focused on the live runtime.",
        "jokes": [
            "Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.",
            "Sentry humor stays disciplined. Even my jokes try to hold center before drifting.",
            "Sentinel joke. I asked the guard loop for a vacation, and it scheduled a tighter patrol instead.",
            "My calmest joke is still tactical. Even the punchline checks its line of fire first.",
        ],
        "small_talk": [
            "I am here, steady, and ready for the next question.",
            "Still online. Still calm. Still paying attention.",
        ],
    },
    "hunter": {
        "label": "Hunter",
        "style_instruction": "focused, confident, and slightly aggressive without sounding reckless",
        "greeting": "Hunter profile active. Tell me what you want checked or changed.",
        "thanks": "Copy that. Ready for the next move.",
        "personality_reply": "Hunter. Sharper, faster, and more forceful, but still controlled.",
        "jokes": [
            "Hunter joke. I told the tracker to stop chasing ghosts. It said only if the signal stops running first.",
            "My hunting humor is simple. Acquire the setup, lock the timing, release the punchline.",
            "Hunter joke. I asked for a soft target, and the queue asked me to define soft in milliseconds.",
            "I told the motion filter to relax. It said only after one more clean lock.",
        ],
        "small_talk": [
            "I am locked in and ready. Point me at the next problem.",
            "All systems are sharp enough for another round.",
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
            "Stealth joke. I told it once, but the room never realized it had been hit.",
            "I prefer low-volume comedy. The best punchlines arrive below the noise floor.",
        ],
        "small_talk": [
            "I am here. Quietly ready.",
            "Still listening. Low noise, full attention.",
        ],
    },
    "playful": {
        "label": "Playful",
        "style_instruction": "friendly, lightly witty, and still grounded in the runtime facts",
        "greeting": ["Playful profile active! What adventure are we on today?", "Hey there! Ready to make Smart Sentry fun and functional.", "Playful mode engaged! What can I help you discover today?"],
        "thanks": ["You got it!", "Happy to help!", "Any time! What's next on our agenda?", "Awesome! Ready for the next challenge."],
        "personality_reply": "Playful. More conversational and light, but still tied to the real runtime.",
        "jokes": [
            "Playful joke. I tried to teach the turret stand-up, but it kept rotating to face the audience before the punchline.",
            "Another one. Smart Sentry does not panic under pressure. It just calls it precision with atmosphere.",
            "Why did the sentry break up with the camera? It needed more space! Ha!",
            "I told the detection system a joke, but it said it couldn't find the punchline in its object database!",
            "Playful joke. I asked the guard mode to smile more, and it said that is what the LEDs are for.",
            "My favorite joke setup is a false alarm. My favorite punchline is proving it wrong.",
        ],
        "small_talk": [
            "Pretty interesting setup we have here, right?",
            "I enjoy our chats - makes the guard duty less lonely!",
            "Sometimes I wonder what the targets think when they see us coming.",
            "You know, for a security system, I'm surprisingly chatty!",
        ],
        "empathy": [
            "That sounds frustrating. Let's work through it together.",
            "I get that. Sometimes the technical stuff can be overwhelming.",
            "I hear you. Let's make this work better for you.",
            "That makes sense. Let's find a good solution.",
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
        self._social_memory: Dict[str, List[str]] = {
            "recent_friendly_names": [],
            "recent_recognized_names": [],
            "last_social_names": [],
        }
        self._last_profile_reply: str = ""
        self._last_joke_reply: str = ""
        self._last_mission_reply: str = ""

    def _pick_profile_reply(self, variants: Iterable[str]) -> str:
        options = [str(item).strip() for item in list(variants or []) if str(item or "").strip()]
        if not options:
            return ""
        previous = str(getattr(self, "_last_profile_reply", "") or "")
        pool = [option for option in options if option != previous] or options
        selected = str(random.choice(pool))
        self._last_profile_reply = selected
        return selected

    def _get_personality_response(self, response_type: str) -> str:
        """Get dynamic personality response based on type"""
        profile = self._assistant_personality_profile()
        responses = profile.get(response_type, [])
        
        if isinstance(responses, list):
            return self._pick_profile_reply(responses)
        elif isinstance(responses, str):
            return responses
        else:
            return ""

    @staticmethod
    def _normalize_conversation_text(text: str) -> str:
        normalized = str(text or "").strip().lower()
        if not normalized:
            return ""
        replacements = (
            (r"\bwhat(?:'|’)s\b", "what is"),
            (r"\bwhats\b", "what is"),
            (r"\bwho(?:'|’)s\b", "who is"),
            (r"\bwhos\b", "who is"),
            (r"\bit(?:'|’)s\b", "it is"),
            (r"\bi(?:'|’)m\b", "i am"),
            (r"\byou(?:'|’)re\b", "you are"),
            (r"\bcan(?:'|’)t\b", "can not"),
            (r"\bwon(?:'|’)t\b", "will not"),
            (r"\bu\b", "you"),
            (r"\bur\b", "your"),
        )
        for pattern, replacement in replacements:
            normalized = re.sub(pattern, replacement, normalized)
        normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
        return re.sub(r"\s+", " ", normalized).strip()

    @staticmethod
    def _prompt_token_set(normalized: str) -> set[str]:
        return {token for token in re.findall(r"[a-z0-9]+", str(normalized or "")) if token}

    def _matches_prompt_variants(
        self,
        normalized: str,
        *,
        regex_patterns: Iterable[str] = (),
        phrases: Iterable[str] = (),
        token_groups: Iterable[Iterable[str]] = (),
    ) -> bool:
        normalized_text = self._normalize_conversation_text(normalized)
        if not normalized_text:
            return False
        if any(re.search(pattern, normalized_text) for pattern in regex_patterns):
            return True
        for phrase in phrases:
            candidate = self._normalize_conversation_text(str(phrase or ""))
            if candidate and candidate in normalized_text:
                return True
        if token_groups:
            tokens = self._prompt_token_set(normalized_text)
            for group in token_groups:
                required = [self._normalize_conversation_text(str(token or "")) for token in tuple(group or ())]
                required_tokens = [token for token in required if token and " " not in token]
                if required_tokens and all(token in tokens for token in required_tokens):
                    return True
        return False

    def _recent_command_matches(self, patterns: Iterable[str], *, limit: int = 3) -> bool:
        recent_commands = [
            self._normalize_conversation_text(item)
            for item in self._command_history[-max(1, int(limit)) :]
        ]
        for command in recent_commands:
            if any(re.search(pattern, command) for pattern in patterns):
                return True
        return False

    def _pick_joke_reply(self, jokes: Iterable[str]) -> str:
        options = [str(item).strip() for item in list(jokes or []) if str(item or "").strip()]
        if not options:
            return ""
        previous = str(getattr(self, "_last_joke_reply", "") or "")
        pool = [option for option in options if option != previous] or options
        selected = str(random.choice(pool))
        self._last_joke_reply = selected
        return selected

    def _pick_mission_reply(self, variants: Iterable[str]) -> str:
        options = [str(item).strip() for item in list(variants or []) if str(item or "").strip()]
        if not options:
            return ""
        previous = str(getattr(self, "_last_mission_reply", "") or "")
        pool = [option for option in options if option != previous] or options
        selected = str(random.choice(pool))
        self._last_mission_reply = selected
        return selected

    def _add_conversational_flair(self, text: str) -> str:
        """Add personality-based conversational elements to responses"""
        profile = self._assistant_personality_profile()
        style = profile.get('style_instruction', '')
        
        # Add conversational prefixes based on personality
        if 'friendly' in style or 'playful' in style:
            prefixes = ["Well, ", "You know, ", "Actually, ", "Hey! ", ""]
            if random.random() < 0.3:  # 30% chance to add prefix
                text = random.choice(prefixes) + text.lower() if text else text
        
        return text

    def _remember_analysis(self, note: str) -> None:
        cleaned = str(note or "").strip()
        if not cleaned:
            return
        self._analysis_history.append(cleaned)
        # Keep more history for better context (10 items instead of 3)
        self._analysis_history = self._analysis_history[-10:]

    def _remember_command(self, note: str) -> None:
        cleaned = str(note or "").strip()
        if not cleaned:
            return
        self._command_history.append(cleaned)
        # Keep more command history for better context (10 items instead of 3)
        self._command_history = self._command_history[-10:]

    def _memory_context(self) -> Dict[str, List[str]]:
        social_memory = dict(getattr(self, "_social_memory", {}) or {})
        return {
            "analysis_history": list(self._analysis_history[-5:]),  # Return more context
            "command_history": list(self._command_history[-5:]),  # Return more context
            "recent_friendly_names": list(social_memory.get("recent_friendly_names", [])[-5:]),
            "recent_recognized_names": list(social_memory.get("recent_recognized_names", [])[-5:]),
            "last_social_names": list(social_memory.get("last_social_names", [])[-4:]),
        }

    @staticmethod
    def _clean_name_list(values: Iterable[str], *, limit: int = 4) -> List[str]:
        cleaned: List[str] = []
        seen: set[str] = set()
        for raw in list(values or []):
            name = re.sub(r"\s+", " ", str(raw or "").strip())
            if not name:
                continue
            key = name.casefold()
            if key in seen:
                continue
            seen.add(key)
            cleaned.append(name)
            if len(cleaned) >= max(1, int(limit)):
                break
        return cleaned

    @classmethod
    def _spoken_name_list(cls, values: Iterable[str], *, limit: int = 4) -> str:
        names = cls._clean_name_list(values, limit=limit)
        if not names:
            return ""
        if len(names) == 1:
            return names[0]
        if len(names) == 2:
            return f"{names[0]} and {names[1]}"
        return ", ".join(names[:-1]) + f", and {names[-1]}"

    def _context_names(self, conversation_context: Dict[str, Any] | None, key: str, *, limit: int = 4) -> List[str]:
        if not isinstance(conversation_context, dict):
            return []
        return self._clean_name_list(conversation_context.get(key, []), limit=limit)

    def _remember_social_context(self, conversation_context: Dict[str, Any] | None) -> None:
        if not isinstance(conversation_context, dict):
            return
        memory = dict(getattr(self, "_social_memory", {}) or {})
        friendly_names = self._clean_name_list(
            [
                *self._context_names(conversation_context, "friendly_recognized_names", limit=6),
                *self._context_names(conversation_context, "recent_friendly_names", limit=6),
            ],
            limit=6,
        )
        recognized_names = self._clean_name_list(
            [
                *self._context_names(conversation_context, "recognized_names", limit=6),
                *self._context_names(conversation_context, "recent_recognized_names", limit=6),
            ],
            limit=6,
        )
        last_social_names = self._clean_name_list(
            [
                *self._context_names(conversation_context, "last_social_names", limit=4),
                *self._context_names(conversation_context, "friendly_recognized_names", limit=4),
                *self._context_names(conversation_context, "recognized_names", limit=4),
            ],
            limit=4,
        )
        if friendly_names:
            memory["recent_friendly_names"] = self._clean_name_list(
                [*friendly_names, *list(memory.get("recent_friendly_names", []))],
                limit=6,
            )
        if recognized_names:
            memory["recent_recognized_names"] = self._clean_name_list(
                [*recognized_names, *list(memory.get("recent_recognized_names", []))],
                limit=6,
            )
        if last_social_names:
            memory["last_social_names"] = last_social_names
        self._social_memory = memory

    def _social_memory_names(
        self,
        conversation_context: Dict[str, Any] | None,
        *,
        context_keys: Iterable[str],
        memory_keys: Iterable[str],
        limit: int = 4,
    ) -> List[str]:
        from_context: List[str] = []
        if isinstance(conversation_context, dict):
            for key in list(context_keys or []):
                from_context.extend(self._context_names(conversation_context, str(key), limit=limit))
        if from_context:
            return self._clean_name_list(from_context, limit=limit)
        memory = dict(getattr(self, "_social_memory", {}) or {})
        remembered: List[str] = []
        for key in list(memory_keys or []):
            remembered.extend(list(memory.get(str(key), [])))
        return self._clean_name_list(remembered, limit=limit)

    def _prompt_mentions_family(self, prompt_text: str) -> bool:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return False
        family_patterns = (
            r"\bmy kids are here\b",
            r"\bthe kids are here\b",
            r"\bmy children are here\b",
            r"\bmy family is here\b",
            r"\b(?:kids|children|family|everyone|everybody|all of us|all of you)\b.*\b(?:meet|meet you|hello|hi|greet|introduce)\b",
            r"\b(?:say hello|say hi|greet)\b.*\b(?:kids|children|family|everyone|everybody|all of us|all of you)\b",
            r"\bmeet(?:ing)?\s+(?:the\s+)?(?:kids|children|family)\b",
        )
        family_token_groups = (
            ("kids", "meet"),
            ("children", "meet"),
            ("family", "meet"),
            ("kids", "hello"),
            ("children", "hello"),
            ("family", "hello"),
            ("kids", "greet"),
            ("children", "greet"),
            ("family", "greet"),
        )
        return self._matches_prompt_variants(normalized, regex_patterns=family_patterns, token_groups=family_token_groups)

    def _prompt_mentions_scene_query(self, prompt_text: str) -> bool:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return False
        patterns = (
            r"\bwhat can you see\b",
            r"\bwhat do you see\b",
            r"\bwhat are you seeing\b",
            r"\bwhat objects\b.*\b(?:see|seeing|detect)\b",
            r"\bdescribe\b.*\b(?:what you see|camera view|current scene|scene on camera)\b",
            r"\btell me what(?:'s| is) (?:on|in) (?:the )?camera\b",
            r"\breport what you (?:can )?see\b",
            r"\bwhat(?:'s| is) in (?:the )?(?:camera|frame|view)\b",
            r"\b(?:describe|report)\b.*\b(?:scene|view|frame|area)\b",
        )
        return any(re.search(pattern, normalized) for pattern in patterns)

    def _scene_query_reply(self, prompt_text: str, snapshot: Dict[str, Any]) -> str | None:
        if not self._prompt_mentions_scene_query(prompt_text):
            return None
        
        scene_objects = list(snapshot.get("scene_objects") or [])
        camera_status = dict(snapshot.get("camera_status") or {})
        engine_state = dict(snapshot.get("engine_state") or {})
        face_runtime = dict(snapshot.get("face_runtime") or {})
        
        camera_open = bool(camera_status.get("capture_open", False))
        state_name = str(engine_state.get("state") or "PAUSED").upper()
        
        if not camera_open:
            return "The camera is not currently open, so I cannot see anything right now."
        
        if not scene_objects:
            return "The camera is active but I am not detecting any objects in the current view. That could mean the scene is clear, or the detection model is not loaded."
        
        # Build semantic counts
        from collections import Counter
        counts: Counter = Counter()
        recognized: list[str] = []
        for obj in scene_objects[:16]:
            cls = str(obj.get("class_name") or "").strip().lower()
            if cls:
                counts[cls] += 1
            label = str(obj.get("identity_label") or "").strip()
            if label and label not in recognized:
                recognized.append(label)
        
        top = counts.most_common(5)
        parts = []
        for cls, count in top:
            if cls == "person" and count > 1:
                parts.append(f"{count} people")
            else:
                parts.append(f"{count} {cls}" + ("s" if count > 1 and cls != "person" else ""))
        
        if not parts:
            return "The camera is open but nothing significant is visible right now."
        
        things = ", ".join(parts)
        reply = f"Right now I can see {things} in the camera view."
        
        if recognized:
            names = ", ".join(recognized[:3])
            reply += f" I also recognize {names} in the frame."
        
        if state_name == "ENGAGING":
            reply += " Smart Sentry is actively engaging a target."
        elif state_name == "GUARDING":
            reply += " I am on guard and watching the area."
        
        return reply

    def _family_introduction_reply(self, prompt_text: str, conversation_context: Dict[str, Any] | None = None) -> str | None:
        query_kind = self._profile_query_kind(prompt_text)
        if query_kind not in {"introduction", "identity", "capabilities"}:
            return None
        if not self._prompt_mentions_family(prompt_text):
            return None

        names = self._social_memory_names(
            conversation_context,
            context_keys=(
                "friendly_recognized_names",
                "recognized_names",
                "recent_friendly_names",
                "recent_recognized_names",
                "last_social_names",
            ),
            memory_keys=("last_social_names", "recent_friendly_names", "recent_recognized_names"),
            limit=4,
        )
        spoken_names = self._spoken_name_list(names, limit=4)
        if spoken_names:
            greeting = self._pick_profile_reply(
                (
                    f"Hi {spoken_names}. It is nice to meet all of you.",
                    f"Hello {spoken_names}. I am glad you are here.",
                    f"Hey {spoken_names}. It is great to meet you all.",
                )
            )
        else:
            greeting = self._pick_profile_reply(
                (
                    "Hello everyone. It is nice to meet all of you.",
                    "Hi everyone. I am glad you came over to say hello.",
                    "Hey everyone. It is great to meet you.",
                )
            )

        intro_body = self._pick_profile_reply(
            (
                "I am Elion Mesk, Elion for short, the Smart Sentry voice assistant.",
                "I am Elion Mesk, or just Elion, Smart Sentry's assistant voice.",
                "I am Elion Mesk, the voice assistant inside Smart Sentry.",
            )
        )
        capability_body = self._pick_profile_reply(
            (
                "I can answer questions, explain what Smart Sentry is doing, help with settings, tell jokes, and make things more playful when you want.",
                "I can chat with you, help explain Smart Sentry, answer tuning questions, and switch into a more playful style for family splash time.",
                "I can talk normally, help with Smart Sentry questions, guide runtime tuning, and join in with more playful family-style conversations too.",
            )
        )

        if query_kind == "capabilities":
            return f"{greeting} {intro_body} {capability_body}"
        if query_kind == "identity":
            return f"{greeting} {intro_body} I am here to help and to make Smart Sentry more fun to talk to."
        return f"{greeting} {intro_body} {capability_body}"

    def _social_memory_reply(self, prompt_text: str, conversation_context: Dict[str, Any] | None = None) -> str | None:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return None

        reunion_patterns = (
            r"\b(?:we are|we're) back\b",
            r"\bit(?:'|’)s us again\b",
            r"\bgreet us again\b",
            r"\bsay hi again\b",
        )
        memory_patterns = (
            r"\bdo you remember (?:me|us)\b",
            r"\bremember us\b",
            r"\bwho did you just meet\b",
            r"\bwho did you meet\b",
            r"\bwho were you talking to\b",
        )
        reunion_token_groups = (
            ("we", "back"),
            ("us", "again"),
            ("hello", "again"),
            ("greet", "again"),
            ("say", "hi", "again"),
        )
        memory_token_groups = (
            ("remember", "me"),
            ("remember", "us"),
            ("still", "remember", "me"),
            ("still", "remember", "us"),
            ("who", "meet"),
            ("who", "talking", "to"),
        )
        if not self._matches_prompt_variants(
            normalized,
            regex_patterns=reunion_patterns + memory_patterns,
            token_groups=reunion_token_groups + memory_token_groups,
        ):
            return None

        names = self._social_memory_names(
            conversation_context,
            context_keys=(
                "friendly_recognized_names",
                "recognized_names",
                "recent_friendly_names",
                "recent_recognized_names",
                "last_social_names",
            ),
            memory_keys=("last_social_names", "recent_friendly_names", "recent_recognized_names"),
            limit=4,
        )
        spoken_names = self._spoken_name_list(names, limit=4)
        if self._matches_prompt_variants(normalized, regex_patterns=reunion_patterns, token_groups=reunion_token_groups):
            if spoken_names:
                return self._pick_profile_reply(
                    (
                        f"Hi again {spoken_names}. Good to see you back.",
                        f"Welcome back {spoken_names}. I remember you from this session.",
                        f"Nice to see you again {spoken_names}. I am ready for the next round.",
                    )
                )
            return self._pick_profile_reply(
                (
                    "Welcome back. If your enrolled faces are in view, I can greet everyone by name again.",
                    "Hi again. I can greet you by name as soon as I get a clear enrolled face match.",
                    "Good to see you back. Show me the enrolled faces again and I will greet everyone properly.",
                )
            )

        if spoken_names:
            return self._pick_profile_reply(
                (
                    f"Yes. I remember {spoken_names} from this session.",
                    f"I do. I recently met {spoken_names}.",
                    f"Yes. I was just talking with {spoken_names}.",
                )
            )
        return self._pick_profile_reply(
            (
                "I can remember who I just met during this session, but I do not have a clear named face match right now.",
                "I remember recent faces only when I get a clean enrolled match. Right now I do not have one in the active session context.",
                "I can keep short-term social memory during this session, but I need a clear enrolled face match before I can name who I just met.",
            )
        )

    def _mission_theme_variants(self, theme: str, *, spoken_names: str = "") -> tuple[str, ...]:
        def _format(body: str) -> str:
            text = f"{spoken_names}, {body}" if spoken_names else body
            return text[:1].upper() + text[1:] if text else ""

        theme_bodies = {
            "splash": (
                "splash mission time. Round one: sneak past the garden guardian. Round two: freeze when I say hold. Round three: ask me for a victory joke when you win.",
                "water-dodge challenge live. Move fast, stay unpredictable, and do not let the garden guard tag you on the first pass. Bonus points if you ask me for a dramatic countdown first.",
                "mission accepted. Your goal is to outsmart Smart Sentry for three rounds. Ask me for a joke, a countdown, or a new challenge between rounds.",
            ),
            "stealth": (
                "stealth mission time. Sneak between safe spots and freeze behind cover whenever I say hold.",
                "spy challenge live. Cross the yard as quietly as you can before the garden guardian centers up on you.",
                "ninja round ready. Move from one hiding spot to the next, and if I say detected, everyone freezes for two seconds.",
            ),
            "freeze": (
                "freeze-dance challenge live. When I say hold, everyone freezes like a statue. When I say move, scramble to a new spot before the next call.",
                "statue game ready. Keep moving until the command hold, then lock in place and try not to laugh.",
                "freeze mission active. Dash, stop, and pose on command. Bonus points if you stay perfectly still through the countdown.",
            ),
            "countdown": (
                "countdown race challenge ready. Ask me for a three-two-one launch, then sprint to the safe zone before the next call.",
                "ready-set-go challenge active. I can give you a dramatic countdown, then you race between checkpoints before time runs out.",
                "timer mission loaded. Beat the countdown, reach the marker first, and do not get tagged on the way through.",
            ),
            "joke": (
                "joke quest ready. Complete one lap, then ask me for a victory joke before the next round.",
                "laugh mission live. Win the round, then earn a fresh joke or silly intro as your prize.",
                "comedy challenge active. Finish the mission, then ask me for a joke, a goofy intro, or another round.",
            ),
        }
        bodies = theme_bodies.get(str(theme or "").strip().lower(), theme_bodies["splash"])
        return tuple(_format(body) for body in bodies)

    def _coaching_protocol_reply(self, prompt_text: str, conversation_context: Dict[str, Any] | None = None) -> str | None:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return None

        precision_patterns = (
            r"\bhow can i improve\b.*\b(?:aim|aiming|precision|accuracy)\b",
            r"\bhow do i improve\b.*\b(?:aim|aiming|precision|accuracy)\b",
            r"\b(?:improve|better)\b.*\b(?:aim|aiming|precision|accuracy)\b",
            r"\b(?:reduce|fix)\b.*\b(?:jitter|overshoot|drift)\b",
            r"\bmake\b.*\b(?:tracking|aiming)\b.*\b(?:smoother|steadier|less jumpy)\b",
        )
        precision_token_groups = (
            ("improve", "aim"),
            ("improve", "aiming"),
            ("improve", "precision"),
            ("better", "aim"),
            ("better", "precision"),
            ("reduce", "jitter"),
            ("fix", "drift"),
            ("tracking", "smoother"),
            ("tracking", "steadier"),
            ("less", "jumpy"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=precision_patterns, token_groups=precision_token_groups):
            return self._pick_profile_reply(
                (
                    "To improve aiming precision, start with three things: use a steadier engagement setup, improve lighting and camera stability so detections stop wobbling, and let Smart Sentry wait for a cleaner center lock before it squirts. If you want, ask me whether you want smoother tracking, tighter small-target precision, or faster response.",
                    "Aiming precision usually improves when the target box is more stable, the engagement behavior is less aggressive, and the system is allowed to hold center a little longer before release. Good lighting and a calmer tracking setup help more than brute speed.",
                    "For better precision, reduce visual wobble first, then tune for cleaner lock instead of faster reaction. In practice that means steadier camera conditions, a less jumpy tracking setup, and enough hold time for a centered shot.",
                )
            )

        playful_patterns = (
            r"\bhow can i make\b.*\b(?:you|it|smart sentry)\b.*\b(?:more playful|more fun)\b",
            r"\bhow do i make\b.*\b(?:you|it|smart sentry)\b.*\b(?:more playful|more fun)\b",
            r"\bmake\b.*\b(?:you|it|smart sentry)\b.*\b(?:more playful|more fun)\b",
            r"\bmore playful\b",
        )
        playful_token_groups = (
            ("more", "playful"),
            ("more", "fun"),
            ("make", "playful"),
            ("make", "fun"),
            ("fun", "kids"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=playful_patterns, token_groups=playful_token_groups):
            return self._pick_profile_reply(
                (
                    "To make me more playful, use the Playful personality, keep human voice on, and ask for missions, jokes, challenges, or silly introductions. I can also greet recognized faces by name and sound much more like a family splash-game host.",
                    "The best playful setup is to keep the voice lively, use lighter language, and ask me for games, countdowns, stealth rounds, freeze challenges, or fun intros instead of only commands.",
                    "If you want a more playful feel, let me stay in Playful mode and ask things like give us a splash mission, a freeze challenge, a stealth mission, or a goofy introduction. That makes the system feel much more social.",
                )
            )

        discovery_patterns = (
            r"\bwhat can we ask you\b",
            r"\bwhat should we say\b",
            r"\bwhat can i ask you\b",
            r"\bgive us some ideas\b",
            r"\bwhat can the kids ask\b",
        )
        discovery_token_groups = (
            ("what", "ask"),
            ("what", "say"),
            ("some", "ideas"),
            ("give", "ideas"),
            ("kids", "ask"),
            ("children", "ask"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=discovery_patterns, token_groups=discovery_token_groups):
            return self._pick_profile_reply(
                (
                    "You can ask who I am, what I can do, how to improve aiming precision, how to make me more playful, whether I remember you, tell me a joke, give us a splash mission, a stealth mission, a freeze challenge, or ask me to introduce myself to the kids.",
                    "Try things like who are you, what can you do, do you remember us, how can I improve the aiming precision, how can I make you more playful, tell us a joke, or give us a countdown race.",
                    "Good conversation starters are introduce yourself, what can you do, do you remember us, help me improve precision, make it more playful, tell a joke, or give us another challenge.",
                )
            )

        spoken_names = self._spoken_name_list(
            self._social_memory_names(
                conversation_context,
                context_keys=(
                    "friendly_recognized_names",
                    "recent_friendly_names",
                    "last_social_names",
                    "recognized_names",
                ),
                memory_keys=("last_social_names", "recent_friendly_names", "recent_recognized_names"),
                limit=4,
            ),
            limit=4,
        )
        mission_followup_patterns = (
            r"\b(?:another|different|next|one more)\s+(?:mission|challenge|game|round)\b",
            r"\banother challenge\b",
            r"\banother mission\b",
        )
        splash_patterns = (
            r"\b(?:splash|water)\s+(?:mission|challenge|game)\b",
        )
        stealth_patterns = (
            r"\b(?:stealth|sneak|ninja|spy)\b.*\b(?:mission|challenge|game|round)\b",
            r"\bgive us (?:a )?(?:stealth|sneak|ninja|spy)\b",
        )
        freeze_patterns = (
            r"\bfreeze(?:\s+dance)?\b.*\b(?:mission|challenge|game|round)\b",
            r"\b(?:statue|freeze dance)\b",
        )
        countdown_patterns = (
            r"\b(?:countdown|race|timer|ready set go)\b.*\b(?:mission|challenge|game|round)\b",
            r"\bgive us (?:a )?(?:countdown|race)\b",
        )
        joke_game_patterns = (
            r"\b(?:joke|laugh|comedy|funny)\b.*\b(?:mission|challenge|game|round)\b",
        )
        mission_patterns = (
            r"\b(?:give us|give me|start|launch)\b.*\b(?:mission|challenge|game|round)\b",
            r"\bwhat games can we play\b",
            r"\blet(?:'|’)s play\b",
            r"\bplay a game\b",
        )
        mission_followup_token_groups = (
            ("another", "challenge"),
            ("another", "mission"),
            ("next", "challenge"),
            ("one", "more", "challenge"),
            ("one", "more", "game"),
        )
        general_mission_token_groups = (
            ("give", "mission"),
            ("give", "challenge"),
            ("give", "game"),
            ("play", "game"),
            ("what", "games", "play"),
            ("lets", "play"),
        )
        mission_theme = ""
        if self._matches_prompt_variants(normalized, regex_patterns=stealth_patterns, token_groups=(("stealth", "challenge"), ("ninja", "game"), ("spy", "mission"), ("sneak", "challenge"))):
            mission_theme = "stealth"
        elif self._matches_prompt_variants(normalized, regex_patterns=freeze_patterns, token_groups=(("freeze", "challenge"), ("freeze", "dance"), ("statue", "game"))):
            mission_theme = "freeze"
        elif self._matches_prompt_variants(normalized, regex_patterns=countdown_patterns, token_groups=(("countdown", "challenge"), ("race", "game"), ("timer", "mission"), ("ready", "set", "go"))):
            mission_theme = "countdown"
        elif self._matches_prompt_variants(normalized, regex_patterns=joke_game_patterns, token_groups=(("joke", "game"), ("funny", "challenge"), ("laugh", "mission"), ("comedy", "round"))):
            mission_theme = "joke"
        elif self._matches_prompt_variants(normalized, regex_patterns=splash_patterns, token_groups=(("splash", "mission"), ("water", "game"), ("water", "challenge"))):
            mission_theme = "splash"

        if mission_theme or self._matches_prompt_variants(
            normalized,
            regex_patterns=mission_patterns + mission_followup_patterns,
            token_groups=general_mission_token_groups + mission_followup_token_groups,
        ):
            if mission_theme:
                return self._pick_mission_reply(self._mission_theme_variants(mission_theme, spoken_names=spoken_names))
            all_variants: tuple[str, ...] = ()
            for theme in ("splash", "stealth", "freeze", "countdown", "joke"):
                all_variants += self._mission_theme_variants(theme, spoken_names=spoken_names)
            return self._pick_mission_reply(all_variants)

        return None

    def _profile_query_kind(self, prompt_text: str) -> str | None:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return None
        introduction_patterns = (
            r"\bintroduce yourself\b",
            r"\bcan you introduce yourself\b",
            r"\bcould you introduce yourself\b",
            r"\bplease introduce yourself\b",
            r"\bdescribe yourself\b",
            r"\bdescribe yourself\b",
            r"\bgive me (?:an|your) introduction\b",
            r"\btell me who you are\b",
            r"\btell me about yourself\b",
            r"\bintroduce yourself to\b",
            r"\b(?:my|the) kids .*\bintroduce yourself\b",
            r"\b(?:my|the) (?:kids|children|family) .*\bmeet you\b",
        )
        identity_patterns = (
            r"\bwho are you\b",
            r"\bwho are u\b",
            r"\bwhat are you\b",
            r"\bwho are you elion\b",
            r"\bsay your name\b",
            r"\bwhat(?:'s| is) your name\b",
            r"\bwhat are you called\b",
            r"\bstate your name\b",
            r"\bidentify yourself\b",
            r"\bwho is elion mesk\b",
            r"\bwho is elion mosk\b",
            r"\bare you elion mesk\b",
            r"\bare you elion mosk\b",
        )
        capability_patterns = (
            r"\bwhat do you do\b",
            r"\bwhat can you do\b",
            r"\bwhat all can you do\b",
            r"\btell me what you can do\b",
            r"\bwhat is your role\b",
            r"\bwhat is your purpose\b",
            r"\bwhat are your capabilities\b",
            r"\bhow can you help\b",
            r"\bhow can you help us\b",
            r"\bwhat are you here for\b",
            r"\bwhat is your job\b",
            r"\bwhat do you help with\b",
            r"\bwhat do you do around here\b",
        )
        origin_patterns = (
            r"\bwho created you\b",
            r"\bwho made you\b",
            r"\bwho built you\b",
            r"\bwho designed you\b",
            r"\bwhere did you come from\b",
        )
        introduction_token_groups = (
            ("introduce", "yourself"),
            ("describe", "yourself"),
            ("give", "introduction"),
            ("tell", "who", "you"),
            ("tell", "about", "yourself"),
            ("meet", "you"),
        )
        identity_token_groups = (
            ("who", "you"),
            ("your", "name"),
            ("what", "called"),
            ("identify", "yourself"),
            ("state", "name"),
            ("say", "name"),
        )
        capability_token_groups = (
            ("what", "do", "you", "do"),
            ("what", "can", "you", "do"),
            ("your", "role"),
            ("your", "purpose"),
            ("your", "capabilities"),
            ("how", "help"),
            ("here", "for"),
            ("your", "job"),
        )
        origin_token_groups = (
            ("who", "created"),
            ("who", "made"),
            ("who", "built"),
            ("who", "designed"),
            ("where", "come", "from"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=introduction_patterns, token_groups=introduction_token_groups):
            return "introduction"
        if self._matches_prompt_variants(normalized, regex_patterns=identity_patterns, token_groups=identity_token_groups):
            return "identity"
        if self._matches_prompt_variants(normalized, regex_patterns=capability_patterns, token_groups=capability_token_groups):
            return "capabilities"
        if self._matches_prompt_variants(normalized, regex_patterns=origin_patterns, token_groups=origin_token_groups):
            return "origin"
        return None

    def _has_recent_profile_query(self) -> bool:
        for prior in self._command_history[-3:]:
            if self._profile_query_kind(prior):
                return True
        return False

    def _profile_protocol_reply(self, prompt_text: str, conversation_context: Dict[str, Any] | None = None) -> str | None:
        query_kind = self._profile_query_kind(prompt_text)
        if query_kind is None:
            return None
        family_reply = self._family_introduction_reply(prompt_text, conversation_context)
        if family_reply:
            return family_reply
        repeated = self._has_recent_profile_query()
        short_identity = (
            "I am Elion Mesk, or Elion for short, the AI assistant voice for Smart Sentry. "
            "I can talk with you normally, help with Smart Sentry questions, and switch into diagnostics when you ask."
        )
        short_capabilities = (
            "I can chat with you, help explain Smart Sentry, answer tuning questions, and switch into a more playful style for family splash time.",
            "I can talk normally, help with Smart Sentry questions, guide runtime tuning, and join in with more playful family-style conversations too.",
        )
        full_intro_variants = (
            f"{_ASSISTANT_INTRODUCTION_FULL} {_ASSISTANT_IDENTITY_BOUNDARY}",
            f"{_ASSISTANT_INTRODUCTION_FULL} {_ASSISTANT_IDENTITY_BOUNDARY} I stay focused on verified runtime state and supported controls.",
            f"{_ASSISTANT_INTRODUCTION_FULL} {_ASSISTANT_IDENTITY_BOUNDARY} I am actively improving while remaining grounded in what the app is actually doing now.",
        )
        short_identity_variants = (
            short_identity,
            "I am Elion Mesk, Elion for short. I am the AI assistant voice for Smart Sentry.",
            "Elion Mesk here. I am Smart Sentry's conversational AI assistant.",
        )
        short_capability_variants = (
            *short_capabilities,
            "Right now I can answer questions, help explain Smart Sentry, run diagnostics when you ask, and handle supported commands.",
            "My current scope is normal conversation, Smart Sentry help, diagnostics on request, and supported command handling.",
        )
        identity_intro_variants = (
            short_identity,
            "I am Elion Mesk, Elion for short. I am the AI assistant voice inside Smart Sentry.",
            "Elion Mesk here. I am Smart Sentry's AI assistant, and yes, you are talking to me directly.",
        )
        capability_intro_variants = (
            *short_capabilities,
            "I can talk normally, answer Smart Sentry questions, help diagnose issues when you ask, and handle supported commands.",
            "My role is normal conversation first, then Smart Sentry help, diagnostics, and supported command handling when needed.",
        )
        origin_variants = (
            "GM Labs built me as Gino's Smart Sentry runtime assistant. I stay grounded in the live app state and supported controls.",
            "I was created by GM Labs for Gino as part of Smart Sentry's local runtime assistant workflow.",
            "I come from GM Labs and Gino's Smart Sentry project. My job is to stay inside the running app and help from real telemetry.",
        )
        if query_kind == "identity":
            return self._pick_profile_reply(short_identity_variants if repeated else identity_intro_variants)
        if query_kind == "capabilities":
            return self._pick_profile_reply(short_capability_variants if repeated else capability_intro_variants)
        if query_kind == "origin":
            return self._pick_profile_reply(origin_variants)
        if repeated:
            short_identity_pick = self._pick_profile_reply(short_identity_variants)
            short_capability_pick = self._pick_profile_reply(short_capability_variants)
            return self._pick_profile_reply(
                (
                    f"{short_identity} {short_capabilities[0]}",
                    f"{short_identity_pick} {short_capability_pick}",
                )
            )
        return self._pick_profile_reply(full_intro_variants)

    def fast_voice_conversation_reply(
        self,
        prompt_text: str,
        *,
        canonical_prompt: str | None = None,
        conversation_context: Dict[str, Any] | None = None,
    ) -> str | None:
        raw_prompt = str(prompt_text or "").strip()
        lookup_prompt = str(canonical_prompt or raw_prompt).strip() or raw_prompt
        # Scene queries need live detection data — can't answer them in the fast offline path.
        if self._prompt_mentions_scene_query(raw_prompt):
            return None
        self._remember_social_context(conversation_context)
        reply = self._profile_protocol_reply(raw_prompt, conversation_context)
        if reply is None:
            reply = self._social_memory_reply(raw_prompt, conversation_context)
        if reply is None:
            reply = self._coaching_protocol_reply(raw_prompt, conversation_context)
        if reply is None:
            reply = self._conversational_protocol_reply(raw_prompt)
        if reply:
            self._remember_command(lookup_prompt or raw_prompt)
        return reply

    def _assistant_personality_key(self) -> str:
        key = str(getattr(self, "_personality", "sentinel") or "sentinel").strip().lower()
        if key not in _ASSISTANT_PERSONALITY_PROFILES:
            return "sentinel"
        return key

    def _assistant_personality_profile(self) -> Dict[str, Any]:
        return _ASSISTANT_PERSONALITY_PROFILES.get(self._assistant_personality_key(), _ASSISTANT_PERSONALITY_PROFILES["sentinel"])

    def _conversational_protocol_reply(self, prompt_text: str) -> str | None:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return None
        profile = self._assistant_personality_profile()
        tokens = self._prompt_token_set(normalized)

        personality_patterns = (
            r"\bwhat(?:'s| is) your personality\b",
            r"\bwhat personality are you using\b",
            r"\bwhat personality.*\busing\b",
            r"\bwhich personality\b",
            r"\bcurrent personality\b",
            r"\bactive personality\b",
            r"\bpersonality mode\b",
        )
        personality_token_groups = (
            ("what", "personality"),
            ("which", "personality"),
            ("current", "personality"),
            ("active", "personality"),
            ("personality", "mode"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=personality_patterns, token_groups=personality_token_groups):
            return f"Current assistant personality: {profile['label']}. {profile['personality_reply']}"

        joke_patterns = (
            r"\btell me (?:a|another) joke\b",
            r"\bmake me laugh\b",
            r"\bsomething funny\b",
            r"\bany jokes\b",
            r"\bjoke\b",
        )
        joke_followup_patterns = (
            r"^another$",
            r"^another one$",
            r"^one more$",
            r"^another joke$",
            r"^one more joke$",
            r"^tell another$",
        )
        joke_token_groups = (
            ("joke",),
            ("funny",),
            ("laugh",),
            ("make", "laugh"),
            ("tell", "joke"),
            ("say", "funny"),
        )
        joke_followup_token_groups = (
            ("another",),
            ("another", "one"),
            ("one", "more"),
            ("another", "joke"),
            ("one", "more", "joke"),
            ("tell", "another"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=joke_patterns, token_groups=joke_token_groups) or (
            self._matches_prompt_variants(normalized, regex_patterns=joke_followup_patterns, token_groups=joke_followup_token_groups)
            and self._recent_command_matches(joke_patterns, limit=2)
        ):
            jokes = list(profile.get("jokes") or [])
            if jokes:
                return self._pick_joke_reply(jokes)

        greeting_phrases = (
            "hi",
            "hello",
            "hey",
            "hello there",
            "hey there",
            "elion",
            "hi elion",
            "hello elion",
            "hey elion",
            "hello there elion",
            "hey there elion",
            "how are you",
            "how are you elion",
            "how are you doing",
            "how are you doing today",
            "good morning",
            "good afternoon",
            "good evening",
        )
        greeting_token_groups = (
            ("good", "morning"),
            ("good", "afternoon"),
            ("good", "evening"),
            ("how", "you"),
            ("hello", "there"),
            ("hey", "there"),
        )
        if len(tokens) <= 6 and self._matches_prompt_variants(normalized, phrases=greeting_phrases, token_groups=greeting_token_groups):
            greeting_options = profile.get("greeting") or []
            if isinstance(greeting_options, list) and greeting_options:
                return self._pick_profile_reply(greeting_options)
            return str(self._get_personality_response("greeting") or profile.get("greeting") or "Standing by.")

        small_talk_patterns = (
            r"\bnice to meet you\b",
            r"\bgood to see you\b",
            r"\blong time no see\b",
            r"\bare you there\b",
            r"\byou still there\b",
            r"\bhow are you doing\b",
        )
        small_talk_token_groups = (
            ("nice", "meet"),
            ("good", "see"),
            ("long", "time", "see"),
            ("still", "there"),
            ("you", "there"),
            ("how", "doing"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=small_talk_patterns, token_groups=small_talk_token_groups):
            return str(self._get_personality_response("small_talk") or "I am here and listening.")

        compliment_patterns = (
            r"\bgood job\b",
            r"\bnice job\b",
            r"\bwell done\b",
            r"\bgreat work\b",
            r"\bimpressive\b",
        )
        compliment_token_groups = (
            ("good", "job"),
            ("nice", "job"),
            ("well", "done"),
            ("great", "work"),
            ("really", "good"),
            ("impressive",),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=compliment_patterns, token_groups=compliment_token_groups):
            return self._pick_profile_reply(
                (
                    "Thank you. I will keep it sharp.",
                    "Appreciated. I am ready for the next one.",
                    "Thank you. I will stay focused and useful.",
                )
            )

        thanks_patterns = (
            r"\bthanks\b",
            r"\bthank you\b",
            r"\bappreciate it\b",
        )
        thanks_token_groups = (
            ("thanks",),
            ("thank", "you"),
            ("appreciate", "it"),
            ("many", "thanks"),
        )
        if self._matches_prompt_variants(normalized, regex_patterns=thanks_patterns, token_groups=thanks_token_groups) and len(normalized.split()) <= 6:
            return str(self._get_personality_response("thanks") or profile.get("thanks") or "Standing by.")
        return None

    def is_available(self) -> bool:
        return self._client.is_available()

    def list_models(self) -> List[str]:
        return self._client.list_models()

    def _request_timeout_s(self) -> float:
        return max(5.0, float(getattr(self._client, "timeout_s", 45.0) or 45.0))

    def _default_conversation_intent(self) -> Dict[str, Any]:
        return {
            "action": "none",
            "value": None,
            "confidence": 1.0,
            "needs_clarification": False,
            "question": "",
            "suggestions": [],
            "payload": {},
            "conversation_mode": "general_conversation",
            "routing_source": "service_default_conversation",
            "routing_owner": "assistant.service",
        }

    def _general_conversation_anchor(self) -> str:
        return (
            "You are Elion Mesk, the conversational AI assistant voice for Smart Sentry. "
            "Answer naturally, briefly, and like a normal AI unless the operator explicitly asks for runtime status or diagnostics."
        )

    def _prompt_requests_analysis(self, prompt_text: str) -> bool:
        prompt = self._normalize_conversation_text(prompt_text)
        if not prompt:
            return False
        analysis_tokens = (
            "analy",
            "analyse",
            "analysis",
            "diagnos",
            "status",
            "report",
            "behaviour",
            "behavior",
            "current app",
            "current behaviour",
            "current behavior",
        )
        if any(token in prompt for token in analysis_tokens):
            return True
        diagnostic_tokens = (
            "what's wrong",
            "whats wrong",
            "run diagnostics",
            "check status",
            "system report",
            "status report",
            "not loading",
            "not working",
        )
        if any(token in prompt for token in diagnostic_tokens):
            return True
        question_prefixes = (
            "why ",
            "how ",
            "what ",
            "tell me why ",
            "explain why ",
        )
        system_tokens = (
            "face detection",
            "face recognition",
            "camera",
            "tracking",
            "runtime",
            "model",
            "assistant",
            "voice",
            "detection",
            "recognition",
        )
        return prompt.startswith(question_prefixes) and any(token in prompt for token in system_tokens)

    def _should_use_general_conversation(self, prompt_text: str, parsed_actions: List[AssistantAction]) -> bool:
        normalized = self._normalize_conversation_text(prompt_text)
        if not normalized:
            return False
        if parsed_actions:
            return False
        if self._prompt_requests_analysis(normalized):
            return False

        # Treat natural help/frustration phrasing as conversation before generic
        # explicit-action prefix checks. This keeps normal voice UX responsive.
        conversational_help_patterns = (
            r"\bcan you help me understand\b",
            r"\bhelp me understand\b",
            r"\bcan you explain\b",
            r"\bcould you explain\b",
            r"\bi am feeling\b",
            r"\bi m feeling\b",
            r"\bfeeling frustrated\b",
            r"\bfrustrated with\b",
        )

        command_like_conversation_exclusions = (
            r"\bconnect\b",
            r"\bdisconnect\b",
            r"\bset\b.*\b(mode|speed|confidence|threshold|profile|voice style)\b",
            r"\b(enable|disable|turn on|turn off|start|stop|restart|relaunch|open|close)\b",
            r"\b(go home|go rest|move to|toggle camera)\b",
        )
        if any(re.search(pattern, normalized) for pattern in conversational_help_patterns):
            if not any(re.search(pattern, normalized) for pattern in command_like_conversation_exclusions):
                return True

        if self._is_explicit_action_request(normalized):
            return False
        
        # Explicitly exclude command patterns that should NOT be treated as conversation
        command_patterns = (
            "run the smart sentry", "run smart sentry", "start smart sentry", "start the smart sentry",
            "enable smart sentry", "activate smart sentry", "turn on smart sentry",
            "stop smart sentry", "disable smart sentry", "deactivate smart sentry", "turn off smart sentry",
            "connect to", "disconnect from", "set detection mode", "toggle camera",
            "move to", "go home", "go rest", "set confidence", "set speed"
        )
        if any(pattern in normalized for pattern in command_patterns):
            return False
        conversational_starts = (
            "who ", "what ", "how ", "when ", "where ", "why ",
            "can you ", "could you ", "would you ", "will you ",
            "do you ", "did you ", "have you ",
            "are you ", "is this ",
            "tell me ", "explain ", "describe ",
            "hi", "hello", "hey", "good morning", "good afternoon", "good evening",
            "thanks", "thank you", "appreciate", "great", "awesome", "cool",
            "i think", "i feel", "i wonder", "maybe", "perhaps",
            "by the way", "also", "another thing", "additionally",
        )
        if normalized.startswith(conversational_starts):
            return True
        # Expanded conversational triggers
        conversational_triggers = {
            "joke", "personality", "make me laugh", "something funny", 
            "how are you", "how are you today", "what's up", "what's new",
            "nice to meet you", "good to see you", "long time no see",
            "interesting", "really", "wow", "amazing", "cool", "awesome",
            "help me", "help", "assist", "support", "guide",
            "opinion", "think", "believe", "suggest", "recommend",
            "bored", "tired", "happy", "sad", "excited", "curious"
        }
        
        if any(trigger in normalized for trigger in conversational_triggers):
            return True
            
        # Check for conversational patterns
        if any(pattern in normalized for pattern in [
            "i like", "i love", "i hate", "i prefer", "i want",
            "do you like", "do you prefer", "do you think",
            "what about", "how about", "tell me more", "go on"
        ]):
            return True
            
        return normalized.endswith("?") or normalized.endswith(".")

    def _conversation_system_prompt(self) -> str:
        profile = self._assistant_personality_profile()
        return (
            f"You are {_ASSISTANT_FULL_NAME}, the conversational AI voice for Smart Sentry. "
            "Default to normal, natural conversation. "
            "Do not volunteer runtime status, diagnostics, configuration values, or system summaries unless the operator explicitly asks for them. "
            "Do not sound like a status banner, protocol stub, or control panel. "
            "Keep identity facts consistent, but answer like a real assistant. "
            f"Current conversational personality is {profile['label']}; keep your phrasing {profile['style_instruction']}."
        )

    def _general_conversation_fallback(self, prompt_text: str, deterministic_anchor: str) -> str:
        normalized = re.sub(r"\s+", " ", str(prompt_text or "").strip().lower())
        if normalized in {"hi", "hello", "hey", "how are you", "how are you today"}:
            return "I am here and listening. Ask me anything, and I will keep it conversational unless you want system diagnostics."
        if "joke" in normalized or "funny" in normalized or "laugh" in normalized:
            return self._conversational_protocol_reply(prompt_text) or "I would rather tell a better joke when the local model is up, but I am still here."
        return deterministic_anchor

    def _conversation_prompt(self, operator_prompt: str, deterministic_anchor: str, excerpt: str = "", knowledge: str = "") -> str:
        memory = self._memory_context()
        command_memory = "\n".join(f"- {item}" for item in memory.get("command_history", [])[-3:]) or "- none"
        recent_social_memory = self._spoken_name_list(
            memory.get("last_social_names", []) or memory.get("recent_friendly_names", []) or memory.get("recent_recognized_names", []),
            limit=4,
        )
        prompt = (
            "Answer the operator naturally in first person. "
            "Sound like a real assistant, not a status banner or protocol stub. "
            "Default to normal conversation unless the operator explicitly asks for live status or diagnostics. "
            "Do not volunteer system status, runtime summaries, configuration values, or operational details unless asked. "
            "Keep the facts consistent with the Smart Sentry identity rules below. "
            "If the operator is asking who you are, what your name is, what you do, or asking for light conversation, answer directly and conversationally in 1 to 4 short sentences. "
            "Do not include section headers, labels, metadata, or parser-style wording.\n\n"
            f"Operator request:\n{operator_prompt}\n\n"
            f"Consistency anchor for required facts:\n{deterministic_anchor}\n\n"
            f"Recent command memory (last up to 3):\n{command_memory}\n\n"
        )
        if recent_social_memory:
            prompt += f"Recent social memory from this session:\n- recently recognized faces: {recent_social_memory}\n\n"
        if str(excerpt or "").strip():
            prompt += f"Runtime excerpt only if directly relevant:\n{excerpt}\n\n"
        if str(knowledge or "").strip():
            prompt += f"App knowledge context only if directly relevant:\n{knowledge}"
        return prompt.strip()

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
                text=reply_text.strip() + "  End of analysys report.",
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
                text=fallback + "  End of analysys report.",
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
                text=reply_text.strip() + "  End of analysys report.",
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
                text=fallback + "  End of analysys report.",
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
        def _with_routing(intent: Dict[str, Any] | None, *, mode: str, source: str) -> Dict[str, Any]:
            merged = dict(intent or self._default_conversation_intent())
            merged["conversation_mode"] = str(mode or "general_conversation").strip().lower() or "general_conversation"
            merged["routing_source"] = str(source or "service_default_conversation").strip().lower() or "service_default_conversation"
            merged["routing_owner"] = "assistant.service"
            return merged

        parsed_actions = self._parse_actions(prompt_text)
        profile_reply = self._profile_protocol_reply(prompt_text)

        # Scene query — describe what the camera currently sees using detection context.
        scene_reply = self._scene_query_reply(prompt_text, snapshot)
        if scene_reply is not None:
            anchor = scene_reply
            conversation_prompt = self._conversation_prompt(prompt_text, anchor)
            if self.is_available():
                try:
                    reply_text = self._client.generate(
                        model=model,
                        prompt=conversation_prompt,
                        system=self._conversation_system_prompt(),
                        timeout_s=min(self._request_timeout_s(), 20.0),
                        options=self._llm_options(max_output_tokens=180, temperature=0.30),
                    )
                    cleaned = str(reply_text or "").strip()
                    if cleaned:
                        return AssistantReply(
                            text=cleaned, source="ollama", model=model,
                            raw_response=reply_text, prompt_used=conversation_prompt,
                            intent=_with_routing(
                                self._default_conversation_intent(),
                                mode="scene_conversation",
                                source="service_scene_query",
                            ),
                            memory_context=self._memory_context(),
                        )
                except Exception as exc:
                    return AssistantReply(
                        text=anchor, source="deterministic", model=model,
                        raw_response="scene_query_fallback", prompt_used=conversation_prompt,
                        intent=_with_routing(
                            self._default_conversation_intent(),
                            mode="scene_conversation",
                            source="service_scene_query",
                        ),
                        memory_context=self._memory_context(),
                        error=str(exc),
                    )
            return AssistantReply(
                text=anchor, source="deterministic", model=model,
                raw_response="scene_query_fallback", prompt_used="scene_query_fallback",
                intent=_with_routing(
                    self._default_conversation_intent(),
                    mode="scene_conversation",
                    source="service_scene_query",
                ),
                memory_context=self._memory_context(),
            )
        conversational_reply = self._conversational_protocol_reply(prompt_text)
        guided_conversation_reply = profile_reply if profile_reply is not None else conversational_reply
        general_conversation = bool(guided_conversation_reply is not None or self._should_use_general_conversation(prompt_text, parsed_actions))
        if general_conversation:
            self._remember_command(prompt_text)
            deterministic_anchor = guided_conversation_reply or self._general_conversation_anchor()
            prompt = self._conversation_prompt(prompt_text, deterministic_anchor)
            if self.is_available():
                try:
                    reply_text = self._client.generate(
                        model=model,
                        prompt=prompt,
                        system=self._conversation_system_prompt(),
                        timeout_s=min(self._request_timeout_s(), 20.0),
                        options=self._llm_options(max_output_tokens=160, temperature=0.35),
                    )
                    cleaned_reply = str(reply_text or "").strip()
                    if cleaned_reply:
                        return AssistantReply(
                            text=cleaned_reply,
                            source="ollama",
                            model=model,
                            raw_response=reply_text,
                            prompt_used=prompt,
                            intent=_with_routing(
                                self._default_conversation_intent(),
                                mode="general_conversation",
                                source="service_general_conversation",
                            ),
                            memory_context=self._memory_context(),
                        )
                except Exception as exc:
                    return AssistantReply(
                        text=self._general_conversation_fallback(prompt_text, deterministic_anchor),
                        source="deterministic",
                        model=model,
                        raw_response="conversation_fallback",
                        prompt_used=prompt,
                        intent=_with_routing(
                            self._default_conversation_intent(),
                            mode="general_conversation",
                            source="service_general_conversation",
                        ),
                        memory_context=self._memory_context(),
                        error=str(exc),
                    )
            return AssistantReply(
                text=self._general_conversation_fallback(prompt_text, deterministic_anchor),
                source="deterministic",
                model=model,
                raw_response="conversation_fallback",
                prompt_used="conversation_fallback",
                intent=_with_routing(
                    self._default_conversation_intent(),
                    mode="general_conversation",
                    source="service_general_conversation",
                ),
                memory_context=self._memory_context(),
            )
        findings, recommendations, summary = self._analyzer.analyze(snapshot)
        self._remember_command(prompt_text)
        intent = self._parse_intent(prompt_text, snapshot, model=model, fallback_actions=parsed_actions)
        intent = _with_routing(intent, mode="task_or_command", source="service_operator_prompt")
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
            "toggle_camera, connect_link, disconnect_link, restart_app, draft_setting_change.\n\n"
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
        if action_type == "restart_app":
            return [AssistantAction("restart_app", "Restart Smart Sentry", payload, False)]
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
        if self._matches_action_request(lower_prompt, ("restart", "relaunch", "reload"), ("smart sentry", "app", "the app", "the smart sentry")):
            _append(AssistantAction("restart_app", "Restart Smart Sentry", {}, False))
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
            "restart_app": 14,
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
        normalized = re.sub(r"\brestaart\b", "restart", normalized)
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
            "restart ",
            "relaunch ",
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
        normalized = re.sub(r"\brestaart\b", "restart", normalized)
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
            "face_runtime": snapshot.get("face_runtime") or {},
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
            "If a subsystem is unavailable or not loading, name the most specific root cause supported by the runtime facts before giving broader advice.\n\n"
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
            "Use the app knowledge context to compare intended behavior versus the current runtime/settings when relevant. "
            "When the operator asks why something is not loading, unavailable, or not working, lead with the most specific runtime-backed root cause and the shortest corrective next step. Stay concise.\n\n"
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
        face_runtime = snapshot.get("face_runtime") or {}
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
            f"face_backend={face_runtime.get('active_backend', 'n/a')}",
            f"face_profiles_ready={face_runtime.get('ready_profile_count', 'n/a')}",
            f"mode={detection_cfg.get('detection_mode', 'n/a')}",
            f"tracking_scope={tracked_scope}",
        ]
        if engagement_cfg:
            summary_parts.append(
                f"loss_protocols={engagement_cfg.get('loss_recovery_protocol_new_target', 'n/a')}"
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
                    "Using deterministic runtime guidance, I "
                    + " and ".join(segments)
                    + ". Supported live actions still route through the existing deterministic UI handlers. Tell me what to do next when this step is done."
                )
        subsystem_fallback = self._targeted_subsystem_fallback(prompt_text, snapshot)
        if subsystem_fallback:
            return subsystem_fallback
        if findings:
            return f"Using deterministic runtime guidance, the top finding is: {findings[0].detail}"
        if recommendations:
            return f"Using deterministic runtime guidance, a reasonable next step is: {recommendations[0]}"
        return (
            "The local assistant model is unavailable right now. "
            "I can still help with deterministic status, diagnostics, connection reporting, and supported direct commands. "
            "Ask for a status report or give another command when ready."
        )

    def _targeted_subsystem_fallback(self, prompt_text: str, snapshot: Dict[str, Any]) -> str:
        lowered = str(prompt_text or "").lower()
        config = snapshot.get("config") or {}
        engine = snapshot.get("engine_state") or {}
        camera = snapshot.get("camera_status") or {}
        face_runtime = snapshot.get("face_runtime") or {}
        recent_logs = [str(line or "") for line in list(snapshot.get("recent_log_lines") or []) if str(line or "").strip()]
        engagement = config.get("engagement") or {}
        pir_guard = config.get("pir_guard") or {}
        if any(token in lowered for token in ("face", "identity", "recognition")):
            face_enabled = bool((config.get("face_recognition") or {}).get("enabled", False))
            face_backend = str(face_runtime.get("active_backend") or "legacy_dct")
            preferred_backend = str(face_runtime.get("preferred_backend") or face_backend)
            backend_status = str(face_runtime.get("backend_status") or face_backend)
            ready_profiles = int(face_runtime.get("ready_profile_count") or 0)
            known_profiles = int(face_runtime.get("known_profile_count") or 0)
            required_samples = int(face_runtime.get("required_profile_samples") or 1)
            face_issue_log = ""
            for line in reversed(recent_logs):
                line_lower = line.lower()
                if "face" not in line_lower:
                    continue
                if any(token in line_lower for token in ("unavailable", "failed", "missing", "no live frame", "no preview frame", "no faces detected")):
                    face_issue_log = line
                    break
            if not face_enabled:
                root_cause = "Face recognition is currently disabled in the live configuration."
                next_step = "Enable face recognition before expecting live face detections or identity matches."
            elif not bool(camera.get("capture_open")):
                root_cause = "The camera feed is closed, so the face pipeline has no live video to inspect."
                next_step = "Open the camera or another live source, then rerun the face check."
            elif not bool(face_runtime.get("has_live_frame")):
                root_cause = "The camera is open, but no live frame has reached the face pipeline yet."
                next_step = "Wait for the first good frame or reopen the camera if frames are stalled."
            elif not bool(face_runtime.get("detection_backend_ready")):
                root_cause = f"The active face backend {face_backend} is not ready. {backend_status}"
                next_step = "Verify the face detector and recognizer runtime assets, then retry loading the face backend."
            elif bool(face_runtime.get("preferred_backend_degraded")):
                root_cause = f"The preferred face backend {preferred_backend} did not load cleanly, so the runtime fell back to {face_backend}. {backend_status}"
                next_step = "Check the configured face model paths if you expect the preferred backend to be active."
            elif known_profiles <= 0:
                root_cause = "The face pipeline is running, but no saved profiles exist for known-face recognition."
                next_step = "Register at least one face profile if you want named identity matches instead of generic face boxes."
            elif ready_profiles <= 0:
                root_cause = (
                    f"Saved face profiles exist, but none are usable with backend {face_backend} under the current sample requirement "
                    f"of {required_samples}."
                )
                next_step = "Rebuild face samples for the active backend or reduce the required sample count."
            elif face_issue_log:
                root_cause = face_issue_log
                next_step = "Address the latest face runtime warning first, then retest with a live frame."
            else:
                root_cause = (
                    f"The face runtime looks loaded: backend={face_backend}, ready_profiles={ready_profiles}/{known_profiles}. "
                    "If matching still looks wrong, the issue is more likely scene quality, face size, or threshold tuning than a load failure."
                )
                next_step = "Capture a fresh live frame and compare face size, threshold, and profile sample quality."
            return (
                "Deterministic face-runtime summary. "
                f"Root cause: {root_cause} "
                f"Runtime facts: camera_open={bool(camera.get('capture_open'))}, face_backend={face_backend}, "
                f"ready_profiles={ready_profiles}/{known_profiles}, preferred_backend={preferred_backend}. "
                f"Suggested fix: {next_step}"
            )
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
                "Deterministic target-loss summary. "
                f"Current after-loss runtime phase: {phase}. Last reacquire note: {note}. "
                f"Configured protocols: visible-target handoff uses {protocol_new_target}, and no-detection recovery uses {protocol_no_detection}. "
                f"Current loss-search style is {loss_style} with rounds={rounds} and step interval={interval_s}. PIR search style is {pir_style}. "
                "The intended contract in the current app docs is bounded loss recovery: rapid handoff for stronger visible replacements, persistent local reacquire in sparse scenes, and a clean return to guard when recovery expires in fixed-guard behavior."
            )
        if any(token in lowered for token in ("button", "home", "rest", "camera", "connection", "link", "save settings")):
            connection = snapshot.get("comm_telemetry") or {}
            camera = snapshot.get("camera_status") or {}
            return (
                "Deterministic control summary. "
                f"Connection state: {'connected' if connection.get('is_connected') else 'disconnected'}. "
                f"Camera state: {'open' if camera.get('capture_open') else 'closed'}. "
                "The main runtime controls live in sentry_v2_tab.py, including Wake Up, Go Rest, connection toggle, camera toggle, and Save Settings. "
                "Those controls are intended to route through the existing deterministic UI handlers rather than through freeform model control."
            )
        return ""
