import torch

class HuobzStreamGenerator:
    """Custom streaming generator to replace transformers_stream_generator"""

    def __init__(self, model):
        self.model = model

    def generate(self, input_ids, max_length=100):
        """Generates output token by token (streaming)."""
        output_ids = input_ids.clone()

        for _ in range(max_length):
            with torch.no_grad():
                output = self.model(output_ids)
                next_token = output.argmax(dim=-1)[:, -1].unsqueeze(-1)
                output_ids = torch.cat((output_ids, next_token), dim=-1)

                yield next_token  # ✅ Streaming output

# ✅ Usage Example
if __name__ == "__main__":
    dummy_model = torch.nn.Linear(10, 10)  # Mock model for testing
    input_tokens = torch.randint(0, 10, (1, 5))  # Dummy input

    generator = HuobzStreamGenerator(dummy_model)
    for token in generator.generate(input_tokens, max_length=5):
        print(f"Generated Token: {token.item()}")
