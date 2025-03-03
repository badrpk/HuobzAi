import requests
import json
import os
import time
from bs4 import BeautifulSoup

QUORA_URL = "https://www.quora.com/search?q="
STORAGE_FOLDER = "huobz_quora_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_quora(query):
    print(f"🔍 Scraping Quora for: {query}...")

    url = QUORA_URL + query.replace(" ", "+")
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to fetch Quora results for {query}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        questions = soup.find_all("a", {"href": True})

        extracted_qna = []
        for question in questions:
            q_title = question.text
            q_link = "https://www.quora.com" + question["href"]
            extracted_qna.append({"question": q_title, "url": q_link})

        file_path = os.path.join(STORAGE_FOLDER, f"{query}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted_qna, f, indent=4)

        print(f"✅ Saved {len(extracted_qna)} Quora Q&A for {query}")

    except Exception as e:
        print(f"⚠️ Error scraping Quora for {query}: {str(e)}")

TOPICS = ["Artificial Intelligence", "Machine Learning", "Blockchain", "Neuroscience", "Quantum Computing"]

while True:
    for topic in TOPICS:
        scrape_quora(topic)
        time.sleep(5)
