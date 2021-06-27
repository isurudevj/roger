import boto3

# Let's use Amazon S3
client = boto3.client('apigateway')

api_name = "RogerTestApi"

response = client.create_rest_api(
    name=api_name
)
