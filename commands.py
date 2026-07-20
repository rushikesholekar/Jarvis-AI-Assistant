
import random

from click import command


from app.logger import log
from core.speak import speak
from features.ai import ask_ai
from app.config import NOISE_COMMANDS
from utils.text_utils import normalize_command


from handlers.apps import handle_apps
from handlers.browser import handle_browser
from handlers.memory_handler import handle_memory
from handlers.weather_handler import handle_weather
from handlers.datetime_handler import handle_datetime


def execute(command):
    
    command = normalize_command(command)

    for phrase in NOISE_COMMANDS:
        if command == phrase:
            return
    
    if handle_apps(command):
        return
    
    elif handle_browser(command):
        return
    
    elif handle_datetime(command):
        return
    
    elif handle_weather(command):
        return

    if "hello" in command.lower():
        speak("Hello sir! How can i help you?")

    elif "how are you" in command.lower():
        speak("I am fine sir! How are you?")

        
    else:

        memory_response = handle_memory(command)

        if memory_response:
            speak(memory_response)
            return


    
        log("Using AI")
        question = command
        thinking = [
        "Thinking.",
        "One moment.",
        "Let me think.",
        "Just a second."
        ]

        speak(random.choice(thinking))

        try:
            answer = ask_ai(question)
            speak(answer)

        except Exception as e:
            log(f"AI Error: {e}")
            speak("Sorry sir, I couldn't reach my AI brain.")
            
    
        




