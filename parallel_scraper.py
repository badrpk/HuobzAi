import requests
import concurrent.futures
from bs4 import BeautifulSoup

popular_sites = [
    "https://www.bbc.com", "https://www.nytimes.com", "https://www.cnn.com",
    "https://www.wikipedia.org", "https://www.nasa.gov", "https://www.healthline.com"
]

# Function to extract text from a website
def extract_text_from_url(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([para.get_text() for para in paragraphs])
        return text[:5000]  # Limit text to 5000 characters per site
    except Exception as e:
        print(f"⚠️ Failed to extract from {url}: {e}")
        return ""

# Multi-threaded web crawling
def extract_web_knowledge():
    print("🌍 Extracting knowledge from multiple sites...")
    knowledge = ""

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(extract_text_from_url, popular_sites)
    
    for site_text in results:
        if site_text:
            knowledge += site_text + "\n"
    
    print("✅ Web knowledge extracted successfully.")
    return knowledge
