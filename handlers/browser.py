import webbrowser
from urllib.parse import quote
from core.speak import speak
from app.logger import log

def handle_browser(command: str) -> bool:
    if "search" in command:
        if "youtube" in command:
            query = command.replace("search", "", 1).replace("on youtube", "").strip()
            if not query:
                speak("What would you like to search for on YouTube?")
                return True
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={quote(query)}")
            return True

        query = command.replace("search", "", 1).strip()
        if not query:
            speak("What would you like to search for?")
            return True
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={quote(query)}")
        return True

    if "open youtube" in command:
        log("Opening Youtube...")
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "open google" in command:
        log("Opening Google...")
        speak("opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "open github" in command:
        log("Opening Github...")
        speak("opening github")
        webbrowser.open("https://www.github.com")
        return True

    elif "open chat gpt" in command:
        log("Opening Chatgpt...")
        speak("opening chatgpt")
        webbrowser.open("https://www.chatgpt.com")
        return True
    return False
