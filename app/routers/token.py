
from fastapi import APIRouter
from app.schema import Token, TokenResponse 
from app.services.session_service import verify_log_in



router = APIRouter()
 
# Log In
@router.post("/login")
def log_in_user(token:Token):

    verified_user = verify_log_in(token)
    if isinstance(verified_user, str):
         #check how you can return error response with custom message and status code
        return TokenResponse(id="", email="", message=verified_user)

    return verified_user


#To-do , Log out 
@router.post("/logout")
def log_out_user(userId):
    return 
