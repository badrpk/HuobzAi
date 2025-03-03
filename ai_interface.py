import threading
import time
from ai_trainer import generate_response
from knowledge_database import flag_incorrect_knowledge

def ask_ai():
    while True:
        question = input("\n💬 Ask a question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer = generate_response(question)
        print(f"\n🤖 Huobz AI: {answer}")

        feedback = input("\n✔️ (t) Correct, (f) Incorrect? ").strip().lower()
        if feedback == 'f':
            flag_incorrect_knowledge(question, answer)

if __name__ == "__main__":
    ai_thread = threading.Thread(target=ask_ai)
    ai_thread.start()
