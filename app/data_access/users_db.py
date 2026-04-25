

from sqlalchemy.orm import Session
from app.schema import User


def retrive_user_by_email(db :Session, user:User):
    return db.query(User).filter(user.email == email).first()



