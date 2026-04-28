import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    email : EmailStr
    password : str 


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime 

    # This allows Pydantic to read data from ORM objects
    model_config = ConfigDict(arbitrary_types_allowed=True)

    
class SessionReq(BaseModel):
    email : EmailStr
    password : str 

class SessionRes(BaseModel):
    id:int 
    email:str 
    message : str = "" # This is just for testing purpose, you can replace it with error response in future

class Token(BaseModel):
    access_token: str
    token_type: str