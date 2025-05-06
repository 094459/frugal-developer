import boto3
import json
import time

# Initialize AWS clients
cloudwatch = boto3.client('cloudwatch')
logs = boto3.client('logs')

# Constants
LOG_GROUP = "MyLambdaLogGroup"
METRIC_NAMESPACE = "MyLambdaMetrics"

def lambda_handler(event, context):
    # Example 1: Sending a CloudWatch Metric on Every Invocation (High API Calls)
    # Instead of batching, this sends a metric every time Lambda is triggered.
    cloudwatch.put_metric_data(
        Namespace=METRIC_NAMESPACE,
        MetricData=[
            {
                'MetricName': 'Invocations',
                'Value': 1,
                'Unit': 'Count'
            }
        ]
    )

    # Example 2: Scanning All Log Streams Instead of Filtering Efficiently
    # Fetches all log streams instead of limiting by time range or specific criteria.
    log_streams = logs.describe_log_streams(
        logGroupName=LOG_GROUP
    )

    # Example 3: Querying an Entire Day of Logs Repeatedly
    # This fetches 24 hours of logs every time Lambda runs, causing redundant processing.
    end_time = int(time.time() * 1000)  # Current time in milliseconds
    start_time = end_time - (24 * 60 * 60 * 1000)  # 24 hours ago

    response = logs.filter_log_events(
        logGroupName=LOG_GROUP,
        startTime=start_time,
        endTime=end_time
    )

    log_entries = [event['message'] for event in response.get('events', [])]
    
    # Example 4: Storing Logs as Custom Metrics (High Cost)
    # Each log message is sent as a separate metric instead of aggregating them.
    for message in log_entries:
        cloudwatch.put_metric_data(
            Namespace=METRIC_NAMESPACE,
            MetricData=[
                {
                    'MetricName': 'LogMessageLength',
                    'Value': len(message),
                    'Unit': 'Count'
                }
            ]
        )

    # Example 5: Running in an Overly Frequent CloudWatch Schedule
    # If this Lambda is scheduled to run every minute or every few seconds, the costs escalate quickly.

    return {
        'statusCode': 200,
        'body': json.dumps(f"Processed {len(log_entries)} log messages")
    }
