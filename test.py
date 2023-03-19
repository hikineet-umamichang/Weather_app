# -*- coding: utf-8 -*-

import requests
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
CITY_NAME = "London"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {"q": CITY_NAME, "appid": API_KEY, "units": "metric"}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]

    temprature = main["temp"]
    weather_description = weather["description"]

    print(f"現在の天気：{weather_description}")
    print(f"現在の気温：{temprature}")
else:
    print("Error", response.status_code)
