import torch
from huobz_tokenizer import HuobzTokenizer
from huobz_transformer import HuobzTransformer

# Load AI
huobz_model = HuobzTransformer(vocab_size=5000, embed_dim=128, num_heads=4, num_layers=2, ff_dim=256, max_length=100).to("cpu")
huobz_tokenizer = HuobzTokenizer()

# Knowledge Testing Mode
def knowledge_testing():
    while True:
        user_input = input("\n🧠 Ask Huobz AI a question (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("🛑 Exiting Knowledge Test Mode.")
            break
        else:
            encoded_question = huobz_tokenizer.encode(user_input)
            input_tensor = torch.tensor([encoded_question], dtype=torch.long)
            response = huobz_model(input_tensor)
            print(f"🤖 Huobz AI Answer: {response}")
