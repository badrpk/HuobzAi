import requests
import json
import os
import time

NEWS_API_URL = "https://newsapi.org/v2/top-headlines?category="
API_KEY = "YOUR_NEWS_API_KEY"
STORAGE_FOLDER = "huobz_news_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_news(category):
    print(f"🔍 Fetching latest news in {category}...")

    url = f"{NEWS_API_URL}{category}&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ Failed to fetch news for {category}")
            return

        articles = response.json()["articles"]
        extracted_news = [{"title": a["title"], "url": a["url"]} for a in articles]

        file_path = os.path.join(STORAGE_FOLDER, f"{category}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted_news, f, indent=4)

        print(f"✅ Saved {len(extracted_news)} articles for {category}")

    except Exception as e:
        print(f"⚠️ Error fetching news for {category}: {str(e)}")

CATEGORIES = ["technology", "science", "business", "health", "world"]

while True:
    for category in CATEGORIES:
        scrape_news(category)
        time.sleep(5)
