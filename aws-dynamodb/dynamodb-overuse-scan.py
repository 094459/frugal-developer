import boto3

dynamodb = boto3.client("dynamodb")
table_name = "your-dynamodb-table"

# Scanning entire table instead of querying specific records
response = dynamodb.scan(TableName=table_name)

# Process items (even if we only need a few)
for item in response.get("Items", []):
    print(item)
