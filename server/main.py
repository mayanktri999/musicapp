

from models.base import Base
from database import engine
from fastapi import FastAPI, Request
from routes import auth


app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["auth"])


Base.metadata.create_all(engine)
    
 