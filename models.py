from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Database object
db = SQLAlchemy()


# ====================================
# USER MODEL
# ====================================
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        default='user'
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship
    notes = db.relationship(
        'SecureNote',
        backref='owner',
        lazy=True,
        cascade='all, delete-orphan'
    )

    # =========================
    # PASSWORD HASHING
    # =========================
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'<User {self.username}>'


# ====================================
# SECURE NOTE MODEL
# ====================================
class SecureNote(db.Model):
    __tablename__ = 'secure_notes'

    id = db.Column(db.Integer, primary_key=True)

    encrypted_content = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    def __repr__(self):
        return f'<SecureNote {self.id}>'