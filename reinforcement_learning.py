import random

knowledge_quality = {}  # Dictionary to store knowledge quality scores

def rate_knowledge(knowledge):
    """Simulate AI evaluating the usefulness of knowledge"""
    return random.uniform(0.5, 1.0)  # Assign random quality score

def refine_knowledge(knowledge):
    """Filter out low-quality knowledge and keep only the best data"""
    score = rate_knowledge(knowledge)
    if score > 0.7:  # Keep only high-quality knowledge
        print("✅ High-quality knowledge accepted.")
        return knowledge
    else:
        print("❌ Low-quality knowledge rejected.")
        return ""
