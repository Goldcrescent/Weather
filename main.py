import requests

YOUR_API_KEY = "a03e85b8d2cb88a5f53b544442f8ab56"
city = "Northwich"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR_API_KEY}"
    response = requests.get(url)
    return response.json()

def get_tempandweather(city):
    weather_data = get_weather_data(city)
    return weather_data["main"]["temp"], weather_data["weather"][0]["main"]

print(get_tempandweather(city))