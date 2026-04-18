from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash("This user already exists")
        return redirect(url_for('auth.register'))
    else:
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Sucessful! Redirecting")
        return redirect(url_for('auth.login'))
    
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('main.index'))
    else:
        flash("Invalid username or password, please try again.")
        return redirect(url_for('auth.login'))