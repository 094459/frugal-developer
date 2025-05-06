import boto3
import pandas as pd
import io

s3 = boto3.client('s3')
bucket_name = "your-bucket-name"
file_key = "large-dataset.csv"

# Downloading the entire dataset every time
response = s3.get_object(Bucket=bucket_name, Key=file_key)
data = response['Body'].read()  # Reads the entire file into memory

# Loading a massive dataset into Pandas all at once
df = pd.read_csv(io.BytesIO(data))
print(df.head())
