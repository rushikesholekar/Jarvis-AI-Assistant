import subprocess
from speak import speak

def handle_apps(command):
    if "notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        return True

    elif "calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        return True

    elif "file explorer" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")
        return True

    elif "paint" in command:
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")
        return True

    elif "command prompt" in command:
        speak("opening command prompt")
        subprocess.Popen("cmd.exe")
        return True

    elif "visual studio code" in command or "vs code" in command:
        speak("Opening visual studio code")
        subprocess.Popen("code", shell=True)
        return True
    
    elif "chrome" in command:
        speak("Opening google chrome")
        subprocess.Popen(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        return True

    return False