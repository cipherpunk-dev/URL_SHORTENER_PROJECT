from pydantic import BaseSettings
from functools import lru_cache
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent.parent/".env" #Relative path to .env added
class Settings(BaseSettings):     #basic pydantic validation
    env_name:str ="Local"
    base_url:str ="http://localhost:8000"
    db_url:str ="sqlite:///./shortener.db"
    class Config:        #if .env exist take values from there
        env_file=str(ENV_PATH)
        case_sensitive=False     #freedom to name .env any case(keeping the name same though)
@lru_cache
def get_settings()-> Settings:   #just a routine to print local settings
    settings=Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
