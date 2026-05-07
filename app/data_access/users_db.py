

from sqlalchemy.orm import Session
from app.data_access import model
from app.schema import User



def retrieve_user_by_email(db :Session,email:str):
    
    return db.query(model.User).filter(model.User.email == email).first()

def get_user_by_id(db :Session,user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def add_new_db_user(db:Session,user:User):

    db_user = model.User(email=user.email,password =user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_db_user(db:Session,user:User):

    db.delete(user)
    db.commit()

    return None
     


