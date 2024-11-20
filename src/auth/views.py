from sqlmodel import Session
from src.database import get_db
from src.auth.models import UserCreate
from src.auth.services import register_user,login_user
from fastapi import APIRouter, Depends,Body


router = APIRouter()


@router.post("/register")
def create_user(user_create:UserCreate,db:Session = Depends(get_db)):
    return register_user(db, user_create)


@router.post("/login")
def login(email:str = Body(...),password:str = Body(...),db:Session = Depends(get_db)):
    return login_user(email,password,db)