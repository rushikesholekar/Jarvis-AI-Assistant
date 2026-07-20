import asyncio
import edge_tts
import os
from playsound3 import playsound

from app.config import VOICE

async def _generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

def speak(text):
    asyncio.run(_generate_voice(text))
    playsound("voice.mp3")
    os.remove("voice.mp3")