from pydantic import BaseSttings, AnyUrl
from functools import lru_cache

class Settings(BaseSttings):
    APP_NAME: str = "Sistema Biblioteca"
    DEBUG: bool = True
    DATABASE_URL: AnyUrl = "sqlite:///./biblioteca.db"
    SECRET_KEY: str = "troca_para_uma_chave_secreta"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()