from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email : EmailStr
    password : str 

class UserResponse(BaseModel):
    id:str
    email:str
    message : str = "" # This is just for testing purpose, you can replace it with error response in future

    
class Token(BaseModel):
    email : EmailStr
    password : str 

class TokenResponse(BaseModel):
    id:str
    email:str
    message : str = "" # This is just for testing purpose, you can replace it with error response in future

