from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            flash('You have been logged in.', category='success')
            return render_template('home.html')

        else:
            flash('Invalid credentials.', category='error')
           
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/create_account')
def create_account():
    return render_template('signup.html')
