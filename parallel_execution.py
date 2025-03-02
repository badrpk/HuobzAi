import torch
import multiprocessing

def cpu_task():
    return sum(i * i for i in range(10000000))

def gpu_task():
    tensor = torch.randn(1000, 1000).to("cuda" if torch.cuda.is_available() else "cpu")
    return torch.matmul(tensor, tensor)

def parallel_execution():
    with multiprocessing.Pool(processes=2) as pool:
        cpu_result, gpu_result = pool.map(lambda f: f(), [cpu_task, gpu_task])
    return cpu_result, gpu_result

# Run optimized AI processing
parallel_execution()
