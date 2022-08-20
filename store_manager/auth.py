from flask import Blueprint, render_template, request, flash
from .import db
from .models import User



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
                return render_template('home.html')
        
            flash('Invalid credentials.', category='error')
           
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/create_account')
def create_account():
    return render_template('signup.html')
