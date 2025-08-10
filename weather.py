import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        return None

def main():
    api_key = "f0a8e2957d3f9f33eecd24c08b2665b5"  
    city = input("Enter city name: ")
    weather = get_weather(api_key, city)
    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Condition: {weather['description'].title()}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    main()
