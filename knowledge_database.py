import os
import json

# Define the knowledge database file
DATABASE_FILE = "huobz_knowledge.json"

# Ensure the knowledge database file exists
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "w") as f:
        json.dump({}, f)

def load_knowledge():
    """Load knowledge from the database file."""
    try:
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_knowledge(data):
    """Save knowledge to the database file."""
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def store_knowledge(topic, content, answer="No answer available"):
    """
    Store knowledge in the database.

    Args:
        topic (str): The topic of the knowledge.
        content (str): The full text content of the knowledge.
        answer (str): A short summary or direct answer (if available).
    """
    knowledge_db = load_knowledge()
    knowledge_db[topic] = {
        "content": content,
        "answer": answer
    }
    save_knowledge(knowledge_db)
    print(f"✅ Knowledge stored under '{topic}'.")

def query_knowledge(topic):
    """
    Retrieve knowledge based on a topic.

    Args:
        topic (str): The topic to search for.

    Returns:
        dict: Knowledge entry if found, otherwise an empty response.
    """
    knowledge_db = load_knowledge()
    if topic in knowledge_db:
        return {
            "topic": topic,
            "content": knowledge_db[topic].get("content", "No content available"),
            "answer": knowledge_db[topic].get("answer", "No answer available")
        }
    else:
        return {
            "topic": topic,
            "content": "No content available",
            "answer": "No answer available"
        }

def get_all_knowledge():
    """
    Retrieve all stored knowledge.

    Returns:
        list: A list of all knowledge entries.
    """
    knowledge_db = load_knowledge()
    results = []
    for topic, data in knowledge_db.items():
        results.append({
            "topic": topic,
            "content": data.get("content", "No content available"),
            "answer": data.get("answer", "No answer available")
        })
    return results

# Test the knowledge storage system
if __name__ == "__main__":
    # Example usage
    store_knowledge("Artificial Intelligence", "AI is the simulation of human intelligence by machines.", "AI is about making machines intelligent.")
    store_knowledge("Quantum Computing", "Quantum computers use quantum bits to perform calculations.", "Quantum computing is a new paradigm in computation.")
    
    print("\n🔍 Query Example:")
    print(query_knowledge("Artificial Intelligence"))

    print("\n📚 All Stored Knowledge:")
    print(get_all_knowledge())
