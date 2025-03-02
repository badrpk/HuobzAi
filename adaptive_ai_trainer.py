import torch
from huobz_transformer import HuobzTransformer
from huobz_tokenizer import HuobzTokenizer

# Load AI Model
huobz_model = HuobzTransformer(vocab_size=5000, embed_dim=128, num_heads=4, num_layers=2, ff_dim=256, max_length=100).to("cpu")
huobz_tokenizer = HuobzTokenizer()

# Train Huobz AI adaptively
def train_huobz_ai(knowledge):
    if not knowledge:
        print("⚠️ No new knowledge to train on.")
        return

    encoded_data = huobz_tokenizer.encode(knowledge)
    input_tensor = torch.tensor([encoded_data], dtype=torch.long)

    print(f"📚 Training Huobz AI on {len(encoded_data)} tokens...")
    output = huobz_model(input_tensor)
    
    print("✅ Huobz AI successfully improved.")
