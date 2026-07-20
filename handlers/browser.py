import webbrowser
from urllib.parse import quote
from core.speak import speak
from app.logger import log

def handle_browser(command):
    if "open youtube" in command:
        log("Opening Youtube...")
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "google" in command:
        log("Opening Google...")
        speak("opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "github" in command:
        log("Opening Github...")
        speak("opening github")
        webbrowser.open("https://www.github.com")
        return True

    elif "chat gpt" in command:
        log("Opening Chatgpt...")
        speak("opening chatgpt")
        webbrowser.open("https://www.chatgpt.com")
        return True

    
    elif "search" in command and "youtube" not in command:
        query = command.replace("search", "")
        encoded_query = quote(query)
        speak(f"Opening google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={encoded_query}")
        return True

    elif "search" in command and "youtube" in command:
        query = command.replace("search", "")
        query = query.replace("on youtube", "")
        query = query.strip()
        speak(f"searching on youtube for {query}")
        encoded_query = quote(query)
        webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_query}")
        return True
    return False