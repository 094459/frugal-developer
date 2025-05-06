import boto3
import time

logs = boto3.client('logs')
log_group = "my-log-group"

def optimized_log_fetch():
    """Optimized: Fetches only recent logs in batches"""
    now = int(time.time() * 1000)
    one_hour_ago = now - (60 * 60 * 1000)  # Fetch last 1 hour of logs

    response = logs.filter_log_events(
        logGroupName=log_group,
        startTime=one_hour_ago,
        endTime=now,  # Fetch only recent logs
        limit=50  # Limit log count per API call
    )
    
    return response.get("events", [])

print(optimized_log_fetch())  # Much lower API cost!
