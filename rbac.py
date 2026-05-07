# -----------------------------
# ADMIN ROLE CHECK
# -----------------------------
def is_admin(user):

    # Kullanıcı yoksa
    if user is None:
        return False

    return user["role"] == "admin"


# -----------------------------
# USER ROLE CHECK
# -----------------------------
def is_user(user):

    # Kullanıcı yoksa
    if user is None:
        return False

    return user["role"] == "user"


# -----------------------------
# LOGIN CHECK
# -----------------------------
def is_logged_in(session):

    return "user_id" in session


# -----------------------------
# ADMIN ACCESS CONTROL
# -----------------------------
def can_access_admin(session):

    # Kullanıcı giriş yapmamışsa
    if "role" not in session:
        return False

    # Admin değilse
    if session["role"] != "admin":
        return False

    return True