import json
import os

def load_memory():

    if not os.path.exists("memory.json"):
        with open("memory.json", "w") as file:
            json.dump({}, file)

    with open("memory.json", "r") as file:
        memory = json.load(file)

    return memory

def save_memory(key, value):
    memory = load_memory()

    memory[key] = value

    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)

def get_memory(key):
    memory = load_memory()

    return memory.get(key)

def delete_memory(key):
    memory = load_memory()

    if key in memory:
        del memory[key]

        with open("memory.json", "w") as file:
            json.dump(memory, file, indent=4)

        return True

    return False