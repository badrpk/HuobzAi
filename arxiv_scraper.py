import requests
import xml.etree.ElementTree as ET
import json
import time
import os

ARXIV_API_URL = "http://export.arxiv.org/api/query?search_query=all:"
STORAGE_FOLDER = "huobz_arxiv_data"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_arxiv(query):
    print(f"🔍 Searching arXiv: {query}...")

    response = requests.get(ARXIV_API_URL + query)
    if response.status_code != 200:
        print(f"❌ Failed to fetch arXiv results for {query}")
        return

    root = ET.fromstring(response.text)
    papers = []

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        link = entry.find("{http://www.w3.org/2005/Atom}id").text
        papers.append({"title": title, "url": link})

    if papers:
        file_path = os.path.join(STORAGE_FOLDER, f"{query}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=4)

        print(f"✅ Saved {len(papers)} papers for {query}")

TOPICS = ["Artificial Intelligence", "Machine Learning", "Quantum Computing", "Blockchain", "Neuroscience"]

while True:
    for topic in TOPICS:
        scrape_arxiv(topic)
        time.sleep(10)
