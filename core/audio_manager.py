"""A single, lazily-created microphone stream shared by voice features."""

from __future__ import annotations

import queue

import sounddevice as sd

from app.config import BLOCK_SIZE, MIC_DEVICE, SAMPLE_RATE

CHANNELS = 1
audio_queue = queue.Queue(maxsize=50)
_stream: sd.InputStream | None = None


def audio_callback(indata, frames, time, status):

    if status:
        print(f"Audio status: {status}")

    try:
        audio_queue.put_nowait(indata.copy())

    except queue.Full:
        try:
            audio_queue.get_nowait()   # discard oldest chunk
        except queue.Empty:
            pass

        audio_queue.put_nowait(indata.copy())


def _get_stream() -> sd.InputStream:
    global _stream
    if _stream is None:
        _stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            blocksize=BLOCK_SIZE,
            device=MIC_DEVICE,
            callback=audio_callback,
        )
    return _stream


def start() -> None:
    stream = _get_stream()
    if not stream.active:
        stream.start()


def stop() -> None:
    if _stream is not None and _stream.active:
        _stream.stop()


def get_chunk():
    return audio_queue.get()


def clear_queue() -> None:
    while not audio_queue.empty():
        try:
            audio_queue.get_nowait()
        except queue.Empty:
            break
