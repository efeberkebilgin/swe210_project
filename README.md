# 🔐 Secure Notes Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge\&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge\&logo=sqlite)
![Security](https://img.shields.io/badge/Security-RBAC_&_Encryption-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Professional-success?style=for-the-badge)

<h3>🛡️ Professional Secure Web Application for SWE210 Software Security Course</h3>

<p>
Modern Flask-based secure note management platform with authentication,
RBAC authorization and encrypted data storage.
</p>

</div>

---

Professional Flask-based secure web application developed for the SWE210 Software Security course project.

## ✨ Project Highlights

This project demonstrates:

* Secure Authentication
* Password Hashing
* Role-Based Access Control (RBAC)
* Secure Session Management
* Symmetric Encryption
* Secure Database Design
* Protected Admin Panel
* Secure Note Storage

---

# Project Overview

The Secure Notes Management System is a secure web application where users can:

* Register accounts
* Login securely
* Create encrypted notes
* Manage private data
* Access role-based dashboards

The system was designed with software security principles in mind and implements multiple security mechanisms to protect sensitive information.

---

# 🚀 Security Features

## 🔑 Authentication System

The application includes a secure authentication mechanism using:

* Password hashing
* Session management
* User validation
* Protected routes

Passwords are never stored as plaintext.

---

## 🔐 Password Hashing

Passwords are hashed using:

```python
generate_password_hash()
```

Verification is performed using:

```python
check_password_hash()
```

Benefits:

* Prevents plaintext password leaks
* Increases account security
* Protects against database compromise

---

## 👥 Role-Based Access Control (RBAC)

Two roles are implemented:

| Role  | Permissions                               |
| ----- | ----------------------------------------- |
| User  | Create and manage own secure notes        |
| Admin | Access admin dashboard and monitor system |

Unauthorized users cannot access admin-only routes.

---

## 🧬 Encryption System

Sensitive note data is encrypted before storage.

Encryption is implemented using:

* Fernet Symmetric Encryption
* SHA256 key generation
* Base64 secure encoding

Main security workflow:

1. User submits note
2. Note is encrypted
3. Encrypted data is stored in database
4. Data is decrypted only when needed

---

# ⚙️ Technologies Used

| Technology       | Purpose          |
| ---------------- | ---------------- |
| Flask            | Web framework    |
| Flask-SQLAlchemy | Database ORM     |
| SQLite           | Database         |
| Werkzeug         | Password hashing |
| Cryptography     | Data encryption  |
| HTML/CSS         | Frontend UI      |

---

# 📁 Project Structure

```text
project/
│
├── app.py
├── config.py
├── models.py
├── routes.py
├── encryption.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── admin.html
│
└── static/
    └── css/
        └── style.css
```

---

# 📚 File Descriptions

## 🖥️ app.py

Main Flask application file.

Responsibilities:

* Flask app initialization
* Blueprint registration
* Database initialization
* Application startup

---

## ⚙️ config.py

Stores application configuration.

Contains:

* Flask secret key
* Database configuration
* Encryption secret key

---

## 🗄️ models.py

Contains SQLAlchemy database models.

Models:

### User Model

Stores:

* Username
* Email
* Password hash
* User role

### SecureNote Model

Stores:

* Encrypted note content
* Creation timestamp
* User relationship

---

## 🔒 encryption.py

Handles encryption and decryption operations.

Features:

* Secure Fernet encryption
* SHA256-based key generation
* Safe encrypted storage

---

## 🌐 routes.py

Contains all Flask routes.

Main routes:

| Route        | Description        |
| ------------ | ------------------ |
| /            | Home page          |
| /register    | User registration  |
| /login       | User login         |
| /logout      | Logout             |
| /dashboard   | User dashboard     |
| /create-note | Create secure note |
| /delete-note | Delete note        |
| /admin       | Admin panel        |

---

# Database Design

## Users Table

| Field         | Description           |
| ------------- | --------------------- |
| id            | User ID               |
| username      | Username              |
| email         | User email            |
| password_hash | Hashed password       |
| role          | User role             |
| created_at    | Account creation date |

---

## Secure Notes Table

| Field             | Description         |
| ----------------- | ------------------- |
| id                | Note ID             |
| encrypted_content | Encrypted note text |
| created_at        | Creation timestamp  |
| user_id           | Note owner          |

---

# 💻 Installation Guide

## 1. Clone or Download Project

Place project files inside a folder.

---

## 2. Open Project in VS Code

```text
File → Open Folder
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start Flask server:

```bash
python app.py
```

If successful:

```text
Running on http://127.0.0.1:5000
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Creating Admin User

Run Python shell:

```bash
python
```

Then execute:

```python
from app import app
from models import db, User

with app.app_context():
    user = User.query.filter_by(username="your_username").first()
    user.role = "admin"
    db.session.commit()
```

---

# 🔒 Security Workflow

## User Registration

1. User submits credentials
2. Password is hashed
3. User stored in database

---

## User Login

1. Credentials submitted
2. Password hash verified
3. Session created
4. User redirected to dashboard

---

## Secure Note Creation

1. User submits note
2. Note encrypted using Fernet
3. Encrypted data stored
4. Only owner can access note

---

## Admin Authorization

1. Session checked
2. Role verified
3. Access granted only to admins

---

# 🛡️ Security Advantages

This system protects against:

* Plaintext password exposure
* Unauthorized admin access
* Sensitive data leakage
* Direct note access by other users
* Session misuse

---

# Example Security Mechanisms

## Password Hashing Example

```python
new_user.set_password(password)
```

---

## Encryption Example

```python
encrypted_content = crypto.encrypt_data(content)
```

---

## Access Control Example

```python
@admin_required
```

---

# 📈 Future Improvements

Potential upgrades:

* Flask-WTF CSRF protection
* JWT authentication
* Email verification
* Password complexity validation
* Docker deployment
* HTTPS support
* Logging system
* API support
* Unit testing

---

# Screenshots Recommendation

Recommended screenshots for report:

1. Home page
2. Register page
3. Login page
4. Dashboard
5. Secure note creation
6. Database encrypted data
7. Admin panel
8. Unauthorized access protection

---

# ✅ Conclusion

The Secure Notes Management System demonstrates modern software security practices using Flask and Python.

The project successfully implements:

* Secure authentication
* Password hashing
* Role-based authorization
* Data encryption
* Secure session management

This project provides a strong foundation for understanding secure web application development principles.

---

# 👨‍💻 Author

<div align="center">

### SWE210 Software Security Course Project

Developed using:

🐍 Python • 🌐 Flask • 🗄️ SQLAlchemy • 🔐 Cryptography

</div>

SWE210 Software Security Course Project

Developed using Flask, SQLAlchemy and Cryptography.
