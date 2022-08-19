from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@views.route('/products', methods=['GET'])
def products():
    return render_template('products.html')

@views.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html')

