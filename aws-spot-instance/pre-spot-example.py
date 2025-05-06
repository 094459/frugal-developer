import time

def process_large_task():
    """Simulated long-running process that does NOT handle Spot interruptions"""
    for i in range(100):
        print(f"Processing step {i}...")
        time.sleep(5)  # Simulate long-running processing
    print("Task completed!")

# Run the processing function
process_large_task()
