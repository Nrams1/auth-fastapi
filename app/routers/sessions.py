
from fastapi import APIRouter
from app.schema import Session, SessionResponse 
from app.services.session_service import verify_log_in



router = APIRouter()

# Log In
@router.post("/sessions")
def log_in_user(session:Session):

    verified_user = verify_log_in(session)
    if isinstance(verified_user, str):
         #check how you can return error response with custom message and status code

        return SessionResponse(id="", email="", message=verified_user)

    return verified_user