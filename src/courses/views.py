from fastapi import Depends,APIRouter
from sqlmodel import Session

from src.courses.services import CourseService
from src.courses.models import CourseCreate, CourseUpdate
from src.database import get_db



router= APIRouter()




@router.post("/new")
def create_course(course_data: CourseCreate,db:Session= Depends(get_db)):
    service= CourseService(db)
    return service.create_course(course_data)



@router.get("/")
def get_all_courses(db:Session= Depends(get_db)):
    service= CourseService(db)
    return service.get_all_courses()

@router.get("/{course_id}")
def get_course_by_id(course_id:int,db:Session= Depends(get_db)):
    service= CourseService(db)
    return service.get_course_by_id(course_id)

@router.put("/{course_id}/edit")

def edit_course_by_id(course_id:int,course_data: CourseUpdate,db:Session= Depends(get_db)):
    service= CourseService(db)
    return service.edit_course(course_id,course_data) 

@router.delete("/{course_id}/delete")
def delete_course(course_id,db:Session= Depends(get_db)):
    service= CourseService(db)
    service.delete_course(course_id)