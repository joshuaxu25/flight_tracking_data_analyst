from pydantic import BaseSettings


class Settings(BaseSettings):
    START_DATE_TIME: str
    END_DATE_TIME: str


settings = Settings()