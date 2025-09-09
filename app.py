from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # अपनी OpenWeatherMap API key यहाँ लगाएं

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                }
            else:
                error = "City not found. Please enter a valid city name."
        else:
            error = "Please enter a city name."
    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
