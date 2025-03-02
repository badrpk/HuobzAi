import torch

# ✅ Check for Qwen Dependencies
try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    qwen_available = True
except ImportError:
    print("⚠️ Warning: Missing dependencies for Qwen. Skipping Qwen model.")
    qwen_available = False

from huobz_tokenizer import HuobzTokenizer
from huobz_transformer import HuobzTransformer

# ✅ Force CPU execution (since CUDA is not available)
device = torch.device("cpu")

# ✅ Load Huobz AI Model
MAX_LENGTH = 100
VOCAB_SIZE = 5000
EMBED_DIM = 128
NUM_HEADS = 4
NUM_LAYERS = 2
FF_DIM = 256

huobz_model = HuobzTransformer(VOCAB_SIZE, EMBED_DIM, NUM_HEADS, NUM_LAYERS, FF_DIM, MAX_LENGTH)
huobz_model.load_state_dict(torch.load("huobz_transformer.pth", map_location=device))
huobz_model.to(device)
huobz_model.eval()
huobz_tokenizer = HuobzTokenizer()
huobz_tokenizer.load("huobz_tokenizer.json")

# ✅ Load Qwen Model (if dependencies exist)
if qwen_available:
    try:
        qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
        qwen_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True).to(device)
        qwen_model.eval()
    except Exception as e:
        print(f"⚠️ Warning: Failed to load Qwen. Skipping. Error: {e}")
        qwen_available = False
else:
    qwen_tokenizer = None
    qwen_model = None

# ✅ Load LLaMA Model (Ensure Hugging Face Authentication)
try:
    llama_tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True)
    llama_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True).to(device)
    llama_model.eval()
    llama_available = True
except Exception as e:
    print(f"⚠️ Warning: Failed to load LLaMA. Skipping. Error: {e}")
    llama_available = False

conversation_history = []
max_history = 5  # Number of previous exchanges to keep

def generate_huobz_response(user_input):
    """ Generate response using Huobz AI """
    conversation_history.append(user_input)
    if len(conversation_history) > max_history:
        conversation_history.pop(0)

    full_input = " ".join(conversation_history)
    tokenized_input = huobz_tokenizer.encode(full_input)

    if len(tokenized_input) > MAX_LENGTH:
        tokenized_input = tokenized_input[-MAX_LENGTH:]

    input_ids = torch.tensor([tokenized_input], dtype=torch.long).to(device)

    with torch.no_grad():
        output = huobz_model(input_ids)
        predicted_tokens = torch.argmax(output[:, -10:, :], dim=-1).tolist()[0]  # Generate 10 words
    response = huobz_tokenizer.decode(predicted_tokens)
    conversation_history.append(response)
    return response

def generate_qwen_response(user_input):
    """ Generate response using Qwen AI (if available) """
    if not qwen_available:
        return "⚠️ Qwen AI is not available."
    try:
        input_ids = qwen_tokenizer(user_input, return_tensors="pt").input_ids.to(device)
        with torch.no_grad():
            output = qwen_model.generate(input_ids, max_length=100)
        return qwen_tokenizer.decode(output[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ Qwen AI Error: {e}"

def generate_llama_response(user_input):
    """ Generate response using LLaMA AI """
    if not llama_available:
        return "⚠️ LLaMA AI is not available."
    try:
        input_ids = llama_tokenizer(user_input, return_tensors="pt").input_ids.to(device)
        with torch.no_grad():
            output = llama_model.generate(input_ids, max_length=100)
        return llama_tokenizer.decode(output[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ LLaMA AI Error: {e}"

print("\n🧠 **Huobz AI vs Qwen vs LLaMA Chat Mode (CPU)** (Type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("🛑 Exiting Chat. Goodbye!")
        break

    huobz_response = generate_huobz_response(user_input)
    qwen_response = generate_qwen_response(user_input) if qwen_available else "⚠️ Qwen AI is not available."
    llama_response = generate_llama_response(user_input) if llama_available else "⚠️ LLaMA AI is not available."

    print(f"\n🤖 **Huobz AI**: {huobz_response}")
    print(f"🦾 **Qwen AI**: {qwen_response}")
    print(f"🦙 **LLaMA AI**: {llama_response}\n")
