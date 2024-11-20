



from fastapi import Depends, HTTPException,status
from sqlmodel import Session

from src.courses.models import Course, CourseCreate, CourseUpdate
from src.database import get_db


class CourseService:
    def __init__(self,db :Session = Depends(get_db)):
        self.db= db
        
        
    def create_course(self,course_data:CourseCreate) -> Course:
        new_course = Course(**course_data.dict())
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        
        return new_course
    
    
    
    def get_all_courses(self) -> list[Course]:
        courses= self.db.query(Course).all()
        return courses
    
    
    
    def get_course_by_id(self, course_id:int) -> Course:
        course= self.db.query(Course).filter(Course.id == course_id).first()
        
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        
        return course
    
     
    def edit_course(self, course_id:int, course_data: CourseUpdate) -> Course:
        course= self.db.query(Course).filter(Course.id == course_id).first()
        
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        
        course.name= course_data.name
        course.description= course_data.description
        course.start_date= course_data.start_date
        course.end_date= course_data.end_date
        course.schedule= course_data.schedule
        
        self.db.commit()
        self.db.refresh(course)
        
        return course
    
    
    def delete_course(self, course_id: int):
        course= self.db.query(Course).filter(Course.id == course_id).first()
        
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        
        self.db.delete(course)
        self.db.commit()