import time
from web_scraper import fetch_latest_web_knowledge
from knowledge_database import store_knowledge, query_knowledge
from memory_optimization import optimize_storage
from ai_trainer import train_huobz_model, generate_response

# Function to check and optimize storage
def check_storage():
    result = optimize_storage()
    if result is not None:
        storage_used, total_storage = result
        print(f"\n💾 **Storage Used:** {storage_used:.2f}% ({total_storage}GB)")
        if storage_used >= 95:
            print("⚠️ **Warning:** Storage is at 95%. Initiating automatic compression...")
    else:
        print("\n⚠️ **Error:** Storage check failed. Please verify `memory_optimization.py`.")

# Function to fetch new knowledge and train AI
def fetch_and_train():
    print("\n🌍 **Fetching the latest web knowledge...**\n")
    
    web_data = fetch_latest_web_knowledge()
    
    for entry in web_data:
        title, content = entry["title"], entry["content"]
        print(f"🔍 Learning from {entry['url']}... ✅")
        
        # Store the extracted knowledge
        store_knowledge(title, content)
    
    print("\n✅ **Knowledge Updated! Training AI...**\n")
    train_huobz_model()

# Main function for Huobz Autopilot
def main_autopilot():
    print("\n🚀 **Huobz Autopilot Mode Activated**\n")
    
    # Check storage first
    check_storage()

    while True:
        fetch_and_train()

        # Display current storage usage
        check_storage()

        # Display stored knowledge stats
        knowledge_entries = query_knowledge("")
        if knowledge_entries:
            print(f"\n📚 **Stored Knowledge Entries:** {len(knowledge_entries)}")
        else:
            print("\n📚 **No stored knowledge yet. Learning in progress...**")

        print("\n💬 **Ask a question (or type 'exit' to quit):**", end=" ")
        user_input = input().strip()
        
        if user_input.lower() == "exit":
            print("\n🛑 **Exiting Huobz Autopilot.** Goodbye!\n")
            break
        
        response = generate_response(user_input)
        print(f"\n🤖 **Huobz AI Answer:** {response}\n")
        
        # Auto-train on missing responses
        if response == "I don't have an answer yet. Learning more...":
            print("\n🔄 **Updating AI Model with new knowledge...**\n")
            fetch_and_train()

        # Wait for 5 seconds before next cycle
        print("\n✅ **Huobz AI Updated. Next scan in 5 seconds...**\n")
        time.sleep(5)

# Run Huobz Autopilot
if __name__ == "__main__":
    main_autopilot()
