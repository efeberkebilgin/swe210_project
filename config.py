class Config:

    # Flask Secret Key
    SECRET_KEY = 'SUPER_SECRET_FLASK_KEY_2026'

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///secure_notes.db'

    # Disable modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Encryption Key
    ENCRYPTION_SECRET_KEY = 'SUPER_SECURE_ENCRYPTION_KEY_2026'