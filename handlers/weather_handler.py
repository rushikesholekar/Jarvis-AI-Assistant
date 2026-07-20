from features.weather import get_weather
from core.speak import speak
from app.config import DEFAULT_CITY

def handle_weather(command):
    if "weather" in command or "climate" in command or "temperature" in command:
        city = command
        if " in " in command:
            city = command.split(" in ")[1]
            city = city.replace("please", "")
            city = city.replace("today", "")
            city = city.strip()
            
        else:
            city = DEFAULT_CITY
        weather = get_weather(city)

        speak(weather)

        return True
    
    return False
