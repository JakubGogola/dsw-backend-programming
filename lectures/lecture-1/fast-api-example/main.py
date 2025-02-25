from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import FastAPI, Request
import time
from fastapi import Request
from fastapi.responses import JSONResponse


app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    print(f"Request: {request.method} {request.url} | Time: {duration:.4f}s")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "HTTP Error", "detail": exc.detail},
    )

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
async def create_user(user: User):
    return {"message": "User created", "user": user}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item"}

@app.get("/users/{user_id}", summary="Get user by ID", description="Returns user details.")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}

@app.get("/cause-error")
async def cause_error():
    raise Exception("Something went wrong!")

@app.get("/teapot")
async def teapot():
    raise HTTPException(status_code=418, detail="Server refuses to brew coffee because it's a teapot.")
