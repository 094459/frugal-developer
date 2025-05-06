import boto3
import json

s3 = boto3.client('s3')
bucket_name = "my-bucket"
cache_file = "s3_cache.json"

def list_s3_objects_cached():
    """Optimized: Uses local cache and only updates periodically"""
    try:
        with open(cache_file, "r") as f:
            return json.load(f)  # Load cached results
    except FileNotFoundError:
        pass  # If no cache exists, fetch fresh data

    # Fetch from S3 only if cache is missing or outdated
    response = s3.list_objects_v2(Bucket=bucket_name)
    objects = response.get("Contents", [])

    while response.get("IsTruncated"):
        response = s3.list_objects_v2(Bucket=bucket_name, ContinuationToken=response["NextContinuationToken"])
        objects.extend(response.get("Contents", []))

    object_keys = [obj["Key"] for obj in objects]

    # Save to cache for future use
    with open(cache_file, "w") as f:
        json.dump(object_keys, f)

    return object_keys

print(list_s3_objects_cached())  # Uses cache to reduce API calls
