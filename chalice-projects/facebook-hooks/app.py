import boto3
from chalice import Chalice

app = Chalice(app_name='facebook-hooks')
sqs_client = boto3.client("sqs")
sts_client = boto3.client('sts')


@app.route('/hooks', methods=['POST'])
def message():
    data = app.current_request.raw_body.decode()
    caller_identity = sts_client.get_caller_identity()
    account_id = caller_identity['Account']
    response = sqs_client.send_message(
        QueueUrl=f'https://sqs.us-east-1.amazonaws.com/{account_id}/facebook-hooks',
        MessageBody=data
    )
    print(response)
    return "OK"


@app.route('/hooks', methods=['GET'])
def verify():
    hub_challenge = app.current_request.query_params['hub.challenge']
    return hub_challenge
