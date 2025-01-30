from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY 


app = Flask(__name__)


NEWS_API_URL = "https://newsapi.org/v2/everything"


def get_news(keyword):
    params = {
        'q': keyword,
        'apiKey': NEWS_API_KEY,
        'pageSize': 11  
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if data['status'] == 'ok':
        return data['articles']
    else:
        return []


@app.route("/", methods=["GET", "POST"])

def home():
    news_articles = []
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            news_articles = get_news(keyword)  
    return render_template("index.html", articles=news_articles)

if __name__ == "__main__":
    app.run(debug=True)
