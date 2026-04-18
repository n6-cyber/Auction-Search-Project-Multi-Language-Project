# Imports 
from flask import Flask
from flask_login import LoginManager
from config import config
from app.models import db, User
from app.auth import auth_bp
from app.routes import main_bp

# Initializes, configures and links database

def create_app(config_name='development'):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)

    