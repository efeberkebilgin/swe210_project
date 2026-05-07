import bcrypt
from models import create_user, get_user


# -----------------------------
# REGISTER FUNCTION
# -----------------------------
def register(username, password, role="user"):

    # Şifreyi byte formatına çevir
    password_bytes = password.encode('utf-8')

    # Şifreyi hashle
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    # Database'e kullanıcı ekle
    create_user(
        username,
        hashed_password.decode('utf-8'),
        role
    )

    return True


# -----------------------------
# LOGIN FUNCTION
# -----------------------------
def login(username, password):

    # Kullanıcıyı database'den çek
    user = get_user(username)

    # Kullanıcı bulunamadıysa
    if user is None:
        return None

    # Girilen şifreyi byte'a çevir
    password_bytes = password.encode('utf-8')

    # Database'deki hash'i byte'a çevir
    stored_hash = user["password"].encode('utf-8')

    # Şifre doğrulama
    if bcrypt.checkpw(password_bytes, stored_hash):
        return user

    return None