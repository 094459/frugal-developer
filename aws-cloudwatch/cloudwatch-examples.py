import boto3
import time
import random

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

namespace = "MyApplicationMetrics"

# Example 1: Sending Metrics One at a Time Instead of Batching
# This loops 1000 times, making 1000 separate API calls (very costly!)
for i in range(1000):
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': 'RequestCount',
                'Value': random.randint(1, 100),
                'Unit': 'Count'
            }
        ]
    )
    time.sleep(0.1)  # Artificial delay, but still excessive API calls

# Example 2: Fetching Logs Inefficiently (Polling Too Often)
# Polls CloudWatch Logs every second instead of using proper log streaming
log_group = "MyApplicationLogGroup"
log_stream = "MyApplicationLogStream"

while True:  # Infinite loop polling logs every second (very expensive)
    response = cloudwatch.describe_log_streams(
        logGroupName=log_group,
        logStreamNamePrefix=log_stream
    )
    print(response)
    time.sleep(1)  # Polling too frequently
