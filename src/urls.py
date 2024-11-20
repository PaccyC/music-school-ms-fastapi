from fastapi.routing import APIRouter
from src.auth.views import router as auth_router
from src.courses.views import router as courses_router

api_router = APIRouter()


api_router.include_router(auth_router,prefix="/auth", tags=["UserAuth"])

api_router.include_router(courses_router,prefix="/courses", tags=["Course"])