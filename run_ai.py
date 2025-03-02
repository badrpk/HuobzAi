import subprocess
import tiktoken
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time

# Initialize tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

# Load Qwen and LLaMA AI models
print("Loading Qwen and LLaMA AI models...")

qwen_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto")
qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B")

llama_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", device_map="auto")
llama_tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

print("Qwen and LLaMA models loaded successfully!")


def process_text(input_text):
    """ Tokenizes text using tiktoken """
    tokens = tokenizer.encode(input_text)
    decoded_text = tokenizer.decode(tokens)
    return tokens, decoded_text


def run_qwen_llama(input_text):
    """ Runs input through Qwen and LLaMA """
    start_time = time.time()

    # Qwen
    qwen_input = qwen_tokenizer(input_text, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    qwen_output = qwen_model.generate(**qwen_input)
    qwen_response = qwen_tokenizer.decode(qwen_output[0], skip_special_tokens=True)

    # LLaMA
    llama_input = llama_tokenizer(input_text, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    llama_output = llama_model.generate(**llama_input)
    llama_response = llama_tokenizer.decode(llama_output[0], skip_special_tokens=True)

    execution_time = time.time() - start_time
    return qwen_response, llama_response, execution_time


def run_python_ai(input_text):
    """ Runs input through Huobz AI (Python) """
    start_time = time.time()
    result = subprocess.run(["python3", "huobz_ai.py", input_text], capture_output=True, text=True)
    execution_time = time.time() - start_time
    return result.stdout.strip(), execution_time


def run_cpp_ai(input_text):
    """ Runs input through Huobz AI (C++) """
    start_time = time.time()
    subprocess.run(["g++", "-o", "huobz_ai_cpp", "huobz_ai.cpp"])  # Compile if not compiled
    result = subprocess.run(["./huobz_ai_cpp", input_text], capture_output=True, text=True)
    execution_time = time.time() - start_time
    return result.stdout.strip(), execution_time


def run_assembly_ai(input_text):
    """ Runs input through Huobz AI (Assembly) """
    start_time = time.time()
    subprocess.run(["nasm", "-f", "elf64", "huobz_ai.s", "-o", "huobz_ai.o"])  # Assemble
    subprocess.run(["ld", "-o", "huobz_ai", "huobz_ai.o"])  # Link
    result = subprocess.run(["./huobz_ai", input_text], capture_output=True, text=True)
    execution_time = time.time() - start_time
    return result.stdout.strip(), execution_time


if __name__ == "__main__":
    print("\nHuobz AI Execution Benchmark")
    user_input = input("Enter your text: ")

    # Tokenization
    tokens, decoded = process_text(user_input)
    print("\n🔹 Tokenized Input:", tokens)
    print("🔹 Decoded Text:", decoded)

    # Execute AI models
    print("\nExecuting AI models...\n")

    qwen_response, llama_response, ql_time = run_qwen_llama(user_input)
    print("\n📌 Qwen Response:", qwen_response)
    print("\n📌 LLaMA Response:", llama_response)
    print(f"⏱ Execution Time (Qwen & LLaMA): {ql_time:.4f} sec\n")

    huobz_python_response, python_time = run_python_ai(user_input)
    print("\n📌 Huobz AI (Python) Response:", huobz_python_response)
    print(f"⏱ Execution Time (Python AI): {python_time:.4f} sec\n")

    huobz_cpp_response, cpp_time = run_cpp_ai(user_input)
    print("\n📌 Huobz AI (C++) Response:", huobz_cpp_response)
    print(f"⏱ Execution Time (C++ AI): {cpp_time:.4f} sec\n")

    huobz_asm_response, asm_time = run_assembly_ai(user_input)
    print("\n📌 Huobz AI (Assembly) Response:", huobz_asm_response)
    print(f"⏱ Execution Time (Assembly AI): {asm_time:.4f} sec\n")

    print("\n✅ Execution Completed! Share input/output, and I'll rank performance on a scale of 1-10.")
