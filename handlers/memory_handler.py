from features.memory import save_memory, get_memory, delete_memory
from features.ai import extract_memory
from utils.text_utils import normalize_key
from app.logger import log
import string
import re

def handle_memory(command):

    response = handle_regex_memory(command)

    if response:
        return response
    
    response = handle_statement_memory(command)
    
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

        log(f"I'll remember that your {key} is {value}.")
        return f"I'll remember that your {key} is {value}."
    
    elif command.startswith("what is"):

        key = command.replace("what is", "", 1)

        key = normalize_key(key)

        value = get_memory(key)

        if value is None:
            return f"I don't know your {key} yet."
        
        log(f"Your {key} is {value}.")
        return f"Your {key} is {value}."
    
    elif command.startswith("forget"):

        key = command.replace("forget", "", 1)

        key = normalize_key(key)

        deleted = delete_memory(key)

        if deleted:
            log(f"I forgot your {key}")
            return f"I forgot your {key}"
        else:
            log(f"I don't have a memory about {key}")
            return f"I don't have a memory about {key}"
        
def handle_statement_memory(command):
    print("[DEBUG] handle_statement_memory called")

    patterns = [
    (r"my favorite color is (.+)", "favorite color"),
    (r"my name is (.+)", "name"),
    (r"i live in (.+)", "location"),
    (r"i study (.+)", "education"),
    (r"i am learning (.+)", "learning"),
    (r"my birthday is (.+)", "birthday"),
        ]

    for pattern, key in patterns:

        match = re.search(
            pattern,
            command,
            re.IGNORECASE
    )

        if match:

         key = normalize_key(key)
         value = match.group(1).strip()

         save_memory(key, value)

         log(f"I'll remember that your {key} is {value}.")
         return f"I'll remember that your {key} is {value}."

    return None
            
def handle_ai_memory(command):
    
    memory = extract_memory(command) or {}

    key = normalize_key(memory.get("key", ""))
    value = memory.get("value", "").strip()

    if not key or not value:
        return None

    save_memory(key, value)
    log(f"I'll remember that your {key} is {value}.")
    return f"I'll remember that your {key} is {value}."
