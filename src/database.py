from typing import Generator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, Session
from src.config import get_settings


db_settings= get_settings()

SQLALCHEMY_DATABASE_URL= db_settings.SQLALCHEMY_DATABASE_URL
print(f"Connection to database: {SQLALCHEMY_DATABASE_URL}")

engine= create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db() -> Generator:
    with Session(engine) as db:
        yield db
        