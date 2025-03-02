import time

total_tokens = 0
start_time = time.time()

def update_dashboard():
    elapsed_time = time.time() - start_time
    estimated_completion = (10_000_000 - total_tokens) / (total_tokens + 1) * elapsed_time / 60
    print(f"\n🚀 AI Learning Progress:")
    print(f"✅ Total Tokens Processed: {total_tokens}")
    print(f"🕒 Estimated Time Left: {round(estimated_completion, 2)} minutes")

def test_ai():
    while True:
        user_input = input("\n🧠 Ask Huobz AI a question (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("🛑 Exiting Knowledge Test Mode.")
            break
        else:
            print(f"🤖 Huobz AI Answer: {user_input} ...learning in progress...")
