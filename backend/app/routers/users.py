from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/users")

@router.post("/login")
def login_or_create_user(email: str, name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        # initialize a new user with acc information
        user = User(email=email, name=name)
        db.add(user)
        db.commit()
    return {"profile_completed": user.profile_completed}