import shutil

def optimize_storage():
    """Checks and optimizes storage usage."""
    total, used, free = shutil.disk_usage("/")
    
    storage_used = (used / total) * 100  # Convert to percentage
    total_storage_gb = total // (1024 ** 3)  # Convert bytes to GB
    
    print(f"\n💾 **Storage Used:** {storage_used:.2f}% ({total_storage_gb}GB)")

    if storage_used >= 95:
        print("⚠️ **Warning:** Storage is at 95%. Initiating automatic compression...")
        # Implement automatic compression logic here (e.g., remove redundant knowledge)

    return storage_used, total_storage_gb
