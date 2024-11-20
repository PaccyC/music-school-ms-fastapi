from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import date

class CourseBase(SQLModel):
    name: str
    description: str
    teacher_id: Optional[int] = Field(
        default=None,
        foreign_key="users.id", nullable=False
    )
    start_date: date
    end_date: date
    schedule: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass
class Course(CourseBase, table=True):
    __tablename__ = "courses"
    id: Optional[int] = Field(primary_key=True, nullable=False, default=None)


class EnrollmentBase(SQLModel):
    student_id: Optional[int] = Field(
        default=None,
        foreign_key="users.id", nullable=False
    )
    course_id: Optional[int] = Field(
        default=None,
        foreign_key="courses.id", nullable=False
    )
    enrollment_date: date 
     

class Enrollmet(EnrollmentBase,table=True):
    __tablename__= "enrollment"
    id: Optional[int] = Field(primary_key=True, nullable=False, default=None)