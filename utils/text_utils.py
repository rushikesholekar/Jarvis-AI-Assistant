import string
import re

FILLER_WORDS = {
    "please",
    "can",
    "could",
    "would",
    "you",
    "hey",
    "jarvis",
    "sir",
    "kindly",
    "just",
    "the",
    "a",
    "an",
    "for",
    "to"
}

def normalize_command(command):
    command = command.lower().strip()
    command = command.translate(
        str.maketrans("", "", string.punctuation)
    )
    words = command.split()
    words = [word for word in words if word not in FILLER_WORDS]
    command = " ".join(words)
    return command

def remove_wake_word(command):
    pattern = r'^(hey|hi|hello)?\s*jarvis[,.! ]*'
    return re.sub(pattern, '', command, flags=re.IGNORECASE).strip()

def normalize_key(key):
    key = key.lower().strip()

    if key.startswith("my "):
        key = key[3:]

    key = key.strip(string.punctuation + " ")

    replacements = {
        "favourite": "favorite",
        "colour": "color",
        "centre": "center",
        "programme": "program"
    }

    for old, new in replacements.items():
        key = key.replace(old, new)

    return key
