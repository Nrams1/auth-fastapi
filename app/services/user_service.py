

from app.schema import User, UserResponse
from app.data_access import db, users_db
from bcrypt import gensalt, hashpw
from app.data_access import model
from sqlalchemy.orm import Session
from app.security import hash_password


def create_new_user(db:Session,user:User):

    try :
    # Check if user for given email exist , if exist return error response with custom message and status code
        new_user = users_db.retrieve_user_by_email(db,user.email)


        if new_user is None:

            
            print("here")
            user.password = hash_password(user.password)
            db_user = users_db.add_new_db_user(db,user)

            return db_user

        print("there")

    except Exception:
        print("hello2")
        return None

    



        
                
