import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather
    else:
        return None

def main():
    city = input("Enter city name: ")
    api_key = "7425ed2c92f0dfef0ab2f0ff415d49ae"  
    weather = get_weather(city, api_key)
    if weather:
        print(f"Weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or API request failed")

if __name__ == "__main__":
    main()