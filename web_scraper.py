import requests
from bs4 import BeautifulSoup

# List of high-traffic websites for AI learning
WEBSITES = [
    "https://www.bbc.com/news",
    "https://www.cnn.com",
    "https://www.nytimes.com",
    "https://www.wikipedia.org"
]

# Function to extract content from a webpage
def scrape_web_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Ensure we got a valid response
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from paragraphs
        paragraphs = soup.find_all("p")
        content = " ".join([para.get_text() for para in paragraphs])

        return content if content else "No readable content found."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from {url}: {str(e)}"

# Function to fetch and format web knowledge
def fetch_latest_web_knowledge():
    knowledge_entries = []

    for website in WEBSITES:
        print(f"🔍 Scraping {website}...")
        content = scrape_web_content(website)

        # Store structured data
        knowledge_entries.append({
            "url": website,
            "title": f"Extracted Data from {website}",
            "content": content,
            "category": "General Knowledge"
        })

    return knowledge_entries
