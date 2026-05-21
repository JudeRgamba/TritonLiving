from app.database import Base
from sqlalchemy import Column, String, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, primary_key=True)
    name = Column(String)
    profile_completed = Column(Boolean, default=False) # check if the user has an account
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    

