# roger

Roger is a collection of easy web hooks using AWS serverless.


<h1 align="center">Roger Roger !!!</h1>
<h1 align="center">Web hooks made easy for developers.</h1>

<p align="center">
    <img width="460" height="300" src="https://github.com/isurudevj/roger/raw/main/github-docs/roger-roger.gif">
</p>


<h2>Motive</h2>

<p>
Often times developers have to set up webhooks to integrate with certain web service providers.
<br><br>Examples:<br><br>
facebook messenger webhooks - for chat bots<br>
twitter feeds webhooks - for sentiment analysis<br> 
braintree webhooks - for payment subscription updates<br>
</p>

Using a tool like [ngrok](https://ngrok.com) is usually the preferred way by developers,
but roger is a better way based on AWS serverless listed bellow.

1. AWS API Gateway
2. AWS Lambda
3. AWS SQS

Amount you will have to pay is much lesser than the tunnel based solutions.
Its production ready, design for high availability and scalability.

AWS provides the AWS Chalice a boiler-plate, a python based microframework for serverless.
Serverless coding and deployment is never being this easy.


# Two steps approach

1. I use AWS cloudformation to create the resources I need. (here I use SQS)
2. Chalice to create, test and deploy AWS serverless app

### Topics

[Set up](chalice.md)

### Extras

[Developer Essentials Boto3](DEVELOPER.md)<br>
[AWS CLI Cheat Sheet](aws-cli-cheat-sheet.md)<br>
[Lambda + API Gateway](https://docs.aws.amazon.com/code-samples/latest/catalog/python-lambda-boto_client_examples-api_gateway_rest.py.html) <br>
[AWS Chalice](chalice-resources.md) <br>


#### Facebook Bots
[Web hooks](https://developers.facebook.com/docs/messenger-platform/webhook#setup)

