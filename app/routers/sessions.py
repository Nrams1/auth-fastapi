
from fastapi import APIRouter ,Depends
from app.data_access.db import get_db
from app.schema import SessionReq 
from app.services.session_service import verify_log_in
from sqlalchemy.orm import Session




router = APIRouter()


 
# Log In
@router.post("/login")
def log_in_user(session_req:SessionReq ,db:Session = Depends(get_db)):
    res = verify_log_in(session_req,db)
   
    return res


#To-do , Log out 
@router.post("/logout")
def log_out_user(userId):
    return 
