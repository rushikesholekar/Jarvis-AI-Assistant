import string

def normalize_command(command):
    command = command.lower().strip()
    command = command.strip(string.punctuation + " ")
    return command

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