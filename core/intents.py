"""Types shared by Jarvis command routing and future tool plugins."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re


class Intent(str, Enum):
    IGNORED = "ignored"
    APPLICATION = "application"
    BROWSER = "browser"
    DATE_TIME = "date_time"
    WEATHER = "weather"
    MEMORY = "memory"
    CONVERSATION = "conversation"
    AI = "ai"


@dataclass(frozen=True)
class RouteResult:
    """The observable result of routing one user command."""

    intent: Intent
    normalized_command: str
    response: str | None = None


_PERSONAL_MEMORY_CUES = re.compile(
    r"\b(my|i am|i'm|i live|i study|i am learning|i want to become)\b",
    re.IGNORECASE,
)


def is_personal_memory_candidate(command: str) -> bool:
    """Return whether a command plausibly contains a user-owned fact."""
    return bool(_PERSONAL_MEMORY_CUES.search(command))
