from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta,datetime

from jose import JWTError,jwt
from sqlmodel import Session
from src.database import get_db
from src.auth.models import DataToken,User



oath2_scheme= OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY="616de5b2fe37ac5cbcbfdb27d18cdddf39cc686e829b8c417dad98b8e69b5850"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_DAYS=1

def create_access_token(data: dict):
    to_encode= data.copy()
    expire= datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({"expire":expire.strftime("%Y-%m-%d %H:%M:%S")})
    
    encode_jwt= jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    
    return encode_jwt


def verify_token_access(token: str, credentials_exception):
    try:
        payload= jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        
        token_data= DataToken(id=id)
        
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    return token_data



def get_current_user(token: str = Depends(oath2_scheme),db: Session = Depends(get_db)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate":"Bearer"})
    token= verify_token_access(token, credentials_exception)
    
    user= db.query(User).filter(User.id == token.id).first()
    
    return user