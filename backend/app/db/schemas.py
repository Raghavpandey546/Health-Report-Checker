from pydantic import BaseModel, EmailStr
from typing import Optional

# --- User Schemas ---

# Schema for what the user MUST provide during registration
class UserCreate(BaseModel):
    email: EmailStr  # Pydantic will validate this is a real email format
    password: str

# Schema for what we return to the user (the "public" user data)
# Notice: NO password!
class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True  # Tell pydantic to read data from our model
