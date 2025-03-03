import requests
import json
import os
import time

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories?q="
STORAGE_FILE = "github_repos.json"
STORAGE_FOLDER = "huobz_github_data"
SCRAPED_REPOS = set()

if os.path.exists(STORAGE_FILE):
    with open(STORAGE_FILE, "r") as f:
        SCRAPED_REPOS = set(json.load(f))

os.makedirs(STORAGE_FOLDER, exist_ok=True)

def scrape_github(query):
    """Scrapes GitHub for open-source projects."""
    global SCRAPED_REPOS
    print(f"🔍 Searching GitHub: {query}...")

    url = GITHUB_SEARCH_URL + query.replace(" ", "+") + "&sort=stars"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to fetch GitHub results for {query} (Status Code: {response.status_code})")
            return

        repos = response.json()["items"]
        extracted_repos = []

        for repo in repos[:10]:  # Limit to top 10 repos
            repo_name = repo["name"]
            repo_url = repo["html_url"]
            if repo_url not in SCRAPED_REPOS:
                extracted_repos.append({"name": repo_name, "url": repo_url})
                SCRAPED_REPOS.add(repo_url)

        if extracted_repos:
            with open(STORAGE_FILE, "w") as f:
                json.dump(list(SCRAPED_REPOS), f)

            file_path = os.path.join(STORAGE_FOLDER, f"{query}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(extracted_repos, f, indent=4)

            print(f"✅ Saved {len(extracted_repos)} repos for {query}")
        else:
            print(f"⚠️ No new repos found for {query}")

    except Exception as e:
        print(f"⚠️ Error scraping GitHub for {query}: {str(e)}")

TOPICS = ["Artificial Intelligence", "Machine Learning", "Quantum Computing", "Blockchain", "Economics", "Neuroscience"]

while True:
    for topic in TOPICS:
        scrape_github(topic)
        time.sleep(5)
