    
import uuid
from sqlalchemy import Column, String, LargeBinary
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
        __tablename__ = "users"
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        username = Column(String(100))
        email = Column(String(100))
        password = Column(LargeBinary)   