
from fastapi import APIRouter, Depends, HTTPException
from app.data_access import model , users_db
from app.data_access.db import get_db
from app.schema import User, UserResponse 
from sqlalchemy.orm import Session

from app.services.user_service import create_new_user
from security import get_current_user




router = APIRouter()


# Create New User
@router.post("/users",response_model=UserResponse,status_code=200) 
def create_user(user:User,db:Session = Depends(get_db)):

    user = create_new_user(db,user)

    if user is None :
        # Have to change the error code
        raise HTTPException(status_code=400, detail="User with this email already exist")
    
    return user
  

# Get Profile
@router.get("/users/me/profile",response_model=UserResponse ,status_code=200)
def get_user_profile(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
     
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user

@router.delete("/users/me",status_code=200)
def delete_user(db:Session = Depends(get_db),current_user:User = Depends(get_current_user)):
    
    if current_user :
        users_db.delete_db_user(db,current_user) 
        return {"message": "User deleted successfully"}
        
    raise HTTPException(status_code=404, detail="User not found")
    
    
    

