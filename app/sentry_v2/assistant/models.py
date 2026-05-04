from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AssistantFinding:
    severity: str
    title: str
    detail: str


@dataclass
class AssistantAction:
    action_type: str
    label: str
    payload: Dict[str, Any] = field(default_factory=dict)
    requires_permission: bool = True


@dataclass
class AssistantReply:
    text: str
    source: str
    findings: List[AssistantFinding] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    actions: List[AssistantAction] = field(default_factory=list)
    raw_response: str = ""
    prompt_used: str = ""
    runtime_excerpt: str = ""
    model: str = ""
    intent: Dict[str, Any] = field(default_factory=dict)
    memory_context: Dict[str, List[str]] = field(default_factory=dict)
    error: Optional[str] = None

    @property
    def ok(self) -> bool:
        return not bool(self.error)
