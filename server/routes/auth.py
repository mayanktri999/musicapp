   
import uuid
from fastapi import FastAPI, HTTPException
from models.user import User
import bcrypt
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from database import db

router = APIRouter()


app = FastAPI()

@app.post("/signup")
def signup_user(user: UserCreate):
    
    
    #check if the user already exists in the database
    user_db = db.query(User).filter((User.email == user.email)).first()

    if  user_db:
         raise HTTPException(status_code=400, detail="User with this email already exists")
         
   
    #add the user to the database
    hash_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), username=user.username, email=user.email, password=hash_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

