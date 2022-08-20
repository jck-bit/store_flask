from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from flask_login import login_user, logout_user, login_required, current_user



auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            if password == user.password:
                flash('You are now logged in.')
                login_user(user)
                return render_template('home.html')
        
            flash('Invalid credentials.', category='error')
           
    
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/create_account')
def create_account():
    return render_template('signup.html')
