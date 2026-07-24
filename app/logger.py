from pathlib import Path
from datetime import datetime
from colorama import init, Fore, Style


init(autoreset=True)

INFO = Fore.CYAN
SUCCESS = Fore.GREEN
WARNING = Fore.YELLOW
ERROR = Fore.RED
WHITE = Fore.WHITE
LISTEN = Fore.MAGENTA

LOG_FOLDER = Path("log")
LOG_FOLDER.mkdir(exist_ok=True)

LOG_FILE = LOG_FOLDER / "jarvis.log"

def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


def _timestamp():
    return datetime.now().strftime("%H:%M:%S")

def _print_log(color, label, message):
    timestamp = _timestamp()
    print(f"{color}[{timestamp}][{label}]{WHITE} {message}")
    formatted = f"[{timestamp}][{label}] {message}"
    write_log(formatted)



def log(message):
    _print_log(INFO, "INFO", message)

def listening(message):
     _print_log(LISTEN, "LISTENING", message)


def success(message):
     _print_log(SUCCESS, "SUCCESS", message)


def warning(message):
     _print_log(WARNING, "WARNING", message)


def errors(message):
     _print_log(ERROR, "ERROR", message)