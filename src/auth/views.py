from src.auth.services import register_user
from fastapi import APIRouter


router = APIRouter()


@router.post("/register")
def register_user():
    pass