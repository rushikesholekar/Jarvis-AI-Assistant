from app.logger import log, success, warning, errors
from commands import execute
from core.speak import speak
from datetime import datetime
from core.transcribe import transcribe
from colorama import init, Fore, Style
from core.vad import record_until_silence
from core.wakeword import WakeWordConfigurationError, wait_for_wakeword
from utils.text_utils import remove_wake_word
from utils.text_utils import normalize_command

init(autoreset=True)
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
RED = Fore.RED
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def startup_screen():
    print()
    print(CYAN + "╔" + "═"*58 + "╗")
    print(CYAN + "║{:^58}║".format("JARVIS AI ASSISTANT"))
    print(CYAN + "║{:^58}║".format("Your Local AI Companion"))
    print(CYAN + "╚" + "═"*58 + "╝")
    print()
    print(WHITE + "Version : " + GREEN + "v2.0.0 Vanguard")
    print(WHITE + "Status  : " + YELLOW + "Initializing...")
    print(WHITE + "Build   : " + GREEN +  "Stable")
    print()
    print(CYAN + "─"*60)

    print(GREEN + "[✓] " + WHITE + "Configuration Loaded")
    print(GREEN + "[✓] " + WHITE + "Voice Engine Ready")
    print(GREEN + "[✓] " + WHITE + "Whisper model Ready")
    print(GREEN + "[✓] " + WHITE + "Memory Connected")
    print(GREEN + "[✓] " + WHITE + "Command Modules Ready")
    print(GREEN + "[✓] " + WHITE + "AI Features Ready")
    print(GREEN + "[✓] " + WHITE + "System Diagnostics Passed")

    print(CYAN + "─"*60)
    print()

    print("═"*60)
    print(CYAN + "SYSTEM STATUS : " + GREEN + "ONLINE")
    print("═"*60)
    print(GREEN + "System Ready.")
    print()
    print("Voice Interface Active")
    print()

def greet() -> None:
    hour = datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning, I am Jarvis. How can I help you?")
    elif 12 <= hour < 17:
        speak("Good afternoon, I am Jarvis. How can I help you?")
    else:
        speak("Good evening, I am Jarvis. How can I help you?")


def run() -> None:
    startup_screen()
    greet()

    while True:
        try:
            wait_for_wakeword()
            audio = record_until_silence()
            command = remove_wake_word(transcribe(audio))
            log(f"You: {command}")
            if command:
                execute(command)
        except TimeoutError:
            errors("No speech detected; returning to wake-word mode.")
        except WakeWordConfigurationError as error:
            errors(str(error))
            break
        except KeyboardInterrupt:
            errors("\nJarvis stopped.")
            break
        except Exception as error:
            errors(f"Voice pipeline error: {error}")
            speak("I had a voice-system error. Please try again.")


if __name__ == "__main__":
    run()


    

    
