import requests
import json
from knowledge_database import store_knowledge

YOUTUBE_SEARCH_API = "https://www.googleapis.com/youtube/v3/search"

def scrape_youtube():
    """Scrapes YouTube trending videos for knowledge extraction."""
    print("🔍 Scraping YouTube...")
    
    params = {
        "part": "snippet",
        "chart": "mostPopular",
        "regionCode": "US",
        "maxResults": 5,
        "key": "YOUR_YOUTUBE_API_KEY"
    }

    response = requests.get(YOUTUBE_SEARCH_API, params=params)
    videos = response.json().get("items", [])

    for video in videos:
        title = video["snippet"]["title"]
        description = video["snippet"]["description"]
        content = f"{title}\n\n{description}"

        store_knowledge(title, content)
        print(f"✅ Saved: {title}")
