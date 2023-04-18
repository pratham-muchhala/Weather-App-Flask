from flask import Flask, render_template, request
import requests  # pip install requests

app = Flask(__name__)  # Initialise app


# Config
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["name"]

        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=75b32280c1375181a46f69e6824e7ef0&units=metric"
        response = requests.get(url.format(city_name)).json()
        print(response)
        temp = response["main"]["temp"]
        weather = response["weather"][0]["description"]
        min_temp = response["main"]["temp_min"]
        max_temp = response["main"]["temp_max"]
        icon = response["weather"][0]["icon"]

        print(temp, weather, min_temp, max_temp, icon)
        return render_template(
            "index.html",
            temp=temp,
            weather=weather,
            min_temp=min_temp,
            max_temp=max_temp,
            icon=icon,
            city_name=city_name,
        )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
