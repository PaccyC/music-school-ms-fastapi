from fastapi import Depends, HTTPException,status
from sqlmodel import Session
from src.database import get_db
from src.auth.models import UserCreate,User,Token
import bcrypt

from fastapi.security import OAuth2PasswordRequestForm

from  src.utils import jwt_token_operations
def register_user(db:Session, user_create: UserCreate):
    password = user_create.password
    email= user_create.email
    phoneNumber= user_create.phoneNumber
    
    existing_email_profiles= db.query(User).filter(
        User.email == email
    ).all()
    
    if email and (len(existing_email_profiles) > 0):
        return {
            "status":"false",
            "message": "Email already exists. Please try again"
        }
    

    existing_phone_profiles= db.query(User).filter(
        User.phoneNumber == phoneNumber
    ).all()
    
    
    if phoneNumber and (len(existing_phone_profiles) > 0):
        return {
            "status":"false",
            "message": "Email already exists. Please try again"
        }
        
        # Hashing the password
        
    salt= bcrypt.gensalt(10)
    
    hashed_password= bcrypt.hashpw(password.encode("utf-8"),salt)
    user_create.password = hashed_password.decode("utf-8")
    
    db_user= User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Generate the JWT TOKEN
    
    token_data= {
        "id":db_user.id,
        "email":db_user.email,
        "role":db_user.role,
        "first_name":db_user.first_name,
        "last_name":db_user.last_name,
    }
    
    jwt_token = jwt_token_operations.create_access_token(token_data)
    
    
    response= {
            "status":"True",
            "message": "User created successfully",
            "user": db_user,
            "token": jwt_token
        }
    return  response


def login_user( email:str, password:str, db:Session= Depends(get_db)):
    user= db.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials")
        
    if not bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials")
    
    
    token_data= {
        "user_id":user.id,
        "email":user.email,
        "role":user.role,
        "first_name":user.first_name,
        "last_name":user.last_name,
    }
    access_token= jwt_token_operations.create_access_token(data=token_data)
    
    
    return {
        "access_token": access_token, 
        "message":"User logged in successfully",
        "status": status.HTTP_200_OK,
        "user":user
        }



def get_user_by_id(user_id:int, db : Session =Depends(get_db)):
    user= db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
   
    return user