from dotenv import load_dotenv
import os
import requests
from app.logger import log, warning, success, errors

load_dotenv()
def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            return "Sorry sir, I couldn't find that city."

        city = data["name"]
        temperature = round(data["main"]["temp"], 1)
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = round(data["wind"]["speed"], 1)

        weather = (
            f"The current weather in {city} is {description}. "
            f"The temperature is {temperature} degrees Celsius. "
            f"The humidity is {humidity} percent, "
            f"and the wind speed is {wind_speed} meters per second."
        )
        log(f"{weather}")
        return weather

    except Exception as e:
        errors(f"Weather error = {e}")
        return("Sorry sir, I couldn't get the weather right now.")