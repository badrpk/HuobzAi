import subprocess
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Define Transformer Models
MODELS = {
    "ChatGPT": "mistralai/Mistral-7B-Instruct-v0.1",
    "Grok": "meta-llama/Llama-2-7b-chat-hf",
    "LLaMA": "huggingfaceh4/zephyr-7b-beta",
    "DeepSeek": "deepseek-ai/deepseek-chat",
    "Claude": "mistralai/Mixtral-8x7B-Instruct-v0.1"
}

# Define compiled AI binaries
AI_PROGRAMS = {
    "Assembly": ["./huobz_ai"],
    "C++": ["./huobz_ai_cpp"],
    "Python": ["python3", "huobz_ai.py"],
}

class TransformerAI:
    def __init__(self, model_name):
        print(f"Loading {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(MODELS[model_name])
        self.model = AutoModelForCausalLM.from_pretrained(MODELS[model_name])

    def generate_response(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=200)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

def get_ai_response(ai_name, cmd, question):
    """Run a compiled AI program and return its response."""
    try:
        result = subprocess.run(cmd, input=question, capture_output=True, text=True, timeout=2)
        return result.stdout.strip()
    except Exception:
        return "Error: AI crashed or timed out"

def run_all_ai_models(question):
    responses = {}

    # Run Transformer Models
    for model_name in MODELS:
        ai = TransformerAI(model_name)
        responses[model_name] = ai.generate_response(question)

    # Run Assembly, C++, Python AI
    for ai_name, cmd in AI_PROGRAMS.items():
        responses[ai_name] = get_ai_response(ai_name, cmd, question)

    return responses

if __name__ == "__main__":
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ").strip()
        if question.lower() == "exit":
            break

        print("\n==== AI Model Responses ====")
        responses = run_all_ai_models(question)
        for model, response in responses.items():
            print(f"\n{model} AI Response:\n{response}")

        print("\nCopy and paste responses into chat for assessment.")
