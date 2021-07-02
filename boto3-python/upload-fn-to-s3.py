import shutil
import boto3
import os
from botocore.config import Config

config = Config(
    region_name='us-east-1'
)

client = boto3.client("s3", config=config)

s3_bucket_name = 'roger1.dreamstack.net'

response = client.list_buckets()

bucket_name = next(filter((lambda bucket: bucket['Name'] == s3_bucket_name), response['Buckets']), None)

if bucket_name is None:
    response = client.create_bucket(
        Bucket=s3_bucket_name
    )
    print("New bucket created ")
    print(response)
else:
    print(bucket_name['Name'])

shutil.make_archive('function', 'zip', 'facebook-hooks', '.')

with open('function.zip', 'rb') as data:
    client.upload_fileobj(data, s3_bucket_name, 'function.zip')

os.remove('function.zip')
