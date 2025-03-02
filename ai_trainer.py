import torch
import torch.nn as nn
import torch.optim as optim
from huobz_transformer import HuobzTransformer
from huobz_tokenizer import tokenize_text

# Device setup (CPU/GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define training data (sample text for initial training)
training_data = [
    "Huobz AI is revolutionizing technology.",
    "Artificial Intelligence will shape the future.",
    "Machine learning models improve over time.",
    "Data is the new oil in the digital economy.",
    "Neural networks are inspired by the human brain.",
    "AI can generate text, images, and even music.",
    "Ethical AI is important for a fair society."
]

# Tokenization
encoded_data = [tokenize_text(text) for text in training_data]
max_seq_length = max(len(seq) for seq in encoded_data)

# Padding sequences to uniform length
for i in range(len(encoded_data)):
    encoded_data[i] += [0] * (max_seq_length - len(encoded_data[i]))

# Convert data to tensors
input_data = torch.tensor(encoded_data, dtype=torch.long).to(device)

# Initialize Model
model = HuobzTransformer(vocab_size=5000, embed_size=256, num_heads=8, num_layers=6).to(device)

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

def train_huobz_model(epochs=5):
    """Trains the Huobz AI model from scratch."""
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(input_data)  # Forward pass
        loss = criterion(output.view(-1, 5000), input_data.view(-1))  # Calculate loss
        loss.backward()  # Backpropagation
        optimizer.step()  # Update weights

        print(f"✅ Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

    # Save trained model
    torch.save(model.state_dict(), "huobz_transformer.pth")
    print("✅ Model trained and saved successfully!")

def load_or_train_model():
    """Loads an existing model or trains a new one if not found."""
    try:
        model.load_state_dict(torch.load("huobz_transformer.pth", map_location=device))
        print("✅ Pre-trained model loaded successfully!")
    except FileNotFoundError:
        print("🚀 No existing model found. Training a new one...")
        train_huobz_model()

def generate_response(input_text):
    """Generates a response using the trained Huobz AI model."""
    model.eval()
    with torch.no_grad():
        tokenized_input = tokenize_text(input_text)
        tokenized_input += [0] * (max_seq_length - len(tokenized_input))  # Padding
        input_tensor = torch.tensor([tokenized_input], dtype=torch.long).to(device)
        output = model(input_tensor)
        predicted_index = torch.argmax(output, dim=-1)
        return " ".join([str(idx.item()) for idx in predicted_index[0]])

# Train or Load Model
load_or_train_model()
