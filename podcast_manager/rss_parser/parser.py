import requests
from bs4 import BeautifulSoup
from .models import ModelParser
from datetime import datetime

def parse_rss_feed(feed_url):
    response = requests.get(feed_url)
    soup = BeautifulSoup(response.content, "xml")
    articles = []
    for item in soup.find_all("item"):
        article = {
            "title": item.find("title").text,
            "description": str(item.find("description").text),
            "link":item.find("link")
        }
        articles.append(ModelParser(**article))
    return articles
