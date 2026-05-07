

from fastapi import HTTPException

from app.data_access import users_db 
from sqlalchemy.orm import Session

from app.schema import Token
from security import create_access_token, verify_password



def  verify_log_in( db:Session,form_data ):
    # Check if email and password match
   
    verified_user = users_db.retrieve_user_by_email(db,form_data.username)

    if verified_user is not None and verify_password(form_data.password,verified_user.password):

        access_token = create_access_token(data={"sub": str(verified_user.id)})
            
        return {"access_token":access_token,"token_type":"Bearer","user":verified_user}
    
   



        
    
                 
        
        
