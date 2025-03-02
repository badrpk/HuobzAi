def make_decision(situation):
    if "urgent" in situation:
        return "Prioritize and take immediate action!"
    elif "complex" in situation:
        return "Break problem into smaller steps and analyze each."
    else:
        return "Gather more data before deciding."

# Example
situation = "This is an urgent security issue."
print(make_decision(situation))
