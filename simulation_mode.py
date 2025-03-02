import random

def simulate_future():
    scenarios = [
        "If AI replaces jobs, what will happen?",
        "What if space travel becomes affordable?",
        "How will climate change affect human civilization?"
    ]
    
    scenario = random.choice(scenarios)
    print(f"🔬 Simulating: {scenario}")
    return "Based on my analysis, here is what could happen..."
    
print(simulate_future())
