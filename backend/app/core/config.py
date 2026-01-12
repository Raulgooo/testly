import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

class Settings:
    PROJECT_NAME: str = "Testly MVP Backend"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables.")

settings = Settings()