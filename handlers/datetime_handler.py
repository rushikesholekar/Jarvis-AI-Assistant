from datetime import datetime
import re
from core.speak import speak

def handle_datetime(command):
    if "time" in command and "date" in command:
        now = datetime.now()
        day_string = now.strftime("%A")
        date_string = now.strftime("%d %B %Y")
        hour = now.strftime("%I").lstrip("0")
        minute = now.strftime("%M")
        period = now.strftime("%p")
        print(f"Today is {day_string}, {date_string}, and the current time is {hour} {minute} {period}.")
        speak(f"Today is {day_string}, {date_string}, and the current time is {hour} {minute} {period}.")
        return True
    
    elif "time" in command:
        now = datetime.now()
        hour = now.strftime("%I").lstrip("0")
        minute = now.strftime("%M")
        period = now.strftime("%p")

        if minute == "00":
            speak(f"It's {hour} o'clock {period}")
        else:
            speak(f"It's {hour} {minute} {period}")
        return True

    elif "date" in command:
        current_date = datetime.now()
        date_string = current_date.strftime("%A, %d %B %Y")
        speak(f"Today is {date_string}")
        return True

    elif re.search(r"\bday\b", command):
        current_day = datetime.now()
        day_string = current_day.strftime("%A")
        speak(f"Today is {day_string}")
        return True
    return False
