
from bcrypt import checkpw
from app.schema import SessionReq, SessionRes
from app.services import user_service
from app.data_access import users_db 
from sqlalchemy.orm import Session



def  verify_log_in(session_req:SessionReq ,db:Session):
    # Check if email and password match
    verified_user = users_db.retrieve_user_by_email(session_req,db)

    if verified_user is not None and verified_user.email == session_req.email and checkpw(session_req.password.encode('utf-8'),verified_user.password.encode('utf-8')) :
            
            return SessionRes(id=verified_user.id,email=verified_user.email,message="Logged in successfully")

    return SessionRes(id=0,email="",message="Invalid Credentials")
        
    
                 
        
        
