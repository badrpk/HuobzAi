import sys

# Memory-based AI learning
memory = {}

print("Huobz AI: Ask me anything...")

while True:
    user_input = input("You: ").strip().lower()

    # Check if the AI has already learned this response
    if user_input in memory:
        print(f"Huobz AI: {memory[user_input]}")
        continue

    # AI doesn't know, asks for training
    print("Huobz AI: I need more training...")
    new_response = input("Huobz AI: What should I say next time? ").strip()

    # Store new response
    memory[user_input] = new_response
    print("Huobz AI: I have learned from you!")
