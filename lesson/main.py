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
    api_key = "13e2e91ca5585170bfc25294bde29a16"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "01570c09ab3a4e3fbc4082e3921d48f1"
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

if __name__ == "__main__":
    app.run(debug=True)
