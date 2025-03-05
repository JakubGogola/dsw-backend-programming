#!/bin/bash

# Base URL for the API
BASE_URL="http://localhost:8000"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Create a new user (POST /users/)
create_user() {
    local name=$1
    local email=$2
    echo "Creating a new user..."
    response=$(curl -s -w "\n%{http_code}" -X 'POST' "$BASE_URL/users/" \
        -H 'Content-Type: application/json' \
        -d "{
            \"name\": \"$name\",
            \"email\": \"$email\",
            \"is_active\": true
        }")
    
    # Split response into body and status code
    body=$(echo "$response" | head -n 1)
    status_code=$(echo "$response" | tail -n 1)

    echo "Status code: $status_code"
    echo "Response: $body"
    echo "------------------------------------"
}

# Get a list of users (GET /users/)
get_users() {
    echo "Fetching the list of users..."
    response=$(curl -s -w "\n%{http_code}" -X 'GET' "$BASE_URL/users/")
    
    body=$(echo "$response" | head -n 1)
    status_code=$(echo "$response" | tail -n 1)

    echo "Status code: $status_code"
    echo "Response: $body"
    echo "------------------------------------"
}

# Get a specific user by ID (GET /users/{user_id})
get_user_by_id() {
    USER_ID=$1
    echo "Fetching user with ID $USER_ID..."
    response=$(curl -s -w "\n%{http_code}" -X 'GET' "$BASE_URL/users/$USER_ID")
    
    body=$(echo "$response" | head -n 1)
    status_code=$(echo "$response" | tail -n 1)

    echo "Status code: $status_code"
    echo "Response: $body"
    echo "------------------------------------"
}

# Main function to run all tests
run_tests() {
    # Generate a random email for John Doe
    JOHN_EMAIL="john_$(date +%s)_$RANDOM@example.com"
    
    echo -e "${GREEN}Testing successful user creation${NC}"
    create_user "John Doe" "$JOHN_EMAIL"
    
    echo -e "${GREEN}Testing duplicate email (should fail)${NC}"
    create_user "Jane Doe" "$JOHN_EMAIL"
    
    echo -e "${GREEN}Testing invalid email format (should fail)${NC}"
    create_user "Invalid Email" "not-an-email"
    
    echo -e "${GREEN}Testing empty name (should fail)${NC}"
    create_user "" "test@example.com"
    
    echo -e "${GREEN}Testing get all users${NC}"
    get_users
    
    echo -e "${GREEN}Testing get existing user${NC}"
    get_user_by_id 1
    
    echo -e "${GREEN}Testing get non-existent user${NC}"
    get_user_by_id 999
}

# Run the tests
run_tests
