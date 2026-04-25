
from app.schema import Session, SessionResponse
from app.services import user_service


def  verify_log_in(session:Session):
    # Check if emmail and password match
    for user_info in user_service.users_list:
        if user_info["email"] == session.email and user_info["password"] == session.password :
                
                return SessionResponse(id=user_info["id"],email=session.email,message="Logged in successfully")
    
    return SessionResponse(id=user_info["id"],email=session.email,message="Invalid Credentials")
        
    
                 
        
        
