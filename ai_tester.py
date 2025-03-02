import subprocess

# AI program commands
commands = {
    "Assembly": ["./huobz_ai"],
    "C++": ["./huobz_ai_cpp"],
    "Python": ["python3", "huobz_ai.py"],
}

def get_ai_response(ai_name, cmd, question):
    """Run an AI program with a question and return the response."""
    try:
        result = subprocess.run(cmd, input=question, capture_output=True, text=True, timeout=1)
        return result.stdout.strip()
    except Exception as e:
        return "Error: AI crashed or timed out"

while True:
    # Ask user for input question
    question = input("\nEnter your question (or type 'exit' to quit): ").strip()
    if question.lower() == "exit":
        break

    print("\n==== AI Responses ====")

    responses = {}
    for ai, cmd in commands.items():
        response = get_ai_response(ai, cmd, question)
        responses[ai] = response
        print(f"\n{ai} AI Response:\n{response}")

    print("\nCopy and paste these responses into our chat to assess performance.")
