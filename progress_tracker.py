import time

start_time = time.time()
total_tokens_converted = 0

# Estimate time left
def estimate_time_remaining():
    elapsed_time = time.time() - start_time
    avg_time_per_token = elapsed_time / (total_tokens_converted + 1)
    tokens_remaining = 10_000_000 - total_tokens_converted
    estimated_time = avg_time_per_token * tokens_remaining / 60
    return round(estimated_time, 2)

# Display Progress
def display_progress():
    print(f"\n✅ Total Tokens Processed: {total_tokens_converted}")
    print(f"🕒 Estimated Time Left: {estimate_time_remaining()} minutes")
