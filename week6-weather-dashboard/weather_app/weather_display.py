from datetime import datetime

def display_weather(data, cached):
    print("\n🌤️ WEATHER DASHBOARD")
    print("=======================")
    print("City:", data["name"])
    print("Updated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Source:", "Cached" if cached else "Live API")
    print("\nCurrent Weather")
    print("----------------")
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Condition:", data["weather"][0]["description"].title())