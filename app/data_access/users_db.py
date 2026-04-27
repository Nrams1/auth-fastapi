

from sqlalchemy.orm import Session
from app.data_access import model
from app.schema import User


def retrieve_user_by_email(user:User,db :Session):
    
    return db.query(model.User).filter(model.User.email == user.email).first()

def get_user_by_id(user_id: int,db :Session):
    return db.query(model.User).filter(model.User.id == user_id).first()


