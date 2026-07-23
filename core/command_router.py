"""The single routing boundary between user language and Jarvis capabilities."""

from __future__ import annotations

import random

from app.config import NOISE_COMMANDS
from app.logger import log
from core.intents import Intent, RouteResult
from core.speak import speak
from features.ai import ask_ai
from handlers.apps import handle_apps
from handlers.browser import handle_browser
from handlers.datetime_handler import handle_datetime
from handlers.memory_handler import handle_memory
from handlers.weather_handler import handle_weather
from utils.text_utils import normalize_command


THINKING_RESPONSES = (
    "Thinking.",
    "One moment.",
    "Let me think.",
    "Just a second.",
)


def route_command(raw_command: str) -> RouteResult:
    """Route one command and return its outcome.

    Handlers receive normalized text for reliable matching. The AI fallback gets
    the original text so normalisation never damages the meaning of a question.
    """
    original = raw_command.strip()
    command = normalize_command(original)

    if command in NOISE_COMMANDS:
        return RouteResult(Intent.IGNORED, command)

    for intent, handler in (
        (Intent.APPLICATION, handle_apps),
        (Intent.BROWSER, handle_browser),
        (Intent.DATE_TIME, handle_datetime),
        (Intent.WEATHER, handle_weather),
    ):
        if handler(command):
            log(f"Routed command to {intent.value}")
            return RouteResult(intent, command)

    if command == "hello":
        response = "Hello. How can I help?"
        speak(response)
        return RouteResult(Intent.CONVERSATION, command, response)

    if command == "how are you":
        response = "I am operating normally. How can I help?"
        speak(response)
        return RouteResult(Intent.CONVERSATION, command, response)

    memory_response = handle_memory(command)
    if memory_response:
        speak(memory_response)
        return RouteResult(Intent.MEMORY, command, memory_response)

    log("Routed command to local AI")
    speak(random.choice(THINKING_RESPONSES))
    try:
        answer = ask_ai(original)
    except Exception as error:
        log(f"AI error: {error}")
        answer = "Sorry, I could not reach my AI brain."

    speak(answer)
    return RouteResult(Intent.AI, command, answer)
