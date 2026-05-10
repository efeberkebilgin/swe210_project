import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = 'sqlite:///secure_notes.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENCRYPTION_SECRET_KEY = os.getenv(
        "ENCRYPTION_SECRET_KEY"
    )

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SECURE = False

    SESSION_COOKIE_SAMESITE = 'Lax'