#!/bin/sh

curl -X POST 'https://1crb6huiwd.execute-api.us-east-1.amazonaws.com/dev/hooks' -H 'Content-Type: application/json;utf-8' -d '{
  "message" : "Hello Chalice World"
}'