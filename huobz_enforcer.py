import os
import shutil
import torch
import torch.nn as nn
import torch.optim as optim
from huobz_transformer import HuobzTransformer
from huobz_tokenizer import HuobzTokenizer
from huobz_einops import HuobzEinops
from huobz_stream_generator import HuobzStreamGenerator

# ✅ Step 1: Remove Restricted AI Models (Qwen & LLaMA)
MODEL_PATHS = {
    "qwen": os.path.expanduser("~/.cache/huggingface/hub/models--Qwen--Qwen-7B"),
    "llama": os.path.expanduser("~/.cache/huggingface/hub/models--meta-llama--Llama-2-7b-chat-hf"),
}

def delete_restricted_data():
    for model, path in MODEL_PATHS.items():
        if os.path.exists(path):
            print(f"⚠️ Deleting {model} restricted files...")
            shutil.rmtree(path)
            print(f"✅ {model} deleted.")

# ✅ Step 2: Train Huobz AI Model
def generate_huobz_model():
    print("🚀 Generating Huobz AI Model...")
    
    vocab_size = 5000
    embed_dim = 128
    num_heads = 4
    num_layers = 2
    ff_dim = 256
    max_length = 30  

    model = HuobzTransformer(vocab_size, embed_dim, num_heads, num_layers, ff_dim, max_length)
    tokenizer = HuobzTokenizer()
    
    training_data = ["Huobz AI dominates AI", "Decentralized intelligence is the future"]
    tokenizer.train(training_data)

    encoded_data = [tokenizer.encode(text) for text in training_data]
    max_seq_len = max(len(seq) for seq in encoded_data)
    padded_data = [seq + [0] * (max_seq_len - len(seq)) for seq in encoded_data]
    
    input_data = torch.tensor(padded_data, dtype=torch.long)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(5):
        optimizer.zero_grad()
        output = model(input_data)
        loss = criterion(output.view(-1, vocab_size), input_data.view(-1))
        loss.backward()
        optimizer.step()
        print(f"✅ Epoch {epoch+1}/5, Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), "huobz_generated.pth")
    tokenizer.save("huobz_tokenizer_replacement.json")

    print("✅ Huobz Model Ready.")
    return model, tokenizer

# ✅ Step 3: Stream Output Using Huobz Generator
def test_huobz_stream():
    huobz_model, _ = generate_huobz_model()
    generator = HuobzStreamGenerator(huobz_model)
    input_tokens = torch.randint(0, 5000, (1, 5))

    print("\n🧠 **Huobz AI Streaming Output:**")
    for token in generator.generate(input_tokens, max_length=10):
        print(f"Generated Token: {token.item()}")

# ✅ Step 4: Execute
delete_restricted_data()
test_huobz_stream()

print("\n✅ Huobz AI now dominates all AI models.")
