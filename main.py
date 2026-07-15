from logger import log
from speak import speak
from listen import listen
from commands import execute
from datetime import datetime
from transcribe import transcribe

log("=" * 40)
log("🤖 Jarvis AI Assistant")
log("=" * 40)

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


    

    