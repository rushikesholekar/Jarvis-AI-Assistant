import sounddevice as sd
import soundfile as sf
import numpy as np
from silero_vad import load_silero_vad
import torch


SAMPLE_RATE = 16000
CHANNELS = 1

SPEECH_THRESHOLD = 0.20
MAX_SILENCE = 50

model = load_silero_vad()

def record_until_silence():
    """
    Records audio until the user stops speaking.
    """

    print("Listening for speech...")

    DEVICE = 15

    frames = []

    silence_chunks = 0

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        blocksize=512,
        device=DEVICE
    ) as stream:

        print("Recording...")

        for i in range(200):

            audio, overflow = stream.read(512)

            frames.append(audio)

            audio_tensor = torch.from_numpy(audio.flatten())

            speech_probability = model(audio_tensor, SAMPLE_RATE).item()
            
            print(f"Speech probability: {speech_probability:.3f}")

            if speech_probability >= SPEECH_THRESHOLD:
                silence_chunks = 0
            else:
                silence_chunks += 1

            if silence_chunks >= MAX_SILENCE:
                print("Silence detected. Stopping recording...")
                break


    print("Finished")

    audio = np.concatenate(frames, axis=0)

    print("Recording finished.")

    sf.write(
    "temp.wav",
    audio,
    SAMPLE_RATE
    )

    print("Saved as temp.wav")

record_until_silence()