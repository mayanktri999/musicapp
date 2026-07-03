from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

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

    pass