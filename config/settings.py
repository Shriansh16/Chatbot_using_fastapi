import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()
#handles the environment variables
class Settings(BaseSettings):
    GROQ_API_KEY: str = os.getenv('GROQ_API_KEY')

settings = Settings()