from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return render_template('index.html')

@main_bp.route('/search')
@login_required
def search():
    return render_template('search.html')

@main_bp.route('/watchlist')
@login_required
def watchlist():
    return render_template('watchlist.html', user=current_user)