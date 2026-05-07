import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    email : EmailStr
    password : str 


class UserResponse(BaseModel):
    id: int
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
    user : UserResponse
    