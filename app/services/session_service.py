
from bcrypt import checkpw
from app.schema import SessionReq, SessionRes
from app.services import user_service
from app.data_access import users_db 
from sqlalchemy.orm import Session

from security import create_access_token, verify_password




def  verify_log_in(session_req:SessionReq ,db:Session):
    # Check if email and password match
    verified_user = users_db.retrieve_user_by_email(session_req,db)

    if verified_user is not None and verify_password(session_req.password,verified_user.password):

        access_token = create_access_token(data={"sub": session_req.username})
            
        return {"access_token": access_token, "token_type": "bearer","message":"Logged in successfully"}

    return SessionRes(id=0,email="",message="Invalid Credentials")
        
    
                 
        
        
