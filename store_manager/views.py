from curses.ascii import US
from flask import Blueprint, render_template, request, jsonify
from .import db
from .models import User, Products
from flask_login import   login_required, current_user



views = Blueprint('views', __name__)

@views.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/products', methods=['GET'])
@login_required
def products():
    return render_template('products.html', user=current_user)

@views.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html')


@views.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']


    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'})

@views.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    users_list = []
    for user in users:
        user_object = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password': user.password
        }
        users_list.append(user_object)
    return jsonify(users_list)