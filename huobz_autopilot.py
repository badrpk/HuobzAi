import requests
import json
import time
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# ✅ Load AI Model
MODEL_NAME = "facebook/bart-large-cnn"  # Example model, adjust as needed
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# ✅ Use CPU
device = torch.device("cpu")
model.to(device)

print("🚀 Huobz AutoPilot AI Started...")

# ✅ Fetch latest research papers (Example API call)
def fetch_web_knowledge():
    print("🌍 Fetching latest web knowledge...")
    response = requests.get("https://api.example.com/research")  # Replace with actual API
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Failed to fetch research data")
        return []

# ✅ Process and summarize fetched data
def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    inputs = {key: val.to(device) for key, val in inputs.items()}
    
    # ✅ Fix min_length and max_length issue
    min_length = 10
    max_length = 100
    
    # ✅ Ensure min_length < max_length dynamically
    max_length = max(min_length + 20, max_length)  

    summary_ids = model.generate(
        inputs["input_ids"],
        min_length=min_length,
        max_length=max_length,
        do_sample=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# ✅ Save summaries
def save_summary(data):
    with open("data/summary.json", "w") as f:
        json.dump(data, f)
    print("💾 Summarized knowledge saved at data/summary.json")

# ✅ Check AI backend server connection
def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# ✅ Backend servers to check
backend_servers = [
    "http://192.168.1.100:5000",
    "http://192.168.1.101:5000",
    "http://192.168.1.102:5000"
]

# ✅ Fetch & Process Data
research_papers = fetch_web_knowledge()

if research_papers:
    print(f"✅ Fetched {len(research_papers)} research papers")
    
    summaries = []
    for paper in research_papers:
        summaries.append(summarize_text(paper["abstract"]))  # Adjust key as needed
    
    save_summary(summaries)

else:
    print("❌ No research papers fetched!")

# ✅ Check AI Server Availability
server_connected = False

for server in backend_servers:
    if check_server(server):
        print(f"✅ Connected to AI Server: {server}")
        server_connected = True
        break
    else:
        print(f"❌ Could not connect to {server}")

if not server_connected:
    print("⏳ Waiting for next cycle...")
    time.sleep(30)  # Retry after 30 seconds
