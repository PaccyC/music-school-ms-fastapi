import logging
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from src.database import engine
from src.urls import api_router
from src.config import settings
app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app.include_router(api_router,prefix="/api/v1")

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
    )

@app.on_event("startup")
def on_startup():
    print(settings.SQLALCHEMY_DATABASE_URL)
    SQLModel.metadata.create_all(bind=engine)