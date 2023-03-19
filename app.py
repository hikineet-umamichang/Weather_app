from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city_name):
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        weather_description = weather["description"]

        return {"temperature": temperature, "description": weather_description}
    else:
        return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_weather", methods=["POST"])
def get_weather():
    city_name = request.form["city_name"]
    weather_data = get_weather_data(city_name)
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
