#!/bin/sh

curl -X POST localhost:8000/hooks -H 'Content-Type: application/json;utf-8' -d '{
  "message" : "Hello Chalice"
}'