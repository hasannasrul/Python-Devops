import boto3
import os

# Goal is to create s3 bucket 
session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key=('AWS_SECRET_ACCESS_KEY'))

s3 = session.client('s3')
bucket_name = 'hasan-3080-boto'
response = s3.create_bucket(Bucket=bucket_name)
# response
print(response)