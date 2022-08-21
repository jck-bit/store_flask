from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from . import db
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
                login_user(user, remember=False)
                
                
                return render_template('home.html', user=current_user)
                
                
            flash('Invalid credentials.', category='error')
           
    
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/create-account' , methods=['GET', 'POST'])
def create_account():

    if request.method == "POST":
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        username = request.form.get('username')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')

        elif len(password1) < 6:
            flash('Password must be at least 6 characters', category='error')

        elif password1 != password2:
            flash('Passwords do not match')
        
        elif (email.find('@') == -1) or (email.find('.') == -1):
            flash('Please enter a valid email', category='error')

        else:
            new_user = User(email=email, password=password1, username=username)

            db.session.add(new_user)
            db.session.commit()

            flash('User created successfully', category='success')
            return redirect (url_for('views.home'))

    return render_template('signup.html')
    


