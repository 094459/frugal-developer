import boto3

s3 = boto3.client('s3')
bucket_name = "my-bucket"

def list_all_s3_objects():
    """Inefficient: Lists ALL objects every time, causing excessive API calls"""
    response = s3.list_objects_v2(Bucket=bucket_name)
    objects = response.get("Contents", [])
    
    while response.get("IsTruncated"):
        response = s3.list_objects_v2(Bucket=bucket_name, ContinuationToken=response["NextContinuationToken"])
        objects.extend(response.get("Contents", []))

    return [obj["Key"] for obj in objects]  # Returns full list of object keys

print(list_all_s3_objects())  # This can generate high costs if called frequently!
