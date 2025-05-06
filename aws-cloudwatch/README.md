Why This Code is Expensive and Unoptimized

1. Sending Metrics One at a Time (put_metric_data)

1000 API calls instead of batching multiple metrics in one request.
AWS charges per API request, so this significantly increases costs.

2. Polling Logs Every Second (describe_log_streams)

Polling CloudWatch Logs too frequently leads to unnecessary API calls.
Instead, use AWS CloudWatch log subscriptions to get real-time log updates.

---

How to Optimize and Reduce Costs

✅ Batch metric submissions: Use put_metric_data with multiple MetricData entries.
✅ Use log subscriptions: Stream logs via AWS Lambda instead of polling every second.


---


Why This Lambda Function is Expensive and Inefficient

1. Excessive CloudWatch Metric Submissions (put_metric_data)

Sends one metric per invocation instead of batching multiple metrics.
Logs each message length as a separate metric, leading to thousands of API calls.

2. Inefficient Log Scanning (describe_log_streams & filter_log_events)

Fetches all log streams instead of filtering by time or recent logs.
Queries an entire day of logs on every invocation, even if new logs are minimal.

3. Running Too Frequently on CloudWatch Scheduled Events

If triggered every minute or less, it results in millions of API calls per month.
CloudWatch Logs and Metrics API calls are not free and can become extremely costly at scale.

---

✅ Batch metric submissions: Send multiple data points in a single put_metric_data request.
✅ Use CloudWatch Log Subscriptions: Stream logs using Lambda instead of polling logs repeatedly.
✅ Query logs efficiently: Use a shorter time range and only fetch new logs since the last execution.
✅ Use CloudWatch Insights for aggregation: Instead of sending custom metrics per log, use CloudWatch Insights queries.
✅ Reduce invocation frequency: Schedule Lambda to run only when needed instead of every minute.