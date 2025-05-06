import boto3

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = "your-bucket-name"

# Example 1: Listing Objects 
# This lists all objects in the bucket multiple times (incurring multiple API calls)
for _ in range(1000):  # Unnecessary repeated calls
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            print(obj['Key'])

# Example 2: Downloading Files 
# Downloading each file in chunks of 1KB (high request overhead)
for obj in objects['Contents']:
    key = obj['Key']
    with open(key, 'wb') as f:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        body = response['Body']
        while chunk := body.read(1024):  # Reading in tiny chunks
            f.write(chunk)

# Example 3: Uploading Data 
# Uploading a large file in 1KB chunks instead of using multipart upload
large_file = "large_file.txt"
with open(large_file, "rb") as f:
    part_number = 1
    while chunk := f.read(1024):  # Reading tiny chunks
        s3.put_object(Bucket=bucket_name, Key=f"uploads/{large_file}_part{part_number}", Body=chunk)
        part_number += 1  # Storing unnecessary multiple objects instead of one optimized multipart upload

# Example 4: Repeatedly Checking If a File Exists
# Calls `head_object` multiple times instead of caching the response
file_key = "somefile.txt"
for _ in range(10000):  # Excessive API calls
    try:
        s3.head_object(Bucket=bucket_name, Key=file_key)
    except s3.exceptions.ClientError:
        pass

# Example 5: Deleting Objects One by One Instead of Batch Deletion
# This makes a separate API call for each object instead of using delete_objects()
for obj in objects['Contents']:
    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
