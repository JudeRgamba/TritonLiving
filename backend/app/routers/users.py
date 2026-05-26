from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import GoogleAuthRequest, UserResponse
from app.auth import verify_google_token, create_jwt
from app.dependencies import get_current_user

router = APIRouter(prefix="/users")

@router.post("/login")
def login_or_create_user(body: GoogleAuthRequest, db: Session = Depends(get_db)):
    try:
        # Verify the Google token and extract user info
        idinfo = verify_google_token(body.token)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

    email = idinfo["email"]
    name = idinfo.get("name", "")

    # Query for existing user or create a new one
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create a JWT for the user that is used for authentication in subsequent requests
    token = create_jwt(user.id)

    return {
        "access_token": token, 
        "profile_completed": user.profile_completed,
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
        },
    }

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user