

from app.schema import User, UserResponse
from app.data_access import db, users_db
from bcrypt import gensalt, hashpw
from app.data_access import model
from sqlalchemy.orm import Session



def create_new_user(user:User,db:Session):

    # Check if user for given email exist , if exist return error response with custom message and status code
    new_user = users_db.retrieve_user_by_email(user,db)

    if new_user is None:

    # Create new user , Hash password and save in database 
        hash_password = hashpw(user.password.encode('utf-8'),gensalt())
        # Check if hashpassword did not fail , and handle the error
        db_user = model.User(email=user.email,password = hash_password.decode('utf-8'))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    
    return "User already Exist"
    

def retrieve_user_profile(id:User,db:Session):
     
    db_user = users_db.get_user_by_id(id,db)

    if db_user is None:
         
         return "User Id not available"


    return  db_user
          
                
