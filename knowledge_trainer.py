import os
import time
from ai_trainer import train_huobz_model
from knowledge_database import compress_knowledge, query_knowledge
from memory_optimization import optimize_storage

# Path where Wikipedia data is stored
WIKI_DATA_PATH = "huobz_wikipedia_data"

# Function to load Wikipedia knowledge from stored files
def load_wikipedia_knowledge():
    knowledge_entries = []
    
    if not os.path.exists(WIKI_DATA_PATH):
        print("⚠️ No Wikipedia data found. Run wikipedia_scraper.py first.")
        return knowledge_entries
    
    for file in os.listdir(WIKI_DATA_PATH):
        file_path = os.path.join(WIKI_DATA_PATH, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            knowledge_entries.append(content)
    
    return knowledge_entries

# Function to train AI continuously using stored knowledge
def continuous_training():
    while True:
        # Optimize storage before training
        used_storage, total_storage = optimize_storage()
        print(f"💾 **Storage Used:** {used_storage:.2f}% ({total_storage}GB)")

        # Load stored Wikipedia knowledge
        knowledge_data = load_wikipedia_knowledge()
        
        if knowledge_data:
            print("🧠 Training AI with Wikipedia data...")
            train_huobz_model(knowledge_data)
            
            # After training, refine and compress stored knowledge
            print("📊 Compressing and refining knowledge...")
            compress_knowledge()
        
        else:
            print("⏳ Waiting for Wikipedia data...")

        # Sleep before the next training cycle
        time.sleep(10)

if __name__ == "__main__":
    continuous_training()
