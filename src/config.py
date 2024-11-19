
from functools import lru_cache
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv



load_dotenv()

@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    DB_HOST:str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER : str = os.getenv("DB_USER")
    DB_PASSWORD :str = os.getenv("DB_PASSWORD")
    DB_NAME :str = os.getenv("DB_NAME")



    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings= Settings()