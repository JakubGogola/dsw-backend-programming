#!/bin/bash

# 1. Create User (Valid Request)
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "age": 30, "email": "john@example.com"}'

echo -e "\n------\n"

# 2. Create User (Invalid Request - Missing Email)
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "age": 30}'

echo -e "\n------\n"

# 3. Get Users by Age (Valid Query)
curl -X GET "http://127.0.0.1:8000/users/?age=25"

echo -e "\n------\n"

# 4. Get Users by Age (Invalid Query - Out of Range)
curl -X GET "http://127.0.0.1:8000/users/?age=15"

echo -e "\n------\n"

# 5. Get User by ID (Valid Path Parameter)
curl -X GET "http://127.0.0.1:8000/users/123"

echo -e "\n------\n"

# 6. Get User by ID (Invalid Path Parameter - Negative ID)
curl -X GET "http://127.0.0.1:8000/users/-5"

echo -e "\n------\n"

# 7. Get User by UUID (Valid UUID)
curl -X GET "http://127.0.0.1:8000/users/uuid/550e8400-e29b-41d4-a716-446655440000"

echo -e "\n------\n"

# 8. Get User by UUID (Invalid UUID Format)
curl -X GET "http://127.0.0.1:8000/users/uuid/invalid-uuid"

echo -e "\n------\n"

# 9. Create Advanced User (Valid Request)
curl -X POST "http://127.0.0.1:8000/users/advanced/" \
     -H "Content-Type: application/json" \
     -d '{
           "id": "550e8400-e29b-41d4-a716-446655440000",
           "name": "Alice",
           "age": 25,
           "email": "alice@example.com",
           "is_active": true,
           "roles": ["admin", "user"]
         }'

echo -e "\n------\n"

# 10. Create Advanced User (Invalid - Name Too Short)
curl -X POST "http://127.0.0.1:8000/users/advanced/" \
     -H "Content-Type: application/json" \
     -d '{
           "id": "550e8400-e29b-41d4-a716-446655440000",
           "name": "Al",
           "age": 25,
           "email": "alice@example.com"
         }'

echo -e "\n------\n"
