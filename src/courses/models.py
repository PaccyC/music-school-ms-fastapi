from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import ForeignKey
from datetime import datetime

class CourseBase(SQLModel):
    name: str
    description: str
    teacher_id: Optional[int] = Field(
        default=None,
        foreign_key="users.id", nullable=False
    )
    start_date: datetime
    end_date: datetime
    schedule: str


class Course(CourseBase, table=True):
    __tablename__ = "courses"
    id: Optional[int] = Field(primary_key=True, nullable=False, default=None)
