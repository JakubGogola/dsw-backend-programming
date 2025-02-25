#!/bin/bash

curl -X POST "http://localhost:8000/orders" \
     -H "Content-Type: application/json" \
     -d '{
           "user_id": 1,
           "total": 250.0
         }' | jq

curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Alice Johnson",
           "email": "alice.johnson@example.com"
         }' | jq

curl -X DELETE "http://localhost:8000/users/1" | jq

curl -X GET "http://localhost:8000/users/1" | jq

curl -X GET "http://localhost:8000/users/1/orders" | jq

curl -X GET "http://localhost:8000/users" | jq
