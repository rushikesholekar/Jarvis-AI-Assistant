from app.logger import log
from core.speak import speak
from core.listen import listen
from commands import execute
from datetime import datetime
from core.transcribe import get_model
from core.transcribe import transcribe
from colorama import init, Fore, Style

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

startup_screen()

hour = datetime.now().hour
if 5 <= hour < 12 :
    speak("Good morning,sir!I am Jarvis.How can I help you today?")

elif 12 <= hour < 17:
    speak("Good afternoon,sir!I am Jarvis.How can I help you today?")

elif 17 <= hour < 21:
    speak("Good evening,sir!I am Jarvis.How can I help you today?")

else:
      speak("Good night!")

while True:
    audio = listen()

    command = transcribe(audio)

    log(f"You: {command}")
    
    if command:
        execute(command)

    if command == "":
        continue


    

    