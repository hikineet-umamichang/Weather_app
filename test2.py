import requests

API_KEY = "YOUR_API_KEY"
CITY_NAME = "CITY_NAME"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY_NAME,
    "appid": API_KEY,
    "units": "metric"  # 気温を摂氏で取得
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]

    temperature = main["temp"]
    weather_description = weather["description"]

    print(f"現在の天気: {weather_description}")
    print(f"現在の気温: {temperature}℃")
else:
    print("Error:", response.status_code)
