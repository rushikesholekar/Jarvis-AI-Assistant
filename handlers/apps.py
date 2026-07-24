import subprocess

from app.logger import log, success, warning, errors
from core.speak import speak

APPLICATIONS = (
    (("notepad",), "Notepad", ["notepad.exe"]),
    (("calculator",), "Calculator", ["calc.exe"]),
    (("file explorer",), "File Explorer", ["explorer.exe"]),
    (("paint",), "Paint", ["mspaint.exe"]),
    (("command prompt",), "Command Prompt", ["cmd.exe"]),
    (("visual studio code", "vs code"), "Visual Studio Code", ["code"]),
    (("chrome",), "Google Chrome", [r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]),
)


def handle_apps(command: str) -> bool:
    """Launch only applications declared in the explicit allowlist above."""
    for phrases, name, executable in APPLICATIONS:
        if not any(phrase in command for phrase in phrases):
            continue

        log(f"Opening {name}")
        speak(f"Opening {name}")
        try:
            subprocess.Popen(executable)
        except FileNotFoundError:
            errors(f"{name} was not found on this computer.")
            speak(f"I could not find {name} on this computer.")
        return True

    return False
