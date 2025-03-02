import torch
import torch.nn as nn
import torch.optim as optim

class HuobzTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size, num_heads, num_layers, hidden_dim=512):
        """
        Transformer-based AI model for Huobz.
        
        Args:
        - vocab_size: Number of words in vocabulary.
        - embed_size: Size of word embeddings.
        - num_heads: Number of attention heads.
        - num_layers: Number of transformer encoder layers.
        - hidden_dim: Dimension of the hidden layer.
        """
        super(HuobzTransformer, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embed_size)
        encoder_layers = nn.TransformerEncoderLayer(
            d_model=embed_size, nhead=num_heads, dim_feedforward=hidden_dim, batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_layers)
        self.fc_out = nn.Linear(embed_size, vocab_size)

    def forward(self, x):
        """
        Forward pass of the transformer model.
        """
        embedded = self.embedding(x)
        transformed = self.transformer_encoder(embedded)
        output = self.fc_out(transformed)
        return output

# Example test run
if __name__ == "__main__":
    vocab_size = 5000
    embed_size = 256
    num_heads = 8
    num_layers = 6

    model = HuobzTransformer(vocab_size, embed_size, num_heads, num_layers)
    dummy_input = torch.randint(0, vocab_size, (1, 10))
    output = model(dummy_input)
    
    print("✅ Model initialized successfully.")
    print("🧠 Output shape:", output.shape)
