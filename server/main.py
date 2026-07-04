
from tokenize import String
from unittest.mock import Base
import uuid

from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column, Integer, String, LargeBinary

app = FastAPI()
DATABASE_URL = "postgresql://postgres:mayank2006@localhost:5432/musicapp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
Base = declarative_base()

class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, )
        username = Column(String(100))
        email = Column(String(100))
        password = Column(LargeBinary)       
    

@app.post("/signup")
def signup_user(user: UserCreate):
    
    
    #check if the user already exists in the database
    user_db = db.query(User).filter((User.email == user.email)).first()

    if  user_db:
         return {"message": "user with this email already exists"}
    #add the user to the database
    user_db =User(id=str(uuid.uuid4()), username=user.username, email=user.email, password=user.password)
    db.add(user_db)
    db.commit()

    return user_db

Base.metadata.create_all(engine)