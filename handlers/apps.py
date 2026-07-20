import subprocess
from core.speak import speak
from app.logger import log

def handle_apps(command):
    if "notepad" in command:
        log("Opening Notepad")
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        return True

    elif "calculator" in command:
        log("Opening Calculator")
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        return True

    elif "file explorer" in command:
        log("Opening File Explorer")
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")
        return True

    elif "paint" in command:
        log("Opening Paint")
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")
        return True

    elif "command prompt" in command:
        log("Opening Command Prompt")
        speak("opening command prompt")
        subprocess.Popen("cmd.exe")
        return True

    elif "visual studio code" in command or "vs code" in command:
        log("Opening Visual Studio Code")
        speak("Opening visual studio code")
        subprocess.Popen("code", shell=True)
        return True
    
    elif "chrome" in command:
        log("Opening Google Chrome")
        speak("Opening google chrome")
        subprocess.Popen(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        return True

    return False