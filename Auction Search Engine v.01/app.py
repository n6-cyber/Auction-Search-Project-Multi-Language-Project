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

    # don't touch this right now.
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
    