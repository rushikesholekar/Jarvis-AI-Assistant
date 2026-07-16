
from faster_whisper import WhisperModel

model = None


def get_model():
    global model

    if model is None:
        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

    return model


def transcribe(audio_file):
    model = get_model()

    segments, info = model.transcribe(
    audio_file,
    language="en",
    beam_size=5)

    text = ""

    text = " ".join(segment.text.strip() for segment in segments)

    return text