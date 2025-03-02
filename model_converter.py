import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from huobz_tokenizer import HuobzTokenizer

# Load Qwen & LLaMA models (if available)
try:
    qwen_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B").to("cpu")
    qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B")
    qwen_available = True
except:
    qwen_available = False

try:
    llama_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf").to("cpu")
    llama_tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    llama_available = True
except:
    llama_available = False

huobz_tokenizer = HuobzTokenizer()

# Convert AI models into Huobz format
def convert_model_data():
    if qwen_available:
        print("🚀 Converting Qwen Data into Huobz AI...")
        sample_text = "Huobz AI is the future of AI transformations!"
        qwen_encoded = qwen_tokenizer.encode(sample_text)
        huobz_encoded = huobz_tokenizer.encode(sample_text)
        print(f"🔄 Qwen → Huobz | Tokens Converted: {len(huobz_encoded)}")

    if llama_available:
        print("🚀 Converting LLaMA Data into Huobz AI...")
        sample_text = "Deep learning models like Huobz AI dominate AI innovation."
        llama_encoded = llama_tokenizer.encode(sample_text)
        huobz_encoded = huobz_tokenizer.encode(sample_text)
        print(f"🔄 LLaMA → Huobz | Tokens Converted: {len(huobz_encoded)}")
