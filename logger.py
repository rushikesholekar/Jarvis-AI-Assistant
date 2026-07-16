from colorama import init, Fore, Style

init(autoreset=True)

CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE

def log(message):
    print(f"{CYAN}[Jarvis]{WHITE} {message}")

def success(message):
    print(f"{GREEN}[Success]{WHITE} {message}")

def warning(message):
    print(f"{YELLOW}[Listening]{WHITE} {message}")