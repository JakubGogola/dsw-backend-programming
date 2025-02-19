#!/bin/bash

BASE_URL="http://localhost:8000"

curl -X GET "$BASE_URL/users/1" | jq

curl -X POST "$BASE_URL/users" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Alice Johnson",
           "email": "alice.johnson@example.com"
         }' | jq

curl -X GET "$BASE_URL/items/2" | jq

curl -X GET "$BASE_URL/items/1" | jq

curl -X GET "$BASE_URL/cause-error" | jq

curl -X GET "$BASE_URL/teapot" | jq
