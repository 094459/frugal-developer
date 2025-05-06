import boto3
from boto3.dynamodb.conditions import Key

# Use the resource interface instead of client for higher-level operations
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("your-dynamodb-table")

def query_with_pagination(partition_key_value, page_size=25):
    """
    Query DynamoDB with pagination to reduce costs and improve performance.
    
    Args:
        partition_key_value: The value for the partition key to query
        page_size: Number of items to retrieve per page
    """
    # Replace 'your-partition-key' with your actual partition key name
    query_params = {
        'KeyConditionExpression': Key('your-partition-key').eq(partition_key_value),
        'Limit': page_size
    }
    
    # Initial query
    response = table.query(**query_params)
    
    # Process the first page of results
    process_items(response.get('Items', []))
    
    # Continue fetching and processing if there are more results
    while 'LastEvaluatedKey' in response:
        query_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
        response = table.query(**query_params)
        process_items(response.get('Items', []))

def process_items(items):
    """Process the retrieved items."""
    for item in items:
        print(item)

def scan_with_pagination_if_necessary(filter_expression=None, page_size=25):
    """
    Use scan with pagination and filtering only when absolutely necessary.
    This is still expensive but better than scanning the entire table at once.
    
    Args:
        filter_expression: Optional filter to reduce returned data
        page_size: Number of items to retrieve per page
    """
    scan_params = {
        'Limit': page_size
    }
    
    if filter_expression:
        scan_params['FilterExpression'] = filter_expression
    
    # Initial scan
    response = table.scan(**scan_params)
    
    # Process the first page of results
    process_items(response.get('Items', []))
    
    # Continue fetching and processing if there are more results
    while 'LastEvaluatedKey' in response:
        scan_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
        response = table.scan(**scan_params)
        process_items(response.get('Items', []))

# Example usage:
if __name__ == "__main__":
    # Preferred: Use query with a specific partition key value
    # query_with_pagination("example-id")
    
    # Only if absolutely necessary: Use scan with pagination and filtering
    # from boto3.dynamodb.conditions import Attr
    # filter_expr = Attr('status').eq('active')
    # scan_with_pagination_if_necessary(filter_expr)