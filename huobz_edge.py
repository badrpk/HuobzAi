import os

def check_device():
    """Detect if Huobz AI can run on an edge device"""
    if os.path.exists("/sys/class/thermal/thermal_zone0/temp"):
        print("✅ Running Huobz AI on an edge device.")
    else:
        print("❌ Edge device not detected.")

check_device()
