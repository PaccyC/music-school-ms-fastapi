from sqlmodel import Session
from src.database import get_db
from src.auth.models import User, UserCreate
from src.auth.services import register_user,login_user,get_user_by_id
from fastapi import APIRouter, Depends,Body
from src.utils.jwt_token_operations import get_current_user


router = APIRouter()


@router.post("/register")
def create_user(user_create:UserCreate,db:Session = Depends(get_db)):
    return register_user(db, user_create)


@router.post("/login")
def login(email:str = Body(...),password:str = Body(...),db:Session = Depends(get_db)):
    return login_user(email,password,db)

@router.get("/profile")
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
        "role": current_user.role,
        "username": current_user.username,
    }


@router.get("/{user_id}")
def get_user_profile(user_id:int,db: Session = Depends(get_db)):
    return get_user_by_id(user_id,db)
