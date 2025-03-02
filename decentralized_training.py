from huobz_blockchain import distribute_training_task

def train_huobz_on_edge():
    task_data = {"task": "train", "model": "huobz", "dataset": "latest"}
    distribute_training_task(task_data)

train_huobz_on_edge()
