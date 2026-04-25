
from fastapi import APIRouter, Depends
from app.data_access import model
from app.data_access.db import get_db
from app.schema import User 
from sqlalchemy.orm import Session




router = APIRouter()


# Create New User
@router.post("/users")
def create_user(user :User,db:Session = Depends(get_db)):
    # check if email exist 
    new_user = db.query(model.User).filter(model.User.email == user.email).first()
    #print(new_user.isInstance())
    if new_user is None:
      
        db_user = model.User(email=user.email,password=user.password)
        added_user = db.add(db_user)
        db.commit()
        
        new_user = db.query(model.User).filter(model.User.email == user.email).first()

        return new_user
    
    return new_user
        

    print("-------------------------")
    print(new_user)
    print("-------------------------")
    


""""    
# Get Profile
@router.get("/users/{user_id}")
def get_user_profile(user_id:str):
    #Assuming the user is already added
    user_profile = retrive_user_profile(user_id)


    return user_profile


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
