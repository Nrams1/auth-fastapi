
from fastapi import APIRouter ,Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from app.data_access.db import get_db
from app.schema import Token, User
from app.services.session_service import verify_log_in
from sqlalchemy.orm import Session

from security import get_current_user




router = APIRouter()


 
# Log In
@router.post("/login",status_code=200,response_model=Token)
def log_in_user(form_data: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    
    token = verify_log_in(db,form_data)
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return token


#To-do , Log out 
@router.post("/logout",status_code=200)
def log_out_user(db:Session = Depends(get_db),current_user:User = Depends(get_current_user)):
    
    return {"message": "Logged out successfully."}



    
