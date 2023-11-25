from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}\\sqlite3.db"
    echo: bool = True


settings = Settings()
