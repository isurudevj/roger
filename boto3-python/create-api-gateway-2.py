import boto3

# Let's use Amazon S3
client = boto3.client('apigateway')

api_name = "RogerTestApi"
path_part = "roger"

response = client.get_rest_apis()

first = next(filter((lambda item: item['name'] == api_name), response['items']), None)

rest_api_id = first['id']

print("API ID -> " + rest_api_id)

response = client.get_resources(
    restApiId=rest_api_id
)

parent_resource_id = next(filter(lambda item: item['path'] == "/", response['items']), None)['id']

print("Parent Resource ID -> " + parent_resource_id)

response = client.create_resource(
    restApiId=rest_api_id,
    parentId=parent_resource_id,
    pathPart='roger'
)

response = client.put_method(
    restApiId=rest_api_id,
    resourceId=response['id'],
    httpMethod='POST',
    authorizationType='NONE'
)
