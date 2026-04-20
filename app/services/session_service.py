
from app.schema import Session, SessionResponse
from app.services import user_service


def  verify_log_in(session:Session):
    # Check if emmail and password match
    res = ""
    for user_info in user_service.users_list:
        if user_info["email"] == session.email and  user_info["password"] == session.password :
            
                return SessionResponse(id=user_info["id"],email=session.email,message="logged in successfully")
        
        elif user_info["email"] == session.email and  user_info["password"] != session.password : 
                 return "Invalid password"
        
    return "User Doesnt Exist"  