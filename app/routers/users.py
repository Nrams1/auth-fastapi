
from fastapi import APIRouter
from app.schema import User, UserResponse
from app.services.user_service import create_new_user, retrive_user_profile



router = APIRouter()


# Create New User
@router.post("/users", response_model= UserResponse)
def create_user(user :User):
    user_res = create_new_user(user)

    if isinstance(user_res, str):
         #check how you can return error response with custom message and status code

        return UserResponse(id="", email="", message="User Exist")

    return user_res


    
# Get Profile
@router.get("/users/{user_id}")
def get_user_profile(user_id:str):
    #Assuming the user is already added
    user_profile = retrive_user_profile(user_id)


    return user_profile

""""
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
