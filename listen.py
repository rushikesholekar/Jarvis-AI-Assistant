import sounddevice as sd
import soundfile as sf
from colorama import init, Fore, Style
init(autoreset=True)
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN

from config import MIC_DEVICE, SAMPLE_RATE, DURATION

def listen():
    print(CYAN + "🎤" +" " + YELLOW + "Listening...")

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