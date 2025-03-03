import requests
import json
import os
import time

REDDIT_URL = "https://www.reddit.com/r/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
STORAGE_FOLDER = "huobz_reddit_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_reddit(subreddit):
    print(f"🔍 Scraping Reddit: r/{subreddit}...")

    url = f"{REDDIT_URL}{subreddit}/hot.json?limit=10"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Failed to fetch Reddit: {subreddit}")
            return

        posts = response.json()["data"]["children"]
        extracted_posts = [{"title": post["data"]["title"], "url": post["data"]["url"]} for post in posts]

        file_path = os.path.join(STORAGE_FOLDER, f"{subreddit}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted_posts, f, indent=4)

        print(f"✅ Saved {len(extracted_posts)} posts from r/{subreddit}")

    except Exception as e:
        print(f"⚠️ Error scraping Reddit: {subreddit}: {str(e)}")

SUBREDDITS = ["ArtificialIntelligence", "MachineLearning", "QuantumComputing", "Blockchain", "Economics", "Neuroscience"]

while True:
    for subreddit in SUBREDDITS:
        scrape_reddit(subreddit)
        time.sleep(5)
