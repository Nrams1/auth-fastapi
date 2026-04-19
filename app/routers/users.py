
from pydantic import BaseModel
from fastapi import APIRouter
from app.schema import Session, SessionResponse, User, UserResponse
from app.services.user_service import create_new_user, verify_log_in



router = APIRouter()


# Create New User
@router.post("/users", response_model= UserResponse)
def create_user(user :User):
    user_res = create_new_user(user)

    if isinstance(user_res, str):
         #check how you can return error response with custom message and status code

        return UserResponse(id="", email="", message="User Exist")

    return user_res

# Log In
@router.post("/sessions")
def log_in_user(session:Session):

    verified_user = verify_log_in(session)
    if isinstance(verified_user, str):
         #check how you can return error response with custom message and status code

        return SessionResponse(id="", email="", message=verified_user)

    return verified_user

    




"""
@router.get("/users/{user_id}")
def get_user_profile(user_id):
    #Assuming the user is already added
    print(user_dict)
    return user_dict[user_id]

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
