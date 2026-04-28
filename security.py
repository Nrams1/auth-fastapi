from datetime import timedelta, timezone , datetime
from bcrypt import checkpw
from fastapi.security import OAuth2PasswordBearer
import jwt

# extract toke from http header
oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "mykey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

def verify_password(plain_password,Hashed_password):
    return  checkpw(plain_password.encode('utf-8'),Hashed_password.encode('utf-8'))

def create_access_token(data:dict, expires_delta:timedelta=timedelta(minutes=15)):

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
