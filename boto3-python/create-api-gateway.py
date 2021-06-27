import boto3

# Let's use Amazon S3
client = boto3.client('s3')

data = open('../github-docs/roger-roger.gif', 'rb')
response = client.put_object(
    Body= data,
    Bucket='roger.dreamstack.net',
    Key='roger.gif',
)
print(response)
