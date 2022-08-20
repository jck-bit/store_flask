from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'store_manager.db'

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisissecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:/// {DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


   

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from .models import User, Products

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    return app

def create_database(app):
    if not path.exists('store_manager/' + DB_NAME):
        db.create_all(app=app)
        print('Database created')
    else:
        print('Database already exists')