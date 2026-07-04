from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine

app = FastAPI()
DATABASE_URL = "postgresql://postgres:password@localhost/dbname"
engine = create_engine(DATABASE_URL)

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