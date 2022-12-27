from dotenv import dotenv_values
from pydantic import BaseSettings


class Config(BaseSettings):
    PORT: int = 8011
    DB_HOST: str = ""
    DB_PORT: int = 5432
    DB_NAME: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""


config_dict = dotenv_values(".env")
settings = Config(**config_dict)
