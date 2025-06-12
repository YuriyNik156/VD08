from flask import Flask, render_template, request
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG: QUOTES_API_KEY =", os.getenv("QUOTES_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quotes():
    quote = None
    author = None

    if request.method == "POST":
        source = random.choice(["ninjas", "zen", "slate"])

        if source == "ninjas":
            data = get_quotes_ninjas()
            if data:
                quote = data[0].get("quote")
                author = data[0].get("author")

        elif source == "zen":
            quote, author = get_quote_zen()

        elif source == "slate":
            quote, author = get_quote_slate()

    return render_template("quotes.html", quote=quote, author=author)

def get_quotes_ninjas():
    api_key = os.getenv("QUOTES_API_KEY")
    url = "https://api.api-ninjas.com/v1/quotes"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def get_quote_zen():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]["q"], data[0]["a"]
    return None, None

def get_quote_slate():
    url = "https://quoteslate.vercel.app/api/quote"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["quote"], data["author"]
    return None, None

if __name__ == "__main__":
    app.run(debug=True)