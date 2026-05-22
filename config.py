import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Safe default values are provided so the project runs even if .env is missing.
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key-for-production")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///secure_notes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENCRYPTION_SECRET_KEY = os.getenv("ENCRYPTION_SECRET_KEY", "change-this-encryption-key-for-production")

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  # True should be used only when HTTPS is enabled.
    SESSION_COOKIE_SAMESITE = "Lax"
