from app import app
from models import db, User

ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "admin@report.com"
ADMIN_PASSWORD = "Admin12345!"


with app.app_context():
    existing_admin = User.query.filter_by(username=ADMIN_USERNAME).first()

    if not existing_admin:
        new_admin = User(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            role="admin"
        )
        new_admin.set_password(ADMIN_PASSWORD)

        db.session.add(new_admin)
        db.session.commit()

        print("SUCCESS: Admin account created.")
        print(f"Username: {ADMIN_USERNAME}")
        print(f"Password: {ADMIN_PASSWORD}")
    else:
        existing_admin.role = "admin"
        db.session.commit()
        print("INFO: Admin account already exists and role is admin.")
