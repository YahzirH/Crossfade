from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    lastfm_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()