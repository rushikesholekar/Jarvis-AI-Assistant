import sounddevice as sd
import soundfile as sf

from config import MIC_DEVICE, SAMPLE_RATE, DURATION

def listen():
    print("🎤 Listening...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=MIC_DEVICE
    )

    sd.wait()

    filename = "input.wav"
    sf.write(filename, recording, SAMPLE_RATE)

    return filename