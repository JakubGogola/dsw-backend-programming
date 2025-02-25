# coding: utf-8

from fastapi import APIRouter, Body, HTTPException, Path
from pydantic import StrictInt
from typing import List

from openapi_server.models.order import Order
from openapi_server.models.order_create import OrderCreate
from openapi_server.models.user import User
from openapi_server.models.user_create import UserCreate

router = APIRouter()

# Mock data
mock_users = [
    User(id=1, name="John Doe", email="john.doe@example.com"),
    User(id=2, name="Jane Smith", email="jane.smith@example.com"),
]

mock_orders = [
    Order(id=1, user_id=1, total=100.0),
    Order(id=2, user_id=1, total=200.0),
    Order(id=3, user_id=2, total=150.0),
]

@router.post("/orders", response_model=Order, status_code=201)
async def create_order(order_create: OrderCreate = Body(...)):
    new_order = Order(id=len(mock_orders) + 1, user_id=order_create.user_id, total=order_create.total)
    mock_orders.append(new_order)
    return new_order

@router.post("/users", response_model=User, status_code=201)
async def create_user(user_create: UserCreate = Body(...)):
    new_user = User(id=len(mock_users) + 1, name=user_create.name, email=user_create.email)
    mock_users.append(new_user)
    return new_user

@router.delete("/users/{id}", status_code=204)
async def delete_user(id: StrictInt = Path(...)):
    global mock_users
    mock_users = [user for user in mock_users if user.id != id]
    return None

@router.get("/users/{id}", response_model=User)
async def get_user(id: StrictInt = Path(...)):
    for user in mock_users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/users/{id}/orders", response_model=List[Order])
async def get_user_orders(id: StrictInt = Path(...)):
    return [order for order in mock_orders if order.user_id == id]

@router.get("/users", response_model=List[User])
async def get_users():
    return mock_users

