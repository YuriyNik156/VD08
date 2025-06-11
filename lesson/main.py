import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    news = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
        news = get_news()
    return render_template("index.html", weather=weather, news=news)

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

if __name__ == "__main__":
    app.run(debug=True)
