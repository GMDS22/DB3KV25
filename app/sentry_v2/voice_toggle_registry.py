from __future__ import annotations

import re
from typing import Iterable, Tuple


DEFAULT_ENABLE_VERBS = ("enable", "turn on", "activate")
DEFAULT_DISABLE_VERBS = ("disable", "turn off", "deactivate")
SHOW_ENABLE_VERBS = ("show", "enable", "turn on")
SHOW_DISABLE_VERBS = ("hide", "disable", "turn off")
START_ENABLE_VERBS = ("enable", "start", "activate", "run")
START_DISABLE_VERBS = ("disable", "stop", "deactivate")
OUTPUT_ENABLE_VERBS = ("turn on", "enable", "activate")
OUTPUT_DISABLE_VERBS = ("turn off", "disable", "deactivate")


VOICE_TOGGLE_SPECS: tuple[dict[str, object], ...] = (
    {
        "key": "video_feed",
        "label": "Video feed",
        "control_attr": "_chk_show_video",
        "enable_command": "enable video feed",
        "disable_command": "disable video feed",
        "aliases": ("video feed", "video display", "camera feed"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "test_media_loop",
        "label": "Test media loop",
        "control_attr": "_chk_test_media_loop",
        "enable_command": "enable test media loop",
        "disable_command": "disable test media loop",
        "aliases": ("test media loop", "test video loop", "media loop"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "ai_assistant",
        "label": "AI assistant",
        "control_attr": "_chk_ai_enabled",
        "enable_command": "enable ai assistant",
        "disable_command": "disable ai assistant",
        "aliases": ("ai assistant", "assistant"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "human_voice",
        "label": "Human voice",
        "control_attr": "_chk_human_voice_enabled",
        "enable_command": "enable human voice",
        "disable_command": "disable human voice",
        "aliases": ("human voice", "voice speech", "spoken voice"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "sound",
        "label": "Sound",
        "control_attr": "_chk_sound_enabled",
        "enable_command": "enable sound",
        "disable_command": "disable sound",
        "aliases": ("sound", "sound cues", "buzzer sound"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "face_recognition",
        "label": "Face recognition",
        "control_attr": "_chk_face_enabled",
        "enable_command": "enable face recognition",
        "disable_command": "disable face recognition",
        "aliases": ("face recognition", "face id"),
        "enable_verbs": START_ENABLE_VERBS,
        "disable_verbs": START_DISABLE_VERBS,
    },
    {
        "key": "face_suppression",
        "label": "Face suppression",
        "control_attr": "_chk_face_suppress",
        "enable_command": "enable face suppression",
        "disable_command": "disable face suppression",
        "aliases": (
            "face suppression",
            "known face suppression",
            "suppress known faces",
            "friendly face suppression",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "face_announcements",
        "label": "Face announcements",
        "control_attr": "_chk_face_announce",
        "enable_command": "enable face announcements",
        "disable_command": "disable face announcements",
        "aliases": ("face announcements", "face name announcements", "name announcements"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "face_gesture",
        "label": "Face greeting gesture",
        "control_attr": "_chk_face_gesture",
        "enable_command": "enable face greeting gesture",
        "disable_command": "disable face greeting gesture",
        "aliases": ("face greeting gesture", "face greeting", "greeting gesture"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "shortcuts",
        "label": "Shortcuts",
        "control_attr": "_chk_shortcuts_enabled",
        "enable_command": "enable shortcuts",
        "disable_command": "disable shortcuts",
        "aliases": ("shortcuts", "keyboard shortcuts", "window shortcuts"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "manual_keyboard_controls",
        "label": "Manual keyboard controls",
        "control_attr": "_chk_manual_keyboard_enabled",
        "enable_command": "enable manual keyboard controls",
        "disable_command": "disable manual keyboard controls",
        "aliases": (
            "manual keyboard controls",
            "manual keyboard movement",
            "manual movement keys",
            "manual fire keys",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_auto_speak",
        "label": "Assistant auto speak",
        "control_attr": "_chk_ai_auto_speak",
        "enable_command": "enable assistant auto speak",
        "disable_command": "disable assistant auto speak",
        "aliases": ("assistant auto speak", "auto speak", "assistant speech replies"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "auto_speak_cue_requirement",
        "label": "Auto speak cue requirement",
        "control_attr": "_chk_ai_auto_speak_requires_cue",
        "enable_command": "enable auto speak cue requirement",
        "disable_command": "disable auto speak cue requirement",
        "aliases": (
            "auto speak cue requirement",
            "auto speak cue name requirement",
            "assistant cue requirement",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "mute_buzzer_human_voice",
        "label": "Mute buzzer in human voice mode",
        "control_attr": "_chk_mute_buzzer_for_human_voice",
        "enable_command": "enable mute buzzer in human voice mode",
        "disable_command": "disable mute buzzer in human voice mode",
        "aliases": (
            "mute buzzer in human voice mode",
            "human voice buzzer mute",
            "mute buzzer for human voice",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "speech_cleanup",
        "label": "Speech cleanup",
        "control_attr": "_chk_human_voice_cleanup",
        "enable_command": "enable speech cleanup",
        "disable_command": "disable speech cleanup",
        "aliases": ("speech cleanup", "voice cleanup", "natural speech cleanup"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "known_face_hello_once",
        "label": "One hello per known face",
        "control_attr": "_chk_known_face_hello_once",
        "enable_command": "enable one hello per known face",
        "disable_command": "disable one hello per known face",
        "aliases": (
            "one hello per known face",
            "known face hello once",
            "hello once per session",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "tracking_voice_reports",
        "label": "Tracking voice reports",
        "control_attr": "_chk_autotracking_voice_reports",
        "enable_command": "enable tracking voice reports",
        "disable_command": "disable tracking voice reports",
        "aliases": ("tracking voice reports", "autotracking voice reports", "tracking voice updates"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "pir_voice_reports",
        "label": "PIR voice reports",
        "control_attr": "_chk_pir_voice_reports",
        "enable_command": "enable pir voice reports",
        "disable_command": "disable pir voice reports",
        "aliases": ("pir voice reports", "pir voice alerts", "pir spoken alerts"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "acoustic_voice_reports",
        "label": "Acoustic voice reports",
        "control_attr": "_chk_acoustic_voice_reports",
        "enable_command": "enable acoustic voice reports",
        "disable_command": "disable acoustic voice reports",
        "aliases": ("acoustic voice reports", "acoustic voice alerts", "acoustic spoken alerts"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_mode_switching",
        "label": "Assistant mode switching",
        "control_attr": "_chk_ai_allow_modes",
        "enable_command": "enable assistant mode switching",
        "disable_command": "disable assistant mode switching",
        "aliases": ("assistant mode switching", "assistant mode changes", "assistant mode suggestions"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_tuning_drafts",
        "label": "Assistant tuning drafts",
        "control_attr": "_chk_ai_allow_tuning",
        "enable_command": "enable assistant tuning drafts",
        "disable_command": "disable assistant tuning drafts",
        "aliases": (
            "assistant tuning drafts",
            "assistant tuning changes",
            "assistant setting drafts",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_runtime_analysis",
        "label": "Assistant runtime analysis",
        "control_attr": "_chk_ai_allow_analysis",
        "enable_command": "enable assistant runtime analysis",
        "disable_command": "disable assistant runtime analysis",
        "aliases": ("assistant runtime analysis", "assistant analysis", "assistant summaries"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_actions",
        "label": "Assistant actions",
        "control_attr": "_chk_ai_allow_actions",
        "enable_command": "enable assistant actions",
        "disable_command": "disable assistant actions",
        "aliases": ("assistant actions", "assistant local actions", "assistant action execution"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "assistant_log_context",
        "label": "Assistant log context",
        "control_attr": "_chk_ai_include_logs",
        "enable_command": "enable assistant log context",
        "disable_command": "disable assistant log context",
        "aliases": ("assistant log context", "assistant include logs", "assistant recent logs"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "auto_lighting",
        "label": "Auto lighting",
        "control_attr": "_chk_auto_lighting",
        "enable_command": "enable auto lighting",
        "disable_command": "disable auto lighting",
        "aliases": ("auto lighting", "automatic lighting"),
        "enable_verbs": START_ENABLE_VERBS,
        "disable_verbs": START_DISABLE_VERBS,
    },
    {
        "key": "auto_export_runtime",
        "label": "Auto export runtime",
        "control_attr": "_chk_auto_export_runtime_qa",
        "apply_method": "_on_auto_export_runtime_toggled",
        "call_apply_method_after_set": True,
        "enable_command": "enable auto export runtime",
        "disable_command": "disable auto export runtime",
        "aliases": ("auto export runtime", "runtime auto export", "automatic export"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "auto_trigger",
        "label": "Auto trigger",
        "control_attr": "_chk_auto_trigger",
        "enable_command": "enable auto trigger",
        "disable_command": "disable auto trigger",
        "aliases": ("auto trigger", "automatic trigger"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "ml_scoring",
        "label": "ML scoring",
        "control_attr": "_chk_ml",
        "enable_command": "enable ml scoring",
        "disable_command": "disable ml scoring",
        "aliases": ("ml scoring", "machine learning scoring", "ml refinement"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "ml_training_logging",
        "label": "ML training logging",
        "control_attr": "_chk_log_ml_training",
        "enable_command": "enable ml training logging",
        "disable_command": "disable ml training logging",
        "aliases": ("ml training logging", "ml training log", "training logging"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "optimize_travel_order",
        "label": "Optimize travel order",
        "control_attr": "_chk_optimize",
        "enable_command": "enable optimize travel order",
        "disable_command": "disable optimize travel order",
        "aliases": (
            "optimize travel order",
            "optimise travel order",
            "slew order optimization",
            "slew order optimisation",
        ),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "precision_refinement",
        "label": "Precision refinement",
        "control_attr": "_chk_precision",
        "enable_command": "enable precision refinement",
        "disable_command": "disable precision refinement",
        "aliases": ("precision refinement", "precision aim", "precision aiming"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "continuous_hunt_on_loss",
        "label": "Continuous hunt on loss",
        "control_attr": "_chk_continuous_hunt_loss",
        "enable_command": "enable continuous hunt on loss",
        "disable_command": "disable continuous hunt on loss",
        "aliases": ("continuous hunt on loss", "keep hunting on loss", "hunt on loss"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "adaptive_loss_recovery",
        "label": "Adaptive loss recovery",
        "control_attr": "_chk_adaptive_loss_recovery",
        "enable_command": "enable adaptive loss recovery",
        "disable_command": "disable adaptive loss recovery",
        "aliases": ("adaptive loss recovery", "adaptive after loss search", "after loss search"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "precision_logging",
        "label": "Precision logging",
        "control_attr": "_chk_precision_logging",
        "enable_command": "enable precision logging",
        "disable_command": "disable precision logging",
        "aliases": ("precision logging", "precision tuning logger", "precision logger"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "startup_to_rest",
        "label": "Startup to rest",
        "control_attr": "_chk_rest_on_startup",
        "enable_command": "enable startup to rest",
        "disable_command": "disable startup to rest",
        "aliases": ("startup to rest", "rest on startup"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "close_to_rest",
        "label": "Close to rest",
        "control_attr": "_chk_rest_on_close",
        "enable_command": "enable close to rest",
        "disable_command": "disable close to rest",
        "aliases": ("close to rest", "rest on close"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "scope_view",
        "label": "Scope view",
        "control_attr": "_chk_scope_view",
        "enable_command": "enable scope view",
        "disable_command": "disable scope view",
        "aliases": ("scope view", "engaging scope view"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "overlay",
        "label": "Overlay",
        "control_attr": "_chk_overlay",
        "enable_command": "enable overlay",
        "disable_command": "disable overlay",
        "aliases": ("overlay", "visual overlay"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "threat_scores",
        "label": "Threat scores",
        "control_attr": "_chk_scores",
        "enable_command": "enable threat scores",
        "disable_command": "disable threat scores",
        "aliases": ("threat scores", "scores"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "engagement_zone",
        "label": "Engagement zone",
        "control_attr": "_chk_zone",
        "enable_command": "enable engagement zone",
        "disable_command": "disable engagement zone",
        "aliases": ("engagement zone", "guard zone"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "guard_crosshair",
        "label": "Guard crosshair",
        "control_attr": "_chk_guard_crosshair",
        "enable_command": "enable guard crosshair",
        "disable_command": "disable guard crosshair",
        "aliases": ("guard crosshair", "crosshair"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "no_fire_mask_overlay",
        "label": "No fire mask overlay",
        "control_attr": "_chk_show_no_fire_masks",
        "enable_command": "enable no fire mask overlay",
        "disable_command": "disable no fire mask overlay",
        "aliases": ("no fire mask overlay", "no fire masks", "safe zone masks"),
        "enable_verbs": SHOW_ENABLE_VERBS,
        "disable_verbs": SHOW_DISABLE_VERBS,
    },
    {
        "key": "mask_trace_diagnostics",
        "label": "Mask trace diagnostics",
        "control_attr": "_chk_mask_trace",
        "enable_command": "enable mask trace diagnostics",
        "disable_command": "disable mask trace diagnostics",
        "aliases": ("mask trace diagnostics", "mask trace", "mask diagnostics trace"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "prompted_targets",
        "label": "Prompted targets",
        "control_attr": "_chk_prompted_enabled",
        "enable_command": "enable prompted targets",
        "disable_command": "disable prompted targets",
        "aliases": ("prompted targets", "prompted target matching"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "prompted_auto_fire",
        "label": "Prompted auto fire",
        "control_attr": "_chk_prompted_auto_fire",
        "enable_command": "enable prompted auto fire",
        "disable_command": "disable prompted auto fire",
        "aliases": ("prompted auto fire", "auto fire for prompted targets"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "pir_sensors",
        "label": "PIR sensors",
        "control_attr": "_chk_pir_enabled",
        "enable_command": "enable pir sensors",
        "disable_command": "disable pir sensors",
        "aliases": ("pir sensors", "pir guard"),
        "enable_verbs": START_ENABLE_VERBS,
        "disable_verbs": START_DISABLE_VERBS,
    },
    {
        "key": "pir_event_blink",
        "label": "PIR event blink",
        "control_attr": "_chk_pir_event_blink",
        "enable_command": "enable pir event blink",
        "disable_command": "disable pir event blink",
        "aliases": ("pir event blink", "pir led blink"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "pir_scan",
        "label": "PIR scan",
        "control_attr": "_chk_pir_scan_enabled",
        "enable_command": "enable pir scan",
        "disable_command": "disable pir scan",
        "aliases": ("pir scan", "scan on no detection", "pir scan on no detection"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "acoustic_guard",
        "label": "Acoustic guard",
        "control_attr": "_chk_acoustic_enabled",
        "enable_command": "enable acoustic guard",
        "disable_command": "disable acoustic guard",
        "aliases": ("acoustic guard", "microphone anomaly trigger"),
        "enable_verbs": START_ENABLE_VERBS,
        "disable_verbs": START_DISABLE_VERBS,
    },
    {
        "key": "invert_pan",
        "label": "Invert pan",
        "control_attr": "_chk_invert_pan",
        "enable_command": "enable invert pan",
        "disable_command": "disable invert pan",
        "aliases": ("invert pan", "pan inversion"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "invert_tilt",
        "label": "Invert tilt",
        "control_attr": "_chk_invert_tilt",
        "enable_command": "enable invert tilt",
        "disable_command": "disable invert tilt",
        "aliases": ("invert tilt", "tilt inversion"),
        "enable_verbs": DEFAULT_ENABLE_VERBS,
        "disable_verbs": DEFAULT_DISABLE_VERBS,
    },
    {
        "key": "pan_tilt_motion",
        "label": "Pan tilt motion",
        "control_attr": "_btn_motion_enable",
        "enable_command": "enable pan tilt motion",
        "disable_command": "disable pan tilt motion",
        "aliases": ("pan tilt motion", "motion control", "servo motion"),
        "enable_verbs": START_ENABLE_VERBS,
        "disable_verbs": START_DISABLE_VERBS,
    },
    {
        "key": "led",
        "label": "LED",
        "control_attr": "_btn_led",
        "enable_command": "enable led",
        "disable_command": "disable led",
        "aliases": ("led", "led light", "manual light"),
        "enable_verbs": OUTPUT_ENABLE_VERBS,
        "disable_verbs": OUTPUT_DISABLE_VERBS,
    },
    {
        "key": "laser",
        "label": "Laser",
        "control_attr": "_btn_laser",
        "enable_command": "enable laser",
        "disable_command": "disable laser",
        "aliases": ("laser", "laser pointer"),
        "enable_verbs": OUTPUT_ENABLE_VERBS,
        "disable_verbs": OUTPUT_DISABLE_VERBS,
    },
    {
        "key": "accessory_output",
        "label": "Accessory output",
        "control_attr": "_btn_acc",
        "enable_command": "enable accessory output",
        "disable_command": "disable accessory output",
        "aliases": ("accessory output", "acc output", "accessory"),
        "enable_verbs": OUTPUT_ENABLE_VERBS,
        "disable_verbs": OUTPUT_DISABLE_VERBS,
    },
    {
        "key": "spare_output",
        "label": "Spare output",
        "control_attr": "_btn_spare",
        "enable_command": "enable spare output",
        "disable_command": "disable spare output",
        "aliases": ("spare output", "spare"),
        "enable_verbs": OUTPUT_ENABLE_VERBS,
        "disable_verbs": OUTPUT_DISABLE_VERBS,
    },
)


def _voice_toggle_aliases(spec: dict[str, object]) -> tuple[str, ...]:
    aliases: list[str] = []
    for alias in tuple(spec.get("aliases", ()) or ()):
        normalized = re.sub(r"\s+", " ", str(alias or "").strip().lower())
        if normalized:
            aliases.append(normalized)
    return tuple(aliases)


def voice_toggle_status_command(spec: dict[str, object]) -> str:
    explicit = re.sub(r"\s+", " ", str(spec.get("status_command", "") or "").strip().lower())
    if explicit:
        return explicit
    aliases = _voice_toggle_aliases(spec)
    if not aliases:
        return ""
    return f"status {aliases[0]}"


def iter_voice_toggle_grammar_fragments() -> tuple[str, ...]:
    phrases: list[str] = []
    for spec in VOICE_TOGGLE_SPECS:
        enable_command = str(spec["enable_command"])
        disable_command = str(spec["disable_command"])
        status_command = voice_toggle_status_command(spec)
        aliases = _voice_toggle_aliases(spec)
        enable_verbs = tuple(str(verb) for verb in spec["enable_verbs"])
        disable_verbs = tuple(str(verb) for verb in spec["disable_verbs"])
        phrases.extend((enable_command, disable_command))
        if status_command:
            phrases.append(status_command)
        for alias in aliases:
            for verb in enable_verbs:
                phrases.append(f"{verb} {alias}")
                phrases.append(f"{verb} the {alias}")
            for verb in disable_verbs:
                phrases.append(f"{verb} {alias}")
                phrases.append(f"{verb} the {alias}")
            phrases.append(f"{alias} on")
            phrases.append(f"{alias} off")
            phrases.append(f"status {alias}")
            phrases.append(f"status of {alias}")
            phrases.append(f"what is the status of {alias}")
            phrases.append(f"what is the current status of {alias}")
            phrases.append(f"what's the status of {alias}")
            phrases.append(f"what's the current status of {alias}")
            phrases.append(f"what is {alias} status")
            phrases.append(f"what's {alias} status")
            phrases.append(f"is {alias} enabled")
            phrases.append(f"is {alias} disabled")
            phrases.append(f"is {alias} running")
            phrases.append(f"is {alias} active")
            phrases.append(f"is {alias} on")
            phrases.append(f"is {alias} off")
            phrases.append(f"is the {alias} enabled")
            phrases.append(f"is the {alias} disabled")
            phrases.append(f"is the {alias} running")
            phrases.append(f"is the {alias} active")
            phrases.append(f"is the {alias} on")
            phrases.append(f"is the {alias} off")
        
    deduped: list[str] = []
    seen: set[str] = set()
    for phrase in phrases:
        normalized = re.sub(r"\s+", " ", str(phrase or "").strip().lower())
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(normalized)
    return tuple(deduped)


def iter_voice_toggle_command_patterns() -> tuple[tuple[str, str], ...]:
    polite_prefix = r"(?:(?:please|can\s+you|could\s+you|would\s+you)\s+)?"
    courtesy_suffix = r"(?:\s+(?:please|now))?"
    patterns: list[tuple[str, str]] = []
    for spec in VOICE_TOGGLE_SPECS:
        status_command = voice_toggle_status_command(spec)
        aliases = sorted(_voice_toggle_aliases(spec), key=len, reverse=True)
        alias_pattern = "(?:" + "|".join(re.escape(alias) for alias in aliases) + ")"
        enable_verbs = sorted((str(verb) for verb in spec["enable_verbs"]), key=len, reverse=True)
        disable_verbs = sorted((str(verb) for verb in spec["disable_verbs"]), key=len, reverse=True)
        enable_pattern = "(?:" + "|".join(re.escape(verb) for verb in enable_verbs) + ")"
        disable_pattern = "(?:" + "|".join(re.escape(verb) for verb in disable_verbs) + ")"
        patterns.append(
            (
                rf"^{polite_prefix}{enable_pattern}\s+(?:the\s+)?{alias_pattern}{courtesy_suffix}$",
                str(spec["enable_command"]),
            )
        )
        patterns.append(
            (
                rf"^{polite_prefix}{disable_pattern}\s+(?:the\s+)?{alias_pattern}{courtesy_suffix}$",
                str(spec["disable_command"]),
            )
        )
        patterns.append(
            (
                rf"^{polite_prefix}{alias_pattern}\s+(?:on|enabled?){courtesy_suffix}$",
                str(spec["enable_command"]),
            )
        )
        patterns.append(
            (
                rf"^{polite_prefix}{alias_pattern}\s+(?:off|disabled?){courtesy_suffix}$",
                str(spec["disable_command"]),
            )
        )
        if status_command:
            patterns.append(
                (
                    rf"^{polite_prefix}status(?:\s+of)?\s+(?:the\s+)?{alias_pattern}{courtesy_suffix}$",
                    status_command,
                )
            )
            patterns.append(
                (
                    rf"^{polite_prefix}(?:what\s+is|what's)\s+the\s+(?:current\s+)?status\s+of\s+(?:the\s+)?{alias_pattern}{courtesy_suffix}$",
                    status_command,
                )
            )
            patterns.append(
                (
                    rf"^{polite_prefix}(?:what\s+is|what's)\s+(?:the\s+)?{alias_pattern}\s+status{courtesy_suffix}$",
                    status_command,
                )
            )
            patterns.append(
                (
                    rf"^{polite_prefix}is\s+(?:the\s+)?{alias_pattern}\s+(?:currently\s+)?(?:enabled?|disabled?|running|active|on|off){courtesy_suffix}$",
                    status_command,
                )
            )
    return tuple(patterns)
