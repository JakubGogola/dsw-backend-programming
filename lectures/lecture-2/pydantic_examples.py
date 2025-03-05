from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

class AdvancedUser(BaseModel):
    id: UUID
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=100)
    email: EmailStr
    is_active: bool = True
    roles: list[str] = ["user"]

@app.post("/users/")
async def create_user(user: User):
    return {"message": f"User {user.name} with email {user.email} created!"}

@app.get("/users/")
async def read_users(age: int = Query(..., gt=18, lt=100)):
    return {"message": f"Users with age {age}"}

@app.get("/users/{user_id}")
async def read_user(user_id: int = Path(..., gt=0)):
    return {"message": f"User ID: {user_id}"}

@app.get("/users/uuid/{user_uuid}")
async def read_user_by_uuid(user_uuid: UUID):
    return {"message": f"User UUID: {user_uuid}"}

@app.post("/users/advanced/")
async def create_advanced_user(user: AdvancedUser):
    return {"message": f"Advanced user {user.name} with roles {user.roles} created!"}


