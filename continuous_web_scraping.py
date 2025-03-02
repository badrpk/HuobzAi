import requests
from bs4 import BeautifulSoup
import time

def fetch_latest_news():
    url = "https://news.google.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = [h.text for h in soup.find_all("h3")[:5]]
    return headlines

while True:
    print("📡 Fetching latest news...")
    news = fetch_latest_news()
    for article in news:
        print(f"📰 {article}")
    time.sleep(600)  # Every 10 minutes
