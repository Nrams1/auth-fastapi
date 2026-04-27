
from fastapi import APIRouter, Depends
from app.data_access import model
from app.data_access.db import get_db
from app.schema import User, UserResponse 
from sqlalchemy.orm import Session

from app.services.user_service import create_new_user, retrieve_user_profile




router = APIRouter()


# Create New User
@router.post("/users",) 
def create_user(user :User,db:Session = Depends(get_db)):
    res = create_new_user(user,db)

    
    return res
  

# Get Profile
@router.get("/users/{user_id}")
def get_user_profile(user_id:int,db:Session = Depends(get_db)):

    user_profile = retrieve_user_profile(user_id,db)

    return user_profile

"""

@router.put("/users/{use_id}")
def update_user_details(id):    
    user_dict[id]= {
  "Name": "item4 " ,
  "email":"x.com4" ,
  "password": "xxxoend4"

}
    return user_dict


@router.delete("/users/{user_id}")
def delete_user(id):
    user_dict.pop(id)
    return user_dict
"""
