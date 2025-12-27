from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from blog_app.models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))