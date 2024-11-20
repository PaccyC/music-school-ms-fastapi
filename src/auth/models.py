from sqlmodel import Field, SQLModel
from typing import Optional
from enum import Enum
from typing import ClassVar
from pydantic import BaseModel
# Define an Enum for the roles
class RoleEnum(str, Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"

class UserBase(SQLModel):
    ROLE_CHOICES: ClassVar[tuple[str, str, str]] = ("admin", "student", "teacher")

    username: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None
    role: RoleEnum  # Use the Enum here
    phoneNumber: str = None

class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(primary_key=True, nullable=False, default=None)

class UserCreate(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class DataToken(BaseModel):
    id: Optional[str] = None