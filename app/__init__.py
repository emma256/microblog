from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET KEY'] = 'Secret*23@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saccoplus:Today*123@127.0.0.1/saccoplus'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

from app import models

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)
    





