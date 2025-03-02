import json

class HuobzMemory:
    def __init__(self, memory_file="huobz_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def remember(self, topic, info):
        self.memory[topic] = info
        self.save_memory()

    def recall(self, topic):
        return self.memory.get(topic, "No knowledge found.")

# Example Usage:
huobz_memory = HuobzMemory()
huobz_memory.remember("Quantum Computing", "It is a type of computing that uses quantum bits (qubits).")
print(huobz_memory.recall("Quantum Computing"))
