from app import app
from models import db, User

with app.app_context():
    
    existing_admin = User.query.filter_by(username='admin').first()
    
    if not existing_admin:
        new_admin = User(
            username='admin',
            email='admin@report.com',
            role='admin'  
        )
        
        new_admin.set_password('Admin12345')
        
        db.session.add(new_admin)
        db.session.commit()
        
        print("✅ SUCCESS: Admin account created!")
        print("Username      : admin")
        print("Password      : Admin12345")
    else:
        print("ℹ️ INFO: Admin account already exists in the database.")