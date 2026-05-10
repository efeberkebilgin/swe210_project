import re

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from functools import wraps

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from models import db, User, SecureNote
from encryption import EncryptionManager
from config import Config


# ====================================
# BLUEPRINT
# ====================================
routes = Blueprint('routes', __name__)

# ====================================
# RATE LIMITER
# ====================================
limiter = Limiter(
    key_func=get_remote_address
)

# ====================================
# ENCRYPTION OBJECT
# ====================================
crypto = EncryptionManager(
    Config.ENCRYPTION_SECRET_KEY
)


# ====================================
# LOGIN REQUIRED DECORATOR
# ====================================
def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'user_id' not in session:

            flash('Please login first.', 'danger')

            return redirect(url_for('routes.login'))

        return f(*args, **kwargs)

    return decorated_function


# ====================================
# ADMIN REQUIRED DECORATOR
# ====================================
def admin_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'user_id' not in session:

            flash('Please login first.', 'danger')

            return redirect(url_for('routes.login'))

        user = User.query.get(session['user_id'])

        if not user or not user.is_admin():

            flash('Unauthorized access!', 'danger')

            return redirect(url_for('routes.dashboard'))

        return f(*args, **kwargs)

    return decorated_function


# ====================================
# PASSWORD POLICY
# ====================================
def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*]", password):
        return False

    return True


# ====================================
# HOME PAGE
# ====================================
@routes.route('/')
def home():

    return render_template('home.html')


# ====================================
# REGISTER
# ====================================
@routes.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # VALIDATION
        if not username or not email or not password:

            flash('All fields are required.', 'danger')

            return redirect(url_for('routes.register'))

        # PASSWORD POLICY CHECK
        if not validate_password(password):

            flash(
                'Password must contain uppercase, lowercase, number and special character.',
                'danger'
            )

            return redirect(url_for('routes.register'))

        # EXISTING USER CHECK
        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:

            flash('User already exists.', 'warning')

            return redirect(url_for('routes.register'))

        # CREATE USER
        new_user = User(
            username=username,
            email=email,
            role='user'
        )

        # HASH PASSWORD
        new_user.set_password(password)

        db.session.add(new_user)

        db.session.commit()

        flash('Registration successful!', 'success')

        return redirect(url_for('routes.login'))

    return render_template('register.html')


# ====================================
# LOGIN
# ====================================
@routes.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(
            username=username
        ).first()

        # PASSWORD VERIFICATION
        if user and user.check_password(password):

            # SESSION MANAGEMENT
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role

            flash('Login successful!', 'success')

            return redirect(url_for('routes.dashboard'))

        # FAILED LOGIN LOG
        print(f"[FAILED LOGIN] Username: {username}")

        flash('Invalid username or password.', 'danger')

    return render_template('login.html')


# ====================================
# LOGOUT
# ====================================
@routes.route('/logout')
@login_required
def logout():

    session.clear()

    flash('Logged out successfully.', 'success')

    return redirect(url_for('routes.login'))


# ====================================
# DASHBOARD
# ====================================
@routes.route('/dashboard')
@login_required
def dashboard():

    user = User.query.get(session['user_id'])

    notes = SecureNote.query.filter_by(
        user_id=user.id
    ).all()

    decrypted_notes = []

    for note in notes:

        decrypted_notes.append({
            'id': note.id,
            'content': crypto.decrypt_data(
                note.encrypted_content
            ),
            'created_at': note.created_at
        })

    return render_template(
        'dashboard.html',
        user=user,
        notes=decrypted_notes
    )


# ====================================
# CREATE SECURE NOTE
# ====================================
@routes.route('/create-note', methods=['POST'])
@login_required
def create_note():

    content = request.form.get('content')

    if not content:

        flash('Content cannot be empty.', 'warning')

        return redirect(url_for('routes.dashboard'))

    # ENCRYPT NOTE
    encrypted_content = crypto.encrypt_data(content)

    note = SecureNote(
        encrypted_content=encrypted_content,
        user_id=session['user_id']
    )

    db.session.add(note)

    db.session.commit()

    flash('Secure note added successfully.', 'success')

    return redirect(url_for('routes.dashboard'))


# ====================================
# DELETE NOTE
# ====================================
@routes.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):

    note = SecureNote.query.get_or_404(note_id)

    # ACCESS CONTROL
    if note.user_id != session['user_id']:

        flash('Unauthorized action.', 'danger')

        return redirect(url_for('routes.dashboard'))

    db.session.delete(note)

    db.session.commit()

    flash('Note deleted.', 'success')

    return redirect(url_for('routes.dashboard'))


# ====================================
# ADMIN PANEL
# ====================================
@routes.route('/admin')
@admin_required
def admin_panel():

    users = User.query.all()

    notes = SecureNote.query.all()

    return render_template(
        'admin.html',
        users=users,
        notes=notes
    )