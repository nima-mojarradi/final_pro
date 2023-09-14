import requests
from lxml import etree
from .models import ModelParser
from datetime import datetime

def parse_rss_feed(feed_url):
    response = requests.get(feed_url)
    tree = etree.fromstring(response.content)
    channel_data = tree.find('channel')
    articles = []
    for item in channel_data.findall("item"):
        article = {
            "title": item.find("title").text,
            "description": str(item.find("description").text),
            "link": item.find("link")
        }
        print("Title:", article["title"])
        print("Description:", article["description"])
        print("Link:", article["link"])
        articles.append(ModelParser(**article))
    return articles