import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    db_url: str = Field(..., alias="MONGO_URL")
    db_name:str =Field(..., alias="DB_NAME")
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings:Settings = Settings()
