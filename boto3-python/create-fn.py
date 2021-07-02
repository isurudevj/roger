import boto3
from botocore.config import Config

config = Config(
    region_name='us-east-1'
)

client = boto3.client('sts', config=config)

response = client.get_caller_identity()

account_id = response['Account']

print("Account id of the aws user - " + account_id)

client = boto3.client('lambda', config=config)

function_name = "facebook-hook"
bucket_id = "roger1.dreamstack.net"
role_arn_copy = "arn:aws:iam::209594204310:role/service-role/GetStartedLambdaBasicExecutionRole"
role_arn = "arn:aws:iam::" + account_id + ":role/service-role/facebook-lambda"

iam = boto3.client('iam', config=config)
response = client.create_role(
    AssumeRolePolicyDocument='<URL-encoded-JSON>',
    Path='/roger',
    RoleName='FacebookRole',
)

print('Role creation response', response)

response = client.create_function(
    Code={
        'S3Bucket': bucket_id,
        'S3Key': 'function.zip',
    },
    FunctionName=function_name,
    Role=role_arn_copy,
    Runtime='nodejs14.x',
    Handler='index.handler',
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)
