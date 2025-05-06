import boto3
import time
import os

# Initialize EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# File to store processing progress
CHECKPOINT_FILE = "checkpoint.txt"

def save_checkpoint(progress):
    """Save progress to a checkpoint file"""
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(str(progress))

def load_checkpoint():
    """Load last checkpointed progress"""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def is_spot_termination():
    """Check if the instance is being interrupted"""
    try:
        response = boto3.client("ec2").describe_instance_status(
            IncludeAllInstances=True
        )
        for instance in response["InstanceStatuses"]:
            for event in instance.get("Events", []):
                if event["Code"] == "instance-stop":
                    return True
    except Exception as e:
        print("Error checking Spot termination status:", e)
    return False

def process_large_task():
    """Simulated long-running process with checkpointing"""
    progress = load_checkpoint()
    
    for i in range(progress, 100):
        if is_spot_termination():
            print("Spot instance is terminating! Saving progress...")
            save_checkpoint(i)
            return
        
        print(f"Processing step {i}...")
        time.sleep(5)  # Simulate processing time
        
        if i % 10 == 0:
            save_checkpoint(i)  # Save progress every 10 steps

    print("Task completed!")

# Run the processing function
process_large_task()
