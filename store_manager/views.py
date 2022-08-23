from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from .import db
from .models import Sales, User, Products
from flask_login import   login_required, current_user
import json

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/products', methods=['GET'])
@login_required
def products():
    products = Products.query.all()

    return render_template('products.html', products=products, user=current_user)

@views.route('/delete-product', methods=['POST'])
def delete_product():
    product = json.loads(request.data)
    product = Products.query.get(product['id'])
    db.session.delete(product)
    db.session.commit()
    
    return flash('Product deleted successfully')

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



@views.route('/sales', methods=['GET'])
def get_all_sales():
    sales = Sales.query.all()
    sales_list = []
    for sale in sales:

        sales_object= {
           'id':sale.id,
           'total': sale.total,
           'data' : sale.data,
           'date' : sale.date,
           'user_id':sale.user_id
        } 
    sales_list.append(sales_object)

    return jsonify(sales_list)

@views.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']

    product = Products(name=name, price=price, description=description)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully.'})
    
@views.route('/edit-product', methods=['POST'])
def edit_product():
    data = request.get_json()
    product_id = data['product_id']
    name = data['name']
    price = data['price']
    description = data['description']

    product = Products.query.get(product_id)
    product.name = name
    product.price = price
    product.description = description
    db.session.commit()

    return jsonify({'message': 'Product updated successfully.'})

@views.route('/sales', methods=['POST'])
def create_sale():
   sale = request.get_json()

   new_sale = Sales(data=sale['data'], total=sale['total'])

   db.session.add(new_sale)
   db.session.commit()

   return jsonify({'message': 'Sale created successfully.'})
