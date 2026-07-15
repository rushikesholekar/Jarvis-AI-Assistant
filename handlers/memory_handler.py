from features.memory import save_memory, get_memory, delete_memory
from features.ai import extract_memory
from utils.text_utils import normalize_key
import string
import re

def handle_memory(command):

    response = handle_regex_memory(command)

    if response:
        return response
    
    response = handle_ai_memory(command)

    if response:
        return response

    return None
    
def handle_regex_memory(command):
    if command.startswith("remember"):

        match = re.search(
            r"remember (?:my )?(.*?) is (.*)",
            command,
            re.IGNORECASE
        )

        if not match:
            return "Please say something like: Remember my favorite color is blue."

        key = normalize_key(match.group(1))
        value = match.group(2).strip()

        save_memory(key, value)

        return f"I'll remember that your {key} is {value}."
    
    elif command.startswith("what is"):

        key = command.replace("what is", "", 1)

        key = normalize_key(key)

        value = get_memory(key)

        if value is None:
            return f"I don't know your {key} yet."

        return f"Your {key} is {value}."
    
    elif command.startswith("forget"):

        key = command.replace("forget", "", 1)

        key = normalize_key(key)

        deleted = delete_memory(key)

        if deleted:
            return f"I forgot your {key}"
        else:
            return f"I don't have a memory about {key}"
            
def handle_ai_memory(command):
    
    memory = extract_memory(command) or {}

    key = normalize_key(memory.get("key", ""))
    value = memory.get("value", "").strip()

    if not key or not value:
        return None

    save_memory(key, value)
    return f"I'll remember that your {key} is {value}."
        
