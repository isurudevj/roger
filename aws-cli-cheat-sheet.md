#S3

1. Copy file from bucket to local

```shell
aws s3 cp s3:\\mybucket\myfile.git .
```

2. Copy file to bucket from local

```shell
aws s3 cp myfile.gif s3:\\mybucket\myfile.gif
```

3. List files from bucket

```shell
aws s3 ls mybucket
```