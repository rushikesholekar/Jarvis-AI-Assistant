import webbrowser
from urllib.parse import quote
from speak import speak

def handle_browser(command):
    if "open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "google" in command:
        speak("opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "github" in command:
        speak("opening github")
        webbrowser.open("https://www.github.com")
        return True

    elif "chat gpt" in command:
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