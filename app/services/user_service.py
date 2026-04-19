
from pydantic import BaseModel, EmailStr
import uuid
from app.schema import User, UserResponse

user_response_list = []
users_dict = {} # This is just for testing purpose, you can replace it with database in future
users_list = [] # This is just for testing purpose, you can replace it with database in future





def create_new_user(user:User):
    # Get the user by email from database

    # Check if user for given email exist
    for i in users_list:
        if i["email"] == user.email:    
            return "User with given email already exist"

    # Create new user , Hash password and save in database 
    id = str(uuid.uuid4())
    users_dict = user.model_dump()
    users_dict["id"] = id
    users_list.append(users_dict)

    # Create new user return response
    user_new = UserResponse(id=id, email=user.email,message="User Created Successfully") 
   
    print(users_list)
    user_response_list.append(user_new)
    #Return a token to user for authentication and authorization

    

    return user_new
