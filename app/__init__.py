from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET KEY'] = 'Secret*23@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saccoplus:Today*123@127.0.0.1/saccoplus'

Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager= LoginManager(app)

login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"
    


from app import models


from app.home import home
from app.auth import auth
from app.admin import admin


app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(admin)



