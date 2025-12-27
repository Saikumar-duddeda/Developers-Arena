import requests
import json
import os
import time
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


API_KEY = os.getenv("WEATHER_API_KEY")
print("API KEY LOADED:", API_KEY)
BASE_URL = "https://api.openweathermap.org/data/2.5"
CACHE_FILE = "data/cache.json"
CACHE_TIME = 600

def get_cached_data(city):
    if not os.path.exists(CACHE_FILE):
        return None
    with open(CACHE_FILE, "r") as f:
        data = json.load(f)
    if city in data and time.time() - data[city]["timestamp"] < CACHE_TIME:
        return data[city]["weather"]
    return None

def save_cache(city, weather):
    data = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            data = json.load(f)
    data[city] = {"timestamp": time.time(), "weather": weather}
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_weather(city):
    cached = get_cached_data(city)
    if cached:
        return cached, True
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(f"{BASE_URL}/weather", params=params)
    if r.status_code != 200:
        return None, False
    weather = r.json()
    save_cache(city, weather)
    return weather, False
