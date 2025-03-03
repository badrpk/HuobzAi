import requests
import json
import os
import time

STACK_OVERFLOW_API = "https://api.stackexchange.com/2.3/search?order=desc&sort=votes&site=stackoverflow"
STORAGE_FOLDER = "huobz_stackoverflow_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_stackoverflow(query):
    print(f"🔍 Scraping Stack Overflow: {query}...")

    url = f"{STACK_OVERFLOW_API}&intitle={query.replace(' ', '+')}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ Failed to fetch Stack Overflow: {query}")
            return

        questions = response.json()["items"]
        extracted_questions = [{"title": q["title"], "url": q["link"]} for q in questions]

        file_path = os.path.join(STORAGE_FOLDER, f"{query}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted_questions, f, indent=4)

        print(f"✅ Saved {len(extracted_questions)} questions for {query}")

    except Exception as e:
        print(f"⚠️ Error scraping Stack Overflow: {query}: {str(e)}")

TOPICS = ["Python programming", "Machine Learning", "AI models", "Blockchain development", "Quantum Computing"]

while True:
    for topic in TOPICS:
        scrape_stackoverflow(topic)
        time.sleep(5)
