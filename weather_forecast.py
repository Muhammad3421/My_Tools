cities = {
    "New York": {"lat": 40.7128, "lon": 74.0060},
    "Los Angeles": {"lat": 34.0522, "lon": 118.2437},
    "Chicago": {"lat": 41.8781, "lon": 87.6298},
    "Houston": {"lat": 29.7633, "lon": 95.3632},
    "Phoenix": {"lat": 33.4484, "lon": 112.0739}
}

def get_forecast(city):
    forecast = [
        {"date": "2024-04-30", "min_temp": 60, "max_temp": 75, "weather": "Sunny"},
        {"date": "2024-05-01", "min_temp": 58, "max_temp": 72, "weather": "Partly Cloudy"},
        {"date": "2024-05-02", "min_temp": 55, "max_temp": 70, "weather": "Rain"},
        {"date": "2024-05-03", "min_temp": 52, "max_temp": 68, "weather": "Cloudy"},
        {"date": "2024-05-04", "min_temp": 50, "max_temp": 65, "weather": "Sunny"},
        {"date": "2024-05-05", "min_temp": 48, "max_temp": 62, "weather": "Partly Cloudy"},
        {"date": "2024-05-06", "min_temp": 45, "max_temp": 60, "weather": "Rain"}
    ]
    return forecast
 
def main():
    print("Choose a city:")
    for i, city in enumerate(cities.keys()):
        print(f"{i+1}. {city}")

    choice = int(input("Enter the number of your chosen city: "))
    chosen_city = list(cities.keys())[choice-1]

    forecast = get_forecast(chosen_city)

    print(f"\n7-day forecast for {chosen_city}:")
    for day in forecast:
        print(f"Date: {day['date']}, Min Temp: {day['min_temp']}°F, Max Temp: {day['max_temp']}°F, Weather: {day['weather']}")