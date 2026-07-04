
from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app = FastAPI()
DATABASE_URL = "postgresql://postgres:mayank2006@localhost:5432/musicapp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/signup")
def signup_user(user: UserCreate):
    #extract user data from the request
    print(user.username)
    print(user.email)
    print(user.password)
    #check if the user already exists in the database
    #connect to the database and check for existing user

    pass