import os
import time
import wikipediaapi
from knowledge_database import store_knowledge

wiki_wiki = wikipediaapi.Wikipedia('en')

def extract_wikipedia():
    topics = ["Artificial intelligence", "Machine learning", "Neural networks",
              "Physics", "Chemistry", "Mathematics", "Biology", "History", "Economics"]
    
    while True:
        for topic in topics:
            page = wiki_wiki.page(topic)
            if page.exists():
                print(f"🔍 Extracting Wikipedia: {topic}...")
                store_knowledge(topic, page.text, "Wikipedia")
        time.sleep(5)  # Wait before fetching again

if __name__ == "__main__":
    extract_wikipedia()
