import sounddevice as sd
import numpy as np
import queue

print(sd.query_devices(15))

from openwakeword.model import Model


SAMPLE_RATE = 16000
BLOCK_SIZE = 1280


audio_queue = queue.Queue()


print("Loading Jarvis wake word model...")

model = Model(
    wakeword_models=[
        "hey_jarvis_v0.1.onnx"
    ],
    inference_framework="onnx"
)

print("Jarvis wake word ready!")
print("Listening for 'Hey Jarvis'...")


def audio_callback(indata, frames, time, status):

    if status:
        print("Audio status:", status)

    audio_queue.put(indata.copy())


with sd.InputStream(
    device=15,
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    blocksize=BLOCK_SIZE,
    callback=audio_callback
):

    while True:

        audio = audio_queue.get()

        audio = np.squeeze(audio)

        audio = (audio * 32767).astype(np.int16)

        prediction = model.predict(audio)

        score = prediction["hey_jarvis_v0.1.onnx"]

        # Only show meaningful scores
        if score > 0.05:
            print(f"Wake confidence: {score:.3f}")

        # Wake Jarvis
        if score > 0.60:
            print("\n🎉 Wake word detected!")
            print("Good morning Commander!\n")
            break