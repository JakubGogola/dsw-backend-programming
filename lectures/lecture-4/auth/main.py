from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from database import SessionLocal, engine, Base
from models import User
import users
from auth import create_access_token, decode_access_token
from password import verify_password

app = FastAPI()

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Add startup event to create test user
@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    try:
        # Check if test user already exists
        test_user = users.get_user(db, "testuser")
        if not test_user:
            # Create test user if it doesn't exist
            users.create_user(db, "testuser", "password123")
            print("Test user created successfully!")
            print("Username: testuser")
            print("Password: password123")
    except Exception as e:
        print(f"Error creating test user: {e}")
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = users.get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid login credentials")

    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    if users.get_user(db, username):
        raise HTTPException(status_code=400, detail="User already exists")
    user = users.create_user(db, username, password)
    return {"message": "Account created", "username": user.username}

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    user_data = decode_access_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": f"Welcome {user_data['sub']}!"}
