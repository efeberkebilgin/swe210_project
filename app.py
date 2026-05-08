from flask import Flask
from config import Config
from models import db
from routes import routes


app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register blueprint
app.register_blueprint(routes)


# Create tables automatically
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)