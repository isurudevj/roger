import boto3

client = boto3.client('sts')

response = client.get_caller_identity()

account_id = response['Account']

print("Account id of the aws user - " + account_id)

client = boto3.client('lambda')

function_name = "facebook-hook"
bucket_id = "facebook.dreamstack.net"
role_arn = "arn:aws:iam::" + account_id + ":role/lambda-role"

response = client.create_function(
    Code={
        'S3Bucket': bucket_id,
        'S3Key': 'function.zip',
    },
    FunctionName=function_name,
    Role=role_arn,
    Runtime='nodejs14.x',
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)
