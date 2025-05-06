import boto3
import time

s3 = boto3.client('s3')
bucket_name = "your-bucket-name"

# List the bucket contents 1000 times (excessive API calls)
for _ in range(1000):
    objects = s3.list_objects_v2(Bucket=bucket_name)

# Download the same files over and over instead of caching
for obj in objects.get("Contents", []):
    key = obj["Key"]
    s3.download_file(bucket_name, key, f"/tmp/{key}")  # Re-downloading every time

# Uploading large file in small chunks without using multipart upload
with open("large_file.dat", "rb") as f:
    while chunk := f.read(1024):  # Reading in tiny 1KB chunks
        s3.put_object(Bucket=bucket_name, Key="uploads/large_file.dat", Body=chunk)
