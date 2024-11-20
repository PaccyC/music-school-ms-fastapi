from sqlmodel import Session
from src.database import get_db
from src.auth.models import UserCreate
from src.auth.services import register_user
from fastapi import APIRouter, Depends


router = APIRouter()


@router.post("/register")
def create_user(user_create:UserCreate,db:Session = Depends(get_db)):
    return register_user(db, user_create)