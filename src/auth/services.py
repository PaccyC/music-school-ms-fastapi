from sqlmodel import Session
from src.auth.models import UserCreate,User
import bcrypt

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
    
    response= {
            "status":"True",
            "message": "User created successfully",
            "user": db_user
        }
    return  response