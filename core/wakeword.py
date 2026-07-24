"""Wake-word detection with explicit model validation and model reuse."""

from __future__ import annotations

import numpy as np
import time
from openwakeword.model import Model

from app.config import WAKE_WORD_MODEL_PATH, WAKE_WORD_THRESHOLD
from core.audio_manager import clear_queue, get_chunk, start
from core.speak import speak
from app.logger import log, warning, success, errors, listening

_model: Model | None = None


class WakeWordConfigurationError(RuntimeError):
    """Raised when Jarvis has no usable custom wake-word model."""


def _get_model() -> Model:
    global _model
    if _model is None:
        if not WAKE_WORD_MODEL_PATH.is_file():
            raise WakeWordConfigurationError(
                "Wake-word model not found at "
                f"'{WAKE_WORD_MODEL_PATH}'. Set JARVIS_WAKE_WORD_MODEL to a valid .onnx file."
            )
        _model = Model(
            wakeword_models=[str(WAKE_WORD_MODEL_PATH)],
            inference_framework="onnx",
        )
    return _model


def wait_for_wakeword() -> None:
    start()
    model = _get_model()
    
    listening("Listening for the Jarvis wake word...")

    while True:
        audio = np.squeeze(get_chunk())
        audio = np.clip(audio * 32767, -32768, 32767).astype(np.int16)

        predictions = model.predict(audio)

        score = float(next(iter(predictions.values())))

        if score >= WAKE_WORD_THRESHOLD:
            success("Wake word detected.")
            model.reset() 
            clear_queue()
            speak("Yes?")
            return


if __name__ == "__main__":
    wait_for_wakeword()
