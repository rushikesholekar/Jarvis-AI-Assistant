"""Voice activity detection for a single user command."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from silero_vad import load_silero_vad

from app.config import (
    BLOCK_SIZE,
    MAX_RECORDING_SECONDS,
    SAMPLE_RATE,
    SILENCE_SECONDS,
    SPEECH_THRESHOLD,
)
from core.audio_manager import get_chunk

model = load_silero_vad()


def record_until_silence(output_file: str | Path = "temp.wav") -> str:
    """Record one command and stop when speech is followed by silence."""
    print("Listening for speech...")
    frames: list[np.ndarray] = []
    speech_started = False
    silence_samples = 0
    max_chunks = max(1, int(MAX_RECORDING_SECONDS * SAMPLE_RATE / BLOCK_SIZE))
    max_silence_samples = int(SILENCE_SECONDS * SAMPLE_RATE)

    for _ in range(max_chunks):
        chunk = get_chunk()
        frames.append(chunk)

        for start in range(0, len(chunk), 512):
            piece = chunk.flatten()[start : start + 512]
            if len(piece) < 512:
                continue

            probability = model(torch.from_numpy(piece).unsqueeze(0), SAMPLE_RATE).item()
            
            if probability >= SPEECH_THRESHOLD:
                speech_started = True
                silence_samples = 0
            elif speech_started:
                silence_samples += len(piece)

            if speech_started and silence_samples >= max_silence_samples:
                audio = np.concatenate(frames, axis=0)
                sf.write(output_file, audio, SAMPLE_RATE)
                return str(output_file)

    if not speech_started:
        raise TimeoutError("No speech was detected before the recording limit.")

    audio = np.concatenate(frames, axis=0)
    sf.write(output_file, audio, SAMPLE_RATE)
    return str(output_file)
