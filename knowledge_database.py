import json
import os
import zlib
from transformers import pipeline  # Hugging Face summarizer

DB_FILE = "huobz_knowledge.json"
SUMMARIZER = pipeline("summarization", model="facebook/bart-large-cnn")

def load_database():
    """Load existing knowledge database."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return {}

def save_database(data):
    """Save knowledge database."""
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def store_knowledge(topic, content):
    """Stores knowledge efficiently with AI summarization & compression."""
    db = load_database()
    
    # AI-based summarization
    summary = SUMMARIZER(content, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    
    # Compress data
    compressed_data = zlib.compress(content.encode())
    
    db[topic] = {"summary": summary, "data": compressed_data.hex()}
    save_database(db)
    print(f"✅ Stored: {topic} (Summary + Compressed)")

def query_knowledge(topic):
    """Retrieves knowledge with decompression."""
    db = load_database()
    if topic in db:
        decompressed_data = zlib.decompress(bytes.fromhex(db[topic]["data"])).decode()
        return {"summary": db[topic]["summary"], "content": decompressed_data}
    return None
