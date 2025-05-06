import boto3

logs = boto3.client('logs')
log_group = "my-log-group"

def expensive_log_fetch():
    """Inefficient: Fetches ALL log events every time"""
    response = logs.filter_log_events(logGroupName=log_group)
    events = response.get("events", [])

    while "nextToken" in response:
        response = logs.filter_log_events(logGroupName=log_group, nextToken=response["nextToken"])
        events.extend(response.get("events", []))

    return events

print(expensive_log_fetch())  # This can quickly rack up high API costs!
