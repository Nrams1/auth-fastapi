from datetime import timedelta, timezone , datetime
from typing import Annotated
from bcrypt import checkpw, gensalt, hashpw
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session

from app.data_access import users_db
from app.data_access.db import get_db

# extract toke from http header
oath2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = "mykey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1



def hash_password(password):
    return  hashpw(password.encode('utf-8'),gensalt()).decode('utf-8')

def verify_password(plain_password,Hashed_password):
    return  checkpw(plain_password.encode('utf-8'),Hashed_password.encode('utf-8'))


def create_access_token(data:dict, expires_delta:timedelta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oath2_scheme), db: Session = Depends(get_db)): 

    credentials_exception = HTTPException( status_code=401, detail="authentication failed", headers={"WWW-Authenticate": "Bearer"}, )

    try: 
        
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        user_id:str = payload.get("sub")
       
        if user_id is None: 
            raise credentials_exception
        
        user_db = users_db.get_user_by_id(db,user_id)
        
        #check if user_db exists
        if user_db is None :
            raise  credentials_exception 
        return user_db
    
    except jwt.PyJWTError as e:
        print("JWT ERROR:", e)
        raise credentials_exception
    


    
