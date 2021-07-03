## Prerequisites

### 1. Install python 3.+

### 2. Install boto3 - aws sdk for python

```shell
pip install boto3 
```

### 3. Install `chalice`

```shell
pip instlal chalice
```

### 4. Install AWS CLI
[AWS CLI Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

### 5. Local testing /Deploying Facebook hooks

Go to `calice-projects/facebook-hooks`

1. Deploy cloudformation stack to create sqs topic

```shell
aws cloudformation deploy --template-file fbh_cf_template.yml --stack-name "facebook-hooks"
```

2. Running chalice locally to test
```shell
chalice local
```

3. Deploying chalice to AWS

```shell
chalice deploy
```

## Extras

1. Creating a project with chalice

```shell
chalice new-project facebook-hooks
```

## Resources

[Cloud Formation SQS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.html)

[AWS Boto3 python SDK API Doc](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)

## Helpful tutorials

[Book Store App](https://auth0.com/blog/how-to-create-crud-rest-api-with-aws-chalice/)