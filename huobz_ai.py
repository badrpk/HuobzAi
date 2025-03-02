import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# ✅ Select Model (Change between 'qwen' or 'llama')
MODEL_PATH = "/home/userland/models/qwen"   # Use Qwen
# MODEL_PATH = "/home/userland/models/llama"  # Use LLaMA

# ✅ Load Model & Tokenizer
print(f"🚀 Loading AI Model from {MODEL_PATH}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16, device_map="auto")

# ✅ AI Response Function
def get_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    output = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# ✅ Chat Loop
print("\n🚀 HuobzAI is running! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Huobz AI: Goodbye! Have a great day! 👋")
        break
    response = get_response(user_input)
    print(f"Huobz AI: {response}")
