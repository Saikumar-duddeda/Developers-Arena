from weather_app.weather_api import get_weather
from weather_app.weather_display import display_weather
import os

os.makedirs("data", exist_ok=True)

while True:
    city = input("\nEnter city (or 'exit'): ")
    if city.lower() == "exit":
        break
    weather, cached = get_weather(city)
    if weather:
        display_weather(weather, cached)
    else:
        print("Error fetching weather.")