from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Genshin Character Scraper"
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    BASE_URL: str = "https://genshin-impact.fandom.com/wiki/Characters"
    OUTPUT_FILE: str = "genshin_characters.csv"
    
    class Config:
        env_file = ".env"

settings = Settings()