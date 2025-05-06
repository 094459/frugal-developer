❌ Breaks on Spot Instances

This example does not handle Spot Instance interruptions, leading to:

Lost progress if the instance is terminated.
Wasted computing time due to no recovery mechanisms.
Unpredictable failures when using Spot Instances.

❌ Why This is NOT Spot-Friendly:
No interruption handling → If the Spot Instance is interrupted, all progress is lost.
No checkpointing → If the instance stops at step 90, the next instance must restart from step 0.
No auto-recovery strategy → There’s no way to detect termination and restart elsewhere.


✅ Works well with Spot Instances
This example is designed to handle Spot Instance interruptions gracefully using:

Frequent checkpointing to save progress.
Automatic interruption handling (via AWS EC2 Spot Termination Notices).
Auto-recovery (relaunching the process if interrupted).

✅ Why This is Spot-Friendly:

Implements checkpointing → Saves progress every 10 iterations.
Handles Spot Termination Notices → Gracefully stops before forced termination.
Allows auto-recovery → Can resume from the last saved step if restarted on a new Spot Instance.
Minimizes data loss → Writes progress to disk, avoiding full task restart.

---

### Things to think about

1️⃣ Not Handling Spot Instance Interruptions

❌ Gotcha:
AWS can terminate Spot Instances with only 2 minutes' notice.
If your app doesn't listen for interruption signals, it may lose all progress.

✅ Solution:
Monitor Spot Termination Notices via the AWS Metadata Service.
Handle termination signals gracefully (save progress and exit cleanly).

```
import requests

def is_spot_instance_terminating():
    """Check if the Spot Instance is scheduled for termination"""
    try:
        response = requests.get(
            "http://169.254.169.254/latest/meta-data/spot/instance-action",
            timeout=1
        )
        return response.status_code == 200  # If 200, the instance is terminating
    except requests.exceptions.RequestException:
        return False  # No interruption detected

```

2️⃣ No Checkpointing (Losing Progress on Termination)

❌ Gotcha:
If a long-running process is interrupted, it must restart from scratch.
All computation before termination is wasted.
✅ Solution:
Implement checkpointing: Save progress to a database, file, or cloud storage.
Use Amazon S3, DynamoDB, or EFS to store checkpoints.
Example Code (Checkpointing)

```
import json

CHECKPOINT_FILE = "progress_checkpoint.json"

def save_checkpoint(step):
    """Save processing progress"""
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"last_step": step}, f)

def load_checkpoint():
    """Load last saved progress"""
    try:
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f)["last_step"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0  # Start from zero if no checkpoint found

```

3️⃣ Using Spot Instances for Non-Interruptible Workloads

❌ Gotcha:
Some applications must run to completion (e.g., database transactions, critical batch jobs).
If the Spot Instance is interrupted mid-process, data integrity issues may occur.
✅ Solution:
Use On-Demand instances for critical workloads.
Use a job scheduler (e.g., AWS Step Functions, Kubernetes) to reschedule failed jobs.

Example Use Case:

✅ Spot-Friendly Workloads	    ❌ Not Spot-Friendly Workloads
Machine Learning Training	    Stateful Databases
Batch Processing (HPC)	        Real-time Transaction Processing
Web Crawlers	                Payment Processing
Big Data Analytics	            Streaming Pipelines (Kafka, Kinesis)


4️⃣ Not Using Auto Recovery (Jobs Get Lost)

❌ Gotcha:
If a Spot Instance is interrupted, it won’t restart automatically.
Your workload might get lost unless manually restarted.
✅ Solution:
Use Auto Scaling Groups (ASG) to automatically relaunch new Spot Instances.
Use ECS or Kubernetes to reschedule interrupted jobs.

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name my-spot-group \
    --launch-template LaunchTemplateId=my-launch-template \
    --min-size 1 --max-size 10 \
    --instance-market-options MarketType=spot

```

5️⃣ Ignoring Data Persistence (Ephemeral Storage Loss)

❌ Gotcha:
Spot Instances lose all local (ephemeral) storage when terminated.
If you store important files in /tmp, they will be lost.
✅ Solution:
Use Amazon S3, EFS, or EBS for data that needs to persist.
Attach EBS volumes to Spot Instances so data remains available.

Example: Mounting EBS in a Spot Instance

```
aws ec2 attach-volume --volume-id vol-1234567890abcdef --instance-id i-1234567890abcdef --device /dev/sdf

```