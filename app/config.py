"""Runtime configuration for Jarvis."""

from __future__ import annotations

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Speech settings
VOICE = os.getenv("JARVIS_VOICE", "en-US-GuyNeural")

# Audio settings. Leave JARVIS_MIC_DEVICE unset to use the system default.
_microphone = os.getenv("JARVIS_MIC_DEVICE")
MIC_DEVICE = int(_microphone) if _microphone else None
SAMPLE_RATE = int(os.getenv("JARVIS_SAMPLE_RATE", "16000"))
BLOCK_SIZE = int(os.getenv("JARVIS_BLOCK_SIZE", "1280"))
MAX_RECORDING_SECONDS = float(os.getenv("JARVIS_MAX_RECORDING_SECONDS", "12.0"))
SILENCE_SECONDS = float(os.getenv("JARVIS_SILENCE_SECONDS", "1.5"))
SPEECH_THRESHOLD = float(os.getenv("JARVIS_SPEECH_THRESHOLD", "0.15"))

# This custom model is deliberately local and should not be committed.
WAKE_WORD_MODEL_PATH = Path(
    os.getenv("JARVIS_WAKE_WORD_MODEL", PROJECT_ROOT / "models" / "hey_jarvis.onnx")
)
WAKE_WORD_THRESHOLD = float(os.getenv("JARVIS_WAKE_WORD_THRESHOLD", "0.45"))

# AI settings
AI_MODEL = "llama3.2"
MAX_HISTORY = 20

# Weather settings
DEFAULT_CITY = "Mumbai"

# Commands to ignore rather than send to an LLM.
NOISE_COMMANDS = {
    "",
    "you",
    "thank",
    "thanks",
    "thank you",
    "thank you very much",
    "ok",
    "okay",
    "okay thanks",
    "thanks man",
    "thank u",
}
