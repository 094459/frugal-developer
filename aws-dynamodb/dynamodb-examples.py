import boto3
import random
import string

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

table_name = "your-dynamodb-table"

# Example 1: Scanning Entire Table Multiple Times
# Scans the entire table 1000 times instead of using efficient queries
for _ in range(1000):
    response = dynamodb.scan(TableName=table_name)
    for item in response.get('Items', []):
        print(item)

# Example 2: Fetching Items One-by-One Instead of Batch Operations
# Retrieving multiple items separately rather than using batch_get_item
keys = [{'id': {'S': str(i)}} for i in range(1000)]
for key in keys:
    response = dynamodb.get_item(TableName=table_name, Key=key)
    print(response.get('Item'))

# Example 3: Writing Items One-by-One Instead of Batch Writes
# Writes 1000 items one at a time instead of using batch_write_item
for i in range(1000):
    item = {
        'id': {'S': str(i)},
        'data': {'S': ''.join(random.choices(string.ascii_letters, k=100))}
    }
    dynamodb.put_item(TableName=table_name, Item=item)

# Example 4: Deleting Items One-by-One Instead of Batch Deletes
# Deletes records one at a time instead of using batch_write_item
for key in keys:
    dynamodb.delete_item(TableName=table_name, Key=key)

# Example 5: Repeatedly Checking If an Item Exists
# Calls `get_item` 10,000 times instead of fetching items in a single query
for i in range(10000):
    key = {'id': {'S': str(i)}}
    try:
        response = dynamodb.get_item(TableName=table_name, Key=key)
        if 'Item' not in response:
            print(f"Item {i} not found")
    except dynamodb.exceptions.ResourceNotFoundException:
        pass

# Example 6: Using a Scan Instead of Query for Indexed Lookups
# Scans the entire table to find items instead of using an index query
def find_item(value):
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression="data = :val",
        ExpressionAttributeValues={":val": {"S": value}}
    )
    return response.get('Items', [])

