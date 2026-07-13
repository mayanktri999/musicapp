   
import uuid
from fastapi import Depends, FastAPI, HTTPException
from models.user import User
import bcrypt
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from database import  get_db
from sqlalchemy.orm import Session

router = APIRouter()


app = FastAPI()

@router.post("/signup", response_model=UserCreate)
def signup_user(user: UserCreate,db: Session = Depends(get_db)):
    
    
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

