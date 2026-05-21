from pydantic import BaseModel, EmailStr

class GoogleAuthRequest(BaseModel):
    token: str  # Google ID token from frontend

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    profile_completed: bool

    class Config:
        from_attributes = True