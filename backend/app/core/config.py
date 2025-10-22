from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Loads settings from the .env file.
    """
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"  # Tell pydantic to load from .env

# Create one "instance" of the settings to be used everywhere
settings = Settings()
