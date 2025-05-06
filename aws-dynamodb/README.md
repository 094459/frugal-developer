Why This Code is Expensive and Unoptimized

1. Overusing scan() Instead of query()

Scanning the entire table 1000 times is extremely costly and slow, especially for large datasets.
A query operation should be used instead if the table has a partition key.

2. Fetching Items One-by-One Instead of Batch Reads

Uses get_item in a loop instead of a single batch_get_item request.
DynamoDB charges per read request, making this unnecessarily expensive.

3. Writing Items Inefficiently

Uses put_item 1000 times instead of batch writing via batch_write_item.
Batch writing reduces API calls and improves efficiency.

4. Deleting Items One-by-One Instead of Batch Deletes

Calls delete_item repeatedly instead of using batch write for deletions.

5. Checking Existence with Excessive API Calls

Calls get_item 10,000 times to check existence instead of querying multiple items at once.

6. Using a Full Table Scan for Indexed Lookups

---

Instead of using query() on an indexed attribute, it scans the entire table, significantly increasing cost.

Better Alternatives to Optimize DynamoDB Usage
✅ Use query() instead of scan() where possible.
✅ Use batch_get_item() to fetch multiple items in a single request.
✅ Use batch_write_item() for bulk inserts and deletes.
✅ Cache results to avoid unnecessary repeated lookups.
✅ Use Global Secondary Indexes (GSI) for fast indexed queries instead of full scans.

---

**Why is it inffecient to log a metric with every Lambda invocation?**

1️⃣ Increased CloudWatch API Costs
AWS charges for each put_metric_data API request.
If your Lambda function is invoked 100,000 times per day, that results in 100,000 CloudWatch API calls.
Pricing (as of AWS Free Tier limits):
First 1 million API requests/month → Free
Beyond that → ~$0.01 per 1,000 requests
100M invocations = $1,000/month just for metric logging! 🚨
✅ Optimization:

Batch metric data using put_metric_data to send multiple data points in one request.
Use CloudWatch Embedded Metrics Format (EMF) to reduce API calls.
2️⃣ Increased Latency and Execution Time
Each put_metric_data call adds extra execution time to the Lambda function.
Since AWS Lambda bills per millisecond, even small delays increase cost.
If put_metric_data takes 100ms, it slows execution and increases Lambda costs.
✅ Optimization:

Asynchronous logging: Offload metric logging to AWS CloudWatch Logs and process it later.
Use AWS Embedded Metrics for efficient logging.
3️⃣ Unnecessary Storage Costs
Each metric data point is stored in CloudWatch Metrics, which incurs storage costs.
Storing high-frequency invocation data rapidly increases CloudWatch storage usage.
✅ Optimization:

Instead of logging per invocation, aggregate metrics and push them at intervals (e.g., every 5 mins).
Use percentile-based metrics instead of logging every event individually.
4️⃣ Duplicate or Redundant Metrics
Logging invocation count per Lambda duplicates the default CloudWatch metric (Invocations).
AWS Lambda automatically tracks invocations, durations, and errors without needing custom metrics.
✅ Optimization:

Use built-in Lambda metrics like AWS/Lambda Invocations instead of custom metrics.
5️⃣ Exceeding CloudWatch Limits
CloudWatch has soft limits on the number of custom metrics per account.
Excessive put_metric_data calls may cause throttling or delays in metric updates.
✅ Optimization:

Consolidate metrics before sending.
Use CloudWatch Logs Insights to query logs instead of sending every event as a metric.



**Optimized Example**

Instead of calling put_metric_data on every Lambda invocation, batch and send metrics periodically.


```
import boto3
import time

cloudwatch = boto3.client('cloudwatch')
metric_buffer = []

def log_metric(value):
    global metric_buffer
    metric_buffer.append({'MetricName': 'ExecutionCount', 'Value': value, 'Unit': 'Count'})

    if len(metric_buffer) >= 10:  # Batch every 10 metrics
        cloudwatch.put_metric_data(
            Namespace="MyLambdaMetrics",
            MetricData=metric_buffer
        )
        metric_buffer = []  # Reset buffer

def lambda_handler(event, context):
    start_time = time.time()
    
    # Do some work...
    time.sleep(0.1)  

    log_metric(1)  # Log once, but in batches

    return {"statusCode": 200, "execution_time": time.time() - start_time}
```



Benefits of This Approach
✅ Reduces API calls by up to 10x (sending 1 batch instead of 10 separate requests).
✅ Minimizes execution time and improves Lambda efficiency.
✅ Lowers CloudWatch storage costs by reducing unnecessary metric data points.
✅ Prevents exceeding CloudWatch limits and avoids throttling.