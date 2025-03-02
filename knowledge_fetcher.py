import requests
import os
from bs4 import BeautifulSoup
from knowledge_database import store_knowledge

BOOK_SOURCES = [
    "https://openlibrary.org/search?q=",
    "https://scholar.google.com/scholar?q="
]

BOOK_DIR = "huobz_books"

# Ensure book directory exists
os.makedirs(BOOK_DIR, exist_ok=True)

def find_and_download_books(query, category):
    for source in BOOK_SOURCES:
        search_url = source + query.replace(" ", "+")
        print(f"🔍 Searching for books: {search_url}")
        
        try:
            response = requests.get(search_url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract top book links
            book_links = [a["href"] for a in soup.find_all("a", href=True) if "book" in a["href"]][:3]
            
            for link in book_links:
                book_url = f"https://openlibrary.org{link}" if "openlibrary" in source else link
                book_title = link.split("/")[-1]
                book_path = os.path.join(BOOK_DIR, f"{book_title}.txt")

                # Download book content
                book_content = requests.get(book_url).text[:5000]  # Save only the first 5000 chars for efficiency
                
                with open(book_path, "w", encoding="utf-8") as f:
                    f.write(book_content)
                
                store_knowledge(category, book_title, book_content)
                print(f"📚 Downloaded & stored: {book_title}")
        
        except Exception as e:
            print(f"⚠️ Failed to fetch books: {e}")

    print("✅ Books downloaded and knowledge stored.")
