import requests
import os

# 📌 Book Sources (Public and Open-Access)
BOOK_SOURCES = {
    "economics": "https://openlibrary.org/subjects/economics.json",
    "physics": "https://openlibrary.org/subjects/physics.json",
    "artificial intelligence": "https://openlibrary.org/subjects/artificial_intelligence.json",
    "medicine": "https://openlibrary.org/subjects/medicine.json",
    "law": "https://openlibrary.org/subjects/law.json",
    "computer science": "https://openlibrary.org/subjects/computer_science.json",
}

# 📌 Download Books for Faculty
def download_faculty_books(faculty):
    """Download books related to a faculty from Open Library."""
    
    if faculty not in BOOK_SOURCES:
        print(f"⚠️ No books found for {faculty}.")
        return

    print(f"📖 Fetching book list for {faculty}...")

    response = requests.get(BOOK_SOURCES[faculty])
    if response.status_code == 200:
        data = response.json()
        books = data.get("works", [])[:5]  # Get top 5 books
        
        for book in books:
            title = book["title"]
            book_id = book["key"].split("/")[-1]
            book_url = f"https://openlibrary.org/books/{book_id}"

            print(f"📚 **{title}** - [Read Here]({book_url})")
            
            # Save reference in knowledge database
            knowledge_entry = {
                "faculty": faculty,
                "title": title,
                "source": book_url
            }
            with open("huobz_knowledge.json", "a") as f:
                f.write(str(knowledge_entry) + "\n")
    else:
        print("⚠️ Failed to fetch book list.")
