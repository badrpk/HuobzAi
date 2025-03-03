import requests
import json
import random
import time
from bs4 import BeautifulSoup
from knowledge_database import store_knowledge

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Special:Random"

def scrape_wikipedia():
    """Scrapes Wikipedia for random articles and stores knowledge."""
    print("🔍 Scraping Wikipedia...")
    
    for _ in range(3):  # Scrape 3 articles per cycle
        response = requests.get(WIKIPEDIA_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.find("h1").text
        content = "\n".join([p.text for p in soup.find_all("p")[:5]])  # Extract first 5 paragraphs

        if title and content:
            store_knowledge(title, content)
            print(f"✅ Saved: {title}")
        
        time.sleep(random.randint(5, 10))  # Random delay to avoid IP ban
