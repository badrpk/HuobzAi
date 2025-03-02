import json
import os
import re

TOKENIZER_FILE = "huobz_tokenizer.json"

def load_tokenizer():
    """Loads tokenizer from file, or creates a new one if missing."""
    if os.path.exists(TOKENIZER_FILE):
        try:
            with open(TOKENIZER_FILE, "r") as f:
                tokenizer_data = json.load(f)
                if isinstance(tokenizer_data, dict) and "word_to_index" in tokenizer_data:
                    print("✅ Loaded existing tokenizer.")
                    return tokenizer_data["word_to_index"], tokenizer_data["index_to_word"]
        except (json.JSONDecodeError, KeyError, TypeError):
            print("⚠️ Corrupt tokenizer file detected. Regenerating...")

    # If loading fails, create a new tokenizer
    print("⚠️ No tokenizer found! Creating a new one...")
    sample_vocab = ["Huobz", "AI", "is", "revolutionizing", "technology", ".", "learning", "future", "intelligence"]
    word_to_index = {word: i for i, word in enumerate(sample_vocab, start=1)}
    index_to_word = {i: word for word, i in word_to_index.items()}

    save_tokenizer(word_to_index, index_to_word)
    return word_to_index, index_to_word

def save_tokenizer(word_to_index, index_to_word):
    """Saves tokenizer to file."""
    tokenizer_data = {"word_to_index": word_to_index, "index_to_word": index_to_word}
    with open(TOKENIZER_FILE, "w") as f:
        json.dump(tokenizer_data, f)
    print("✅ Tokenizer saved.")

def preprocess_text(text):
    """Cleans and normalizes text input."""
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9.,!? ]+", "", text)  # Remove special characters
    return text

def tokenize_text(text):
    """Tokenizes a given text into numerical indices."""
    text = preprocess_text(text)
    return [word_to_index.get(word, 0) for word in text.split()]  # 0 for unknown words

def detokenize_text(indices):
    """Converts token indices back into words."""
    return " ".join([index_to_word.get(idx, "<UNK>") for idx in indices])

def update_tokenizer(new_words):
    """Adds new words to the tokenizer and saves updates."""
    global word_to_index, index_to_word
    new_added = False
    for word in new_words:
        if word not in word_to_index:
            new_index = len(word_to_index) + 1
            word_to_index[word] = new_index
            index_to_word[new_index] = word
            new_added = True

    if new_added:
        save_tokenizer(word_to_index, index_to_word)
        print("✅ Tokenizer updated with new words.")

# Load tokenizer
word_to_index, index_to_word = load_tokenizer()

# Example Test
if __name__ == "__main__":
    sample_text = "Huobz AI is revolutionizing technology."
    encoded = tokenize_text(sample_text)
    decoded = detokenize_text(encoded)

    print(f"✅ Encoded: {encoded}")
    print(f"✅ Decoded: {decoded}")
