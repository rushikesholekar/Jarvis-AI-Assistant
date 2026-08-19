"""Shared registry that self-registering command handlers populate on import."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from core.intents import Intent


@dataclass(frozen=True)
class PluginHandler:
    """A named, self-registered command handler."""

    name: str
    intent: Intent
    handler: Callable[[str], bool]


HANDLERS: list[PluginHandler] = []