import multiprocessing

def process_task(task_id):
    print(f"🔄 Processing task {task_id} in parallel...")
    
tasks = [multiprocessing.Process(target=process_task, args=(i,)) for i in range(5)]

for task in tasks:
    task.start()

for task in tasks:
    task.join()

print("✅ All tasks completed in parallel!")
