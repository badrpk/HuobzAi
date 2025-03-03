import requests
import json
import os
import time
from bs4 import BeautifulSoup

GOOGLE_PATENTS_URL = "https://patents.google.com/?q="
STORAGE_FOLDER = "huobz_patent_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_patents(query):
    print(f"🔍 Scraping Google Patents for: {query}...")

    url = GOOGLE_PATENTS_URL + query.replace(" ", "+")
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to fetch patents for {query}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        patents = soup.find_all("a", {"href": True})

        extracted_patents = []
        for patent in patents:
            p_title = patent.text
            p_link = "https://patents.google.com" + patent["href"]
            extracted_patents.append({"title": p_title, "url": p_link})

        file_path = os.path.join(STORAGE_FOLDER, f"{query}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted_patents, f, indent=4)

        print(f"✅ Saved {len(extracted_patents)} patents for {query}")

    except Exception as e:
        print(f"⚠️ Error scraping patents for {query}: {str(e)}")

TOPICS = ["Artificial Intelligence", "Quantum Computing", "Medical Technology", "Green Energy"]

while True:
    for topic in TOPICS:
        scrape_patents(topic)
        time.sleep(5)
